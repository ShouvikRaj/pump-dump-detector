# Stage 5 model

Updated 2026-11-08T05:52:25Z. Rule `model-v3` (docs/stage5.md on the code branch), written down before any model was trained. Every candidate is scored once, by the LightGBM model of the week it was flagged in (trained on the labels available before that week began, recent ones weighted more), and the score goes into the prospective log `model/predictions.csv`. **crash**: a close 40% or more below the flag price within 10 sessions (the avoid signal, first). **pump**: Stage 4's pump label. A candidate is flagged when its score is at least twice the base rate.

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
| 2026-11-05 22:33 | ABNB | other | 0.1% | no model | 100% / 0% / 0% / 20% | Users discuss upcoming earnings, express skepticism about management, and joke about stock buybacks. |
| 2026-11-05 22:33 | IONQ | other | 3.3% | no model | 100% / 0% / 0% / 10% | Mixed chatter includes bearish skepticism about valuations, a specific earnings beat mention, and bullish hype. |
| 2026-11-05 22:19 | VOO | other | 0.6% | no model | 100% / 0% / 0% / 0% | Users discuss VOO as a safe investment alternative to high-risk leveraged ETFs and meme stocks. |
| 2026-11-05 21:12 | SNDK | other | 6.0% | no model | 100% / 5.0% / 0% / 7.5% | Chatter discusses SNDK price drops, potential stock splits, and mixed investment opinions. |
| 2026-11-05 20:49 | ROPE | other | 0.3% | no model | 100% / 0% / 0% / 0% | Users discuss $ROPE with high urgency, mentioning full portfolio allocations and calls. |
| 2026-11-05 19:19 | SQQQ | other | 0.3% | no model | 100% / 18% / 0% / 0% | Users discuss SQQQ price movements, express bullish sentiment, and mention selling positions. |
| 2026-11-05 17:29 | APLD | other | 0.2% | no model | 100% / 0% / 7.7% / 0% | Users discuss APLD's performance, location, and potential as an AI/data center stock with mixed sentiment. |
| 2026-11-05 16:25 | CRWD | other | 0.1% | no model | 100% / 0% / 0% / 0% | Users discuss CRWD price action, potential lawsuits, and general market sentiment without specific buy pitches or confirmed events. |
| 2026-11-05 16:25 | DNUT | other | 0.2% | no model | 100% / 30% / 0% / 0% | Users express excitement and urgency about significant price gains in DNUT stock. |
| 2026-11-05 15:05 | NVDA | other | 0.1% | no model | 100% / 0% / 0% / 0% | Mixed chatter regarding NVDA price targets, earnings anticipation, and general market sentiment. |
| 2026-11-05 13:17 | OKLO | other | 0.1% | no model | 100% / 0% / 0% / 0% | Users discuss OKLO's poor performance, potential for a bounce, and compare it to other failing stocks. |
| 2026-11-05 09:54 | WMT | other | 0.1% | no model | 100% / 0% / 0% / 0% | Users discuss WMT valuation, growth, and portfolio performance with mixed bullish and sarcastic tones. |
| 2026-11-05 08:22 | IBKR | other | 0.1% | no model | 100% / 0% / 0% / 0% | Users discuss IBKR trading features, platform complaints, and personal losses on options. |
| 2026-11-05 07:30 | TTWO | other | 0.1% | no model | 100% / 16% / 0% / 5.3% | Users discuss TTWO's price surge, speculate on GTA 6, and mention potential earnings or events. |
| 2026-11-05 04:50 | SOXS | other | 7.3% | no model | 100% / 3.8% / 0% / 0% | Users discuss SOXS price movements, express bullish/bearish opinions, and joke about its history. |
| 2026-11-05 03:15 | SOXL | other | **28%** | no model | 100% / 0% / 0% / 0% | Users discuss SOXL volatility, express pain from losses, debate holding leveraged ETFs, and make bearish price predictions. |
| 2026-11-05 01:08 | SOXX | other | 0.2% | no model | 100% / 0% / 0% / 0% | Users discuss SOXX price movements, leverage mechanics, and market conditions without specific company events or buy pitches. |
| 2026-11-05 00:45 | GEV | other | 0.2% | no model | 100% / 0% / 0% / 0% | Users discuss GEV price movements, ownership, and general market sentiment without specific corporate events. |
| 2026-11-04 22:27 | BROS | other | 0.2% | no model | 100% / 0% / 0% / 10% | Users discuss a sharp price drop and question a recent earnings call for Dutch Bros. |
| 2026-11-04 21:19 | APP | other | 0.1% | no model | 100% / 0% / 0% / 0% | Users discuss Applovin's earnings beat, massive put open interest, and price targets in a highly speculative manner. |

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
