# Stage 1 candidates

Updated 2026-10-21T21:12:49Z by run `39676785685`. A candidate is a ticker whose Reddit mentions (or hype-language
posts) in the last 24 hours jumped above its prior 7-day mean + 2 sd, with at least
10 mentions from 5 different authors. It stays listed until it goes
24 hours without a new flag. These are statistical flags, not accusations or advice.

| Ticker | Flagged since (UTC) | Why | Mentions 24h | Baseline/day | Authors | Hype posts | Subreddits | Exchange | StockTwits | Example |
|---|---|---|---|---|---|---|---|---|---|---|
| AMOD | 2026-10-21 16:41 | mention spike | 21 | 0.43 | 8 | 0 | pennystocks 21 | Nasdaq |  | [link](https://www.reddit.com/r/pennystocks/comments/1xbpwyi/) |
| GOOG | 2026-10-19 22:36 | mention spike | 97 | 20.14 | 63 | 0 | wallstreetbets 96, smallstreetbets 1 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xbxqf2/comment/19rg9xcpsaq74/) |
| GOOGL | 2026-10-20 18:16 | mention spike | 78 | 22.43 | 43 | 1 | wallstreetbets 78 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xbz1vw/comment/19rga22wyqayr/) |
| IBM | 2026-10-21 18:15 | mention spike | 49 | 3.0 | 30 | 1 | wallstreetbets 49 | NYSE | #4 | [link](https://www.reddit.com/r/wallstreetbets/comments/1xbxqf2/comment/19rg9ceiy7orn/) |
| LRCX | 2026-10-20 16:42 | mention spike | 60 | 3.43 | 38 | 1 | wallstreetbets 60 | Nasdaq | #3 | [link](https://www.reddit.com/r/wallstreetbets/comments/1xbxqf2/comment/19rg9fulanqck/) |
| META | 2026-10-21 11:34 | mention spike | 272 | 31.71 | 161 | 1 | wallstreetbets 271, smallstreetbets 1 | Nasdaq | #2 | [link](https://www.reddit.com/r/wallstreetbets/comments/1xbe5uu/) |
| MRNA | 2026-10-20 23:18 | mention spike | 29 | 9.43 | 19 | 0 | wallstreetbets 29 | Nasdaq | #12 | [link](https://www.reddit.com/r/wallstreetbets/comments/1xbj0tb/comment/19rg71j0v7683/) |
| NFLX | 2026-10-19 19:31 | mention spike | 153 | 31.43 | 115 | 0 | wallstreetbets 148, smallstreetbets 5 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xbqi72/) |
| OKLO | 2026-10-20 21:21 | mention spike | 17 | 6.0 | 16 | 0 | wallstreetbets 17 | NYSE |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xbcbq2/) |
| SLS | 2026-10-21 08:01 | mention spike | 13 | 5.43 | 10 | 1 | wallstreetbets 12, smallstreetbets 1 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xb2ztj/comment/19rg4zp2i1l6t/) |
| SMCI | 2026-10-20 21:06 | mention spike | 82 | 9.86 | 55 | 1 | wallstreetbets 81, smallstreetbets 1 | Nasdaq |  | [link](https://www.reddit.com/r/smallstreetbets/comments/1xbi8mj/) |
| SPCX | 2026-10-20 10:18 | mention spike | 353 | 69.14 | 218 | 1 | wallstreetbets 351, smallstreetbets 2 | Nasdaq |  | [link](https://www.reddit.com/r/smallstreetbets/comments/1xbph9h/) |
| MSTR | 2026-10-21 19:47 | mention spike | 14 | 8.14 | 9 | 0 | wallstreetbets 14 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xbj0tb/comment/19rg5tn2f0w8x/) |
| PAC | 2026-10-21 02:19 | mention spike | 5 | 1.0 | 5 | 0 | smallstreetbets 5 | NYSE |  | [link](https://www.reddit.com/r/smallstreetbets/comments/1xay6zv/comment/phyzgua/) |
| HTZ | 2026-10-20 13:24 | mention spike | 12 | 8.71 | 9 | 0 | wallstreetbets 12 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xbxqf2/comment/19rga62wl9qg4/) |

Full history: `episodes.csv` (one row per first flag, with the numbers known at that moment).
