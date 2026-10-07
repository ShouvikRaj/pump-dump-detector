# Stage 5 design notes: model, retraining and validation

Stage 5 turns the labeled history into a model that scores every new candidate at its flag time, retrains it
every week as Stage 4's labels arrive, and evaluates it the way the project brief asks: walk-forward over a
development period, then once on a locked hold-out period at the end.

The rule was first written down and committed on 2026-10-06 as `model-v1` (with `text-v1` and `llm-v1`), before any
model was trained and before any Stage 3 outcome or Stage 4 label row was opened. The same day, still before any model
was trained or any outcome or label row opened, it was replaced by `model-v2` (with `text-v2` and `llm-v2`), and on
2026-10-07, again before any model was trained or any outcome or label row opened, by `model-v3` (adds the
`technical` group, `technical-v1`), which this file describes: "Changing the rule" lists what changed and why, and "What had been seen" at the end lists what
was known each time. Change it only as a new version written here first.

## What is predicted

| Target | Positive | Negative | Why |
|---|---|---|---|
| `crash` (first) | Stage 4's `crash_10 = 1`: a close 40% or more below the flag price within 10 sessions | `crash_10 = 0` | the brief's safer first test: an "avoid" signal, nobody has to trade |
| `pump` | Stage 4's `label = pump` (`label-v1`) | `label = not_pump` or `real_news` | the main label; news-driven moves are negatives, telling them apart is part of the job |

A row joins a target once that target has settled in `labels/labels.csv` (`crash_10` not blank; `label` not
`pending` or `unknown`). Snapshots without a price (`archetype = unknown`) are left out.

**Rows.** Models are trained on every Stage 2 snapshot, candidates **and** their matched controls: the controls
are the brief's "negative examples" with no chatter, and they teach the market-only part of a crash. Scores,
signals and every metric below are for **candidates only**, the population the signal is meant for.

## When a label counts (no lookahead)

A label exists only after its window has closed, and so does the market's behaviour in that window. A row may be
used to train a model only from `available_at` on:

- `crash`: the close of session 10 (Stage 3's session dates in `track/daily.csv`) plus 4 hours;
- `pump`: the close of session 15 plus 4 hours if `ret_max_5 >= 0.50` (the drop is measured over the 10 sessions after
  the peak), otherwise session 10 plus 4 hours;
- if tracking ended before that session, the close of the last session recorded, plus 4 hours.

4 hours covers Stage 3's hour-old-close rule and the daily `track` and `label` runs after it. The same rule is used for
the live model and for the walk-forward replay, so the replay reproduces what the live loop could have known.

## Features (`model-v3`)

Only what was known at the flag time: Stage 1's episode rows, Stage 2's snapshot row, the text of the Reddit
documents counted in the episode, Stage 4 labels already usable then (by the rule above), and the raw Stage 2 price
bars and daily Nasdaq cross-section for the `technical` group. Nine groups; controls
have no chatter, so their chatter counts are 0 and every other chatter, text and LLM feature is blank (LightGBM treats
blank as missing).

| Group | Features |
|---|---|
| `chatter` (Stage 1) | `mentions_log` ln(1 + mentions_24h), `baseline_log` ln(1 + baseline_mean), `spike_z` z, `authors_ratio` authors / mentions, `post_share` posts / mentions, `hype_share` hype documents / mentions, `hype_spike` (the flag's reasons include the hype spike), `wsb_share` and `pennystocks_share` (by_subreddit / mentions), `cashtag_share` (cashtag mentions / mentions), `stocktwits_trending` (on StockTwits' trending list at the flag) |
| `text` (`text-v2`, below) | `top_author_share`, `dup_share`, `near_dup_share`, `promo_share`, `squeeze_share`, `news_share`, `dilution_share`, `link_share`, `multi_ticker_share`, `length_log` |
| `llm` (`llm-v2`, below) | `llm_about_share`, `llm_pitch_share`, `llm_warning_share`, `llm_event_share` (shares of the documents shown), `llm_sentiment` (-2 to 2) |
| `price_volume` (Stage 2) | `price_log` ln(price_at_flag), `move_since_close`, `ret_1d`, `ret_5d`, `ret_20d`, `rel_vol_last_log` ln(1 + rel_vol_last), `rel_vol_today_log` ln(1 + rel_vol_today), `volatility_20d`, `pct_from_52w_high`, `dollar_vol_log` ln(1 + dollar_vol_20d) |
| `size` (Stage 2) | `market_cap_log` ln(1 + market_cap), `float_log` ln(1 + float_shares, else shares_outstanding), `turnover_last`, `listing_age_log` ln(1 + days since first_trade_date), `reverse_splits_1y`, `otc` (venue is OTC), `institution_pct` |
| `short_interest` (Stage 2) | `si_pct_float`, `si_days_to_cover`, `si_change` si_shares / si_prev_shares - 1 |
| `filings` (Stage 2) | `sec_filer` (has a CIK), `dilution_90d`, `offerings_424b_30d`, `days_since_dilution`, `current_reports_30d`, `days_since_report`, `report_hard_news` (the last 8-K before the flag has item 2.02, 2.01, 5.01, 1.03 or 1.01), `unregistered_sales_90d`, `late_notices_365d`, `name_change_1y` |
| `technical` (`technical-v1`, from Stage 2's raw bars, below) | `vwap_ext`, `off_high`, `mins_since_high`, `gap_open`, `ret_60m`, `vol_60m_rel`, `max_ret_20d`, `up_streak`, `run_up`, `atr_stretch`, `ssr_today`, `runners_breadth` |
| `history` (Stages 1 and 4) | `prior_flags_90d` (earlier flags of the same stock in the 90 days before this one), `days_since_prior_flag` (blank if none), `prior_crashes` (earlier flags of the same stock that crashed, `crash_10 = 1`, counted once that label was usable as in "When a label counts") |

The archetype is not a feature (it is a function of price, float and venue, which are); it is used to report results
per pump type.

### Technical features (`technical-v1`)

How stretched a spike was at the flag, computed by `technical.py` from the raw data Stage 2 saved for each snapshot
(`market/raw/`: about 2 years of daily bars and about 5 days of 5-minute bars, pre- and post-market included) and from
the daily Nasdaq cross-section (`market/universe/`). Only bars finished by `as_of` count; "the flag's day" is its ET
date. Each snapshot gets one row in `model/technical.csv`, written once and never changed. Sources and reasons:
`research/trading-risk-findings.md` in the project files.

| Feature | Definition |
|---|---|
| `vwap_ext` | price at flag (as Stage 2 defines it) / VWAP of the flag day's regular-session 5-minute bars - 1; VWAP uses each bar's (high + low + close) / 3 |
| `off_high` | price at flag / highest high of the flag day's bars, pre- and post-market included - 1 |
| `mins_since_high` | minutes from the end of that highest bar to the flag |
| `gap_open` | first regular-session bar's open on the flag day / the last close before that day - 1 |
| `ret_60m` | price at flag / close of the last bar that ended at least 60 minutes before the flag - 1; blank if that bar ended more than 2 hours before |
| `vol_60m_rel` | regular-session volume in the hour before the flag / (mean daily volume of the last 20 closed sessions x the session minutes in that hour / 390); blank with fewer than 5 session minutes |
| `max_ret_20d` | largest close-to-close return among the last 20 closed sessions (the MAX effect) |
| `up_streak` | closed sessions in a row, up to the last, that closed above the session before |
| `run_up` | last close / lowest close of the last 10 closed sessions - 1 |
| `atr_stretch` | (last close - mean of the last 20 closes) / mean true range of the last 14 sessions |
| `ssr_today` | 1 if the last closed session's low, or the flag day's regular-session low so far, was 10% or more below the close before it (SEC Rule 201 restricts shorting that day and the next), else 0 |
| `runners_breadth` | listed stocks under $10 up 40% or more in the latest cross-section whose session had closed by the flag (a mania gauge) |

Blank (missing to LightGBM) where the bars don't allow a value: weekends and overnight flags have no flag-day bars,
OTC stocks have no pre- or post-market bars. The `model` job computes rows for snapshots whose raw file is in its
checkout (the last `RAW_DAYS` days); older ones were backfilled once by a run with a longer window.

### Text features (`text-v2`)

The documents are the ones behind the episode's `mentions_24h`: posts and comments in the three subreddits that
mention the ticker, created in the 24 hours up to the flag and **collected by** the flag time, bots excluded. Shares
are over those documents. They are found with Stage 1's current extractor (`tickers-v4` since 2026-10-06), whichever
version flagged the episode, so an episode flagged on mentions a later extractor ignores is described by the
documents still counted (PMI's r/wallstreetbets documents, about the ISM index, dropped out under `tickers-v4`).

| Feature | Definition |
|---|---|
| `top_author_share` | documents by the most active author |
| `dup_share` | documents whose normalised text (lower case, links, digits and the ticker removed, at least 20 letters, first 200 characters) also appears under a different author: copy-paste, coordinated phrasing |
| `near_dup_share` | documents that share at least half of their three-word sequences (Jaccard similarity of word triples of the same normalised text, at least 8 words) with a document by a different author: reworded copies of one pitch, which `dup_share` misses |
| `promo_share` | documents using any of Stage 1's sales-pitch hype categories: urgency, price_target, low_float, gem, next_big, multibagger |
| `squeeze_share` | documents using the squeeze category |
| `news_share` | documents naming a company event: earnings, revenue, guidance, FDA, approval, clinical trial, contract, partnership, merger, acquisition, buyout, press release, "announced", 8-K |
| `dilution_share` | documents naming dilution: offering, dilution, warrants, reverse split, shelf, S-1, S-3, 424B |
| `link_share` | documents linking outside Reddit and image hosts (press releases, articles, promoter sites) |
| `multi_ticker_share` | documents that mention other tickers too (watch lists rather than one pitch) |
| `length_log` | ln(1 + mean characters per document) |

They are computed once per candidate, soon after the flag, and stored (`model/text.csv`). A candidate with only
`text-v1` features is redone as `text-v2` by the next run that has its raw files checked out; the old row stays.

### LLM labels (`llm-v2`)

The brief gives the LLM two jobs: read the post text (hype, coordinated phrasing, bot-like accounts) and check
news and filings, to separate pumps from real news. `llm-v2` gives it only work whose answer can be checked against
the documents, and leaves judging and counting to code (why: "Changing the rule", `model-v2`). Once per candidate, a
language model reads:

- the same documents as the text features: posts first, then the most recent comments, each cut to 400 characters,
  at most 40 documents and 12,000 characters, **numbered** [1], [2], ...; authors replaced by A1, A2, ... so repeated
  posting stays visible;
- the company name, venue and price at the flag, and the SEC filings Stage 2 found before the flag (date and items of
  the last 8-K/6-K, date and form of the last registration or prospectus).

It answers in JSON, with one label for every document, by its number:

| Label | The document |
|---|---|
| `other` | is about the company but fits none of the labels below; most documents: questions, price talk, opinions, jokes, saying one owns it, likes it or expects it to rise |
| `not_this_company` | uses the ticker for something else: another company or fund, an index or economic report, an abbreviation or an ordinary word |
| `pitch` | tries to get others to buy: price targets, rockets or "to the moon", "about to pop", "squeeze incoming", urgency ("don't miss", "get in before"), telling people to buy |
| `warning` | calls it a pump-and-dump, scam or rug pull, or warns others of dilution, an offering or a coming dump (plain bearish opinions are `other`) |
| `event` | states a specific company event, announced or scheduled: earnings, an FDA or other regulatory decision, a contract or government award, a partnership, a merger or acquisition, an offering or financing (rumours, jokes, price moves and opinions are not events) |
| `pitch_and_event` | both |

and four more fields: `summary` first (what the chatter is about, at most 20 words; report only), `event_type`
(none, earnings, regulatory, deal, financing or other; report only), `event_quote` (up to 15 words copied exactly
from an event document) and `sentiment` (-2 bearish to 2 bullish, about the company).

The code checks the answer before anything is counted:

- the format (these fields, one of the six labels for every document shown, sentiment -2 to 2) is enforced by the
  server as a JSON-schema grammar and checked again by the parser, because llama.cpp can silently drop a grammar it
  fails to parse; an answer that doesn't parse is a failed rating;
- labels for documents not shown, unknown labels and missing ones are unusable: that document counts as `other`, and
  the number is recorded;
- a document that names the stock as a cashtag or with its exchange (Stage 1's extraction method) is about the stock,
  whatever its label says;
- the event documents count only if the event quote is found in one of the documents (at least 80% of it in one
  piece, ignoring case and punctuation); otherwise the event share is 0.

Features, as shares of the documents shown: `llm_about_share` (not `not_this_company`), `llm_pitch_share` (`pitch`
or `pitch_and_event`), `llm_warning_share`, `llm_event_share` (`event` or `pitch_and_event`; 0 unless the quote checks
out), each counting only documents about the stock, and `llm_sentiment`. The labels are stored as four lists of
document numbers (`not_about`, `pitch`, `warning`, `event`).
Coordination is no longer asked of the LLM: the text features measure it directly (`dup_share`, `near_dup_share`,
`top_author_share`).

- Model: chosen by the test below and run by llama.cpp's server (release `b10456`, with `--jinja`, so the model's own
  chat template applies and thinking mode is off) on the workflow's own runner (`scripts/llm_server.sh`; both
  downloads pinned and cached). No account, key, paid plan or outside service. Temperature 0, seed 0. The model's
  training data ends before these flags, and it sees nothing written after the flag.
- Each rating is stored once in `model/llm.csv` with the lists, the quote, the result of the checks (`llm_checks`),
  `llm-v2`, the model id and a hash of the prompt, and never recomputed. If the server is down, the rating is retried
  on later runs for 3 days after the flag, then recorded as failed (features blank); an answer that doesn't parse is
  recorded as failed at once (at temperature 0 the same prompt gets the same answer), and a candidate whose flag
  documents can't be found in the raw files is recorded as `no_documents`. A run starts no new rating after 90
  minutes (about 30 candidates with the chosen model); the rest wait for the next run. A candidate is scored only
  once its rating exists or has been given up on, so its one score includes the rating whenever there is one. If
  ratings keep failing, the `llm` group is simply blank and the pruning rule below drops it.
- Only ratings of the current version are features. A candidate rated by an older version is rated again by the next
  run that has its raw files checked out (the old row stays in the file); one whose raw files are no longer checked
  out keeps a blank `llm` group. A redo never holds up the candidate's one score.
- Changing the model or the prompt is a new `llm` version; old ratings keep theirs.

### Testing the LLM step

A prompt or model is tested before its ratings are stored. `docs/stage5-llm-gold.json` holds hand labels for the
documents shown for the first 15 candidates (265 documents, flagged 2026-10-04 to 06): for each of the four lists,
the documents clearly in it (`yes`) and the arguable ones (`maybe`, counted neither way), labelled from the documents
alone before any `llm-v2` answer existed. The `llm-eval` workflow rates the candidates whose raw files it checks out
with a given model and the current prompt, and reports per list the documents right (in the model's list, labelled
yes), wrong (in its list, labelled neither yes nor maybe) and missed (labelled yes, not in its list), counting only
labelled documents the prompt still shows, plus quotes found and seconds per candidate. It writes nothing to the
data branch.

The `llm-v2` model was chosen this way, by a rule fixed before the runs. Three open-weights models small enough for a
free runner's CPU, all 4-bit (`Q4_K_M`) GGUF files from unsloth pinned by revision, with the same prompt, llama.cpp
build and settings: Qwen3-4B-Instruct-2507 (the `llm-v1` model), Qwen3.5-4B and Qwen3.5-9B (all Apache 2.0). The model
with the most right minus wrong over `not_about`, `pitch` and `event` together wins, among those with no unparseable
answer and at most 3 minutes per candidate on average; of the models within 5 of the best, the fastest. (`warning`
has one clear document in the set, too few to compare.) The results are at the end of this file.

## The model

LightGBM, binary, fixed parameters (no tuning on results): learning rate 0.05, 150 rounds, 7 leaves, depth 3,
at least 10 rows per leaf, 80% feature and row sampling per round, L2 1.0, seed 0, one thread, deterministic. One
model per target. No class reweighting, so scores stay comparable to base rates.

**Recency.** Each training row is weighted by 0.5^(age / 56 days), age measured from the training cut-off to the
row's flag time: an 8-week half-life, so the model follows the newest patterns (pattern decay) without forgetting
older ones.

**Weekly retraining.** Weeks start Monday 00:00 UTC. The model for week W is trained on every row whose label was
available before W began, and scores the candidates flagged during W. It trains only when that set holds at least
50 rows and 5 positives; otherwise week W has no model and its candidates get no score.

## The signal

The score is the model's probability. A candidate is **flagged** (high risk) when its score is at least **twice
the base rate**: the recency-weighted share of positives among the training set's candidates (at least 1%). Lift 2
is a "much likelier than a typical candidate" line that doesn't depend on how rare the target is.

**Prospective log.** Each candidate is scored once, by the first daily run after its flag that has its LLM rating
(above), with its week's model,
and the score, the threshold, whether it was flagged and the model's training size are appended to
`model/predictions.csv` with the time. That file is never rewritten: it is Phase 1 of the paper-trading plan
(signal-only logging), and it is what the hold-out is judged on.

## Walk-forward validation (development period)

**Development period: candidates flagged before 2027-01-04 00:00 UTC.** On every run, each development week is
replayed: the week's model is trained exactly as above (labels available before the week began) and scores that
week's candidates, so every development score is out of sample. Metrics pool the replayed scores of candidates whose
target has settled:

- base rate, positives, flagged, **precision, recall, F1** of the flag, and lift (precision / base rate);
- threshold-free: average precision (AP; a random score gets the base rate) and ROC AUC;
- for all candidates, for each archetype (`low_float_runner`, `otc_penny`, `other`), and for the two pump types
  together;
- in three consecutive blocks of development weeks (as equal in length as possible), the "separate time periods".

The replay is recomputed every run because labels keep settling; it is deterministic given the data.

## Robust or not

The brief: a robust pattern works across separate time periods, holds per pump type, survives 1-3% slippage and
clearly beats the control group. For each target, five checks on the development replay (all candidates):

| Check | Passes when | Needs at least |
|---|---|---|
| beats the base rate | precision >= 1.5 x base rate and AP > base rate | 10 positive candidates |
| separate periods | precision > base rate in each of the three blocks | 3 positives in every block |
| per pump type | precision > that archetype's base rate, in `low_float_runner` and in `otc_penny` | 5 positives in the archetype (else that archetype is skipped; both skipped = not enough data) |
| beats the control group | target rate of flagged candidates > target rate of their own matched controls | 10 flagged candidates with settled controls |
| survives slippage | flagged candidates' mean 10-session return (Stage 3's `ret_close_10`) <= -3%, and below the unflagged candidates' mean | 10 flagged candidates with `ret_close_10` |

A target's signal is **robust** when all five pass. Each check is reported as pass, fail or not enough data yet. The
slippage check reads the signal as "avoid": a holder who skipped the flagged candidates saved more than a 3% round
trip (the top of the brief's 1-3% range). Nothing here trades or shorts.

## Pruning weak feature groups (the feedback loop)

"Keep only robust patterns, prune weak ones" applies to the nine feature groups. Once a target's development replay
holds **20 positive candidates**, every run also replays the development weeks with each group left out. A group
is **weak** when leaving it out does not lower AP: AP without it >= AP with all groups, both pooled and in at least
two of the three blocks. The model that scores new candidates (the deployed model) uses every group except the
weak ones (if every group came out weak, none is dropped). Before 20 positives, all groups are used.

The replay also reports two reference models: market only (`price_volume`, `size`, `short_interest`, `filings`) and
social only (`chatter`, `text`, `llm`), which answer whether combining the two beats either alone. `history` is in
neither.

Pruning is chosen on the development weeks, so the deployed model's replay score is optimistic and is labeled that
way; the robustness checks above use the all-groups replay, and the hold-out judges the deployed model.

## The locked hold-out

**Hold-out: candidates flagged on or after 2027-01-04 00:00 UTC.** Collection stops by itself between early February
and early April 2027 (README, "How long it runs"), so the hold-out is at least the final four weeks of flags and grows
if collection runs longer.

- Hold-out candidates are scored like any other, once, into the prospective log (scores are not outcomes).
- Their scores are not compared with their labels, and no metric on them is computed, printed or written, until
  collection has finished, every hold-out snapshot has been tracked and none of their targets is pending. No one
  should compare them by hand either. (A hold-out snapshot that Stage 4 never labels at all stops holding this up
  45 days after the last flag, and is left out.)
- Pruning decisions use development weeks only, and nothing in this file may change on or after 2027-01-04. A rule
  change made after that date anyway makes the hold-out result invalid, and the report must say so.
- Their labels do train the models of later weeks once available, as a live system would; each hold-out score is
  still made before its own outcome existed.
- When the condition holds, the next run computes the final evaluation once, from the prospective log, with the same
  metrics and checks, writes it to `model/holdout.md` and `model/holdout.csv`, and never recomputes it.

## Outputs (on the `data` branch)

| Path | What |
|---|---|
| `model/text.csv` | append-only: text features of each candidate (`text-v2`; older `text-v1` rows kept), with the document count and when they were computed |
| `model/llm.csv` | append-only: LLM labels of each candidate (`llm-v2`; older `llm-v1` ratings kept), with the document lists, event quote, checks, model id, prompt hash, status and time |
| `model/predictions.csv` | append-only: the prospective log, one row per candidate and target |
| `model/walkforward.csv` | rebuilt every run: the development replay, one row per development candidate (scores of the all-groups and deployed models per target, and the targets) |
| `model/README.md` | the report: model status, latest scores, development results, robustness checks, feature groups kept or pruned, hold-out status |
| `model/holdout.md`, `model/holdout.csv` | the final hold-out evaluation, written once |
| `model/state.json` | LLM retry bookkeeping (internal) |

`python -m pumpdump build-db` loads them as `model_text`, `model_llm`, `model_predictions` and `model_walkforward`.

## When it runs and when it stops

The `model` workflow runs once a day after Stage 4's labels: `scripts/pace.sh` starts it at the first pacer after
00:11 UTC (the label run's slot is 23:21), with a `11 0 * * *` cron as backup. It reads the candidates, snapshots,
Stage 3 sessions and outcomes, Stage 4 labels and the last few days of raw Reddit files, and writes only `model/`.
Once the hold-out evaluation has been written, it turns itself off.

## Changing the rule

Write the new version here first, with the reason, before running it, and keep the old version's results next to it.
Never tune features, parameters, thresholds or the hold-out date on results. Nothing may change on or after the
hold-out start (2027-01-04).

### `model-v3` (2026-10-07, before any model was trained)

Prompted by shouvik's request (2026-10-06) to use trading and risk-management research to find market patterns; the
research is in `research/trading-risk-findings.md` in the project files. Only the features changed: a ninth group,
`technical` (above), which is also part of the "market only" reference model. The targets, label timing, the model and
its parameters, the signal, the validation, the robustness checks, the pruning rule and the hold-out did not change.
Pruning treats the group like any other, so it is dropped automatically if it doesn't help.

| Change | Why |
|---|---|
| `vwap_ext`, `off_high`, `mins_since_high`, `gap_open` | Spikes on retail attention fade within days (Barber, Huang, Odean & Schwarz 2022: Robinhood herding events +14% on the day, then -3.5% over 5 days; Renault 2018: -3.1% over 5 days after OTC tweet spikes). In a vendor's data on 3,000+ small-cap gap-ups (SmallCapLab, 2022-26), 75% closed below VWAP, 67% below their open, and 63% had made their high of the day before 10:00. These say how far the spike had already run or rolled over. |
| `ret_60m`, `vol_60m_rel` | The last hour's return and volume before a pump were the strongest predictors in Xu & Livshits (2019) and Nghiem et al. (2021); listed in stage5-findings as the biggest missing feature. 5-minute bars, which Stage 2 already saves, are enough. |
| `max_ret_20d` | Stocks with the largest one-day return in the past month underperform (Bali, Cakici & Whitelaw 2011, about 1% a month). |
| `up_streak`, `run_up`, `atr_stretch` | Multi-day runs and how far above trend a stock is; the fade traders' setup ("first red day") needs 2-3 up days and a large extension first. |
| `ssr_today` | Rule 201 restricts shorting after a 10% fall, which matters for the paper-trading rule (docs/paper-trading.md) and marks a stock already breaking down. |
| `runners_breadth` | Fades fail in manias (January 2021 in the Digital Finance 2026 r/pennystocks study); the count of big movers in our own daily cross-section is a free gauge. |
| No RSI, MACD, Bollinger or candlestick flags | A 2026 test of these on US stocks 2000-2026 after costs and multiple-testing correction refuted them (arXiv 2607.20093); with about 50 labels at first, fewer features is better. |

### `model-v2` (2026-10-06, before any model was trained)

Prompted by the first `llm-v1` ratings, a reading of the eight research papers in the brief and a search for newer
work. The targets, label timing, the model and its parameters, the signal, the validation, the robustness checks, the
pruning rule and the hold-out did not change.

| Change | Why |
|---|---|
| `llm-v1` (four 0-3 scores of the whole chatter) replaced by `llm-v2` (a label for each document, an event quote, checks in code) | The first `llm-v1` ratings (15 candidates) made claims the documents don't support: coordination 2 or 3 for four large companies (Vistra, Applied Digital, SpaceX, Microsoft) whose chatter had no copied text (`dup_share` was 0 for all 15), and news 3 for PMI, whose documents were about the ISM purchasing managers' index, an economic report. A score for a whole conversation can't be checked; a list of documents and a copied quote can. This follows the usual advice for keeping a small model honest: extract rather than judge, ask for verbatim evidence and verify it (as Chain-of-Verification does, here in code rather than by the model), constrain the output to a schema and validate what comes back. PumpSense (2026) checks every ticker its LLM extracts against a list, and found LLMs too erratic to be the detector themselves, which is why LightGBM, not the LLM, makes the call here. |
| Coordination measured by the text features only; `near_dup_share` added (`text-v2`) | Promotion campaigns post the same message from many accounts: Renault (2017) found promoter rings and scheduled bot posting, Mirtaheri et al. (2021) found 84% of very active pump accounts were bots or suspended, and AIMM (2025) measures coordination as the share of post pairs above a similarity threshold. Exact copies were already in `dup_share`; reworded ones were not. |
| New `history` group | The same stocks get pumped again: in Xu & Livshits (2019) 35% of pumps targeted a coin already pumped on the same exchange, and both they and Nghiem et al. (2021) use the number of earlier pumps as a feature. |
| llama.cpp started with `--jinja`, thinking off | Newer Qwen models think out loud by default; only the model's own chat template, which `--jinja` turns on, applies `enable_thinking: false`. |

## Known gaps

- Labels are scarce: most candidates are large caps that neither pump nor crash, and `label-v1` is strict, so the
  pump model may not train before the hold-out. The crash model is the realistic first result, as the brief expects.
- Float and insider holdings are Stage 2's current-at-snapshot values, not point in time (minutes of lag).
- `runners_breadth` uses the newest cross-section file in the checkout whose session had closed by the flag. The
  Nasdaq file lags a session or two, so for some flags it counts an older session than the one just closed (stale,
  never ahead of the flag).
- When collection ends, the nightly run turns the pacer off, so the last `track`, `label` and `model` runs rely on
  their crons, which fire unreliably for this repository. If `model/holdout.md` hasn't appeared a few weeks after
  collection ended, start the workflows by hand (Actions, then Run workflow).
- The LLM is small (9 billion parameters, 4-bit) so that it runs on a free runner's CPU, at about 3 minutes per
  candidate; a larger hosted model would read the chatter better but needs an account or a key. `llm-v2` asks it only
  for checkable labels, so a weak reader shows up as missed or wrong labels rather than invented scores, and the
  model works without the ratings. In the test set the chosen model missed 14 of 33 pitches and 10 of 12 events
  (results at the end of this file), so `llm_pitch_share` and `llm_event_share` understate both.
- The hand-labelled test set is small (265 documents) and 13 of its 15 candidates are large caps, so it says little
  about penny-stock chatter. Before the next `llm` version, label the documents of some penny-stock candidates the
  same way (before seeing any answer) and test on those too.
- `history` counts flags since collection began (2026-10-04), so early candidates have little history.
- One model covers both pump types; results are reported per archetype, but there are too few labels for separate
  models.
- Stage 4's real-news rule ignores press releases (8-K items 7.01/8.01, 6-Ks). Classifying their text would change the
  labels, which needs a `label-v2` decision from shouvik; it is not done here.

## What had been seen before this was written

The flag-time inputs only: `candidates/episodes.csv` and `market/snapshots.csv` on the data branch (15 candidates and
45 snapshots on 2026-10-06, 13 of the candidates large caps), to choose the features. From project notes: Stage 4's
first label (SDEV, real news, crashed within 10 sessions). No `track/` outcome or `labels/` row was opened, and no
model had been trained.

After this file was committed, the code was run once on a copy of the live data branch as a functional test
(2026-10-06 02:16 UTC, no LLM): it rebuilt each candidate's flag documents (the counts matched Stage 1's
`mentions_24h` for all 15), found no label available for training, so trained nothing, and printed no outcome.
The clarifications added after that run (refusals and waiting for the LLM rating; a never-labeled hold-out snapshot
not blocking the evaluation forever) change no validation or hold-out rule.

`llm-v1` first named GitHub Models (`openai/gpt-4.1-mini`). The first probe run on 2026-10-06 got a plain "OK" instead
of an answer: GitHub retired GitHub Models on 2026-07-30. Before any rating was stored, `llm-v1` was changed to an
open-weights model run by llama.cpp on the runner, which needs no account or key: Qwen3-4B-Instruct-2507, 4-bit GGUF
`Qwen3-4B-Instruct-2507-Q4_K_M.gguf` from `unsloth/Qwen3-4B-Instruct-2507-GGUF` at revision `a06e946`. A probe on the
runner took 133 s for a full-size prompt (2,747 tokens read at 24 per second, 88 written at 4.5 per second), so the
summary was cut to at most 20 words; everything else stayed the same.

`model-v2` was written after the first live run had stored `llm-v1` ratings and `text-v1` features for the first 15
candidates. In addition to the above, what had been seen then: those ratings and features (`model/llm.csv`,
`model/text.csv`), and the documents shown to the LLM for the 15 candidates, which were read and labelled by hand for
the test set before any `llm-v2` answer existed. Still no `track/` outcome or `labels/` row had been opened, and no
model had been trained (no label was usable yet).

`model-v3` was written on 2026-10-07. In addition to the above, what had been seen then: the raw Stage 2 files of
the 111 snapshots taken so far (37 candidates), the Nasdaq cross-sections, and the `technical-v1` values the new code
computed from them, printed once as a functional test. Still no `track/` outcome or `labels/` row had been opened,
and no model had been trained (`model/README.md`: "no model yet" for both targets).

## LLM test results (2026-10-06)

`llm-eval` runs of 2026-10-06 on the test set's 15 candidates, of whose 265 labelled documents 256 were still shown
(tickers-v4 had dropped PMI's nine r/wallstreetbets ones), with llama.cpp `b10456` on a free GitHub runner (runs
37426096778, 37426100087 and 37426102760 for lists; 37429223329, 37429226799 and 37429230141 for one label per
document). R/W/M are the documents right, wrong and missed, as defined in "Testing the LLM step"; the score is right
minus wrong over `not_about`, `pitch` and `event`. All 90 answers parsed. The test reads only the flag documents,
the episodes and the snapshots; still no `track/` outcome or `labels/` row had been opened, and no model trained.

| Answer | Model | Seconds per candidate, mean (longest) | `not_about` R/W/M | `pitch` R/W/M | `warning` R/W/M | `event` R/W/M | Event quotes found / not found | Score |
|---|---|---|---|---|---|---|---|---|
| lists | Qwen3-4B-Instruct-2507 | 76 (152) | 0/54/1 | 28/98/5 | 1/25/0 | 4/0/8 | 2/0 | -120 |
| lists | Qwen3.5-4B | 98 (181) | 0/0/1 | 32/99/1 | 1/37/0 | 8/1/4 | 4/0 | -60 |
| lists | Qwen3.5-9B | 163 (294) | 0/0/1 | 31/54/2 | 1/37/0 | 9/2/3 | 8/0 | -16 |
| one label per document | Qwen3-4B-Instruct-2507 | 64 (130) | 0/4/1 | 24/27/9 | 1/17/0 | 1/1/11 | 1/1 | -7 |
| one label per document | Qwen3.5-4B | 84 (153) | 0/0/1 | 18/6/15 | 1/3/0 | 3/4/9 | 5/0 | 11 |
| one label per document | Qwen3.5-9B | 178 (326) | 0/0/1 | 19/2/14 | 1/1/0 | 2/1/10 | 3/0 | 18 |

The first answer format asked for the four lists of document numbers. With it every model put far more documents in
`pitch` than belong there (54 to 99 wrong, against 28 to 32 right), and Qwen3-4B-Instruct-2507 also called 54
documents not about the company. Before any `llm-v2` rating was stored, the answer was changed to one label per
document, with `other` listed first and described as the usual case (the format described above), and the three
models were run again. The rule was applied to those three runs.

**Chosen: Qwen3.5-9B**, the 4-bit GGUF `Qwen3.5-9B-Q4_K_M.gguf` from `unsloth/Qwen3.5-9B-GGUF` at revision `3885219`:
the best score (18; Qwen3.5-4B's 11 is more than 5 below it), at 178 seconds per candidate on average, within the
3-minute limit. To fit a day's candidates at that speed, a run now starts no new rating after 90 minutes instead of
35, and the `model` workflow's time limit went from 75 to 150 minutes.

What its labels are worth: in this set 19 of its 21 `pitch` labels and 2 of its 3 `event` labels were right, and all
3 of its event quotes were found in the documents; but it found only 19 of the 33 clear pitches and 2 of the 12 clear
events. `warning` can't be judged from one clear example. The test set also guided the change of format, so these
scores flatter the prompt: the next `llm` version is to be tested on documents labelled after this (Known gaps).

The first `model` run with it (run 37435090061, 2026-10-06 08:17 UTC) rated all 16 candidates flagged by then, with
no failure and no dropped label, in about 90 seconds each. Its answers differ a little from the test run's although
the model, prompt and settings are the same, presumably because that runner's CPU was different (it read prompts
four times faster), which changes the arithmetic slightly: scored against the hand labels (14 of the 15 test
candidates; PMI, down to one document, left out), `pitch` 14 right, 2 wrong, 19 missed and `event` 3 right, 0 wrong,
9 missed. Ratings are therefore reproducible only on the same kind of runner, which matters little because each one
is computed once and stored.
