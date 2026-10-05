"""Exercise scripts/datastore.sh against a local bare repo standing in for GitHub."""

import os
import shutil
import subprocess
from datetime import datetime, timedelta, timezone
from pathlib import Path

import pytest

SCRIPT = Path(__file__).resolve().parents[1] / "scripts" / "datastore.sh"
pytestmark = pytest.mark.skipif(shutil.which("git") is None, reason="git not installed")


def sh(*args, env, cwd=None, check=True):
    return subprocess.run(args, env=env, cwd=cwd, check=check, capture_output=True, text=True)


@pytest.fixture
def env(tmp_path):
    remote = tmp_path / "remote.git"
    subprocess.run(["git", "init", "--quiet", "--bare", str(remote)], check=True)
    e = dict(os.environ)
    e.update(
        DATASTORE_REMOTE=f"file://{remote}",
        GIT_CONFIG_GLOBAL=str(tmp_path / "gitconfig"),  # keep the developer's git config (signing etc.) out
        GIT_CONFIG_NOSYSTEM="1",
    )
    (tmp_path / "gitconfig").write_text("[protocol \"file\"]\n\tallow = always\n[uploadpack]\n\tallowFilter = true\n")
    return e


def day_dir(days_ago):
    return (datetime.now(timezone.utc) - timedelta(days=days_ago)).strftime("%Y/%m/%d")


def month(days_ago=0):
    return (datetime.now(timezone.utc) - timedelta(days=days_ago)).strftime("%Y-%m")


def write(root: Path, rel: str, text: str):
    p = root / rel
    p.parent.mkdir(parents=True, exist_ok=True)
    p.write_text(text)


def remote_file(env, tmp_path, rel):
    out = tmp_path / "inspect"
    if out.exists():
        shutil.rmtree(out)
    sh("git", "clone", "--quiet", "--branch", "data", env["DATASTORE_REMOTE"], str(out), env=env)
    p = out / rel
    return p.read_text() if p.exists() else None


def test_first_push_creates_branch_and_later_checkouts_are_sparse(env, tmp_path):
    a = tmp_path / "a"
    sh("bash", str(SCRIPT), "checkout", str(a), "9", env=env)
    write(a, "state/state.json", "{}\n")
    write(a, f"raw/reddit/{day_dir(0)}/r1.jsonl.gz", "today")
    write(a, f"raw/reddit/{day_dir(20)}/old.jsonl.gz", "old")
    write(a, f"logs/runs/{month()}.csv", "h\nrow1\n")
    sh("bash", str(SCRIPT), "push", str(a), "run 1", env=env)

    b = tmp_path / "b"
    sh("bash", str(SCRIPT), "checkout", str(b), "9", env=env)
    assert (b / "state/state.json").exists()
    assert (b / f"raw/reddit/{day_dir(0)}/r1.jsonl.gz").exists()
    assert not (b / f"raw/reddit/{day_dir(20)}").exists()  # outside the 9-day window

    # appending to a monthly log in a sparse checkout must not clobber it
    with open(b / f"logs/runs/{month()}.csv", "a") as fh:
        fh.write("row2\n")
    sh("bash", str(SCRIPT), "push", str(b), "run 2", env=env)
    assert remote_file(env, tmp_path, f"logs/runs/{month()}.csv") == "h\nrow1\nrow2\n"
    assert remote_file(env, tmp_path, f"raw/reddit/{day_dir(20)}/old.jsonl.gz") == "old"


def test_push_replays_commit_when_branch_moved(env, tmp_path):
    a = tmp_path / "a"
    sh("bash", str(SCRIPT), "checkout", str(a), "2", env=env)
    write(a, "state/state.json", "{}\n")
    sh("bash", str(SCRIPT), "push", str(a), "seed", env=env)

    x, y = tmp_path / "x", tmp_path / "y"
    sh("bash", str(SCRIPT), "checkout", str(x), "2", env=env)
    sh("bash", str(SCRIPT), "checkout", str(y), "2", env=env)
    write(x, f"raw/reddit/{day_dir(0)}/x.jsonl.gz", "x")
    write(y, f"raw/reddit/{day_dir(0)}/y.jsonl.gz", "y")
    sh("bash", str(SCRIPT), "push", str(x), "x", env=env)
    res = sh("bash", str(SCRIPT), "push", str(y), "y", env=env)

    assert "replaying" in res.stdout
    assert remote_file(env, tmp_path, f"raw/reddit/{day_dir(0)}/x.jsonl.gz") == "x"
    assert remote_file(env, tmp_path, f"raw/reddit/{day_dir(0)}/y.jsonl.gz") == "y"


def test_files_written_outside_the_sparse_checkout_are_pushed(env, tmp_path):
    # e.g. a run checked out at 23:59:50 that writes its raw file into the next day's directory
    a = tmp_path / "a"
    sh("bash", str(SCRIPT), "checkout", str(a), "2", env=env)
    write(a, f"raw/reddit/{day_dir(20)}/old.jsonl.gz", "old")
    sh("bash", str(SCRIPT), "push", str(a), "seed", env=env)

    b = tmp_path / "b"
    sh("bash", str(SCRIPT), "checkout", str(b), "2", env=env)
    write(b, f"raw/reddit/{day_dir(-2)}/ahead.jsonl.gz", "ahead")
    sh("bash", str(SCRIPT), "push", str(b), "run", env=env)

    assert remote_file(env, tmp_path, f"raw/reddit/{day_dir(-2)}/ahead.jsonl.gz") == "ahead"
    assert remote_file(env, tmp_path, f"raw/reddit/{day_dir(20)}/old.jsonl.gz") == "old"  # not deleted


def test_checkout_patterns_include_tomorrow(env):
    out = sh("bash", str(SCRIPT), "patterns", "1", env=env).stdout.split()
    assert {f"/raw/reddit/{day_dir(d)}/" for d in (-1, 0, 1)} <= set(out)
    assert f"/raw/reddit/{day_dir(2)}/" not in out


def test_push_with_no_changes_is_a_noop(env, tmp_path):
    a = tmp_path / "a"
    sh("bash", str(SCRIPT), "checkout", str(a), "1", env=env)
    res = sh("bash", str(SCRIPT), "push", str(a), "empty", env=env)
    assert "nothing to commit" in res.stdout


def test_market_checkout_has_what_the_market_job_needs_and_its_push_survives_a_collect_push(env, tmp_path):
    now = datetime.now(timezone.utc)
    universe_now = f"market/universe/{now:%Y/%m/%Y-%m-%d}.csv.gz"
    universe_old = f"market/universe/{now - timedelta(days=40):%Y/%m/%Y-%m-%d}.csv.gz"
    needed = ["candidates/episodes.csv", "ref/symbols.csv", f"daily/mention_counts/{month()}.csv",
              "market/snapshots.csv", "market/state.json", "market/README.md", universe_now]
    not_needed = ["state/state.json", f"raw/reddit/{day_dir(0)}/r.jsonl.gz", f"market/raw/{day_dir(0)}/old.json.gz",
                  universe_old]
    a = tmp_path / "a"
    sh("bash", str(SCRIPT), "checkout", str(a), "2", env=env)
    for rel in needed + not_needed:
        write(a, rel, rel + "\n")
    sh("bash", str(SCRIPT), "push", str(a), "seed", env=env)

    m = tmp_path / "m"
    sh("bash", str(SCRIPT), "checkout-market", str(m), env=env)
    assert [rel for rel in needed if not (m / rel).exists()] == []
    assert [rel for rel in not_needed if (m / rel).exists()] == []

    with open(m / "market/snapshots.csv", "a") as fh:
        fh.write("row\n")
    write(m, f"market/raw/{day_dir(0)}/new.json.gz", "new")

    x = tmp_path / "x"  # a collect run that pushes while the market run is working
    sh("bash", str(SCRIPT), "checkout", str(x), "2", env=env)
    write(x, f"raw/reddit/{day_dir(0)}/x.jsonl.gz", "x")
    sh("bash", str(SCRIPT), "push", str(x), "collect", env=env)

    res = sh("bash", str(SCRIPT), "push", str(m), "market", env=env)
    assert "replaying" in res.stdout
    assert remote_file(env, tmp_path, "market/snapshots.csv") == "market/snapshots.csv\nrow\n"
    assert remote_file(env, tmp_path, f"market/raw/{day_dir(0)}/new.json.gz") == "new"
    assert remote_file(env, tmp_path, f"market/raw/{day_dir(0)}/old.json.gz") == f"market/raw/{day_dir(0)}/old.json.gz\n"
    assert remote_file(env, tmp_path, f"raw/reddit/{day_dir(0)}/x.jsonl.gz") == "x"
    assert remote_file(env, tmp_path, universe_old) == universe_old + "\n"
