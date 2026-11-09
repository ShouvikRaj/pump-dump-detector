# Stage 1 candidates

Updated 2026-11-09T22:44:06Z by run `42713340701`. A candidate is a ticker whose Reddit mentions (or hype-language
posts) in the last 24 hours jumped above its prior 7-day mean + 2 sd, with at least
10 mentions from 5 different authors. It stays listed until it goes
24 hours without a new flag. These are statistical flags, not accusations or advice.

| Ticker | Flagged since (UTC) | Why | Mentions 24h | Baseline/day | Authors | Hype posts | Subreddits | Exchange | StockTwits | Example |
|---|---|---|---|---|---|---|---|---|---|---|
| ASML | 2026-11-09 22:18 | mention spike | 10 | 2.14 | 9 | 0 | wallstreetbets 9, smallstreetbets 1 | Nasdaq |  | [link](https://www.reddit.com/r/smallstreetbets/comments/1xrurrh/comment/19se8zgthwtlv/) |
| ASTS | 2026-11-09 22:33 | mention spike | 78 | 39.43 | 50 | 0 | wallstreetbets 78 | Nasdaq | #1 | [link](https://www.reddit.com/r/wallstreetbets/comments/1xs3lzi/comment/19se9nju2djs2/) |
| CVS | 2026-11-09 13:52 | mention spike | 18 | 0.86 | 16 | 0 | wallstreetbets 18 | NYSE |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xrfbie/) |
| HIMS | 2026-11-09 21:25 | mention spike | 17 | 1.57 | 13 | 0 | wallstreetbets 17 | NYSE | #3 | [link](https://www.reddit.com/r/wallstreetbets/comments/1xs3lzi/comment/19se715rmacf7/) |
| IVF | 2026-11-09 22:18 | mention spike | 16 | 0.57 | 16 | 0 | wallstreetbets 15, smallstreetbets 1 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xs4ayj/comment/19se9z81pfzxg/) |
| NNN | 2026-11-09 15:04 | mention spike | 14 | 5.0 | 13 | 0 | wallstreetbets 14 | NYSE |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xraj53/comment/19sdtwmumgskg/) |
| NVDA | 2026-11-09 00:16 | mention spike | 1387 | 174.71 | 738 | 0 | wallstreetbets 1369, smallstreetbets 18 | Nasdaq | #10 | [link](https://www.reddit.com/r/wallstreetbets/comments/1xs5swp/) |
| NYT | 2026-11-09 11:01 | mention spike | 13 | 1.29 | 11 | 0 | wallstreetbets 13 | NYSE |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xrrwsf/) |
| OMH | 2026-11-09 20:48 | mention spike | 15 | 1.14 | 13 | 0 | wallstreetbets 8, pennystocks 7 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xs3lzi/comment/19se75798vplw/) |
| ONDS | 2026-11-09 20:48 | mention spike | 10 | 3.43 | 6 | 0 | wallstreetbets 9, pennystocks 1 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xrot48/comment/19se49e8ob9nm/) |
| RKLB | 2026-11-09 21:25 | mention spike | 110 | 22.71 | 61 | 1 | wallstreetbets 110 | Nasdaq | #6 | [link](https://www.reddit.com/r/wallstreetbets/comments/1xs3lzi/comment/19seab5h3a541/) |
| TTD | 2026-11-09 21:11 | mention spike | 29 | 1.86 | 20 | 0 | wallstreetbets 29 | Nasdaq | #2 | [link](https://www.reddit.com/r/wallstreetbets/comments/1xs3lzi/comment/19se9jmd4wfol/) |
| AVGO | 2026-11-09 15:56 | mention spike | 21 | 12.43 | 18 | 0 | wallstreetbets 21 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xs3lzi/comment/19se9cvgmuyck/) |

Full history: `episodes.csv` (one row per first flag, with the numbers known at that moment).
