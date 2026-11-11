# Stage 1 candidates

Updated 2026-11-11T01:19:47Z by run `42936826726`. A candidate is a ticker whose Reddit mentions (or hype-language
posts) in the last 24 hours jumped above its prior 7-day mean + 2 sd, with at least
10 mentions from 5 different authors. It stays listed until it goes
24 hours without a new flag. These are statistical flags, not accusations or advice.

| Ticker | Flagged since (UTC) | Why | Mentions 24h | Baseline/day | Authors | Hype posts | Subreddits | Exchange | StockTwits | Example |
|---|---|---|---|---|---|---|---|---|---|---|
| ANT | 2026-11-10 14:52 | mention spike | 113 | 24.14 | 81 | 0 | wallstreetbets 113 | ? |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xt1f1n/) |
| AVGO | 2026-11-09 15:56 | mention spike | 32 | 13.29 | 26 | 0 | wallstreetbets 32 | Nasdaq | #23 | [link](https://www.reddit.com/r/wallstreetbets/comments/1xsyjq5/comment/19sg8uz47qe83/) |
| CRWV | 2026-11-10 20:00 | mention spike | 349 | 31.0 | 168 | 2 | wallstreetbets 349 | Nasdaq | #1 | [link](https://www.reddit.com/r/wallstreetbets/comments/1xt13eq/) |
| GEV | 2026-11-10 15:44 | mention spike | 13 | 3.0 | 10 | 0 | wallstreetbets 13 | NYSE |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xsk1rq/comment/19sfy460aog00/) |
| RGTI | 2026-11-10 21:21 | mention spike | 18 | 2.43 | 12 | 0 | wallstreetbets 18 | Nasdaq | #3 | [link](https://www.reddit.com/r/wallstreetbets/comments/1xsyjq5/comment/19sg6obswrnup/) |
| MSTR | 2026-11-10 19:20 | mention spike | 9 | 4.71 | 7 | 0 | wallstreetbets 9 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xsp9vp/) |
| TTD | 2026-11-09 21:11 | mention spike | 12 | 7.86 | 11 | 0 | wallstreetbets 12 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xsv7pt/) |
| IVF | 2026-11-09 22:18 | mention spike | 0 |  | 0 | 0 |  | Nasdaq |  |  |
| RKLB | 2026-11-09 21:25 | mention spike | 63 | 35.71 | 46 | 1 | wallstreetbets 62, smallstreetbets 1 | Nasdaq |  | [link](https://www.reddit.com/r/smallstreetbets/comments/1xsxl8t/) |
| ASTS | 2026-11-09 22:33 | mention spike | 67 | 44.14 | 49 | 1 | wallstreetbets 67 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xsyjq5/comment/19sg5gfxc8683/) |
| OMH | 2026-11-09 20:48 | mention spike | 13 | 3.43 | 8 | 0 | pennystocks 7, wallstreetbets 6 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xt1asn/) |
| TTWO | 2026-11-10 16:24 | mention spike | 18 | 11.57 | 16 | 0 | wallstreetbets 18 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xsyjq5/comment/19sg3nxtsu4ck/) |
| HIMS | 2026-11-09 21:25 | mention spike | 13 | 4.14 | 13 | 0 | wallstreetbets 13 | NYSE | #15 | [link](https://www.reddit.com/r/wallstreetbets/comments/1xsv7pt/) |
| GLD | 2026-11-10 17:08 | mention spike | 11 | 6.71 | 4 | 0 | wallstreetbets 11 | NYSE Arca |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xsk1rq/comment/19sfstj51nldw/) |
| CVS | 2026-11-09 13:52 | mention spike | 3 | 3.57 | 3 | 0 | wallstreetbets 3 | NYSE |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xrfbie/comment/19sg74jrxxv28/) |
| NVDA | 2026-11-09 00:16 | mention spike | 1231 | 368.86 | 644 | 2 | wallstreetbets 1223, smallstreetbets 8 | Nasdaq | #7 | [link](https://www.reddit.com/r/wallstreetbets/comments/1xt31p8/) |
| NYT | 2026-11-09 11:01 | mention spike | 10 | 3.43 | 10 | 0 | wallstreetbets 9, smallstreetbets 1 | NYSE |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xsq1s1/) |
| NNN | 2026-11-09 15:04 | mention spike | 9 | 5.71 | 7 | 0 | wallstreetbets 8, smallstreetbets 1 | NYSE |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xsct7h/) |
| ASML | 2026-11-09 22:18 | mention spike | 5 | 3.29 | 4 | 0 | wallstreetbets 5 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xspyjp/comment/19sg20lq2ifwh/) |

Full history: `episodes.csv` (one row per first flag, with the numbers known at that moment).
