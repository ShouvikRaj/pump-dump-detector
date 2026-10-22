# Stage 1 candidates

Updated 2026-10-22T13:19:18Z by run `39785663623`. A candidate is a ticker whose Reddit mentions (or hype-language
posts) in the last 24 hours jumped above its prior 7-day mean + 2 sd, with at least
10 mentions from 5 different authors. It stays listed until it goes
24 hours without a new flag. These are statistical flags, not accusations or advice.

| Ticker | Flagged since (UTC) | Why | Mentions 24h | Baseline/day | Authors | Hype posts | Subreddits | Exchange | StockTwits | Example |
|---|---|---|---|---|---|---|---|---|---|---|
| AMOD | 2026-10-21 16:41 | mention spike | 18 | 1.71 | 9 | 0 | pennystocks 18 | Nasdaq |  | [link](https://www.reddit.com/r/pennystocks/comments/1xbpwyi/) |
| AVEX | 2026-10-22 11:25 | mention spike | 10 | 0.86 | 8 | 0 | wallstreetbets 6, pennystocks 4 | NYSE | #15 | [link](https://www.reddit.com/r/wallstreetbets/comments/1xbyywi/) |
| BABA | 2026-10-22 02:50 | mention spike | 12 | 1.29 | 9 | 0 | wallstreetbets 12 | NYSE |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xbxqf2/comment/19rh54s6o6fc4/) |
| GOOG | 2026-10-19 22:36 | mention spike | 99 | 24.0 | 63 | 0 | wallstreetbets 99 | Nasdaq | #20 | [link](https://www.reddit.com/r/wallstreetbets/comments/1xceeju/comment/19rhfgwxbo1c5/) |
| GOOGL | 2026-10-20 18:16 | mention spike | 85 | 24.86 | 42 | 1 | wallstreetbets 85 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xceeju/comment/19rhfbn5gdneq/) |
| IBM | 2026-10-21 18:15 | mention spike | 106 | 2.57 | 74 | 1 | wallstreetbets 105, smallstreetbets 1 | NYSE | #4 | [link](https://www.reddit.com/r/wallstreetbets/comments/1xc8ief/) |
| LRCX | 2026-10-20 16:42 | mention spike | 79 | 4.29 | 50 | 1 | wallstreetbets 79 | Nasdaq | #7 | [link](https://www.reddit.com/r/wallstreetbets/comments/1xceeju/comment/19rhh20nxlbr8/) |
| META | 2026-10-21 11:34 | mention spike | 381 | 34.29 | 207 | 1 | wallstreetbets 380, smallstreetbets 1 | Nasdaq | #1 | [link](https://www.reddit.com/r/wallstreetbets/comments/1xc0ooq/) |
| MRNA | 2026-10-20 23:18 | mention spike | 29 | 10.29 | 18 | 0 | wallstreetbets 28, smallstreetbets 1 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xceeju/comment/19rhg4ywteh8g/) |
| MSTR | 2026-10-21 19:47 | mention spike | 19 | 8.29 | 13 | 0 | wallstreetbets 19 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xc0sah/) |
| NOK | 2026-10-22 05:55 | mention spike | 16 | 3.86 | 12 | 0 | wallstreetbets 16 | NYSE | #2 | [link](https://www.reddit.com/r/wallstreetbets/comments/1xceeju/comment/19rhgnjms25dw/) |
| RDDT | 2026-10-21 22:45 | mention spike | 25 | 10.71 | 19 | 0 | wallstreetbets 25 | NYSE |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xceeju/comment/19rhfx80z0kox/) |
| SDEV | 2026-10-22 07:27 | mention spike | 13 | 0.29 | 7 | 0 | pennystocks 11, wallstreetbets 2 | NYSE American |  | [link](https://www.reddit.com/r/pennystocks/comments/1xc7pzo/) |
| TSLA | 2026-10-22 07:27 | mention spike | 232 | 86.0 | 142 | 1 | wallstreetbets 230, smallstreetbets 2 | Nasdaq | #8 | [link](https://www.reddit.com/r/wallstreetbets/comments/1xbxty0/) |
| OKLO | 2026-10-20 21:21 | mention spike | 6 | 7.57 | 6 | 0 | wallstreetbets 6 | NYSE |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xbxqf2/comment/19rgue5p772g5/) |
| SPCX | 2026-10-20 10:18 | mention spike | 199 | 98.29 | 113 | 0 | wallstreetbets 196, smallstreetbets 3 | Nasdaq |  | [link](https://www.reddit.com/r/smallstreetbets/comments/1xccjwa/) |
| SMCI | 2026-10-20 21:06 | mention spike | 20 | 19.43 | 13 | 0 | wallstreetbets 20 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xceeju/comment/19rhfxdbxr4ck/) |
| NFLX | 2026-10-19 19:31 | mention spike | 72 | 46.43 | 54 | 0 | wallstreetbets 70, smallstreetbets 2 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xcbbl9/) |
| SLS | 2026-10-21 08:01 | mention spike | 6 | 6.14 | 5 | 1 | wallstreetbets 5, smallstreetbets 1 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xceeju/comment/19rhgetx550ow/) |
| PAC | 2026-10-21 02:19 | mention spike | 0 |  | 0 | 0 |  | NYSE |  |  |

Full history: `episodes.csv` (one row per first flag, with the numbers known at that moment).
