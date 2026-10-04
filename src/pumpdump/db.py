"""SQLite working store: documents, ticker mentions and windowed counts.

Every row keeps `created_utc` (when the post/comment was written) and
`collected_at` (when our collector first received it). Counting functions take
an `as_of` time and, in strict mode, only see documents collected by then, so
a replay over history never uses information we didn't have at that moment.
"""

from __future__ import annotations

import json
import sqlite3
from typing import Collection, Iterable

from .hype import MIN_HYPE_CATEGORIES, hype_categories
from .spikes import DAY, TickerWindow
from .tickers import TickerExtractor

DOC_COLUMNS = [
    "id",
    "kind",
    "subreddit",
    "author",
    "created_utc",
    "collected_at",
    "source",
    "source_retrieved_at",
    "title",
    "body",
    "link_id",
    "parent_id",
    "url",
    "permalink",
    "flair",
    "score",
    "num_comments",
    "upvote_ratio",
    "removed_by_category",
    "run_id",
    "fetch_mode",
]

SCHEMA = """
CREATE TABLE IF NOT EXISTS docs (
    id TEXT PRIMARY KEY,                 -- t3_ post / t1_ comment fullname
    kind TEXT NOT NULL,                  -- 'post' | 'comment'
    subreddit TEXT NOT NULL,
    author TEXT,
    created_utc INTEGER NOT NULL,        -- written on Reddit (epoch s, UTC)
    collected_at REAL NOT NULL,          -- first received by our collector
    source TEXT NOT NULL,
    source_retrieved_at INTEGER,         -- when Arctic Shift archived it
    title TEXT,
    body TEXT,                           -- selftext for posts
    link_id TEXT,
    parent_id TEXT,
    url TEXT,
    permalink TEXT,
    flair TEXT,
    score INTEGER,                       -- as received; NOT a decision-time feature
    num_comments INTEGER,
    upvote_ratio REAL,
    removed_by_category TEXT,
    run_id TEXT,
    fetch_mode TEXT,                     -- backfill | live | reconcile
    extracted INTEGER NOT NULL DEFAULT 0
);
CREATE INDEX IF NOT EXISTS docs_created ON docs(created_utc);
CREATE INDEX IF NOT EXISTS docs_link ON docs(link_id);

CREATE TABLE IF NOT EXISTS mentions (
    doc_id TEXT NOT NULL,
    ticker TEXT NOT NULL,
    method TEXT NOT NULL,                -- exchange | cashtag | bare
    in_universe INTEGER NOT NULL,
    kind TEXT NOT NULL,
    subreddit TEXT NOT NULL,
    author TEXT,
    created_utc INTEGER NOT NULL,
    collected_at REAL NOT NULL,
    hype_score INTEGER NOT NULL,
    hype_categories TEXT,
    n_tickers INTEGER NOT NULL,          -- tickers mentioned in the same doc
    PRIMARY KEY (doc_id, ticker)
);
CREATE INDEX IF NOT EXISTS mentions_ticker_time ON mentions(ticker, created_utc);
CREATE INDEX IF NOT EXISTS mentions_time ON mentions(created_utc);
"""

DELETED = "[deleted]"


def connect(path: str = ":memory:") -> sqlite3.Connection:
    conn = sqlite3.connect(path)
    conn.executescript(SCHEMA)
    return conn


def insert_docs(conn: sqlite3.Connection, records: Iterable[dict]) -> int:
    """Insert records; an id already present keeps its first-seen copy."""
    before = conn.total_changes
    placeholders = ",".join("?" * len(DOC_COLUMNS))
    conn.executemany(
        f"INSERT OR IGNORE INTO docs ({','.join(DOC_COLUMNS)}) VALUES ({placeholders})",
        ([r.get(c) for c in DOC_COLUMNS] for r in records),
    )
    conn.commit()
    return conn.total_changes - before


def existing_ids(conn: sqlite3.Connection, ids: Collection[str]) -> set[str]:
    found: set[str] = set()
    ids = list(ids)
    for i in range(0, len(ids), 500):
        chunk = ids[i : i + 500]
        q = f"SELECT id FROM docs WHERE id IN ({','.join('?' * len(chunk))})"
        found.update(row[0] for row in conn.execute(q, chunk))
    return found


def extract_mentions(conn: sqlite3.Connection, extractor: TickerExtractor, excluded_authors: Collection[str]) -> int:
    """Extract tickers and hype for every not-yet-processed doc. Returns mention rows added."""
    excluded = set(excluded_authors)
    rows = []
    done = []
    for doc_id, kind, sub, author, created, collected, title, body in conn.execute(
        "SELECT id, kind, subreddit, author, created_utc, collected_at, title, body FROM docs WHERE extracted = 0"
    ):
        done.append((doc_id,))
        if author in excluded:
            continue
        mentions = extractor.extract(title, body)
        if not mentions:
            continue
        cats = sorted(hype_categories(title, body))
        for m in mentions:
            rows.append(
                (doc_id, m.ticker, m.method, int(m.in_universe), kind, sub, author, created, collected, len(cats), ",".join(cats), len(mentions))
            )
    conn.executemany("INSERT OR IGNORE INTO mentions VALUES (?,?,?,?,?,?,?,?,?,?,?,?)", rows)
    conn.executemany("UPDATE docs SET extracted = 1 WHERE id = ?", done)
    conn.commit()
    return len(rows)


def window_counts(conn: sqlite3.Connection, as_of: float, n_days: int = 8, strict: bool = True) -> dict[str, TickerWindow]:
    """Per-ticker counts for day 0 = (as_of-24h, as_of] and days 1..n_days-1 before it."""
    q = f"""
        SELECT ticker,
               CAST((:t - created_utc) / {DAY} AS INTEGER) AS d,
               COUNT(*),
               COUNT(DISTINCT CASE WHEN author <> :del THEN author END),
               SUM(hype_score >= :h),
               COUNT(DISTINCT CASE WHEN hype_score >= :h AND author <> :del THEN author END)
        FROM mentions
        WHERE created_utc <= :t AND created_utc > :t - {n_days * DAY}
          AND (collected_at <= :t OR NOT :strict)
        GROUP BY ticker, d
    """
    out: dict[str, TickerWindow] = {}
    params = {"t": as_of, "del": DELETED, "h": MIN_HYPE_CATEGORIES, "strict": int(strict)}
    for ticker, d, n, a, h, ha in conn.execute(q, params):
        w = out.get(ticker)
        if w is None:
            w = out[ticker] = TickerWindow(ticker, [0] * n_days, [0] * n_days, [0] * n_days, 0)
        w.counts[d], w.authors[d], w.hype_docs[d] = n, a, h
        if d == 0:
            w.hype_authors_now = ha
    return out


def ticker_details(conn: sqlite3.Connection, as_of: float, ticker: str, n_examples: int = 3, strict: bool = True) -> dict:
    """Breakdown of the trailing 24h of mentions of one ticker, for candidate reports."""
    where = "ticker = :k AND created_utc <= :t AND created_utc > :t - 86400 AND (m.collected_at <= :t OR NOT :strict)"
    params = {"k": ticker, "t": as_of, "strict": int(strict)}
    by_sub = dict(
        conn.execute(f"SELECT subreddit, COUNT(*) FROM mentions m WHERE {where} GROUP BY subreddit ORDER BY subreddit", params).fetchall()
    )
    kinds = dict(conn.execute(f"SELECT kind, COUNT(*) FROM mentions m WHERE {where} GROUP BY kind", params).fetchall())
    examples = [
        "https://www.reddit.com" + p
        for (p,) in conn.execute(
            f"""SELECT d.permalink FROM mentions m JOIN docs d ON d.id = m.doc_id
                WHERE {where.replace('created_utc', 'm.created_utc')} AND d.permalink IS NOT NULL
                ORDER BY m.kind = 'post' DESC, m.created_utc DESC LIMIT :n""",
            {**params, "n": n_examples},
        )
    ]
    methods = dict(conn.execute(f"SELECT method, COUNT(*) FROM mentions m WHERE {where} GROUP BY method", params).fetchall())
    return {
        "by_subreddit": by_sub,
        "posts": kinds.get("post", 0),
        "comments": kinds.get("comment", 0),
        "methods": methods,
        "examples": examples,
    }


def to_json(obj) -> str:
    return json.dumps(obj, separators=(",", ":"), sort_keys=True)


DAILY_FIELDS = ["date", "ticker", "mentions", "authors", "posts", "comments", "hype_docs", "in_universe", "by_subreddit"]


def daily_counts(conn: sqlite3.Connection, day_start: int) -> list[dict]:
    """Mention counts for every ticker over one UTC day [day_start, day_start+24h).

    Kept for all tickers, flagged or not, so later stages can draw control
    groups ("chatter but no pump").
    """
    from datetime import datetime, timezone

    day = datetime.fromtimestamp(day_start, timezone.utc).strftime("%Y-%m-%d")
    params = {"a": day_start, "b": day_start + DAY, "del": DELETED, "h": MIN_HYPE_CATEGORIES}
    where = "created_utc >= :a AND created_utc < :b"
    by_sub: dict[str, dict[str, int]] = {}
    for ticker, sub, n in conn.execute(f"SELECT ticker, subreddit, COUNT(*) FROM mentions WHERE {where} GROUP BY ticker, subreddit", params):
        by_sub.setdefault(ticker, {})[sub] = n
    rows = []
    for ticker, n, a, posts, comments, h, inu in conn.execute(
        f"""SELECT ticker, COUNT(*), COUNT(DISTINCT CASE WHEN author <> :del THEN author END),
                   SUM(kind = 'post'), SUM(kind = 'comment'), SUM(hype_score >= :h), MAX(in_universe)
            FROM mentions WHERE {where} GROUP BY ticker ORDER BY ticker""",
        params,
    ):
        rows.append(
            {
                "date": day,
                "ticker": ticker,
                "mentions": n,
                "authors": a,
                "posts": posts,
                "comments": comments,
                "hype_docs": h,
                "in_universe": inu,
                "by_subreddit": to_json(by_sub.get(ticker, {})),
            }
        )
    return rows
