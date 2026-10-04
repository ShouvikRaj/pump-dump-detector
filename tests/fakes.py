"""Test doubles: an in-memory Arctic Shift server and a manual clock."""

from __future__ import annotations

from urllib.parse import urlparse


class FakeClock:
    def __init__(self, start: float = 1_791_000_000.0):
        self.now = start
        self.sleeps: list[float] = []

    def time(self) -> float:
        return self.now

    def sleep(self, seconds: float) -> None:
        self.sleeps.append(seconds)
        self.now += seconds


def post(id_, created, sub="pennystocks", author="alice", title="", selftext="", **extra):
    item = {
        "id": id_,
        "author": author,
        "author_fullname": f"t2_{author}",
        "created_utc": created,
        "retrieved_on": created + 20,
        "subreddit": sub,
        "title": title,
        "selftext": selftext,
        "url": f"https://www.reddit.com/r/{sub}/comments/{id_}/x/",
        "domain": f"self.{sub}",
        "permalink": f"/r/{sub}/comments/{id_}/x/",
        "link_flair_text": None,
        "author_flair_text": None,
        "score": 1,
        "num_comments": 0,
        "upvote_ratio": 1.0,
        "over_18": False,
        "stickied": False,
        "is_self": True,
        "removed_by_category": None,
        "distinguished": None,
        "edited": False,
        "num_crossposts": 0,
    }
    item.update(extra)
    return item


def comment(id_, created, sub="pennystocks", author="bob", body="", link_id="t3_p1", parent_id=None, **extra):
    item = {
        "id": id_,
        "author": author,
        "author_fullname": f"t2_{author}",
        "created_utc": created,
        "retrieved_on": created + 25,
        "subreddit": sub,
        "body": body,
        "link_id": link_id,
        "parent_id": parent_id or link_id,
        "score": 1,
        "permalink": f"/r/{sub}/comments/{link_id[3:]}/x/{id_}/",
        "author_flair_text": None,
        "distinguished": None,
        "edited": False,
        "is_submitter": False,
        "stickied": False,
    }
    item.update(extra)
    return item


class FakeArcticShift:
    """Serves /api/{posts,comments}/search with the real API's filtering rules.

    `after_inclusive` toggles whether `after` keeps items created exactly at
    that second (the live API's behaviour is not documented).
    `failures` is a list of (status, headers) returned before normal answers.
    `auto_size` is how many items limit=auto returns.
    """

    def __init__(self, posts=(), comments=(), after_inclusive=False, auto_size=250, failures=(), reject_fields=False):
        self.items = {"posts": list(posts), "comments": list(comments)}
        self.after_inclusive = after_inclusive
        self.auto_size = auto_size
        self.failures = list(failures)
        self.reject_fields = reject_fields
        self.calls: list[tuple[str, dict]] = []

    def get(self, url: str, params: dict, timeout: float = 30):
        self.calls.append((url, dict(params)))
        if self.failures:
            status, headers = self.failures.pop(0)
            return status, headers, {"error": "fake failure"}
        if self.reject_fields and "fields" in params:
            return 422, {}, {"error": "Invalid field"}
        path = urlparse(url).path
        kind = "posts" if path == "/api/posts/search" else "comments" if path == "/api/comments/search" else None
        if kind is None:
            return 404, {}, {"error": "not found"}
        rows = [it for it in self.items[kind] if it["subreddit"].lower() == str(params["subreddit"]).lower()]
        if "after" in params:
            a = int(params["after"])
            rows = [it for it in rows if (it["created_utc"] >= a if self.after_inclusive else it["created_utc"] > a)]
        if "before" in params:
            b = int(params["before"])
            rows = [it for it in rows if it["created_utc"] < b]
        rows.sort(key=lambda it: it["created_utc"], reverse=params.get("sort") == "desc")
        limit = params.get("limit", 25)
        n = self.auto_size if limit == "auto" else int(limit)
        rows = rows[:n]
        if "fields" in params:
            keep = params["fields"].split(",")
            rows = [{k: it[k] for k in keep if k in it} for it in rows]
        return 200, {"X-RateLimit-Remaining": "100"}, {"data": rows}
