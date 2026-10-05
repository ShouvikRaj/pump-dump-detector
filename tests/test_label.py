from datetime import date, datetime, timedelta
from zoneinfo import ZoneInfo

from pumpdump import cli, label, track
from pumpdump.market import SNAPSHOT_FIELDS, SNAPSHOTS
from pumpdump.store import Datastore

ET = ZoneInfo("America/New_York")
AS_OF = datetime(2026, 10, 5, 10, 9, tzinfo=ET).timestamp()  # Monday, during the session
NOW = datetime(2026, 11, 20, 12, tzinfo=ET).timestamp()
PUMP = [4.0, 5.0, 6.0, 5.0, 4.0] + [2.0] * 10  # +65% peak on session 3, then -73% from it; closes 50% below the flag


def snap(sid="S1", ticker="ABCD", role="candidate", cik="1", price="4.0", **extra):
    row = dict.fromkeys(SNAPSHOT_FIELDS, "")
    row.update(snapshot_id=sid, episode_id="E1", role=role, ticker=ticker, as_of=str(AS_OF), price_at_flag=price, cik=cik,
               archetype="low_float_runner", **extra)
    return row


def tracked(closes, sid="S1"):
    """Stage 3 rows for one session per weekday from the flag's day on: high = close x 1.1, low = close x 0.9."""
    rows, d = [], date(2026, 10, 5)
    for k, c in enumerate(closes, 1):
        while d.weekday() >= 5:
            d += timedelta(days=1)
        rows.append({"snapshot_id": sid, "k": str(k), "session": d.isoformat(), "open": str(c), "high": str(round(c * 1.1, 6)),
                     "low": str(round(c * 0.9, 6)), "close": str(c)})
        d += timedelta(days=1)
    return rows


def filing(form, accepted, items="", sid="S1"):
    return {"snapshot_id": sid, "form": form, "accepted_at_utc": accepted, "items": items}


def outcome_row(s, daily, filings, status):
    # Stage 3's own outcome function, as written to (and read back from) track/outcomes.csv
    return {k: "" if v is None else str(v) for k, v in track.outcome(s, daily, filings, status, NOW).items()}


def case(closes, filings=(), status="active", **snap_fields):
    s = snap(**snap_fields)
    daily, filings = tracked(closes), list(filings)
    return label.label_row(outcome_row(s, daily, filings, status), s, daily, filings, "0", NOW)


def test_pump_and_dump_path():
    row = case(PUMP)
    assert row["label"] == "pump" and row["pump_dump"] == 1 and row["real_news"] == 0
    assert row["crash_10"] == 1 and row["min_close_10"] == 2.0 and row["ret_min_close_10"] == -0.5
    assert row["peak_k_5"] == "3" and row["peak_maybe_before_flag"] == 0 and row["label_version"] == "label-v1"


def test_a_big_rise_waits_for_the_ten_sessions_after_its_peak():
    row = case([4.0, 5.0, 6.0] + [5.0] * 8)  # peak on session 3; sessions 4-13 needed, 11 recorded
    assert row["label"] == "pending" and row["pump_dump"] == "" and row["crash_10"] == 0


def test_a_rise_that_holds_is_not_a_pump():
    row = case([4.0, 5.0, 6.0] + [5.0] * 12)  # +65%, but the low after the peak is only 32% below it
    assert row["label"] == "not_pump" and row["pump_dump"] == 0 and row["crash_10"] == 0


def test_no_rise_is_final_once_the_news_window_has_been_rechecked():
    assert case([4.0] * 7)["label"] == "pending"  # pump_dump is 0 after 5 sessions, news waits for 10
    row = case([4.0] * 10)
    assert row["label"] == "not_pump" and row["crash_10"] == 0 and row["ret_min_close_10"] == 0.0
    # not an SEC filer: no news is known at once
    row = case([4.0] * 5, cik="")
    assert row["label"] == "not_pump" and row["real_news"] == 0 and row["crash_10"] == ""


def test_a_crash_counts_as_soon_as_a_close_crosses_the_line():
    row = case([4.0, 2.4, 3.0])  # 2.4 = 60% of the 4.0 flag price
    assert row["crash_10"] == 1 and row["min_close_10"] == "" and row["label"] == "pending"
    assert case([4.0, 2.41, 3.0])["crash_10"] == ""


def test_real_news_beats_pump():
    row = case(PUMP, [filing("8-K", "2026-10-06T12:30:00Z", "2.02,9.01")])
    assert row["label"] == "real_news" and row["pump_dump"] == 1 and row["real_news"] == 1
    assert row["news_filings"] == "8-K 2026-10-06T12:30 2.02,9.01 (news)"
    # settles as soon as the 8-K's session is in, not before
    assert case([4.0, 4.0], [filing("8-K", "2026-10-06T12:30:00Z", "5.01")])["label"] == "real_news"
    row = case([4.0, 4.0], [filing("8-K", "2026-10-07T12:30:00Z", "5.01")])
    assert row["label"] == "pending" and row["news_filings"] == ""


def test_a_material_agreement_is_news_unless_it_comes_with_a_share_sale():
    agreement = filing("8-K", "2026-10-06T12:00:00Z", "1.01,9.01")
    assert case(PUMP, [agreement])["label"] == "real_news"
    assert case(PUMP, [filing("8-K", "2026-10-06T12:00:00Z", "1.01,3.02,9.01")])["label"] == "pump"
    row = case(PUMP, [agreement, filing("424B5", "2026-10-07T21:00:00Z")])  # registered direct offering
    assert row["label"] == "pump" and row["news_filings"] == "8-K 2026-10-06T12:00 1.01,9.01"
    assert case(PUMP, [agreement, filing("424B5", "2026-10-09T21:00:00Z")])["label"] == "real_news"  # 3 days later


def test_press_releases_and_foreign_reports_are_listed_but_not_counted():
    row = case(PUMP, [filing("8-K", "2026-10-06T12:00:00Z", "8.01,9.01"), filing("6-K", "2026-10-07T11:00:00Z"),
                      filing("8-K/A", "2026-10-07T12:00:00Z", "2.02")])
    assert row["label"] == "pump" and row["real_news"] == 0
    assert row["news_filings"] == "8-K 2026-10-06T12:00 8.01,9.01; 6-K 2026-10-07T11:00 no items; 8-K/A 2026-10-07T12:00 2.02"


def test_the_news_window_runs_from_72_hours_before_the_flag_to_session_5():
    pre = {"last_current_report_at": "2026-10-03T13:00:00Z", "last_current_report_items": "2.02,9.01"}  # 2 days before
    assert case(PUMP, **pre)["label"] == "real_news"
    assert case(PUMP, last_current_report_at="2026-10-01T13:00:00Z", last_current_report_items="2.02")["label"] == "pump"
    # session 5 is Friday Oct 9; an 8-K after its close is too late
    row = case(PUMP, [filing("8-K", "2026-10-09T20:30:00Z", "2.02")])
    assert row["label"] == "pump" and row["news_filings"] == ""
    assert case(PUMP, [filing("8-K", "2026-10-09T19:30:00Z", "2.02")])["label"] == "real_news"


def test_unknown_when_tracking_ends_before_the_rule_can_be_evaluated():
    row = case([4.0, 6.5, 6.0], status="expired")  # rose, then stopped trading
    assert row["label"] == "unknown" and row["real_news"] == 0
    assert row["note"] == "tracking ended (expired) after 3 sessions, up 79% at its high"
    row = case([], status="no_price", price="")
    assert row["label"] == "unknown" and row["note"] == "no price at the flag"


def test_a_peak_in_the_flag_session_is_marked():
    # the flag came during session 1, whose high may be from before the flag
    row = case([6.0] + [2.0] * 14)
    assert row["label"] == "pump" and row["peak_maybe_before_flag"] == 1


def write_store(tmp_path, cases):
    ds = Datastore(tmp_path)
    snaps, daily, outcomes = [], [], []
    for s, closes in cases:
        rows = tracked(closes, s["snapshot_id"])
        snaps.append(s)
        daily += rows
        outcomes.append(outcome_row(s, rows, [], "active"))
    ds.write_csv(SNAPSHOTS, SNAPSHOT_FIELDS, snaps)
    ds.write_csv(track.DAILY, track.DAILY_FIELDS, daily)
    ds.write_csv(track.OUTCOMES, track.OUTCOME_FIELDS, outcomes)
    ds.write_csv("candidates/episodes.csv", ["episode_id", "warmup"], [{"episode_id": "E1", "warmup": "1"}])
    return ds


def test_run_labels_candidates_and_controls_alike_and_reports_by_archetype(tmp_path):
    ds = write_store(tmp_path, [(snap(), PUMP), (snap("E1/WXYZ", "WXYZ", "control"), [4.0] * 12),
                                (snap("E1/QRST", "QRST", "control"), [4.0] * 3)])
    summary = label.run_label(ds, clock=lambda: NOW)
    rows = {r["ticker"]: r for r in ds.read_csv(label.LABELS)}
    assert {t: r["label"] for t, r in rows.items()} == {"ABCD": "pump", "WXYZ": "not_pump", "QRST": "pending"}
    assert rows["WXYZ"]["warmup"] == "1" and rows["ABCD"]["crash_10"] == "1"
    assert summary["counts"] == {"pump": 1, "not_pump": 1, "pending": 1} and summary["crashes"] == 1
    assert summary["new"] == ["ABCD (candidate) pump", "WXYZ (control) not_pump"] and summary["untracked"] == 0
    readme = ds.path(label.README).read_text()
    assert "| low float runner | candidate | 1 | 0 | 0 | 1 of 1 (100%) | 0 | 0 |" in readme
    assert "| low float runner | control | 0 | 0 | 1 | 0 of 1 (0%) | 1 | 0 |" in readme
    assert "| 2026-10-05 14:09 | ABCD | candidate | low float runner | pump | yes | +65% | -73% | -50% |  |" in readme
    assert "1 of the labeled candidates was flagged in Stage 1's warm-up week" in readme
    # labels already given are not new on the next run
    assert label.run_label(ds, clock=lambda: NOW)["new"] == []


def test_cli_label_writes_a_summary_and_keeps_going_while_collecting(tmp_path):
    ds = write_store(tmp_path, [(snap(), PUMP)])
    ds.write_csv(SNAPSHOTS, SNAPSHOT_FIELDS, [snap(), snap("E2", "NEWT")])  # NEWT has no outcome row yet
    summary, out = tmp_path / "summary.md", tmp_path / "gh_output"
    assert cli.main(["label", "--datastore", str(tmp_path), "--run-id", "7", "--summary", str(summary),
                     "--github-output", str(out)]) == 0
    text = summary.read_text()
    assert "## Label run 7" in text and "1 labeled: 1 pump, 0 real news, 0 not pump" in text and "New labels: ABCD" in text
    assert "finished=false" in out.read_text()
