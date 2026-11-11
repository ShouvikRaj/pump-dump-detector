# Stage 1 candidates

Updated 2026-11-11T14:06:10Z by run `43034011581`. A candidate is a ticker whose Reddit mentions (or hype-language
posts) in the last 24 hours jumped above its prior 7-day mean + 2 sd, with at least
10 mentions from 5 different authors. It stays listed until it goes
24 hours without a new flag. These are statistical flags, not accusations or advice.

| Ticker | Flagged since (UTC) | Why | Mentions 24h | Baseline/day | Authors | Hype posts | Subreddits | Exchange | StockTwits | Example |
|---|---|---|---|---|---|---|---|---|---|---|
| ANT | 2026-11-10 14:52 | mention spike | 122 | 27.71 | 88 | 0 | wallstreetbets 122 | ? |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xt1f1n/) |
| AVGO | 2026-11-09 15:56 | mention spike | 38 | 13.71 | 28 | 0 | wallstreetbets 38 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xtexaq/comment/19sh3wl2bz279/) |
| CRWV | 2026-11-10 20:00 | mention spike | 441 | 31.71 | 207 | 3 | wallstreetbets 440, smallstreetbets 1 | Nasdaq | #12 | [link](https://www.reddit.com/r/smallstreetbets/comments/1xtf57a/) |
| GEV | 2026-11-10 15:44 | mention spike | 16 | 3.43 | 9 | 0 | wallstreetbets 16 | NYSE |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xsyjq5/comment/19sgzs2ih04ua/) |
| NBIS | 2026-11-11 12:32 | mention spike | 122 | 47.71 | 78 | 0 | wallstreetbets 122 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xt2u2d/) |
| NVDA | 2026-11-09 00:16 | mention spike | 1390 | 392.0 | 689 | 4 | wallstreetbets 1379, smallstreetbets 11 | Nasdaq | #5 | [link](https://www.reddit.com/r/wallstreetbets/comments/1xtfe3a/) |
| NVDL | 2026-11-11 07:39 | mention spike | 11 | 1.71 | 9 | 0 | wallstreetbets 11 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xt33ld/comment/19sh3biroe1tx/) |
| RGTI | 2026-11-10 21:21 | mention spike | 18 | 2.43 | 12 | 0 | wallstreetbets 18 | Nasdaq | #3 | [link](https://www.reddit.com/r/wallstreetbets/comments/1xsyjq5/comment/19sg6obswrnup/) |
| MSTR | 2026-11-10 19:20 | mention spike | 10 | 4.86 | 9 | 0 | wallstreetbets 10 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xsp9vp/) |
| TTD | 2026-11-09 21:11 | mention spike | 4 | 9.0 | 4 | 0 | wallstreetbets 4 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xsv7pt/) |
| IVF | 2026-11-09 22:18 | mention spike | 0 |  | 0 | 0 |  | Nasdaq |  |  |
| RKLB | 2026-11-09 21:25 | mention spike | 55 | 37.29 | 38 | 0 | wallstreetbets 54, smallstreetbets 1 | Nasdaq |  | [link](https://www.reddit.com/r/smallstreetbets/comments/1xsxl8t/) |
| ASTS | 2026-11-09 22:33 | mention spike | 63 | 45.0 | 42 | 1 | wallstreetbets 63 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xsprt1/comment/19sh6zedfcav5/) |
| OMH | 2026-11-09 20:48 | mention spike | 12 | 3.86 | 9 | 0 | pennystocks 7, wallstreetbets 5 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xt1asn/) |
| TTWO | 2026-11-10 16:24 | mention spike | 25 | 11.71 | 21 | 0 | wallstreetbets 25 | Nasdaq | #24 | [link](https://www.reddit.com/r/wallstreetbets/comments/1xtexaq/comment/19sh324qyasio/) |
| HIMS | 2026-11-09 21:25 | mention spike | 10 | 4.71 | 10 | 0 | wallstreetbets 10 | NYSE | #20 | [link](https://www.reddit.com/r/wallstreetbets/comments/1xsv7pt/) |
| GLD | 2026-11-10 17:08 | mention spike | 12 | 7.0 | 3 | 0 | wallstreetbets 12 | NYSE Arca |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xsyjq5/comment/19sgvsqyu4gao/) |
| CVS | 2026-11-09 13:52 | mention spike | 1 | 3.86 | 1 | 0 | wallstreetbets 1 | NYSE |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xrfbie/comment/19sg74jrxxv28/) |

Full history: `episodes.csv` (one row per first flag, with the numbers known at that moment).
