import re

from fakes import FakeClock, FakeRedditRSS, atom_feed, comment, post
from pumpdump.sources.arctic_shift import to_record
from pumpdump.sources.reddit_rss import RedditRSS, parse_feed

T0 = 1_791_000_000

# trimmed from the live feeds (2026-10-10): a self post and a comment
LIVE = b"""<?xml version="1.0" encoding="UTF-8"?><feed xmlns="http://www.w3.org/2005/Atom" xmlns:media="http://search.yahoo.com/mrss/"><category term="pennystocks" label="r/pennystocks"/><title>newest submissions</title>
<entry><author><name>/u/AutoModerator</name><uri>https://www.reddit.com/user/AutoModerator</uri></author><category term="pennystocks" label="r/pennystocks"/><content type="html">&lt;!-- SC_OFF --&gt;&lt;div class=&quot;md&quot;&gt;&lt;p&gt;Talk about your daily plays &lt;strong&gt;$ABCD&lt;/strong&gt;. &lt;/p&gt; &lt;p&gt;Trade responsibly.&lt;/p&gt; &lt;/div&gt;&lt;!-- SC_ON --&gt; &amp;#32; submitted by &amp;#32; &lt;a href=&quot;https://www.reddit.com/user/AutoModerator&quot;&gt; /u/AutoModerator &lt;/a&gt; &lt;br/&gt; &lt;span&gt;&lt;a href=&quot;https://www.reddit.com/r/pennystocks/comments/1x25je4/the_lounge/&quot;&gt;[link]&lt;/a&gt;&lt;/span&gt; &amp;#32; &lt;span&gt;&lt;a href=&quot;https://www.reddit.com/r/pennystocks/comments/1x25je4/the_lounge/&quot;&gt;[comments]&lt;/a&gt;&lt;/span&gt;</content><id>t3_1x25je4</id><link href="https://www.reddit.com/r/pennystocks/comments/1x25je4/the_lounge/" /><updated>2026-10-10T04:00:43+00:00</updated><published>2026-10-10T04:00:43+00:00</published><title>The Lounge &amp; more</title></entry>
<entry><author><name>/u/IndividualMessage836</name><uri>https://www.reddit.com/user/IndividualMessage836</uri></author><category term="smallstreetbets" label="r/smallstreetbets" /><content type="html">&lt;!-- SC_OFF --&gt;&lt;div class=&quot;md&quot;&gt;&lt;p&gt;This ain&amp;#39;t going to happen&lt;/p&gt; &lt;table&gt;&lt;tr&gt;&lt;td&gt;GME&lt;/td&gt;&lt;td&gt;AMC&lt;/td&gt;&lt;/tr&gt;&lt;/table&gt; &lt;/div&gt;&lt;!-- SC_ON --&gt;</content><id>t1_pf1swta</id><link href="https://www.reddit.com/r/smallstreetbets/comments/1x1u0bc/are_we_winning_now/pf1swta/"/><updated>2026-10-10T14:07:57+00:00</updated><title>/u/IndividualMessage836 on Are we winning now?</title></entry>
</feed>"""


def test_parse_feed_reads_a_live_post():
    (p, _) = parse_feed(LIVE, "posts")
    assert p["id"] == "1x25je4"
    assert p["created_utc"] == 1_791_604_843  # 2026-10-10T04:00:43Z
    assert (p["author"], p["subreddit"]) == ("AutoModerator", "pennystocks")
    assert p["title"] == "The Lounge & more"
    assert p["selftext"] == "Talk about your daily plays $ABCD.\nTrade responsibly."  # no "submitted by" footer
    assert p["url"] == "https://www.reddit.com/r/pennystocks/comments/1x25je4/the_lounge/"


def test_parse_feed_reads_a_live_comment():
    (_, c) = parse_feed(LIVE, "comments")
    assert c["id"] == "pf1swta"
    assert c["created_utc"] == 1_791_641_277  # comments only carry <updated>
    assert (c["author"], c["subreddit"]) == ("IndividualMessage836", "smallstreetbets")
    assert c["body"] == "This ain't going to happen\nGME\nAMC"  # table cells don't run together
    assert c["link_id"] == "t3_1x1u0bc"


def test_parsed_items_become_records_marked_as_rss():
    (_, c) = parse_feed(LIVE, "comments")
    c["_collected_at"] = T0
    rec = to_record("comments", c, "r1", source="reddit_rss")
    assert (rec["id"], rec["source"], rec["source_retrieved_at"]) == ("t1_pf1swta", "reddit_rss", None)
    assert rec["permalink"] == "/r/smallstreetbets/comments/1x1u0bc/comment/pf1swta/"


def make(server, **kw):
    clock = FakeClock(start=T0 + 10_000)
    return RedditRSS(get=server.get, sleep=clock.sleep, clock=clock.time, **kw), clock


def test_pages_back_until_it_reaches_items_it_already_has():
    comments = [comment(f"c{i}", T0 + i * 10) for i in range(250)]
    rss, _ = make(FakeRedditRSS(comments=comments))

    res = rss.fetch_back_to("comments", "pennystocks", since=T0 + 1200)  # c120 and older are known

    assert res.complete is True and res.error is None
    assert res.pages == 2
    assert {it["id"] for it in res.items} >= {f"c{i}" for i in range(121, 250)}
    assert res.newest_created == T0 + 2490


def test_a_listing_that_ends_before_reaching_back_leaves_a_hole():
    comments = [comment(f"c{i}", T0 + i) for i in range(1500)]
    server = FakeRedditRSS(comments=comments, cap=1000)
    rss, _ = make(server)

    res = rss.fetch_back_to("comments", "pennystocks", since=T0 + 10)

    assert res.complete is False and res.error is None
    assert min(it["created_utc"] for it in res.items) == T0 + 500
    assert len(server.calls) <= 11


USED_UP = {"x-ratelimit-remaining": "0.0", "x-ratelimit-reset": "40"}


def test_waits_for_reddits_reset_when_the_rate_limit_is_used_up():
    comments = [comment(f"c{i}", T0 + i) for i in range(300)]
    server = FakeRedditRSS(comments=comments, headers=USED_UP)
    rss, clock = make(server)

    res = rss.fetch_back_to("comments", "pennystocks", since=T0, deadline=clock.now + 600)

    assert res.complete is True and res.error is None
    assert len(server.calls) == 3 and clock.sleeps == [41.0, 41.0]


def test_a_reset_after_the_deadline_ends_the_run_s_reading_without_asking_again():
    # runners share IP addresses, so another user may have spent this window's budget already
    comments = [comment(f"c{i}", T0 + i) for i in range(300)]
    server = FakeRedditRSS(comments=comments, headers=USED_UP)
    rss, clock = make(server)

    res = rss.fetch_back_to("comments", "pennystocks", since=T0, deadline=clock.now + 30)
    later = rss.fetch_back_to("posts", "pennystocks", since=T0, deadline=clock.now + 30)

    assert len(server.calls) == 1 and len(res.items) == 100
    assert res.complete is False and "rate limit" in res.error
    assert later.items == [] and "rate limit" in later.error


def test_a_429_waits_for_the_reset_and_tries_again_once():
    server = FakeRedditRSS(comments=[comment("c1", T0 + 5)], failures=[(429, {**USED_UP, "x-ratelimit-reset": "20"})])
    rss, clock = make(server)

    res = rss.fetch_back_to("comments", "pennystocks", since=T0 + 5, deadline=clock.now + 600)

    assert res.complete is True and len(server.calls) == 2 and clock.sleeps == [21.0]


def test_http_errors_are_reported_without_items():
    server = FakeRedditRSS(status=429)
    rss, _ = make(server)
    res = rss.fetch_back_to("posts", "pennystocks", since=T0)
    assert res.items == [] and res.complete is False and "429" in res.error
    assert len(server.calls) == 2  # one more try after waiting


def test_requests_are_spaced_and_respect_the_deadline():
    comments = [comment(f"c{i}", T0 + i) for i in range(1000)]
    rss, clock = make(FakeRedditRSS(comments=comments), min_interval=2.0)

    res = rss.fetch_back_to("comments", "pennystocks", since=T0, deadline=clock.now + 3)

    assert res.pages == 2 and res.complete is False
    assert clock.sleeps == [2.0]


def test_posts_feed_is_read_from_new():
    server = FakeRedditRSS(posts=[post("p1", T0 + 5, title="$ZZZZ", selftext="go")])
    rss, _ = make(server)
    res = rss.fetch_back_to("posts", "pennystocks", since=T0)
    assert server.calls[0][0] == "https://www.reddit.com/r/pennystocks/new/.rss"
    assert [(it["id"], it["title"], it["selftext"]) for it in res.items] == [("p1", "$ZZZZ", "go")]
    assert res.complete is False  # nothing at or before `since` came back, so it can't vouch for the gap


def serve(feed):
    return RedditRSS(get=lambda url, params, timeout=30: (200, {}, feed), sleep=lambda s: None, min_interval=0)


def test_entries_without_a_category_get_the_requested_subreddit():
    feed = re.sub(rb"<category [^>]*/>", b"", atom_feed("comments", [comment("c1", T0 + 5)]))
    (c,) = serve(feed).fetch_back_to("comments", "PennyStocks", since=T0 + 5).items
    assert c["subreddit"] == "PennyStocks"


def test_an_unreadable_timestamp_is_an_error_not_a_crash():
    feed = atom_feed("comments", [comment("c1", T0 + 5)]).replace(b"<updated>", b"<updated>yesterday ")
    res = serve(feed).fetch_back_to("comments", "pennystocks", since=T0)
    assert res.items == [] and "unreadable" in res.error
