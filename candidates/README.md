# Stage 1 candidates

Updated 2026-10-20T15:24:07Z by run `39447820865`. A candidate is a ticker whose Reddit mentions (or hype-language
posts) in the last 24 hours jumped above its prior 7-day mean + 2 sd, with at least
10 mentions from 5 different authors. It stays listed until it goes
24 hours without a new flag. These are statistical flags, not accusations or advice.

| Ticker | Flagged since (UTC) | Why | Mentions 24h | Baseline/day | Authors | Hype posts | Subreddits | Exchange | StockTwits | Example |
|---|---|---|---|---|---|---|---|---|---|---|
| AMZN | 2026-10-19 16:13 | mention spike | 75 | 22.57 | 41 | 0 | wallstreetbets 75 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xa66i7/) |
| CRWV | 2026-10-20 14:57 | mention spike | 192 | 79.0 | 90 | 0 | wallstreetbets 192 | Nasdaq | #1 | [link](https://www.reddit.com/r/wallstreetbets/comments/1xau0nd/) |
| GLD | 2026-10-19 16:13 | mention spike | 15 | 5.0 | 12 | 0 | wallstreetbets 15 | NYSE Arca |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xao1uu/comment/phwgpe2/) |
| HTZ | 2026-10-20 13:24 | mention spike | 22 | 6.86 | 13 | 1 | wallstreetbets 22 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xaqvd4/) |
| NFLX | 2026-10-19 19:31 | mention spike | 35 | 9.86 | 28 | 0 | wallstreetbets 35 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xa8tas/) |
| RIVN | 2026-10-19 18:51 | mention spike | 23 | 2.43 | 12 | 0 | wallstreetbets 23 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xao1uu/comment/phvvgmh/) |
| SPCX | 2026-10-20 10:18 | mention spike | 95 | 37.14 | 66 | 0 | wallstreetbets 95 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xad35t/) |
| APLD | 2026-10-20 04:07 | mention spike | 20 | 18.71 | 15 | 0 | wallstreetbets 20 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xamm2t/) |
| TCRT | 2026-10-19 14:18 | mention spike | 0 |  | 0 | 0 |  | Nasdaq |  |  |
| GOOG | 2026-10-19 22:36 | mention spike | 25 | 17.57 | 16 | 0 | wallstreetbets 25 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1x8t7xg/comment/phwmd7z/) |
| TQQQ | 2026-10-19 16:13 | mention spike | 6 | 8.71 | 6 | 1 | wallstreetbets 6 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xao1uu/comment/phv9dt7/) |

Full history: `episodes.csv` (one row per first flag, with the numbers known at that moment).
