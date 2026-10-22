# Stage 1 candidates

Updated 2026-10-22T01:58:07Z by run `39707932480`. A candidate is a ticker whose Reddit mentions (or hype-language
posts) in the last 24 hours jumped above its prior 7-day mean + 2 sd, with at least
10 mentions from 5 different authors. It stays listed until it goes
24 hours without a new flag. These are statistical flags, not accusations or advice.

| Ticker | Flagged since (UTC) | Why | Mentions 24h | Baseline/day | Authors | Hype posts | Subreddits | Exchange | StockTwits | Example |
|---|---|---|---|---|---|---|---|---|---|---|
| AMOD | 2026-10-21 16:41 | mention spike | 25 | 0.57 | 10 | 0 | pennystocks 25 | Nasdaq |  | [link](https://www.reddit.com/r/pennystocks/comments/1xbpwyi/) |
| GOOG | 2026-10-19 22:36 | mention spike | 109 | 20.29 | 68 | 0 | wallstreetbets 108, smallstreetbets 1 | Nasdaq | #14 | [link](https://www.reddit.com/r/wallstreetbets/comments/1xbxqf2/comment/19rgk0mewf5sx/) |
| GOOGL | 2026-10-20 18:16 | mention spike | 84 | 23.14 | 43 | 1 | wallstreetbets 84 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xbxqf2/comment/19rgjsqx8iwwz/) |
| IBM | 2026-10-21 18:15 | mention spike | 89 | 2.71 | 59 | 1 | wallstreetbets 88, smallstreetbets 1 | NYSE | #3 | [link](https://www.reddit.com/r/wallstreetbets/comments/1xbxqf2/comment/19rgllcl3p6aq/) |
| LRCX | 2026-10-20 16:42 | mention spike | 67 | 3.86 | 43 | 1 | wallstreetbets 67 | Nasdaq | #5 | [link](https://www.reddit.com/r/wallstreetbets/comments/1xbxqf2/comment/19rgfh65xt1r7/) |
| META | 2026-10-21 11:34 | mention spike | 328 | 32.43 | 184 | 1 | wallstreetbets 326, smallstreetbets 2 | Nasdaq | #1 | [link](https://www.reddit.com/r/wallstreetbets/comments/1xc0ooq/) |
| MRNA | 2026-10-20 23:18 | mention spike | 27 | 10.0 | 17 | 0 | wallstreetbets 27 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xb2qdl/comment/19rgl825ub2ht/) |
| RDDT | 2026-10-21 22:45 | mention spike | 24 | 10.43 | 18 | 0 | wallstreetbets 23, smallstreetbets 1 | NYSE |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xbxqf2/comment/19rgjg3ccgmqo/) |
| MSTR | 2026-10-21 19:47 | mention spike | 15 | 8.14 | 11 | 0 | wallstreetbets 15 | Nasdaq | #4 | [link](https://www.reddit.com/r/wallstreetbets/comments/1xc0sah/) |
| OKLO | 2026-10-20 21:21 | mention spike | 12 | 6.57 | 11 | 0 | wallstreetbets 12 | NYSE |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xbcbq2/) |
| SPCX | 2026-10-20 10:18 | mention spike | 248 | 86.71 | 147 | 0 | wallstreetbets 246, smallstreetbets 2 | Nasdaq |  | [link](https://www.reddit.com/r/smallstreetbets/comments/1xc48w0/) |
| SMCI | 2026-10-20 21:06 | mention spike | 37 | 16.43 | 25 | 1 | wallstreetbets 36, smallstreetbets 1 | Nasdaq | #18 | [link](https://www.reddit.com/r/smallstreetbets/comments/1xbi8mj/) |
| NFLX | 2026-10-19 19:31 | mention spike | 118 | 37.57 | 88 | 0 | wallstreetbets 113, smallstreetbets 5 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xbqi72/) |
| SLS | 2026-10-21 08:01 | mention spike | 5 | 6.14 | 4 | 1 | wallstreetbets 4, smallstreetbets 1 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xb2ztj/comment/19rg4zp2i1l6t/) |
| PAC | 2026-10-21 02:19 | mention spike | 2 | 1.43 | 2 | 0 | smallstreetbets 2 | NYSE |  | [link](https://www.reddit.com/r/smallstreetbets/comments/1xay6zv/comment/phyzgua/) |
| HTZ | 2026-10-20 13:24 | mention spike | 16 | 9.0 | 12 | 0 | wallstreetbets 15, pennystocks 1 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xc1047/) |

Full history: `episodes.csv` (one row per first flag, with the numbers known at that moment).
