# Stage 1 candidates

Updated 2026-10-15T22:35:18Z by run `38818056942`. A candidate is a ticker whose Reddit mentions (or hype-language
posts) in the last 24 hours jumped above its prior 7-day mean + 2 sd, with at least
10 mentions from 5 different authors. It stays listed until it goes
24 hours without a new flag. These are statistical flags, not accusations or advice.

| Ticker | Flagged since (UTC) | Why | Mentions 24h | Baseline/day | Authors | Hype posts | Subreddits | Exchange | StockTwits | Example |
|---|---|---|---|---|---|---|---|---|---|---|
| TSM | 2026-10-14 19:51 | mention spike | 62 | 10.71 | 38 | 2 | wallstreetbets 61, smallstreetbets 1 | NYSE |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1x6vy59/comment/pgzu3b6/) |
| WETO | 2026-10-15 21:16 | mention spike | 11 | 0.14 | 5 | 0 | pennystocks 9, smallstreetbets 1, wallstreetbets 1 | Nasdaq |  | [link](https://www.reddit.com/r/smallstreetbets/comments/1x6ky4z/) |
| RKLB | 2026-10-14 19:24 | mention spike | 45 | 16.0 | 39 | 0 | wallstreetbets 45 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1x6vy59/comment/pgzogoy/) |
| WMT | 2026-10-14 19:24 | mention spike | 12 | 3.43 | 8 | 0 | wallstreetbets 12 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1x6hm3b/comment/pgxdtjm/) |
| TLT | 2026-10-14 18:31 | mention spike | 26 | 9.86 | 16 | 0 | wallstreetbets 26 | Nasdaq | #20 | [link](https://www.reddit.com/r/wallstreetbets/comments/1x6vy59/comment/pgzkgbi/) |
| CRWV | 2026-10-13 03:58 | mention spike | 80 | 22.14 | 59 | 0 | wallstreetbets 78, smallstreetbets 2 | Nasdaq | #7 | [link](https://www.reddit.com/r/wallstreetbets/comments/1x6w7ry/) |
| SOFI | 2026-10-14 18:18 | mention spike | 5 | 6.14 | 5 | 0 | wallstreetbets 5 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1x6hm3b/comment/pgxaxph/) |
| HOOD | 2026-10-14 20:04 | mention spike | 9 | 11.0 | 6 | 0 | wallstreetbets 9 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1x6vy59/comment/pgzq1wg/) |
| SOXS | 2026-10-15 15:04 | mention spike | 10 | 6.43 | 10 | 0 | wallstreetbets 9, smallstreetbets 1 | NYSE Arca |  | [link](https://www.reddit.com/r/smallstreetbets/comments/1x6ebnf/) |
| NBIS | 2026-10-13 03:35 | mention spike | 90 | 55.57 | 57 | 0 | wallstreetbets 88, smallstreetbets 2 | Nasdaq | #10 | [link](https://www.reddit.com/r/wallstreetbets/comments/1x6w7ry/) |
| PFE | 2026-10-14 20:17 | mention spike | 2 | 1.57 | 2 | 0 | wallstreetbets 2 | NYSE |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1x6hm3b/comment/pgwndqx/) |
| GLND | 2026-10-14 12:29 | mention spike | 1 | 4.0 | 1 | 0 | pennystocks 1 | Nasdaq |  | [link](https://www.reddit.com/r/pennystocks/comments/1x6mb1l/) |
| ORCL | 2026-10-14 16:58 | mention spike | 8 | 10.43 | 7 | 0 | wallstreetbets 7, smallstreetbets 1 | NYSE |  | [link](https://www.reddit.com/r/smallstreetbets/comments/1x6knlh/) |
| CLF | 2026-10-14 11:39 | mention spike | 0 |  | 0 | 0 |  | NYSE | #16 |  |
| ASML | 2026-10-12 17:40 | mention spike | 6 | 15.29 | 4 | 0 | wallstreetbets 6 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1x6oykz/comment/pgx6vkt/) |
| TCRT | 2026-10-14 13:12 | mention spike | 0 |  | 0 | 0 |  | Nasdaq |  |  |
| LQDA | 2026-10-14 19:11 | mention spike | 0 |  | 0 | 0 |  | Nasdaq |  |  |
| BAC | 2026-10-13 20:37 | mention spike | 0 |  | 0 | 0 |  | NYSE |  |  |

Full history: `episodes.csv` (one row per first flag, with the numbers known at that moment).
