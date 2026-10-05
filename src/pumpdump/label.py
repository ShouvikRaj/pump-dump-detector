"""Stage 4: label every candidate and control once enough sessions have passed since its flag.

Once a day (the `label` workflow, after Stage 3's `track` run) this reads Stage 2's snapshots and Stage 3's
tracked sessions and filings, and rebuilds labels/labels.csv (one row per snapshot) and labels/README.md. Candidates
and controls get the same rule, `label-v1`, written down before any outcome was looked at (docs/stage4.md):

  pump_dump  up 50% within 5 sessions after the flag, then down 40% from that peak within the next 10
  crash_10   a close 40% or more below the flag price within 10 sessions (the "avoid" signal)
  real_news  a hard-news 8-K from 72 hours before the flag to session 5's close
  label      real_news, else pump if pump_dump, else not_pump; pending until settled, unknown if tracking ended first
"""

from __future__ import annotations

import time
from collections import Counter, defaultdict
from datetime import date
from typing import Callable

from .features import DILUTION_FORMS, _accepted_ts, iso
from .market import SNAPSHOTS
from .store import Datastore
from .track import DAILY, FILINGS, KEY_FIELDS, OUTCOMES, _close_ts, _num, _pct

LABEL_VERSION = "label-v1"
PUMP_RISE = 0.50  # Stage 3's ret_max_5 at least this...
PUMP_DROP = -0.40  # ...then its drop_from_peak_10 at most this
CRASH_LINE = 0.60  # a close at or below this fraction of the flag price...
CRASH_SESSIONS = 10  # ...within this many sessions
NEWS_BEFORE_S = 72 * 3600  # the news window opens 72 hours before the flag...
NEWS_LAST_K = 5  # ...and closes at this session's close
NEWS_SETTLE_K = 10  # "no news" is final after this many sessions (Stage 3 re-reads EDGAR daily until then)
NEWS_ITEMS = frozenset({"2.02", "2.01", "5.01", "1.03"})  # results, acquisition/disposal, change in control, bankruptcy
AGREEMENT_ITEM = "1.01"  # material definitive agreement: news unless it is a financing
FINANCING_ITEMS = frozenset({"2.03", "3.02"})
FINANCING_GAP_S = 48 * 3600  # a dilution filing this close to a 1.01 8-K makes it a financing
REPORT_FORMS = frozenset({"8-K", "8-K/A", "6-K", "6-K/A"})

LABELS = "labels/labels.csv"
README = "labels/README.md"
LABEL_FIELDS = [*KEY_FIELDS, "archetype", "as_of_utc", "warmup", "track_status", "sessions", "label", "pump_dump",
                "crash_10", "real_news", "ret_max_5", "peak_k_5", "drop_from_peak_10", "min_close_10", "ret_min_close_10",
                "peak_maybe_before_flag", "news_filings", "note", "labeled_at_utc", "label_version"]
SETTLED = ("pump", "real_news", "not_pump")
ARCHETYPES = ("low_float_runner", "otc_penny", "other")


def _items(text) -> set[str]:
    return {i.strip() for i in str(text or "").split(",") if i.strip()}


def news_in_window(snap: dict, filings: list[dict], start: float, end: float) -> tuple[bool, list[str]]:
    """Whether a hard-news 8-K was accepted between `start` and `end`, and every 8-K/6-K accepted then, described."""
    reports = []  # (accepted, form, items)
    if snap.get("last_current_report_at"):  # Stage 2: the last 8-K/6-K before the flag; only 8-Ks carry items
        items = _items(snap.get("last_current_report_items"))
        reports.append((_accepted_ts(snap["last_current_report_at"]), "8-K" if items else "8-K/6-K", items))
    dilution = [_accepted_ts(snap["last_dilution_at"])] if snap.get("last_dilution_at") else []
    for f in filings:
        t = _accepted_ts(f["accepted_at_utc"])
        if f["form"] in DILUTION_FORMS:
            dilution.append(t)
        elif f["form"] in REPORT_FORMS:
            reports.append((t, f["form"], _items(f.get("items"))))
    found, listed = False, []
    for t, form, items in sorted(reports, key=lambda r: r[0]):
        if not start <= t <= end:
            continue
        financing = bool(items & FINANCING_ITEMS) or any(abs(d - t) <= FINANCING_GAP_S for d in dilution)
        news = form == "8-K" and bool(items & NEWS_ITEMS or (AGREEMENT_ITEM in items and not financing))
        found = found or news
        listed.append(f"{form} {iso(t)[:16]} {','.join(sorted(items)) or 'no items'}{' (news)' if news else ''}")
    return found, listed


def _flag(v: int | None):
    return "" if v is None else v


def label_row(o: dict, snap: dict, daily: list[dict], filings: list[dict], warmup: str, now: float) -> dict:
    """The label of one snapshot from its Stage 3 outcome row, tracked sessions and filings (docs/stage4.md)."""
    row = dict.fromkeys(LABEL_FIELDS, "")
    row.update({k: o[k] for k in KEY_FIELDS}, archetype=o["archetype"], as_of_utc=o["as_of_utc"], warmup=warmup,
               track_status=o["status"], sessions=o["sessions"], ret_max_5=o["ret_max_5"], peak_k_5=o["peak_k_5"],
               drop_from_peak_10=o["drop_from_peak_10"], labeled_at_utc=iso(now), label_version=LABEL_VERSION)
    base = _num(o["base_price"])
    if not base:
        row.update(label="unknown", note="no price at the flag")
        return row
    tracking = o["status"] == "active"
    by_k = {int(r["k"]): r for r in daily}

    rise, drop = _num(o["ret_max_5"]), _num(o["drop_from_peak_10"])
    pump = None
    if rise is not None and rise < PUMP_RISE:
        pump = 0
    elif rise is not None and drop is not None:
        pump = int(drop <= PUMP_DROP)

    closes = [c for k in range(1, CRASH_SESSIONS + 1) if (c := _num(by_k.get(k, {}).get("close"))) is not None]
    all_in = all(k in by_k for k in range(1, CRASH_SESSIONS + 1))
    crash = 1 if any(c <= CRASH_LINE * base for c in closes) else 0 if all_in else None
    if all_in and closes:
        row.update(min_close_10=min(closes), ret_min_close_10=round(min(closes) / base - 1, 6))

    # the window ends at session 5's close; until then (or when trading stopped first) at the last recorded close,
    # so a filing counts only once its session is in and the result doesn't depend on when the run happened
    as_of = _accepted_ts(o["as_of_utc"])
    last = min(NEWS_LAST_K, max(by_k, default=0))
    end = _close_ts(date.fromisoformat(by_k[last]["session"])) if last else as_of
    found, listed = news_in_window(snap, filings, as_of - NEWS_BEFORE_S, end)
    news = 1 if found else 0 if not snap.get("cik") or len(by_k) >= NEWS_SETTLE_K or not tracking else None

    if news == 1:
        label = "real_news"
    elif pump is not None and news is not None:
        label = "pump" if pump else "not_pump"
    else:
        label = "pending" if tracking else "unknown"
    note = ""
    if label == "unknown":  # often halted or delisted; say so when it had risen 50% first
        note = f"tracking ended ({o['status']}) after {len(by_k)} sessions"
        highs = [h for k in range(1, 6) if (h := _num(by_k.get(k, {}).get("high"))) is not None]
        if highs and max(highs) / base - 1 >= PUMP_RISE:
            note += f", up {max(highs) / base - 1:.0%} at its high"
    row.update(label=label, pump_dump=_flag(pump), crash_10=_flag(crash), real_news=_flag(news),
               peak_maybe_before_flag=_flag(None if pump is None else int(
                   pump == 1 and o["peak_k_5"] == "1" and o["flag_in_session_1"] == "1")),
               news_filings="; ".join(listed), note=note)
    return row


def run_label(ds: Datastore, clock: Callable[[], float] = time.time) -> dict:
    now = clock()
    outcomes = ds.read_csv(OUTCOMES)
    snaps = {s["snapshot_id"]: s for s in ds.read_csv(SNAPSHOTS)}
    warmup = {e["episode_id"]: e.get("warmup", "") for e in ds.read_csv("candidates/episodes.csv")}
    daily: dict[str, list] = defaultdict(list)
    for r in ds.read_csv(DAILY):
        daily[r["snapshot_id"]].append(r)
    filings: dict[str, list] = defaultdict(list)
    for r in ds.read_csv(FILINGS):
        filings[r["snapshot_id"]].append(r)
    before = {r["snapshot_id"]: r["label"] for r in ds.read_csv(LABELS)}
    rows = [label_row(o, snaps.get(o["snapshot_id"], {}), daily[o["snapshot_id"]], filings[o["snapshot_id"]],
                      warmup.get(o["episode_id"], ""), now) for o in outcomes]
    if rows:
        ds.write_csv(LABELS, LABEL_FIELDS, rows)
        ds.write_text(README, render_readme(rows, now))
    return {
        "counts": dict(Counter(r["label"] for r in rows)),
        "crashes": sum(1 for r in rows if r["crash_10"] == 1),
        "new": [f"{r['ticker']} ({r['role']}) {r['label']}" for r in rows
                if r["label"] in SETTLED and before.get(r["snapshot_id"]) != r["label"]],
        "untracked": len(set(snaps) - {o["snapshot_id"] for o in outcomes}),  # snapshotted after the last track run
    }


def _yes(v) -> str:
    return {"1": "yes", "0": "no"}.get(str(v), "")


def _rate(k: int, n: int) -> str:
    return f"{k} of {n} ({k / n:.0%})" if n else "-"


def render_readme(rows: list[dict], now: float, limit: int = 50) -> str:
    lines = [
        "# Stage 4 labels", "",
        f"Updated {iso(now)}. Every candidate and control gets the same rule, `{LABEL_VERSION}`, written down before any "
        "outcome was looked at (docs/stage4.md in the code branch). Sessions count from the flag; returns are against "
        "the price at the flag. All rows: `labels/labels.csv`.", "",
        "- **pump**: up 50% or more within 5 sessions, then down 40% or more from that peak within the next 10",
        "- **real news**: earnings, a completed acquisition, a change of control, bankruptcy or a material agreement that "
        "isn't a share sale, filed with the SEC (8-K) between 72 hours before the flag and session 5; it beats pump",
        "- **not pump**: neither, once the windows have closed (10 sessions; 15 after a 50% rise)",
        "- **crash** (a separate label, for the avoid signal): a close 40% or more below the flag price within 10 sessions",
        "",
        "| Archetype | Role | Pump | Real news | Not pump | Crash | Pending | Unknown |",
        "|---|---|---|---|---|---|---|---|",
    ]
    groups: dict[tuple, list] = defaultdict(list)
    for r in rows:
        groups[(r["archetype"], r["role"])].append(r)

    def order(key):
        arch, role = key
        return ARCHETYPES.index(arch) if arch in ARCHETYPES else len(ARCHETYPES), arch, role != "candidate"

    for arch, role in sorted(groups, key=order):
        g = groups[(arch, role)]
        c = Counter(r["label"] for r in g)
        crash = [str(r["crash_10"]) for r in g if str(r["crash_10"]) != ""]
        lines.append(f"| {arch.replace('_', ' ')} | {role} | {c['pump']} | {c['real_news']} | {c['not_pump']} | "
                     f"{_rate(crash.count('1'), len(crash))} | {c['pending']} | {c['unknown']} |")
    warm = sum(1 for r in rows if r["role"] == "candidate" and r["label"] in SETTLED and str(r["warmup"]) == "1")
    lines += ["", "Crash counts the snapshots whose crash label has settled."]
    if warm:
        lines.append(f"{warm} of the labeled candidates {'was' if warm == 1 else 'were'} flagged in Stage 1's warm-up week "
                     "(`warmup = 1`), when part of the chatter baseline was backfilled.")

    done = [r for r in rows if r["label"] in SETTLED or r["label"] == "unknown"]
    lines += ["", "## Labeled so far", ""]
    if not done:
        lines.append("Nothing yet: a label is final 10 sessions after the flag (15 after a 50% rise).")
        return "\n".join(lines) + "\n"
    lines += ["| Flagged (UTC) | Ticker | Role | Archetype | Label | Crash | Peak, 5 sessions | Drop from peak | "
              "Lowest close, 10 sessions | News filings |", "|---|---|---|---|---|---|---|---|---|---|"]
    # newest flags first, each candidate followed by its controls
    for r in sorted(done, key=lambda r: (r["as_of_utc"], r["role"] == "candidate", r["ticker"]), reverse=True)[:limit]:
        note = f" ({r['note']})" if r["note"] else ""
        lines.append(
            f"| {r['as_of_utc'][:16].replace('T', ' ')} | {r['ticker']} | {r['role']} | {r['archetype'].replace('_', ' ')} | "
            f"{r['label'].replace('_', ' ')}{note} | {_yes(r['crash_10'])} | {_pct(r['ret_max_5'])} | "
            f"{_pct(r['drop_from_peak_10'])} | {_pct(r['ret_min_close_10'])} | {r['news_filings']} |"
        )
    if len(done) > limit:
        lines.append(f"\n{len(done) - limit} older rows are in `labels/labels.csv`.")
    return "\n".join(lines) + "\n"
