# Stage 1 candidates

Updated 2026-10-20T11:24:45Z by run `39414682141`. A candidate is a ticker whose Reddit mentions (or hype-language
posts) in the last 24 hours jumped above its prior 7-day mean + 2 sd, with at least
10 mentions from 5 different authors. It stays listed until it goes
24 hours without a new flag. These are statistical flags, not accusations or advice.

| Ticker | Flagged since (UTC) | Why | Mentions 24h | Baseline/day | Authors | Hype posts | Subreddits | Exchange | StockTwits | Example |
|---|---|---|---|---|---|---|---|---|---|---|
| AMZN | 2026-10-19 16:13 | mention spike | 70 | 20.43 | 42 | 0 | wallstreetbets 70 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xa66i7/) |
| APLD | 2026-10-20 04:07 | mention spike | 35 | 17.0 | 24 | 0 | wallstreetbets 34, smallstreetbets 1 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xamm2t/) |
| GLD | 2026-10-19 16:13 | mention spike | 17 | 4.71 | 11 | 0 | wallstreetbets 17 | NYSE Arca |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xa7cu6/comment/phszhop/) |
| NFLX | 2026-10-19 19:31 | mention spike | 27 | 9.86 | 23 | 0 | wallstreetbets 27 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xa8tas/) |
| RIVN | 2026-10-19 18:51 | mention spike | 23 | 2.57 | 13 | 0 | wallstreetbets 23 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xa7cu6/comment/phseny4/) |
| SPCX | 2026-10-20 10:18 | mention spike | 86 | 37.0 | 59 | 0 | wallstreetbets 86 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xad35t/) |
| TCRT | 2026-10-19 14:18 | mention spike | 13 | 4.14 | 6 | 0 | pennystocks 13 | Nasdaq |  | [link](https://www.reddit.com/r/pennystocks/comments/1x9mwl7/comment/phpkaok/) |
| GOOG | 2026-10-19 22:36 | mention spike | 21 | 18.14 | 13 | 0 | wallstreetbets 21 | Nasdaq | #20 | [link](https://www.reddit.com/r/wallstreetbets/comments/1xa7cu6/comment/phtaake/) |
| TQQQ | 2026-10-19 16:13 | mention spike | 8 | 8.57 | 8 | 1 | wallstreetbets 8 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xao1uu/comment/phv9dt7/) |

Full history: `episodes.csv` (one row per first flag, with the numbers known at that moment).
