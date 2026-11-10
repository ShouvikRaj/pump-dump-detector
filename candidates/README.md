# Stage 1 candidates

Updated 2026-11-10T20:23:06Z by run `42893823069`. A candidate is a ticker whose Reddit mentions (or hype-language
posts) in the last 24 hours jumped above its prior 7-day mean + 2 sd, with at least
10 mentions from 5 different authors. It stays listed until it goes
24 hours without a new flag. These are statistical flags, not accusations or advice.

| Ticker | Flagged since (UTC) | Why | Mentions 24h | Baseline/day | Authors | Hype posts | Subreddits | Exchange | StockTwits | Example |
|---|---|---|---|---|---|---|---|---|---|---|
| ANT | 2026-11-10 14:52 | mention spike | 95 | 23.29 | 65 | 0 | wallstreetbets 95 | ? |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xsnad5/) |
| ASTS | 2026-11-09 22:33 | mention spike | 94 | 41.0 | 66 | 1 | wallstreetbets 94 | Nasdaq | #6 | [link](https://www.reddit.com/r/wallstreetbets/comments/1xsk1rq/comment/19sfv24lwghkz/) |
| AVGO | 2026-11-09 15:56 | mention spike | 32 | 13.0 | 25 | 0 | wallstreetbets 32 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xs3lzi/comment/19sfurxoc62qp/) |
| CRWV | 2026-11-10 20:00 | mention spike | 82 | 31.29 | 59 | 0 | wallstreetbets 81, smallstreetbets 1 | Nasdaq | #15 | [link](https://www.reddit.com/r/smallstreetbets/comments/1xs72bz/) |
| GEV | 2026-11-10 15:44 | mention spike | 12 | 3.0 | 9 | 0 | wallstreetbets 12 | NYSE |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xsk1rq/comment/19sfvf3f5u0w4/) |
| HIMS | 2026-11-09 21:25 | mention spike | 23 | 2.57 | 20 | 0 | wallstreetbets 23 | NYSE | #3 | [link](https://www.reddit.com/r/wallstreetbets/comments/1xsv7pt/) |
| IVF | 2026-11-09 22:18 | mention spike | 12 | 1.29 | 12 | 0 | wallstreetbets 11, smallstreetbets 1 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xs4ayj/comment/19se9z81pfzxg/) |
| MSTR | 2026-11-10 19:20 | mention spike | 11 | 4.57 | 8 | 0 | wallstreetbets 11 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xsp9vp/) |
| OMH | 2026-11-09 20:48 | mention spike | 17 | 2.57 | 11 | 0 | wallstreetbets 11, pennystocks 6 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xsk1rq/comment/19sfpns8tsdms/) |
| RKLB | 2026-11-09 21:25 | mention spike | 142 | 23.29 | 80 | 2 | wallstreetbets 142 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xsprrz/) |
| TTD | 2026-11-09 21:11 | mention spike | 44 | 3.14 | 33 | 0 | wallstreetbets 44 | Nasdaq | #9 | [link](https://www.reddit.com/r/wallstreetbets/comments/1xsv7pt/) |
| TTWO | 2026-11-10 16:24 | mention spike | 31 | 9.57 | 22 | 0 | wallstreetbets 31 | Nasdaq | #8 | [link](https://www.reddit.com/r/wallstreetbets/comments/1xsk1rq/comment/19sfviu3s8ni9/) |
| GLD | 2026-11-10 17:08 | mention spike | 13 | 6.71 | 4 | 0 | wallstreetbets 13 | NYSE Arca | #29 | [link](https://www.reddit.com/r/wallstreetbets/comments/1xsk1rq/comment/19sfstj51nldw/) |
| CVS | 2026-11-09 13:52 | mention spike | 6 | 3.0 | 6 | 0 | wallstreetbets 6 | NYSE |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xrfbie/comment/19sf8vuyo16rp/) |
| NVDA | 2026-11-09 00:16 | mention spike | 1166 | 347.86 | 629 | 1 | wallstreetbets 1157, smallstreetbets 9 | Nasdaq | #1 | [link](https://www.reddit.com/r/wallstreetbets/comments/1xswibo/) |
| NYT | 2026-11-09 11:01 | mention spike | 11 | 3.14 | 11 | 0 | wallstreetbets 10, smallstreetbets 1 | NYSE |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xsq1s1/) |
| NNN | 2026-11-09 15:04 | mention spike | 10 | 6.0 | 8 | 0 | wallstreetbets 9, smallstreetbets 1 | NYSE |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xsct7h/) |
| ASML | 2026-11-09 22:18 | mention spike | 5 | 3.43 | 4 | 0 | wallstreetbets 4, smallstreetbets 1 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xspyjp/comment/19sft4qlr8uf4/) |
| ONDS | 2026-11-09 20:48 | mention spike | 3 | 4.71 | 3 | 0 | wallstreetbets 3 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xsk1rq/comment/19sfrbhlipyiq/) |
| MSS | 2026-11-09 23:23 | mention spike | 6 | 1.0 | 4 | 0 | wallstreetbets 5, smallstreetbets 1 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xsk1rq/comment/19sfrdz4m7cht/) |

Full history: `episodes.csv` (one row per first flag, with the numbers known at that moment).
