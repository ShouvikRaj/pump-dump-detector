# Stage 1 candidates

Updated 2026-10-18T19:15:33Z by run `39157619034`. A candidate is a ticker whose Reddit mentions (or hype-language
posts) in the last 24 hours jumped above its prior 7-day mean + 2 sd, with at least
10 mentions from 5 different authors. It stays listed until it goes
24 hours without a new flag. These are statistical flags, not accusations or advice.

| Ticker | Flagged since (UTC) | Why | Mentions 24h | Baseline/day | Authors | Hype posts | Subreddits | Exchange | StockTwits | Example |
|---|---|---|---|---|---|---|---|---|---|---|
| VTI | 2026-10-18 05:58 | mention spike | 13 | 2.29 | 11 | 0 | wallstreetbets 13 | NYSE Arca | #22 | [link](https://www.reddit.com/r/wallstreetbets/comments/1x8t7xg/comment/phjkg1n/) |
| SCHD | 2026-10-17 04:49 | mention spike | 11 | 4.57 | 8 | 0 | wallstreetbets 11 | NYSE Arca |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1x8t7xg/comment/phily2s/) |
| NFLX | 2026-10-17 17:37 | mention spike | 5 | 9.0 | 5 | 0 | wallstreetbets 5 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1x8t7xg/comment/phia75f/) |
| VOO | 2026-10-16 19:07 | mention spike | 30 | 18.71 | 27 | 0 | wallstreetbets 30 | NYSE Arca |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1x8s3ma/) |

Full history: `episodes.csv` (one row per first flag, with the numbers known at that moment).
