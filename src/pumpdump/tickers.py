"""Find stock ticker mentions in Reddit text.

Follows Nam & Skillicorn (2025): regex candidates checked against exchange
symbol lists. Three ways a ticker can be mentioned, strongest first:

  exchange  "NASDAQ: ABCD", "(OTC: ABCDF)"  - counts even if not in the symbol
            list (non-reporting OTC pinks are missing from SEC/Nasdaq lists).
            Non-US exchanges are kept as "TSXV:ABC" so they never mix with US
            tickers.
  cashtag   "$ABCD"  - counts if listed, or if unlisted with 3+ letters and not
            a currency/crypto coin.
  bare      "ABCD"   - must be ALL CAPS, 3-5 letters, listed, and not a common
            English word or finance acronym (so "PUMP", "MOON", "CEO" don't
            count unless written as cashtags).

Each document yields at most one Mention per ticker (strongest method wins).
"""

from __future__ import annotations

import html
import re
from dataclasses import dataclass
from functools import lru_cache
from importlib import resources
from typing import Collection, Iterable

EXTRACTOR_VERSION = "tickers-v1"

_STRENGTH = {"exchange": 3, "cashtag": 2, "bare": 1}

_US_EXCHANGES = (
    r"NASDAQ|NYSE\s?AMERICAN|NYSEAMERICAN|NYSE\s?ARCA|NYSEARCA|NYSE|AMEX|"
    r"OTCQB|OTCQX|OTCMKTS|OTC\s?PINK|OTCPINK|OTC|PINK|CBOE"
)
_FOREIGN_EXCHANGES = r"TSXV|TSX-V|TSX|CSE|NEO|ASX|LSE|AIM|FRA|FSE|XETRA|LON|ETR"
_FOREIGN_RE = re.compile(rf"^(?:{_FOREIGN_EXCHANGES})$", re.IGNORECASE)

# Exchange names are case-insensitive, the symbol after the colon must be caps.
_EXCHANGE_RE = re.compile(
    rf"(?<![A-Za-z0-9])(?i:({_US_EXCHANGES}|{_FOREIGN_EXCHANGES}))\s*:\s*\$?([A-Z]{{1,5}})(?:\.([A-Z]))?(?![A-Za-z0-9])"
)
_CASHTAG_RE = re.compile(r"(?<![\w$])\$([A-Za-z]{1,5})(?:\.([A-Za-z]))?(?![A-Za-z0-9])")
_BARE_RE = re.compile(r"(?<![A-Za-z0-9$#@._-])([A-Z]{3,5})(?![A-Za-z0-9_])")

_URL_RE = re.compile(r"(?:https?://|www\.)\S+", re.IGNORECASE)
_MD_LINK_TARGET_RE = re.compile(r"\]\([^)\s]*\)")
_REDDIT_REF_RE = re.compile(r"(?<![A-Za-z0-9])/?[ru]/[A-Za-z0-9_-]+")


@dataclass(frozen=True, order=True)
class Mention:
    ticker: str
    method: str
    in_universe: bool


def clean_text(text: str) -> str:
    """Decode HTML entities and drop URLs, markdown link targets and r/ u/ refs."""
    text = html.unescape(text)
    text = _MD_LINK_TARGET_RE.sub("]", text)
    text = _URL_RE.sub(" ", text)
    return _REDDIT_REF_RE.sub(" ", text)


class TickerExtractor:
    def __init__(
        self,
        universe: Collection[str],
        common_words: Collection[str],
        acronyms: Collection[str],
        cashtag_block: Collection[str],
    ) -> None:
        self.universe = frozenset(s.upper() for s in universe)
        self.common_words = frozenset(w.lower() for w in common_words)
        self.acronyms = frozenset(a.upper() for a in acronyms)
        self.cashtag_block = frozenset(c.upper() for c in cashtag_block)

    def _with_class(self, base: str, cls: str | None) -> str:
        if cls:
            candidate = f"{base}.{cls.upper()}"
            if candidate in self.universe:
                return candidate
        return base

    def extract(self, *texts: str | None) -> list[Mention]:
        text = clean_text("\n".join(t for t in texts if t))
        found: dict[str, Mention] = {}

        def add(m: Mention) -> None:
            old = found.get(m.ticker)
            if old is None or _STRENGTH[m.method] > _STRENGTH[old.method]:
                found[m.ticker] = m

        def take_exchange(match: re.Match) -> str:
            exch, sym, cls = match.groups()
            if _FOREIGN_RE.match(exch):
                add(Mention(f"{exch.upper().replace('-', '')}:{sym}", "exchange", False))
            else:
                ticker = self._with_class(sym, cls)
                add(Mention(ticker, "exchange", ticker in self.universe))
            return " "  # consumed, so the symbol isn't re-read as a bare token

        text = _EXCHANGE_RE.sub(take_exchange, text)

        for sym, cls in _CASHTAG_RE.findall(text):
            ticker = self._with_class(sym.upper(), cls)
            if ticker in self.universe:
                add(Mention(ticker, "cashtag", True))
            elif len(ticker) >= 3 and ticker not in self.cashtag_block:
                add(Mention(ticker, "cashtag", False))

        for sym in _BARE_RE.findall(text):
            if sym in self.universe and sym.lower() not in self.common_words and sym not in self.acronyms:
                add(Mention(sym, "bare", True))

        return sorted(found.values())


def _read_wordlist(name: str) -> list[str]:
    raw = resources.files("pumpdump.data").joinpath(name).read_text()
    return [line.strip() for line in raw.splitlines() if line.strip() and not line.startswith("#")]


@lru_cache(maxsize=None)
def packaged_wordlists() -> tuple[tuple[str, ...], tuple[str, ...], tuple[str, ...]]:
    return (
        tuple(_read_wordlist("common_words.txt")),
        tuple(_read_wordlist("acronyms.txt")),
        tuple(_read_wordlist("cashtag_block.txt")),
    )


def default_extractor(universe: Iterable[str]) -> TickerExtractor:
    common, acronyms, block = packaged_wordlists()
    return TickerExtractor(universe=set(universe), common_words=common, acronyms=acronyms, cashtag_block=block)
