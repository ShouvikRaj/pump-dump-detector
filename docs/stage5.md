# Stage 5 design notes: model, retraining and validation

Stage 5 turns the labeled history into a model that scores every new candidate at its flag time, retrains it
every week as Stage 4's labels arrive, and evaluates it the way the project brief asks: walk-forward over a
development period, then once on a locked hold-out period at the end.

Everything in this file (version `model-v1`, with `text-v1` and `llm-v1`) was written down and committed on
2026-10-06, before any model was trained and before any Stage 3 outcome or Stage 4 label row was opened (see "What
had been seen" at the end). Change it only as a new version written here first (see "Changing the rule").

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

## Features (`model-v1`)

Only what was known at the flag time: Stage 1's episode row, Stage 2's snapshot row, and the text of the Reddit
documents counted in the episode. Seven groups; controls have no chatter, so their chatter counts are 0 and every
other chatter, text and LLM feature is blank (LightGBM treats blank as missing).

| Group | Features |
|---|---|
| `chatter` (Stage 1) | `mentions_log` ln(1 + mentions_24h), `baseline_log` ln(1 + baseline_mean), `spike_z` z, `authors_ratio` authors / mentions, `post_share` posts / mentions, `hype_share` hype documents / mentions, `hype_spike` (the flag's reasons include the hype spike), `wsb_share` and `pennystocks_share` (by_subreddit / mentions), `cashtag_share` (cashtag mentions / mentions), `stocktwits_trending` (on StockTwits' trending list at the flag) |
| `text` (`text-v1`, below) | `top_author_share`, `dup_share`, `promo_share`, `squeeze_share`, `news_share`, `dilution_share`, `link_share`, `multi_ticker_share`, `length_log` |
| `llm` (`llm-v1`, below) | `llm_promotion` (0-3), `llm_coordination` (0-3), `llm_news` (0-3), `llm_sentiment` (-2 to 2) |
| `price_volume` (Stage 2) | `price_log` ln(price_at_flag), `move_since_close`, `ret_1d`, `ret_5d`, `ret_20d`, `rel_vol_last_log` ln(1 + rel_vol_last), `rel_vol_today_log` ln(1 + rel_vol_today), `volatility_20d`, `pct_from_52w_high`, `dollar_vol_log` ln(1 + dollar_vol_20d) |
| `size` (Stage 2) | `market_cap_log` ln(1 + market_cap), `float_log` ln(1 + float_shares, else shares_outstanding), `turnover_last`, `listing_age_log` ln(1 + days since first_trade_date), `reverse_splits_1y`, `otc` (venue is OTC), `institution_pct` |
| `short_interest` (Stage 2) | `si_pct_float`, `si_days_to_cover`, `si_change` si_shares / si_prev_shares - 1 |
| `filings` (Stage 2) | `sec_filer` (has a CIK), `dilution_90d`, `offerings_424b_30d`, `days_since_dilution`, `current_reports_30d`, `days_since_report`, `report_hard_news` (the last 8-K before the flag has item 2.02, 2.01, 5.01, 1.03 or 1.01), `unregistered_sales_90d`, `late_notices_365d`, `name_change_1y` |

The archetype is not a feature (it is a function of price, float and venue, which are); it is used to report results
per pump type.

### Text features (`text-v1`)

The documents are exactly the ones behind the episode's `mentions_24h`: posts and comments in the three subreddits
that mention the ticker (Stage 1's extractor, `tickers-v3`), created in the 24 hours up to the flag and **collected
by** the flag time, bots excluded. Shares are over those documents.

| Feature | Definition |
|---|---|
| `top_author_share` | documents by the most active author |
| `dup_share` | documents whose normalised text (lower case, links, digits and the ticker removed, at least 20 letters, first 200 characters) also appears under a different author: copy-paste, coordinated phrasing |
| `promo_share` | documents using any of Stage 1's sales-pitch hype categories: urgency, price_target, low_float, gem, next_big, multibagger |
| `squeeze_share` | documents using the squeeze category |
| `news_share` | documents naming a company event: earnings, revenue, guidance, FDA, approval, clinical trial, contract, partnership, merger, acquisition, buyout, press release, "announced", 8-K |
| `dilution_share` | documents naming dilution: offering, dilution, warrants, reverse split, shelf, S-1, S-3, 424B |
| `link_share` | documents linking outside Reddit and image hosts (press releases, articles, promoter sites) |
| `multi_ticker_share` | documents that mention other tickers too (watch lists rather than one pitch) |
| `length_log` | ln(1 + mean characters per document) |

They are computed once per candidate, soon after the flag, and stored (`model/text.csv`).

### LLM ratings (`llm-v1`)

The brief gives the LLM two jobs: read the post text (hype, coordinated phrasing, bot-like accounts) and check
news and filings, to separate pumps from real news. Once per candidate, a language model reads:

- the same documents: posts first, then the most recent comments, each cut to 400 characters, at most 40 documents
  and 12,000 characters; authors replaced by A1, A2, ... so repeated posting stays visible;
- the company name, venue and price at the flag, and the SEC filings Stage 2 found before the flag (date and items of
  the last 8-K/6-K, date and form of the last registration or prospectus).

It answers in JSON: `promotion` (0-3, how much the chatter is a sales pitch), `coordination` (0-3, the same phrases
from different authors, near-identical posts, one author posting repeatedly), `news` (0-3, how much the discussion is
about a concrete, checkable company event rather than price action), `sentiment` (-2 bearish to 2 bullish),
`catalyst` (none, earnings, regulatory, deal, financing, other) and a one-sentence `summary`. The four numbers are
features; catalyst and summary go in the report only.

- Model: GitHub Models (`openai/gpt-4.1-mini`), called from the workflow with the repository's built-in
  `GITHUB_TOKEN` (`models: read` permission): no account, key or paid plan. Temperature 0. Its training data ends
  long before these flags, so it cannot know what happened next; it sees nothing written after the flag.
- Each rating is stored once in `model/llm.csv` with the model id, `llm-v1` and a hash of the prompt, and never
  recomputed. A failed call is retried on later runs for 3 days after the flag, then recorded as failed (features
  blank); a prompt the provider's content filter refuses is recorded as failed at once, and a candidate whose flag
  documents can't be found in the raw files is recorded as `no_documents`. A candidate is scored only once its rating exists or
  has been given up on, so its one score includes the rating whenever there is one. If the service is unavailable,
  the `llm` group is simply blank and the pruning rule below drops it.
- Changing the model or the prompt is a new `llm` version; old ratings keep theirs.

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

"Keep only robust patterns, prune weak ones" applies to the seven feature groups. Once a target's development replay
holds **20 positive candidates**, every run also replays the development weeks with each group left out. A group
is **weak** when leaving it out does not lower AP: AP without it >= AP with all groups, both pooled and in at least
two of the three blocks. The model that scores new candidates (the deployed model) uses every group except the
weak ones (if every group came out weak, none is dropped). Before 20 positives, all groups are used.

The replay also reports two reference models: market only (`price_volume`, `size`, `short_interest`, `filings`) and
social only (`chatter`, `text`, `llm`), which answer whether combining the two beats either alone.

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
| `model/text.csv` | append-only: text features of each candidate (`text-v1`), with the document count and when they were computed |
| `model/llm.csv` | append-only: LLM ratings of each candidate (`llm-v1`), with model id, prompt hash, status and time |
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

## Known gaps

- Labels are scarce: most candidates are large caps that neither pump nor crash, and `label-v1` is strict, so the
  pump model may not train before the hold-out. The crash model is the realistic first result, as the brief expects.
- Float and insider holdings are Stage 2's current-at-snapshot values, not point in time (minutes of lag).
- When collection ends, the nightly run turns the pacer off, so the last `track`, `label` and `model` runs rely on
  their crons, which fire unreliably for this repository. If `model/holdout.md` hasn't appeared a few weeks after
  collection ended, start the workflows by hand (Actions, then Run workflow).
- The LLM ratings depend on GitHub Models staying available and free at this volume (a few dozen calls a day, well
  under its free limit); the model works without them.
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
