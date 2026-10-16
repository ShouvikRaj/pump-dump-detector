# Stage 1 candidates

Updated 2026-10-16T18:27:56Z by run `38947396872`. A candidate is a ticker whose Reddit mentions (or hype-language
posts) in the last 24 hours jumped above its prior 7-day mean + 2 sd, with at least
10 mentions from 5 different authors. It stays listed until it goes
24 hours without a new flag. These are statistical flags, not accusations or advice.

| Ticker | Flagged since (UTC) | Why | Mentions 24h | Baseline/day | Authors | Hype posts | Subreddits | Exchange | StockTwits | Example |
|---|---|---|---|---|---|---|---|---|---|---|
| BETR | 2026-10-15 23:28 | mention spike | 10 | 0.29 | 5 | 1 | pennystocks 8, wallstreetbets 2 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1x6vy59/comment/pgzlywb/) |
| RCS | 2026-10-16 12:29 | mention spike | 13 | 0.0 | 12 | 0 | wallstreetbets 13 | NYSE |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1x73hxs/comment/ph4kk07/) |
| TSLA | 2026-10-16 07:11 | mention spike | 213 | 19.86 | 147 | 0 | wallstreetbets 211, smallstreetbets 2 | Nasdaq | #3 | [link](https://www.reddit.com/r/wallstreetbets/comments/1x7mqih/) |
| USO | 2026-10-16 11:23 | mention spike | 25 | 5.14 | 13 | 0 | wallstreetbets 25 | NYSE Arca | #25 | [link](https://www.reddit.com/r/wallstreetbets/comments/1x7c5j6/comment/ph5ktgf/) |
| QQQ | 2026-10-16 18:27 | mention spike | 150 | 66.57 | 88 | 0 | wallstreetbets 150 | Nasdaq | #1 | [link](https://www.reddit.com/r/wallstreetbets/comments/1x7c5j6/comment/ph5qj7s/) |
| IBKR | 2026-10-16 13:35 | mention spike | 8 | 3.71 | 6 | 0 | wallstreetbets 8 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1x7c5j6/comment/ph541ns/) |
| WETO | 2026-10-15 21:16 | mention spike | 7 | 2.14 | 5 | 0 | pennystocks 6, wallstreetbets 1 | Nasdaq |  | [link](https://www.reddit.com/r/pennystocks/comments/1x6bsmm/comment/pgz650o/) |
| DRMA | 2026-10-15 23:28 | mention spike | 3 | 1.29 | 2 | 0 | pennystocks 2, wallstreetbets 1 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1x7c5j6/comment/ph49pid/) |
| TSM | 2026-10-14 19:51 | mention spike | 16 | 17.57 | 14 | 0 | wallstreetbets 16 | NYSE |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1x7c5j6/comment/ph5cljw/) |
| RKLB | 2026-10-14 19:24 | mention spike | 32 | 19.57 | 24 | 1 | wallstreetbets 32 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1x7l36z/) |
| WMT | 2026-10-14 19:24 | mention spike | 2 | 5.0 | 2 | 0 | wallstreetbets 2 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1x7c5j6/comment/ph4lhx7/) |
| TLT | 2026-10-14 18:31 | mention spike | 12 | 12.0 | 8 | 0 | wallstreetbets 12 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1x7c5j6/comment/ph5j614/) |

Full history: `episodes.csv` (one row per first flag, with the numbers known at that moment).
