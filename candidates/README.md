# Stage 1 candidates

Updated 2026-10-16T16:15:20Z by run `38930352652`. A candidate is a ticker whose Reddit mentions (or hype-language
posts) in the last 24 hours jumped above its prior 7-day mean + 2 sd, with at least
10 mentions from 5 different authors. It stays listed until it goes
24 hours without a new flag. These are statistical flags, not accusations or advice.

| Ticker | Flagged since (UTC) | Why | Mentions 24h | Baseline/day | Authors | Hype posts | Subreddits | Exchange | StockTwits | Example |
|---|---|---|---|---|---|---|---|---|---|---|
| BETR | 2026-10-15 23:28 | mention spike | 10 | 0.29 | 5 | 1 | pennystocks 8, wallstreetbets 2 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1x6vy59/comment/pgzlywb/) |
| RCS | 2026-10-16 12:29 | mention spike | 13 | 0.0 | 12 | 0 | wallstreetbets 13 | NYSE |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1x73hxs/comment/ph4kk07/) |
| TSLA | 2026-10-16 07:11 | mention spike | 185 | 20.14 | 130 | 0 | wallstreetbets 183, smallstreetbets 2 | Nasdaq | #2 | [link](https://www.reddit.com/r/wallstreetbets/comments/1x7dg4r/) |
| USO | 2026-10-16 11:23 | mention spike | 19 | 5.43 | 7 | 0 | wallstreetbets 19 | NYSE Arca |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1x7c5j6/comment/ph4sge4/) |
| IBKR | 2026-10-16 13:35 | mention spike | 8 | 3.57 | 6 | 0 | wallstreetbets 7, pennystocks 1 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1x7chad/comment/ph3te0t/) |
| WETO | 2026-10-15 21:16 | mention spike | 8 | 2.0 | 5 | 0 | pennystocks 7, wallstreetbets 1 | Nasdaq |  | [link](https://www.reddit.com/r/pennystocks/comments/1x6bsmm/comment/pgz650o/) |
| DRMA | 2026-10-15 23:28 | mention spike | 3 | 1.29 | 2 | 0 | pennystocks 2, wallstreetbets 1 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1x7c5j6/comment/ph49pid/) |
| TSM | 2026-10-14 19:51 | mention spike | 14 | 18.14 | 13 | 0 | wallstreetbets 14 | NYSE |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1x7c5j6/comment/ph4e1ie/) |
| RKLB | 2026-10-14 19:24 | mention spike | 28 | 19.29 | 21 | 1 | wallstreetbets 28 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1x7c5j6/comment/ph4t89c/) |
| WMT | 2026-10-14 19:24 | mention spike | 3 | 5.0 | 3 | 0 | wallstreetbets 3 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1x7c5j6/comment/ph4lhx7/) |
| TLT | 2026-10-14 18:31 | mention spike | 11 | 11.43 | 8 | 0 | wallstreetbets 11 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1x7c5j6/comment/ph3xhrx/) |
| CRWV | 2026-10-13 03:58 | mention spike | 71 | 30.0 | 55 | 0 | wallstreetbets 70, smallstreetbets 1 | Nasdaq | #3 | [link](https://www.reddit.com/r/wallstreetbets/comments/1x77qv8/) |
| SOFI | 2026-10-14 18:18 | mention spike | 0 |  | 0 | 0 |  | Nasdaq |  |  |
| HOOD | 2026-10-14 20:04 | mention spike | 2 | 10.43 | 2 | 0 | wallstreetbets 2 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1x6vy59/comment/ph2rl4u/) |
| SOXS | 2026-10-15 15:04 | mention spike | 12 | 6.14 | 9 | 0 | wallstreetbets 11, smallstreetbets 1 | NYSE Arca |  | [link](https://www.reddit.com/r/smallstreetbets/comments/1x7gy8a/) |

Full history: `episodes.csv` (one row per first flag, with the numbers known at that moment).
