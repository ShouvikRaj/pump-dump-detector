"""The hourly crypto run: Telegram previews, the market-wide scan, bars and outcomes (docs/crypto.md).

Everything lives under crypto/ in the datastore (the data branch):

    crypto/state.json                       when the live track started / stopped
    crypto/telegram/channels.csv            channels read, how found, last post seen
    crypto/telegram/posts/YYYY/MM/DD/*.jsonl.gz   every post read (one file per run), with its tg-v1 class
    crypto/events.csv                       append-only: one row per event (history, telegram, scan)
    crypto/bars/<source>/<event_id>.json.gz bars fetched for the event, and when
    crypto/outcomes.csv                     crypto-label-v1, rebuilt from the bars every run
"""

from __future__ import annotations

import gzip
import io
import json
import time
from datetime import datetime, timezone
from pathlib import Path
from typing import Callable

from ..store import Datastore
from . import telegram as tg
from .exchanges import HOUR, LIVE, MIN, ExchangeError, Http
from .rules import (
    DAY, LABEL_VERSION, OUTCOME_FIELDS, PREFILTER_RANGE, SCAN_VERSION, excluded, outcomes, scan_flags,
)

ROOT = Path("crypto")
STATE = ROOT / "state.json"
CHANNELS = ROOT / "telegram" / "channels.csv"
EVENTS = ROOT / "events.csv"
OUTCOMES = ROOT / "outcomes.csv"

CHANNEL_FIELDS = [
    "name", "title", "subscribers", "source", "added_at", "status", "checked_at", "last_post_id", "last_post_at",
    "last_countdown_at", "posts", "announcements", "calls",
]
EVENT_FIELDS = [
    "event_id", "source", "kind", "exchange", "base", "quote", "t0", "t0_utc", "collected_at", "rule", "channel",
    "post_url", "named_exchange", "spike", "vol_ratio", "quote_volume", "median_quote_volume", "list",
    "time_source", "text",
]
STOP_MAX_DAYS = 180
FALLBACK_ORDER = ("mexc", "kucoin", "gate", "binance")
MINUTE_BEFORE, MINUTE_AFTER = 60 * MIN, 4 * HOUR
HOURLY_BEFORE, HOURLY_AFTER = 48 * HOUR, 7 * DAY
LIVE_PAGES, FIRST_PAGES = 5, 25
NEW_CHANNELS_PER_RUN, MAX_CHANNELS = 10, 300
DEAD_AFTER_DAYS, DEAD_RECHECK_DAYS = 180, 7
SNOWBALL_NAME = __import__("re").compile(r"(?i)pump|signal|whale|gem|call|moon|100x|x100")


def iso(ts: float | None) -> str:
    return "" if ts is None else datetime.fromtimestamp(ts, timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")


def bars_path(source: str, event_id: str) -> Path:
    return ROOT / "bars" / source / f"{event_id}.json.gz"


def load_bars(ds: Datastore, source: str, event_id: str) -> dict:
    p = ds.path(bars_path(source, event_id))
    if not p.exists():
        return {}
    return json.loads(gzip.decompress(p.read_bytes()))


def save_bars(ds: Datastore, source: str, event_id: str, data: dict) -> None:
    buf = io.BytesIO()
    with gzip.GzipFile(fileobj=buf, mode="wb", mtime=0) as gz:
        gz.write(json.dumps(data, separators=(",", ":")).encode())
    p = ds.path(bars_path(source, event_id))
    p.parent.mkdir(parents=True, exist_ok=True)
    p.write_bytes(buf.getvalue())


def write_jsonl_gz(ds: Datastore, rel: Path, rows: list[dict]) -> None:
    buf = io.BytesIO()
    with gzip.GzipFile(fileobj=buf, mode="wb", mtime=0) as gz:
        for r in rows:
            gz.write((json.dumps(r, ensure_ascii=False, separators=(",", ":")) + "\n").encode())
    p = ds.path(rel)
    p.parent.mkdir(parents=True, exist_ok=True)
    p.write_bytes(buf.getvalue())


def seed_channels() -> list[tuple[str, str]]:
    text = (Path(__file__).parent.parent / "data" / "crypto_channels.txt").read_text()
    out = []
    for line in text.splitlines():
        if line.strip() and not line.startswith("#"):
            name, _, note = line.strip().partition(" ")
            out.append((name, note.strip()))
    return out


def stock_collection_finished(ds: Datastore) -> bool:
    p = ds.path("state/state.json")
    return p.exists() and bool(json.loads(p.read_text()).get("finished"))


class Run:
    def __init__(self, ds: Datastore, http: Http | None = None, clock: Callable[[], float] = time.time,
                 max_seconds: float = 20 * 60, run_id: str = "local", log=print):
        self.ds = ds
        self.http = http or Http()
        self.clock = clock
        self.started = clock()
        self.deadline = self.started + max_seconds
        self.run_id = run_id
        self.log = log
        self.exchanges = {k: cls(self.http) for k, cls in LIVE.items()}
        self.tickers: dict[str, dict[str, dict]] = {}
        self.errors: list[str] = []
        self.events = ds.read_csv(EVENTS)
        self.event_ids = {e["event_id"] for e in self.events}
        self.new_events: list[dict] = []
        p = ds.path(STATE)
        self.state = json.loads(p.read_text()) if p.exists() else {}

    def time_left(self) -> float:
        return self.deadline - self.clock()

    def add_event(self, row: dict) -> bool:
        if row["event_id"] in self.event_ids:
            return False
        row.setdefault("collected_at", iso(self.clock()))
        row["t0_utc"] = iso(row["t0"] / 1000)
        self.event_ids.add(row["event_id"])
        self.events.append(row)
        self.new_events.append(row)
        return True

    # ---- tickers ----------------------------------------------------------------------------------------------
    def load_tickers(self) -> None:
        for name, ex in self.exchanges.items():
            try:
                self.tickers[name] = {t["base"]: t for t in ex.tickers()}
            except (ExchangeError, ValueError, KeyError) as exc:
                self.errors.append(f"{name} tickers: {exc}")
                self.log(f"::warning::{name} tickers failed: {exc}")

    def listed(self, exchange: str, base: str) -> bool:
        return base in self.tickers.get(exchange, {})

    # ---- Telegram -----------------------------------------------------------------------------------------------
    def telegram(self) -> dict:
        channels = {c["name"].lower(): c for c in self.ds.read_csv(CHANNELS)}
        now = self.clock()
        for name, note in seed_channels():
            if name.lower() not in channels:
                channels[name.lower()] = dict.fromkeys(CHANNEL_FIELDS, "") | dict(
                    name=name, source=f"seed: {note}", added_at=iso(now), status="new", posts="0", announcements="0", calls="0")
        posts_out: list[dict] = []
        found_links: dict[str, str] = {}
        stats = dict(channels_read=0, posts=0, announcements=0, calls=0, added=0, errors=0)
        for key, ch in list(channels.items()):
            if self.time_left() < 8 * 60:
                break
            if ch["status"] in ("no_preview", "dead") and ch["checked_at"] and \
                    now - tg.iso_to_ts(ch["checked_at"]) < DEAD_RECHECK_DAYS * DAY / 1000:
                continue
            try:
                new_posts, page = self._read_channel(ch)
            except Exception as exc:  # one broken channel must not stop the run
                stats["errors"] += 1
                self.errors.append(f"telegram {ch['name']}: {exc}")
                continue
            stats["channels_read"] += 1
            ch["checked_at"] = iso(now)
            if not page.public:
                ch["status"] = "no_preview"
                continue
            ch["title"] = page.title or ch["title"]
            ch["subscribers"] = page.subscribers or ch["subscribers"]
            last_cd = tg.iso_to_ts(ch["last_countdown_at"]) if ch["last_countdown_at"] else None
            classes, last_cd = tg.classify_channel([(tg.iso_to_ts(p.date), p.text, p.links) for p in new_posts], last_cd)
            ch["last_countdown_at"] = iso(last_cd) if last_cd else ""
            for p, c in zip(new_posts, classes):
                posts_out.append(dict(channel=p.channel, id=p.id, date=p.date, collected_at=iso(now), text=p.text,
                                      links=p.links, views=p.views, tg_class=c.kind, ticker=c.ticker, quote=c.quote,
                                      named_exchange=c.exchange, rule=tg.TG_VERSION))
                ch["posts"] = str(int(ch["posts"] or 0) + 1)
                if c.kind in ("announcement", "call"):
                    stats["announcements" if c.kind == "announcement" else "calls"] += 1
                    ch[c.kind + "s"] = str(int(ch[c.kind + "s"] or 0) + 1)
                    self._telegram_event(p, c)
                for name in tg.channel_links(p.text, p.links):
                    found_links.setdefault(name, ch["name"])
            if new_posts:
                ch["last_post_id"] = str(new_posts[-1].id)
                ch["last_post_at"] = new_posts[-1].date
            last_at = ch["last_post_at"]
            ch["status"] = "dead" if not last_at or now - tg.iso_to_ts(last_at) > DEAD_AFTER_DAYS * 86400 else "active"
            stats["posts"] += len(new_posts)

        # snowball: public channels linked from collected posts whose name or title looks like a pump/signal channel
        for name, via in found_links.items():
            if stats["added"] >= NEW_CHANNELS_PER_RUN or len(channels) >= MAX_CHANNELS or self.time_left() < 6 * 60:
                break
            if name.lower() in channels:
                continue
            status, body = self.http.get(tg.PREVIEW.format(name=name))
            page = tg.parse_page(name, body.decode("utf-8", "replace"), status)
            if not page.public or not (SNOWBALL_NAME.search(name) or SNOWBALL_NAME.search(page.title)):
                continue
            channels[name.lower()] = dict.fromkeys(CHANNEL_FIELDS, "") | dict(
                name=name, title=page.title, subscribers=page.subscribers, source=f"link from {via}",
                added_at=iso(now), status="new", posts="0", announcements="0", calls="0")
            stats["added"] += 1

        self.ds.write_csv(CHANNELS, CHANNEL_FIELDS, sorted(channels.values(), key=lambda c: c["name"].lower()))
        if posts_out:
            d = datetime.fromtimestamp(self.started, timezone.utc)
            write_jsonl_gz(self.ds, ROOT / "telegram" / "posts" / d.strftime("%Y/%m/%d") / f"{d:%H%M%S}Z_{self.run_id}.jsonl.gz",
                           posts_out)
        return stats

    def _read_channel(self, ch: dict) -> tuple[list[tg.Post], tg.Page]:
        last_id = int(ch["last_post_id"] or 0)
        pages = LIVE_PAGES if last_id else FIRST_PAGES
        posts: dict[int, tg.Post] = {}
        before = None
        first_page = None
        for _ in range(pages):
            url = tg.PREVIEW.format(name=ch["name"]) + (f"?before={before}" if before else "")
            status, body = self.http.get(url)
            page = tg.parse_page(ch["name"], body.decode("utf-8", "replace"), status)
            first_page = first_page or page
            if not page.public or not page.posts:
                break
            for p in page.posts:
                if p.id > last_id:
                    posts[p.id] = p
            oldest = page.posts[0].id
            if oldest <= last_id + 1 or before == oldest:
                break
            before = oldest
        return [posts[k] for k in sorted(posts)], first_page

    def _telegram_event(self, p: tg.Post, c: tg.Classified) -> None:
        base = c.ticker.upper()
        # a named exchange is the pump's venue: if it no longer lists the coin, no other exchange stands in for it
        if c.exchange:
            exch = c.exchange if c.exchange in LIVE and self.listed(c.exchange, base) else ""
        else:
            exch = next((e for e in FALLBACK_ORDER if self.listed(e, base)), "")
        t0 = int(tg.iso_to_ts(p.date) * 1000)
        self.add_event(dict(
            event_id=f"tg-{p.channel}-{p.id}", source="telegram", kind=c.kind, exchange=exch or "unmatched",
            base=base, quote="USDT", t0=t0, rule=tg.TG_VERSION, channel=p.channel,
            post_url=f"https://t.me/{p.channel}/{p.id}", named_exchange=c.exchange, text=p.text[:300]))

    # ---- scan ---------------------------------------------------------------------------------------------------
    def scan(self) -> dict:
        now_ms = int(self.clock() * 1000)
        last_complete = now_ms - now_ms % HOUR - HOUR  # open time of the last completed hour
        live_since = self.state["live_since"] * 1000
        last_flag: dict[tuple[str, str], int] = {}
        for e in self.events:
            if e["source"] == "scan":
                k = (e["exchange"], e["base"])
                last_flag[k] = max(last_flag.get(k, 0), int(e["t0"]))
        stats = dict(prefiltered=0, flagged=0)
        for name, tickers in self.tickers.items():
            ex = self.exchanges[name]
            for base, t in sorted(tickers.items()):
                if self.time_left() < 4 * 60:
                    self.errors.append("scan stopped early: time budget")
                    return stats
                if excluded(base) or t["low"] <= 0 or t["high"] < PREFILTER_RANGE * t["low"]:
                    continue
                stats["prefiltered"] += 1
                try:
                    bars = ex.klines(t["symbol"], "1h", last_complete - 48 * HOUR, last_complete + HOUR)
                except (ExchangeError, ValueError, KeyError, IndexError) as exc:
                    self.errors.append(f"{name} {base} klines: {exc}")
                    continue
                for f in scan_flags(bars, None, last_flag.get((name, base))):
                    if f["t0"] < live_since - DAY:
                        continue
                    eid = f"scan-{name}-{base}-{datetime.fromtimestamp(f['t0'] / 1000, timezone.utc):%Y%m%d%H}"
                    if self.add_event(dict(event_id=eid, source="scan", kind="spike", exchange=name, base=base,
                                           quote="USDT", t0=f["t0"], rule=SCAN_VERSION, spike=f["spike"],
                                           vol_ratio=f["vol_ratio"], quote_volume=f["quote_volume"],
                                           median_quote_volume=f["median_quote_volume"])):
                        stats["flagged"] += 1
                        save_bars(self.ds, "scan", eid, dict(hourly=bars, hourly_fetched_at=iso(self.clock())))
                    last_flag[(name, base)] = f["t0"]
        return stats

    # ---- bars ---------------------------------------------------------------------------------------------------
    def fetch_due_bars(self) -> dict:
        now_ms = int(self.clock() * 1000)
        stats = dict(minute=0, final=0, failed=0)
        for e in sorted(self.events, key=lambda e: int(e["t0"])):
            if e["source"] == "history" or e["exchange"] not in LIVE:
                continue
            if self.time_left() < 90:
                break
            t0 = int(e["t0"])
            b = load_bars(self.ds, e["source"], e["event_id"])
            ex = self.exchanges[e["exchange"]]
            sym = ex.symbol(e["base"], e["quote"])
            changed = False
            try:
                if not b.get("minute_fetched_at") and now_ms >= t0 + MINUTE_AFTER + 5 * MIN:
                    start = t0 - t0 % MIN - MINUTE_BEFORE
                    b["minute"] = ex.klines(sym, "1m", start, t0 - t0 % MIN + MINUTE_AFTER)
                    b["minute_fetched_at"] = iso(self.clock())
                    if e["kind"] != "spike":
                        b["hourly"] = ex.klines(sym, "1h", t0 - t0 % HOUR - HOURLY_BEFORE, now_ms - now_ms % HOUR)
                        b["hourly_fetched_at"] = iso(self.clock())
                    stats["minute"] += 1
                    changed = True
                if not b.get("final_at") and now_ms >= t0 + HOURLY_AFTER + HOUR:
                    hourly = ex.klines(sym, "1h", t0 - t0 % HOUR - HOURLY_BEFORE, t0 - t0 % HOUR + HOURLY_AFTER + HOUR)
                    if hourly:
                        b["hourly"] = hourly
                    b["final_at"] = iso(self.clock())
                    b["delisted"] = not self.listed(e["exchange"], e["base"]) if e["exchange"] in self.tickers else False
                    stats["final"] += 1
                    changed = True
            except (ExchangeError, ValueError, KeyError, IndexError) as exc:
                stats["failed"] += 1
                self.errors.append(f"bars {e['event_id']}: {exc}")
            if changed:
                save_bars(self.ds, e["source"], e["event_id"], b)
        return stats

    # ---- outcomes -----------------------------------------------------------------------------------------------
    def rebuild_outcomes(self) -> dict:
        rows, counts = [], {}
        for e in self.events:
            b = load_bars(self.ds, e["source"], e["event_id"])
            if e["exchange"] not in LIVE:
                o = dict.fromkeys(OUTCOME_FIELDS, "") | dict(status="not_covered", label_version=LABEL_VERSION)
            elif e["source"] != "history" and e["kind"] != "spike" and not b.get("minute_fetched_at"):
                o = dict.fromkeys(OUTCOME_FIELDS, "") | dict(status="pending", label_version=LABEL_VERSION)
            elif not b:
                o = dict.fromkeys(OUTCOME_FIELDS, "") | dict(status="pending", label_version=LABEL_VERSION)
            else:
                o = outcomes(e["kind"], int(e["t0"]), b.get("minute") or [], b.get("hourly") or [],
                             final=bool(b.get("final_at")), delisted=bool(b.get("delisted")))
            counts[o["status"]] = counts.get(o["status"], 0) + 1
            rows.append({"event_id": e["event_id"], "source": e["source"], "kind": e["kind"]} | o)
        self.ds.write_csv(OUTCOMES, ["event_id", "source", "kind", *OUTCOME_FIELDS], rows)
        return counts


def write_readme(ds: Datastore, state: dict, counts: dict, n_events: dict) -> None:
    lines = [
        "# Crypto track",
        "",
        "Exchange pump events and public Telegram channels, kept apart from the stock pipeline. Rules, sources and",
        "field definitions: docs/crypto.md on main (tg-v1, scan-v1, crypto-label-v1).",
        "",
        f"Live since {iso(state.get('live_since'))}." + (f" Collection stopped {state['stopped']['at']} ({state['stopped']['reason']})."
                                                         if state.get("stopped") else ""),
        "",
        "| Events | Count |", "|---|---|",
        *[f"| {k} | {v} |" for k, v in sorted(n_events.items())],
        "",
        "| Outcome status | Count |", "|---|---|",
        *[f"| {k} | {v} |" for k, v in sorted(counts.items())],
        "",
        "- `events.csv`: one row per event; `outcomes.csv`: crypto-label-v1 per event, rebuilt every run.",
        "- `bars/<source>/<event_id>.json.gz`: the event's 1-minute and hourly bars [open time ms, open, high, low,",
        "  close, base volume, quote volume] and when they were fetched.",
        "- `telegram/channels.csv`, `telegram/posts/`: every public post read, with its tg-v1 class.",
    ]
    ds.write_text(ROOT / "README.md", "\n".join(lines) + "\n")


def run_crypto(ds: Datastore, run_id: str, max_seconds: float = 20 * 60, http: Http | None = None,
               clock: Callable[[], float] = time.time, log=print) -> dict:
    r = Run(ds, http=http, clock=clock, max_seconds=max_seconds, run_id=run_id, log=log)
    st = r.state
    st.setdefault("live_since", r.started)
    collecting = not st.get("stopped")
    if collecting:
        reason = None
        if stock_collection_finished(ds):
            reason = "the stock collection finished"
        elif r.started - st["live_since"] >= STOP_MAX_DAYS * 86400:
            reason = f"reached the {STOP_MAX_DAYS}-day limit"
        if reason:
            st["stopped"] = dict(at=iso(r.started), reason=reason)
            collecting = False
    summary = dict(run_id=run_id, collecting=collecting)
    r.load_tickers()
    if collecting:
        summary["telegram"] = r.telegram()
        summary["scan"] = r.scan()
    summary["bars"] = r.fetch_due_bars()
    if r.new_events:
        ds.append_csv(EVENTS, EVENT_FIELDS, r.new_events)
    summary["outcomes"] = r.rebuild_outcomes()
    n_events: dict[str, int] = {}
    for e in r.events:
        k = f"{e['source']} / {e['kind']}"
        n_events[k] = n_events.get(k, 0) + 1
    summary["events"] = n_events
    summary["new_events"] = len(r.new_events)
    summary["errors"] = r.errors[:50]
    summary["finished"] = not collecting and summary["outcomes"].get("pending", 0) == 0
    st["last_run"] = dict(at=iso(r.started), run_id=run_id, new_events=len(r.new_events), errors=len(r.errors))
    ds.write_text(STATE, json.dumps(st, indent=2, sort_keys=True) + "\n")
    write_readme(ds, st, summary["outcomes"], n_events)
    return summary
