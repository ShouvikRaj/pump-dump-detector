"""Nasdaq's stock screener: last price, volume and market cap of every listed US stock.

One request returns all ~7,000 Nasdaq/NYSE/NYSE American stocks (no ETFs, no
OTC). Its prices lag by a session or two; the "Last price as of <date>" label
from a second, one-row request says which session they are from.
"""

from __future__ import annotations

import json
import re
from datetime import datetime

from .web import BROWSER_UA, Web, short_text

SCREENER_URL = "https://api.nasdaq.com/api/screener/stocks"
HEADERS = {"User-Agent": BROWSER_UA, "Accept": "application/json, text/plain, */*",
           "Origin": "https://www.nasdaq.com", "Referer": "https://www.nasdaq.com/"}
FIELDS = ["symbol", "name", "last_sale", "pct_change", "volume", "market_cap", "country", "ipo_year", "sector", "industry"]
_ASOF = re.compile(r"as of ([A-Za-z]{3})[a-z]* (\d{1,2}), (\d{4})")


class NasdaqError(Exception):
    pass


def _number(text, cast=float):
    s = str(text or "").replace("$", "").replace(",", "").replace("%", "").strip()
    try:
        return cast(float(s))
    except ValueError:
        return None


def _get(web: Web, params: dict) -> dict:
    status, text = web.fetch(SCREENER_URL, params=params, headers=HEADERS)
    if status != 200:
        raise NasdaqError(f"screener HTTP {status}: {short_text(text)}")
    return json.loads(text).get("data") or {}


def listed_universe(web: Web) -> tuple[str | None, list[dict]]:
    """(price date YYYY-MM-DD or None, one row per listed stock)."""
    label = str(_get(web, {"tableonly": "true", "limit": "1", "offset": "0"}).get("asof") or "")
    m = _ASOF.search(label)
    asof = datetime.strptime(" ".join(m.groups()), "%b %d %Y").date().isoformat() if m else None
    rows = []
    for r in _get(web, {"tableonly": "true", "download": "true"}).get("rows") or []:
        rows.append(
            {
                "symbol": r.get("symbol", "").strip(),
                "name": r.get("name", "").strip(),
                "last_sale": _number(r.get("lastsale")),
                "pct_change": _number(r.get("pctchange")),
                "volume": _number(r.get("volume"), int),
                "market_cap": _number(r.get("marketCap"), int),
                "country": r.get("country", ""),
                "ipo_year": r.get("ipoyear", ""),
                "sector": r.get("sector", ""),
                "industry": r.get("industry", ""),
            }
        )
    return asof, rows
