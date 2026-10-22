# Stage 1 candidates

Updated 2026-10-22T05:29:09Z by run `39727579093`. A candidate is a ticker whose Reddit mentions (or hype-language
posts) in the last 24 hours jumped above its prior 7-day mean + 2 sd, with at least
10 mentions from 5 different authors. It stays listed until it goes
24 hours without a new flag. These are statistical flags, not accusations or advice.

| Ticker | Flagged since (UTC) | Why | Mentions 24h | Baseline/day | Authors | Hype posts | Subreddits | Exchange | StockTwits | Example |
|---|---|---|---|---|---|---|---|---|---|---|
| AMOD | 2026-10-21 16:41 | mention spike | 25 | 0.57 | 10 | 0 | pennystocks 25 | Nasdaq |  | [link](https://www.reddit.com/r/pennystocks/comments/1xbpwyi/) |
| BABA | 2026-10-22 02:50 | mention spike | 11 | 1.29 | 8 | 0 | wallstreetbets 11 | NYSE | #4 | [link](https://www.reddit.com/r/wallstreetbets/comments/1xbxqf2/comment/19rgv47ubc7c5/) |
| GOOG | 2026-10-19 22:36 | mention spike | 110 | 20.43 | 69 | 0 | wallstreetbets 109, smallstreetbets 1 | Nasdaq | #27 | [link](https://www.reddit.com/r/wallstreetbets/comments/1xbxqf2/comment/19rgtgda213qa/) |
| GOOGL | 2026-10-20 18:16 | mention spike | 86 | 23.43 | 43 | 1 | wallstreetbets 86 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xbdbqm/comment/19rgtswlw22ww/) |
| IBM | 2026-10-21 18:15 | mention spike | 95 | 2.57 | 65 | 1 | wallstreetbets 94, smallstreetbets 1 | NYSE | #13 | [link](https://www.reddit.com/r/wallstreetbets/comments/1xc8ief/) |
| LRCX | 2026-10-20 16:42 | mention spike | 68 | 4.14 | 44 | 1 | wallstreetbets 68 | Nasdaq | #6 | [link](https://www.reddit.com/r/wallstreetbets/comments/1xbxqf2/comment/19rgvbx3av8kj/) |
| META | 2026-10-21 11:34 | mention spike | 339 | 32.43 | 190 | 1 | wallstreetbets 337, smallstreetbets 2 | Nasdaq | #3 | [link](https://www.reddit.com/r/wallstreetbets/comments/1xc0ooq/) |
| MRNA | 2026-10-20 23:18 | mention spike | 29 | 10.14 | 19 | 0 | wallstreetbets 28, smallstreetbets 1 | Nasdaq |  | [link](https://www.reddit.com/r/smallstreetbets/comments/1xbxqt6/comment/19rgq98gnz4yr/) |
| MSTR | 2026-10-21 19:47 | mention spike | 16 | 8.14 | 12 | 0 | wallstreetbets 16 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xc0sah/) |
| RDDT | 2026-10-21 22:45 | mention spike | 26 | 10.43 | 19 | 0 | wallstreetbets 25, smallstreetbets 1 | NYSE |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xbxqf2/comment/19rgs7leqb2g2/) |
| OKLO | 2026-10-20 21:21 | mention spike | 8 | 7.29 | 8 | 0 | wallstreetbets 8 | NYSE |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xbxqf2/comment/19rgue5p772g5/) |
| SPCX | 2026-10-20 10:18 | mention spike | 228 | 91.29 | 132 | 0 | wallstreetbets 226, smallstreetbets 2 | Nasdaq |  | [link](https://www.reddit.com/r/smallstreetbets/comments/1xc48w0/) |
| SMCI | 2026-10-20 21:06 | mention spike | 30 | 17.57 | 21 | 0 | wallstreetbets 29, smallstreetbets 1 | Nasdaq | #8 | [link](https://www.reddit.com/r/smallstreetbets/comments/1xbi8mj/) |
| NFLX | 2026-10-19 19:31 | mention spike | 94 | 41.14 | 68 | 0 | wallstreetbets 91, smallstreetbets 3 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xbqi72/) |
| SLS | 2026-10-21 08:01 | mention spike | 5 | 6.0 | 4 | 1 | wallstreetbets 4, smallstreetbets 1 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xb2ztj/comment/19rg4zp2i1l6t/) |
| PAC | 2026-10-21 02:19 | mention spike | 0 |  | 0 | 0 |  | NYSE |  |  |
| HTZ | 2026-10-20 13:24 | mention spike | 13 | 9.43 | 11 | 0 | wallstreetbets 12, pennystocks 1 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xc1047/) |

Full history: `episodes.csv` (one row per first flag, with the numbers known at that moment).
