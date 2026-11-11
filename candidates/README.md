# Stage 1 candidates

Updated 2026-11-11T07:39:08Z by run `42980391923`. A candidate is a ticker whose Reddit mentions (or hype-language
posts) in the last 24 hours jumped above its prior 7-day mean + 2 sd, with at least
10 mentions from 5 different authors. It stays listed until it goes
24 hours without a new flag. These are statistical flags, not accusations or advice.

| Ticker | Flagged since (UTC) | Why | Mentions 24h | Baseline/day | Authors | Hype posts | Subreddits | Exchange | StockTwits | Example |
|---|---|---|---|---|---|---|---|---|---|---|
| ANT | 2026-11-10 14:52 | mention spike | 129 | 25.57 | 90 | 0 | wallstreetbets 129 | ? |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xt1f1n/) |
| AVGO | 2026-11-09 15:56 | mention spike | 41 | 13.14 | 29 | 0 | wallstreetbets 41 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xsyjq5/comment/19sgq0kw41nk0/) |
| CRWV | 2026-11-10 20:00 | mention spike | 399 | 30.86 | 189 | 3 | wallstreetbets 399 | Nasdaq | #1 | [link](https://www.reddit.com/r/wallstreetbets/comments/1xt6szx/) |
| GEV | 2026-11-10 15:44 | mention spike | 16 | 3.0 | 11 | 0 | wallstreetbets 16 | NYSE |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xsyjq5/comment/19sgmnshy55kx/) |
| NVDA | 2026-11-09 00:16 | mention spike | 1288 | 384.0 | 663 | 2 | wallstreetbets 1279, smallstreetbets 9 | Nasdaq | #21 | [link](https://www.reddit.com/r/smallstreetbets/comments/1xtaa6s/) |
| RGTI | 2026-11-10 21:21 | mention spike | 18 | 2.43 | 12 | 0 | wallstreetbets 18 | Nasdaq | #3 | [link](https://www.reddit.com/r/wallstreetbets/comments/1xsyjq5/comment/19sg6obswrnup/) |
| NVDL | 2026-11-11 07:39 | mention spike | 10 | 1.71 | 8 | 0 | wallstreetbets 10 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xsyjq5/comment/19sgq6qshkmtf/) |
| MSTR | 2026-11-10 19:20 | mention spike | 10 | 4.57 | 7 | 0 | wallstreetbets 10 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xsp9vp/) |
| TTD | 2026-11-09 21:11 | mention spike | 11 | 8.0 | 10 | 0 | wallstreetbets 11 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xsv7pt/) |
| IVF | 2026-11-09 22:18 | mention spike | 0 |  | 0 | 0 |  | Nasdaq |  |  |
| RKLB | 2026-11-09 21:25 | mention spike | 61 | 36.43 | 43 | 0 | wallstreetbets 60, smallstreetbets 1 | Nasdaq |  | [link](https://www.reddit.com/r/smallstreetbets/comments/1xsxl8t/) |
| ASTS | 2026-11-09 22:33 | mention spike | 64 | 44.57 | 43 | 1 | wallstreetbets 64 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xsyjq5/comment/19sgoqhb05dvk/) |
| OMH | 2026-11-09 20:48 | mention spike | 14 | 3.43 | 9 | 0 | pennystocks 7, wallstreetbets 7 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xt1asn/) |
| TTWO | 2026-11-10 16:24 | mention spike | 25 | 11.43 | 21 | 0 | wallstreetbets 25 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xsyjq5/comment/19sglzhjhjc75/) |
| HIMS | 2026-11-09 21:25 | mention spike | 12 | 4.29 | 12 | 0 | wallstreetbets 12 | NYSE | #30 | [link](https://www.reddit.com/r/wallstreetbets/comments/1xsv7pt/) |
| GLD | 2026-11-10 17:08 | mention spike | 14 | 6.71 | 4 | 0 | wallstreetbets 14 | NYSE Arca |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xsyjq5/comment/19sgium207fcx/) |
| CVS | 2026-11-09 13:52 | mention spike | 2 | 3.71 | 2 | 0 | wallstreetbets 2 | NYSE |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xrfbie/comment/19sg74jrxxv28/) |
| NYT | 2026-11-09 11:01 | mention spike | 10 | 3.57 | 10 | 0 | wallstreetbets 9, smallstreetbets 1 | NYSE |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xsq1s1/) |
| NNN | 2026-11-09 15:04 | mention spike | 6 | 6.43 | 5 | 0 | wallstreetbets 5, smallstreetbets 1 | NYSE |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xsyjq5/comment/19sgax8c2avsw/) |

Full history: `episodes.csv` (one row per first flag, with the numbers known at that moment).
