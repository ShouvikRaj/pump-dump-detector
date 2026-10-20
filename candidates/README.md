# Stage 1 candidates

Updated 2026-10-20T17:09:42Z by run `39463523253`. A candidate is a ticker whose Reddit mentions (or hype-language
posts) in the last 24 hours jumped above its prior 7-day mean + 2 sd, with at least
10 mentions from 5 different authors. It stays listed until it goes
24 hours without a new flag. These are statistical flags, not accusations or advice.

| Ticker | Flagged since (UTC) | Why | Mentions 24h | Baseline/day | Authors | Hype posts | Subreddits | Exchange | StockTwits | Example |
|---|---|---|---|---|---|---|---|---|---|---|
| AMZN | 2026-10-19 16:13 | mention spike | 64 | 24.57 | 33 | 0 | wallstreetbets 64 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xa66i7/) |
| HTZ | 2026-10-20 13:24 | mention spike | 23 | 6.86 | 14 | 1 | wallstreetbets 23 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xaqvd4/) |
| LRCX | 2026-10-20 16:42 | mention spike | 11 | 1.86 | 5 | 0 | wallstreetbets 11 | Nasdaq | #20 | [link](https://www.reddit.com/r/wallstreetbets/comments/1xao1uu/comment/phx0wj9/) |
| NFLX | 2026-10-19 19:31 | mention spike | 46 | 9.71 | 36 | 0 | wallstreetbets 46 | Nasdaq | #1 | [link](https://www.reddit.com/r/wallstreetbets/comments/1xa8tas/) |
| RIVN | 2026-10-19 18:51 | mention spike | 18 | 3.0 | 10 | 0 | wallstreetbets 18 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xao1uu/comment/phvvgmh/) |
| SPCX | 2026-10-20 10:18 | mention spike | 105 | 38.0 | 73 | 0 | wallstreetbets 105 | Nasdaq | #17 | [link](https://www.reddit.com/r/wallstreetbets/comments/1xad35t/) |
| CRWV | 2026-10-20 14:57 | mention spike | 181 | 81.29 | 85 | 0 | wallstreetbets 181 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xau0nd/) |
| GLD | 2026-10-19 16:13 | mention spike | 11 | 5.86 | 8 | 0 | wallstreetbets 11 | NYSE Arca |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xao1uu/comment/phx5xqg/) |
| IWM | 2026-10-20 16:03 | mention spike | 11 | 4.86 | 10 | 0 | wallstreetbets 11 | NYSE Arca |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xao1uu/comment/phwslve/) |
| APLD | 2026-10-20 04:07 | mention spike | 21 | 19.0 | 17 | 0 | wallstreetbets 21 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xamm2t/) |
| TCRT | 2026-10-19 14:18 | mention spike | 0 |  | 0 | 0 |  | Nasdaq |  |  |
| GOOG | 2026-10-19 22:36 | mention spike | 25 | 17.71 | 17 | 0 | wallstreetbets 25 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xao1uu/comment/phx4fla/) |
| TQQQ | 2026-10-19 16:13 | mention spike | 5 | 8.86 | 5 | 1 | wallstreetbets 5 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xao1uu/comment/phv9dt7/) |

Full history: `episodes.csv` (one row per first flag, with the numbers known at that moment).
