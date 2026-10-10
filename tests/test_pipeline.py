import gzip
import json

import pytest

from fakes import FakeArcticShift, FakeClock, FakeRedditRSS, comment, post
from pumpdump.pipeline import Settings, collection_done, health, run_collect
from pumpdump.sources.arctic_shift import ArcticShift
from pumpdump.sources.reddit_rss import FeedResult, RedditRSS
from pumpdump.store import Datastore

T = 1_791_150_720  # 2026-10-04 21:52:00 UTC
DAY = 86_400
SYMBOLS = {
    "AAAA": {"symbol": "AAAA", "name": "Steady Corp", "exchange": "Nasdaq", "is_etf": 0, "cik": None, "source": "nasdaqtrader"},
    "ZZZZ": {"symbol": "ZZZZ", "name": "Spike Inc", "exchange": "OTC", "is_etf": 0, "cik": 1, "source": "sec"},
}
SETTINGS = Settings(subreddits=("pennystocks", "wallstreetbets"), max_seconds=10_000)


def world():
    posts, comments = [], []
    for d in range(9):  # AAAA: 3 mentions every day, never spikes
        for j in range(3):
            comments.append(comment(f"a{d}x{j}", T - d * DAY - 3600 - j * 60, author=f"u{j}", body="AAAA is fine"))
    for j in range(12):  # ZZZZ: 12 hype comments from 6 authors in the last 24h, nothing before
        comments.append(comment(f"z{j}", T - 2 * 3600 - j * 60, author=f"z{j % 6}", body="$ZZZZ to the moon 🚀"))
    posts.append(post("p1", T - 5 * 3600, title="$ZZZZ DD", selftext="low float"))
    posts.append(post("p2", T - 3 * DAY, sub="wallstreetbets", title="SPY puts"))
    return posts, comments


def run(ds, server, clock, run_id, **kw):
    # min_interval > 0 makes every request cost fake time, so run budgets can run out
    client = ArcticShift(get=server.get, sleep=clock.sleep, clock=clock.time, min_interval=kw.pop("min_interval", 0))
    rss = kw.pop("rss", None)
    return run_collect(
        ds,
        client,
        run_id=run_id,
        settings=kw.pop("settings", SETTINGS),
        fetch_symbols=kw.pop("fetch_symbols", lambda: (SYMBOLS, [])),
        fetch_trending=kw.pop("fetch_trending", lambda: []),
        fallback=rss and RedditRSS(get=rss.get, sleep=clock.sleep, clock=clock.time, min_interval=0).fetch_back_to,
        clock=clock.time,
    )


def raw_ids(path):
    with gzip.open(path, "rt") as fh:
        return [json.loads(line)["id"] for line in fh]


@pytest.fixture
def setup(tmp_path):
    posts, comments = world()
    return Datastore(tmp_path), FakeArcticShift(posts=posts, comments=comments), FakeClock(start=T)


def test_first_run_backfills_and_flags_the_spiking_ticker(setup):
    ds, server, clock = setup
    summary = run(ds, server, clock, "r1")

    files = ds.raw_files()
    assert len(files) == 1
    assert len(raw_ids(files[0])) == 2 + 27 + 12
    assert summary["new_docs"] == 41

    state = ds.load_state()
    assert state["streams"]["pennystocks/comments"]["cursor"] == T - 3600
    assert state["streams"]["pennystocks/comments"]["last_complete_at"] == T
    assert state["streams"]["wallstreetbets/posts"]["cursor"] == T - 3 * DAY

    episodes = ds.read_csv("candidates/episodes.csv")
    assert [e["ticker"] for e in episodes] == ["ZZZZ"]
    e = episodes[0]
    assert e["reasons"] == "mention_spike hype_spike"
    assert (e["mentions_24h"], e["authors_24h"], e["hype_docs_24h"]) == ("13", "7", "12")
    assert e["exchange"] == "OTC"
    assert e["warmup"] == "1"
    assert e["first_flagged_at_utc"] == "2026-10-04T21:52:00Z"
    assert "https://www.reddit.com/r/pennystocks/comments/p1/" in e["examples"]
    assert "ZZZZ" in (ds.root / "candidates/README.md").read_text()
    assert summary["detection"] == "ran"


def test_second_run_only_stores_new_items_and_keeps_episode_open(setup):
    ds, server, clock = setup
    run(ds, server, clock, "r1")

    server.items["comments"] += [
        comment("z100", T + 300, author="z1", body="$ZZZZ still running"),
        comment("z101", T + 600, author="z2", body="$ZZZZ"),
    ]
    clock.now = T + 900
    summary = run(ds, server, clock, "r2")

    files = ds.raw_files()
    assert len(files) == 2
    assert sorted(raw_ids(files[1])) == ["t1_z100", "t1_z101"]
    assert summary["new_docs"] == 2
    assert [e["ticker"] for e in ds.read_csv("candidates/episodes.csv")] == ["ZZZZ"]
    active = ds.read_csv("candidates/active.csv")
    assert [(a["ticker"], a["n_flags"], a["mentions_24h"]) for a in active] == [("ZZZZ", "2", "15")]


def test_failed_stream_keeps_others_going_and_skips_detection(setup):
    ds, server, clock = setup
    real_get = server.get

    def get(url, params, timeout=30):
        if params["subreddit"] == "wallstreetbets" and url.endswith("/comments/search"):
            return 500, {}, {"error": "boom"}
        return real_get(url, params, timeout)

    server.get = get
    summary = run(ds, server, clock, "r1")

    state = ds.load_state()
    assert state["streams"]["pennystocks/comments"]["cursor"] == T - 3600
    bad = state["streams"]["wallstreetbets/comments"]
    assert bad.get("cursor") is None and bad["consecutive_errors"] == 1
    assert "500" in bad["last_error"]
    assert len(raw_ids(ds.raw_files()[0])) == 41  # wsb had no comments in this world anyway
    assert summary["detection"].startswith("skipped")
    assert ds.read_csv("candidates/episodes.csv") == []
    log = ds.read_csv("logs/runs/2026-10.csv")
    assert {r["stream"]: r["error"] != "" for r in log} == {
        "pennystocks/posts": False,
        "wallstreetbets/posts": False,
        "pennystocks/comments": False,
        "wallstreetbets/comments": True,
    }


def test_stocktwits_failure_does_not_break_the_run(setup):
    ds, server, clock = setup

    def boom():
        raise RuntimeError("403")

    summary = run(ds, server, clock, "r1", fetch_trending=boom)
    assert summary["detection"] == "ran"
    assert any("stocktwits" in e for e in summary["warnings"])


def test_stocktwits_rows_are_logged_and_rank_attached_to_candidates(setup):
    ds, server, clock = setup
    rows = [{"collected_at": T, "rank": 4, "symbol": "ZZZZ", "title": "Spike", "exchange": "OTC", "watchlist_count": 9, "is_crypto": 0}]
    run(ds, server, clock, "r1", fetch_trending=lambda: rows)
    assert ds.read_csv("stocktwits/trending/2026-10.csv")[0]["symbol"] == "ZZZZ"
    assert ds.read_csv("candidates/episodes.csv")[0]["stocktwits_rank"] == "4"


def test_daily_rollover_reconciles_late_items_and_writes_counts(setup):
    ds, server, clock = setup
    run(ds, server, clock, "r1")

    # Arctic Shift ingested this comment late: created 21:00 on Oct 4, long before our cursor overlap
    server.items["comments"].append(comment("late1", T - 3 * 3600, author="q", body="$ZZZZ"))
    clock.now = T + 3 * 3600  # 2026-10-05 00:52 UTC
    summary = run(ds, server, clock, "r2")

    assert summary["daily"] == "2026-10-04"
    assert "t1_late1" in raw_ids(ds.raw_files()[-1])
    counts = {r["ticker"]: r for r in ds.read_csv("daily/mention_counts/2026-10.csv") if r["date"] == "2026-10-04"}
    assert counts["ZZZZ"]["mentions"] == "14"  # 12 comments + post + late comment
    assert counts["AAAA"]["mentions"] == "3"
    assert ds.load_state()["daily_done_for"] == "2026-10-04"

    clock.now = T + 3 * 3600 + 900
    assert run(ds, server, clock, "r3")["daily"] is None


def daily_rows(ds):
    return ds.read_csv("daily/mention_counts/2026-09.csv") + ds.read_csv("daily/mention_counts/2026-10.csv")


def test_backfilled_days_get_daily_counts_once(setup):
    ds, server, clock = setup
    run(ds, server, clock, "r1")  # backfill from Sep 25 21:52

    by_date = {}
    for r in daily_rows(ds):
        by_date.setdefault(r["date"], {})[r["ticker"]] = r["mentions"]
    # Sep 25 is only partly covered; Oct 4 waits for the 00:30 re-fetch
    assert sorted(by_date) == ["2026-09-26", "2026-09-27", "2026-09-28", "2026-09-29", "2026-09-30",
                               "2026-10-01", "2026-10-02", "2026-10-03"]
    assert all(day == {"AAAA": "3"} for day in by_date.values())

    clock.now = T + 900
    run(ds, server, clock, "r2")
    assert len(daily_rows(ds)) == 8  # nothing written twice


def test_days_missed_while_the_collector_was_down_get_counts_after_it_catches_up(setup):
    ds, server, clock = setup
    run(ds, server, clock, "r1")
    server.items["comments"] += [comment("d5", T + 6 * 3600, body="AAAA"), comment("d6", T + DAY + 6 * 3600, body="AAAA")]

    clock.now = T + 2 * DAY + 3 * 3600  # down until Oct 7 00:52 UTC
    summary = run(ds, server, clock, "r2")

    assert summary["daily"] == "2026-10-06"
    dates = [r["date"] for r in daily_rows(ds) if r["ticker"] == "AAAA"]
    assert sorted(dates)[-3:] == ["2026-10-04", "2026-10-05", "2026-10-06"]
    assert len(dates) == len(set(dates))


def test_daily_reconcile_that_runs_out_of_time_resumes_where_it_stopped(setup):
    ds, server, clock = setup
    server.items["comments"].append(comment("w0", T - 3600, sub="wallstreetbets", body="hi"))
    run(ds, server, clock, "r1")
    # 450 comments Arctic Shift archived late, spread over Oct 4 before our cursor overlap
    day = T - 21 * 3600 - 52 * 60  # 2026-10-04 00:00 UTC
    server.items["comments"] += [comment(f"late{i}", day + i * 40, sub="wallstreetbets", body="$QWRT") for i in range(450)]
    slow = dict(min_interval=10, settings=Settings(subreddits=SETTINGS.subreddits, max_seconds=65))

    clock.now = T + 3 * 3600  # 2026-10-05 00:52 UTC: one 250-item page fits in the budget
    summary = run(ds, server, clock, "r2", **slow)
    assert summary["daily"] is None
    assert any("incomplete" in w for w in summary["warnings"])

    calls_before = len(server.calls)
    clock.now += 900
    summary = run(ds, server, clock, "r3", **slow)
    assert summary["daily"] == "2026-10-04"
    resumed = [(url, params) for url, params in server.calls[calls_before:] if "before" in params]
    assert {(url.rsplit("/", 2)[-2], params["subreddit"]) for url, params in resumed} == {("comments", "wallstreetbets")}
    counts = {r["ticker"]: r for r in daily_rows(ds) if r["date"] == "2026-10-04"}
    assert counts["QWRT"]["mentions"] == "450"


def test_symbol_refresh_that_lost_a_source_is_retried_within_hours(setup):
    ds, server, clock = setup
    calls = []

    def fetch():
        calls.append(clock.now)
        return SYMBOLS, (["https://www.sec.gov/...: 403 Forbidden"] if len(calls) == 1 else [])

    run(ds, server, clock, "r1", fetch_symbols=fetch)
    clock.now = T + 3 * 3600
    run(ds, server, clock, "r2", fetch_symbols=fetch)  # SEC failed last time: try again
    clock.now = T + 6 * 3600
    run(ds, server, clock, "r3", fetch_symbols=fetch)  # clean refresh 3 h ago: keep it
    assert calls == [T, T + 3 * 3600]



def test_symbols_are_refreshed_as_soon_as_an_sec_contact_is_added(setup, monkeypatch):
    ds, server, clock = setup
    calls = []

    def fetch():
        calls.append(clock.now)
        return SYMBOLS, ["https://www.sec.gov/...: skipped, set the SEC_USER_AGENT secret"]

    monkeypatch.delenv("SEC_USER_AGENT", raising=False)
    run(ds, server, clock, "r1", fetch_symbols=fetch)
    clock.now = T + 900
    run(ds, server, clock, "r2", fetch_symbols=fetch)  # nothing changed and the retry wait isn't over
    monkeypatch.setenv("SEC_USER_AGENT", "pump-dump-detector someone@example.org")
    clock.now = T + 1800
    run(ds, server, clock, "r3", fetch_symbols=fetch)  # the secret was just added: refresh now
    assert calls == [T, T + 1800]

STOP = Settings(stop_min_days=120, stop_min_episodes=2, stop_episode_age_days=10, stop_max_days=180)


def add_episodes(ds, flagged, warmup):
    rows = [{"episode_id": f"E{i}", "first_flagged_at": t, "warmup": w} for i, (t, w) in enumerate(zip(flagged, warmup))]
    ds.append_csv("candidates/episodes.csv", ["episode_id", "first_flagged_at", "warmup"], rows)


def test_collection_goes_on_until_enough_settled_candidates_or_the_day_limit(tmp_path):
    ds = Datastore(tmp_path)
    state = {"live_since": T}
    now = T + 130 * DAY
    # a warm-up flag and one too recent for its 10-day follow-up don't count
    add_episodes(ds, [T + 2 * DAY, T + 50 * DAY, T + 125 * DAY], ["1", "0", "0"])
    assert collection_done(ds, state, now, STOP) is None
    add_episodes(ds, [T + 100 * DAY], ["0"])
    assert collection_done(ds, state, now, STOP) == "2 candidates after 130 days"
    assert collection_done(ds, state, T + 119 * DAY, STOP) is None  # enough candidates, too few days
    assert collection_done(Datastore(tmp_path / "empty"), state, T + 180 * DAY, STOP) == "reached the 180-day limit"


def test_finished_collection_fetches_nothing_and_says_so(setup):
    ds, server, clock = setup
    run(ds, server, clock, "r1")
    calls = len(server.calls)

    clock.now = T + 181 * DAY
    summary = run(ds, server, clock, "r2")
    assert summary["finished"] == "reached the 180-day limit"
    assert len(server.calls) == calls
    assert "Collection finished" in ds.path("candidates/README.md").read_text()
    assert json.loads(ds.path("reports/health.json").read_text())["healthy"]  # no stale-data alert

    clock.now += 900
    run(ds, server, clock, "r3")
    assert ds.path("candidates/README.md").read_text().count("Collection finished") == 1


def test_health_reports_stale_and_erroring_streams():
    now = T
    state = {
        "streams": {
            "a/posts": {"initialized_at": now - DAY, "last_complete_at": now - 600, "consecutive_errors": 0},
            "a/comments": {"initialized_at": now - DAY, "last_complete_at": now - 5 * 3600, "consecutive_errors": 0},
            "b/posts": {"initialized_at": now - DAY, "last_complete_at": now - 60, "consecutive_errors": 4, "last_error": "HTTP 500"},
            "b/comments": {"initialized_at": now - 7 * 3600, "last_complete_at": None, "consecutive_errors": 0},
        }
    }
    h = health(state, now, Settings(subreddits=("a", "b")))
    assert h["healthy"] is False
    joined = " | ".join(h["problems"])
    assert "a/comments" in joined and "b/posts" in joined and "b/comments" in joined
    assert "a/posts" not in joined


def test_health_ok_when_all_streams_fresh():
    state = {"streams": {f"{s}/{k}": {"initialized_at": T - DAY, "last_complete_at": T - 60, "consecutive_errors": 0} for s in ("a",) for k in ("posts", "comments")}}
    assert health(state, T, Settings(subreddits=("a",))) == {"healthy": True, "problems": []}


def test_item_archived_late_but_inside_overlap_is_caught_by_next_run(setup):
    ds, server, clock = setup
    run(ds, server, clock, "r1")  # pennystocks comments cursor is now T - 3600

    server.items["comments"].append(comment("late2", T - 3600 - 600, author="q", body="hello"))
    clock.now = T + 900
    run(ds, server, clock, "r2")

    assert "t1_late2" in raw_ids(ds.raw_files()[-1])


def test_partial_symbol_refresh_merges_into_existing_list(setup):
    ds, server, clock = setup
    run(ds, server, clock, "r1")  # saves SYMBOLS (AAAA, ZZZZ)

    clock.now = T + 21 * 3600  # past the refresh interval
    client = ArcticShift(get=server.get, sleep=clock.sleep, clock=clock.time, min_interval=0)
    new = {"BBBB": {"symbol": "BBBB", "name": "New Listing", "exchange": "Nasdaq", "is_etf": 0, "cik": None, "source": "nasdaqtrader"}}
    summary = run_collect(
        ds, client, run_id="r2", settings=SETTINGS, fetch_symbols=lambda: (new, ["sec.gov: 403"]), fetch_trending=None, clock=clock.time
    )

    saved = {r["symbol"] for r in ds.read_csv("ref/symbols.csv")}
    assert saved == {"AAAA", "ZZZZ", "BBBB"}  # SEC failed, so its old OTC entry (ZZZZ) is kept
    assert any("403" in w for w in summary["warnings"])
    assert ds.load_state()["symbols_refreshed_at"] == T + 21 * 3600


def test_field_the_api_stopped_accepting_is_reported_once_and_collection_continues(setup):
    from fakes import DOC_FIELDS

    ds, _, clock = setup
    posts, comments = world()
    valid = {**DOC_FIELDS, "comments": DOC_FIELDS["comments"] - {"author_flair_text"}}
    server = FakeArcticShift(posts=posts, comments=comments, valid_fields=valid)

    summary = run(ds, server, clock, "r1")

    assert summary["new_docs"] == len(posts) + len(comments)
    assert [w for w in summary["warnings"] if "author_flair_text" in w] == [
        "arctic shift: API rejected field comments.author_flair_text; collecting without it"
    ]


class Outage:
    """Arctic Shift behind Cloudflare with its server gone (2026-10-09): every request is a 522."""

    def __init__(self):
        self.calls = 0

    def get(self, url, params, timeout=30):
        self.calls += 1
        return 522, {}, {"error": "arctic-shift.photon-reddit.com | 522: Connection timed out"}


def raw_records(ds):
    out = []
    for path in ds.raw_files():
        with gzip.open(path, "rt") as fh:
            out += [json.loads(line) for line in fh]
    return out


def chatter(prefix, start, n, sub="pennystocks", body="$YYYY ripping"):
    return [comment(f"{prefix}{j}", start + j * 60, sub=sub, author=f"{prefix}{j % 6}", body=body) for j in range(n)]


def test_reddit_rss_keeps_collection_and_flagging_going_while_arctic_shift_is_down(setup):
    ds, server, clock = setup
    server.items["comments"].append(comment("w0", T - 3600, sub="wallstreetbets", body="hi"))
    run(ds, server, clock, "r1")
    cursors = {k: st["cursor"] for k, st in ds.load_state()["streams"].items()}
    new = chatter("y", T + 600, 12)  # a new ticker takes off after Arctic Shift went down
    reddit = FakeRedditRSS(posts=server.items["posts"], comments=server.items["comments"] + new)
    outage = Outage()
    server.get = outage.get

    clock.now = T + 3600
    summary = run(ds, server, clock, "r2", rss=reddit)

    assert outage.calls == 6  # one stream's retries, then the run stops asking
    assert summary["detection"] == "ran" and summary["new_candidates"] == ["YYYY"]
    stored = {r["id"]: r for r in raw_records(ds)}
    assert all(stored[f"t1_y{j}"]["source"] == "reddit_rss" and stored[f"t1_y{j}"]["fetch_mode"] == "fallback" for j in range(12))
    state = ds.load_state()
    assert {k: st["cursor"] for k, st in state["streams"].items()} == cursors  # Arctic Shift re-reads it all later
    log = [r for r in ds.read_csv("logs/runs/2026-10.csv") if r["run_id"] == "r2"]
    assert {(r["stream"], r["mode"], r["complete"]) for r in log if r["mode"] == "fallback"} == {
        (k, "fallback", "1") for k in cursors
    }
    assert all("unreachable" in r["error"] for r in log if r["mode"] == "live" and r["stream"] != "pennystocks/posts")


def test_fallback_that_cannot_reach_back_vouches_only_from_its_own_first_read(setup):
    ds, server, clock = setup
    run(ds, server, clock, "r1")
    busy = chatter("w", T + 60, 300, sub="wallstreetbets", body="hi")  # more than the feed lists
    reddit = FakeRedditRSS(posts=server.items["posts"], comments=server.items["comments"] + busy, cap=100)
    server.get = Outage().get

    clock.now = T + 5 * 3600  # Arctic Shift's last complete fetch is now 5 h old
    summary = run(ds, server, clock, "r2", rss=reddit)
    assert summary["detection"].startswith("skipped: wallstreetbets/comments")
    assert any("wallstreetbets/comments: Reddit RSS" in w and "waits for Arctic Shift" in w for w in summary["warnings"])

    clock.now += 900  # nothing new: this read reaches back to the last one
    assert run(ds, server, clock, "r3", rss=reddit)["detection"] == "ran"


def test_arctic_shift_back_fills_in_what_the_feed_missed(setup):
    ds, server, clock = setup
    run(ds, server, clock, "r1")
    busy = chatter("w", T + 60, 300, sub="wallstreetbets", body="hi")
    server.items["comments"] += busy
    reddit = FakeRedditRSS(posts=server.items["posts"], comments=server.items["comments"], cap=100)
    real_get = server.get
    server.get = Outage().get
    clock.now = T + 5 * 3600
    run(ds, server, clock, "r2", rss=reddit)

    server.get = real_get
    clock.now += 900
    run(ds, server, clock, "r3", rss=reddit)

    ids = [r["id"] for r in raw_records(ds)]
    assert len(ids) == len(set(ids))  # nothing stored twice
    modes = {r["id"]: r["fetch_mode"] for r in raw_records(ds) if r["id"].startswith("t1_w")}
    assert len(modes) == 300
    assert sorted(set(modes.values())) == ["fallback", "live"]  # the feed's newest 100, then Arctic Shift's rest
    assert ds.load_state()["streams"]["wallstreetbets/comments"]["cursor"] == T + 60 + 299 * 60


def test_a_long_outage_is_probed_once_per_run(setup):
    ds, server, clock = setup
    run(ds, server, clock, "r1")
    outage = Outage()
    server.get = outage.get
    for i in range(4):
        clock.now += 900
        run(ds, server, clock, f"down{i}")
    outage.calls = 0

    clock.now += 900
    run(ds, server, clock, "r6")

    assert outage.calls == 1  # every stream has failed 4 runs in a row: one try notices when it's back


def test_a_broken_fallback_never_breaks_the_run(setup):
    ds, server, clock = setup
    run(ds, server, clock, "r1")
    server.get = Outage().get

    def broken(kind, sub, since, deadline=None):
        raise ValueError("feed changed shape")

    clock.now += 900
    summary = run_collect(ds, ArcticShift(get=server.get, sleep=clock.sleep, clock=clock.time, min_interval=0),
                          run_id="r2", settings=SETTINGS, fetch_symbols=lambda: (SYMBOLS, []), fallback=broken,
                          clock=clock.time)

    rows = [r for r in summary["streams"] if r["mode"] == "fallback"]
    assert len(rows) == 4 and all("feed changed shape" in r["error"] for r in rows)
    assert ds.load_state()["last_run"]["run_id"] == "r2"


def test_while_arctic_shift_is_down_the_fallback_may_use_the_whole_run(setup):
    ds, server, clock = setup
    run(ds, server, clock, "r1")
    server.get = Outage().get
    deadlines = []

    def fallback(kind, sub, since, deadline=None):
        deadlines.append(deadline)
        return FeedResult()

    clock.now = T + 3 * 3600  # past 00:30 UTC: the daily re-fetch is due, but Arctic Shift can't serve it
    started = clock.now
    run_collect(ds, ArcticShift(get=server.get, sleep=clock.sleep, clock=clock.time, min_interval=0),
                run_id="r2", settings=SETTINGS, fetch_symbols=lambda: (SYMBOLS, []), fallback=fallback,
                clock=clock.time)

    assert len(deadlines) == 4 and set(deadlines) == {started + SETTINGS.max_seconds}
