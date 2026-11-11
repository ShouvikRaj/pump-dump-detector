# Stage 1 candidates

Updated 2026-11-11T16:59:10Z by run `43062386127`. A candidate is a ticker whose Reddit mentions (or hype-language
posts) in the last 24 hours jumped above its prior 7-day mean + 2 sd, with at least
10 mentions from 5 different authors. It stays listed until it goes
24 hours without a new flag. These are statistical flags, not accusations or advice.

| Ticker | Flagged since (UTC) | Why | Mentions 24h | Baseline/day | Authors | Hype posts | Subreddits | Exchange | StockTwits | Example |
|---|---|---|---|---|---|---|---|---|---|---|
| ANT | 2026-11-10 14:52 | mention spike | 114 | 31.86 | 85 | 0 | wallstreetbets 114 | ? |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xtkxyp/) |
| AVGO | 2026-11-09 15:56 | mention spike | 34 | 15.71 | 25 | 0 | wallstreetbets 34 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xtexaq/comment/19shemwd4tof5/) |
| CRWV | 2026-11-10 20:00 | mention spike | 490 | 33.14 | 229 | 3 | wallstreetbets 489, smallstreetbets 1 | Nasdaq | #1 | [link](https://www.reddit.com/r/smallstreetbets/comments/1xtf57a/) |
| MSFT | 2026-11-11 15:26 | mention spike | 124 | 47.57 | 93 | 0 | wallstreetbets 124 | Nasdaq | #3 | [link](https://www.reddit.com/r/wallstreetbets/comments/1xtgne3/) |
| NBIS | 2026-11-11 12:32 | mention spike | 161 | 47.43 | 93 | 0 | wallstreetbets 161 | Nasdaq | #11 | [link](https://www.reddit.com/r/wallstreetbets/comments/1xt2u2d/) |
| NVDA | 2026-11-09 00:16 | hype spike mention spike | 1116 | 452.29 | 595 | 5 | wallstreetbets 1105, smallstreetbets 11 | Nasdaq | #28 | [link](https://www.reddit.com/r/wallstreetbets/comments/1xtmfab/) |
| RGTI | 2026-11-10 21:21 | mention spike | 18 | 2.71 | 12 | 0 | wallstreetbets 18 | Nasdaq | #12 | [link](https://www.reddit.com/r/wallstreetbets/comments/1xtexaq/comment/19sham8gm7kdg/) |
| MSTR | 2026-11-10 19:20 | mention spike | 8 | 5.29 | 6 | 0 | wallstreetbets 8 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xtexaq/comment/19sh9fmvffizn/) |
| NVDL | 2026-11-11 07:39 | mention spike | 8 | 2.29 | 7 | 0 | wallstreetbets 8 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xtexaq/comment/19shbznetfk6a/) |
| GEV | 2026-11-10 15:44 | mention spike | 13 | 4.57 | 8 | 0 | wallstreetbets 13 | NYSE |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xtexaq/comment/19shby819v55v/) |
| TTD | 2026-11-09 21:11 | mention spike | 2 | 9.29 | 2 | 0 | wallstreetbets 2 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xsv7pt/) |
| IVF | 2026-11-09 22:18 | mention spike | 0 |  | 0 | 0 |  | Nasdaq |  |  |
| RKLB | 2026-11-09 21:25 | mention spike | 50 | 38.86 | 36 | 0 | wallstreetbets 47, pennystocks 2, smallstreetbets 1 | Nasdaq |  | [link](https://www.reddit.com/r/pennystocks/comments/1xtjd2t/) |
| ASTS | 2026-11-09 22:33 | mention spike | 61 | 46.29 | 43 | 1 | wallstreetbets 61 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xtexaq/comment/19shfd9dw1p0j/) |
| OMH | 2026-11-09 20:48 | mention spike | 12 | 4.57 | 10 | 0 | wallstreetbets 7, pennystocks 5 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xt1asn/) |
| TTWO | 2026-11-10 16:24 | mention spike | 24 | 12.86 | 21 | 0 | wallstreetbets 24 | Nasdaq | #22 | [link](https://www.reddit.com/r/wallstreetbets/comments/1xtmbpo/) |
| HIMS | 2026-11-09 21:25 | mention spike | 5 | 5.43 | 5 | 0 | wallstreetbets 5 | NYSE |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xsv7pt/) |
| GLD | 2026-11-10 17:08 | mention spike | 10 | 7.0 | 2 | 0 | wallstreetbets 10 | NYSE Arca | #6 | [link](https://www.reddit.com/r/wallstreetbets/comments/1xtexaq/comment/19shezgnsfzdx/) |

Full history: `episodes.csv` (one row per first flag, with the numbers known at that moment).
