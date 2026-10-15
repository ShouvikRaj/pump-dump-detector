# Stage 1 candidates

Updated 2026-10-15T21:29:10Z by run `38810134503`. A candidate is a ticker whose Reddit mentions (or hype-language
posts) in the last 24 hours jumped above its prior 7-day mean + 2 sd, with at least
10 mentions from 5 different authors. It stays listed until it goes
24 hours without a new flag. These are statistical flags, not accusations or advice.

| Ticker | Flagged since (UTC) | Why | Mentions 24h | Baseline/day | Authors | Hype posts | Subreddits | Exchange | StockTwits | Example |
|---|---|---|---|---|---|---|---|---|---|---|
| TSM | 2026-10-14 19:51 | mention spike | 59 | 10.71 | 35 | 2 | wallstreetbets 58, smallstreetbets 1 | NYSE |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1x6mzgj/comment/pgz4idx/) |
| WETO | 2026-10-15 21:16 | mention spike | 11 | 0.14 | 5 | 0 | pennystocks 9, smallstreetbets 1, wallstreetbets 1 | Nasdaq |  | [link](https://www.reddit.com/r/smallstreetbets/comments/1x6ky4z/) |
| RKLB | 2026-10-14 19:24 | mention spike | 41 | 16.0 | 37 | 0 | wallstreetbets 41 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1x6vy59/comment/pgzc6x9/) |
| WMT | 2026-10-14 19:24 | mention spike | 12 | 3.43 | 8 | 0 | wallstreetbets 12 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1x6hm3b/comment/pgxdtjm/) |
| TLT | 2026-10-14 18:31 | mention spike | 25 | 9.86 | 15 | 0 | wallstreetbets 25 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1x6hm3b/comment/pgxisau/) |
| CRWV | 2026-10-13 03:58 | mention spike | 66 | 22.14 | 51 | 0 | wallstreetbets 64, smallstreetbets 2 | Nasdaq | #5 | [link](https://www.reddit.com/r/smallstreetbets/comments/1x6knlh/) |
| SOFI | 2026-10-14 18:18 | mention spike | 5 | 6.14 | 5 | 0 | wallstreetbets 5 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1x6hm3b/comment/pgxaxph/) |
| HOOD | 2026-10-14 20:04 | mention spike | 8 | 11.0 | 5 | 0 | wallstreetbets 8 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1x6hm3b/comment/pgx17u4/) |
| SOXS | 2026-10-15 15:04 | mention spike | 9 | 6.43 | 9 | 0 | wallstreetbets 8, smallstreetbets 1 | NYSE Arca |  | [link](https://www.reddit.com/r/smallstreetbets/comments/1x6ebnf/) |
| NBIS | 2026-10-13 03:35 | mention spike | 80 | 55.57 | 51 | 0 | wallstreetbets 78, smallstreetbets 2 | Nasdaq | #1 | [link](https://www.reddit.com/r/smallstreetbets/comments/1x6knlh/) |
| PFE | 2026-10-14 20:17 | mention spike | 2 | 1.57 | 2 | 0 | wallstreetbets 2 | NYSE |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1x6hm3b/comment/pgwndqx/) |
| GLND | 2026-10-14 12:29 | mention spike | 1 | 4.0 | 1 | 0 | pennystocks 1 | Nasdaq |  | [link](https://www.reddit.com/r/pennystocks/comments/1x6mb1l/) |
| ORCL | 2026-10-14 16:58 | mention spike | 8 | 10.43 | 7 | 0 | wallstreetbets 7, smallstreetbets 1 | NYSE | #28 | [link](https://www.reddit.com/r/smallstreetbets/comments/1x6knlh/) |
| CLF | 2026-10-14 11:39 | mention spike | 0 |  | 0 | 0 |  | NYSE |  |  |
| ASML | 2026-10-12 17:40 | mention spike | 6 | 15.43 | 4 | 0 | wallstreetbets 6 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1x6oykz/comment/pgx6vkt/) |
| TCRT | 2026-10-14 13:12 | mention spike | 0 |  | 0 | 0 |  | Nasdaq |  |  |
| LQDA | 2026-10-14 19:11 | mention spike | 0 |  | 0 | 0 |  | Nasdaq |  |  |
| BAC | 2026-10-13 20:37 | mention spike | 0 |  | 0 | 0 |  | NYSE |  |  |
| VOO | 2026-10-14 17:34 | mention spike | 10 | 13.14 | 9 | 0 | wallstreetbets 9, smallstreetbets 1 | NYSE Arca |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1x6iuac/comment/pgxldqx/) |

Full history: `episodes.csv` (one row per first flag, with the numbers known at that moment).
