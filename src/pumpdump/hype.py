"""Lexicon of promotional "hype" language.

Stage 1 stand-in for the LLM classifier planned for later stages: a document's
hype score is the number of distinct categories below that it uses. One rocket
emoji is everyday WSB noise, so a document counts as hype at 2+ categories.
"""

from __future__ import annotations

import re

HYPE_VERSION = "hype-v1"
MIN_HYPE_CATEGORIES = 2

_I = re.IGNORECASE

CATEGORIES: dict[str, re.Pattern[str]] = {
    "moon": re.compile(r"\bmoon(?:ing|shot|s)?\b|\bto the moon\b|🌙|🌕", _I),
    "rocket": re.compile(r"🚀|\brocket(?:s|ing)?\b", _I),
    "squeeze": re.compile(
        r"\b(?:short|gamma)\s+squeeze\b|\bsqueez(?:e|ing)\b|\bshorts?\s+(?:are\s+)?(?:trapped|burning|covering|r\s+fuk)\b",
        _I,
    ),
    "multibagger": re.compile(r"\b(?:[5-9]|[1-9]\d{1,3})\s?x\b|\b(?:ten|hundred|multi)[\s-]?bagger\b", _I),
    "urgency": re.compile(
        r"\bdon'?t\s+miss\b|\blast\s+chance\b|\bbefore\s+it'?s\s+too\s+late\b|\bact\s+fast\b|\bget\s+in\s+(?:now|early)\b"
        r"|\bbuy\s+now\b|\bload(?:ing)?\s+up\b|\bloaded\s+up\b|\bit'?s\s+happening\b"
        r"|\babout\s+to\s+(?:explode|blow|pop|rip|run|moon)\b|\beasy\s+money\b",
        _I,
    ),
    "next_big": re.compile(r"\bnext\s+(?:gme|amc|tesla|tsla|nvda|nvidia|big\s+thing|runner|10\s?bagger)\b", _I),
    "explosive": re.compile(
        r"\bexplod(?:e|es|ing)\b|\bexplosive\b|\bparabolic\b|\bskyrocket(?:s|ing)?\b|\brip(?:ping)?\s+(?:higher|hard)\b",
        _I,
    ),
    "gem": re.compile(r"\bhidden\s+gem\b|\bgem\b|\bsleeping\s+giant\b|\bunder\s+the\s+radar\b|\bground\s+floor\b", _I),
    "wealth": re.compile(r"\blambos?\b|\btendies\b|\bmillionaires?\b|\blife[\s-]changing\b|💰|🤑|💸", _I),
    "diamond": re.compile(r"💎|🙌|\bdiamond\s+hands?\b|\bhold\s+the\s+line\b|\bhodl\b", _I),
    "low_float": re.compile(r"\blow\s+float\b|\btiny\s+float\b|\bfloat\s+(?:is\s+)?(?:only|tiny|small)\b", _I),
    "price_target": re.compile(r"\b(?:pt|price\s+target)\s*(?:of\s*)?\$\s?\d", _I),
    "fire": re.compile(r"🔥|📈"),
}


def hype_categories(*texts: str | None) -> set[str]:
    text = "\n".join(t for t in texts if t)
    if not text:
        return set()
    return {name for name, pattern in CATEGORIES.items() if pattern.search(text)}


def hype_score(*texts: str | None) -> int:
    return len(hype_categories(*texts))


def is_hype(*texts: str | None) -> bool:
    return hype_score(*texts) >= MIN_HYPE_CATEGORIES
