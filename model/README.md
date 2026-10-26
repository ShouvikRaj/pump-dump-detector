# Stage 5 model

Updated 2026-10-26T00:15:34Z. Rule `model-v3` (docs/stage5.md on the code branch), written down before any model was trained. Every candidate is scored once, by the LightGBM model of the week it was flagged in (trained on the labels available before that week began, recent ones weighted more), and the score goes into the prospective log `model/predictions.csv`. **crash**: a close 40% or more below the flag price within 10 sessions (the avoid signal, first). **pump**: Stage 4's pump label. A candidate is flagged when its score is at least twice the base rate.

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
| 2026-10-23 20:37 | CRWD | other | no model | no model | 100% / 30% / 0% / 0% | Users discuss CRWD stock performance, price targets, and relative strength in a bearish market. |
| 2026-10-23 20:37 | RDDT | other | no model | no model | 100% / 25% / 0% / 5.0% | Users discuss RDDT earnings, price targets, and meme stock potential with mixed sentiment. |
| 2026-10-23 18:21 | LUNR | other | no model | no model | 100% / 0% / 0% / 0% | Users discuss LUNR in relation to Cathie Wood's Ark fund and general tech sector volatility. |
| 2026-10-23 16:35 | USO | other | no model | no model | 100% / 0% / 0% / 0% | Users discuss USO price targets, rallies, and short interest with mixed bullish and bearish sentiments. |
| 2026-10-23 15:42 | BE | other | no model | no model | 100% / 9.1% / 0% / 9.1% | Users discuss BE's Q3 earnings beat, S&P 500 inclusion, and subsequent price reaction. |
| 2026-10-23 14:50 | IREN | other | no model | no model | 100% / 2.5% / 2.5% / 10% | Mixed chatter regarding IREN, including bullish hype about a new EU deal, bearish warnings about dilution, and general price discussion. |
| 2026-10-23 13:45 | ASTS | other | no model | no model | 100% / 10% / 0% / 0% | Users discuss ASTS losses, SpaceX competition, and potential buy opportunities. |
| 2026-10-23 13:03 | SKHY | other | no model | no model | 100% / 8.0% / 4.0% / 0% | Users discuss SKHY earnings, price dips, and potential pumps before the upcoming event. |
| 2026-10-23 12:23 | CRDO | other | no model | no model | 100% / 0% / 0% / 0% | Users discuss holding CRDO, express confusion over a sudden price drop, and speculate on a potential dump. |
| 2026-10-23 10:49 | MU | other | no model | no model | 100% / 0% / 0% / 0% | Users discuss Micron stock price movements, express bearish views via put options, and mention earnings context. |
| 2026-10-23 06:51 | MSFT | other | no model | no model | 100% / 0% / 0% / 3.3% | Discussions focus on MSFT earnings anticipation, AI valuation concerns, and mixed trading sentiment. |
| 2026-10-23 05:06 | AMD | other | no model | no model | 100% / 0% / 0% / 0% | Users discuss AMD price volatility, express bearish views on recent drops, and debate AI sector health. |
| 2026-10-23 03:07 | SPY | other | no model | no model | 100% / 0% / 0% / 0% | Users discuss SPY price movements, options strategies, and market sentiment with mixed bullish and bearish views. |
| 2026-10-23 02:14 | NVDA | other | no model | no model | 100% / 0% / 0% / 0% | Mixed chatter regarding NVDA price action, valuation concerns, and potential earnings impact. |
| 2026-10-23 00:59 | TQQQ | other | no model | no model | 100% / 0% / 0% / 0% | Users discuss TQQQ volatility, express regret over losses, and speculate on potential price movements. |
| 2026-10-23 00:03 | AAPL | other | no model | no model | 100% / 0% / 0% / 0% | Users discuss AAPL price strength, earnings anticipation, and general market sentiment with mixed bullish and bearish views. |
| 2026-10-22 23:50 | SOXS | other | no model | no model | 100% / 0% / 0% / 0% | Users discuss trading SOXS, noting price gains, holding positions, and comparing it to SOXL. |
| 2026-10-22 22:49 | CBRS | other | no model | no model | 100% / 0% / 0% / 0% | Users express extreme bearish sentiment, fear of loss, and confusion regarding the stock's performance. |
| 2026-10-22 22:30 | SNDK | other | no model | no model | 100% / 0% / 0% / 0% | Users discuss SNDK price drops, losses, and potential earnings impact without specific event announcements or promotional pitches. |
| 2026-10-22 22:30 | WMT | other | no model | no model | 100% / 0% / 0% / 0% | Users discuss WMT stock performance, options positions, and general bullish sentiment without specific corporate events. |
| 2026-10-22 22:06 | LMT | other | no model | no model | 100% / 30% / 0% / 20% | Users discuss LMT stock price movements, war context, and a specific contract rumor. |
| 2026-10-22 22:06 | SQQQ | other | no model | no model | 100% / 0% / 0% / 0% | Users discuss holding, selling, or buying SQQQ calls based on recent market movements. |
| 2026-10-22 21:18 | INTC | other | no model | no model | 100% / 0% / 0% / 0% | Users discuss INTC price levels, missed highs, and upcoming earnings alongside jokes and bearish fair value opinions. |
| 2026-10-22 21:05 | SCHD | other | no model | no model | 100% / 0% / 0% / 0% | Users discuss SCHD performance, portfolio allocation, and compare it to other ETFs with mixed sentiment. |
| 2026-10-22 20:12 | LULU | other | no model | no model | 100% / 14% / 7.1% / 0% | Users discuss LULU price movements, joke about founder racism, and speculate on a fake NVDA acquisition. |
| 2026-10-22 19:45 | QQQ | other | no model | no model | 100% / 0% / 0% / 0% | Users discuss QQQ price movements, options strategies, and market sentiment with mixed bullish and bearish views. |
| 2026-10-22 19:45 | VST | other | no model | no model | 100% / 20% / 20% / 0% | Users discuss VST price drops, potential rug pulls, and request pumps. |
| 2026-10-22 19:30 | AMAT | other | no model | no model | 100% / 20% / 0% / 0% | Mixed chatter on AMAT ranging from bearish views on hardware to urgent buy pitches and confusion about bankruptcy. |
| 2026-10-22 18:52 | SOXX | other | no model | no model | 100% / 0% / 0% / 0% | Users discuss SOXX price volatility, express bearish views, and mention a potential earnings-driven rally. |
| 2026-10-22 18:38 | RSP | other | no model | no model | 100% / 0% / 0% / 0% | Users discuss RSP price movements, comparing it to SPY and noting sector rotations. |
| 2026-10-22 17:45 | AAOI | other | no model | no model | 100% / 0% / 0% / 0% | Users discuss AAOI price drops, express confusion about company news, and offer conflicting bullish and bearish opinions. |
| 2026-10-22 17:45 | ORCL | other | no model | no model | 100% / 0% / 0% / 0% | Users discuss ORCL's declining price, bearish outlook, and potential risks to its AI strategy. |
| 2026-10-22 17:45 | TOGI | otc penny | no model | no model | 0% / 0% / 0% / 0% | Chatter discusses a YouTuber named TOGI and their positions on MRNA, unrelated to TurnOnGreen, Inc. |
| 2026-10-22 17:45 | XXII | other | no model | no model | 100% / 23% / 0% / 31% | Users discuss high volume and positive preliminary financials for XXII, urging others to buy without stop losses. |
| 2026-10-22 16:39 | FPS | other | no model | no model | 100% / 0% / 0% / 0% | Users discuss a recent price drop in FPS, citing CFO departure and energy sector trends. |
| 2026-10-22 15:59 | GEV | other | no model | no model | 100% / 0% / 0% / 0% | Users discuss GEV price drops, express bearish sentiment, and create a banbet targeting a $900 price level. |
| 2026-10-22 15:59 | PLTR | other | no model | no model | 100% / 14% / 0% / 0% | Mixed chatter on PLTR price action, with some users expressing bullish optimism and others showing bearish frustration or calling for a decline. |
| 2026-10-22 15:59 | SOXL | other | no model | no model | 100% / 7.5% / 0% / 0% | Users discuss SOXL price volatility, losses, and potential reversals without mentioning specific corporate events. |
| 2026-10-22 14:55 | BKYI | low float runner | no model | no model | 100% / 0% / 0% / 0% | Users discuss BKYI's potential price surge, volume, and short interest following news of a new contract. |
| 2026-10-22 14:55 | SHFS | other | no model | no model | 100% / 50% / 0% / 0% | Users discuss SHFS as a penny stock with high potential and volume, suggesting buy entries. |

## Development walk-forward (flags before 2027-01-04)

Each development week replayed exactly as it would have run: its model trained only on labels available before the week began, scoring that week's candidates. Results count candidates whose label has settled.

### crash

No scored candidate with a settled label yet.

### pump

No scored candidate with a settled label yet.

## Hold-out (flags from 2027-01-04)

Still locked, with 0 hold-out candidates so far. They are scored like any other, but their scores are not compared with their outcomes until collection has finished and every hold-out label has settled; then they are evaluated once, into `model/holdout.md`.
