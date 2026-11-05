# Stage 5 model

Updated 2026-11-05T06:33:08Z. Rule `model-v3` (docs/stage5.md on the code branch), written down before any model was trained. Every candidate is scored once, by the LightGBM model of the week it was flagged in (trained on the labels available before that week began, recent ones weighted more), and the score goes into the prospective log `model/predictions.csv`. **crash**: a close 40% or more below the flag price within 10 sessions (the avoid signal, first). **pump**: Stage 4's pump label. A candidate is flagged when its score is at least twice the base rate.

## This week's models (week of 2026-11-02)

| Target | Status | Trained on | Positives | Base rate | Flag at | Feature groups |
|---|---|---|---|---|---|---|
| crash | trained | 456 rows | 11 | 5.3% | 11% | chatter, text, llm, price_volume, size, short_interest, filings, history, technical |
| pump | no model yet | 452 rows | 2 | - | - | chatter, text, llm, price_volume, size, short_interest, filings, history, technical |

A week's model needs 50 rows and 5 positives whose labels were settled before the week began; a label settles 10 sessions (two weeks) after the flag, 15 after a 50% rise.

What this week's crash model leans on (share of split gain): `volatility_20d` 44%, `days_since_report` 9%, `max_ret_20d` 7%, `institution_pct` 5%, `market_cap_log` 5%, `days_since_dilution` 4%, `turnover_last` 4%, `ret_1d` 3%.

## Latest candidates (last 7 days)

Scores as logged when each candidate was first seen; flagged ones in bold. The LLM column gives the shares of the posts shown that are about the company, pitch it, warn about it and state a company event (counted only when its quote checks out).

| Flagged (UTC) | Ticker | Archetype | Crash risk | Pump risk | LLM about / pitch / warning / event | What the chatter was about |
|---|---|---|---|---|---|---|
| 2026-11-05 04:50 | SOXS | other | 7.3% | no model | 100% / 3.8% / 0% / 0% | Users discuss SOXS price movements, express bullish/bearish opinions, and joke about its history. |
| 2026-11-05 03:15 | SOXL | other | **28%** | no model | 100% / 0% / 0% / 0% | Users discuss SOXL volatility, express pain from losses, debate holding leveraged ETFs, and make bearish price predictions. |
| 2026-11-05 01:08 | SOXX | other | 0.2% | no model | 100% / 0% / 0% / 0% | Users discuss SOXX price movements, leverage mechanics, and market conditions without specific company events or buy pitches. |
| 2026-11-05 00:45 | GEV | other | 0.2% | no model | 100% / 0% / 0% / 0% | Users discuss GEV price movements, ownership, and general market sentiment without specific corporate events. |
| 2026-11-04 22:27 | BROS | other | 0.2% | no model | 100% / 0% / 0% / 10% | Users discuss a sharp price drop and question a recent earnings call for Dutch Bros. |
| 2026-11-04 21:19 | APP | other | 0.1% | no model | 100% / 0% / 0% / 0% | Users discuss Applovin's earnings beat, massive put open interest, and price targets in a highly speculative manner. |
| 2026-11-04 21:19 | COHR | other | 1.2% | no model | 100% / 0% / 0% / 23% | Users discuss COHR earnings, express bearish sentiment, and joke about the stock price dropping. |
| 2026-11-04 21:07 | UUUU | other | 0.1% | no model | 100% / 62% / 0% / 23% | Users discuss UUUU earnings, price targets, and potential stock movements in r/wallstreetbets. |
| 2026-11-04 20:01 | ARM | other | 0.1% | no model | 100% / 0% / 0% / 6.2% | Users discuss ARM earnings, short positions, and potential price drops before the event. |
| 2026-11-04 19:48 | MU | other | 0.1% | no model | 100% / 16% / 0% / 0% | Chatter includes hype, price targets, and confusion over a price drop, with no specific corporate events mentioned. |
| 2026-11-04 19:21 | MCD | other | 0.1% | no model | 100% / 0% / 0% / 0% | Users discuss MCD price gains, ownership, and general market sentiment without specific events or pitches. |
| 2026-11-04 18:32 | NBIS | other | 0.1% | no model | 100% / 0% / 5.0% / 0% | Users express extreme bearish sentiment, calling the stock a scam or pump-and-dump, while some speculate on a potential rebound. |
| 2026-11-04 18:32 | USO | other | 0.1% | no model | 100% / 0% / 0% / 0% | Users discuss USO price movements, geopolitical tensions with Iran, and trading strategies involving puts and calls. |
| 2026-11-04 18:08 | CRWV | other | 0.2% | no model | 100% / 18% / 15% / 0% | Chatter is overwhelmingly bearish, with users calling CRWV a scam, predicting insolvency, and warning of a pump-and-dump. |
| 2026-11-04 18:08 | IREN | other | 0.2% | no model | 100% / 0% / 0% / 3.3% | Mixed chatter regarding IREN data center policies, earnings expectations, and potential regulatory headwinds. |
| 2026-11-04 18:08 | QCOM | other | 0.1% | no model | 100% / 0% / 0% / 14% | Users discuss QCOM earnings, potential price moves, and specific financial data in a bearish to neutral tone. |
| 2026-11-04 15:47 | DUOL | other | 0.1% | no model | 100% / 10% / 20% / 0% | Users discuss potential earnings leaks, massive price spikes, and extreme volatility for DUOL. |
| 2026-11-04 15:47 | VST | other | 0.1% | no model | 100% / 0% / 0% / 0% | Users discuss VST price drops, political news, and express bearish sentiment without specific company events. |
| 2026-11-04 15:35 | UBER | other | 0.1% | no model | 100% / 0% / 0% / 0% | Users discuss UBER stock ownership, price targets, and robotaxi growth without specific company events. |
| 2026-11-04 14:40 | DJT | other | 0.1% | no model | 100% / 0% / 0% / 0% | Chatter includes jokes, shorting calls, and confusion about the stock's identity and recent performance. |
| 2026-11-04 14:27 | TSLA | other | 0.0% | no model | 100% / 0% / 0% / 0% | Users discuss TSLA's price drop, attributing it to Elon Musk's political involvement and potential investigations. |
| 2026-11-04 13:44 | PARA | low float runner | **77%** | no model | 100% / 10% / 0% / 0% | Chatter focuses on PARA price movements, breakouts, and a trading recap showing significant gains. |
| 2026-11-04 13:44 | TLT | other | 0.2% | no model | 100% / 0% / 0% / 0% | Users discuss TLT price movements, dividends, and market correlations without specific corporate events. |
| 2026-11-04 13:20 | MRNA | other | 0.2% | no model | 100% / 0% / 0% / 0% | Users express confusion and frustration over Moderna's unexpected price rise, with some admitting short squeezes. |
| 2026-11-04 12:50 | DXYZ | other | 0.1% | no model | 100% / 30% / 10% / 0% | Users discuss DXYZ's potential rise due to an Anthropic IPO, with mixed sentiments on dilution and valuation. |
| 2026-11-04 07:16 | FSLR | other | 0.1% | no model | 100% / 9.1% / 0% / 0% | Users discuss FSLR price movements, political context, and express bullish optimism or caution regarding potential pumps. |
| 2026-11-04 05:49 | SPCX | other | 0.1% | no model | 100% / 0% / 0% / 0% | Users discuss SPCX price drops, Elon Musk's political troubles, and potential nationalization or merger rumors. |
| 2026-11-04 01:25 | SGOV | other | 0.2% | no model | 100% / 0% / 0% / 0% | Users discuss SGOV as a safe cash alternative and express relief at holding it during market volatility. |
| 2026-11-03 23:11 | NVTS | other | 0.4% | no model | 100% / 0% / 0% / 30% | Users discuss NVTS earnings, price movements, and express bullish or bearish opinions. |
| 2026-11-03 22:03 | DAMD | other | **41%** | no model | 100% / 0% / 0% / 0% | Users discuss buying the inverse AMD ETF to short the underlying stock. |
| 2026-11-03 21:29 | ALAB | other | 0.4% | no model | 100% / 0% / 0% / 0% | Users discuss ALAB in relation to a college semiconductor event and speculate on its price movement. |
| 2026-11-03 21:29 | AMC | other | 0.1% | no model | 90% / 10% / 0% / 10% | Users discuss AMC stock, mentioning Citadel, earnings, and potential fat-finger errors. |
| 2026-11-03 21:29 | ANET | other | 0.1% | no model | 100% / 0% / 0% / 0% | Mixed chatter regarding ANET stock performance, insider selling concerns, and general market sentiment. |
| 2026-11-03 18:57 | DDOG | other | 0.2% | no model | 100% / 10% / 0% / 0% | Users discuss DDOG stock prices, express hope for recovery, and mention buying calls. |
| 2026-11-03 17:35 | TSM | other | 0.1% | no model | 100% / 0% / 0% / 0% | Users discuss TSM price movements, supply chain issues, and express bullish sentiment with no specific company events mentioned. |
| 2026-11-03 15:08 | AEHR | other | 0.6% | no model | 100% / 60% / 0% / 30% | Users discuss AEHR earnings, short squeeze potential, and express bullish expectations for a price pump. |
| 2026-11-03 14:58 | OKLO | other | 0.1% | no model | 100% / 0% / 0% / 0% | Users discuss OKLO price history, portfolio performance, and express confusion or regret over recent losses. |
| 2026-11-03 08:03 | IREN | other | 0.4% | no model | 100% / 9.1% / 0% / 4.5% | Mixed chatter on IREN ranging from bullish earnings rumors to bearish price targets and jokes. |
| 2026-11-03 07:23 | APLD | other | 0.2% | no model | 100% / 0% / 0% / 0% | Users express extreme distress, massive losses, and frustration over the stock's decline. |
| 2026-11-03 00:57 | AAOI | other | 1.2% | no model | 100% / 35% / 0% / 24% | Users discuss AAOI earnings, potential AMD partnership rumors, valuation, and recent dilution. |

## Development walk-forward (flags before 2027-01-04)

Each development week replayed exactly as it would have run: its model trained only on labels available before the week began, scoring that week's candidates. Results count candidates whose label has settled.

### crash

| Candidates | n | Positives | Base rate | Flagged | Precision | Recall | F1 | Lift | AP | AUC |
|---|---|---|---|---|---|---|---|---|---|---|
| all candidates | 1 | 1 | 100% | 1 | 100% | 100% | 1.00 | 1.0x | 1.00 | - |
| low float runner | 1 | 1 | 100% | 1 | 100% | 100% | 1.00 | 1.0x | 1.00 | - |
| pump types together | 1 | 1 | 100% | 1 | 100% | 100% | 1.00 | 1.0x | 1.00 | - |

| Model | AP | Precision | Recall | F1 |
|---|---|---|---|---|
| all groups | 1.00 | 100% | 100% | 1.00 |
| market only | 1.00 | 100% | 100% | 1.00 |
| social only | 1.00 | 100% | 100% | 1.00 |

| Robustness check | Result | Detail |
|---|---|---|
| beats the base rate | not enough data | 1 positives (needs 10) |
| separate periods | not enough data | needs 3 positives in each of three blocks of weeks |
| per pump type | not enough data | needs 5 positives in a pump type |
| beats the control group | not enough data | 0 flagged with settled controls (needs 10) |
| survives slippage | not enough data | 0 flagged with a 10-session return (needs 10) |

Verdict: **not robust yet** (some checks need more labels).

Feature groups: all used; weak groups are pruned once the replay holds 20 positive candidates (1 so far).

### pump

No scored candidate with a settled label yet.

## Hold-out (flags from 2027-01-04)

Still locked, with 0 hold-out candidates so far. They are scored like any other, but their scores are not compared with their outcomes until collection has finished and every hold-out label has settled; then they are evaluated once, into `model/holdout.md`.
