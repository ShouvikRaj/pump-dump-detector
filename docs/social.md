# Social chatter beyond Reddit: StockTwits, Bluesky and X

shouvik asked (2026-10-06) to expand the dataset from Reddit to Reddit + Twitter/X, using a free, account-free
source like Arctic Shift if one exists. This is what was found and what was built (`social-v1`).

## Is there a free X source? (checked 2026-10-07)

No. Every route was tried from a GitHub runner (probe run 37618643063):

| Route | Result |
|---|---|
| X API v2 without a key | 401. The free tier ended 2026-02-06; reads are pay-per-use, about $0.005 per post returned, recent search covers the last 7 days only |
| Nitter instances, XCancel (search pages and RSS) | gone: X's legal action shut them down in September 2026 (XCancel answers 451 "service is suspended", nitter.net refuses connections, Nitter's repo is archived) |
| x.com search pages | Cloudflare bot wall (403) |
| X embed/syndication endpoints | single tweets by id only (no search); the profile timeline answers 429 |
| twscrape, Twikit, Scweet, snscrape | need logged-in X accounts (snscrape is dead); scraping with bot accounts breaks X's terms, gets accounts banned, and GitHub's IP ranges are blocked, so it is not used |
| Paid resellers (TwitterAPI.io, SocialData, Apify) | need an account and a card, and resell scraped data; not used |

What does work for free, without an account, from GitHub's runners:

| Source | Why it is the closest substitute |
|---|---|
| **StockTwits symbol streams** (`api.stocktwits.com/api/2/streams/symbol/<T>.json`) | Twitter-style posts, built around cashtags, heavy on small caps and OTC names (the 2017-era pump literature's "Twitter" data is largely the same crowd). 30 messages a page, paged back in time. Each message carries the author's follower count, join date and post count, and an optional bullish/bearish tag: exactly the promoter and new-account signals Renault (2017) and Mirtaheri (2021) got from Twitter. |
| **Bluesky post search** (`api.bsky.app/xrpc/app.bsky.feed.searchPosts`) | Open network, no key (the `public.api.bsky.app` host refuses search; `api.bsky.app` answers). About 5,800 posts a day carry a cashtag, mostly news and filing bots, so it is thin but free. |

Mastodon tag timelines also answer but carry almost no stock talk, so they are left out.

## What was built

The `social` workflow starts after every `collect` run, like `market` (plus a cron backup every 6 hours). For each
Stage 1 candidate, and each Stage 2 control once its market snapshot exists, it fetches StockTwits and Bluesky
posts from 72 hours before the flag up to the fetch, stores them raw, and writes a `flag` row to
`social/snapshots.csv`. Candidates then get a follow-up row (`d1` ... `d10`) about every 24 hours for 10 days with
the posts since the previous row, which covers the pump and the dump (useful later for exits in paper trading).

Features per source (`st_`, `bsky_`, `x_`), over the 24 hours before the flag for `flag` rows:
`n`, `authors`, `top_author_share`, `new_acct_share` (account under 90 days old when posting), `median_followers`,
`bull_share` (bullish / tagged), `dup_share` (posts whose text, minus links and numbers, appears more than once),
plus `n_72h`, `n_after_flag`, `fetched` and `truncated` (page limit hit: counts are lower bounds).

Limits: 10 StockTwits pages (300 messages) per row, 3 Bluesky pages, 80 StockTwits requests per run, 8 minutes.
A StockTwits failure is retried at the next run. Bluesky turns away about one unauthenticated search in three
with a 403 ("forbidden by administrative rules"), so each request is tried up to 4 times; a source that still fails
leaves its columns blank (unknown, not zero) and the reason in `errors`. (The first run, on 2026-10-07 12:14 UTC,
kept partial Bluesky counts in 7 rows whose `errors` show the 403.) Episodes flagged before 2026-10-07 got their `flag` rows late
(`lag_s` says how late); posts deleted in between are missing.

**X, if shouvik pays for it:** add a repository secret `X_BEARER_TOKEN` (X developer console, pay-per-use credits)
and the same run also searches X for each ticker's cashtag (original posts only) into the `x_` columns. It reads at
most `X_DAILY_POSTS` posts a day (repository variable, default 200, about $1 a day at $0.005 a post). Without the
secret X is skipped and nothing is billed.

It stops by itself: once collection has finished and no follow-up is left, the workflow turns itself off.

## Does this change the plan or the strategies?

Not much. Re-checked against the original plan (pump-dump-detector-context.txt) and research/papers.md:

- **Flagging stays Reddit-only** (spikes-v1). So label-v1, model-v2 and the 2027-01-04 hold-out stay valid.
  Renault's 7-day mean + 2 sd rule (20 tweets from 20 users) is already what spikes-v1 uses on Reddit. A StockTwits
  spike as a second trigger is possible later, but it would change which stocks become candidates, so it waits for
  shouvik's call and for evidence (do StockTwits spikes lead Reddit ones?).
- **The original plan already listed StockTwits** as the second social source; until now only its trending list
  was kept. The per-message data adds what the papers found most useful from Twitter: promoter and bot-likeness
  signals (one account dominating, new accounts, copy-paste posts, follower counts; Renault, Mirtaheri) and
  sentiment (Renault). Market features stay the main signal (Mirtaheri, Nghiem, Xu & Livshits).
- **The model**: the `flag`-row features are flag-time safe, so a later model version can add them as a feature
  group, dropped if it doesn't help (the same test Stage 5 already applies). That is a Stage 5 decision for after
  enough rows exist; model-v2 is unchanged.
- **Labels, validation, controls, slippage, paper trading**: unchanged.
