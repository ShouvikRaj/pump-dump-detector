"""A synthetic data branch for Stage 5 tests: candidates, controls, their Stage 2-4 rows, written as the stages do.

Crashes are planted where the brief expects them: small, heavily hyped candidates crash often, everything else
rarely, so a working model has something to find and a broken one doesn't find it by accident.
"""

from __future__ import annotations

import json
import random
from datetime import date, datetime, timedelta
from zoneinfo import ZoneInfo

from pumpdump.features import iso
from pumpdump.label import LABEL_FIELDS, LABELS
from pumpdump.market import SNAPSHOT_FIELDS, SNAPSHOTS
from pumpdump.pipeline import EPISODE_FIELDS
from pumpdump.store import Datastore
from pumpdump.track import DAILY, DAILY_FIELDS, OUTCOME_FIELDS, OUTCOMES

ET = ZoneInfo("America/New_York")
DAY = 86_400
START = 1_791_158_400.0  # Monday 2026-10-05 00:00 UTC
HOLDOUT = 1_799_020_800.0  # Monday 2027-01-04 00:00 UTC


def letters(n: int) -> str:
    """A 4-letter ticker for candidate number n (AAAA, AAAB, ...), so the extractor can find it as a cashtag."""
    return "".join(chr(65 + (n // 26 ** i) % 26) for i in (3, 2, 1, 0))


def close_ts(d: date) -> float:
    return datetime(d.year, d.month, d.day, 16, tzinfo=ET).timestamp()


def sessions_after(as_of: float, now: float, n: int = 20) -> list[date]:
    """Weekdays whose close came after `as_of` and is an hour old by `now` (no holidays here)."""
    d, out = datetime.fromtimestamp(as_of, ET).date(), []
    while len(out) < n:
        if d.weekday() < 5 and close_ts(d) > as_of:
            if close_ts(d) + 3600 > now:
                break
            out.append(d)
        d += timedelta(days=1)
    return out


def _snapshot(sid, role, eid, ticker, as_of, small, rng):
    row = dict.fromkeys(SNAPSHOT_FIELDS, "")
    price = rng.uniform(1.5, 8) if small else rng.uniform(20, 300)
    float_shares = rng.uniform(2e6, 15e6) if small else rng.uniform(1e8, 5e9)
    row.update(snapshot_id=sid, role=role, episode_id=eid, ticker=ticker, as_of=str(as_of), as_of_utc=iso(as_of),
               venue="listed", archetype="low_float_runner" if small else "other", price_at_flag=f"{price:.4g}",
               ret_1d=f"{rng.gauss(0.05 if small else 0, 0.1):.4f}", ret_5d=f"{rng.gauss(0, 0.2):.4f}",
               ret_20d=f"{rng.gauss(0, 0.3):.4f}", rel_vol_last=f"{rng.uniform(0.5, 6 if small else 2):.3f}",
               volatility_20d=f"{rng.uniform(0.05, 0.15) if small else rng.uniform(0.01, 0.03):.4f}",
               dollar_vol_20d=f"{price * rng.uniform(1e5, 1e6):.0f}", float_shares=f"{float_shares:.0f}",
               shares_outstanding=f"{float_shares * 1.3:.0f}", market_cap=f"{price * float_shares * 1.3:.0f}",
               first_trade_date="2019-01-02", cik="1" if rng.random() < 0.9 else "",
               dilution_filings_90d=str(rng.randint(0, 2) if small else 0), current_reports_30d=str(rng.randint(0, 3)))
    return row


def make_datastore(root, *, weeks: int = 14, per_day: int = 3, now: float, live_since: float = START,
                   seed: int = 0) -> Datastore:
    rng = random.Random(seed)
    ds = Datastore(root)
    episodes, snaps, labels, daily, outcomes = [], [], [], [], []
    for day in range(weeks * 7):
        for j in range(per_day):
            as_of = round(START + day * DAY + rng.uniform(13, 21) * 3600, 3)  # US trading hours
            if as_of > now:
                continue
            eid, ticker = f"E{day:03d}{j}", letters(day * per_day + j)
            small = rng.random() < 0.4
            hype = rng.random()
            mentions = rng.randint(10, 60)
            ep = dict.fromkeys(EPISODE_FIELDS, "")
            ep.update(episode_id=eid, ticker=ticker, first_flagged_at=str(as_of), first_flagged_at_utc=iso(as_of),
                      reasons="mention_spike hype_spike" if hype > 0.7 else "mention_spike",
                      mentions_24h=str(mentions), authors_24h=str(max(5, int(mentions * rng.uniform(0.3, 0.9)))),
                      posts_24h=str(mentions // 4), comments_24h=str(mentions - mentions // 4),
                      baseline_mean=f"{rng.uniform(0, 5):.3f}", z=f"{rng.uniform(2, 12):.3f}",
                      hype_docs_24h=str(int(mentions * hype)),
                      by_subreddit=json.dumps({"pennystocks" if small else "wallstreetbets": mentions}),
                      methods=json.dumps({"cashtag": mentions // 3, "bare": mentions - mentions // 3}),
                      stocktwits_rank="3" if rng.random() < 0.2 else "", warmup="1" if as_of < START + 7 * DAY else "0")
            episodes.append(ep)
            for k, role in enumerate(("candidate", "control", "control")):
                sid = f"S{day:03d}{j}{k}"
                s = _snapshot(sid, role, eid, ticker if role == "candidate" else "X" + letters(day * per_day + j) + str(k),
                              as_of, small, rng)
                snaps.append(s)
                risky = role == "candidate" and small and hype > 0.6
                crash = rng.random() < (0.7 if risky else 0.08 if small else 0.01)
                pump = crash and rng.random() < (0.5 if risky else 0.1)
                days = sessions_after(as_of, now)
                for kk, d in enumerate(days, 1):
                    daily.append({"snapshot_id": sid, "episode_id": eid, "role": role, "ticker": s["ticker"],
                                  "session": d.isoformat(), "k": str(kk)})
                status = "done" if len(days) >= 20 else "active"
                need = 15 if pump else 10
                settled = len(days) >= need
                out = dict.fromkeys(OUTCOME_FIELDS, "")
                out.update(snapshot_id=sid, episode_id=eid, role=role, ticker=s["ticker"], archetype=s["archetype"],
                           as_of_utc=iso(as_of), status=status, sessions=str(len(days)))
                if len(days) >= 10:
                    out["ret_close_10"] = f"{-0.5 if crash else rng.uniform(-0.15, 0.3):.4f}"
                outcomes.append(out)
                lab = dict.fromkeys(LABEL_FIELDS, "")
                lab.update(snapshot_id=sid, episode_id=eid, role=role, ticker=s["ticker"], archetype=s["archetype"],
                           as_of_utc=iso(as_of), track_status=status, sessions=str(len(days)),
                           ret_max_5="0.6" if pump else "0.1", label_version="label-v1")
                if len(days) >= 10:
                    lab["crash_10"] = str(int(crash))
                if settled:
                    news = not pump and rng.random() < 0.05
                    lab.update(label="real_news" if news else "pump" if pump else "not_pump", pump_dump=str(int(pump)))
                else:
                    lab["label"] = "pending"
                labels.append(lab)
    ds.write_csv("candidates/episodes.csv", EPISODE_FIELDS, episodes)
    ds.write_csv(SNAPSHOTS, SNAPSHOT_FIELDS, snaps)
    ds.write_csv(LABELS, LABEL_FIELDS, labels)
    ds.write_csv(DAILY, DAILY_FIELDS, daily)
    ds.write_csv(OUTCOMES, OUTCOME_FIELDS, outcomes)
    ds.save_state({"version": 1, "streams": {}, "episodes": {}, "live_since": live_since})
    return ds
