# Stage 5 model

Updated 2026-10-06T02:40:13Z. Rule `model-v1` (docs/stage5.md on the code branch), written down before any model was trained. Every candidate is scored once, by the LightGBM model of the week it was flagged in (trained on the labels available before that week began, recent ones weighted more), and the score goes into the prospective log `model/predictions.csv`. **crash**: a close 40% or more below the flag price within 10 sessions (the avoid signal, first). **pump**: Stage 4's pump label. A candidate is flagged when its score is at least twice the base rate.

## This week's models (week of 2026-10-05)

| Target | Status | Trained on | Positives | Base rate | Flag at | Feature groups |
|---|---|---|---|---|---|---|
| crash | no model yet | 0 rows | 0 | - | - | chatter, text, llm, price_volume, size, short_interest, filings |
| pump | no model yet | 0 rows | 0 | - | - | chatter, text, llm, price_volume, size, short_interest, filings |

A week's model needs 50 rows and 5 positives whose labels were settled before the week began; a label settles 10 sessions (two weeks) after the flag, 15 after a 50% rise.

## Latest candidates (last 7 days)

Scores as logged when each candidate was first seen; flagged ones in bold. LLM ratings are 0-3.

| Flagged (UTC) | Ticker | Archetype | Crash risk | Pump risk | LLM promotion / coordination / news | What the chatter was about |
|---|---|---|---|---|---|---|
| 2026-10-06 00:59 | IWM | other | no model | no model | 0 / 1 / 0 | Strong negative sentiment and criticism of IWM's price movement amid interest rate concerns. |
| 2026-10-05 23:41 | ALEC | other | no model | no model | 1 / 0 / 3 | Positive sentiment driven by a major Genentech license agreement announcement |
| 2026-10-05 21:14 | MSFT | other | no model | no model | 3 / 2 / 0 | Widespread bullish hype with price targets and viral memes driving MSFT enthusiasm |
| 2026-10-05 21:14 | QCOM | other | no model | no model | 1 / 0 / 1 | Discussion centers on QCOM's earnings and valuation, with mixed sentiment and mild promotional elements. |
| 2026-10-05 17:49 | IREN | other | no model | no model | 0 / 0 / 0 | Discussion is speculative, lacking concrete events or clear sentiment. |
| 2026-10-05 16:38 | DELL | other | no model | no model | 1 / 1 / 0 | Positive sentiment with speculative price targets and hype around DELL's potential surge |
| 2026-10-05 16:24 | GME | other | no model | no model | 1 / 1 / 0 | Reddit chatter promotes GME with insider buying and trend-based bullishness, despite skepticism and criticism. |
| 2026-10-05 15:33 | VEEA | low float runner | no model | no model | 1 / 1 / 1 | Retail bullishness around merger news with short squeeze expectations |
| 2026-10-05 15:18 | TSM | other | no model | no model | 1 / 1 / 0 | TSM is being heavily discussed with bullish sentiment and price-driven hype. |
| 2026-10-05 14:51 | SPCX | other | no model | no model | 3 / 3 / 0 | Extensive hype and price targets with no real company updates or events. |
| 2026-10-05 14:23 | APLD | other | no model | no model | 2 / 3 / 0 | Multiple users promote APLD with hype around earnings, using repetitive phrases and coordinated messaging. |
| 2026-10-05 14:09 | SDEV | other | no model | no model | 1 / 1 / 0 | SDEV price drop sparks panic and confusion among traders |
| 2026-10-05 13:55 | PMI | low float runner | no model | no model | 0 / 1 / 3 | Reddit chatter focuses on upcoming ISM PMI data and market reaction, with some coordination in timing and phrasing. |
| 2026-10-05 04:15 | VST | other | no model | no model | 3 / 3 / 0 | Intense bullish hype and coordinated promotion of VST with no concrete company events. |
| 2026-10-04 23:23 | DRTS | other | no model | no model | 3 / 0 / 0 | Excited hype and speculative enthusiasm about DRTS's cancer treatment potential with no concrete news. |

## Development walk-forward (flags before 2027-01-04)

Each development week replayed exactly as it would have run: its model trained only on labels available before the week began, scoring that week's candidates. Results count candidates whose label has settled.

### crash

No scored candidate with a settled label yet.

### pump

No scored candidate with a settled label yet.

## Hold-out (flags from 2027-01-04)

Still locked, with 0 hold-out candidates so far. They are scored like any other, but their scores are not compared with their outcomes until collection has finished and every hold-out label has settled; then they are evaluated once, into `model/holdout.md`.
