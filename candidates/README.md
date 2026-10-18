# Stage 1 candidates

Updated 2026-10-18T16:49:43Z by run `39146506837`. A candidate is a ticker whose Reddit mentions (or hype-language
posts) in the last 24 hours jumped above its prior 7-day mean + 2 sd, with at least
10 mentions from 5 different authors. It stays listed until it goes
24 hours without a new flag. These are statistical flags, not accusations or advice.

| Ticker | Flagged since (UTC) | Why | Mentions 24h | Baseline/day | Authors | Hype posts | Subreddits | Exchange | StockTwits | Example |
|---|---|---|---|---|---|---|---|---|---|---|
| SCHD | 2026-10-17 04:49 | mention spike | 11 | 4.0 | 8 | 0 | wallstreetbets 11 | NYSE Arca |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1x8t7xg/comment/phily2s/) |
| VTI | 2026-10-18 05:58 | mention spike | 13 | 2.0 | 11 | 0 | wallstreetbets 13 | NYSE Arca |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1x8t7xg/comment/phiwo4r/) |
| NFLX | 2026-10-17 17:37 | mention spike | 8 | 8.29 | 8 | 0 | wallstreetbets 8 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1x8t7xg/comment/phia75f/) |
| VOO | 2026-10-16 19:07 | mention spike | 31 | 17.14 | 28 | 0 | wallstreetbets 31 | NYSE Arca | #10 | [link](https://www.reddit.com/r/wallstreetbets/comments/1x8s3ma/) |
| TQQQ | 2026-10-16 18:54 | mention spike | 4 | 5.0 | 4 | 0 | wallstreetbets 4 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1x8t7xg/comment/phg0wwv/) |
| QQQ | 2026-10-16 18:27 | mention spike | 41 | 84.0 | 36 | 0 | wallstreetbets 41 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1x7qdzy/comment/phixpuc/) |

Full history: `episodes.csv` (one row per first flag, with the numbers known at that moment).
