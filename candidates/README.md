# Stage 1 candidates

Updated 2026-11-11T12:05:07Z by run `43016424639`. A candidate is a ticker whose Reddit mentions (or hype-language
posts) in the last 24 hours jumped above its prior 7-day mean + 2 sd, with at least
10 mentions from 5 different authors. It stays listed until it goes
24 hours without a new flag. These are statistical flags, not accusations or advice.

| Ticker | Flagged since (UTC) | Why | Mentions 24h | Baseline/day | Authors | Hype posts | Subreddits | Exchange | StockTwits | Example |
|---|---|---|---|---|---|---|---|---|---|---|
| ANT | 2026-11-10 14:52 | mention spike | 128 | 26.29 | 91 | 0 | wallstreetbets 128 | ? |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xt1f1n/) |
| AVGO | 2026-11-09 15:56 | mention spike | 40 | 13.57 | 29 | 0 | wallstreetbets 40 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xsyjq5/comment/19sgy56wosepw/) |
| CRWV | 2026-11-10 20:00 | mention spike | 422 | 31.0 | 204 | 3 | wallstreetbets 421, smallstreetbets 1 | Nasdaq | #2 | [link](https://www.reddit.com/r/smallstreetbets/comments/1xtf57a/) |
| GEV | 2026-11-10 15:44 | mention spike | 19 | 3.0 | 12 | 0 | wallstreetbets 19 | NYSE |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xsyjq5/comment/19sgzs2ih04ua/) |
| NVDA | 2026-11-09 00:16 | mention spike | 1340 | 387.71 | 678 | 4 | wallstreetbets 1329, smallstreetbets 11 | Nasdaq | #1 | [link](https://www.reddit.com/r/wallstreetbets/comments/1xtfe3a/) |
| NVDL | 2026-11-11 07:39 | mention spike | 10 | 1.71 | 8 | 0 | wallstreetbets 10 | Nasdaq | #27 | [link](https://www.reddit.com/r/wallstreetbets/comments/1xsyjq5/comment/19sgq6qshkmtf/) |
| RGTI | 2026-11-10 21:21 | mention spike | 18 | 2.43 | 12 | 0 | wallstreetbets 18 | Nasdaq | #6 | [link](https://www.reddit.com/r/wallstreetbets/comments/1xsyjq5/comment/19sg6obswrnup/) |
| MSTR | 2026-11-10 19:20 | mention spike | 9 | 4.71 | 7 | 0 | wallstreetbets 9 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xsp9vp/) |
| TTD | 2026-11-09 21:11 | mention spike | 9 | 8.29 | 8 | 0 | wallstreetbets 9 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xsv7pt/) |
| IVF | 2026-11-09 22:18 | mention spike | 0 |  | 0 | 0 |  | Nasdaq |  |  |
| RKLB | 2026-11-09 21:25 | mention spike | 60 | 36.57 | 42 | 0 | wallstreetbets 59, smallstreetbets 1 | Nasdaq |  | [link](https://www.reddit.com/r/smallstreetbets/comments/1xsxl8t/) |
| ASTS | 2026-11-09 22:33 | mention spike | 64 | 45.0 | 43 | 1 | wallstreetbets 64 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xtexaq/comment/19sh17mo7hnms/) |
| OMH | 2026-11-09 20:48 | mention spike | 12 | 3.71 | 8 | 0 | pennystocks 7, wallstreetbets 5 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xt1asn/) |
| TTWO | 2026-11-10 16:24 | mention spike | 24 | 11.71 | 20 | 0 | wallstreetbets 24 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xsyjq5/comment/19sgtz16nwrcw/) |
| HIMS | 2026-11-09 21:25 | mention spike | 10 | 4.57 | 10 | 0 | wallstreetbets 10 | NYSE | #21 | [link](https://www.reddit.com/r/wallstreetbets/comments/1xsv7pt/) |
| GLD | 2026-11-10 17:08 | mention spike | 14 | 6.86 | 4 | 0 | wallstreetbets 14 | NYSE Arca |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xsyjq5/comment/19sgvsqyu4gao/) |
| CVS | 2026-11-09 13:52 | mention spike | 1 | 3.86 | 1 | 0 | wallstreetbets 1 | NYSE |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xrfbie/comment/19sg74jrxxv28/) |
| NYT | 2026-11-09 11:01 | mention spike | 9 | 3.71 | 9 | 0 | wallstreetbets 9 | NYSE |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xsq1s1/) |
| NNN | 2026-11-09 15:04 | mention spike | 5 | 6.57 | 4 | 0 | wallstreetbets 5 | NYSE |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xsyjq5/comment/19sgax8c2avsw/) |

Full history: `episodes.csv` (one row per first flag, with the numbers known at that moment).
