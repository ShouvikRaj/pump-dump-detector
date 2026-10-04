"""Mention-spike rule (Renault 2017, adapted to Reddit).

For a ticker at evaluation time T, day 0 is the trailing 24 hours (T-24h, T]
and days 1..7 are the seven 24-hour windows before it. A ticker spikes when

    mentions_day0 > mean(days 1..7) + k_sd * sd_eff
    and mentions_day0 >= min_mentions and distinct_authors_day0 >= min_authors

Renault used k_sd = 2 with at least 20 messages from 20 users on Twitter. Our
three subreddits are much quieter, so the gates are 10 mentions from 5 authors.

sd_eff = max(sample sd, sqrt(mean)): a perfectly flat baseline (sd 0) would
otherwise flag a ticker going from 10 to 11 mentions, so the sd is floored at
the Poisson noise of a count with that mean. A ticker never mentioned before
has mean 0 and sd_eff 0, so only the gates decide.

The same test runs on "hype documents" (2+ hype categories, see hype.py) to
catch sudden promotional language even when total chatter is steady.
"""

from __future__ import annotations

import math
import statistics
from dataclasses import dataclass, field
from typing import Sequence

DETECTOR_VERSION = "spikes-v1"
DAY = 86_400


@dataclass(frozen=True)
class SpikeParams:
    baseline_days: int = 7
    k_sd: float = 2.0
    min_mentions: int = 10
    min_authors: int = 5
    min_hype_docs: int = 5
    min_hype_authors: int = 3


@dataclass
class TickerWindow:
    """Daily counts for one ticker: index 0 is the trailing 24h, 1..7 the baseline."""

    ticker: str
    counts: list[int]
    authors: list[int]
    hype_docs: list[int]
    hype_authors_now: int


@dataclass
class SpikeResult:
    ticker: str
    reasons: list[str]
    mentions: int
    authors: int
    baseline_mean: float
    baseline_sd: float
    threshold: float
    z: float
    hype_docs: int
    hype_authors: int
    hype_baseline_mean: float
    hype_threshold: float
    extra: dict = field(default_factory=dict)


def spike_threshold(baseline: Sequence[int], k_sd: float) -> tuple[float, float, float]:
    mean = statistics.fmean(baseline)
    sd = statistics.stdev(baseline) if len(baseline) > 1 else 0.0
    sd_eff = max(sd, math.sqrt(mean))
    return mean, sd_eff, mean + k_sd * sd_eff


def day_index(created_utc: float, as_of: float, n_days: int) -> int | None:
    if created_utc > as_of:
        return None
    idx = int((as_of - created_utc) // DAY)
    return idx if idx < n_days else None


def evaluate(w: TickerWindow, p: SpikeParams) -> SpikeResult:
    base = slice(1, 1 + p.baseline_days)
    mean, sd_eff, thr = spike_threshold(w.counts[base], p.k_sd)
    h_mean, _h_sd, h_thr = spike_threshold(w.hype_docs[base], p.k_sd)

    reasons = []
    if w.counts[0] > thr and w.counts[0] >= p.min_mentions and w.authors[0] >= p.min_authors:
        reasons.append("mention_spike")
    if w.hype_docs[0] > h_thr and w.hype_docs[0] >= p.min_hype_docs and w.hype_authors_now >= p.min_hype_authors:
        reasons.append("hype_spike")

    return SpikeResult(
        ticker=w.ticker,
        reasons=reasons,
        mentions=w.counts[0],
        authors=w.authors[0],
        baseline_mean=mean,
        baseline_sd=sd_eff,
        threshold=thr,
        z=(w.counts[0] - mean) / max(sd_eff, 1.0),
        hype_docs=w.hype_docs[0],
        hype_authors=w.hype_authors_now,
        hype_baseline_mean=h_mean,
        hype_threshold=h_thr,
    )
