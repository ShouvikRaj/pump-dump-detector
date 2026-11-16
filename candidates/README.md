# Stage 1 candidates

Updated 2026-11-16T12:10:11Z by run `43863066225`. A candidate is a ticker whose Reddit mentions (or hype-language
posts) in the last 24 hours jumped above its prior 7-day mean + 2 sd, with at least
10 mentions from 5 different authors. It stays listed until it goes
24 hours without a new flag. These are statistical flags, not accusations or advice.

| Ticker | Flagged since (UTC) | Why | Mentions 24h | Baseline/day | Authors | Hype posts | Subreddits | Exchange | StockTwits | Example |
|---|---|---|---|---|---|---|---|---|---|---|
| WMT | 2026-11-16 07:17 | mention spike | 13 | 3.29 | 13 | 0 | wallstreetbets 13 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xwwq7f/) |
| ASML | 2026-11-15 23:05 | mention spike | 3 | 7.86 | 3 | 0 | wallstreetbets 3 | Nasdaq | #23 | [link](https://www.reddit.com/r/wallstreetbets/comments/1xwa164/comment/19sp0fwp4wjl0/) |
| DXYZ | 2026-11-14 23:53 | mention spike | 6 | 5.71 | 6 | 0 | wallstreetbets 6 | NYSE | #12 | [link](https://www.reddit.com/r/wallstreetbets/comments/1xwft7z/comment/19spfi8w8u9fm/) |
| MSTR | 2026-11-13 06:20 | mention spike | 18 | 12.0 | 14 | 0 | wallstreetbets 18 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xxmkhj/comment/19spxk5q9f6bn/) |
| COIN | 2026-11-15 21:05 | mention spike | 6 | 1.43 | 5 | 1 | wallstreetbets 6 | Nasdaq | #29 | [link](https://www.reddit.com/r/wallstreetbets/comments/1xx6mql/comment/19spokxwna3d0/) |
| TSM | 2026-11-15 07:52 | mention spike | 5 | 8.43 | 5 | 0 | wallstreetbets 5 | NYSE |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xx6mql/comment/19spso3cx3mo1/) |

Full history: `episodes.csv` (one row per first flag, with the numbers known at that moment).
