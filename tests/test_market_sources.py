import pytest

from market_fakes import (
    CHART_404,
    SCREENER_ASOF,
    FakeClock,
    FakeHTTP,
    chart_json,
    finra_json,
    screener_rows_json,
    shares_json,
    submissions_json,
    summary_json,
)
from pumpdump.sources import edgar, finra, nasdaq
from pumpdump.sources.web import Web
from pumpdump.sources.yahoo import NoData, SourceError, Yahoo, yahoo_symbol


def make_web(http, clock=None, **kw):
    clock = clock or FakeClock()
    return Web(request=http, sleep=clock.sleep, clock=clock.time, **kw)


# -- Web -------------------------------------------------------------------------


def test_web_retries_server_errors_then_returns_the_answer():
    http = FakeHTTP([("GET", "https://example.com/", [(503, "busy"), (200, "ok")])])
    clock = FakeClock()
    assert make_web(http, clock).fetch("https://example.com/x") == (200, "ok")
    assert len(http.calls) == 2 and len(clock.sleeps) == 1


def test_web_gives_up_after_max_retries_and_returns_the_last_status():
    http = FakeHTTP([("GET", "https://example.com/", [(429, "slow down")])])
    assert make_web(http, max_retries=2).fetch("https://example.com/x") == (429, "slow down")
    assert len(http.calls) == 3


def test_web_does_not_retry_client_errors():
    http = FakeHTTP([("GET", "https://example.com/", [(404, "nope")])])
    assert make_web(http).fetch("https://example.com/x") == (404, "nope")
    assert len(http.calls) == 1


def test_web_spaces_requests_to_the_same_host():
    http = FakeHTTP([("GET", "https://", [(200, "ok")])])
    clock = FakeClock()
    web = make_web(http, clock, min_interval=1.0)
    web.fetch("https://a.example/1")
    web.fetch("https://b.example/1")  # other host: no wait
    web.fetch("https://a.example/2")
    assert clock.sleeps == [1.0]



def test_web_stops_asking_a_host_that_keeps_failing_for_the_rest_of_the_run():
    # bounds a run's length when a source hangs: each failed fetch costs up to 4 timeouts plus backoff
    http = FakeHTTP([("GET", "https://down.example/", [(0, "ConnectTimeout")]), ("GET", "https://up.example/", [(200, "ok")])])
    web = make_web(http, max_retries=1)
    assert web.fetch("https://down.example/1")[0] == 0
    assert web.fetch("https://down.example/2")[0] == 0
    asked = len(http.calls)
    status, text = web.fetch("https://down.example/3")
    assert status == 0 and "skipped" in text and len(http.calls) == asked
    assert web.fetch("https://up.example/1") == (200, "ok")


def test_web_keeps_asking_a_host_that_fails_now_and_then():
    http = FakeHTTP([("GET", "https://flaky.example/", [(503, "busy"), (200, "ok"), (503, "busy"), (200, "ok")])])
    web = make_web(http, max_retries=0)
    assert [web.fetch(f"https://flaky.example/{i}")[0] for i in range(4)] == [503, 200, 503, 200]

# -- Yahoo -----------------------------------------------------------------------

T0 = 1_790_602_200  # a session open (13:30 UTC)


def test_yahoo_symbol_uses_dashes_for_share_classes():
    assert yahoo_symbol("BRK.B") == "BRK-B"
    assert yahoo_symbol("DRTS") == "DRTS"


def test_chart_returns_bars_without_empty_entries_and_reverse_splits():
    bars = [(T0, 1.0, 1.2, 0.9, 1.1, 1000), (T0 + 86400, None, None, None, None, None), (T0 + 2 * 86400, 1.1, 1.3, 1.0, 1.2, 2000)]
    http = FakeHTTP([("GET", "https://query1.finance.yahoo.com/v8/finance/chart/", [(200, chart_json(bars, splits=[(T0, 1, 10)]))])])
    chart = Yahoo(make_web(http)).chart("ABCD", T0 - 86400, T0 + 3 * 86400, interval="1d")

    assert chart["bars"] == [[T0, 1.0, 1.2, 0.9, 1.1, 1000], [T0 + 2 * 86400, 1.1, 1.3, 1.0, 1.2, 2000]]
    assert chart["splits"] == [{"t": T0, "numerator": 1.0, "denominator": 10.0}]
    assert chart["meta"]["fullExchangeName"] == "NasdaqCM"
    call = http.calls[0]
    assert call["url"].endswith("/chart/ABCD")
    assert call["params"]["interval"] == "1d" and call["params"]["period1"] == T0 - 86400



def test_chart_prices_lose_yahoos_float32_noise():
    # Yahoo serves 0.08 as 0.0800000017881393; unrounded, an unchanged price shows a tiny move
    bars = [(T0, 0.0800000017881393, 0.0800000017881393, 0.0799999982118607, 0.0800000017881393, 1000),
            (T0 + 86400, 14.514100074768066, 14.6, 14.4, 502.6499938964844, 2000)]
    http = FakeHTTP([("GET", "https://query1.finance.yahoo.com/", [(200, chart_json(bars))])])
    chart = Yahoo(make_web(http)).chart("ABCD", T0, T0 + 2 * 86400)
    assert chart["bars"] == [[T0, 0.08, 0.08, 0.08, 0.08, 1000], [T0 + 86400, 14.5141, 14.6, 14.4, 502.65, 2000]]

def test_chart_of_a_quiet_window_has_no_bars():
    http = FakeHTTP([("GET", "https://query1.finance.yahoo.com/", [(200, chart_json([]))])])
    assert Yahoo(make_web(http)).chart("ABCD", T0, T0 + 3600, interval="5m", prepost=True)["bars"] == []


def test_chart_of_an_unknown_symbol_raises_no_data():
    http = FakeHTTP([("GET", "https://query1.finance.yahoo.com/", [(404, CHART_404)])])
    with pytest.raises(NoData, match="No data found"):
        Yahoo(make_web(http)).chart("ZZZZZ", T0, T0 + 86400)


def test_chart_server_errors_raise_source_error():
    http = FakeHTTP([("GET", "https://query1.finance.yahoo.com/", [(502, "<html>bad gateway</html>")])])
    with pytest.raises(SourceError, match="HTTP 502"):
        Yahoo(make_web(http, max_retries=1)).chart("ABCD", T0, T0 + 86400)


def summary_http(*summary_responses):
    return FakeHTTP(
        [
            ("GET", "https://fc.yahoo.com", [(404, "")]),
            ("GET", "https://query2.finance.yahoo.com/v1/test/getcrumb", [(200, "abc123")]),
            ("GET", "https://query2.finance.yahoo.com/v10/finance/quoteSummary/", list(summary_responses)),
        ]
    )


def test_summary_gets_a_crumb_and_returns_plain_values():
    http = summary_http((200, summary_json(floatShares=64_101_174, sharesOutstanding=92_478_154, exchange="NCM", sector="Healthcare", sharesShort=None)))
    s = Yahoo(make_web(http)).summary("DRTS")

    assert s["floatShares"] == 64_101_174 and s["sharesOutstanding"] == 92_478_154
    assert s["exchange"] == "NCM" and s["sector"] == "Healthcare"
    assert s["sharesShort"] is None
    assert http.calls[-1]["params"]["crumb"] == "abc123"


def test_summary_refreshes_an_expired_crumb_once():
    http = summary_http((401, '{"finance":{"error":{"code":"Unauthorized","description":"Invalid Crumb"}}}'), (200, summary_json(floatShares=5)))
    assert Yahoo(make_web(http)).summary("ABCD")["floatShares"] == 5
    assert len(http.urls("https://query2.finance.yahoo.com/v1/test/getcrumb")) == 2


def test_summary_of_an_unknown_symbol_raises_no_data():
    http = summary_http((404, '{"quoteSummary":{"result":null,"error":{"code":"Not Found","description":"Quote not found for symbol: ZZZZZ"}}}'))
    with pytest.raises(NoData):
        Yahoo(make_web(http)).summary("ZZZZZ")


# -- SEC EDGAR ---------------------------------------------------------------------

UA = "pump-dump-detector me@example.com"


def test_submissions_keep_filings_since_a_date_with_acceptance_times():
    body = submissions_json(
        [
            ("424B5", "2026-09-30", "2026-09-30T20:15:00.000Z", ""),
            ("8-K", "2026-09-11", "2026-09-11T14:38:02.000Z", "3.02,9.01"),
            ("10-K", "2024-03-01", "2024-03-01T16:00:00.000Z", ""),
        ],
        former_names=[("OLD NAME INC", "2019-01-01T00:00:00.000Z", "2025-06-01T00:00:00.000Z")],
    )
    http = FakeHTTP([("GET", "https://data.sec.gov/submissions/", [(200, body)])])
    sub = edgar.submissions(make_web(http), 1871321, UA, since="2025-01-01")

    assert http.calls[0]["url"] == "https://data.sec.gov/submissions/CIK0001871321.json"
    assert http.calls[0]["headers"]["User-Agent"] == UA
    assert [f["form"] for f in sub["filings"]] == ["424B5", "8-K"]
    assert sub["filings"][1] == {"form": "8-K", "filed": "2026-09-11", "accepted": "2026-09-11T14:38:02.000Z", "items": "3.02,9.01",
                                "accession": "0000000001-26-000001"}
    assert sub["category"] == "Non-accelerated filer; Smaller reporting company"
    assert sub["former_names"] == [{"name": "OLD NAME INC", "from": "2019-01-01", "to": "2025-06-01"}]


def test_submissions_refused_raise_with_the_status():
    http = FakeHTTP([("GET", "https://data.sec.gov/", [(403, "<title>Undeclared Automated Tool</title>")])])
    with pytest.raises(edgar.EdgarError, match="HTTP 403"):
        edgar.submissions(make_web(http), 1, UA, since="2025-01-01")


def test_shares_facts_are_listed_and_missing_concepts_are_empty():
    http = FakeHTTP([("GET", "https://data.sec.gov/api/xbrl/companyconcept/", [(200, shares_json([("2026-08-12", 328_731_362, "2026-08-14", "10-Q")]))])])
    assert edgar.shares_facts(make_web(http), 880242, UA) == [{"end": "2026-08-12", "val": 328_731_362, "filed": "2026-08-14", "form": "10-Q"}]
    http404 = FakeHTTP([("GET", "https://data.sec.gov/", [(404, "<Error><Code>NoSuchKey</Code></Error>")])])
    assert edgar.shares_facts(make_web(http404), 1, UA) == []


# -- FINRA ---------------------------------------------------------------------------


def test_short_interest_asks_for_one_symbol_over_a_date_range_and_sorts():
    rows = [("2026-09-15", 3_483_059, 3_092_873, 7.3), ("2026-08-31", 3_092_873, 3_060_060, 4.33)]
    http = FakeHTTP([("POST", "https://api.finra.org/", [(200, finra_json(rows))])])
    out = finra.short_interest(make_web(http), "DRTS", "2026-07-01", "2026-10-05")

    assert [r["settlementDate"] for r in out] == ["2026-08-31", "2026-09-15"]
    assert out[1]["currentShortPositionQuantity"] == 3_483_059
    body = http.calls[0]["json"]
    assert body["compareFilters"] == [{"compareType": "equal", "fieldName": "symbolCode", "fieldValue": "DRTS"}]
    assert body["dateRangeFilters"] == [{"fieldName": "settlementDate", "startDate": "2026-07-01", "endDate": "2026-10-05"}]


@pytest.mark.parametrize("status,text", [(204, ""), (200, "[]"), (200, "")])
def test_short_interest_with_no_rows_is_empty(status, text):
    http = FakeHTTP([("POST", "https://api.finra.org/", [(status, text)])])
    assert finra.short_interest(make_web(http), "ZZZZ", "2026-07-01", "2026-10-05") == []


def test_short_interest_errors_raise():
    http = FakeHTTP([("POST", "https://api.finra.org/", [(400, '{"message":"bad"}')])])
    with pytest.raises(finra.FinraError, match="HTTP 400"):
        finra.short_interest(make_web(http), "DRTS", "2026-07-01", "2026-10-05")


# -- Nasdaq screener ---------------------------------------------------------------------


def test_listed_universe_parses_numbers_and_the_price_date():
    http = FakeHTTP(
        [
            ("GET", "https://api.nasdaq.com/api/screener/stocks", [(200, SCREENER_ASOF), (200, screener_rows_json([("DRTS", "14.51", 380026, 1341858015), ("XYZ", "0.85", 0, 0)]))]),
        ]
    )
    asof, rows = nasdaq.listed_universe(make_web(http))

    assert asof == "2026-10-01"
    assert rows[0] == {
        "symbol": "DRTS", "name": "DRTS Inc.", "last_sale": 14.51, "pct_change": 1.5, "volume": 380026,
        "market_cap": 1341858015, "country": "United States", "ipo_year": "", "sector": "Health Care", "industry": "Biotechnology",
    }
    assert rows[1]["last_sale"] == 0.85
    assert http.calls[1]["params"]["download"] == "true"
