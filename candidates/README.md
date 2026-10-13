# Stage 1 candidates

Updated 2026-10-13T08:00:30Z by run `38366276762`. A candidate is a ticker whose Reddit mentions (or hype-language
posts) in the last 24 hours jumped above its prior 7-day mean + 2 sd, with at least
10 mentions from 5 different authors. It stays listed until it goes
24 hours without a new flag. These are statistical flags, not accusations or advice.

| Ticker | Flagged since (UTC) | Why | Mentions 24h | Baseline/day | Authors | Hype posts | Subreddits | Exchange | StockTwits | Example |
|---|---|---|---|---|---|---|---|---|---|---|
| ASML | 2026-10-12 17:40 | mention spike | 18 | 3.0 | 15 | 0 | wallstreetbets 18 | Nasdaq | #8 | [link](https://www.reddit.com/r/wallstreetbets/comments/1x4q3x5/) |
| BMBL | 2026-10-12 20:58 | mention spike | 17 | 0.0 | 15 | 0 | wallstreetbets 17 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1x4o7d7/) |
| CBRS | 2026-10-12 14:20 | mention spike | 45 | 4.86 | 28 | 0 | wallstreetbets 45 | Nasdaq | #18 | [link](https://www.reddit.com/r/wallstreetbets/comments/1x45v0k/) |
| CRWV | 2026-10-13 03:58 | mention spike | 10 | 4.0 | 10 | 0 | wallstreetbets 10 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1x4c9un/comment/pgey0f7/) |
| IREN | 2026-10-12 03:44 | mention spike | 38 | 14.43 | 31 | 0 | wallstreetbets 38 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1x4j0dz/) |
| META | 2026-10-12 20:58 | mention spike | 46 | 17.0 | 35 | 1 | wallstreetbets 46 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1x46klu/) |
| MU | 2026-10-12 14:20 | mention spike | 33 | 7.57 | 13 | 0 | wallstreetbets 33 | Nasdaq | #25 | [link](https://www.reddit.com/r/wallstreetbets/comments/1x4awl8/) |
| NBIS | 2026-10-13 03:35 | mention spike | 55 | 23.0 | 38 | 0 | wallstreetbets 55 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1x4kuuh/comment/pgfs4n0/) |
| NIO | 2026-10-12 22:44 | mention spike | 12 | 1.43 | 6 | 0 | wallstreetbets 12 | NYSE |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1x4e5vg/) |
| ONDS | 2026-10-12 14:47 | mention spike | 12 | 5.29 | 9 | 0 | wallstreetbets 12 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1vlsoz5/comment/pgfifxu/) |
| RDDT | 2026-10-12 20:18 | mention spike | 44 | 19.43 | 29 | 1 | wallstreetbets 44 | NYSE |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1x46klu/) |
| SKHY | 2026-10-13 02:56 | mention spike | 31 | 9.29 | 25 | 0 | wallstreetbets 31 | Nasdaq | #21 | [link](https://www.reddit.com/r/wallstreetbets/comments/1x4nr5m/) |
| SNDK | 2026-10-13 01:10 | mention spike | 109 | 41.86 | 64 | 0 | wallstreetbets 109 | Nasdaq | #1 | [link](https://www.reddit.com/r/wallstreetbets/comments/1x4pdjy/) |
| UNH | 2026-10-12 20:32 | mention spike | 14 | 3.43 | 14 | 0 | wallstreetbets 14 | NYSE | #6 | [link](https://www.reddit.com/r/wallstreetbets/comments/1x4c9un/comment/pgfljha/) |
| WFF | 2026-10-12 18:19 | mention spike | 14 | 1.71 | 9 | 1 | wallstreetbets 9, pennystocks 5 | Nasdaq | #3 | [link](https://www.reddit.com/r/wallstreetbets/comments/1x4c9un/comment/pgd2sfc/) |
| SXTC | 2026-10-13 08:00 | mention spike | 11 | 1.57 | 6 | 1 | pennystocks 11 | Nasdaq |  | [link](https://www.reddit.com/r/pennystocks/comments/1x438u3/) |
| TSM | 2026-10-12 15:13 | mention spike | 17 | 7.14 | 12 | 0 | wallstreetbets 17 | NYSE |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1x4486f/) |
| SOXX | 2026-10-12 14:20 | mention spike | 11 | 4.71 | 9 | 0 | wallstreetbets 11 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1x4c9un/comment/pgeut42/) |
| SOFI | 2026-10-12 21:51 | mention spike | 9 | 4.0 | 6 | 0 | wallstreetbets 9 | Nasdaq | #15 | [link](https://www.reddit.com/r/wallstreetbets/comments/1x4c9un/comment/pgflnhd/) |
| SMCI | 2026-10-12 17:00 | mention spike | 10 | 4.57 | 6 | 0 | wallstreetbets 10 | Nasdaq | #11 | [link](https://www.reddit.com/r/wallstreetbets/comments/1x4c9un/comment/pgee3q9/) |
| MGM | 2026-10-12 06:49 | mention spike | 2 | 2.14 | 1 | 0 | wallstreetbets 2 | NYSE |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1x3hx1e/comment/pfeuath/) |

Full history: `episodes.csv` (one row per first flag, with the numbers known at that moment).
