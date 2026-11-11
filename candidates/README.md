# Stage 1 candidates

Updated 2026-11-11T15:26:11Z by run `43047003741`. A candidate is a ticker whose Reddit mentions (or hype-language
posts) in the last 24 hours jumped above its prior 7-day mean + 2 sd, with at least
10 mentions from 5 different authors. It stays listed until it goes
24 hours without a new flag. These are statistical flags, not accusations or advice.

| Ticker | Flagged since (UTC) | Why | Mentions 24h | Baseline/day | Authors | Hype posts | Subreddits | Exchange | StockTwits | Example |
|---|---|---|---|---|---|---|---|---|---|---|
| ANT | 2026-11-10 14:52 | mention spike | 114 | 29.57 | 82 | 0 | wallstreetbets 114 | ? |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xt1f1n/) |
| AVGO | 2026-11-09 15:56 | mention spike | 37 | 14.71 | 27 | 0 | wallstreetbets 37 | Nasdaq | #19 | [link](https://www.reddit.com/r/wallstreetbets/comments/1xtexaq/comment/19sham4018k4k/) |
| CRWV | 2026-11-10 20:00 | mention spike | 468 | 32.29 | 221 | 3 | wallstreetbets 467, smallstreetbets 1 | Nasdaq | #3 | [link](https://www.reddit.com/r/smallstreetbets/comments/1xtf57a/) |
| NBIS | 2026-11-11 12:32 | mention spike | 138 | 46.86 | 84 | 0 | wallstreetbets 138 | Nasdaq | #24 | [link](https://www.reddit.com/r/wallstreetbets/comments/1xt2u2d/) |
| NVDA | 2026-11-09 00:16 | mention spike | 1348 | 408.29 | 672 | 4 | wallstreetbets 1337, smallstreetbets 11 | Nasdaq | #13 | [link](https://www.reddit.com/r/wallstreetbets/comments/1xtiwzd/) |
| RGTI | 2026-11-10 21:21 | mention spike | 18 | 2.71 | 12 | 0 | wallstreetbets 18 | Nasdaq | #6 | [link](https://www.reddit.com/r/wallstreetbets/comments/1xtexaq/comment/19sham8gm7kdg/) |
| MSFT | 2026-11-11 15:26 | mention spike | 105 | 46.57 | 86 | 0 | wallstreetbets 105 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xtgne3/) |
| MSTR | 2026-11-10 19:20 | mention spike | 11 | 5.0 | 8 | 0 | wallstreetbets 11 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xtexaq/comment/19sh9fmvffizn/) |
| NVDL | 2026-11-11 07:39 | mention spike | 7 | 2.29 | 6 | 0 | wallstreetbets 7 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xt33ld/comment/19sh3biroe1tx/) |
| GEV | 2026-11-10 15:44 | mention spike | 12 | 4.43 | 7 | 0 | wallstreetbets 12 | NYSE |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xtexaq/comment/19sha3yx2xzog/) |
| TTD | 2026-11-09 21:11 | mention spike | 2 | 9.29 | 2 | 0 | wallstreetbets 2 | Nasdaq | #11 | [link](https://www.reddit.com/r/wallstreetbets/comments/1xsv7pt/) |
| IVF | 2026-11-09 22:18 | mention spike | 0 |  | 0 | 0 |  | Nasdaq |  |  |
| RKLB | 2026-11-09 21:25 | mention spike | 49 | 38.71 | 35 | 0 | wallstreetbets 46, pennystocks 2, smallstreetbets 1 | Nasdaq | #23 | [link](https://www.reddit.com/r/pennystocks/comments/1xtjd2t/) |
| ASTS | 2026-11-09 22:33 | mention spike | 65 | 45.0 | 43 | 1 | wallstreetbets 65 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xtexaq/comment/19shb0auq609w/) |
| OMH | 2026-11-09 20:48 | mention spike | 14 | 4.14 | 10 | 0 | pennystocks 7, wallstreetbets 7 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xt1asn/) |
| TTWO | 2026-11-10 16:24 | mention spike | 23 | 12.43 | 20 | 0 | wallstreetbets 23 | Nasdaq | #16 | [link](https://www.reddit.com/r/wallstreetbets/comments/1xtjtks/) |
| HIMS | 2026-11-09 21:25 | mention spike | 8 | 5.0 | 8 | 0 | wallstreetbets 8 | NYSE |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xsv7pt/) |
| GLD | 2026-11-10 17:08 | mention spike | 11 | 6.86 | 2 | 0 | wallstreetbets 11 | NYSE Arca |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xsyjq5/comment/19sgvsqyu4gao/) |

Full history: `episodes.csv` (one row per first flag, with the numbers known at that moment).
