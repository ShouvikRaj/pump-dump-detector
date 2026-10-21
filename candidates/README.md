# Stage 1 candidates

Updated 2026-10-21T23:25:17Z by run `39693202269`. A candidate is a ticker whose Reddit mentions (or hype-language
posts) in the last 24 hours jumped above its prior 7-day mean + 2 sd, with at least
10 mentions from 5 different authors. It stays listed until it goes
24 hours without a new flag. These are statistical flags, not accusations or advice.

| Ticker | Flagged since (UTC) | Why | Mentions 24h | Baseline/day | Authors | Hype posts | Subreddits | Exchange | StockTwits | Example |
|---|---|---|---|---|---|---|---|---|---|---|
| AMOD | 2026-10-21 16:41 | mention spike | 25 | 0.43 | 10 | 0 | pennystocks 25 | Nasdaq |  | [link](https://www.reddit.com/r/pennystocks/comments/1xbpwyi/) |
| GOOG | 2026-10-19 22:36 | mention spike | 104 | 20.14 | 64 | 0 | wallstreetbets 103, smallstreetbets 1 | Nasdaq | #8 | [link](https://www.reddit.com/r/wallstreetbets/comments/1xbxqf2/comment/19rgej5xcbyg1/) |
| GOOGL | 2026-10-20 18:16 | mention spike | 83 | 22.86 | 41 | 1 | wallstreetbets 83 | Nasdaq | #15 | [link](https://www.reddit.com/r/wallstreetbets/comments/1xbxqf2/comment/19rgfpis256ow/) |
| IBM | 2026-10-21 18:15 | mention spike | 84 | 2.86 | 54 | 1 | wallstreetbets 84 | NYSE | #3 | [link](https://www.reddit.com/r/wallstreetbets/comments/1xbxqf2/comment/19rgf55arr4mc/) |
| LRCX | 2026-10-20 16:42 | mention spike | 68 | 3.71 | 44 | 1 | wallstreetbets 68 | Nasdaq | #7 | [link](https://www.reddit.com/r/wallstreetbets/comments/1xbxqf2/comment/19rgfh65xt1r7/) |
| META | 2026-10-21 11:34 | mention spike | 318 | 32.29 | 179 | 1 | wallstreetbets 317, smallstreetbets 1 | Nasdaq | #2 | [link](https://www.reddit.com/r/wallstreetbets/comments/1xc0ooq/) |
| MRNA | 2026-10-20 23:18 | mention spike | 28 | 9.71 | 18 | 0 | wallstreetbets 28 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xb2qdl/comment/19rgfmg16790h/) |
| MSTR | 2026-10-21 19:47 | mention spike | 15 | 8.14 | 10 | 0 | wallstreetbets 15 | Nasdaq | #10 | [link](https://www.reddit.com/r/wallstreetbets/comments/1xc0sah/) |
| OKLO | 2026-10-20 21:21 | mention spike | 15 | 6.14 | 14 | 0 | wallstreetbets 15 | NYSE |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xbcbq2/) |
| RDDT | 2026-10-21 22:45 | mention spike | 20 | 10.71 | 14 | 0 | wallstreetbets 19, smallstreetbets 1 | NYSE |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xbxqf2/comment/19rgepocka6g1/) |
| SPCX | 2026-10-20 10:18 | mention spike | 279 | 81.57 | 175 | 1 | wallstreetbets 277, smallstreetbets 2 | Nasdaq |  | [link](https://www.reddit.com/r/smallstreetbets/comments/1xbph9h/) |
| SMCI | 2026-10-20 21:06 | mention spike | 45 | 15.0 | 32 | 1 | wallstreetbets 44, smallstreetbets 1 | Nasdaq |  | [link](https://www.reddit.com/r/smallstreetbets/comments/1xbi8mj/) |
| NFLX | 2026-10-19 19:31 | mention spike | 132 | 34.86 | 99 | 0 | wallstreetbets 127, smallstreetbets 5 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xbqi72/) |
| SLS | 2026-10-21 08:01 | mention spike | 6 | 6.14 | 5 | 1 | wallstreetbets 5, smallstreetbets 1 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xb2ztj/comment/19rg4zp2i1l6t/) |
| PAC | 2026-10-21 02:19 | mention spike | 2 | 1.43 | 2 | 0 | smallstreetbets 2 | NYSE |  | [link](https://www.reddit.com/r/smallstreetbets/comments/1xay6zv/comment/phyzgua/) |
| HTZ | 2026-10-20 13:24 | mention spike | 16 | 8.71 | 12 | 0 | wallstreetbets 15, pennystocks 1 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xc1047/) |

Full history: `episodes.csv` (one row per first flag, with the numbers known at that moment).
