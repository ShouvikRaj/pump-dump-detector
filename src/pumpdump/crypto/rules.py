"""scan-v1 (market-wide spike flags) and crypto-label-v1 (outcomes), as written in docs/crypto.md.

Pure functions over bars [t_ms, open, high, low, close, base_volume, quote_volume]; no I/O.
"""

from __future__ import annotations

import re
import statistics

SCAN_VERSION = "scan-v1"
LABEL_VERSION = "crypto-label-v1"

MIN = 60_000
HOUR = 3_600_000
DAY = 24 * HOUR

SPIKE = 0.20
VOL_RATIO = 5.0
MIN_QUOTE_VOL = 10_000.0
MIN_MEDIAN_QUOTE_VOL = 100.0
EPISODE_GAP_MS = 72 * HOUR
PREFILTER_RANGE = 1.2

STABLES = {
    "USDT", "USDC", "BUSD", "TUSD", "FDUSD", "DAI", "USDD", "USDP", "PYUSD", "USDE", "USD1", "EUR", "EURC", "EURT",
    "AEUR", "GUSD", "USDJ", "UST", "USTC", "FRAX", "LUSD", "SUSD", "XAUT", "PAXG", "USDQ", "USDS", "RLUSD", "USDG",
}
_LEVERAGED = re.compile(r"\d+[LS]$|(?:UP|DOWN|BULL|BEAR)$")
# tokenised US shares some exchanges list as coins (Gate's MSFTON, the xStocks such as AAPLX): stems before ON / X
US_STOCKS = {
    "AAPL", "MSFT", "NVDA", "TSLA", "AMZN", "GOOGL", "GOOG", "META", "NFLX", "AMD", "COIN", "MSTR", "HOOD", "SPY", "QQQ",
    "CRCL", "PLTR", "ORCL", "INTC", "AVGO", "BABA", "DIS", "JPM", "KO", "PEP", "MCD", "WMT", "COST", "IBM", "UBER",
    "SHOP", "PYPL", "CRWD", "SNOW", "ABNB", "GME", "AMC", "NKE", "XOM", "CVX", "LLY", "UNH", "GLD", "SLV", "TQQQ", "IWM",
    "VTI", "ARKK", "RDDT", "SMCI", "MU", "TSM", "ASML", "ADBE", "CRM", "QCOM", "TXN", "ARM", "APP", "BRKB",
}


def excluded(base: str) -> bool:
    """Stablecoins, leveraged tokens and tokenised US shares are not crypto pump targets."""
    b = base.upper()
    if b in STABLES or _LEVERAGED.search(b):
        return True
    return (b.endswith("ON") and b[:-2] in US_STOCKS) or (b.endswith("X") and b[:-1] in US_STOCKS)


def scan_flags(bars: list[list], last_checked_open: int | None, last_flag_open: int | None) -> list[dict]:
    """scan-v1 over one pair's hourly bars (oldest first, completed hours only).

    Checks every hour after `last_checked_open` that has its previous bar and 24 earlier bars.
    """
    flags = []
    by_t = {b[0]: b for b in bars}
    for i, b in enumerate(bars):
        t = b[0]
        if last_checked_open is not None and t <= last_checked_open:
            continue
        prev = by_t.get(t - HOUR)
        window = [by_t[t - k * HOUR][6] for k in range(1, 25) if (t - k * HOUR) in by_t]
        if prev is None or len(window) < 24 or prev[4] <= 0:
            continue
        median = statistics.median(window)
        spike = b[2] / prev[4] - 1
        if (
            spike >= SPIKE
            and b[6] >= MIN_QUOTE_VOL
            and median >= MIN_MEDIAN_QUOTE_VOL
            and b[6] >= VOL_RATIO * median
            and (last_flag_open is None or t - last_flag_open >= EPISODE_GAP_MS)
        ):
            flags.append(dict(t0=t, spike=round(spike, 4), vol_ratio=round(b[6] / median, 2), quote_volume=round(b[6], 2),
                              median_quote_volume=round(median, 2), prev_close=prev[4]))
            last_flag_open = t
    return flags


OUTCOME_FIELDS = [
    "status", "p0", "p_entry", "peak_ret_1h", "minutes_to_peak", "pump", "pump_dump", "crash_7d", "ret_entry_1h",
    "ret_entry_24h", "ret_entry_7d", "max_ret_entry_24h", "min_ret_entry_24h", "delisted", "label_version",
]


def _r(x):
    return "" if x is None else round(x, 6)


def outcomes(kind: str, t0: int, minute: list[list], hourly: list[list], final: bool, delisted: bool = False) -> dict:
    """crypto-label-v1 for one event. `final`: the 7-day hourly bars have been fetched (or never will be)."""
    o = dict.fromkeys(OUTCOME_FIELDS, "")
    o["label_version"] = LABEL_VERSION
    o["delisted"] = int(delisted)
    m = sorted(minute)
    h = sorted(hourly)
    spike = kind == "spike"

    if spike:
        prev = next((b for b in h if b[0] == t0 - HOUR), None)
        flag = next((b for b in h if b[0] == t0), None)
        if prev is None or flag is None:
            o["status"] = "no_data" if final else "pending"
            return o
        p0, p_entry, entry_end = prev[4], flag[4], t0 + HOUR
        peak, peak_t = flag[2], None
        if m:  # the minute bars place the peak inside the flag hour
            in_hour = [b for b in m if t0 <= b[0] < t0 + HOUR]
            if in_hour:
                pb = max(in_hour, key=lambda b: b[2])
                peak, peak_t = pb[2], pb[0]
    else:
        if not m:
            o["status"] = "no_data" if final else "pending"
            return o
        before = [b for b in m if b[0] + MIN <= t0]
        entry_close = -(-(t0 + 2 * MIN) // MIN) * MIN  # first minute boundary at or after t0 + 2 min
        # minutes without trades have no bar, so prices carry forward: the last close at or before the moment
        upto_entry = [b for b in m if b[0] + MIN <= entry_close]
        first_hour = [b for b in m if t0 - t0 % MIN <= b[0] < t0 + HOUR]
        if not before:
            o["status"] = "no_data"
            return o
        p0, p_entry, entry_end = before[-1][4], upto_entry[-1][4], entry_close
        if first_hour:
            pb = max(first_hour, key=lambda b: b[2])
            peak, peak_t = pb[2], pb[0]
        else:
            peak, peak_t = p0, None

    if p0 <= 0 or p_entry <= 0:
        o["status"] = "no_data"
        return o
    o["p0"], o["p_entry"] = p0, p_entry
    peak_ret = peak / p0 - 1
    o["peak_ret_1h"] = _r(peak_ret)
    o["minutes_to_peak"] = "" if peak_t is None else round((peak_t - t0) / MIN, 1)
    o["pump"] = int(peak_ret >= 0.10)

    # one price path after t0: minute bars while they last, then hourly bars from the next full hour
    m_end = m[-1][0] + MIN if m else t0
    path = [b + [MIN] for b in m if b[0] >= t0 - t0 % MIN] + [b + [HOUR] for b in h if b[0] >= max(t0, m_end)]
    path.sort()

    def close_at(t):  # last close of a bar ending at or before t
        cands = [b for b in path if b[0] + b[7] <= t]
        return cands[-1][4] if cands else None

    horizon_known = path[-1][0] + path[-1][7] if path else t0
    complete = final or horizon_known >= t0 + 7 * DAY

    # pump_dump: a 20% peak, then a give-back of half the rise within 24 h of the peak
    pt = peak_t if peak_t is not None else t0
    if peak_ret >= 0.20:
        after = [b for b in path if b[0] >= pt + (MIN if peak_t is not None else HOUR) and b[0] < pt + DAY]
        line = p0 + 0.5 * (peak - p0)
        hit = any(b[3] <= line for b in after)
        if hit:
            o["pump_dump"] = 1
        elif complete or horizon_known >= pt + DAY:
            o["pump_dump"] = 0
    else:
        o["pump_dump"] = 0

    closes_7d = [b[4] for b in path if b[0] + b[7] <= t0 + 7 * DAY]
    if any(c <= 0.6 * p0 for c in closes_7d):
        o["crash_7d"] = 1
    elif complete:
        o["crash_7d"] = 0

    for name, dt in (("ret_entry_1h", HOUR), ("ret_entry_24h", DAY), ("ret_entry_7d", 7 * DAY)):
        if horizon_known >= t0 + dt:
            c = close_at(t0 + dt)
            o[name] = _r(c / p_entry - 1) if c else ""
    win = [b for b in path if entry_end <= b[0] < entry_end + DAY]
    if win and (horizon_known >= entry_end + DAY or complete):
        o["max_ret_entry_24h"] = _r(max(b[2] for b in win) / p_entry - 1)
        o["min_ret_entry_24h"] = _r(min(b[3] for b in win) / p_entry - 1)

    if horizon_known >= t0 + 7 * DAY:
        o["status"] = "settled"
    elif final:
        o["status"] = "partial"
    else:
        o["status"] = "pending"
    return o
