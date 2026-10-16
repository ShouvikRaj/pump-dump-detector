# Stage 1 candidates

Updated 2026-10-16T13:49:13Z by run `38910702776`. A candidate is a ticker whose Reddit mentions (or hype-language
posts) in the last 24 hours jumped above its prior 7-day mean + 2 sd, with at least
10 mentions from 5 different authors. It stays listed until it goes
24 hours without a new flag. These are statistical flags, not accusations or advice.

| Ticker | Flagged since (UTC) | Why | Mentions 24h | Baseline/day | Authors | Hype posts | Subreddits | Exchange | StockTwits | Example |
|---|---|---|---|---|---|---|---|---|---|---|
| BETR | 2026-10-15 23:28 | mention spike | 11 | 0.14 | 5 | 1 | pennystocks 9, wallstreetbets 2 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1x6vy59/comment/pgzlywb/) |
| DRMA | 2026-10-15 23:28 | mention spike | 10 | 0.14 | 5 | 0 | pennystocks 10 | Nasdaq |  | [link](https://www.reddit.com/r/pennystocks/comments/1x6bsmm/comment/pgzqmfi/) |
| IBKR | 2026-10-16 13:35 | mention spike | 10 | 3.29 | 7 | 0 | wallstreetbets 9, pennystocks 1 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1x7chad/comment/ph3te0t/) |
| RCS | 2026-10-16 12:29 | mention spike | 10 | 0.0 | 9 | 0 | wallstreetbets 10 | NYSE |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1x73hxs/comment/ph3f680/) |
| TSLA | 2026-10-16 07:11 | mention spike | 134 | 18.57 | 101 | 0 | wallstreetbets 132, smallstreetbets 2 | Nasdaq | #1 | [link](https://www.reddit.com/r/wallstreetbets/comments/1x7dg4r/) |
| USO | 2026-10-16 11:23 | mention spike | 19 | 5.57 | 6 | 0 | wallstreetbets 19 | NYSE Arca |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1x6vy59/comment/ph2s73t/) |
| WETO | 2026-10-15 21:16 | mention spike | 13 | 1.29 | 6 | 0 | pennystocks 12, wallstreetbets 1 | Nasdaq |  | [link](https://www.reddit.com/r/pennystocks/comments/1x6bsmm/comment/pgz650o/) |
| TSM | 2026-10-14 19:51 | mention spike | 36 | 14.86 | 21 | 2 | wallstreetbets 36 | NYSE |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1x7c5j6/comment/ph3uboo/) |
| RKLB | 2026-10-14 19:24 | mention spike | 41 | 17.0 | 35 | 1 | wallstreetbets 41 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1x7chad/comment/ph3movz/) |
| WMT | 2026-10-14 19:24 | mention spike | 8 | 4.0 | 5 | 0 | wallstreetbets 8 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1x6hm3b/comment/pgxdtjm/) |
| TLT | 2026-10-14 18:31 | mention spike | 18 | 10.43 | 10 | 0 | wallstreetbets 18 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1x7c5j6/comment/ph3eztx/) |
| CRWV | 2026-10-13 03:58 | mention spike | 82 | 26.0 | 63 | 0 | wallstreetbets 81, smallstreetbets 1 | Nasdaq | #3 | [link](https://www.reddit.com/r/wallstreetbets/comments/1x77qv8/) |
| SOFI | 2026-10-14 18:18 | mention spike | 2 | 6.57 | 2 | 0 | wallstreetbets 2 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1x6hm3b/comment/pgxaxph/) |
| HOOD | 2026-10-14 20:04 | mention spike | 7 | 10.14 | 6 | 0 | wallstreetbets 7 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1x6vy59/comment/ph2rl4u/) |
| SOXS | 2026-10-15 15:04 | mention spike | 9 | 6.0 | 7 | 0 | wallstreetbets 9 | NYSE Arca |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1x7c5j6/comment/ph3ssk8/) |
| NBIS | 2026-10-13 03:35 | mention spike | 81 | 57.14 | 57 | 0 | wallstreetbets 81 | Nasdaq | #16 | [link](https://www.reddit.com/r/wallstreetbets/comments/1x77qv8/) |
| PFE | 2026-10-14 20:17 | mention spike | 3 | 1.57 | 3 | 0 | wallstreetbets 3 | NYSE |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1x7c5j6/comment/ph3wf01/) |

Full history: `episodes.csv` (one row per first flag, with the numbers known at that moment).
