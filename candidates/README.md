# Stage 1 candidates

Updated 2026-10-13T03:09:36Z by run `38340292570`. A candidate is a ticker whose Reddit mentions (or hype-language
posts) in the last 24 hours jumped above its prior 7-day mean + 2 sd, with at least
10 mentions from 5 different authors. It stays listed until it goes
24 hours without a new flag. These are statistical flags, not accusations or advice.

| Ticker | Flagged since (UTC) | Why | Mentions 24h | Baseline/day | Authors | Hype posts | Subreddits | Exchange | StockTwits | Example |
|---|---|---|---|---|---|---|---|---|---|---|
| ASML | 2026-10-12 17:40 | mention spike | 17 | 3.0 | 14 | 0 | wallstreetbets 17 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1x4c9un/comment/pgeblap/) |
| BMBL | 2026-10-12 20:58 | mention spike | 13 | 0.0 | 12 | 0 | wallstreetbets 13 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1x4ac7l/) |
| CBRS | 2026-10-12 14:20 | mention spike | 44 | 5.43 | 27 | 0 | wallstreetbets 44 | Nasdaq | #21 | [link](https://www.reddit.com/r/wallstreetbets/comments/1x45v0k/) |
| IREN | 2026-10-12 03:44 | mention spike | 41 | 13.71 | 34 | 0 | wallstreetbets 41 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1x4j0dz/) |
| META | 2026-10-12 20:58 | mention spike | 47 | 17.29 | 36 | 1 | wallstreetbets 47 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1x46klu/) |
| MU | 2026-10-12 14:20 | mention spike | 32 | 7.71 | 13 | 0 | wallstreetbets 32 | Nasdaq | #1 | [link](https://www.reddit.com/r/wallstreetbets/comments/1x4awl8/) |
| NIO | 2026-10-12 22:44 | mention spike | 11 | 1.43 | 5 | 0 | wallstreetbets 11 | NYSE |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1x4e5vg/) |
| ONDS | 2026-10-12 14:47 | mention spike | 13 | 5.14 | 10 | 0 | wallstreetbets 13 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1x3xuss/comment/pfhgfgy/) |
| RDDT | 2026-10-12 20:18 | mention spike | 46 | 19.0 | 31 | 1 | wallstreetbets 46 | NYSE |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1x46klu/) |
| SKHY | 2026-10-13 02:56 | mention spike | 29 | 9.14 | 23 | 0 | wallstreetbets 29 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1x4c9un/comment/pgeokym/) |
| SNDK | 2026-10-13 01:10 | mention spike | 101 | 41.0 | 59 | 0 | wallstreetbets 101 | Nasdaq | #3 | [link](https://www.reddit.com/r/wallstreetbets/comments/1x4c9un/comment/pgen9p7/) |
| SOFI | 2026-10-12 21:51 | mention spike | 12 | 3.57 | 9 | 0 | wallstreetbets 12 | Nasdaq | #10 | [link](https://www.reddit.com/r/wallstreetbets/comments/1x4e5vg/comment/pgdaj57/) |
| TSM | 2026-10-12 15:13 | mention spike | 19 | 6.71 | 13 | 0 | wallstreetbets 19 | NYSE |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1x4486f/) |
| UNH | 2026-10-12 20:32 | mention spike | 13 | 3.43 | 13 | 0 | wallstreetbets 13 | NYSE |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1x4c9un/comment/pgebtps/) |
| WFF | 2026-10-12 18:19 | mention spike | 15 | 1.57 | 9 | 1 | wallstreetbets 9, pennystocks 6 | Nasdaq | #22 | [link](https://www.reddit.com/r/wallstreetbets/comments/1x4c9un/comment/pgd2sfc/) |
| SOXX | 2026-10-12 14:20 | mention spike | 11 | 4.86 | 8 | 0 | wallstreetbets 11 | Nasdaq | #30 | [link](https://www.reddit.com/r/wallstreetbets/comments/1x4c9un/comment/pgdglp8/) |
| SMCI | 2026-10-12 17:00 | mention spike | 12 | 4.29 | 8 | 0 | wallstreetbets 11, smallstreetbets 1 | Nasdaq |  | [link](https://www.reddit.com/r/smallstreetbets/comments/1x3tsce/) |
| MGM | 2026-10-12 06:49 | mention spike | 6 | 1.57 | 2 | 0 | wallstreetbets 6 | NYSE |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1x3trws/) |

Full history: `episodes.csv` (one row per first flag, with the numbers known at that moment).
