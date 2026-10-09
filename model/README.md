# Stage 5 model

Updated 2026-10-09T05:59:31Z. Rule `model-v3` (docs/stage5.md on the code branch), written down before any model was trained. Every candidate is scored once, by the LightGBM model of the week it was flagged in (trained on the labels available before that week began, recent ones weighted more), and the score goes into the prospective log `model/predictions.csv`. **crash**: a close 40% or more below the flag price within 10 sessions (the avoid signal, first). **pump**: Stage 4's pump label. A candidate is flagged when its score is at least twice the base rate.

## This week's models (week of 2026-10-05)

| Target | Status | Trained on | Positives | Base rate | Flag at | Feature groups |
|---|---|---|---|---|---|---|
| crash | no model yet | 0 rows | 0 | - | - | chatter, text, llm, price_volume, size, short_interest, filings, history, technical |
| pump | no model yet | 0 rows | 0 | - | - | chatter, text, llm, price_volume, size, short_interest, filings, history, technical |

A week's model needs 50 rows and 5 positives whose labels were settled before the week began; a label settles 10 sessions (two weeks) after the flag, 15 after a 50% rise.

## Latest candidates (last 7 days)

Scores as logged when each candidate was first seen; flagged ones in bold. The LLM column gives the shares of the posts shown that are about the company, pitch it, warn about it and state a company event (counted only when its quote checks out).

| Flagged (UTC) | Ticker | Archetype | Crash risk | Pump risk | LLM about / pitch / warning / event | What the chatter was about |
|---|---|---|---|---|---|---|
| 2026-10-09 01:49 | ONDS | other | no model | no model | 100% / 0% / 0% / 0% | Users discuss owning ONDS, speculate on price targets, and mention speculative growth stocks. |
| 2026-10-09 01:09 | IBM | other | no model | no model | 91% / 0% / 0% / 0% | Users discuss IBM's decline, joke about the name, and speculate on a potential acquisition or price surge. |
| 2026-10-09 00:30 | SOXL | other | no model | no model | 100% / 0% / 0% / 0% | Users discuss SOXL price movements, express bullish/bearish opinions, and mention unrelated events like OpenAI funding. |
| 2026-10-09 00:16 | MCD | other | no model | no model | 100% / 0% / 0% / 0% | Users discuss MCD's low price, dividends, and promotions, with some urging others to buy. |
| 2026-10-08 21:37 | CIFR | other | no model | no model | 100% / 0% / 0% / 0% | Users express extreme bearishness, calling the stock a scam and noting recent price drops. |
| 2026-10-08 21:11 | ASTS | other | no model | no model | 100% / 0% / 2.5% / 0% | Users discuss a sharp price drop, potential lawsuits, and competitor threats against ASTS. |
| 2026-10-08 20:17 | AAOI | other | no model | no model | 100% / 9.1% / 0% / 0% | Users discuss AAOI's recent price dip, capex status, and potential for a significant price increase. |
| 2026-10-08 19:38 | CMG | other | no model | no model | 91% / 27% / 0% / 27% | Users discuss a potential Starbucks buyout of Chipotle, citing management connections and undervaluation. |
| 2026-10-08 18:59 | SBUX | other | no model | no model | 100% / 10% / 0% / 10% | Users discuss rumors of a Starbucks takeover of Chipotle and trade options based on the speculation. |
| 2026-10-08 18:20 | USO | other | no model | no model | 100% / 0% / 0% / 0% | Users discuss USO price movements, express bullish/bearish views, and mention specific trades. |
| 2026-10-08 18:05 | NBIS | other | no model | no model | 100% / 0% / 0% / 2.6% | Chatter discusses NBIS price action, mentions a specific NVIDIA executive spotlight, and includes mixed sentiment with some buying and selling. |
| 2026-10-08 17:52 | DELL | other | no model | no model | 100% / 0% / 0% / 0% | Chatter focuses on Michael Dell's wife's appearance as a meme and joke, with no mention of company events. |
| 2026-10-08 17:11 | ORCL | other | no model | no model | 100% / 0% / 0% / 6.7% | Mixed chatter includes panic over price drops, profit taking, and news about trucking gas for data centers. |
| 2026-10-08 16:17 | GME | other | no model | no model | 100% / 4.0% / 8.0% / 4.0% | Mixed chatter includes a pitch about insider buying, warnings about dilution and scams, and general meme stock hype. |
| 2026-10-08 15:51 | BWET | other | no model | no model | 100% / 0% / 0% / 0% | Users discuss BWET's massive price surge, joke about the name, and debate the impact of a lawsuit on shipping benchmarks. |
| 2026-10-08 13:39 | META | other | no model | no model | 100% / 0% / 0% / 0% | Users discuss META stock price, AI strategy, and express frustration or hope regarding recent performance. |
| 2026-10-08 13:27 | TTWO | other | no model | no model | 100% / 9.1% / 0% / 0% | Users discuss TTWO price targets, GTA VI anticipation, and trading strategies without specific corporate events. |
| 2026-10-08 13:12 | PLTR | other | no model | no model | 100% / 0% / 7.7% / 0% | Chatter includes mixed reactions to PLTR price movements, with some users warning of a pump-and-dump while others express bullish optimism. |
| 2026-10-08 04:07 | ADBE | other | no model | no model | 100% / 0% / 0% / 0% | Users discuss bearish theses regarding AI clones and open-source alternatives threatening Adobe's subscription model. |
| 2026-10-08 03:01 | KEEL | other | no model | no model | 100% / 0% / 0% / 0% | Users discuss KEEL stock performance, express skepticism about its progress, and mention buying calls for a potential drop. |
| 2026-10-07 20:50 | SMCI | other | no model | no model | 100% / 23% / 0% / 7.7% | Mixed chatter on SMCI ranging from bullish price targets to bearish warnings and a rumor of a buyout. |
| 2026-10-07 20:50 | UUUU | other | no model | no model | 100% / 0% / 0% / 0% | Users express extreme frustration and disappointment over UUUU's recent price decline and poor performance. |
| 2026-10-07 20:37 | LEVI | other | no model | no model | 100% / 0% / 0% / 7.7% | Users discuss LEVI stock performance, noting a stock drop despite positive earnings results. |
| 2026-10-07 19:18 | IREN | other | no model | no model | 100% / 9.1% / 0% / 0% | Mixed chatter includes bullish targets, complaints about price drops, and mentions of analyst upgrades. |
| 2026-10-07 17:44 | LLY | other | no model | no model | 100% / 18% / 0% / 0% | Users express bullish sentiment and speculate on a stock split for LLY. |
| 2026-10-07 16:38 | BIYA | low float runner | no model | no model | 100% / 20% / 0% / 0% | Users discuss BIYA price spikes, volume, and set aggressive sell targets, with one user claiming a massive percentage gain. |
| 2026-10-07 13:01 | GLD | other | no model | no model | 100% / 0% / 0% / 0% | Users discuss GLD price drops, short positions, and speculate on Burry's holdings without specific company events. |
| 2026-10-07 12:34 | SOXL | other | no model | no model | 100% / 9.7% / 0% / 0% | Users discuss SOXL price movements, express bearish views via put options, and issue a coordinated buy signal. |
| 2026-10-07 12:08 | BULL | other | no model | no model | 100% / 7.7% / 0% / 0% | Users discuss Webull stock volatility, regulatory news, and ask for buy/sell advice. |
| 2026-10-07 12:08 | SOXS | other | no model | no model | 100% / 23% / 0% / 0% | Users urge buying SOXS based on a non-existent Iran deal rumor and a specific options pinning event. |
| 2026-10-07 10:09 | SNDK | other | no model | no model | 100% / 0% / 0% / 0% | Users express extreme frustration and bearish sentiment regarding Sandisk stock performance. |
| 2026-10-06 23:59 | CRWD | other | no model | no model | 100% / 10% / 10% / 0% | Users discuss CRWD price movements, past outages, and speculate on future trends with mixed bullish and bearish sentiment. |
| 2026-10-06 19:34 | AVGO | other | no model | no model | 100% / 0% / 0% / 0% | Chatter focuses on AVGO price action, bagholder frustration, and expectations for a significant price increase. |
| 2026-10-06 18:54 | SKHY | other | no model | no model | 91% / 18% / 9.1% / 0% | Mixed chatter includes bullish call options, bearish warnings, and unrelated comments. |
| 2026-10-06 18:28 | INTC | other | no model | no model | 100% / 0% / 0% / 0% | Mixed chatter on INTC ranging from profit-taking and bearish sentiment to confusion over a specific executive's options. |
| 2026-10-06 18:14 | OKLO | other | no model | no model | 100% / 0% / 17% / 0% | Users discuss OKLO price movements, sector rotation, and skepticism regarding the company's lack of product delivery. |
| 2026-10-06 18:01 | PENG | other | no model | no model | 100% / 0% / 0% / 0% | Users discuss PENG stock volatility and potential earnings impact with mixed sentiment. |
| 2026-10-06 17:21 | CIRC | other | no model | no model | 100% / 20% / 0% / 0% | Users discuss a potential hedge fund squeeze and express bullish excitement about CIRC stock. |
| 2026-10-06 17:08 | SPY | other | no model | no model | 100% / 0% / 0% / 0% | Users discuss SPY price movements, compare it to QQQ, and make bearish or bullish predictions without specific corporate events. |
| 2026-10-06 16:43 | HTZ | other | no model | no model | 100% / 15% / 0% / 0% | Users discuss a sudden price surge in HTZ, comparing it to previous rallies and short squeezes. |

## Development walk-forward (flags before 2027-01-04)

Each development week replayed exactly as it would have run: its model trained only on labels available before the week began, scoring that week's candidates. Results count candidates whose label has settled.

### crash

No scored candidate with a settled label yet.

### pump

No scored candidate with a settled label yet.

## Hold-out (flags from 2027-01-04)

Still locked, with 0 hold-out candidates so far. They are scored like any other, but their scores are not compared with their outcomes until collection has finished and every hold-out label has settled; then they are evaluated once, into `model/holdout.md`.
