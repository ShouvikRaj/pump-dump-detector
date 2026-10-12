# Stage 1 candidates

Updated 2026-10-12T23:11:03Z by run `38320710492`. A candidate is a ticker whose Reddit mentions (or hype-language
posts) in the last 24 hours jumped above its prior 7-day mean + 2 sd, with at least
10 mentions from 5 different authors. It stays listed until it goes
24 hours without a new flag. These are statistical flags, not accusations or advice.

| Ticker | Flagged since (UTC) | Why | Mentions 24h | Baseline/day | Authors | Hype posts | Subreddits | Exchange | StockTwits | Example |
|---|---|---|---|---|---|---|---|---|---|---|
| ASML | 2026-10-12 17:40 | mention spike | 13 | 3.0 | 11 | 0 | wallstreetbets 13 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1x4c9un/comment/pfj3qmb/) |
| BMBL | 2026-10-12 20:58 | mention spike | 12 | 0.0 | 11 | 0 | wallstreetbets 12 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1x4ac7l/) |
| CBRS | 2026-10-12 14:20 | mention spike | 41 | 5.14 | 22 | 0 | wallstreetbets 41 | Nasdaq | #2 | [link](https://www.reddit.com/r/wallstreetbets/comments/1x45v0k/) |
| IREN | 2026-10-12 03:44 | mention spike | 47 | 11.0 | 37 | 0 | wallstreetbets 47 | Nasdaq | #30 | [link](https://www.reddit.com/r/wallstreetbets/comments/1x4cb65/) |
| META | 2026-10-12 20:58 | mention spike | 43 | 17.57 | 32 | 1 | wallstreetbets 43 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1x46klu/) |
| MU | 2026-10-12 14:20 | mention spike | 31 | 8.0 | 12 | 0 | wallstreetbets 31 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1x4awl8/) |
| NIO | 2026-10-12 22:44 | mention spike | 11 | 1.43 | 5 | 0 | wallstreetbets 11 | NYSE |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1x4e5vg/) |
| ONDS | 2026-10-12 14:47 | mention spike | 14 | 5.0 | 11 | 0 | wallstreetbets 14 | Nasdaq | #3 | [link](https://www.reddit.com/r/wallstreetbets/comments/1x3xuss/comment/pfhgfgy/) |
| RDDT | 2026-10-12 20:18 | mention spike | 43 | 18.71 | 29 | 1 | wallstreetbets 43 | NYSE |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1x46klu/) |
| SOFI | 2026-10-12 21:51 | mention spike | 12 | 3.57 | 9 | 0 | wallstreetbets 12 | Nasdaq | #29 | [link](https://www.reddit.com/r/wallstreetbets/comments/1x4e5vg/comment/pgdaj57/) |
| SOXX | 2026-10-12 14:20 | mention spike | 12 | 4.71 | 9 | 0 | wallstreetbets 12 | Nasdaq | #21 | [link](https://www.reddit.com/r/wallstreetbets/comments/1x4c9un/comment/pgdglp8/) |
| UNH | 2026-10-12 20:32 | mention spike | 11 | 3.29 | 11 | 0 | wallstreetbets 11 | NYSE | #6 | [link](https://www.reddit.com/r/wallstreetbets/comments/1x4c9un/comment/pgdava9/) |
| WFF | 2026-10-12 18:19 | mention spike | 15 | 1.57 | 9 | 1 | wallstreetbets 9, pennystocks 6 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1x4c9un/comment/pgd2sfc/) |
| TSM | 2026-10-12 15:13 | mention spike | 17 | 6.71 | 12 | 0 | wallstreetbets 17 | NYSE | #23 | [link](https://www.reddit.com/r/wallstreetbets/comments/1x4486f/) |
| SMCI | 2026-10-12 17:00 | mention spike | 10 | 4.29 | 6 | 0 | wallstreetbets 9, smallstreetbets 1 | Nasdaq |  | [link](https://www.reddit.com/r/smallstreetbets/comments/1x3tsce/) |
| MGM | 2026-10-12 06:49 | mention spike | 6 | 1.57 | 2 | 0 | wallstreetbets 6 | NYSE |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1x3trws/) |

Full history: `episodes.csv` (one row per first flag, with the numbers known at that moment).
