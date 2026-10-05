"""Command line: `python -m pumpdump <command>`.

  collect   one collection run against a datastore directory (the data branch)
  market    Stage 2: market snapshot of each new candidate as of its flag time, plus controls
  build-db  build a full SQLite database from a datastore
  scan      show the tickers and hype categories found in a piece of text
  status    say whether collection has finished (enough data for analysis)
"""

from __future__ import annotations

import argparse
import json
import os
import sqlite3
import sys
import time
from datetime import datetime, timezone
from pathlib import Path

from . import db, market
from .hype import hype_categories
from .market import default_sources, dry_run, run_market
from .pipeline import Settings, collection_done, run_collect
from .sources.arctic_shift import BASE_URL, ArcticShift
from .sources.stocktwits import fetch_trending
from .store import Datastore
from .symbols import load_symbols, refresh_symbols
from .tickers import default_extractor


def make_client(max_retries: int = 5) -> ArcticShift:
    # env overrides exist for tuning politeness and for local end-to-end tests
    return ArcticShift(
        max_retries=max_retries,
        min_interval=float(os.environ.get("ARCTIC_SHIFT_MIN_INTERVAL", "1.0")),
        base_url=os.environ.get("ARCTIC_SHIFT_BASE_URL", BASE_URL),
    )


def render_summary(summary: dict) -> str:
    if summary.get("finished"):
        return f"## Collection run {summary['run_id']}\n\nCollection finished ({summary['finished']}); nothing fetched.\n"
    lines = [f"## Collection run {summary['run_id']}", "", f"{summary['new_docs']} new items stored. Started {summary['started_at']}.", ""]
    lines += ["| Stream | Mode | Fetched | New | Pages | Caught up | Cursor | Archive lag (s) | Error |", "|---|---|---|---|---|---|---|---|---|"]
    for s in summary["streams"]:
        lines.append(
            f"| {s['stream']} | {s['mode']} | {s['fetched']} | {s['new']} | {s['pages']} | {'yes' if s['complete'] else 'no'} "
            f"| {s['cursor_utc']} | {s['median_archive_lag_s']} | {s['error'][:120]} |"
        )
    lines += ["", f"Spike detection: {summary['detection']}"]
    if summary.get("daily"):
        lines.append(f"Daily catch-up and mention counts written for {summary['daily']}.")
    if summary.get("daily_filled"):
        lines.append(f"Mention counts filled in for {', '.join(summary['daily_filled'])}.")
    if summary["new_candidates"]:
        lines.append(f"New candidates: {', '.join(summary['new_candidates'])}")
    if summary["active"]:
        lines.append(f"Active candidates: {', '.join(summary['active'])}")
    h = summary.get("health", {})
    if h and not h.get("healthy", True):
        lines += ["", "Health problems:"] + [f"- {p}" for p in h["problems"]]
    if summary["warnings"]:
        lines += ["", "Warnings:"] + [f"- {w}" for w in summary["warnings"]]
    return "\n".join(lines) + "\n"


def cmd_collect(args: argparse.Namespace) -> int:
    ds = Datastore(args.datastore)
    settings = Settings(max_seconds=args.max_minutes * 60)
    run_id = args.run_id or os.environ.get("GITHUB_RUN_ID") or time.strftime("%Y%m%dT%H%M%S", time.gmtime())
    summary = run_collect(
        ds,
        make_client(args.max_retries),
        run_id=str(run_id),
        settings=settings,
        fetch_symbols=lambda: refresh_symbols(),
        fetch_trending=None if args.no_stocktwits else (lambda: fetch_trending(time.time)),
        clock=lambda: time.time(),
    )
    text = render_summary(summary)
    print(text)
    if args.summary:
        with open(args.summary, "a", encoding="utf-8") as fh:
            fh.write(text)
    # source outages are tracked in the state and reported by the health check, so the
    # run still succeeds and gets pushed; only crashes fail it
    return 0


def render_market_summary(summary: dict) -> str:
    lines = [f"## Market run {summary['run_id']}", ""]
    if summary["snapshots"]:
        lines.append(
            f"Snapshots of {len(summary['snapshots'])} new candidates ({', '.join(summary['snapshots'])}) "
            f"and {len(summary['controls'])} controls ({', '.join(summary['controls']) or 'none'})."
        )
    else:
        lines.append("No new candidates to snapshot.")
    if summary["universe"]:
        lines.append(f"Saved the listed-stock universe: {summary['universe']}.")
    if summary["pending"]:
        lines += ["", "Retrying on the next runs:"] + [f"- {p}" for p in summary["pending"]]
    if summary["warnings"]:
        lines += ["", "Warnings:"] + [f"- {w}" for w in summary["warnings"]]
    return "\n".join(lines) + "\n"


def _utc_timestamp(text: str) -> float:
    dt = datetime.fromisoformat(text)
    return (dt if dt.tzinfo else dt.replace(tzinfo=timezone.utc)).timestamp()


def cmd_market(args: argparse.Namespace) -> int:
    ds = Datastore(args.datastore)
    src = default_sources()
    if args.dry_run:
        now = time.time()
        as_of = _utc_timestamp(args.as_of) if args.as_of else now
        for row in dry_run(src, args.dry_run, load_symbols(ds), as_of, now):
            print(json.dumps(row, default=str))
        return 0
    run_id = args.run_id or os.environ.get("GITHUB_RUN_ID") or time.strftime("%Y%m%dT%H%M%S", time.gmtime())
    summary = run_market(ds, src, run_id=str(run_id), clock=lambda: time.time(), max_seconds=args.max_minutes * 60)
    text = render_market_summary(summary)
    print(text)
    if args.summary:
        with open(args.summary, "a", encoding="utf-8") as fh:
            fh.write(text)
    # like collect: source failures are recorded in the rows and the summary; only crashes fail the run
    return 0


def _convert(v: str):
    if v == "":
        return None
    for cast in (int, float):
        try:
            return cast(v)
        except ValueError:
            pass
    return v


def _load_csv_table(conn: sqlite3.Connection, table: str, rows: list[dict]) -> None:
    if not rows:
        return
    cols = list(rows[0].keys())
    conn.execute(f'CREATE TABLE "{table}" ({", ".join(f"{c!r} " for c in cols)})'.replace("'", '"'))
    conn.executemany(
        f'INSERT INTO "{table}" VALUES ({",".join("?" * len(cols))})', ([_convert(r.get(c) or "") for c in cols] for r in rows)
    )


def _read_monthly(ds: Datastore, folder: str) -> list[dict]:
    rows: list[dict] = []
    base = ds.path(folder)
    if base.exists():
        for p in sorted(base.glob("*.csv")):
            rows += ds.read_csv(p.relative_to(ds.root))
    return rows


def cmd_build_db(args: argparse.Namespace) -> int:
    ds = Datastore(args.datastore)
    out = Path(args.out)
    if out.exists():
        out.unlink()
    since = None
    if args.since:
        since = time.mktime(time.strptime(args.since, "%Y-%m-%d")) - time.timezone
    conn = db.connect(str(out))
    n_docs = db.insert_docs(conn, ds.iter_raw(since=since))
    symbols = load_symbols(ds)
    n_mentions = db.extract_mentions(conn, default_extractor(symbols.keys()), Settings().excluded_authors)
    _load_csv_table(conn, "symbols", ds.read_csv("ref/symbols.csv"))
    _load_csv_table(conn, "candidate_episodes", ds.read_csv("candidates/episodes.csv"))
    _load_csv_table(conn, "candidate_episode_ends", ds.read_csv("candidates/episode_ends.csv"))
    _load_csv_table(conn, "daily_mention_counts", _read_monthly(ds, "daily/mention_counts"))
    _load_csv_table(conn, "stocktwits_trending", _read_monthly(ds, "stocktwits/trending"))
    _load_csv_table(conn, "runs", _read_monthly(ds, "logs/runs"))
    _load_csv_table(conn, "market_snapshots", ds.read_csv(market.SNAPSHOTS))
    universe = [{"date": p.name[:10], **r} for p in market.universe_files(ds) for r in market.read_universe(p)]
    _load_csv_table(conn, "market_universe", universe)
    conn.commit()
    conn.close()
    print(f"wrote {out}: {n_docs} docs, {n_mentions} mentions")
    return 0


def cmd_scan(args: argparse.Namespace) -> int:
    symbols = load_symbols(Datastore(args.datastore)) if args.datastore else {}
    ext = default_extractor(symbols.keys())
    mentions = ext.extract(args.text)
    print(json.dumps({"tickers": [m.__dict__ for m in mentions], "hype": sorted(hype_categories(args.text))}, ensure_ascii=False))
    return 0


def cmd_status(args: argparse.Namespace) -> int:
    ds = Datastore(args.datastore)
    reason = collection_done(ds, ds.load_state(), time.time(), Settings())
    print(f"finished: {reason}" if reason else "collecting")
    if args.github_output:
        with open(args.github_output, "a", encoding="utf-8") as fh:
            fh.write(f"finished={'true' if reason else 'false'}\nreason={reason or ''}\n")
    return 0


def main(argv: list[str] | None = None) -> int:
    p = argparse.ArgumentParser(prog="pumpdump", description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    sub = p.add_subparsers(dest="cmd", required=True)

    c = sub.add_parser("collect", help="run one collection pass")
    c.add_argument("--datastore", required=True)
    c.add_argument("--run-id")
    c.add_argument("--max-minutes", type=float, default=10.0)
    c.add_argument("--max-retries", type=int, default=5)
    c.add_argument("--summary", help="append a markdown summary here (e.g. $GITHUB_STEP_SUMMARY)")
    c.add_argument("--no-stocktwits", action="store_true")
    c.set_defaults(func=cmd_collect)

    m = sub.add_parser("market", help="Stage 2: snapshot new candidates' market data")
    m.add_argument("--datastore", required=True)
    m.add_argument("--run-id")
    m.add_argument("--max-minutes", type=float, default=8.0)
    m.add_argument("--summary", help="append a markdown summary here (e.g. $GITHUB_STEP_SUMMARY)")
    m.add_argument("--dry-run", nargs="+", metavar="TICKER", help="only print snapshots of these tickers; save nothing")
    m.add_argument("--as-of", help="with --dry-run: snapshot time, ISO 8601 (UTC if no offset); default now")
    m.set_defaults(func=cmd_market)

    b = sub.add_parser("build-db", help="build a SQLite database from a datastore")
    b.add_argument("--datastore", required=True)
    b.add_argument("--out", default="pumpdump.sqlite")
    b.add_argument("--since", help="only raw files collected on/after YYYY-MM-DD")
    b.set_defaults(func=cmd_build_db)

    s = sub.add_parser("scan", help="show tickers and hype found in text")
    s.add_argument("text")
    s.add_argument("--datastore", help="use this datastore's symbol list")
    s.set_defaults(func=cmd_scan)

    st = sub.add_parser("status", help="say whether collection has finished")
    st.add_argument("--datastore", required=True)
    st.add_argument("--github-output", help="also write finished=true|false and reason= here ($GITHUB_OUTPUT)")
    st.set_defaults(func=cmd_status)

    args = p.parse_args(argv)
    return args.func(args)


if __name__ == "__main__":
    sys.exit(main())
