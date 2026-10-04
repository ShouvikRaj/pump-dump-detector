import gzip
import json

import pytest

from fakes import FakeArcticShift, FakeClock, comment, post
from pumpdump.pipeline import Settings, health, run_collect
from pumpdump.sources.arctic_shift import ArcticShift
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
    client = ArcticShift(get=server.get, sleep=clock.sleep, clock=clock.time, min_interval=0)
    return run_collect(
        ds,
        client,
        run_id=run_id,
        settings=kw.pop("settings", SETTINGS),
        fetch_symbols=lambda: (SYMBOLS, []),
        fetch_trending=kw.pop("fetch_trending", lambda: []),
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
    assert "https://www.reddit.com/r/pennystocks/comments/p1/x/" in e["examples"]
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
    counts = {r["ticker"]: r for r in ds.read_csv("daily/mention_counts/2026-10.csv")}
    assert counts["ZZZZ"]["date"] == "2026-10-04"
    assert counts["ZZZZ"]["mentions"] == "14"  # 12 comments + post + late comment
    assert counts["AAAA"]["mentions"] == "3"
    assert ds.load_state()["daily_done_for"] == "2026-10-04"

    clock.now = T + 3 * 3600 + 900
    assert run(ds, server, clock, "r3")["daily"] is None


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
