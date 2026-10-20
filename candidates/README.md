# Stage 1 candidates

Updated 2026-10-20T17:49:51Z by run `39469334477`. A candidate is a ticker whose Reddit mentions (or hype-language
posts) in the last 24 hours jumped above its prior 7-day mean + 2 sd, with at least
10 mentions from 5 different authors. It stays listed until it goes
24 hours without a new flag. These are statistical flags, not accusations or advice.

| Ticker | Flagged since (UTC) | Why | Mentions 24h | Baseline/day | Authors | Hype posts | Subreddits | Exchange | StockTwits | Example |
|---|---|---|---|---|---|---|---|---|---|---|
| AMZN | 2026-10-19 16:13 | mention spike | 63 | 24.86 | 32 | 0 | wallstreetbets 63 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xa66i7/) |
| LRCX | 2026-10-20 16:42 | mention spike | 11 | 1.71 | 5 | 0 | wallstreetbets 11 | Nasdaq | #21 | [link](https://www.reddit.com/r/wallstreetbets/comments/1xao1uu/comment/phx0wj9/) |
| NFLX | 2026-10-19 19:31 | mention spike | 49 | 9.86 | 38 | 0 | wallstreetbets 49 | Nasdaq | #1 | [link](https://www.reddit.com/r/wallstreetbets/comments/1xa8tas/) |
| RIVN | 2026-10-19 18:51 | mention spike | 16 | 3.29 | 8 | 0 | wallstreetbets 16 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xao1uu/comment/phvvgmh/) |
| SPCX | 2026-10-20 10:18 | mention spike | 106 | 38.0 | 73 | 0 | wallstreetbets 106 | Nasdaq | #14 | [link](https://www.reddit.com/r/wallstreetbets/comments/1xad35t/) |
| HTZ | 2026-10-20 13:24 | mention spike | 20 | 7.0 | 14 | 1 | wallstreetbets 20 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xaqvd4/) |
| CRWV | 2026-10-20 14:57 | mention spike | 169 | 83.29 | 83 | 0 | wallstreetbets 169 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xau0nd/) |
| GLD | 2026-10-19 16:13 | mention spike | 10 | 6.0 | 7 | 0 | wallstreetbets 10 | NYSE Arca |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xao1uu/comment/phx5xqg/) |
| IWM | 2026-10-20 16:03 | mention spike | 10 | 5.0 | 10 | 0 | wallstreetbets 10 | NYSE Arca |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xao1uu/comment/phwslve/) |
| APLD | 2026-10-20 04:07 | mention spike | 19 | 19.29 | 16 | 0 | wallstreetbets 19 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xamm2t/) |
| TCRT | 2026-10-19 14:18 | mention spike | 0 |  | 0 | 0 |  | Nasdaq |  |  |
| GOOG | 2026-10-19 22:36 | mention spike | 25 | 17.14 | 17 | 0 | wallstreetbets 25 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xao1uu/comment/phx4fla/) |
| TQQQ | 2026-10-19 16:13 | mention spike | 5 | 8.86 | 5 | 1 | wallstreetbets 5 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xao1uu/comment/phv9dt7/) |

Full history: `episodes.csv` (one row per first flag, with the numbers known at that moment).
