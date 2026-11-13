# Stage 5 model

Updated 2026-11-13T00:18:36Z. Rule `model-v3` (docs/stage5.md on the code branch), written down before any model was trained. Every candidate is scored once, by the LightGBM model of the week it was flagged in (trained on the labels available before that week began, recent ones weighted more), and the score goes into the prospective log `model/predictions.csv`. **crash**: a close 40% or more below the flag price within 10 sessions (the avoid signal, first). **pump**: Stage 4's pump label. A candidate is flagged when its score is at least twice the base rate.

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
| 2026-11-12 21:20 | CSCO | other | 0.0% | no model | 100% / 0% / 0% / 0% | Users discuss CSCO options pricing, compare it to NVDA/AMAT, and react to potential earnings beats. |
| 2026-11-12 20:54 | MSFT | other | 0.1% | no model | 100% / 0% / 0% / 0% | Users discuss a major Microsoft Outlook outage, expressing skepticism about the stock's resilience and calling for short positions. |
| 2026-11-12 20:43 | ASML | other | 0.0% | no model | 100% / 0% / 0% / 0% | Users discuss ASML's market position, EUV technology, and geopolitical tensions with China. |
| 2026-11-12 18:42 | AMAT | other | 0.1% | no model | 100% / 0% / 0% / 10% | Users discuss AMAT earnings, express bearish sentiment, and speculate on potential stock drops. |
| 2026-11-12 18:15 | GLD | other | 0.1% | no model | 100% / 0% / 0% / 0% | Users discuss GLD price movements, express bearish views, and speculate on future drops without mentioning specific corporate events. |
| 2026-11-12 17:47 | SMCI | other | 0.2% | no model | 100% / 0% / 0% / 0% | Users discuss SMCI's stock drop due to regulatory probes and Jensen's scandal, with no promotional pitches found. |
| 2026-11-12 17:34 | TRT | low float runner | 0.3% | no model | 0% / 0% / 0% / 0% | All documents discuss TRT as a medical treatment for Jensen, not the stock Trio-Tech International. |
| 2026-11-12 17:04 | PARA | other | **95%** | no model | 100% / 10% / 0% / 10% | Users discuss trading PARA, noting a price target and recent filings, with mixed sentiment on potential moves. |
| 2026-11-12 16:56 | CBRS | other | 0.1% | no model | 100% / 0% / 0% / 0% | Users discuss CBRS price movements, earnings anticipation, and potential volatility without confirming specific scheduled events. |
| 2026-11-12 16:04 | PLCE | other | **14%** | no model | 100% / 10% / 0% / 0% | Users discuss PLCE price movements, potential pumps, and scalp opportunities in penny stock forums. |
| 2026-11-12 14:43 | LUNR | other | 2.1% | no model | 100% / 0% / 0% / 29% | Users discuss LUNR earnings, price movements, and express bullish or bearish opinions on the stock. |
| 2026-11-12 05:40 | SLI | other | 0.6% | no model | 0% / 0% / 0% / 0% | All documents discuss Jensen Huang and Nvidia's SLI technology, not Standard Lithium Ltd. |
| 2026-11-12 05:14 | AMD | other | 2.8% | no model | 100% / 0% / 0% / 0% | Chatter discusses AMD stock price movements, potential NVDA/AMD executive connections, and mixed bullish/bearish opinions. |
| 2026-11-12 03:27 | NXXT | low float runner | **93%** | no model | 100% / 0% / 10% / 10% | Discussions cover NXXT's massive price surge, frequent trading halts, delisting announcements, and potential scam accusations. |
| 2026-11-12 01:54 | GME | other | 0.2% | no model | 100% / 12% / 0% / 5.9% | Users discuss GME options, past trading experiences, and joke about a fake NVDA acquisition. |
| 2026-11-12 01:02 | NYT | other | 0.1% | no model | 0% / 0% / 0% / 0% | All documents discuss an affair involving Nvidia's CEO, not the New York Times Company stock. |
| 2026-11-12 01:02 | OUST | other | 4.7% | no model | 0% / 0% / 0% / 0% | All documents discuss NVIDIA CEO Jensen Huang, not Ouster, Inc. |
| 2026-11-11 15:26 | MSFT | other | 0.3% | no model | 100% / 0% / 0% / 0% | Users discuss MSFT price movements, AI competition with Anthropic, and trade positions without specific corporate events. |
| 2026-11-11 12:32 | NBIS | other | 1.2% | no model | 100% / 0% / 0% / 0% | Chatter focuses on NBIS price action, upcoming earnings, and bullish sentiment regarding CoreWeave news. |
| 2026-11-11 07:39 | NVDL | other | 2.8% | no model | 100% / 0% / 0% / 0% | Users discuss buying, selling, and holding strategies for the NVDL ETF with mixed sentiment. |
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

## Development walk-forward (flags before 2027-01-04)

Each development week replayed exactly as it would have run: its model trained only on labels available before the week began, scoring that week's candidates. Results count candidates whose label has settled.

### crash

| Candidates | n | Positives | Base rate | Flagged | Precision | Recall | F1 | Lift | AP | AUC |
|---|---|---|---|---|---|---|---|---|---|---|
| all candidates | 4 | 4 | 100% | 4 | 100% | 100% | 1.00 | 1.0x | 1.00 | - |
| low float runner | 1 | 1 | 100% | 1 | 100% | 100% | 1.00 | 1.0x | 1.00 | - |
| other | 3 | 3 | 100% | 3 | 100% | 100% | 1.00 | 1.0x | 1.00 | - |
| pump types together | 1 | 1 | 100% | 1 | 100% | 100% | 1.00 | 1.0x | 1.00 | - |

| Model | AP | Precision | Recall | F1 |
|---|---|---|---|---|
| all groups | 1.00 | 100% | 100% | 1.00 |
| market only | 1.00 | 100% | 100% | 1.00 |
| social only | 1.00 | 100% | 75% | 0.86 |

| Robustness check | Result | Detail |
|---|---|---|
| beats the base rate | not enough data | 4 positives (needs 10) |
| separate periods | not enough data | needs 3 positives in each of three blocks of weeks |
| per pump type | not enough data | needs 5 positives in a pump type |
| beats the control group | not enough data | 0 flagged with settled controls (needs 10) |
| survives slippage | not enough data | 0 flagged with a 10-session return (needs 10) |

Verdict: **not robust yet** (some checks need more labels).

Feature groups: all used; weak groups are pruned once the replay holds 20 positive candidates (4 so far).

### pump

No scored candidate with a settled label yet.

## Hold-out (flags from 2027-01-04)

Still locked, with 0 hold-out candidates so far. They are scored like any other, but their scores are not compared with their outcomes until collection has finished and every hold-out label has settled; then they are evaluated once, into `model/holdout.md`.
