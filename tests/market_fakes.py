"""Test doubles for Stage 2: a scripted HTTP transport and builders for source payloads."""

from __future__ import annotations

import json


class FakeHTTP:
    """Answers requests from `routes`: (method, url_prefix, [(status, text), ...]).

    Responses for a route are used in order; the last one repeats. Every call is
    recorded in `calls`, so tests can check what was asked.
    """

    def __init__(self, routes=()):
        self.routes = [(m, prefix, list(responses)) for m, prefix, responses in routes]
        self.calls: list[dict] = []

    def add(self, method, prefix, *responses):
        self.routes.insert(0, (method, prefix, list(responses)))

    def __call__(self, method, url, params=None, headers=None, json=None, timeout=30):
        self.calls.append({"method": method, "url": url, "params": params, "headers": headers, "json": json})
        for m, prefix, responses in self.routes:
            if m == method and url.startswith(prefix):
                return responses.pop(0) if len(responses) > 1 else responses[0]
        return 404, '{"error": "no route"}'

    def urls(self, prefix=""):
        return [c["url"] for c in self.calls if c["url"].startswith(prefix)]


class FakeClock:
    def __init__(self, start: float = 1_791_200_000.0):
        self.now = start
        self.sleeps: list[float] = []

    def time(self) -> float:
        return self.now

    def sleep(self, seconds: float) -> None:
        self.sleeps.append(seconds)
        self.now += seconds


def chart_json(bars, splits=(), exchange="NCM", full_exchange="NasdaqCM", first_trade=1_615_213_800, name="Test Co"):
    """A Yahoo chart response. bars: (t, open, high, low, close, volume); None values are allowed."""
    result = {
        "meta": {
            "currency": "USD",
            "symbol": "TEST",
            "exchangeName": exchange,
            "fullExchangeName": full_exchange,
            "instrumentType": "EQUITY",
            "firstTradeDate": first_trade,
            "regularMarketPrice": bars[-1][4] if bars else None,
            "regularMarketTime": bars[-1][0] if bars else None,
            "timezone": "EDT",
            "longName": name,
        },
        "indicators": {"quote": [{"open": [], "high": [], "low": [], "close": [], "volume": []}]},
    }
    if bars:
        result["timestamp"] = [b[0] for b in bars]
        q = result["indicators"]["quote"][0]
        for i, key in enumerate(["open", "high", "low", "close", "volume"], start=1):
            q[key] = [b[i] for b in bars]
    if splits:
        result["events"] = {
            "splits": {str(t): {"date": t, "numerator": n, "denominator": d, "splitRatio": f"{n:g}:{d:g}"} for t, n, d in splits}
        }
    return json.dumps({"chart": {"result": [result], "error": None}})


CHART_404 = json.dumps({"chart": {"result": None, "error": {"code": "Not Found", "description": "No data found, symbol may be delisted"}}})


def summary_json(**fields):
    """A quoteSummary response; fields are placed in the module Yahoo uses for them."""
    modules = {"price": {}, "summaryDetail": {}, "defaultKeyStatistics": {}, "summaryProfile": {}}
    where = {
        "exchange": "price", "exchangeName": "price", "quoteType": "price", "longName": "price", "marketCap": "price",
        "averageVolume": "summaryDetail", "sector": "summaryProfile", "industry": "summaryProfile", "country": "summaryProfile",
    }
    for key, value in fields.items():
        module = where.get(key, "defaultKeyStatistics")
        wrapped = value if isinstance(value, str) or value is None else {"raw": value, "fmt": str(value)}
        modules[module][key] = wrapped if value is not None else {}
    return json.dumps({"quoteSummary": {"result": [modules], "error": None}})


def submissions_json(filings, name="Test Co", former_names=(), category="Non-accelerated filer<br>Smaller reporting company"):
    """filings: (form, filingDate, acceptanceDateTime, items)."""
    return json.dumps(
        {
            "cik": "0000000001",
            "name": name,
            "sic": "2834",
            "sicDescription": "Pharmaceutical Preparations",
            "category": category,
            "stateOfIncorporation": "NV",
            "formerNames": [{"name": n, "from": f, "to": t} for n, f, t in former_names],
            "tickers": ["TEST"],
            "exchanges": ["OTC"],
            "filings": {
                "recent": {
                    "form": [f[0] for f in filings],
                    "filingDate": [f[1] for f in filings],
                    "acceptanceDateTime": [f[2] for f in filings],
                    "items": [f[3] for f in filings],
                    "accessionNumber": [f"0000000001-26-{i:06d}" for i in range(len(filings))],
                    "primaryDocument": ["doc.htm"] * len(filings),
                },
                "files": [],
            },
        }
    )


def shares_json(facts):
    """facts: (end, val, filed, form)."""
    return json.dumps(
        {
            "cik": 1,
            "taxonomy": "dei",
            "tag": "EntityCommonStockSharesOutstanding",
            "units": {"shares": [{"end": e, "val": v, "filed": f, "form": form, "accn": "x"} for e, v, f, form in facts]},
        }
    )


def finra_json(rows):
    """rows: (settlementDate, current, previous, days_to_cover)."""
    return json.dumps(
        [
            {
                "settlementDate": d,
                "symbolCode": "TEST",
                "currentShortPositionQuantity": cur,
                "previousShortPositionQuantity": prev,
                "daysToCoverQuantity": dtc,
                "averageDailyVolumeQuantity": 1000,
                "marketClassCode": "SC",
            }
            for d, cur, prev, dtc in rows
        ]
    )


def screener_rows_json(rows):
    """rows: (symbol, lastsale, volume, marketCap)."""
    return json.dumps(
        {
            "data": {
                "asOf": None,
                "headers": {},
                "rows": [
                    {
                        "symbol": s,
                        "name": f"{s} Inc.",
                        "lastsale": f"${p}",
                        "netchange": "0.10",
                        "pctchange": "1.5%",
                        "volume": str(v),
                        "marketCap": f"{cap}.00",
                        "country": "United States",
                        "ipoyear": "",
                        "industry": "Biotechnology",
                        "sector": "Health Care",
                        "url": f"/market-activity/stocks/{s.lower()}",
                    }
                    for s, p, v, cap in rows
                ],
            }
        }
    )


SCREENER_ASOF = json.dumps({"data": {"table": {"rows": []}, "totalrecords": 7000, "asof": "Last price as of Oct 1, 2026"}})


def session_bars(last, n=30, close=4.0, volume=100_000, step=0.0):
    """Daily bars (09:30 ET stamps) for the n weekdays ending at date `last`."""
    from datetime import datetime, timedelta
    from zoneinfo import ZoneInfo

    et = ZoneInfo("America/New_York")
    days, d = [], last
    while len(days) < n:
        if d.weekday() < 5:
            days.append(d)
        d -= timedelta(days=1)
    bars = []
    for i, d in enumerate(reversed(days)):
        c = round(close + step * (i - n + 1), 4)
        bars.append((datetime(d.year, d.month, d.day, 9, 30, tzinfo=et).timestamp(), c, c * 1.02, c * 0.98, c, volume))
    return bars


class MarketWorld:
    """Every Stage 2 source behind one fake transport, answering per symbol/CIK.

    Unknown symbols get Yahoo's 404; hosts in `down` answer 503.
    """

    def __init__(self):
        self.daily: dict[str, list] = {}
        self.intraday: dict[str, list] = {}
        self.summaries: dict[str, dict] = {}
        self.submissions: dict[int, str] = {}
        self.shares: dict[int, str] = {}
        self.short: dict[str, list] = {}
        self.universe: list = []
        self.universe_label = "Last price as of Oct 1, 2026"
        self.down: set[str] = set()
        self.calls: list[dict] = []

    def add_stock(self, sym, bars, summary=None, intraday=(), short=()):
        self.daily[sym] = list(bars)
        self.intraday[sym] = list(intraday)
        self.summaries[sym] = summary or {}
        self.short[sym] = list(short)

    def __call__(self, method, url, params=None, headers=None, json=None, timeout=30):
        from urllib.parse import urlparse

        self.calls.append({"method": method, "url": url, "params": params, "headers": headers, "json": json})
        u = urlparse(url)
        if u.hostname in self.down:
            return 503, "<html>down</html>"
        path = u.path
        if u.hostname == "fc.yahoo.com":
            return 404, ""
        if path == "/v1/test/getcrumb":
            return 200, "crumb1"
        if path.startswith("/v8/finance/chart/"):
            sym = path.rsplit("/", 1)[1]
            if sym not in self.daily:
                return 404, CHART_404
            p1, p2 = params["period1"], params["period2"]
            bars = self.daily[sym] if params["interval"] == "1d" else self.intraday[sym]
            return 200, chart_json([b for b in bars if p1 <= b[0] <= p2], exchange=self.summaries[sym].get("exchange", "NCM"),
                                   full_exchange=self.summaries[sym].get("exchangeName", "NasdaqCM"))
        if path.startswith("/v10/finance/quoteSummary/"):
            sym = path.rsplit("/", 1)[1]
            if sym not in self.summaries:
                return 404, '{"quoteSummary":{"result":null,"error":{"code":"Not Found","description":"Quote not found"}}}'
            return 200, summary_json(**self.summaries[sym])
        if path.startswith("/submissions/CIK"):
            cik = int(path[len("/submissions/CIK"):-5])
            return (200, self.submissions[cik]) if cik in self.submissions else (404, "<Error>NoSuchKey</Error>")
        if path.startswith("/api/xbrl/companyconcept/CIK"):
            cik = int(path.split("CIK")[1][:10])
            return (200, self.shares[cik]) if cik in self.shares else (404, "<Error>NoSuchKey</Error>")
        if u.hostname == "api.finra.org":
            sym = json["compareFilters"][0]["fieldValue"]
            return 200, finra_json(self.short.get(sym, []))
        if path == "/api/screener/stocks":
            if params.get("download") == "true":
                return 200, screener_rows_json(self.universe)
            import json as _json

            return 200, _json.dumps({"data": {"asof": self.universe_label}})
        return 404, "no route"

    def symbols_asked(self, kind="chart"):
        prefix = {"chart": "/v8/finance/chart/", "summary": "/v10/finance/quoteSummary/"}[kind]
        from urllib.parse import urlparse

        return [urlparse(c["url"]).path.rsplit("/", 1)[1] for c in self.calls if urlparse(c["url"]).path.startswith(prefix)]
