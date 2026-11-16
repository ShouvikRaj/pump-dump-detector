# Stage 1 candidates

Updated 2026-11-16T01:46:24Z by run `43787566620`. A candidate is a ticker whose Reddit mentions (or hype-language
posts) in the last 24 hours jumped above its prior 7-day mean + 2 sd, with at least
10 mentions from 5 different authors. It stays listed until it goes
24 hours without a new flag. These are statistical flags, not accusations or advice.

| Ticker | Flagged since (UTC) | Why | Mentions 24h | Baseline/day | Authors | Hype posts | Subreddits | Exchange | StockTwits | Example |
|---|---|---|---|---|---|---|---|---|---|---|
| ASML | 2026-11-15 23:05 | mention spike | 16 | 6.0 | 15 | 0 | wallstreetbets 16 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xwa164/comment/19sp0fwp4wjl0/) |
| DXYZ | 2026-11-14 23:53 | mention spike | 12 | 4.57 | 12 | 0 | wallstreetbets 12 | NYSE | #17 | [link](https://www.reddit.com/r/wallstreetbets/comments/1xwft7z/comment/19sp7g5soauyq/) |
| MSTR | 2026-11-13 06:20 | mention spike | 21 | 10.71 | 16 | 0 | wallstreetbets 21 | Nasdaq | #8 | [link](https://www.reddit.com/r/wallstreetbets/comments/1xx6mql/comment/19sp7dpb3sqyp/) |
| COIN | 2026-11-15 21:05 | mention spike | 8 | 1.0 | 7 | 1 | wallstreetbets 8 | Nasdaq | #29 | [link](https://www.reddit.com/r/wallstreetbets/comments/1xwesfj/comment/19souzj7ihpgl/) |
| TSM | 2026-11-15 07:52 | mention spike | 3 | 8.57 | 3 | 0 | wallstreetbets 3 | NYSE |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xx3xel/comment/19sp4le1yfo3p/) |
| LHX | 2026-11-14 03:08 | mention spike | 1 | 3.14 | 1 | 0 | wallstreetbets 1 | NYSE |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xvjlim/comment/19sotl24p2e6c/) |
| ATC | 2026-11-13 22:10 | mention spike | 0 |  | 0 | 0 |  | Nasdaq |  |  |

Full history: `episodes.csv` (one row per first flag, with the numbers known at that moment).
