# Stage 5 model

Updated 2026-11-27T08:11:48Z. Rule `model-v3` (docs/stage5.md on the code branch), written down before any model was trained. Every candidate is scored once, by the LightGBM model of the week it was flagged in (trained on the labels available before that week began, recent ones weighted more), and the score goes into the prospective log `model/predictions.csv`. **crash**: a close 40% or more below the flag price within 10 sessions (the avoid signal, first). **pump**: Stage 4's pump label. A candidate is flagged when its score is at least twice the base rate.

## This week's models (week of 2026-11-23)

| Target | Status | Trained on | Positives | Base rate | Flag at | Feature groups |
|---|---|---|---|---|---|---|
| crash | trained | 1213 rows | 30 | 6.6% | 13% | chatter, text, llm, price_volume, size, short_interest, filings, history, technical |
| pump | trained | 1209 rows | 5 | 1.2% | 2.3% | chatter, text, llm, price_volume, size, short_interest, filings, history, technical |

What this week's crash model leans on (share of split gain): `volatility_20d` 14%, `pennystocks_share` 10%, `turnover_last` 9%, `si_days_to_cover` 7%, `days_since_report` 6%, `wsb_share` 4%, `price_log` 3%, `ret_1d` 2%.

What this week's pump model leans on (share of split gain): `gap_open` 37%, `move_since_close` 8%, `length_log` 7%, `wsb_share` 6%, `si_change` 6%, `rel_vol_today_log` 4%, `vol_60m_rel` 4%, `institution_pct` 3%.

## Latest candidates (last 7 days)

Scores as logged when each candidate was first seen; flagged ones in bold. The LLM column gives the shares of the posts shown that are about the company, pitch it, warn about it and state a company event (counted only when its quote checks out).

| Flagged (UTC) | Ticker | Archetype | Crash risk | Pump risk | LLM about / pitch / warning / event | What the chatter was about |
|---|---|---|---|---|---|---|
| 2026-11-26 00:54 | AAPL | other | 0.1% | 0.0% | 100% / 0% / 0% / 0% | Users discuss AAPL's resilience, price action, and market dominance while expressing mixed sentiments and skepticism. |
| 2026-11-26 00:54 | META | other | 0.3% | 0.0% | 100% / 0% / 0% / 0% | Users discuss META's volatility, price drops, and potential rebounds without specific company events or pump-and-dump warnings. |
| 2026-11-26 00:54 | VTI | other | 0.1% | 0.0% | 100% / 0% / 0% / 0% | Users discuss VTI performance, compare it to other funds, and advise on long-term holding strategies. |
| 2026-11-26 00:44 | NRSN | low float runner | **76%** | **3.1%** | 100% / 17% / 0% / 17% | Chatter focuses on Phase 2b ALS trial data and aggressive price targets. |
| 2026-11-26 00:44 | SOXL | other | 2.3% | 0.1% | 100% / 0% / 0% / 0% | Users discuss SOXL's severe drawdown, express regret over buying, and joke about its volatility. |
| 2026-11-26 00:44 | SOXS | other | 12% | **2.7%** | 100% / 0% / 0% / 0% | Users discuss hedging strategies, price movements, and trading tactics for the SOXS ETF. |
| 2026-11-25 21:55 | SGOV | other | 0.1% | 0.0% | 100% / 0% / 0% / 0% | Users discuss SGOV as a safe haven or cash parking spot amidst market losses, contrasting it with riskier assets. |
| 2026-11-25 00:43 | BENF | other | **46%** | **2.8%** | 100% / 0% / 0% / 0% | Users discuss BENF price targets, volume, and chart patterns with bullish sentiment. |
| 2026-11-24 21:15 | DELL | other | 2.3% | 0.1% | 100% / 0% / 0% / 18% | Chatter focuses on Dell's reported earnings miss, guidance cuts, and subsequent stock price crash. |
| 2026-11-24 00:45 | DJT | other | 1.7% | 0.0% | 100% / 0% / 3.3% / 0% | Chatter focuses on DJT's alleged influence over Nvidia and Jensen Huang's reinstatement, mixed with debt concerns and insults. |
| 2026-11-24 00:45 | HPE | other | 1.1% | 1.0% | 100% / 3.6% / 0% / 14% | Users discuss HPE earnings results, with mixed reactions ranging from disappointment to optimism. |
| 2026-11-24 00:45 | IVVD | other | 2.1% | 0.4% | 100% / 15% / 0% / 31% | Users discuss IVVD Phase 3 trial results, FDA alignment, and set a new price target. |
| 2026-11-24 00:45 | MSS | low float runner | **53%** | 0.7% | 100% / 7.1% / 0% / 0% | Chatter discusses MSS stock price levels, volume, and potential trades, with one comment mentioning Nvidia executives. |
| 2026-11-24 00:45 | NYT | other | 0.1% | 0.0% | 0% / 0% / 0% / 0% | Users discuss NYT reporting on Nvidia and Jensen Huang, labeling the newspaper as biased or a mouthpiece for the CIA. |
| 2026-11-24 00:45 | SOAR | other | **51%** | 2.1% | 100% / 20% / 0% / 20% | Users discuss SOAR stock price movements, short interest, and recent positive news in a penny stock context. |
| 2026-11-23 00:51 | SMCI | other | 0.2% | 0.0% | 100% / 0% / 23% / 0% | Users discuss SMCI's stock performance, alleging book cooking, and analyzing a market resolution regarding an AI industry downturn. |
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

## Development walk-forward (flags before 2027-01-04)

Each development week replayed exactly as it would have run: its model trained only on labels available before the week began, scoring that week's candidates. Results count candidates whose label has settled.

### crash

| Candidates | n | Positives | Base rate | Flagged | Precision | Recall | F1 | Lift | AP | AUC |
|---|---|---|---|---|---|---|---|---|---|---|
| all candidates | 129 | 13 | 10% | 13 | 69% | 69% | 0.69 | 6.9x | 0.75 | 0.90 |
| low float runner | 4 | 2 | 50% | 3 | 67% | 100% | 0.80 | 1.3x | 1.00 | 1.00 |
| other | 125 | 11 | 8.8% | 10 | 70% | 64% | 0.67 | 8.0x | 0.69 | 0.89 |
| pump types together | 4 | 2 | 50% | 3 | 67% | 100% | 0.80 | 1.3x | 1.00 | 1.00 |
| weeks of 2026-11-02 to 2026-11-02 | 87 | 4 | 4.6% | 6 | 50% | 75% | 0.60 | 10.9x | 0.64 | 0.78 |
| weeks of 2026-11-09 to 2026-11-09 | 40 | 7 | 18% | 6 | 83% | 71% | 0.77 | 4.8x | 0.85 | 0.95 |
| weeks of 2026-11-16 to 2026-11-16 | 2 | 2 | 100% | 1 | 100% | 50% | 0.67 | 1.0x | 1.00 | - |

| Model | AP | Precision | Recall | F1 |
|---|---|---|---|---|
| all groups | 0.75 | 69% | 69% | 0.69 |
| market only | 0.73 | 67% | 77% | 0.71 |
| social only | 0.58 | 75% | 46% | 0.57 |

| Robustness check | Result | Detail |
|---|---|---|
| beats the base rate | pass | precision 69% vs base rate 10%; AP 0.75 |
| separate periods | not enough data | needs 3 positives in each of three blocks of weeks |
| per pump type | not enough data | needs 5 positives in a pump type |
| beats the control group | pass | flagged 64% vs their controls 4.5% |
| survives slippage | pass | flagged mean 10-session return -51.2% vs unflagged -9.6% (needs -3% or lower) |

Verdict: **not robust yet** (some checks need more labels).

Feature groups: all used; weak groups are pruned once the replay holds 20 positive candidates (13 so far).

### pump

| Candidates | n | Positives | Base rate | Flagged | Precision | Recall | F1 | Lift | AP | AUC |
|---|---|---|---|---|---|---|---|---|---|---|
| all candidates | 2 | 0 | 0% | 0 | - | - | - | - | - | - |
| other | 2 | 0 | 0% | 0 | - | - | - | - | - | - |

| Model | AP | Precision | Recall | F1 |
|---|---|---|---|---|
| all groups | - | - | - | - |
| market only | - | - | - | - |
| social only | - | - | - | - |

| Robustness check | Result | Detail |
|---|---|---|
| beats the base rate | not enough data | 0 positives (needs 10) |
| separate periods | not enough data | needs 3 positives in each of three blocks of weeks |
| per pump type | not enough data | needs 5 positives in a pump type |
| beats the control group | not enough data | 0 flagged with settled controls (needs 10) |
| survives slippage | not enough data | 0 flagged with a 10-session return (needs 10) |

Verdict: **not robust yet** (some checks need more labels).

Feature groups: all used; weak groups are pruned once the replay holds 20 positive candidates (0 so far).

## Hold-out (flags from 2027-01-04)

Still locked, with 0 hold-out candidates so far. They are scored like any other, but their scores are not compared with their outcomes until collection has finished and every hold-out label has settled; then they are evaluated once, into `model/holdout.md`.
