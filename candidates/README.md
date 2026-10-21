# Stage 1 candidates

Updated 2026-10-21T20:59:36Z by run `39674921797`. A candidate is a ticker whose Reddit mentions (or hype-language
posts) in the last 24 hours jumped above its prior 7-day mean + 2 sd, with at least
10 mentions from 5 different authors. It stays listed until it goes
24 hours without a new flag. These are statistical flags, not accusations or advice.

| Ticker | Flagged since (UTC) | Why | Mentions 24h | Baseline/day | Authors | Hype posts | Subreddits | Exchange | StockTwits | Example |
|---|---|---|---|---|---|---|---|---|---|---|
| AMOD | 2026-10-21 16:41 | mention spike | 21 | 0.43 | 8 | 0 | pennystocks 21 | Nasdaq |  | [link](https://www.reddit.com/r/pennystocks/comments/1xbpwyi/) |
| GOOG | 2026-10-19 22:36 | mention spike | 95 | 20.0 | 61 | 0 | wallstreetbets 94, smallstreetbets 1 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xb4ajv/) |
| GOOGL | 2026-10-20 18:16 | mention spike | 76 | 22.43 | 43 | 1 | wallstreetbets 76 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xbxqf2/comment/19rg99jx2d8o0/) |
| IBM | 2026-10-21 18:15 | mention spike | 49 | 3.0 | 30 | 1 | wallstreetbets 49 | NYSE | #4 | [link](https://www.reddit.com/r/wallstreetbets/comments/1xbxqf2/comment/19rg9ceiy7orn/) |
| LRCX | 2026-10-20 16:42 | mention spike | 60 | 3.43 | 38 | 1 | wallstreetbets 60 | Nasdaq | #3 | [link](https://www.reddit.com/r/wallstreetbets/comments/1xbxqf2/comment/19rg9fulanqck/) |
| META | 2026-10-21 11:34 | mention spike | 257 | 31.71 | 151 | 1 | wallstreetbets 256, smallstreetbets 1 | Nasdaq | #2 | [link](https://www.reddit.com/r/wallstreetbets/comments/1xbe5uu/) |
| MRNA | 2026-10-20 23:18 | mention spike | 29 | 9.43 | 19 | 0 | wallstreetbets 29 | Nasdaq | #10 | [link](https://www.reddit.com/r/wallstreetbets/comments/1xbj0tb/comment/19rg71j0v7683/) |
| NFLX | 2026-10-19 19:31 | mention spike | 156 | 30.71 | 117 | 0 | wallstreetbets 151, smallstreetbets 5 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xbqi72/) |
| OKLO | 2026-10-20 21:21 | mention spike | 17 | 6.0 | 16 | 0 | wallstreetbets 17 | NYSE |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xbcbq2/) |
| SLS | 2026-10-21 08:01 | mention spike | 13 | 5.43 | 10 | 1 | wallstreetbets 12, smallstreetbets 1 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xb2ztj/comment/19rg4zp2i1l6t/) |
| SMCI | 2026-10-20 21:06 | mention spike | 85 | 9.43 | 57 | 1 | wallstreetbets 84, smallstreetbets 1 | Nasdaq |  | [link](https://www.reddit.com/r/smallstreetbets/comments/1xbi8mj/) |
| SPCX | 2026-10-20 10:18 | mention spike | 365 | 67.29 | 228 | 1 | wallstreetbets 363, smallstreetbets 2 | Nasdaq |  | [link](https://www.reddit.com/r/smallstreetbets/comments/1xbph9h/) |
| MSTR | 2026-10-21 19:47 | mention spike | 14 | 8.14 | 9 | 0 | wallstreetbets 14 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xbj0tb/comment/19rg5tn2f0w8x/) |
| PAC | 2026-10-21 02:19 | mention spike | 5 | 1.0 | 5 | 0 | smallstreetbets 5 | NYSE |  | [link](https://www.reddit.com/r/smallstreetbets/comments/1xay6zv/comment/phyzgua/) |
| HTZ | 2026-10-20 13:24 | mention spike | 10 | 8.71 | 8 | 0 | wallstreetbets 10 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xbxqf2/comment/19rg94jl5rcww/) |

Full history: `episodes.csv` (one row per first flag, with the numbers known at that moment).
