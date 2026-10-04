from pumpdump.episodes import update_episodes
from pumpdump.spikes import SpikeResult

H = 3600


def flag(ticker, mentions=12, z=5.0, reasons=("mention_spike",)):
    return SpikeResult(
        ticker=ticker,
        reasons=list(reasons),
        mentions=mentions,
        authors=6,
        baseline_mean=0.0,
        baseline_sd=0.0,
        threshold=0.0,
        z=z,
        hype_docs=0,
        hype_authors=0,
        hype_baseline_mean=0.0,
        hype_threshold=0.0,
    )


def test_first_flag_opens_an_episode():
    episodes = {}
    opened, ended = update_episodes(episodes, [flag("ABCD")], as_of=1000.0, gap=24 * H)
    assert [r.ticker for r in opened] == ["ABCD"]
    assert ended == []
    assert episodes["ABCD"]["first_flagged_at"] == 1000.0
    assert episodes["ABCD"]["n_flags"] == 1


def test_repeat_flag_within_gap_extends_episode_and_tracks_peaks():
    episodes = {}
    update_episodes(episodes, [flag("ABCD", mentions=12, z=5.0)], as_of=1000.0, gap=24 * H)
    opened, ended = update_episodes(
        episodes, [flag("ABCD", mentions=30, z=9.0, reasons=("hype_spike",))], as_of=1000.0 + 23 * H, gap=24 * H
    )
    assert opened == [] and ended == []
    ep = episodes["ABCD"]
    assert ep["first_flagged_at"] == 1000.0
    assert ep["last_flagged_at"] == 1000.0 + 23 * H
    assert (ep["n_flags"], ep["peak_mentions"], ep["peak_z"]) == (2, 30, 9.0)
    assert ep["reasons_seen"] == ["hype_spike", "mention_spike"]


def test_episode_ends_after_gap_without_flags():
    episodes = {}
    update_episodes(episodes, [flag("ABCD")], as_of=1000.0, gap=24 * H)
    opened, ended = update_episodes(episodes, [], as_of=1000.0 + 25 * H, gap=24 * H)
    assert opened == []
    assert [e["ticker"] for e in ended] == ["ABCD"]
    assert ended[0]["ended_at"] == 1000.0 + 25 * H
    assert episodes == {}


def test_flag_after_gap_starts_a_new_episode():
    episodes = {}
    update_episodes(episodes, [flag("ABCD")], as_of=1000.0, gap=24 * H)
    opened, ended = update_episodes(episodes, [flag("ABCD")], as_of=1000.0 + 30 * H, gap=24 * H)
    assert [r.ticker for r in opened] == ["ABCD"]
    assert [e["ticker"] for e in ended] == ["ABCD"]
    assert episodes["ABCD"]["first_flagged_at"] == 1000.0 + 30 * H
    assert episodes["ABCD"]["episode_id"] != ended[0]["episode_id"]


def test_unflagged_results_are_ignored():
    episodes = {}
    opened, _ = update_episodes(episodes, [flag("ABCD", reasons=())], as_of=1000.0, gap=24 * H)
    assert opened == [] and episodes == {}
