"""Exercise scripts/pace.sh with a fake `gh` that records calls and serves canned `gh run list` output."""

import json
import os
import shutil
import subprocess
import sys
from pathlib import Path

import pytest

SCRIPT = Path(__file__).resolve().parents[1] / "scripts" / "pace.sh"
pytestmark = pytest.mark.skipif(shutil.which("jq") is None, reason="jq not installed")

NOW = 1_791_170_000  # 2026-10-05 03:53:20 UTC

FAKE_GH = """#!PYTHON
import json, os, sys
args = sys.argv[1:]
log = os.environ["FAKE_GH_LOG"]
earlier = open(log).read().splitlines() if os.path.exists(log) else []
with open(log, "a") as fh:
    fh.write(json.dumps(args) + "\\n")
if args[:2] == ["run", "list"]:
    sys.stdout.write(os.environ["FAKE_RUNS"])
elif args[:2] == ["workflow", "run"]:
    tries = sum(1 for line in earlier if json.loads(line)[:2] == ["workflow", "run"])
    sys.exit(1 if tries < int(os.environ.get("FAKE_DISPATCH_FAILURES", "0")) else 0)
"""


def iso(ts):
    return subprocess.run(["date", "-u", "-d", f"@{ts}", "+%Y-%m-%dT%H:%M:%SZ"], capture_output=True, text=True).stdout.strip()


@pytest.fixture
def run(tmp_path):
    bindir = tmp_path / "bin"
    bindir.mkdir()
    gh = bindir / "gh"
    gh.write_text(FAKE_GH.replace("PYTHON", sys.executable))
    gh.chmod(0o755)
    log = tmp_path / "gh.log"

    def _run(runs, dispatch_failures=0):
        env = dict(
            os.environ,
            PATH=f"{bindir}{os.pathsep}{os.environ['PATH']}",
            FAKE_GH_LOG=str(log),
            # newest first, like `gh run list`
            FAKE_RUNS=json.dumps([{"status": s, "createdAt": iso(NOW - age)} for s, age in runs]),
            FAKE_DISPATCH_FAILURES=str(dispatch_failures),
            PACE_NOW=str(NOW),
            PACE_RETRY_DELAY="0",
        )
        res = subprocess.run(["bash", str(SCRIPT)], env=env, capture_output=True, text=True)
        calls = [json.loads(line) for line in log.read_text().splitlines()] if log.exists() else []
        log.unlink(missing_ok=True)
        return res, [c for c in calls if c[:2] == ["workflow", "run"]]

    return _run


def test_starts_the_next_collect_run_after_the_wait(run):
    res, dispatched = run([("completed", 16 * 60), ("completed", 31 * 60)])
    assert res.returncode == 0, res.stderr
    assert [c[:3] for c in dispatched] == [["workflow", "run", "collect.yml"]]


def test_starts_a_run_when_there_is_no_history(run):
    res, dispatched = run([])
    assert res.returncode == 0, res.stderr
    assert len(dispatched) == 1


def test_leaves_it_to_a_collect_run_that_is_already_queued_or_running(run):
    for status in ("queued", "in_progress", "waiting"):
        res, dispatched = run([(status, 60), ("completed", 16 * 60)])
        assert res.returncode == 0, res.stderr
        assert dispatched == []


def test_stops_the_chain_when_the_wait_timer_is_missing(run):
    # without the environment's wait timer the pacer would restart collect every couple of minutes
    res, dispatched = run([("completed", 2 * 60)])
    assert res.returncode == 0, res.stderr
    assert dispatched == []
    assert "wait timer" in res.stdout


def test_retries_a_failed_dispatch(run):
    res, dispatched = run([("completed", 16 * 60)], dispatch_failures=2)
    assert res.returncode == 0, res.stderr
    assert len(dispatched) == 3


def test_fails_when_every_dispatch_fails(run):
    res, dispatched = run([("completed", 16 * 60)], dispatch_failures=5)
    assert res.returncode != 0
    assert len(dispatched) == 3
