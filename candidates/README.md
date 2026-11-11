# Stage 1 candidates

Updated 2026-11-11T10:58:11Z by run `43007274811`. A candidate is a ticker whose Reddit mentions (or hype-language
posts) in the last 24 hours jumped above its prior 7-day mean + 2 sd, with at least
10 mentions from 5 different authors. It stays listed until it goes
24 hours without a new flag. These are statistical flags, not accusations or advice.

| Ticker | Flagged since (UTC) | Why | Mentions 24h | Baseline/day | Authors | Hype posts | Subreddits | Exchange | StockTwits | Example |
|---|---|---|---|---|---|---|---|---|---|---|
| ANT | 2026-11-10 14:52 | mention spike | 132 | 25.57 | 93 | 0 | wallstreetbets 132 | ? |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xt1f1n/) |
| AVGO | 2026-11-09 15:56 | mention spike | 42 | 13.29 | 29 | 0 | wallstreetbets 42 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xsyjq5/comment/19sgy56wosepw/) |
| CRWV | 2026-11-10 20:00 | mention spike | 415 | 31.0 | 199 | 3 | wallstreetbets 415 | Nasdaq | #1 | [link](https://www.reddit.com/r/wallstreetbets/comments/1xt6szx/) |
| GEV | 2026-11-10 15:44 | mention spike | 17 | 3.0 | 11 | 0 | wallstreetbets 17 | NYSE |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xsyjq5/comment/19sgxm2tlgwhv/) |
| NVDA | 2026-11-09 00:16 | mention spike | 1317 | 387.0 | 672 | 3 | wallstreetbets 1306, smallstreetbets 11 | Nasdaq | #2 | [link](https://www.reddit.com/r/smallstreetbets/comments/1xtdck2/) |
| NVDL | 2026-11-11 07:39 | mention spike | 10 | 1.71 | 8 | 0 | wallstreetbets 10 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xsyjq5/comment/19sgq6qshkmtf/) |
| RGTI | 2026-11-10 21:21 | mention spike | 18 | 2.43 | 12 | 0 | wallstreetbets 18 | Nasdaq | #3 | [link](https://www.reddit.com/r/wallstreetbets/comments/1xsyjq5/comment/19sg6obswrnup/) |
| MSTR | 2026-11-10 19:20 | mention spike | 10 | 4.57 | 7 | 0 | wallstreetbets 10 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xsp9vp/) |
| TTD | 2026-11-09 21:11 | mention spike | 11 | 8.0 | 10 | 0 | wallstreetbets 11 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xsv7pt/) |
| IVF | 2026-11-09 22:18 | mention spike | 0 |  | 0 | 0 |  | Nasdaq |  |  |
| RKLB | 2026-11-09 21:25 | mention spike | 59 | 36.57 | 41 | 0 | wallstreetbets 58, smallstreetbets 1 | Nasdaq | #20 | [link](https://www.reddit.com/r/smallstreetbets/comments/1xsxl8t/) |
| ASTS | 2026-11-09 22:33 | mention spike | 62 | 44.86 | 41 | 1 | wallstreetbets 62 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xsyjq5/comment/19sgt8om1a54y/) |
| OMH | 2026-11-09 20:48 | mention spike | 14 | 3.43 | 9 | 0 | pennystocks 7, wallstreetbets 7 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xt1asn/) |
| TTWO | 2026-11-10 16:24 | mention spike | 25 | 11.57 | 21 | 0 | wallstreetbets 25 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xsyjq5/comment/19sgtz16nwrcw/) |
| HIMS | 2026-11-09 21:25 | mention spike | 11 | 4.43 | 11 | 0 | wallstreetbets 11 | NYSE | #12 | [link](https://www.reddit.com/r/wallstreetbets/comments/1xsv7pt/) |
| GLD | 2026-11-10 17:08 | mention spike | 14 | 6.86 | 4 | 0 | wallstreetbets 14 | NYSE Arca |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xsyjq5/comment/19sgvsqyu4gao/) |
| CVS | 2026-11-09 13:52 | mention spike | 2 | 3.71 | 2 | 0 | wallstreetbets 2 | NYSE |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xrfbie/comment/19sg74jrxxv28/) |
| NYT | 2026-11-09 11:01 | mention spike | 10 | 3.57 | 10 | 0 | wallstreetbets 9, smallstreetbets 1 | NYSE |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xsq1s1/) |
| NNN | 2026-11-09 15:04 | mention spike | 6 | 6.43 | 5 | 0 | wallstreetbets 5, smallstreetbets 1 | NYSE |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xsyjq5/comment/19sgax8c2avsw/) |

Full history: `episodes.csv` (one row per first flag, with the numbers known at that moment).
