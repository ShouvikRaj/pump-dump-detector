# Stage 1 candidates

Updated 2026-10-13T07:20:40Z by run `38361992068`. A candidate is a ticker whose Reddit mentions (or hype-language
posts) in the last 24 hours jumped above its prior 7-day mean + 2 sd, with at least
10 mentions from 5 different authors. It stays listed until it goes
24 hours without a new flag. These are statistical flags, not accusations or advice.

| Ticker | Flagged since (UTC) | Why | Mentions 24h | Baseline/day | Authors | Hype posts | Subreddits | Exchange | StockTwits | Example |
|---|---|---|---|---|---|---|---|---|---|---|
| ASML | 2026-10-12 17:40 | mention spike | 19 | 2.86 | 16 | 0 | wallstreetbets 19 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1x4q3x5/) |
| BMBL | 2026-10-12 20:58 | mention spike | 17 | 0.0 | 15 | 0 | wallstreetbets 17 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1x4o7d7/) |
| CBRS | 2026-10-12 14:20 | mention spike | 45 | 4.86 | 28 | 0 | wallstreetbets 45 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1x45v0k/) |
| CRWV | 2026-10-13 03:58 | mention spike | 10 | 4.0 | 10 | 0 | wallstreetbets 10 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1x4c9un/comment/pgey0f7/) |
| IREN | 2026-10-12 03:44 | mention spike | 38 | 14.14 | 31 | 0 | wallstreetbets 38 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1x4j0dz/) |
| META | 2026-10-12 20:58 | mention spike | 47 | 16.86 | 36 | 1 | wallstreetbets 47 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1x46klu/) |
| MU | 2026-10-12 14:20 | mention spike | 33 | 7.57 | 13 | 0 | wallstreetbets 33 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1x4awl8/) |
| NBIS | 2026-10-13 03:35 | mention spike | 54 | 22.86 | 37 | 0 | wallstreetbets 54 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1x4c9un/comment/pgfgli1/) |
| NIO | 2026-10-12 22:44 | mention spike | 12 | 1.43 | 6 | 0 | wallstreetbets 12 | NYSE |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1x4e5vg/) |
| ONDS | 2026-10-12 14:47 | mention spike | 13 | 5.14 | 10 | 0 | wallstreetbets 13 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1vlsoz5/comment/pgfifxu/) |
| RDDT | 2026-10-12 20:18 | mention spike | 44 | 19.43 | 29 | 1 | wallstreetbets 44 | NYSE |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1x46klu/) |
| SKHY | 2026-10-13 02:56 | mention spike | 31 | 9.29 | 25 | 0 | wallstreetbets 31 | Nasdaq | #9 | [link](https://www.reddit.com/r/wallstreetbets/comments/1x4nr5m/) |
| SNDK | 2026-10-13 01:10 | mention spike | 104 | 41.57 | 61 | 0 | wallstreetbets 104 | Nasdaq | #6 | [link](https://www.reddit.com/r/wallstreetbets/comments/1x4pdjy/) |
| TSM | 2026-10-12 15:13 | mention spike | 21 | 6.71 | 14 | 0 | wallstreetbets 21 | NYSE |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1x4486f/) |
| UNH | 2026-10-12 20:32 | mention spike | 13 | 3.43 | 13 | 0 | wallstreetbets 13 | NYSE | #2 | [link](https://www.reddit.com/r/wallstreetbets/comments/1x4c9un/comment/pgebtps/) |
| WFF | 2026-10-12 18:19 | mention spike | 15 | 1.57 | 9 | 1 | wallstreetbets 9, pennystocks 6 | Nasdaq | #1 | [link](https://www.reddit.com/r/wallstreetbets/comments/1x4c9un/comment/pgd2sfc/) |
| SOXX | 2026-10-12 14:20 | mention spike | 11 | 4.71 | 9 | 0 | wallstreetbets 11 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1x4c9un/comment/pgeut42/) |
| SOFI | 2026-10-12 21:51 | mention spike | 10 | 3.71 | 7 | 0 | wallstreetbets 10 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1x4e5vg/comment/pgdaj57/) |
| SMCI | 2026-10-12 17:00 | mention spike | 10 | 4.57 | 6 | 0 | wallstreetbets 10 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1x4c9un/comment/pgee3q9/) |
| MGM | 2026-10-12 06:49 | mention spike | 2 | 2.14 | 1 | 0 | wallstreetbets 2 | NYSE |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1x3hx1e/comment/pfeuath/) |

Full history: `episodes.csv` (one row per first flag, with the numbers known at that moment).
