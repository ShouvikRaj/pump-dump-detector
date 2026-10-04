"""US ticker universe used to validate bare-word mentions.

Sources (both free, no key):
  * Nasdaq Trader symbol directory: every Nasdaq / NYSE / NYSE American /
    NYSE Arca / Cboe / IEX listing, with an ETF flag.
  * SEC company_tickers_exchange.json: adds OTC issuers that file with the SEC
    and their CIK (needed for EDGAR filing checks in Stage 2).
Non-reporting OTC pinks are in neither list; the extractor still counts them
when written as $CASHTAG or "OTC: XXXX".

The merged list is saved to ref/symbols.csv in the datastore; git history of
that file gives the universe as of any date.
"""

from __future__ import annotations

import json
import os
import re
from typing import Callable

from .store import Datastore

NASDAQ_LISTED_URL = "https://www.nasdaqtrader.com/dynamic/SymDir/nasdaqlisted.txt"
OTHER_LISTED_URL = "https://www.nasdaqtrader.com/dynamic/SymDir/otherlisted.txt"
SEC_TICKERS_URL = "https://www.sec.gov/files/company_tickers_exchange.json"
SYMBOLS_FILE = "ref/symbols.csv"
FIELDS = ["symbol", "name", "exchange", "is_etf", "cik", "source"]

_OTHER_EXCHANGES = {"A": "NYSE American", "N": "NYSE", "P": "NYSE Arca", "Z": "Cboe BZX", "V": "IEX"}
_VALID = re.compile(r"^[A-Z]{1,5}(?:\.[A-Z]{1,2})?$")


def _rows(text: str) -> list[list[str]]:
    lines = [ln for ln in text.splitlines() if ln.strip() and not ln.startswith("File Creation Time")]
    return [ln.split("|") for ln in lines[1:]]


def parse_nasdaq_listed(text: str) -> list[dict]:
    out = []
    for cols in _rows(text):
        sym, name, test_issue, etf = cols[0].strip(), cols[1].strip(), cols[3].strip(), cols[6].strip()
        if test_issue == "Y" or not _VALID.match(sym):
            continue
        out.append({"symbol": sym, "name": name, "exchange": "Nasdaq", "is_etf": int(etf == "Y"), "cik": None})
    return out


def parse_other_listed(text: str) -> list[dict]:
    out = []
    for cols in _rows(text):
        sym, name, exch, etf, test_issue = (c.strip() for c in (cols[0], cols[1], cols[2], cols[4], cols[6]))
        if test_issue == "Y" or not _VALID.match(sym):
            continue
        out.append(
            {"symbol": sym, "name": name, "exchange": _OTHER_EXCHANGES.get(exch, exch), "is_etf": int(etf == "Y"), "cik": None}
        )
    return out


def parse_sec_tickers(obj: dict) -> list[dict]:
    idx = {name: i for i, name in enumerate(obj["fields"])}
    out = []
    for row in obj["data"]:
        sym = str(row[idx["ticker"]]).upper().replace("-", ".")
        if not _VALID.match(sym):
            continue
        out.append(
            {
                "symbol": sym,
                "name": row[idx["name"]],
                "exchange": row[idx["exchange"]] or "",
                "is_etf": 0,
                "cik": row[idx["cik"]],
            }
        )
    return out


def merge_symbols(listed: list[dict], sec: list[dict]) -> dict[str, dict]:
    merged: dict[str, dict] = {}
    for r in listed:
        merged.setdefault(r["symbol"], {**r, "source": "nasdaqtrader"})
    for r in sec:
        if r["symbol"] in merged:
            m = merged[r["symbol"]]
            m["cik"] = r["cik"]
            m["source"] = "both"
        else:
            merged[r["symbol"]] = {**r, "source": "sec"}
    return merged


def http_fetch_text(url: str, timeout: float = 60) -> str:
    import requests

    ua = os.environ.get("SEC_USER_AGENT") or "pump-dump-detector/0.1 (research; +https://github.com/ShouvikRaj/pump-dump-detector)"
    resp = requests.get(url, headers={"User-Agent": ua, "Accept-Encoding": "gzip, deflate"}, timeout=timeout)
    resp.raise_for_status()
    return resp.text


def refresh_symbols(fetch: Callable[[str], str] = http_fetch_text) -> tuple[dict[str, dict], list[str]]:
    errors: list[str] = []
    listed: list[dict] = []
    sec: list[dict] = []
    for url, parse in ((NASDAQ_LISTED_URL, parse_nasdaq_listed), (OTHER_LISTED_URL, parse_other_listed)):
        try:
            listed += parse(fetch(url))
        except Exception as exc:  # one bad source must not stop collection
            errors.append(f"{url}: {exc}")
    try:
        sec = parse_sec_tickers(json.loads(fetch(SEC_TICKERS_URL)))
    except Exception as exc:
        errors.append(f"{SEC_TICKERS_URL}: {exc}")
    return merge_symbols(listed, sec), errors


def save_symbols(ds: Datastore, symbols: dict[str, dict]) -> None:
    ds.write_csv(SYMBOLS_FILE, FIELDS, (symbols[s] for s in sorted(symbols)))


def load_symbols(ds: Datastore) -> dict[str, dict]:
    return {r["symbol"]: r for r in ds.read_csv(SYMBOLS_FILE)}
