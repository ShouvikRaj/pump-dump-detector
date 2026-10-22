# Stage 1 candidates

Updated 2026-10-22T00:35:01Z by run `39700113381`. A candidate is a ticker whose Reddit mentions (or hype-language
posts) in the last 24 hours jumped above its prior 7-day mean + 2 sd, with at least
10 mentions from 5 different authors. It stays listed until it goes
24 hours without a new flag. These are statistical flags, not accusations or advice.

| Ticker | Flagged since (UTC) | Why | Mentions 24h | Baseline/day | Authors | Hype posts | Subreddits | Exchange | StockTwits | Example |
|---|---|---|---|---|---|---|---|---|---|---|
| AMOD | 2026-10-21 16:41 | mention spike | 25 | 0.57 | 10 | 0 | pennystocks 25 | Nasdaq |  | [link](https://www.reddit.com/r/pennystocks/comments/1xbpwyi/) |
| GOOG | 2026-10-19 22:36 | mention spike | 108 | 20.14 | 67 | 0 | wallstreetbets 107, smallstreetbets 1 | Nasdaq | #18 | [link](https://www.reddit.com/r/wallstreetbets/comments/1xbz1vw/comment/19rgishjrs4cg/) |
| GOOGL | 2026-10-20 18:16 | mention spike | 83 | 23.0 | 42 | 1 | wallstreetbets 83 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xbxqf2/comment/19rgir51q0ahx/) |
| IBM | 2026-10-21 18:15 | mention spike | 85 | 3.0 | 55 | 1 | wallstreetbets 84, smallstreetbets 1 | NYSE | #2 | [link](https://www.reddit.com/r/wallstreetbets/comments/1xbxqf2/comment/19rghjoecokro/) |
| LRCX | 2026-10-20 16:42 | mention spike | 67 | 3.86 | 43 | 1 | wallstreetbets 67 | Nasdaq | #3 | [link](https://www.reddit.com/r/wallstreetbets/comments/1xbxqf2/comment/19rgfh65xt1r7/) |
| META | 2026-10-21 11:34 | mention spike | 326 | 32.14 | 184 | 1 | wallstreetbets 324, smallstreetbets 2 | Nasdaq | #7 | [link](https://www.reddit.com/r/wallstreetbets/comments/1xc0ooq/) |
| MRNA | 2026-10-20 23:18 | mention spike | 28 | 9.71 | 18 | 0 | wallstreetbets 28 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xb2qdl/comment/19rgfmg16790h/) |
| MSTR | 2026-10-21 19:47 | mention spike | 16 | 8.0 | 11 | 0 | wallstreetbets 16 | Nasdaq | #9 | [link](https://www.reddit.com/r/wallstreetbets/comments/1xc0sah/) |
| RDDT | 2026-10-21 22:45 | mention spike | 23 | 10.57 | 17 | 0 | wallstreetbets 22, smallstreetbets 1 | NYSE |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xbxqf2/comment/19rghxna0a2ht/) |
| OKLO | 2026-10-20 21:21 | mention spike | 13 | 6.43 | 12 | 0 | wallstreetbets 13 | NYSE |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xbcbq2/) |
| SPCX | 2026-10-20 10:18 | mention spike | 267 | 83.71 | 162 | 0 | wallstreetbets 265, smallstreetbets 2 | Nasdaq |  | [link](https://www.reddit.com/r/smallstreetbets/comments/1xbph9h/) |
| SMCI | 2026-10-20 21:06 | mention spike | 39 | 15.86 | 27 | 1 | wallstreetbets 38, smallstreetbets 1 | Nasdaq |  | [link](https://www.reddit.com/r/smallstreetbets/comments/1xbi8mj/) |
| NFLX | 2026-10-19 19:31 | mention spike | 128 | 36.0 | 97 | 0 | wallstreetbets 123, smallstreetbets 5 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xbqi72/) |
| SLS | 2026-10-21 08:01 | mention spike | 5 | 6.14 | 4 | 1 | wallstreetbets 4, smallstreetbets 1 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xb2ztj/comment/19rg4zp2i1l6t/) |
| PAC | 2026-10-21 02:19 | mention spike | 2 | 1.43 | 2 | 0 | smallstreetbets 2 | NYSE |  | [link](https://www.reddit.com/r/smallstreetbets/comments/1xay6zv/comment/phyzgua/) |
| HTZ | 2026-10-20 13:24 | mention spike | 16 | 9.0 | 12 | 0 | wallstreetbets 15, pennystocks 1 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xc1047/) |

Full history: `episodes.csv` (one row per first flag, with the numbers known at that moment).
