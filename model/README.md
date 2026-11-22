# Stage 5 model

Updated 2026-11-22T06:34:55Z. Rule `model-v3` (docs/stage5.md on the code branch), written down before any model was trained. Every candidate is scored once, by the LightGBM model of the week it was flagged in (trained on the labels available before that week began, recent ones weighted more), and the score goes into the prospective log `model/predictions.csv`. **crash**: a close 40% or more below the flag price within 10 sessions (the avoid signal, first). **pump**: Stage 4's pump label. A candidate is flagged when its score is at least twice the base rate.

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
| 2026-11-22 00:48 | MSTR | other | 6.2% | no model | 100% / 8.8% / 12% / 0% | Users discuss MSTR's massive losses, debt, dilution fears, and potential for a pump-and-dump scheme. |
| 2026-11-22 00:48 | NYT | other | 0.1% | no model | 0% / 0% / 0% / 0% | Chatter discusses NYT reporting on Jensen Huang, with no mention of the New York Times Company stock. |
| 2026-11-21 03:02 | ASML | other | 0.2% | no model | 100% / 0% / 0% / 0% | Discussion on ASML's role in chip manufacturing, China restrictions, and a user buying shares. |
| 2026-11-21 00:55 | CRWD | other | 0.2% | no model | 100% / 0% / 0% / 21% | Users discuss rumors of a CrowdStrike-Zscaler acquisition and the resulting stock price drop. |
| 2026-11-21 00:55 | VOO | other | 0.3% | no model | 100% / 0% / 0% / 0% | Users discuss VOO performance, compare it to other assets, and debate passive investing strategies. |
| 2026-11-21 00:46 | SNDK | other | **37%** | no model | 100% / 0% / 0% / 0% | Users discuss SNDK's stock price drop, split, and bearish sentiment following a short report. |
| 2026-11-21 00:46 | VWAV | other | **79%** | no model | 100% / 7.7% / 46% / 0% | Users discuss VWAV price drops, warn of manipulation, and joke about the company's circular share swaps. |
| 2026-11-20 18:35 | TLT | other | 0.1% | no model | 100% / 20% / 0% / 0% | Users discuss TLT as a hedge against recession and oil dips, with bullish sentiment and price targets. |
| 2026-11-20 17:56 | ORCL | other | 0.7% | no model | 100% / 0% / 0% / 0% | Users discuss ORCL price movements, past losses, and potential earnings plays without specific event announcements. |
| 2026-11-20 14:10 | AMD | other | 11% | no model | 100% / 0% / 0% / 0% | Chatter focuses on export control allegations, stock price volatility, and bearish sentiment regarding AMD. |
| 2026-11-20 14:10 | SGOV | other | 0.2% | no model | 100% / 0% / 0% / 0% | Users discuss holding SGOV as a safe haven or cash equivalent while waiting for other investments. |
| 2026-11-20 03:06 | INTU | other | 0.2% | no model | 100% / 0% / 0% / 0% | Users discuss INTU's sharp price drop, joke about bankruptcy, and speculate on a move to $150. |
| 2026-11-20 03:06 | ROPE | other | 0.1% | no model | 100% / 18% / 0% / 0% | Users discuss buying $ROPE calls and express bullish opinions on the ETF. |
| 2026-11-20 00:51 | GME | other | 0.2% | no model | 100% / 0% / 0% / 0% | Users discuss GameStop stock, referencing memes, past squeezes, and general bullish sentiment without specific corporate events. |
| 2026-11-20 00:51 | OPEX | other | 9.9% | no model | 100% / 0% / 0% / 0% | Users discuss OPEX ETF volatility, liquidity issues, and market bleeding before an expiration date. |
| 2026-11-19 03:02 | CRWD | other | 0.4% | no model | 100% / 0% / 0% / 8.3% | Users discuss CRWD cybersecurity stock, valuations, and mention upcoming earnings. |
| 2026-11-19 01:56 | MU | other | 6.8% | no model | 100% / 0% / 0% / 0% | Users discuss Micron's earnings, demand, and price targets in a bullish manner. |
| 2026-11-19 00:49 | AMZN | other | 0.1% | no model | 100% / 0% / 0% / 0% | Users discuss AMZN's potential price rise due to an Anthropic IPO and general market optimism. |
| 2026-11-19 00:49 | LULU | other | 0.2% | no model | 100% / 0% / 0% / 0% | Users discuss LULU price movements, express confusion over high prices, and report shorting losses. |
| 2026-11-19 00:49 | SPCX | other | 1.6% | no model | 100% / 0% / 2.5% / 0% | Users discuss SPCX's past performance, compare it to the upcoming Anthropic IPO, and warn of potential pump-and-dump schemes. |
| 2026-11-19 00:42 | GLD | other | 0.3% | no model | 100% / 0% / 0% / 0% | Users discuss GLD price levels, express bearish views on puts, and share unrelated jokes or opinions. |
| 2026-11-19 00:42 | TTWO | other | 0.2% | no model | 100% / 2.5% / 5.0% / 0% | Users discuss TTWO stock price movements, GTA 6 launch expectations, and potential trading strategies. |
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

## Development walk-forward (flags before 2027-01-04)

Each development week replayed exactly as it would have run: its model trained only on labels available before the week began, scoring that week's candidates. Results count candidates whose label has settled.

### crash

| Candidates | n | Positives | Base rate | Flagged | Precision | Recall | F1 | Lift | AP | AUC |
|---|---|---|---|---|---|---|---|---|---|---|
| all candidates | 100 | 11 | 11% | 11 | 73% | 73% | 0.73 | 6.6x | 0.74 | 0.89 |
| low float runner | 2 | 2 | 100% | 2 | 100% | 100% | 1.00 | 1.0x | 1.00 | - |
| other | 98 | 9 | 9.2% | 9 | 67% | 67% | 0.67 | 7.3x | 0.64 | 0.87 |
| pump types together | 2 | 2 | 100% | 2 | 100% | 100% | 1.00 | 1.0x | 1.00 | - |

| Model | AP | Precision | Recall | F1 |
|---|---|---|---|---|
| all groups | 0.74 | 73% | 73% | 0.73 |
| market only | 0.71 | 67% | 73% | 0.70 |
| social only | 0.58 | 71% | 45% | 0.56 |

| Robustness check | Result | Detail |
|---|---|---|
| beats the base rate | pass | precision 73% vs base rate 11%; AP 0.74 |
| separate periods | not enough data | needs 3 positives in each of three blocks of weeks |
| per pump type | not enough data | needs 5 positives in a pump type |
| beats the control group | not enough data | 8 flagged with settled controls (needs 10) |
| survives slippage | not enough data | 7 flagged with a 10-session return (needs 10) |

Verdict: **not robust yet** (some checks need more labels).

Feature groups: all used; weak groups are pruned once the replay holds 20 positive candidates (11 so far).

### pump

No scored candidate with a settled label yet.

## Hold-out (flags from 2027-01-04)

Still locked, with 0 hold-out candidates so far. They are scored like any other, but their scores are not compared with their outcomes until collection has finished and every hold-out label has settled; then they are evaluated once, into `model/holdout.md`.
