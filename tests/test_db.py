import pytest

from pumpdump import db
from pumpdump.tickers import TickerExtractor

DAY = 86_400
T = 1_791_150_720


def doc(id_, created, collected=None, kind="comment", sub="pennystocks", author="alice", title=None, body="", permalink=None):
    return {
        "id": id_,
        "kind": kind,
        "subreddit": sub,
        "author": author,
        "created_utc": created,
        "collected_at": collected if collected is not None else created,
        "source": "arctic_shift",
        "source_retrieved_at": created + 20,
        "title": title,
        "body": body,
        "link_id": None,
        "parent_id": None,
        "url": None,
        "permalink": permalink or f"/r/{sub}/{id_}",
        "flair": None,
        "score": 1,
        "num_comments": 0,
        "upvote_ratio": None,
        "removed_by_category": None,
        "run_id": "r",
    }


@pytest.fixture
def ext():
    return TickerExtractor(universe={"GME", "AMC", "ABCD"}, common_words={"the"}, acronyms={"CEO"}, cashtag_block={"BTC"})


@pytest.fixture
def conn():
    c = db.connect(":memory:")
    yield c
    c.close()


def test_insert_docs_keeps_first_seen_copy(conn):
    assert db.insert_docs(conn, [doc("t1_a", T, collected=T + 10)]) == 1
    assert db.insert_docs(conn, [doc("t1_a", T, collected=T + 999), doc("t1_b", T)]) == 1
    assert conn.execute("select collected_at from docs where id='t1_a'").fetchone()[0] == T + 10
    assert db.existing_ids(conn, ["t1_a", "t1_b", "t1_c"]) == {"t1_a", "t1_b"}


def test_extract_mentions_records_tickers_hype_and_skips_bots(conn, ext):
    db.insert_docs(
        conn,
        [
            doc("t3_p", T, kind="post", title="$ABCD to the moon 🚀", body="short squeeze soon, AMC too"),
            doc("t1_c", T, body="nothing here"),
            doc("t1_bot", T, author="AutoModerator", body="$GME $AMC"),
        ],
    )

    assert db.extract_mentions(conn, ext, excluded_authors={"AutoModerator"}) == 2
    rows = conn.execute(
        "select doc_id, ticker, method, in_universe, kind, hype_score, n_tickers from mentions order by ticker"
    ).fetchall()
    assert rows == [("t3_p", "ABCD", "cashtag", 1, "post", 3, 2), ("t3_p", "AMC", "bare", 1, "post", 3, 2)]
    # every doc is marked processed, so a second pass does nothing
    assert db.extract_mentions(conn, ext, excluded_authors={"AutoModerator"}) == 0


def test_extract_mentions_applies_the_subreddit_rules(conn):
    ext = TickerExtractor(universe={"PMI"}, common_words=(), acronyms=(), cashtag_block=(), wsb_acronyms={"PMI"})
    db.insert_docs(
        conn,
        [doc("t1_w", T, sub="wallstreetbets", body="PMI in 2 min"), doc("t1_p", T, sub="pennystocks", body="PMI just got halted")],
    )
    db.extract_mentions(conn, ext, excluded_authors=set())
    assert conn.execute("select doc_id, ticker from mentions").fetchall() == [("t1_p", "PMI")]


def _seed(conn, ext, docs):
    db.insert_docs(conn, docs)
    db.extract_mentions(conn, ext, excluded_authors=set())


def test_window_counts_buckets_by_24h_before_as_of(conn, ext):
    _seed(
        conn,
        ext,
        [
            doc("t1_1", T - 10, author="a", body="$ABCD"),
            doc("t1_2", T - DAY + 5, author="b", body="$ABCD"),
            doc("t1_3", T - DAY + 6, author="b", body="$ABCD"),  # same author twice
            doc("t1_4", T - DAY - 5, author="c", body="$ABCD"),  # day 1
            doc("t1_5", T - 7 * DAY - 5, author="d", body="$ABCD"),  # day 7
            doc("t1_6", T - 8 * DAY - 5, author="e", body="$ABCD"),  # outside window
        ],
    )

    w = db.window_counts(conn, as_of=T)["ABCD"]
    assert w.counts == [3, 1, 0, 0, 0, 0, 0, 1]
    assert w.authors == [2, 1, 0, 0, 0, 0, 0, 1]


def test_strict_window_ignores_docs_collected_after_as_of(conn, ext):
    _seed(
        conn,
        ext,
        [
            doc("t1_1", T - 100, collected=T - 50, body="$ABCD"),
            doc("t1_2", T - 100, collected=T + 50, author="b", body="$ABCD"),  # collected later
        ],
    )
    assert db.window_counts(conn, as_of=T)["ABCD"].counts[0] == 1
    assert db.window_counts(conn, as_of=T, strict=False)["ABCD"].counts[0] == 2


def test_deleted_authors_count_as_mentions_but_not_authors(conn, ext):
    _seed(conn, ext, [doc("t1_1", T - 5, author="[deleted]", body="$ABCD"), doc("t1_2", T - 6, author=None, body="$ABCD")])
    w = db.window_counts(conn, as_of=T)["ABCD"]
    assert (w.counts[0], w.authors[0]) == (2, 0)


def test_hype_docs_and_hype_authors(conn, ext):
    _seed(
        conn,
        ext,
        [
            doc("t1_1", T - 5, author="a", body="$ABCD 🚀 short squeeze"),
            doc("t1_2", T - 6, author="a", body="$ABCD 💎🙌 lambo"),
            doc("t1_3", T - 7, author="b", body="$ABCD 🚀"),  # one category: not hype
        ],
    )
    w = db.window_counts(conn, as_of=T)["ABCD"]
    assert w.hype_docs[0] == 2
    assert w.hype_authors_now == 1


def test_ticker_details_lists_subreddits_and_examples(conn, ext):
    _seed(
        conn,
        ext,
        [
            doc("t3_p", T - 50, kind="post", sub="pennystocks", title="$ABCD DD", permalink="/r/pennystocks/p"),
            doc("t1_c", T - 40, sub="wallstreetbets", body="$ABCD", permalink="/r/wallstreetbets/c"),
            doc("t1_old", T - 2 * DAY, sub="smallstreetbets", body="$ABCD"),
        ],
    )
    d = db.ticker_details(conn, as_of=T, ticker="ABCD")
    assert d["by_subreddit"] == {"pennystocks": 1, "wallstreetbets": 1}
    assert d["posts"] == 1 and d["comments"] == 1
    assert d["examples"] == ["https://www.reddit.com/r/pennystocks/p", "https://www.reddit.com/r/wallstreetbets/c"]


def test_daily_counts_cover_one_utc_day_for_every_ticker(conn, ext):
    day_start = 1_791_072_000  # 2026-10-04 00:00 UTC
    _seed(
        conn,
        ext,
        [
            doc("t3_p", day_start + 10, kind="post", sub="wallstreetbets", author="a", title="$ABCD 🚀 short squeeze"),
            doc("t1_1", day_start + 20, sub="pennystocks", author="b", body="$ABCD and $GME"),
            doc("t1_2", day_start + 86_399, sub="pennystocks", author="[deleted]", body="$GME"),
            doc("t1_3", day_start - 1, author="c", body="$ABCD"),  # previous day
            doc("t1_4", day_start + 86_400, author="d", body="$ABCD"),  # next day
        ],
    )
    rows = {r["ticker"]: r for r in db.daily_counts(conn, day_start)}
    assert set(rows) == {"ABCD", "GME"}
    assert rows["ABCD"] == {
        "date": "2026-10-04",
        "ticker": "ABCD",
        "mentions": 2,
        "authors": 2,
        "posts": 1,
        "comments": 1,
        "hype_docs": 1,
        "in_universe": 1,
        "by_subreddit": '{"pennystocks":1,"wallstreetbets":1}',
    }
    assert (rows["GME"]["mentions"], rows["GME"]["authors"]) == (2, 1)


def test_docs_table_has_no_columns_for_fields_the_source_never_fills():
    conn = db.connect(":memory:")
    cols = {row[1] for row in conn.execute("PRAGMA table_info(docs)")}
    assert not {"upvote_ratio", "removed_by_category"} & cols
