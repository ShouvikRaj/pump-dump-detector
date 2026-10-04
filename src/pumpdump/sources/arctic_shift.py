"""Reddit posts and comments from the Arctic Shift archive.

Reddit closed self-serve API keys in November 2025 and unauthenticated .json
in May 2026, so PRAW is not usable for a hobby project. Arctic Shift
(https://github.com/ArthurHeitmann/arctic_shift) archives Reddit in near real
time (items show up ~20-30 s after posting) and needs no key.

Caveat for later stages: Arctic Shift stores score=1 / num_comments=0 at
ingest and only refreshes them ~36 h later, so engagement numbers are only
usable from a snapshot collected before the decision point.
"""

from __future__ import annotations

import time
from dataclasses import dataclass, field
from typing import Any, Callable

import requests

BASE_URL = "https://arctic-shift.photon-reddit.com"
USER_AGENT = "pump-dump-detector/0.1 (research; https://github.com/ShouvikRaj/pump-dump-detector)"
FULL_PAGE = 100  # a page shorter than this means we've caught up (limit=100 or limit=auto)

POST_FIELDS = (
    "id,author,author_fullname,created_utc,retrieved_on,subreddit,title,selftext,url,domain,permalink,"
    "link_flair_text,author_flair_text,score,num_comments,upvote_ratio,over_18,stickied,is_self,"
    "removed_by_category,distinguished,edited,num_crossposts"
)
COMMENT_FIELDS = (
    "id,author,author_fullname,created_utc,retrieved_on,subreddit,body,link_id,parent_id,score,permalink,"
    "author_flair_text,distinguished,edited,is_submitter,stickied"
)
FIELDS = {"posts": POST_FIELDS, "comments": COMMENT_FIELDS}

Getter = Callable[..., tuple[int, dict, Any]]


class ArcticShiftError(RuntimeError):
    pass


def requests_getter(user_agent: str = USER_AGENT) -> Getter:
    session = requests.Session()
    session.headers["User-Agent"] = user_agent

    def get(url: str, params: dict, timeout: float = 30) -> tuple[int, dict, Any]:
        try:
            resp = session.get(url, params=params, timeout=timeout)
        except requests.RequestException as exc:
            return 0, {}, {"error": f"{type(exc).__name__}: {exc}"}
        try:
            body = resp.json()
        except ValueError:
            body = {"error": resp.text[:500]}
        return resp.status_code, dict(resp.headers), body

    return get


class ArcticShift:
    def __init__(
        self,
        get: Getter | None = None,
        sleep: Callable[[float], None] | None = None,
        clock: Callable[[], float] | None = None,
        min_interval: float = 1.0,
        max_retries: int = 5,
        base_url: str = BASE_URL,
    ) -> None:
        self.get = get or requests_getter()
        self.sleep = sleep or (lambda s: time.sleep(s))
        self.clock = clock or (lambda: time.time())
        self.min_interval = min_interval
        self.max_retries = max_retries
        self.base_url = base_url
        self.use_fields = True
        self._last_request: float | None = None
        self.requests_made = 0

    def _throttle(self) -> None:
        if self._last_request is not None:
            wait = self._last_request + self.min_interval - self.clock()
            if wait > 0:
                self.sleep(wait)

    def search(
        self,
        kind: str,
        subreddit: str,
        after: int,
        before: int | None = None,
        limit: int | str = 100,
        sort: str = "asc",
    ) -> list[dict]:
        url = f"{self.base_url}/api/{kind}/search"
        status, body = 0, None
        for attempt in range(self.max_retries + 1):
            params: dict[str, Any] = {"subreddit": subreddit, "after": int(after), "sort": sort, "limit": limit}
            if before is not None:
                params["before"] = int(before)
            if self.use_fields:
                params["fields"] = FIELDS[kind]
            self._throttle()
            self._last_request = self.clock()
            self.requests_made += 1
            status, headers, body = self.get(url, params, timeout=60)
            if status == 200:
                data = body.get("data") if isinstance(body, dict) else None
                if not isinstance(data, list):
                    raise ArcticShiftError(f"unexpected response shape: {str(body)[:200]}")
                return data
            if status == 422 and self.use_fields:
                self.use_fields = False  # a field name was rejected; ask for whole records
                continue
            if status == 422 and limit == "auto":
                limit = FULL_PAGE  # heavy query timed out; ask for a smaller page
            elif status not in (0, 422, 429) and status < 500:
                raise ArcticShiftError(f"HTTP {status} for {kind} r/{subreddit}: {str(body)[:200]}")
            if attempt == self.max_retries:
                break
            self.sleep(_retry_wait(status, headers, attempt))
        raise ArcticShiftError(f"HTTP {status} for {kind} r/{subreddit} after {self.max_retries + 1} tries: {str(body)[:200]}")


def _retry_wait(status: int, headers: dict, attempt: int) -> float:
    if status == 429:
        for key in ("X-RateLimit-Reset", "x-ratelimit-reset"):
            if key in headers:
                try:
                    return max(1.0, min(float(headers[key]), 300.0))
                except ValueError:
                    pass
    return float(min(2 ** (attempt + 1), 60))


@dataclass
class FetchResult:
    items: list[dict] = field(default_factory=list)
    newest_created: int | None = None
    pages: int = 0
    complete: bool = False
    error: str | None = None
    tie_skips: int = 0


def fetch_since(
    client: ArcticShift,
    kind: str,
    subreddit: str,
    after: int,
    before: int | None = None,
    limit: int | str = 100,
    max_pages: int = 1000,
    deadline: float | None = None,
) -> FetchResult:
    """Page forward through items created after `after`, oldest first.

    Each item gets `_collected_at`: the time its page arrived. Items come back
    in creation order, so everything up to `newest_created` has been seen even
    when paging stops early (cap, deadline or error).
    """
    res = FetchResult()
    seen: set[str] = set()
    cursor = int(after)
    while res.pages < max_pages and (deadline is None or client.clock() < deadline):
        try:
            page = client.search(kind, subreddit, after=cursor, before=before, limit=limit)
        except ArcticShiftError as exc:
            res.error = str(exc)
            return res
        received = client.clock()
        res.pages += 1
        new = [it for it in page if it["id"] not in seen]
        for it in new:
            seen.add(it["id"])
            it["_collected_at"] = received
            res.items.append(it)
            created = int(it["created_utc"])
            if res.newest_created is None or created > res.newest_created:
                res.newest_created = created
        if len(page) < FULL_PAGE:
            res.complete = True
            return res
        last = max(int(it["created_utc"]) for it in page)
        nxt = last - 1  # re-read the boundary second so ties split across pages aren't lost
        if not new or nxt <= cursor:
            nxt = max(cursor + 1, last)  # a whole page inside one second: skip ahead
            res.tie_skips += 1
        cursor = nxt
    return res


def to_record(kind: str, item: dict, run_id: str) -> dict:
    is_post = kind == "posts"
    return {
        "id": ("t3_" if is_post else "t1_") + item["id"],
        "kind": "post" if is_post else "comment",
        "subreddit": (item.get("subreddit") or "").lower(),
        "author": item.get("author"),
        "author_fullname": item.get("author_fullname"),
        "created_utc": int(item["created_utc"]),
        "collected_at": item["_collected_at"],
        "source": "arctic_shift",
        "source_retrieved_at": item.get("retrieved_on"),
        "title": item.get("title") if is_post else None,
        "body": item.get("selftext") if is_post else item.get("body"),
        "link_id": None if is_post else item.get("link_id"),
        "parent_id": None if is_post else item.get("parent_id"),
        "url": item.get("url"),
        "permalink": item.get("permalink"),
        "flair": item.get("link_flair_text"),
        "author_flair": item.get("author_flair_text"),
        "score": item.get("score"),
        "num_comments": item.get("num_comments"),
        "upvote_ratio": item.get("upvote_ratio"),
        "removed_by_category": item.get("removed_by_category"),
        "distinguished": item.get("distinguished"),
        "stickied": item.get("stickied"),
        "edited": item.get("edited"),
        "run_id": run_id,
    }
