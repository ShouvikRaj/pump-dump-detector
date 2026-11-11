# Stage 1 candidates

Updated 2026-11-11T15:01:07Z by run `43042566947`. A candidate is a ticker whose Reddit mentions (or hype-language
posts) in the last 24 hours jumped above its prior 7-day mean + 2 sd, with at least
10 mentions from 5 different authors. It stays listed until it goes
24 hours without a new flag. These are statistical flags, not accusations or advice.

| Ticker | Flagged since (UTC) | Why | Mentions 24h | Baseline/day | Authors | Hype posts | Subreddits | Exchange | StockTwits | Example |
|---|---|---|---|---|---|---|---|---|---|---|
| ANT | 2026-11-10 14:52 | mention spike | 110 | 29.71 | 78 | 0 | wallstreetbets 110 | ? |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xt1f1n/) |
| AVGO | 2026-11-09 15:56 | mention spike | 38 | 14.43 | 27 | 0 | wallstreetbets 38 | Nasdaq | #16 | [link](https://www.reddit.com/r/wallstreetbets/comments/1xtexaq/comment/19sh9jy1q3nq9/) |
| CRWV | 2026-11-10 20:00 | mention spike | 453 | 32.0 | 214 | 3 | wallstreetbets 452, smallstreetbets 1 | Nasdaq | #5 | [link](https://www.reddit.com/r/smallstreetbets/comments/1xtf57a/) |
| MSTR | 2026-11-10 19:20 | mention spike | 12 | 4.86 | 9 | 0 | wallstreetbets 12 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xsp9vp/) |
| NBIS | 2026-11-11 12:32 | mention spike | 127 | 47.0 | 81 | 0 | wallstreetbets 127 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xt2u2d/) |
| NVDA | 2026-11-09 00:16 | mention spike | 1363 | 404.29 | 674 | 4 | wallstreetbets 1352, smallstreetbets 11 | Nasdaq | #11 | [link](https://www.reddit.com/r/wallstreetbets/comments/1xtiwzd/) |
| RGTI | 2026-11-10 21:21 | mention spike | 16 | 2.71 | 11 | 0 | wallstreetbets 16 | Nasdaq | #4 | [link](https://www.reddit.com/r/wallstreetbets/comments/1xsyjq5/comment/19sg6obswrnup/) |
| NVDL | 2026-11-11 07:39 | mention spike | 8 | 2.14 | 7 | 0 | wallstreetbets 8 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xt33ld/comment/19sh3biroe1tx/) |
| GEV | 2026-11-10 15:44 | mention spike | 11 | 4.43 | 7 | 0 | wallstreetbets 11 | NYSE |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xtexaq/comment/19sh8z718rjs5/) |
| TTD | 2026-11-09 21:11 | mention spike | 2 | 9.29 | 2 | 0 | wallstreetbets 2 | Nasdaq | #23 | [link](https://www.reddit.com/r/wallstreetbets/comments/1xsv7pt/) |
| IVF | 2026-11-09 22:18 | mention spike | 0 |  | 0 | 0 |  | Nasdaq |  |  |
| RKLB | 2026-11-09 21:25 | mention spike | 52 | 38.29 | 36 | 0 | wallstreetbets 49, pennystocks 2, smallstreetbets 1 | Nasdaq |  | [link](https://www.reddit.com/r/pennystocks/comments/1xtjd2t/) |
| ASTS | 2026-11-09 22:33 | mention spike | 62 | 45.14 | 41 | 1 | wallstreetbets 62 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xtexaq/comment/19sh8v1iebowz/) |
| OMH | 2026-11-09 20:48 | mention spike | 15 | 3.86 | 11 | 0 | pennystocks 8, wallstreetbets 7 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xt1asn/) |
| TTWO | 2026-11-10 16:24 | mention spike | 21 | 12.57 | 19 | 0 | wallstreetbets 21 | Nasdaq | #18 | [link](https://www.reddit.com/r/wallstreetbets/comments/1xtexaq/comment/19sh9rluer8bm/) |
| HIMS | 2026-11-09 21:25 | mention spike | 8 | 5.0 | 8 | 0 | wallstreetbets 8 | NYSE | #25 | [link](https://www.reddit.com/r/wallstreetbets/comments/1xsv7pt/) |
| GLD | 2026-11-10 17:08 | mention spike | 11 | 6.86 | 2 | 0 | wallstreetbets 11 | NYSE Arca |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xsyjq5/comment/19sgvsqyu4gao/) |

Full history: `episodes.csv` (one row per first flag, with the numbers known at that moment).
