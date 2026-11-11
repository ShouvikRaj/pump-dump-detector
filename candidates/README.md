# Stage 1 candidates

Updated 2026-11-11T00:14:08Z by run `42928245416`. A candidate is a ticker whose Reddit mentions (or hype-language
posts) in the last 24 hours jumped above its prior 7-day mean + 2 sd, with at least
10 mentions from 5 different authors. It stays listed until it goes
24 hours without a new flag. These are statistical flags, not accusations or advice.

| Ticker | Flagged since (UTC) | Why | Mentions 24h | Baseline/day | Authors | Hype posts | Subreddits | Exchange | StockTwits | Example |
|---|---|---|---|---|---|---|---|---|---|---|
| ANT | 2026-11-10 14:52 | mention spike | 111 | 23.86 | 80 | 0 | wallstreetbets 111 | ? |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xt1f1n/) |
| AVGO | 2026-11-09 15:56 | mention spike | 30 | 13.43 | 24 | 0 | wallstreetbets 30 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xsyjq5/comment/19sg49cxy5i80/) |
| CRWV | 2026-11-10 20:00 | mention spike | 341 | 31.0 | 165 | 2 | wallstreetbets 341 | Nasdaq | #1 | [link](https://www.reddit.com/r/wallstreetbets/comments/1xt13eq/) |
| GEV | 2026-11-10 15:44 | mention spike | 13 | 3.0 | 10 | 0 | wallstreetbets 13 | NYSE |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xsk1rq/comment/19sfy460aog00/) |
| RGTI | 2026-11-10 21:21 | mention spike | 17 | 2.43 | 12 | 0 | wallstreetbets 17 | Nasdaq | #5 | [link](https://www.reddit.com/r/wallstreetbets/comments/1xsyjq5/comment/19sfzgetac802/) |
| MSTR | 2026-11-10 19:20 | mention spike | 10 | 4.57 | 8 | 0 | wallstreetbets 10 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xsp9vp/) |
| TTD | 2026-11-09 21:11 | mention spike | 16 | 7.29 | 15 | 0 | wallstreetbets 16 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xsv7pt/) |
| IVF | 2026-11-09 22:18 | mention spike | 0 |  | 0 | 0 |  | Nasdaq |  |  |
| RKLB | 2026-11-09 21:25 | mention spike | 65 | 35.43 | 48 | 1 | wallstreetbets 64, smallstreetbets 1 | Nasdaq |  | [link](https://www.reddit.com/r/smallstreetbets/comments/1xsxl8t/) |
| ASTS | 2026-11-09 22:33 | mention spike | 68 | 45.43 | 50 | 1 | wallstreetbets 68 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xsyjq5/comment/19sg5gfxc8683/) |
| OMH | 2026-11-09 20:48 | mention spike | 13 | 3.43 | 8 | 0 | pennystocks 7, wallstreetbets 6 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xt1asn/) |
| TTWO | 2026-11-10 16:24 | mention spike | 18 | 11.57 | 16 | 0 | wallstreetbets 18 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xsyjq5/comment/19sg3nxtsu4ck/) |
| HIMS | 2026-11-09 21:25 | mention spike | 12 | 4.14 | 12 | 0 | wallstreetbets 12 | NYSE | #18 | [link](https://www.reddit.com/r/wallstreetbets/comments/1xsv7pt/) |
| GLD | 2026-11-10 17:08 | mention spike | 11 | 6.71 | 4 | 0 | wallstreetbets 11 | NYSE Arca |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xsk1rq/comment/19sfstj51nldw/) |
| CVS | 2026-11-09 13:52 | mention spike | 3 | 3.43 | 3 | 0 | wallstreetbets 3 | NYSE |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xrfbie/comment/19sf8vuyo16rp/) |
| NVDA | 2026-11-09 00:16 | mention spike | 1223 | 364.29 | 639 | 2 | wallstreetbets 1214, smallstreetbets 9 | Nasdaq | #4 | [link](https://www.reddit.com/r/wallstreetbets/comments/1xt31p8/) |
| NYT | 2026-11-09 11:01 | mention spike | 10 | 3.29 | 10 | 0 | wallstreetbets 9, smallstreetbets 1 | NYSE |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xsq1s1/) |
| NNN | 2026-11-09 15:04 | mention spike | 10 | 5.71 | 8 | 0 | wallstreetbets 9, smallstreetbets 1 | NYSE |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xsct7h/) |
| ASML | 2026-11-09 22:18 | mention spike | 5 | 3.43 | 4 | 0 | wallstreetbets 5 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xspyjp/comment/19sg20lq2ifwh/) |
| ONDS | 2026-11-09 20:48 | mention spike | 3 | 4.57 | 3 | 0 | wallstreetbets 3 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xsk1rq/comment/19sfrbhlipyiq/) |

Full history: `episodes.csv` (one row per first flag, with the numbers known at that moment).
