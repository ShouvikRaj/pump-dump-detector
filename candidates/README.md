# Stage 1 candidates

Updated 2026-10-21T16:27:08Z by run `39633846097`. A candidate is a ticker whose Reddit mentions (or hype-language
posts) in the last 24 hours jumped above its prior 7-day mean + 2 sd, with at least
10 mentions from 5 different authors. It stays listed until it goes
24 hours without a new flag. These are statistical flags, not accusations or advice.

| Ticker | Flagged since (UTC) | Why | Mentions 24h | Baseline/day | Authors | Hype posts | Subreddits | Exchange | StockTwits | Example |
|---|---|---|---|---|---|---|---|---|---|---|
| GOOG | 2026-10-19 22:36 | mention spike | 93 | 18.57 | 60 | 0 | wallstreetbets 92, smallstreetbets 1 | Nasdaq | #7 | [link](https://www.reddit.com/r/wallstreetbets/comments/1xb4ajv/) |
| GOOGL | 2026-10-20 18:16 | mention spike | 76 | 18.86 | 38 | 0 | wallstreetbets 76 | Nasdaq | #16 | [link](https://www.reddit.com/r/wallstreetbets/comments/1xbj0tb/comment/pi0o3fb/) |
| LRCX | 2026-10-20 16:42 | mention spike | 15 | 2.86 | 10 | 0 | wallstreetbets 15 | Nasdaq | #29 | [link](https://www.reddit.com/r/wallstreetbets/comments/1xbj0tb/comment/pi0od9s/) |
| META | 2026-10-21 11:34 | mention spike | 77 | 29.43 | 65 | 0 | wallstreetbets 76, smallstreetbets 1 | Nasdaq | #26 | [link](https://www.reddit.com/r/wallstreetbets/comments/1xbe5uu/) |
| MRNA | 2026-10-20 23:18 | mention spike | 23 | 7.71 | 19 | 0 | wallstreetbets 23 | Nasdaq | #12 | [link](https://www.reddit.com/r/wallstreetbets/comments/1xb2qdl/) |
| NFLX | 2026-10-19 19:31 | mention spike | 252 | 14.86 | 181 | 0 | wallstreetbets 248, smallstreetbets 4 | Nasdaq | #2 | [link](https://www.reddit.com/r/wallstreetbets/comments/1xbqi72/) |
| OKLO | 2026-10-20 21:21 | mention spike | 16 | 5.86 | 15 | 0 | wallstreetbets 16 | NYSE |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xbcbq2/) |
| PAC | 2026-10-21 02:19 | mention spike | 11 | 0.14 | 11 | 0 | smallstreetbets 11 | NYSE |  | [link](https://www.reddit.com/r/smallstreetbets/comments/1xay6zv/comment/phyzgua/) |
| SLS | 2026-10-21 08:01 | mention spike | 13 | 5.29 | 11 | 0 | wallstreetbets 12, smallstreetbets 1 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xbj0tb/comment/pi0jeey/) |
| SMCI | 2026-10-20 21:06 | mention spike | 106 | 5.43 | 69 | 1 | wallstreetbets 105, smallstreetbets 1 | Nasdaq | #4 | [link](https://www.reddit.com/r/smallstreetbets/comments/1xbi8mj/) |
| SPCX | 2026-10-20 10:18 | mention spike | 453 | 48.43 | 284 | 2 | wallstreetbets 451, smallstreetbets 2 | Nasdaq | #1 | [link](https://www.reddit.com/r/smallstreetbets/comments/1xbph9h/) |
| HTZ | 2026-10-20 13:24 | mention spike | 7 | 9.29 | 5 | 0 | wallstreetbets 6, pennystocks 1 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xbj0tb/comment/pi0oxpj/) |
| AMZN | 2026-10-19 16:13 | mention spike | 29 | 30.86 | 16 | 0 | wallstreetbets 29 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xb7uvn/) |
| RIVN | 2026-10-19 18:51 | mention spike | 4 | 4.71 | 4 | 0 | wallstreetbets 4 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xbj0tb/comment/pi0aaus/) |
| CRWV | 2026-10-20 14:57 | mention spike | 77 | 105.86 | 37 | 1 | wallstreetbets 77 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xbj0tb/comment/pi0os0n/) |
| GLD | 2026-10-19 16:13 | mention spike | 2 | 6.57 | 2 | 0 | wallstreetbets 2 | NYSE Arca |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xao1uu/comment/phxdbir/) |

Full history: `episodes.csv` (one row per first flag, with the numbers known at that moment).
