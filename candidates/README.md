# Stage 1 candidates

Updated 2026-11-16T13:08:11Z by run `43871091751`. A candidate is a ticker whose Reddit mentions (or hype-language
posts) in the last 24 hours jumped above its prior 7-day mean + 2 sd, with at least
10 mentions from 5 different authors. It stays listed until it goes
24 hours without a new flag. These are statistical flags, not accusations or advice.

| Ticker | Flagged since (UTC) | Why | Mentions 24h | Baseline/day | Authors | Hype posts | Subreddits | Exchange | StockTwits | Example |
|---|---|---|---|---|---|---|---|---|---|---|
| WMT | 2026-11-16 07:17 | mention spike | 13 | 3.29 | 13 | 0 | wallstreetbets 13 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xwwq7f/) |
| ASML | 2026-11-15 23:05 | mention spike | 3 | 7.86 | 3 | 0 | wallstreetbets 3 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xwa164/comment/19sp0fwp4wjl0/) |
| DXYZ | 2026-11-14 23:53 | mention spike | 5 | 5.86 | 5 | 0 | wallstreetbets 5 | NYSE |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xwft7z/comment/19spfi8w8u9fm/) |
| MSTR | 2026-11-13 06:20 | mention spike | 18 | 12.0 | 14 | 0 | wallstreetbets 18 | Nasdaq | #12 | [link](https://www.reddit.com/r/wallstreetbets/comments/1xxmkhj/comment/19spxk5q9f6bn/) |
| COIN | 2026-11-15 21:05 | mention spike | 8 | 1.43 | 7 | 1 | wallstreetbets 8 | Nasdaq | #10 | [link](https://www.reddit.com/r/wallstreetbets/comments/1xxmkhj/comment/19sq1ztdeowxv/) |

Full history: `episodes.csv` (one row per first flag, with the numbers known at that moment).
