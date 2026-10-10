"""Reachability probe for Reddit data sources (run on a GitHub runner; prints only, writes nothing).

For when Arctic Shift is down: does Arctic Shift answer, is PullPush reachable,
and do Reddit's public RSS feeds answer from GitHub's runners, how far back a
feed reaches with ?after= paging, and what rate limit Reddit announces.
"""

import json
import time
import xml.etree.ElementTree as ET
from datetime import datetime

import requests

UA = "pump-dump-detector/0.1 (research; https://github.com/ShouvikRaj/pump-dump-detector)"
ATOM = "{http://www.w3.org/2005/Atom}"
AS = "https://arctic-shift.photon-reddit.com"
PP = "https://api.pullpush.io/reddit/search"
s = requests.Session()
s.headers["User-Agent"] = UA
wait_until = {}  # host -> time its rate-limit window resets


def get(url):
    host = url.split("/")[2]
    if time.time() < wait_until.get(host, 0):
        time.sleep(wait_until[host] - time.time())
    t = time.time()
    try:
        r = s.get(url, timeout=60)
    except requests.RequestException as e:
        return 0, {}, str(e).encode(), time.time() - t
    try:
        if float(r.headers.get("x-ratelimit-remaining", 1)) < 1:
            wait_until[host] = time.time() + float(r.headers.get("x-ratelimit-reset", 60)) + 1
    except ValueError:
        pass
    return r.status_code, r.headers, r.content, time.time() - t


def ago(ts):
    return f"{(time.time() - ts) / 3600:.1f}h ago"


def json_times(body):
    d = json.loads(body)
    items = d.get("data") if isinstance(d, dict) else None
    if isinstance(items, dict):  # reddit listing
        items = [c.get("data", {}) for c in items.get("children", [])]
    return [(it.get("name") or it.get("id"), float(it["created_utc"])) for it in items or [] if "created_utc" in it]


def feed_times(body):
    out = []
    for e in ET.fromstring(body).iter(f"{ATOM}entry"):
        ts = e.findtext(f"{ATOM}published") or e.findtext(f"{ATOM}updated")
        out.append((e.findtext(f"{ATOM}id"), datetime.fromisoformat(ts.replace("Z", "+00:00")).timestamp()))
    return out


def probe(name, url, kind, show=0):
    code, headers, body, dt = get(url)
    limits = {k: v for k, v in headers.items() if k.lower().startswith(("x-ratelimit", "retry-after"))}
    line = f"{name:34s} {code} {len(body):>8d}B {dt:5.1f}s {headers.get('content-type', '')[:30]}"
    items = []
    if code == 200 and kind != "raw":
        try:
            items = json_times(body) if kind == "json" else feed_times(body)
        except Exception as e:  # noqa: BLE001 - report whatever the body was
            line += f" unparsable ({e}): {body[:300]!r}"
    if items:
        times = [t for _, t in items]
        line += f" {len(items)} items, newest {ago(max(times))}, oldest {ago(min(times))}"
    elif code != 200 or kind == "raw":
        line += f" {body[:120]!r}"
    print(line + (f" {limits}" if limits else ""), flush=True)
    if show and code == 200:
        print("   sample:", body[body.find(b"<entry"):][:show].decode(errors="replace"), flush=True)
    return items


def pages(name, base, n):
    """Page back through a feed with ?after=, reporting each page's span and whether pages overlap."""
    after, seen = None, set()
    for i in range(n):
        items = probe(f"{name} p{i + 1}", base + (f"&after={after}" if after else ""), "feed")
        if not items:
            return
        ids = [x for x, _ in items]
        if seen & set(ids):
            print(f"   page {i + 1} repeats {len(seen & set(ids))} ids from earlier pages")
        seen |= set(ids)
        after = ids[-1]


print("== Arctic Shift")
probe("front page", f"{AS}/", "raw")
probe("comments r/wsb newest", f"{AS}/api/comments/search?subreddit=wallstreetbets&limit=5&sort=desc", "json")

print("== PullPush")
probe("comments r/wsb newest", f"{PP}/comment/?subreddit=wallstreetbets&size=5&sort=desc", "json")

print("== Reddit RSS")
probe("old.reddit r/pennystocks posts", "https://old.reddit.com/r/pennystocks/new/.rss?limit=100", "feed", show=300)
probe("www r/pennystocks posts", "https://www.reddit.com/r/pennystocks/new/.rss?limit=100", "feed", show=1500)
pages("www r/pennystocks comments", "https://www.reddit.com/r/pennystocks/comments/.rss?limit=100", 3)
probe("www r/smallstreetbets comments", "https://www.reddit.com/r/smallstreetbets/comments/.rss?limit=100", "feed", show=1500)
pages("www r/wsb comments", "https://www.reddit.com/r/wallstreetbets/comments/.rss?limit=100", 4)
