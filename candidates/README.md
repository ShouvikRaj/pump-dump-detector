# Stage 1 candidates

Updated 2026-11-11T04:09:10Z by run `42956509074`. A candidate is a ticker whose Reddit mentions (or hype-language
posts) in the last 24 hours jumped above its prior 7-day mean + 2 sd, with at least
10 mentions from 5 different authors. It stays listed until it goes
24 hours without a new flag. These are statistical flags, not accusations or advice.

| Ticker | Flagged since (UTC) | Why | Mentions 24h | Baseline/day | Authors | Hype posts | Subreddits | Exchange | StockTwits | Example |
|---|---|---|---|---|---|---|---|---|---|---|
| ANT | 2026-11-10 14:52 | mention spike | 129 | 25.43 | 89 | 0 | wallstreetbets 129 | ? |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xt1f1n/) |
| AVGO | 2026-11-09 15:56 | mention spike | 36 | 13.29 | 27 | 0 | wallstreetbets 36 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xpo1gj/comment/19sga4ltaktk2/) |
| CRWV | 2026-11-10 20:00 | mention spike | 390 | 31.14 | 184 | 3 | wallstreetbets 390 | Nasdaq | #1 | [link](https://www.reddit.com/r/wallstreetbets/comments/1xt6szx/) |
| GEV | 2026-11-10 15:44 | mention spike | 15 | 3.0 | 10 | 0 | wallstreetbets 15 | NYSE |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xsyjq5/comment/19sgbnb3yro8z/) |
| NVDA | 2026-11-09 00:16 | mention spike | 1275 | 379.0 | 661 | 2 | wallstreetbets 1266, smallstreetbets 9 | Nasdaq | #3 | [link](https://www.reddit.com/r/wallstreetbets/comments/1xt6rv2/) |
| RGTI | 2026-11-10 21:21 | mention spike | 18 | 2.43 | 12 | 0 | wallstreetbets 18 | Nasdaq | #9 | [link](https://www.reddit.com/r/wallstreetbets/comments/1xsyjq5/comment/19sg6obswrnup/) |
| MSTR | 2026-11-10 19:20 | mention spike | 10 | 4.57 | 7 | 0 | wallstreetbets 10 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xsp9vp/) |
| TTD | 2026-11-09 21:11 | mention spike | 11 | 8.0 | 10 | 0 | wallstreetbets 11 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xsv7pt/) |
| IVF | 2026-11-09 22:18 | mention spike | 0 |  | 0 | 0 |  | Nasdaq |  |  |
| RKLB | 2026-11-09 21:25 | mention spike | 64 | 36.14 | 46 | 0 | wallstreetbets 63, smallstreetbets 1 | Nasdaq |  | [link](https://www.reddit.com/r/smallstreetbets/comments/1xsxl8t/) |
| ASTS | 2026-11-09 22:33 | mention spike | 62 | 44.86 | 43 | 1 | wallstreetbets 62 | Nasdaq | #11 | [link](https://www.reddit.com/r/wallstreetbets/comments/1xsyjq5/comment/19sgeh58k324g/) |
| OMH | 2026-11-09 20:48 | mention spike | 14 | 3.43 | 9 | 0 | pennystocks 7, wallstreetbets 7 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xt1asn/) |
| TTWO | 2026-11-10 16:24 | mention spike | 23 | 11.43 | 19 | 0 | wallstreetbets 23 | Nasdaq | #4 | [link](https://www.reddit.com/r/wallstreetbets/comments/1xsyjq5/comment/19sggenu7kwp0/) |
| HIMS | 2026-11-09 21:25 | mention spike | 12 | 4.29 | 12 | 0 | wallstreetbets 12 | NYSE |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xsv7pt/) |
| GLD | 2026-11-10 17:08 | mention spike | 11 | 6.71 | 4 | 0 | wallstreetbets 11 | NYSE Arca |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xsk1rq/comment/19sfstj51nldw/) |
| CVS | 2026-11-09 13:52 | mention spike | 2 | 3.71 | 2 | 0 | wallstreetbets 2 | NYSE |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xrfbie/comment/19sg74jrxxv28/) |
| NYT | 2026-11-09 11:01 | mention spike | 10 | 3.57 | 10 | 0 | wallstreetbets 9, smallstreetbets 1 | NYSE |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xsq1s1/) |
| NNN | 2026-11-09 15:04 | mention spike | 7 | 6.29 | 6 | 0 | wallstreetbets 6, smallstreetbets 1 | NYSE |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xsyjq5/comment/19sgax8c2avsw/) |

Full history: `episodes.csv` (one row per first flag, with the numbers known at that moment).
