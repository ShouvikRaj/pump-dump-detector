# Stage 1 candidates

Updated 2026-10-15T17:03:55Z by run `38774109678`. A candidate is a ticker whose Reddit mentions (or hype-language
posts) in the last 24 hours jumped above its prior 7-day mean + 2 sd, with at least
10 mentions from 5 different authors. It stays listed until it goes
24 hours without a new flag. These are statistical flags, not accusations or advice.

| Ticker | Flagged since (UTC) | Why | Mentions 24h | Baseline/day | Authors | Hype posts | Subreddits | Exchange | StockTwits | Example |
|---|---|---|---|---|---|---|---|---|---|---|
| CRWV | 2026-10-13 03:58 | mention spike | 107 | 15.29 | 78 | 0 | wallstreetbets 107 | Nasdaq | #2 | [link](https://www.reddit.com/r/wallstreetbets/comments/1x6hm3b/comment/pgxgkk2/) |
| RKLB | 2026-10-14 19:24 | mention spike | 75 | 10.14 | 66 | 0 | wallstreetbets 75 | Nasdaq | #7 | [link](https://www.reddit.com/r/wallstreetbets/comments/1x6hm3b/comment/pgxjo6n/) |
| SOFI | 2026-10-14 18:18 | mention spike | 14 | 4.86 | 14 | 0 | wallstreetbets 14 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1x6hm3b/comment/pgxaxph/) |
| TLT | 2026-10-14 18:31 | mention spike | 43 | 8.14 | 20 | 0 | wallstreetbets 43 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1x6hm3b/comment/pgxisau/) |
| TSM | 2026-10-14 19:51 | mention spike | 76 | 8.0 | 47 | 2 | wallstreetbets 75, smallstreetbets 1 | NYSE | #13 | [link](https://www.reddit.com/r/wallstreetbets/comments/1x6eacg/comment/pgx7u5u/) |
| WMT | 2026-10-14 19:24 | mention spike | 25 | 1.57 | 14 | 0 | wallstreetbets 25 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1x6hm3b/comment/pgxdtjm/) |
| HOOD | 2026-10-14 20:04 | mention spike | 19 | 9.71 | 13 | 0 | wallstreetbets 19 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1x60zj9/) |
| SOXS | 2026-10-15 15:04 | mention spike | 14 | 6.0 | 12 | 0 | wallstreetbets 13, smallstreetbets 1 | NYSE Arca |  | [link](https://www.reddit.com/r/smallstreetbets/comments/1x6ebnf/) |
| NBIS | 2026-10-13 03:35 | mention spike | 124 | 48.71 | 76 | 0 | wallstreetbets 123, smallstreetbets 1 | Nasdaq | #8 | [link](https://www.reddit.com/r/wallstreetbets/comments/1x6hm3b/comment/pgxlgih/) |
| PFE | 2026-10-14 20:17 | mention spike | 5 | 1.14 | 5 | 0 | wallstreetbets 5 | NYSE |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1x6hm3b/comment/pgwndqx/) |
| GLND | 2026-10-14 12:29 | mention spike | 1 | 3.86 | 1 | 0 | pennystocks 1 | Nasdaq |  | [link](https://www.reddit.com/r/pennystocks/comments/1x5hhxp/comment/pgqaxep/) |
| ORCL | 2026-10-14 16:58 | mention spike | 14 | 9.57 | 11 | 0 | wallstreetbets 14 | NYSE |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1x6hm3b/comment/pgx6d4m/) |
| CLF | 2026-10-14 11:39 | mention spike | 0 |  | 0 | 0 |  | NYSE |  |  |
| ASML | 2026-10-12 17:40 | mention spike | 7 | 15.43 | 5 | 0 | wallstreetbets 7 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1x6oykz/comment/pgx6vkt/) |
| TCRT | 2026-10-14 13:12 | mention spike | 0 |  | 0 | 0 |  | Nasdaq |  |  |
| LQDA | 2026-10-14 19:11 | mention spike | 1 | 1.43 | 1 | 0 | smallstreetbets 1 | Nasdaq |  | [link](https://www.reddit.com/r/smallstreetbets/comments/1x5zon7/) |
| BAC | 2026-10-13 20:37 | mention spike | 2 | 6.71 | 2 | 0 | wallstreetbets 2 | NYSE | #26 | [link](https://www.reddit.com/r/wallstreetbets/comments/1x61ifg/comment/pgrdasi/) |
| VOO | 2026-10-14 17:34 | mention spike | 13 | 12.71 | 12 | 0 | wallstreetbets 13 | NYSE Arca |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1x6iuac/comment/pgxldqx/) |
| GME | 2026-10-13 14:38 | mention spike | 25 | 27.71 | 19 | 0 | wallstreetbets 21, smallstreetbets 4 | NYSE |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1x6kq33/) |
| RSP | 2026-10-14 00:41 | mention spike | 2 | 4.0 | 2 | 0 | wallstreetbets 2 | NYSE Arca |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1x6mzgj/comment/pgwwsn4/) |
| SOXL | 2026-10-13 22:51 | mention spike | 48 | 33.57 | 28 | 0 | wallstreetbets 48 | NYSE Arca |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1x6hm3b/comment/pgxjys5/) |

Full history: `episodes.csv` (one row per first flag, with the numbers known at that moment).
