# Stage 1 candidates

Updated 2026-10-20T19:30:07Z by run `39482764240`. A candidate is a ticker whose Reddit mentions (or hype-language
posts) in the last 24 hours jumped above its prior 7-day mean + 2 sd, with at least
10 mentions from 5 different authors. It stays listed until it goes
24 hours without a new flag. These are statistical flags, not accusations or advice.

| Ticker | Flagged since (UTC) | Why | Mentions 24h | Baseline/day | Authors | Hype posts | Subreddits | Exchange | StockTwits | Example |
|---|---|---|---|---|---|---|---|---|---|---|
| AMZN | 2026-10-19 16:13 | mention spike | 56 | 25.71 | 29 | 0 | wallstreetbets 56 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xao1uu/comment/phxirfz/) |
| GOOG | 2026-10-19 22:36 | mention spike | 31 | 17.14 | 21 | 0 | wallstreetbets 31 | Nasdaq | #16 | [link](https://www.reddit.com/r/wallstreetbets/comments/1xao1uu/comment/phxmb8h/) |
| GOOGL | 2026-10-20 18:16 | mention spike | 44 | 19.0 | 20 | 0 | wallstreetbets 44 | Nasdaq | #9 | [link](https://www.reddit.com/r/wallstreetbets/comments/1xao1uu/comment/phxnqrm/) |
| HTZ | 2026-10-20 13:24 | mention spike | 20 | 7.14 | 15 | 1 | wallstreetbets 19, pennystocks 1 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xaqvd4/) |
| LRCX | 2026-10-20 16:42 | mention spike | 12 | 1.71 | 5 | 0 | wallstreetbets 12 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xao1uu/comment/phxjn0k/) |
| NFLX | 2026-10-19 19:31 | mention spike | 66 | 10.29 | 51 | 0 | wallstreetbets 66 | Nasdaq | #2 | [link](https://www.reddit.com/r/wallstreetbets/comments/1xa8tas/) |
| SPCX | 2026-10-20 10:18 | mention spike | 122 | 39.14 | 86 | 0 | wallstreetbets 122 | Nasdaq | #5 | [link](https://www.reddit.com/r/wallstreetbets/comments/1xad35t/) |
| RIVN | 2026-10-19 18:51 | mention spike | 11 | 3.57 | 5 | 0 | wallstreetbets 11 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xao1uu/comment/phvvgmh/) |
| CRWV | 2026-10-20 14:57 | mention spike | 124 | 90.43 | 67 | 0 | wallstreetbets 124 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xau0nd/) |
| GLD | 2026-10-19 16:13 | mention spike | 8 | 6.29 | 6 | 0 | wallstreetbets 8 | NYSE Arca |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xao1uu/comment/phxdbir/) |
| IWM | 2026-10-20 16:03 | mention spike | 10 | 5.0 | 10 | 0 | wallstreetbets 10 | NYSE Arca |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xao1uu/comment/phwslve/) |
| APLD | 2026-10-20 04:07 | mention spike | 17 | 19.43 | 15 | 0 | wallstreetbets 17 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xamm2t/) |
| TCRT | 2026-10-19 14:18 | mention spike | 0 |  | 0 | 0 |  | Nasdaq |  |  |
| TQQQ | 2026-10-19 16:13 | mention spike | 5 | 8.86 | 4 | 1 | wallstreetbets 5 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1x7chad/comment/phxfqsb/) |

Full history: `episodes.csv` (one row per first flag, with the numbers known at that moment).
