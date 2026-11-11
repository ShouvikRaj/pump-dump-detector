# Stage 1 candidates

Updated 2026-11-11T18:31:12Z by run `43077427862`. A candidate is a ticker whose Reddit mentions (or hype-language
posts) in the last 24 hours jumped above its prior 7-day mean + 2 sd, with at least
10 mentions from 5 different authors. It stays listed until it goes
24 hours without a new flag. These are statistical flags, not accusations or advice.

| Ticker | Flagged since (UTC) | Why | Mentions 24h | Baseline/day | Authors | Hype posts | Subreddits | Exchange | StockTwits | Example |
|---|---|---|---|---|---|---|---|---|---|---|
| ANT | 2026-11-10 14:52 | mention spike | 110 | 33.29 | 85 | 0 | wallstreetbets 110 | ? |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xtooay/) |
| AVGO | 2026-11-09 15:56 | mention spike | 37 | 16.14 | 26 | 0 | wallstreetbets 36, smallstreetbets 1 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xtexaq/comment/19shj8e1303j5/) |
| CRWV | 2026-11-10 20:00 | mention spike | 505 | 35.14 | 239 | 3 | wallstreetbets 503, smallstreetbets 2 | Nasdaq | #10 | [link](https://www.reddit.com/r/wallstreetbets/comments/1xtoxn0/) |
| GEV | 2026-11-10 15:44 | mention spike | 14 | 4.57 | 9 | 0 | wallstreetbets 14 | NYSE |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xtexaq/comment/19shiwgpl0cm8/) |
| NBIS | 2026-11-11 12:32 | mention spike | 179 | 48.14 | 108 | 1 | wallstreetbets 178, smallstreetbets 1 | Nasdaq | #4 | [link](https://www.reddit.com/r/wallstreetbets/comments/1xt2u2d/) |
| NVDA | 2026-11-09 00:16 | hype spike mention spike | 974 | 479.57 | 519 | 5 | wallstreetbets 964, smallstreetbets 10 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xtpc8j/) |
| RGTI | 2026-11-10 21:21 | mention spike | 17 | 2.86 | 11 | 0 | wallstreetbets 17 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xtexaq/comment/19sham8gm7kdg/) |
| MSFT | 2026-11-11 15:26 | mention spike | 78 | 55.71 | 61 | 0 | wallstreetbets 78 | Nasdaq | #27 | [link](https://www.reddit.com/r/wallstreetbets/comments/1xtpc8j/) |
| MSTR | 2026-11-10 19:20 | mention spike | 8 | 5.43 | 6 | 0 | wallstreetbets 8 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xtexaq/comment/19shfla470vz7/) |
| NVDL | 2026-11-11 07:39 | mention spike | 9 | 2.29 | 8 | 0 | wallstreetbets 9 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xtexaq/comment/19shfroitlpes/) |
| TTD | 2026-11-09 21:11 | mention spike | 2 | 9.29 | 2 | 0 | wallstreetbets 2 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xsv7pt/) |
| IVF | 2026-11-09 22:18 | mention spike | 0 |  | 0 | 0 |  | Nasdaq |  |  |
| RKLB | 2026-11-09 21:25 | mention spike | 47 | 39.57 | 33 | 0 | wallstreetbets 44, pennystocks 2, smallstreetbets 1 | Nasdaq |  | [link](https://www.reddit.com/r/pennystocks/comments/1xtjd2t/) |
| ASTS | 2026-11-09 22:33 | mention spike | 52 | 48.0 | 35 | 1 | wallstreetbets 52 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xtnfuy/comment/19shiw6wdd7t0/) |
| OMH | 2026-11-09 20:48 | mention spike | 10 | 5.0 | 9 | 0 | pennystocks 5, wallstreetbets 5 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xt1asn/) |
| TTWO | 2026-11-10 16:24 | mention spike | 26 | 13.14 | 22 | 0 | wallstreetbets 26 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xtnc9r/) |
| HIMS | 2026-11-09 21:25 | mention spike | 4 | 5.57 | 4 | 0 | wallstreetbets 4 | NYSE |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xsv7pt/) |
| GLD | 2026-11-10 17:08 | mention spike | 13 | 6.86 | 5 | 0 | wallstreetbets 13 | NYSE Arca | #14 | [link](https://www.reddit.com/r/wallstreetbets/comments/1xtexaq/comment/19shj8phkhh40/) |

Full history: `episodes.csv` (one row per first flag, with the numbers known at that moment).
