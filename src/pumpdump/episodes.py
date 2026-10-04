"""Group repeated flags of a ticker into episodes.

A spiking ticker is flagged again on every run while it stays hot. The first
flag opens an episode (that row is the candidate, timestamped when we first
knew); later flags within `gap` seconds extend it; `gap` seconds without a
flag close it.
"""

from __future__ import annotations

from datetime import datetime, timezone

from .spikes import SpikeResult


def _episode_id(ticker: str, ts: float) -> str:
    return f"{ticker}-{datetime.fromtimestamp(ts, timezone.utc).strftime('%Y%m%dT%H%M%SZ')}"


def update_episodes(
    episodes: dict, results: list[SpikeResult], as_of: float, gap: float
) -> tuple[list[SpikeResult], list[dict]]:
    """Mutates `episodes` (ticker -> state). Returns (newly opened results, closed episodes)."""
    opened: list[SpikeResult] = []
    ended: list[dict] = []
    flagged = {r.ticker: r for r in results if r.reasons}

    for ticker in sorted(episodes):
        ep = episodes[ticker]
        if as_of - ep["last_flagged_at"] > gap:
            ended.append({**ep, "ticker": ticker, "ended_at": as_of})
            del episodes[ticker]

    for ticker, r in sorted(flagged.items()):
        ep = episodes.get(ticker)
        if ep is None:
            episodes[ticker] = {
                "episode_id": _episode_id(ticker, as_of),
                "first_flagged_at": as_of,
                "last_flagged_at": as_of,
                "n_flags": 1,
                "peak_mentions": r.mentions,
                "peak_z": round(r.z, 3),
                "reasons_seen": sorted(r.reasons),
            }
            opened.append(r)
        else:
            ep["last_flagged_at"] = as_of
            ep["n_flags"] += 1
            ep["peak_mentions"] = max(ep["peak_mentions"], r.mentions)
            ep["peak_z"] = max(ep["peak_z"], round(r.z, 3))
            ep["reasons_seen"] = sorted(set(ep["reasons_seen"]) | set(r.reasons))
    return opened, ended
