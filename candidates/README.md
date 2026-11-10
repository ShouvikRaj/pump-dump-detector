# Stage 1 candidates

Updated 2026-11-10T20:00:10Z by run `42889349741`. A candidate is a ticker whose Reddit mentions (or hype-language
posts) in the last 24 hours jumped above its prior 7-day mean + 2 sd, with at least
10 mentions from 5 different authors. It stays listed until it goes
24 hours without a new flag. These are statistical flags, not accusations or advice.

| Ticker | Flagged since (UTC) | Why | Mentions 24h | Baseline/day | Authors | Hype posts | Subreddits | Exchange | StockTwits | Example |
|---|---|---|---|---|---|---|---|---|---|---|
| ANT | 2026-11-10 14:52 | mention spike | 93 | 23.29 | 64 | 0 | wallstreetbets 93 | ? |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xsnad5/) |
| ASTS | 2026-11-09 22:33 | mention spike | 96 | 41.43 | 66 | 1 | wallstreetbets 96 | Nasdaq | #4 | [link](https://www.reddit.com/r/wallstreetbets/comments/1xsk1rq/comment/19sfv24lwghkz/) |
| AVGO | 2026-11-09 15:56 | mention spike | 32 | 13.0 | 25 | 0 | wallstreetbets 32 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xs3lzi/comment/19sfurxoc62qp/) |
| GLD | 2026-11-10 17:08 | mention spike | 15 | 6.43 | 5 | 0 | wallstreetbets 15 | NYSE Arca | #12 | [link](https://www.reddit.com/r/wallstreetbets/comments/1xsk1rq/comment/19sfstj51nldw/) |
| HIMS | 2026-11-09 21:25 | mention spike | 23 | 2.57 | 20 | 0 | wallstreetbets 23 | NYSE | #3 | [link](https://www.reddit.com/r/wallstreetbets/comments/1xsv7pt/) |
| IVF | 2026-11-09 22:18 | mention spike | 12 | 1.29 | 12 | 0 | wallstreetbets 11, smallstreetbets 1 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xs4ayj/comment/19se9z81pfzxg/) |
| MSTR | 2026-11-10 19:20 | mention spike | 11 | 4.71 | 8 | 0 | wallstreetbets 11 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xsp9vp/) |
| OMH | 2026-11-09 20:48 | mention spike | 18 | 2.43 | 12 | 0 | wallstreetbets 11, pennystocks 7 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xsk1rq/comment/19sfpns8tsdms/) |
| RKLB | 2026-11-09 21:25 | mention spike | 143 | 23.0 | 81 | 2 | wallstreetbets 143 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xsprrz/) |
| TTD | 2026-11-09 21:11 | mention spike | 44 | 3.14 | 33 | 0 | wallstreetbets 44 | Nasdaq | #7 | [link](https://www.reddit.com/r/wallstreetbets/comments/1xsv7pt/) |
| TTWO | 2026-11-10 16:24 | mention spike | 30 | 9.57 | 22 | 0 | wallstreetbets 30 | Nasdaq | #19 | [link](https://www.reddit.com/r/wallstreetbets/comments/1xsuaol/comment/19sft4lz50lqa/) |
| CRWV | 2026-11-10 20:00 | mention spike | 67 | 31.43 | 52 | 0 | wallstreetbets 66, smallstreetbets 1 | Nasdaq |  | [link](https://www.reddit.com/r/smallstreetbets/comments/1xs72bz/) |
| GEV | 2026-11-10 15:44 | mention spike | 11 | 3.0 | 8 | 0 | wallstreetbets 11 | NYSE |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xsk1rq/comment/19sfjsbn95lhe/) |
| CVS | 2026-11-09 13:52 | mention spike | 6 | 3.0 | 6 | 0 | wallstreetbets 6 | NYSE |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xrfbie/comment/19sf8vuyo16rp/) |
| NVDA | 2026-11-09 00:16 | mention spike | 1114 | 346.14 | 619 | 0 | wallstreetbets 1105, smallstreetbets 9 | Nasdaq | #1 | [link](https://www.reddit.com/r/wallstreetbets/comments/1xswibo/) |
| NYT | 2026-11-09 11:01 | mention spike | 11 | 3.14 | 11 | 0 | wallstreetbets 10, smallstreetbets 1 | NYSE |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xsq1s1/) |
| NNN | 2026-11-09 15:04 | mention spike | 10 | 6.0 | 8 | 0 | wallstreetbets 9, smallstreetbets 1 | NYSE |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xsct7h/) |
| ASML | 2026-11-09 22:18 | mention spike | 5 | 3.43 | 4 | 0 | wallstreetbets 4, smallstreetbets 1 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xspyjp/comment/19sft4qlr8uf4/) |
| ONDS | 2026-11-09 20:48 | mention spike | 4 | 4.57 | 4 | 0 | wallstreetbets 4 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xsk1rq/comment/19sfrbhlipyiq/) |
| MSS | 2026-11-09 23:23 | mention spike | 6 | 1.0 | 4 | 0 | wallstreetbets 5, smallstreetbets 1 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xsk1rq/comment/19sfrdz4m7cht/) |

Full history: `episodes.csv` (one row per first flag, with the numbers known at that moment).
