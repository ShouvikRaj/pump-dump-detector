# Stage 1 candidates

Updated 2026-11-11T13:26:09Z by run `43027978734`. A candidate is a ticker whose Reddit mentions (or hype-language
posts) in the last 24 hours jumped above its prior 7-day mean + 2 sd, with at least
10 mentions from 5 different authors. It stays listed until it goes
24 hours without a new flag. These are statistical flags, not accusations or advice.

| Ticker | Flagged since (UTC) | Why | Mentions 24h | Baseline/day | Authors | Hype posts | Subreddits | Exchange | StockTwits | Example |
|---|---|---|---|---|---|---|---|---|---|---|
| ANT | 2026-11-10 14:52 | mention spike | 124 | 27.29 | 92 | 0 | wallstreetbets 124 | ? |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xt1f1n/) |
| AVGO | 2026-11-09 15:56 | mention spike | 38 | 13.86 | 28 | 0 | wallstreetbets 38 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xtexaq/comment/19sh3wl2bz279/) |
| CRWV | 2026-11-10 20:00 | mention spike | 436 | 31.71 | 206 | 3 | wallstreetbets 435, smallstreetbets 1 | Nasdaq | #2 | [link](https://www.reddit.com/r/smallstreetbets/comments/1xtf57a/) |
| GEV | 2026-11-10 15:44 | mention spike | 16 | 3.43 | 9 | 0 | wallstreetbets 16 | NYSE |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xsyjq5/comment/19sgzs2ih04ua/) |
| NBIS | 2026-11-11 12:32 | mention spike | 119 | 47.57 | 77 | 0 | wallstreetbets 119 | Nasdaq | #13 | [link](https://www.reddit.com/r/wallstreetbets/comments/1xt2u2d/) |
| NVDA | 2026-11-09 00:16 | mention spike | 1383 | 390.29 | 691 | 4 | wallstreetbets 1372, smallstreetbets 11 | Nasdaq | #6 | [link](https://www.reddit.com/r/wallstreetbets/comments/1xtfe3a/) |
| NVDL | 2026-11-11 07:39 | mention spike | 11 | 1.71 | 9 | 0 | wallstreetbets 11 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xt33ld/comment/19sh3biroe1tx/) |
| RGTI | 2026-11-10 21:21 | mention spike | 18 | 2.43 | 12 | 0 | wallstreetbets 18 | Nasdaq | #3 | [link](https://www.reddit.com/r/wallstreetbets/comments/1xsyjq5/comment/19sg6obswrnup/) |
| MSTR | 2026-11-10 19:20 | mention spike | 10 | 4.86 | 9 | 0 | wallstreetbets 10 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xsp9vp/) |
| TTD | 2026-11-09 21:11 | mention spike | 6 | 8.71 | 5 | 0 | wallstreetbets 6 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xsv7pt/) |
| IVF | 2026-11-09 22:18 | mention spike | 0 |  | 0 | 0 |  | Nasdaq |  |  |
| RKLB | 2026-11-09 21:25 | mention spike | 59 | 36.71 | 40 | 0 | wallstreetbets 58, smallstreetbets 1 | Nasdaq |  | [link](https://www.reddit.com/r/smallstreetbets/comments/1xsxl8t/) |
| ASTS | 2026-11-09 22:33 | mention spike | 62 | 44.86 | 42 | 1 | wallstreetbets 62 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xtexaq/comment/19sh17mo7hnms/) |
| OMH | 2026-11-09 20:48 | mention spike | 12 | 3.86 | 9 | 0 | pennystocks 7, wallstreetbets 5 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xt1asn/) |
| TTWO | 2026-11-10 16:24 | mention spike | 25 | 11.71 | 21 | 0 | wallstreetbets 25 | Nasdaq | #22 | [link](https://www.reddit.com/r/wallstreetbets/comments/1xtexaq/comment/19sh324qyasio/) |
| HIMS | 2026-11-09 21:25 | mention spike | 9 | 4.71 | 9 | 0 | wallstreetbets 9 | NYSE | #12 | [link](https://www.reddit.com/r/wallstreetbets/comments/1xsv7pt/) |
| GLD | 2026-11-10 17:08 | mention spike | 14 | 6.71 | 4 | 0 | wallstreetbets 14 | NYSE Arca |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xsyjq5/comment/19sgvsqyu4gao/) |
| CVS | 2026-11-09 13:52 | mention spike | 1 | 3.86 | 1 | 0 | wallstreetbets 1 | NYSE |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xrfbie/comment/19sg74jrxxv28/) |
| NYT | 2026-11-09 11:01 | mention spike | 8 | 3.86 | 8 | 0 | wallstreetbets 8 | NYSE |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xsq1s1/) |

Full history: `episodes.csv` (one row per first flag, with the numbers known at that moment).
