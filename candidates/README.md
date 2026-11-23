# Stage 1 candidates

Updated 2026-11-23T02:07:36Z by run `45097764241`. A candidate is a ticker whose Reddit mentions (or hype-language
posts) in the last 24 hours jumped above its prior 7-day mean + 2 sd, with at least
10 mentions from 5 different authors. It stays listed until it goes
24 hours without a new flag. These are statistical flags, not accusations or advice.

| Ticker | Flagged since (UTC) | Why | Mentions 24h | Baseline/day | Authors | Hype posts | Subreddits | Exchange | StockTwits | Example |
|---|---|---|---|---|---|---|---|---|---|---|
| SMCI | 2026-11-23 00:51 | mention spike | 11 | 7.14 | 11 | 0 | wallstreetbets 11 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1y1eq6h/comment/19t16yy4g06dh/) |
| NYT | 2026-11-22 00:48 | mention spike | 4 | 10.57 | 4 | 0 | wallstreetbets 4 | NYSE |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1y1eq6h/comment/19t1coxdvwzt0/) |
| MSTR | 2026-11-22 00:48 | mention spike | 11 | 21.71 | 11 | 0 | wallstreetbets 11 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1y2gl1m/) |

Full history: `episodes.csv` (one row per first flag, with the numbers known at that moment).
