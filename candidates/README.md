# Stage 1 candidates

Updated 2026-10-21T00:07:09Z by run `39518537730`. A candidate is a ticker whose Reddit mentions (or hype-language
posts) in the last 24 hours jumped above its prior 7-day mean + 2 sd, with at least
10 mentions from 5 different authors. It stays listed until it goes
24 hours without a new flag. These are statistical flags, not accusations or advice.

| Ticker | Flagged since (UTC) | Why | Mentions 24h | Baseline/day | Authors | Hype posts | Subreddits | Exchange | StockTwits | Example |
|---|---|---|---|---|---|---|---|---|---|---|
| GOOGL | 2026-10-20 18:16 | mention spike | 56 | 18.71 | 23 | 0 | wallstreetbets 56 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xb2j2b/comment/phyi9m7/) |
| HTZ | 2026-10-20 13:24 | mention spike | 19 | 7.43 | 15 | 0 | wallstreetbets 18, pennystocks 1 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xaqvd4/) |
| LRCX | 2026-10-20 16:42 | mention spike | 14 | 1.86 | 7 | 0 | wallstreetbets 14 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xb2j2b/comment/phyifg7/) |
| NFLX | 2026-10-19 19:31 | mention spike | 175 | 11.86 | 126 | 0 | wallstreetbets 175 | Nasdaq | #3 | [link](https://www.reddit.com/r/wallstreetbets/comments/1xb427h/) |
| OKLO | 2026-10-20 21:21 | mention spike | 14 | 5.14 | 13 | 0 | wallstreetbets 14 | NYSE |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xatiax/) |
| SMCI | 2026-10-20 21:06 | mention spike | 75 | 5.57 | 50 | 0 | wallstreetbets 75 | Nasdaq | #2 | [link](https://www.reddit.com/r/wallstreetbets/comments/1xb2j2b/comment/phyk7ha/) |
| SPCX | 2026-10-20 10:18 | mention spike | 325 | 41.14 | 210 | 2 | wallstreetbets 325 | Nasdaq | #1 | [link](https://www.reddit.com/r/wallstreetbets/comments/1xb69ph/) |
| MRNA | 2026-10-20 23:18 | mention spike | 17 | 8.43 | 15 | 0 | wallstreetbets 17 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xb2qdl/) |
| GOOG | 2026-10-19 22:36 | mention spike | 26 | 19.0 | 21 | 0 | wallstreetbets 26 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xb4ajv/) |
| AMZN | 2026-10-19 16:13 | mention spike | 48 | 26.71 | 27 | 0 | wallstreetbets 48 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xb7uvn/) |
| RIVN | 2026-10-19 18:51 | mention spike | 4 | 4.71 | 3 | 0 | wallstreetbets 4 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xb2j2b/comment/phygrnr/) |
| CRWV | 2026-10-20 14:57 | mention spike | 120 | 93.86 | 68 | 1 | wallstreetbets 120 | Nasdaq | #25 | [link](https://www.reddit.com/r/wallstreetbets/comments/1xau0nd/) |
| GLD | 2026-10-19 16:13 | mention spike | 6 | 6.43 | 5 | 0 | wallstreetbets 6 | NYSE Arca |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xao1uu/comment/phxdbir/) |
| IWM | 2026-10-20 16:03 | mention spike | 9 | 5.29 | 9 | 0 | wallstreetbets 9 | NYSE Arca | #18 | [link](https://www.reddit.com/r/wallstreetbets/comments/1xao1uu/comment/phxslms/) |
| APLD | 2026-10-20 04:07 | mention spike | 15 | 19.14 | 13 | 0 | wallstreetbets 15 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xamm2t/) |
| TCRT | 2026-10-19 14:18 | mention spike | 0 |  | 0 | 0 |  | Nasdaq |  |  |

Full history: `episodes.csv` (one row per first flag, with the numbers known at that moment).
