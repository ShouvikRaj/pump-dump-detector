# Stage 1 candidates

Updated 2026-10-16T13:09:09Z by run `38905582725`. A candidate is a ticker whose Reddit mentions (or hype-language
posts) in the last 24 hours jumped above its prior 7-day mean + 2 sd, with at least
10 mentions from 5 different authors. It stays listed until it goes
24 hours without a new flag. These are statistical flags, not accusations or advice.

| Ticker | Flagged since (UTC) | Why | Mentions 24h | Baseline/day | Authors | Hype posts | Subreddits | Exchange | StockTwits | Example |
|---|---|---|---|---|---|---|---|---|---|---|
| BETR | 2026-10-15 23:28 | mention spike | 11 | 0.14 | 5 | 1 | pennystocks 9, wallstreetbets 2 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1x6vy59/comment/pgzlywb/) |
| DRMA | 2026-10-15 23:28 | mention spike | 10 | 0.14 | 5 | 0 | pennystocks 10 | Nasdaq |  | [link](https://www.reddit.com/r/pennystocks/comments/1x6bsmm/comment/pgzqmfi/) |
| RCS | 2026-10-16 12:29 | mention spike | 10 | 0.0 | 9 | 0 | wallstreetbets 10 | NYSE |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1x73hxs/comment/ph3f680/) |
| TSLA | 2026-10-16 07:11 | mention spike | 119 | 18.43 | 91 | 0 | wallstreetbets 117, smallstreetbets 2 | Nasdaq | #1 | [link](https://www.reddit.com/r/wallstreetbets/comments/1x7dg4r/) |
| WETO | 2026-10-15 21:16 | mention spike | 19 | 0.43 | 7 | 0 | pennystocks 18, wallstreetbets 1 | Nasdaq |  | [link](https://www.reddit.com/r/pennystocks/comments/1x6bsmm/comment/pgz650o/) |
| TSM | 2026-10-14 19:51 | mention spike | 42 | 13.86 | 22 | 2 | wallstreetbets 42 | NYSE |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1x7c5j6/comment/ph3mu24/) |
| USO | 2026-10-16 11:23 | mention spike | 20 | 6.14 | 7 | 0 | wallstreetbets 20 | NYSE Arca |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1x6vy59/comment/ph2s73t/) |
| RKLB | 2026-10-14 19:24 | mention spike | 50 | 15.71 | 44 | 1 | wallstreetbets 50 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1x7chad/comment/ph3movz/) |
| WMT | 2026-10-14 19:24 | mention spike | 11 | 3.57 | 7 | 0 | wallstreetbets 11 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1x6hm3b/comment/pgxdtjm/) |
| TLT | 2026-10-14 18:31 | mention spike | 22 | 10.0 | 14 | 0 | wallstreetbets 22 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1x7c5j6/comment/ph3eztx/) |
| CRWV | 2026-10-13 03:58 | mention spike | 75 | 25.43 | 60 | 0 | wallstreetbets 74, smallstreetbets 1 | Nasdaq | #6 | [link](https://www.reddit.com/r/wallstreetbets/comments/1x77qv8/) |
| SOFI | 2026-10-14 18:18 | mention spike | 4 | 6.29 | 4 | 0 | wallstreetbets 4 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1x6hm3b/comment/pgxaxph/) |
| HOOD | 2026-10-14 20:04 | mention spike | 10 | 10.29 | 7 | 0 | wallstreetbets 10 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1x6vy59/comment/ph2rl4u/) |
| SOXS | 2026-10-15 15:04 | mention spike | 10 | 5.71 | 8 | 0 | wallstreetbets 10 | NYSE Arca |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1x7chad/comment/ph3nfg3/) |
| NBIS | 2026-10-13 03:35 | mention spike | 85 | 55.86 | 58 | 0 | wallstreetbets 85 | Nasdaq | #14 | [link](https://www.reddit.com/r/wallstreetbets/comments/1x77qv8/) |
| PFE | 2026-10-14 20:17 | mention spike | 2 | 1.57 | 2 | 0 | wallstreetbets 2 | NYSE |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1x6hm3b/comment/pgwndqx/) |

Full history: `episodes.csv` (one row per first flag, with the numbers known at that moment).
