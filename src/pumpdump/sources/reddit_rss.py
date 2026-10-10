"""Reddit posts and comments from Reddit's public RSS feeds: the collector's fallback while Arctic Shift is down.

www.reddit.com/r/SUB/new/.rss (posts) and /r/SUB/comments/.rss (comments) need no key and answer from
GitHub's runners (checked 2026-10-10, when Arctic Shift had been down a day: about 100 requests per 10
minutes, announced in x-ratelimit-* headers; old.reddit.com answers with a login page and .json is
blocked). A page holds the newest 100 items and ?after=<fullname> pages back until Reddit's listing stops
at about 1000 items: days of r/pennystocks, but only about two hours of r/wallstreetbets comments.

Feeds have no score, num_comments, author_fullname or parent_id, don't list removed items, and give the
body as rendered HTML, which is turned back into text here.
"""

from __future__ import annotations

import html
import re
import time
import xml.etree.ElementTree as ET
from dataclasses import dataclass, field
from datetime import datetime
from typing import Any, Callable

import requests

from .arctic_shift import USER_AGENT

FEED_URL = "https://www.reddit.com/r/{sub}/{path}/.rss"
PATHS = {"posts": "new", "comments": "comments"}
PREFIX = {"posts": "t3_", "comments": "t1_"}
PAGE = 100
MAX_PAGES = 10  # Reddit's listings stop at about 1000 items
ATOM = "{http://www.w3.org/2005/Atom}"

_MD_RE = re.compile(r"<!-- SC_OFF -->(.*?)<!-- SC_ON -->", re.S)  # the post or comment text itself
_BREAK_RE = re.compile(r"<br\s*/?>|</?(?:p|div|li|ul|ol|blockquote|pre|h[1-6]|table|thead|tbody|tr|td|th|hr)\b[^>]*>", re.I)
_TAG_RE = re.compile(r"<[^>]+>")
_LINK_RE = re.compile(r'<a href="([^"]+)">\[link\]</a>')
_POST_ID_RE = re.compile(r"/comments/([a-z0-9]+)/")

Getter = Callable[..., tuple[int, dict, Any]]


def requests_getter(user_agent: str = USER_AGENT) -> Getter:
    session = requests.Session()
    session.headers["User-Agent"] = user_agent

    def get(url: str, params: dict, timeout: float = 30) -> tuple[int, dict, Any]:
        try:
            resp = session.get(url, params=params, timeout=timeout)
        except requests.RequestException as exc:
            return 0, {}, f"{type(exc).__name__}: {exc}".encode()
        return resp.status_code, {k.lower(): v for k, v in resp.headers.items()}, resp.content

    return get


def _text(fragment: str) -> str:
    text = html.unescape(_TAG_RE.sub("", _BREAK_RE.sub("\n", fragment)))
    return "\n".join(line.strip() for line in text.splitlines() if line.strip())


def parse_feed(xml: bytes | str, kind: str) -> list[dict]:
    """Feed entries as Arctic-Shift-shaped items (id without prefix, created_utc, author, subreddit, ...)."""
    items = []
    for e in ET.fromstring(xml).iter(f"{ATOM}entry"):
        fullname = e.findtext(f"{ATOM}id") or ""
        stamp = e.findtext(f"{ATOM}published") or e.findtext(f"{ATOM}updated")  # comments only have <updated>
        if not stamp or "_" not in fullname:
            continue
        content = e.findtext(f"{ATOM}content") or ""
        md = _MD_RE.search(content)
        category = e.find(f"{ATOM}category")
        link = e.find(f"{ATOM}link")
        item = {
            "id": fullname.split("_", 1)[1],
            "created_utc": int(datetime.fromisoformat(stamp).timestamp()),
            "author": (e.findtext(f"{ATOM}author/{ATOM}name") or "").removeprefix("/u/") or None,
            "subreddit": category.get("term", "") if category is not None else "",
        }
        text = _text(md.group(1)) if md else ""
        href = link.get("href", "") if link is not None else ""
        if kind == "posts":
            target = _LINK_RE.search(content)
            item.update(title=e.findtext(f"{ATOM}title"), selftext=text, url=html.unescape(target.group(1)) if target else href)
        else:
            post_id = _POST_ID_RE.search(href)
            item.update(body=text, link_id=f"t3_{post_id.group(1)}" if post_id else None)
        items.append(item)
    return items


@dataclass
class FeedResult:
    items: list[dict] = field(default_factory=list)  # newest first, each stamped with `_collected_at`
    pages: int = 0
    complete: bool = False  # nothing created after `since` can be missing
    error: str | None = None

    @property
    def newest_created(self) -> int | None:
        return max((it["created_utc"] for it in self.items), default=None)

    @property
    def oldest_created(self) -> int | None:
        return min((it["created_utc"] for it in self.items), default=None)


class RedditRSS:
    def __init__(
        self,
        get: Getter | None = None,
        sleep: Callable[[float], None] | None = None,
        clock: Callable[[], float] | None = None,
        min_interval: float = 1.0,
    ) -> None:
        self.get = get or requests_getter()
        self.sleep = sleep or (lambda s: time.sleep(s))
        self.clock = clock or (lambda: time.time())
        self.min_interval = min_interval
        self._last_request: float | None = None

    def fetch_back_to(
        self, kind: str, subreddit: str, since: int, deadline: float | None = None, max_pages: int = MAX_PAGES
    ) -> FeedResult:
        """Read the feed newest first until it reaches an item created at or before `since`.

        `complete` means nothing created after `since` was missed: the pages reached back that far.
        Otherwise the stretch between `since` and the oldest item read is a hole only Arctic Shift can
        fill. An empty page proves nothing, since Reddit's listing cap ends a feed the same way.
        """
        res = FeedResult()
        seen: set[str] = set()
        after = None
        while res.pages < max_pages:
            wait = 0.0 if self._last_request is None else self._last_request + self.min_interval - self.clock()
            if deadline is not None and self.clock() + max(wait, 0.0) >= deadline:
                break
            if wait > 0:
                self.sleep(wait)
            self._last_request = self.clock()
            params = {"limit": PAGE, **({"after": after} if after else {})}
            status, headers, body = self.get(FEED_URL.format(sub=subreddit, path=PATHS[kind]), params, timeout=30)
            if status != 200:
                res.error = f"HTTP {status} for Reddit RSS {kind} r/{subreddit}"
                return res
            try:
                page = parse_feed(body, kind)
            except (ET.ParseError, ValueError) as exc:  # not XML, or a timestamp in a new format
                res.error = f"unreadable Reddit RSS {kind} r/{subreddit}: {exc}"
                return res
            received = self.clock()
            res.pages += 1
            if not page:
                return res
            for it in page:
                if it["id"] not in seen:
                    seen.add(it["id"])
                    it["_collected_at"] = received
                    it["subreddit"] = it["subreddit"] or subreddit
                    res.items.append(it)
            if min(it["created_utc"] for it in page) <= since:
                res.complete = True
                return res
            try:
                remaining = float(headers.get("x-ratelimit-remaining", 1))
            except (TypeError, ValueError):
                remaining = 1.0
            if remaining < 1:
                res.error = f"Reddit RSS rate limit used up (resets in {headers.get('x-ratelimit-reset', '?')} s)"
                return res
            after = PREFIX[kind] + page[-1]["id"]
        return res
