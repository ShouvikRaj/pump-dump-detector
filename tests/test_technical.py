import gzip
import json
from datetime import date, datetime, timedelta
from zoneinfo import ZoneInfo

import pytest

from pumpdump import technical as t
from pumpdump.market import SNAPSHOT_FIELDS, SNAPSHOTS
from pumpdump.store import Datastore

ET = ZoneInfo("America/New_York")


def et(d, hh=9, mm=30):
    return datetime(d.year, d.month, d.day, hh, mm, tzinfo=ET).timestamp()


def sessions(last, n):
    out, d = [], last
    while len(out) < n:
        if d.weekday() < 5:
            out.append(d)
        d -= timedelta(days=1)
    return out[::-1]


def daily(closes, last=date(2026, 10, 2), lows=None):
    """Daily bars at 09:30 ET ending at `last`; high = close + 1, low = close - 1 unless given."""
    days = sessions(last, len(closes))
    return [[et(d), c, c + 1, (lows[i] if lows else c - 1), c, 1000] for i, (d, c) in enumerate(zip(days, closes))]


def bar(d, hh, mm, o, h, low, c, v):
    return [et(d, hh, mm), o, h, low, c, v]


FLAT = [10.0] * 30
MON = date(2026, 10, 5)


def test_daily_features():
    closes = [10.0] * 25 + [11.0, 12.0, 15.0]
    x = t.daily_features(daily(closes))
    assert x["up_streak"] == 3
    assert x["max_ret_20d"] == pytest.approx(0.25)
    assert x["run_up"] == pytest.approx(0.5)
    assert x["atr_stretch"] > 1  # the close is well above its 20-day mean, in daily ranges
    assert x["ssr_today"] == 0


def test_ssr_from_last_session():
    closes = [10.0] * 25 + [8.0]
    x = t.daily_features(daily(closes, lows=[9.0] * 25 + [8.5]))
    assert x["ssr_today"] == 1  # low 8.5 <= 0.9 x 10


def test_intraday_features_and_no_lookahead():
    done = daily(FLAT, last=date(2026, 10, 2))
    bars = [
        bar(MON, 8, 0, 11, 11, 11, 11, 0),  # pre-market, no volume
        bar(MON, 9, 30, 12, 14, 12, 13, 1000),  # opens 20% up, high 14
        bar(MON, 9, 35, 13, 13, 11, 11.5, 3000),
        bar(MON, 9, 40, 11.5, 11.5, 8.5, 9, 2000),  # falls below 0.9 x 10 = 9
        bar(MON, 9, 45, 9, 30, 9, 30, 99999),  # after the flag: must be ignored
    ]
    as_of = et(MON, 9, 45)
    x = t.intraday_features(bars, as_of, 9.0, done)
    assert x["gap_open"] == pytest.approx(0.2)
    assert x["off_high"] == pytest.approx(9 / 14 - 1)
    assert x["mins_since_high"] == pytest.approx(10)
    vwap = (13 * 1000 + (35.5 / 3) * 3000 + (29 / 3) * 2000) / 6000
    assert x["vwap_ext"] == pytest.approx(9 / vwap - 1)
    assert x["ssr_intraday"] == 1
    # 15 session minutes before the flag: 6000 shares vs 1000/day x 15/390
    assert x["vol_60m_rel"] == pytest.approx(6000 / (1000 * 15 / 390))
    assert x["ret_60m"] == pytest.approx(9 / 11 - 1)  # vs the pre-market bar that ended at 08:05
    assert t.intraday_features(bars, as_of, 9.0, done) == x


def test_ret_60m_and_weekend():
    done = daily(FLAT, last=date(2026, 10, 2))
    bars = [bar(MON, 10, 0, 10, 10, 10, 10, 100), bar(MON, 11, 0, 12, 12, 12, 12, 100)]
    x = t.intraday_features(bars, et(MON, 11, 5), 12.0, done)
    assert x["ret_60m"] == pytest.approx(0.2)
    sat = date(2026, 10, 3)
    y = t.intraday_features([bar(date(2026, 10, 2), 15, 55, 10, 10, 10, 10, 1)], et(sat, 12), 10.0, done)
    assert "off_high" not in y and "vwap_ext" not in y and "vol_60m_rel" not in y


def test_breadth_uses_only_closed_sessions():
    rows = [{"last_sale": "$5", "pct_change": "45.0"}, {"last_sale": "$12", "pct_change": "80"},
            {"last_sale": "2.5", "pct_change": "39.9"}, {"last_sale": "1", "pct_change": "60"}]
    uni = {"2026-10-02": rows[:1], "2026-10-05": rows}
    assert t.breadth(uni, et(MON, 15)) == ("2026-10-02", 1)  # Monday's session not closed yet
    assert t.breadth(uni, et(MON, 16, 30)) == ("2026-10-05", 2)
    assert t.breadth(uni, et(date(2026, 10, 1), 12)) == ("", None)


def test_update_appends_once(tmp_path):
    ds = Datastore(tmp_path)
    as_of, snap_at = et(MON, 9, 45), et(MON, 9, 47)
    snap = dict.fromkeys(SNAPSHOT_FIELDS, "")
    snap.update(snapshot_id="ABCD-1", role="candidate", episode_id="ABCD-1", ticker="ABCD", as_of=as_of,
                snapshot_at=snap_at)
    ds.append_csv(SNAPSHOTS, SNAPSHOT_FIELDS, [snap])
    raw = {"daily": {"bars": daily(FLAT)}, "intraday": {"bars": [bar(MON, 9, 30, 12, 14, 12, 13, 1000)]}}
    p = ds.path(t.raw_path(snap))
    p.parent.mkdir(parents=True)
    p.write_bytes(gzip.compress(json.dumps(raw).encode()))
    assert t.update(ds, snap_at) == 1
    assert t.update(ds, snap_at) == 0
    (row,) = ds.read_csv(t.TECHNICAL)
    assert row["technical_version"] == t.TECHNICAL_VERSION
    assert float(row["gap_open"]) == pytest.approx(0.2)
    assert row["runners_breadth"] == ""  # no cross-section checked out
