# Stage 1 candidates

Updated 2026-10-21T23:38:44Z by run `39694623636`. A candidate is a ticker whose Reddit mentions (or hype-language
posts) in the last 24 hours jumped above its prior 7-day mean + 2 sd, with at least
10 mentions from 5 different authors. It stays listed until it goes
24 hours without a new flag. These are statistical flags, not accusations or advice.

| Ticker | Flagged since (UTC) | Why | Mentions 24h | Baseline/day | Authors | Hype posts | Subreddits | Exchange | StockTwits | Example |
|---|---|---|---|---|---|---|---|---|---|---|
| AMOD | 2026-10-21 16:41 | mention spike | 25 | 0.43 | 10 | 0 | pennystocks 25 | Nasdaq |  | [link](https://www.reddit.com/r/pennystocks/comments/1xbpwyi/) |
| GOOG | 2026-10-19 22:36 | mention spike | 106 | 20.14 | 66 | 0 | wallstreetbets 105, smallstreetbets 1 | Nasdaq | #12 | [link](https://www.reddit.com/r/wallstreetbets/comments/1xbz1vw/comment/19rggc2si4079/) |
| GOOGL | 2026-10-20 18:16 | mention spike | 83 | 22.86 | 41 | 1 | wallstreetbets 83 | Nasdaq | #9 | [link](https://www.reddit.com/r/wallstreetbets/comments/1xbxqf2/comment/19rgfpis256ow/) |
| IBM | 2026-10-21 18:15 | mention spike | 84 | 2.86 | 54 | 1 | wallstreetbets 84 | NYSE | #3 | [link](https://www.reddit.com/r/wallstreetbets/comments/1xbxqf2/comment/19rgf55arr4mc/) |
| LRCX | 2026-10-20 16:42 | mention spike | 68 | 3.71 | 44 | 1 | wallstreetbets 68 | Nasdaq | #6 | [link](https://www.reddit.com/r/wallstreetbets/comments/1xbxqf2/comment/19rgfh65xt1r7/) |
| META | 2026-10-21 11:34 | mention spike | 318 | 32.29 | 179 | 1 | wallstreetbets 317, smallstreetbets 1 | Nasdaq | #2 | [link](https://www.reddit.com/r/wallstreetbets/comments/1xc0ooq/) |
| MRNA | 2026-10-20 23:18 | mention spike | 28 | 9.71 | 18 | 0 | wallstreetbets 28 | Nasdaq | #24 | [link](https://www.reddit.com/r/wallstreetbets/comments/1xb2qdl/comment/19rgfmg16790h/) |
| MSTR | 2026-10-21 19:47 | mention spike | 15 | 8.14 | 10 | 0 | wallstreetbets 15 | Nasdaq | #13 | [link](https://www.reddit.com/r/wallstreetbets/comments/1xc0sah/) |
| RDDT | 2026-10-21 22:45 | mention spike | 22 | 10.57 | 16 | 0 | wallstreetbets 21, smallstreetbets 1 | NYSE |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xbxqf2/comment/19rgg97pipmar/) |
| OKLO | 2026-10-20 21:21 | mention spike | 14 | 6.29 | 13 | 0 | wallstreetbets 14 | NYSE |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xbcbq2/) |
| SPCX | 2026-10-20 10:18 | mention spike | 276 | 82.0 | 171 | 1 | wallstreetbets 274, smallstreetbets 2 | Nasdaq |  | [link](https://www.reddit.com/r/smallstreetbets/comments/1xbph9h/) |
| SMCI | 2026-10-20 21:06 | mention spike | 44 | 15.14 | 31 | 1 | wallstreetbets 43, smallstreetbets 1 | Nasdaq |  | [link](https://www.reddit.com/r/smallstreetbets/comments/1xbi8mj/) |
| NFLX | 2026-10-19 19:31 | mention spike | 129 | 35.29 | 97 | 0 | wallstreetbets 124, smallstreetbets 5 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xbqi72/) |
| SLS | 2026-10-21 08:01 | mention spike | 6 | 6.14 | 5 | 1 | wallstreetbets 5, smallstreetbets 1 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xb2ztj/comment/19rg4zp2i1l6t/) |
| PAC | 2026-10-21 02:19 | mention spike | 2 | 1.43 | 2 | 0 | smallstreetbets 2 | NYSE |  | [link](https://www.reddit.com/r/smallstreetbets/comments/1xay6zv/comment/phyzgua/) |
| HTZ | 2026-10-20 13:24 | mention spike | 16 | 8.71 | 12 | 0 | wallstreetbets 15, pennystocks 1 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xc1047/) |

Full history: `episodes.csv` (one row per first flag, with the numbers known at that moment).
