# Stage 1 candidates

Updated 2026-11-11T15:50:08Z by run `43051424558`. A candidate is a ticker whose Reddit mentions (or hype-language
posts) in the last 24 hours jumped above its prior 7-day mean + 2 sd, with at least
10 mentions from 5 different authors. It stays listed until it goes
24 hours without a new flag. These are statistical flags, not accusations or advice.

| Ticker | Flagged since (UTC) | Why | Mentions 24h | Baseline/day | Authors | Hype posts | Subreddits | Exchange | StockTwits | Example |
|---|---|---|---|---|---|---|---|---|---|---|
| ANT | 2026-11-10 14:52 | mention spike | 117 | 29.71 | 86 | 0 | wallstreetbets 117 | ? |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xtkxyp/) |
| AVGO | 2026-11-09 15:56 | mention spike | 36 | 15.14 | 27 | 0 | wallstreetbets 36 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xtexaq/comment/19shc9sgbzjl1/) |
| CRWV | 2026-11-10 20:00 | mention spike | 479 | 32.29 | 222 | 3 | wallstreetbets 478, smallstreetbets 1 | Nasdaq | #1 | [link](https://www.reddit.com/r/smallstreetbets/comments/1xtf57a/) |
| MSFT | 2026-11-11 15:26 | mention spike | 118 | 46.71 | 94 | 0 | wallstreetbets 118 | Nasdaq | #9 | [link](https://www.reddit.com/r/wallstreetbets/comments/1xtgne3/) |
| NBIS | 2026-11-11 12:32 | mention spike | 144 | 47.29 | 86 | 0 | wallstreetbets 144 | Nasdaq | #24 | [link](https://www.reddit.com/r/wallstreetbets/comments/1xt2u2d/) |
| RGTI | 2026-11-10 21:21 | mention spike | 18 | 2.71 | 12 | 0 | wallstreetbets 18 | Nasdaq | #5 | [link](https://www.reddit.com/r/wallstreetbets/comments/1xtexaq/comment/19sham8gm7kdg/) |
| NVDA | 2026-11-09 00:16 | mention spike | 1303 | 419.0 | 657 | 4 | wallstreetbets 1292, smallstreetbets 11 | Nasdaq | #12 | [link](https://www.reddit.com/r/wallstreetbets/comments/1xtiwzd/) |
| MSTR | 2026-11-10 19:20 | mention spike | 10 | 5.14 | 7 | 0 | wallstreetbets 10 | Nasdaq | #26 | [link](https://www.reddit.com/r/wallstreetbets/comments/1xtexaq/comment/19sh9fmvffizn/) |
| NVDL | 2026-11-11 07:39 | mention spike | 8 | 2.29 | 7 | 0 | wallstreetbets 8 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xtexaq/comment/19shbznetfk6a/) |
| GEV | 2026-11-10 15:44 | mention spike | 13 | 4.57 | 8 | 0 | wallstreetbets 13 | NYSE |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xtexaq/comment/19shby819v55v/) |
| TTD | 2026-11-09 21:11 | mention spike | 2 | 9.29 | 2 | 0 | wallstreetbets 2 | Nasdaq | #13 | [link](https://www.reddit.com/r/wallstreetbets/comments/1xsv7pt/) |
| IVF | 2026-11-09 22:18 | mention spike | 0 |  | 0 | 0 |  | Nasdaq |  |  |
| RKLB | 2026-11-09 21:25 | mention spike | 48 | 39.0 | 34 | 0 | wallstreetbets 45, pennystocks 2, smallstreetbets 1 | Nasdaq | #25 | [link](https://www.reddit.com/r/pennystocks/comments/1xtjd2t/) |
| ASTS | 2026-11-09 22:33 | mention spike | 60 | 45.86 | 41 | 1 | wallstreetbets 60 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xtexaq/comment/19shcd284n46c/) |
| OMH | 2026-11-09 20:48 | mention spike | 15 | 4.14 | 11 | 0 | wallstreetbets 8, pennystocks 7 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xt1asn/) |
| TTWO | 2026-11-10 16:24 | mention spike | 23 | 12.57 | 20 | 0 | wallstreetbets 23 | Nasdaq | #17 | [link](https://www.reddit.com/r/wallstreetbets/comments/1xtkngd/) |
| HIMS | 2026-11-09 21:25 | mention spike | 6 | 5.29 | 6 | 0 | wallstreetbets 6 | NYSE |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xsv7pt/) |
| GLD | 2026-11-10 17:08 | mention spike | 11 | 6.86 | 2 | 0 | wallstreetbets 11 | NYSE Arca |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xsyjq5/comment/19sgvsqyu4gao/) |

Full history: `episodes.csv` (one row per first flag, with the numbers known at that moment).
