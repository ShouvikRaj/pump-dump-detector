# Stage 1 candidates

Updated 2026-10-15T19:43:16Z by run `38796090564`. A candidate is a ticker whose Reddit mentions (or hype-language
posts) in the last 24 hours jumped above its prior 7-day mean + 2 sd, with at least
10 mentions from 5 different authors. It stays listed until it goes
24 hours without a new flag. These are statistical flags, not accusations or advice.

| Ticker | Flagged since (UTC) | Why | Mentions 24h | Baseline/day | Authors | Hype posts | Subreddits | Exchange | StockTwits | Example |
|---|---|---|---|---|---|---|---|---|---|---|
| RKLB | 2026-10-14 19:24 | mention spike | 65 | 11.57 | 59 | 0 | wallstreetbets 65 | Nasdaq | #20 | [link](https://www.reddit.com/r/wallstreetbets/comments/1x6hm3b/comment/pgxjo6n/) |
| TLT | 2026-10-14 18:31 | mention spike | 29 | 9.29 | 16 | 0 | wallstreetbets 29 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1x6hm3b/comment/pgxisau/) |
| TSM | 2026-10-14 19:51 | mention spike | 70 | 8.86 | 41 | 2 | wallstreetbets 69, smallstreetbets 1 | NYSE |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1x6eacg/comment/pgx7u5u/) |
| WMT | 2026-10-14 19:24 | mention spike | 18 | 2.57 | 12 | 0 | wallstreetbets 18 | Nasdaq | #15 | [link](https://www.reddit.com/r/wallstreetbets/comments/1x6hm3b/comment/pgxdtjm/) |
| CRWV | 2026-10-13 03:58 | mention spike | 75 | 19.86 | 58 | 0 | wallstreetbets 75 | Nasdaq | #3 | [link](https://www.reddit.com/r/wallstreetbets/comments/1x6hm3b/comment/pgxgkk2/) |
| SOFI | 2026-10-14 18:18 | mention spike | 7 | 5.86 | 7 | 0 | wallstreetbets 7 | Nasdaq | #17 | [link](https://www.reddit.com/r/wallstreetbets/comments/1x6hm3b/comment/pgxaxph/) |
| HOOD | 2026-10-14 20:04 | mention spike | 11 | 10.86 | 7 | 0 | wallstreetbets 11 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1x6hm3b/comment/pgx17u4/) |
| SOXS | 2026-10-15 15:04 | mention spike | 13 | 6.0 | 11 | 0 | wallstreetbets 12, smallstreetbets 1 | NYSE Arca |  | [link](https://www.reddit.com/r/smallstreetbets/comments/1x6ebnf/) |
| NBIS | 2026-10-13 03:35 | mention spike | 91 | 53.14 | 57 | 0 | wallstreetbets 90, smallstreetbets 1 | Nasdaq | #2 | [link](https://www.reddit.com/r/wallstreetbets/comments/1x6hm3b/comment/pgxlgih/) |
| PFE | 2026-10-14 20:17 | mention spike | 3 | 1.43 | 3 | 0 | wallstreetbets 3 | NYSE |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1x6hm3b/comment/pgwndqx/) |
| GLND | 2026-10-14 12:29 | mention spike | 0 |  | 0 | 0 |  | Nasdaq |  |  |
| ORCL | 2026-10-14 16:58 | mention spike | 8 | 10.29 | 6 | 0 | wallstreetbets 8 | NYSE |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1x6hm3b/comment/pgx6d4m/) |
| CLF | 2026-10-14 11:39 | mention spike | 0 |  | 0 | 0 |  | NYSE |  |  |
| ASML | 2026-10-12 17:40 | mention spike | 6 | 15.43 | 4 | 0 | wallstreetbets 6 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1x6oykz/comment/pgx6vkt/) |
| TCRT | 2026-10-14 13:12 | mention spike | 0 |  | 0 | 0 |  | Nasdaq |  |  |
| LQDA | 2026-10-14 19:11 | mention spike | 0 |  | 0 | 0 |  | Nasdaq |  |  |
| BAC | 2026-10-13 20:37 | mention spike | 2 | 6.71 | 2 | 0 | wallstreetbets 2 | NYSE |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1x61ifg/comment/pgrdasi/) |
| VOO | 2026-10-14 17:34 | mention spike | 9 | 13.29 | 8 | 0 | wallstreetbets 9 | NYSE Arca |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1x6iuac/comment/pgxldqx/) |

Full history: `episodes.csv` (one row per first flag, with the numbers known at that moment).
