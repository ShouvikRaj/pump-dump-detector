# Stage 1 candidates

Updated 2026-10-13T13:18:50Z by run `38403839380`. A candidate is a ticker whose Reddit mentions (or hype-language
posts) in the last 24 hours jumped above its prior 7-day mean + 2 sd, with at least
10 mentions from 5 different authors. It stays listed until it goes
24 hours without a new flag. These are statistical flags, not accusations or advice.

| Ticker | Flagged since (UTC) | Why | Mentions 24h | Baseline/day | Authors | Hype posts | Subreddits | Exchange | StockTwits | Example |
|---|---|---|---|---|---|---|---|---|---|---|
| ASML | 2026-10-12 17:40 | mention spike | 16 | 3.43 | 12 | 0 | wallstreetbets 16 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1x4q3x5/) |
| BMBL | 2026-10-12 20:58 | mention spike | 20 | 0.0 | 17 | 0 | wallstreetbets 20 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1x4vom8/) |
| CBRS | 2026-10-12 14:20 | mention spike | 44 | 4.71 | 28 | 0 | wallstreetbets 44 | Nasdaq | #28 | [link](https://www.reddit.com/r/wallstreetbets/comments/1x45v0k/) |
| IREN | 2026-10-12 03:44 | mention spike | 39 | 14.86 | 33 | 0 | wallstreetbets 39 | Nasdaq | #9 | [link](https://www.reddit.com/r/wallstreetbets/comments/1x4j0dz/) |
| JPM | 2026-10-13 10:39 | mention spike | 37 | 4.43 | 26 | 0 | wallstreetbets 37 | NYSE | #6 | [link](https://www.reddit.com/r/wallstreetbets/comments/1x4skqc/comment/pggndb7/) |
| META | 2026-10-12 20:58 | mention spike | 48 | 17.14 | 35 | 1 | wallstreetbets 48 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1x46klu/) |
| MU | 2026-10-12 14:20 | mention spike | 36 | 7.43 | 14 | 0 | wallstreetbets 36 | Nasdaq | #2 | [link](https://www.reddit.com/r/wallstreetbets/comments/1x4awl8/) |
| NBIS | 2026-10-13 03:35 | mention spike | 53 | 23.86 | 37 | 0 | wallstreetbets 53 | Nasdaq | #12 | [link](https://www.reddit.com/r/wallstreetbets/comments/1x4skqc/comment/pgh5511/) |
| NIO | 2026-10-12 22:44 | mention spike | 12 | 1.43 | 6 | 0 | wallstreetbets 12 | NYSE |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1x4e5vg/) |
| RDDT | 2026-10-12 20:18 | mention spike | 46 | 19.43 | 31 | 1 | wallstreetbets 46 | NYSE |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1x46klu/) |
| SKHY | 2026-10-13 02:56 | mention spike | 33 | 9.71 | 27 | 0 | wallstreetbets 33 | Nasdaq | #10 | [link](https://www.reddit.com/r/wallstreetbets/comments/1x4nr5m/) |
| SNDK | 2026-10-13 01:10 | mention spike | 119 | 42.14 | 69 | 1 | wallstreetbets 119 | Nasdaq | #4 | [link](https://www.reddit.com/r/wallstreetbets/comments/1x4pdjy/) |
| SOXX | 2026-10-12 14:20 | mention spike | 17 | 4.86 | 11 | 0 | wallstreetbets 17 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1x4skqc/comment/pggpa0j/) |
| SXTC | 2026-10-13 08:00 | mention spike | 10 | 2.0 | 5 | 1 | pennystocks 10 | Nasdaq |  | [link](https://www.reddit.com/r/pennystocks/comments/1x438u3/) |
| TSM | 2026-10-12 15:13 | mention spike | 17 | 6.43 | 12 | 0 | wallstreetbets 17 | NYSE |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1x4486f/) |
| UNH | 2026-10-12 20:32 | mention spike | 28 | 3.43 | 27 | 0 | wallstreetbets 28 | NYSE | #3 | [link](https://www.reddit.com/r/wallstreetbets/comments/1x4skqc/comment/pgh3n1l/) |
| WFF | 2026-10-12 18:19 | mention spike | 14 | 1.71 | 9 | 1 | wallstreetbets 9, pennystocks 5 | Nasdaq | #7 | [link](https://www.reddit.com/r/wallstreetbets/comments/1x4c9un/comment/pgd2sfc/) |
| ONDS | 2026-10-12 14:47 | mention spike | 10 | 5.86 | 7 | 0 | wallstreetbets 10 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1x4skqc/comment/pggsqhn/) |
| CRWV | 2026-10-13 03:58 | mention spike | 7 | 4.71 | 7 | 0 | wallstreetbets 7 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1x4skqc/comment/pgh1ang/) |
| SOFI | 2026-10-12 21:51 | mention spike | 7 | 4.29 | 4 | 0 | wallstreetbets 7 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1x4c9un/comment/pgflnhd/) |
| SMCI | 2026-10-12 17:00 | mention spike | 10 | 4.57 | 6 | 0 | wallstreetbets 10 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1x4c9un/comment/pgee3q9/) |

Full history: `episodes.csv` (one row per first flag, with the numbers known at that moment).
