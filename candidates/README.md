# Stage 1 candidates

Updated 2026-11-11T16:46:11Z by run `43060241540`. A candidate is a ticker whose Reddit mentions (or hype-language
posts) in the last 24 hours jumped above its prior 7-day mean + 2 sd, with at least
10 mentions from 5 different authors. It stays listed until it goes
24 hours without a new flag. These are statistical flags, not accusations or advice.

| Ticker | Flagged since (UTC) | Why | Mentions 24h | Baseline/day | Authors | Hype posts | Subreddits | Exchange | StockTwits | Example |
|---|---|---|---|---|---|---|---|---|---|---|
| ANT | 2026-11-10 14:52 | mention spike | 112 | 31.43 | 83 | 0 | wallstreetbets 112 | ? |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xtkxyp/) |
| AVGO | 2026-11-09 15:56 | mention spike | 36 | 15.43 | 27 | 0 | wallstreetbets 36 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xtexaq/comment/19shemwd4tof5/) |
| CRWV | 2026-11-10 20:00 | mention spike | 487 | 32.86 | 227 | 3 | wallstreetbets 486, smallstreetbets 1 | Nasdaq |  | [link](https://www.reddit.com/r/smallstreetbets/comments/1xtf57a/) |
| MSFT | 2026-11-11 15:26 | mention spike | 122 | 47.0 | 94 | 0 | wallstreetbets 122 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xtgne3/) |
| NBIS | 2026-11-11 12:32 | mention spike | 158 | 47.43 | 91 | 0 | wallstreetbets 158 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xt2u2d/) |
| NVDA | 2026-11-09 00:16 | hype spike mention spike | 1154 | 445.57 | 611 | 5 | wallstreetbets 1143, smallstreetbets 11 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xtmfab/) |
| RGTI | 2026-11-10 21:21 | mention spike | 18 | 2.71 | 12 | 0 | wallstreetbets 18 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xtexaq/comment/19sham8gm7kdg/) |
| MSTR | 2026-11-10 19:20 | mention spike | 8 | 5.29 | 6 | 0 | wallstreetbets 8 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xtexaq/comment/19sh9fmvffizn/) |
| NVDL | 2026-11-11 07:39 | mention spike | 8 | 2.29 | 7 | 0 | wallstreetbets 8 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xtexaq/comment/19shbznetfk6a/) |
| GEV | 2026-11-10 15:44 | mention spike | 13 | 4.57 | 8 | 0 | wallstreetbets 13 | NYSE |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xtexaq/comment/19shby819v55v/) |
| TTD | 2026-11-09 21:11 | mention spike | 2 | 9.29 | 2 | 0 | wallstreetbets 2 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xsv7pt/) |
| IVF | 2026-11-09 22:18 | mention spike | 0 |  | 0 | 0 |  | Nasdaq |  |  |
| RKLB | 2026-11-09 21:25 | mention spike | 50 | 38.86 | 36 | 0 | wallstreetbets 47, pennystocks 2, smallstreetbets 1 | Nasdaq |  | [link](https://www.reddit.com/r/pennystocks/comments/1xtjd2t/) |
| ASTS | 2026-11-09 22:33 | mention spike | 61 | 46.14 | 43 | 1 | wallstreetbets 61 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xtexaq/comment/19sher04w2uw3/) |
| OMH | 2026-11-09 20:48 | mention spike | 12 | 4.57 | 10 | 0 | wallstreetbets 7, pennystocks 5 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xt1asn/) |
| TTWO | 2026-11-10 16:24 | mention spike | 25 | 12.71 | 22 | 0 | wallstreetbets 25 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xtmbpo/) |
| HIMS | 2026-11-09 21:25 | mention spike | 5 | 5.43 | 5 | 0 | wallstreetbets 5 | NYSE |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xsv7pt/) |
| GLD | 2026-11-10 17:08 | mention spike | 10 | 6.86 | 2 | 0 | wallstreetbets 10 | NYSE Arca |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xsyjq5/comment/19sgvsqyu4gao/) |

Full history: `episodes.csv` (one row per first flag, with the numbers known at that moment).
