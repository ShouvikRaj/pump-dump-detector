# Stage 1 candidates

Updated 2026-10-20T21:21:24Z by run `39499599787`. A candidate is a ticker whose Reddit mentions (or hype-language
posts) in the last 24 hours jumped above its prior 7-day mean + 2 sd, with at least
10 mentions from 5 different authors. It stays listed until it goes
24 hours without a new flag. These are statistical flags, not accusations or advice.

| Ticker | Flagged since (UTC) | Why | Mentions 24h | Baseline/day | Authors | Hype posts | Subreddits | Exchange | StockTwits | Example |
|---|---|---|---|---|---|---|---|---|---|---|
| GOOG | 2026-10-19 22:36 | mention spike | 34 | 17.71 | 26 | 0 | wallstreetbets 34 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xb4ajv/) |
| GOOGL | 2026-10-20 18:16 | mention spike | 50 | 18.86 | 21 | 0 | wallstreetbets 50 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xb2j2b/comment/phy02u4/) |
| HTZ | 2026-10-20 13:24 | mention spike | 18 | 7.43 | 14 | 0 | wallstreetbets 17, pennystocks 1 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xaqvd4/) |
| LRCX | 2026-10-20 16:42 | mention spike | 12 | 1.71 | 5 | 0 | wallstreetbets 12 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xao1uu/comment/phxjn0k/) |
| NFLX | 2026-10-19 19:31 | mention spike | 146 | 11.57 | 109 | 0 | wallstreetbets 146 | Nasdaq | #2 | [link](https://www.reddit.com/r/wallstreetbets/comments/1xb427h/) |
| SMCI | 2026-10-20 21:06 | mention spike | 33 | 5.57 | 28 | 0 | wallstreetbets 33 | Nasdaq | #3 | [link](https://www.reddit.com/r/wallstreetbets/comments/1xb2j2b/comment/phy1ch3/) |
| SPCX | 2026-10-20 10:18 | mention spike | 234 | 40.29 | 152 | 1 | wallstreetbets 234 | Nasdaq | #1 | [link](https://www.reddit.com/r/wallstreetbets/comments/1xb427h/) |
| OKLO | 2026-10-20 21:21 | mention spike | 13 | 5.86 | 12 | 0 | wallstreetbets 13 | NYSE |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xatiax/) |
| AMZN | 2026-10-19 16:13 | mention spike | 53 | 26.0 | 28 | 0 | wallstreetbets 53 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xb2h1z/comment/phxyvzj/) |
| RIVN | 2026-10-19 18:51 | mention spike | 3 | 4.57 | 2 | 0 | wallstreetbets 3 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xao1uu/comment/phvvgmh/) |
| CRWV | 2026-10-20 14:57 | mention spike | 117 | 93.0 | 66 | 0 | wallstreetbets 117 | Nasdaq | #19 | [link](https://www.reddit.com/r/wallstreetbets/comments/1xau0nd/) |
| GLD | 2026-10-19 16:13 | mention spike | 6 | 6.43 | 5 | 0 | wallstreetbets 6 | NYSE Arca |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xao1uu/comment/phxdbir/) |
| IWM | 2026-10-20 16:03 | mention spike | 9 | 5.29 | 9 | 0 | wallstreetbets 9 | NYSE Arca | #10 | [link](https://www.reddit.com/r/wallstreetbets/comments/1xao1uu/comment/phxslms/) |
| APLD | 2026-10-20 04:07 | mention spike | 15 | 19.29 | 13 | 0 | wallstreetbets 15 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xamm2t/) |
| TCRT | 2026-10-19 14:18 | mention spike | 0 |  | 0 | 0 |  | Nasdaq |  |  |
| TQQQ | 2026-10-19 16:13 | mention spike | 4 | 9.0 | 3 | 1 | wallstreetbets 4 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1x7chad/comment/phxfqsb/) |

Full history: `episodes.csv` (one row per first flag, with the numbers known at that moment).
