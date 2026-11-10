# Stage 1 candidates

Updated 2026-11-10T13:59:07Z by run `42828396812`. A candidate is a ticker whose Reddit mentions (or hype-language
posts) in the last 24 hours jumped above its prior 7-day mean + 2 sd, with at least
10 mentions from 5 different authors. It stays listed until it goes
24 hours without a new flag. These are statistical flags, not accusations or advice.

| Ticker | Flagged since (UTC) | Why | Mentions 24h | Baseline/day | Authors | Hype posts | Subreddits | Exchange | StockTwits | Example |
|---|---|---|---|---|---|---|---|---|---|---|
| ASTS | 2026-11-09 22:33 | mention spike | 88 | 39.57 | 56 | 0 | wallstreetbets 88 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xpjj4e/comment/19sfesk02dlk4/) |
| CVS | 2026-11-09 13:52 | mention spike | 11 | 2.29 | 10 | 0 | wallstreetbets 11 | NYSE |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xrfbie/comment/19sf8vuyo16rp/) |
| HIMS | 2026-11-09 21:25 | mention spike | 21 | 1.71 | 17 | 0 | wallstreetbets 21 | NYSE | #15 | [link](https://www.reddit.com/r/wallstreetbets/comments/1xsk1rq/comment/19sfcfrmlei9v/) |
| IVF | 2026-11-09 22:18 | mention spike | 16 | 0.71 | 16 | 0 | wallstreetbets 15, smallstreetbets 1 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xs4ayj/comment/19se9z81pfzxg/) |
| NVDA | 2026-11-09 00:16 | mention spike | 920 | 275.29 | 552 | 0 | wallstreetbets 907, smallstreetbets 13 | Nasdaq | #7 | [link](https://www.reddit.com/r/wallstreetbets/comments/1xsmvag/) |
| OMH | 2026-11-09 20:48 | mention spike | 17 | 1.43 | 13 | 0 | wallstreetbets 11, pennystocks 6 | Nasdaq |  | [link](https://www.reddit.com/r/pennystocks/comments/1xse80g/comment/19sfb5rm713mt/) |
| RKLB | 2026-11-09 21:25 | mention spike | 136 | 21.14 | 76 | 2 | wallstreetbets 136 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xsdy48/) |
| TTD | 2026-11-09 21:11 | mention spike | 45 | 2.57 | 33 | 0 | wallstreetbets 45 | Nasdaq | #1 | [link](https://www.reddit.com/r/wallstreetbets/comments/1xsk1rq/comment/19sfe8l7tz5s0/) |
| NYT | 2026-11-09 11:01 | mention spike | 9 | 2.57 | 9 | 0 | wallstreetbets 8, smallstreetbets 1 | NYSE |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xsik05/comment/19sfag03fc5a9/) |
| NNN | 2026-11-09 15:04 | mention spike | 12 | 5.71 | 9 | 0 | wallstreetbets 11, smallstreetbets 1 | NYSE |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xsct7h/) |
| ASML | 2026-11-09 22:18 | mention spike | 1 | 3.43 | 1 | 0 | smallstreetbets 1 | Nasdaq |  | [link](https://www.reddit.com/r/smallstreetbets/comments/1xrurrh/comment/19se8zgthwtlv/) |
| ONDS | 2026-11-09 20:48 | mention spike | 9 | 3.71 | 6 | 0 | wallstreetbets 8, pennystocks 1 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xs3lzi/comment/19sejep6ua8gy/) |
| MSS | 2026-11-09 23:23 | mention spike | 5 | 0.86 | 3 | 0 | wallstreetbets 5 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xs3lzi/comment/19selz71ip5r4/) |
| AVGO | 2026-11-09 15:56 | mention spike | 20 | 12.86 | 15 | 0 | wallstreetbets 20 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xsjfsh/comment/19sfbtphxs30i/) |

Full history: `episodes.csv` (one row per first flag, with the numbers known at that moment).
