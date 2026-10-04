import pytest

from pumpdump.hype import hype_categories, hype_score, is_hype


@pytest.mark.parametrize(
    "text, expected",
    [
        ("To the moon 🚀🚀", {"moon", "rocket"}),
        ("short squeeze incoming, shorts are trapped", {"squeeze"}),
        ("this could be a 10x easy", {"multibagger"}),
        ("100X potential", {"multibagger"}),
        ("Don't miss this one, load up before it's too late", {"urgency"}),
        ("next GME for sure", {"next_big"}),
        ("about to go parabolic", {"explosive"}),
        ("hidden gem flying under the radar", {"gem"}),
        ("tendies and lambos incoming", {"wealth"}),
        ("💎🙌 hold the line", {"diamond"}),
        ("super low float, only 2M float", {"low_float"}),
        ("PT $5 by friday", {"price_target"}),
        ("price target of $12", {"price_target"}),
        ("🔥📈", {"fire"}),
    ],
)
def test_hype_categories(text, expected):
    assert hype_categories(text) == expected


@pytest.mark.parametrize(
    "text",
    [
        "Q3 revenue grew 5%, guidance unchanged",
        "2x leveraged ETFs decay over time",
        "the moonlight was nice",
        "",
        None,
    ],
)
def test_neutral_text_has_no_hype(text):
    assert hype_categories(text) == set()


def test_categories_are_case_insensitive():
    assert hype_categories("TO THE MOON") == {"moon"}


def test_score_counts_distinct_categories_across_texts():
    assert hype_score("🚀🚀🚀 moon", "short squeeze") == 3


def test_is_hype_needs_two_categories():
    assert not is_hype("🚀")
    assert is_hype("🚀 short squeeze")
