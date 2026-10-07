"""`python -m pumpdump.crypto run|history|classify` (docs/crypto.md)."""

from __future__ import annotations

import argparse
import json
import os
import sys
import time

from ..store import Datastore


def render(summary: dict, title: str) -> str:
    lines = [f"## {title}", ""]
    for k, v in summary.items():
        if k == "errors":
            continue
        lines.append(f"- **{k}**: {json.dumps(v, ensure_ascii=False) if isinstance(v, (dict, list)) else v}")
    if summary.get("errors"):
        lines += ["", f"{len(summary['errors'])} errors (first ones):", *[f"- {e[:200]}" for e in summary["errors"][:15]]]
    return "\n".join(lines) + "\n"


def main(argv: list[str] | None = None) -> int:
    p = argparse.ArgumentParser(prog="python -m pumpdump.crypto")
    sub = p.add_subparsers(dest="cmd", required=True)
    r = sub.add_parser("run", help="one hourly run: Telegram, scan, due bars, outcomes")
    h = sub.add_parser("history", help="add the public pump lists and fetch their Binance/KuCoin bars (resumable)")
    for a in (r, h):
        a.add_argument("--datastore", required=True)
        a.add_argument("--run-id", default=os.environ.get("GITHUB_RUN_ID") or time.strftime("%Y%m%dT%H%M%S", time.gmtime()))
        a.add_argument("--max-minutes", type=float, default=20.0)
        a.add_argument("--summary", help="append a markdown summary here ($GITHUB_STEP_SUMMARY)")
        a.add_argument("--github-output", help="write finished=true|false here ($GITHUB_OUTPUT)")
    h.add_argument("--pumpsense-dir", help="checkout of the PumpSense repository (chat_data/*/result11.csv)")
    c = sub.add_parser("classify", help="print the tg-v1 class of a post's text")
    c.add_argument("text")
    c.add_argument("--after-countdown", action="store_true")
    args = p.parse_args(argv)

    if args.cmd == "classify":
        from .telegram import classify
        print(json.dumps(classify(args.text, [], args.after_countdown).__dict__))
        return 0

    ds = Datastore(args.datastore)
    if args.cmd == "run":
        from .run import run_crypto
        summary = run_crypto(ds, str(args.run_id), max_seconds=args.max_minutes * 60)
        title = f"Crypto run {args.run_id}"
    else:
        from .history import run_history
        summary = run_history(ds, str(args.run_id), args.pumpsense_dir, max_seconds=args.max_minutes * 60)
        title = f"Crypto history run {args.run_id}"
    text = render(summary, title)
    print(text)
    if args.summary:
        with open(args.summary, "a", encoding="utf-8") as fh:
            fh.write(text)
    if args.github_output:
        with open(args.github_output, "a", encoding="utf-8") as fh:
            fh.write(f"finished={'true' if summary.get('finished') else 'false'}\n")
    return 0


if __name__ == "__main__":
    sys.exit(main())
