"""Posts about one ticker from Twitter-like sources, newest first, back to a start time.

- StockTwits symbol streams: free, no key; 30 messages a page, paged back with `max`.
- Bluesky post search on api.bsky.app: free, no key (public.api.bsky.app refuses search, checked
  2026-10-07); posts are kept only if they contain the cashtag.
- X API v2 recent search: paid per post read, so it runs only when an X_BEARER_TOKEN is set.

There is no free, account-free way to read X any more (checked 2026-10-07: Nitter and XCancel shut down
in September 2026, x.com sits behind a bot wall, the API has had no free tier since February 2026).
See docs/social.md.

Every fetcher returns (posts, info): posts normalised to POST_FIELDS, info = {"requests", "truncated",
"error"}. `truncated` means the page limit was hit before reaching `since`, so counts are lower bounds.
"""

from __future__ import annotations

import json
import re
from datetime import datetime, timezone

from .web import Web, short_text

POST_FIELDS = ["source", "id", "created_at", "author_id", "author", "author_followers", "author_joined",
               "author_posts", "sentiment", "likes", "text", "symbols", "url"]

STOCKTWITS_URL = "https://api.stocktwits.com/api/2/streams/symbol/{symbol}.json"
BLUESKY_URL = "https://api.bsky.app/xrpc/app.bsky.feed.searchPosts"
X_URL = "https://api.x.com/2/tweets/search/recent"
UA = {"User-Agent": "Mozilla/5.0 (compatible; pump-dump-detector/0.1; research)", "Accept": "application/json"}


def _ts(text: str | None) -> float | None:
    if not text:
        return None
    try:
        dt = datetime.fromisoformat(text.replace("Z", "+00:00"))
    except ValueError:
        return None
    return (dt if dt.tzinfo else dt.replace(tzinfo=timezone.utc)).timestamp()


def _iso(ts: float) -> str:
    return datetime.fromtimestamp(ts, timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")


def _info(requests: int = 0, truncated: bool = False, error: str = "") -> dict:
    return {"requests": requests, "truncated": truncated, "error": error}


def _json(status: int, text: str) -> dict:
    if status != 200:
        raise ValueError(f"HTTP {status}: {short_text(text)}")
    return json.loads(text)


# StockTwits ------------------------------------------------------------------------------------------------

def parse_stocktwits(obj: dict) -> list[dict]:
    out = []
    for m in obj.get("messages") or []:
        u = m.get("user") or {}
        sentiment = ((m.get("entities") or {}).get("sentiment") or {}).get("basic") or ""
        out.append({
            "source": "stocktwits",
            "id": str(m.get("id")),
            "created_at": _ts(m.get("created_at")),
            "author_id": str(u.get("id", "")),
            "author": u.get("username", ""),
            "author_followers": u.get("followers"),
            "author_joined": _ts(u.get("join_date")),
            "author_posts": u.get("ideas"),
            "sentiment": sentiment.lower(),
            "likes": (m.get("likes") or {}).get("total", 0),
            "text": m.get("body", ""),
            "symbols": [s.get("symbol", "") for s in m.get("symbols") or []],
            "url": f"https://stocktwits.com/{u.get('username', '')}/message/{m.get('id')}",
        })
    return out


def fetch_stocktwits(web: Web, ticker: str, since: float, max_pages: int) -> tuple[list[dict], dict]:
    posts: list[dict] = []
    params: dict = {}
    for page in range(1, max_pages + 1):
        status, text = web.fetch(STOCKTWITS_URL.format(symbol=ticker), params=params or None, headers=UA)
        if status == 404:
            return posts, _info(page, error="not on StockTwits")
        try:
            obj = _json(status, text)
        except ValueError as exc:
            return posts, _info(page, error=f"stocktwits: {exc}")
        batch = parse_stocktwits(obj)
        posts += [p for p in batch if p["created_at"] is not None and p["created_at"] >= since]
        cursor = obj.get("cursor") or {}
        oldest = min((p["created_at"] for p in batch if p["created_at"]), default=None)
        if not batch or not cursor.get("more") or oldest is None or oldest < since:
            return posts, _info(page)
        params = {"max": cursor["max"]}
    return posts, _info(max_pages, truncated=True)


# Bluesky ---------------------------------------------------------------------------------------------------

def parse_bluesky(obj: dict, ticker: str) -> list[dict]:
    tag = re.compile(rf"\${re.escape(ticker)}\b", re.IGNORECASE)
    out = []
    for p in obj.get("posts") or []:
        rec = p.get("record") or {}
        text = rec.get("text", "")
        if not tag.search(text):
            continue
        a = p.get("author") or {}
        rkey = str(p.get("uri", "")).rsplit("/", 1)[-1]
        out.append({
            "source": "bluesky",
            "id": p.get("uri", ""),
            "created_at": _ts(rec.get("createdAt")) or _ts(p.get("indexedAt")),
            "author_id": a.get("did", ""),
            "author": a.get("handle", ""),
            "author_followers": None,  # search results carry no follower counts
            "author_joined": _ts(a.get("createdAt")),
            "author_posts": None,
            "sentiment": "",
            "likes": p.get("likeCount", 0),
            "text": text,
            "symbols": sorted({m.upper() for m in re.findall(r"\$([A-Za-z]{1,5})\b", text)}),
            "url": f"https://bsky.app/profile/{a.get('handle', '')}/post/{rkey}",
        })
    return out


def fetch_bluesky(web: Web, ticker: str, since: float, max_pages: int) -> tuple[list[dict], dict]:
    posts: list[dict] = []
    params = {"q": f"${ticker}", "sort": "latest", "limit": 100, "since": _iso(since)}
    for page in range(1, max_pages + 1):
        try:
            obj = _json(*web.fetch(BLUESKY_URL, params=params, headers=UA))
        except ValueError as exc:
            return posts, _info(page, error=f"bluesky: {exc}")
        posts += [p for p in parse_bluesky(obj, ticker) if p["created_at"] is not None and p["created_at"] >= since]
        if not obj.get("cursor") or not obj.get("posts"):
            return posts, _info(page)
        params = {**params, "cursor": obj["cursor"]}
    return posts, _info(max_pages, truncated=True)


# X (paid) --------------------------------------------------------------------------------------------------

def parse_x(obj: dict) -> list[dict]:
    users = {u["id"]: u for u in (obj.get("includes") or {}).get("users") or []}
    out = []
    for t in obj.get("data") or []:
        u = users.get(t.get("author_id"), {})
        um = u.get("public_metrics") or {}
        out.append({
            "source": "x",
            "id": str(t.get("id")),
            "created_at": _ts(t.get("created_at")),
            "author_id": str(t.get("author_id", "")),
            "author": u.get("username", ""),
            "author_followers": um.get("followers_count"),
            "author_joined": _ts(u.get("created_at")),
            "author_posts": um.get("tweet_count"),
            "sentiment": "",
            "likes": (t.get("public_metrics") or {}).get("like_count", 0),
            "text": t.get("text", ""),
            "symbols": [c.get("tag", "").upper() for c in (t.get("entities") or {}).get("cashtags") or []],
            "url": f"https://x.com/{u.get('username', 'i')}/status/{t.get('id')}",
        })
    return out


def fetch_x(web: Web, ticker: str, since: float, max_posts: int, token: str) -> tuple[list[dict], dict]:
    """Recent search (last 7 days) for the cashtag, original posts only; X bills each post returned."""
    posts: list[dict] = []
    params = {
        "query": f"${ticker} -is:retweet",
        "start_time": _iso(max(since, 0)),
        "max_results": 100,
        "tweet.fields": "created_at,author_id,public_metrics,entities",
        "expansions": "author_id",
        "user.fields": "created_at,public_metrics,username",
    }
    page = 0
    while max_posts - len(posts) >= 10:  # X's smallest page is 10
        page += 1
        params["max_results"] = min(100, max_posts - len(posts))
        try:
            obj = _json(*web.fetch(X_URL, params=params, headers={**UA, "Authorization": f"Bearer {token}"}))
        except ValueError as exc:
            return posts, _info(page, error=f"x: {exc}")
        posts += parse_x(obj)
        nxt = (obj.get("meta") or {}).get("next_token")
        if not nxt:
            return posts, _info(page)
        params["next_token"] = nxt
    return posts, _info(page, truncated=True)
