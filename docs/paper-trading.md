# Paper trading rule (`paper-v1`)

Written down on 2026-10-07, before any model was trained and before any Stage 3 outcome or Stage 4 label row was
opened, so the trades can't be fitted to results. Change it only as a new version written here first, with the
reason. Research behind each choice: `research/trading-risk-findings.md` in the project files.

No real money, ever. The simulator runs in GitHub Actions on Stage 3's daily bars (`track/daily.csv`), needs no
broker account, and is built once the first crash models exist. It starts trading (Phase 2 of the brief's plan) only
after the crash model passes its five robustness checks on the development replay (docs/stage5.md); until then
Phase 1, the prospective log `model/predictions.csv`, is the only output.

## The trade

The evidence (Robinhood herding, OTC tweet spikes, small-cap gap-ups) says attention spikes give back part of the
move within days, so the trade is a short after the spike has started to fail, held at most 10 sessions.

| | Rule |
|---|---|
| Which candidates | flagged by the crash model (score at least twice the base rate, docs/stage5.md); listed (not OTC); price $1 or more at entry; 20-day average dollar volume $1M or more |
| Entry | the open of the session after the first red day: the first session among sessions 0-5 after the flag (session 0 = the flag's own session if it hadn't closed yet) whose close is below the close before it. No red day by session 5 means no trade |
| Skip | if SSR (SEC Rule 201) is in force at entry: the red day's low was 10% or more below the close before it |
| Stop (upper barrier) | the highest high from the flag to the entry; a trade whose stop would be more than 30% above the entry is skipped |
| Profit target (lower barrier) | 30% below the entry |
| Time exit (vertical barrier) | the close of session 10 after entry |
| Fills | at the barrier price, or at the session's open if it opens beyond the barrier (gaps and halts are paid in full); if one session reaches both the stop and the target, the stop counts |

## Sizing and limits

| | Rule |
|---|---|
| Paper equity | $100,000 at the start |
| Risk per trade | 0.5% of current equity: shares = 0.005 x equity / (stop - entry), rounded down |
| Position cap | 5% of equity, and 1% of the stock's 20-day average dollar volume |
| Portfolio caps | at most 5 open shorts, at most 25% of equity short in total, one position per stock; a trade that would break a cap is skipped, not shrunk |
| Circuit breaker | no new entries once equity is 10% below its peak, until shouvik reviews it |
| Not in `paper-v1` | Kelly sizing and sizing by model score; considered after 100 paper trades, as `paper-v2` |

## Costs

| | Base case | Stress |
|---|---|---|
| Slippage, round trip | 2% of entry value | 3%, and 5% |
| Borrow fee | 50% a year on the entry value, per calendar day held | 200% a year |
| Commission | 0 | 0 |

If a free daily borrow-fee source becomes part of the data (the Interactive Brokers short-stock file is the
candidate), its fee replaces the base case and the stress stays at 200%.

## How it is judged (Phase 3)

- The same rule, unchanged, on candidates the model didn't flag and on the matched controls (Stage 2), so the result
  shows whether the model adds anything beyond "short anything that spiked".
- Reported per trade: expectancy after costs, hit rate, profit factor; for the account: worst drawdown and the
  Sharpe ratio, deflated for the three cost cases tried.
- **Profitable** only if, with at least 30 trades: expectancy is positive under 3% slippage and 200% borrow, and
  beats both comparison groups. Fewer than 30 trades is "not enough data yet", not a failure.
- Trades on hold-out candidates (flagged from 2027-01-04) are reported separately, once, with the model's hold-out
  evaluation.
