# Stage 1 candidates

Updated 2026-10-21T14:17:07Z by run `39614090625`. A candidate is a ticker whose Reddit mentions (or hype-language
posts) in the last 24 hours jumped above its prior 7-day mean + 2 sd, with at least
10 mentions from 5 different authors. It stays listed until it goes
24 hours without a new flag. These are statistical flags, not accusations or advice.

| Ticker | Flagged since (UTC) | Why | Mentions 24h | Baseline/day | Authors | Hype posts | Subreddits | Exchange | StockTwits | Example |
|---|---|---|---|---|---|---|---|---|---|---|
| GOOG | 2026-10-19 22:36 | mention spike | 70 | 18.43 | 49 | 0 | wallstreetbets 69, smallstreetbets 1 | Nasdaq | #3 | [link](https://www.reddit.com/r/wallstreetbets/comments/1xb4ajv/) |
| GOOGL | 2026-10-20 18:16 | mention spike | 77 | 17.57 | 31 | 0 | wallstreetbets 77 | Nasdaq | #13 | [link](https://www.reddit.com/r/wallstreetbets/comments/1xbj0tb/comment/pi0h0wg/) |
| LRCX | 2026-10-20 16:42 | mention spike | 17 | 2.0 | 10 | 0 | wallstreetbets 17 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xbj0tb/comment/phzysps/) |
| META | 2026-10-21 11:34 | mention spike | 66 | 31.0 | 56 | 0 | wallstreetbets 65, smallstreetbets 1 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xbe5uu/) |
| MRNA | 2026-10-20 23:18 | mention spike | 22 | 8.0 | 19 | 0 | wallstreetbets 22 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xb2qdl/) |
| NFLX | 2026-10-19 19:31 | mention spike | 251 | 12.86 | 178 | 0 | wallstreetbets 247, smallstreetbets 4 | Nasdaq | #1 | [link](https://www.reddit.com/r/smallstreetbets/comments/1xbil0a/) |
| PAC | 2026-10-21 02:19 | mention spike | 11 | 0.14 | 11 | 0 | smallstreetbets 11 | NYSE |  | [link](https://www.reddit.com/r/smallstreetbets/comments/1xay6zv/comment/phyzgua/) |
| SLS | 2026-10-21 08:01 | mention spike | 12 | 5.57 | 10 | 0 | wallstreetbets 12 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xb2j2b/comment/phzo68y/) |
| SMCI | 2026-10-20 21:06 | mention spike | 104 | 5.43 | 68 | 1 | wallstreetbets 103, smallstreetbets 1 | Nasdaq | #4 | [link](https://www.reddit.com/r/smallstreetbets/comments/1xbi8mj/) |
| SPCX | 2026-10-20 10:18 | mention spike | 427 | 47.14 | 273 | 2 | wallstreetbets 426, smallstreetbets 1 | Nasdaq | #2 | [link](https://www.reddit.com/r/wallstreetbets/comments/1xb69ph/) |
| OKLO | 2026-10-20 21:21 | mention spike | 15 | 5.86 | 14 | 0 | wallstreetbets 15 | NYSE |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xbcbq2/) |
| HTZ | 2026-10-20 13:24 | mention spike | 7 | 10.0 | 6 | 0 | wallstreetbets 6, pennystocks 1 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xb2j2b/comment/phzgb1n/) |
| AMZN | 2026-10-19 16:13 | mention spike | 31 | 29.71 | 19 | 0 | wallstreetbets 31 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xb7uvn/) |
| RIVN | 2026-10-19 18:51 | mention spike | 4 | 4.86 | 4 | 0 | wallstreetbets 4 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xbj0tb/comment/pi0aaus/) |
| CRWV | 2026-10-20 14:57 | mention spike | 80 | 103.0 | 42 | 1 | wallstreetbets 80 | Nasdaq | #18 | [link](https://www.reddit.com/r/wallstreetbets/comments/1xau0nd/) |
| GLD | 2026-10-19 16:13 | mention spike | 4 | 6.43 | 3 | 0 | wallstreetbets 4 | NYSE Arca |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xao1uu/comment/phxdbir/) |
| IWM | 2026-10-20 16:03 | mention spike | 8 | 5.86 | 7 | 0 | wallstreetbets 8 | NYSE Arca |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xbj0tb/comment/pi0eyqv/) |

Full history: `episodes.csv` (one row per first flag, with the numbers known at that moment).
