"""History events: three public lists of Telegram pump announcements, with Binance and KuCoin bars.

- PumpSense (Mahrous et al., ICBC 2026; MIT): chat exports of 39 channels with hand labels, 2017-2023.
- La Morgia et al. (ICCCN 2020 / TOIT 2023; MIT): pump_telegram.csv, 2017-2021.
- Ardia & Bluteau (IRFA 2024): list_pd_events.csv, Binance BTC pairs, 2019-2022. Cite the paper and
  put DOI 10.5281/zenodo.12019080 in a footnote when using it.

The lists are read from their repositories at pinned commits by the `crypto` workflow's history mode
(nothing of theirs is copied into this repository). Merging and time rules: docs/crypto.md.
"""

from __future__ import annotations

import ast
import csv
import glob
import io
import os
from datetime import datetime, timedelta, timezone

from .exchanges import HOUR, MIN, BinanceBulk, ExchangeError, Http, Kucoin
from .run import EVENT_FIELDS, EVENTS, Run, iso, load_bars, save_bars
from .rules import DAY

LAMORGIA = "https://raw.githubusercontent.com/SystemsLab-Sapienza/pump-and-dump-dataset/d71250d4cb055dde2d415c8cba38a0dcd6eb6e16/pump_telegram.csv"
ARDIA = "https://raw.githubusercontent.com/ArdiaD/PumpDump/f493993cc3c528a8b1f563bdffef6ac77488f533/data/list_pd_events.csv"
PUMPSENSE_REPO = "https://github.com/AhmedMahrous00/icbc_2026_reproducibility"
PUMPSENSE_COMMIT = "2fdffd8e5ece48aec317ee5981ee4d4d723ee709"
PUMPSENSE_SHIFT = timedelta(hours=-2)
MERGE_WINDOW = timedelta(hours=3)
PRIORITY = {"ardia": 0, "lamorgia": 1, "pumpsense": 2}
EXCHANGE_NAMES = {"gate.io": "gate", "binance": "binance", "kucoin": "kucoin"}


def _plain(t: str) -> str:
    if not t:
        return ""
    try:
        v = ast.literal_eval(t)
    except (ValueError, SyntaxError, MemoryError, RecursionError):
        return t
    if isinstance(v, str):
        return v
    if isinstance(v, list):
        return "".join(x if isinstance(x, str) else (x.get("text", "") if isinstance(x, dict) else "") for x in v)
    return str(v)


def read_lists(http: Http, pumpsense_dir: str | None) -> list[dict]:
    """Every listed announcement as dict(list, exchange, base, quote, t (UTC datetime), channel, text, time_source)."""
    out = []
    status, body = http.get(LAMORGIA)
    if status == 200:
        for r in csv.DictReader(io.StringIO(body.decode())):
            t = datetime.fromisoformat(f"{r['date']}T{r['hour']}").replace(tzinfo=timezone.utc)
            out.append(dict(list="lamorgia", exchange=r["exchange"].strip().lower(), base=r["symbol"].strip().upper(),
                            quote="BTC", t=t, channel=r["group"], text="", time_source="lamorgia_gmt"))
    status, body = http.get(ARDIA)
    if status == 200:
        for r in csv.DictReader(io.StringIO(body.decode())):
            t = datetime.fromisoformat(r["Date"].replace("Z", "+00:00"))
            out.append(dict(list="ardia", exchange="binance", base=r["Currency"].strip().upper(), quote="BTC", t=t,
                            channel=r["Channel"], text="", time_source="ardia_utc"))
    if pumpsense_dir:
        csv.field_size_limit(10**9)
        for f in sorted(glob.glob(os.path.join(pumpsense_dir, "chat_data", "*", "result11.csv"))):
            group = os.path.basename(os.path.dirname(f))
            with open(f, encoding="utf-8", errors="replace", newline="") as fh:
                for r in csv.DictReader(fh):
                    if (r.get("Pump") or "").strip() not in ("1", "1.0") or not (r.get("Coin") or "").strip():
                        continue
                    base, _, quote = r["Coin"].strip().partition("/")
                    t = datetime.fromisoformat(r["date"]).replace(tzinfo=timezone.utc) + PUMPSENSE_SHIFT
                    out.append(dict(list="pumpsense", exchange=r["Exchange"].strip().lower(), base=base.upper(),
                                    quote=(quote or "btc").upper(), t=t, channel=group, text=_plain(r["text"])[:300],
                                    time_source="pumpsense_minus_2h"))
    return out


def merge(items: list[dict]) -> list[dict]:
    """One event per (exchange, coin, announcements within 3 hours); time from the most exact list."""
    items = sorted(items, key=lambda x: (x["exchange"], x["base"], x["t"]))
    groups: list[list[dict]] = []
    for it in items:
        g = groups[-1] if groups else None
        if g and g[0]["exchange"] == it["exchange"] and g[0]["base"] == it["base"] and it["t"] - g[-1]["t"] <= MERGE_WINDOW:
            g.append(it)
        else:
            groups.append([it])
    events = []
    for g in groups:
        best = min(g, key=lambda x: (PRIORITY[x["list"]], x["t"]))
        exch = EXCHANGE_NAMES.get(best["exchange"], best["exchange"] or "unknown")
        quote = next((x["quote"] for x in g if x["list"] == "pumpsense"), best["quote"])
        t0 = int(best["t"].timestamp() * 1000)
        events.append(dict(
            event_id=f"hist-{exch}-{best['base']}-{best['t']:%Y%m%d%H%M}", source="history", kind="announcement",
            exchange=exch, base=best["base"], quote=quote, t0=t0, rule="history-merge-v1",
            channel="; ".join(dict.fromkeys(x["channel"] for x in g)), list="+".join(sorted({x["list"] for x in g})),
            time_source=best["time_source"], text=next((x["text"] for x in g if x["text"]), "")))
    return events


def run_history(ds, run_id: str, pumpsense_dir: str | None, max_seconds: float = 100 * 60, log=print) -> dict:
    http = Http(min_interval=0.1)
    r = Run(ds, http=http, max_seconds=max_seconds, run_id=run_id, log=log)
    added = 0
    for e in merge(read_lists(http, pumpsense_dir)):
        added += r.add_event(e)
    if r.new_events:
        ds.append_csv(EVENTS, EVENT_FIELDS, r.new_events)
    bulk, kucoin = BinanceBulk(http), Kucoin(http)
    fetched = failed = skipped = 0
    for e in sorted(r.events, key=lambda e: int(e["t0"])):
        if e["source"] != "history" or e["exchange"] not in ("binance", "kucoin"):
            continue
        if load_bars(ds, "history", e["event_id"]):
            skipped += 1
            continue
        if r.time_left() < 120:
            break
        t0 = int(e["t0"])
        src = bulk if e["exchange"] == "binance" else kucoin
        sym = src.symbol(e["base"], e["quote"])
        try:
            minute = src.klines(sym, "1m", t0 - t0 % MIN - 60 * MIN, t0 - t0 % MIN + 4 * HOUR)
            hourly = src.klines(sym, "1h", t0 - t0 % HOUR - 48 * HOUR, t0 - t0 % HOUR + 7 * DAY + HOUR)
        except (ExchangeError, ValueError, KeyError, IndexError, OSError) as exc:
            failed += 1
            r.errors.append(f"history bars {e['event_id']}: {exc}")
            continue
        now = iso(r.clock())
        save_bars(ds, "history", e["event_id"], dict(minute=minute, hourly=hourly, minute_fetched_at=now,
                                                     hourly_fetched_at=now, final_at=now, symbol=sym))
        fetched += 1
    counts = r.rebuild_outcomes()
    remaining = sum(1 for e in r.events if e["source"] == "history" and e["exchange"] in ("binance", "kucoin")
                    and not load_bars(ds, "history", e["event_id"]))
    return dict(added=added, fetched=fetched, failed=failed, skipped=skipped, remaining=remaining, outcomes=counts,
                errors=r.errors[:30])
