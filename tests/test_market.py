import gzip
import json
import sqlite3
from datetime import date, datetime
from zoneinfo import ZoneInfo

import pytest

from market_fakes import FakeClock, MarketWorld, session_bars, shares_json, submissions_json
from pumpdump import cli, market
from pumpdump.db import DAILY_FIELDS
from pumpdump.pipeline import EPISODE_FIELDS
from pumpdump.sources.web import Web
from pumpdump.sources.yahoo import Yahoo
from pumpdump.store import Datastore
from pumpdump.symbols import save_symbols

ET = ZoneInfo("America/New_York")
AS_OF = datetime(2026, 10, 4, 19, 24, tzinfo=ET).timestamp()  # Sunday evening, like DRTS
LAST = date(2026, 10, 2)
UA = "pump-dump-detector me@example.com"


def sym(symbol, exchange="Nasdaq", cik="", is_etf=0):
    return {"symbol": symbol, "name": f"{symbol} Corp", "exchange": exchange, "is_etf": is_etf, "cik": cik, "source": "test"}


LISTED = [f"L{i}" for i in range(1, 13)]
OTC = [f"O{i}" for i in range(1, 6)]


@pytest.fixture
def world():
    w = MarketWorld()
    w.add_stock(
        "ABCD",
        session_bars(LAST, close=4.0),
        summary={"exchange": "NCM", "exchangeName": "NasdaqCM", "quoteType": "EQUITY", "floatShares": 8_000_000,
                 "sharesOutstanding": 12_000_000, "sector": "Healthcare"},
        short=[("2026-09-15", 800_000, 700_000, 3.5)],
    )
    for s in LISTED + ["CHAT"]:
        w.add_stock(s, session_bars(LAST, close=5.0), summary={"exchange": "NMS", "exchangeName": "NasdaqGS", "floatShares": 5_000_000})
    w.add_stock("BIG", session_bars(LAST, close=150.0), summary={"exchange": "NYQ", "exchangeName": "NYSE"})
    for s in OTC + ["OPNK"]:
        w.add_stock(s, session_bars(LAST, close=0.05), summary={"exchange": "PNK", "exchangeName": "OTC Markets Pink"})
    w.submissions[1001] = submissions_json(
        [("424B5", "2026-09-30", "2026-09-30T20:15:00.000Z", ""), ("8-K", "2026-09-11", "2026-09-11T14:38:02.000Z", "3.02,9.01")]
    )
    w.shares[1001] = shares_json([("2026-08-12", 11_500_000, "2026-08-14", "10-Q")])
    w.universe = [("ABCD", "4.00", 1000, 48_000_000), ("CHAT", "4.10", 1000, 1), ("BIG", "150.00", 1000, 1)]
    w.universe += [(s, f"{3 + 0.2 * i:.2f}", 1000, 1) for i, s in enumerate(LISTED)]
    return w


@pytest.fixture
def ds(tmp_path):
    d = Datastore(tmp_path / "ds")
    syms = [sym("ABCD", cik="1001"), sym("CHAT"), sym("BIG", "NYSE"), sym("SPYX", "NYSE Arca", is_etf=1)]
    syms += [sym(s) for s in LISTED] + [sym(s, "OTC", cik=str(2000 + i)) for i, s in enumerate(OTC)] + [sym("OPNK", "OTC")]
    save_symbols(d, {s["symbol"]: s for s in syms})
    d.append_csv(
        "daily/mention_counts/2026-10.csv",
        DAILY_FIELDS,
        [{"date": "2026-10-01", "ticker": "CHAT", "mentions": 3}, {"date": "2026-10-01", "ticker": "O1", "mentions": 1}],
    )
    d.append_csv("daily/mention_counts/2026-09.csv", DAILY_FIELDS, [{"date": "2026-09-20", "ticker": "L2", "mentions": 9}])
    return d


def add_episode(ds, ticker, as_of=AS_OF):
    eid = f"{ticker}-{datetime.fromtimestamp(as_of, ZoneInfo('UTC')).strftime('%Y%m%dT%H%M%SZ')}"
    ds.append_csv("candidates/episodes.csv", EPISODE_FIELDS, [{"episode_id": eid, "ticker": ticker, "first_flagged_at": as_of}])
    return eid


def run(ds, world, clock, contact=UA, **kw):
    web = Web(request=world, sleep=clock.sleep, clock=clock.time)
    src = market.MarketSources(yahoo=Yahoo(web), web=web, sec_contact=contact)
    return market.run_market(ds, src, run_id="r1", clock=clock.time, **kw)


def rows(ds):
    return ds.read_csv(market.SNAPSHOTS)


def test_new_candidate_gets_a_snapshot_two_matched_controls_and_raw_files(ds, world):
    eid = add_episode(ds, "ABCD")
    clock = FakeClock(AS_OF + 120)
    summary = run(ds, world, clock)

    out = rows(ds)
    cand = [r for r in out if r["role"] == "candidate"]
    ctrl = [r for r in out if r["role"] == "control"]
    assert len(cand) == 1 and len(ctrl) == 2
    c = cand[0]
    assert c["snapshot_id"] == eid and c["episode_id"] == eid and c["ticker"] == "ABCD"
    assert c["venue"] == "listed" and c["archetype"] == "low_float_runner"
    assert float(c["price_at_flag"]) == 4.0 and c["last_session"] == "2026-10-02"
    assert int(float(c["float_shares"])) == 8_000_000 and int(float(c["sec_shares_outstanding"])) == 11_500_000
    assert c["si_settlement_date"] == "2026-09-15" and float(c["si_pct_float"]) == pytest.approx(0.1)
    assert c["dilution_filings_90d"] == "1" and c["unregistered_sales_90d"] == "1" and c["last_dilution_form"] == "424B5"
    assert c["errors"] == "" and c["market_version"] == market.MARKET_VERSION
    assert float(c["lag_s"]) == pytest.approx(120, abs=60)
    for r in ctrl:
        assert r["episode_id"] == eid and r["snapshot_id"] == f"{eid}/{r['ticker']}"
        assert r["ticker"] in LISTED and r["as_of"] == c["as_of"]
    raw_files = sorted(ds.path("market/raw").rglob("*.json.gz"))
    assert len(raw_files) == 3
    raw = json.loads(gzip.decompress(raw_files[0].read_bytes()))
    assert raw["daily"]["bars"] and "intraday" in raw and "short_interest" in raw
    assert "ABCD" in ds.path(market.README).read_text()
    assert summary["snapshots"] == ["ABCD"]



def test_timing_columns_keep_full_precision(ds, world):
    add_episode(ds, "ABCD", as_of=AS_OF + 1.5)
    run(ds, world, FakeClock(AS_OF + 120.25))
    c = [r for r in rows(ds) if r["role"] == "candidate"][0]
    assert float(c["as_of"]) == AS_OF + 1.5
    assert AS_OF + 120.25 <= float(c["snapshot_at"]) < AS_OF + 180

def test_a_second_run_does_not_snapshot_the_same_candidate_again(ds, world):
    add_episode(ds, "ABCD")
    clock = FakeClock(AS_OF + 120)
    run(ds, world, clock)
    clock.now += 900
    summary = run(ds, world, clock)
    assert len(rows(ds)) == 3 and summary["snapshots"] == []



def test_rows_written_before_a_column_was_added_are_carried_over_under_the_new_header(ds, world):
    old_fields = [f for f in market.SNAPSHOT_FIELDS if f != "last_current_report_at"]
    ds.append_csv(market.SNAPSHOTS, old_fields, [{"snapshot_id": "OLD-1", "role": "candidate", "ticker": "OLD", "errors": "x"}])
    add_episode(ds, "ABCD")
    run(ds, world, FakeClock(AS_OF + 120))
    with ds.path(market.SNAPSHOTS).open() as fh:
        assert fh.readline().strip().split(",") == market.SNAPSHOT_FIELDS
    old = [r for r in rows(ds) if r["snapshot_id"] == "OLD-1"][0]
    assert old["ticker"] == "OLD" and old["errors"] == "x" and old["last_current_report_at"] == ""
    assert [r["ticker"] for r in rows(ds) if r["role"] == "candidate"] == ["OLD", "ABCD"]

def test_a_ticker_yahoo_does_not_know_is_written_at_once_without_controls(ds, world):
    add_episode(ds, "ZZZZ")
    clock = FakeClock(AS_OF + 120)
    run(ds, world, clock)
    run(ds, world, clock)

    out = rows(ds)
    assert len(out) == 1 and out[0]["ticker"] == "ZZZZ"
    assert "yahoo: No data found" in out[0]["errors"] and out[0]["price_at_flag"] == "" and out[0]["archetype"] == "unknown"


def test_a_yahoo_outage_keeps_the_candidate_pending_then_gives_up_after_12_hours(ds, world):
    add_episode(ds, "ABCD")
    world.down = {"query1.finance.yahoo.com"}
    clock = FakeClock(AS_OF + 120)
    summary = run(ds, world, clock)
    assert rows(ds) == [] and len(summary["pending"]) == 1
    assert json.loads(ds.path(market.STATE).read_text())["pending"]

    clock.now += 13 * 3600
    run(ds, world, clock)
    out = rows(ds)
    assert len(out) == 1 and "gave up after 2 tries" in out[0]["errors"]
    assert json.loads(ds.path(market.STATE).read_text())["pending"] == {}



class BrokenYahoo(Yahoo):
    """Yahoo whose chart parsing blows up for one ticker, standing in for an unexpected bug or odd data."""

    def chart(self, ticker, *args, **kwargs):
        if ticker == "ABCD":
            raise KeyError("timestamp")
        return super().chart(ticker, *args, **kwargs)


def test_a_candidate_that_crashes_does_not_block_the_others_and_is_written_after_12_hours(ds, world):
    add_episode(ds, "ABCD")
    add_episode(ds, "OPNK")
    clock = FakeClock(AS_OF + 120)

    def broken_run():
        web = Web(request=world, sleep=clock.sleep, clock=clock.time)
        src = market.MarketSources(yahoo=BrokenYahoo(web), web=web, sec_contact=UA)
        return market.run_market(ds, src, run_id="r1", clock=clock.time)

    summary = broken_run()
    assert [r["ticker"] for r in rows(ds) if r["role"] == "candidate"] == ["OPNK"]
    assert len(summary["pending"]) == 1 and "KeyError" in summary["pending"][0]

    clock.now += 13 * 3600
    broken_run()
    abcd = [r for r in rows(ds) if r["ticker"] == "ABCD"]
    assert len(abcd) == 1 and "crash: KeyError" in abcd[0]["errors"] and abcd[0]["as_of_utc"]

def test_a_foreign_listing_is_recorded_without_any_lookup(ds, world):
    add_episode(ds, "TSXV:ABC")
    run(ds, world, FakeClock(AS_OF + 120))
    out = rows(ds)
    assert len(out) == 1 and "non-US listing" in out[0]["errors"] and out[0]["venue"] == "unknown"
    assert not any("ABC" in c["url"] or "ABC" in json.dumps(c["json"] or {}) for c in world.calls)


def test_the_listed_universe_is_saved_once_a_day_under_its_price_date(ds, world):
    clock = FakeClock(AS_OF + 120)
    summary = run(ds, world, clock)
    path = ds.path("market/universe/2026/10/2026-10-01.csv.gz")
    assert path.exists() and "15 listed stocks" in summary["universe"]
    n_calls = len(world.calls)
    clock.now += 3600
    run(ds, world, clock)
    assert len(world.calls) == n_calls  # nothing to snapshot and the universe is fresh


def test_otc_candidates_get_otc_controls_that_nobody_mentioned(ds, world):
    add_episode(ds, "OPNK")
    run(ds, world, FakeClock(AS_OF + 120))
    out = rows(ds)
    cand = [r for r in out if r["role"] == "candidate"][0]
    ctrl = [r["ticker"] for r in out if r["role"] == "control"]
    assert cand["venue"] == "otc" and cand["archetype"] == "otc_penny"
    assert len(ctrl) == 2 and set(ctrl) <= set(OTC) - {"O1"}



def test_controls_of_a_low_float_runner_are_low_float_runners_too(ds, world):
    world.universe = [("ABCD", "4.00", 1000, 1)] + [(s, "4.00", 1000, 1) for s in LISTED[:10]]
    for s in LISTED[:8]:
        world.summaries[s]["floatShares"] = 50_000_000
    add_episode(ds, "ABCD")
    run(ds, world, FakeClock(AS_OF + 120))
    assert sorted(r["ticker"] for r in rows(ds) if r["role"] == "control") == ["L10", "L9"]


def test_controls_of_an_otc_penny_stock_are_otc_penny_stocks_too(ds, world):
    for s in ("O2", "O3", "O4"):
        world.daily[s] = session_bars(LAST, close=3.0)
    add_episode(ds, "OPNK")
    summary = run(ds, world, FakeClock(AS_OF + 120))
    assert [r["ticker"] for r in rows(ds) if r["role"] == "control"] == ["O5"]
    assert "only 1 of 2 controls found for OPNK" in summary["warnings"]

def test_controls_yahoo_has_no_data_for_are_replaced(ds, world):
    world.universe = [("ABCD", "4.00", 1000, 1), ("L1", "4.00", 1000, 1), ("L2", "4.10", 1000, 1), ("L3", "3.90", 1000, 1)]
    del world.daily["L1"]
    add_episode(ds, "ABCD")
    run(ds, world, FakeClock(AS_OF + 120))
    assert sorted(r["ticker"] for r in rows(ds) if r["role"] == "control") == ["L2", "L3"]


def test_without_an_sec_contact_filings_are_left_blank_and_the_reason_noted(ds, world):
    add_episode(ds, "ABCD")
    run(ds, world, FakeClock(AS_OF + 120), contact=None)
    c = [r for r in rows(ds) if r["role"] == "candidate"][0]
    assert "SEC_USER_AGENT" in c["errors"]
    assert c["dilution_filings_90d"] == "" and c["sec_shares_outstanding"] == ""
    assert not any("sec.gov" in call["url"] for call in world.calls)



def test_the_readme_table_survives_errors_with_pipes_and_line_breaks():
    row = dict.fromkeys(market.SNAPSHOT_FIELDS, "")
    row.update(role="candidate", ticker="ABCD", as_of_utc="2026-10-04T23:24:00Z", archetype="unknown", venue="unknown",
               errors="yahoo: chart HTTP 503: <td>a|b|c</td>\nmore")
    table = [line for line in market.render_readme([row], AS_OF).splitlines() if "|" in line]
    assert len(table) == 3  # header, rule, one row
    assert table[2].startswith("| ABCD") and table[2].endswith(" |") and table[2].count("|") == 13

# -- control selection ------------------------------------------------------------------


def uni(*pairs):
    return [{"symbol": s, "last_sale": p} for s, p in pairs]


SYMS = {s: sym(s) for s in ["A1", "A2", "CHAT", "BIG"] + [f"B{i}" for i in range(12)]} | {"ETF1": sym("ETF1", "NYSE Arca", is_etf=1)}


def test_controls_skip_excluded_tickers_and_etfs():
    picks = market.pick_controls("seed", "listed", 4.0, uni(("CHAT", 4.0), ("A1", 4.0), ("ETF1", 4.0)), SYMS, exclude={"CHAT"})
    assert picks == ["A1"]


def test_controls_are_common_stock_not_warrants_units_rights_notes_or_preferreds():
    names = {
        "A1": "Alpha Corp. Common Stock",
        "A2": "Beta plc American Depositary Shares, each representing the right to receive one ordinary share",
        "B0": "DUKE Robotics Corp. - Warrant",
        "B1": "Gamma Acquisition Corp. Units, each consisting of one Class A ordinary share and one right",
        "B2": "Gamma Acquisition Corp. Rights",
        "B3": "Delta Co. 6.250% Senior Notes due 2069",
        "B4": "Delta Co. Depositary Shares each representing 1/1000th interest in a share of Series A Preferred Stock",
        "B5": "Preferred Bank Common Stock",
        "B6": "Epsilon Inc. Series A Common Stock Purchase Warrants",
        "B7": "Zeta Royalty Partners Common Units Representing Limited Partner Interests",
    }
    universe = [{"symbol": s, "last_sale": 4.0, "name": n} for s, n in names.items()]
    assert sorted(market.pick_controls("seed", "listed", 4.0, universe, SYMS, exclude=set())) == ["A1", "A2", "B5", "B7"]


def test_controls_are_price_matched_when_enough_qualify():
    universe = uni(("BIG", 150.0), *[(f"B{i}", 3.0 + 0.1 * i) for i in range(12)])
    picks = market.pick_controls("seed", "listed", 4.0, universe, SYMS, exclude=set())
    assert len(picks) == market.CONTROL_TRIES and "BIG" not in picks



def test_controls_are_also_size_matched_when_enough_qualify():
    universe = [{"symbol": f"B{i}", "last_sale": 4.0, "market_cap": 50e6 if i < 10 else 5e9} for i in range(12)]
    picks = market.pick_controls("seed", "listed", 4.0, universe, SYMS, exclude=set(), market_cap=40e6)
    assert len(picks) == 10 and not {"B10", "B11"} & set(picks)

def test_controls_widen_to_all_listed_stocks_when_few_are_price_matched():
    universe = uni(("BIG", 150.0), ("A1", 4.0), ("A2", 4.2))
    assert sorted(market.pick_controls("seed", "listed", 4.0, universe, SYMS, exclude=set())) == ["A1", "A2", "BIG"]


def test_control_draws_are_reproducible_per_episode():
    universe = uni(*[(f"B{i}", 4.0) for i in range(12)])
    a = market.pick_controls("ABCD-1", "listed", 4.0, universe, SYMS, exclude=set())
    assert a == market.pick_controls("ABCD-1", "listed", 4.0, universe, SYMS, exclude=set())
    assert a != market.pick_controls("EFGH-2", "listed", 4.0, universe, SYMS, exclude=set())


def test_unknown_venues_get_no_controls():
    assert market.pick_controls("seed", "unknown", 4.0, uni(("A1", 4.0)), SYMS, exclude=set()) == []


def test_without_a_universe_file_listed_controls_come_from_the_symbol_list():
    picks = market.pick_controls("seed", "listed", 4.0, [], SYMS, exclude={"CHAT", "BIG"})
    assert len(picks) == market.CONTROL_TRIES and set(picks) <= {"A1", "A2"} | {f"B{i}" for i in range(12)}


# -- command line and database ------------------------------------------------------------


@pytest.fixture
def offline(monkeypatch, world):
    """Point the CLI's market sources at the fake world, with a fake clock."""
    clock = FakeClock(AS_OF + 120)
    web = Web(request=world, sleep=clock.sleep, clock=clock.time)
    monkeypatch.setattr(cli, "default_sources", lambda: market.MarketSources(yahoo=Yahoo(web), web=web, sec_contact=UA))
    monkeypatch.setattr(cli.time, "time", clock.time)
    return world


def test_market_command_snapshots_new_candidates_and_writes_a_summary(ds, offline, tmp_path):
    add_episode(ds, "ABCD")
    out = tmp_path / "summary.md"
    assert cli.main(["market", "--datastore", str(ds.root), "--run-id", "7", "--summary", str(out)]) == 0
    assert [r["ticker"] for r in rows(ds) if r["role"] == "candidate"] == ["ABCD"]
    assert {r["run_id"] for r in rows(ds)} == {"7"}
    text = out.read_text()
    assert "ABCD" in text and "2 controls" in text and "15 listed stocks" in text


def test_market_dry_run_prints_one_json_row_per_ticker_and_saves_nothing(ds, offline, capsys):
    args = ["market", "--datastore", str(ds.root), "--dry-run", "ABCD", "ZZZZ", "--as-of", "2026-10-04T23:24:00Z"]
    assert cli.main(args) == 0
    out = [json.loads(line) for line in capsys.readouterr().out.splitlines() if line.startswith("{")]
    assert [r["ticker"] for r in out] == ["ABCD", "ZZZZ"]
    assert out[0]["as_of_utc"] == "2026-10-04T23:24:00Z" and out[0]["archetype"] == "low_float_runner"
    assert "No data found" in out[1]["errors"]
    assert not ds.path("market").exists()


def test_build_db_loads_market_snapshots_and_the_daily_universe(ds, offline, tmp_path):
    add_episode(ds, "ABCD")
    cli.main(["market", "--datastore", str(ds.root), "--run-id", "7"])
    db_path = tmp_path / "x.sqlite"
    assert cli.main(["build-db", "--datastore", str(ds.root), "--out", str(db_path)]) == 0
    conn = sqlite3.connect(db_path)
    got = conn.execute("select ticker, archetype, price_at_flag from market_snapshots where role = 'candidate'").fetchall()
    assert got == [("ABCD", "low_float_runner", 4.0)]
    assert conn.execute("select count(*) from market_snapshots where role = 'control'").fetchone() == (2,)
    assert conn.execute("select count(*), min(date), max(date) from market_universe").fetchone() == (15, "2026-10-01", "2026-10-01")
