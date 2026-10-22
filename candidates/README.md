# Stage 1 candidates

Updated 2026-10-22T00:07:59Z by run `39697394251`. A candidate is a ticker whose Reddit mentions (or hype-language
posts) in the last 24 hours jumped above its prior 7-day mean + 2 sd, with at least
10 mentions from 5 different authors. It stays listed until it goes
24 hours without a new flag. These are statistical flags, not accusations or advice.

| Ticker | Flagged since (UTC) | Why | Mentions 24h | Baseline/day | Authors | Hype posts | Subreddits | Exchange | StockTwits | Example |
|---|---|---|---|---|---|---|---|---|---|---|
| AMOD | 2026-10-21 16:41 | mention spike | 25 | 0.57 | 10 | 0 | pennystocks 25 | Nasdaq |  | [link](https://www.reddit.com/r/pennystocks/comments/1xbpwyi/) |
| GOOG | 2026-10-19 22:36 | mention spike | 106 | 20.14 | 66 | 0 | wallstreetbets 105, smallstreetbets 1 | Nasdaq | #4 | [link](https://www.reddit.com/r/wallstreetbets/comments/1xbz1vw/comment/19rggc2si4079/) |
| GOOGL | 2026-10-20 18:16 | mention spike | 82 | 23.0 | 41 | 1 | wallstreetbets 82 | Nasdaq | #19 | [link](https://www.reddit.com/r/wallstreetbets/comments/1xbxqf2/comment/19rgfpis256ow/) |
| IBM | 2026-10-21 18:15 | mention spike | 84 | 3.0 | 54 | 1 | wallstreetbets 84 | NYSE | #2 | [link](https://www.reddit.com/r/wallstreetbets/comments/1xbxqf2/comment/19rghjoecokro/) |
| LRCX | 2026-10-20 16:42 | mention spike | 67 | 3.86 | 43 | 1 | wallstreetbets 67 | Nasdaq | #5 | [link](https://www.reddit.com/r/wallstreetbets/comments/1xbxqf2/comment/19rgfh65xt1r7/) |
| META | 2026-10-21 11:34 | mention spike | 321 | 32.14 | 180 | 1 | wallstreetbets 320, smallstreetbets 1 | Nasdaq | #3 | [link](https://www.reddit.com/r/wallstreetbets/comments/1xc0ooq/) |
| MRNA | 2026-10-20 23:18 | mention spike | 28 | 9.71 | 18 | 0 | wallstreetbets 28 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xb2qdl/comment/19rgfmg16790h/) |
| MSTR | 2026-10-21 19:47 | mention spike | 15 | 8.14 | 10 | 0 | wallstreetbets 15 | Nasdaq | #11 | [link](https://www.reddit.com/r/wallstreetbets/comments/1xc0sah/) |
| RDDT | 2026-10-21 22:45 | mention spike | 22 | 10.57 | 16 | 0 | wallstreetbets 21, smallstreetbets 1 | NYSE |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xbxqf2/comment/19rgg97pipmar/) |
| OKLO | 2026-10-20 21:21 | mention spike | 13 | 6.43 | 12 | 0 | wallstreetbets 13 | NYSE |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xbcbq2/) |
| SPCX | 2026-10-20 10:18 | mention spike | 270 | 83.29 | 165 | 0 | wallstreetbets 268, smallstreetbets 2 | Nasdaq |  | [link](https://www.reddit.com/r/smallstreetbets/comments/1xbph9h/) |
| SMCI | 2026-10-20 21:06 | mention spike | 40 | 15.71 | 27 | 1 | wallstreetbets 39, smallstreetbets 1 | Nasdaq |  | [link](https://www.reddit.com/r/smallstreetbets/comments/1xbi8mj/) |
| NFLX | 2026-10-19 19:31 | mention spike | 127 | 35.71 | 96 | 0 | wallstreetbets 122, smallstreetbets 5 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xbqi72/) |
| SLS | 2026-10-21 08:01 | mention spike | 6 | 6.0 | 5 | 1 | wallstreetbets 5, smallstreetbets 1 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xb2ztj/comment/19rg4zp2i1l6t/) |
| PAC | 2026-10-21 02:19 | mention spike | 2 | 1.43 | 2 | 0 | smallstreetbets 2 | NYSE |  | [link](https://www.reddit.com/r/smallstreetbets/comments/1xay6zv/comment/phyzgua/) |
| HTZ | 2026-10-20 13:24 | mention spike | 16 | 9.0 | 12 | 0 | wallstreetbets 15, pennystocks 1 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xc1047/) |

Full history: `episodes.csv` (one row per first flag, with the numbers known at that moment).
