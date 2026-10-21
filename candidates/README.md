# Stage 1 candidates

Updated 2026-10-21T21:39:28Z by run `39680393186`. A candidate is a ticker whose Reddit mentions (or hype-language
posts) in the last 24 hours jumped above its prior 7-day mean + 2 sd, with at least
10 mentions from 5 different authors. It stays listed until it goes
24 hours without a new flag. These are statistical flags, not accusations or advice.

| Ticker | Flagged since (UTC) | Why | Mentions 24h | Baseline/day | Authors | Hype posts | Subreddits | Exchange | StockTwits | Example |
|---|---|---|---|---|---|---|---|---|---|---|
| AMOD | 2026-10-21 16:41 | mention spike | 21 | 0.43 | 8 | 0 | pennystocks 21 | Nasdaq |  | [link](https://www.reddit.com/r/pennystocks/comments/1xbpwyi/) |
| GOOG | 2026-10-19 22:36 | mention spike | 100 | 20.14 | 64 | 0 | wallstreetbets 99, smallstreetbets 1 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xbxqf2/comment/19rgb9xt37pcz/) |
| GOOGL | 2026-10-20 18:16 | mention spike | 83 | 22.71 | 43 | 1 | wallstreetbets 83 | Nasdaq | #20 | [link](https://www.reddit.com/r/wallstreetbets/comments/1xbxqf2/comment/19rgb9xt37pcz/) |
| IBM | 2026-10-21 18:15 | mention spike | 53 | 2.86 | 30 | 1 | wallstreetbets 53 | NYSE | #4 | [link](https://www.reddit.com/r/wallstreetbets/comments/1xbxqf2/comment/19rgb3a4kgi02/) |
| LRCX | 2026-10-20 16:42 | mention spike | 61 | 3.57 | 39 | 1 | wallstreetbets 61 | Nasdaq | #3 | [link](https://www.reddit.com/r/wallstreetbets/comments/1xbxqf2/comment/19rgapkvpiihv/) |
| META | 2026-10-21 11:34 | mention spike | 288 | 32.29 | 164 | 1 | wallstreetbets 287, smallstreetbets 1 | Nasdaq | #2 | [link](https://www.reddit.com/r/wallstreetbets/comments/1xbe5uu/) |
| MRNA | 2026-10-20 23:18 | mention spike | 29 | 9.43 | 19 | 0 | wallstreetbets 29 | Nasdaq | #13 | [link](https://www.reddit.com/r/wallstreetbets/comments/1xbj0tb/comment/19rg71j0v7683/) |
| NFLX | 2026-10-19 19:31 | mention spike | 143 | 32.86 | 109 | 0 | wallstreetbets 138, smallstreetbets 5 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xbqi72/) |
| OKLO | 2026-10-20 21:21 | mention spike | 16 | 6.14 | 15 | 0 | wallstreetbets 16 | NYSE |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xbcbq2/) |
| SMCI | 2026-10-20 21:06 | mention spike | 67 | 11.86 | 45 | 1 | wallstreetbets 66, smallstreetbets 1 | Nasdaq |  | [link](https://www.reddit.com/r/smallstreetbets/comments/1xbi8mj/) |
| SPCX | 2026-10-20 10:18 | mention spike | 339 | 71.57 | 208 | 1 | wallstreetbets 337, smallstreetbets 2 | Nasdaq |  | [link](https://www.reddit.com/r/smallstreetbets/comments/1xbph9h/) |
| SLS | 2026-10-21 08:01 | mention spike | 10 | 5.86 | 7 | 1 | wallstreetbets 9, smallstreetbets 1 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xb2ztj/comment/19rg4zp2i1l6t/) |
| MSTR | 2026-10-21 19:47 | mention spike | 14 | 8.14 | 9 | 0 | wallstreetbets 14 | Nasdaq | #12 | [link](https://www.reddit.com/r/wallstreetbets/comments/1xbj0tb/comment/19rg5tn2f0w8x/) |
| PAC | 2026-10-21 02:19 | mention spike | 4 | 1.14 | 4 | 0 | smallstreetbets 4 | NYSE |  | [link](https://www.reddit.com/r/smallstreetbets/comments/1xay6zv/comment/phyzgua/) |
| HTZ | 2026-10-20 13:24 | mention spike | 12 | 8.71 | 9 | 0 | wallstreetbets 12 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xbxqf2/comment/19rga62wl9qg4/) |

Full history: `episodes.csv` (one row per first flag, with the numbers known at that moment).
