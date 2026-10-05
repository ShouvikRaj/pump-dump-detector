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

NOW = 1_791_172_400  # 2026-10-05 03:53:20 UTC

FAKE_GH = """#!PYTHON
import json, os, subprocess, sys
args = sys.argv[1:]
log = os.environ["FAKE_GH_LOG"]
earlier = open(log).read().splitlines() if os.path.exists(log) else []
with open(log, "a") as fh:
    fh.write(json.dumps(args) + "\\n")
if args[:2] == ["run", "list"]:
    out = os.environ["FAKE_NIGHTLY" if "nightly.yml" in args else "FAKE_TRACK" if "track.yml" in args
                     else "FAKE_LABEL" if "label.yml" in args else "FAKE_RUNS"]
    if "--jq" in args:
        out = subprocess.run(["jq", "-r", args[args.index("--jq") + 1]], input=out, capture_output=True, text=True, check=True).stdout
    sys.stdout.write(out)
elif args[0] == "api":
    sys.stdout.write(os.environ["FAKE_SELF_CREATED"] + "\\n")
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

    def _run(runs, dispatch_failures=0, nightly_age=10 * 60, now=NOW, nightly=False, waited=13 * 60, pacers=False, track_age=10 * 60, tracks=False,
             label_age=10 * 60, labels=False):
        env = dict(
            os.environ,
            PATH=f"{bindir}{os.pathsep}{os.environ['PATH']}",
            FAKE_GH_LOG=str(log),
            # newest first, like `gh run list`
            FAKE_RUNS=json.dumps([{"status": s, "createdAt": iso(now - age)} for s, age in runs]),
            FAKE_NIGHTLY=json.dumps([] if nightly_age is None else [{"createdAt": iso(now - nightly_age)}]),
            FAKE_DISPATCH_FAILURES=str(dispatch_failures),
            FAKE_SELF_CREATED=iso(now - waited),
            FAKE_TRACK=json.dumps([] if track_age is None else [{"createdAt": iso(now - track_age)}]),
            FAKE_LABEL=json.dumps([] if label_age is None else [{"createdAt": iso(now - label_age)}]),
            GH_REPO="owner/repo",
            GITHUB_RUN_ID="1",
            PACE_NOW=str(now),
            PACE_RETRY_DELAY="0",
        )
        res = subprocess.run(["bash", str(SCRIPT)], env=env, capture_output=True, text=True)
        calls = [json.loads(line) for line in log.read_text().splitlines()] if log.exists() else []
        log.unlink(missing_ok=True)
        dispatched = [c for c in calls if c[:2] == ["workflow", "run"]]
        if nightly:
            return res, [c for c in dispatched if c[2] == "nightly.yml"]
        if tracks:
            return res, [c for c in dispatched if c[2] == "track.yml"]
        if labels:
            return res, [c for c in dispatched if c[2] == "label.yml"]
        if pacers:
            return res, [c for c in dispatched if c[2] == "pace.yml"]
        return res, [c for c in dispatched if c[2] == "collect.yml"]

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


# NOW is 03:53:20 UTC, after the nightly build's 03:41 slot
def test_starts_the_nightly_build_when_todays_never_ran(run):
    # GitHub's cron missed it: the last nightly is from 01:32 UTC, before today's slot
    res, nightly = run([("completed", 16 * 60)], nightly_age=2 * 3600 + 20 * 60, nightly=True)
    assert res.returncode == 0, res.stderr
    assert [c[:3] for c in nightly] == [["workflow", "run", "nightly.yml"]]


def test_starts_the_nightly_build_when_there_is_no_history(run):
    res, nightly = run([("completed", 16 * 60)], nightly_age=None, nightly=True)
    assert len(nightly) == 1


def test_leaves_the_nightly_alone_once_it_ran_today(run):
    res, nightly = run([("completed", 16 * 60)], nightly_age=10 * 60, nightly=True)
    assert nightly == []


def test_leaves_the_nightly_alone_before_its_slot(run):
    # 02:00 UTC; yesterday's nightly ran at 03:45
    two_am = NOW - (NOW % 86400) + 2 * 3600
    res, nightly = run([("completed", 16 * 60)], nightly_age=22 * 3600 + 15 * 60, now=two_am, nightly=True)
    assert nightly == []


def test_checks_the_nightly_even_while_a_collect_run_is_active(run):
    res, nightly = run([("in_progress", 60)], nightly_age=None, nightly=True)
    assert len(nightly) == 1


def test_queues_the_next_pacer_too(run):
    # a collect run GitHub never gives a runner can't queue a pacer, so each pacer queues the next one as well
    res, pacers = run([("completed", 16 * 60)], pacers=True)
    assert res.returncode == 0, res.stderr
    assert [c[:3] for c in pacers] == [["workflow", "run", "pace.yml"]]


def test_queues_the_next_pacer_while_a_collect_run_is_active(run):
    res, pacers = run([("in_progress", 60)], pacers=True)
    assert res.returncode == 0, res.stderr
    assert len(pacers) == 1


def test_does_not_queue_a_pacer_when_the_wait_timer_is_missing(run):
    # this pacer ran 5 s after it was queued: pacer -> pacer would loop every few seconds
    res, pacers = run([("completed", 16 * 60)], waited=5, pacers=True)
    assert res.returncode == 0, res.stderr
    assert pacers == []
    assert "wait timer" in res.stdout


def test_still_queues_a_pacer_when_collect_cannot_be_started(run):
    res, pacers = run([("completed", 16 * 60)], dispatch_failures=3, pacers=True)
    assert res.returncode != 0
    assert len(pacers) == 1


def test_starts_the_track_run_after_its_slot(run):
    # 22:50 UTC; the last track run was yesterday
    late = NOW - (NOW % 86400) + 22 * 3600 + 50 * 60
    res, tracks = run([("completed", 16 * 60)], now=late, track_age=24 * 3600, tracks=True)
    assert res.returncode == 0, res.stderr
    assert [c[:3] for c in tracks] == [["workflow", "run", "track.yml"]]
    res, tracks = run([("completed", 16 * 60)], now=late, track_age=5 * 60, tracks=True)
    assert tracks == []
    res, tracks = run([("completed", 16 * 60)], tracks=True)  # 03:53 UTC, before the slot
    assert tracks == []


def test_starts_the_label_run_after_its_slot(run):
    # 23:30 UTC, after the track run's slot; the last label run was yesterday
    late = NOW - (NOW % 86400) + 23 * 3600 + 30 * 60
    res, labels = run([("completed", 16 * 60)], now=late, label_age=24 * 3600, labels=True)
    assert res.returncode == 0, res.stderr
    assert [c[:3] for c in labels] == [["workflow", "run", "label.yml"]]
    res, labels = run([("completed", 16 * 60)], now=late, label_age=5 * 60, labels=True)
    assert labels == []
    res, labels = run([("completed", 16 * 60)], now=late - 20 * 60, label_age=24 * 3600, labels=True)  # 23:10, before it
    assert labels == []
