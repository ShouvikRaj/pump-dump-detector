# Stage 1 candidates

Updated 2026-10-16T12:29:32Z by run `38900789243`. A candidate is a ticker whose Reddit mentions (or hype-language
posts) in the last 24 hours jumped above its prior 7-day mean + 2 sd, with at least
10 mentions from 5 different authors. It stays listed until it goes
24 hours without a new flag. These are statistical flags, not accusations or advice.

| Ticker | Flagged since (UTC) | Why | Mentions 24h | Baseline/day | Authors | Hype posts | Subreddits | Exchange | StockTwits | Example |
|---|---|---|---|---|---|---|---|---|---|---|
| BETR | 2026-10-15 23:28 | mention spike | 11 | 0.14 | 5 | 1 | pennystocks 9, wallstreetbets 2 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1x6vy59/comment/pgzlywb/) |
| DRMA | 2026-10-15 23:28 | mention spike | 11 | 0.0 | 5 | 0 | pennystocks 11 | Nasdaq |  | [link](https://www.reddit.com/r/pennystocks/comments/1x6bsmm/comment/pgzqmfi/) |
| TSLA | 2026-10-16 07:11 | mention spike | 105 | 18.43 | 81 | 0 | wallstreetbets 103, smallstreetbets 2 | Nasdaq | #1 | [link](https://www.reddit.com/r/wallstreetbets/comments/1x7dg4r/) |
| TSM | 2026-10-14 19:51 | mention spike | 44 | 13.43 | 25 | 2 | wallstreetbets 44 | NYSE |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1x7c5j6/comment/ph3dp0a/) |
| USO | 2026-10-16 11:23 | mention spike | 20 | 6.14 | 7 | 0 | wallstreetbets 20 | NYSE Arca |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1x6vy59/comment/ph2s73t/) |
| WETO | 2026-10-15 21:16 | mention spike | 21 | 0.14 | 8 | 0 | pennystocks 19, smallstreetbets 1, wallstreetbets 1 | Nasdaq |  | [link](https://www.reddit.com/r/smallstreetbets/comments/1x6ky4z/) |
| RCS | 2026-10-16 12:29 | mention spike | 10 | 0.0 | 9 | 0 | wallstreetbets 10 | NYSE |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1x73hxs/comment/ph3f680/) |
| RKLB | 2026-10-14 19:24 | mention spike | 48 | 15.71 | 43 | 1 | wallstreetbets 48 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1x7c5j6/comment/ph39rj4/) |
| WMT | 2026-10-14 19:24 | mention spike | 12 | 3.43 | 8 | 0 | wallstreetbets 12 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1x6hm3b/comment/pgxdtjm/) |
| TLT | 2026-10-14 18:31 | mention spike | 26 | 9.43 | 17 | 0 | wallstreetbets 26 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1x7c5j6/comment/ph3eztx/) |
| CRWV | 2026-10-13 03:58 | mention spike | 82 | 24.29 | 66 | 0 | wallstreetbets 80, smallstreetbets 2 | Nasdaq | #23 | [link](https://www.reddit.com/r/wallstreetbets/comments/1x77qv8/) |
| SOFI | 2026-10-14 18:18 | mention spike | 4 | 6.29 | 4 | 0 | wallstreetbets 4 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1x6hm3b/comment/pgxaxph/) |
| HOOD | 2026-10-14 20:04 | mention spike | 10 | 10.29 | 7 | 0 | wallstreetbets 10 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1x6vy59/comment/ph2rl4u/) |
| SOXS | 2026-10-15 15:04 | mention spike | 8 | 5.57 | 8 | 0 | wallstreetbets 8 | NYSE Arca |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1x6vy59/comment/pgzttml/) |
| NBIS | 2026-10-13 03:35 | mention spike | 90 | 55.14 | 61 | 0 | wallstreetbets 88, smallstreetbets 2 | Nasdaq | #15 | [link](https://www.reddit.com/r/wallstreetbets/comments/1x77qv8/) |
| PFE | 2026-10-14 20:17 | mention spike | 2 | 1.57 | 2 | 0 | wallstreetbets 2 | NYSE |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1x6hm3b/comment/pgwndqx/) |
| GLND | 2026-10-14 12:29 | mention spike | 1 | 4.0 | 1 | 0 | pennystocks 1 | Nasdaq |  | [link](https://www.reddit.com/r/pennystocks/comments/1x6mb1l/) |
| ORCL | 2026-10-14 16:58 | mention spike | 5 | 10.57 | 5 | 0 | wallstreetbets 4, smallstreetbets 1 | NYSE |  | [link](https://www.reddit.com/r/smallstreetbets/comments/1x6knlh/) |

Full history: `episodes.csv` (one row per first flag, with the numbers known at that moment).
