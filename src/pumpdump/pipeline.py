"""One collection run: fetch new Reddit items, store them, flag candidates.

Order matters for safety: the raw file is written before the state (cursors)
is saved, so a crash can only cause a re-fetch, never a gap.
"""

from __future__ import annotations

import statistics
import time
from dataclasses import dataclass, field
from datetime import datetime, timedelta, timezone
from typing import Callable

from . import db
from .episodes import update_episodes
from .sources.arctic_shift import ArcticShift, fetch_since, to_record
from .sources.stocktwits import FIELDS as TRENDING_FIELDS
from .spikes import DAY, DETECTOR_VERSION, SpikeParams, SpikeResult, evaluate
from .store import Datastore, utc_dt
from .symbols import load_symbols, refresh_symbols, save_symbols
from .tickers import EXTRACTOR_VERSION, default_extractor

EPISODE_FIELDS = [
    "episode_id",
    "ticker",
    "first_flagged_at",
    "first_flagged_at_utc",
    "run_id",
    "reasons",
    "mentions_24h",
    "authors_24h",
    "posts_24h",
    "comments_24h",
    "baseline_mean",
    "baseline_sd",
    "threshold",
    "z",
    "hype_docs_24h",
    "hype_authors_24h",
    "hype_baseline_mean",
    "hype_threshold",
    "by_subreddit",
    "methods",
    "in_universe",
    "exchange",
    "name",
    "is_etf",
    "stocktwits_rank",
    "warmup",
    "examples",
    "detector_version",
    "extractor_version",
]
EPISODE_END_FIELDS = [
    "episode_id",
    "ticker",
    "first_flagged_at_utc",
    "last_flagged_at_utc",
    "ended_at_utc",
    "n_flags",
    "peak_mentions",
    "peak_z",
    "reasons_seen",
]
ACTIVE_FIELDS = [
    "ticker",
    "episode_id",
    "first_flagged_at_utc",
    "last_flagged_at_utc",
    "n_flags",
    "reasons_seen",
    "mentions_24h",
    "authors_24h",
    "baseline_mean",
    "z",
    "hype_docs_24h",
    "peak_mentions",
    "peak_z",
    "exchange",
    "name",
    "stocktwits_rank",
    "examples",
]
RUN_LOG_FIELDS = [
    "run_id",
    "run_started_at_utc",
    "stream",
    "mode",
    "after_utc",
    "fetched",
    "new",
    "pages",
    "complete",
    "cursor_utc",
    "median_archive_lag_s",
    "median_collect_lag_s",
    "error",
]


DATA_README = """# Collected data (branch `data`)

Written by the `collect` workflow every 15 minutes. Code and docs live on `main`.

| Path | What |
|---|---|
| `candidates/README.md` | Current candidates, human readable |
| `candidates/episodes.csv` | One row per candidate, written the moment it was first flagged (never edited) |
| `candidates/episode_ends.csv` | When each candidate went quiet, with its peak numbers |
| `candidates/active.csv` | Candidates flagged in the last 24 hours |
| `raw/reddit/YYYY/MM/DD/*.jsonl.gz` | Every post and comment, one file per run (huge runs split into `_pNN` parts), partitioned by the UTC date it was collected |
| `daily/mention_counts/YYYY-MM.csv` | Mentions per ticker per UTC day, for all tickers (control groups) |
| `stocktwits/trending/YYYY-MM.csv` | StockTwits trending list at each run |
| `logs/runs/YYYY-MM.csv` | What each run fetched, lags and errors |
| `reports/health.json` | Latest health check (an issue opens automatically when it fails) |
| `ref/symbols.csv` | US ticker list (Nasdaq Trader + SEC); git history gives past versions |
| `state/state.json` | Cursors and open episodes (internal) |

Every record carries `created_utc` (when it was posted) and `collected_at`
(when the collector received it). Build a SQLite database with
`python -m pumpdump build-db --datastore <checkout of this branch>`, or
download the `pumpdump-sqlite` artifact from the latest `nightly` run.
"""


@dataclass(frozen=True)
class Settings:
    subreddits: tuple[str, ...] = ("pennystocks", "smallstreetbets", "wallstreetbets")
    backfill_days: int = 9  # 1 current day + 7 baseline days + 1 spare
    window_days: int = 8
    overlap_posts: int = 3 * 3600  # re-read this much before the cursor to catch late archiving
    overlap_comments: int = 30 * 60
    limit: int | str = "auto"
    max_seconds: float = 600.0
    stale_seconds: int = 3 * 3600
    catchup_seconds: int = 6 * 3600
    max_consecutive_errors: int = 4
    episode_gap: int = 24 * 3600
    symbol_refresh_seconds: int = 20 * 3600
    daily_after_seconds: int = 30 * 60  # reconcile yesterday once it's 00:30 UTC
    excluded_authors: frozenset = frozenset({"AutoModerator", "VisualMod", "WSBVoteBot"})
    params: SpikeParams = field(default_factory=SpikeParams)

    def streams(self) -> list[tuple[str, str]]:
        # cheap streams first; the busy wallstreetbets comments go last so a
        # slow backfill can't starve the others of run time
        subs = sorted(self.subreddits, key=lambda s: s == "wallstreetbets")
        return [(s, "posts") for s in subs] + [(s, "comments") for s in subs]

    def overlap(self, kind: str) -> int:
        return self.overlap_posts if kind == "posts" else self.overlap_comments


def iso(ts: float | None) -> str:
    return "" if ts is None else utc_dt(ts).strftime("%Y-%m-%dT%H:%M:%SZ")


def _median(values: list[float]) -> float | str:
    return round(float(statistics.median(values)), 1) if values else ""


def coverage_problem(state: dict, as_of: float, s: Settings) -> str | None:
    """Why spike detection can't run yet (None if it can)."""
    need_since = as_of - s.window_days * DAY
    for sub, kind in s.streams():
        st = state["streams"].get(f"{sub}/{kind}")
        if st is None or st.get("last_complete_at") is None:
            return f"{sub}/{kind} has not caught up yet"
        if st["complete_since"] > need_since:
            return f"{sub}/{kind} history starts {iso(st['complete_since'])}, need {iso(need_since)}"
        if as_of - st["last_complete_at"] > s.stale_seconds:
            return f"{sub}/{kind} last complete fetch {iso(st['last_complete_at'])}"
    return None


def health(state: dict, now: float, s: Settings) -> dict:
    problems = []
    for sub, kind in s.streams():
        key = f"{sub}/{kind}"
        st = state.get("streams", {}).get(key)
        if st is None:
            problems.append(f"{key}: never run")
            continue
        last = st.get("last_complete_at")
        if last is None:
            if now - st["initialized_at"] > s.catchup_seconds:
                problems.append(f"{key}: still not caught up {round((now - st['initialized_at']) / 3600, 1)}h after starting")
        elif now - last > s.stale_seconds:
            problems.append(f"{key}: no complete fetch for {round((now - last) / 3600, 1)}h (last error: {st.get('last_error')})")
        if st.get("consecutive_errors", 0) >= s.max_consecutive_errors:
            problems.append(f"{key}: {st['consecutive_errors']} failed runs in a row: {st.get('last_error')}")
    return {"healthy": not problems, "problems": problems}


def _fetch_stream(client, sub, kind, after, before, mode, run_id, conn, settings, deadline):
    res = fetch_since(client, kind, sub, after=int(after), before=before, limit=settings.limit, deadline=deadline)
    recs = [to_record(kind, it, run_id) for it in res.items]
    known = db.existing_ids(conn, [r["id"] for r in recs])
    fresh = [r for r in recs if r["id"] not in known]
    for r in fresh:
        r["fetch_mode"] = mode
    db.insert_docs(conn, fresh)
    return res, recs, fresh


def run_collect(
    ds: Datastore,
    client: ArcticShift,
    *,
    run_id: str,
    settings: Settings = Settings(),
    fetch_symbols: Callable[[], tuple[dict, list[str]]] = refresh_symbols,
    fetch_trending: Callable[[], list[dict]] | None = None,
    clock: Callable[[], float] = time.time,
) -> dict:
    started = clock()
    deadline = started + settings.max_seconds
    state = ds.load_state()
    state.setdefault("live_since", started)
    summary: dict = {
        "run_id": run_id,
        "started_at": iso(started),
        "new_docs": 0,
        "streams": [],
        "warnings": [],
        "detection": None,
        "daily": None,
        "new_candidates": [],
        "active": [],
    }

    # -- ticker universe ------------------------------------------------------
    symbols = load_symbols(ds)
    if not symbols or started - state.get("symbols_refreshed_at", 0) > settings.symbol_refresh_seconds:
        try:
            fresh_symbols, errors = fetch_symbols()
            summary["warnings"] += [f"symbols: {e}" for e in errors]
            if fresh_symbols:
                # if a source failed, keep its old entries rather than dropping them
                merged = {**symbols, **fresh_symbols} if errors else fresh_symbols
                save_symbols(ds, merged)
                symbols = load_symbols(ds)
                state["symbols_refreshed_at"] = started
        except Exception as exc:
            summary["warnings"].append(f"symbols: {exc}")
    if not symbols:
        summary["warnings"].append("symbols: no ticker list, only $CASHTAG and exchange-prefixed mentions count")

    # -- working database: the last window of raw files -------------------------
    conn = db.connect()
    db.insert_docs(conn, ds.iter_raw(since=started - (settings.window_days + 1) * DAY))

    # -- daily rollover: decide now so regular collection leaves it time --------
    today = utc_dt(started).date()
    yesterday = (today - timedelta(days=1)).isoformat()
    day_start_ts = datetime(today.year, today.month, today.day, tzinfo=timezone.utc).timestamp()
    if state.get("daily_done_for") is None:
        state["daily_done_for"] = yesterday  # first run: the backfill just fetched yesterday in full
    rollover = state["daily_done_for"] < yesterday and started >= day_start_ts + settings.daily_after_seconds
    regular_deadline = started + settings.max_seconds * 0.6 if rollover else deadline

    # -- regular collection -----------------------------------------------------
    new_records: list[dict] = []
    log_rows = []
    for sub, kind in settings.streams():
        key = f"{sub}/{kind}"
        st = state["streams"].setdefault(
            key,
            {
                "initialized_at": started,
                "complete_since": started - settings.backfill_days * DAY,
                "cursor": None,
                "last_complete_at": None,
                "consecutive_errors": 0,
                "last_error": None,
            },
        )
        mode = "live" if st["last_complete_at"] is not None else "backfill"
        after = st["cursor"] - settings.overlap(kind) if st["cursor"] is not None else st["complete_since"]
        res, recs, fresh = _fetch_stream(client, sub, kind, after, None, mode, run_id, conn, settings, regular_deadline)
        new_records += fresh
        if res.newest_created is not None:
            st["cursor"] = max(st["cursor"] or 0, res.newest_created)
        if res.complete:
            st["last_complete_at"] = clock()
        if res.error:
            st["consecutive_errors"] = st.get("consecutive_errors", 0) + 1
            st["last_error"] = res.error[:300]
            st["last_error_at"] = clock()
        elif res.complete:
            st["consecutive_errors"] = 0
        row = {
            "run_id": run_id,
            "run_started_at_utc": iso(started),
            "stream": key,
            "mode": mode,
            "after_utc": iso(after),
            "fetched": len(recs),
            "new": len(fresh),
            "pages": res.pages,
            "complete": int(res.complete),
            "cursor_utc": iso(st["cursor"]),
            "median_archive_lag_s": _median(
                [r["source_retrieved_at"] - r["created_utc"] for r in recs if r.get("source_retrieved_at")]
            ),
            "median_collect_lag_s": _median([r["collected_at"] - r["created_utc"] for r in fresh]),
            "error": res.error or "",
        }
        log_rows.append(row)
        summary["streams"].append(row)

    # -- reconcile yesterday: pick up anything archived after we passed it -----
    reconciled_day_start = None
    if rollover:
        y_start = day_start_ts - DAY
        complete = True
        for sub, kind in settings.streams():
            res, recs, fresh = _fetch_stream(
                client, sub, kind, y_start - 1, day_start_ts, "reconcile", run_id, conn, settings, deadline
            )
            new_records += fresh
            complete &= res.complete
            log_rows.append(
                {
                    "run_id": run_id,
                    "run_started_at_utc": iso(started),
                    "stream": f"{sub}/{kind}",
                    "mode": "reconcile",
                    "after_utc": iso(y_start),
                    "fetched": len(recs),
                    "new": len(fresh),
                    "pages": res.pages,
                    "complete": int(res.complete),
                    "cursor_utc": "",
                    "median_archive_lag_s": "",
                    "median_collect_lag_s": _median([r["collected_at"] - r["created_utc"] for r in fresh]),
                    "error": res.error or "",
                }
            )
        if complete:
            reconciled_day_start = int(y_start)
        else:
            summary["warnings"].append(f"reconcile of {yesterday} incomplete, will retry next run")

    # -- persist raw items first, then everything derived ------------------------
    ds.write_raw(new_records, started, run_id)
    if not ds.path("README.md").exists():
        ds.write_text("README.md", DATA_README)
    summary["new_docs"] = len(new_records)

    extractor = default_extractor(symbols.keys())
    db.extract_mentions(conn, extractor, settings.excluded_authors)

    if reconciled_day_start is not None:
        counts = db.daily_counts(conn, reconciled_day_start)
        ds.append_csv(f"daily/mention_counts/{yesterday[:7]}.csv", db.DAILY_FIELDS, counts)
        state["daily_done_for"] = yesterday
        summary["daily"] = yesterday

    trending_rank: dict[str, int] = {}
    if fetch_trending is not None:
        try:
            trending = fetch_trending()
            ds.append_csv(f"stocktwits/trending/{utc_dt(started).strftime('%Y-%m')}.csv", TRENDING_FIELDS, trending)
            trending_rank = {r["symbol"]: r["rank"] for r in trending}
        except Exception as exc:
            summary["warnings"].append(f"stocktwits: {exc}")

    # -- spike detection --------------------------------------------------------
    as_of = clock()
    problem = coverage_problem(state, as_of, settings)
    if problem:
        summary["detection"] = f"skipped: {problem}"
    else:
        summary["detection"] = "ran"
        windows = db.window_counts(conn, as_of, n_days=settings.window_days)
        results = {w.ticker: evaluate(w, settings.params) for w in windows.values() if w.counts[0] > 0}
        opened, ended = update_episodes(state["episodes"], list(results.values()), as_of, settings.episode_gap)
        warmup = int(as_of - state["live_since"] < settings.window_days * DAY)
        new_rows = [
            _episode_row(r, state["episodes"][r.ticker], conn, as_of, run_id, symbols, trending_rank, warmup)
            for r in opened
        ]
        ds.append_csv("candidates/episodes.csv", EPISODE_FIELDS, new_rows)
        ds.append_csv(
            "candidates/episode_ends.csv",
            EPISODE_END_FIELDS,
            [
                {
                    **e,
                    "first_flagged_at_utc": iso(e["first_flagged_at"]),
                    "last_flagged_at_utc": iso(e["last_flagged_at"]),
                    "ended_at_utc": iso(e["ended_at"]),
                    "reasons_seen": " ".join(e["reasons_seen"]),
                }
                for e in ended
            ],
        )
        active = _active_rows(state["episodes"], results, conn, as_of, symbols, trending_rank)
        ds.write_csv("candidates/active.csv", ACTIVE_FIELDS, active)
        ds.write_text("candidates/README.md", render_candidates(active, as_of, run_id, state["live_since"], settings))
        summary["new_candidates"] = [r["ticker"] for r in new_rows]
        summary["active"] = [a["ticker"] for a in active]

    h = health(state, clock(), settings)
    summary["health"] = h
    ds.write_text("reports/health.json", db.to_json(h) + "\n")
    ds.append_csv(f"logs/runs/{utc_dt(started).strftime('%Y-%m')}.csv", RUN_LOG_FIELDS, log_rows)
    state["last_run"] = {"run_id": run_id, "started_at": started, "finished_at": clock(), "new_docs": len(new_records)}
    ds.save_state(state)
    conn.close()
    return summary


def _episode_row(r: SpikeResult, ep: dict, conn, as_of, run_id, symbols, trending_rank, warmup) -> dict:
    d = db.ticker_details(conn, as_of, r.ticker)
    sym = symbols.get(r.ticker, {})
    return {
        "episode_id": ep["episode_id"],
        "ticker": r.ticker,
        "first_flagged_at": round(as_of, 3),
        "first_flagged_at_utc": iso(as_of),
        "run_id": run_id,
        "reasons": " ".join(r.reasons),
        "mentions_24h": r.mentions,
        "authors_24h": r.authors,
        "posts_24h": d["posts"],
        "comments_24h": d["comments"],
        "baseline_mean": round(r.baseline_mean, 3),
        "baseline_sd": round(r.baseline_sd, 3),
        "threshold": round(r.threshold, 3),
        "z": round(r.z, 3),
        "hype_docs_24h": r.hype_docs,
        "hype_authors_24h": r.hype_authors,
        "hype_baseline_mean": round(r.hype_baseline_mean, 3),
        "hype_threshold": round(r.hype_threshold, 3),
        "by_subreddit": db.to_json(d["by_subreddit"]),
        "methods": db.to_json(d["methods"]),
        "in_universe": int(r.ticker in symbols),
        "exchange": sym.get("exchange", ""),
        "name": sym.get("name", ""),
        "is_etf": sym.get("is_etf", ""),
        "stocktwits_rank": trending_rank.get(r.ticker, ""),
        "warmup": warmup,
        "examples": " ".join(d["examples"]),
        "detector_version": DETECTOR_VERSION,
        "extractor_version": EXTRACTOR_VERSION,
    }


def _active_rows(episodes, results, conn, as_of, symbols, trending_rank) -> list[dict]:
    rows = []
    for ticker, ep in sorted(episodes.items(), key=lambda kv: -kv[1]["last_flagged_at"]):
        r = results.get(ticker)
        d = db.ticker_details(conn, as_of, ticker, n_examples=1)
        sym = symbols.get(ticker, {})
        rows.append(
            {
                "ticker": ticker,
                "episode_id": ep["episode_id"],
                "first_flagged_at_utc": iso(ep["first_flagged_at"]),
                "last_flagged_at_utc": iso(ep["last_flagged_at"]),
                "n_flags": ep["n_flags"],
                "reasons_seen": " ".join(ep["reasons_seen"]),
                "mentions_24h": r.mentions if r else 0,
                "authors_24h": r.authors if r else 0,
                "baseline_mean": round(r.baseline_mean, 2) if r else "",
                "z": round(r.z, 2) if r else "",
                "hype_docs_24h": r.hype_docs if r else 0,
                "peak_mentions": ep["peak_mentions"],
                "peak_z": ep["peak_z"],
                "exchange": sym.get("exchange", ""),
                "name": sym.get("name", ""),
                "stocktwits_rank": trending_rank.get(ticker, ""),
                "examples": " ".join(d["examples"]),
                "_by_subreddit": d["by_subreddit"],
            }
        )
    return rows


def render_candidates(active: list[dict], as_of: float, run_id: str, live_since: float, s: Settings) -> str:
    lines = [
        "# Stage 1 candidates",
        "",
        f"Updated {iso(as_of)} by run `{run_id}`. A candidate is a ticker whose Reddit mentions (or hype-language",
        f"posts) in the last 24 hours jumped above its prior {s.params.baseline_days}-day mean + {s.params.k_sd:g} sd, with at least",
        f"{s.params.min_mentions} mentions from {s.params.min_authors} different authors. It stays listed until it goes",
        f"{s.episode_gap // 3600} hours without a new flag. These are statistical flags, not accusations or advice.",
        "",
    ]
    warm_until = live_since + s.window_days * DAY
    if as_of < warm_until:
        lines += [
            f"Warm-up until {iso(warm_until)}: part of the baseline was backfilled from the archive rather than",
            "collected live, so flags in this period are marked `warmup=1` in episodes.csv.",
            "",
        ]
    if not active:
        lines.append("No active candidates right now.")
    else:
        lines += [
            "| Ticker | Flagged since (UTC) | Why | Mentions 24h | Baseline/day | Authors | Hype posts | Subreddits | Exchange | StockTwits | Example |",
            "|---|---|---|---|---|---|---|---|---|---|---|",
        ]
        for a in active:
            subs = ", ".join(f"{k} {v}" for k, v in sorted(a["_by_subreddit"].items(), key=lambda kv: -kv[1]))
            example = f"[link]({a['examples'].split()[0]})" if a["examples"] else ""
            st = f"#{a['stocktwits_rank']}" if a["stocktwits_rank"] != "" else ""
            lines.append(
                f"| {a['ticker']} | {a['first_flagged_at_utc'][:16].replace('T', ' ')} | {a['reasons_seen'].replace('_', ' ')} "
                f"| {a['mentions_24h']} | {a['baseline_mean']} | {a['authors_24h']} | {a['hype_docs_24h']} | {subs} "
                f"| {a['exchange'] or '?'} | {st} | {example} |"
            )
    lines += ["", "Full history: `episodes.csv` (one row per first flag, with the numbers known at that moment)."]
    return "\n".join(lines) + "\n"
