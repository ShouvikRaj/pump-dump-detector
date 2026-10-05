import pytest
import requests

from pumpdump.store import Datastore
from pumpdump.symbols import (
    NASDAQ_LISTED_URL,
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

CONTACT = "pump-dump-detector someone@example.org"

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


def test_refresh_survives_one_failed_source(monkeypatch):
    monkeypatch.setenv("SEC_USER_AGENT", CONTACT)

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
    status_code = 200
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


def test_sec_requests_carry_the_configured_contact(monkeypatch):
    monkeypatch.setenv("SEC_USER_AGENT", CONTACT)
    seen = _capture_headers(monkeypatch)
    http_fetch_text(SEC_TICKERS_URL)
    assert seen["User-Agent"] == CONTACT


def test_a_bare_email_gets_the_project_name_in_front(monkeypatch):
    # SEC's documented format is "Name contact@domain"; the secret may hold just the address
    monkeypatch.setenv("SEC_USER_AGENT", " someone@example.org ")
    seen = _capture_headers(monkeypatch)
    http_fetch_text(SEC_TICKERS_URL)
    assert seen["User-Agent"] == "pump-dump-detector someone@example.org"


def test_contact_email_is_sent_only_to_sec(monkeypatch):
    monkeypatch.setenv("SEC_USER_AGENT", CONTACT)
    seen = _capture_headers(monkeypatch)
    http_fetch_text(NASDAQ_LISTED_URL)
    assert "@" not in seen["User-Agent"]


def test_refresh_skips_sec_without_a_contact(monkeypatch):
    # sec.gov refuses a User-Agent without a reachable contact (GitHub no-reply addresses included),
    # so asking it would only collect a 403
    monkeypatch.delenv("SEC_USER_AGENT", raising=False)
    requested = []

    def fetch(url):
        requested.append(url)
        return NASDAQ_LISTED if "nasdaqlisted" in url else OTHER_LISTED

    symbols, errors = refresh_symbols(fetch)
    assert SEC_TICKERS_URL not in requested
    assert set(symbols) == {"AAAP", "AACG", "A", "BRK.B", "SPY"}
    assert len(errors) == 1 and "SEC_USER_AGENT" in errors[0]


def test_refused_request_reports_the_page_title(monkeypatch):
    # tells an "undeclared automated tool" refusal apart from a CDN/IP block
    class Denied:
        status_code = 403
        text = "<html><head><title>Access Denied</title></head><body>Reference #18.9f</body></html>"

    monkeypatch.setattr(requests, "get", lambda url, headers, timeout: Denied())
    with pytest.raises(RuntimeError, match="HTTP 403.*Access Denied"):
        http_fetch_text(SEC_TICKERS_URL)
