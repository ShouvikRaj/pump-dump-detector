# Stage 1 candidates

Updated 2026-10-21T22:58:50Z by run `39690198508`. A candidate is a ticker whose Reddit mentions (or hype-language
posts) in the last 24 hours jumped above its prior 7-day mean + 2 sd, with at least
10 mentions from 5 different authors. It stays listed until it goes
24 hours without a new flag. These are statistical flags, not accusations or advice.

| Ticker | Flagged since (UTC) | Why | Mentions 24h | Baseline/day | Authors | Hype posts | Subreddits | Exchange | StockTwits | Example |
|---|---|---|---|---|---|---|---|---|---|---|
| AMOD | 2026-10-21 16:41 | mention spike | 25 | 0.43 | 10 | 0 | pennystocks 25 | Nasdaq |  | [link](https://www.reddit.com/r/pennystocks/comments/1xbpwyi/) |
| GOOG | 2026-10-19 22:36 | mention spike | 105 | 20.0 | 65 | 0 | wallstreetbets 104, smallstreetbets 1 | Nasdaq | #6 | [link](https://www.reddit.com/r/wallstreetbets/comments/1xbxqf2/comment/19rgej5xcbyg1/) |
| GOOGL | 2026-10-20 18:16 | mention spike | 83 | 22.86 | 42 | 1 | wallstreetbets 83 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xbxqf2/comment/19rgc2q1vjnz6/) |
| IBM | 2026-10-21 18:15 | mention spike | 83 | 2.86 | 53 | 1 | wallstreetbets 83 | NYSE | #3 | [link](https://www.reddit.com/r/wallstreetbets/comments/1xbxqf2/comment/19rgey6jqp3c2/) |
| LRCX | 2026-10-20 16:42 | mention spike | 67 | 3.71 | 44 | 1 | wallstreetbets 67 | Nasdaq | #7 | [link](https://www.reddit.com/r/wallstreetbets/comments/1xbxqf2/comment/19rgewx2u8i05/) |
| META | 2026-10-21 11:34 | mention spike | 317 | 32.14 | 178 | 1 | wallstreetbets 316, smallstreetbets 1 | Nasdaq | #2 | [link](https://www.reddit.com/r/wallstreetbets/comments/1xc0ooq/) |
| MRNA | 2026-10-20 23:18 | mention spike | 27 | 9.71 | 17 | 0 | wallstreetbets 27 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xbj0tb/comment/19rg71j0v7683/) |
| MSTR | 2026-10-21 19:47 | mention spike | 15 | 8.14 | 10 | 0 | wallstreetbets 15 | Nasdaq | #4 | [link](https://www.reddit.com/r/wallstreetbets/comments/1xc0sah/) |
| OKLO | 2026-10-20 21:21 | mention spike | 15 | 6.14 | 14 | 0 | wallstreetbets 15 | NYSE |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xbcbq2/) |
| RDDT | 2026-10-21 22:45 | mention spike | 20 | 10.71 | 14 | 0 | wallstreetbets 19, smallstreetbets 1 | NYSE |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xbxqf2/comment/19rgepocka6g1/) |
| SPCX | 2026-10-20 10:18 | mention spike | 293 | 79.57 | 182 | 1 | wallstreetbets 291, smallstreetbets 2 | Nasdaq |  | [link](https://www.reddit.com/r/smallstreetbets/comments/1xbph9h/) |
| SMCI | 2026-10-20 21:06 | mention spike | 47 | 14.71 | 33 | 1 | wallstreetbets 46, smallstreetbets 1 | Nasdaq |  | [link](https://www.reddit.com/r/smallstreetbets/comments/1xbi8mj/) |
| NFLX | 2026-10-19 19:31 | mention spike | 138 | 34.0 | 102 | 0 | wallstreetbets 133, smallstreetbets 5 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xbqi72/) |
| SLS | 2026-10-21 08:01 | mention spike | 9 | 5.71 | 6 | 1 | wallstreetbets 8, smallstreetbets 1 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xb2ztj/comment/19rg4zp2i1l6t/) |
| PAC | 2026-10-21 02:19 | mention spike | 2 | 1.43 | 2 | 0 | smallstreetbets 2 | NYSE |  | [link](https://www.reddit.com/r/smallstreetbets/comments/1xay6zv/comment/phyzgua/) |
| HTZ | 2026-10-20 13:24 | mention spike | 15 | 8.71 | 11 | 0 | wallstreetbets 14, pennystocks 1 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xc1047/) |

Full history: `episodes.csv` (one row per first flag, with the numbers known at that moment).
