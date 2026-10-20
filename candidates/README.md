# Stage 1 candidates

Updated 2026-10-20T13:50:50Z by run `39433794190`. A candidate is a ticker whose Reddit mentions (or hype-language
posts) in the last 24 hours jumped above its prior 7-day mean + 2 sd, with at least
10 mentions from 5 different authors. It stays listed until it goes
24 hours without a new flag. These are statistical flags, not accusations or advice.

| Ticker | Flagged since (UTC) | Why | Mentions 24h | Baseline/day | Authors | Hype posts | Subreddits | Exchange | StockTwits | Example |
|---|---|---|---|---|---|---|---|---|---|---|
| AMZN | 2026-10-19 16:13 | mention spike | 80 | 20.29 | 46 | 0 | wallstreetbets 80 | Nasdaq | #9 | [link](https://www.reddit.com/r/wallstreetbets/comments/1xa66i7/) |
| GLD | 2026-10-19 16:13 | mention spike | 17 | 4.71 | 11 | 0 | wallstreetbets 17 | NYSE Arca |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xao1uu/comment/phw0dmk/) |
| HTZ | 2026-10-20 13:24 | mention spike | 21 | 6.71 | 13 | 1 | wallstreetbets 21 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xaqvd4/) |
| NFLX | 2026-10-19 19:31 | mention spike | 31 | 9.43 | 26 | 0 | wallstreetbets 31 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xa8tas/) |
| RIVN | 2026-10-19 18:51 | mention spike | 24 | 2.43 | 13 | 0 | wallstreetbets 24 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xao1uu/comment/phvvgmh/) |
| SPCX | 2026-10-20 10:18 | mention spike | 96 | 36.71 | 64 | 0 | wallstreetbets 96 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xad35t/) |
| APLD | 2026-10-20 04:07 | mention spike | 21 | 18.57 | 15 | 0 | wallstreetbets 21 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xamm2t/) |
| TCRT | 2026-10-19 14:18 | mention spike | 3 | 5.57 | 2 | 0 | pennystocks 3 | Nasdaq |  | [link](https://www.reddit.com/r/pennystocks/comments/1x9mwl7/comment/phpkaok/) |
| GOOG | 2026-10-19 22:36 | mention spike | 23 | 17.57 | 15 | 0 | wallstreetbets 23 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xao1uu/comment/phvvjuz/) |
| TQQQ | 2026-10-19 16:13 | mention spike | 8 | 8.57 | 8 | 1 | wallstreetbets 8 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xao1uu/comment/phv9dt7/) |

Full history: `episodes.csv` (one row per first flag, with the numbers known at that moment).
