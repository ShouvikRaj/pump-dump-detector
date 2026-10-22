# Stage 1 candidates

Updated 2026-10-22T07:27:06Z by run `39739854912`. A candidate is a ticker whose Reddit mentions (or hype-language
posts) in the last 24 hours jumped above its prior 7-day mean + 2 sd, with at least
10 mentions from 5 different authors. It stays listed until it goes
24 hours without a new flag. These are statistical flags, not accusations or advice.

| Ticker | Flagged since (UTC) | Why | Mentions 24h | Baseline/day | Authors | Hype posts | Subreddits | Exchange | StockTwits | Example |
|---|---|---|---|---|---|---|---|---|---|---|
| AMOD | 2026-10-21 16:41 | mention spike | 25 | 0.57 | 10 | 0 | pennystocks 25 | Nasdaq |  | [link](https://www.reddit.com/r/pennystocks/comments/1xbpwyi/) |
| BABA | 2026-10-22 02:50 | mention spike | 11 | 1.29 | 8 | 0 | wallstreetbets 11 | NYSE | #5 | [link](https://www.reddit.com/r/wallstreetbets/comments/1xbxqf2/comment/19rgv47ubc7c5/) |
| GOOG | 2026-10-19 22:36 | mention spike | 111 | 21.0 | 71 | 0 | wallstreetbets 110, smallstreetbets 1 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xcam5g/comment/19rh18y5jm3tt/) |
| GOOGL | 2026-10-20 18:16 | mention spike | 89 | 23.43 | 45 | 1 | wallstreetbets 89 | Nasdaq | #7 | [link](https://www.reddit.com/r/wallstreetbets/comments/1xcam5g/comment/19rh18y5jm3tt/) |
| IBM | 2026-10-21 18:15 | mention spike | 100 | 2.57 | 70 | 1 | wallstreetbets 99, smallstreetbets 1 | NYSE | #9 | [link](https://www.reddit.com/r/wallstreetbets/comments/1xc8ief/) |
| LRCX | 2026-10-20 16:42 | mention spike | 71 | 4.14 | 47 | 1 | wallstreetbets 71 | Nasdaq | #6 | [link](https://www.reddit.com/r/wallstreetbets/comments/1xbxqf2/comment/19rgxy4nahjj8/) |
| META | 2026-10-21 11:34 | mention spike | 346 | 32.43 | 194 | 1 | wallstreetbets 344, smallstreetbets 2 | Nasdaq | #12 | [link](https://www.reddit.com/r/wallstreetbets/comments/1xc0ooq/) |
| MRNA | 2026-10-20 23:18 | mention spike | 27 | 10.43 | 17 | 0 | wallstreetbets 26, smallstreetbets 1 | Nasdaq | #20 | [link](https://www.reddit.com/r/smallstreetbets/comments/1xbxqt6/comment/19rgq98gnz4yr/) |
| MSTR | 2026-10-21 19:47 | mention spike | 15 | 8.29 | 11 | 0 | wallstreetbets 15 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xc0sah/) |
| NOK | 2026-10-22 05:55 | mention spike | 10 | 3.57 | 9 | 0 | wallstreetbets 10 | NYSE | #3 | [link](https://www.reddit.com/r/wallstreetbets/comments/1xbxqf2/comment/19rgwkjba3uhv/) |
| RDDT | 2026-10-21 22:45 | mention spike | 26 | 10.43 | 19 | 0 | wallstreetbets 25, smallstreetbets 1 | NYSE |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xbxqf2/comment/19rgs7leqb2g2/) |
| SDEV | 2026-10-22 07:27 | mention spike | 10 | 0.29 | 6 | 0 | pennystocks 9, wallstreetbets 1 | NYSE American |  | [link](https://www.reddit.com/r/pennystocks/comments/1xc7pzo/) |
| TSLA | 2026-10-22 07:27 | mention spike | 235 | 83.57 | 146 | 1 | wallstreetbets 232, smallstreetbets 3 | Nasdaq | #13 | [link](https://www.reddit.com/r/wallstreetbets/comments/1xbxty0/) |
| OKLO | 2026-10-20 21:21 | mention spike | 8 | 7.29 | 8 | 0 | wallstreetbets 8 | NYSE |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xbxqf2/comment/19rgue5p772g5/) |
| SPCX | 2026-10-20 10:18 | mention spike | 219 | 93.0 | 131 | 0 | wallstreetbets 217, smallstreetbets 2 | Nasdaq |  | [link](https://www.reddit.com/r/smallstreetbets/comments/1xc48w0/) |
| SMCI | 2026-10-20 21:06 | mention spike | 28 | 17.86 | 20 | 0 | wallstreetbets 27, smallstreetbets 1 | Nasdaq | #8 | [link](https://www.reddit.com/r/smallstreetbets/comments/1xbi8mj/) |
| NFLX | 2026-10-19 19:31 | mention spike | 93 | 41.29 | 67 | 0 | wallstreetbets 90, smallstreetbets 3 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xcbbl9/) |
| SLS | 2026-10-21 08:01 | mention spike | 5 | 6.0 | 4 | 1 | wallstreetbets 4, smallstreetbets 1 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xb2ztj/comment/19rg4zp2i1l6t/) |
| PAC | 2026-10-21 02:19 | mention spike | 0 |  | 0 | 0 |  | NYSE |  |  |
| HTZ | 2026-10-20 13:24 | mention spike | 12 | 9.57 | 10 | 0 | wallstreetbets 11, pennystocks 1 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xc1047/) |

Full history: `episodes.csv` (one row per first flag, with the numbers known at that moment).
