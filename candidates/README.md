# Stage 1 candidates

Updated 2026-11-10T12:52:07Z by run `42818433523`. A candidate is a ticker whose Reddit mentions (or hype-language
posts) in the last 24 hours jumped above its prior 7-day mean + 2 sd, with at least
10 mentions from 5 different authors. It stays listed until it goes
24 hours without a new flag. These are statistical flags, not accusations or advice.

| Ticker | Flagged since (UTC) | Why | Mentions 24h | Baseline/day | Authors | Hype posts | Subreddits | Exchange | StockTwits | Example |
|---|---|---|---|---|---|---|---|---|---|---|
| ASTS | 2026-11-09 22:33 | mention spike | 89 | 39.86 | 58 | 0 | wallstreetbets 89 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xsk1rq/comment/19sfbzhckcmis/) |
| CVS | 2026-11-09 13:52 | mention spike | 14 | 1.86 | 13 | 0 | wallstreetbets 14 | NYSE |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xrfbie/comment/19sf8vuyo16rp/) |
| HIMS | 2026-11-09 21:25 | mention spike | 20 | 1.71 | 16 | 0 | wallstreetbets 20 | NYSE | #6 | [link](https://www.reddit.com/r/wallstreetbets/comments/1xsk1rq/comment/19sfa6a3f0tmq/) |
| IVF | 2026-11-09 22:18 | mention spike | 16 | 0.71 | 16 | 0 | wallstreetbets 15, smallstreetbets 1 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xs4ayj/comment/19se9z81pfzxg/) |
| NVDA | 2026-11-09 00:16 | mention spike | 979 | 264.86 | 577 | 0 | wallstreetbets 965, smallstreetbets 14 | Nasdaq | #10 | [link](https://www.reddit.com/r/wallstreetbets/comments/1xslgfr/) |
| NYT | 2026-11-09 11:01 | mention spike | 10 | 2.43 | 10 | 0 | wallstreetbets 9, smallstreetbets 1 | NYSE |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xrrwsf/) |
| OMH | 2026-11-09 20:48 | mention spike | 19 | 1.14 | 15 | 0 | wallstreetbets 11, pennystocks 8 | Nasdaq |  | [link](https://www.reddit.com/r/pennystocks/comments/1xse80g/comment/19sfb5rm713mt/) |
| RKLB | 2026-11-09 21:25 | mention spike | 131 | 21.29 | 73 | 2 | wallstreetbets 131 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xsdy48/) |
| TTD | 2026-11-09 21:11 | mention spike | 46 | 2.0 | 32 | 0 | wallstreetbets 46 | Nasdaq | #1 | [link](https://www.reddit.com/r/wallstreetbets/comments/1xsk1rq/comment/19sfb5wzsnksh/) |
| NNN | 2026-11-09 15:04 | mention spike | 12 | 5.71 | 9 | 0 | wallstreetbets 11, smallstreetbets 1 | NYSE |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xsct7h/) |
| ASML | 2026-11-09 22:18 | mention spike | 2 | 3.29 | 2 | 0 | smallstreetbets 1, wallstreetbets 1 | Nasdaq |  | [link](https://www.reddit.com/r/smallstreetbets/comments/1xrurrh/comment/19se8zgthwtlv/) |
| ONDS | 2026-11-09 20:48 | mention spike | 9 | 3.71 | 6 | 0 | wallstreetbets 8, pennystocks 1 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xs3lzi/comment/19sejep6ua8gy/) |
| MSS | 2026-11-09 23:23 | mention spike | 5 | 0.86 | 3 | 0 | wallstreetbets 5 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xs3lzi/comment/19selz71ip5r4/) |
| AVGO | 2026-11-09 15:56 | mention spike | 20 | 13.14 | 15 | 0 | wallstreetbets 20 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xsjfsh/comment/19sfbtphxs30i/) |

Full history: `episodes.csv` (one row per first flag, with the numbers known at that moment).
