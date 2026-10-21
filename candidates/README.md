# Stage 1 candidates

Updated 2026-10-21T03:38:10Z by run `39539043996`. A candidate is a ticker whose Reddit mentions (or hype-language
posts) in the last 24 hours jumped above its prior 7-day mean + 2 sd, with at least
10 mentions from 5 different authors. It stays listed until it goes
24 hours without a new flag. These are statistical flags, not accusations or advice.

| Ticker | Flagged since (UTC) | Why | Mentions 24h | Baseline/day | Authors | Hype posts | Subreddits | Exchange | StockTwits | Example |
|---|---|---|---|---|---|---|---|---|---|---|
| GOOGL | 2026-10-20 18:16 | mention spike | 55 | 18.86 | 21 | 0 | wallstreetbets 55 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xba7uk/comment/phz1yat/) |
| HTZ | 2026-10-20 13:24 | mention spike | 20 | 7.71 | 16 | 0 | wallstreetbets 19, pennystocks 1 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xaqvd4/) |
| LRCX | 2026-10-20 16:42 | mention spike | 15 | 2.0 | 8 | 0 | wallstreetbets 15 | Nasdaq | #7 | [link](https://www.reddit.com/r/wallstreetbets/comments/1x7lpd9/comment/phz2lop/) |
| MRNA | 2026-10-20 23:18 | mention spike | 20 | 8.43 | 17 | 0 | wallstreetbets 20 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xb2qdl/) |
| NFLX | 2026-10-19 19:31 | mention spike | 197 | 12.29 | 138 | 0 | wallstreetbets 196, smallstreetbets 1 | Nasdaq | #3 | [link](https://www.reddit.com/r/wallstreetbets/comments/1xb9f43/) |
| OKLO | 2026-10-20 21:21 | mention spike | 13 | 5.57 | 11 | 0 | wallstreetbets 13 | NYSE |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xbcbq2/) |
| PAC | 2026-10-21 02:19 | mention spike | 11 | 0.14 | 11 | 0 | smallstreetbets 11 | NYSE |  | [link](https://www.reddit.com/r/smallstreetbets/comments/1xay6zv/comment/phyzgua/) |
| SMCI | 2026-10-20 21:06 | mention spike | 83 | 5.29 | 56 | 0 | wallstreetbets 83 | Nasdaq | #2 | [link](https://www.reddit.com/r/wallstreetbets/comments/1xb2j2b/comment/phz0kod/) |
| SPCX | 2026-10-20 10:18 | mention spike | 365 | 42.86 | 232 | 2 | wallstreetbets 364, smallstreetbets 1 | Nasdaq | #1 | [link](https://www.reddit.com/r/wallstreetbets/comments/1xb69ph/) |
| GOOG | 2026-10-19 22:36 | mention spike | 26 | 19.43 | 21 | 0 | wallstreetbets 26 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xb4ajv/) |
| AMZN | 2026-10-19 16:13 | mention spike | 45 | 27.71 | 26 | 0 | wallstreetbets 45 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xb7uvn/) |
| RIVN | 2026-10-19 18:51 | mention spike | 4 | 4.71 | 3 | 0 | wallstreetbets 4 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xb2j2b/comment/phygrnr/) |
| CRWV | 2026-10-20 14:57 | mention spike | 118 | 95.14 | 64 | 1 | wallstreetbets 118 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xau0nd/) |
| GLD | 2026-10-19 16:13 | mention spike | 5 | 6.43 | 4 | 0 | wallstreetbets 5 | NYSE Arca |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xao1uu/comment/phxdbir/) |
| IWM | 2026-10-20 16:03 | mention spike | 9 | 5.43 | 9 | 0 | wallstreetbets 9 | NYSE Arca |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xb2j2b/comment/phyqhjy/) |
| APLD | 2026-10-20 04:07 | mention spike | 17 | 18.71 | 14 | 0 | wallstreetbets 17 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xamm2t/) |
| TCRT | 2026-10-19 14:18 | mention spike | 0 |  | 0 | 0 |  | Nasdaq |  |  |

Full history: `episodes.csv` (one row per first flag, with the numbers known at that moment).
