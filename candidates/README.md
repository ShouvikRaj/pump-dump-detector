# Stage 1 candidates

Updated 2026-10-22T03:29:07Z by run `39716470850`. A candidate is a ticker whose Reddit mentions (or hype-language
posts) in the last 24 hours jumped above its prior 7-day mean + 2 sd, with at least
10 mentions from 5 different authors. It stays listed until it goes
24 hours without a new flag. These are statistical flags, not accusations or advice.

| Ticker | Flagged since (UTC) | Why | Mentions 24h | Baseline/day | Authors | Hype posts | Subreddits | Exchange | StockTwits | Example |
|---|---|---|---|---|---|---|---|---|---|---|
| AMOD | 2026-10-21 16:41 | mention spike | 25 | 0.57 | 10 | 0 | pennystocks 25 | Nasdaq |  | [link](https://www.reddit.com/r/pennystocks/comments/1xbpwyi/) |
| BABA | 2026-10-22 02:50 | mention spike | 10 | 1.29 | 7 | 0 | wallstreetbets 10 | NYSE | #3 | [link](https://www.reddit.com/r/wallstreetbets/comments/1xbxqf2/comment/19rgohec6ht0j/) |
| GOOG | 2026-10-19 22:36 | mention spike | 109 | 20.57 | 69 | 0 | wallstreetbets 108, smallstreetbets 1 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xbxqf2/comment/19rgpujo8sbvp/) |
| GOOGL | 2026-10-20 18:16 | mention spike | 82 | 23.43 | 41 | 1 | wallstreetbets 82 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xbxqf2/comment/19rgjsqx8iwwz/) |
| IBM | 2026-10-21 18:15 | mention spike | 90 | 2.57 | 60 | 1 | wallstreetbets 89, smallstreetbets 1 | NYSE | #7 | [link](https://www.reddit.com/r/wallstreetbets/comments/1xbxqf2/comment/19rgod9q084ys/) |
| LRCX | 2026-10-20 16:42 | mention spike | 65 | 4.14 | 41 | 1 | wallstreetbets 65 | Nasdaq | #6 | [link](https://www.reddit.com/r/wallstreetbets/comments/1xbxqf2/comment/19rgfh65xt1r7/) |
| META | 2026-10-21 11:34 | mention spike | 331 | 32.71 | 186 | 1 | wallstreetbets 329, smallstreetbets 2 | Nasdaq | #1 | [link](https://www.reddit.com/r/wallstreetbets/comments/1xc0ooq/) |
| MRNA | 2026-10-20 23:18 | mention spike | 29 | 10.14 | 19 | 0 | wallstreetbets 28, smallstreetbets 1 | Nasdaq |  | [link](https://www.reddit.com/r/smallstreetbets/comments/1xbxqt6/comment/19rgq98gnz4yr/) |
| RDDT | 2026-10-21 22:45 | mention spike | 26 | 10.43 | 20 | 0 | wallstreetbets 25, smallstreetbets 1 | NYSE |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xbxqf2/comment/19rgp6ljregpx/) |
| MSTR | 2026-10-21 19:47 | mention spike | 15 | 8.14 | 11 | 0 | wallstreetbets 15 | Nasdaq | #5 | [link](https://www.reddit.com/r/wallstreetbets/comments/1xc0sah/) |
| OKLO | 2026-10-20 21:21 | mention spike | 11 | 6.71 | 11 | 0 | wallstreetbets 11 | NYSE |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xatiax/comment/19rg7egourlep/) |
| SPCX | 2026-10-20 10:18 | mention spike | 232 | 90.0 | 135 | 0 | wallstreetbets 230, smallstreetbets 2 | Nasdaq | #29 | [link](https://www.reddit.com/r/smallstreetbets/comments/1xc48w0/) |
| SMCI | 2026-10-20 21:06 | mention spike | 34 | 16.86 | 22 | 1 | wallstreetbets 33, smallstreetbets 1 | Nasdaq | #18 | [link](https://www.reddit.com/r/smallstreetbets/comments/1xbi8mj/) |
| NFLX | 2026-10-19 19:31 | mention spike | 106 | 39.57 | 79 | 0 | wallstreetbets 101, smallstreetbets 5 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xbqi72/) |
| SLS | 2026-10-21 08:01 | mention spike | 5 | 6.0 | 4 | 1 | wallstreetbets 4, smallstreetbets 1 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xb2ztj/comment/19rg4zp2i1l6t/) |
| PAC | 2026-10-21 02:19 | mention spike | 0 |  | 0 | 0 |  | NYSE |  |  |
| HTZ | 2026-10-20 13:24 | mention spike | 15 | 9.14 | 12 | 0 | wallstreetbets 14, pennystocks 1 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xc1047/) |

Full history: `episodes.csv` (one row per first flag, with the numbers known at that moment).
