# Stage 1 candidates

Updated 2026-10-21T06:43:08Z by run `39556482352`. A candidate is a ticker whose Reddit mentions (or hype-language
posts) in the last 24 hours jumped above its prior 7-day mean + 2 sd, with at least
10 mentions from 5 different authors. It stays listed until it goes
24 hours without a new flag. These are statistical flags, not accusations or advice.

| Ticker | Flagged since (UTC) | Why | Mentions 24h | Baseline/day | Authors | Hype posts | Subreddits | Exchange | StockTwits | Example |
|---|---|---|---|---|---|---|---|---|---|---|
| GOOG | 2026-10-19 22:36 | mention spike | 30 | 19.43 | 25 | 0 | wallstreetbets 30 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xb4ajv/) |
| GOOGL | 2026-10-20 18:16 | mention spike | 55 | 18.71 | 21 | 0 | wallstreetbets 55 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xba7uk/comment/phz1yat/) |
| HTZ | 2026-10-20 13:24 | mention spike | 23 | 7.71 | 18 | 0 | wallstreetbets 22, pennystocks 1 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xaqvd4/) |
| LRCX | 2026-10-20 16:42 | mention spike | 15 | 2.0 | 8 | 0 | wallstreetbets 15 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1x7lpd9/comment/phz2lop/) |
| MRNA | 2026-10-20 23:18 | mention spike | 22 | 8.29 | 19 | 0 | wallstreetbets 22 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xb2qdl/) |
| NFLX | 2026-10-19 19:31 | mention spike | 211 | 12.0 | 149 | 0 | wallstreetbets 208, smallstreetbets 3 | Nasdaq | #3 | [link](https://www.reddit.com/r/wallstreetbets/comments/1xbdbqm/) |
| OKLO | 2026-10-20 21:21 | mention spike | 17 | 5.57 | 15 | 0 | wallstreetbets 17 | NYSE | #27 | [link](https://www.reddit.com/r/wallstreetbets/comments/1xbcbq2/) |
| PAC | 2026-10-21 02:19 | mention spike | 11 | 0.14 | 11 | 0 | smallstreetbets 11 | NYSE |  | [link](https://www.reddit.com/r/smallstreetbets/comments/1xay6zv/comment/phyzgua/) |
| SMCI | 2026-10-20 21:06 | mention spike | 89 | 5.29 | 60 | 1 | wallstreetbets 89 | Nasdaq | #2 | [link](https://www.reddit.com/r/wallstreetbets/comments/1xb2j2b/comment/phzh78n/) |
| SPCX | 2026-10-20 10:18 | mention spike | 379 | 43.43 | 239 | 2 | wallstreetbets 378, smallstreetbets 1 | Nasdaq | #1 | [link](https://www.reddit.com/r/wallstreetbets/comments/1xb69ph/) |
| AMZN | 2026-10-19 16:13 | mention spike | 45 | 28.29 | 25 | 0 | wallstreetbets 45 | Nasdaq | #6 | [link](https://www.reddit.com/r/wallstreetbets/comments/1xb7uvn/) |
| RIVN | 2026-10-19 18:51 | mention spike | 4 | 4.71 | 3 | 0 | wallstreetbets 4 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xb2j2b/comment/phygrnr/) |
| CRWV | 2026-10-20 14:57 | mention spike | 122 | 95.29 | 67 | 1 | wallstreetbets 122 | Nasdaq | #30 | [link](https://www.reddit.com/r/wallstreetbets/comments/1xau0nd/) |
| GLD | 2026-10-19 16:13 | mention spike | 5 | 6.43 | 4 | 0 | wallstreetbets 5 | NYSE Arca |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xao1uu/comment/phxdbir/) |
| IWM | 2026-10-20 16:03 | mention spike | 9 | 5.43 | 9 | 0 | wallstreetbets 9 | NYSE Arca |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xb2j2b/comment/phyqhjy/) |
| APLD | 2026-10-20 04:07 | mention spike | 12 | 19.43 | 10 | 0 | wallstreetbets 12 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xamm2t/) |
| TCRT | 2026-10-19 14:18 | mention spike | 0 |  | 0 | 0 |  | Nasdaq |  |  |

Full history: `episodes.csv` (one row per first flag, with the numbers known at that moment).
