# Stage 1 candidates

Updated 2026-10-22T04:10:09Z by run `39720113525`. A candidate is a ticker whose Reddit mentions (or hype-language
posts) in the last 24 hours jumped above its prior 7-day mean + 2 sd, with at least
10 mentions from 5 different authors. It stays listed until it goes
24 hours without a new flag. These are statistical flags, not accusations or advice.

| Ticker | Flagged since (UTC) | Why | Mentions 24h | Baseline/day | Authors | Hype posts | Subreddits | Exchange | StockTwits | Example |
|---|---|---|---|---|---|---|---|---|---|---|
| AMOD | 2026-10-21 16:41 | mention spike | 25 | 0.57 | 10 | 0 | pennystocks 25 | Nasdaq |  | [link](https://www.reddit.com/r/pennystocks/comments/1xbpwyi/) |
| BABA | 2026-10-22 02:50 | mention spike | 10 | 1.29 | 7 | 0 | wallstreetbets 10 | NYSE | #2 | [link](https://www.reddit.com/r/wallstreetbets/comments/1xbxqf2/comment/19rgohec6ht0j/) |
| GOOG | 2026-10-19 22:36 | mention spike | 110 | 20.43 | 69 | 0 | wallstreetbets 109, smallstreetbets 1 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xbxqf2/comment/19rgs7leqb2g2/) |
| GOOGL | 2026-10-20 18:16 | mention spike | 84 | 23.43 | 42 | 1 | wallstreetbets 84 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xbxqf2/comment/19rgret0cya00/) |
| IBM | 2026-10-21 18:15 | mention spike | 94 | 2.57 | 64 | 1 | wallstreetbets 93, smallstreetbets 1 | NYSE | #6 | [link](https://www.reddit.com/r/wallstreetbets/comments/1xc8ief/) |
| LRCX | 2026-10-20 16:42 | mention spike | 65 | 4.14 | 41 | 1 | wallstreetbets 65 | Nasdaq | #7 | [link](https://www.reddit.com/r/wallstreetbets/comments/1xbxqf2/comment/19rgfh65xt1r7/) |
| META | 2026-10-21 11:34 | mention spike | 334 | 32.71 | 188 | 1 | wallstreetbets 332, smallstreetbets 2 | Nasdaq | #3 | [link](https://www.reddit.com/r/wallstreetbets/comments/1xc0ooq/) |
| MRNA | 2026-10-20 23:18 | mention spike | 29 | 10.14 | 19 | 0 | wallstreetbets 28, smallstreetbets 1 | Nasdaq | #23 | [link](https://www.reddit.com/r/smallstreetbets/comments/1xbxqt6/comment/19rgq98gnz4yr/) |
| MSTR | 2026-10-21 19:47 | mention spike | 16 | 8.14 | 12 | 0 | wallstreetbets 16 | Nasdaq | #9 | [link](https://www.reddit.com/r/wallstreetbets/comments/1xc0sah/) |
| RDDT | 2026-10-21 22:45 | mention spike | 27 | 10.43 | 20 | 0 | wallstreetbets 26, smallstreetbets 1 | NYSE |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xbxqf2/comment/19rgs7leqb2g2/) |
| OKLO | 2026-10-20 21:21 | mention spike | 7 | 7.29 | 7 | 0 | wallstreetbets 7 | NYSE |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xatiax/comment/19rg7egourlep/) |
| SPCX | 2026-10-20 10:18 | mention spike | 234 | 90.29 | 136 | 0 | wallstreetbets 232, smallstreetbets 2 | Nasdaq |  | [link](https://www.reddit.com/r/smallstreetbets/comments/1xc48w0/) |
| SMCI | 2026-10-20 21:06 | mention spike | 29 | 17.57 | 20 | 0 | wallstreetbets 28, smallstreetbets 1 | Nasdaq |  | [link](https://www.reddit.com/r/smallstreetbets/comments/1xbi8mj/) |
| NFLX | 2026-10-19 19:31 | mention spike | 103 | 40.0 | 76 | 0 | wallstreetbets 99, smallstreetbets 4 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xbqi72/) |
| SLS | 2026-10-21 08:01 | mention spike | 5 | 6.0 | 4 | 1 | wallstreetbets 4, smallstreetbets 1 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xb2ztj/comment/19rg4zp2i1l6t/) |
| PAC | 2026-10-21 02:19 | mention spike | 0 |  | 0 | 0 |  | NYSE |  |  |
| HTZ | 2026-10-20 13:24 | mention spike | 14 | 9.29 | 12 | 0 | wallstreetbets 13, pennystocks 1 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xc1047/) |

Full history: `episodes.csv` (one row per first flag, with the numbers known at that moment).
