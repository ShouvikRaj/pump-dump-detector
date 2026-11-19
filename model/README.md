# Stage 5 model

Updated 2026-11-19T00:18:39Z. Rule `model-v3` (docs/stage5.md on the code branch), written down before any model was trained. Every candidate is scored once, by the LightGBM model of the week it was flagged in (trained on the labels available before that week began, recent ones weighted more), and the score goes into the prospective log `model/predictions.csv`. **crash**: a close 40% or more below the flag price within 10 sessions (the avoid signal, first). **pump**: Stage 4's pump label. A candidate is flagged when its score is at least twice the base rate.

## This week's models (week of 2026-11-16)

| Target | Status | Trained on | Positives | Base rate | Flag at | Feature groups |
|---|---|---|---|---|---|---|
| crash | trained | 955 rows | 24 | 6.8% | 14% | chatter, text, llm, price_volume, size, short_interest, filings, history, technical |
| pump | no model yet | 953 rows | 4 | - | - | chatter, text, llm, price_volume, size, short_interest, filings, history, technical |

A week's model needs 50 rows and 5 positives whose labels were settled before the week began; a label settles 10 sessions (two weeks) after the flag, 15 after a 50% rise.

What this week's crash model leans on (share of split gain): `volatility_20d` 34%, `si_days_to_cover` 9%, `days_since_report` 4%, `turnover_last` 4%, `pennystocks_share` 3%, `authors_ratio` 3%, `ret_1d` 2%, `ret_5d` 2%.

## Latest candidates (last 7 days)

Scores as logged when each candidate was first seen; flagged ones in bold. The LLM column gives the shares of the posts shown that are about the company, pitch it, warn about it and state a company event (counted only when its quote checks out).

| Flagged (UTC) | Ticker | Archetype | Crash risk | Pump risk | LLM about / pitch / warning / event | What the chatter was about |
|---|---|---|---|---|---|---|
| 2026-11-18 21:40 | PANW | other | 0.8% | no model | 100% / 9.1% / 0% / 9.1% | Chatter focuses on PANW's massive AI acquisition, earnings results, and extremely high valuation metrics. |
| 2026-11-18 17:15 | UNH | other | 0.1% | no model | 100% / 0% / 0% / 0% | Users express confusion and anger over UNH's significant price drop, with some selling shares and mocking the company. |
| 2026-11-17 23:46 | AAOI | other | **23%** | no model | 100% / 27% / 6.7% / 6.7% | Chatter includes jokes, price movements, dilution concerns, and mixed buy/sell sentiments regarding AAOI. |
| 2026-11-17 21:20 | HSBC | other | 0.0% | no model | 100% / 0% / 0% / 9.1% | Users discuss HSBC selling a loan and express skepticism about the bank's AI strategy and reputation. |
| 2026-11-17 18:16 | SOXX | other | 1.8% | no model | 100% / 14% / 0% / 0% | Users discuss SOXX price movements, sector trends, and express bullish or bearish opinions on the semiconductor index fund. |
| 2026-11-17 16:08 | SPCX | other | 1.5% | no model | 100% / 0% / 0% / 0% | Chatter discusses SPCX's IPO performance, potential merger with TSLA, and compares it to other tech stocks like ANT. |
| 2026-11-17 14:06 | SPAI | low float runner | **22%** | no model | 100% / 30% / 0% / 0% | Users discuss SPAI stock, citing growth, earnings, and specific price targets with rapid buying and selling. |
| 2026-11-17 12:33 | SLS | other | 3.6% | no model | 100% / 14% / 4.5% / 9.1% | Chatter discusses SLS trading halt, potential buyout rumors, and a Phase 3 clinical trial success announcement. |
| 2026-11-17 10:45 | SHAZ | other | 4.3% | no model | 100% / 0% / 0% / 0% | Users discuss a major shareholder's massive losses and the stock's sharp decline, mocking the investor. |
| 2026-11-17 10:05 | JPM | other | 0.1% | no model | 100% / 0% / 0% / 0% | Users discuss a software bug and outage affecting JPM and other banks, while others mention buybacks. |
| 2026-11-17 10:05 | SNDK | other | **33%** | no model | 100% / 0% / 0% / 0% | Chatter discusses SNDK price drops, compares it to other tech stocks, and mentions a user's call positions. |
| 2026-11-17 06:59 | ROPE | other | 0.2% | no model | 100% / 55% / 0% / 0% | Users discuss buying ROPE, with some urging others to go all-in. |
| 2026-11-17 03:38 | RSP | other | 0.1% | no model | 100% / 0% / 0% / 0% | Users discuss RSP as a broad market ETF alternative to concentrated tech stocks, noting its performance and holding it in portfolios. |
| 2026-11-17 03:28 | ASTS | other | 8.4% | no model | 100% / 0% / 0% / 0% | Users discuss ASTS performance, compare it to SpaceX and RKLB, and debate its financial viability and future prospects. |
| 2026-11-17 01:13 | TQQQ | other | **23%** | no model | 100% / 0% / 0% / 0% | Users discuss TQQQ volatility, losses, and trading strategies with mixed sentiment. |
| 2026-11-17 00:48 | INTC | other | 12% | no model | 100% / 0% / 0% / 0% | Users discuss a shareholder lawsuit, Nvidia selling Intel shares, and general bearish sentiment regarding Intel's stock performance. |
| 2026-11-17 00:31 | VOO | other | 0.2% | no model | 100% / 0% / 0% / 0% | Users discuss VOO as a safe index fund alternative to risky individual stocks. |
| 2026-11-16 23:04 | PLTR | other | 0.2% | no model | 100% / 0% / 0% / 0% | Users discuss PLTR holdings, joke about price drops, and mention potential post-earnings sell-offs without specific event details. |
| 2026-11-16 22:11 | RCAT | other | 4.8% | no model | 100% / 0% / 0% / 0% | Users discuss RCAT's poor earnings performance, price decline, and potential delisting. |
| 2026-11-16 20:09 | LXEO | other | 1.8% | no model | 100% / 20% / 0% / 20% | Users discuss LXEO price targets, analyst upgrades, and potential entry points based on trial news. |
| 2026-11-16 18:57 | IREN | other | 3.5% | no model | 100% / 0% / 10% / 3.3% | Users discuss IREN's price, express extreme bearishness, question its legitimacy as a scam, and mention an Intel stake. |
| 2026-11-16 15:08 | HOOD | other | 0.3% | no model | 100% / 0% / 0% / 0% | Users discuss HOOD price, express confusion, fear of a drop, and mention buying alongside other stocks. |
| 2026-11-16 07:17 | WMT | other | 0.1% | no model | 100% / 0% / 0% / 0% | Users discuss WMT valuation, earnings impact, and holiday shopping trends with mixed bearish and neutral sentiment. |
| 2026-11-15 23:05 | ASML | other | 0.1% | no model | 100% / 0% / 0% / 0% | Discussions focus on ASML's monopoly, export bans to China, and technological barriers preventing reverse engineering. |
| 2026-11-15 21:05 | COIN | other | 0.1% | no model | 90% / 0% / 0% / 0% | Users discuss COIN's performance relative to crypto market trends and compare it to other stocks. |
| 2026-11-15 07:52 | TSM | other | 0.3% | no model | 100% / 0% / 0% / 0% | Users discuss geopolitical tensions involving Taiwan and TSM, with mixed opinions on stock impact and some jokes. |
| 2026-11-14 23:53 | DXYZ | other | 0.1% | no model | 100% / 6.7% / 13% / 0% | Users discuss DXYZ's performance relative to the Anthropic IPO, debating its value as a fund versus a scam. |
| 2026-11-14 03:08 | LHX | other | 0.1% | no model | 100% / 0% / 0% / 10% | Users discuss LHX price drops, shorting activity, and joke about a flight grounding event. |
| 2026-11-14 02:06 | WMT | other | 0.2% | no model | 100% / 40% / 0% / 0% | Mixed chatter on WMT ranging from bullish mooning claims to bearish recession warnings and general portfolio mentions. |
| 2026-11-14 01:03 | HSBC | other | 0.1% | no model | 90% / 0% / 0% / 0% | Users discuss HSBC's reputation for money laundering, a downgrade, and express strong negative sentiment. |
| 2026-11-14 00:36 | DHS | other | 0.1% | no model | 0% / 0% / 0% / 0% | All documents discuss the Department of Homeland Security, not the WisdomTree U.S. High Dividend Fund. |
| 2026-11-13 23:41 | NWS | other | 0.1% | no model | 0% / 0% / 0% / 0% | Chatter discusses a nationwide outage of the US National Weather Service, not the stock. |
| 2026-11-13 22:10 | ATC | other | 0.5% | no model | 0% / 0% / 0% / 0% | All documents discuss an unrelated Air Traffic Control system outage, not the GraniteShares Autocallable COIN ETF. |
| 2026-11-13 19:02 | IWM | other | 0.3% | no model | 100% / 0% / 0% / 0% | Users discuss IWM price action, technical breaches, and general market sentiment without specific company events. |
| 2026-11-13 16:24 | XLAB | other | 8.4% | no model | 100% / 55% / 9.1% / 0% | Users discuss increasing volume, potential short squeezes, and weekend selling pressure for XLAB. |
| 2026-11-13 15:04 | TSLA | other | 0.1% | no model | 100% / 0% / 7.5% / 7.5% | Chatter discusses a potential Tesla-SpaceX merger, Elon Musk's role, and a suspicious price pump. |
| 2026-11-13 14:07 | SMU | other | **39%** | no model | 0% / 0% / 0% / 0% | Chatter discusses SMU as a university and mocks Colette Kress's background, unrelated to the stock. |
| 2026-11-13 13:30 | AIMD | other | **22%** | no model | 100% / 50% / 0% / 10% | Users discuss a recent $9M contract announcement and speculate on price increases for AIMD. |
| 2026-11-13 13:15 | ARM | other | 4.0% | no model | 100% / 0% / 0% / 0% | Users discuss potential CEO changes, hiring rumors, and technical comparisons regarding ARM Holdings. |
| 2026-11-13 10:58 | CRWD | other | 0.1% | no model | 100% / 0% / 0% / 0% | Users discuss CRWD price movements, valuation concerns, and potential future performance in r/wallstreetbets. |

## Development walk-forward (flags before 2027-01-04)

Each development week replayed exactly as it would have run: its model trained only on labels available before the week began, scoring that week's candidates. Results count candidates whose label has settled.

### crash

| Candidates | n | Positives | Base rate | Flagged | Precision | Recall | F1 | Lift | AP | AUC |
|---|---|---|---|---|---|---|---|---|---|---|
| all candidates | 70 | 8 | 11% | 9 | 78% | 88% | 0.82 | 6.8x | 0.81 | 0.89 |
| low float runner | 2 | 2 | 100% | 2 | 100% | 100% | 1.00 | 1.0x | 1.00 | - |
| other | 68 | 6 | 8.8% | 7 | 71% | 83% | 0.77 | 8.1x | 0.71 | 0.85 |
| pump types together | 2 | 2 | 100% | 2 | 100% | 100% | 1.00 | 1.0x | 1.00 | - |

| Model | AP | Precision | Recall | F1 |
|---|---|---|---|---|
| all groups | 0.81 | 78% | 88% | 0.82 |
| market only | 0.80 | 78% | 88% | 0.82 |
| social only | 0.74 | 71% | 62% | 0.67 |

| Robustness check | Result | Detail |
|---|---|---|
| beats the base rate | not enough data | 8 positives (needs 10) |
| separate periods | not enough data | needs 3 positives in each of three blocks of weeks |
| per pump type | not enough data | needs 5 positives in a pump type |
| beats the control group | not enough data | 3 flagged with settled controls (needs 10) |
| survives slippage | not enough data | 3 flagged with a 10-session return (needs 10) |

Verdict: **not robust yet** (some checks need more labels).

Feature groups: all used; weak groups are pruned once the replay holds 20 positive candidates (8 so far).

### pump

No scored candidate with a settled label yet.

## Hold-out (flags from 2027-01-04)

Still locked, with 0 hold-out candidates so far. They are scored like any other, but their scores are not compared with their outcomes until collection has finished and every hold-out label has settled; then they are evaluated once, into `model/holdout.md`.
