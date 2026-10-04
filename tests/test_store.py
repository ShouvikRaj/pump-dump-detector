import gzip
import json

from pumpdump.store import Datastore

T = 1_791_150_720  # 2026-10-04 21:52:00 UTC
DAY = 86_400


def rec(id_, created, collected):
    return {"id": id_, "kind": "post", "created_utc": created, "collected_at": collected}


def test_raw_file_is_partitioned_by_collection_date_and_gzipped(tmp_path):
    ds = Datastore(tmp_path)
    paths = ds.write_raw([rec("t3_a", T - 100, T)], run_started=T, run_id="123")

    assert paths == [tmp_path / "raw/reddit/2026/10/04/215200Z_123.jsonl.gz"]
    with gzip.open(paths[0], "rt") as fh:
        assert [json.loads(line) for line in fh] == [rec("t3_a", T - 100, T)]


def test_write_raw_with_no_records_writes_nothing(tmp_path):
    assert Datastore(tmp_path).write_raw([], run_started=T, run_id="1") == []
    assert not (tmp_path / "raw").exists()


def test_large_runs_are_split_into_parts_that_read_back_in_order(tmp_path):
    ds = Datastore(tmp_path)
    records = [rec(f"t1_{i}", T - i, T) for i in range(5)]
    paths = ds.write_raw(records, run_started=T, run_id="9", max_records_per_file=2)
    assert [p.name for p in paths] == ["215200Z_9_p00.jsonl.gz", "215200Z_9_p01.jsonl.gz", "215200Z_9_p02.jsonl.gz"]
    assert [r["id"] for r in ds.iter_raw()] == [f"t1_{i}" for i in range(5)]


def test_iter_raw_reads_partitions_on_or_after_since_date(tmp_path):
    ds = Datastore(tmp_path)
    ds.write_raw([rec("old", T - 10 * DAY, T - 10 * DAY)], run_started=T - 10 * DAY, run_id="1")
    ds.write_raw([rec("edge", T - 2 * DAY, T - 2 * DAY)], run_started=T - 2 * DAY, run_id="2")
    ds.write_raw([rec("new", T, T)], run_started=T, run_id="3")

    # since = 2 days ago at 23:59 -> that whole UTC day is still read
    since = T - 2 * DAY + 2 * 3600 + 7 * 60
    assert [r["id"] for r in ds.iter_raw(since=since)] == ["edge", "new"]


def test_state_roundtrip_and_default(tmp_path):
    ds = Datastore(tmp_path)
    assert ds.load_state() == {"version": 1, "streams": {}, "episodes": {}}
    ds.save_state({"version": 1, "streams": {"a/posts": {"cursor": 5}}, "episodes": {}})
    assert Datastore(tmp_path).load_state()["streams"]["a/posts"]["cursor"] == 5


def test_append_csv_writes_header_once(tmp_path):
    ds = Datastore(tmp_path)
    ds.append_csv("logs/x.csv", ["a", "b"], [{"a": 1, "b": 2}])
    ds.append_csv("logs/x.csv", ["a", "b"], [{"a": 3, "b": None}])
    assert (tmp_path / "logs/x.csv").read_text() == "a,b\n1,2\n3,\n"
    assert ds.read_csv("logs/x.csv") == [{"a": "1", "b": "2"}, {"a": "3", "b": ""}]


def test_read_missing_csv_is_empty(tmp_path):
    assert Datastore(tmp_path).read_csv("nope.csv") == []
