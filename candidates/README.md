# Stage 1 candidates

Updated 2026-10-21T19:23:08Z by run `39659607128`. A candidate is a ticker whose Reddit mentions (or hype-language
posts) in the last 24 hours jumped above its prior 7-day mean + 2 sd, with at least
10 mentions from 5 different authors. It stays listed until it goes
24 hours without a new flag. These are statistical flags, not accusations or advice.

| Ticker | Flagged since (UTC) | Why | Mentions 24h | Baseline/day | Authors | Hype posts | Subreddits | Exchange | StockTwits | Example |
|---|---|---|---|---|---|---|---|---|---|---|
| AMOD | 2026-10-21 16:41 | mention spike | 21 | 0.43 | 8 | 0 | pennystocks 21 | Nasdaq |  | [link](https://www.reddit.com/r/pennystocks/comments/1xbpwyi/) |
| GOOG | 2026-10-19 22:36 | mention spike | 97 | 19.57 | 61 | 0 | wallstreetbets 96, smallstreetbets 1 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xb4ajv/) |
| GOOGL | 2026-10-20 18:16 | mention spike | 68 | 21.71 | 38 | 0 | wallstreetbets 68 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xbj0tb/comment/19rg4idkz6vyd/) |
| IBM | 2026-10-21 18:15 | mention spike | 16 | 2.71 | 14 | 0 | wallstreetbets 16 | NYSE | #15 | [link](https://www.reddit.com/r/wallstreetbets/comments/1xbj0tb/comment/19rg4v5e0tidd/) |
| LRCX | 2026-10-20 16:42 | mention spike | 26 | 3.43 | 15 | 0 | wallstreetbets 26 | Nasdaq | #4 | [link](https://www.reddit.com/r/wallstreetbets/comments/1xbj0tb/comment/19rg4nhpzh4xu/) |
| META | 2026-10-21 11:34 | mention spike | 120 | 30.29 | 83 | 0 | wallstreetbets 119, smallstreetbets 1 | Nasdaq | #2 | [link](https://www.reddit.com/r/wallstreetbets/comments/1xbe5uu/) |
| MRNA | 2026-10-20 23:18 | mention spike | 26 | 8.71 | 21 | 0 | wallstreetbets 26 | Nasdaq | #7 | [link](https://www.reddit.com/r/wallstreetbets/comments/1xb2qdl/) |
| NFLX | 2026-10-19 19:31 | mention spike | 237 | 19.14 | 172 | 0 | wallstreetbets 232, smallstreetbets 5 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xbqi72/) |
| OKLO | 2026-10-20 21:21 | mention spike | 16 | 5.86 | 15 | 0 | wallstreetbets 16 | NYSE |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xbcbq2/) |
| SLS | 2026-10-21 08:01 | mention spike | 12 | 5.57 | 10 | 0 | wallstreetbets 11, smallstreetbets 1 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xb2ztj/comment/pi0v7kr/) |
| SMCI | 2026-10-20 21:06 | mention spike | 108 | 6.14 | 68 | 1 | wallstreetbets 107, smallstreetbets 1 | Nasdaq | #20 | [link](https://www.reddit.com/r/smallstreetbets/comments/1xbi8mj/) |
| SPCX | 2026-10-20 10:18 | mention spike | 469 | 51.43 | 277 | 2 | wallstreetbets 467, smallstreetbets 2 | Nasdaq | #1 | [link](https://www.reddit.com/r/smallstreetbets/comments/1xbph9h/) |
| PAC | 2026-10-21 02:19 | mention spike | 6 | 0.86 | 6 | 0 | smallstreetbets 6 | NYSE |  | [link](https://www.reddit.com/r/smallstreetbets/comments/1xay6zv/comment/phyzgua/) |
| HTZ | 2026-10-20 13:24 | mention spike | 7 | 8.86 | 5 | 0 | wallstreetbets 7 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xbj0tb/comment/pi0szjg/) |
| AMZN | 2026-10-19 16:13 | mention spike | 36 | 31.43 | 20 | 0 | wallstreetbets 36 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xb7uvn/) |

Full history: `episodes.csv` (one row per first flag, with the numbers known at that moment).
