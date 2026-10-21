# Stage 1 candidates

Updated 2026-10-21T01:03:23Z by run `39523960390`. A candidate is a ticker whose Reddit mentions (or hype-language
posts) in the last 24 hours jumped above its prior 7-day mean + 2 sd, with at least
10 mentions from 5 different authors. It stays listed until it goes
24 hours without a new flag. These are statistical flags, not accusations or advice.

| Ticker | Flagged since (UTC) | Why | Mentions 24h | Baseline/day | Authors | Hype posts | Subreddits | Exchange | StockTwits | Example |
|---|---|---|---|---|---|---|---|---|---|---|
| GOOGL | 2026-10-20 18:16 | mention spike | 56 | 18.86 | 23 | 0 | wallstreetbets 56 | Nasdaq | #30 | [link](https://www.reddit.com/r/wallstreetbets/comments/1xb2j2b/comment/phyoast/) |
| HTZ | 2026-10-20 13:24 | mention spike | 19 | 7.71 | 15 | 0 | wallstreetbets 18, pennystocks 1 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xaqvd4/) |
| LRCX | 2026-10-20 16:42 | mention spike | 14 | 1.86 | 7 | 0 | wallstreetbets 14 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xb2j2b/comment/phyifg7/) |
| MRNA | 2026-10-20 23:18 | mention spike | 18 | 8.43 | 16 | 0 | wallstreetbets 18 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xb2qdl/) |
| NFLX | 2026-10-19 19:31 | mention spike | 178 | 12.0 | 127 | 0 | wallstreetbets 178 | Nasdaq | #2 | [link](https://www.reddit.com/r/wallstreetbets/comments/1xb9f43/) |
| OKLO | 2026-10-20 21:21 | mention spike | 15 | 5.14 | 14 | 0 | wallstreetbets 15 | NYSE |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xatiax/) |
| SMCI | 2026-10-20 21:06 | mention spike | 76 | 5.43 | 50 | 0 | wallstreetbets 76 | Nasdaq | #3 | [link](https://www.reddit.com/r/wallstreetbets/comments/1xb2j2b/comment/phym344/) |
| SPCX | 2026-10-20 10:18 | mention spike | 336 | 42.0 | 214 | 2 | wallstreetbets 336 | Nasdaq | #1 | [link](https://www.reddit.com/r/wallstreetbets/comments/1xb69ph/) |
| GOOG | 2026-10-19 22:36 | mention spike | 26 | 19.43 | 21 | 0 | wallstreetbets 26 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xb4ajv/) |
| AMZN | 2026-10-19 16:13 | mention spike | 47 | 27.29 | 27 | 0 | wallstreetbets 47 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xb7uvn/) |
| RIVN | 2026-10-19 18:51 | mention spike | 4 | 4.71 | 3 | 0 | wallstreetbets 4 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xb2j2b/comment/phygrnr/) |
| CRWV | 2026-10-20 14:57 | mention spike | 123 | 94.0 | 68 | 1 | wallstreetbets 123 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xau0nd/) |
| GLD | 2026-10-19 16:13 | mention spike | 5 | 6.57 | 4 | 0 | wallstreetbets 5 | NYSE Arca |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xao1uu/comment/phxdbir/) |
| IWM | 2026-10-20 16:03 | mention spike | 8 | 5.43 | 8 | 0 | wallstreetbets 8 | NYSE Arca |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xao1uu/comment/phxslms/) |
| APLD | 2026-10-20 04:07 | mention spike | 15 | 18.86 | 13 | 0 | wallstreetbets 15 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xamm2t/) |
| TCRT | 2026-10-19 14:18 | mention spike | 0 |  | 0 | 0 |  | Nasdaq |  |  |

Full history: `episodes.csv` (one row per first flag, with the numbers known at that moment).
