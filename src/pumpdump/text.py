"""Stage 5 text inputs: what the Reddit documents behind a flag said, read two ways.

The documents are exactly the ones behind an episode's `mentions_24h`: posts and comments that mention the ticker,
created in the 24 hours up to the flag and collected by then (bots excluded, as in Stage 1).

  text-v1  lexicon features: author concentration, copy-paste across authors, sales-pitch, squeeze, news and
           dilution vocabulary, outside links, watch lists, length
  llm-v1   a language model's ratings of the same documents (promotion, coordination, news, sentiment) from a small
           open-weights model that llama.cpp's server runs on the workflow's own runner: no account, key or service

Both are computed once per candidate, soon after the flag, and stored (model/text.csv, model/llm.csv). Design:
docs/stage5.md.
"""

from __future__ import annotations

import hashlib
import json
import math
import re
import time
from collections import Counter
from datetime import datetime, timezone
from typing import Callable

import requests

from .db import DELETED
from .spikes import DAY

TEXT_VERSION = "text-v1"
LLM_VERSION = "llm-v1"
TEXT = "model/text.csv"
LLM = "model/llm.csv"

TEXT_FEATURES = ["top_author_share", "dup_share", "promo_share", "squeeze_share", "news_share", "dilution_share",
                 "link_share", "multi_ticker_share", "length_log"]
LLM_FEATURES = ["llm_promotion", "llm_coordination", "llm_news", "llm_sentiment"]
TEXT_FIELDS = ["episode_id", "ticker", "as_of_utc", "n_docs", *TEXT_FEATURES, "computed_at_utc", "text_version"]
LLM_FIELDS = ["episode_id", "ticker", "as_of_utc", "status", *LLM_FEATURES, "llm_catalyst", "llm_summary", "n_docs",
              "prompt_sha", "model", "rated_at_utc", "error", "llm_version"]

PROMO_CATEGORIES = frozenset({"urgency", "price_target", "low_float", "gem", "next_big", "multibagger"})
_I = re.IGNORECASE
NEWS_RE = re.compile(
    r"\b(?:earnings|revenue|guidance|fda|approv(?:al|ed)|clinical\s+trials?|contracts?|partnerships?|mergers?"
    r"|acquisitions?|buyouts?|press\s+releases?|announced|8-?k)\b", _I)
DILUTION_RE = re.compile(r"\b(?:offerings?|dilut(?:ion|ive|ing)|warrants?|reverse\s+split|shelf|s-?[13]|424b\d?)\b", _I)
LINK_RE = re.compile(r"https?://(?!(?:[\w-]+\.)*(?:reddit\.com|redd\.it|imgur\.com|redditmedia\.com)\b)", _I)
_URL_RE = re.compile(r"https?://\S+", _I)
MIN_DUP_LETTERS = 20

# llm-v1: what the model reads
MAX_DOCS = 40
DOC_CHARS = 400
MAX_CHARS = 12_000
LLM_URL = "http://127.0.0.1:8080/v1/chat/completions"  # llama.cpp's OpenAI-compatible server (scripts/llm_server.sh)
LLM_MODEL = "unsloth/Qwen3-4B-Instruct-2507-GGUF@a06e946/Qwen3-4B-Instruct-2507-Q4_K_M.gguf"  # the workflow passes its own
CATALYSTS = ("none", "earnings", "regulatory", "deal", "financing", "other")
SYSTEM_PROMPT = ("You rate Reddit chatter about one stock for a research project that detects pump-and-dump schemes. "
                 "Judge only what the posts below show. Reply with one JSON object and nothing else.")
RATING_PROMPT = """Rate the chatter:
- promotion: 0-3, how much of it is a sales pitch to get others to buy (price targets, urgency, "get in before", rockets, low-float pitches). 0 none, 3 mostly.
- coordination: 0-3, signs of coordinated or bot-like posting (the same phrases from different authors, near-identical posts, one author posting again and again). 0 none, 3 strong.
- news: 0-3, how much the discussion is about a concrete, checkable company event (earnings, an FDA or regulatory decision, a contract, a merger, an offering) rather than price action. 0 none, 3 mainly.
- sentiment: -2 to 2, bearish to bullish.
- catalyst: the main company event discussed: none, earnings, regulatory, deal, financing or other.
- summary: one sentence on what the chatter is about.
Reply as {"promotion": 0, "coordination": 0, "news": 0, "sentiment": 0, "catalyst": "none", "summary": "..."}"""


def _hhmm(ts: float, fmt: str = "%m-%d %H:%M") -> str:
    return datetime.fromtimestamp(ts, timezone.utc).strftime(fmt)


def flag_documents(conn, ticker: str, as_of: float) -> list[dict]:
    """The documents behind the episode's mentions_24h, oldest first (needs Stage 1's `mentions` table filled)."""
    q = """SELECT d.id, d.kind, d.subreddit, d.author, d.created_utc, d.title, d.body, d.url, m.hype_categories, m.n_tickers
           FROM mentions m JOIN docs d ON d.id = m.doc_id
           WHERE m.ticker = ? AND m.created_utc > ? AND m.created_utc <= ? AND m.collected_at <= ?
           ORDER BY m.created_utc, d.id"""
    cols = ["id", "kind", "subreddit", "author", "created_utc", "title", "body", "url", "hype_categories", "n_tickers"]
    return [dict(zip(cols, row)) for row in conn.execute(q, (ticker, as_of - DAY, as_of, as_of))]


def _author_key(d: dict) -> str:
    # deleted accounts can't be told apart, so each such document stands alone
    a = d.get("author")
    return a if a and a != DELETED else f"?{d['id']}"


def _dup_key(d: dict, ticker: str) -> str | None:
    t = _URL_RE.sub(" ", f"{d.get('title') or ''} {d.get('body') or ''}".lower())
    t = re.sub(r"\$?\b" + re.escape(ticker.lower()) + r"\b", " ", t)
    t = re.sub(r"[^a-z]+", " ", t).strip()
    return t[:200] if sum(c.isalpha() for c in t) >= MIN_DUP_LETTERS else None


def text_features(docs: list[dict], ticker: str) -> dict:
    """text-v1 features of the flag documents (docs/stage5.md); all blank when there are none."""
    n = len(docs)
    out: dict = {"n_docs": n, **dict.fromkeys(TEXT_FEATURES)}
    if not n:
        return out
    authors = Counter(_author_key(d) for d in docs)
    keys = [_dup_key(d, ticker) for d in docs]
    key_authors: dict[str, set] = {}
    for d, k in zip(docs, keys):
        if k:
            key_authors.setdefault(k, set()).add(_author_key(d))
    cats = [set(filter(None, (d.get("hype_categories") or "").split(","))) for d in docs]
    texts = [f"{d.get('title') or ''}\n{d.get('body') or ''}" for d in docs]

    def share(flags) -> float:
        return round(sum(1 for f in flags if f) / n, 6)

    out.update(
        top_author_share=share([True] * max(authors.values())),
        dup_share=share(k is not None and len(key_authors[k]) > 1 for k in keys),
        promo_share=share(c & PROMO_CATEGORIES for c in cats),
        squeeze_share=share("squeeze" in c for c in cats),
        news_share=share(NEWS_RE.search(t) for t in texts),
        dilution_share=share(DILUTION_RE.search(t) for t in texts),
        link_share=share(LINK_RE.search(f"{t}\n{d.get('url') or ''}") for t, d in zip(texts, docs)),
        multi_ticker_share=share((d.get("n_tickers") or 1) > 1 for d in docs),
        length_log=round(math.log1p(sum(len(d.get("title") or "") + len(d.get("body") or "") for d in docs) / n), 6),
    )
    return out


def _flat(text: str | None) -> str:
    return re.sub(r"\s+", " ", text or "").strip()


def _filings_line(snap: dict) -> str:
    if not snap.get("cik"):
        return "The company is not an SEC filer, so there are no SEC filings on record."
    parts = []
    if snap.get("last_current_report_at"):
        items = snap.get("last_current_report_items") or ""
        parts.append(f"last 8-K/6-K on {snap['last_current_report_at'][:10]}" + (f" (items {items})" if items else ""))
    if snap.get("last_dilution_at"):
        parts.append(f"last registration or prospectus: {snap.get('last_dilution_form') or 'filing'} on "
                     f"{snap['last_dilution_at'][:10]}")
    return "SEC filings before the cut-off: " + ("; ".join(parts) if parts else "none on record") + "."


def select_documents(docs: list[dict]) -> list[dict]:
    """Posts first (oldest first), then the most recent comments, within MAX_DOCS and MAX_CHARS."""
    posts = [d for d in docs if d["kind"] == "post"]
    comments = sorted((d for d in docs if d["kind"] != "post"), key=lambda d: d["created_utc"], reverse=True)
    chosen, total = [], 0
    for d in posts + comments:
        size = min(DOC_CHARS, len(_flat(" | ".join(filter(None, [d.get("title"), d.get("body")])))))
        if len(chosen) >= MAX_DOCS or total + size > MAX_CHARS - 60 * (len(chosen) + 1):
            break
        chosen.append(d)
        total += size
    return [d for d in posts if d in chosen] + sorted((d for d in chosen if d["kind"] != "post"),
                                                       key=lambda d: d["created_utc"])


def build_prompt(snap: dict, docs: list[dict], as_of: float) -> tuple[str, str]:
    """(system, user) messages of llm-v1 for one candidate."""
    chosen = select_documents(docs)
    alias: dict[str, str] = {}
    lines = []
    for i, d in enumerate(chosen, 1):
        key = _author_key(d)
        if key.startswith("?"):
            who = "deleted"
        else:
            who = alias.setdefault(key, f"A{len(alias) + 1}")
        body = _flat(" | ".join(filter(None, [d.get("title"), d.get("body")])))[:DOC_CHARS]
        lines.append(f"[{i}] {d['kind']}, r/{d['subreddit']}, {who}, {_hhmm(d['created_utc'])}: {body}")
    venue = {"listed": "listed on a US exchange", "otc": "traded over the counter"}.get(snap.get("venue") or "", "venue unknown")
    price = f"${float(snap['price_at_flag']):g}" if snap.get("price_at_flag") else "unknown"
    user = "\n".join([
        f"Stock: {snap['ticker']} ({snap.get('name') or 'name unknown'}), {venue}, price {price} at the cut-off.",
        _filings_line(snap),
        f"Cut-off: {_hhmm(as_of, '%Y-%m-%d %H:%M')} UTC. Below are {len(chosen)} of the {len(docs)} Reddit posts and "
        "comments that mentioned the stock in the 24 hours before it (authors anonymised as A1, A2, ...):",
        "",
        *lines,
        "",
        RATING_PROMPT,
    ])
    return SYSTEM_PROMPT, user


def _clamp(v, lo: int, hi: int) -> int:
    if isinstance(v, bool) or not isinstance(v, (int, float)):
        raise ValueError(f"not a number: {v!r}")
    return max(lo, min(hi, round(v)))


def parse_rating(content: str) -> dict:
    """The llm-v1 fields from the model's reply; ValueError if it isn't the JSON asked for."""
    m = re.search(r"\{.*\}", content or "", re.S)
    if not m:
        raise ValueError("no JSON object in the reply")
    obj = json.loads(m.group(0))
    catalyst = str(obj.get("catalyst") or "none").strip().lower()
    return {
        "llm_promotion": _clamp(obj.get("promotion"), 0, 3),
        "llm_coordination": _clamp(obj.get("coordination"), 0, 3),
        "llm_news": _clamp(obj.get("news"), 0, 3),
        "llm_sentiment": _clamp(obj.get("sentiment"), -2, 2),
        "llm_catalyst": catalyst if catalyst in CATALYSTS else "other",
        "llm_summary": _flat(str(obj.get("summary") or ""))[:300],
    }


def prompt_sha(system: str, user: str) -> str:
    return hashlib.sha256(f"{system}\n\n{user}".encode()).hexdigest()[:16]


class LLMError(Exception):
    """The call failed in a way that may pass (rate limit, outage, missing permission): try again on a later run."""


class LLMRefused(LLMError):
    """The service rejected this prompt (e.g. its content filter): retrying the same prompt won't help."""


class ChatClient:
    """Minimal client for an OpenAI-compatible chat endpoint; by default llama.cpp's server on this machine."""

    def __init__(self, url: str = LLM_URL, model: str = LLM_MODEL, post: Callable = requests.post,
                 sleep: Callable[[float], None] = time.sleep, clock: Callable[[], float] = time.monotonic,
                 min_interval: float = 0.0, timeout: float = 900):
        self.url, self.model, self.post, self.sleep, self.clock = url, model, post, sleep, clock
        self.min_interval, self.timeout = min_interval, timeout  # a long prompt takes a CPU a minute or two
        self._last: float | None = None

    def complete(self, system: str, user: str) -> str:
        if self._last is not None:
            wait = self._last + self.min_interval - self.clock()
            if wait > 0:
                self.sleep(wait)
        try:
            r = self.post(self.url, timeout=self.timeout, headers={"Content-Type": "application/json"},
                          json={"model": self.model, "temperature": 0, "seed": 0, "max_tokens": 400,
                                "response_format": {"type": "json_object"},
                                "messages": [{"role": "system", "content": system}, {"role": "user", "content": user}]})
        except requests.RequestException as exc:
            raise LLMError(f"network: {exc}") from exc
        finally:
            self._last = self.clock()
        if r.status_code == 400 and "content_filter" in r.text:  # a hosted model's filter refused this prompt
            raise LLMRefused(f"HTTP 400: {r.text[:200]}")
        if r.status_code != 200:
            raise LLMError(f"HTTP {r.status_code}: {r.text[:200]}")
        try:
            return r.json()["choices"][0]["message"]["content"]
        except (ValueError, KeyError, IndexError, TypeError) as exc:
            raise LLMError(f"unexpected reply: {r.text[:200]}") from exc


def probe_llm(llm, clock: Callable[[], float] = time.monotonic) -> tuple[bool, list[str]]:
    """Time one full-size rating (as long as a real prompt gets) and check that it parses; nothing is saved."""
    as_of = time.time()
    docs = [{"id": f"t1_{i}", "kind": "comment", "subreddit": "pennystocks", "author": f"user{i % 9}",
             "created_utc": as_of - 3600 + i, "title": None,
             "body": f"$ABCD comment {i}: short squeeze incoming, low float, get in before the news " + "x" * 400}
            for i in range(MAX_DOCS)]
    snap = {"ticker": "ABCD", "name": "Abcd Inc.", "venue": "listed", "price_at_flag": "3.21", "cik": ""}
    system, user = build_prompt(snap, docs, as_of)
    t0 = clock()
    answer = llm.complete(system, user)
    lines = [f"{getattr(llm, 'model', '')}: a {len(system) + len(user)}-character prompt answered in "
             f"{clock() - t0:.0f} s: {answer[:300]!r}"]
    try:
        lines.append(f"parsed: {parse_rating(answer)}")
        return True, lines
    except ValueError as exc:
        lines.append(f"could not parse: {exc}")
        return False, lines
