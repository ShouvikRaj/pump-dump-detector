# Stage 1 candidates

Updated 2026-10-20T12:57:49Z by run `39426267743`. A candidate is a ticker whose Reddit mentions (or hype-language
posts) in the last 24 hours jumped above its prior 7-day mean + 2 sd, with at least
10 mentions from 5 different authors. It stays listed until it goes
24 hours without a new flag. These are statistical flags, not accusations or advice.

| Ticker | Flagged since (UTC) | Why | Mentions 24h | Baseline/day | Authors | Hype posts | Subreddits | Exchange | StockTwits | Example |
|---|---|---|---|---|---|---|---|---|---|---|
| AMZN | 2026-10-19 16:13 | mention spike | 78 | 20.29 | 44 | 0 | wallstreetbets 78 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xa66i7/) |
| GLD | 2026-10-19 16:13 | mention spike | 16 | 4.86 | 10 | 0 | wallstreetbets 16 | NYSE Arca |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xa7cu6/comment/phszhop/) |
| NFLX | 2026-10-19 19:31 | mention spike | 30 | 9.57 | 25 | 0 | wallstreetbets 30 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xa8tas/) |
| RIVN | 2026-10-19 18:51 | mention spike | 23 | 2.43 | 13 | 0 | wallstreetbets 23 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xa7cu6/comment/phseny4/) |
| SPCX | 2026-10-20 10:18 | mention spike | 92 | 37.0 | 63 | 0 | wallstreetbets 92 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xad35t/) |
| APLD | 2026-10-20 04:07 | mention spike | 25 | 18.29 | 17 | 0 | wallstreetbets 24, smallstreetbets 1 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xamm2t/) |
| TCRT | 2026-10-19 14:18 | mention spike | 7 | 5.0 | 4 | 0 | pennystocks 7 | Nasdaq |  | [link](https://www.reddit.com/r/pennystocks/comments/1x9mwl7/comment/phpkaok/) |
| GOOG | 2026-10-19 22:36 | mention spike | 22 | 18.0 | 14 | 0 | wallstreetbets 22 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xao1uu/comment/phvh9m1/) |
| TQQQ | 2026-10-19 16:13 | mention spike | 8 | 8.57 | 8 | 1 | wallstreetbets 8 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xao1uu/comment/phv9dt7/) |

Full history: `episodes.csv` (one row per first flag, with the numbers known at that moment).
