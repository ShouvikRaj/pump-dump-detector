import re

import requests

from pumpdump.store import Datastore
from pumpdump.symbols import (
    SEC_TICKERS_URL,
    http_fetch_text,
    load_symbols,
    merge_symbols,
    parse_nasdaq_listed,
    parse_other_listed,
    parse_sec_tickers,
    refresh_symbols,
    save_symbols,
)

NASDAQ_LISTED = """Symbol|Security Name|Market Category|Test Issue|Financial Status|Round Lot Size|ETF|NextShares
AAAP|Pacer Barings CLO Market Flex ETF|G|N|N|100|Y|N
AACG|ATA Creativity Global - American Depositary Shares, each representing two common shares|S|N|N|100|N|N
ZXZZT|NASDAQ TEST STOCK|G|Y|N|100|N|N
File Creation Time: 1004202616:00|||||||
"""

OTHER_LISTED = """ACT Symbol|Security Name|Exchange|CQS Symbol|ETF|Round Lot Size|Test Issue|NASDAQ Symbol
A|Agilent Technologies, Inc. Common Stock|N|A|N|100|N|A
ABR$D|Arbor Realty Trust 6.375% Series D Cumulative Redeemable Preferred Stock|N|ABRpD|N|100|N|ABR-D
BRK.B|Berkshire Hathaway Inc. Class B|N|BRK.B|N|100|N|BRK/B
SPY|SPDR S&P 500 ETF Trust|P|SPY|Y|100|N|SPY
ZTST|Test Issue|A|ZTST|N|100|Y|ZTST
File Creation Time: 1004202616:00|||||||
"""

SEC = {
    "fields": ["cik", "name", "ticker", "exchange"],
    "data": [
        [1067983, "BERKSHIRE HATHAWAY INC", "BRK-B", "NYSE"],
        [2070829, "Contemporary Amperex Technology Co., Limited/ADR", "CYATY", "OTC"],
        [90000, "Agilent Technologies", "A", "NYSE"],
        [12345, "No exchange corp", "NOEX", None],
    ],
}


def test_parse_nasdaq_listed_skips_test_issues_and_footer():
    rows = parse_nasdaq_listed(NASDAQ_LISTED)
    assert [(r["symbol"], r["exchange"], r["is_etf"]) for r in rows] == [
        ("AAAP", "Nasdaq", 1),
        ("AACG", "Nasdaq", 0),
    ]


def test_parse_other_listed_maps_exchange_codes_and_skips_preferreds():
    rows = parse_other_listed(OTHER_LISTED)
    assert [(r["symbol"], r["exchange"], r["is_etf"]) for r in rows] == [
        ("A", "NYSE", 0),
        ("BRK.B", "NYSE", 0),
        ("SPY", "NYSE Arca", 1),
    ]


def test_parse_sec_normalises_class_shares():
    rows = parse_sec_tickers(SEC)
    assert [(r["symbol"], r["exchange"], r["cik"]) for r in rows] == [
        ("BRK.B", "NYSE", 1067983),
        ("CYATY", "OTC", 2070829),
        ("A", "NYSE", 90000),
        ("NOEX", "", 12345),
    ]


def test_merge_prefers_exchange_lists_and_keeps_sec_cik():
    merged = merge_symbols(parse_nasdaq_listed(NASDAQ_LISTED) + parse_other_listed(OTHER_LISTED), parse_sec_tickers(SEC))
    assert merged["BRK.B"]["exchange"] == "NYSE"
    assert merged["BRK.B"]["cik"] == 1067983
    assert merged["BRK.B"]["source"] == "both"
    assert merged["CYATY"]["source"] == "sec"
    assert merged["SPY"]["source"] == "nasdaqtrader"
    assert len(merged) == 7


def test_refresh_survives_one_failed_source(tmp_path):
    def fetch(url):
        if "sec.gov" in url:
            raise RuntimeError("403 Forbidden")
        return NASDAQ_LISTED if "nasdaqlisted" in url else OTHER_LISTED

    symbols, errors = refresh_symbols(fetch)
    assert set(symbols) == {"AAAP", "AACG", "A", "BRK.B", "SPY"}
    assert len(errors) == 1 and "sec.gov" in errors[0]


def test_save_and_load_roundtrip(tmp_path):
    ds = Datastore(tmp_path)
    merged = merge_symbols(parse_other_listed(OTHER_LISTED), parse_sec_tickers(SEC))
    save_symbols(ds, merged)
    loaded = load_symbols(ds)
    assert loaded["CYATY"]["exchange"] == "OTC"
    assert loaded["SPY"]["is_etf"] == "1"
    assert set(loaded) == set(merged)


def test_load_missing_symbols_is_empty(tmp_path):
    assert load_symbols(Datastore(tmp_path)) == {}


class _Ok:
    text = "ok"

    def raise_for_status(self):
        pass


def _capture_headers(monkeypatch):
    seen = {}

    def fake_get(url, headers, timeout):
        seen.update(headers)
        return _Ok()

    monkeypatch.setattr(requests, "get", fake_get)
    return seen


def test_default_user_agent_declares_a_contact_email(monkeypatch):
    # sec.gov answers 403 unless the User-Agent names a contact ("Name admin@example.com")
    monkeypatch.delenv("SEC_USER_AGENT", raising=False)
    seen = _capture_headers(monkeypatch)
    http_fetch_text(SEC_TICKERS_URL)
    assert re.search(r"\S+@\S+\.\w+", seen["User-Agent"])


def test_sec_user_agent_variable_overrides_the_default(monkeypatch):
    monkeypatch.setenv("SEC_USER_AGENT", "someone else@example.org")
    seen = _capture_headers(monkeypatch)
    http_fetch_text(SEC_TICKERS_URL)
    assert seen["User-Agent"] == "someone else@example.org"
