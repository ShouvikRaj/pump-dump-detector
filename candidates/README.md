# Stage 1 candidates

Updated 2026-11-10T06:50:09Z by run `42770812916`. A candidate is a ticker whose Reddit mentions (or hype-language
posts) in the last 24 hours jumped above its prior 7-day mean + 2 sd, with at least
10 mentions from 5 different authors. It stays listed until it goes
24 hours without a new flag. These are statistical flags, not accusations or advice.

| Ticker | Flagged since (UTC) | Why | Mentions 24h | Baseline/day | Authors | Hype posts | Subreddits | Exchange | StockTwits | Example |
|---|---|---|---|---|---|---|---|---|---|---|
| ASTS | 2026-11-09 22:33 | mention spike | 85 | 40.0 | 56 | 0 | wallstreetbets 85 | Nasdaq | #8 | [link](https://www.reddit.com/r/wallstreetbets/comments/1xs3lzi/comment/19seozh7lg8dh/) |
| CVS | 2026-11-09 13:52 | mention spike | 16 | 1.43 | 15 | 0 | wallstreetbets 16 | NYSE |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xrfbie/comment/19sei8viswold/) |
| HIMS | 2026-11-09 21:25 | mention spike | 18 | 1.71 | 14 | 0 | wallstreetbets 18 | NYSE | #5 | [link](https://www.reddit.com/r/wallstreetbets/comments/1xs3lzi/comment/19sengu1n5qao/) |
| IVF | 2026-11-09 22:18 | mention spike | 17 | 0.57 | 17 | 0 | wallstreetbets 16, smallstreetbets 1 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xs4ayj/comment/19se9z81pfzxg/) |
| NNN | 2026-11-09 15:04 | mention spike | 18 | 4.71 | 15 | 0 | wallstreetbets 18 | NYSE |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xsct7h/) |
| NVDA | 2026-11-09 00:16 | mention spike | 1143 | 235.57 | 634 | 0 | wallstreetbets 1127, smallstreetbets 16 | Nasdaq | #30 | [link](https://www.reddit.com/r/smallstreetbets/comments/1xsfg6v/) |
| OMH | 2026-11-09 20:48 | mention spike | 16 | 1.14 | 14 | 0 | wallstreetbets 9, pennystocks 7 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xs3lzi/comment/19sebk3yv28o4/) |
| RKLB | 2026-11-09 21:25 | mention spike | 128 | 21.57 | 71 | 2 | wallstreetbets 128 | Nasdaq | #13 | [link](https://www.reddit.com/r/wallstreetbets/comments/1xsdy48/) |
| TTD | 2026-11-09 21:11 | mention spike | 42 | 2.0 | 28 | 0 | wallstreetbets 42 | Nasdaq | #2 | [link](https://www.reddit.com/r/wallstreetbets/comments/1xs3lzi/comment/19sei2raj6cf9/) |
| NYT | 2026-11-09 11:01 | mention spike | 9 | 2.29 | 9 | 0 | wallstreetbets 9 | NYSE |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xrrwsf/) |
| ASML | 2026-11-09 22:18 | mention spike | 8 | 2.43 | 7 | 0 | wallstreetbets 7, smallstreetbets 1 | Nasdaq |  | [link](https://www.reddit.com/r/smallstreetbets/comments/1xrurrh/comment/19se8zgthwtlv/) |
| ONDS | 2026-11-09 20:48 | mention spike | 9 | 3.71 | 6 | 0 | wallstreetbets 8, pennystocks 1 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xs3lzi/comment/19sejep6ua8gy/) |
| MSS | 2026-11-09 23:23 | mention spike | 7 | 0.57 | 5 | 0 | wallstreetbets 7 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xs3lzi/comment/19selz71ip5r4/) |
| AVGO | 2026-11-09 15:56 | mention spike | 16 | 12.86 | 14 | 0 | wallstreetbets 16 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xs4ylt/comment/19seeb52rh3gk/) |

Full history: `episodes.csv` (one row per first flag, with the numbers known at that moment).
