# Stage 1 candidates

Updated 2026-10-15T22:08:55Z by run `38814996453`. A candidate is a ticker whose Reddit mentions (or hype-language
posts) in the last 24 hours jumped above its prior 7-day mean + 2 sd, with at least
10 mentions from 5 different authors. It stays listed until it goes
24 hours without a new flag. These are statistical flags, not accusations or advice.

| Ticker | Flagged since (UTC) | Why | Mentions 24h | Baseline/day | Authors | Hype posts | Subreddits | Exchange | StockTwits | Example |
|---|---|---|---|---|---|---|---|---|---|---|
| TSM | 2026-10-14 19:51 | mention spike | 61 | 10.71 | 37 | 2 | wallstreetbets 60, smallstreetbets 1 | NYSE | #28 | [link](https://www.reddit.com/r/wallstreetbets/comments/1x6vy59/comment/pgzl43k/) |
| WETO | 2026-10-15 21:16 | mention spike | 11 | 0.14 | 5 | 0 | pennystocks 9, smallstreetbets 1, wallstreetbets 1 | Nasdaq |  | [link](https://www.reddit.com/r/smallstreetbets/comments/1x6ky4z/) |
| RKLB | 2026-10-14 19:24 | mention spike | 44 | 16.0 | 39 | 0 | wallstreetbets 44 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1x6vy59/comment/pgzo0az/) |
| WMT | 2026-10-14 19:24 | mention spike | 12 | 3.43 | 8 | 0 | wallstreetbets 12 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1x6hm3b/comment/pgxdtjm/) |
| TLT | 2026-10-14 18:31 | mention spike | 26 | 9.86 | 16 | 0 | wallstreetbets 26 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1x6vy59/comment/pgzkgbi/) |
| CRWV | 2026-10-13 03:58 | mention spike | 75 | 22.14 | 58 | 0 | wallstreetbets 73, smallstreetbets 2 | Nasdaq | #6 | [link](https://www.reddit.com/r/wallstreetbets/comments/1x6w7ry/) |
| SOFI | 2026-10-14 18:18 | mention spike | 5 | 6.14 | 5 | 0 | wallstreetbets 5 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1x6hm3b/comment/pgxaxph/) |
| HOOD | 2026-10-14 20:04 | mention spike | 8 | 11.0 | 5 | 0 | wallstreetbets 8 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1x6hm3b/comment/pgx17u4/) |
| SOXS | 2026-10-15 15:04 | mention spike | 9 | 6.43 | 9 | 0 | wallstreetbets 8, smallstreetbets 1 | NYSE Arca |  | [link](https://www.reddit.com/r/smallstreetbets/comments/1x6ebnf/) |
| NBIS | 2026-10-13 03:35 | mention spike | 84 | 55.57 | 54 | 0 | wallstreetbets 82, smallstreetbets 2 | Nasdaq | #4 | [link](https://www.reddit.com/r/wallstreetbets/comments/1x6w7ry/) |
| PFE | 2026-10-14 20:17 | mention spike | 2 | 1.57 | 2 | 0 | wallstreetbets 2 | NYSE |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1x6hm3b/comment/pgwndqx/) |
| GLND | 2026-10-14 12:29 | mention spike | 1 | 4.0 | 1 | 0 | pennystocks 1 | Nasdaq |  | [link](https://www.reddit.com/r/pennystocks/comments/1x6mb1l/) |
| ORCL | 2026-10-14 16:58 | mention spike | 8 | 10.43 | 7 | 0 | wallstreetbets 7, smallstreetbets 1 | NYSE |  | [link](https://www.reddit.com/r/smallstreetbets/comments/1x6knlh/) |
| CLF | 2026-10-14 11:39 | mention spike | 0 |  | 0 | 0 |  | NYSE |  |  |
| ASML | 2026-10-12 17:40 | mention spike | 6 | 15.29 | 4 | 0 | wallstreetbets 6 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1x6oykz/comment/pgx6vkt/) |
| TCRT | 2026-10-14 13:12 | mention spike | 0 |  | 0 | 0 |  | Nasdaq |  |  |
| LQDA | 2026-10-14 19:11 | mention spike | 0 |  | 0 | 0 |  | Nasdaq |  |  |
| BAC | 2026-10-13 20:37 | mention spike | 0 |  | 0 | 0 |  | NYSE |  |  |

Full history: `episodes.csv` (one row per first flag, with the numbers known at that moment).
