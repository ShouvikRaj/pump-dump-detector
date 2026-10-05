"""Yahoo Finance: price bars (chart API) and share/float figures (quoteSummary).

Both answer plain requests from GitHub's runners when they carry a browser
User-Agent (checked 2026-10-05). quoteSummary also needs a "crumb", fetched
with the cookie that fc.yahoo.com sets. Prices are split-adjusted as served.
quoteSummary values are current, not historical: a snapshot records when it
fetched them.
"""

from __future__ import annotations

import json

from .web import BROWSER_UA, Web, short_text

CHART_URL = "https://query1.finance.yahoo.com/v8/finance/chart/{}"
SUMMARY_URL = "https://query2.finance.yahoo.com/v10/finance/quoteSummary/{}"
COOKIE_URL = "https://fc.yahoo.com"
CRUMB_URL = "https://query2.finance.yahoo.com/v1/test/getcrumb"
HEADERS = {"User-Agent": BROWSER_UA, "Accept": "application/json"}

META_KEYS = ("exchangeName", "fullExchangeName", "instrumentType", "currency", "firstTradeDate", "timezone",
             "regularMarketPrice", "regularMarketTime", "longName", "shortName")
SUMMARY_FIELDS = {
    "price": ("exchange", "exchangeName", "quoteType", "longName", "shortName", "marketCap", "regularMarketPrice"),
    "summaryDetail": ("averageVolume", "averageVolume10days"),
    "defaultKeyStatistics": ("floatShares", "sharesOutstanding", "impliedSharesOutstanding", "heldPercentInsiders",
                             "heldPercentInstitutions", "sharesShort", "dateShortInterest", "lastSplitDate",
                             "lastSplitFactor"),
    "summaryProfile": ("sector", "industry", "country"),
}


class NoData(Exception):
    """Yahoo has nothing for this symbol (unknown, or delisted long ago)."""


class SourceError(Exception):
    """Yahoo failed in a way that may pass (network, rate limit, server error)."""


def yahoo_symbol(ticker: str) -> str:
    return ticker.replace(".", "-")  # BRK.B -> BRK-B


def _json(text: str):
    try:
        return json.loads(text)
    except ValueError:
        return None


def _not_found(status: int, body, key: str) -> str | None:
    err = ((body or {}).get(key) or {}).get("error") if isinstance(body, dict) else None
    if status == 404 or (isinstance(err, dict) and err.get("code") == "Not Found"):
        return (err or {}).get("description") or "not found"
    return None


def parse_chart(result: dict) -> dict:
    q = (result.get("indicators", {}).get("quote") or [{}])[0]
    bars = []
    for i, t in enumerate(result.get("timestamp") or []):
        row = [q.get(k, [None] * (i + 1))[i] for k in ("open", "high", "low", "close", "volume")]
        if row[3] is None:
            continue  # Yahoo leaves gaps as nulls
        bars.append([t] + row)
    splits = sorted(
        ({"t": s["date"], "numerator": float(s["numerator"]), "denominator": float(s["denominator"])}
         for s in ((result.get("events") or {}).get("splits") or {}).values()),
        key=lambda s: s["t"],
    )
    meta = result.get("meta") or {}
    return {"meta": {k: meta.get(k) for k in META_KEYS}, "bars": bars, "splits": splits}


def _raw(value):
    if isinstance(value, dict):
        return value.get("raw")  # {} (missing) -> None
    return value


class Yahoo:
    def __init__(self, web: Web) -> None:
        self.web = web
        self._crumb: str | None = None

    def chart(self, ticker: str, period1: float, period2: float, interval: str = "1d", prepost: bool = False) -> dict:
        params = {"period1": int(period1), "period2": int(period2), "interval": interval,
                  "includePrePost": "true" if prepost else "false", "events": "div,splits"}
        status, text = self.web.fetch(CHART_URL.format(yahoo_symbol(ticker)), params=params, headers=HEADERS)
        body = _json(text)
        missing = _not_found(status, body, "chart")
        if missing:
            raise NoData(missing)
        result = ((body or {}).get("chart") or {}).get("result") if isinstance(body, dict) else None
        if status != 200 or not result:
            raise SourceError(f"chart HTTP {status}: {short_text(text)}")
        return parse_chart(result[0])

    def _get_crumb(self) -> str:
        if self._crumb is None:
            self.web.fetch(COOKIE_URL, headers={"User-Agent": BROWSER_UA})  # 404, but sets the cookie
            status, text = self.web.fetch(CRUMB_URL, headers={"User-Agent": BROWSER_UA})
            crumb = text.strip()
            if status != 200 or not crumb or "<" in crumb or " " in crumb:
                raise SourceError(f"crumb HTTP {status}: {short_text(text)}")
            self._crumb = crumb
        return self._crumb

    def summary(self, ticker: str) -> dict:
        modules = ",".join(SUMMARY_FIELDS)
        for attempt in range(2):
            params = {"modules": modules, "crumb": self._get_crumb()}
            status, text = self.web.fetch(SUMMARY_URL.format(yahoo_symbol(ticker)), params=params, headers=HEADERS)
            if status == 401 and attempt == 0:
                self._crumb = None  # expired; get a new one once
                continue
            break
        body = _json(text)
        missing = _not_found(status, body, "quoteSummary")
        if missing:
            raise NoData(missing)
        result = ((body or {}).get("quoteSummary") or {}).get("result") if isinstance(body, dict) else None
        if status != 200 or not result:
            raise SourceError(f"quoteSummary HTTP {status}: {short_text(text)}")
        modules_data = result[0]
        return {key: _raw((modules_data.get(module) or {}).get(key)) for module, keys in SUMMARY_FIELDS.items() for key in keys}
