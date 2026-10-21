# Stage 1 candidates

Updated 2026-10-21T22:17:18Z by run `39685270393`. A candidate is a ticker whose Reddit mentions (or hype-language
posts) in the last 24 hours jumped above its prior 7-day mean + 2 sd, with at least
10 mentions from 5 different authors. It stays listed until it goes
24 hours without a new flag. These are statistical flags, not accusations or advice.

| Ticker | Flagged since (UTC) | Why | Mentions 24h | Baseline/day | Authors | Hype posts | Subreddits | Exchange | StockTwits | Example |
|---|---|---|---|---|---|---|---|---|---|---|
| AMOD | 2026-10-21 16:41 | mention spike | 21 | 0.43 | 8 | 0 | pennystocks 21 | Nasdaq |  | [link](https://www.reddit.com/r/pennystocks/comments/1xbpwyi/) |
| GOOG | 2026-10-19 22:36 | mention spike | 103 | 20.0 | 64 | 0 | wallstreetbets 102, smallstreetbets 1 | Nasdaq | #11 | [link](https://www.reddit.com/r/wallstreetbets/comments/1xbxqf2/comment/19rgcwb80sq3o/) |
| GOOGL | 2026-10-20 18:16 | mention spike | 83 | 23.0 | 42 | 1 | wallstreetbets 83 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xbxqf2/comment/19rgc2q1vjnz6/) |
| IBM | 2026-10-21 18:15 | mention spike | 76 | 2.86 | 47 | 1 | wallstreetbets 76 | NYSE | #3 | [link](https://www.reddit.com/r/wallstreetbets/comments/1xbxqf2/comment/19rgd40mk3mzl/) |
| LRCX | 2026-10-20 16:42 | mention spike | 65 | 3.57 | 43 | 1 | wallstreetbets 65 | Nasdaq | #4 | [link](https://www.reddit.com/r/wallstreetbets/comments/1xbxqf2/comment/19rgbx4tk0un9/) |
| META | 2026-10-21 11:34 | mention spike | 306 | 32.14 | 171 | 1 | wallstreetbets 305, smallstreetbets 1 | Nasdaq | #2 | [link](https://www.reddit.com/r/wallstreetbets/comments/1xc0ooq/) |
| MRNA | 2026-10-20 23:18 | mention spike | 29 | 9.43 | 19 | 0 | wallstreetbets 29 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xbj0tb/comment/19rg71j0v7683/) |
| MSTR | 2026-10-21 19:47 | mention spike | 15 | 8.14 | 10 | 0 | wallstreetbets 15 | Nasdaq | #5 | [link](https://www.reddit.com/r/wallstreetbets/comments/1xc0sah/) |
| OKLO | 2026-10-20 21:21 | mention spike | 16 | 6.14 | 15 | 0 | wallstreetbets 16 | NYSE |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xbcbq2/) |
| SMCI | 2026-10-20 21:06 | mention spike | 58 | 13.14 | 42 | 1 | wallstreetbets 57, smallstreetbets 1 | Nasdaq |  | [link](https://www.reddit.com/r/smallstreetbets/comments/1xbi8mj/) |
| SPCX | 2026-10-20 10:18 | mention spike | 324 | 75.0 | 198 | 1 | wallstreetbets 322, smallstreetbets 2 | Nasdaq |  | [link](https://www.reddit.com/r/smallstreetbets/comments/1xbph9h/) |
| NFLX | 2026-10-19 19:31 | mention spike | 140 | 33.57 | 105 | 0 | wallstreetbets 135, smallstreetbets 5 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xbqi72/) |
| SLS | 2026-10-21 08:01 | mention spike | 10 | 5.71 | 7 | 1 | wallstreetbets 9, smallstreetbets 1 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xb2ztj/comment/19rg4zp2i1l6t/) |
| PAC | 2026-10-21 02:19 | mention spike | 4 | 1.14 | 4 | 0 | smallstreetbets 4 | NYSE |  | [link](https://www.reddit.com/r/smallstreetbets/comments/1xay6zv/comment/phyzgua/) |
| HTZ | 2026-10-20 13:24 | mention spike | 15 | 8.57 | 11 | 0 | wallstreetbets 15 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xc1047/) |

Full history: `episodes.csv` (one row per first flag, with the numbers known at that moment).
