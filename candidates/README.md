# Stage 1 candidates

Updated 2026-10-21T15:34:08Z by run `39625819723`. A candidate is a ticker whose Reddit mentions (or hype-language
posts) in the last 24 hours jumped above its prior 7-day mean + 2 sd, with at least
10 mentions from 5 different authors. It stays listed until it goes
24 hours without a new flag. These are statistical flags, not accusations or advice.

| Ticker | Flagged since (UTC) | Why | Mentions 24h | Baseline/day | Authors | Hype posts | Subreddits | Exchange | StockTwits | Example |
|---|---|---|---|---|---|---|---|---|---|---|
| GOOG | 2026-10-19 22:36 | mention spike | 87 | 18.57 | 57 | 0 | wallstreetbets 86, smallstreetbets 1 | Nasdaq | #5 | [link](https://www.reddit.com/r/wallstreetbets/comments/1xb4ajv/) |
| GOOGL | 2026-10-20 18:16 | mention spike | 78 | 18.43 | 37 | 0 | wallstreetbets 78 | Nasdaq | #8 | [link](https://www.reddit.com/r/wallstreetbets/comments/1xbj0tb/comment/pi0lg7v/) |
| LRCX | 2026-10-20 16:42 | mention spike | 18 | 2.14 | 9 | 0 | wallstreetbets 18 | Nasdaq | #18 | [link](https://www.reddit.com/r/wallstreetbets/comments/1xbj0tb/comment/pi0jgoq/) |
| META | 2026-10-21 11:34 | mention spike | 75 | 29.29 | 64 | 0 | wallstreetbets 74, smallstreetbets 1 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xbe5uu/) |
| MRNA | 2026-10-20 23:18 | mention spike | 22 | 7.86 | 20 | 0 | wallstreetbets 22 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xb2qdl/) |
| NFLX | 2026-10-19 19:31 | mention spike | 252 | 13.86 | 181 | 0 | wallstreetbets 248, smallstreetbets 4 | Nasdaq | #2 | [link](https://www.reddit.com/r/smallstreetbets/comments/1xbil0a/) |
| OKLO | 2026-10-20 21:21 | mention spike | 15 | 5.86 | 15 | 0 | wallstreetbets 15 | NYSE |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xbcbq2/) |
| PAC | 2026-10-21 02:19 | mention spike | 11 | 0.14 | 11 | 0 | smallstreetbets 11 | NYSE |  | [link](https://www.reddit.com/r/smallstreetbets/comments/1xay6zv/comment/phyzgua/) |
| SLS | 2026-10-21 08:01 | mention spike | 13 | 5.71 | 11 | 0 | wallstreetbets 12, smallstreetbets 1 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xbj0tb/comment/pi0jeey/) |
| SMCI | 2026-10-20 21:06 | mention spike | 105 | 5.43 | 69 | 1 | wallstreetbets 104, smallstreetbets 1 | Nasdaq | #3 | [link](https://www.reddit.com/r/smallstreetbets/comments/1xbi8mj/) |
| SPCX | 2026-10-20 10:18 | mention spike | 463 | 46.57 | 289 | 2 | wallstreetbets 461, smallstreetbets 2 | Nasdaq | #1 | [link](https://www.reddit.com/r/smallstreetbets/comments/1xbph9h/) |
| HTZ | 2026-10-20 13:24 | mention spike | 7 | 9.57 | 6 | 0 | wallstreetbets 6, pennystocks 1 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xb2j2b/comment/phzgb1n/) |
| AMZN | 2026-10-19 16:13 | mention spike | 28 | 30.86 | 15 | 0 | wallstreetbets 28 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xb7uvn/) |
| RIVN | 2026-10-19 18:51 | mention spike | 4 | 4.71 | 4 | 0 | wallstreetbets 4 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xbj0tb/comment/pi0aaus/) |
| CRWV | 2026-10-20 14:57 | mention spike | 77 | 105.57 | 38 | 1 | wallstreetbets 77 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xbj0tb/comment/pi0m1lk/) |
| GLD | 2026-10-19 16:13 | mention spike | 3 | 6.57 | 2 | 0 | wallstreetbets 3 | NYSE Arca |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xao1uu/comment/phxdbir/) |
| IWM | 2026-10-20 16:03 | mention spike | 6 | 5.71 | 6 | 0 | wallstreetbets 6 | NYSE Arca |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xbj0tb/comment/pi0eyqv/) |

Full history: `episodes.csv` (one row per first flag, with the numbers known at that moment).
