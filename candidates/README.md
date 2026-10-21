# Stage 1 candidates

Updated 2026-10-21T12:14:09Z by run `39597183548`. A candidate is a ticker whose Reddit mentions (or hype-language
posts) in the last 24 hours jumped above its prior 7-day mean + 2 sd, with at least
10 mentions from 5 different authors. It stays listed until it goes
24 hours without a new flag. These are statistical flags, not accusations or advice.

| Ticker | Flagged since (UTC) | Why | Mentions 24h | Baseline/day | Authors | Hype posts | Subreddits | Exchange | StockTwits | Example |
|---|---|---|---|---|---|---|---|---|---|---|
| GOOG | 2026-10-19 22:36 | mention spike | 45 | 18.86 | 35 | 0 | wallstreetbets 44, smallstreetbets 1 | Nasdaq | #8 | [link](https://www.reddit.com/r/wallstreetbets/comments/1xb4ajv/) |
| GOOGL | 2026-10-20 18:16 | mention spike | 61 | 18.57 | 24 | 0 | wallstreetbets 61 | Nasdaq | #6 | [link](https://www.reddit.com/r/wallstreetbets/comments/1xbj0tb/comment/pi02zbj/) |
| LRCX | 2026-10-20 16:42 | mention spike | 17 | 2.0 | 10 | 0 | wallstreetbets 17 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xbj0tb/comment/phzysps/) |
| META | 2026-10-21 11:34 | mention spike | 65 | 32.71 | 54 | 0 | wallstreetbets 64, smallstreetbets 1 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xbe5uu/) |
| MRNA | 2026-10-20 23:18 | mention spike | 21 | 8.29 | 18 | 0 | wallstreetbets 21 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xb2qdl/) |
| NFLX | 2026-10-19 19:31 | mention spike | 227 | 12.57 | 165 | 0 | wallstreetbets 223, smallstreetbets 4 | Nasdaq | #2 | [link](https://www.reddit.com/r/smallstreetbets/comments/1xbil0a/) |
| OKLO | 2026-10-20 21:21 | mention spike | 16 | 6.0 | 14 | 0 | wallstreetbets 16 | NYSE |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xbcbq2/) |
| PAC | 2026-10-21 02:19 | mention spike | 11 | 0.14 | 11 | 0 | smallstreetbets 11 | NYSE |  | [link](https://www.reddit.com/r/smallstreetbets/comments/1xay6zv/comment/phyzgua/) |
| SLS | 2026-10-21 08:01 | mention spike | 13 | 5.43 | 10 | 0 | wallstreetbets 13 | Nasdaq | #3 | [link](https://www.reddit.com/r/wallstreetbets/comments/1xb2j2b/comment/phzo68y/) |
| SMCI | 2026-10-20 21:06 | mention spike | 100 | 5.29 | 68 | 1 | wallstreetbets 99, smallstreetbets 1 | Nasdaq | #4 | [link](https://www.reddit.com/r/smallstreetbets/comments/1xbi8mj/) |
| SPCX | 2026-10-20 10:18 | mention spike | 389 | 46.0 | 248 | 2 | wallstreetbets 388, smallstreetbets 1 | Nasdaq | #1 | [link](https://www.reddit.com/r/wallstreetbets/comments/1xb69ph/) |
| HTZ | 2026-10-20 13:24 | mention spike | 19 | 8.29 | 16 | 0 | wallstreetbets 18, pennystocks 1 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xaqvd4/) |
| AMZN | 2026-10-19 16:13 | mention spike | 35 | 29.57 | 21 | 0 | wallstreetbets 35 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xb7uvn/) |
| RIVN | 2026-10-19 18:51 | mention spike | 4 | 4.71 | 3 | 0 | wallstreetbets 4 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xb2j2b/comment/phygrnr/) |
| CRWV | 2026-10-20 14:57 | mention spike | 115 | 96.71 | 60 | 1 | wallstreetbets 115 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xau0nd/) |
| GLD | 2026-10-19 16:13 | mention spike | 5 | 6.29 | 4 | 0 | wallstreetbets 5 | NYSE Arca |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xao1uu/comment/phxdbir/) |
| IWM | 2026-10-20 16:03 | mention spike | 10 | 5.43 | 10 | 0 | wallstreetbets 10 | NYSE Arca |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xbj0tb/comment/phzxmw9/) |

Full history: `episodes.csv` (one row per first flag, with the numbers known at that moment).
