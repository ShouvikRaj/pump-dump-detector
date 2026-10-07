import gzip
import json

from market_fakes import FakeClock, FakeHTTP
from pumpdump import cli, social
from pumpdump.market import SNAPSHOT_FIELDS, SNAPSHOTS
from pumpdump.sources import social as src
from pumpdump.sources.web import Web
from pumpdump.store import Datastore

HOUR = 3600
FLAG = 1_791_300_000.0  # 2026-10-06 ~15:20 UTC
ST = "https://api.stocktwits.com/api/2/streams/symbol/"


def iso(ts):
    return src._iso(ts)


def st_msg(i, t, user=1, followers=10, joined="2012-01-01", sentiment="Bullish", body="ABCD to the moon"):
    return {"id": i, "created_at": iso(t), "body": body, "likes": {"total": 2},
            "entities": {"sentiment": {"basic": sentiment} if sentiment else None},
            "symbols": [{"symbol": "ABCD"}],
            "user": {"id": user, "username": f"u{user}", "followers": followers, "join_date": joined, "ideas": 5}}


def st_page(msgs, more=False, max_id=0):
    return 200, json.dumps({"messages": msgs, "cursor": {"more": more, "max": max_id}})


def bsky_page(posts, cursor=None):
    return 200, json.dumps({"posts": posts, **({"cursor": cursor} if cursor else {})})


def bsky_post(t, text="$ABCD squeeze", did="did:plc:a"):
    return {"uri": f"at://{did}/app.bsky.feed.post/3abc", "author": {"did": did, "handle": "a.bsky.social"},
            "record": {"text": text, "createdAt": iso(t)}, "likeCount": 1}


def make_web(http, clock):
    return Web(request=http, sleep=clock.sleep, clock=clock.time, min_interval=0)


def test_stocktwits_pages_back_until_since():
    http = FakeHTTP()
    http.add("GET", ST + "ABCD.json", st_page([st_msg(3, FLAG), st_msg(2, FLAG - 10 * HOUR)], more=True, max_id=2),
             st_page([st_msg(1, FLAG - 80 * HOUR)], more=True, max_id=1))
    clock = FakeClock(FLAG + HOUR)
    posts, info = src.fetch_stocktwits(make_web(http, clock), "ABCD", FLAG - 72 * HOUR, max_pages=5)
    assert [p["id"] for p in posts] == ["3", "2"]  # the 80h-old message is before `since`
    assert info == {"requests": 2, "truncated": False, "error": ""}
    assert http.calls[1]["params"] == {"max": 2}
    assert posts[0]["sentiment"] == "bullish" and posts[0]["author_followers"] == 10


def test_stocktwits_page_limit_marks_truncated():
    http = FakeHTTP([("GET", ST, [st_page([st_msg(1, FLAG)], more=True, max_id=1)])])
    posts, info = src.fetch_stocktwits(make_web(http, FakeClock()), "ABCD", FLAG - HOUR, max_pages=2)
    assert info["truncated"] and info["requests"] == 2


def test_bluesky_keeps_only_posts_with_the_cashtag():
    obj = {"posts": [bsky_post(FLAG), bsky_post(FLAG, text="abcd is a word, $ABCDE another"),
                     bsky_post(FLAG, text="buy $abcd now")]}
    assert [p["text"] for p in src.parse_bluesky(obj, "ABCD")] == ["$ABCD squeeze", "buy $abcd now"]


def test_bluesky_retries_its_load_shedding_403s():
    http = FakeHTTP([("GET", src.BLUESKY_URL, [(403, "forbidden by administrative rules"), bsky_page([bsky_post(FLAG)])])])
    clock = FakeClock(FLAG + HOUR)
    posts, info = src.fetch_bluesky(make_web(http, clock), "ABCD", FLAG - HOUR, max_pages=3)
    assert len(posts) == 1 and info == {"requests": 2, "truncated": False, "error": ""}


def test_failed_source_leaves_counts_blank(tmp_path):
    ds = setup(tmp_path)
    clock = FakeClock(FLAG + 900)
    http = FakeHTTP([*routes()[:2], ("GET", src.BLUESKY_URL, [(403, "no")])])
    assert social.run_social(ds, make_web(http, clock), clock.time, 600)["written"] == []  # retried while recent
    clock.now = FLAG + 12 * 86400  # too late to retry: kept, with Bluesky blank
    summary = social.run_social(ds, make_web(http, clock), clock.time, 600)
    assert "| ABCD-1_ABCD_flag | 288h | 1 |  |" in social.render_summary(summary, "r1")
    row = ds.read_csv(social.SNAPSHOTS)[0]
    assert row["st_n"] == "1" and row["bsky_n"] == "" and row["errors"].startswith("bluesky: HTTP 403")


def test_x_parse_joins_users():
    obj = {"data": [{"id": "9", "author_id": "7", "created_at": iso(FLAG), "text": "$ABCD",
                     "entities": {"cashtags": [{"tag": "abcd"}]}, "public_metrics": {"like_count": 3}}],
           "includes": {"users": [{"id": "7", "username": "pumper", "created_at": iso(FLAG - 86400),
                                   "public_metrics": {"followers_count": 12, "tweet_count": 400}}]}}
    (p,) = src.parse_x(obj)
    assert p["author"] == "pumper" and p["author_followers"] == 12 and p["symbols"] == ["ABCD"]


def test_stats_counts_only_the_window_and_flags_new_accounts_and_copies():
    posts = src.parse_stocktwits({"messages": [
        st_msg(1, FLAG - HOUR, user=1, joined=iso(FLAG - 10 * 86400)[:10], body="BUY ABCD NOW https://x.y/1"),
        st_msg(2, FLAG - 2 * HOUR, user=1, joined=iso(FLAG - 10 * 86400)[:10], body="buy abcd now https://x.y/2"),
        st_msg(3, FLAG - 3 * HOUR, user=2, sentiment="Bearish", body="dilution coming"),
        st_msg(4, FLAG + HOUR, user=3),  # after the flag: not counted
    ]})
    s = social.stats(posts, FLAG - 24 * HOUR, FLAG)
    assert s["n"] == 3 and s["authors"] == 2
    assert s["top_author_share"] == round(2 / 3, 4)
    assert s["new_acct_share"] == round(2 / 3, 4)
    assert s["bull_share"] == round(2 / 3, 4)
    assert s["dup_share"] == round(2 / 3, 4)


def setup(tmp_path):
    ds = Datastore(tmp_path)
    ds.write_csv("candidates/episodes.csv", ["episode_id", "ticker", "first_flagged_at", "warmup"],
                 [{"episode_id": "ABCD-1", "ticker": "ABCD", "first_flagged_at": FLAG, "warmup": "0"}])
    ctrl = dict.fromkeys(SNAPSHOT_FIELDS, "")
    ctrl.update(snapshot_id="ABCD-1_WXYZ", role="control", episode_id="ABCD-1", ticker="WXYZ", as_of=str(FLAG))
    ds.write_csv(SNAPSHOTS, SNAPSHOT_FIELDS, [ctrl])
    return ds


def routes():
    return [("GET", ST + "ABCD.json", [st_page([st_msg(2, FLAG + 600), st_msg(1, FLAG - HOUR)])]),
            ("GET", ST + "WXYZ.json", [(404, "{}")]),
            ("GET", src.BLUESKY_URL, [bsky_page([bsky_post(FLAG - 2 * HOUR)])])]


def test_run_writes_flag_rows_then_daily_follow_ups(tmp_path):
    ds = setup(tmp_path)
    clock = FakeClock(FLAG + 900)
    http = FakeHTTP(routes())
    s = social.run_social(ds, make_web(http, clock), clock.time, max_seconds=600)
    rows = ds.read_csv(social.SNAPSHOTS)
    assert [(r["ticker"], r["phase"]) for r in rows] == [("ABCD", "flag"), ("WXYZ", "flag")]
    abcd = rows[0]
    assert (abcd["st_n"], abcd["st_n_72h"], abcd["st_n_after_flag"], abcd["bsky_n"]) == ("1", "1", "1", "1")
    assert abcd["lag_s"] == "900" and abcd["x_n"] == ""  # X off without a token
    assert rows[1]["errors"] == "not on StockTwits"
    assert not any("api.x.com" in u for u in http.urls())
    raw = list((tmp_path / "social/raw").rglob("ABCD-1_ABCD_flag.json.gz"))
    assert len(raw) == 1 and len(json.loads(gzip.decompress(raw[0].read_bytes()))["posts"]["stocktwits"]) == 2
    assert s["pending"] == 0

    # nothing new until a day later; then only the candidate gets a follow-up
    assert social.run_social(ds, make_web(http, clock), clock.time, 600)["written"] == []
    clock.now += 24 * HOUR
    social.run_social(ds, make_web(http, clock), clock.time, 600)
    rows = ds.read_csv(social.SNAPSHOTS)
    assert [(r["ticker"], r["phase"]) for r in rows][-1] == ("ABCD", "d1")
    assert rows[-1]["window_start_utc"] == iso(FLAG + 900)


def test_follow_ups_stop_after_ten_days(tmp_path):
    ds = setup(tmp_path)
    clock = FakeClock(FLAG + 900)
    http = FakeHTTP(routes())
    for _ in range(14):
        social.run_social(ds, make_web(http, clock), clock.time, 600)
        clock.now += 24 * HOUR
    phases = [r["phase"] for r in ds.read_csv(social.SNAPSHOTS) if r["ticker"] == "ABCD"]
    assert phases == ["flag"] + [f"d{i}" for i in range(1, 11)]


def test_stocktwits_failure_is_retried_next_run(tmp_path):
    ds = setup(tmp_path)
    clock = FakeClock(FLAG + 900)
    http = FakeHTTP([("GET", ST + "ABCD.json", [(500, "down")]), *routes()[1:]])
    s = social.run_social(ds, make_web(http, clock), clock.time, 600)
    assert [r["ticker"] for r in ds.read_csv(social.SNAPSHOTS)] == ["WXYZ"]
    assert "retried next run" in s["warnings"][0]


def test_x_runs_with_a_token_within_the_daily_budget(tmp_path):
    ds = setup(tmp_path)
    clock = FakeClock(FLAG + 900)
    x = {"data": [{"id": str(i), "author_id": "7", "created_at": iso(FLAG - HOUR), "text": "$ABCD"} for i in range(10)],
         "meta": {"next_token": "n"}}
    http = FakeHTTP([*routes(), ("GET", src.X_URL, [(200, json.dumps(x))])])
    social.run_social(ds, make_web(http, clock), clock.time, 600, x_token="t", x_daily_posts=15)
    rows = ds.read_csv(social.SNAPSHOTS)
    assert [r["x_fetched"] for r in rows] == ["10", ""]  # 15 a day: 10 fetched, then too few left for a call
    x_calls = [c for c in http.calls if c["url"] == src.X_URL]
    assert len(x_calls) == 1 and x_calls[0]["headers"]["Authorization"] == "Bearer t"
    assert x_calls[0]["params"]["max_results"] == 15


def test_cli_social_reports_not_finished_while_collecting(tmp_path, monkeypatch):
    ds = setup(tmp_path)
    monkeypatch.setattr(social, "Web", lambda: make_web(FakeHTTP(routes()), FakeClock(FLAG + 900)))
    out = tmp_path / "out.txt"
    assert cli.main(["social", "--datastore", str(tmp_path), "--github-output", str(out)]) == 0
    assert out.read_text() == "finished=false\n"
    assert len(ds.read_csv(social.SNAPSHOTS)) == 2
