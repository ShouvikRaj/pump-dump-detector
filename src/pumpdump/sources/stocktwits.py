"""StockTwits trending symbols (optional, public endpoint, no key).

One request per run gives StockTwits' current top-30 trending list, a second
independent hype signal next to Reddit mentions. Failures are logged and
ignored: StockTwits is not needed for Stage 1 to work.
"""

from __future__ import annotations

import requests

TRENDING_URL = "https://api.stocktwits.com/api/2/trending/symbols.json"
FIELDS = ["collected_at", "rank", "symbol", "title", "exchange", "watchlist_count", "is_crypto"]


def parse_trending(obj: dict, collected_at: float) -> list[dict]:
    rows = []
    for rank, s in enumerate(obj.get("symbols") or [], start=1):
        symbol = str(s.get("symbol", ""))
        rows.append(
            {
                "collected_at": collected_at,
                "rank": rank,
                "symbol": symbol,
                "title": s.get("title", ""),
                "exchange": s.get("exchange") or "",
                "watchlist_count": s.get("watchlist_count"),
                "is_crypto": int(symbol.endswith(".X")),
            }
        )
    return rows


def fetch_trending(clock, timeout: float = 30) -> list[dict]:
    resp = requests.get(
        TRENDING_URL,
        headers={"User-Agent": "Mozilla/5.0 (compatible; pump-dump-detector/0.1; research)", "Accept": "application/json"},
        timeout=timeout,
    )
    resp.raise_for_status()
    return parse_trending(resp.json(), collected_at=clock())
