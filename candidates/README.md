# Stage 1 candidates

Updated 2026-10-16T06:31:55Z by run `38861674946`. A candidate is a ticker whose Reddit mentions (or hype-language
posts) in the last 24 hours jumped above its prior 7-day mean + 2 sd, with at least
10 mentions from 5 different authors. It stays listed until it goes
24 hours without a new flag. These are statistical flags, not accusations or advice.

| Ticker | Flagged since (UTC) | Why | Mentions 24h | Baseline/day | Authors | Hype posts | Subreddits | Exchange | StockTwits | Example |
|---|---|---|---|---|---|---|---|---|---|---|
| BETR | 2026-10-15 23:28 | mention spike | 11 | 0.14 | 5 | 1 | pennystocks 9, wallstreetbets 2 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1x6vy59/comment/pgzlywb/) |
| DRMA | 2026-10-15 23:28 | mention spike | 11 | 0.0 | 5 | 0 | pennystocks 11 | Nasdaq |  | [link](https://www.reddit.com/r/pennystocks/comments/1x6bsmm/comment/pgzqmfi/) |
| TSM | 2026-10-14 19:51 | mention spike | 46 | 13.0 | 27 | 2 | wallstreetbets 45, smallstreetbets 1 | NYSE |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1x6vy59/comment/ph16gut/) |
| WETO | 2026-10-15 21:16 | mention spike | 21 | 0.14 | 8 | 0 | pennystocks 19, smallstreetbets 1, wallstreetbets 1 | Nasdaq |  | [link](https://www.reddit.com/r/smallstreetbets/comments/1x6ky4z/) |
| RKLB | 2026-10-14 19:24 | mention spike | 45 | 15.43 | 39 | 0 | wallstreetbets 45 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1x6vy59/comment/pgzvyy2/) |
| WMT | 2026-10-14 19:24 | mention spike | 12 | 3.43 | 8 | 0 | wallstreetbets 12 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1x6hm3b/comment/pgxdtjm/) |
| TLT | 2026-10-14 18:31 | mention spike | 24 | 10.14 | 16 | 0 | wallstreetbets 24 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1x6vy59/comment/pgzkgbi/) |
| CRWV | 2026-10-13 03:58 | mention spike | 86 | 22.0 | 63 | 0 | wallstreetbets 84, smallstreetbets 2 | Nasdaq | #5 | [link](https://www.reddit.com/r/wallstreetbets/comments/1x77qv8/) |
| SOFI | 2026-10-14 18:18 | mention spike | 4 | 6.29 | 4 | 0 | wallstreetbets 4 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1x6hm3b/comment/pgxaxph/) |
| HOOD | 2026-10-14 20:04 | mention spike | 9 | 10.71 | 6 | 0 | wallstreetbets 9 | Nasdaq | #28 | [link](https://www.reddit.com/r/wallstreetbets/comments/1x6vy59/comment/pgzq1wg/) |
| SOXS | 2026-10-15 15:04 | mention spike | 8 | 6.29 | 8 | 0 | wallstreetbets 8 | NYSE Arca |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1x6vy59/comment/pgzttml/) |
| NBIS | 2026-10-13 03:35 | mention spike | 88 | 55.14 | 58 | 0 | wallstreetbets 86, smallstreetbets 2 | Nasdaq | #7 | [link](https://www.reddit.com/r/wallstreetbets/comments/1x77qv8/) |
| PFE | 2026-10-14 20:17 | mention spike | 2 | 1.57 | 2 | 0 | wallstreetbets 2 | NYSE |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1x6hm3b/comment/pgwndqx/) |
| GLND | 2026-10-14 12:29 | mention spike | 1 | 4.0 | 1 | 0 | pennystocks 1 | Nasdaq |  | [link](https://www.reddit.com/r/pennystocks/comments/1x6mb1l/) |
| ORCL | 2026-10-14 16:58 | mention spike | 7 | 10.29 | 7 | 0 | wallstreetbets 6, smallstreetbets 1 | NYSE |  | [link](https://www.reddit.com/r/smallstreetbets/comments/1x6knlh/) |
| CLF | 2026-10-14 11:39 | mention spike | 0 |  | 0 | 0 |  | NYSE |  |  |

Full history: `episodes.csv` (one row per first flag, with the numbers known at that moment).
