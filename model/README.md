# Stage 5 model

Updated 2026-10-27T04:53:47Z. Rule `model-v3` (docs/stage5.md on the code branch), written down before any model was trained. Every candidate is scored once, by the LightGBM model of the week it was flagged in (trained on the labels available before that week began, recent ones weighted more), and the score goes into the prospective log `model/predictions.csv`. **crash**: a close 40% or more below the flag price within 10 sessions (the avoid signal, first). **pump**: Stage 4's pump label. A candidate is flagged when its score is at least twice the base rate.

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

## Development walk-forward (flags before 2027-01-04)

Each development week replayed exactly as it would have run: its model trained only on labels available before the week began, scoring that week's candidates. Results count candidates whose label has settled.

### crash

No scored candidate with a settled label yet.

### pump

No scored candidate with a settled label yet.

## Hold-out (flags from 2027-01-04)

Still locked, with 0 hold-out candidates so far. They are scored like any other, but their scores are not compared with their outcomes until collection has finished and every hold-out label has settled; then they are evaluated once, into `model/holdout.md`.
