# Stage 5 model

Updated 2026-10-16T00:22:15Z. Rule `model-v3` (docs/stage5.md on the code branch), written down before any model was trained. Every candidate is scored once, by the LightGBM model of the week it was flagged in (trained on the labels available before that week began, recent ones weighted more), and the score goes into the prospective log `model/predictions.csv`. **crash**: a close 40% or more below the flag price within 10 sessions (the avoid signal, first). **pump**: Stage 4's pump label. A candidate is flagged when its score is at least twice the base rate.

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
| 2026-10-15 23:28 | BETR | other | no model | no model | 100% / 91% / 0% / 0% | Users discuss BETR as a heavily shorted penny stock with high squeeze potential and urge others to buy. |
| 2026-10-15 23:28 | DRMA | other | no model | no model | 100% / 0% / 0% / 0% | Users discuss DRMA price action, volume, and potential moves based on test results. |
| 2026-10-15 21:16 | WETO | low float runner | no model | no model | 100% / 55% / 0% / 9.1% | Users discuss WETO trading strategy, warn against stop losses, and mention a cancelled ATM offering. |
| 2026-10-15 15:04 | SOXS | other | no model | no model | 100% / 0% / 0% / 0% | Users discuss holding, selling, or buying SOXS, with mentions of AI news and market volatility. |
| 2026-10-14 20:17 | PFE | other | no model | no model | 100% / 10% / 0% / 0% | Users discuss Pfizer as a defensive stock, dividend play, and potential AI beneficiary with mixed bullish and neutral sentiments. |
| 2026-10-14 20:04 | HOOD | other | no model | no model | 100% / 0% / 0% / 0% | Users discuss HOOD price drops, buying dips, and general market sentiment without specific company events. |
| 2026-10-14 19:51 | TSM | other | no model | no model | 94% / 24% / 0% / 53% | Users discuss TSM earnings anticipation, market recovery, and set price targets. |
| 2026-10-14 19:24 | RKLB | other | no model | no model | 100% / 0% / 0% / 0% | Users discuss RKLB losses, compare it to competitors, and express skepticism about its future potential. |
| 2026-10-14 19:24 | WMT | other | no model | no model | 100% / 0% / 0% / 0% | Users discuss WMT as a defensive stock, express bullish sentiment, and mention buying calls. |
| 2026-10-14 19:11 | LQDA | other | no model | no model | 100% / 70% / 0% / 20% | Users discuss LQDA price targets, a lawsuit settlement, and short interest, with mixed bullish and bearish sentiments. |
| 2026-10-14 18:31 | TLT | other | no model | no model | 100% / 0% / 0% / 0% | Users discuss TLT price movements, yields, and correlations with other assets without mentioning specific corporate events. |
| 2026-10-14 18:18 | SOFI | other | no model | no model | 100% / 0% / 0% / 0% | Users express extreme frustration and bearish sentiment regarding SOFI's price drop and performance. |
| 2026-10-14 17:34 | VOO | other | no model | no model | 100% / 0% / 0% / 0% | Users discuss holding VOO for long-term growth, comparing it to other assets, and expressing mixed views on current market valuations. |
| 2026-10-14 16:58 | ORCL | other | no model | no model | 100% / 0% / 0% / 0% | Users discuss ORCL price movements, options strategies, and rumors of a deal or government stake. |
| 2026-10-14 15:25 | ARM | other | no model | no model | 100% / 0% / 0% / 20% | Users discuss ARM's legal loss to Qualcomm and a potential forced sale due to collateralized debt. |
| 2026-10-14 13:12 | TCRT | low float runner | no model | no model | 100% / 20% / 0% / 0% | Chatter focuses on TCRT price targets, volume, and a reported catalyst driving a significant price increase. |
| 2026-10-14 12:46 | UPST | other | no model | no model | 100% / 40% / 10% / 0% | Users express frustration over losses, warn of potential pump-and-dumps, and share price targets for UPST. |
| 2026-10-14 12:29 | GLND | other | no model | no model | 100% / 55% / 0% / 0% | Users discuss Greenland Energy Company, citing a Greenland announcement and volume increases as reasons to buy. |
| 2026-10-14 11:39 | CLF | other | no model | no model | 100% / 10% / 0% / 10% | Users discuss Cleveland-Cliffs earnings, datacenter demand, and potential short squeeze. |
| 2026-10-14 05:42 | BBAI | other | no model | no model | 100% / 20% / 0% / 0% | Users discuss BBAI's recent $225M government contract announcement and speculate on potential price spikes. |
| 2026-10-14 00:41 | RSP | other | no model | no model | 100% / 0% / 0% / 0% | Users discuss RSP performance, correlation with SPY, and market breadth without specific company events or urgent buy pitches. |
| 2026-10-13 22:51 | SOXL | other | no model | no model | 100% / 0% / 0% / 0% | Users discuss SOXL volatility, losses, and leverage while joking about its performance. |
| 2026-10-13 20:37 | BAC | other | no model | no model | 100% / 0% / 0% / 0% | Users discuss BAC options and express bearish views citing a recent fine. |
| 2026-10-13 20:10 | AAOI | other | no model | no model | 100% / 0% / 0% / 0% | Users discuss recent losses and bearish sentiment regarding AAOI stock, with no specific company events mentioned. |
| 2026-10-13 18:51 | JBDI | low float runner | no model | no model | 100% / 17% / 8.3% / 0% | Users discuss JBDI trading halts, high volume, and express excitement or regret over recent price jumps. |
| 2026-10-13 18:32 | TTWO | other | no model | no model | 100% / 12% / 0% / 0% | Users discuss TTWO stock, mentioning GTA6, price drops, and potential bankruptcy rumors. |
| 2026-10-13 16:38 | CLGN | low float runner | no model | no model | 100% / 70% / 0% / 0% | Users discuss CLGN, equating it to LightSolver, and list it as a buy recommendation alongside other stocks. |
| 2026-10-13 14:38 | GME | other | no model | no model | 100% / 0% / 0% / 0% | Users discuss GME price action, CEO buying, and potential squeezes with mixed bullish and skeptical sentiments. |
| 2026-10-13 13:59 | AMC | other | no model | no model | 100% / 33% / 17% / 0% | Users discuss AMC stock, mentioning potential squeezes, dilution, and price targets. |
| 2026-10-13 13:59 | MSFT | other | no model | no model | 100% / 0% / 0% / 0% | Users discuss MSFT price movements, gains, and potential rallies while some express skepticism about its strength. |
| 2026-10-13 13:32 | OKLO | other | no model | no model | 100% / 0% / 4.5% / 0% | Users discuss OKLO's low price, express skepticism about insiders selling, and debate buying the stock. |
| 2026-10-13 13:32 | USAR | other | no model | no model | 100% / 0% / 0% / 0% | Users discuss USAR price, short interest, and personal investment experiences with mixed sentiment. |
| 2026-10-13 10:39 | JPM | other | no model | no model | 100% / 0% / 0% / 33% | Users discuss JPM earnings results, noting a miss in EPS and revenue, followed by a price drop. |
| 2026-10-13 08:00 | SXTC | other | no model | no model | 100% / 27% / 0% / 9.1% | Users discuss SXTC price recovery, a corrected offering event, and express bullish expectations. |
| 2026-10-13 03:58 | CRWV | other | no model | no model | 100% / 0% / 0% / 0% | Users discuss CRWV price action, express skepticism about ownership, and mention buying or shorting. |
| 2026-10-13 03:35 | NBIS | other | no model | no model | 100% / 0% / 0% / 0% | Chatter focuses on extreme volatility, price targets, and emotional reactions to NBIS stock movements. |
| 2026-10-13 02:56 | SKHY | other | no model | no model | 100% / 14% / 0% / 0% | Users discuss SKHY price drops, express regret over losses, and debate the stock's potential recovery. |
| 2026-10-13 01:10 | SNDK | other | no model | no model | 100% / 0% / 0% / 0% | Users discuss SNDK price drops, express confusion over news, and speculate on future movements. |
| 2026-10-12 22:44 | NIO | other | no model | no model | 100% / 0% / 9.1% / 0% | Users discuss NIO's financial health, express strong negative opinions, and mention a potential short squeeze. |
| 2026-10-12 21:51 | SOFI | other | no model | no model | 100% / 0% / 0% / 0% | Users discuss SOFI as a meme stock, mention its short float, and list it among stocks near 52-week lows. |

## Development walk-forward (flags before 2027-01-04)

Each development week replayed exactly as it would have run: its model trained only on labels available before the week began, scoring that week's candidates. Results count candidates whose label has settled.

### crash

No scored candidate with a settled label yet.

### pump

No scored candidate with a settled label yet.

## Hold-out (flags from 2027-01-04)

Still locked, with 0 hold-out candidates so far. They are scored like any other, but their scores are not compared with their outcomes until collection has finished and every hold-out label has settled; then they are evaluated once, into `model/holdout.md`.
