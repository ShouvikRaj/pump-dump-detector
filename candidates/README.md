# Stage 1 candidates

Updated 2026-11-16T07:41:09Z by run `43825175017`. A candidate is a ticker whose Reddit mentions (or hype-language
posts) in the last 24 hours jumped above its prior 7-day mean + 2 sd, with at least
10 mentions from 5 different authors. It stays listed until it goes
24 hours without a new flag. These are statistical flags, not accusations or advice.

| Ticker | Flagged since (UTC) | Why | Mentions 24h | Baseline/day | Authors | Hype posts | Subreddits | Exchange | StockTwits | Example |
|---|---|---|---|---|---|---|---|---|---|---|
| WMT | 2026-11-16 07:17 | mention spike | 10 | 3.29 | 10 | 0 | wallstreetbets 10 | Nasdaq | #19 | [link](https://www.reddit.com/r/wallstreetbets/comments/1xwwq7f/) |
| ASML | 2026-11-15 23:05 | mention spike | 6 | 7.43 | 6 | 0 | wallstreetbets 6 | Nasdaq | #10 | [link](https://www.reddit.com/r/wallstreetbets/comments/1xwa164/comment/19sp0fwp4wjl0/) |
| DXYZ | 2026-11-14 23:53 | mention spike | 10 | 5.14 | 10 | 0 | wallstreetbets 10 | NYSE | #28 | [link](https://www.reddit.com/r/wallstreetbets/comments/1xwft7z/comment/19spfi8w8u9fm/) |
| MSTR | 2026-11-13 06:20 | mention spike | 19 | 11.71 | 13 | 0 | wallstreetbets 19 | Nasdaq | #1 | [link](https://www.reddit.com/r/wallstreetbets/comments/1xx6mql/comment/19spk5jmv1nyb/) |
| COIN | 2026-11-15 21:05 | mention spike | 6 | 1.29 | 5 | 1 | wallstreetbets 6 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xwesfj/comment/19souzj7ihpgl/) |
| TSM | 2026-11-15 07:52 | mention spike | 4 | 8.43 | 4 | 0 | wallstreetbets 4 | NYSE |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xx6mql/comment/19spfu5m17z43/) |

Full history: `episodes.csv` (one row per first flag, with the numbers known at that moment).
