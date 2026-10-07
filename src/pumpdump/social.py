"""Twitter-like chatter about each candidate and control: StockTwits, Bluesky and (if paid for) X.

Started after every collect run (the `social` workflow). For each Stage 1 candidate, and for each of Stage 2's
matched controls once its market snapshot exists, it fetches the posts of the 72 hours before the flag and
since, stores them raw, and writes one row of flag-time features to social/snapshots.csv. Each candidate then
gets a follow-up row about once a day for 10 days (the posts since the previous row), which shows the chatter
through the pump and the dump. It adds data only: it never changes which tickers get flagged.

No lookahead: the `flag` row's features count only posts created before the flag. Posts deleted before the
fetch are missing, so `lag_s` (fetch time minus flag time) is recorded; the first rows of old episodes were
fetched days late. Design notes: docs/social.md.
"""

from __future__ import annotations

import gzip
import io
import json
import os
import re
import statistics
from collections import Counter
from typing import Callable

from .features import iso
from .market import SNAPSHOTS as MARKET_SNAPSHOTS
from .pipeline import Settings, collection_done
from .sources import social as src
from .sources.web import Web
from .store import Datastore, _atomic_write_bytes, utc_dt

SOCIAL_VERSION = "social-v1"
SNAPSHOTS = "social/snapshots.csv"
README = "social/README.md"
HOUR = 3600.0
DAY = 86400.0
PRE_FLAG_S = 72 * HOUR  # posts fetched before the flag
FEATURE_S = 24 * HOUR  # flag-row features: the 24 hours before the flag
FOLLOW_DAYS = 10  # follow-up rows per candidate
FOLLOW_EVERY_S = 23.5 * HOUR
NEW_ACCOUNT_S = 90 * DAY
STOCKTWITS_PAGES = 10  # 300 messages per ticker and row
BLUESKY_PAGES = 3
STOCKTWITS_REQUESTS_PER_RUN = 80
RETRY_S = (FOLLOW_DAYS + 1) * DAY  # a failed StockTwits fetch is retried next run until then, then kept with its error

SOURCES = {"st": "stocktwits", "bsky": "bluesky", "x": "x"}
STATS = ["n", "authors", "top_author_share", "new_acct_share", "median_followers", "bull_share", "dup_share"]
SNAPSHOT_FIELDS = (
    ["snap_key", "episode_id", "ticker", "role", "phase", "flag_at", "flag_at_utc", "window_start_utc",
     "window_end_utc", "collected_at", "collected_at_utc", "lag_s"]
    + [f"{p}_{s}" for p in SOURCES for s in [*STATS, "n_72h", "n_after_flag", "fetched", "truncated"]]
    + ["errors", "social_version"]
)

README_TEXT = """# Social chatter (StockTwits, Bluesky, X)

Written by the `social` workflow (docs/social.md on main). One row in `snapshots.csv` per fetch:

- `phase` = `flag`: the first fetch for a candidate or control. Features (`st_*` StockTwits, `bsky_*` Bluesky,
  `x_*` X) count posts created in the 24 hours **before** the flag, so they are safe model inputs; `*_n_72h`
  covers 72 hours before, `*_n_after_flag` the posts between the flag and the fetch.
- `phase` = `d1` ... `d10`: candidates only, about daily for 10 days; features count the posts in
  `[window_start_utc, window_end_utc)`, i.e. since the previous row. Not for flag-time models (lookahead).
- `lag_s`: fetch time minus flag time. Deleted posts are missing, so large lags undercount promoters.
- `*_truncated` = 1: the page limit was hit, so counts are lower bounds (very busy tickers).
- `*_fetched`: posts fetched for the row (for X, what was billed).

Raw posts: `raw/YYYY/MM/DD/<snap_key>.json.gz` by fetch date, with every post's text, author, follower count and
account age where the source gives them.
"""


def _norm(text: str) -> str:
    text = re.sub(r"https?://\S+", "", text.lower())
    return re.sub(r"[^a-z$]+", " ", text).strip()


def stats(posts: list[dict], start: float, end: float) -> dict:
    """Features of the posts created in [start, end)."""
    w = [p for p in posts if p["created_at"] is not None and start <= p["created_at"] < end]
    out = dict.fromkeys(STATS, "")
    out["n"] = len(w)
    if not w:
        return out
    by_author = Counter(p["author_id"] for p in w)
    out["authors"] = len(by_author)
    out["top_author_share"] = round(by_author.most_common(1)[0][1] / len(w), 4)
    joined = [p for p in w if p.get("author_joined") is not None]
    if joined:
        out["new_acct_share"] = round(sum(p["created_at"] - p["author_joined"] < NEW_ACCOUNT_S for p in joined) / len(joined), 4)
    followers = [p["author_followers"] for p in w if isinstance(p.get("author_followers"), (int, float))]
    if followers:
        out["median_followers"] = statistics.median(followers)
    bull = sum(p.get("sentiment") == "bullish" for p in w)
    bear = sum(p.get("sentiment") == "bearish" for p in w)
    if bull + bear:
        out["bull_share"] = round(bull / (bull + bear), 4)
    texts = Counter(_norm(p["text"]) for p in w if _norm(p["text"]))
    out["dup_share"] = round(sum(c for c in texts.values() if c > 1) / len(w), 4)
    return out


def targets(ds: Datastore) -> list[dict]:
    """Every candidate, plus every control that has a market snapshot, with its flag time."""
    out = []
    for e in ds.read_csv("candidates/episodes.csv"):
        out.append({"episode_id": e["episode_id"], "ticker": e["ticker"], "role": "candidate",
                    "flag_at": float(e["first_flagged_at"])})
    for m in ds.read_csv(MARKET_SNAPSHOTS):
        if m.get("role") == "control":
            out.append({"episode_id": m["episode_id"], "ticker": m["ticker"], "role": "control",
                        "flag_at": float(m["as_of"])})
    return out


def due(ds: Datastore, now: float) -> list[dict]:
    """Rows to fetch now: missing flag rows (newest flag first), then follow-ups that are a day old."""
    rows: dict[tuple, list[dict]] = {}
    for r in ds.read_csv(SNAPSHOTS):
        rows.setdefault((r["episode_id"], r["ticker"]), []).append(r)
    flags, follows = [], []
    for t in targets(ds):
        done = rows.get((t["episode_id"], t["ticker"]), [])
        if not done:
            flags.append({**t, "phase": "flag", "start": t["flag_at"] - PRE_FLAG_S})
            continue
        if t["role"] != "candidate" or len(done) > FOLLOW_DAYS or now - t["flag_at"] > (FOLLOW_DAYS + 1) * DAY:
            continue
        last = max(float(r["collected_at"]) for r in done)
        if now - last >= FOLLOW_EVERY_S:
            follows.append({**t, "phase": f"d{len(done)}", "start": last})
    flags.sort(key=lambda t: -t["flag_at"])
    follows.sort(key=lambda t: t["flag_at"])
    return flags + follows


def x_used_today(ds: Datastore, now: float) -> int:
    day = utc_dt(now).date()
    return sum(int(r.get("x_fetched") or 0) for r in ds.read_csv(SNAPSHOTS)
               if r.get("collected_at") and utc_dt(float(r["collected_at"])).date() == day)


def snapshot(web: Web, t: dict, now: float, x_token: str, x_budget: int) -> tuple[dict, dict]:
    """Fetch one row's posts from every source; returns (row, raw)."""
    fetched = {"st": src.fetch_stocktwits(web, t["ticker"], t["start"], STOCKTWITS_PAGES),
               "bsky": src.fetch_bluesky(web, t["ticker"], t["start"], BLUESKY_PAGES)}
    if x_token and x_budget >= 10:
        fetched["x"] = src.fetch_x(web, t["ticker"], t["start"], min(100, x_budget), x_token)
    flag, key = t["flag_at"], f"{t['episode_id']}_{t['ticker']}_{t['phase']}"
    if t["phase"] == "flag":
        start, end = flag - FEATURE_S, flag
    else:
        start, end = t["start"], now
    row = dict.fromkeys(SNAPSHOT_FIELDS, "")
    row |= {"snap_key": key, "episode_id": t["episode_id"], "ticker": t["ticker"], "role": t["role"],
           "phase": t["phase"], "flag_at": flag, "flag_at_utc": iso(flag), "window_start_utc": iso(start),
           "window_end_utc": iso(end), "collected_at": round(now, 3), "collected_at_utc": iso(now),
           "lag_s": round(now - flag), "social_version": SOCIAL_VERSION}
    errors = []
    for p, (posts, info) in fetched.items():
        failed = info["error"] and info["error"] != "not on StockTwits"
        if not failed:  # a failed fetch leaves the counts blank (unknown), not 0
            row.update({f"{p}_{k}": v for k, v in stats(posts, start, end).items()})
        if t["phase"] == "flag" and not failed:
            row[f"{p}_n_72h"] = sum(1 for q in posts if flag - PRE_FLAG_S <= q["created_at"] < flag)
            row[f"{p}_n_after_flag"] = sum(1 for q in posts if q["created_at"] >= flag)
        row[f"{p}_fetched"] = len(posts)
        row[f"{p}_truncated"] = int(info["truncated"])
        if info["error"]:
            errors.append(info["error"])
    row["errors"] = "; ".join(errors)
    raw = {"snap_key": key, "collected_at": now, "since": t["start"],
           "posts": {SOURCES[p]: posts for p, (posts, _) in fetched.items()},
           "info": {SOURCES[p]: info for p, (_, info) in fetched.items()}}
    return row, raw


def write_raw(ds: Datastore, raw: dict) -> None:
    rel = f"social/raw/{utc_dt(raw['collected_at']).strftime('%Y/%m/%d')}/{raw['snap_key']}.json.gz"
    buf = io.BytesIO()
    with gzip.GzipFile(fileobj=buf, mode="wb", mtime=0) as gz:
        gz.write(json.dumps(raw, ensure_ascii=False, separators=(",", ":")).encode())
    _atomic_write_bytes(ds.path(rel), buf.getvalue())


def run_social(ds: Datastore, web: Web, clock: Callable[[], float], max_seconds: float,
               x_token: str = "", x_daily_posts: int = 0) -> dict:
    started = clock()
    todo = due(ds, started)
    summary = {"written": [], "pending": len(todo), "warnings": [], "st_requests": 0}
    x_left = max(0, x_daily_posts - x_used_today(ds, started)) if x_token else 0
    for t in todo:
        if clock() - started > max_seconds or summary["st_requests"] >= STOCKTWITS_REQUESTS_PER_RUN:
            break
        now = clock()
        row, raw = snapshot(web, t, now, x_token, x_left)
        summary["st_requests"] += raw["info"]["stocktwits"]["requests"]
        st_error = raw["info"]["stocktwits"]["error"]
        if st_error and st_error != "not on StockTwits" and now - t["flag_at"] < RETRY_S:
            summary["warnings"].append(f"{row['snap_key']}: {row['errors']} (retried next run)")
            continue
        x_left -= int(row.get("x_fetched") or 0)
        write_raw(ds, raw)
        ds.append_csv(SNAPSHOTS, SNAPSHOT_FIELDS, [row])
        summary["written"].append(row)
        if row["errors"]:
            summary["warnings"].append(f"{row['snap_key']}: {row['errors']}")
    if summary["written"] and not ds.path(README).exists():
        ds.write_text(README, README_TEXT)
    summary["pending"] -= len(summary["written"])
    return summary


def finished(ds: Datastore, now: float) -> bool:
    """Over once collection has stopped and nothing is left to fetch."""
    return collection_done(ds, ds.load_state(), now, Settings()) is not None and not due(ds, now)


def render_summary(summary: dict, run_id: str) -> str:
    lines = [f"## Social run {run_id}", "",
             f"Wrote {len(summary['written'])} rows ({summary['st_requests']} StockTwits requests); "
             f"{summary['pending']} still due.", ""]
    if summary["written"]:
        lines += ["| Row | Lag | StockTwits 24h pre-flag / window | Bluesky | X | New accounts (ST) | Bullish (ST) |",
                  "|---|---|---|---|---|---|---|"]
        for r in summary["written"]:
            lines.append(f"| {r['snap_key']} | {int(r['lag_s']) // 3600}h | {r['st_n']} | {r['bsky_n']} | "
                         f"{r.get('x_n', '')} | {r['st_new_acct_share']} | {r['st_bull_share']} |")
    if summary["warnings"]:
        lines += ["", "Warnings:"] + [f"- {w}" for w in summary["warnings"]]
    return "\n".join(lines) + "\n"


def x_settings() -> tuple[str, int]:
    """X_BEARER_TOKEN (repo secret) turns X on; X_DAILY_POSTS caps posts read per day (default 200 = $1 at $0.005)."""
    token = os.environ.get("X_BEARER_TOKEN", "").strip()
    return token, int(os.environ.get("X_DAILY_POSTS") or 200) if token else 0
