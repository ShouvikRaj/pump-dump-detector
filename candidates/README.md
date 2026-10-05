# Stage 1 candidates

Updated 2026-10-05T13:41:21Z by run `37318668503`. A candidate is a ticker whose Reddit mentions (or hype-language
posts) in the last 24 hours jumped above its prior 7-day mean + 2 sd, with at least
10 mentions from 5 different authors. It stays listed until it goes
24 hours without a new flag. These are statistical flags, not accusations or advice.

Warm-up until 2026-10-12T22:41:09Z: part of the baseline was backfilled from the archive rather than
collected live, so flags in this period are marked `warmup=1` in episodes.csv.

| Ticker | Flagged since (UTC) | Why | Mentions 24h | Baseline/day | Authors | Hype posts | Subreddits | Exchange | StockTwits | Example |
|---|---|---|---|---|---|---|---|---|---|---|
| DRTS | 2026-10-04 23:23 | mention spike | 23 | 1.0 | 20 | 1 | wallstreetbets 23 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1wxl6cr/) |
| VST | 2026-10-05 04:15 | mention spike | 45 | 6.0 | 22 | 0 | wallstreetbets 45 | NYSE | #7 | [link](https://www.reddit.com/r/wallstreetbets/comments/1wy4mk1/comment/pe0fzyd/) |

Full history: `episodes.csv` (one row per first flag, with the numbers known at that moment).
