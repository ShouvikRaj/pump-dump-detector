# Stage 1 candidates

Updated 2026-10-22T13:59:14Z by run `39791613613`. A candidate is a ticker whose Reddit mentions (or hype-language
posts) in the last 24 hours jumped above its prior 7-day mean + 2 sd, with at least
10 mentions from 5 different authors. It stays listed until it goes
24 hours without a new flag. These are statistical flags, not accusations or advice.

| Ticker | Flagged since (UTC) | Why | Mentions 24h | Baseline/day | Authors | Hype posts | Subreddits | Exchange | StockTwits | Example |
|---|---|---|---|---|---|---|---|---|---|---|
| AMOD | 2026-10-21 16:41 | mention spike | 17 | 1.86 | 9 | 0 | pennystocks 17 | Nasdaq |  | [link](https://www.reddit.com/r/pennystocks/comments/1xbpwyi/) |
| AVEX | 2026-10-22 11:25 | mention spike | 10 | 0.86 | 8 | 0 | wallstreetbets 6, pennystocks 4 | NYSE | #18 | [link](https://www.reddit.com/r/wallstreetbets/comments/1xbyywi/) |
| BABA | 2026-10-22 02:50 | mention spike | 12 | 1.29 | 9 | 0 | wallstreetbets 12 | NYSE |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xbxqf2/comment/19rh54s6o6fc4/) |
| GOOG | 2026-10-19 22:36 | mention spike | 87 | 25.57 | 57 | 0 | wallstreetbets 87 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xceeju/comment/19rhj13v7rcn8/) |
| GOOGL | 2026-10-20 18:16 | mention spike | 79 | 26.14 | 39 | 1 | wallstreetbets 79 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xceeju/comment/19rhj3jwxnumd/) |
| IBM | 2026-10-21 18:15 | mention spike | 116 | 2.71 | 83 | 1 | wallstreetbets 115, smallstreetbets 1 | NYSE | #3 | [link](https://www.reddit.com/r/wallstreetbets/comments/1xc8ief/) |
| LRCX | 2026-10-20 16:42 | mention spike | 80 | 4.29 | 50 | 1 | wallstreetbets 80 | Nasdaq | #7 | [link](https://www.reddit.com/r/wallstreetbets/comments/1xceeju/comment/19rhip2iqnr9d/) |
| META | 2026-10-21 11:34 | mention spike | 421 | 35.29 | 230 | 1 | wallstreetbets 420, smallstreetbets 1 | Nasdaq | #1 | [link](https://www.reddit.com/r/wallstreetbets/comments/1xciuk0/) |
| MRNA | 2026-10-20 23:18 | mention spike | 28 | 10.43 | 17 | 0 | wallstreetbets 27, smallstreetbets 1 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xceeju/comment/19rhg4ywteh8g/) |
| MSTR | 2026-10-21 19:47 | mention spike | 19 | 8.43 | 13 | 0 | wallstreetbets 19 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xc0sah/) |
| NOK | 2026-10-22 05:55 | mention spike | 20 | 3.86 | 15 | 0 | wallstreetbets 20 | NYSE | #2 | [link](https://www.reddit.com/r/wallstreetbets/comments/1xceeju/comment/19rhizpnlqklg/) |
| RDDT | 2026-10-21 22:45 | mention spike | 26 | 10.71 | 18 | 0 | wallstreetbets 26 | NYSE |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xceeju/comment/19rhj0fcrvp38/) |
| SDEV | 2026-10-22 07:27 | mention spike | 13 | 0.29 | 7 | 0 | pennystocks 11, wallstreetbets 2 | NYSE American |  | [link](https://www.reddit.com/r/pennystocks/comments/1xc7pzo/) |
| TSLA | 2026-10-22 07:27 | mention spike | 236 | 87.29 | 141 | 1 | wallstreetbets 234, smallstreetbets 2 | Nasdaq | #15 | [link](https://www.reddit.com/r/wallstreetbets/comments/1xbxty0/) |
| OKLO | 2026-10-20 21:21 | mention spike | 6 | 7.57 | 6 | 0 | wallstreetbets 6 | NYSE |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xbxqf2/comment/19rgue5p772g5/) |
| SPCX | 2026-10-20 10:18 | mention spike | 178 | 102.86 | 99 | 0 | wallstreetbets 174, smallstreetbets 4 | Nasdaq |  | [link](https://www.reddit.com/r/smallstreetbets/comments/1xcit0a/) |
| SMCI | 2026-10-20 21:06 | mention spike | 18 | 20.0 | 14 | 0 | wallstreetbets 18 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xceeju/comment/19rhi0yrd0szn/) |
| NFLX | 2026-10-19 19:31 | mention spike | 73 | 47.57 | 51 | 0 | wallstreetbets 71, smallstreetbets 2 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xcbbl9/) |
| SLS | 2026-10-21 08:01 | mention spike | 6 | 6.14 | 5 | 1 | wallstreetbets 5, smallstreetbets 1 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xceeju/comment/19rhgetx550ow/) |
| PAC | 2026-10-21 02:19 | mention spike | 0 |  | 0 | 0 |  | NYSE |  |  |

Full history: `episodes.csv` (one row per first flag, with the numbers known at that moment).
