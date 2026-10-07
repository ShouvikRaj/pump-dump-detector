"""Keyless public market data of the exchanges the crypto track reads.

MEXC, Gate, KuCoin and Binance answer GitHub's US runners (checked 2026-10-07, run
37619315867): Binance's trading API refuses US addresses (451), but its market-data-only
mirror data-api.binance.vision and its bulk history files at data.binance.vision don't.

Bars everywhere are [open_time_ms, open, high, low, close, base_volume, quote_volume] in UTC.
"""

from __future__ import annotations

import csv
import io
import json
import time
import zipfile
from datetime import datetime, timezone
from typing import Callable

import requests

UA = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36"
MIN = 60_000
HOUR = 3_600_000

Bar = list  # [t_ms, o, h, l, c, v, qv]


class Http:
    """requests with per-host spacing and a few retries on network errors, 429s and 5xx."""

    def __init__(self, min_interval: float = 0.25, retries: int = 3, sleep: Callable[[float], None] = time.sleep):
        self.s = requests.Session()
        self.s.headers["User-Agent"] = UA
        self.min_interval = min_interval
        self.retries = retries
        self.sleep = sleep
        self._last: dict[str, float] = {}

    def get(self, url: str, params: dict | None = None, timeout: float = 30) -> tuple[int, bytes]:
        host = url.split("/")[2]
        for attempt in range(self.retries + 1):
            wait = self._last.get(host, 0) + self.min_interval - time.monotonic()
            if wait > 0:
                self.sleep(wait)
            self._last[host] = time.monotonic()
            try:
                r = self.s.get(url, params=params, timeout=timeout)
                status, body = r.status_code, r.content
            except requests.RequestException as exc:
                status, body = 0, str(exc).encode()
            if (status == 0 or status == 429 or status >= 500) and attempt < self.retries:
                self.sleep(2.0 * 2**attempt)
                continue
            return status, body
        return status, body

    def json(self, url: str, params: dict | None = None):
        status, body = self.get(url, params)
        if status != 200:
            raise ExchangeError(f"{url} -> {status} {body[:160]!r}")
        return json.loads(body)


class ExchangeError(RuntimeError):
    pass


def _f(x) -> float:
    return float(x) if x not in (None, "") else 0.0


class Exchange:
    name = ""
    quote = "USDT"

    def __init__(self, http: Http):
        self.http = http

    def tickers(self) -> list[dict]:
        """All USDT spot pairs: base, symbol (the exchange's own), high, low, last, quote_volume (24 h)."""
        raise NotImplementedError

    def klines(self, symbol: str, interval: str, start_ms: int, end_ms: int) -> list[Bar]:
        """Bars with open time in [start_ms, end_ms), interval '1m' or '1h', oldest first, paging as needed."""
        step = MIN if interval == "1m" else HOUR
        out: dict[int, Bar] = {}
        cursor = start_ms
        while cursor < end_ms:
            chunk = self._klines(symbol, interval, cursor, min(end_ms, cursor + self.page * step))
            for b in chunk:
                if start_ms <= b[0] < end_ms:
                    out[b[0]] = b
            cursor += self.page * step
        return [out[k] for k in sorted(out)]

    page = 500

    def _klines(self, symbol: str, interval: str, start_ms: int, end_ms: int) -> list[Bar]:
        raise NotImplementedError

    def symbol(self, base: str, quote: str = "USDT") -> str:
        raise NotImplementedError


class Mexc(Exchange):
    name = "mexc"
    base_url = "https://api.mexc.com"
    page = 500
    intervals = {"1m": "1m", "1h": "60m"}

    def symbol(self, base, quote="USDT"):
        return f"{base}{quote}"

    def tickers(self):
        out = []
        for t in self.http.json(f"{self.base_url}/api/v3/ticker/24hr"):
            sym = t.get("symbol", "")
            if sym.endswith("USDT"):
                out.append(dict(base=sym[:-4], symbol=sym, high=_f(t.get("highPrice")), low=_f(t.get("lowPrice")),
                                last=_f(t.get("lastPrice")), quote_volume=_f(t.get("quoteVolume"))))
        return out

    def _klines(self, symbol, interval, start_ms, end_ms):
        rows = self.http.json(f"{self.base_url}/api/v3/klines", dict(
            symbol=symbol, interval=self.intervals[interval], startTime=start_ms, endTime=end_ms - 1, limit=1000))
        return [[int(r[0]), _f(r[1]), _f(r[2]), _f(r[3]), _f(r[4]), _f(r[5]), _f(r[7])] for r in rows]


class BinanceData(Mexc):
    """Binance through its market-data-only mirror (same API shape as MEXC's, which copied Binance's)."""

    name = "binance"
    base_url = "https://data-api.binance.vision"
    intervals = {"1m": "1m", "1h": "1h"}

    def tickers(self):
        out = []
        for t in self.http.json(f"{self.base_url}/api/v3/ticker/24hr"):
            sym = t.get("symbol", "")
            if sym.endswith("USDT") and _f(t.get("quoteVolume")) > 0:
                out.append(dict(base=sym[:-4], symbol=sym, high=_f(t.get("highPrice")), low=_f(t.get("lowPrice")),
                                last=_f(t.get("lastPrice")), quote_volume=_f(t.get("quoteVolume"))))
        return out


class Gate(Exchange):
    name = "gate"
    base_url = "https://api.gateio.ws/api/v4"
    page = 900  # at most 1000 points per request

    def symbol(self, base, quote="USDT"):
        return f"{base}_{quote}"

    def tickers(self):
        out = []
        for t in self.http.json(f"{self.base_url}/spot/tickers"):
            pair = t.get("currency_pair", "")
            if pair.endswith("_USDT"):
                out.append(dict(base=pair[:-5], symbol=pair, high=_f(t.get("high_24h")), low=_f(t.get("low_24h")),
                                last=_f(t.get("last")), quote_volume=_f(t.get("quote_volume"))))
        return out

    def _klines(self, symbol, interval, start_ms, end_ms):
        try:
            rows = self.http.json(f"{self.base_url}/spot/candlesticks", {
                "currency_pair": symbol, "interval": interval, "from": start_ms // 1000, "to": (end_ms - 1) // 1000})
        except ExchangeError as exc:
            # Gate keeps only the last 10,000 points of each interval and says so with a 400
            if "400" in str(exc):
                return []
            raise
        # [t_s, quote_volume, close, high, low, open, base_volume, closed]
        return [[int(r[0]) * 1000, _f(r[5]), _f(r[3]), _f(r[4]), _f(r[2]), _f(r[6]), _f(r[1])] for r in rows]


class Kucoin(Exchange):
    name = "kucoin"
    base_url = "https://api.kucoin.com/api/v1"
    page = 1400  # at most 1500 per request
    intervals = {"1m": "1min", "1h": "1hour"}

    def symbol(self, base, quote="USDT"):
        return f"{base}-{quote}"

    def tickers(self):
        out = []
        for t in self.http.json(f"{self.base_url}/market/allTickers")["data"]["ticker"]:
            sym = t.get("symbol", "")
            if sym.endswith("-USDT"):
                out.append(dict(base=sym[:-5], symbol=sym, high=_f(t.get("high")), low=_f(t.get("low")),
                                last=_f(t.get("last")), quote_volume=_f(t.get("volValue"))))
        return out

    def _klines(self, symbol, interval, start_ms, end_ms):
        d = self.http.json(f"{self.base_url}/market/candles", {
            "type": self.intervals[interval], "symbol": symbol, "startAt": start_ms // 1000, "endAt": (end_ms - 1) // 1000})
        # [t_s, open, close, high, low, base_volume, quote_volume], newest first
        return [[int(r[0]) * 1000, _f(r[1]), _f(r[3]), _f(r[4]), _f(r[2]), _f(r[5]), _f(r[6])] for r in reversed(d.get("data") or [])]


LIVE = {"mexc": Mexc, "gate": Gate, "kucoin": Kucoin, "binance": BinanceData}


# ---- Binance bulk history (data.binance.vision) ------------------------------------------------------------

BULK = "https://data.binance.vision/data/spot"


def _bulk_rows(http: Http, url: str) -> list[Bar] | None:
    status, body = http.get(url)
    if status == 404:
        return None
    if status != 200:
        raise ExchangeError(f"{url} -> {status}")
    with zipfile.ZipFile(io.BytesIO(body)) as z:
        text = z.read(z.namelist()[0]).decode()
    out = []
    for r in csv.reader(io.StringIO(text)):
        if not r or not r[0].isdigit():
            continue
        t = int(r[0])
        if t > 10**14:  # files from 2025 on are in microseconds
            t //= 1000
        out.append([t, _f(r[1]), _f(r[2]), _f(r[3]), _f(r[4]), _f(r[5]), _f(r[7])])
    return out


class BinanceBulk:
    """Binance spot bars from the public bulk files: daily 1m files, monthly 1h files (cached per file)."""

    name = "binance"

    def __init__(self, http: Http):
        self.http = http
        self.cache: dict[str, list[Bar] | None] = {}

    def symbol(self, base, quote="BTC"):
        return f"{base}{quote}"

    def _file(self, symbol: str, interval: str, period: str) -> list[Bar]:
        kind = "daily" if interval == "1m" else "monthly"
        url = f"{BULK}/{kind}/klines/{symbol}/{interval}/{symbol}-{interval}-{period}.zip"
        if url not in self.cache:
            self.cache[url] = _bulk_rows(self.http, url)
        return self.cache[url] or []

    def klines(self, symbol: str, interval: str, start_ms: int, end_ms: int) -> list[Bar]:
        step = 86_400_000 if interval == "1m" else None
        periods = []
        t = start_ms
        while t < end_ms:
            d = datetime.fromtimestamp(t / 1000, timezone.utc)
            if step:
                periods.append(d.strftime("%Y-%m-%d"))
                t = (t // step + 1) * step
            else:
                periods.append(d.strftime("%Y-%m"))
                t = int(datetime(d.year + (d.month == 12), d.month % 12 + 1, 1, tzinfo=timezone.utc).timestamp() * 1000)
        out = {}
        for p in dict.fromkeys(periods):
            for b in self._file(symbol, interval, p):
                if start_ms <= b[0] < end_ms:
                    out[b[0]] = b
        return [out[k] for k in sorted(out)]
