# Stage 1 candidates

Updated 2026-10-21T20:32:57Z by run `39671126612`. A candidate is a ticker whose Reddit mentions (or hype-language
posts) in the last 24 hours jumped above its prior 7-day mean + 2 sd, with at least
10 mentions from 5 different authors. It stays listed until it goes
24 hours without a new flag. These are statistical flags, not accusations or advice.

| Ticker | Flagged since (UTC) | Why | Mentions 24h | Baseline/day | Authors | Hype posts | Subreddits | Exchange | StockTwits | Example |
|---|---|---|---|---|---|---|---|---|---|---|
| AMOD | 2026-10-21 16:41 | mention spike | 21 | 0.43 | 8 | 0 | pennystocks 21 | Nasdaq |  | [link](https://www.reddit.com/r/pennystocks/comments/1xbpwyi/) |
| GOOG | 2026-10-19 22:36 | mention spike | 94 | 20.0 | 60 | 0 | wallstreetbets 93, smallstreetbets 1 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xb4ajv/) |
| GOOGL | 2026-10-20 18:16 | mention spike | 69 | 22.29 | 42 | 0 | wallstreetbets 69 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xbyash/comment/19rg8dj493o80/) |
| IBM | 2026-10-21 18:15 | mention spike | 43 | 2.71 | 27 | 1 | wallstreetbets 43 | NYSE | #2 | [link](https://www.reddit.com/r/wallstreetbets/comments/1xbxqf2/comment/19rg8bozvv19f/) |
| LRCX | 2026-10-20 16:42 | mention spike | 55 | 3.43 | 33 | 0 | wallstreetbets 55 | Nasdaq | #5 | [link](https://www.reddit.com/r/wallstreetbets/comments/1xbxqf2/comment/19rg8drl5gh0i/) |
| META | 2026-10-21 11:34 | mention spike | 221 | 31.14 | 140 | 0 | wallstreetbets 220, smallstreetbets 1 | Nasdaq | #1 | [link](https://www.reddit.com/r/wallstreetbets/comments/1xbe5uu/) |
| MRNA | 2026-10-20 23:18 | mention spike | 30 | 9.29 | 20 | 0 | wallstreetbets 30 | Nasdaq | #8 | [link](https://www.reddit.com/r/wallstreetbets/comments/1xbj0tb/comment/19rg71j0v7683/) |
| MSTR | 2026-10-21 19:47 | mention spike | 15 | 8.0 | 10 | 0 | wallstreetbets 15 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xbj0tb/comment/19rg5tn2f0w8x/) |
| NFLX | 2026-10-19 19:31 | mention spike | 167 | 29.29 | 123 | 0 | wallstreetbets 162, smallstreetbets 5 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xbqi72/) |
| OKLO | 2026-10-20 21:21 | mention spike | 17 | 6.0 | 16 | 0 | wallstreetbets 17 | NYSE |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xbcbq2/) |
| SLS | 2026-10-21 08:01 | mention spike | 13 | 5.43 | 10 | 1 | wallstreetbets 12, smallstreetbets 1 | Nasdaq | #19 | [link](https://www.reddit.com/r/wallstreetbets/comments/1xb2ztj/comment/19rg4zp2i1l6t/) |
| SMCI | 2026-10-20 21:06 | mention spike | 107 | 6.29 | 69 | 1 | wallstreetbets 106, smallstreetbets 1 | Nasdaq | #26 | [link](https://www.reddit.com/r/smallstreetbets/comments/1xbi8mj/) |
| SPCX | 2026-10-20 10:18 | mention spike | 396 | 63.0 | 242 | 1 | wallstreetbets 394, smallstreetbets 2 | Nasdaq |  | [link](https://www.reddit.com/r/smallstreetbets/comments/1xbph9h/) |
| PAC | 2026-10-21 02:19 | mention spike | 5 | 1.0 | 5 | 0 | smallstreetbets 5 | NYSE |  | [link](https://www.reddit.com/r/smallstreetbets/comments/1xay6zv/comment/phyzgua/) |
| HTZ | 2026-10-20 13:24 | mention spike | 9 | 8.86 | 7 | 0 | wallstreetbets 9 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xbxqf2/comment/19rg7ph70iwwx/) |

Full history: `episodes.csv` (one row per first flag, with the numbers known at that moment).
