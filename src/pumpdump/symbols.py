"""US ticker universe used to validate bare-word mentions.

Sources (both free, no key):
  * Nasdaq Trader symbol directory: every Nasdaq / NYSE / NYSE American /
    NYSE Arca / Cboe / IEX listing, with an ETF flag.
  * SEC company_tickers_exchange.json: adds OTC issuers that file with the SEC
    and their CIK (needed for EDGAR filing checks in Stage 2). Fetched only when
    the SEC_USER_AGENT secret names a contact (see sec_contact).
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
from urllib.parse import urlparse

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


USER_AGENT = "pump-dump-detector/0.1 (research; +https://github.com/ShouvikRaj/pump-dump-detector)"


def sec_contact() -> str | None:
    """User-Agent for sec.gov from the SEC_USER_AGENT secret ("pump-dump-detector you@example.com").

    sec.gov refuses requests whose User-Agent doesn't name a reachable contact, and GitHub no-reply
    addresses don't count (checked from GitHub Actions, 2026-10-05). The secret keeps the address
    out of the public code and logs, and it is sent to sec.gov only.
    """
    ua = os.environ.get("SEC_USER_AGENT", "").strip()
    return ua if "@" in ua else None


def http_fetch_text(url: str, timeout: float = 60) -> str:
    import requests

    ua = USER_AGENT
    host = urlparse(url).hostname or ""
    if host == "sec.gov" or host.endswith(".sec.gov"):
        ua = sec_contact() or USER_AGENT
    resp = requests.get(url, headers={"User-Agent": ua, "Accept-Encoding": "gzip, deflate"}, timeout=timeout)
    if resp.status_code >= 400:
        raise RuntimeError(f"HTTP {resp.status_code} for {url}: {_page_summary(resp.text)}")
    return resp.text


def _page_summary(text: str, limit: int = 160) -> str:
    """The <title> of an error page (or its first words), which says why a server refused."""
    m = re.search(r"<title[^>]*>(.*?)</title>", text, re.I | re.S)
    plain = m.group(1) if m else re.sub(r"<[^>]+>", " ", text)
    return " ".join(plain.split())[:limit]


def refresh_symbols(fetch: Callable[[str], str] = http_fetch_text) -> tuple[dict[str, dict], list[str]]:
    errors: list[str] = []
    listed: list[dict] = []
    sec: list[dict] = []
    for url, parse in ((NASDAQ_LISTED_URL, parse_nasdaq_listed), (OTHER_LISTED_URL, parse_other_listed)):
        try:
            listed += parse(fetch(url))
        except Exception as exc:  # one bad source must not stop collection
            errors.append(f"{url}: {exc}")
    if sec_contact() is None:
        errors.append(
            f"{SEC_TICKERS_URL}: skipped, SEC refuses requests without a contact email; "
            "set the SEC_USER_AGENT secret (e.g. 'pump-dump-detector you@example.com')"
        )
    else:
        try:
            sec = parse_sec_tickers(json.loads(fetch(SEC_TICKERS_URL)))
        except Exception as exc:
            errors.append(f"{SEC_TICKERS_URL}: {exc}")
    return merge_symbols(listed, sec), errors


def save_symbols(ds: Datastore, symbols: dict[str, dict]) -> None:
    ds.write_csv(SYMBOLS_FILE, FIELDS, (symbols[s] for s in sorted(symbols)))


def load_symbols(ds: Datastore) -> dict[str, dict]:
    return {r["symbol"]: r for r in ds.read_csv(SYMBOLS_FILE)}
