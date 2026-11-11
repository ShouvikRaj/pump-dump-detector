# Stage 1 candidates

Updated 2026-11-11T14:33:09Z by run `43038267076`. A candidate is a ticker whose Reddit mentions (or hype-language
posts) in the last 24 hours jumped above its prior 7-day mean + 2 sd, with at least
10 mentions from 5 different authors. It stays listed until it goes
24 hours without a new flag. These are statistical flags, not accusations or advice.

| Ticker | Flagged since (UTC) | Why | Mentions 24h | Baseline/day | Authors | Hype posts | Subreddits | Exchange | StockTwits | Example |
|---|---|---|---|---|---|---|---|---|---|---|
| ANT | 2026-11-10 14:52 | mention spike | 116 | 28.71 | 84 | 0 | wallstreetbets 116 | ? |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xt1f1n/) |
| AVGO | 2026-11-09 15:56 | mention spike | 39 | 13.71 | 28 | 0 | wallstreetbets 39 | Nasdaq | #19 | [link](https://www.reddit.com/r/wallstreetbets/comments/1xtexaq/comment/19sh8tiudknhd/) |
| CRWV | 2026-11-10 20:00 | mention spike | 447 | 31.86 | 212 | 3 | wallstreetbets 446, smallstreetbets 1 | Nasdaq | #11 | [link](https://www.reddit.com/r/smallstreetbets/comments/1xtf57a/) |
| NBIS | 2026-11-11 12:32 | mention spike | 123 | 47.57 | 78 | 0 | wallstreetbets 123 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xt2u2d/) |
| NVDA | 2026-11-09 00:16 | mention spike | 1409 | 393.14 | 697 | 4 | wallstreetbets 1398, smallstreetbets 11 | Nasdaq | #6 | [link](https://www.reddit.com/r/wallstreetbets/comments/1xtiwzd/) |
| NVDL | 2026-11-11 07:39 | mention spike | 11 | 1.71 | 9 | 0 | wallstreetbets 11 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xt33ld/comment/19sh3biroe1tx/) |
| RGTI | 2026-11-10 21:21 | mention spike | 17 | 2.57 | 12 | 0 | wallstreetbets 17 | Nasdaq | #3 | [link](https://www.reddit.com/r/wallstreetbets/comments/1xsyjq5/comment/19sg6obswrnup/) |
| GEV | 2026-11-10 15:44 | mention spike | 11 | 4.29 | 6 | 0 | wallstreetbets 11 | NYSE |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xtexaq/comment/19sh8mjputcyo/) |
| MSTR | 2026-11-10 19:20 | mention spike | 10 | 4.86 | 9 | 0 | wallstreetbets 10 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xsp9vp/) |
| TTD | 2026-11-09 21:11 | mention spike | 3 | 9.14 | 3 | 0 | wallstreetbets 3 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xsv7pt/) |
| IVF | 2026-11-09 22:18 | mention spike | 0 |  | 0 | 0 |  | Nasdaq |  |  |
| RKLB | 2026-11-09 21:25 | mention spike | 50 | 37.86 | 35 | 0 | wallstreetbets 49, smallstreetbets 1 | Nasdaq |  | [link](https://www.reddit.com/r/smallstreetbets/comments/1xsxl8t/) |
| ASTS | 2026-11-09 22:33 | mention spike | 62 | 45.14 | 41 | 1 | wallstreetbets 62 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xtexaq/comment/19sh8v1iebowz/) |
| OMH | 2026-11-09 20:48 | mention spike | 12 | 3.86 | 9 | 0 | pennystocks 7, wallstreetbets 5 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xt1asn/) |
| TTWO | 2026-11-10 16:24 | mention spike | 23 | 12.0 | 20 | 0 | wallstreetbets 23 | Nasdaq | #28 | [link](https://www.reddit.com/r/wallstreetbets/comments/1xtexaq/comment/19sh324qyasio/) |
| HIMS | 2026-11-09 21:25 | mention spike | 9 | 4.86 | 9 | 0 | wallstreetbets 9 | NYSE | #15 | [link](https://www.reddit.com/r/wallstreetbets/comments/1xsv7pt/) |
| GLD | 2026-11-10 17:08 | mention spike | 11 | 7.0 | 2 | 0 | wallstreetbets 11 | NYSE Arca |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xsyjq5/comment/19sgvsqyu4gao/) |

Full history: `episodes.csv` (one row per first flag, with the numbers known at that moment).
