# Stage 1 candidates

Updated 2026-11-15T23:58:07Z by run `43777251366`. A candidate is a ticker whose Reddit mentions (or hype-language
posts) in the last 24 hours jumped above its prior 7-day mean + 2 sd, with at least
10 mentions from 5 different authors. It stays listed until it goes
24 hours without a new flag. These are statistical flags, not accusations or advice.

| Ticker | Flagged since (UTC) | Why | Mentions 24h | Baseline/day | Authors | Hype posts | Subreddits | Exchange | StockTwits | Example |
|---|---|---|---|---|---|---|---|---|---|---|
| ASML | 2026-11-15 23:05 | mention spike | 17 | 5.86 | 16 | 0 | wallstreetbets 17 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xwa164/comment/19sp0fwp4wjl0/) |
| DXYZ | 2026-11-14 23:53 | mention spike | 17 | 3.71 | 16 | 0 | wallstreetbets 17 | NYSE |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xx3xel/comment/19sotc11qa6kj/) |
| MSTR | 2026-11-13 06:20 | mention spike | 19 | 10.43 | 15 | 0 | wallstreetbets 19 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xx6mql/comment/19sp2pbdw6rus/) |
| COIN | 2026-11-15 21:05 | mention spike | 9 | 0.86 | 8 | 1 | wallstreetbets 9 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xwesfj/comment/19souzj7ihpgl/) |
| TSM | 2026-11-15 07:52 | mention spike | 2 | 8.57 | 2 | 0 | wallstreetbets 2 | NYSE |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xwhukf/comment/19soj7mygicbk/) |
| LHX | 2026-11-14 03:08 | mention spike | 1 | 3.14 | 1 | 0 | wallstreetbets 1 | NYSE | #23 | [link](https://www.reddit.com/r/wallstreetbets/comments/1xvjlim/comment/19sotl24p2e6c/) |
| ATC | 2026-11-13 22:10 | mention spike | 1 | 11.71 | 1 | 0 | wallstreetbets 1 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xwgsga/comment/19snenbqh4tlw/) |

Full history: `episodes.csv` (one row per first flag, with the numbers known at that moment).
