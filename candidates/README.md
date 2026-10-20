# Stage 1 candidates

Updated 2026-10-20T16:29:54Z by run `39457808963`. A candidate is a ticker whose Reddit mentions (or hype-language
posts) in the last 24 hours jumped above its prior 7-day mean + 2 sd, with at least
10 mentions from 5 different authors. It stays listed until it goes
24 hours without a new flag. These are statistical flags, not accusations or advice.

| Ticker | Flagged since (UTC) | Why | Mentions 24h | Baseline/day | Authors | Hype posts | Subreddits | Exchange | StockTwits | Example |
|---|---|---|---|---|---|---|---|---|---|---|
| AMZN | 2026-10-19 16:13 | mention spike | 63 | 24.43 | 32 | 0 | wallstreetbets 63 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xa66i7/) |
| CRWV | 2026-10-20 14:57 | mention spike | 190 | 79.71 | 90 | 0 | wallstreetbets 190 | Nasdaq | #27 | [link](https://www.reddit.com/r/wallstreetbets/comments/1xau0nd/) |
| GLD | 2026-10-19 16:13 | mention spike | 14 | 5.29 | 11 | 0 | wallstreetbets 14 | NYSE Arca |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xao1uu/comment/phwxa0y/) |
| HTZ | 2026-10-20 13:24 | mention spike | 23 | 6.86 | 14 | 1 | wallstreetbets 23 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xaqvd4/) |
| NFLX | 2026-10-19 19:31 | mention spike | 43 | 9.86 | 34 | 0 | wallstreetbets 43 | Nasdaq | #13 | [link](https://www.reddit.com/r/wallstreetbets/comments/1xa8tas/) |
| RIVN | 2026-10-19 18:51 | mention spike | 20 | 2.71 | 12 | 0 | wallstreetbets 20 | Nasdaq | #28 | [link](https://www.reddit.com/r/wallstreetbets/comments/1xao1uu/comment/phvvgmh/) |
| SPCX | 2026-10-20 10:18 | mention spike | 104 | 37.71 | 72 | 0 | wallstreetbets 104 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xad35t/) |
| IWM | 2026-10-20 16:03 | mention spike | 11 | 4.86 | 10 | 0 | wallstreetbets 11 | NYSE Arca |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xao1uu/comment/phwslve/) |
| APLD | 2026-10-20 04:07 | mention spike | 21 | 18.86 | 17 | 0 | wallstreetbets 21 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xamm2t/) |
| TCRT | 2026-10-19 14:18 | mention spike | 0 |  | 0 | 0 |  | Nasdaq |  |  |
| GOOG | 2026-10-19 22:36 | mention spike | 24 | 17.71 | 16 | 0 | wallstreetbets 24 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1x8t7xg/comment/phwmd7z/) |
| TQQQ | 2026-10-19 16:13 | mention spike | 5 | 8.86 | 5 | 1 | wallstreetbets 5 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xao1uu/comment/phv9dt7/) |

Full history: `episodes.csv` (one row per first flag, with the numbers known at that moment).
