"""Test doubles: in-memory Arctic Shift and Reddit RSS servers and a manual clock."""

from __future__ import annotations

from datetime import datetime, timezone
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


# `fields` values the live API accepts (api/README.md, checked 2026-10-04)
_SHARED_FIELDS = {"author", "author_fullname", "author_flair_text", "created_utc", "distinguished", "id",
                  "retrieved_on", "subreddit", "subreddit_id", "score"}
DOC_FIELDS = {
    "posts": _SHARED_FIELDS | {"crosspost_parent", "link_flair_text", "num_comments", "over_18", "post_hint",
                               "selftext", "spoiler", "title", "url"},
    "comments": _SHARED_FIELDS | {"body", "link_id", "parent_id"},
}


class FakeArcticShift:
    """Serves /api/{posts,comments}/search with the real API's filtering rules.

    `after_inclusive` toggles whether `after` keeps items created exactly at
    that second (the live API's behaviour is not documented).
    `failures` is a list of (status, headers) returned before normal answers.
    `auto_size` is how many items limit=auto returns.
    `valid_fields` maps kind -> accepted `fields` names; like the live API, the
    first unknown name gets a 400 "'name' is not a valid field".
    """

    def __init__(self, posts=(), comments=(), after_inclusive=False, auto_size=250, failures=(), valid_fields=None):
        self.items = {"posts": list(posts), "comments": list(comments)}
        self.after_inclusive = after_inclusive
        self.auto_size = auto_size
        self.failures = list(failures)
        self.valid_fields = valid_fields or DOC_FIELDS
        self.calls: list[tuple[str, dict]] = []

    def get(self, url: str, params: dict, timeout: float = 30):
        self.calls.append((url, dict(params)))
        if self.failures:
            status, headers = self.failures.pop(0)
            return status, headers, {"error": "fake failure"}
        path = urlparse(url).path
        kind = "posts" if path == "/api/posts/search" else "comments" if path == "/api/comments/search" else None
        if kind is None:
            return 404, {}, {"error": "not found"}
        for name in params.get("fields", "").split(",") if "fields" in params else ():
            if name not in self.valid_fields[kind]:
                return 400, {}, {"data": None, "error": f"'{name}' is not a valid field"}
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


def atom_feed(kind: str, rows: list[dict]) -> bytes:
    """Reddit's Atom feed for `rows` (fakes.post/comment dicts), shaped like the live one (2026-10-10)."""
    from html import escape

    entries = []
    for it in rows:
        sub, author = it["subreddit"], it["author"]
        stamp = datetime.fromtimestamp(it["created_utc"], timezone.utc).isoformat()
        if kind == "posts":
            link = f"https://www.reddit.com/r/{sub}/comments/{it['id']}/x/"
            md = f'<!-- SC_OFF --><div class="md"><p>{escape(it["selftext"])}</p></div><!-- SC_ON -->' if it["selftext"] else ""
            html_ = (f'{md} &#32; submitted by &#32; <a href="https://www.reddit.com/user/{author}"> /u/{author} </a> <br/>'
                     f' <span><a href="{escape(it["url"])}">[link]</a></span> &#32; <span><a href="{link}">[comments]</a></span>')
            extra = f"<published>{stamp}</published><title>{escape(it['title'])}</title>"
            fullname = f"t3_{it['id']}"
        else:
            link = f"https://www.reddit.com/r/{sub}/comments/{it['link_id'][3:]}/x/{it['id']}/"
            html_ = f'<!-- SC_OFF --><div class="md"><p>{escape(it["body"])}</p></div><!-- SC_ON -->'
            extra = f"<title>/u/{author} on x</title>"
            fullname = f"t1_{it['id']}"
        entries.append(
            f'<entry><author><name>/u/{author}</name><uri>https://www.reddit.com/user/{author}</uri></author>'
            f'<category term="{sub}" label="r/{sub}"/><content type="html">{escape(html_)}</content>'
            f'<id>{fullname}</id><link href="{link}"/><updated>{stamp}</updated>{extra}</entry>'
        )
    return ('<?xml version="1.0" encoding="UTF-8"?><feed xmlns="http://www.w3.org/2005/Atom">'
            '<category term="x" label="r/x"/><title>feed</title>' + "".join(entries) + "</feed>").encode()


class FakeRedditRSS:
    """Serves www.reddit.com/r/SUB/{new,comments}/.rss: newest first, `limit` per page, ?after=<fullname>
    pages back, and like Reddit's listings the feed stops after `cap` items. `failures` is a list of
    (status, headers) returned before normal answers; `status` other than 200 fails every request."""

    def __init__(self, posts=(), comments=(), cap=1000, headers=None, status=200, failures=()):
        self.items = {"posts": list(posts), "comments": list(comments)}
        self.cap = cap
        self.headers = headers if headers is not None else {"x-ratelimit-remaining": "99.0", "x-ratelimit-reset": "500"}
        self.status = status
        self.failures = list(failures)
        self.calls: list[tuple[str, dict]] = []

    def get(self, url: str, params: dict, timeout: float = 30):
        self.calls.append((url, dict(params)))
        if self.failures:
            status, headers = self.failures.pop(0)
            return status, headers, b"Too Many Requests"
        if self.status != 200:
            return self.status, {}, b""
        sub, path = urlparse(url).path.split("/")[2:4]
        kind = "posts" if path == "new" else "comments"
        rows = [it for it in self.items[kind] if it["subreddit"].lower() == sub.lower()]
        rows = sorted(rows, key=lambda it: it["created_utc"], reverse=True)[: self.cap]
        if params.get("after"):
            names = [("t3_" if kind == "posts" else "t1_") + it["id"] for it in rows]
            rows = rows[names.index(params["after"]) + 1 :] if params["after"] in names else []
        return 200, dict(self.headers), atom_feed(kind, rows[: int(params.get("limit", 25))])
