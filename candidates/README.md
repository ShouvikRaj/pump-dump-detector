# Stage 1 candidates

Updated 2026-10-22T10:41:09Z by run `39764146779`. A candidate is a ticker whose Reddit mentions (or hype-language
posts) in the last 24 hours jumped above its prior 7-day mean + 2 sd, with at least
10 mentions from 5 different authors. It stays listed until it goes
24 hours without a new flag. These are statistical flags, not accusations or advice.

| Ticker | Flagged since (UTC) | Why | Mentions 24h | Baseline/day | Authors | Hype posts | Subreddits | Exchange | StockTwits | Example |
|---|---|---|---|---|---|---|---|---|---|---|
| AMOD | 2026-10-21 16:41 | mention spike | 25 | 0.57 | 10 | 0 | pennystocks 25 | Nasdaq |  | [link](https://www.reddit.com/r/pennystocks/comments/1xbpwyi/) |
| BABA | 2026-10-22 02:50 | mention spike | 12 | 1.29 | 9 | 0 | wallstreetbets 12 | NYSE |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xbxqf2/comment/19rh54s6o6fc4/) |
| GOOG | 2026-10-19 22:36 | mention spike | 115 | 21.14 | 73 | 0 | wallstreetbets 115 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xbxqf2/comment/19rh8bfocuexv/) |
| GOOGL | 2026-10-20 18:16 | mention spike | 85 | 24.0 | 42 | 1 | wallstreetbets 85 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xbxqf2/comment/19rh3b408v86b/) |
| IBM | 2026-10-21 18:15 | mention spike | 101 | 2.57 | 71 | 1 | wallstreetbets 100, smallstreetbets 1 | NYSE | #7 | [link](https://www.reddit.com/r/wallstreetbets/comments/1xc8ief/) |
| LRCX | 2026-10-20 16:42 | mention spike | 71 | 4.43 | 47 | 1 | wallstreetbets 71 | Nasdaq | #9 | [link](https://www.reddit.com/r/wallstreetbets/comments/1xbxqf2/comment/19rh6wh3nrtwk/) |
| META | 2026-10-21 11:34 | mention spike | 363 | 33.0 | 197 | 1 | wallstreetbets 362, smallstreetbets 1 | Nasdaq | #2 | [link](https://www.reddit.com/r/wallstreetbets/comments/1xc0ooq/) |
| MRNA | 2026-10-20 23:18 | mention spike | 27 | 10.29 | 17 | 0 | wallstreetbets 26, smallstreetbets 1 | Nasdaq |  | [link](https://www.reddit.com/r/smallstreetbets/comments/1xbxqt6/comment/19rgq98gnz4yr/) |
| MSTR | 2026-10-21 19:47 | mention spike | 15 | 8.29 | 11 | 0 | wallstreetbets 15 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xc0sah/) |
| NOK | 2026-10-22 05:55 | mention spike | 11 | 3.57 | 9 | 0 | wallstreetbets 11 | NYSE | #4 | [link](https://www.reddit.com/r/wallstreetbets/comments/1xceeju/comment/19rh9fw5r7cu9/) |
| RDDT | 2026-10-21 22:45 | mention spike | 25 | 10.57 | 18 | 0 | wallstreetbets 25 | NYSE |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xbxqf2/comment/19rgs7leqb2g2/) |
| SDEV | 2026-10-22 07:27 | mention spike | 12 | 0.29 | 6 | 0 | pennystocks 10, wallstreetbets 2 | NYSE American |  | [link](https://www.reddit.com/r/pennystocks/comments/1xc7pzo/) |
| TSLA | 2026-10-22 07:27 | mention spike | 231 | 84.86 | 145 | 1 | wallstreetbets 229, smallstreetbets 2 | Nasdaq | #8 | [link](https://www.reddit.com/r/wallstreetbets/comments/1xbxty0/) |
| OKLO | 2026-10-20 21:21 | mention spike | 7 | 7.43 | 7 | 0 | wallstreetbets 7 | NYSE |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xbxqf2/comment/19rgue5p772g5/) |
| SPCX | 2026-10-20 10:18 | mention spike | 215 | 94.57 | 128 | 0 | wallstreetbets 212, smallstreetbets 3 | Nasdaq |  | [link](https://www.reddit.com/r/smallstreetbets/comments/1xccjwa/) |
| SMCI | 2026-10-20 21:06 | mention spike | 21 | 18.86 | 15 | 0 | wallstreetbets 21 | Nasdaq | #28 | [link](https://www.reddit.com/r/wallstreetbets/comments/1xbxqf2/comment/19rgtb4iaivq8/) |
| NFLX | 2026-10-19 19:31 | mention spike | 86 | 43.14 | 64 | 0 | wallstreetbets 84, smallstreetbets 2 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xcbbl9/) |
| SLS | 2026-10-21 08:01 | mention spike | 4 | 6.14 | 3 | 1 | wallstreetbets 3, smallstreetbets 1 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xb2ztj/comment/19rg4zp2i1l6t/) |
| PAC | 2026-10-21 02:19 | mention spike | 0 |  | 0 | 0 |  | NYSE |  |  |
| HTZ | 2026-10-20 13:24 | mention spike | 15 | 9.43 | 12 | 0 | wallstreetbets 14, pennystocks 1 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xc1047/) |

Full history: `episodes.csv` (one row per first flag, with the numbers known at that moment).
