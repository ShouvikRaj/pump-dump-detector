import pytest

from pumpdump.tickers import Mention, TickerExtractor, default_extractor

UNIVERSE = {"GME", "AMC", "PUMP", "CEO", "EPS", "BB", "BRK.B", "NVDA", "SOFI", "MULN", "BTC", "ON"}
COMMON_WORDS = {"pump", "on", "the", "moon", "it"}
ACRONYMS = {"CEO", "EPS", "DD"}
CASHTAG_BLOCK = {"BTC", "ETH", "USD"}


@pytest.fixture
def ext():
    return TickerExtractor(
        universe=UNIVERSE,
        common_words=COMMON_WORDS,
        acronyms=ACRONYMS,
        cashtag_block=CASHTAG_BLOCK,
    )


def tickers(mentions):
    return [(m.ticker, m.method, m.in_universe) for m in mentions]


def test_cashtag_in_universe(ext):
    assert tickers(ext.extract("$GME to the moon")) == [("GME", "cashtag", True)]


def test_lowercase_cashtag_is_normalised(ext):
    assert tickers(ext.extract("loading $gme today")) == [("GME", "cashtag", True)]


def test_unknown_cashtag_kept_but_marked_outside_universe(ext):
    # OTC pinks that don't file with the SEC are missing from symbol lists
    assert tickers(ext.extract("$ABCD is the next runner")) == [("ABCD", "cashtag", False)]


def test_unknown_two_letter_cashtag_dropped(ext):
    assert ext.extract("$XY looks fun") == []


def test_crypto_cashtag_dropped_when_not_listed(ext):
    assert ext.extract("$ETH and $USD pairs") == []


def test_blocked_cashtag_kept_when_it_is_a_listed_symbol(ext):
    assert tickers(ext.extract("$BTC etf flows")) == [("BTC", "cashtag", True)]


def test_dollar_amounts_are_not_tickers(ext):
    assert ext.extract("went from $5 to $10.50 in a day") == []


def test_bare_uppercase_symbol_in_universe(ext):
    assert tickers(ext.extract("Loaded AMC calls")) == [("AMC", "bare", True)]


def test_bare_common_word_needs_cashtag(ext):
    assert ext.extract("PUMP IT") == []
    assert tickers(ext.extract("$PUMP is cheap")) == [("PUMP", "cashtag", True)]


def test_bare_acronym_is_ignored(ext):
    assert ext.extract("CEO says EPS beat") == []


def test_bare_token_outside_universe_is_ignored(ext):
    assert ext.extract("ZZZZ is great") == []


def test_lowercase_bare_word_is_not_a_ticker(ext):
    assert ext.extract("amc and gme") == []


def test_two_letter_bare_token_needs_cashtag(ext):
    assert ext.extract("BB earnings") == []
    assert tickers(ext.extract("$BB earnings")) == [("BB", "cashtag", True)]


def test_us_exchange_prefix_counts_even_outside_universe(ext):
    assert tickers(ext.extract("Acme Corp (NASDAQ: ACME) jumps")) == [("ACME", "exchange", False)]
    assert tickers(ext.extract("OTC:ABCDF filed today")) == [("ABCDF", "exchange", False)]
    assert tickers(ext.extract("listed on OTCQB: XYZW")) == [("XYZW", "exchange", False)]


def test_foreign_exchange_prefix_is_kept_apart_from_us_tickers(ext):
    assert tickers(ext.extract("Miner (TSXV: GME) drills")) == [("TSXV:GME", "exchange", False)]


def test_exchange_prefix_requires_uppercase_symbol(ext):
    assert ext.extract("the nyse: it was closed") == []


def test_one_mention_per_ticker_keeps_strongest_method(ext):
    assert tickers(ext.extract("GME GME $GME (NYSE: GME)")) == [("GME", "exchange", True)]


def test_urls_and_reddit_refs_are_ignored(ext):
    assert ext.extract("see https://example.com/AMC/GME and r/GME u/AMC") == []


def test_markdown_link_text_counts_but_target_does_not(ext):
    assert tickers(ext.extract("[AMC news](https://x.com/GME)")) == [("AMC", "bare", True)]


def test_class_share_cashtag(ext):
    assert tickers(ext.extract("$BRK.B is boring")) == [("BRK.B", "cashtag", True)]


def test_sentence_punctuation_and_possessives(ext):
    assert tickers(ext.extract("I like $GME. AMC's float is big")) == [
        ("AMC", "bare", True),
        ("GME", "cashtag", True),
    ]


def test_plural_acronym_is_not_a_ticker(ext):
    assert ext.extract("NVDAs and ETFs") == []


def test_html_entities_are_decoded(ext):
    assert tickers(ext.extract("&gt; &#36;MULN &amp; SOFI")) == [("MULN", "cashtag", True), ("SOFI", "bare", True)]


def test_extract_combines_title_and_body(ext):
    assert tickers(ext.extract("NVDA dd", "also $AMC")) == [("AMC", "cashtag", True), ("NVDA", "bare", True)]


def test_none_text_is_ignored(ext):
    assert ext.extract(None, "") == []


def test_mention_is_hashable_value():
    assert Mention("GME", "cashtag", True) == Mention("GME", "cashtag", True)


def test_default_extractor_loads_packaged_word_lists():
    ext = default_extractor(universe={"PUMP", "AMC", "IMO"})
    assert ext.extract("PUMP AMC IMO") == [Mention("AMC", "bare", True)]


def test_hyphenated_compound_is_not_a_bare_ticker():
    # "GLP-1" drugs and "GPT-5" models were the top false matches in the first live data
    ext = TickerExtractor(universe={"GLP", "GPT", "DRTS"}, common_words=(), acronyms=(), cashtag_block=())
    assert tickers(ext.extract("GLP-1 drugs, GPT-5 says DRTS - cancer play")) == [("DRTS", "bare", True)]


def test_common_word_on_bare_allowlist_counts():
    ext = TickerExtractor(
        universe={"SPY", "NOW"}, common_words={"spy", "now"}, acronyms=(), cashtag_block=(), bare_allow={"SPY"}
    )
    assert tickers(ext.extract("SPY puts NOW")) == [("SPY", "bare", True)]


def test_default_extractor_skips_reddit_slang_that_collides_with_listed_symbols():
    slang = "TACO MAGA GPT DRAM HBM HYSA WTI DOW DEI YALL RTH ODTE AINT BYD WEN ADP".split()
    ext = default_extractor(universe=set(slang) | {"SPY", "HOOD", "APP", "DRTS"})
    text = " ".join(slang) + " but SPY calls, HOOD, APP and DRTS"
    assert [m.ticker for m in ext.extract(text)] == ["APP", "DRTS", "HOOD", "SPY"]
    assert ext.extract("$TACO") == [Mention("TACO", "cashtag", True)]


def test_default_extractor_skips_finance_terms_that_became_listed_symbols_with_the_sec_list():
    # tickers-v3: SEC's list (loading since 2026-10-05) added OTC/SPAC symbols that on Reddit are finance jargon
    terms = "COLA EMI ACAT".split()
    ext = default_extractor(universe=set(terms) | {"FNMA", "BLGO"})
    text = "my COLA raise, the EMI on my loan, an ACAT transfer, then FNMA and BLGO"
    assert [m.ticker for m in ext.extract(text)] == ["BLGO", "FNMA"]
    assert ext.extract("$COLA") == [Mention("COLA", "cashtag", True)]


def test_report_names_count_bare_outside_wallstreetbets_only():
    # tickers-v4: on r/wallstreetbets a bare "PMI" is the ISM/S&P index; on r/pennystocks it is Picard Medical
    ext = TickerExtractor(
        universe={"PMI", "AMC"}, common_words=(), acronyms=(), cashtag_block=(), wsb_acronyms={"PMI"}
    )
    assert tickers(ext.extract("Services PMI came in hot, AMC", subreddit="wallstreetbets")) == [("AMC", "bare", True)]
    assert tickers(ext.extract("PMI in 2 min", subreddit="WallStreetBets")) == []
    assert tickers(ext.extract("$PMI", subreddit="wallstreetbets")) == [("PMI", "cashtag", True)]
    assert tickers(ext.extract("PMI just got halted", subreddit="pennystocks")) == [("PMI", "bare", True)]
    assert tickers(ext.extract("PMI just got halted")) == [("PMI", "bare", True)]


def test_default_extractor_reads_pmi_on_wallstreetbets_as_the_economic_index():
    ext = default_extractor(universe={"PMI"})
    assert ext.extract("ISM PMI in 2 min", subreddit="wallstreetbets") == []
    assert ext.extract("Who is with me on PMI", subreddit="pennystocks") == [Mention("PMI", "bare", True)]
