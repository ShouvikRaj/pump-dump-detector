import pytest

from fakes import DOC_FIELDS, FakeArcticShift, FakeClock, comment, post
from pumpdump.sources.arctic_shift import ArcticShift, ArcticShiftError, fetch_since, requests_getter, to_record

T0 = 1_791_000_000


def make_client(server, clock=None, **kw):
    clock = clock or FakeClock()
    return ArcticShift(get=server.get, sleep=clock.sleep, clock=clock.time, **kw), clock


@pytest.mark.parametrize("inclusive", [False, True])
def test_paginates_until_caught_up_and_returns_each_item_once(inclusive):
    comments = [comment(f"c{i}", T0 + i * 10) for i in range(250)]
    server = FakeArcticShift(comments=comments, after_inclusive=inclusive)
    client, _ = make_client(server)

    res = fetch_since(client, "comments", "pennystocks", after=T0 - 1, limit=100)

    assert [it["id"] for it in res.items] == [f"c{i}" for i in range(250)]
    assert res.complete is True
    assert res.newest_created == T0 + 2490
    assert res.error is None


def test_items_sharing_a_second_across_page_boundary_are_not_lost():
    # 5 comments posted in the same second straddle the 100-item page edge
    comments = [comment(f"c{i}", T0 + i) for i in range(98)]
    comments += [comment(f"tie{j}", T0 + 98) for j in range(5)]
    comments += [comment(f"d{i}", T0 + 100 + i) for i in range(20)]
    server = FakeArcticShift(comments=comments)
    client, _ = make_client(server)

    res = fetch_since(client, "comments", "pennystocks", after=T0 - 1, limit=100)

    assert sorted(it["id"] for it in res.items) == sorted(c["id"] for c in comments)


def test_limit_auto_pages_are_followed():
    comments = [comment(f"c{i}", T0 + i) for i in range(600)]
    server = FakeArcticShift(comments=comments, auto_size=250)
    client, _ = make_client(server)

    res = fetch_since(client, "comments", "pennystocks", after=T0 - 1, limit="auto")

    assert len(res.items) == 600
    assert res.complete is True


def test_page_cap_stops_early_and_reports_incomplete():
    comments = [comment(f"c{i}", T0 + i) for i in range(500)]
    server = FakeArcticShift(comments=comments)
    client, _ = make_client(server)

    res = fetch_since(client, "comments", "pennystocks", after=T0 - 1, limit=100, max_pages=2)

    assert res.complete is False
    assert res.pages == 2
    # everything up to the newest fetched item is contiguous
    assert res.newest_created == max(it["created_utc"] for it in res.items)
    assert {it["id"] for it in res.items} == {f"c{i}" for i in range(res.newest_created - T0 + 1)}


def test_deadline_stops_paging():
    comments = [comment(f"c{i}", T0 + i) for i in range(500)]
    server = FakeArcticShift(comments=comments)
    clock = FakeClock()
    client, _ = make_client(server, clock=clock, min_interval=1.0)

    res = fetch_since(client, "comments", "pennystocks", after=T0 - 1, limit=100, deadline=clock.now + 1.5)

    assert res.complete is False
    assert 1 <= res.pages <= 3


def test_items_are_stamped_with_time_their_page_arrived():
    posts = [post(f"p{i}", T0 + i) for i in range(150)]
    server = FakeArcticShift(posts=posts)
    clock = FakeClock(start=2_000_000_000.0)
    client, _ = make_client(server, clock=clock, min_interval=2.0)

    res = fetch_since(client, "posts", "pennystocks", after=T0 - 1, limit=100)

    first_page = {it["_collected_at"] for it in res.items[:100]}
    second_page = {it["_collected_at"] for it in res.items[100:]}
    assert first_page == {2_000_000_000.0}
    assert second_page == {2_000_000_002.0}


def test_rate_limit_waits_for_reset_header_then_retries():
    server = FakeArcticShift(posts=[post("p1", T0)], failures=[(429, {"X-RateLimit-Reset": "7"})])
    client, clock = make_client(server)

    res = fetch_since(client, "posts", "pennystocks", after=T0 - 1)

    assert [it["id"] for it in res.items] == ["p1"]
    assert 7 in clock.sleeps


def test_server_errors_are_retried_with_backoff():
    server = FakeArcticShift(posts=[post("p1", T0)], failures=[(500, {}), (0, {}), (503, {})])
    client, clock = make_client(server)

    res = fetch_since(client, "posts", "pennystocks", after=T0 - 1)

    assert [it["id"] for it in res.items] == ["p1"]
    assert len(server.calls) == 4


def test_persistent_failure_keeps_partial_results_and_reports_error():
    posts = [post(f"p{i}", T0 + i) for i in range(150)]
    server = FakeArcticShift(posts=posts)
    client, _ = make_client(server, max_retries=2)
    original = server.get
    calls = {"n": 0}

    def flaky(url, params, timeout=30):
        calls["n"] += 1
        if calls["n"] > 1:
            return 500, {}, {"error": "down"}
        return original(url, params, timeout)

    client.get = flaky
    res = fetch_since(client, "posts", "pennystocks", after=T0 - 1, limit=100)

    assert len(res.items) == 100
    assert res.complete is False
    assert "500" in res.error


def test_an_outage_makes_later_requests_in_the_run_fail_fast():
    # 2026-10-09: Cloudflare answered 522 for a day; six streams x six tries used up every run's budget
    server = FakeArcticShift(posts=[post("p1", T0)], failures=[(522, {})] * 20)
    client, _ = make_client(server, max_retries=2)

    first = fetch_since(client, "posts", "pennystocks", after=T0 - 1)
    calls = len(server.calls)
    second = fetch_since(client, "comments", "wallstreetbets", after=T0 - 1)

    assert "522" in first.error and calls == 3
    assert len(server.calls) == calls  # not asked again this run
    assert "unreachable" in second.error


def test_a_probing_client_tries_once_until_the_server_answers():
    down = FakeArcticShift(posts=[post("p1", T0)], failures=[(522, {})] * 5)
    client, _ = make_client(down, max_retries=2)
    client.probing = True  # a long outage: one try is enough to notice it's back

    assert "522" in fetch_since(client, "posts", "pennystocks", after=T0 - 1).error
    assert len(down.calls) == 1

    back = FakeArcticShift(posts=[post("p1", T0)], comments=[comment("c1", T0)])
    client, _ = make_client(back, max_retries=2)
    client.probing = True
    assert fetch_since(client, "posts", "pennystocks", after=T0 - 1).complete
    back.failures = [(522, {})]  # once it has answered, a hiccup is retried as usual
    assert fetch_since(client, "comments", "pennystocks", after=T0 - 1).complete


def test_query_timeouts_do_not_count_as_an_outage():
    server = FakeArcticShift(posts=[post("p1", T0)], failures=[(422, {})] * 3)
    client, _ = make_client(server, max_retries=2)

    assert "422" in fetch_since(client, "posts", "wallstreetbets", after=T0 - 1).error
    assert [it["id"] for it in fetch_since(client, "posts", "pennystocks", after=T0 - 1).items] == ["p1"]


def test_html_error_pages_are_reduced_to_their_title(monkeypatch):
    page = '<!DOCTYPE html>\n<!--[if lt IE 7]> <html class="no-js ie6 oldie" lang="en-US"> <![endif]-->' + " " * 600
    page += "<title>arctic-shift.photon-reddit.com | 522: Connection timed out</title>"

    class Resp:
        status_code, headers, text = 522, {}, page

        def json(self):
            raise ValueError("not json")

    monkeypatch.setattr("requests.Session.get", lambda self, url, params=None, timeout=None: Resp())
    status, _, body = requests_getter()("https://example.org", {})
    assert (status, body) == (522, {"error": "arctic-shift.photon-reddit.com | 522: Connection timed out"})


def test_default_field_lists_are_accepted_by_the_api():
    server = FakeArcticShift(posts=[post("p1", T0, title="hi")], comments=[comment("c1", T0, body="yo")])
    client, _ = make_client(server)

    assert client.search("posts", "pennystocks", after=T0 - 1)[0]["title"] == "hi"
    assert client.search("comments", "pennystocks", after=T0 - 1)[0]["body"] == "yo"
    assert len(server.calls) == 2 and all("fields" in params for _, params in server.calls)


def test_field_the_api_rejects_is_dropped_and_remembered():
    valid = {**DOC_FIELDS, "posts": DOC_FIELDS["posts"] - {"author_flair_text"}}
    server = FakeArcticShift(posts=[post("p1", T0, title="hi")], valid_fields=valid)
    client, clock = make_client(server)

    assert client.search("posts", "pennystocks", after=T0 - 1)[0]["title"] == "hi"
    assert client.search("posts", "pennystocks", after=T0 - 1)[0]["title"] == "hi"

    fields = [params["fields"].split(",") for _, params in server.calls]
    assert len(fields) == 3
    assert "author_flair_text" in fields[0]
    assert "author_flair_text" not in fields[1] and "author_flair_text" not in fields[2]
    assert "title" in fields[2]
    assert client.dropped_fields == ["posts.author_flair_text"]


def test_client_error_other_than_fields_is_raised():
    server = FakeArcticShift(failures=[(400, {})] * 10)
    client, _ = make_client(server)
    with pytest.raises(ArcticShiftError):
        client.search("posts", "pennystocks", after=T0)


def test_empty_result_is_complete_without_cursor():
    client, _ = make_client(FakeArcticShift())
    res = fetch_since(client, "posts", "pennystocks", after=T0)
    assert res.items == [] and res.complete is True and res.newest_created is None


def test_requests_are_spaced_by_min_interval():
    comments = [comment(f"c{i}", T0 + i) for i in range(250)]
    server = FakeArcticShift(comments=comments)
    clock = FakeClock()
    client, _ = make_client(server, clock=clock, min_interval=1.5)

    fetch_since(client, "comments", "pennystocks", after=T0 - 1, limit=100)

    assert clock.sleeps == [1.5, 1.5]


def test_to_record_normalises_post():
    item = post("abc", T0, sub="PennyStocks", author="alice", title="$GME", selftext="body", score=5, num_comments=3)
    item["_collected_at"] = T0 + 30.5
    rec = to_record("posts", item, run_id="r1")
    assert rec["id"] == "t3_abc"
    assert rec["kind"] == "post"
    assert rec["subreddit"] == "pennystocks"
    assert rec["created_utc"] == T0
    assert rec["collected_at"] == T0 + 30.5
    assert rec["source"] == "arctic_shift"
    assert rec["source_retrieved_at"] == T0 + 20
    assert (rec["title"], rec["body"]) == ("$GME", "body")
    assert (rec["score"], rec["num_comments"]) == (5, 3)
    assert rec["link_id"] is None
    assert rec["run_id"] == "r1"


def test_to_record_builds_permalinks_the_api_does_not_return():
    p = post("abc", T0, sub="PennyStocks")
    c = comment("xyz", T0, sub="wallstreetbets", link_id="t3_p9")
    for item in (p, c):
        del item["permalink"]
        item["_collected_at"] = T0
    assert to_record("posts", p, run_id="r")["permalink"] == "/r/pennystocks/comments/abc/"
    assert to_record("comments", c, run_id="r")["permalink"] == "/r/wallstreetbets/comments/p9/comment/xyz/"


def test_to_record_normalises_comment():
    item = comment("xyz", T0, body="nice", link_id="t3_p9", parent_id="t1_c1")
    item["_collected_at"] = T0 + 60
    rec = to_record("comments", item, run_id="r2")
    assert rec["id"] == "t1_xyz"
    assert rec["kind"] == "comment"
    assert rec["title"] is None
    assert rec["body"] == "nice"
    assert (rec["link_id"], rec["parent_id"]) == ("t3_p9", "t1_c1")


def test_to_record_omits_fields_the_api_never_serves():
    # a None here would read as "not removed" / "not edited", which nobody actually knows
    item = post("abc", T0, crosspost_parent="t3_zzz")
    item["_collected_at"] = T0
    rec = to_record("posts", item, run_id="r")
    assert not {"upvote_ratio", "removed_by_category", "stickied", "edited"} & rec.keys()
    assert rec["crosspost_parent"] == "t3_zzz"
