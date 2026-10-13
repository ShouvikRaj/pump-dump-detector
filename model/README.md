# Stage 5 model

Updated 2026-10-13T00:17:51Z. Rule `model-v3` (docs/stage5.md on the code branch), written down before any model was trained. Every candidate is scored once, by the LightGBM model of the week it was flagged in (trained on the labels available before that week began, recent ones weighted more), and the score goes into the prospective log `model/predictions.csv`. **crash**: a close 40% or more below the flag price within 10 sessions (the avoid signal, first). **pump**: Stage 4's pump label. A candidate is flagged when its score is at least twice the base rate.

## This week's models (week of 2026-10-12)

| Target | Status | Trained on | Positives | Base rate | Flag at | Feature groups |
|---|---|---|---|---|---|---|
| crash | no model yet | 0 rows | 0 | - | - | chatter, text, llm, price_volume, size, short_interest, filings, history, technical |
| pump | no model yet | 0 rows | 0 | - | - | chatter, text, llm, price_volume, size, short_interest, filings, history, technical |

A week's model needs 50 rows and 5 positives whose labels were settled before the week began; a label settles 10 sessions (two weeks) after the flag, 15 after a 50% rise.

## Latest candidates (last 7 days)

Scores as logged when each candidate was first seen; flagged ones in bold. The LLM column gives the shares of the posts shown that are about the company, pitch it, warn about it and state a company event (counted only when its quote checks out).

| Flagged (UTC) | Ticker | Archetype | Crash risk | Pump risk | LLM about / pitch / warning / event | What the chatter was about |
|---|---|---|---|---|---|---|
| 2026-10-12 22:44 | NIO | other | no model | no model | 100% / 0% / 9.1% / 0% | Users discuss NIO's financial health, express strong negative opinions, and mention a potential short squeeze. |
| 2026-10-12 21:51 | SOFI | other | no model | no model | 100% / 0% / 0% / 0% | Users discuss SOFI as a meme stock, mention its short float, and list it among stocks near 52-week lows. |
| 2026-10-12 20:58 | BMBL | other | no model | no model | 100% / 10% / 30% / 30% | Users discuss a reported $1B buyout of Bumble Inc. and warn of a potential pump-and-dump scheme. |
| 2026-10-12 20:58 | META | other | no model | no model | 100% / 2.5% / 0% / 2.5% | Chatter discusses META's AI model 'Muse', price movements, and potential earnings impact with mixed sentiment. |
| 2026-10-12 20:32 | UNH | other | no model | no model | 100% / 0% / 0% / 0% | Users discuss UNH earnings anticipation and call options with mixed bullish and bearish sentiments. |
| 2026-10-12 20:18 | RDDT | other | no model | no model | 100% / 12% / 0% / 0% | Users discuss RDDT valuation, express bullish optimism, and reference a large position increase. |
| 2026-10-12 18:19 | WFF | other | no model | no model | 100% / 30% / 0% / 0% | Users discuss erratic price movements, halts, and express confusion about the stock's performance without citing specific corporate events. |
| 2026-10-12 17:40 | ASML | other | no model | no model | 100% / 10% / 0% / 60% | Users discuss upcoming earnings for ASML and TSMC, with mixed opinions on potential price drops. |
| 2026-10-12 17:00 | SMCI | other | no model | no model | 100% / 27% / 0% / 0% | Users discuss SMCI price movements, express bullish optimism, and mention unrelated geopolitical events. |
| 2026-10-12 15:13 | TSM | other | no model | no model | 100% / 0% / 0% / 36% | Users discuss TSM earnings anticipation, trading strategies, and general market sentiment regarding the semiconductor stock. |
| 2026-10-12 14:47 | ONDS | other | no model | no model | 100% / 36% / 9.1% / 0% | Users discuss ONDS potential, warn of dilution, and set price targets. |
| 2026-10-12 14:20 | CBRS | other | no model | no model | 100% / 0% / 0% / 0% | Users express extreme distress, fear, and hopelessness regarding a sharp decline in CBRS stock price. |
| 2026-10-12 14:20 | MU | other | no model | no model | 100% / 0% / 0% / 0% | Users discuss a sharp price drop in $MU, blaming manipulation and expressing anger over the crash. |
| 2026-10-12 14:20 | SOXX | other | no model | no model | 100% / 0% / 0% / 0% | Users discuss SOXX holdings, compare it to other funds, and analyze recent price movements and sector correlations. |
| 2026-10-12 06:49 | MGM | other | no model | no model | 91% / 0% / 0% / 0% | Users discuss MGM's oversold technicals and potential for a mean reversion bounce. |
| 2026-10-12 03:44 | IREN | other | no model | no model | 100% / 0% / 0% / 7.4% | Chatter focuses on a rumored deal between IREN and Anthropic, with mixed reactions ranging from bullish excitement to skepticism about the company's fundamentals. |
| 2026-10-09 13:59 | UNH | other | no model | no model | 100% / 20% / 0% / 0% | Discussions focus on UNH earnings, options activity, and mixed sentiment regarding potential pumps or delusions. |
| 2026-10-09 13:19 | SLS | other | no model | no model | 100% / 0% / 0% / 8.3% | Users discuss SLS clinical data, express bullish sentiment, and mention specific upcoming events like the 80th patient milestone. |
| 2026-10-09 12:52 | DAL | other | no model | no model | 100% / 0% / 0% / 20% | Users discuss Delta Air Lines stock, mentioning missed guidance, late conference calls, and trading puts. |
| 2026-10-09 12:39 | HUM | other | no model | no model | 100% / 0% / 0% / 9.1% | Chatter focuses on Humana stock price, options premiums, and a scheduled CMS rating event. |
| 2026-10-09 12:39 | TSM | other | no model | no model | 92% / 0% / 0% / 0% | Users discuss TSM earnings expectations, meme stock behavior, and clarify its relationship to semiconductor ETFs. |
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

## Development walk-forward (flags before 2027-01-04)

Each development week replayed exactly as it would have run: its model trained only on labels available before the week began, scoring that week's candidates. Results count candidates whose label has settled.

### crash

No scored candidate with a settled label yet.

### pump

No scored candidate with a settled label yet.

## Hold-out (flags from 2027-01-04)

Still locked, with 0 hold-out candidates so far. They are scored like any other, but their scores are not compared with their outcomes until collection has finished and every hold-out label has settled; then they are evaluated once, into `model/holdout.md`.
