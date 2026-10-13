# Stage 1 candidates

Updated 2026-10-13T05:34:39Z by run `38352053812`. A candidate is a ticker whose Reddit mentions (or hype-language
posts) in the last 24 hours jumped above its prior 7-day mean + 2 sd, with at least
10 mentions from 5 different authors. It stays listed until it goes
24 hours without a new flag. These are statistical flags, not accusations or advice.

| Ticker | Flagged since (UTC) | Why | Mentions 24h | Baseline/day | Authors | Hype posts | Subreddits | Exchange | StockTwits | Example |
|---|---|---|---|---|---|---|---|---|---|---|
| ASML | 2026-10-12 17:40 | mention spike | 18 | 2.86 | 15 | 0 | wallstreetbets 18 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1x4c9un/comment/pgesa82/) |
| BMBL | 2026-10-12 20:58 | mention spike | 16 | 0.0 | 14 | 0 | wallstreetbets 16 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1x4o7d7/) |
| CBRS | 2026-10-12 14:20 | mention spike | 45 | 5.14 | 28 | 0 | wallstreetbets 45 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1x45v0k/) |
| CRWV | 2026-10-13 03:58 | mention spike | 10 | 4.0 | 10 | 0 | wallstreetbets 10 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1x4c9un/comment/pgey0f7/) |
| IREN | 2026-10-12 03:44 | mention spike | 40 | 13.86 | 33 | 0 | wallstreetbets 40 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1x4j0dz/) |
| META | 2026-10-12 20:58 | mention spike | 47 | 17.0 | 36 | 1 | wallstreetbets 47 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1x46klu/) |
| MU | 2026-10-12 14:20 | mention spike | 33 | 7.57 | 13 | 0 | wallstreetbets 33 | Nasdaq | #23 | [link](https://www.reddit.com/r/wallstreetbets/comments/1x4awl8/) |
| NBIS | 2026-10-13 03:35 | mention spike | 54 | 22.71 | 37 | 0 | wallstreetbets 54 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1x4c9un/comment/pgf8xqh/) |
| NIO | 2026-10-12 22:44 | mention spike | 12 | 1.43 | 6 | 0 | wallstreetbets 12 | NYSE |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1x4e5vg/) |
| ONDS | 2026-10-12 14:47 | mention spike | 13 | 5.14 | 10 | 0 | wallstreetbets 13 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1x3xuss/comment/pfhgfgy/) |
| RDDT | 2026-10-12 20:18 | mention spike | 44 | 19.29 | 29 | 1 | wallstreetbets 44 | NYSE |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1x46klu/) |
| SKHY | 2026-10-13 02:56 | mention spike | 31 | 9.29 | 25 | 0 | wallstreetbets 31 | Nasdaq | #8 | [link](https://www.reddit.com/r/wallstreetbets/comments/1x4nr5m/) |
| SNDK | 2026-10-13 01:10 | mention spike | 102 | 41.14 | 60 | 0 | wallstreetbets 102 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1x4nr5m/comment/pgf7czp/) |
| SOXX | 2026-10-12 14:20 | mention spike | 12 | 4.57 | 9 | 0 | wallstreetbets 12 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1x4c9un/comment/pgeut42/) |
| TSM | 2026-10-12 15:13 | mention spike | 21 | 6.71 | 14 | 0 | wallstreetbets 21 | NYSE |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1x4486f/) |
| UNH | 2026-10-12 20:32 | mention spike | 13 | 3.43 | 13 | 0 | wallstreetbets 13 | NYSE | #6 | [link](https://www.reddit.com/r/wallstreetbets/comments/1x4c9un/comment/pgebtps/) |
| WFF | 2026-10-12 18:19 | mention spike | 15 | 1.57 | 9 | 1 | wallstreetbets 9, pennystocks 6 | Nasdaq | #29 | [link](https://www.reddit.com/r/wallstreetbets/comments/1x4c9un/comment/pgd2sfc/) |
| SOFI | 2026-10-12 21:51 | mention spike | 11 | 3.71 | 8 | 0 | wallstreetbets 11 | Nasdaq | #12 | [link](https://www.reddit.com/r/wallstreetbets/comments/1x4e5vg/comment/pgdaj57/) |
| SMCI | 2026-10-12 17:00 | mention spike | 11 | 4.43 | 7 | 0 | wallstreetbets 10, smallstreetbets 1 | Nasdaq |  | [link](https://www.reddit.com/r/smallstreetbets/comments/1x3tsce/) |
| MGM | 2026-10-12 06:49 | mention spike | 6 | 1.57 | 2 | 0 | wallstreetbets 6 | NYSE |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1x3trws/) |

Full history: `episodes.csv` (one row per first flag, with the numbers known at that moment).
