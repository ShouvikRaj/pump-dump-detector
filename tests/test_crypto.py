import gzip
import json
from datetime import datetime, timezone

from pumpdump.crypto import rules, telegram as tg
from pumpdump.crypto.exchanges import HOUR, MIN, ExchangeError
from pumpdump.crypto.history import merge
from pumpdump.crypto.run import run_crypto
from pumpdump.store import Datastore


def ms(s):
    return int(datetime.fromisoformat(s).replace(tzinfo=timezone.utc).timestamp() * 1000)


# ---- tg-v1 -------------------------------------------------------------------------------------------------------

def test_classify_announcements_and_calls():
    a = tg.classify("The Coin We Are Pumping Today is : STRIKE Target is 300-700% https://www.kucoin.com/trade/STRIKE-USDT")
    assert (a.kind, a.ticker, a.quote, a.exchange) == ("announcement", "STRIKE", "USDT", "kucoin")
    assert tg.classify("COIN IS : 👉🏻 LBP 👈🏻 BUY BUY BUY").ticker == "LBP"
    assert tg.classify("The coin we picked today is :  👉  A P P C   👈").ticker == "APPC"
    assert tg.classify("Pump coin name : #evx").ticker == "EVX"
    # results, teasers and reminders name no target
    assert tg.classify("📈 RESULTS\nCoin: ABC\nIncrease: +128%").kind == "other"
    assert tg.classify("🚀 5 Hour left for the BINANCE pump🚀 To know the coin name earlier").kind == "other"
    c = tg.classify("📢 Coin:  #LINA / BTC\n🔓 Buy zone :104-110\n🚀 Sell :118-130-145\nStop Loss- 97")
    assert (c.kind, c.ticker) == ("call", "LINA")
    assert tg.classify("Good morning everyone").kind == "other"


def test_bare_ticker_counts_only_after_a_countdown():
    posts = [(0, "5 minutes left! Next post will be the coin", []), (300, "#NEBL #NEBL", []), (7200, "#NEBL", [])]
    out, last = tg.classify_channel(posts)
    assert [c.kind for c in out] == ["other", "announcement", "other"]
    assert out[1].ticker == "NEBL" and last == 0


PAGE = """
<div class="tgme_channel_info_header_title"><span dir="auto">Mexc Pump</span></div>
<div class="tgme_channel_info_description">Biggest pumps</div>
<span class="counter_value">12.3K</span> <span class="counter_type">subscribers</span>
<div class="tgme_widget_message_wrap js-widget_message_wrap"><div class="tgme_widget_message" data-post="mexcpump/41">
<div class="tgme_widget_message_text js-message_text" dir="auto">10 minutes left<br/>join t.me/otherpumps</div>
<span class="tgme_widget_message_views">5K</span><time datetime="2026-10-02T16:50:00+00:00" class="time">16:50</time></div></div>
<div class="tgme_widget_message_wrap js-widget_message_wrap"><div class="tgme_widget_message" data-post="mexcpump/42">
<div class="tgme_widget_message_text js-message_text" dir="auto">The coin we are pumping today is: <b>$ABCD</b> <a href="https://www.mexc.com/exchange/ABCD_USDT">mexc</a></div>
<time datetime="2026-10-02T17:00:03+00:00" class="time">17:00</time></div></div>
"""


def test_parse_page():
    p = tg.parse_page("mexcpump", PAGE)
    assert p.public and p.title == "Mexc Pump" and p.subscribers == "12.3K"
    assert [x.id for x in p.posts] == [41, 42]
    assert p.posts[0].text == "10 minutes left\njoin t.me/otherpumps"
    assert tg.channel_links(p.posts[0].text, p.posts[0].links) == {"otherpumps"}
    c = tg.classify(p.posts[1].text, p.posts[1].links)
    assert (c.kind, c.ticker, c.exchange) == ("announcement", "ABCD", "mexc")


# ---- scan-v1 and crypto-label-v1 -----------------------------------------------------------------------------------

def hours(start, closes, qv=200.0, spike_at=None, spike_high=None, spike_qv=None):
    out = []
    for i, c in enumerate(closes):
        t = start + i * HOUR
        hi = spike_high if t == spike_at else c * 1.01
        out.append([t, c, hi, c * 0.99, c, 1.0, spike_qv if t == spike_at else qv])
    return out


def test_scan_flags():
    t0 = ms("2026-10-07T00:00:00") + 30 * HOUR
    bars = hours(ms("2026-10-07T00:00:00"), [1.0] * 40, spike_at=t0, spike_high=1.25, spike_qv=20_000)
    flags = rules.scan_flags(bars, None, None)
    assert [f["t0"] for f in flags] == [t0] and flags[0]["spike"] == 0.25 and flags[0]["vol_ratio"] == 100
    assert rules.scan_flags(bars, None, t0 - 10 * HOUR) == []  # inside the 72 h episode
    small = hours(ms("2026-10-07T00:00:00"), [1.0] * 40, spike_at=t0, spike_high=1.25, spike_qv=9_000)
    assert rules.scan_flags(small, None, None) == []
    assert rules.excluded("BTC3L") and rules.excluded("USDC") and rules.excluded("MSFTON") and rules.excluded("AAPLX")
    assert not rules.excluded("PEPE") and not rules.excluded("TON")


def minutes(start, prices):
    return [[start + i * MIN, p, p, p, p, 1.0, 100.0] for i, p in enumerate(prices)]


def test_label_pump_and_dump_announcement():
    t0 = ms("2026-10-02T17:00:03")
    base = t0 - t0 % MIN
    m = minutes(base - 60 * MIN, [1.0] * 60 + [1.0, 1.1, 1.5, 1.4, 1.2] + [1.05] * 235)
    h = hours(base - 48 * HOUR - 0, [1.0] * 48 + [1.05] * 4 + [0.55] * (7 * 24))
    o = rules.outcomes("announcement", t0, m, h, final=True)
    # the price 2 minutes after a post at 17:00:03 is the close of the 17:02 bar (the boundary at 17:03)
    assert o["status"] == "settled" and o["p0"] == 1.0 and o["p_entry"] == 1.5
    assert o["peak_ret_1h"] == 0.5 and o["minutes_to_peak"] == 1.9 and o["pump"] == 1 and o["pump_dump"] == 1
    assert o["crash_7d"] == 1 and o["ret_entry_1h"] == round(1.05 / 1.5 - 1, 6)


def test_label_quiet_coin_and_pending():
    t0 = ms("2026-10-02T17:00:00")
    m = minutes(t0 - 60 * MIN, [2.0] * 300)
    o = rules.outcomes("call", t0, m, [], final=False)
    assert o["status"] == "pending" and o["pump"] == 0 and o["pump_dump"] == 0 and o["crash_7d"] == ""
    assert rules.outcomes("call", t0, [], [], final=True)["status"] == "no_data"


# ---- history merge ---------------------------------------------------------------------------------------------------

def test_history_merge_prefers_exact_times():
    t = datetime(2019, 7, 25, 18, 0, 4, tzinfo=timezone.utc)
    items = [
        dict(list="pumpsense", exchange="binance", base="APPC", quote="BTC", t=t.replace(second=4), channel="BPG",
             text="Coin is APPC", time_source="pumpsense_minus_2h"),
        dict(list="lamorgia", exchange="binance", base="APPC", quote="BTC", t=t.replace(second=0), channel="BPG",
             text="", time_source="lamorgia_gmt"),
        dict(list="lamorgia", exchange="yobit", base="APPC", quote="BTC", t=t, channel="X", text="", time_source="lamorgia_gmt"),
    ]
    ev = merge(items)
    assert len(ev) == 2
    b = next(e for e in ev if e["exchange"] == "binance")
    assert b["list"] == "lamorgia+pumpsense" and b["time_source"] == "lamorgia_gmt" and b["text"] == "Coin is APPC"


# ---- one end-to-end run with fake exchanges and a fake Telegram ----------------------------------------------------------

class FakeHttp:
    def __init__(self, now_ms):
        self.now = now_ms
        self.calls = []

    def get(self, url, params=None, timeout=30):
        self.calls.append(url)
        if url.startswith("https://t.me/s/mexcpumpcoins"):
            return 200, PAGE.replace("mexcpump/", "mexcpumpcoins/").encode()
        if url.startswith("https://t.me/s/otherpumps"):
            return 200, b'<div class="tgme_channel_info_header_title"><span>Other Pumps</span></div>'
        if url.startswith("https://t.me/s/"):
            return 200, b"<html>no channel</html>"
        return 404, b""

    def json(self, url, params=None):
        self.calls.append(url)
        if "mexc.com/api/v3/ticker" in url:
            return [{"symbol": "ABCDUSDT", "highPrice": "1.3", "lowPrice": "1.0", "lastPrice": "1.1", "quoteVolume": "9e5"},
                    {"symbol": "FLATUSDT", "highPrice": "1.0", "lowPrice": "1.0", "lastPrice": "1.0", "quoteVolume": "9e5"}]
        if "mexc.com/api/v3/klines" in url:
            last = self.now - self.now % HOUR - HOUR
            start = last - 47 * HOUR
            spike_at = last - 2 * HOUR
            rows = hours(start, [1.0] * 48, spike_at=spike_at, spike_high=1.3, spike_qv=50_000)
            return [[b[0], str(b[1]), str(b[2]), str(b[3]), str(b[4]), "1", b[0] + HOUR - 1, str(b[6])] for b in rows
                    if params["startTime"] <= b[0] <= params["endTime"]]
        raise ExchangeError(f"{url} -> 451")


def test_run_end_to_end(tmp_path):
    ds = Datastore(tmp_path)
    now = ms("2026-10-07T12:30:00")
    s = run_crypto(ds, "r1", http=FakeHttp(now), clock=lambda: now / 1000, log=lambda *_: None)
    assert s["collecting"] and s["new_events"] == 2
    events = {e["event_id"]: e for e in ds.read_csv("crypto/events.csv")}
    ann = events["tg-mexcpumpcoins-42"]
    assert (ann["kind"], ann["exchange"], ann["base"]) == ("announcement", "mexc", "ABCD")
    spike = next(e for e in events.values() if e["source"] == "scan")
    assert spike["exchange"] == "mexc" and spike["base"] == "ABCD" and float(spike["spike"]) == 0.3
    chans = {c["name"]: c for c in ds.read_csv("crypto/telegram/channels.csv")}
    assert chans["otherpumps"]["source"] == "link from mexcpumpcoins" and chans["mexcpumpcoins"]["last_post_id"] == "42"
    outs = {o["event_id"]: o for o in ds.read_csv("crypto/outcomes.csv")}
    assert outs["tg-mexcpumpcoins-42"]["status"] == "pending"  # its 7 days are not over
    posts = list((tmp_path / "crypto/telegram/posts").rglob("*.jsonl.gz"))
    assert len(posts) == 1 and len(gzip.decompress(posts[0].read_bytes()).splitlines()) == 2
    # a second run adds nothing new
    s2 = run_crypto(ds, "r2", http=FakeHttp(now), clock=lambda: now / 1000 + 3600, log=lambda *_: None)
    assert s2["new_events"] == 0
    assert json.loads((tmp_path / "crypto/state.json").read_text())["live_since"] == now / 1000
