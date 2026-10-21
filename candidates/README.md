# Stage 1 candidates

Updated 2026-10-21T17:27:37Z by run `39643831365`. A candidate is a ticker whose Reddit mentions (or hype-language
posts) in the last 24 hours jumped above its prior 7-day mean + 2 sd, with at least
10 mentions from 5 different authors. It stays listed until it goes
24 hours without a new flag. These are statistical flags, not accusations or advice.

| Ticker | Flagged since (UTC) | Why | Mentions 24h | Baseline/day | Authors | Hype posts | Subreddits | Exchange | StockTwits | Example |
|---|---|---|---|---|---|---|---|---|---|---|
| AMOD | 2026-10-21 16:41 | mention spike | 18 | 0.29 | 5 | 0 | pennystocks 18 | Nasdaq |  | [link](https://www.reddit.com/r/pennystocks/comments/1xbpwyi/) |
| GOOG | 2026-10-19 22:36 | mention spike | 99 | 18.71 | 62 | 0 | wallstreetbets 98, smallstreetbets 1 | Nasdaq | #7 | [link](https://www.reddit.com/r/wallstreetbets/comments/1xb4ajv/) |
| GOOGL | 2026-10-20 18:16 | mention spike | 74 | 19.71 | 36 | 0 | wallstreetbets 74 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xbj0tb/comment/pi0szlk/) |
| LRCX | 2026-10-20 16:42 | mention spike | 12 | 3.29 | 10 | 0 | wallstreetbets 12 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xbj0tb/comment/pi0od9s/) |
| META | 2026-10-21 11:34 | mention spike | 87 | 29.57 | 71 | 0 | wallstreetbets 86, smallstreetbets 1 | Nasdaq | #23 | [link](https://www.reddit.com/r/wallstreetbets/comments/1xbe5uu/) |
| NFLX | 2026-10-19 19:31 | mention spike | 249 | 15.71 | 180 | 0 | wallstreetbets 244, smallstreetbets 5 | Nasdaq | #3 | [link](https://www.reddit.com/r/wallstreetbets/comments/1xbqi72/) |
| OKLO | 2026-10-20 21:21 | mention spike | 16 | 5.86 | 15 | 0 | wallstreetbets 16 | NYSE |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xbcbq2/) |
| PAC | 2026-10-21 02:19 | mention spike | 11 | 0.14 | 11 | 0 | smallstreetbets 11 | NYSE |  | [link](https://www.reddit.com/r/smallstreetbets/comments/1xay6zv/comment/phyzgua/) |
| SLS | 2026-10-21 08:01 | mention spike | 13 | 5.29 | 11 | 0 | wallstreetbets 12, smallstreetbets 1 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xbj0tb/comment/pi0jeey/) |
| SMCI | 2026-10-20 21:06 | mention spike | 106 | 5.43 | 69 | 1 | wallstreetbets 105, smallstreetbets 1 | Nasdaq | #5 | [link](https://www.reddit.com/r/smallstreetbets/comments/1xbi8mj/) |
| SPCX | 2026-10-20 10:18 | mention spike | 458 | 48.43 | 284 | 2 | wallstreetbets 456, smallstreetbets 2 | Nasdaq | #1 | [link](https://www.reddit.com/r/smallstreetbets/comments/1xbph9h/) |
| MRNA | 2026-10-20 23:18 | mention spike | 18 | 8.57 | 15 | 0 | wallstreetbets 18 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xb2qdl/) |
| HTZ | 2026-10-20 13:24 | mention spike | 7 | 8.86 | 5 | 0 | wallstreetbets 7 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xbj0tb/comment/pi0szjg/) |
| AMZN | 2026-10-19 16:13 | mention spike | 32 | 31.43 | 17 | 0 | wallstreetbets 32 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xb7uvn/) |
| RIVN | 2026-10-19 18:51 | mention spike | 4 | 4.71 | 4 | 0 | wallstreetbets 4 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xbj0tb/comment/pi0aaus/) |

Full history: `episodes.csv` (one row per first flag, with the numbers known at that moment).
