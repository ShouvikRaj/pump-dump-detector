# Stage 1 candidates

Updated 2026-11-25T20:46:09Z by run `45697395783`. A candidate is a ticker whose Reddit mentions (or hype-language
posts) in the last 24 hours jumped above its prior 7-day mean + 2 sd, with at least
10 mentions from 5 different authors. It stays listed until it goes
24 hours without a new flag. These are statistical flags, not accusations or advice.

| Ticker | Flagged since (UTC) | Why | Mentions 24h | Baseline/day | Authors | Hype posts | Subreddits | Exchange | StockTwits | Example |
|---|---|---|---|---|---|---|---|---|---|---|
| DELL | 2026-11-24 21:15 | mention spike | 47 | 4.0 | 39 | 0 | wallstreetbets 47 | NYSE | #14 | [link](https://www.reddit.com/r/wallstreetbets/comments/1y4ug32/) |
| BENF | 2026-11-25 00:43 | mention spike | 2 | 1.57 | 2 | 0 | pennystocks 2 | Nasdaq |  | [link](https://www.reddit.com/r/pennystocks/comments/1y4yruq/comment/19t5y651znmkg/) |
| HPE | 2026-11-24 00:45 | mention spike | 0 |  | 0 | 0 |  | NYSE |  |  |

Full history: `episodes.csv` (one row per first flag, with the numbers known at that moment).
