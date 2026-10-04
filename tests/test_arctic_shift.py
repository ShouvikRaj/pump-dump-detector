import pytest

from fakes import FakeArcticShift, FakeClock, comment, post
from pumpdump.sources.arctic_shift import ArcticShift, ArcticShiftError, fetch_since, to_record

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


def test_unknown_field_rejection_falls_back_to_full_records():
    server = FakeArcticShift(posts=[post("p1", T0, title="hi")], reject_fields=True)
    client, _ = make_client(server)

    res = fetch_since(client, "posts", "pennystocks", after=T0 - 1)

    assert res.items[0]["title"] == "hi"
    assert "fields" in server.calls[0][1]
    assert "fields" not in server.calls[-1][1]


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


def test_to_record_normalises_comment():
    item = comment("xyz", T0, body="nice", link_id="t3_p9", parent_id="t1_c1")
    item["_collected_at"] = T0 + 60
    rec = to_record("comments", item, run_id="r2")
    assert rec["id"] == "t1_xyz"
    assert rec["kind"] == "comment"
    assert rec["title"] is None
    assert rec["body"] == "nice"
    assert (rec["link_id"], rec["parent_id"]) == ("t3_p9", "t1_c1")
