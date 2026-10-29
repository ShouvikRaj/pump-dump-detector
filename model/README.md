# Stage 5 model

Updated 2026-10-29T00:14:35Z. Rule `model-v3` (docs/stage5.md on the code branch), written down before any model was trained. Every candidate is scored once, by the LightGBM model of the week it was flagged in (trained on the labels available before that week began, recent ones weighted more), and the score goes into the prospective log `model/predictions.csv`. **crash**: a close 40% or more below the flag price within 10 sessions (the avoid signal, first). **pump**: Stage 4's pump label. A candidate is flagged when its score is at least twice the base rate.

## This week's models (week of 2026-10-26)

| Target | Status | Trained on | Positives | Base rate | Flag at | Feature groups |
|---|---|---|---|---|---|---|
| crash | no model yet | 246 rows | 4 | - | - | chatter, text, llm, price_volume, size, short_interest, filings, history, technical |
| pump | no model yet | 244 rows | 0 | - | - | chatter, text, llm, price_volume, size, short_interest, filings, history, technical |

A week's model needs 50 rows and 5 positives whose labels were settled before the week began; a label settles 10 sessions (two weeks) after the flag, 15 after a 50% rise.

## Latest candidates (last 7 days)

Scores as logged when each candidate was first seen; flagged ones in bold. The LLM column gives the shares of the posts shown that are about the company, pitch it, warn about it and state a company event (counted only when its quote checks out).

| Flagged (UTC) | Ticker | Archetype | Crash risk | Pump risk | LLM about / pitch / warning / event | What the chatter was about |
|---|---|---|---|---|---|---|
| 2026-10-28 23:40 | COHR | other | no model | no model | 100% / 0% / 0% / 0% | Users discuss sudden price movements of COHR, linking it to LITE and MRVL without specific company events. |
| 2026-10-28 22:11 | GGLL | other | no model | no model | 100% / 0% / 0% / 0% | Users discuss holding Direxion Daily GOOGL Bull 2X ETF and express bullish sentiment. |
| 2026-10-28 21:57 | NOW | other | no model | no model | 100% / 30% / 0% / 10% | Users discuss ServiceNow stock price movements, potential earnings spikes, and market sentiment in r/wallstreetbets. |
| 2026-10-28 21:46 | GOOGL | other | no model | no model | 100% / 0% / 0% / 0% | Chatter focuses on GOOGL's earnings miss, AI concerns, and subsequent stock decline with mixed sentiment. |
| 2026-10-28 21:20 | FTNT | other | no model | no model | 100% / 10% / 0% / 0% | Chatter discusses a massive sector drop, attributing it to FTNT, with mixed bearish and bullish sentiments. |
| 2026-10-28 21:20 | LITE | other | no model | no model | 100% / 56% / 0% / 56% | Users discuss a rumor of Marvell acquiring Lumentum, driving aggressive buy signals and price speculation. |
| 2026-10-28 21:20 | MRVL | other | no model | no model | 100% / 0% / 0% / 14% | Users discuss a sudden 11% drop in MRVL following rumors of an acquisition of Lumentum Holdings. |
| 2026-10-28 20:50 | GOOG | other | no model | no model | 100% / 0% / 0% / 2.5% | Users discuss GOOG earnings miss, AI concerns, and significant price drops. |
| 2026-10-28 18:38 | ORCL | other | no model | no model | 100% / 25% / 2.5% / 0% | Users discuss a sudden price surge in ORCL, citing potential insider trading and pump-and-dump suspicions alongside bullish hype. |
| 2026-10-28 17:04 | DJT | other | no model | no model | 100% / 0% / 0% / 0% | Users discuss DJT's AI capabilities, political connections, and make jokes about its intelligence and market performance. |
| 2026-10-28 16:10 | ENPH | other | no model | no model | 100% / 0% / 0% / 0% | Users discuss ENPH price drops, past highs, and potential data center demand while expressing regret over losses. |
| 2026-10-28 13:05 | SLS | other | no model | no model | 100% / 31% / 15% / 31% | Chatter focuses on an announced '80th event' and mixed opinions on the stock price. |
| 2026-10-28 11:39 | VRT | other | no model | no model | 100% / 0% / 0% / 10% | Chatter focuses on VRT earnings beat, guidance raises, and price reaction. |
| 2026-10-28 00:47 | GLD | other | no model | no model | 100% / 14% / 0% / 0% | Users discuss GLD price movements, FOMC impact, and speculate on buying calls or the stock reaching $400. |
| 2026-10-27 20:57 | BBAI | other | no model | no model | 100% / 0% / 0% / 0% | Users discuss BBAI earnings, volume, and price movements in r/pennystocks and r/wallstreetbets. |
| 2026-10-27 19:51 | SKHY | other | no model | no model | 100% / 0% / 0% / 20% | Chatter focuses on SKHY earnings anticipation, price targets, and speculative trading strategies. |
| 2026-10-27 19:12 | STX | other | no model | no model | 100% / 55% / 0% / 9.1% | Users discuss buying STX calls, mention earnings leaks, and compare it to other stocks. |
| 2026-10-27 17:53 | BRAI | other | no model | no model | 100% / 30% / 10% / 0% | Users discuss BRAI's massive price surge, attributing it to momentum, news, or potential pump-and-dump schemes. |
| 2026-10-27 17:38 | ASML | other | no model | no model | 100% / 0% / 0% / 0% | Users discuss ASML's critical role in semiconductor manufacturing and AI hardware supply chains. |
| 2026-10-27 17:13 | USAR | other | no model | no model | 100% / 0% / 0% / 0% | Users discuss USAR price movements, political context, and trading strategies without citing specific corporate events. |
| 2026-10-27 14:48 | INOD | other | no model | no model | 100% / 0% / 0% / 0% | Users discuss a sharp price drop in INOD, citing layoffs and potential client loss as reasons to buy the dip. |
| 2026-10-27 13:39 | GOOGL | other | no model | no model | 100% / 7.5% / 0% / 2.5% | Chatter focuses on GOOGL earnings anticipation, mixed with bearish predictions, bullish calls, and a rumor about Buffett selling. |
| 2026-10-27 03:54 | HOOD | other | no model | no model | 100% / 0% / 0% / 0% | Users discuss HOOD earnings, express bearish sentiment, and mention potential price drops. |
| 2026-10-27 02:38 | VOO | other | no model | no model | 100% / 0% / 0% / 0% | Users discuss VOO as a safe index fund, contrasting it with risky individual stocks and options. |
| 2026-10-27 00:43 | AMKR | other | no model | no model | 100% / 0% / 0% / 0% | Users discuss AMKR earnings, NVIDIA partnership, and price movements with mixed bullish and bearish sentiments. |
| 2026-10-27 00:43 | COIN | other | no model | no model | 100% / 0% / 0% / 0% | Users discuss COIN alongside other stocks, mentioning potential earnings misses, dilution fears, and general market sentiment. |
| 2026-10-27 00:43 | DXYZ | other | no model | no model | 100% / 70% / 0% / 10% | Users hype DXYZ as a high-risk, high-reward stock with potential for massive gains. |
| 2026-10-27 00:43 | GOOG | other | no model | no model | 100% / 0% / 0% / 0% | Chatter discusses GOOG price action, earnings rumors, and mixed sentiment with no confirmed specific events. |
| 2026-10-27 00:43 | RIVN | other | no model | no model | 100% / 0% / 0% / 0% | Users express extreme frustration and regret over significant financial losses on RIVN, with no promotional content or specific corporate events mentioned. |
| 2026-10-27 00:43 | SOFI | other | no model | no model | 100% / 0% / 0% / 0% | Users discuss SOFI earnings, options plays, and potential stock movement before a scheduled event. |
| 2026-10-27 00:09 | MSFT | other | no model | no model | 100% / 0% / 0% / 5.0% | Chatter discusses MSFT layoffs, earnings anticipation, and general market sentiment with mixed bullish and bearish views. |
| 2026-10-26 19:24 | CLS | other | no model | no model | 100% / 70% / 0% / 70% | Users discuss CLS earnings anticipation, price drops, and urge buying calls. |
| 2026-10-26 14:04 | RDDT | other | no model | no model | 93% / 6.7% / 3.3% / 3.3% | Users discuss RDDT price drops, earnings anticipation, and express confusion or bearish sentiment. |
| 2026-10-26 13:24 | STNE | other | no model | no model | 100% / 0% / 0% / 0% | Users discuss buying Brazilian stocks including STNE following a market dip. |
| 2026-10-26 11:48 | NU | other | no model | no model | 100% / 30% / 0% / 0% | Users express disappointment and hope for a rebound in NU, with one user urging others to buy the dip. |
| 2026-10-26 09:22 | PBR | other | no model | no model | 100% / 40% / 0% / 20% | Users discuss PBR volatility due to Brazilian election results and express bullish intent to buy. |
| 2026-10-26 08:42 | MELI | other | no model | no model | 100% / 0% / 0% / 0% | Users discuss a significant drop in MELI stock prices, attributing it to Brazil news and political factors. |
| 2026-10-26 00:21 | EWZ | other | no model | no model | 100% / 0% / 0% / 0% | Users discuss EWZ price drops following Brazilian election results, with no specific corporate events or pitches identified. |
| 2026-10-23 20:37 | CRWD | other | no model | no model | 100% / 30% / 0% / 0% | Users discuss CRWD stock performance, price targets, and relative strength in a bearish market. |
| 2026-10-23 20:37 | RDDT | other | no model | no model | 100% / 25% / 0% / 5.0% | Users discuss RDDT earnings, price targets, and meme stock potential with mixed sentiment. |

## Development walk-forward (flags before 2027-01-04)

Each development week replayed exactly as it would have run: its model trained only on labels available before the week began, scoring that week's candidates. Results count candidates whose label has settled.

### crash

No scored candidate with a settled label yet.

### pump

No scored candidate with a settled label yet.

## Hold-out (flags from 2027-01-04)

Still locked, with 0 hold-out candidates so far. They are scored like any other, but their scores are not compared with their outcomes until collection has finished and every hold-out label has settled; then they are evaluated once, into `model/holdout.md`.
