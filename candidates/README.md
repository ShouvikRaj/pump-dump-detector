# Stage 1 candidates

Updated 2026-10-13T09:33:15Z by run `38377063194`. A candidate is a ticker whose Reddit mentions (or hype-language
posts) in the last 24 hours jumped above its prior 7-day mean + 2 sd, with at least
10 mentions from 5 different authors. It stays listed until it goes
24 hours without a new flag. These are statistical flags, not accusations or advice.

| Ticker | Flagged since (UTC) | Why | Mentions 24h | Baseline/day | Authors | Hype posts | Subreddits | Exchange | StockTwits | Example |
|---|---|---|---|---|---|---|---|---|---|---|
| ASML | 2026-10-12 17:40 | mention spike | 17 | 3.14 | 14 | 0 | wallstreetbets 17 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1x4q3x5/) |
| BMBL | 2026-10-12 20:58 | mention spike | 17 | 0.0 | 15 | 0 | wallstreetbets 17 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1x4o7d7/) |
| CBRS | 2026-10-12 14:20 | mention spike | 45 | 4.86 | 28 | 0 | wallstreetbets 45 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1x45v0k/) |
| IREN | 2026-10-12 03:44 | mention spike | 42 | 14.57 | 35 | 0 | wallstreetbets 42 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1x4j0dz/) |
| META | 2026-10-12 20:58 | mention spike | 46 | 17.0 | 35 | 1 | wallstreetbets 46 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1x46klu/) |
| MU | 2026-10-12 14:20 | mention spike | 32 | 7.43 | 13 | 0 | wallstreetbets 32 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1x4awl8/) |
| NBIS | 2026-10-13 03:35 | mention spike | 55 | 23.0 | 38 | 0 | wallstreetbets 55 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1x4kuuh/comment/pgfs4n0/) |
| NIO | 2026-10-12 22:44 | mention spike | 12 | 1.43 | 6 | 0 | wallstreetbets 12 | NYSE |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1x4e5vg/) |
| ONDS | 2026-10-12 14:47 | mention spike | 12 | 5.29 | 9 | 0 | wallstreetbets 12 | Nasdaq | #4 | [link](https://www.reddit.com/r/wallstreetbets/comments/1vlsoz5/comment/pgfifxu/) |
| RDDT | 2026-10-12 20:18 | mention spike | 44 | 19.43 | 29 | 1 | wallstreetbets 44 | NYSE |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1x46klu/) |
| SKHY | 2026-10-13 02:56 | mention spike | 30 | 9.43 | 25 | 0 | wallstreetbets 30 | Nasdaq | #2 | [link](https://www.reddit.com/r/wallstreetbets/comments/1x4nr5m/) |
| SNDK | 2026-10-13 01:10 | mention spike | 110 | 42.14 | 64 | 0 | wallstreetbets 110 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1x4pdjy/) |
| SXTC | 2026-10-13 08:00 | mention spike | 11 | 1.57 | 6 | 1 | pennystocks 11 | Nasdaq |  | [link](https://www.reddit.com/r/pennystocks/comments/1x438u3/) |
| UNH | 2026-10-12 20:32 | mention spike | 14 | 3.43 | 14 | 0 | wallstreetbets 14 | NYSE | #3 | [link](https://www.reddit.com/r/wallstreetbets/comments/1x4c9un/comment/pgfljha/) |
| WFF | 2026-10-12 18:19 | mention spike | 14 | 1.71 | 9 | 1 | wallstreetbets 9, pennystocks 5 | Nasdaq | #1 | [link](https://www.reddit.com/r/wallstreetbets/comments/1x4c9un/comment/pgd2sfc/) |
| SOXX | 2026-10-12 14:20 | mention spike | 11 | 4.86 | 9 | 0 | wallstreetbets 11 | Nasdaq | #19 | [link](https://www.reddit.com/r/wallstreetbets/comments/1x4c9un/comment/pgfxxs0/) |
| CRWV | 2026-10-13 03:58 | mention spike | 10 | 4.0 | 10 | 0 | wallstreetbets 10 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1x4c9un/comment/pgey0f7/) |
| TSM | 2026-10-12 15:13 | mention spike | 17 | 7.0 | 12 | 0 | wallstreetbets 17 | NYSE |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1x4486f/) |
| SOFI | 2026-10-12 21:51 | mention spike | 8 | 4.14 | 5 | 0 | wallstreetbets 8 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1x4c9un/comment/pgflnhd/) |
| SMCI | 2026-10-12 17:00 | mention spike | 10 | 4.57 | 6 | 0 | wallstreetbets 10 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1x4c9un/comment/pgee3q9/) |
| MGM | 2026-10-12 06:49 | mention spike | 0 |  | 0 | 0 |  | NYSE |  |  |

Full history: `episodes.csv` (one row per first flag, with the numbers known at that moment).
