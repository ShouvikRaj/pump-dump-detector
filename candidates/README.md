# Stage 1 candidates

Updated 2026-11-25T15:28:09Z by run `45645035513`. A candidate is a ticker whose Reddit mentions (or hype-language
posts) in the last 24 hours jumped above its prior 7-day mean + 2 sd, with at least
10 mentions from 5 different authors. It stays listed until it goes
24 hours without a new flag. These are statistical flags, not accusations or advice.

| Ticker | Flagged since (UTC) | Why | Mentions 24h | Baseline/day | Authors | Hype posts | Subreddits | Exchange | StockTwits | Example |
|---|---|---|---|---|---|---|---|---|---|---|
| DELL | 2026-11-24 21:15 | mention spike | 41 | 3.71 | 36 | 0 | wallstreetbets 41 | NYSE | #1 | [link](https://www.reddit.com/r/wallstreetbets/comments/1y4ug32/) |
| BENF | 2026-11-25 00:43 | mention spike | 7 | 0.86 | 6 | 0 | pennystocks 7 | Nasdaq |  | [link](https://www.reddit.com/r/pennystocks/comments/1y4yruq/comment/19t5y651znmkg/) |
| HPE | 2026-11-24 00:45 | mention spike | 1 | 7.57 | 1 | 0 | wallstreetbets 1 | NYSE |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1y3u28s/comment/19t4uwxevhmmd/) |

Full history: `episodes.csv` (one row per first flag, with the numbers known at that moment).
