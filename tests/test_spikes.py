import math

import pytest

from pumpdump.spikes import SpikeParams, TickerWindow, day_index, evaluate, spike_threshold

DAY = 86_400


def window(counts, authors=None, hype=None, hype_authors=0, ticker="ABCD"):
    return TickerWindow(
        ticker=ticker,
        counts=counts,
        authors=authors if authors is not None else [c for c in counts],
        hype_docs=hype if hype is not None else [0] * len(counts),
        hype_authors_now=hype_authors,
    )


def test_threshold_uses_sample_sd():
    # baseline mean 3, sample sd sqrt(28/6) = 2.1602 > sqrt(3)
    mean, sd, thr = spike_threshold([2, 4, 3, 5, 1, 0, 6], k_sd=2.0)
    assert mean == 3
    assert sd == pytest.approx(2.1602, abs=1e-4)
    assert thr == pytest.approx(7.3205, abs=1e-4)


def test_flat_baseline_falls_back_to_poisson_noise():
    # sd 0 would flag any +1; sqrt(mean) = sqrt(10) keeps the bar at 10 + 2*3.162
    mean, sd, thr = spike_threshold([10] * 7, k_sd=2.0)
    assert sd == pytest.approx(math.sqrt(10))
    assert thr == pytest.approx(16.3246, abs=1e-4)


def test_new_ticker_from_zero_baseline_spikes_when_gates_pass():
    result = evaluate(window([12, 0, 0, 0, 0, 0, 0, 0], authors=[6] + [0] * 7), SpikeParams())
    assert result.reasons == ["mention_spike"]
    assert result.baseline_mean == 0
    assert result.mentions == 12


def test_too_few_distinct_authors_blocks_spike():
    result = evaluate(window([12] + [0] * 7, authors=[4] + [0] * 7), SpikeParams())
    assert result.reasons == []


def test_too_few_mentions_blocks_spike():
    result = evaluate(window([9] + [0] * 7, authors=[9] + [0] * 7), SpikeParams())
    assert result.reasons == []


def test_count_inside_normal_variation_is_not_a_spike():
    assert evaluate(window([13] + [10] * 7), SpikeParams()).reasons == []
    assert evaluate(window([17] + [10] * 7), SpikeParams()).reasons == ["mention_spike"]


def test_threshold_is_strict():
    params = SpikeParams(min_mentions=1, min_authors=1)
    # mean 4, sd floor sqrt(4) = 2 -> threshold exactly 8
    assert evaluate(window([8] + [4] * 7), params).reasons == []
    assert evaluate(window([9] + [4] * 7), params).reasons == ["mention_spike"]


def test_hype_spike_flags_even_without_mention_spike():
    w = window([30] + [28, 30, 25, 33, 29, 31, 30], hype=[6] + [0] * 7, hype_authors=3)
    assert evaluate(w, SpikeParams()).reasons == ["hype_spike"]


def test_hype_spike_needs_distinct_hype_authors():
    w = window([30] + [28, 30, 25, 33, 29, 31, 30], hype=[6] + [0] * 7, hype_authors=2)
    assert evaluate(w, SpikeParams()).reasons == []


def test_both_reasons_can_fire():
    w = window([20] + [0] * 7, hype=[8] + [0] * 7, hype_authors=5)
    assert evaluate(w, SpikeParams()).reasons == ["mention_spike", "hype_spike"]


def test_z_score_uses_effective_sd_with_floor_of_one():
    assert evaluate(window([12] + [0] * 7), SpikeParams()).z == 12.0
    assert evaluate(window([17] + [10] * 7), SpikeParams()).z == pytest.approx((17 - 10) / math.sqrt(10))


@pytest.mark.parametrize(
    "created, expected",
    [
        (1_000_000, 0),  # exactly at as_of
        (1_000_000 - DAY + 1, 0),
        (1_000_000 - DAY, 1),  # (T-48h, T-24h] is day 1
        (1_000_000 - 7 * DAY - 1, 7),
        (1_000_000 - 8 * DAY, None),  # outside the 8-day window
        (1_000_001, None),  # after as_of: never visible
    ],
)
def test_day_index(created, expected):
    assert day_index(created, as_of=1_000_000, n_days=8) == expected
