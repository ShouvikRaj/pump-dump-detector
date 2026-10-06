"""Stage 5 text inputs: what the Reddit documents behind a flag said, read two ways.

The documents are exactly the ones behind an episode's `mentions_24h`: posts and comments that mention the ticker,
created in the 24 hours up to the flag and collected by then (bots excluded, as in Stage 1).

  text-v2  lexicon features: author concentration, copy-paste and near-copies across authors, sales-pitch, squeeze,
           news and dilution vocabulary, outside links, watch lists, length
  llm-v2   a language model's label for each of the same documents, by number (other, not this company, pitch,
           warning, company event, with a quote of the event), checked against the documents and turned into shares,
           from a small open-weights model that llama.cpp's server runs on the workflow's own runner: no account, key
           or service

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
from dataclasses import dataclass
from datetime import datetime, timezone
from difflib import SequenceMatcher
from typing import Callable

import requests

from .db import DELETED
from .spikes import DAY

TEXT_VERSION = "text-v2"
LLM_VERSION = "llm-v2"
TEXT = "model/text.csv"
LLM = "model/llm.csv"

TEXT_FEATURES = ["top_author_share", "dup_share", "promo_share", "squeeze_share", "news_share", "dilution_share",
                 "link_share", "multi_ticker_share", "length_log", "near_dup_share"]
LLM_FEATURES = ["llm_about_share", "llm_pitch_share", "llm_warning_share", "llm_event_share", "llm_sentiment"]
LLM_LISTS = ("not_about", "pitch", "warning", "event")
LABELS = ("other", "not_this_company", "pitch", "warning", "event", "pitch_and_event")  # one per document
_IN_LIST = {"not_about": ("not_this_company",), "pitch": ("pitch", "pitch_and_event"), "warning": ("warning",),
            "event": ("event", "pitch_and_event")}
# columns are only ever added at the end, so older rows keep theirs (llm-v1 rated promotion, coordination and news 0-3)
TEXT_FIELDS = ["episode_id", "ticker", "as_of_utc", "n_docs", *TEXT_FEATURES[:-1], "computed_at_utc", "text_version",
               "near_dup_share"]
LLM_FIELDS = ["episode_id", "ticker", "as_of_utc", "status", "llm_promotion", "llm_coordination", "llm_news",
              "llm_sentiment", "llm_catalyst", "llm_summary", "n_docs", "prompt_sha", "model", "rated_at_utc", "error",
              "llm_version", "llm_about_share", "llm_pitch_share", "llm_warning_share", "llm_event_share",
              "llm_event_quote", "llm_checks", "llm_lists", "n_shown"]

PROMO_CATEGORIES = frozenset({"urgency", "price_target", "low_float", "gem", "next_big", "multibagger"})
_I = re.IGNORECASE
NEWS_RE = re.compile(
    r"\b(?:earnings|revenue|guidance|fda|approv(?:al|ed)|clinical\s+trials?|contracts?|partnerships?|mergers?"
    r"|acquisitions?|buyouts?|press\s+releases?|announced|8-?k)\b", _I)
DILUTION_RE = re.compile(r"\b(?:offerings?|dilut(?:ion|ive|ing)|warrants?|reverse\s+split|shelf|s-?[13]|424b\d?)\b", _I)
LINK_RE = re.compile(r"https?://(?!(?:[\w-]+\.)*(?:reddit\.com|redd\.it|imgur\.com|redditmedia\.com)\b)", _I)
_URL_RE = re.compile(r"https?://\S+", _I)
MIN_DUP_LETTERS = 20
NEAR_DUP_JACCARD = 0.5  # share of 3-word shingles two documents have in common
MIN_NEAR_DUP_WORDS = 8

# llm-v2: what the model reads and how it answers
MAX_DOCS = 40
DOC_CHARS = 400
MAX_CHARS = 12_000
QUOTE_MATCH = 0.8  # an event quote counts when this much of it appears, in one piece, in a document
LLM_URL = "http://127.0.0.1:8080/v1/chat/completions"  # llama.cpp's OpenAI-compatible server (scripts/llm_server.sh)
LLM_MODEL = "unsloth/Qwen3.5-9B-GGUF@3885219/Qwen3.5-9B-Q4_K_M.gguf"  # the workflow passes its own
CATALYSTS = ("none", "earnings", "regulatory", "deal", "financing", "other")
SYSTEM_PROMPT = ("You label Reddit posts and comments about one stock for a research project that detects "
                 "pump-and-dump schemes. Use only the documents shown, not what you know or guess about the company. "
                 "Reply with one JSON object and nothing else.")
LABEL_PROMPT = """Give every document one label, by its number:
- other: about {name} but none of the labels below. Most documents are "other": questions, price talk, opinions, jokes, saying one owns {ticker}, likes it or expects it to rise.
- not_this_company: "{ticker}" here means something other than {name}: another company or fund, an index or economic report, an abbreviation or an ordinary word.
- pitch: tries to get others to buy {ticker}: price targets, rockets or "to the moon", "about to pop", "squeeze incoming", urgency ("don't miss", "get in before"), or telling people to buy.
- warning: calls {ticker} a pump-and-dump, scam or rug pull, or warns others of dilution, an offering or a coming dump. Plain bearish opinions are "other".
- event: states a specific company event, announced or scheduled: earnings, an FDA or other regulatory decision, a contract or government award, a partnership, a merger or acquisition, an offering or financing. Rumours, jokes, price moves and opinions are not events.
- pitch_and_event: both a pitch and an event.
Also give:
- summary: first, one short sentence (at most 20 words) on what the chatter is about.
- event_type: the main event in the event documents: none, earnings, regulatory, deal, financing or other.
- event_quote: up to 15 words copied exactly from one event document that state the event; "" when no document is an event.
- sentiment: -2 to 2, how bearish or bullish the documents about {name} are overall."""


def _hhmm(ts: float, fmt: str = "%m-%d %H:%M") -> str:
    return datetime.fromtimestamp(ts, timezone.utc).strftime(fmt)


def flag_documents(conn, ticker: str, as_of: float) -> list[dict]:
    """The documents behind the episode's mentions_24h, oldest first (needs Stage 1's `mentions` table filled)."""
    q = """SELECT d.id, d.kind, d.subreddit, d.author, d.created_utc, d.title, d.body, d.url, m.hype_categories, m.n_tickers,
                  m.method
           FROM mentions m JOIN docs d ON d.id = m.doc_id
           WHERE m.ticker = ? AND m.created_utc > ? AND m.created_utc <= ? AND m.collected_at <= ?
           ORDER BY m.created_utc, d.id"""
    cols = ["id", "kind", "subreddit", "author", "created_utc", "title", "body", "url", "hype_categories", "n_tickers",
            "method"]
    return [dict(zip(cols, row)) for row in conn.execute(q, (ticker, as_of - DAY, as_of, as_of))]


def _author_key(d: dict) -> str:
    # deleted accounts can't be told apart, so each such document stands alone
    a = d.get("author")
    return a if a and a != DELETED else f"?{d['id']}"


def _letters_only(d: dict, ticker: str) -> str:
    """Lower case, without links, the ticker, digits and punctuation: what stays the same in a copied pitch."""
    t = _URL_RE.sub(" ", f"{d.get('title') or ''} {d.get('body') or ''}".lower())
    t = re.sub(r"\$?\b" + re.escape(ticker.lower()) + r"\b", " ", t)
    return re.sub(r"[^a-z]+", " ", t).strip()


def _dup_key(d: dict, ticker: str) -> str | None:
    t = _letters_only(d, ticker)
    return t[:200] if sum(c.isalpha() for c in t) >= MIN_DUP_LETTERS else None


def _shingles(d: dict, ticker: str) -> set | None:
    words = _letters_only(d, ticker).split()
    return {tuple(words[i:i + 3]) for i in range(len(words) - 2)} if len(words) >= MIN_NEAR_DUP_WORDS else None


def _near_copies(docs: list[dict], ticker: str) -> list[bool]:
    """Whether each document shares at least NEAR_DUP_JACCARD of its 3-word shingles with one by another author."""
    sh = [_shingles(d, ticker) for d in docs]
    out = [False] * len(docs)
    for i in range(len(docs)):
        for j in range(i + 1, len(docs)):
            if sh[i] and sh[j] and _author_key(docs[i]) != _author_key(docs[j]) \
                    and len(sh[i] & sh[j]) >= NEAR_DUP_JACCARD * len(sh[i] | sh[j]):
                out[i] = out[j] = True
    return out


def text_features(docs: list[dict], ticker: str) -> dict:
    """text-v2 features of the flag documents (docs/stage5.md); all blank when there are none."""
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
        near_dup_share=share(_near_copies(docs, ticker)),
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


@dataclass
class Prompt:
    """One candidate's llm-v2 request: the messages, the documents shown (numbered from 1) and the answer's format."""
    system: str
    user: str
    docs: list
    schema: dict


def rating_schema(n: int) -> dict:
    """The JSON the model must answer with: one label for each document shown, in order. llama.cpp turns it into a
    grammar, so (unless the server drops the grammar) other output can't be produced."""
    nums = [str(i) for i in range(1, n + 1)]
    labels = {"type": "object", "properties": {k: {"enum": list(LABELS)} for k in nums}, "required": nums,
              "additionalProperties": False}
    props = {"summary": {"type": "string", "maxLength": 200}, "labels": labels,
             "event_type": {"enum": list(CATALYSTS)}, "event_quote": {"type": "string", "maxLength": 150},
             "sentiment": {"type": "integer", "minimum": -2, "maximum": 2}}
    return {"type": "object", "properties": props, "required": list(props), "additionalProperties": False}


def _doc_text(d: dict) -> str:
    return _flat(" | ".join(filter(None, [d.get("title"), d.get("body")])))[:DOC_CHARS]


def build_prompt(snap: dict, docs: list[dict], as_of: float) -> Prompt:
    """The llm-v2 request for one candidate."""
    chosen = select_documents(docs)
    alias: dict[str, str] = {}
    lines = []
    for i, d in enumerate(chosen, 1):
        key = _author_key(d)
        if key.startswith("?"):
            who = "deleted"
        else:
            who = alias.setdefault(key, f"A{len(alias) + 1}")
        lines.append(f"[{i}] {d['kind']}, r/{d['subreddit']}, {who}, {_hhmm(d['created_utc'])}: {_doc_text(d)}")
    venue = {"listed": "listed on a US exchange", "otc": "traded over the counter"}.get(snap.get("venue") or "", "venue unknown")
    price = f"${float(snap['price_at_flag']):g}" if snap.get("price_at_flag") else "unknown"
    name = snap.get("name") or "the company"
    user = "\n".join([
        f"Stock: {snap['ticker']} ({snap.get('name') or 'name unknown'}), {venue}, price {price} at the cut-off.",
        _filings_line(snap),
        f"Cut-off: {_hhmm(as_of, '%Y-%m-%d %H:%M')} UTC. Below are {len(chosen)} of the {len(docs)} Reddit posts and "
        "comments that mentioned the stock in the 24 hours before it (authors anonymised as A1, A2, ...):",
        "",
        *lines,
        "",
        LABEL_PROMPT.format(ticker=snap["ticker"], name=name),
    ])
    return Prompt(SYSTEM_PROMPT, user, chosen, rating_schema(len(chosen)))


def _clamp(v, lo: int, hi: int) -> int:
    if isinstance(v, bool) or not isinstance(v, (int, float)):
        raise ValueError(f"not a number: {v!r}")
    return max(lo, min(hi, round(v)))


def _norm(t: str) -> str:
    return re.sub(r"[^a-z0-9]+", " ", t.lower()).strip()


def quote_found(quote: str, texts: list[str]) -> bool:
    """Whether the quote (at least 8 characters) appears in one of the texts, allowing for small slips."""
    q = _norm(quote)
    if len(q) < 8:
        return False
    for t in map(_norm, texts):
        m = SequenceMatcher(None, q, t, autojunk=False).find_longest_match(0, len(q), 0, len(t))
        if m.size >= QUOTE_MATCH * len(q):
            return True
    return False


def parse_rating(content: str, prompt: Prompt) -> dict:
    """The llm-v2 fields from the model's reply, checked against the documents shown; ValueError if it isn't the
    JSON asked for. Labels for documents not shown, unknown labels and missing ones are unusable (the document counts
    as other), a document naming the stock as a cashtag (or with its exchange) is about the stock whatever the model
    says, and the event share counts only when the event quote is found in the documents."""
    m = re.search(r"\{.*\}", content or "", re.S)
    if not m:
        raise ValueError("no JSON object in the reply")
    obj = json.loads(m.group(0))
    n = len(prompt.docs)
    given = obj.get("labels")
    if not isinstance(given, dict):
        raise ValueError(f"labels is not an object: {given!r}")
    of = {i: given.get(str(i)) for i in range(1, n + 1)}
    dropped = sum(1 for k, v in given.items() if not (str(k).isdigit() and 1 <= int(k) <= n and v in LABELS))
    dropped += sum(1 for v in of.values() if v is None)
    lists = {k: [i for i, v in of.items() if v in _IN_LIST[k]] for k in LLM_LISTS}
    named = {i for i, d in enumerate(prompt.docs, 1) if d.get("method") in ("cashtag", "exchange")}
    overruled = len(set(lists["not_about"]) & named)
    lists["not_about"] = [i for i in lists["not_about"] if i not in named]
    about = [i for i in range(1, n + 1) if i not in lists["not_about"]]
    quote = _flat(str(obj.get("event_quote") or ""))[:200]
    texts = [_doc_text(d) for d in prompt.docs]
    events = [i for i in lists["event"] if i in about]
    verdict = "none" if not events else "ok" if quote_found(quote, texts) else "failed"

    def share(refs) -> float:
        return round(len([i for i in refs if i in about]) / n, 6) if n else 0.0

    catalyst = str(obj.get("event_type") or "none").strip().lower()
    return {
        "llm_about_share": round(len(about) / n, 6) if n else 0.0,
        "llm_pitch_share": share(lists["pitch"]),
        "llm_warning_share": share(lists["warning"]),
        "llm_event_share": share(events) if verdict == "ok" else 0.0,
        "llm_sentiment": _clamp(obj.get("sentiment"), -2, 2),
        "llm_catalyst": catalyst if catalyst in CATALYSTS else "other",
        "llm_event_quote": quote,
        "llm_summary": _flat(str(obj.get("summary") or ""))[:300],
        "llm_checks": f"quote={verdict} dropped={dropped} overruled={overruled}",
        "llm_lists": json.dumps(lists, separators=(", ", ": ")),
        "n_shown": n,
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
        self.min_interval, self.timeout = min_interval, timeout  # a full-size prompt takes a CPU minutes
        self._last: float | None = None

    def complete(self, system: str, user: str, schema: dict | None = None) -> str:
        if self._last is not None:
            wait = self._last + self.min_interval - self.clock()
            if wait > 0:
                self.sleep(wait)
        fmt = ({"type": "json_schema", "json_schema": {"name": "labels", "strict": True, "schema": schema}} if schema
               else {"type": "json_object"})
        try:
            r = self.post(self.url, timeout=self.timeout, headers={"Content-Type": "application/json"},
                          json={"model": self.model, "temperature": 0, "seed": 0, "max_tokens": 900,
                                "response_format": fmt, "chat_template_kwargs": {"enable_thinking": False},
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
             "created_utc": as_of - 3600 + i, "title": None, "method": "bare",
             "body": f"ABCD comment {i}: short squeeze incoming, low float, get in before the news " + "x" * 400}
            for i in range(MAX_DOCS)]
    snap = {"ticker": "ABCD", "name": "Abcd Inc.", "venue": "listed", "price_at_flag": "3.21", "cik": ""}
    p = build_prompt(snap, docs, as_of)
    t0 = clock()
    answer = llm.complete(p.system, p.user, p.schema)
    lines = [f"{getattr(llm, 'model', '')}: a {len(p.system) + len(p.user)}-character prompt answered in "
             f"{clock() - t0:.0f} s: {answer[:600]!r}"]
    try:
        lines.append(f"parsed: {parse_rating(answer, p)}")
        return True, lines
    except ValueError as exc:
        lines.append(f"could not parse: {exc}")
        return False, lines
