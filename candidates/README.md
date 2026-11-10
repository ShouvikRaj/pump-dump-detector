# Stage 1 candidates

Updated 2026-11-10T11:05:10Z by run `42803678391`. A candidate is a ticker whose Reddit mentions (or hype-language
posts) in the last 24 hours jumped above its prior 7-day mean + 2 sd, with at least
10 mentions from 5 different authors. It stays listed until it goes
24 hours without a new flag. These are statistical flags, not accusations or advice.

| Ticker | Flagged since (UTC) | Why | Mentions 24h | Baseline/day | Authors | Hype posts | Subreddits | Exchange | StockTwits | Example |
|---|---|---|---|---|---|---|---|---|---|---|
| ASTS | 2026-11-09 22:33 | mention spike | 88 | 39.86 | 58 | 0 | wallstreetbets 88 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xs3lzi/comment/19sf7d0xvii5d/) |
| CVS | 2026-11-09 13:52 | mention spike | 15 | 1.57 | 14 | 0 | wallstreetbets 15 | NYSE |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xrfbie/comment/19sei8viswold/) |
| HIMS | 2026-11-09 21:25 | mention spike | 19 | 1.71 | 15 | 0 | wallstreetbets 19 | NYSE | #2 | [link](https://www.reddit.com/r/wallstreetbets/comments/1xs3lzi/comment/19sf5qxfv663p/) |
| IVF | 2026-11-09 22:18 | mention spike | 16 | 0.71 | 16 | 0 | wallstreetbets 15, smallstreetbets 1 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xs4ayj/comment/19se9z81pfzxg/) |
| NVDA | 2026-11-09 00:16 | mention spike | 1067 | 250.71 | 614 | 0 | wallstreetbets 1052, smallstreetbets 15 | Nasdaq | #20 | [link](https://www.reddit.com/r/smallstreetbets/comments/1xsfg6v/) |
| OMH | 2026-11-09 20:48 | mention spike | 16 | 1.14 | 14 | 0 | wallstreetbets 9, pennystocks 7 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xs3lzi/comment/19sebk3yv28o4/) |
| RKLB | 2026-11-09 21:25 | mention spike | 130 | 21.29 | 72 | 2 | wallstreetbets 130 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xsdy48/) |
| TTD | 2026-11-09 21:11 | mention spike | 42 | 2.0 | 28 | 0 | wallstreetbets 42 | Nasdaq | #1 | [link](https://www.reddit.com/r/wallstreetbets/comments/1xs3lzi/comment/19sei2raj6cf9/) |
| NNN | 2026-11-09 15:04 | mention spike | 11 | 5.71 | 8 | 0 | wallstreetbets 11 | NYSE |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xsct7h/) |
| NYT | 2026-11-09 11:01 | mention spike | 8 | 2.43 | 8 | 0 | wallstreetbets 8 | NYSE |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xrrwsf/) |
| ASML | 2026-11-09 22:18 | mention spike | 3 | 3.14 | 3 | 0 | wallstreetbets 2, smallstreetbets 1 | Nasdaq |  | [link](https://www.reddit.com/r/smallstreetbets/comments/1xrurrh/comment/19se8zgthwtlv/) |
| ONDS | 2026-11-09 20:48 | mention spike | 9 | 3.71 | 6 | 0 | wallstreetbets 8, pennystocks 1 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xs3lzi/comment/19sejep6ua8gy/) |
| MSS | 2026-11-09 23:23 | mention spike | 5 | 0.86 | 3 | 0 | wallstreetbets 5 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xs3lzi/comment/19selz71ip5r4/) |
| AVGO | 2026-11-09 15:56 | mention spike | 16 | 13.0 | 14 | 0 | wallstreetbets 16 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xsjfsh/comment/19sf6b47ow4lc/) |

Full history: `episodes.csv` (one row per first flag, with the numbers known at that moment).
