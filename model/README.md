# Stage 5 model

Updated 2026-10-18T00:15:09Z. Rule `model-v3` (docs/stage5.md on the code branch), written down before any model was trained. Every candidate is scored once, by the LightGBM model of the week it was flagged in (trained on the labels available before that week began, recent ones weighted more), and the score goes into the prospective log `model/predictions.csv`. **crash**: a close 40% or more below the flag price within 10 sessions (the avoid signal, first). **pump**: Stage 4's pump label. A candidate is flagged when its score is at least twice the base rate.

## This week's models (week of 2026-10-12)

| Target | Status | Trained on | Positives | Base rate | Flag at | Feature groups |
|---|---|---|---|---|---|---|
| crash | no model yet | 0 rows | 0 | - | - | chatter, text, llm, price_volume, size, short_interest, filings, history, technical |
| pump | no model yet | 0 rows | 0 | - | - | chatter, text, llm, price_volume, size, short_interest, filings, history, technical |

A week's model needs 50 rows and 5 positives whose labels were settled before the week began; a label settles 10 sessions (two weeks) after the flag, 15 after a 50% rise.

## Latest candidates (last 7 days)

Scores as logged when each candidate was first seen; flagged ones in bold. The LLM column gives the shares of the posts shown that are about the company, pitch it, warn about it and state a company event (counted only when its quote checks out).

| Flagged (UTC) | Ticker | Archetype | Crash risk | Pump risk | LLM about / pitch / warning / event | What the chatter was about |
|---|---|---|---|---|---|---|
| 2026-10-17 17:37 | NFLX | other | no model | no model | 100% / 0% / 0% / 7.7% | Mixed chatter on NFLX ranging from skepticism about value traps to speculation on earnings and IV. |
| 2026-10-17 04:49 | SCHD | other | no model | no model | 100% / 0% / 0% / 0% | Users discuss buying SCHD as a safe value pick and dividend growth strategy. |
| 2026-10-17 01:44 | SOXX | other | no model | no model | 100% / 0% / 0% / 0% | Users discuss SOXX price drops, losses, and bearish sentiment regarding the semiconductor sector. |
| 2026-10-16 21:33 | AMD | other | no model | no model | 100% / 0% / 0% / 0% | Mixed chatter on AMD including profit taking, bearish sentiment, and speculation on price targets. |
| 2026-10-16 21:20 | SGRX | other | no model | no model | 100% / 0% / 0% / 0% | Users discuss SGRX price targets, recent drops, and potential upside in penny stock forums. |
| 2026-10-16 21:20 | XLAB | other | no model | no model | 100% / 29% / 7.1% / 0% | Mixed chatter on XLAB including volume analysis, price targets, and accusations of pump-and-dump schemes. |
| 2026-10-16 20:40 | AAPL | other | no model | no model | 100% / 0% / 0% / 0% | Users discuss AAPL's unusual resilience during a market downturn, noting its green performance, call options activity, and lack of specific catalysts. |
| 2026-10-16 20:14 | AVGO | other | no model | no model | 100% / 0% / 0% / 0% | Users discuss AVGO's poor performance, VMware acquisition concerns, and general bearish sentiment without specific corporate events. |
| 2026-10-16 19:34 | SOXS | other | no model | no model | 100% / 19% / 6.2% / 0% | Users discuss trading SOXS, with some warning of decay and others offering shares for sale. |
| 2026-10-16 19:07 | MSTR | other | no model | no model | 100% / 10% / 0% / 0% | Users discuss MSTR, mention Michael Saylor, and express mixed opinions ranging from bullish excitement to skepticism. |
| 2026-10-16 19:07 | OPEX | other | no model | no model | 100% / 0% / 0% / 0% | Users discuss OPEX expiration day volatility, oil market news, and general trading sentiments. |
| 2026-10-16 19:07 | VOO | other | no model | no model | 100% / 0% / 0% / 0% | Users discuss VOO as a safe investment, express regret over missing out, and react to price drops. |
| 2026-10-16 18:54 | TQQQ | other | no model | no model | 100% / 18% / 0% / 0% | Users discuss TQQQ trading strategies, past performance, and express bullish optimism for upcoming market moves. |
| 2026-10-16 18:27 | QQQ | other | no model | no model | 100% / 0% / 0% / 0% | Users discuss QQQ price drops, short positions, and bearish sentiment without mentioning specific corporate events. |
| 2026-10-16 13:35 | IBKR | other | no model | no model | 100% / 0% / 0% / 0% | Users discuss IBKR trading mechanics, commissions, and portfolio margin requirements without mentioning specific company events. |
| 2026-10-16 12:29 | RCS | other | no model | no model | 0% / 0% / 0% / 0% | All documents discuss RCS thrusters in a rocket engineering context, not the PIMCO fund. |
| 2026-10-16 11:23 | USO | other | no model | no model | 100% / 0% / 0% / 0% | Users discuss USO price movements, express regret over buying puts, and joke about market volatility. |
| 2026-10-16 07:11 | TSLA | other | no model | no model | 100% / 28% / 0% / 5.0% | Users discuss a SpaceX/TSLA merger rumor, price targets, and general bullish sentiment. |
| 2026-10-15 23:28 | BETR | other | no model | no model | 100% / 91% / 0% / 0% | Users discuss BETR as a heavily shorted penny stock with high squeeze potential and urge others to buy. |
| 2026-10-15 23:28 | DRMA | other | no model | no model | 100% / 0% / 0% / 0% | Users discuss DRMA price action, volume, and potential moves based on test results. |
| 2026-10-15 21:16 | WETO | low float runner | no model | no model | 100% / 55% / 0% / 9.1% | Users discuss WETO trading strategy, warn against stop losses, and mention a cancelled ATM offering. |
| 2026-10-15 15:04 | SOXS | other | no model | no model | 100% / 0% / 0% / 0% | Users discuss holding, selling, or buying SOXS, with mentions of AI news and market volatility. |
| 2026-10-14 20:17 | PFE | other | no model | no model | 100% / 10% / 0% / 0% | Users discuss Pfizer as a defensive stock, dividend play, and potential AI beneficiary with mixed bullish and neutral sentiments. |
| 2026-10-14 20:04 | HOOD | other | no model | no model | 100% / 0% / 0% / 0% | Users discuss HOOD price drops, buying dips, and general market sentiment without specific company events. |
| 2026-10-14 19:51 | TSM | other | no model | no model | 94% / 24% / 0% / 53% | Users discuss TSM earnings anticipation, market recovery, and set price targets. |
| 2026-10-14 19:24 | RKLB | other | no model | no model | 100% / 0% / 0% / 0% | Users discuss RKLB losses, compare it to competitors, and express skepticism about its future potential. |
| 2026-10-14 19:24 | WMT | other | no model | no model | 100% / 0% / 0% / 0% | Users discuss WMT as a defensive stock, express bullish sentiment, and mention buying calls. |
| 2026-10-14 19:11 | LQDA | other | no model | no model | 100% / 70% / 0% / 20% | Users discuss LQDA price targets, a lawsuit settlement, and short interest, with mixed bullish and bearish sentiments. |
| 2026-10-14 18:31 | TLT | other | no model | no model | 100% / 0% / 0% / 0% | Users discuss TLT price movements, yields, and correlations with other assets without mentioning specific corporate events. |
| 2026-10-14 18:18 | SOFI | other | no model | no model | 100% / 0% / 0% / 0% | Users express extreme frustration and bearish sentiment regarding SOFI's price drop and performance. |
| 2026-10-14 17:34 | VOO | other | no model | no model | 100% / 0% / 0% / 0% | Users discuss holding VOO for long-term growth, comparing it to other assets, and expressing mixed views on current market valuations. |
| 2026-10-14 16:58 | ORCL | other | no model | no model | 100% / 0% / 0% / 0% | Users discuss ORCL price movements, options strategies, and rumors of a deal or government stake. |
| 2026-10-14 15:25 | ARM | other | no model | no model | 100% / 0% / 0% / 20% | Users discuss ARM's legal loss to Qualcomm and a potential forced sale due to collateralized debt. |
| 2026-10-14 13:12 | TCRT | low float runner | no model | no model | 100% / 20% / 0% / 0% | Chatter focuses on TCRT price targets, volume, and a reported catalyst driving a significant price increase. |
| 2026-10-14 12:46 | UPST | other | no model | no model | 100% / 40% / 10% / 0% | Users express frustration over losses, warn of potential pump-and-dumps, and share price targets for UPST. |
| 2026-10-14 12:29 | GLND | other | no model | no model | 100% / 55% / 0% / 0% | Users discuss Greenland Energy Company, citing a Greenland announcement and volume increases as reasons to buy. |
| 2026-10-14 11:39 | CLF | other | no model | no model | 100% / 10% / 0% / 10% | Users discuss Cleveland-Cliffs earnings, datacenter demand, and potential short squeeze. |
| 2026-10-14 05:42 | BBAI | other | no model | no model | 100% / 20% / 0% / 0% | Users discuss BBAI's recent $225M government contract announcement and speculate on potential price spikes. |
| 2026-10-14 00:41 | RSP | other | no model | no model | 100% / 0% / 0% / 0% | Users discuss RSP performance, correlation with SPY, and market breadth without specific company events or urgent buy pitches. |
| 2026-10-13 22:51 | SOXL | other | no model | no model | 100% / 0% / 0% / 0% | Users discuss SOXL volatility, losses, and leverage while joking about its performance. |

## Development walk-forward (flags before 2027-01-04)

Each development week replayed exactly as it would have run: its model trained only on labels available before the week began, scoring that week's candidates. Results count candidates whose label has settled.

### crash

No scored candidate with a settled label yet.

### pump

No scored candidate with a settled label yet.

## Hold-out (flags from 2027-01-04)

Still locked, with 0 hold-out candidates so far. They are scored like any other, but their scores are not compared with their outcomes until collection has finished and every hold-out label has settled; then they are evaluated once, into `model/holdout.md`.
