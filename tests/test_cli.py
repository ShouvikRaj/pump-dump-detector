import sqlite3

import pytest

from fakes import FakeArcticShift, comment, post
from pumpdump import cli
from pumpdump.store import Datastore

T = 1_791_150_720
DAY = 86_400


@pytest.fixture
def offline(monkeypatch):
    """Point the CLI at an in-memory Arctic Shift and stub the other network sources."""
    server = FakeArcticShift(
        posts=[post("p1", T - 3600, title="$ZZZZ to the moon 🚀 short squeeze")],
        comments=[comment(f"c{i}", T - 1800 - i, author=f"a{i}", body="$ZZZZ 🚀 loading up") for i in range(12)],
    )
    monkeypatch.setattr(
        cli, "make_client", lambda max_retries=5: cli.ArcticShift(get=server.get, min_interval=0, max_retries=max_retries)
    )
    monkeypatch.setattr(cli, "refresh_symbols", lambda: ({}, ["offline"]))
    monkeypatch.setattr(cli, "fetch_trending", lambda clock: [])
    monkeypatch.setattr(cli.time, "time", lambda: T)
    return server


def test_collect_command_writes_datastore_and_summary(tmp_path, offline):
    summary_file = tmp_path / "summary.md"
    code = cli.main(["collect", "--datastore", str(tmp_path / "ds"), "--run-id", "42", "--summary", str(summary_file)])

    assert code == 0
    ds = Datastore(tmp_path / "ds")
    assert len(ds.raw_files()) == 1
    assert [e["ticker"] for e in ds.read_csv("candidates/episodes.csv")] == ["ZZZZ"]
    text = summary_file.read_text()
    assert "ZZZZ" in text and "13 new" in text


def test_source_outage_is_recorded_for_the_health_check_not_a_failed_run(tmp_path, offline):
    # a failed run would skip the push, losing the error counts the health check needs
    offline.failures = [(500, {})] * 1000
    code = cli.main(["collect", "--datastore", str(tmp_path / "ds"), "--run-id", "1", "--max-retries", "0"])
    assert code == 0
    streams = Datastore(tmp_path / "ds").load_state()["streams"]
    assert streams and all(st["consecutive_errors"] == 1 for st in streams.values())


def test_build_db_creates_queryable_sqlite(tmp_path, offline):
    cli.main(["collect", "--datastore", str(tmp_path / "ds"), "--run-id", "42"])
    out = tmp_path / "pumpdump.sqlite"

    assert cli.main(["build-db", "--datastore", str(tmp_path / "ds"), "--out", str(out)]) == 0

    conn = sqlite3.connect(out)
    assert conn.execute("select count(*) from docs").fetchone()[0] == 13
    assert conn.execute("select count(*) from mentions where ticker='ZZZZ'").fetchone()[0] == 13
    assert conn.execute("select ticker, mentions_24h from candidate_episodes").fetchall() == [("ZZZZ", 13)]
    assert conn.execute("select count(*) from runs").fetchone()[0] > 0


def test_scan_prints_tickers_and_hype(capsys):
    assert cli.main(["scan", "$GME to the moon 🚀 short squeeze"]) == 0
    out = capsys.readouterr().out
    assert "GME" in out and "squeeze" in out
