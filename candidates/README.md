# Stage 1 candidates

Updated 2026-11-09T22:18:11Z by run `42709262782`. A candidate is a ticker whose Reddit mentions (or hype-language
posts) in the last 24 hours jumped above its prior 7-day mean + 2 sd, with at least
10 mentions from 5 different authors. It stays listed until it goes
24 hours without a new flag. These are statistical flags, not accusations or advice.

| Ticker | Flagged since (UTC) | Why | Mentions 24h | Baseline/day | Authors | Hype posts | Subreddits | Exchange | StockTwits | Example |
|---|---|---|---|---|---|---|---|---|---|---|
| CVS | 2026-11-09 13:52 | mention spike | 18 | 0.86 | 16 | 0 | wallstreetbets 18 | NYSE |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xrfbie/) |
| HIMS | 2026-11-09 21:25 | mention spike | 16 | 1.57 | 12 | 0 | wallstreetbets 16 | NYSE | #3 | [link](https://www.reddit.com/r/wallstreetbets/comments/1xs3lzi/comment/19se715rmacf7/) |
| NNN | 2026-11-09 15:04 | mention spike | 15 | 4.86 | 14 | 0 | wallstreetbets 15 | NYSE |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xraj53/comment/19sdtwmumgskg/) |
| NVDA | 2026-11-09 00:16 | mention spike | 1330 | 169.14 | 724 | 0 | wallstreetbets 1312, smallstreetbets 18 | Nasdaq | #10 | [link](https://www.reddit.com/r/wallstreetbets/comments/1xs3min/) |
| NYT | 2026-11-09 11:01 | mention spike | 14 | 1.14 | 12 | 0 | wallstreetbets 14 | NYSE |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xrrwsf/) |
| OMH | 2026-11-09 20:48 | mention spike | 14 | 1.14 | 12 | 0 | pennystocks 7, wallstreetbets 7 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xs3lzi/comment/19se75798vplw/) |
| ONDS | 2026-11-09 20:48 | mention spike | 10 | 3.43 | 6 | 0 | wallstreetbets 9, pennystocks 1 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xrot48/comment/19se49e8ob9nm/) |
| RKLB | 2026-11-09 21:25 | mention spike | 92 | 22.71 | 56 | 1 | wallstreetbets 92 | Nasdaq | #4 | [link](https://www.reddit.com/r/wallstreetbets/comments/1xs3lzi/comment/19se8ygrinsrp/) |
| TTD | 2026-11-09 21:11 | mention spike | 25 | 1.86 | 17 | 0 | wallstreetbets 25 | Nasdaq | #2 | [link](https://www.reddit.com/r/wallstreetbets/comments/1xrot48/comment/19se78edbfsmb/) |
| ASML | 2026-11-09 22:18 | mention spike | 10 | 2.14 | 9 | 0 | wallstreetbets 9, smallstreetbets 1 | Nasdaq |  | [link](https://www.reddit.com/r/smallstreetbets/comments/1xrurrh/comment/19se8zgthwtlv/) |
| IVF | 2026-11-09 22:18 | mention spike | 12 | 0.57 | 12 | 0 | wallstreetbets 11, smallstreetbets 1 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xs4ayj/comment/19se8xzgzppk5/) |
| AVGO | 2026-11-09 15:56 | mention spike | 20 | 12.43 | 17 | 0 | wallstreetbets 20 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xrot48/comment/19se5olbyx6lc/) |

Full history: `episodes.csv` (one row per first flag, with the numbers known at that moment).
