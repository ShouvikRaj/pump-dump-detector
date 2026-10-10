"""Reachability probe for Reddit data sources (run on a GitHub runner; prints only, writes nothing).

For when Arctic Shift is down: does Arctic Shift answer, is PullPush's archive
current, and do Reddit's public RSS feeds answer from GitHub's runners, how far
back one feed page reaches and whether ?after= paging works.
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


def get(url):
    t = time.time()
    try:
        r = s.get(url, timeout=60)
        return r.status_code, r.headers, r.content, time.time() - t
    except requests.RequestException as e:
        return 0, {}, str(e).encode(), time.time() - t


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


def probe(name, url, kind):
    code, headers, body, dt = get(url)
    limits = {k: v for k, v in headers.items() if k.lower().startswith(("x-ratelimit", "retry-after"))}
    line = f"{name:34s} {code} {len(body):>8d}B {dt:5.1f}s"
    items = []
    if code == 200 and kind != "raw":
        try:
            items = json_times(body) if kind == "json" else feed_times(body)
        except Exception as e:  # noqa: BLE001 - report whatever the body was
            line += f" unparsable ({e})"
    if items:
        times = [t for _, t in items]
        line += f" {len(items)} items, newest {ago(max(times))}, oldest {ago(min(times))}"
    elif code != 200 or kind == "raw":
        line += f" {body[:120]!r}"
    print(line + (f" {limits}" if limits else ""), flush=True)
    return items


print("== Arctic Shift")
probe("front page", f"{AS}/", "raw")
probe("posts r/pennystocks newest", f"{AS}/api/posts/search?subreddit=pennystocks&limit=5&sort=desc", "json")
probe("comments r/wsb newest", f"{AS}/api/comments/search?subreddit=wallstreetbets&limit=5&sort=desc", "json")

print("== PullPush")
probe("submissions r/pennystocks newest", f"{PP}/submission/?subreddit=pennystocks&size=5&sort=desc", "json")
probe("comments r/wsb newest", f"{PP}/comment/?subreddit=wallstreetbets&size=5&sort=desc", "json")

print("== Reddit")
probe("json r/pennystocks/new", "https://www.reddit.com/r/pennystocks/new.json?limit=5", "json")
for sub in ("pennystocks", "smallstreetbets", "wallstreetbets"):
    for path, label in (("new", "posts"), ("comments", "comments")):
        time.sleep(3)
        items = probe(f"rss r/{sub} {label}", f"https://www.reddit.com/r/{sub}/{path}/.rss?limit=100", "feed")
        if sub == "wallstreetbets" and label == "comments" and items:
            time.sleep(3)
            probe("rss r/wsb comments page 2", f"https://www.reddit.com/r/{sub}/comments/.rss?limit=100&after={items[-1][0]}", "feed")
time.sleep(3)
probe("rss old.reddit r/pennystocks", "https://old.reddit.com/r/pennystocks/new/.rss?limit=100", "feed")
