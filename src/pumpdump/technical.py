"""Technical features (`technical-v1`): how stretched a candidate's spike was at its flag time.

Computed from the raw Stage 2 data already saved for each snapshot (daily bars and 5-minute bars) and the daily
Nasdaq cross-section, using only bars that had finished by `as_of`, like the Stage 2 features. Why each one and what
research it comes from: docs/stage5.md ("technical") and research/trading-risk-findings.md.
"""

from __future__ import annotations

import csv
import gzip
import io
import json
import math
from datetime import date, datetime, timezone

from .features import ET, MARKET_HOLIDAYS, SESSION_CLOSE, SESSION_OPEN, et_date, iso, price_features
from .market import RAW_DIR, SNAPSHOTS
from .store import Datastore

TECHNICAL_VERSION = "technical-v1"
TECHNICAL = "model/technical.csv"
FEATURES = ("vwap_ext", "off_high", "mins_since_high", "gap_open", "ret_60m", "vol_60m_rel", "max_ret_20d",
            "up_streak", "run_up", "atr_stretch", "ssr_today", "runners_breadth")
FIELDS = ["snapshot_id", "technical_version", "computed_at_utc", "universe_date", *FEATURES]
BAR = 300
BARS_PER_SESSION = 78  # 6.5 hours of 5-minute bars
RUNNER_MAX_PRICE, RUNNER_MIN_MOVE = 10.0, 40.0  # a "runner" in the cross-section: under $10, up 40% or more
SSR_DROP = 0.10  # SEC Rule 201: a 10% fall below the previous close restricts shorting that day and the next


def _regular(t: float) -> bool:
    return SESSION_OPEN <= datetime.fromtimestamp(t, ET).time() < SESSION_CLOSE


def _close_ts(d: date) -> float:
    return datetime.combine(d, SESSION_CLOSE, ET).timestamp()


def daily_features(done: list[list]) -> dict:
    """Features of the sessions that had closed by the flag (bars [t, open, high, low, close, volume], oldest first)."""
    out: dict = {}
    closes = [b[4] for b in done]
    if len(closes) >= 21:
        rets = [closes[i] / closes[i - 1] - 1 for i in range(len(closes) - 20, len(closes)) if closes[i - 1]]
        out["max_ret_20d"] = max(rets) if rets else None
    if len(closes) >= 2:
        streak = 0
        for i in range(len(closes) - 1, 0, -1):
            if closes[i] > closes[i - 1]:
                streak += 1
            else:
                break
        out["up_streak"] = streak
    if len(closes) >= 10 and min(closes[-10:]) > 0:
        out["run_up"] = closes[-1] / min(closes[-10:]) - 1
    if len(done) >= 21:
        trs = [max(b[2], p[4]) - min(b[3], p[4]) for p, b in zip(done[-15:-1], done[-14:])]
        atr = sum(trs) / len(trs)
        if atr > 0:
            out["atr_stretch"] = (closes[-1] - sum(closes[-20:]) / 20) / atr
    if len(done) >= 2 and done[-2][4]:
        out["ssr_today"] = int(done[-1][3] <= (1 - SSR_DROP) * done[-2][4])
    return out


def intraday_features(intraday: list[list], as_of: float, price: float | None, done: list[list]) -> dict:
    """Features of the 5-minute bars finished by the flag: those of the flag's ET date (pre-market, session and
    post-market so far; blank if it has none, e.g. weekends), and the hour before the flag."""
    out: dict = {}
    finished = [b for b in intraday if b[0] + BAR <= as_of and b[4] is not None]
    if not finished or price is None:
        return out
    day = et_date(as_of)
    today = [b for b in finished if et_date(b[0]) == day]
    session = [b for b in today if _regular(b[0])]
    before_day = [b for b in done if et_date(b[0]) < day]
    prev_close = before_day[-1][4] if before_day else None
    if today:
        hi = max(today, key=lambda b: (b[2] if b[2] is not None else b[4], -b[0]))
        high = hi[2] if hi[2] is not None else hi[4]
        if high:
            out["off_high"] = price / high - 1
            out["mins_since_high"] = (as_of - (hi[0] + BAR)) / 60
    if session:
        vol = sum(b[5] or 0 for b in session)
        if vol > 0:
            vwap = sum(((b[2] + b[3] + b[4]) / 3 if b[2] is not None and b[3] is not None else b[4]) * (b[5] or 0)
                       for b in session) / vol
            out["vwap_ext"] = price / vwap - 1
        if prev_close and session[0][1]:
            out["gap_open"] = session[0][1] / prev_close - 1
        if prev_close:
            low = min(b[3] if b[3] is not None else b[4] for b in session)
            out["ssr_intraday"] = int(low <= (1 - SSR_DROP) * prev_close)
    before = [b for b in finished if b[0] + BAR <= as_of - 3600]
    if before and before[-1][4] and as_of - (before[-1][0] + BAR) <= 2 * 3600:
        out["ret_60m"] = price / before[-1][4] - 1
    # session minutes in the hour before the flag (Yahoo skips bars without trades, so bars can't be counted)
    open_ts = datetime.combine(day, SESSION_OPEN, ET).timestamp()
    overlap = max(0.0, min(as_of, _close_ts(day)) - max(as_of - 3600, open_ts))
    avg_vol = _avg_vol(done)
    if overlap >= BAR and avg_vol and (session or _trading_day(day)):
        vol = sum(b[5] or 0 for b in session if b[0] + BAR > as_of - 3600)
        out["vol_60m_rel"] = vol / (avg_vol * overlap / (BARS_PER_SESSION * BAR))
    return out


def _trading_day(d: date) -> bool:
    return d.weekday() < 5 and d not in MARKET_HOLIDAYS


def _avg_vol(done: list[list]) -> float | None:
    vols = [b[5] or 0 for b in done[-20:]]
    return sum(vols) / len(vols) if len(vols) >= 5 and sum(vols) > 0 else None


def breadth(universe: dict[str, list[dict]], as_of: float) -> tuple[str, int | None]:
    """Listed runners (under $10, up 40%+) in the latest cross-section whose session had closed by the flag."""
    usable = [d for d in universe if _close_ts(date.fromisoformat(d)) <= as_of]
    if not usable:
        return "", None
    d = max(usable)
    n = 0
    for r in universe[d]:
        try:
            p, chg = float(r["last_sale"].lstrip("$")), float(r["pct_change"].rstrip("%"))
        except (KeyError, ValueError, AttributeError):
            continue
        n += int(p < RUNNER_MAX_PRICE and chg >= RUNNER_MIN_MOVE)
    return d, n


def technical_features(raw: dict, as_of: float, universe: dict[str, list[dict]]) -> dict:
    """technical-v1 features of one snapshot's raw data (market/raw); blank where the bars don't allow one."""
    x: dict = dict.fromkeys(FEATURES)
    daily = (raw.get("daily") or {}).get("bars") or []
    intraday = (raw.get("intraday") or {}).get("bars") or []
    pf = price_features(daily, intraday, as_of)
    done = [b for b in daily if b[4] is not None and _close_ts(et_date(b[0])) <= as_of]
    x.update(daily_features(done))
    intra = intraday_features(intraday, as_of, pf.get("price_at_flag"), done)
    if intra.pop("ssr_intraday", 0):
        x["ssr_today"] = 1  # a 10% fall during the flag's own session restricts shorting too
    x.update(intra)
    x["universe_date"], x["runners_breadth"] = breadth(universe, as_of)
    return x


# -- the data branch ----------------------------------------------------------------------------------------------
def raw_path(snap: dict) -> str:
    day = datetime.fromtimestamp(float(snap["snapshot_at"]), timezone.utc).strftime("%Y/%m/%d")
    return f"{RAW_DIR}/{day}/{snap['snapshot_id'].replace('/', '_').replace(':', '_')}.json.gz"


def load_universe(ds: Datastore) -> dict[str, list[dict]]:
    out = {}
    for path in sorted(ds.path("market/universe").glob("*/*/*.csv.gz")):
        with gzip.open(path, "rt", newline="") as fh:
            out[path.name.removesuffix(".csv.gz")] = list(csv.DictReader(fh))
    return out


def update(ds: Datastore, now: float) -> int:
    """Append technical-v1 rows for snapshots that have none yet and whose raw file is checked out; returns how many.
    A row is never rewritten, so a feature can't change after the model has seen it."""
    have = {r["snapshot_id"] for r in ds.read_csv(TECHNICAL) if r.get("technical_version") == TECHNICAL_VERSION}
    universe = load_universe(ds)
    rows = []
    for s in ds.read_csv(SNAPSHOTS):
        if s["snapshot_id"] in have or not s.get("snapshot_at"):
            continue
        path = ds.path(raw_path(s))
        if not path.exists():
            continue  # not checked out (older than the run's window): computed by a run that has it
        with gzip.open(path, "rb") as fh:
            raw = json.load(io.TextIOWrapper(fh, encoding="utf-8"))
        x = technical_features(raw, float(s["as_of"]), universe)
        rows.append({"snapshot_id": s["snapshot_id"], "technical_version": TECHNICAL_VERSION,
                     "computed_at_utc": iso(now), **{k: _fmt(v) for k, v in x.items()}})
    if rows:
        ds.append_csv(TECHNICAL, FIELDS, rows)
    return len(rows)


def _fmt(v):
    if v is None:
        return ""
    if isinstance(v, float):
        return "" if math.isnan(v) else f"{v:.6g}"
    return v
