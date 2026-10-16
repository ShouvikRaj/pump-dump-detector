# Stage 1 candidates

Updated 2026-10-16T14:29:09Z by run `38916017171`. A candidate is a ticker whose Reddit mentions (or hype-language
posts) in the last 24 hours jumped above its prior 7-day mean + 2 sd, with at least
10 mentions from 5 different authors. It stays listed until it goes
24 hours without a new flag. These are statistical flags, not accusations or advice.

| Ticker | Flagged since (UTC) | Why | Mentions 24h | Baseline/day | Authors | Hype posts | Subreddits | Exchange | StockTwits | Example |
|---|---|---|---|---|---|---|---|---|---|---|
| BETR | 2026-10-15 23:28 | mention spike | 11 | 0.14 | 5 | 1 | pennystocks 9, wallstreetbets 2 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1x6vy59/comment/pgzlywb/) |
| IBKR | 2026-10-16 13:35 | mention spike | 10 | 3.29 | 7 | 0 | wallstreetbets 9, pennystocks 1 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1x7chad/comment/ph3te0t/) |
| RCS | 2026-10-16 12:29 | mention spike | 10 | 0.0 | 9 | 0 | wallstreetbets 10 | NYSE |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1x73hxs/comment/ph3f680/) |
| TSLA | 2026-10-16 07:11 | mention spike | 148 | 18.86 | 107 | 0 | wallstreetbets 146, smallstreetbets 2 | Nasdaq | #2 | [link](https://www.reddit.com/r/wallstreetbets/comments/1x7dg4r/) |
| USO | 2026-10-16 11:23 | mention spike | 19 | 5.43 | 6 | 0 | wallstreetbets 19 | NYSE Arca |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1x6vy59/comment/ph2s73t/) |
| WETO | 2026-10-15 21:16 | mention spike | 11 | 1.57 | 6 | 0 | pennystocks 10, wallstreetbets 1 | Nasdaq |  | [link](https://www.reddit.com/r/pennystocks/comments/1x6bsmm/comment/pgz650o/) |
| DRMA | 2026-10-15 23:28 | mention spike | 8 | 0.43 | 5 | 0 | pennystocks 8 | Nasdaq |  | [link](https://www.reddit.com/r/pennystocks/comments/1x6bsmm/comment/pgzqmfi/) |
| TSM | 2026-10-14 19:51 | mention spike | 19 | 17.29 | 15 | 0 | wallstreetbets 19 | NYSE |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1x7c5j6/comment/ph45ff8/) |
| RKLB | 2026-10-14 19:24 | mention spike | 35 | 17.86 | 29 | 1 | wallstreetbets 35 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1x7chad/comment/ph3movz/) |
| WMT | 2026-10-14 19:24 | mention spike | 8 | 4.14 | 5 | 0 | wallstreetbets 8 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1x7c5j6/comment/ph433ov/) |
| TLT | 2026-10-14 18:31 | mention spike | 19 | 10.43 | 11 | 0 | wallstreetbets 19 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1x7c5j6/comment/ph3xhrx/) |
| CRWV | 2026-10-13 03:58 | mention spike | 78 | 27.0 | 61 | 0 | wallstreetbets 77, smallstreetbets 1 | Nasdaq | #3 | [link](https://www.reddit.com/r/wallstreetbets/comments/1x77qv8/) |
| SOFI | 2026-10-14 18:18 | mention spike | 2 | 6.57 | 2 | 0 | wallstreetbets 2 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1x6hm3b/comment/pgxaxph/) |
| HOOD | 2026-10-14 20:04 | mention spike | 5 | 10.14 | 5 | 0 | wallstreetbets 5 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1x6vy59/comment/ph2rl4u/) |
| SOXS | 2026-10-15 15:04 | mention spike | 10 | 6.0 | 8 | 0 | wallstreetbets 9, smallstreetbets 1 | NYSE Arca |  | [link](https://www.reddit.com/r/smallstreetbets/comments/1x7gy8a/) |
| NBIS | 2026-10-13 03:35 | mention spike | 69 | 59.86 | 47 | 0 | wallstreetbets 69 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1x77qv8/) |
| PFE | 2026-10-14 20:17 | mention spike | 1 | 1.86 | 1 | 0 | wallstreetbets 1 | NYSE |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1x7c5j6/comment/ph3wf01/) |

Full history: `episodes.csv` (one row per first flag, with the numbers known at that moment).
