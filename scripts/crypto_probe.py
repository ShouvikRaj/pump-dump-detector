"""One-off reachability probe for the crypto track (run on a GitHub runner; prints only, writes nothing).

Checks which exchange APIs answer from GitHub's runners, whether Binance's bulk
history files can be downloaded, and which public Telegram channels still show a
web preview (t.me/s/NAME) and when they last posted.
"""

import re
import sys
import time

import requests

UA = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36"
s = requests.Session()
s.headers["User-Agent"] = UA


def get(url, **kw):
    t = time.time()
    try:
        r = s.get(url, timeout=20, **kw)
        return r.status_code, r.content, time.time() - t
    except requests.RequestException as e:
        return 0, str(e).encode(), time.time() - t


HTTP = {
    "mexc tickers": "https://api.mexc.com/api/v3/ticker/24hr",
    "mexc klines": "https://api.mexc.com/api/v3/klines?symbol=BTCUSDT&interval=60m&limit=5",
    "gate tickers": "https://api.gateio.ws/api/v4/spot/tickers",
    "gate candles": "https://api.gateio.ws/api/v4/spot/candlesticks?currency_pair=BTC_USDT&interval=1h&limit=5",
    "kucoin tickers": "https://api.kucoin.com/api/v1/market/allTickers",
    "kucoin candles 2019": "https://api.kucoin.com/api/v1/market/candles?type=1hour&symbol=BTC-USDT&startAt=1546300800&endAt=1546387200",
    "binance api": "https://api.binance.com/api/v3/ping",
    "binance data-api": "https://data-api.binance.vision/api/v3/klines?symbol=BTCUSDT&interval=1h&limit=5",
    "binance bulk 1m 2018 ARNBTC": "https://data.binance.vision/data/spot/daily/klines/ARNBTC/1m/ARNBTC-1m-2018-04-10.zip",
    "binance bulk 1h monthly 2019 APPCBTC": "https://data.binance.vision/data/spot/monthly/klines/APPCBTC/1h/APPCBTC-1h-2019-07.zip",
    "binance bulk 1m 2021 MTHBTC": "https://data.binance.vision/data/spot/daily/klines/MTHBTC/1m/MTHBTC-1m-2021-11-07.zip",
    "bybit": "https://api.bybit.com/v5/market/tickers?category=spot",
    "okx": "https://www.okx.com/api/v5/market/tickers?instType=SPOT",
    "lbank": "https://api.lbkex.com/v2/ticker/24hr.do?symbol=all",
    "xt": "https://sapi.xt.com/v4/public/ticker/24h",
    "bitget": "https://api.bitget.com/api/v2/spot/market/tickers",
    "htx": "https://api.huobi.pro/market/tickers",
    "poloniex": "https://api.poloniex.com/markets/ticker24h",
    "coingecko": "https://api.coingecko.com/api/v3/ping",
    "cryptocompare": "https://min-api.cryptocompare.com/data/v2/histohour?fsym=BTC&tsym=USD&limit=3",
    "geckoterminal": "https://api.geckoterminal.com/api/v2/networks/solana/new_pools",
    "dexscreener": "https://api.dexscreener.com/token-profiles/latest/v1",
}

CHANNELS = sys.argv[1].split(",") if len(sys.argv) > 1 else []

print("== HTTP")
for name, url in HTTP.items():
    code, body, dt = get(url)
    print(f"{name:40s} {code} {len(body):>9d}B {dt:5.1f}s {body[:90]!r}")
    time.sleep(0.3)

print("== Telegram t.me/s")
date_re = re.compile(r'<time datetime="([^"]+)"')
text_re = re.compile(r'<div class="tgme_widget_message_text[^>]*>(.*?)</div>', re.S)
for ch in CHANNELS:
    code, body, dt = get(f"https://t.me/s/{ch}")
    html = body.decode("utf-8", "replace")
    dates = date_re.findall(html)
    texts = [re.sub(r"<[^>]+>", " ", t) for t in text_re.findall(html)]
    pumpish = sum(1 for t in texts if re.search(r"(?i)\bpump|coin (?:is|we)|exchange", t))
    redirected = "tgme_channel_info" not in html
    last = dates[-1] if dates else "-"
    sample = re.sub(r"\s+", " ", texts[-1])[:120] if texts else ""
    print(f"{ch:32s} {code} msgs={len(dates):2d} last={last[:16]} pumpish={pumpish:2d} nopreview={redirected} | {sample}")
    time.sleep(1.0)
