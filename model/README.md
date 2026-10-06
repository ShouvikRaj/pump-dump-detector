# Stage 5 model

Updated 2026-10-06T08:20:48Z. Rule `model-v2` (docs/stage5.md on the code branch), written down before any model was trained. Every candidate is scored once, by the LightGBM model of the week it was flagged in (trained on the labels available before that week began, recent ones weighted more), and the score goes into the prospective log `model/predictions.csv`. **crash**: a close 40% or more below the flag price within 10 sessions (the avoid signal, first). **pump**: Stage 4's pump label. A candidate is flagged when its score is at least twice the base rate.

## This week's models (week of 2026-10-05)

| Target | Status | Trained on | Positives | Base rate | Flag at | Feature groups |
|---|---|---|---|---|---|---|
| crash | no model yet | 0 rows | 0 | - | - | chatter, text, llm, price_volume, size, short_interest, filings, history |
| pump | no model yet | 0 rows | 0 | - | - | chatter, text, llm, price_volume, size, short_interest, filings, history |

A week's model needs 50 rows and 5 positives whose labels were settled before the week began; a label settles 10 sessions (two weeks) after the flag, 15 after a 50% rise.

## Latest candidates (last 7 days)

Scores as logged when each candidate was first seen; flagged ones in bold. The LLM column gives the shares of the posts shown that are about the company, pitch it, warn about it and state a company event (counted only when its quote checks out).

| Flagged (UTC) | Ticker | Archetype | Crash risk | Pump risk | LLM about / pitch / warning / event | What the chatter was about |
|---|---|---|---|---|---|---|
| 2026-10-06 08:17 | MSTR | other | no model | no model | 100% / 0% / 0% / 0% | Users discuss holding MSTR, express bullish optimism, and question debt levels without specific corporate events. |
| 2026-10-06 00:59 | IWM | other | no model | no model | 100% / 0% / 0% / 0% | Users discuss IWM price movements, interest rate sensitivity, and express frustration or confusion about its performance. |
| 2026-10-05 23:41 | ALEC | other | no model | no model | 100% / 10% / 0% / 20% | Chatter discusses a new Genentech license agreement and buying activity for ALEC. |
| 2026-10-05 21:14 | MSFT | other | no model | no model | 100% / 0% / 0% / 0% | Chatter discusses MSFT price action, calls, and a price target raise, with mixed sentiment and no specific corporate events. |
| 2026-10-05 21:14 | QCOM | other | no model | no model | 100% / 9.1% / 0% / 9.1% | Users discuss QCOM price movements, joke about it, and mention upcoming earnings without specific buy pitches or scam warnings. |
| 2026-10-05 17:49 | IREN | other | no model | no model | 100% / 0% / 0% / 0% | Users discuss IREN stock, express confusion, joke about the name, and mention holding positions. |
| 2026-10-05 16:38 | DELL | other | no model | no model | 100% / 0% / 0% / 0% | Users discuss DELL options strategies, price levels, and potential entry points without specific company events. |
| 2026-10-05 16:24 | GME | other | no model | no model | 100% / 10% / 15% / 0% | Chatter discusses GameStop's potential acquisition of eBay, insider buying, and dilution concerns. |
| 2026-10-05 15:33 | VEEA | low float runner | no model | no model | 100% / 27% / 0% / 6.7% | Users discuss a potential short squeeze and merger news for VEEA, with mixed sentiment and no specific corporate event details. |
| 2026-10-05 15:18 | TSM | other | no model | no model | 100% / 0% / 0% / 0% | Users discuss TSMC's geopolitical risks, recent price gains, and express bullish sentiment. |
| 2026-10-05 14:51 | SPCX | other | no model | no model | 100% / 0% / 0% / 0% | Chatter discusses SPCX price movements, with some users joking about a Neptune mission and others noting general market pumping. |
| 2026-10-05 14:23 | APLD | other | no model | no model | 100% / 0% / 0% / 0% | Users discuss APLD earnings, power grid capacity, and potential price moves in anticipation of a Wednesday event. |
| 2026-10-05 14:09 | SDEV | other | no model | no model | 100% / 0% / 12% / 0% | Users discuss SDEV price volatility, express regret over losses, and question if a rug pull occurred. |
| 2026-10-05 13:55 | PMI | low float runner | no model | no model | 100% / 0% / 0% / 0% | User asks if others are holding the stock. |
| 2026-10-05 04:15 | VST | other | no model | no model | 100% / 64% / 0% / 0% | Users express extreme bullishness, claim government funding, and urge others to buy VST. |
| 2026-10-04 23:23 | DRTS | other | no model | no model | 100% / 18% / 0% / 0% | Users discuss DRTS medical technology, portfolio holdings, and express bullish enthusiasm for the stock. |

## Development walk-forward (flags before 2027-01-04)

Each development week replayed exactly as it would have run: its model trained only on labels available before the week began, scoring that week's candidates. Results count candidates whose label has settled.

### crash

No scored candidate with a settled label yet.

### pump

No scored candidate with a settled label yet.

## Hold-out (flags from 2027-01-04)

Still locked, with 0 hold-out candidates so far. They are scored like any other, but their scores are not compared with their outcomes until collection has finished and every hold-out label has settled; then they are evaluated once, into `model/holdout.md`.
