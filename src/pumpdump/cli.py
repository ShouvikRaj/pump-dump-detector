"""Command line: `python -m pumpdump <command>`.

  collect   one collection run against a datastore directory (the data branch)
  market    Stage 2: market snapshot of each new candidate as of its flag time, plus controls
  track     Stage 3: follow candidates and controls for 20 sessions after the flag
  label     Stage 4: label candidates and controls (pump / real news / not pump, and crash)
  model     Stage 5: text features, LLM ratings, weekly LightGBM models and the prospective log
  build-db  build a full SQLite database from a datastore
  scan      show the tickers and hype categories found in a piece of text
  status    say whether collection has finished (enough data for analysis)
"""

from __future__ import annotations

import argparse
import csv
import json
import os
import sqlite3
import sys
import time
from datetime import datetime, timedelta, timezone
from pathlib import Path

from . import db, label, market, model, track
from .hype import hype_categories
from .market import default_sources, dry_run, run_market
from .pipeline import Settings, collection_done, run_collect
from .sources.arctic_shift import BASE_URL, ArcticShift
from .sources.stocktwits import fetch_trending
from .store import Datastore
from .symbols import load_symbols, refresh_symbols
from .text import LLM as MODEL_LLM, LLM_MODEL, LLM_URL, TEXT as MODEL_TEXT, ChatClient, LLMError, probe_llm
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


def render_track_summary(summary: dict, run_id: str) -> str:
    lines = [f"## Track run {run_id}", ""]
    lines.append(
        f"Recorded {summary['new_sessions']} new sessions and {summary['new_filings']} new filings; "
        f"{summary['active']} tickers still followed."
    )
    if summary["tracked"]:
        lines.append("Checked: " + ", ".join(summary["tracked"]) + ".")
    if summary["warnings"]:
        lines += ["", "Warnings:"] + [f"- {w}" for w in summary["warnings"]]
    return "\n".join(lines) + "\n"


def cmd_track(args: argparse.Namespace) -> int:
    ds = Datastore(args.datastore)
    run_id = args.run_id or os.environ.get("GITHUB_RUN_ID") or time.strftime("%Y%m%dT%H%M%S", time.gmtime())
    summary = track.run_track(ds, default_sources(), clock=time.time, max_seconds=args.max_minutes * 60)
    text = render_track_summary(summary, str(run_id))
    print(text)
    if args.summary:
        with open(args.summary, "a", encoding="utf-8") as fh:
            fh.write(text)
    if args.github_output:
        # tracking is over once collection has finished and nothing is left to follow
        finished = collection_done(ds, ds.load_state(), time.time(), Settings()) is not None and summary["active"] == 0
        with open(args.github_output, "a", encoding="utf-8") as fh:
            fh.write(f"finished={'true' if finished else 'false'}\n")
    return 0


def render_label_summary(summary: dict, run_id: str) -> str:
    c = summary["counts"]
    lines = [f"## Label run {run_id}", ""]
    lines.append(
        f"{sum(c.get(k, 0) for k in label.SETTLED)} labeled: {c.get('pump', 0)} pump, {c.get('real_news', 0)} real news, "
        f"{c.get('not_pump', 0)} not pump; {c.get('pending', 0)} pending, {c.get('unknown', 0)} unknown; "
        f"{summary['crashes']} crashed within 10 sessions."
    )
    if summary["new"]:
        lines.append("New labels: " + ", ".join(summary["new"]) + ".")
    return "\n".join(lines) + "\n"


def cmd_label(args: argparse.Namespace) -> int:
    ds = Datastore(args.datastore)
    run_id = args.run_id or os.environ.get("GITHUB_RUN_ID") or time.strftime("%Y%m%dT%H%M%S", time.gmtime())
    summary = label.run_label(ds, clock=time.time)
    text = render_label_summary(summary, str(run_id))
    print(text)
    if args.summary:
        with open(args.summary, "a", encoding="utf-8") as fh:
            fh.write(text)
    if args.github_output:
        # labeling is over once collection has finished, every snapshot has been tracked and no label is pending
        finished = (collection_done(ds, ds.load_state(), time.time(), Settings()) is not None
                    and summary["untracked"] == 0 and summary["counts"].get("pending", 0) == 0)
        with open(args.github_output, "a", encoding="utf-8") as fh:
            fh.write(f"finished={'true' if finished else 'false'}\n")
    return 0


def render_model_summary(summary: dict, run_id: str) -> str:
    llm = summary["llm"]
    lines = [f"## Model run {run_id}", ""]
    lines.append(
        f"Text features for {summary['text']} new candidates; LLM ratings: {llm['ok']} rated, {llm['failed']} failed, "
        f"{llm['waiting']} waiting for a retry. {summary['scored']} new candidates scored."
    )
    lines += [""] + [f"- {t} model this week: {note}" for t, note in summary["models"].items()]
    for t, m in summary["dev"].items():
        if m["n"]:
            lines.append(f"- {t} walk-forward so far: {m['n']} candidates, {m['positives']} positives, "
                         f"{m['flagged']} flagged, average precision {model._num2(m['ap'])}")
    lines += ["", f"Hold-out: {summary['holdout']}."]
    if summary["warnings"]:
        lines += ["", "Warnings:"] + [f"- {w}" for w in summary["warnings"]]
    return "\n".join(lines) + "\n"


def cmd_model(args: argparse.Namespace) -> int:
    if args.llm_probe:  # time one full-size rating against the LLM server; saves nothing
        try:
            ok, lines = probe_llm(ChatClient(url=args.llm_url, model=args.llm_model))
        except LLMError as exc:
            ok, lines = False, [f"the LLM server did not answer: {exc}"]
        print("\n".join(lines))
        return 0 if ok else 1
    ds = Datastore(args.datastore)
    run_id = args.run_id or os.environ.get("GITHUB_RUN_ID") or time.strftime("%Y%m%dT%H%M%S", time.gmtime())
    llm = None if args.no_llm else ChatClient(url=args.llm_url, model=args.llm_model)
    now = time.time()
    raw_since = None
    if args.raw_days is not None:  # only the last N days of raw files were checked out
        raw_since = datetime.fromtimestamp(now, timezone.utc).date() - timedelta(days=args.raw_days)
    if args.llm_eval:  # rate the checked-out candidates with the current prompt, score against hand labels; saves nothing
        gold = json.loads(Path(args.gold).read_text()) if args.gold else None
        rows, lines = model.evaluate_llm(ds, llm, raw_since, gold)
        fields = list(dict.fromkeys(k for r in rows for k in r))
        with open(args.llm_eval, "w", newline="", encoding="utf-8") as fh:
            w = csv.DictWriter(fh, fieldnames=fields, lineterminator="\n")
            w.writeheader()
            w.writerows(rows)
        print("\n".join(lines))
        return 0
    summary = model.run_model(ds, llm, clock=lambda: now, raw_since=raw_since, llm_budget_s=args.llm_minutes * 60)
    report = render_model_summary(summary, str(run_id))
    print(report)
    if args.summary:
        with open(args.summary, "a", encoding="utf-8") as fh:
            fh.write(report)
    if args.github_output:  # finished once the hold-out has been evaluated (after collection ends)
        with open(args.github_output, "a", encoding="utf-8") as fh:
            fh.write(f"finished={'true' if summary['finished'] else 'false'}\n")
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
    _load_csv_table(conn, "track_daily", ds.read_csv(track.DAILY))
    _load_csv_table(conn, "track_filings", ds.read_csv(track.FILINGS))
    _load_csv_table(conn, "track_outcomes", ds.read_csv(track.OUTCOMES))
    _load_csv_table(conn, "labels", ds.read_csv(label.LABELS))
    _load_csv_table(conn, "model_text", ds.read_csv(MODEL_TEXT))
    _load_csv_table(conn, "model_llm", ds.read_csv(MODEL_LLM))
    _load_csv_table(conn, "model_predictions", ds.read_csv(model.PREDICTIONS))
    _load_csv_table(conn, "model_walkforward", ds.read_csv(model.WALKFORWARD))
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

    t = sub.add_parser("track", help="Stage 3: record new sessions and filings of tickers flagged in the last 20 sessions")
    t.add_argument("--datastore", required=True)
    t.add_argument("--run-id")
    t.add_argument("--max-minutes", type=float, default=20.0)
    t.add_argument("--summary", help="append a markdown summary here (e.g. $GITHUB_STEP_SUMMARY)")
    t.add_argument("--github-output", help="write finished=true|false here ($GITHUB_OUTPUT)")
    t.set_defaults(func=cmd_track)

    lb = sub.add_parser("label", help="Stage 4: label candidates and controls whose windows have closed")
    lb.add_argument("--datastore", required=True)
    lb.add_argument("--run-id")
    lb.add_argument("--summary", help="append a markdown summary here (e.g. $GITHUB_STEP_SUMMARY)")
    lb.add_argument("--github-output", help="write finished=true|false here ($GITHUB_OUTPUT)")
    lb.set_defaults(func=cmd_label)

    md = sub.add_parser("model", help="Stage 5: rate new candidates, retrain the weekly models, score, report")
    md.add_argument("--datastore", required=True)
    md.add_argument("--run-id")
    md.add_argument("--raw-days", type=int, help="only the last N days of raw files are present (default: all)")
    md.add_argument("--llm-minutes", type=float, default=35.0, help="start no new LLM rating after this long")
    md.add_argument("--llm-url", default=LLM_URL, help="OpenAI-compatible chat endpoint (default: llama.cpp's server)")
    md.add_argument("--llm-model", default=LLM_MODEL, help="the model the server runs, recorded with each rating")
    md.add_argument("--no-llm", action="store_true", help="skip the LLM ratings (score without them)")
    md.add_argument("--llm-probe", action="store_true", help="only time one full-size rating; save nothing")
    md.add_argument("--llm-eval", metavar="CSV", help="only rate the checked-out candidates into this file; save nothing")
    md.add_argument("--gold", help="with --llm-eval: hand labels to score the answers against (JSON)")
    md.add_argument("--summary", help="append a markdown summary here (e.g. $GITHUB_STEP_SUMMARY)")
    md.add_argument("--github-output", help="write finished=true|false here ($GITHUB_OUTPUT)")
    md.set_defaults(func=cmd_model)

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
