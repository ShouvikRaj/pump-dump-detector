# Stage 5 model

Updated 2026-10-30T00:18:05Z. Rule `model-v3` (docs/stage5.md on the code branch), written down before any model was trained. Every candidate is scored once, by the LightGBM model of the week it was flagged in (trained on the labels available before that week began, recent ones weighted more), and the score goes into the prospective log `model/predictions.csv`. **crash**: a close 40% or more below the flag price within 10 sessions (the avoid signal, first). **pump**: Stage 4's pump label. A candidate is flagged when its score is at least twice the base rate.

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
| 2026-10-30 00:00 | MSTR | other | no model | no model | 100% / 5.6% / 5.6% / 11% | Users discuss MSTR earnings, price movements, and speculate on a potential pump-and-dump scheme. |
| 2026-10-29 22:53 | AAPL | other | no model | no model | 100% / 0% / 0% / 0% | Users discuss AAPL's price resilience, valuation concerns, and its role as a safe haven amidst market volatility. |
| 2026-10-29 22:12 | PINS | other | no model | no model | 100% / 30% / 0% / 60% | Users discuss PINS earnings and express bullish sentiment with price targets. |
| 2026-10-29 22:12 | ROPE | other | no model | no model | 100% / 0% / 0% / 0% | Users discuss buying $ROPE, referencing a hedge fund manager and general bullish sentiment. |
| 2026-10-29 21:47 | GME | other | no model | no model | 100% / 0% / 0% / 0% | Users discuss GME's recent price decline, potential eBay/Amazon acquisition rumors, and past squeeze events. |
| 2026-10-29 21:35 | CROX | other | no model | no model | 100% / 0% / 0% / 0% | Users discuss CROX performance, rotation from tech, and potential shorting opportunities. |
| 2026-10-29 20:56 | NRXP | other | no model | no model | 100% / 10% / 0% / 90% | Chatter focuses on an upcoming FDA regulatory decision and potential stock squeeze for NRXP. |
| 2026-10-29 20:27 | SNDK | other | no model | no model | 100% / 0% / 0% / 18% | Users discuss SNDK earnings expectations, price targets, and potential market moves in r/wallstreetbets. |
| 2026-10-29 19:09 | IWM | other | no model | no model | 100% / 30% / 0% / 0% | Users discuss IWM price movements, express bullish optimism, and note a subsequent drop. |
| 2026-10-29 17:49 | SAP | other | no model | no model | 100% / 17% / 0% / 0% | Users discuss SAP's CEO backstory and express frustration with the software, with one user claiming insider knowledge of post-earnings buying. |
| 2026-10-29 14:09 | LLY | other | no model | no model | 100% / 0% / 0% / 8.3% | Users discuss LLY price targets, earnings anticipation, and general bullish sentiment in r/wallstreetbets. |
| 2026-10-29 14:06 | AMZN | other | no model | no model | 100% / 0% / 0% / 0% | Users discuss AMZN earnings anticipation, price targets, and market sentiment in r/wallstreetbets. |
| 2026-10-29 14:06 | RDDT | other | no model | no model | 100% / 0% / 0% / 5.0% | Users discuss RDDT earnings day, with mixed opinions on potential price drops or gains. |
| 2026-10-29 13:37 | DXYZ | other | no model | no model | 100% / 50% / 0% / 10% | Users discuss DXYZ's undervaluation relative to NAV and potential gains from holdings in Anthropic and OpenAI. |
| 2026-10-29 11:49 | INTC | other | no model | no model | 100% / 29% / 0% / 0% | Users discuss INTC price targets, potential pumps, and joke about a 'GOOG style' move. |
| 2026-10-29 10:54 | ELPW | low float runner | no model | no model | 100% / 30% / 0% / 40% | Chatter focuses on a $25.5M distribution agreement and low float, with multiple users urging immediate buys and price targets. |
| 2026-10-29 04:39 | TTWO | other | no model | no model | 100% / 0% / 0% / 0% | Users discuss TTWO's stock performance relative to GTA6 hype, with mixed opinions on valuation and future potential. |
| 2026-10-29 04:31 | WEN | other | no model | no model | 100% / 10% / 0% / 10% | Chatter discusses a potential takeover, regulatory statement, and price surge for Wendy's stock. |
| 2026-10-29 04:06 | CVNA | other | no model | no model | 100% / 0% / 0% / 9.1% | Users discuss CVNA earnings, joke about its health, and ironically wish others bad luck. |
| 2026-10-29 00:52 | CBRS | other | no model | no model | 100% / 6.2% / 0% / 31% | Users discuss a partnership between Cerebras and Oracle, debate valuation, and share bullish opinions on the stock. |
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

## Development walk-forward (flags before 2027-01-04)

Each development week replayed exactly as it would have run: its model trained only on labels available before the week began, scoring that week's candidates. Results count candidates whose label has settled.

### crash

No scored candidate with a settled label yet.

### pump

No scored candidate with a settled label yet.

## Hold-out (flags from 2027-01-04)

Still locked, with 0 hold-out candidates so far. They are scored like any other, but their scores are not compared with their outcomes until collection has finished and every hold-out label has settled; then they are evaluated once, into `model/holdout.md`.
