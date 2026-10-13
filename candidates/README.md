# Stage 1 candidates

Updated 2026-10-13T11:06:04Z by run `38387801618`. A candidate is a ticker whose Reddit mentions (or hype-language
posts) in the last 24 hours jumped above its prior 7-day mean + 2 sd, with at least
10 mentions from 5 different authors. It stays listed until it goes
24 hours without a new flag. These are statistical flags, not accusations or advice.

| Ticker | Flagged since (UTC) | Why | Mentions 24h | Baseline/day | Authors | Hype posts | Subreddits | Exchange | StockTwits | Example |
|---|---|---|---|---|---|---|---|---|---|---|
| ASML | 2026-10-12 17:40 | mention spike | 16 | 3.29 | 13 | 0 | wallstreetbets 16 | Nasdaq | #11 | [link](https://www.reddit.com/r/wallstreetbets/comments/1x4q3x5/) |
| BMBL | 2026-10-12 20:58 | mention spike | 17 | 0.0 | 15 | 0 | wallstreetbets 17 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1x4o7d7/) |
| CBRS | 2026-10-12 14:20 | mention spike | 44 | 5.0 | 28 | 0 | wallstreetbets 44 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1x45v0k/) |
| IREN | 2026-10-12 03:44 | mention spike | 40 | 14.86 | 33 | 0 | wallstreetbets 40 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1x4j0dz/) |
| JPM | 2026-10-13 10:39 | mention spike | 21 | 4.43 | 15 | 0 | wallstreetbets 21 | NYSE | #2 | [link](https://www.reddit.com/r/wallstreetbets/comments/1x4skqc/comment/pgghiyh/) |
| META | 2026-10-12 20:58 | mention spike | 46 | 17.0 | 35 | 1 | wallstreetbets 46 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1x46klu/) |
| MU | 2026-10-12 14:20 | mention spike | 32 | 7.43 | 13 | 0 | wallstreetbets 32 | Nasdaq | #18 | [link](https://www.reddit.com/r/wallstreetbets/comments/1x4awl8/) |
| NIO | 2026-10-12 22:44 | mention spike | 12 | 1.43 | 6 | 0 | wallstreetbets 12 | NYSE |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1x4e5vg/) |
| ONDS | 2026-10-12 14:47 | mention spike | 11 | 5.43 | 8 | 0 | wallstreetbets 11 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1vlsoz5/comment/pgfifxu/) |
| RDDT | 2026-10-12 20:18 | mention spike | 45 | 19.43 | 30 | 1 | wallstreetbets 45 | NYSE |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1x46klu/) |
| SKHY | 2026-10-13 02:56 | mention spike | 33 | 9.57 | 27 | 0 | wallstreetbets 33 | Nasdaq | #25 | [link](https://www.reddit.com/r/wallstreetbets/comments/1x4nr5m/) |
| SNDK | 2026-10-13 01:10 | mention spike | 114 | 41.86 | 65 | 0 | wallstreetbets 114 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1x4pdjy/) |
| SXTC | 2026-10-13 08:00 | mention spike | 10 | 1.71 | 6 | 1 | pennystocks 10 | Nasdaq |  | [link](https://www.reddit.com/r/pennystocks/comments/1x438u3/) |
| TSM | 2026-10-12 15:13 | mention spike | 17 | 7.0 | 12 | 0 | wallstreetbets 17 | NYSE |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1x4486f/) |
| UNH | 2026-10-12 20:32 | mention spike | 21 | 3.43 | 20 | 0 | wallstreetbets 21 | NYSE | #1 | [link](https://www.reddit.com/r/wallstreetbets/comments/1x4skqc/comment/pggcmtm/) |
| WFF | 2026-10-12 18:19 | mention spike | 14 | 1.71 | 9 | 1 | wallstreetbets 9, pennystocks 5 | Nasdaq | #4 | [link](https://www.reddit.com/r/wallstreetbets/comments/1x4c9un/comment/pgd2sfc/) |
| NBIS | 2026-10-13 03:35 | mention spike | 54 | 23.0 | 37 | 0 | wallstreetbets 54 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1x4kuuh/comment/pgfs4n0/) |
| SOXX | 2026-10-12 14:20 | mention spike | 12 | 4.86 | 10 | 0 | wallstreetbets 12 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1x4q3x5/comment/pggerfq/) |
| CRWV | 2026-10-13 03:58 | mention spike | 10 | 4.0 | 10 | 0 | wallstreetbets 10 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1x4c9un/comment/pgey0f7/) |
| SOFI | 2026-10-12 21:51 | mention spike | 7 | 4.29 | 4 | 0 | wallstreetbets 7 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1x4c9un/comment/pgflnhd/) |
| SMCI | 2026-10-12 17:00 | mention spike | 10 | 4.57 | 6 | 0 | wallstreetbets 10 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1x4c9un/comment/pgee3q9/) |
| MGM | 2026-10-12 06:49 | mention spike | 0 |  | 0 | 0 |  | NYSE |  |  |

Full history: `episodes.csv` (one row per first flag, with the numbers known at that moment).
