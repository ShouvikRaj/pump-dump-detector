"""Stage 3: follow every candidate and control after its flag, one trading session at a time.

Once a day (the `track` workflow, after the US close) this reads market/snapshots.csv and, for each snapshot
still being followed, appends every newly finished session's daily bar to track/daily.csv and every SEC filing
accepted since the flag to track/filings.csv, each with the time it was collected. track/outcomes.csv is then
rebuilt from those rows and Stage 1's daily mention counts: the post-flag path (peak, drawdown, returns, filings,
chatter) that Stage 4 labels from. A
ticker is followed for 20 sessions after its flag (45 calendar days at most), then left alone, so tracking ends
by itself once collection has. Design and definitions: docs/stage3.md.
"""

from __future__ import annotations

import json
import time
from collections import defaultdict
from datetime import date, datetime, timedelta
from typing import Callable

from .features import _accepted_ts, CURRENT_REPORT_FORMS, DAY, DILUTION_FORMS, ET, SESSION_CLOSE, SESSION_OPEN, et_date, iso, utc_date
from .market import SNAPSHOTS, MarketSources
from .sources import edgar
from .sources.yahoo import NoData, SourceError
from .store import Datastore

TRACK_VERSION = "track-v1"
SESSIONS = 20  # sessions followed after the flag
MAX_DAYS = 45  # calendar days after the flag before a ticker is dropped (delisted, halted, no data)
SETTLE_S = 3600  # a session is recorded once its close is an hour old

DAILY = "track/daily.csv"
FILINGS = "track/filings.csv"
OUTCOMES = "track/outcomes.csv"
STATE = "track/state.json"
README = "track/README.md"

KEY_FIELDS = ["snapshot_id", "episode_id", "role", "ticker"]
DAILY_FIELDS = [*KEY_FIELDS, "session", "k", "open", "high", "low", "close", "volume", "adj_factor",
                "collected_at", "collected_at_utc", "track_version"]
FILING_FIELDS = [*KEY_FIELDS, "form", "accepted_at_utc", "items", "k", "collected_at", "collected_at_utc", "track_version",
                 "accession"]
# data.sec.gov serves a filing's acceptanceDateTime 4 hours later (5 in winter) once it is no longer new: 16 filings
# read on 2026-10-05 came back +4 h on 2026-10-06, some of them after the time we had first seen them. The first
# value is the right one, so filings are keyed on their accession number and keep the time first seen.
SEC_SHIFTS = (4 * 3600, 5 * 3600)
OUTCOME_FIELDS = [*KEY_FIELDS, "archetype", "as_of_utc", "base_price", "status", "sessions", "flag_in_session_1",
                  "max_high_5", "ret_max_5", "peak_k_5", "min_low_10_after_peak", "drop_from_peak_10",
                  "ret_close_1", "ret_close_5", "ret_close_10", "ret_close_20",
                  "current_reports_10", "dilution_filings_20", "mentions_next_5d", "mentions_next_20d",
                  "updated_at_utc", "track_version"]


def _close_ts(day: date) -> float:
    return datetime.combine(day, SESSION_CLOSE, ET).timestamp()


def _open_ts(day: date) -> float:
    return datetime.combine(day, SESSION_OPEN, ET).timestamp()


def split_factor(splits: list[dict], as_of: float) -> float:
    """How much the splits after the flag scaled Yahoo's prices: served price = flag-basis price x factor."""
    f = 1.0
    for s in splits:
        if s["t"] > as_of and s["numerator"]:
            f *= s["denominator"] / s["numerator"]
    return f


def sessions_after(chart: dict, as_of: float, now: float) -> list[dict]:
    """The finished sessions whose close came after `as_of`, numbered k = 1, 2, ..., in flag-time prices."""
    factor = split_factor(chart["splits"], as_of)
    by_day: dict[date, list] = {}
    for bar in chart["bars"]:
        by_day[et_date(bar[0])] = bar  # one bar per session; a later duplicate (live bar) wins
    out = []
    for day in sorted(by_day):
        close = _close_ts(day)
        if close <= as_of or close + SETTLE_S > now:
            continue
        _, o, h, low, c, v = by_day[day]
        out.append({"session": day.isoformat(), "k": len(out) + 1, "open": _div(o, factor), "high": _div(h, factor),
                    "low": _div(low, factor), "close": _div(c, factor), "volume": v, "adj_factor": round(factor, 6)})
    return out[:SESSIONS]


def _div(v, f):
    return None if v is None else float(f"{v / f:.6g}")


def _num(v: str) -> float | None:
    try:
        return float(v)
    except (TypeError, ValueError):
        return None


def mention_counts(ds: Datastore) -> dict[tuple[str, str], int]:
    """(ticker, UTC date) -> Reddit mentions that day, from Stage 1's daily counts (every ticker, every day)."""
    counts: dict[tuple[str, str], int] = {}
    base = ds.path("daily/mention_counts")
    for p in sorted(base.glob("*.csv")) if base.exists() else []:
        for r in ds.read_csv(p.relative_to(ds.root)):
            counts[(r["ticker"], r["date"])] = int(r["mentions"] or 0)
    return counts


def _mentions_after(counts: dict, ticker: str, as_of: float, days: int, now: float) -> int | str:
    """Mentions on the `days` UTC days after the flag's day; blank until the last of them has ended."""
    first = date.fromisoformat(utc_date(as_of)) + timedelta(days=1)
    if date.fromisoformat(utc_date(now)) <= first + timedelta(days=days - 1):
        return ""
    return sum(counts.get((ticker, (first + timedelta(days=i)).isoformat()), 0) for i in range(days))


def outcome(snap: dict, daily: list[dict], filings: list[dict], status: str, now: float, counts: dict | None = None) -> dict:
    """Post-flag path metrics of one snapshot from its tracked rows (all prices in flag-time terms)."""
    as_of = float(snap["as_of"])
    base = _num(snap.get("price_at_flag"))
    rows = sorted(daily, key=lambda r: int(r["k"]))
    out = dict.fromkeys(OUTCOME_FIELDS, "")
    out.update({k: snap[k] for k in KEY_FIELDS}, archetype=snap.get("archetype", ""), as_of_utc=iso(as_of),
               base_price=base if base is not None else "", status=status, sessions=len(rows),
               updated_at_utc=iso(now), track_version=TRACK_VERSION)
    for n in (5, 20):
        out[f"mentions_next_{n}d"] = _mentions_after(counts or {}, snap["ticker"], as_of, n, now)
    if rows:
        d1 = date.fromisoformat(rows[0]["session"])
        out["flag_in_session_1"] = int(_open_ts(d1) < as_of < _close_ts(d1))
    if not base:
        return out
    by_k = {int(r["k"]): r for r in rows}
    highs = [(_num(by_k[k]["high"]), k) for k in range(1, 6) if k in by_k and _num(by_k[k]["high"]) is not None]
    if len(highs) == 5:
        peak, peak_k = max(highs)
        out.update(max_high_5=peak, ret_max_5=round(peak / base - 1, 6), peak_k_5=peak_k)
        after = [_num(by_k[k]["low"]) for k in range(peak_k + 1, peak_k + 11) if k in by_k]
        after = [v for v in after if v is not None]
        if len(after) == 10 and peak:
            low = min(after)
            out.update(min_low_10_after_peak=low, drop_from_peak_10=round(low / peak - 1, 6))
    for n in (1, 5, 10, 20):
        c = _num(by_k.get(n, {}).get("close"))
        if c is not None:
            out[f"ret_close_{n}"] = round(c / base - 1, 6)

    def filed_by(k: int, forms) -> int | str:
        if k not in by_k:
            return ""
        end = _close_ts(date.fromisoformat(by_k[k]["session"]))
        return sum(1 for f in filings if f["form"] in forms and as_of < _accepted_ts(f["accepted_at_utc"]) <= end)

    out["current_reports_10"] = filed_by(10, CURRENT_REPORT_FORMS)
    out["dilution_filings_20"] = filed_by(20, DILUTION_FORMS)
    return out


def _status(snap: dict, n_sessions: int, state: dict, now: float) -> str:
    if not _num(snap.get("price_at_flag")):
        return "no_price"
    if state.get(snap["snapshot_id"]) == "no_data":
        return "no_data"
    if n_sessions >= SESSIONS:
        return "done"
    if now > float(snap["as_of"]) + MAX_DAYS * DAY:
        return "expired"
    return "active"


def _shifted(later: float, earlier: float) -> bool:
    return round(later - earlier) in SEC_SHIFTS


def _known_before_flag(snap: dict) -> list[float]:
    """Acceptance times of filings Stage 2 already saw before the flag (its latest 8-K and dilution filing)."""
    return [_accepted_ts(snap[c]) for c in ("last_current_report_at", "last_dilution_at") if snap.get(c)]


def clean_filings(rows: list[dict], snaps: dict[str, dict]) -> list[dict]:
    """Drop copies of a filing re-read with the shifted SEC time, and pre-flag filings that only look post-flag
    because of it (rows from before filings were keyed on their accession number)."""
    out = []
    for r in rows:
        t = _accepted_ts(r["accepted_at_utc"])
        twin = any(o is not r and o["snapshot_id"] == r["snapshot_id"] and o["form"] == r["form"]
                   and o["items"] == r["items"] and _shifted(t, _accepted_ts(o["accepted_at_utc"])) for o in rows)
        snap = snaps.get(r["snapshot_id"], {})
        pre_flag = any(_shifted(t, k) for k in _known_before_flag(snap))
        if not twin and not pre_flag:
            out.append(r)
    return out


def run_track(ds: Datastore, src: MarketSources, clock: Callable[[], float] = time.time, max_seconds: float = 20 * 60) -> dict:
    start = clock()
    snaps = ds.read_csv(SNAPSHOTS)
    daily, filings = ds.read_csv(DAILY), ds.read_csv(FILINGS)
    state = json.loads(ds.path(STATE).read_text()) if ds.path(STATE).exists() else {}
    have: dict[str, set] = defaultdict(set)
    for r in daily:
        have[r["snapshot_id"]].add(r["session"])
    cleaned = clean_filings(filings, {s["snapshot_id"]: s for s in snaps})
    upgrade = bool(filings) and (len(cleaned) != len(filings) or "accession" not in filings[0])
    filings = cleaned
    seen = {(r["snapshot_id"], r["accession"]) for r in filings if r.get("accession")}
    new_daily: list[dict] = []
    new_filings: list[dict] = []
    summary = {"tracked": [], "new_sessions": 0, "new_filings": 0, "warnings": [], "active": 0}
    edgar_cache: dict[str, list] = {}

    for snap in snaps:
        sid = snap["snapshot_id"]
        if _status(snap, len(have[sid]), state, clock()) != "active":
            continue
        if clock() - start > max_seconds:
            summary["warnings"].append("time budget used up; the rest waits for the next run")
            break
        now = clock()
        as_of = float(snap["as_of"])
        key = {k: snap[k] for k in KEY_FIELDS}
        stamp = {"collected_at": round(now, 3), "collected_at_utc": iso(now), "track_version": TRACK_VERSION}
        try:
            chart = src.yahoo.chart(snap["ticker"], as_of - 7 * DAY, now)
        except NoData as exc:
            state[sid] = "no_data"
            summary["warnings"].append(f"{snap['ticker']}: not on Yahoo any more ({exc}); stopped following it")
            continue
        except SourceError as exc:
            summary["warnings"].append(f"{snap['ticker']}: {exc}; retrying next run")
            continue
        sessions = sessions_after(chart, as_of, now)
        added = [s for s in sessions if s["session"] not in have[sid]]
        for s in added:
            have[sid].add(s["session"])
            new_daily.append({**key, **s, **stamp})
        summary["new_sessions"] += len(added)
        summary["tracked"].append(f"{snap['ticker']} ({snap['role']}, {len(have[sid])}/{SESSIONS})")

        cik = snap.get("cik")
        if cik and src.sec_contact:
            try:
                if cik not in edgar_cache:
                    edgar_cache[cik] = edgar.submissions(src.web, int(cik), src.sec_contact, since=utc_date(as_of))["filings"]
                closes = [_close_ts(date.fromisoformat(s["session"])) for s in sessions]
                legacy = [r for r in filings if r["snapshot_id"] == sid and not r.get("accession")]
                for f in edgar_cache[cik]:
                    t = _accepted_ts(f["accepted"]) if f.get("accepted") else None
                    if t is None or t <= as_of or t > now:
                        continue
                    acc_no = f.get("accession") or f"{f['form']} {iso(t)}"
                    if (sid, acc_no) in seen:
                        continue  # the time first seen stands
                    seen.add((sid, acc_no))
                    old = next((r for r in legacy if r["form"] == f["form"] and r["items"] == f.get("items", "")
                                and (_accepted_ts(r["accepted_at_utc"]) == t or _shifted(t, _accepted_ts(r["accepted_at_utc"])))), None)
                    if old is not None:  # recorded before accession numbers were kept
                        old["accession"] = acc_no
                        upgrade = True
                        continue
                    if any(_shifted(t, k) for k in _known_before_flag(snap)):
                        continue  # Stage 2 saw this one before the flag; only the shifted time makes it look later
                    new_filings.append({**key, "form": f["form"], "accepted_at_utc": iso(t), "items": f.get("items", ""),
                                        "k": 1 + sum(1 for c in closes if c < t), **stamp,  # first session that could react
                                        "accession": acc_no})
            except (edgar.EdgarError, ValueError) as exc:
                summary["warnings"].append(f"{snap['ticker']}: SEC {exc}"[:200])

    ds.append_csv(DAILY, DAILY_FIELDS, new_daily)
    if upgrade:
        ds.write_csv(FILINGS, FILING_FIELDS, filings)
    ds.append_csv(FILINGS, FILING_FIELDS, new_filings)
    summary["new_filings"] = len(new_filings)

    now = clock()
    daily_by: dict[str, list] = defaultdict(list)
    for r in ds.read_csv(DAILY):
        daily_by[r["snapshot_id"]].append(r)
    filings_by: dict[str, list] = defaultdict(list)
    for r in ds.read_csv(FILINGS):
        filings_by[r["snapshot_id"]].append(r)
    counts = mention_counts(ds)
    outcomes = []
    for snap in snaps:
        sid = snap["snapshot_id"]
        status = _status(snap, len(daily_by[sid]), state, now)
        summary["active"] += status == "active"
        outcomes.append(outcome(snap, daily_by[sid], filings_by[sid], status, now, counts))
    if snaps:
        ds.write_csv(OUTCOMES, OUTCOME_FIELDS, outcomes)
        ds.write_text(README, render_readme(outcomes, now))
    ds.write_text(STATE, json.dumps(state, indent=2, sort_keys=True) + "\n")
    return summary


def _pct(v) -> str:
    return "" if v in ("", None) else f"{float(v):+.0%}"


def render_readme(outcomes: list[dict], now: float) -> str:
    lines = [
        "# Stage 3 tracking", "",
        f"Updated {iso(now)}. Each candidate and control is followed for {SESSIONS} trading sessions after its flag "
        "(`track/daily.csv`, `track/filings.csv`); this table is rebuilt from those rows each run (`track/outcomes.csv`). "
        "Returns are against the price at the flag. Definitions: docs/stage3.md in the code branch.", "",
        "| Flagged (UTC) | Ticker | Role | Archetype | Status | Sessions | Max high, 5 sessions | Drop from that peak, 10 after | Close after 5 | Close after 20 | 8-Ks by 10 |",
        "|---|---|---|---|---|---|---|---|---|---|---|",
    ]
    for o in sorted(outcomes, key=lambda o: (o["as_of_utc"], o["role"] != "candidate"), reverse=True):
        lines.append(
            f"| {o['as_of_utc'][:16].replace('T', ' ')} | {o['ticker']} | {o['role']} | {o['archetype']} | {o['status']} | "
            f"{o['sessions']} | {_pct(o['ret_max_5'])} | {_pct(o['drop_from_peak_10'])} | {_pct(o['ret_close_5'])} | "
            f"{_pct(o['ret_close_20'])} | {o['current_reports_10']} |"
        )
    return "\n".join(lines) + "\n"
