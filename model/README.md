# Stage 5 model

Updated 2026-11-11T05:59:07Z. Rule `model-v3` (docs/stage5.md on the code branch), written down before any model was trained. Every candidate is scored once, by the LightGBM model of the week it was flagged in (trained on the labels available before that week began, recent ones weighted more), and the score goes into the prospective log `model/predictions.csv`. **crash**: a close 40% or more below the flag price within 10 sessions (the avoid signal, first). **pump**: Stage 4's pump label. A candidate is flagged when its score is at least twice the base rate.

## This week's models (week of 2026-11-09)

| Target | Status | Trained on | Positives | Base rate | Flag at | Feature groups |
|---|---|---|---|---|---|---|
| crash | trained | 677 rows | 15 | 5.3% | 11% | chatter, text, llm, price_volume, size, short_interest, filings, history, technical |
| pump | no model yet | 675 rows | 3 | - | - | chatter, text, llm, price_volume, size, short_interest, filings, history, technical |

A week's model needs 50 rows and 5 positives whose labels were settled before the week began; a label settles 10 sessions (two weeks) after the flag, 15 after a 50% rise.

What this week's crash model leans on (share of split gain): `volatility_20d` 44%, `days_since_report` 7%, `market_cap_log` 6%, `turnover_last` 5%, `vol_60m_rel` 4%, `institution_pct` 3%, `wsb_share` 3%, `ret_1d` 3%.

## Latest candidates (last 7 days)

Scores as logged when each candidate was first seen; flagged ones in bold. The LLM column gives the shares of the posts shown that are about the company, pitch it, warn about it and state a company event (counted only when its quote checks out).

| Flagged (UTC) | Ticker | Archetype | Crash risk | Pump risk | LLM about / pitch / warning / event | What the chatter was about |
|---|---|---|---|---|---|---|
| 2026-11-10 21:21 | RGTI | other | 0.5% | no model | 100% / 9.1% / 0% / 64% | Chatter focuses on Rigetti Computing earnings results, with mixed reactions ranging from bearish disappointment to bullish price targets. |
| 2026-11-10 20:00 | CRWV | other | 0.2% | no model | 100% / 0% / 0% / 0% | Chatter focuses on CRWV earnings anticipation, sector correlations, and mixed sentiment regarding potential price moves. |
| 2026-11-10 19:20 | MSTR | other | 0.5% | no model | 100% / 0% / 0% / 0% | Users discuss MSTR price movements, express skepticism about Michael Saylor's funds, and debate the stock's legitimacy. |
| 2026-11-10 17:08 | GLD | other | 0.1% | no model | 100% / 0% / 0% / 0% | Users discuss GLD trading strategies, profits, and price movements without mentioning specific corporate events. |
| 2026-11-10 16:24 | TTWO | other | 0.1% | no model | 100% / 0% / 0% / 0% | Users discuss TTWO stock price movements, GTA 6 hype, and earnings reactions without specific company events. |
| 2026-11-10 15:44 | GEV | other | 0.0% | no model | 82% / 18% / 0% / 0% | Chatter includes jokes, price targets, and confusion about a 'Chinese spy' rumor regarding GE Vernova. |
| 2026-11-09 23:23 | MSS | other | 10% | no model | 0% / 0% / 0% / 0% | All documents discuss the Chinese Ministry of State Security (MSS) and Alice Huang, not Maison Solutions Inc. |
| 2026-11-09 22:33 | ASTS | other | 1.4% | no model | 100% / 5.0% / 0% / 0% | Chatter focuses on ASTS stock performance relative to RKLB, with mixed opinions, jokes, and speculation about earnings or reports. |
| 2026-11-09 22:18 | ASML | other | 0.2% | no model | 100% / 0% / 0% / 0% | Users discuss ASML espionage rumors, joke about blueprints, and express general bearishness without specific events. |
| 2026-11-09 22:18 | IVF | low float runner | **29%** | no model | 0% / 0% / 0% / 0% | All documents discuss Elon Musk's children and IVF procedures, unrelated to the stock. |
| 2026-11-09 21:25 | HIMS | other | 1.5% | no model | 100% / 0% / 0% / 0% | Users discuss HIMS stock price drops, earnings expectations, and joke about product changes. |
| 2026-11-09 21:25 | RKLB | other | 0.5% | no model | 92% / 0% / 7.5% / 12% | Users discuss RKLB earnings, express bearish sentiment, joke about the stock name, and warn of dilution. |
| 2026-11-09 21:11 | TTD | other | 0.2% | no model | 100% / 30% / 0% / 0% | Users discuss TTD price movements, express exhaustion from volatility, and speculate on future gains. |
| 2026-11-09 20:48 | OMH | other | **34%** | no model | 100% / 0% / 0% / 0% | Users discuss OMH price movements, express confusion, and compare it to other stocks without specific company events. |
| 2026-11-09 20:48 | ONDS | other | 0.2% | no model | 100% / 0% / 0% / 10% | Users discuss holding Ondas Inc for earnings, set price targets, and joke about the stock's potential rise. |
| 2026-11-09 15:56 | AVGO | other | 0.1% | no model | 100% / 0% / 0% / 0% | Users discuss AVGO price movements, sector rotation, and potential risks while some express bullish intent. |
| 2026-11-09 15:04 | NNN | other | 0.0% | no model | 0% / 0% / 0% / 0% | All documents refer to NNN as a slang term for masturbation, not the stock. |
| 2026-11-09 13:52 | CVS | other | 0.0% | no model | 100% / 0% / 0% / 10% | Users discuss CVS's potential breakup, poor customer service, and high prices, with no specific corporate events mentioned. |
| 2026-11-09 11:01 | NYT | other | 0.0% | no model | 0% / 0% / 0% / 0% | All documents discuss a New York Times article about Nvidia CEO Jensen Huang's alleged espionage and affair, not the stock. |
| 2026-11-09 00:16 | NVDA | other | 0.1% | no model | 100% / 12% / 0% / 0% | Chatter focuses on Jensen Huang's personal scandal and its potential impact on NVDA stock price. |
| 2026-11-07 11:05 | GME | other | 0.0% | no model | 100% / 0% / 0% / 0% | Users discuss GME's history, warn against squeeze plays, and debate its current investment viability. |
| 2026-11-07 03:40 | RKLB | other | 0.1% | no model | 100% / 0% / 0% / 0% | Users discuss RKLB price action, earnings expectations, and bearish sentiment regarding high capex and potential dilution. |
| 2026-11-07 02:18 | SPCE | other | 0.1% | no model | 100% / 50% / 20% / 0% | Users discuss SPCE price movements, joke about Elon Musk, and reference a past pump-and-dump scheme. |
| 2026-11-06 20:47 | LUNR | other | 0.3% | no model | 100% / 10% / 0% / 0% | Users discuss LUNR price movements, compare it to other stocks, and make bullish jokes without citing specific corporate events. |
| 2026-11-06 18:22 | VIVK | other | **77%** | no model | 100% / 0% / 0% / 0% | Chatter discusses VIVK price spikes, trading volume, and a halted status without specific company events. |
| 2026-11-06 18:13 | ORCL | other | 1.6% | no model | 100% / 0% / 0% / 25% | Chatter discusses a Microsoft deal wind-down causing Oracle stock to drop, with mixed reactions from bearish to skeptical. |
| 2026-11-06 18:01 | GRND | other | 0.1% | no model | 100% / 0% / 0% / 20% | Chatter includes an AMA announcement, earnings results, and mixed speculative comments on Grindr stock. |
| 2026-11-06 16:54 | WDC | other | 0.4% | no model | 100% / 0% / 0% / 0% | Users express bearish sentiment, discuss price drops, and question the company's future viability. |
| 2026-11-06 15:46 | INOD | other | 2.4% | no model | 100% / 8.7% / 4.3% / 8.7% | Chatter focuses on INOD earnings results, price targets, and a subsequent sell-off described as a rug pull. |
| 2026-11-06 14:52 | DKNG | other | 0.4% | no model | 100% / 10% / 0% / 0% | Users discuss DKNG's price drop, compare it to semis, and express bearish views on its performance. |
| 2026-11-06 09:05 | KORU | other | **27%** | no model | 100% / 0% / 0% / 0% | Users discuss KORU's severe decline, hedge fund failures, and personal losses without any promotional activity. |
| 2026-11-06 07:56 | ASTS | other | 0.3% | no model | 100% / 0% / 0% / 2.5% | Users discuss severe losses, bag holding, and skepticism regarding ASTS fundamentals and upcoming earnings. |
| 2026-11-06 07:56 | TQQQ | other | 8.4% | no model | 100% / 10% / 0% / 0% | Users discuss holding, buying, and price targets for TQQQ with mixed bullish and bearish sentiments. |
| 2026-11-06 04:28 | LABT | other | **16%** | no model | 100% / 10% / 0% / 0% | Users discuss $LABT price targets, recent gains, and breakout patterns without mentioning specific corporate events. |
| 2026-11-06 03:36 | UVXY | other | 9.5% | no model | 100% / 0% / 0% / 0% | Users discuss UVXY volatility, recent gains, and potential crashes due to falling volume. |
| 2026-11-06 02:44 | QQQ | other | 0.5% | no model | 100% / 0% / 0% / 0% | Users discuss QQQ price movements, option trades, and market sentiment without mentioning specific corporate events. |
| 2026-11-06 00:59 | EWY | other | 1.4% | no model | 100% / 0% / 0% / 0% | Users discuss EWY price movements relative to KOSPI and joke about Korean market volatility. |
| 2026-11-06 00:59 | SPY | other | 0.4% | no model | 100% / 0% / 0% / 0% | Users discuss SPY options trading, market volatility, and potential price movements without specific company events. |
| 2026-11-05 23:26 | SGOV | other | 0.3% | no model | 100% / 0% / 0% / 0% | Users discuss holding SGOV for tax-free yields and compare it to volatile stocks, with no specific corporate events mentioned. |
| 2026-11-05 23:10 | VTI | other | 0.6% | no model | 100% / 0% / 0% / 0% | Users discuss buying, selling, and holding VTI as a safe investment or diversification tool. |

## Development walk-forward (flags before 2027-01-04)

Each development week replayed exactly as it would have run: its model trained only on labels available before the week began, scoring that week's candidates. Results count candidates whose label has settled.

### crash

| Candidates | n | Positives | Base rate | Flagged | Precision | Recall | F1 | Lift | AP | AUC |
|---|---|---|---|---|---|---|---|---|---|---|
| all candidates | 3 | 3 | 100% | 3 | 100% | 100% | 1.00 | 1.0x | 1.00 | - |
| low float runner | 1 | 1 | 100% | 1 | 100% | 100% | 1.00 | 1.0x | 1.00 | - |
| other | 2 | 2 | 100% | 2 | 100% | 100% | 1.00 | 1.0x | 1.00 | - |
| pump types together | 1 | 1 | 100% | 1 | 100% | 100% | 1.00 | 1.0x | 1.00 | - |

| Model | AP | Precision | Recall | F1 |
|---|---|---|---|---|
| all groups | 1.00 | 100% | 100% | 1.00 |
| market only | 1.00 | 100% | 100% | 1.00 |
| social only | 1.00 | 100% | 100% | 1.00 |

| Robustness check | Result | Detail |
|---|---|---|
| beats the base rate | not enough data | 3 positives (needs 10) |
| separate periods | not enough data | needs 3 positives in each of three blocks of weeks |
| per pump type | not enough data | needs 5 positives in a pump type |
| beats the control group | not enough data | 0 flagged with settled controls (needs 10) |
| survives slippage | not enough data | 0 flagged with a 10-session return (needs 10) |

Verdict: **not robust yet** (some checks need more labels).

Feature groups: all used; weak groups are pruned once the replay holds 20 positive candidates (3 so far).

### pump

No scored candidate with a settled label yet.

## Hold-out (flags from 2027-01-04)

Still locked, with 0 hold-out candidates so far. They are scored like any other, but their scores are not compared with their outcomes until collection has finished and every hold-out label has settled; then they are evaluated once, into `model/holdout.md`.
