"""Stage 5: score every candidate at its flag time, retrain every week as labels arrive, and evaluate honestly.

Once a day (the `model` workflow, after Stage 4's labels) this

  1. computes the text features and LLM ratings of new candidates' flag-time Reddit documents (text.py);
  2. builds one row per Stage 2 snapshot: features known at the flag (Stage 1 chatter, text, LLM, Stage 2 market
     data), Stage 4's targets (crash, pump), and when each label became usable (no lookahead);
  3. scores each new candidate once with its week's LightGBM model, trained on the labels available before that week
     began with recent rows weighted more, and appends the score to the prospective log (model/predictions.csv);
  4. replays every development week the same way (walk-forward) and reports precision / recall / F1 / AP per
     archetype and period, the five robustness checks, and which feature groups are weak and pruned;
  5. keeps the hold-out (flags from 2027-01-04 on) sealed until collection is over and its labels have settled, then
     evaluates it once.

The rule (`model-v1`, then `model-v2` before any model was trained) is written down in docs/stage5.md. LightGBM and
numpy are only imported to fit and score, so the other commands run without them.
"""

from __future__ import annotations

import csv
import gzip
import json
import math
import statistics
import time
from collections import Counter, defaultdict
from dataclasses import dataclass
from datetime import date, datetime, timedelta, timezone
from typing import Callable

from . import db, text
from .features import DAY, iso
from .label import LABELS
from .market import SNAPSHOTS
from .pipeline import Settings, collection_done
from .store import Datastore
from .symbols import load_symbols
from .tickers import default_extractor
from .track import DAILY, OUTCOMES, _close_ts

MODEL_VERSION = "model-v2"
HOLDOUT_START = datetime(2027, 1, 4, tzinfo=timezone.utc).timestamp()  # a Monday; nothing in the rule changes after it
WEEK = 7 * DAY
HALF_LIFE = 56 * DAY  # recency weight halves every 8 weeks
MIN_ROWS, MIN_POS = 50, 5  # a week's model trains only with this many available rows and positives
LIFT, MIN_BASE_RATE = 2.0, 0.01  # flag = score >= 2 x the training candidates' base rate (at least 1%)
LABEL_DELAY = 4 * 3600  # a label is usable 4 hours after the close of the session that settles it
PRUNE_MIN_POS = 20  # feature groups are pruned only once the replay has this many positive candidates
LLM_RETRY = 3 * DAY  # a failed rating is retried for this long after the flag
HOLDOUT_GRACE = 45 * DAY  # after the last flag, a snapshot Stage 4 never labeled stops holding up the hold-out
HISTORY_WINDOW = 90 * DAY  # earlier flags of the same stock counted by prior_flags_90d
TARGETS = ("crash", "pump")
ARCHETYPES = ("low_float_runner", "otc_penny", "other")
PUMP_TYPES = ("low_float_runner", "otc_penny")
HARD_NEWS_ITEMS = frozenset({"2.02", "2.01", "5.01", "1.03", "1.01"})

GROUPS = {
    "chatter": ["mentions_log", "baseline_log", "spike_z", "authors_ratio", "post_share", "hype_share", "hype_spike",
                "wsb_share", "pennystocks_share", "cashtag_share", "stocktwits_trending"],
    "text": list(text.TEXT_FEATURES),
    "llm": list(text.LLM_FEATURES),
    "price_volume": ["price_log", "move_since_close", "ret_1d", "ret_5d", "ret_20d", "rel_vol_last_log",
                     "rel_vol_today_log", "volatility_20d", "pct_from_52w_high", "dollar_vol_log"],
    "size": ["market_cap_log", "float_log", "turnover_last", "listing_age_log", "reverse_splits_1y", "otc",
             "institution_pct"],
    "short_interest": ["si_pct_float", "si_days_to_cover", "si_change"],
    "filings": ["sec_filer", "dilution_90d", "offerings_424b_30d", "days_since_dilution", "current_reports_30d",
                "days_since_report", "report_hard_news", "unregistered_sales_90d", "late_notices_365d",
                "name_change_1y"],
    "history": ["prior_flags_90d", "days_since_prior_flag", "prior_crashes"],
}
FEATURES = [f for fs in GROUPS.values() for f in fs]
MARKET_GROUPS = ("price_volume", "size", "short_interest", "filings")
SOCIAL_GROUPS = ("chatter", "text", "llm")
PARAMS = {"objective": "binary", "learning_rate": 0.05, "num_leaves": 7, "max_depth": 3, "min_data_in_leaf": 10,
          "feature_fraction": 0.8, "bagging_fraction": 0.8, "bagging_freq": 1, "lambda_l2": 1.0, "seed": 0,
          "num_threads": 1, "deterministic": True, "force_row_wise": True, "verbose": -1}
ROUNDS = 150

PREDICTIONS = "model/predictions.csv"
WALKFORWARD = "model/walkforward.csv"
README = "model/README.md"
HOLDOUT_MD = "model/holdout.md"
HOLDOUT_CSV = "model/holdout.csv"
STATE = "model/state.json"
KEY_FIELDS = ["snapshot_id", "episode_id", "ticker", "as_of_utc", "archetype"]
PREDICTION_FIELDS = [*KEY_FIELDS, "week_utc", "target", "score", "threshold", "flagged", "n_train", "n_pos", "groups",
                     "holdout", "note", "scored_at_utc", "model_version"]
WALKFORWARD_FIELDS = [*KEY_FIELDS, "week_utc", "ret_close_10"] + [
    f"{t}{s}" for t in TARGETS for s in ("", "_score", "_flagged", "_score_deployed", "_flagged_deployed")]
HOLDOUT_FIELDS = [*KEY_FIELDS, "week_utc", "target", "score", "flagged", "y", "ret_close_10"]


# -- small helpers ------------------------------------------------------------------------------------------------
def week_start(ts: float) -> float:
    d = datetime.fromtimestamp(ts, timezone.utc).date()
    monday = d - timedelta(days=d.weekday())
    return datetime(monday.year, monday.month, monday.day, tzinfo=timezone.utc).timestamp()


def recency_weight(age_s: float) -> float:
    return 0.5 ** (age_s / HALF_LIFE)


def features_of(groups) -> list[str]:
    return [f for g, fs in GROUPS.items() if g in groups for f in fs]


def _f(v) -> float | None:
    try:
        x = float(v)
    except (TypeError, ValueError):
        return None
    return x if math.isfinite(x) else None


def _log1p(v: float | None) -> float | None:
    return None if v is None or v <= -1 else math.log1p(v)


def _ratio(a, b) -> float | None:
    return None if a is None or not b else a / b


def _ts(text_value: str) -> float:
    dt = datetime.fromisoformat(text_value.replace("Z", "+00:00"))
    return (dt if dt.tzinfo else dt.replace(tzinfo=timezone.utc)).timestamp()


def _days_since(as_of: float, when: str | None) -> float | None:
    return (as_of - _ts(when)) / DAY if when else None


def _json(v) -> dict:
    try:
        obj = json.loads(v or "{}")
    except ValueError:
        return {}
    return obj if isinstance(obj, dict) else {}


def _day(ts: float) -> str:
    return iso(ts)[:10]


# -- rows ---------------------------------------------------------------------------------------------------------
def targets(lab: dict) -> dict:
    """Stage 4's labels as the two model targets; None until settled."""
    crash = {"1": 1, "0": 0}.get(str(lab.get("crash_10", "")))
    label = lab.get("label")
    pump = 1 if label == "pump" else 0 if label in ("not_pump", "real_news") else None
    return {"crash": crash, "pump": pump}


def available_at(lab: dict, sessions: dict[int, str], target: str) -> float | None:
    """When a settled label may first train a model: 4 h after the close of the session that settles it."""
    k = 15 if target == "pump" and (_f(lab.get("ret_max_5")) or 0) >= 0.5 else 10
    if k in sessions:
        day = sessions[k]
    elif lab.get("track_status") not in ("active", "", None) and sessions:
        day = sessions[max(sessions)]  # tracking ended first: its last session
    else:
        return None
    return _close_ts(date.fromisoformat(day)) + LABEL_DELAY


def features(snap: dict, ep: dict | None, text_row: dict | None, llm_row: dict | None) -> dict:
    """model-v2 features of one snapshot, from what was known at its flag time (docs/stage5.md); the history group
    is filled in by add_history(), which needs every row."""
    x: dict = dict.fromkeys(FEATURES)
    as_of = float(snap["as_of"])
    if snap.get("role") == "candidate" and ep:
        m = _f(ep.get("mentions_24h")) or 0
        subs, methods = _json(ep.get("by_subreddit")), _json(ep.get("methods"))
        x.update(
            mentions_log=_log1p(m), baseline_log=_log1p(_f(ep.get("baseline_mean"))), spike_z=_f(ep.get("z")),
            authors_ratio=_ratio(_f(ep.get("authors_24h")), m), post_share=_ratio(_f(ep.get("posts_24h")), m),
            hype_share=_ratio(_f(ep.get("hype_docs_24h")), m),
            hype_spike=int("hype_spike" in (ep.get("reasons") or "").split()),
            wsb_share=_ratio(_f(subs.get("wallstreetbets", 0)), m),
            pennystocks_share=_ratio(_f(subs.get("pennystocks", 0)), m),
            cashtag_share=_ratio(_f(methods.get("cashtag", 0)), m),
            stocktwits_trending=int(bool(ep.get("stocktwits_rank"))),
        )
        if text_row:
            x.update({k: _f(text_row.get(k)) for k in text.TEXT_FEATURES})
        if llm_row and llm_row.get("status") == "ok" and llm_row.get("llm_version") == text.LLM_VERSION:
            x.update({k: _f(llm_row.get(k)) for k in text.LLM_FEATURES})
    else:  # a control: nobody was talking about it, by construction
        x.update(mentions_log=0.0, baseline_log=0.0)

    g = lambda k: _f(snap.get(k))  # noqa: E731
    price = g("price_at_flag")
    si, si_prev = g("si_shares"), g("si_prev_shares")
    sec = bool(snap.get("cik"))
    items = {i.strip() for i in (snap.get("last_current_report_items") or "").split(",") if i.strip()}
    renamed = _days_since(as_of, snap.get("last_name_change"))
    listed_days = _days_since(as_of, snap.get("first_trade_date"))
    x.update(
        price_log=math.log(price) if price and price > 0 else None, move_since_close=g("move_since_close"),
        ret_1d=g("ret_1d"), ret_5d=g("ret_5d"), ret_20d=g("ret_20d"), rel_vol_last_log=_log1p(g("rel_vol_last")),
        rel_vol_today_log=_log1p(g("rel_vol_today")), volatility_20d=g("volatility_20d"),
        pct_from_52w_high=g("pct_from_52w_high"), dollar_vol_log=_log1p(g("dollar_vol_20d")),
        market_cap_log=_log1p(g("market_cap")), float_log=_log1p(g("float_shares") or g("shares_outstanding")),
        turnover_last=g("turnover_last"), listing_age_log=None if listed_days is None else _log1p(max(0.0, listed_days)),
        reverse_splits_1y=g("reverse_splits_1y"), otc={"otc": 1, "listed": 0}.get(snap.get("venue") or ""),
        institution_pct=g("institution_pct"),
        si_pct_float=g("si_pct_float"), si_days_to_cover=g("si_days_to_cover"),
        si_change=si / si_prev - 1 if si is not None and si_prev else None,
        sec_filer=int(sec), dilution_90d=g("dilution_filings_90d"), offerings_424b_30d=g("offerings_424b_30d"),
        days_since_dilution=_days_since(as_of, snap.get("last_dilution_at")),
        current_reports_30d=g("current_reports_30d"),
        days_since_report=_days_since(as_of, snap.get("last_current_report_at")),
        report_hard_news=int(bool(items & HARD_NEWS_ITEMS) and bool(snap.get("last_current_report_at"))) if sec else None,
        unregistered_sales_90d=g("unregistered_sales_90d"), late_notices_365d=g("late_filing_notices_365d"),
        name_change_1y=int(renamed is not None and 0 <= renamed <= 365) if sec else None,
    )
    return x


@dataclass
class Row:
    snapshot_id: str
    episode_id: str
    role: str
    ticker: str
    archetype: str
    as_of: float
    x: dict
    y: dict
    avail: dict
    ret10: float | None
    label: str

    @property
    def week(self) -> float:
        return week_start(self.as_of)

    @property
    def holdout(self) -> bool:
        return self.as_of >= HOLDOUT_START


def add_history(rows: list[Row], episodes: list[dict]) -> None:
    """The history group: how often the same stock was flagged before, and how often it then crashed, counting only
    flags before the row's own and crash labels usable before it (no lookahead)."""
    flags: dict[str, list[tuple[float, str]]] = defaultdict(list)
    for e in episodes:
        flags[e["ticker"]].append((float(e["first_flagged_at"]), e["episode_id"]))
    crashes: dict[str, list[tuple[float, str]]] = defaultdict(list)
    for r in rows:
        if r.role == "candidate" and r.y["crash"] == 1 and r.avail["crash"] is not None:
            crashes[r.ticker].append((r.avail["crash"], r.episode_id))
    for r in rows:
        prior = [t for t, eid in flags[r.ticker] if t < r.as_of and eid != r.episode_id]
        r.x.update(prior_flags_90d=sum(1 for t in prior if t >= r.as_of - HISTORY_WINDOW),
                   days_since_prior_flag=(r.as_of - max(prior)) / DAY if prior else None,
                   prior_crashes=sum(1 for t, eid in crashes[r.ticker] if t < r.as_of and eid != r.episode_id))


def load_rows(ds: Datastore) -> list[Row]:
    """One row per priced Stage 2 snapshot, with its features, targets and label availability."""
    episode_list = ds.read_csv("candidates/episodes.csv")
    episodes = {e["episode_id"]: e for e in episode_list}
    labels = {r["snapshot_id"]: r for r in ds.read_csv(LABELS)}
    sessions: dict[str, dict[int, str]] = defaultdict(dict)
    for r in ds.read_csv(DAILY):
        sessions[r["snapshot_id"]][int(r["k"])] = r["session"]
    ret10 = {r["snapshot_id"]: _f(r.get("ret_close_10")) for r in ds.read_csv(OUTCOMES)}
    text_rows = {r["episode_id"]: r for r in ds.read_csv(text.TEXT)}  # the latest row of each episode wins
    llm_rows = {r["episode_id"]: r for r in ds.read_csv(text.LLM)}
    rows = []
    for s in ds.read_csv(SNAPSHOTS):
        if s.get("archetype") in ("", "unknown") or not _f(s.get("price_at_flag")):
            continue
        lab = labels.get(s["snapshot_id"], {})
        sid, eid = s["snapshot_id"], s["episode_id"]
        rows.append(Row(sid, eid, s["role"], s["ticker"], s["archetype"], float(s["as_of"]),
                        features(s, episodes.get(eid), text_rows.get(eid), llm_rows.get(eid)), targets(lab),
                        {t: available_at(lab, sessions[sid], t) for t in TARGETS}, ret10.get(sid), lab.get("label", "")))
    add_history(rows, episode_list)
    return rows


# -- models -------------------------------------------------------------------------------------------------------
def _matrix(rows: list[Row], feats: list[str]):
    import numpy as np

    return np.array([[r.x[f] if r.x[f] is not None else np.nan for f in feats] for r in rows], dtype=float)


@dataclass
class Fitted:
    booster: object
    features: list
    threshold: float
    base_rate: float
    n: int
    pos: int

    def predict(self, rows: list[Row]) -> list[float]:
        if not rows:
            return []
        return [float(p) for p in self.booster.predict(_matrix(rows, self.features))]

    def importance(self, top: int = 8) -> list[tuple[str, float]]:
        gain = self.booster.feature_importance(importance_type="gain")
        total = float(sum(gain)) or 1.0
        ranked = sorted(zip(self.features, gain), key=lambda t: -t[1])
        return [(f, float(v) / total) for f, v in ranked[:top] if v > 0]


@dataclass
class NoModel:
    n: int
    pos: int

    @property
    def note(self) -> str:
        return (f"no model: {self.n} rows and {self.pos} positives were available before the week began "
                f"(needs {MIN_ROWS} and {MIN_POS})")


def fit(rows: list[Row], target: str, cutoff: float, feats: list[str]) -> Fitted | NoModel:
    """The model of the week starting at `cutoff`: every row whose label was usable before it, recency weighted."""
    train = [r for r in rows if r.y[target] is not None and r.avail[target] is not None and r.avail[target] < cutoff]
    pos = sum(r.y[target] for r in train)
    if len(train) < MIN_ROWS or pos < MIN_POS:
        return NoModel(len(train), pos)
    import lightgbm as lgb

    weights = [recency_weight(cutoff - r.as_of) for r in train]
    data = lgb.Dataset(_matrix(train, feats), label=[r.y[target] for r in train], weight=weights,
                       feature_name=list(feats), params={"feature_pre_filter": False, "verbose": -1})
    booster = lgb.train(PARAMS, data, num_boost_round=ROUNDS)
    cands = [(w, r.y[target]) for w, r in zip(weights, train) if r.role == "candidate"]
    base = sum(w * y for w, y in cands) / sum(w for w, _ in cands) if cands else 0.0
    return Fitted(booster, list(feats), LIFT * max(base, MIN_BASE_RATE), base, len(train), pos)


class Trainer:
    """fit() with a cache: one model per (target, week, feature set) per run."""

    def __init__(self, rows: list[Row]):
        self.rows, self.cache = rows, {}

    def fit(self, target: str, cutoff: float, feats: list[str]) -> Fitted | NoModel:
        key = (target, cutoff, tuple(feats))
        if key not in self.cache:
            self.cache[key] = fit(self.rows, target, cutoff, feats)
        return self.cache[key]


def replay(trainer: Trainer, by_week: dict[float, list[Row]], target: str, groups) -> dict[str, tuple[float, bool]]:
    """Out-of-sample scores of the given candidates, each from the model of its own week."""
    feats, out = features_of(groups), {}
    for week in sorted(by_week):
        m = trainer.fit(target, week, feats)
        if isinstance(m, Fitted):
            for r, s in zip(by_week[week], m.predict(by_week[week])):
                out[r.snapshot_id] = (s, s >= m.threshold)
    return out


# -- metrics ------------------------------------------------------------------------------------------------------
def average_precision(items) -> float | None:
    pos = sum(y for y, _, _ in items)
    if not pos:
        return None
    ordered = sorted(items, key=lambda t: -t[1])
    ap, tp, fp, prev, i = 0.0, 0, 0, 0.0, 0
    while i < len(ordered):  # one step per distinct score, so ties are scored together
        score = ordered[i][1]
        while i < len(ordered) and ordered[i][1] == score:
            tp, fp, i = tp + ordered[i][0], fp + 1 - ordered[i][0], i + 1
        ap += (tp / pos - prev) * tp / (tp + fp)
        prev = tp / pos
    return ap


def roc_auc(items) -> float | None:
    n, pos = len(items), sum(y for y, _, _ in items)
    if not pos or pos == n:
        return None
    order = sorted(range(n), key=lambda i: items[i][1])
    ranks, i = [0.0] * n, 0
    while i < n:
        j = i
        while j + 1 < n and items[order[j + 1]][1] == items[order[i]][1]:
            j += 1
        for k in range(i, j + 1):
            ranks[order[k]] = (i + j) / 2 + 1
        i = j + 1
    rank_sum = sum(r for r, it in zip(ranks, items) if it[0])
    return (rank_sum - pos * (pos + 1) / 2) / (pos * (n - pos))


def metrics(items) -> dict:
    """items: (y, score, flagged). Precision, recall and F1 of the flag; AP and AUC of the score."""
    n = len(items)
    pos = sum(y for y, _, _ in items)
    flagged = sum(1 for _, _, f in items if f)
    tp = sum(1 for y, _, f in items if y and f)
    precision = tp / flagged if flagged else None
    recall = tp / pos if pos else None
    f1 = None
    if precision is not None and recall is not None:
        f1 = 2 * precision * recall / (precision + recall) if precision + recall else 0.0
    base = pos / n if n else None
    return {"n": n, "positives": pos, "flagged": flagged, "base_rate": base, "precision": precision, "recall": recall,
            "f1": f1, "lift": precision / base if precision is not None and base else None,
            "ap": average_precision(items), "auc": roc_auc(items)}


def split_blocks(weeks, n: int = 3) -> list[list] | None:
    """Consecutive blocks of weeks, as equal in length as possible (earlier blocks take the extra week)."""
    weeks = sorted(weeks)
    if len(weeks) < n:
        return None
    size, extra = divmod(len(weeks), n)
    out, i = [], 0
    for b in range(n):
        k = size + (1 if b < extra else 0)
        out.append(weeks[i:i + k])
        i += k
    return out


def _m(items: list[dict]) -> dict:
    return metrics([(it["y"], it["score"], it["flagged"]) for it in items])


def _pct(v) -> str:
    return "-" if v is None else f"{v:.0%}" if abs(v) >= 0.1 or v == 0 else f"{v:.1%}"


def _num2(v) -> str:
    return "-" if v is None else f"{v:.2f}"


def robustness(items: list[dict]) -> list[dict]:
    """The five checks of docs/stage5.md on scored, settled candidates.

    items: dicts with y, score, flagged, week, archetype, ret10 (Stage 3's ret_close_10) and control_ys (the settled
    targets of the candidate's own matched controls)."""
    out = []

    def add(check, status, detail=""):
        out.append({"check": check, "status": status, "detail": detail})

    m = _m(items)
    if m["positives"] < 10:
        add("beats the base rate", "not enough data", f"{m['positives']} positives (needs 10)")
    else:
        ok = m["precision"] is not None and m["precision"] >= 1.5 * m["base_rate"] and (m["ap"] or 0) > m["base_rate"]
        add("beats the base rate", "pass" if ok else "fail",
            f"precision {_pct(m['precision'])} vs base rate {_pct(m['base_rate'])}; AP {_num2(m['ap'])}")

    blocks = split_blocks({it["week"] for it in items})
    bm = [_m([it for it in items if it["week"] in b]) for b in blocks] if blocks else []
    if not blocks or any(b["positives"] < 3 for b in bm):
        add("separate periods", "not enough data", "needs 3 positives in each of three blocks of weeks")
    else:
        ok = all(b["precision"] is not None and b["precision"] > b["base_rate"] for b in bm)
        add("separate periods", "pass" if ok else "fail",
            "; ".join(f"precision {_pct(b['precision'])} vs {_pct(b['base_rate'])}" for b in bm))

    evaluated = [(a, _m([it for it in items if it["archetype"] == a])) for a in PUMP_TYPES]
    evaluated = [(a, am) for a, am in evaluated if am["positives"] >= 5]
    if not evaluated:
        add("per pump type", "not enough data", "needs 5 positives in a pump type")
    else:
        ok = all(am["precision"] is not None and am["precision"] > am["base_rate"] for _, am in evaluated)
        add("per pump type", "pass" if ok else "fail", "; ".join(
            f"{a.replace('_', ' ')}: precision {_pct(am['precision'])} vs {_pct(am['base_rate'])}" for a, am in evaluated))

    flagged = [it for it in items if it["flagged"] and it["control_ys"]]
    if len(flagged) < 10:
        add("beats the control group", "not enough data", f"{len(flagged)} flagged with settled controls (needs 10)")
    else:
        rate = statistics.mean(it["y"] for it in flagged)
        control = statistics.mean(c for it in flagged for c in it["control_ys"])
        add("beats the control group", "pass" if rate > control else "fail",
            f"flagged {_pct(rate)} vs their controls {_pct(control)}")

    f10 = [it["ret10"] for it in items if it["flagged"] and it["ret10"] is not None]
    u10 = [it["ret10"] for it in items if not it["flagged"] and it["ret10"] is not None]
    if len(f10) < 10 or not u10:
        add("survives slippage", "not enough data", f"{len(f10)} flagged with a 10-session return (needs 10)")
    else:
        fm, um = statistics.mean(f10), statistics.mean(u10)
        add("survives slippage", "pass" if fm <= -0.03 and fm < um else "fail",
            f"flagged mean 10-session return {fm:+.1%} vs unflagged {um:+.1%} (needs -3% or lower)")
    return out


def is_robust(checks: list[dict]) -> bool:
    return bool(checks) and all(c["status"] == "pass" for c in checks)


def _not_lower(a, b) -> bool:
    if a is None or b is None:
        return a is None and b is None
    return a >= b - 1e-12


def weak_groups(everything: tuple, without: dict) -> list[str]:
    """Groups whose removal doesn't lower AP, pooled and in at least two of the three blocks (never all of them)."""
    ap_all, blocks_all = everything
    weak = [g for g in GROUPS if g in without and _not_lower(without[g][0], ap_all)
            and sum(_not_lower(a, b) for a, b in zip(without[g][1], blocks_all)) >= 2]
    return [] if len(weak) == len(GROUPS) else weak


# -- text features and LLM ratings ------------------------------------------------------------------------------------
def _computable(as_of: float, raw_since: date | None, first_day: date | None) -> bool:
    """Whether the raw files holding the flag's documents (collected the day before or on the flag's day) are here."""
    if raw_since is None:
        return True
    flag_day = datetime.fromtimestamp(as_of, timezone.utc).date()
    return all(d >= raw_since or (first_day is not None and d < first_day) for d in (flag_day - timedelta(days=1), flag_day))


def _documents(ds: Datastore, episodes: list[dict]) -> dict[str, list[dict]]:
    """The flag documents of each episode, rebuilt from the raw files the way Stage 1 counted them."""
    days = set()
    for e in episodes:
        d = datetime.fromtimestamp(float(e["first_flagged_at"]), timezone.utc).date()
        days |= {d, d - timedelta(days=1)}
    names = {e["ticker"].split(":")[-1].lower() for e in episodes}
    conn = db.connect()
    for path in ds.raw_files():
        y, m, d = (int(p) for p in path.parent.parts[-3:])
        if date(y, m, d) not in days:
            continue
        with gzip.open(path, "rt", encoding="utf-8") as fh:
            records = [json.loads(line) for line in fh if line.strip()]
        # cheap prefilter: only documents that contain one of the tickers can mention it
        db.insert_docs(conn, (r for r in records
                              if any(n in f"{r.get('title') or ''} {r.get('body') or ''}".lower() for n in names)))
    db.extract_mentions(conn, default_extractor(load_symbols(ds).keys()), Settings().excluded_authors)
    return {e["episode_id"]: text.flag_documents(conn, e["ticker"], float(e["first_flagged_at"])) for e in episodes}


def _upgrade_header(ds: Datastore, rel: str, fields: list[str]) -> None:
    """Rewrite an append-only table under a newer header (columns are only ever added), keeping every row."""
    p = ds.path(rel)
    if not p.exists() or not p.stat().st_size:
        return
    with p.open(newline="", encoding="utf-8") as fh:
        header = next(csv.reader(fh), [])
    if header != fields:
        ds.write_csv(rel, fields, ds.read_csv(rel))


def update_text(ds: Datastore, llm, now: float, raw_since: date | None, summary: dict, llm_budget_s: float | None = None,
                timer: Callable[[], float] = time.monotonic) -> None:
    """Append text features and LLM ratings (the current versions) of candidates that don't have them yet. A
    candidate done by an older version is redone while its raw files are checked out; its old rows stay."""
    episodes = ds.read_csv("candidates/episodes.csv")
    snaps = {s["episode_id"]: s for s in ds.read_csv(SNAPSHOTS)
             if s["role"] == "candidate" and s.get("archetype") not in ("", "unknown")}
    _upgrade_header(ds, text.TEXT, text.TEXT_FIELDS)
    _upgrade_header(ds, text.LLM, text.LLM_FIELDS)
    have_text = {r["episode_id"] for r in ds.read_csv(text.TEXT) if r.get("text_version") == text.TEXT_VERSION}
    llm_rows = ds.read_csv(text.LLM)
    have_llm = {r["episode_id"] for r in llm_rows if r.get("llm_version") == text.LLM_VERSION}
    rated_before = {r["episode_id"] for r in llm_rows}  # by any version: already scored, nothing waits for a redo
    state = json.loads(ds.path(STATE).read_text()) if ds.path(STATE).exists() else {}
    attempts = state.setdefault("llm_attempts", {})
    live_since = ds.load_state().get("live_since")
    first_day = datetime.fromtimestamp(live_since, timezone.utc).date() if live_since else None

    def rating_row(e, status, docs=(), rating=None, sha="", error=""):
        return {"episode_id": e["episode_id"], "ticker": e["ticker"], "as_of_utc": e["first_flagged_at_utc"],
                "status": status, **(rating or {}), "n_docs": len(docs), "prompt_sha": sha,
                "model": getattr(llm, "model", ""), "rated_at_utc": iso(now), "error": error[:300],
                "llm_version": text.LLM_VERSION}

    new_text, new_llm = [], []
    want_llm = [e for e in episodes if llm is not None and e["episode_id"] in snaps and e["episode_id"] not in have_llm]
    for e in want_llm:  # out of retries: give up on it (a redo is never given up: the candidate has a rating)
        if e["episode_id"] not in rated_before and now - float(e["first_flagged_at"]) >= LLM_RETRY:
            last = attempts.pop(e["episode_id"], {}).get("error", "")
            new_llm.append(rating_row(e, "failed", error=last or "no rating within 3 days of the flag"))
    gave_up = {r["episode_id"] for r in new_llm}
    todo = [e for e in episodes
            if (e["episode_id"] not in have_text or (e in want_llm and e["episode_id"] not in gave_up))
            and _computable(float(e["first_flagged_at"]), raw_since, first_day)]
    docs_of = _documents(ds, todo) if todo else {}
    started, blocked = timer(), False
    for e in todo:
        eid, docs, as_of = e["episode_id"], docs_of[e["episode_id"]], float(e["first_flagged_at"])
        if eid not in have_text:
            new_text.append({"episode_id": eid, "ticker": e["ticker"], "as_of_utc": e["first_flagged_at_utc"],
                             **text.text_features(docs, e["ticker"]), "computed_at_utc": iso(now),
                             "text_version": text.TEXT_VERSION})
        if e not in want_llm or eid in gave_up:
            continue
        if not docs:
            new_llm.append(rating_row(e, "no_documents"))
            continue
        if blocked or (llm_budget_s is not None and timer() - started >= llm_budget_s):
            continue  # left for the next run
        p = text.build_prompt(snaps[eid], docs, as_of)
        sha = text.prompt_sha(p.system, p.user)
        try:
            answer = llm.complete(p.system, p.user, p.schema)
        except text.LLMRefused as exc:
            new_llm.append(rating_row(e, "failed", docs, sha=sha, error=str(exc)))
            attempts.pop(eid, None)
            continue
        except text.LLMError as exc:  # server down or busy: try again on a later run, and leave the rest for it
            a = attempts.setdefault(eid, {"n": 0})
            a.update(n=a["n"] + 1, error=str(exc)[:300], at=iso(now))
            blocked = True
            summary["warnings"].append(f"llm: {exc}"[:200])
            continue
        attempts.pop(eid, None)
        try:
            new_llm.append(rating_row(e, "ok", docs, text.parse_rating(answer, p), sha))
        except ValueError as exc:  # the same prompt gets the same answer at temperature 0: no point retrying
            new_llm.append(rating_row(e, "failed", docs, sha=sha, error=f"unparseable: {exc}: {answer[:200]}"))
    ds.append_csv(text.TEXT, text.TEXT_FIELDS, new_text)
    ds.append_csv(text.LLM, text.LLM_FIELDS, new_llm)
    ds.write_text(STATE, json.dumps(state, indent=2, sort_keys=True) + "\n")
    summary["text"] = len(new_text)
    rated = rated_before | {r["episode_id"] for r in new_llm}
    summary["llm"] = {"ok": sum(r["status"] == "ok" for r in new_llm),
                      "failed": sum(r["status"] == "failed" for r in new_llm),
                      "waiting": sum(1 for e in want_llm if e["episode_id"] not in rated)}


def evaluate_llm(ds: Datastore, llm, raw_since: date | None, gold: dict | None = None,
                 timer: Callable[[], float] = time.monotonic) -> tuple[list[dict], list[str]]:
    """Rate every candidate whose flag documents are checked out with the current prompt, and, given hand labels
    ({episode_id: {"docs": [doc ids labelled], list: {"yes": [doc ids], "maybe": [doc ids]}}}), count the right,
    wrong and missed documents of each list ("maybe" documents count neither way). Only labelled documents that the
    prompt still shows are scored. For testing a prompt or model: writes nothing."""
    snaps = {s["episode_id"]: s for s in ds.read_csv(SNAPSHOTS)
             if s["role"] == "candidate" and s.get("archetype") not in ("", "unknown")}
    live_since = ds.load_state().get("live_since")
    first_day = datetime.fromtimestamp(live_since, timezone.utc).date() if live_since else None
    todo = [e for e in ds.read_csv("candidates/episodes.csv")
            if e["episode_id"] in snaps and _computable(float(e["first_flagged_at"]), raw_since, first_day)]
    docs_of = _documents(ds, todo) if todo else {}
    rows, counts, quotes, seconds, scored, details = [], {k: [0, 0, 0] for k in text.LLM_LISTS}, Counter(), [], 0, []
    for e in todo:
        eid, docs = e["episode_id"], docs_of[e["episode_id"]]
        if not docs:
            continue
        p = text.build_prompt(snaps[eid], docs, float(e["first_flagged_at"]))
        ids = [d["id"] for d in p.docs]
        row = {"episode_id": eid, "ticker": e["ticker"], "n_docs": len(docs), "model": getattr(llm, "model", ""),
               "doc_ids": json.dumps(ids)}
        t0 = timer()
        try:
            answer = llm.complete(p.system, p.user, p.schema)
            row.update(seconds=round(timer() - t0, 1), answer=answer[:3000])
            row.update(text.parse_rating(answer, p), status="ok")
            seconds.append(row["seconds"])
        except (text.LLMError, ValueError) as exc:
            rows.append({**row, "status": "failed", "error": str(exc)[:300]})
            continue
        rows.append(row)
        quotes[row["llm_checks"].split()[0]] += 1
        labels = (gold or {}).get(eid)
        if not labels:
            continue
        lists = json.loads(row["llm_lists"])
        judged = set(ids) & set(labels.get("docs", ids))
        scored += len(judged)
        errors = []
        for k in text.LLM_LISTS:
            said = {ids[i - 1] for i in lists[k]} & judged
            yes, maybe = (set(labels.get(k, {}).get(w, [])) & judged for w in ("yes", "maybe"))
            counts[k][0] += len(said & yes)
            counts[k][1] += len(said - yes - maybe)
            counts[k][2] += len(yes - said)
            for what, wrong in (("wrong", said - yes - maybe), ("missed", yes - said)):
                if wrong:
                    errors.append(f"{k} {what} {sorted(ids.index(d) + 1 for d in wrong)}")
        details.append(f"{e['ticker']}: " + ("; ".join(errors) or "all right"))
    lines = [f"{len([r for r in rows if r['status'] == 'ok'])} of {len(rows)} candidates rated"
             + (f", {statistics.mean(seconds):.0f} s each on average (longest {max(seconds):.0f} s)" if seconds else ""),
             f"quotes: {quotes['quote=ok']} found, {quotes['quote=failed']} not found, {quotes['quote=none']} without events"]
    if gold:
        lines += [f"{scored} hand-labelled documents shown"]
        lines += [f"{k}: {r} right, {w} wrong, {m} missed" for k, (r, w, m) in counts.items()]
        lines += ["", "By candidate (document numbers as in the prompt):", *details]
    return rows, lines


# -- the run ------------------------------------------------------------------------------------------------------
def _item(r: Row, target: str, score: float, flagged: bool, controls: dict[str, list[Row]]) -> dict:
    return {"y": r.y[target], "score": score, "flagged": bool(flagged), "week": r.week, "archetype": r.archetype,
            "ret10": r.ret10, "control_ys": [c.y[target] for c in controls.get(r.episode_id, []) if c.y[target] is not None]}


def _evaluate(items: list[dict]) -> dict:
    blocks = split_blocks({it["week"] for it in items})
    groups = {"all candidates": items}
    groups.update({a.replace("_", " "): [it for it in items if it["archetype"] == a] for a in ARCHETYPES})
    groups["pump types together"] = [it for it in items if it["archetype"] in PUMP_TYPES]
    for i, b in enumerate(blocks or [], 1):
        groups[f"weeks of {_day(b[0])} to {_day(b[-1])}"] = [it for it in items if it["week"] in b]
    return {"table": {k: _m(v) for k, v in groups.items()}, "checks": robustness(items), "blocks": blocks}


def development(trainer: Trainer, rows: list[Row]) -> dict:
    """The walk-forward replay of every development week, per target (docs/stage5.md)."""
    dev = [r for r in rows if r.role == "candidate" and not r.holdout]
    by_week: dict[float, list[Row]] = defaultdict(list)
    for r in sorted(dev, key=lambda r: r.as_of):
        by_week[r.week].append(r)
    controls: dict[str, list[Row]] = defaultdict(list)
    for r in rows:
        if r.role == "control":
            controls[r.episode_id].append(r)
    out = {}
    for t in TARGETS:
        scores = {"all groups": replay(trainer, by_week, t, GROUPS)}

        def items_of(sc):
            return [_item(r, t, *sc[r.snapshot_id], controls) for r in dev
                    if r.snapshot_id in sc and r.y[t] is not None]

        items = items_of(scores["all groups"])
        blocks = split_blocks({it["week"] for it in items})
        weak, without = [], {}
        if sum(it["y"] for it in items) >= PRUNE_MIN_POS and blocks:
            def ap_by_block(its):
                return (_m(its)["ap"], [_m([it for it in its if it["week"] in b])["ap"] for b in blocks])

            for g in GROUPS:
                without[g] = ap_by_block(items_of(replay(trainer, by_week, t, [x for x in GROUPS if x != g])))
            weak = weak_groups(ap_by_block(items), without)
        deployed = [g for g in GROUPS if g not in weak]
        if weak:
            scores["deployed (pruned; picked on these weeks)"] = replay(trainer, by_week, t, deployed)
        scores["market only"] = replay(trainer, by_week, t, MARKET_GROUPS)
        scores["social only"] = replay(trainer, by_week, t, SOCIAL_GROUPS)
        out[t] = {"scores": scores, "items": items, "deployed": deployed, "weak": weak, "without": without,
                  "compare": {name: _m(items_of(sc)) for name, sc in scores.items()}, **_evaluate(items)}
    return out


def score_new(ds: Datastore, trainer: Trainer, rows: list[Row], deployed: dict, llm_ready: Callable[[str], bool],
              now: float) -> list[dict]:
    """Append the prospective score of every candidate not yet logged (once per candidate and target)."""
    logged = {(p["snapshot_id"], p["target"]) for p in ds.read_csv(PREDICTIONS)}
    new = []
    for r in sorted((r for r in rows if r.role == "candidate"), key=lambda r: r.as_of):
        if not llm_ready(r.episode_id):
            continue
        for t in TARGETS:
            if (r.snapshot_id, t) in logged:
                continue
            m = trainer.fit(t, r.week, features_of(deployed[t]))
            row = {"snapshot_id": r.snapshot_id, "episode_id": r.episode_id, "ticker": r.ticker, "as_of_utc": iso(r.as_of),
                   "archetype": r.archetype, "week_utc": _day(r.week), "target": t, "n_train": m.n, "n_pos": m.pos,
                   "groups": " ".join(deployed[t]), "holdout": int(r.holdout), "scored_at_utc": iso(now),
                   "model_version": MODEL_VERSION}
            if isinstance(m, Fitted):
                s = m.predict([r])[0]
                row.update(score=round(s, 6), threshold=round(m.threshold, 6), flagged=int(s >= m.threshold))
            else:
                row["note"] = m.note
            new.append(row)
    ds.append_csv(PREDICTIONS, PREDICTION_FIELDS, new)
    return new


def holdout_status(ds: Datastore, rows: list[Row], now: float) -> str:
    """locked, ready (to evaluate now) or evaluated (earlier: never again)."""
    if ds.path(HOLDOUT_MD).exists():
        return "evaluated"
    if collection_done(ds, ds.load_state(), now, Settings()) is None:
        return "locked"
    labels = {r["snapshot_id"]: r["label"] for r in ds.read_csv(LABELS)}
    hold = [s for s in ds.read_csv(SNAPSHOTS)
            if float(s["as_of"]) >= HOLDOUT_START and s.get("archetype") not in ("", "unknown")]
    if any(labels.get(s["snapshot_id"]) == "pending" for s in hold):
        return "locked"
    last_flag = max((float(s["as_of"]) for s in hold), default=HOLDOUT_START)
    if any(s["snapshot_id"] not in labels for s in hold) and now < last_flag + HOLDOUT_GRACE:
        return "locked"
    logged = {(p["snapshot_id"], p["target"]) for p in ds.read_csv(PREDICTIONS)}
    if any((r.snapshot_id, t) not in logged for r in rows if r.role == "candidate" and r.holdout for t in TARGETS):
        return "locked"
    return "ready"


def evaluate_holdout(ds: Datastore, rows: list[Row], now: float) -> None:
    """The one and only evaluation of the hold-out, from the prospective log."""
    by_sid = {r.snapshot_id: r for r in rows}
    controls: dict[str, list[Row]] = defaultdict(list)
    for r in rows:
        if r.role == "control":
            controls[r.episode_id].append(r)
    out_rows, results = [], {}
    preds = [p for p in ds.read_csv(PREDICTIONS) if p["holdout"] == "1" and p["snapshot_id"] in by_sid]
    for t in TARGETS:
        items = []
        for p in (p for p in preds if p["target"] == t):
            r = by_sid[p["snapshot_id"]]
            out_rows.append({**{k: p[k] for k in KEY_FIELDS}, "week_utc": p["week_utc"], "target": t,
                             "score": p["score"], "flagged": p["flagged"],
                             "y": "" if r.y[t] is None else r.y[t], "ret_close_10": "" if r.ret10 is None else r.ret10})
            if p["score"] != "" and r.y[t] is not None:
                items.append(_item(r, t, float(p["score"]), p["flagged"] == "1", controls))
        unscored = sum(1 for p in preds if p["target"] == t and p["score"] == "")
        results[t] = {**_evaluate(items), "unscored": unscored}
    ds.write_csv(HOLDOUT_CSV, HOLDOUT_FIELDS, out_rows)
    lines = ["# Stage 5 hold-out evaluation", "",
             f"Computed once, {iso(now)}, from the prospective log (`model/predictions.csv`): every hold-out candidate "
             f"(flagged on or after {_day(HOLDOUT_START)}) was scored before its outcome existed, by the model of its "
             f"week. Rule `{MODEL_VERSION}` (docs/stage5.md on the code branch). This file is never recomputed.", ""]
    for t in TARGETS:
        res = results[t]
        lines += [f"## {t}", ""]
        if res["unscored"]:
            lines += [f"{res['unscored']} hold-out candidates had no model for their week and are left out.", ""]
        lines += _table(res["table"]) + [""] + _checks(res["checks"]) + [""]
    ds.write_text(HOLDOUT_MD, "\n".join(lines))


def run_model(ds: Datastore, llm=None, clock: Callable[[], float] = time.time, raw_since: date | None = None,
              llm_budget_s: float | None = None, timer: Callable[[], float] = time.monotonic) -> dict:
    now = clock()
    summary: dict = {"text": 0, "llm": {"ok": 0, "failed": 0, "waiting": 0}, "scored": 0, "models": {}, "dev": {},
                     "holdout": "locked", "finished": False, "warnings": []}
    update_text(ds, llm, now, raw_since, summary, llm_budget_s, timer)
    rows = load_rows(ds)
    trainer = Trainer(rows)
    dev = development(trainer, rows)
    deployed = {t: dev[t]["deployed"] for t in TARGETS}
    rated = {r["episode_id"] for r in ds.read_csv(text.LLM)}
    new = score_new(ds, trainer, rows, deployed, lambda eid: llm is None or eid in rated, now)
    summary["scored"] = len({p["snapshot_id"] for p in new})

    this_week = week_start(now)
    current = {t: trainer.fit(t, this_week, features_of(deployed[t])) for t in TARGETS}
    for t, m in current.items():
        summary["models"][t] = (f"trained on {m.n} rows ({m.pos} positives)" if isinstance(m, Fitted) else m.note)
        summary["dev"][t] = dev[t]["table"]["all candidates"]

    status = holdout_status(ds, rows, now)
    if status == "ready":
        evaluate_holdout(ds, rows, now)
        status = "evaluated"
        summary["holdout"] = "evaluated"
    elif status == "evaluated":
        summary["holdout"] = "evaluated earlier"
    summary["finished"] = status == "evaluated"

    write_walkforward(ds, rows, dev)
    ds.write_text(README, render_readme(ds, rows, dev, current, now, status))
    return summary


# -- outputs ------------------------------------------------------------------------------------------------------
def write_walkforward(ds: Datastore, rows: list[Row], dev: dict) -> None:
    out = []
    for r in sorted(rows, key=lambda r: r.as_of):
        if r.role != "candidate" or r.holdout:
            continue
        row = {"snapshot_id": r.snapshot_id, "episode_id": r.episode_id, "ticker": r.ticker, "as_of_utc": iso(r.as_of),
               "archetype": r.archetype, "week_utc": _day(r.week), "ret_close_10": "" if r.ret10 is None else r.ret10}
        scored = False
        for t in TARGETS:
            all_sc = dev[t]["scores"]["all groups"].get(r.snapshot_id)
            dep = next((v for k, v in dev[t]["scores"].items() if k.startswith("deployed")), dev[t]["scores"]["all groups"])
            dep_sc = dep.get(r.snapshot_id)
            row[t] = "" if r.y[t] is None else r.y[t]
            if all_sc:
                scored = True
                row.update({f"{t}_score": round(all_sc[0], 6), f"{t}_flagged": int(all_sc[1])})
            if dep_sc:
                row.update({f"{t}_score_deployed": round(dep_sc[0], 6), f"{t}_flagged_deployed": int(dep_sc[1])})
        if scored:
            out.append(row)
    ds.write_csv(WALKFORWARD, WALKFORWARD_FIELDS, out)


def _table(table: dict) -> list[str]:
    lines = ["| Candidates | n | Positives | Base rate | Flagged | Precision | Recall | F1 | Lift | AP | AUC |",
             "|---|---|---|---|---|---|---|---|---|---|---|"]
    for name, m in table.items():
        if not m["n"]:
            continue
        lift = "-" if m["lift"] is None else f"{m['lift']:.1f}x"
        lines.append(f"| {name} | {m['n']} | {m['positives']} | {_pct(m['base_rate'])} | {m['flagged']} | "
                     f"{_pct(m['precision'])} | {_pct(m['recall'])} | {_num2(m['f1'])} | {lift} | {_num2(m['ap'])} | "
                     f"{_num2(m['auc'])} |")
    return lines


def _checks(checks: list[dict]) -> list[str]:
    lines = ["| Robustness check | Result | Detail |", "|---|---|---|"]
    lines += [f"| {c['check']} | {c['status']} | {c['detail']} |" for c in checks]
    verdict = ("**robust**: all five checks pass" if is_robust(checks) else
               "**not robust yet**" + (" (some checks need more labels)" if any(
                   c["status"] == "not enough data" for c in checks) else ""))
    return lines + ["", f"Verdict: {verdict}."]


def render_readme(ds: Datastore, rows: list[Row], dev: dict, current: dict, now: float, holdout: str) -> str:
    lines = [
        "# Stage 5 model", "",
        f"Updated {iso(now)}. Rule `{MODEL_VERSION}` (docs/stage5.md on the code branch), written down before any model "
        "was trained. Every candidate is scored once, by the LightGBM model of the week it was flagged in (trained on the "
        "labels available before that week began, recent ones weighted more), and the score goes into the prospective "
        "log `model/predictions.csv`. **crash**: a close 40% or more below the flag price within 10 sessions (the avoid "
        "signal, first). **pump**: Stage 4's pump label. A candidate is flagged when its score is at least twice the "
        "base rate.", "",
        f"## This week's models (week of {_day(week_start(now))})", "",
        "| Target | Status | Trained on | Positives | Base rate | Flag at | Feature groups |", "|---|---|---|---|---|---|---|",
    ]
    for t in TARGETS:
        m = current[t]
        groups = ", ".join(dev[t]["deployed"])
        if isinstance(m, Fitted):
            lines.append(f"| {t} | trained | {m.n} rows | {m.pos} | {_pct(m.base_rate)} | {_pct(m.threshold)} | {groups} |")
        else:
            lines.append(f"| {t} | no model yet | {m.n} rows | {m.pos} | - | - | {groups} |")
    if not all(isinstance(m, Fitted) for m in current.values()):
        lines += ["", f"A week's model needs {MIN_ROWS} rows and {MIN_POS} positives whose labels were settled before "
                      "the week began; a label settles 10 sessions (two weeks) after the flag, 15 after a 50% rise."]
    for t, m in current.items():
        if isinstance(m, Fitted) and m.importance():
            lines += ["", f"What this week's {t} model leans on (share of split gain): "
                      + ", ".join(f"`{f}` {v:.0%}" for f, v in m.importance()) + "."]

    # latest prospective scores
    preds = ds.read_csv(PREDICTIONS)
    ratings = {r["episode_id"]: r for r in ds.read_csv(text.LLM)}
    recent: dict[str, dict] = {}
    for p in preds:
        if p["as_of_utc"] >= iso(now - 7 * DAY):
            recent.setdefault(p["snapshot_id"], {"p": p})[p["target"]] = p
    lines += ["", "## Latest candidates (last 7 days)", ""]
    if not recent:
        lines.append("No candidates scored in the last 7 days.")
    else:
        lines += ["Scores as logged when each candidate was first seen; flagged ones in bold. The LLM column gives the "
                  "shares of the posts shown that are about the company, pitch it, warn about it and state a company "
                  "event (counted only when its quote checks out).", "",
                  "| Flagged (UTC) | Ticker | Archetype | Crash risk | Pump risk | LLM about / pitch / warning / event | "
                  "What the chatter was about |", "|---|---|---|---|---|---|---|"]

        def risk(p):
            if not p or p["score"] == "":
                return "no model"
            s = _pct(float(p["score"]))
            return f"**{s}**" if p["flagged"] == "1" else s

        for v in sorted(recent.values(), key=lambda v: v["p"]["as_of_utc"], reverse=True)[:40]:
            p, rt = v["p"], ratings.get(v["p"]["episode_id"], {})
            if rt.get("status") == "ok" and rt.get("llm_version") == text.LLM_VERSION:
                llm = " / ".join(_pct(_f(rt.get(f"llm_{k}_share"))) for k in ("about", "pitch", "warning", "event"))
            elif rt.get("status") == "ok":
                llm = f"older version ({rt.get('llm_version') or 'llm-v1'})"
            else:
                llm = rt.get("status", "").replace("_", " ") or "-"
            about = (rt.get("llm_summary") or "").replace("|", "/")
            lines.append(f"| {p['as_of_utc'][:16].replace('T', ' ')} | {p['ticker']} | {p['archetype'].replace('_', ' ')} | "
                         f"{risk(v.get('crash'))} | {risk(v.get('pump'))} | {llm} | {about} |")

    lines += ["", f"## Development walk-forward (flags before {_day(HOLDOUT_START)})", "",
              "Each development week replayed exactly as it would have run: its model trained only on labels available "
              "before the week began, scoring that week's candidates. Results count candidates whose label has settled.",
              ""]
    for t in TARGETS:
        d = dev[t]
        lines += [f"### {t}", ""]
        if not d["items"]:
            lines += ["No scored candidate with a settled label yet.", ""]
            continue
        lines += _table(d["table"]) + ["", "| Model | AP | Precision | Recall | F1 |", "|---|---|---|---|---|"]
        for name, m in d["compare"].items():
            lines.append(f"| {name} | {_num2(m['ap'])} | {_pct(m['precision'])} | {_pct(m['recall'])} | {_num2(m['f1'])} |")
        lines += [""] + _checks(d["checks"]) + [""]
        pos = sum(it["y"] for it in d["items"])
        if not d["without"]:
            lines.append(f"Feature groups: all used; weak groups are pruned once the replay holds {PRUNE_MIN_POS} "
                         f"positive candidates ({pos} so far).")
        else:
            ap_all = d["table"]["all candidates"]["ap"]
            lines.append("Feature groups (AP with all groups " + _num2(ap_all) + "; without each: " + ", ".join(
                f"{g} {_num2(v[0])}" for g, v in d["without"].items()) + "). " +
                         (f"Pruned as weak: {', '.join(d['weak'])}." if d["weak"] else "None is weak."))
        lines.append("")

    n_hold = sum(1 for r in rows if r.role == "candidate" and r.holdout)
    lines += [f"## Hold-out (flags from {_day(HOLDOUT_START)})", ""]
    if holdout == "evaluated":
        lines.append("Evaluated once, after collection ended: see `model/holdout.md`.")
    else:
        lines.append(f"Still locked, with {n_hold} hold-out candidates so far. They are scored like any other, but "
                     "their scores are not compared with their outcomes until collection has finished and every hold-out "
                     "label has settled; then they are evaluated once, into `model/holdout.md`.")
    return "\n".join(lines) + "\n"
