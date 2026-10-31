# Stage 5 model

Updated 2026-10-31T05:26:13Z. Rule `model-v3` (docs/stage5.md on the code branch), written down before any model was trained. Every candidate is scored once, by the LightGBM model of the week it was flagged in (trained on the labels available before that week began, recent ones weighted more), and the score goes into the prospective log `model/predictions.csv`. **crash**: a close 40% or more below the flag price within 10 sessions (the avoid signal, first). **pump**: Stage 4's pump label. A candidate is flagged when its score is at least twice the base rate.

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
| 2026-10-31 02:57 | INO | other | no model | no model | 100% / 0% / 0% / 0% | Chatter discusses INO's price movement following FDA approval rumors and insider leak claims. |
| 2026-10-31 00:58 | GLD | other | no model | no model | 100% / 0% / 0% / 0% | Users discuss GLD price drops, express frustration, and place bearish bets. |
| 2026-10-31 00:51 | AAOI | other | no model | no model | 100% / 0% / 0% / 0% | Chatter focuses on AAOI price volatility, user holdings, and a specific warning about customer concentration risks. |
| 2026-10-31 00:21 | QCOM | other | no model | no model | 100% / 10% / 0% / 10% | Users discuss QCOM earnings, express bearish views on price drops, and some buy positions. |
| 2026-10-30 22:07 | TLT | other | no model | no model | 100% / 0% / 0% / 0% | Users discuss TLT price movements, trading strategies, and comparisons to other assets without specific corporate events. |
| 2026-10-30 19:57 | SOXL | other | no model | no model | 100% / 5.0% / 0% / 0% | Users discuss SOXL's massive drop, margin calls, and leveraged ETF risks. |
| 2026-10-30 19:04 | SOXX | other | no model | no model | 100% / 17% / 0% / 0% | Users discuss SOXX price drops, portfolio composition, and market volatility with mixed bullish and bearish sentiments. |
| 2026-10-30 18:26 | TQQQ | other | no model | no model | 100% / 0% / 0% / 0% | Users discuss TQQQ price levels, express bullish optimism, and joke about potential drops or gains. |
| 2026-10-30 17:43 | INTL | other | no model | no model | 90% / 0% / 0% / 0% | Users discuss INTL's price drop, confusion over its identity, and comparisons to other stocks. |
| 2026-10-30 17:00 | APP | other | no model | no model | 100% / 0% / 0% / 0% | Users discuss APP stock price drops, express confusion about upcoming earnings, and joke about portfolio losses. |
| 2026-10-30 17:00 | SBUX | other | no model | no model | 100% / 10% / 0% / 20% | Mixed chatter on SBUX including earnings surprise, CEO praise, and unrelated jokes. |
| 2026-10-30 17:00 | SPY | other | no model | no model | 100% / 2.5% / 0% / 0% | Users discuss SPY price action, volatility, and trading strategies with mixed bullish and bearish sentiments. |
| 2026-10-30 16:45 | RSP | other | no model | no model | 100% / 0% / 0% / 0% | Users discuss RSP outperforming SPY and QQQ, with some mentioning calls and portfolio gains. |
| 2026-10-30 16:45 | WMT | other | no model | no model | 100% / 0% / 0% / 0% | Users discuss WMT price movements, valuations, and portfolio positions without specific company events or pump-and-dump warnings. |
| 2026-10-30 15:55 | SOXS | other | no model | no model | 100% / 0% / 0% / 0% | Users discuss SOXS price movements, express regret over selling, and speculate on future gains. |
| 2026-10-30 15:15 | USO | other | no model | no model | 100% / 25% / 0% / 0% | Users discuss USO price movements, express bullish sentiment, and speculate on short covering without mentioning specific corporate events. |
| 2026-10-30 15:02 | SGOV | other | no model | no model | 100% / 0% / 0% / 0% | Users discuss holding SGOV as a safe haven or joke about its stability, with no specific corporate events or pump-and-dump warnings. |
| 2026-10-30 14:50 | SQQQ | other | no model | no model | 100% / 0% / 0% / 0% | Users discuss SQQQ price movements, express regret over selling, and joke about buying TQQQ instead. |
| 2026-10-30 14:19 | QQQ | other | no model | no model | 100% / 0% / 0% / 0% | Users discuss QQQ price levels, options trading, and market sentiment with mixed bullish and bearish views. |
| 2026-10-30 14:07 | COIN | other | no model | no model | 100% / 0% / 0% / 0% | Users discuss shorting COIN, mention CEO selling, and express bearish views. |
| 2026-10-30 13:54 | TSM | other | no model | no model | 100% / 0% / 0% / 0% | Users discuss holding TSM, note its resilience compared to other tech stocks, and mention options positions. |
| 2026-10-30 13:42 | SMCI | other | no model | no model | 100% / 0% / 9.1% / 0% | Users discuss SMCI's accounting issues, past performance, and potential buying opportunities despite skepticism. |
| 2026-10-30 13:25 | AMD | other | no model | no model | 100% / 0% / 0% / 0% | Users discuss AMD's upcoming earnings, current price volatility, and bearish/bullish opinions regarding its valuation and AI prospects. |
| 2026-10-30 11:53 | NVDA | other | no model | no model | 100% / 0% / 0% / 0% | Mixed chatter regarding NVDA earnings, price targets, and general market sentiment. |
| 2026-10-30 11:00 | ARM | other | no model | no model | 100% / 0% / 0% / 0% | Users discuss ARM's potential earnings, general market sentiment, and compare it to other chip stocks. |
| 2026-10-30 10:30 | BURU | other | no model | no model | 100% / 20% / 0% / 10% | Users discuss BURU price targets, express bullish sentiment, and mention a potential financing event. |
| 2026-10-30 09:12 | NKE | other | no model | no model | 100% / 0% / 0% / 0% | Users discuss NKE positions, noting recent gains and joking about a potential pump-and-dump scheme. |
| 2026-10-30 08:33 | PLTR | other | no model | no model | 100% / 0% / 0% / 0% | Mixed chatter includes throwback posts, earnings previews, bearish rumors about fake deals, and skepticism regarding software capabilities. |
| 2026-10-30 05:02 | SCHD | other | no model | no model | 100% / 0% / 0% / 0% | Users discuss SCHD as a safe dividend play, noting its performance and rotation from tech stocks. |
| 2026-10-30 04:49 | VOO | other | no model | no model | 100% / 0% / 0% / 0% | Users discuss holding VOO for retirement, express relief from trading stress, and joke about market volatility. |
| 2026-10-30 01:20 | DJT | other | no model | no model | 100% / 20% / 0% / 0% | Users discuss DJT, referencing political figures, memes, and potential trading opportunities without specific corporate events. |
| 2026-10-30 00:42 | DELL | other | no model | no model | 100% / 0% / 0% / 0% | Users discuss a sharp price drop, rumors of bankruptcy, and past losses regarding DELL stock. |
| 2026-10-30 00:00 | MSTR | other | no model | no model | 100% / 5.6% / 5.6% / 11% | Users discuss MSTR earnings, price movements, and speculate on a potential pump-and-dump scheme. |
| 2026-10-29 22:53 | AAPL | other | no model | no model | 100% / 0% / 0% / 0% | Users discuss AAPL's price resilience, valuation concerns, and its role as a safe haven amidst market volatility. |
| 2026-10-29 22:12 | PINS | other | no model | no model | 100% / 30% / 0% / 60% | Users discuss PINS earnings and express bullish sentiment with price targets. |
| 2026-10-29 22:12 | ROPE | other | no model | no model | 100% / 0% / 0% / 0% | Users discuss buying $ROPE, referencing a hedge fund manager and general bullish sentiment. |
| 2026-10-29 21:47 | GME | other | no model | no model | 100% / 0% / 0% / 0% | Users discuss GME's recent price decline, potential eBay/Amazon acquisition rumors, and past squeeze events. |
| 2026-10-29 21:35 | CROX | other | no model | no model | 100% / 0% / 0% / 0% | Users discuss CROX performance, rotation from tech, and potential shorting opportunities. |
| 2026-10-29 20:56 | NRXP | other | no model | no model | 100% / 10% / 0% / 90% | Chatter focuses on an upcoming FDA regulatory decision and potential stock squeeze for NRXP. |
| 2026-10-29 20:27 | SNDK | other | no model | no model | 100% / 0% / 0% / 18% | Users discuss SNDK earnings expectations, price targets, and potential market moves in r/wallstreetbets. |

## Development walk-forward (flags before 2027-01-04)

Each development week replayed exactly as it would have run: its model trained only on labels available before the week began, scoring that week's candidates. Results count candidates whose label has settled.

### crash

No scored candidate with a settled label yet.

### pump

No scored candidate with a settled label yet.

## Hold-out (flags from 2027-01-04)

Still locked, with 0 hold-out candidates so far. They are scored like any other, but their scores are not compared with their outcomes until collection has finished and every hold-out label has settled; then they are evaluated once, into `model/holdout.md`.
