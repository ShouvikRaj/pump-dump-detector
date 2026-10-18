# Stage 1 candidates

Updated 2026-10-18T16:07:15Z by run `39143495610`. A candidate is a ticker whose Reddit mentions (or hype-language
posts) in the last 24 hours jumped above its prior 7-day mean + 2 sd, with at least
10 mentions from 5 different authors. It stays listed until it goes
24 hours without a new flag. These are statistical flags, not accusations or advice.

| Ticker | Flagged since (UTC) | Why | Mentions 24h | Baseline/day | Authors | Hype posts | Subreddits | Exchange | StockTwits | Example |
|---|---|---|---|---|---|---|---|---|---|---|
| VTI | 2026-10-18 05:58 | mention spike | 12 | 2.0 | 10 | 0 | wallstreetbets 12 | NYSE Arca |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1x8t7xg/comment/phin1lt/) |
| SCHD | 2026-10-17 04:49 | mention spike | 11 | 4.0 | 8 | 0 | wallstreetbets 11 | NYSE Arca |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1x8t7xg/comment/phily2s/) |
| NFLX | 2026-10-17 17:37 | mention spike | 11 | 7.86 | 9 | 0 | wallstreetbets 11 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1x8t7xg/comment/phia75f/) |
| VOO | 2026-10-16 19:07 | mention spike | 30 | 17.29 | 27 | 0 | wallstreetbets 30 | NYSE Arca |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1x8s3ma/) |
| TQQQ | 2026-10-16 18:54 | mention spike | 4 | 5.0 | 4 | 0 | wallstreetbets 4 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1x8t7xg/comment/phg0wwv/) |
| QQQ | 2026-10-16 18:27 | mention spike | 37 | 83.86 | 32 | 0 | wallstreetbets 37 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1x7qdzy/comment/phihsoi/) |
| OPEX | 2026-10-16 19:07 | mention spike | 0 |  | 0 | 0 |  | Cboe BZX |  |  |
| USO | 2026-10-16 11:23 | mention spike | 1 | 9.0 | 1 | 0 | wallstreetbets 1 | NYSE Arca |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1x8nbc1/comment/phe5ejf/) |

Full history: `episodes.csv` (one row per first flag, with the numbers known at that moment).
