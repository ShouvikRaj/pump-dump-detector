# Stage 1 candidates

Updated 2026-11-16T03:33:12Z by run `43798136273`. A candidate is a ticker whose Reddit mentions (or hype-language
posts) in the last 24 hours jumped above its prior 7-day mean + 2 sd, with at least
10 mentions from 5 different authors. It stays listed until it goes
24 hours without a new flag. These are statistical flags, not accusations or advice.

| Ticker | Flagged since (UTC) | Why | Mentions 24h | Baseline/day | Authors | Hype posts | Subreddits | Exchange | StockTwits | Example |
|---|---|---|---|---|---|---|---|---|---|---|
| ASML | 2026-11-15 23:05 | mention spike | 13 | 6.43 | 13 | 0 | wallstreetbets 13 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xwa164/comment/19sp0fwp4wjl0/) |
| DXYZ | 2026-11-14 23:53 | mention spike | 11 | 4.71 | 11 | 0 | wallstreetbets 11 | NYSE |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xwft7z/comment/19sp7g5soauyq/) |
| MSTR | 2026-11-13 06:20 | mention spike | 20 | 11.29 | 13 | 0 | wallstreetbets 20 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xx6mql/comment/19spch0262ohu/) |
| COIN | 2026-11-15 21:05 | mention spike | 6 | 1.29 | 5 | 1 | wallstreetbets 6 | Nasdaq | #14 | [link](https://www.reddit.com/r/wallstreetbets/comments/1xwesfj/comment/19souzj7ihpgl/) |
| TSM | 2026-11-15 07:52 | mention spike | 3 | 8.57 | 3 | 0 | wallstreetbets 3 | NYSE |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xx3xel/comment/19sp4le1yfo3p/) |

Full history: `episodes.csv` (one row per first flag, with the numbers known at that moment).
