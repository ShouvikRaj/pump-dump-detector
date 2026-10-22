# Stage 5 model

Updated 2026-10-22T00:18:44Z. Rule `model-v3` (docs/stage5.md on the code branch), written down before any model was trained. Every candidate is scored once, by the LightGBM model of the week it was flagged in (trained on the labels available before that week began, recent ones weighted more), and the score goes into the prospective log `model/predictions.csv`. **crash**: a close 40% or more below the flag price within 10 sessions (the avoid signal, first). **pump**: Stage 4's pump label. A candidate is flagged when its score is at least twice the base rate.

## This week's models (week of 2026-10-19)

| Target | Status | Trained on | Positives | Base rate | Flag at | Feature groups |
|---|---|---|---|---|---|---|
| crash | no model yet | 33 rows | 1 | - | - | chatter, text, llm, price_volume, size, short_interest, filings, history, technical |
| pump | no model yet | 32 rows | 0 | - | - | chatter, text, llm, price_volume, size, short_interest, filings, history, technical |

A week's model needs 50 rows and 5 positives whose labels were settled before the week began; a label settles 10 sessions (two weeks) after the flag, 15 after a 50% rise.

## Latest candidates (last 7 days)

Scores as logged when each candidate was first seen; flagged ones in bold. The LLM column gives the shares of the posts shown that are about the company, pitch it, warn about it and state a company event (counted only when its quote checks out).

| Flagged (UTC) | Ticker | Archetype | Crash risk | Pump risk | LLM about / pitch / warning / event | What the chatter was about |
|---|---|---|---|---|---|---|
| 2026-10-21 22:45 | RDDT | other | no model | no model | 100% / 0% / 0% / 0% | Users discuss RDDT price targets, app issues, and warn against chasing the stock due to overcrowding. |
| 2026-10-21 19:47 | MSTR | other | no model | no model | 100% / 27% / 6.7% / 0% | Users discuss MSTR price targets, leverage, and ownership of BTC vs the stock. |
| 2026-10-21 18:15 | IBM | other | no model | no model | 100% / 9.1% / 0% / 9.1% | Users discuss IBM's recent price surge, earnings anticipation, and comparisons to other tech giants. |
| 2026-10-21 16:41 | AMOD | low float runner | no model | no model | 100% / 18% / 0% / 5.9% | Users discuss AMOD's price surge, low float, and a news link regarding Bitcoin holdings. |
| 2026-10-21 11:34 | META | other | no model | no model | 100% / 0% / 0% / 22% | Users discuss META earnings, capex, and AI themes with mixed bullish and bearish sentiments. |
| 2026-10-21 08:01 | SLS | other | no model | no model | 92% / 0% / 0% / 0% | Chatter discusses SLS stock price movements, potential gains, and mentions unrelated SpaceX infrastructure. |
| 2026-10-21 02:19 | PAC | other | no model | no model | 0% / 0% / 0% / 0% | All documents discuss political PACs and Super PACs, not the stock PAC. |
| 2026-10-20 23:18 | MRNA | other | no model | no model | 100% / 0% / 0% / 0% | Users discuss MRNA price movements, express bearish views, and speculate on a potential pump or squeeze. |
| 2026-10-20 21:21 | OKLO | other | no model | no model | 100% / 7.7% / 7.7% / 0% | Users discuss OKLO's massive market cap decline, potential pump-and-dump status, and hold positions despite pre-revenue status. |
| 2026-10-20 21:06 | SMCI | other | no model | no model | 100% / 26% / 0% / 4.3% | Users discuss SMCI price spikes, earnings rumors, and potential regulatory issues. |
| 2026-10-20 18:16 | GOOGL | other | no model | no model | 100% / 0% / 0% / 0% | Users express frustration with GOOGL's lack of movement and discuss options, with no specific company events mentioned. |
| 2026-10-20 16:42 | LRCX | other | no model | no model | 100% / 9.1% / 0% / 36% | Users discuss LRCX earnings anticipation, price targets, and potential upside before the event. |
| 2026-10-20 16:03 | IWM | other | no model | no model | 100% / 0% / 0% / 0% | Users discuss new extended-hours options trading for IWM and speculate on price movements. |
| 2026-10-20 14:57 | CRWV | other | no model | no model | 100% / 15% / 0% / 5.0% | Mixed chatter regarding CoreWeave's financial health, potential bankruptcy rumors, and conflicting price targets. |
| 2026-10-20 13:24 | HTZ | other | no model | no model | 100% / 53% / 0% / 0% | Users discuss a potential short squeeze and express bullish optimism for HTZ stock. |
| 2026-10-20 10:18 | SPCX | other | no model | no model | 100% / 10% / 10% / 7.5% | Chatter focuses on upcoming SPCX earnings, Elon Musk's 'giving away shares' meme, and potential price volatility. |
| 2026-10-20 04:07 | APLD | other | no model | no model | 100% / 6.7% / 0% / 0% | Users discuss APLD price action, CEO insider buying, and AI infrastructure risks with mixed bullish and bearish sentiment. |
| 2026-10-19 22:36 | GOOG | other | no model | no model | 100% / 0% / 0% / 0% | Users discuss GOOG investment strategies, price targets, and banbet challenges without specific corporate events. |
| 2026-10-19 19:31 | NFLX | other | no model | no model | 100% / 0% / 0% / 0% | Users discuss NFLX earnings, potential price drops, and hold positions before the event. |
| 2026-10-19 18:51 | RIVN | other | no model | no model | 100% / 0% / 0% / 0% | Users discuss RIVN options, compare it to TSLA, and express skepticism about its future performance. |
| 2026-10-19 16:13 | AMZN | other | no model | no model | 100% / 0% / 0% / 0% | Users discuss AMZN price movements, express bullish sentiment, and speculate on manipulation without citing specific corporate events. |
| 2026-10-19 16:13 | GLD | other | no model | no model | 100% / 0% / 0% / 0% | Users discuss losses, boredom, and lack of movement in GLD, with no specific corporate events or pump-and-dump warnings. |
| 2026-10-19 16:13 | TQQQ | other | no model | no model | 100% / 0% / 0% / 0% | Users discuss TQQQ volatility, losses, and weekend trading strategies with mixed sentiment. |
| 2026-10-19 14:18 | TCRT | low float runner | no model | no model | 100% / 83% / 0% / 0% | Users discuss high trading volume and price targets for TCRT, with no specific company events mentioned. |
| 2026-10-19 06:00 | WDC | other | no model | no model | 100% / 0% / 0% / 0% | Users discuss WDC price movements, losses, and potential upcoming reports without specific event announcements or promotional pitches. |
| 2026-10-18 05:58 | VTI | other | no model | no model | 100% / 0% / 0% / 0% | Users discuss VTI as a long-term hold and tax-loss partner, with no specific events or pump-and-dump warnings. |
| 2026-10-17 17:37 | NFLX | other | no model | no model | 100% / 0% / 0% / 7.7% | Mixed chatter on NFLX ranging from skepticism about value traps to speculation on earnings and IV. |
| 2026-10-17 04:49 | SCHD | other | no model | no model | 100% / 0% / 0% / 0% | Users discuss buying SCHD as a safe value pick and dividend growth strategy. |
| 2026-10-17 01:44 | SOXX | other | no model | no model | 100% / 0% / 0% / 0% | Users discuss SOXX price drops, losses, and bearish sentiment regarding the semiconductor sector. |
| 2026-10-16 21:33 | AMD | other | no model | no model | 100% / 0% / 0% / 0% | Mixed chatter on AMD including profit taking, bearish sentiment, and speculation on price targets. |
| 2026-10-16 21:20 | SGRX | other | no model | no model | 100% / 0% / 0% / 0% | Users discuss SGRX price targets, recent drops, and potential upside in penny stock forums. |
| 2026-10-16 21:20 | XLAB | other | no model | no model | 100% / 29% / 7.1% / 0% | Mixed chatter on XLAB including volume analysis, price targets, and accusations of pump-and-dump schemes. |
| 2026-10-16 20:40 | AAPL | other | no model | no model | 100% / 0% / 0% / 0% | Users discuss AAPL's unusual resilience during a market downturn, noting its green performance, call options activity, and lack of specific catalysts. |
| 2026-10-16 20:14 | AVGO | other | no model | no model | 100% / 0% / 0% / 0% | Users discuss AVGO's poor performance, VMware acquisition concerns, and general bearish sentiment without specific corporate events. |
| 2026-10-16 19:34 | SOXS | other | no model | no model | 100% / 19% / 6.2% / 0% | Users discuss trading SOXS, with some warning of decay and others offering shares for sale. |
| 2026-10-16 19:07 | MSTR | other | no model | no model | 100% / 10% / 0% / 0% | Users discuss MSTR, mention Michael Saylor, and express mixed opinions ranging from bullish excitement to skepticism. |
| 2026-10-16 19:07 | OPEX | other | no model | no model | 100% / 0% / 0% / 0% | Users discuss OPEX expiration day volatility, oil market news, and general trading sentiments. |
| 2026-10-16 19:07 | VOO | other | no model | no model | 100% / 0% / 0% / 0% | Users discuss VOO as a safe investment, express regret over missing out, and react to price drops. |
| 2026-10-16 18:54 | TQQQ | other | no model | no model | 100% / 18% / 0% / 0% | Users discuss TQQQ trading strategies, past performance, and express bullish optimism for upcoming market moves. |
| 2026-10-16 18:27 | QQQ | other | no model | no model | 100% / 0% / 0% / 0% | Users discuss QQQ price drops, short positions, and bearish sentiment without mentioning specific corporate events. |

## Development walk-forward (flags before 2027-01-04)

Each development week replayed exactly as it would have run: its model trained only on labels available before the week began, scoring that week's candidates. Results count candidates whose label has settled.

### crash

No scored candidate with a settled label yet.

### pump

No scored candidate with a settled label yet.

## Hold-out (flags from 2027-01-04)

Still locked, with 0 hold-out candidates so far. They are scored like any other, but their scores are not compared with their outcomes until collection has finished and every hold-out label has settled; then they are evaluated once, into `model/holdout.md`.
