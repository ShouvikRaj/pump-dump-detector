# Stage 1 candidates

Updated 2026-10-20T20:41:35Z by run `39494064199`. A candidate is a ticker whose Reddit mentions (or hype-language
posts) in the last 24 hours jumped above its prior 7-day mean + 2 sd, with at least
10 mentions from 5 different authors. It stays listed until it goes
24 hours without a new flag. These are statistical flags, not accusations or advice.

| Ticker | Flagged since (UTC) | Why | Mentions 24h | Baseline/day | Authors | Hype posts | Subreddits | Exchange | StockTwits | Example |
|---|---|---|---|---|---|---|---|---|---|---|
| GOOG | 2026-10-19 22:36 | mention spike | 35 | 17.43 | 24 | 0 | wallstreetbets 35 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xb2j2b/comment/phxw0mt/) |
| GOOGL | 2026-10-20 18:16 | mention spike | 51 | 18.71 | 21 | 0 | wallstreetbets 51 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xb2j2b/comment/phxsxdc/) |
| HTZ | 2026-10-20 13:24 | mention spike | 18 | 7.43 | 14 | 0 | wallstreetbets 17, pennystocks 1 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xaqvd4/) |
| LRCX | 2026-10-20 16:42 | mention spike | 12 | 1.71 | 5 | 0 | wallstreetbets 12 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xao1uu/comment/phxjn0k/) |
| NFLX | 2026-10-19 19:31 | mention spike | 132 | 11.29 | 99 | 0 | wallstreetbets 132 | Nasdaq | #2 | [link](https://www.reddit.com/r/wallstreetbets/comments/1xa8tas/) |
| SPCX | 2026-10-20 10:18 | mention spike | 197 | 39.43 | 133 | 1 | wallstreetbets 197 | Nasdaq | #1 | [link](https://www.reddit.com/r/wallstreetbets/comments/1xb2e55/) |
| AMZN | 2026-10-19 16:13 | mention spike | 53 | 26.0 | 27 | 0 | wallstreetbets 53 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xb2j2b/comment/phxvnq3/) |
| RIVN | 2026-10-19 18:51 | mention spike | 6 | 4.14 | 3 | 0 | wallstreetbets 6 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xao1uu/comment/phvvgmh/) |
| CRWV | 2026-10-20 14:57 | mention spike | 116 | 92.29 | 64 | 0 | wallstreetbets 116 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xau0nd/) |
| GLD | 2026-10-19 16:13 | mention spike | 6 | 6.57 | 5 | 0 | wallstreetbets 6 | NYSE Arca |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xao1uu/comment/phxdbir/) |
| IWM | 2026-10-20 16:03 | mention spike | 9 | 5.29 | 9 | 0 | wallstreetbets 9 | NYSE Arca | #29 | [link](https://www.reddit.com/r/wallstreetbets/comments/1xao1uu/comment/phxslms/) |
| APLD | 2026-10-20 04:07 | mention spike | 16 | 19.0 | 15 | 0 | wallstreetbets 16 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xamm2t/) |
| TCRT | 2026-10-19 14:18 | mention spike | 0 |  | 0 | 0 |  | Nasdaq |  |  |
| TQQQ | 2026-10-19 16:13 | mention spike | 4 | 9.0 | 3 | 1 | wallstreetbets 4 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1x7chad/comment/phxfqsb/) |

Full history: `episodes.csv` (one row per first flag, with the numbers known at that moment).
