"""Exercise scripts/health_issue.sh with a fake `gh` that records calls and applies --jq with real jq."""

import json
import os
import shutil
import subprocess
import sys
from pathlib import Path

import pytest

SCRIPT = Path(__file__).resolve().parents[1] / "scripts" / "health_issue.sh"
pytestmark = pytest.mark.skipif(shutil.which("jq") is None, reason="jq not installed")

FAKE_GH = """#!PYTHON
import json, os, subprocess, sys
args = sys.argv[1:]
with open(os.environ["FAKE_GH_LOG"], "a") as fh:
    fh.write(json.dumps(args) + "\\n")
canned = {("issue", "list"): "FAKE_ISSUES", ("run", "list"): "FAKE_RUNS"}.get(tuple(args[:2]))
if canned:
    out = os.environ.get(canned, "[]")
    if "--jq" in args:
        out = subprocess.run(["jq", "-r", args[args.index("--jq") + 1]], input=out, capture_output=True, text=True, check=True).stdout
    sys.stdout.write(out)
"""


@pytest.fixture
def run(tmp_path):
    bindir = tmp_path / "bin"
    bindir.mkdir()
    gh = bindir / "gh"
    gh.write_text(FAKE_GH.replace("PYTHON", sys.executable))
    gh.chmod(0o755)
    log = tmp_path / "gh.log"

    def _run(health: dict | None, *, status="success", open_issue=None, earlier=()):
        report = tmp_path / "health.json"
        if health is not None:
            report.write_text(json.dumps(health))
        env = dict(
            os.environ,
            PATH=f"{bindir}{os.pathsep}{os.environ['PATH']}",
            FAKE_GH_LOG=str(log),
            FAKE_ISSUES=json.dumps([{"number": open_issue}] if open_issue else []),
            # newest first, like `gh run list`; the current run is still in progress
            FAKE_RUNS=json.dumps([{"status": "in_progress", "conclusion": ""}] + [{"status": "completed", "conclusion": c} for c in earlier]),
            RUN_STATUS=status,
            GITHUB_RUN_ID="42",
        )
        res = subprocess.run(["bash", str(SCRIPT), str(report)], env=env, capture_output=True, text=True)
        assert res.returncode == 0, res.stderr
        calls = [json.loads(line) for line in log.read_text().splitlines()] if log.exists() else []
        log.unlink(missing_ok=True)
        return [c for c in calls if c[:2] != ["issue", "list"] and c[:2] != ["run", "list"]]

    return _run


HEALTHY = {"healthy": True, "problems": []}
SICK = {"healthy": False, "problems": ["wallstreetbets/comments: no complete fetch for 4.0 h"]}


def created_body(calls):
    (create,) = [c for c in calls if c[:2] == ["issue", "create"]]
    return create[create.index("--body") + 1]


def test_healthy_run_with_no_issue_does_nothing(run):
    assert run(HEALTHY) == []


def test_unhealthy_report_opens_an_issue_listing_the_problems(run):
    calls = run(SICK)
    assert "wallstreetbets/comments: no complete fetch for 4.0 h" in created_body(calls)


def test_unhealthy_report_with_issue_already_open_does_not_open_another(run):
    assert [c for c in run(SICK, open_issue=7) if c[:2] == ["issue", "create"]] == []


def test_recovery_closes_the_open_issue(run):
    assert [c[:3] for c in run(HEALTHY, open_issue=7) if c[:2] == ["issue", "close"]] == [["issue", "close", "7"]]


def test_third_failed_run_in_a_row_opens_an_issue(run):
    # the health report on disk is the previous run's and still says healthy
    calls = run(HEALTHY, status="failure", earlier=["failure", "cancelled", "failure", "success"])
    assert "3 collection runs in a row failed" in created_body(calls)


def test_a_single_failed_run_does_not_alert(run):
    assert run(HEALTHY, status="failure", earlier=["failure", "success"]) == []


def test_failed_run_never_closes_the_issue_from_a_stale_report(run):
    assert [c for c in run(HEALTHY, status="failure", open_issue=7, earlier=["success"]) if c[:2] == ["issue", "close"]] == []


def test_missing_report_after_a_failed_checkout_still_counts_failures(run):
    calls = run(None, status="failure", earlier=["failure", "failure"])
    assert "3 collection runs in a row failed" in created_body(calls)
