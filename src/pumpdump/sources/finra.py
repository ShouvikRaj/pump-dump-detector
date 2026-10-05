"""FINRA consolidated short interest: twice-monthly short positions for listed and OTC stocks.

FINRA's query API serves this dataset without a key (checked from GitHub's
runners, 2026-10-05). Data covers a rolling year of settlement dates.
"""

from __future__ import annotations

import json

from .web import BROWSER_UA, Web, short_text

SHORT_INTEREST_URL = "https://api.finra.org/data/group/otcMarket/name/consolidatedShortInterest"
KEEP = ("settlementDate", "currentShortPositionQuantity", "previousShortPositionQuantity", "daysToCoverQuantity",
        "averageDailyVolumeQuantity", "marketClassCode")


class FinraError(Exception):
    pass


def short_interest(web: Web, ticker: str, start: str, end: str) -> list[dict]:
    """Rows for `ticker` with settlement dates in [start, end] (YYYY-MM-DD), oldest first."""
    body = {
        "limit": 50,
        "compareFilters": [{"compareType": "equal", "fieldName": "symbolCode", "fieldValue": ticker}],
        "dateRangeFilters": [{"fieldName": "settlementDate", "startDate": start, "endDate": end}],
    }
    status, text = web.fetch(
        SHORT_INTEREST_URL, method="POST", json_body=body, headers={"User-Agent": BROWSER_UA, "Accept": "application/json"}
    )
    if status == 204 or (status == 200 and not text.strip()):
        return []
    if status != 200:
        raise FinraError(f"short interest HTTP {status}: {short_text(text)}")
    rows = json.loads(text) or []
    return sorted(({k: r.get(k) for k in KEEP} for r in rows), key=lambda r: r["settlementDate"] or "")
