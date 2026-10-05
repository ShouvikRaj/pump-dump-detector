"""Stage 2 run: a market snapshot of each new candidate, as of its flag time, plus matched controls.

Runs after every collect run (the `market` workflow). Reads
candidates/episodes.csv, snapshots each episode that has no snapshot yet, and
appends one row per snapshot to market/snapshots.csv, with the raw source data
next to it. Rows are never rewritten. Design and definitions: docs/stage2.md.
"""

from __future__ import annotations

import csv
import gzip
import hashlib
import io
import json
import random
import time
from dataclasses import dataclass
from datetime import datetime, timezone
from pathlib import Path
from typing import Callable

from .features import (
    ARCHETYPE_VERSION,
    DAY,
    PRICE_KEYS,
    archetype,
    filing_features,
    former_name_change,
    iso,
    price_features,
    sec_shares_asof,
    short_interest_asof,
    split_features,
    utc_date,
    venue_of,
)
from .sources import edgar, finra, nasdaq
from .sources.web import Web
from .sources.yahoo import NoData, SourceError, Yahoo
from .store import Datastore
from .symbols import load_symbols, sec_contact

MARKET_VERSION = "market-v1"
SNAPSHOTS = "market/snapshots.csv"
STATE = "market/state.json"
README = "market/README.md"
RAW_DIR = "market/raw"
UNIVERSE_DIR = "market/universe"

N_CONTROLS = 2
CONTROL_TRIES = 6
CHATTER_DAYS = 7
RETRY_HOURS = 12
UNIVERSE_EVERY = 20 * 3600
HISTORY_DAYS = 2 * 365  # daily bars captured per snapshot
INTRADAY_DAYS = 5

SNAPSHOT_FIELDS = [
    "snapshot_id", "role", "episode_id", "ticker", "as_of", "as_of_utc", "snapshot_at", "snapshot_at_utc", "lag_s",
    "run_id", "exchange", "yahoo_exchange", "venue", "quote_type", "name", "archetype",
    *PRICE_KEYS, "first_trade_date", "reverse_splits_1y", "last_split_date", "last_split_ratio",
    "shares_outstanding", "float_shares", "insider_pct", "institution_pct",
    "sec_shares_outstanding", "sec_shares_as_of", "sec_shares_filed", "market_cap", "turnover_last", "turnover_today",
    "si_settlement_date", "si_shares", "si_prev_shares", "si_days_to_cover", "si_pct_float",
    "dilution_filings_90d", "dilution_filings_365d", "last_dilution_form", "last_dilution_at", "offerings_424b_30d",
    "current_reports_30d", "unregistered_sales_90d", "late_filing_notices_365d", "last_name_change",
    "cik", "sic", "sec_category", "state_of_incorporation", "sector", "industry", "country",
    "errors", "archetype_version", "market_version",
]


@dataclass
class MarketSources:
    yahoo: Yahoo
    web: Web  # SEC, FINRA, Nasdaq
    sec_contact: str | None


def default_sources() -> MarketSources:
    web = Web()
    return MarketSources(yahoo=Yahoo(web), web=web, sec_contact=sec_contact())


class RetryLater(Exception):
    """The core price data failed in a way that may pass; try this candidate again next run."""


def _ratio(a, b):
    return a / b if a is not None and b else None


def _tidy(v):
    return float(f"{v:.6g}") if isinstance(v, float) else v


def take_snapshot(src: MarketSources, ticker: str, as_of: float, sym: dict, now: float, final: bool = False) -> tuple[dict, dict]:
    """(row, raw) for `ticker` as of `as_of`. Raises RetryLater on a transient price failure unless `final`."""
    row: dict = dict.fromkeys(SNAPSHOT_FIELDS)
    row.update(
        ticker=ticker, as_of=round(as_of, 3), as_of_utc=iso(as_of), snapshot_at=round(now, 3), snapshot_at_utc=iso(now),
        lag_s=round(now - as_of), exchange=sym.get("exchange", ""), name=sym.get("name", ""), cik=sym.get("cik", ""),
        archetype="unknown", archetype_version=ARCHETYPE_VERSION, market_version=MARKET_VERSION,
    )
    raw: dict = {"ticker": ticker, "as_of": as_of, "snapshot_at": now}
    errors: list[str] = []
    if ":" in ticker:  # Stage 1 writes foreign listings as "TSXV:XYZ"
        row["errors"] = raw["errors"] = "ticker: non-US listing, not looked up"
        return row, raw

    daily = intraday = None
    summary: dict = {}
    try:
        daily = src.yahoo.chart(ticker, as_of - HISTORY_DAYS * DAY, now, interval="1d")
    except NoData as exc:
        errors.append(f"yahoo: {exc}")
    except SourceError as exc:
        if not final:
            raise RetryLater(f"yahoo: {exc}") from exc
        errors.append(f"yahoo: {exc}")
    if daily is not None:
        try:
            intraday = src.yahoo.chart(ticker, as_of - INTRADAY_DAYS * DAY, now, interval="5m", prepost=True)
        except (NoData, SourceError) as exc:
            errors.append(f"yahoo 5m: {exc}")
        try:
            summary = src.yahoo.summary(ticker)
        except (NoData, SourceError) as exc:
            errors.append(f"yahoo summary: {exc}")

    sub = facts = None
    cik = str(sym.get("cik") or "").strip()
    if cik and not src.sec_contact:
        errors.append("sec: skipped, the SEC_USER_AGENT secret is not set")
    elif cik:
        try:
            sub = edgar.submissions(src.web, int(cik), src.sec_contact, since=utc_date(as_of - HISTORY_DAYS * DAY))
        except Exception as exc:
            errors.append(f"sec: {exc}")
        try:
            facts = edgar.shares_facts(src.web, int(cik), src.sec_contact)
        except Exception as exc:
            errors.append(f"sec shares: {exc}")
    si_rows = None
    try:
        si_rows = finra.short_interest(src.web, ticker, utc_date(as_of - 120 * DAY), utc_date(as_of))
    except Exception as exc:
        errors.append(f"finra: {exc}")

    meta = (daily or {}).get("meta") or {}
    row.update(price_features((daily or {}).get("bars", []), (intraday or {}).get("bars", []), as_of))
    if daily is not None:
        row.update(split_features(daily["splits"], as_of))
    if meta.get("firstTradeDate"):
        row["first_trade_date"] = utc_date(meta["firstTradeDate"])
    row["yahoo_exchange"] = summary.get("exchange") or meta.get("exchangeName") or ""
    row["venue"] = venue_of(row["exchange"], row["yahoo_exchange"], meta.get("fullExchangeName") or summary.get("exchangeName"))
    row["quote_type"] = summary.get("quoteType") or meta.get("instrumentType") or ""
    row["name"] = row["name"] or summary.get("longName") or meta.get("longName") or ""
    row.update(
        shares_outstanding=summary.get("sharesOutstanding"), float_shares=summary.get("floatShares"),
        insider_pct=summary.get("heldPercentInsiders"), institution_pct=summary.get("heldPercentInstitutions"),
        sector=summary.get("sector"), industry=summary.get("industry"), country=summary.get("country"),
    )
    if facts is not None:
        row.update(sec_shares_asof(facts, as_of))
    if sub is not None:
        row.update(filing_features(sub["filings"], as_of))
        row.update(last_name_change=former_name_change(sub["former_names"], as_of), sic=sub["sic"],
                   sec_category=sub["category"], state_of_incorporation=sub["state_of_incorporation"])
    if si_rows is not None:
        row.update(short_interest_asof(si_rows, as_of))
    shares = row["shares_outstanding"] or row["sec_shares_outstanding"]
    flt = row["float_shares"]
    price = row["price_at_flag"]
    row["market_cap"] = price * shares if price is not None and shares else None
    row["turnover_last"] = _ratio(row["vol_last"], flt)
    row["turnover_today"] = _ratio(row["vol_today"], flt)
    row["si_pct_float"] = _ratio(row["si_shares"], flt)
    row["archetype"] = archetype(row["venue"], price, flt, shares)
    row["errors"] = "; ".join(errors)
    raw.update(daily=daily, intraday=intraday, summary=summary, sec=sub, sec_shares=facts, short_interest=si_rows, errors=errors)
    return {k: _tidy(v) for k, v in row.items()}, raw


def pick_controls(seed: str, venue: str, price: float | None, universe: list[dict], symbols: dict, exclude: set[str],
                  tries: int = CONTROL_TRIES) -> list[str]:
    """Up to `tries` control tickers in random order (seeded by `seed`), from the candidate's venue."""
    def eligible(s: str) -> bool:
        info = symbols.get(s)
        return info is not None and str(info.get("is_etf", "0")) not in ("1", "True") and s not in exclude

    if venue == "listed":
        if universe:
            pool = [r for r in universe if eligible(r["symbol"]) and r.get("last_sale")]
            banded = [r for r in pool if price and price / 2 <= r["last_sale"] <= price * 2]
            names = [r["symbol"] for r in (banded if len(banded) >= 10 else pool)]
        else:
            names = [s for s, info in symbols.items() if info.get("exchange") not in ("OTC", "") and eligible(s)]
    elif venue == "otc":
        names = [s for s, info in symbols.items() if info.get("exchange") == "OTC" and eligible(s)]
    else:
        return []
    names = sorted(set(names))
    random.Random(int(hashlib.sha256(seed.encode()).hexdigest()[:16], 16)).shuffle(names)
    return names[:tries]


def _chatter(ds: Datastore, as_of: float) -> set[str]:
    """Tickers mentioned on any of the CHATTER_DAYS days before `as_of` (daily mention counts)."""
    start = utc_date(as_of - CHATTER_DAYS * DAY)
    end = utc_date(as_of)
    months = {start[:7], end[:7]}
    return {
        r["ticker"]
        for m in months
        for r in ds.read_csv(f"daily/mention_counts/{m}.csv")
        if start <= r["date"] <= end and int(float(r.get("mentions") or 0)) > 0
    }


def _write_gz(ds: Datastore, rel: str, data: bytes) -> None:
    path = ds.path(rel)
    path.parent.mkdir(parents=True, exist_ok=True)
    buf = io.BytesIO()
    with gzip.GzipFile(fileobj=buf, mode="wb", mtime=0) as gz:
        gz.write(data)
    path.write_bytes(buf.getvalue())


def _csv_bytes(fields: list[str], rows: list[dict]) -> bytes:
    buf = io.StringIO()
    w = csv.DictWriter(buf, fieldnames=fields, extrasaction="ignore", lineterminator="\n")
    w.writeheader()
    w.writerows(rows)
    return buf.getvalue().encode()


def universe_files(ds: Datastore) -> list[Path]:
    base = ds.path(UNIVERSE_DIR)
    return sorted(base.glob("*/*/*.csv.gz")) if base.exists() else []


def read_universe(path: Path) -> list[dict]:
    with gzip.open(path, "rt", encoding="utf-8") as fh:
        return list(csv.DictReader(fh))


def _latest_universe(ds: Datastore) -> list[dict]:
    files = universe_files(ds)
    if not files:
        return []
    rows = read_universe(files[-1])
    for r in rows:
        try:
            r["last_sale"] = float(r["last_sale"])
        except (TypeError, ValueError):
            r["last_sale"] = None
    return rows


def _save_snapshot(ds: Datastore, row: dict, raw: dict, now: float) -> None:
    day = datetime.fromtimestamp(now, timezone.utc).strftime("%Y/%m/%d")
    name = row["snapshot_id"].replace("/", "_").replace(":", "_")
    _write_gz(ds, f"{RAW_DIR}/{day}/{name}.json.gz", json.dumps(raw, separators=(",", ":"), default=str).encode())
    ds.append_csv(SNAPSHOTS, SNAPSHOT_FIELDS, [row])


def run_market(
    ds: Datastore,
    src: MarketSources,
    *,
    run_id: str,
    clock: Callable[[], float] = time.time,
    max_seconds: float = 480.0,
    n_controls: int = N_CONTROLS,
) -> dict:
    started = clock()
    state = json.loads(ds.path(STATE).read_text()) if ds.path(STATE).exists() else {}
    state.setdefault("pending", {})
    summary: dict = {"run_id": run_id, "snapshots": [], "controls": [], "pending": [], "universe": None, "warnings": []}

    if started - state.get("universe_fetched_at", 0) >= UNIVERSE_EVERY:
        try:
            asof, rows = nasdaq.listed_universe(src.web)
            day = asof or utc_date(started)
            rel = f"{UNIVERSE_DIR}/{day[:4]}/{day[5:7]}/{day}.csv.gz"
            if rows and not ds.path(rel).exists():
                _write_gz(ds, rel, _csv_bytes(nasdaq.FIELDS, rows))
            state["universe_fetched_at"] = started
            summary["universe"] = f"{len(rows)} listed stocks, prices as of {day}"
        except Exception as exc:  # retried next run
            summary["warnings"].append(f"universe: {exc}")

    episodes = ds.read_csv("candidates/episodes.csv")
    done = {r["snapshot_id"] for r in ds.read_csv(SNAPSHOTS) if r["role"] == "candidate"}
    pending = [e for e in episodes if e["episode_id"] not in done]
    if pending:
        symbols = load_symbols(ds)
        universe = _latest_universe(ds)
        candidate_tickers = {e["ticker"] for e in episodes}
    for i, ep in enumerate(pending):
        if clock() - started > max_seconds:
            summary["warnings"].append(f"time budget used up; {len(pending) - i} candidates left for the next run")
            break
        eid, ticker, as_of = ep["episode_id"], ep["ticker"], float(ep["first_flagged_at"])
        sym = symbols.get(ticker, {})
        try:
            row, raw = take_snapshot(src, ticker, as_of, sym, clock())
        except RetryLater as exc:
            p = state["pending"].setdefault(eid, {"first_attempt_at": clock(), "attempts": 0})
            p["attempts"] += 1
            p["last_error"] = str(exc)[:300]
            if clock() - p["first_attempt_at"] < RETRY_HOURS * 3600:
                summary["pending"].append(f"{ticker}: {exc}")
                continue
            row, raw = take_snapshot(src, ticker, as_of, sym, clock(), final=True)
            if row["price_at_flag"] is None:
                row["errors"] = f"{row['errors']} (gave up after {p['attempts']} tries)"
        state["pending"].pop(eid, None)
        row.update(snapshot_id=eid, role="candidate", episode_id=eid, run_id=run_id)
        _save_snapshot(ds, row, raw, clock())
        summary["snapshots"].append(ticker)

        if not n_controls or row["price_at_flag"] is None or row["venue"] not in ("listed", "otc"):
            continue
        exclude = candidate_tickers | _chatter(ds, as_of)
        got = 0
        for name in pick_controls(eid, row["venue"], row["price_at_flag"], universe, symbols, exclude):
            if got >= n_controls:
                break
            try:
                crow, craw = take_snapshot(src, name, as_of, symbols.get(name, {}), clock())
            except RetryLater as exc:
                summary["warnings"].append(f"control {name} for {ticker}: {exc}")
                continue
            if crow["price_at_flag"] is None:
                continue  # Yahoo has nothing for it; draw the next one
            crow.update(snapshot_id=f"{eid}/{name}", role="control", episode_id=eid, run_id=run_id)
            _save_snapshot(ds, crow, craw, clock())
            summary["controls"].append(name)
            got += 1
        if got < n_controls:
            summary["warnings"].append(f"only {got} of {n_controls} controls found for {ticker}")

    if summary["snapshots"] or not ds.path(README).exists():
        ds.write_text(README, render_readme(ds.read_csv(SNAPSHOTS), clock()))
    ds.write_text(STATE, json.dumps(state, indent=2, sort_keys=True) + "\n")
    return summary


def _num(v, fmt="{:,.2f}", scale=1.0) -> str:
    try:
        return fmt.format(float(v) * scale)
    except (TypeError, ValueError):
        return ""


def _shares(v) -> str:
    try:
        x = float(v)
    except (TypeError, ValueError):
        return ""
    return f"{x / 1e9:.2f}B" if x >= 1e9 else f"{x / 1e6:.1f}M"


def render_readme(rows: list[dict], now: float, limit: int = 30) -> str:
    cands = [r for r in rows if r["role"] == "candidate"]
    n_ctrl = sum(1 for r in rows if r["role"] == "control")
    counts: dict[str, int] = {}
    for r in cands:
        counts[r["archetype"]] = counts.get(r["archetype"], 0) + 1
    lines = [
        "# Stage 2 market snapshots",
        "",
        f"Updated {iso(now)}. Each Stage 1 candidate's market data as of the moment it was flagged (price, volume vs",
        "its 20-day average, float, short interest, SEC dilution filings), plus two matched controls nobody was talking",
        "about. Full rows: `snapshots.csv`; definitions: docs/stage2.md on `main`. Statistical context, not advice.",
        "",
        f"{len(cands)} candidates and {n_ctrl} controls so far. Archetypes: "
        + (", ".join(f"{k} {v}" for k, v in sorted(counts.items(), key=lambda kv: -kv[1])) or "none yet") + ".",
        "",
    ]
    if cands:
        lines += [
            "| Ticker | Flagged (UTC) | Archetype | Venue | Price | Since close | 5 days | Rel. volume | Float | Short % float | Dilution filings 90d | Problems |",
            "|---|---|---|---|---|---|---|---|---|---|---|---|",
        ]
        for r in cands[::-1][:limit]:
            lines.append(
                f"| {r['ticker']} | {r['as_of_utc'][:16].replace('T', ' ')} | {r['archetype'].replace('_', ' ')} | {r['venue']} "
                f"| {_num(r['price_at_flag'], '{:,.4g}')} | {_num(r['move_since_close'], '{:+.1f}%', 100)} "
                f"| {_num(r['ret_5d'], '{:+.1f}%', 100)} | {_num(r['rel_vol_last'], '{:.1f}x')} | {_shares(r['float_shares'])} "
                f"| {_num(r['si_pct_float'], '{:.1f}%', 100)} | {r['dilution_filings_90d']} | {r['errors'][:60]} |"
            )
    return "\n".join(lines) + "\n"


def dry_run(src: MarketSources, tickers: list[str], symbols: dict, as_of: float, now: float) -> list[dict]:
    """Snapshots without writing anything (for checking the live sources)."""
    out = []
    for t in tickers:
        try:
            row, _ = take_snapshot(src, t, as_of, symbols.get(t, {}), now, final=True)
        except Exception as exc:  # report and carry on with the rest
            row = {"ticker": t, "errors": f"crash: {type(exc).__name__}: {exc}"}
        out.append(row)
    return out

