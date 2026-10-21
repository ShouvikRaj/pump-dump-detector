# Stage 1 candidates

Updated 2026-10-21T18:27:10Z by run `39651702050`. A candidate is a ticker whose Reddit mentions (or hype-language
posts) in the last 24 hours jumped above its prior 7-day mean + 2 sd, with at least
10 mentions from 5 different authors. It stays listed until it goes
24 hours without a new flag. These are statistical flags, not accusations or advice.

| Ticker | Flagged since (UTC) | Why | Mentions 24h | Baseline/day | Authors | Hype posts | Subreddits | Exchange | StockTwits | Example |
|---|---|---|---|---|---|---|---|---|---|---|
| AMOD | 2026-10-21 16:41 | mention spike | 20 | 0.43 | 8 | 0 | pennystocks 20 | Nasdaq |  | [link](https://www.reddit.com/r/pennystocks/comments/1xbpwyi/) |
| GOOG | 2026-10-19 22:36 | mention spike | 97 | 19.0 | 62 | 0 | wallstreetbets 96, smallstreetbets 1 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xb4ajv/) |
| GOOGL | 2026-10-20 18:16 | mention spike | 73 | 20.57 | 37 | 0 | wallstreetbets 73 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xbj0tb/comment/19rg1l388wxmp/) |
| IBM | 2026-10-21 18:15 | mention spike | 12 | 2.57 | 9 | 0 | wallstreetbets 12 | NYSE | #22 | [link](https://www.reddit.com/r/wallstreetbets/comments/1x7lpd9/comment/19rg220tvuj0k/) |
| LRCX | 2026-10-20 16:42 | mention spike | 23 | 3.29 | 15 | 0 | wallstreetbets 23 | Nasdaq | #4 | [link](https://www.reddit.com/r/wallstreetbets/comments/1xbj0tb/comment/19rg2guoj3znn/) |
| META | 2026-10-21 11:34 | mention spike | 100 | 30.14 | 73 | 0 | wallstreetbets 99, smallstreetbets 1 | Nasdaq | #5 | [link](https://www.reddit.com/r/wallstreetbets/comments/1xbe5uu/) |
| MRNA | 2026-10-20 23:18 | mention spike | 22 | 8.71 | 18 | 0 | wallstreetbets 22 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xb2qdl/) |
| NFLX | 2026-10-19 19:31 | mention spike | 250 | 16.57 | 179 | 0 | wallstreetbets 245, smallstreetbets 5 | Nasdaq | #16 | [link](https://www.reddit.com/r/wallstreetbets/comments/1xbqi72/) |
| OKLO | 2026-10-20 21:21 | mention spike | 16 | 5.86 | 15 | 0 | wallstreetbets 16 | NYSE |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xbcbq2/) |
| SLS | 2026-10-21 08:01 | mention spike | 13 | 5.43 | 11 | 0 | wallstreetbets 12, smallstreetbets 1 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xb2ztj/comment/pi0v7kr/) |
| SMCI | 2026-10-20 21:06 | mention spike | 113 | 5.43 | 71 | 1 | wallstreetbets 112, smallstreetbets 1 | Nasdaq |  | [link](https://www.reddit.com/r/smallstreetbets/comments/1xbi8mj/) |
| SPCX | 2026-10-20 10:18 | mention spike | 475 | 49.14 | 283 | 2 | wallstreetbets 473, smallstreetbets 2 | Nasdaq | #1 | [link](https://www.reddit.com/r/smallstreetbets/comments/1xbph9h/) |
| PAC | 2026-10-21 02:19 | mention spike | 6 | 0.86 | 6 | 0 | smallstreetbets 6 | NYSE |  | [link](https://www.reddit.com/r/smallstreetbets/comments/1xay6zv/comment/phyzgua/) |
| HTZ | 2026-10-20 13:24 | mention spike | 7 | 8.86 | 5 | 0 | wallstreetbets 7 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xbj0tb/comment/pi0szjg/) |
| AMZN | 2026-10-19 16:13 | mention spike | 36 | 31.14 | 19 | 0 | wallstreetbets 36 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xb7uvn/) |
| RIVN | 2026-10-19 18:51 | mention spike | 4 | 4.71 | 4 | 0 | wallstreetbets 4 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xbj0tb/comment/pi0aaus/) |

Full history: `episodes.csv` (one row per first flag, with the numbers known at that moment).
