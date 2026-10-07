"""Public Telegram channels through their web preview (https://t.me/s/NAME), and rule tg-v1.

No account, no API key, nothing joined: the preview is the page anyone can open in a
browser. It lists a public channel's newest ~20 posts and pages back with ?before=ID.
Rules and reasons: docs/crypto.md.
"""

from __future__ import annotations

import html
import re
from dataclasses import dataclass, field
from datetime import datetime

TG_VERSION = "tg-v1"
PREVIEW = "https://t.me/s/{name}"

_POST = re.compile(r'<div class="tgme_widget_message_wrap.*?(?=<div class="tgme_widget_message_wrap|\Z)', re.S)
_DATA_POST = re.compile(r'data-post="([^"/]+)/(\d+)"')
_TIME = re.compile(r'<time[^>]*datetime="([^"]+)"')
_TEXT = re.compile(r'<div class="tgme_widget_message_text[^"]*"[^>]*>(.*?)</div>', re.S)
_VIEWS = re.compile(r'<span class="tgme_widget_message_views">([^<]+)</span>')
_TITLE = re.compile(r'<div class="tgme_channel_info_header_title"[^>]*>(?:<span[^>]*>)?(.*?)</', re.S)
_DESC = re.compile(r'<div class="tgme_channel_info_description"[^>]*>(.*?)</div>', re.S)
_SUBS = re.compile(r'<span class="counter_value">([^<]+)</span>\s*<span class="counter_type">subscribers?</span>')
_HREF = re.compile(r'href="([^"]+)"')
_TME_LINK = re.compile(r"(?:https?://)?(?:t\.me|telegram\.me)/(?:s/)?([A-Za-z][A-Za-z0-9_]{4,31})(?![A-Za-z0-9_/])")
_NOT_CHANNELS = {"joinchat", "addstickers", "share", "proxy", "iv", "socks", "addlist", "boost", "contact", "login"}


def to_text(fragment: str) -> str:
    """Telegram's message HTML to plain text (line breaks kept, links' visible text kept)."""
    t = re.sub(r"<br\s*/?>", "\n", fragment)
    t = re.sub(r'<i class="emoji"[^>]*><b>(.*?)</b></i>', r"\1", t)
    t = re.sub(r"<[^>]+>", "", t)
    return html.unescape(t).strip()


@dataclass
class Post:
    channel: str
    id: int
    date: str  # ISO 8601 with offset, as Telegram gives it
    text: str
    links: list[str] = field(default_factory=list)
    views: str = ""


@dataclass
class Page:
    status: int
    title: str = ""
    description: str = ""
    subscribers: str = ""
    posts: list[Post] = field(default_factory=list)

    @property
    def public(self) -> bool:
        # a username that is a person, a bot, a private group or nothing gets a page without the channel header
        return self.status == 200 and bool(self.title)


def parse_page(name: str, body: str, status: int = 200) -> Page:
    page = Page(status=status)
    if m := _TITLE.search(body):
        page.title = to_text(m.group(1))
    if m := _DESC.search(body):
        page.description = to_text(m.group(1))
    if m := _SUBS.search(body):
        page.subscribers = m.group(1).strip()
    for block in _POST.findall(body):
        dp = _DATA_POST.search(block)
        tm = _TIME.search(block)
        if not dp or not tm:
            continue
        tx = _TEXT.search(block)
        text = to_text(tx.group(1)) if tx else ""
        links = [html.unescape(h) for h in _HREF.findall(tx.group(1))] if tx else []
        views = _VIEWS.search(block)
        page.posts.append(Post(dp.group(1), int(dp.group(2)), tm.group(1), text, links, views.group(1) if views else ""))
    page.posts.sort(key=lambda p: p.id)
    return page


def channel_links(text: str, links: list[str]) -> set[str]:
    """Public channel usernames a post links to (the papers' snowball)."""
    found = set()
    for src in [text, *links]:
        for m in _TME_LINK.finditer(src):
            name = m.group(1)
            if name.lower() not in _NOT_CHANNELS and not name.lower().endswith("bot"):
                found.add(name)
    return found


# ---- tg-v1 ---------------------------------------------------------------------------------------------------

EXCHANGES = {
    "binance": r"binance",
    "kucoin": r"ku\s?coin",
    "mexc": r"mexc",
    "gate": r"gate(?:\.io|io)?",
    "lbank": r"lbank",
    "xt": r"xt\.com",
    "bitmart": r"bitmart",
    "hotbit": r"hotbit",
    "yobit": r"yobit",
    "poloniex": r"poloniex",
    "htx": r"htx|huobi",
    "bitget": r"bitget",
    "okx": r"okx",
    "bittrex": r"bittrex",
    "cryptopia": r"cryptopia",
    "pancakeswap": r"pancake\s?swap",
    "uniswap": r"uniswap",
    "solana": r"solana|raydium|pump\.fun",
}
_EXCH = [(k, re.compile(rf"(?i)(?<![a-z]){v}(?![a-z])")) for k, v in EXCHANGES.items()]

PUMP_KEYWORDS = re.compile(r"(?i)pump|signal|whale|moon|gem|x100|100x|trading|crypto|coin")

# phrases that name the pump target; the ticker must follow within 40 characters
_ANNOUNCE = re.compile(
    r"(?i)(?:the\s+)?coin\s+(?:we\s+are\s+pumping|we\s+will\s+pump|we\s+pump|we\s+have\s+picked(?:\s+to\s+pump)?|"
    r"for\s+today|to\s+pump|of\s+the\s+day|name)(?:\s+(?:today|tonight|now))?\s*(?:is)?"
    r"|pump(?:ing)?\s+coin(?:\s+name)?"
    r"|\bcoin\s*(?:is\b|=>|->|:|~|=)"
    r"|coin\s+we\s+(?:have\s+)?(?:picked|chosen|selected)(?:\s+[\w']+){0,6}?\s+is"
    r"|coin\s+we\s+are\s+buying\s+is"
    r"|we\s+are\s+pumping|pump\s+alert"
    r"|today'?s\s+coin(?:\s+is)?"
)
# posts that talk about a pump without naming its target now: results, reminders, teasers, cancellations
_NOT_ANNOUNCEMENT = re.compile(
    r"(?i)\b(?:results?|profits?|increase|start\s*:|high\s*:|low\s*:|peak|still|analysis|update|announced|vip|"
    r"reminder|cancel+ed|postponed?|earlier|special|potential|will\s+be|going\s+to\s+be)\b"
)
# a trading call's furniture: entry ranges, stop losses, numbered sell levels
_CALL_SHAPE = re.compile(r"(?i)stop\s*-?\s*loss|\bsl\s*[:=]|buy\s*(?:zone|area|price|range|between)|\bsell\s*[:=@-]|entry\s*(?:zone|price)?\s*[:=]")
_TICKER_AFTER = re.compile(r"[^A-Za-z0-9\n]{0,20}([A-Za-z][A-Za-z0-9]{1,9})\b")
_TRADE_LINK = re.compile(
    r"(?i)(?:/trade/|/exchange/|market=|symbol=|/spot/|/en/trade/)\$?([A-Za-z0-9]{2,10})[_/\-]?(USDT|BTC|ETH|BNB|USDC)\b"
)
_TAGGED = re.compile(r"(?<![A-Za-z0-9])[#$]\s?([A-Za-z][A-Za-z0-9]{1,9})\b")
_PAIR = re.compile(r"\b([A-Z][A-Z0-9]{1,9})\s?/\s?(USDT|BTC|ETH|BNB|USDC)\b")
_COUNTDOWN = re.compile(
    r"(?i)\b\d+\s*(?:minutes?|mins?|hours?|hrs?|h|m)\s*(?:left|remaining|to\s+go|until|before)"
    r"|next\s+(?:post|message)\s+(?:will\s+be|is)\s+the\s+coin|coin\s+(?:will\s+be\s+)?(?:released|announced)\s+in"
)
_BUY = re.compile(r"(?i)\b(?:buy(?:ing)?|entry|accumulat\w*|long)\b")
_TARGET = re.compile(r"(?i)\b(?:targets?|tp\d?|sell(?:ing)?\s*(?:zone|@|:)?)\b")
_NOT_TICKERS = {
    "IS", "THE", "TODAY", "TONIGHT", "NOW", "NAME", "COIN", "BUY", "SELL", "PUMP", "HERE", "AND", "FOR", "OUR", "WILL",
    "BE", "WE", "ARE", "NEXT", "TO", "OF", "ON", "IN", "AT", "IT", "THIS", "THAT", "GET", "READY", "HOLD", "FAST",
    "USDT", "BTC", "ETH", "USD", "BNB", "USDC", "SIGNAL", "SIGNALS", "TARGET", "EXCHANGE", "MARKET", "PROFIT", "VIP",
    "FREE", "LONG", "SHORT", "ENTRY", "STOP", "LOSS", "SL", "TP", "TP1", "TP2", "TP3", "ALL", "DONE", "HIT", "NEW",
    "JOIN", "LINK", "HTTPS", "HTTP", "WWW", "COM", "IO", "EN", "GMT", "UTC", "AM", "PM", "MINUTES", "MIN", "MINS",
    "HOUR", "HOURS", "LEFT", "GUYS", "ALT", "ALTS", "CRYPTO", "TRADE", "TRADING", "LEVERAGE", "CROSS", "SPOT",
    "FUTURES", "PERIOD", "DAYS", "ACHIEVED", "TARGETS", "BREAKOUT", "UPDATE", "NEWS", "CALL", "CALLS", "GEM", "MOON",
    "X", "XX", "OK", "GO", "TEST", "AWESOME", "WITH", "GROWING", "REALLY", "WOW", "THANKS", "SOON", "BIG", "YES", "NO", "PLEASE", "REMEMBER", "HELLO", "EVERYONE", "MEMBERS", "AFTER", "BEFORE", "UP",
}
_LISTED_EXCHANGES = ("mexc", "kucoin", "gate", "binance")


@dataclass
class Classified:
    kind: str  # announcement | call | other
    ticker: str = ""
    quote: str = ""
    exchange: str = ""
    countdown: bool = False


def named_exchange(text: str, links: list[str]) -> str:
    blob = " ".join([text, *links])
    hits = [(m.start(), k) for k, rx in _EXCH for m in [rx.search(blob)] if m]
    return min(hits)[1] if hits else ""


def _ok(tok: str) -> bool:
    return tok.upper() not in _NOT_TICKERS and not tok.isdigit()


def _link_ticker(text: str, links: list[str]) -> tuple[str, str]:
    for src in [*links, text]:
        if m := _TRADE_LINK.search(src):
            return m.group(1).upper(), m.group(2).upper()
    return "", ""


def _bare(text: str) -> str:
    """The ticker of a post that is nothing but a ticker (#XYZ #XYZ, $XYZ, XYZ, XYZ/BTC), else ''."""
    t = re.sub(r"https?://\S+", " ", text)
    t = re.sub(r"[^\w\s/#$]", " ", t)
    toks = [w.strip("#$") for w in t.split()]
    toks = [w for w in toks if w and w.upper() not in {"BUY", "BUY", "NOW", "FAST", "HOLD", "AND", "USDT", "BTC", "ETH"}]
    names = {w.upper().split("/")[0] for w in toks}
    if len(names) == 1 and len(text) <= 60:
        tok = names.pop()
        if re.fullmatch(r"[A-Z][A-Z0-9]{1,9}", tok) and _ok(tok):
            return tok
    return ""


def classify(text: str, links: list[str] | None = None, after_countdown: bool = False) -> Classified:
    """Rule tg-v1 (docs/crypto.md). `after_countdown`: a countdown post came in the 15 minutes before this one."""
    links = links or []
    exch = named_exchange(text, links)
    countdown = bool(_COUNTDOWN.search(text))
    link_tk, link_q = _link_ticker(text, links)

    for m in _ANNOUNCE.finditer(text) if not _NOT_ANNOUNCEMENT.search(text) and not _CALL_SHAPE.search(text) else ():
        tail = text[m.end() : m.end() + 40]
        tok = ""
        if sp := re.match(r"[^A-Za-z0-9\n]{0,20}((?:[(\[\s'\"]*\b[A-Z0-9]\b[)\]\s'\"]*){2,10})", tail):
            tok = re.sub(r"[^A-Z0-9]", "", sp.group(1))
        elif t := _TICKER_AFTER.match(tail):
            tok = t.group(1)
        if tok:
            if len(tok) >= 2 and _ok(tok):
                q = link_q if link_tk == tok.upper() else ""
                if not q and (p := _PAIR.search(text)) and p.group(1) == tok.upper():
                    q = p.group(2)
                return Classified("announcement", tok.upper(), q, exch, countdown)
    if after_countdown and not countdown:
        if link_tk and len(re.sub(r"https?://\S+", "", text).strip()) <= 60:
            return Classified("announcement", link_tk, link_q, exch)
        if tok := _bare(text):
            q = p.group(2) if (p := _PAIR.search(text)) else ""
            return Classified("announcement", tok, q, exch)

    tok, q = "", ""
    if p := _PAIR.search(text):
        tok, q = p.group(1), p.group(2)
    elif link_tk:
        tok, q = link_tk, link_q
    else:
        for m in _TAGGED.finditer(text):
            if _ok(m.group(1)):
                tok = m.group(1).upper()
                break
    if tok and _ok(tok) and _BUY.search(text) and _TARGET.search(text):
        return Classified("call", tok, q, exch, countdown)
    return Classified("other", countdown=countdown)


def classify_channel(posts: list[tuple[float, str, list[str]]], last_countdown_at: float | None = None):
    """Classify one channel's posts in time order: (timestamp, text, links) -> list of Classified.

    Returns the list and the time of the last countdown post (carried between runs).
    """
    out = []
    for ts, text, links in posts:
        after = last_countdown_at is not None and 0 <= ts - last_countdown_at <= 15 * 60
        c = classify(text, links, after)
        if c.countdown:
            last_countdown_at = ts
        out.append(c)
    return out, last_countdown_at


def iso_to_ts(s: str) -> float:
    return datetime.fromisoformat(s.replace("Z", "+00:00")).timestamp()
