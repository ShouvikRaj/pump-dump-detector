import math
from datetime import date, datetime, timedelta
from zoneinfo import ZoneInfo

import pytest

from pumpdump import features as f

ET = ZoneInfo("America/New_York")


def et(y, m, d, hh=9, mm=30):
    return datetime(y, m, d, hh, mm, tzinfo=ET).timestamp()


def sessions(last=date(2026, 10, 2), n=25):
    """Weekday session dates ending at `last`, oldest first."""
    out, d = [], last
    while len(out) < n:
        if d.weekday() < 5:
            out.append(d)
        d -= timedelta(days=1)
    return out[::-1]


def daily(n=25, last=date(2026, 10, 2), last_volume=5000):
    """Bars at 09:30 ET; close rises 0.1 per session; volume 1000 except the last session."""
    days = sessions(last, n)
    bars = []
    for i, d in enumerate(days):
        c = 10 + 0.1 * i
        bars.append([et(d.year, d.month, d.day), c - 0.05, c + 0.2, c - 0.2, c, last_volume if i == n - 1 else 1000])
    return bars


def five_min(d, start=(4, 0), end=(20, 0), price=12.0, volume=100):
    """5-minute bars on ET date d from start to end (bar start times)."""
    t, stop = et(d.year, d.month, d.day, *start), et(d.year, d.month, d.day, *end)
    bars = []
    i = 0
    while t < stop:
        bars.append([t, price, price, price, price + 0.01 * i, volume])
        t += 300
        i += 1
    return bars


# -- price features ------------------------------------------------------------------


def test_weekend_flag_uses_fridays_session_and_has_no_volume_today():
    bars = daily()
    p = f.price_features(bars, [], as_of=et(2026, 10, 4, 19, 24))  # Sunday evening

    closes = [b[4] for b in bars]
    assert p["last_session"] == "2026-10-02"
    assert p["last_close"] == closes[-1]
    assert p["ret_1d"] == pytest.approx(closes[-1] / closes[-2] - 1)
    assert p["ret_5d"] == pytest.approx(closes[-1] / closes[-6] - 1)
    assert p["ret_20d"] == pytest.approx(closes[-1] / closes[-21] - 1)
    assert p["vol_last"] == 5000 and p["avg_vol_20d"] == 1000 and p["rel_vol_last"] == 5.0
    assert p["vol_today"] is None and p["rel_vol_today"] is None
    assert p["price_at_flag"] == closes[-1] and p["price_source"] == "daily"
    assert p["move_since_close"] == 0.0
    assert p["n_sessions"] == 25


def test_flag_during_a_session_ignores_its_unfinished_bars():
    bars = daily() + [[et(2026, 10, 5), 13.0, 15.0, 12.5, 14.9, 99999]]  # today's partial daily bar
    intraday = five_min(date(2026, 10, 5), end=(10, 30))
    as_of = et(2026, 10, 5, 10, 2)
    p = f.price_features(bars, intraday, as_of)

    done = [b for b in intraday if b[0] + 300 <= as_of]
    assert p["last_session"] == "2026-10-02"  # today hasn't closed
    assert p["price_at_flag"] == done[-1][4]  # the 09:55 bar; the 10:00 bar ends after the flag
    assert p["price_time_utc"] == "2026-10-05T14:00:00Z"
    assert p["price_source"] == "5m"
    assert p["vol_today"] == 600  # the six regular-session bars, 09:30 to 09:55
    assert p["rel_vol_today"] == pytest.approx(0.6)
    assert p["move_since_close"] == pytest.approx(done[-1][4] / bars[-2][4] - 1)



def test_before_the_open_volume_today_is_blank_not_zero():
    # Yahoo's pre/post-market bars carry no volume, so counting them would read as "no trading"
    intraday = five_min(date(2026, 10, 5), end=(6, 0), volume=0)
    p = f.price_features(daily(), intraday, et(2026, 10, 5, 6, 0))
    assert p["price_source"] == "5m" and p["vol_today"] is None and p["rel_vol_today"] is None


def test_after_the_open_a_stock_with_no_trades_yet_has_zero_volume_today():
    # Yahoo skips 5-minute bars without trades, so no bar since the open means nothing traded yet
    friday = five_min(date(2026, 10, 2), start=(9, 30), end=(16, 0))
    p = f.price_features(daily(), friday, et(2026, 10, 5, 9, 55))  # Monday morning
    assert p["vol_today"] == 0 and p["rel_vol_today"] == 0


def test_volume_today_stays_blank_on_market_holidays():
    wednesday = five_min(date(2026, 11, 25), start=(9, 30), end=(16, 0))
    p = f.price_features(daily(last=date(2026, 11, 25)), wednesday, et(2026, 11, 26, 11, 0))  # Thanksgiving
    assert p["vol_today"] is None and p["rel_vol_today"] is None


def test_volume_today_stays_blank_without_a_finished_bar_or_without_5m_data():
    friday = five_min(date(2026, 10, 2), start=(9, 30), end=(16, 0))
    assert f.price_features(daily(), friday, et(2026, 10, 4, 19, 24))["vol_today"] is None  # Sunday
    assert f.price_features(daily(), friday, et(2026, 10, 5, 9, 33))["vol_today"] is None  # first bar ends 09:35
    assert f.price_features(daily(), [], et(2026, 10, 5, 11, 0))["vol_today"] is None  # the 5m fetch failed


def test_after_the_close_the_day_counts_and_post_market_sets_the_price():
    bars = daily(last=date(2026, 10, 2))
    intraday = five_min(date(2026, 10, 2), start=(4, 0), end=(16, 25), price=11.0)
    p = f.price_features(bars, intraday, as_of=et(2026, 10, 2, 16, 30))

    assert p["last_session"] == "2026-10-02"
    assert p["price_source"] == "5m" and p["price_at_flag"] == intraday[-1][4]


def test_intraday_bars_older_than_the_last_close_lose_to_the_close():
    bars = daily()
    intraday = five_min(date(2026, 9, 29), end=(16, 0))
    p = f.price_features(bars, intraday, as_of=et(2026, 10, 4, 12, 0))
    assert p["price_source"] == "daily" and p["price_at_flag"] == bars[-1][4]


def test_short_histories_leave_long_windows_blank():
    p = f.price_features(daily(n=4), [], as_of=et(2026, 10, 4))
    assert p["ret_1d"] is not None and p["ret_5d"] is None and p["ret_20d"] is None
    assert p["avg_vol_20d"] is None and p["rel_vol_last"] is None


def test_range_and_volatility():
    bars = daily()
    p = f.price_features(bars, [], as_of=et(2026, 10, 4))
    assert p["high_52w"] == pytest.approx(max(b[2] for b in bars))
    assert p["low_52w"] == pytest.approx(min(b[3] for b in bars))
    assert p["pct_from_52w_high"] == pytest.approx(bars[-1][4] / p["high_52w"] - 1)
    rets = [math.log(bars[i][4] / bars[i - 1][4]) for i in range(len(bars) - 20, len(bars))]
    mean = sum(rets) / len(rets)
    assert p["volatility_20d"] == pytest.approx(math.sqrt(sum((r - mean) ** 2 for r in rets) / (len(rets) - 1)))
    assert p["dollar_vol_20d"] == pytest.approx(sum(b[4] * b[5] for b in bars[-20:]) / 20)


def test_no_bars_at_all_gives_blanks():
    p = f.price_features([], [], as_of=et(2026, 10, 4))
    assert p["price_at_flag"] is None and p["last_close"] is None and p["n_sessions"] == 0


def test_a_listing_with_only_intraday_bars_still_has_a_price():
    intraday = five_min(date(2026, 10, 5), start=(9, 30), end=(11, 0), price=4.0)
    p = f.price_features([], intraday, as_of=et(2026, 10, 5, 11, 0))
    assert p["price_at_flag"] == intraday[-1][4] and p["last_close"] is None and p["move_since_close"] is None


# -- splits, filings, SEC facts, short interest ------------------------------------------


def test_reverse_splits_in_the_last_year_are_counted():
    as_of = et(2026, 10, 4)
    splits = [
        {"t": et(2024, 1, 5), "numerator": 1.0, "denominator": 20.0},  # too old
        {"t": et(2026, 3, 2), "numerator": 1.0, "denominator": 10.0},
        {"t": et(2026, 6, 1), "numerator": 2.0, "denominator": 1.0},  # forward split
        {"t": et(2026, 10, 9), "numerator": 1.0, "denominator": 5.0},  # after the flag
    ]
    s = f.split_features(splits, as_of)
    assert s == {"reverse_splits_1y": 1, "last_split_date": "2026-06-01", "last_split_ratio": "2:1"}


def test_filing_counts_use_acceptance_time_before_the_flag():
    as_of = datetime(2026, 10, 5, 14, 0, tzinfo=ZoneInfo("UTC")).timestamp()
    filings = [
        {"form": "424B5", "filed": "2026-10-05", "accepted": "2026-10-05T14:30:00.000Z", "items": ""},  # after the flag
        {"form": "424B5", "filed": "2026-09-30", "accepted": "2026-09-30T20:15:00.000Z", "items": ""},
        {"form": "S-3", "filed": "2026-08-01", "accepted": "2026-08-01T16:00:00.000Z", "items": ""},
        {"form": "S-1/A", "filed": "2026-01-10", "accepted": "2026-01-10T16:00:00.000Z", "items": ""},
        {"form": "8-K", "filed": "2026-09-11", "accepted": "2026-09-11T14:38:02.000Z", "items": "3.02,9.01"},
        {"form": "6-K", "filed": "2026-09-20", "accepted": "2026-09-20T12:00:00.000Z", "items": ""},
        {"form": "NT 10-Q", "filed": "2026-08-15", "accepted": "2026-08-15T21:00:00.000Z", "items": ""},
        {"form": "S-8", "filed": "2026-09-01", "accepted": "2026-09-01T12:00:00.000Z", "items": ""},  # not dilution here
    ]
    out = f.filing_features(filings, as_of)
    assert out["dilution_filings_90d"] == 2  # 424B5 (Sep 30) + S-3 (Aug 1)
    assert out["dilution_filings_365d"] == 3
    assert out["last_dilution_form"] == "424B5" and out["last_dilution_at"] == "2026-09-30T20:15:00Z"
    assert out["offerings_424b_30d"] == 1
    assert out["current_reports_30d"] == 2
    assert out["last_current_report_at"] == "2026-09-20T12:00:00Z" and out["last_current_report_items"] == ""
    assert out["unregistered_sales_90d"] == 1
    assert out["late_filing_notices_365d"] == 1


def test_the_latest_8k_before_the_flag_is_named_with_its_items():
    # an 8-K just before a mention spike points to real news rather than a pump
    as_of = datetime(2026, 10, 5, 14, 0, tzinfo=ZoneInfo("UTC")).timestamp()
    filings = [
        {"form": "8-K", "filed": "2026-10-05", "accepted": "2026-10-05T12:01:00.000Z", "items": "2.02,9.01"},
        {"form": "8-K", "filed": "2026-10-05", "accepted": "2026-10-05T14:05:00.000Z", "items": "1.01"},  # after
    ]
    out = f.filing_features(filings, as_of)
    assert out["last_current_report_at"] == "2026-10-05T12:01:00Z"
    assert out["last_current_report_items"] == "2.02,9.01"


def test_no_filings_gives_zero_counts():
    out = f.filing_features([], et(2026, 10, 4))
    assert out["dilution_filings_90d"] == 0 and out["last_dilution_form"] == "" and out["last_dilution_at"] == ""
    assert out["last_current_report_at"] == "" and out["last_current_report_items"] == ""


def test_last_name_change_ignores_changes_after_the_flag():
    names = [{"name": "A", "from": "2019-01-01", "to": "2025-06-01"}, {"name": "B", "from": "2025-06-01", "to": "2026-11-01"}]
    assert f.former_name_change(names, et(2026, 10, 4)) == "2025-06-01"
    assert f.former_name_change([], et(2026, 10, 4)) == ""


def test_sec_shares_use_the_latest_value_filed_before_the_flag_date():
    facts = [
        {"end": "2026-04-29", "val": 320_883_262, "filed": "2026-04-30", "form": "10-K/A"},
        {"end": "2026-08-12", "val": 328_731_362, "filed": "2026-08-14", "form": "10-Q"},
        {"end": "2026-10-01", "val": 400_000_000, "filed": "2026-10-04", "form": "10-Q"},  # filed on the flag date
    ]
    out = f.sec_shares_asof(facts, et(2026, 10, 4, 12, 0))
    assert out == {"sec_shares_outstanding": 328_731_362, "sec_shares_as_of": "2026-08-12", "sec_shares_filed": "2026-08-14"}
    assert f.sec_shares_asof([], et(2026, 10, 4))["sec_shares_outstanding"] is None


def test_business_days_skip_weekends():
    assert f.business_days_after(date(2026, 9, 15), 8) == date(2026, 9, 25)
    assert f.business_days_after(date(2026, 10, 2), 1) == date(2026, 10, 5)


def test_short_interest_waits_for_the_assumed_publication_date():
    rows = [
        {"settlementDate": "2026-08-31", "currentShortPositionQuantity": 3_092_873, "previousShortPositionQuantity": 3_060_060, "daysToCoverQuantity": 4.33},
        {"settlementDate": "2026-09-15", "currentShortPositionQuantity": 3_483_059, "previousShortPositionQuantity": 3_092_873, "daysToCoverQuantity": 7.3},
    ]
    before = f.short_interest_asof(rows, et(2026, 9, 24, 12, 0))  # 7 business days after Sep 15
    after = f.short_interest_asof(rows, et(2026, 9, 25, 12, 0))
    assert before["si_settlement_date"] == "2026-08-31" and before["si_shares"] == 3_092_873
    assert after == {"si_settlement_date": "2026-09-15", "si_shares": 3_483_059, "si_prev_shares": 3_092_873, "si_days_to_cover": 7.3}
    assert f.short_interest_asof([], et(2026, 9, 25))["si_shares"] is None


# -- venue and archetype ------------------------------------------------------------------


@pytest.mark.parametrize(
    "symbol_exchange,yahoo_exchange,yahoo_full,expected",
    [
        ("Nasdaq", "NCM", "NasdaqCM", "listed"),
        ("Nasdaq", "PNK", "OTC Markets Pink", "otc"),  # delisted since the symbol list was made
        ("OTC", None, None, "otc"),
        ("", "OID", "OTC Markets OTCID", "otc"),
        ("", "NYQ", "NYSE", "listed"),
        ("NYSE American", None, None, "listed"),
        ("", None, None, "unknown"),
    ],
)
def test_venue_prefers_yahoos_current_exchange(symbol_exchange, yahoo_exchange, yahoo_full, expected):
    assert f.venue_of(symbol_exchange, yahoo_exchange, yahoo_full) == expected


@pytest.mark.parametrize(
    "venue,price,float_shares,shares_out,expected",
    [
        ("listed", 4.2, 8_000_000, 30_000_000, "low_float_runner"),
        ("listed", 4.2, 25_000_000, 30_000_000, "other"),
        ("listed", 4.2, None, 15_000_000, "low_float_runner"),  # float unknown: shares outstanding
        ("listed", 0.6, 5_000_000, 5_000_000, "other"),  # listed but sub-dollar
        ("listed", 14.77, 5_000_000, 5_000_000, "other"),
        ("listed", 4.2, None, None, "other"),
        ("otc", 0.0098, None, 4_638_127_419, "otc_penny"),
        ("otc", 1.83, 120_884_860, 152_070_251, "other"),
        ("unknown", 0.5, None, None, "other"),
        ("listed", None, 5_000_000, 5_000_000, "unknown"),
    ],
)
def test_archetype_rule(venue, price, float_shares, shares_out, expected):
    assert f.archetype(venue, price, float_shares, shares_out) == expected
