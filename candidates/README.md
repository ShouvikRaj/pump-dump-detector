# Stage 1 candidates

Updated 2026-10-16T17:34:51Z by run `38940648250`. A candidate is a ticker whose Reddit mentions (or hype-language
posts) in the last 24 hours jumped above its prior 7-day mean + 2 sd, with at least
10 mentions from 5 different authors. It stays listed until it goes
24 hours without a new flag. These are statistical flags, not accusations or advice.

| Ticker | Flagged since (UTC) | Why | Mentions 24h | Baseline/day | Authors | Hype posts | Subreddits | Exchange | StockTwits | Example |
|---|---|---|---|---|---|---|---|---|---|---|
| BETR | 2026-10-15 23:28 | mention spike | 10 | 0.29 | 5 | 1 | pennystocks 8, wallstreetbets 2 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1x6vy59/comment/pgzlywb/) |
| RCS | 2026-10-16 12:29 | mention spike | 13 | 0.0 | 12 | 0 | wallstreetbets 13 | NYSE |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1x73hxs/comment/ph4kk07/) |
| TSLA | 2026-10-16 07:11 | mention spike | 206 | 20.14 | 144 | 0 | wallstreetbets 204, smallstreetbets 2 | Nasdaq | #1 | [link](https://www.reddit.com/r/wallstreetbets/comments/1x7mejt/) |
| USO | 2026-10-16 11:23 | mention spike | 23 | 5.29 | 11 | 0 | wallstreetbets 23 | NYSE Arca | #12 | [link](https://www.reddit.com/r/wallstreetbets/comments/1x7c5j6/comment/ph5b487/) |
| IBKR | 2026-10-16 13:35 | mention spike | 8 | 3.71 | 6 | 0 | wallstreetbets 8 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1x7c5j6/comment/ph541ns/) |
| WETO | 2026-10-15 21:16 | mention spike | 8 | 2.0 | 5 | 0 | pennystocks 7, wallstreetbets 1 | Nasdaq |  | [link](https://www.reddit.com/r/pennystocks/comments/1x6bsmm/comment/pgz650o/) |
| DRMA | 2026-10-15 23:28 | mention spike | 3 | 1.29 | 2 | 0 | pennystocks 2, wallstreetbets 1 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1x7c5j6/comment/ph49pid/) |
| TSM | 2026-10-14 19:51 | mention spike | 16 | 17.57 | 14 | 0 | wallstreetbets 16 | NYSE |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1x7c5j6/comment/ph5cljw/) |
| RKLB | 2026-10-14 19:24 | mention spike | 29 | 19.57 | 22 | 1 | wallstreetbets 29 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1x7l36z/) |
| WMT | 2026-10-14 19:24 | mention spike | 2 | 5.0 | 2 | 0 | wallstreetbets 2 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1x7c5j6/comment/ph4lhx7/) |
| TLT | 2026-10-14 18:31 | mention spike | 10 | 12.14 | 8 | 0 | wallstreetbets 10 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1x7c5j6/comment/ph5a201/) |
| CRWV | 2026-10-13 03:58 | mention spike | 89 | 30.29 | 63 | 0 | wallstreetbets 89 | Nasdaq | #7 | [link](https://www.reddit.com/r/wallstreetbets/comments/1x77qv8/) |

Full history: `episodes.csv` (one row per first flag, with the numbers known at that moment).
