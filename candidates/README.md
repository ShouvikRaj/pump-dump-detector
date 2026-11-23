# Stage 1 candidates

Updated 2026-11-23T04:45:05Z by run `45113223908`. A candidate is a ticker whose Reddit mentions (or hype-language
posts) in the last 24 hours jumped above its prior 7-day mean + 2 sd, with at least
10 mentions from 5 different authors. It stays listed until it goes
24 hours without a new flag. These are statistical flags, not accusations or advice.

| Ticker | Flagged since (UTC) | Why | Mentions 24h | Baseline/day | Authors | Hype posts | Subreddits | Exchange | StockTwits | Example |
|---|---|---|---|---|---|---|---|---|---|---|
| SMCI | 2026-11-23 00:51 | mention spike | 10 | 7.29 | 10 | 0 | wallstreetbets 10 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1y1eq6h/comment/19t16yy4g06dh/) |
| NYT | 2026-11-22 00:48 | mention spike | 6 | 10.0 | 5 | 0 | wallstreetbets 6 | NYSE |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1y2ztge/comment/19t1qceuh63z6/) |

Full history: `episodes.csv` (one row per first flag, with the numbers known at that moment).
