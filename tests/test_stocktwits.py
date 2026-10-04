from pumpdump.sources.stocktwits import parse_trending

TRENDING = {
    "response": {"status": 200},
    "symbols": [
        {"id": 1, "symbol": "ADA.X", "title": "Cardano", "watchlist_count": 131531, "exchange": "CRYPTO"},
        {"id": 2, "symbol": "UNG", "title": "US Natural Gas Fund", "watchlist_count": 17694, "exchange": "NYSEArca"},
        {"id": 3, "symbol": "ABBV", "title": "Abbvie Inc", "watchlist_count": 32889},
    ],
}


def test_parse_trending_keeps_rank_and_marks_crypto():
    rows = parse_trending(TRENDING, collected_at=1000.5)
    assert [(r["rank"], r["symbol"], r["is_crypto"]) for r in rows] == [(1, "ADA.X", 1), (2, "UNG", 0), (3, "ABBV", 0)]
    assert rows[1]["exchange"] == "NYSEArca"
    assert rows[2]["exchange"] == ""
    assert rows[0]["collected_at"] == 1000.5
    assert rows[0]["watchlist_count"] == 131531


def test_parse_trending_tolerates_missing_symbols_list():
    assert parse_trending({"response": {"status": 200}}, collected_at=1.0) == []
