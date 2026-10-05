from datetime import date, datetime, timedelta
from zoneinfo import ZoneInfo

from market_fakes import CHART_404, FakeClock, FakeHTTP, chart_json, submissions_json
from pumpdump import cli, track
from pumpdump.market import SNAPSHOT_FIELDS, SNAPSHOTS, MarketSources
from pumpdump.sources.web import Web
from pumpdump.sources.yahoo import Yahoo
from pumpdump.store import Datastore

ET = ZoneInfo("America/New_York")
AS_OF = datetime(2026, 10, 5, 10, 9, tzinfo=ET).timestamp()  # Monday, during the session


def et(y, m, d, hh, mm=0):
    return datetime(y, m, d, hh, mm, tzinfo=ET).timestamp()


def snap(sid="S1", ticker="ABCD", role="candidate", price="4.0", cik="", as_of=AS_OF):
    row = dict.fromkeys(SNAPSHOT_FIELDS, "")
    row.update(snapshot_id=sid, episode_id="ABCD-1", role=role, ticker=ticker, as_of=str(as_of), price_at_flag=price,
               cik=cik, archetype="low_float_runner")
    return row


def path_bars(closes, first=date(2026, 10, 5)):
    """Daily bars from `first` on, one per weekday; high = close * 1.1, low = close * 0.9."""
    out, d = [], first
    for c in closes:
        while d.weekday() >= 5:
            d += timedelta(days=1)
        t = datetime(d.year, d.month, d.day, 9, 30, tzinfo=ET).timestamp()
        out.append((t, c, round(c * 1.1, 4), round(c * 0.9, 4), c, 1_000_000))
        d += timedelta(days=1)
    return out


def setup(tmp_path, snaps, routes, now):
    ds = Datastore(tmp_path)
    ds.write_csv(SNAPSHOTS, SNAPSHOT_FIELDS, snaps)
    http = FakeHTTP(routes)
    clock = FakeClock(now)
    web = Web(request=http, sleep=clock.sleep, clock=clock.time, min_interval=0)
    src = MarketSources(yahoo=Yahoo(web), web=web, sec_contact="test me@example.com")
    return ds, src, clock, http


def test_records_finished_sessions_after_the_flag(tmp_path):
    bars = path_bars([4.0, 6.0, 7.0])  # Mon-Wed; Wednesday's session is still open at `now`
    now = et(2026, 10, 7, 12)
    ds, src, clock, _ = setup(tmp_path, [snap()], [("GET", "https://query1.finance.yahoo.com", [(200, chart_json(bars))])], now)
    summary = track.run_track(ds, src, clock=clock.time)
    rows = ds.read_csv(track.DAILY)
    assert [(r["session"], r["k"], r["close"]) for r in rows] == [("2026-10-05", "1", "4.0"), ("2026-10-06", "2", "6.0")]
    assert rows[0]["collected_at_utc"] and rows[0]["track_version"] == track.TRACK_VERSION
    assert summary["new_sessions"] == 2 and summary["active"] == 1
    out = ds.read_csv(track.OUTCOMES)[0]
    assert out["status"] == "active" and out["sessions"] == "2" and out["flag_in_session_1"] == "1"
    assert out["ret_close_1"] == "0.0" and out["ret_max_5"] == ""  # not 5 sessions yet

    # the next day only the new session is appended
    clock.now = et(2026, 10, 8, 18)
    track.run_track(ds, src, clock=clock.time)
    assert [r["session"] for r in ds.read_csv(track.DAILY)] == ["2026-10-05", "2026-10-06", "2026-10-07"]


def test_a_flag_after_the_close_starts_with_the_next_session(tmp_path):
    bars = path_bars([4.0, 5.0])
    ds, src, clock, _ = setup(tmp_path, [snap(as_of=et(2026, 10, 5, 19))],
                              [("GET", "https://query1.finance.yahoo.com", [(200, chart_json(bars))])], et(2026, 10, 7, 9))
    track.run_track(ds, src, clock=clock.time)
    rows = ds.read_csv(track.DAILY)
    assert [(r["session"], r["k"]) for r in rows] == [("2026-10-06", "1")]
    assert ds.read_csv(track.OUTCOMES)[0]["flag_in_session_1"] == "0"


def test_outcome_of_a_pump_and_dump_path(tmp_path):
    # +50% peak on session 3, then -60% from that peak's high within the next 10 sessions
    closes = [4.0, 5.0, 6.0, 5.0, 4.0] + [2.4] * 10 + [2.0] * 10
    bars = path_bars(closes)
    filings = [("8-K", "2026-10-06", "2026-10-06T21:05:00.000Z", "8.01"), ("S-1", "2026-10-08", "2026-10-08T21:00:00.000Z", ""),
               ("10-Q", "2026-09-01", "2026-09-01T20:00:00.000Z", "")]
    routes = [("GET", "https://query1.finance.yahoo.com", [(200, chart_json(bars))]),
              ("GET", "https://data.sec.gov/submissions/", [(200, submissions_json(filings))])]
    ds, src, clock, _ = setup(tmp_path, [snap(cik="1")], routes, et(2026, 11, 10, 12))
    summary = track.run_track(ds, src, clock=clock.time)
    assert len(ds.read_csv(track.DAILY)) == track.SESSIONS
    f = ds.read_csv(track.FILINGS)
    # k = the first session that could react: both were filed after the close; the 10-Q came before the flag
    assert [(r["form"], r["k"]) for r in f] == [("8-K", "3"), ("S-1", "5")]
    out = ds.read_csv(track.OUTCOMES)[0]
    assert out["status"] == "done" and summary["active"] == 0
    assert float(out["max_high_5"]) == 6.6 and out["peak_k_5"] == "3"
    assert abs(float(out["ret_max_5"]) - 0.65) < 1e-9
    assert abs(float(out["drop_from_peak_10"]) - (2.16 / 6.6 - 1)) < 1e-6
    assert out["current_reports_10"] == "1" and out["dilution_filings_20"] == "1"
    assert abs(float(out["ret_close_20"]) + 0.5) < 1e-9

    # done: nothing is fetched again
    calls = []
    src.yahoo.web.request = lambda *a, **k: calls.append(a) or (500, "")
    track.run_track(ds, src, clock=clock.time)
    assert calls == []


def test_prices_stay_in_flag_time_terms_after_a_reverse_split(tmp_path):
    # 1-for-10 reverse split on day 3: Yahoo serves every bar x10, which must not read as a +900% move
    bars = [(t, o * 10, h * 10, lo * 10, c * 10, v) for t, o, h, lo, c, v in path_bars([4.0, 4.0, 4.0])]
    split_t = bars[2][0]
    ds, src, clock, _ = setup(tmp_path, [snap()],
                              [("GET", "https://query1.finance.yahoo.com", [(200, chart_json(bars, splits=[(split_t, 1, 10)]))])],
                              et(2026, 10, 8, 9))
    track.run_track(ds, src, clock=clock.time)
    rows = ds.read_csv(track.DAILY)
    assert [r["close"] for r in rows] == ["4.0", "4.0", "4.0"] and rows[0]["adj_factor"] == "10.0"


def test_gives_up_on_a_ticker_yahoo_no_longer_knows(tmp_path):
    ds, src, clock, http = setup(tmp_path, [snap()], [("GET", "https://query1.finance.yahoo.com", [(404, CHART_404)])],
                                 et(2026, 10, 7, 12))
    summary = track.run_track(ds, src, clock=clock.time)
    assert ds.read_csv(track.OUTCOMES)[0]["status"] == "no_data" and summary["active"] == 0
    n = len(http.calls)
    track.run_track(ds, src, clock=clock.time)
    assert len(http.calls) == n


def test_a_yahoo_outage_is_retried_next_run(tmp_path):
    ds, src, clock, _ = setup(tmp_path, [snap()], [("GET", "https://query1.finance.yahoo.com", [(503, "down")])],
                              et(2026, 10, 7, 12))
    summary = track.run_track(ds, src, clock=clock.time)
    assert summary["active"] == 1 and summary["warnings"]
    assert ds.read_csv(track.OUTCOMES)[0]["status"] == "active"


def test_stops_following_after_45_days_and_skips_rows_without_a_price(tmp_path):
    ds, src, clock, http = setup(tmp_path, [snap(), snap(sid="S2", price="")], [], AS_OF + 46 * 86400)
    summary = track.run_track(ds, src, clock=clock.time)
    assert http.calls == [] and summary["active"] == 0
    assert [o["status"] for o in ds.read_csv(track.OUTCOMES)] == ["expired", "no_price"]


def test_cli_reports_finished_only_when_collection_is_over(tmp_path, monkeypatch):
    ds = Datastore(tmp_path)
    ds.write_csv(SNAPSHOTS, SNAPSHOT_FIELDS, [snap(price="")])
    out = tmp_path / "gh_output"
    monkeypatch.setattr(cli, "default_sources", lambda: MarketSources(yahoo=None, web=None, sec_contact=None))
    cli.main(["track", "--datastore", str(tmp_path), "--github-output", str(out)])
    assert "finished=false" in out.read_text()  # collection has not finished (no live_since yet)


def test_counts_reddit_mentions_after_the_flag_once_the_days_are_over(tmp_path):
    ds, src, clock, _ = setup(tmp_path, [snap(price="")], [], et(2026, 10, 11, 12))  # flag Oct 5; Oct 6-10 are over
    ds.write_csv("daily/mention_counts/2026-10.csv", ["date", "ticker", "mentions"],
                 [{"date": "2026-10-05", "ticker": "ABCD", "mentions": "50"}, {"date": "2026-10-06", "ticker": "ABCD", "mentions": "9"},
                  {"date": "2026-10-10", "ticker": "ABCD", "mentions": "3"}, {"date": "2026-10-06", "ticker": "XYZ", "mentions": "7"}])
    track.run_track(ds, src, clock=clock.time)
    out = ds.read_csv(track.OUTCOMES)[0]
    assert out["mentions_next_5d"] == "12" and out["mentions_next_20d"] == ""
