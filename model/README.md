# Stage 5 model

Updated 2026-11-04T00:24:27Z. Rule `model-v3` (docs/stage5.md on the code branch), written down before any model was trained. Every candidate is scored once, by the LightGBM model of the week it was flagged in (trained on the labels available before that week began, recent ones weighted more), and the score goes into the prospective log `model/predictions.csv`. **crash**: a close 40% or more below the flag price within 10 sessions (the avoid signal, first). **pump**: Stage 4's pump label. A candidate is flagged when its score is at least twice the base rate.

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
| 2026-11-03 23:11 | NVTS | other | 0.4% | no model | 100% / 0% / 0% / 30% | Users discuss NVTS earnings, price movements, and express bullish or bearish opinions. |
| 2026-11-03 22:03 | DAMD | other | **41%** | no model | 100% / 0% / 0% / 0% | Users discuss buying the inverse AMD ETF to short the underlying stock. |
| 2026-11-03 21:29 | ALAB | other | 0.4% | no model | 100% / 0% / 0% / 0% | Users discuss ALAB in relation to a college semiconductor event and speculate on its price movement. |
| 2026-11-03 21:29 | AMC | other | 0.1% | no model | 90% / 10% / 0% / 10% | Users discuss AMC stock, mentioning Citadel, earnings, and potential fat-finger errors. |
| 2026-11-03 21:29 | ANET | other | 0.1% | no model | 100% / 0% / 0% / 0% | Mixed chatter regarding ANET stock performance, insider selling concerns, and general market sentiment. |
| 2026-11-03 18:57 | DDOG | other | 0.2% | no model | 100% / 10% / 0% / 0% | Users discuss DDOG stock prices, express hope for recovery, and mention buying calls. |
| 2026-11-03 17:35 | TSM | other | 0.1% | no model | 100% / 0% / 0% / 0% | Users discuss TSM price movements, supply chain issues, and express bullish sentiment with no specific company events mentioned. |
| 2026-11-03 15:08 | AEHR | other | 0.6% | no model | 100% / 60% / 0% / 30% | Users discuss AEHR earnings, short squeeze potential, and express bullish expectations for a price pump. |
| 2026-11-03 14:58 | OKLO | other | 0.1% | no model | 100% / 0% / 0% / 0% | Users discuss OKLO price history, portfolio performance, and express confusion or regret over recent losses. |
| 2026-11-03 08:03 | IREN | other | 0.4% | no model | 100% / 9.1% / 0% / 4.5% | Mixed chatter on IREN ranging from bullish earnings rumors to bearish price targets and jokes. |
| 2026-11-03 07:23 | APLD | other | 0.2% | no model | 100% / 0% / 0% / 0% | Users express extreme distress, massive losses, and frustration over the stock's decline. |
| 2026-11-03 00:57 | AAOI | other | 1.2% | no model | 100% / 35% / 0% / 24% | Users discuss AAOI earnings, potential AMD partnership rumors, valuation, and recent dilution. |
| 2026-11-02 21:58 | AMD | other | 0.1% | no model | 100% / 0% / 0% / 2.5% | Users discuss AMD's high valuation, upcoming earnings, and potential price drops while debating AI sector trends. |
| 2026-11-02 21:45 | ASTS | other | 0.2% | no model | 100% / 10% / 0% / 0% | Users discuss ASTS stock performance, express frustration over delays, and debate buying opportunities. |
| 2026-11-02 21:29 | HTZ | other | 0.1% | no model | 100% / 0% / 0% / 20% | Users discuss HTZ earnings and price movements with mixed optimism and skepticism. |
| 2026-11-02 21:16 | LITE | other | 7.3% | no model | 100% / 0% / 0% / 100% | Chatter focuses on the MRVL/LITE acquisition deal, with mixed reactions regarding valuation, dilution, and market impact. |
| 2026-11-02 21:05 | MRVL | other | 1.6% | no model | 100% / 0% / 0% / 100% | Users discuss the negative market reaction to Marvell's acquisition of Lumentum, citing dilution and deal terms. |
| 2026-11-02 20:10 | AAPL | other | 0.0% | no model | 100% / 0% / 0% / 5.0% | Users discuss AAPL earnings expectations, bearish sentiment, and potential market crashes. |
| 2026-11-02 20:10 | WMT | other | 0.2% | no model | 100% / 0% / 0% / 0% | Users discuss Walmart stock, mentioning supply runs, price levels, and comparing it to other companies. |
| 2026-11-02 19:43 | MU | other | 0.1% | no model | 100% / 12% / 0% / 0% | Chatter is a mix of extreme bearish panic, bankruptcy rumors, and sudden bullish calls to buy. |
| 2026-11-02 18:46 | SMCI | other | 0.1% | no model | 100% / 9.1% / 9.1% / 18% | Users discuss SMCI earnings, valuation, and potential fraud risks while listing it in an earnings calendar. |
| 2026-11-02 17:39 | SOUN | other | 0.1% | no model | 100% / 69% / 3.8% / 0% | Chatter focuses on a potential short squeeze for SOUN, with one user warning it is a pump and dump. |
| 2026-11-02 15:08 | RKLB | other | 0.1% | no model | 100% / 0% / 0% / 0% | Users discuss RKLB holdings, past performance, and general market sentiment without specific upcoming events. |
| 2026-11-02 13:09 | PLTR | other | 0.1% | no model | 100% / 0% / 0% / 0% | Mixed chatter regarding PLTR options, earnings expectations, and general market sentiment. |
| 2026-11-02 07:17 | ATC | other | 1.0% | no model | 0% / 0% / 0% / 0% | All documents discuss a Lear jet crash ATC audio, not the GraniteShares Autocallable COIN ETF. |
| 2026-11-01 19:38 | NNN | other | no model | no model | 10% / 10% / 0% / 0% | Chatter focuses on a 'NNN challenge' and slang usage rather than the REIT stock. |
| 2026-10-31 21:03 | MSOS | other | no model | no model | 100% / 10% / 0% / 0% | Users discuss MSOS ETF price movements, election catalysts, and past losses without specific company events. |
| 2026-10-31 02:57 | INO | other | no model | no model | 100% / 0% / 0% / 0% | Chatter discusses INO's price movement following FDA approval rumors and insider leak claims. |
| 2026-10-31 00:58 | GLD | other | no model | no model | 100% / 0% / 0% / 0% | Users discuss GLD price drops, express frustration, and place bearish bets. |
| 2026-10-31 00:51 | AAOI | other | no model | no model | 100% / 0% / 0% / 0% | Chatter focuses on AAOI price volatility, user holdings, and a specific warning about customer concentration risks. |
| 2026-10-31 00:21 | QCOM | other | no model | no model | 100% / 10% / 0% / 10% | Users discuss QCOM earnings, express bearish views on price drops, and some buy positions. |
| 2026-10-30 22:07 | TLT | other | no model | no model | 100% / 0% / 0% / 0% | Users discuss TLT price movements, trading strategies, and comparisons to other assets without specific corporate events. |
| 2026-10-30 19:57 | SOXL | other | no model | no model | 100% / 5.0% / 0% / 0% | Users discuss SOXL's massive drop, margin calls, and leveraged ETF risks. |
| 2026-10-30 19:04 | SOXX | other | no model | no model | 100% / 17% / 0% / 0% | Users discuss SOXX price drops, portfolio composition, and market volatility with mixed bullish and bearish sentiments. |
| 2026-10-30 18:26 | TQQQ | other | no model | no model | 100% / 0% / 0% / 0% | Users discuss TQQQ price levels, express bullish optimism, and joke about potential drops or gains. |
| 2026-10-30 17:43 | INTL | other | no model | no model | 90% / 0% / 0% / 0% | Users discuss INTL's price drop, confusion over its identity, and comparisons to other stocks. |
| 2026-10-30 17:00 | APP | other | no model | no model | 100% / 0% / 0% / 0% | Users discuss APP stock price drops, express confusion about upcoming earnings, and joke about portfolio losses. |
| 2026-10-30 17:00 | SBUX | other | no model | no model | 100% / 10% / 0% / 20% | Mixed chatter on SBUX including earnings surprise, CEO praise, and unrelated jokes. |
| 2026-10-30 17:00 | SPY | other | no model | no model | 100% / 2.5% / 0% / 0% | Users discuss SPY price action, volatility, and trading strategies with mixed bullish and bearish sentiments. |
| 2026-10-30 16:45 | RSP | other | no model | no model | 100% / 0% / 0% / 0% | Users discuss RSP outperforming SPY and QQQ, with some mentioning calls and portfolio gains. |

## Development walk-forward (flags before 2027-01-04)

Each development week replayed exactly as it would have run: its model trained only on labels available before the week began, scoring that week's candidates. Results count candidates whose label has settled.

### crash

No scored candidate with a settled label yet.

### pump

No scored candidate with a settled label yet.

## Hold-out (flags from 2027-01-04)

Still locked, with 0 hold-out candidates so far. They are scored like any other, but their scores are not compared with their outcomes until collection has finished and every hold-out label has settled; then they are evaluated once, into `model/holdout.md`.
