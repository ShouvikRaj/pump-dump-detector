"""On-disk datastore (the `data` branch of the repo).

Raw Reddit records are append-only, gzipped JSON lines partitioned by the UTC
date they were *collected*, one file per run (split into `_pNN` parts when huge):

    raw/reddit/YYYY/MM/DD/HHMMSSZ_<run_id>.jsonl.gz

Nothing is ever rewritten, so the files are a log of what the collector knew
and when. Everything else (SQLite, mention counts) is rebuilt from them.
"""

from __future__ import annotations

import csv
import gzip
import io
import json
import os
from datetime import date, datetime, timezone
from pathlib import Path
from typing import Iterable, Iterator

RAW_DIR = Path("raw/reddit")
STATE_FILE = Path("state/state.json")


def utc_dt(ts: float) -> datetime:
    return datetime.fromtimestamp(ts, timezone.utc)


def _atomic_write_bytes(path: Path, data: bytes) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    tmp = path.with_name(path.name + ".tmp")
    tmp.write_bytes(data)
    os.replace(tmp, path)


class Datastore:
    def __init__(self, root: Path | str) -> None:
        self.root = Path(root)

    def path(self, rel: str | Path) -> Path:
        return self.root / rel

    # raw records ---------------------------------------------------------
    def write_raw(
        self, records: list[dict], run_started: float, run_id: str, max_records_per_file: int = 50_000
    ) -> list[Path]:
        """Write one run's records; big runs (the first backfill) are split into `_pNN` parts.

        Parts keep each file far below GitHub's 100 MB limit and sort in write order.
        """
        if not records:
            return []
        dt = utc_dt(run_started)
        stem = f"{dt.strftime('%H%M%S')}Z_{run_id}"
        chunks = [records[i : i + max_records_per_file] for i in range(0, len(records), max_records_per_file)]
        paths = []
        for i, chunk in enumerate(chunks):
            name = f"{stem}.jsonl.gz" if len(chunks) == 1 else f"{stem}_p{i:02d}.jsonl.gz"
            path = self.root / RAW_DIR / dt.strftime("%Y/%m/%d") / name
            buf = io.BytesIO()
            with gzip.GzipFile(fileobj=buf, mode="wb", mtime=0) as gz:
                for r in chunk:
                    gz.write((json.dumps(r, ensure_ascii=False, separators=(",", ":")) + "\n").encode())
            _atomic_write_bytes(path, buf.getvalue())
            paths.append(path)
        return paths

    def raw_files(self, since: float | None = None) -> list[Path]:
        base = self.root / RAW_DIR
        if not base.exists():
            return []
        since_day = utc_dt(since).date() if since is not None else date.min
        files = []
        for day_dir in sorted(base.glob("[0-9][0-9][0-9][0-9]/[0-9][0-9]/[0-9][0-9]")):
            y, m, d = (int(p) for p in day_dir.relative_to(base).parts)
            if date(y, m, d) >= since_day:
                files.extend(sorted(day_dir.glob("*.jsonl.gz")))
        return files

    def iter_raw(self, since: float | None = None) -> Iterator[dict]:
        for path in self.raw_files(since):
            with gzip.open(path, "rt", encoding="utf-8") as fh:
                for line in fh:
                    if line.strip():
                        yield json.loads(line)

    # state -----------------------------------------------------------------
    def load_state(self) -> dict:
        p = self.root / STATE_FILE
        if not p.exists():
            return {"version": 1, "streams": {}, "episodes": {}}
        state = json.loads(p.read_text())
        state.setdefault("streams", {})
        state.setdefault("episodes", {})
        return state

    def save_state(self, state: dict) -> None:
        _atomic_write_bytes(self.root / STATE_FILE, (json.dumps(state, indent=2, sort_keys=True) + "\n").encode())

    # small text / csv outputs ------------------------------------------------
    def append_csv(self, rel: str | Path, fieldnames: list[str], rows: Iterable[dict]) -> None:
        rows = list(rows)
        if not rows:
            return
        p = self.root / rel
        p.parent.mkdir(parents=True, exist_ok=True)
        new = not p.exists() or p.stat().st_size == 0
        with p.open("a", newline="", encoding="utf-8") as fh:
            w = csv.DictWriter(fh, fieldnames=fieldnames, extrasaction="ignore", lineterminator="\n")
            if new:
                w.writeheader()
            w.writerows(rows)

    def write_csv(self, rel: str | Path, fieldnames: list[str], rows: Iterable[dict]) -> None:
        buf = io.StringIO()
        w = csv.DictWriter(buf, fieldnames=fieldnames, extrasaction="ignore", lineterminator="\n")
        w.writeheader()
        w.writerows(rows)
        _atomic_write_bytes(self.root / rel, buf.getvalue().encode())

    def read_csv(self, rel: str | Path) -> list[dict]:
        p = self.root / rel
        if not p.exists():
            return []
        with p.open(newline="", encoding="utf-8") as fh:
            return list(csv.DictReader(fh))

    def write_text(self, rel: str | Path, text: str) -> None:
        _atomic_write_bytes(self.root / rel, text.encode())
