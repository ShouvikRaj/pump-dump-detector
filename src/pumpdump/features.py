"""Stage 2 features: what the market data said at a candidate's flag time.

Pure functions of raw source data and `as_of` (the flag time, epoch seconds).
Each one only looks at what existed before `as_of`: price bars that had
finished, filings already accepted, facts filed on an earlier date, short
interest assumed published. Definitions and reasons: docs/stage2.md.
"""

from __future__ import annotations

import math
import statistics
from datetime import date, datetime, time, timedelta, timezone
from zoneinfo import ZoneInfo

ARCHETYPE_VERSION = "archetype-v1"
ET = ZoneInfo("America/New_York")
DAY = 86_400
SESSION_OPEN = time(9, 30)
SESSION_CLOSE = time(16, 0)  # half days are not modelled (docs/stage2.md, known gaps)
LOW_FLOAT_MAX = 20_000_000
SI_PUBLICATION_LAG_BDAYS = 8

DILUTION_FORMS = frozenset(
    {"S-1", "S-1/A", "S-1MEF", "S-3", "S-3/A", "S-3MEF", "S-3ASR", "F-1", "F-1/A", "F-1MEF", "F-3", "F-3/A", "F-3MEF",
     "F-3ASR", "424B1", "424B2", "424B3", "424B4", "424B5", "424B7", "424B8", "1-A", "1-A/A", "253G1", "253G2", "253G3",
     "253G4"}
)
CURRENT_REPORT_FORMS = frozenset({"8-K", "8-K/A", "6-K", "6-K/A"})
LATE_NOTICE_FORMS = frozenset({"NT 10-K", "NT 10-Q", "NT 20-F", "NT 10-K/A", "NT 10-Q/A", "NT 20-F/A"})
LISTED_EXCHANGES = frozenset({"Nasdaq", "NYSE", "NYSE American", "NYSE Arca", "Cboe BZX", "IEX", "CBOE"})
YAHOO_OTC_CODES = frozenset({"PNK", "OQB", "OQX", "OID", "OEM", "OBB", "OTC", "OGM"})
YAHOO_LISTED_CODES = frozenset({"NMS", "NGM", "NCM", "NAS", "NYQ", "ASE", "PCX", "BTS", "CXI"})

PRICE_KEYS = (
    "price_at_flag", "price_time_utc", "price_source", "last_session", "last_close", "move_since_close", "ret_1d",
    "ret_5d", "ret_20d", "vol_last", "avg_vol_20d", "rel_vol_last", "vol_today", "rel_vol_today", "dollar_vol_20d",
    "volatility_20d", "high_52w", "low_52w", "pct_from_52w_high", "n_sessions",
)


def iso(ts: float | None) -> str:
    return "" if ts is None else datetime.fromtimestamp(ts, timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")


def et_date(ts: float) -> date:
    return datetime.fromtimestamp(ts, ET).date()


def utc_date(ts: float) -> str:
    return datetime.fromtimestamp(ts, timezone.utc).date().isoformat()


def _close_ts(bar_ts: float) -> float:
    return datetime.combine(et_date(bar_ts), SESSION_CLOSE, ET).timestamp()


def price_features(daily: list[list], intraday: list[list], as_of: float, bar_seconds: int = 300) -> dict:
    """Bars are [t, open, high, low, close, volume]; daily t is the session open, intraday t the bar start."""
    out: dict = dict.fromkeys(PRICE_KEYS)
    done = [b for b in daily if _close_ts(b[0]) <= as_of]  # sessions that had closed by the flag
    out["n_sessions"] = len(done)
    last_close_time = None
    if done:
        closes = [b[4] for b in done]
        vols = [b[5] or 0 for b in done]
        last_close_time = _close_ts(done[-1][0])
        out["last_session"] = et_date(done[-1][0]).isoformat()
        out["last_close"] = closes[-1]
        for n, key in ((1, "ret_1d"), (5, "ret_5d"), (20, "ret_20d")):
            if len(closes) > n and closes[-1 - n]:
                out[key] = closes[-1] / closes[-1 - n] - 1
        out["vol_last"] = vols[-1]
        prior = vols[-21:-1]  # the 20 sessions before the last one
        if len(prior) >= 5:
            out["avg_vol_20d"] = sum(prior) / len(prior)
            if out["avg_vol_20d"] > 0:
                out["rel_vol_last"] = vols[-1] / out["avg_vol_20d"]
        recent = done[-20:]
        out["dollar_vol_20d"] = sum(b[4] * (b[5] or 0) for b in recent) / len(recent)
        rets = [
            math.log(closes[i] / closes[i - 1])
            for i in range(max(1, len(closes) - 20), len(closes))
            if closes[i] > 0 and closes[i - 1] > 0
        ]
        if len(rets) >= 5:
            out["volatility_20d"] = statistics.stdev(rets)
        year = done[-252:]
        out["high_52w"] = max(b[2] if b[2] is not None else b[4] for b in year)
        out["low_52w"] = min(b[3] if b[3] is not None else b[4] for b in year)
        if out["high_52w"]:
            out["pct_from_52w_high"] = closes[-1] / out["high_52w"] - 1
        out.update(price_at_flag=closes[-1], price_time_utc=iso(last_close_time), price_source="daily")

    finished = [b for b in intraday if b[0] + bar_seconds <= as_of]
    if finished and (last_close_time is None or finished[-1][0] + bar_seconds > last_close_time):
        # trading after the last close (pre/post market or today's session) sets the price
        out.update(price_at_flag=finished[-1][4], price_time_utc=iso(finished[-1][0] + bar_seconds), price_source="5m")
    if out["price_at_flag"] is not None and out["last_close"]:
        out["move_since_close"] = out["price_at_flag"] / out["last_close"] - 1
    # regular session only: Yahoo's pre/post-market bars carry no volume
    today = [
        b for b in finished
        if et_date(b[0]) == et_date(as_of) and SESSION_OPEN <= datetime.fromtimestamp(b[0], ET).time() < SESSION_CLOSE
    ]
    if today:
        out["vol_today"] = sum(b[5] or 0 for b in today)
        if out["avg_vol_20d"]:
            out["rel_vol_today"] = out["vol_today"] / out["avg_vol_20d"]
    return out


def split_features(splits: list[dict], as_of: float) -> dict:
    past = [s for s in splits if s["t"] <= as_of]
    last = past[-1] if past else None
    return {
        "reverse_splits_1y": sum(1 for s in past if s["t"] > as_of - 365 * DAY and s["numerator"] < s["denominator"]),
        "last_split_date": et_date(last["t"]).isoformat() if last else "",
        "last_split_ratio": f"{last['numerator']:g}:{last['denominator']:g}" if last else "",
    }


def _accepted_ts(text: str) -> float:
    return datetime.fromisoformat(text.replace("Z", "+00:00")).timestamp()


def filing_features(filings: list[dict], as_of: float) -> dict:
    """Counts of filings accepted (made public) in windows before `as_of`."""
    past = sorted(((_accepted_ts(f["accepted"]), f) for f in filings if f.get("accepted")), key=lambda x: x[0])
    past = [(t, f) for t, f in past if t < as_of]

    def count(days: int, keep) -> int:
        return sum(1 for t, f in past if t > as_of - days * DAY and keep(f))

    dilution = [(t, f) for t, f in past if f["form"] in DILUTION_FORMS]
    current = [(t, f) for t, f in past if f["form"] in CURRENT_REPORT_FORMS]
    return {
        "dilution_filings_90d": count(90, lambda f: f["form"] in DILUTION_FORMS),
        "dilution_filings_365d": count(365, lambda f: f["form"] in DILUTION_FORMS),
        "last_dilution_form": dilution[-1][1]["form"] if dilution else "",
        "last_dilution_at": iso(dilution[-1][0]) if dilution else "",
        "offerings_424b_30d": count(30, lambda f: f["form"].startswith("424B")),
        "current_reports_30d": count(30, lambda f: f["form"] in CURRENT_REPORT_FORMS),
        "last_current_report_at": iso(current[-1][0]) if current else "",
        "last_current_report_items": str(current[-1][1].get("items") or "") if current else "",
        "unregistered_sales_90d": count(
            90, lambda f: f["form"].startswith("8-K") and "3.02" in str(f.get("items") or "").split(",")
        ),
        "late_filing_notices_365d": count(365, lambda f: f["form"] in LATE_NOTICE_FORMS),
    }


def former_name_change(former_names: list[dict], as_of: float) -> str:
    """Date the most recent former name stopped being used (a renamed shell is a classic pump vehicle)."""
    day = utc_date(as_of)
    ends = [n["to"] for n in former_names if n.get("to") and n["to"] <= day]
    return max(ends) if ends else ""


def sec_shares_asof(facts: list[dict], as_of: float) -> dict:
    day = utc_date(as_of)
    usable = [f for f in facts if f["filed"] < day]  # `filed` is a date only, so the flag's own day is excluded
    best = max(usable, key=lambda f: (f["filed"], f["end"])) if usable else None
    return {
        "sec_shares_outstanding": best["val"] if best else None,
        "sec_shares_as_of": best["end"] if best else "",
        "sec_shares_filed": best["filed"] if best else "",
    }


def business_days_after(d: date, n: int) -> date:
    while n > 0:
        d += timedelta(days=1)
        if d.weekday() < 5:
            n -= 1
    return d


def short_interest_asof(rows: list[dict], as_of: float) -> dict:
    """Latest FINRA settlement assumed published by `as_of` (settlement + 8 business days)."""
    day = date.fromisoformat(utc_date(as_of))
    usable = [
        r for r in rows
        if r.get("settlementDate")
        and business_days_after(date.fromisoformat(r["settlementDate"]), SI_PUBLICATION_LAG_BDAYS) <= day
    ]
    r = usable[-1] if usable else {}
    return {
        "si_settlement_date": r.get("settlementDate") or "",
        "si_shares": r.get("currentShortPositionQuantity"),
        "si_prev_shares": r.get("previousShortPositionQuantity"),
        "si_days_to_cover": r.get("daysToCoverQuantity"),
    }


def venue_of(symbol_exchange: str, yahoo_exchange: str | None, yahoo_full_exchange: str | None) -> str:
    """listed / otc / unknown. Yahoo's exchange is current, so it wins over the symbol list."""
    full, code = (yahoo_full_exchange or "").upper(), (yahoo_exchange or "").upper()
    if "OTC" in full or code in YAHOO_OTC_CODES:
        return "otc"
    if code in YAHOO_LISTED_CODES or any(k in full for k in ("NASDAQ", "NYSE", "CBOE", "BATS", "IEX")):
        return "listed"
    if symbol_exchange in LISTED_EXCHANGES:
        return "listed"
    if symbol_exchange == "OTC":
        return "otc"
    return "unknown"


def archetype(venue: str, price: float | None, float_shares: float | None, shares_outstanding: float | None) -> str:
    if price is None:
        return "unknown"
    if venue == "otc" and price < 1:
        return "otc_penny"
    if venue == "listed" and 1 <= price <= 10:
        shares = float_shares or shares_outstanding
        if shares and shares <= LOW_FLOAT_MAX:
            return "low_float_runner"
    return "other"
