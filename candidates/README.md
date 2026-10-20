# Stage 1 candidates

Updated 2026-10-20T15:11:53Z by run `39445811507`. A candidate is a ticker whose Reddit mentions (or hype-language
posts) in the last 24 hours jumped above its prior 7-day mean + 2 sd, with at least
10 mentions from 5 different authors. It stays listed until it goes
24 hours without a new flag. These are statistical flags, not accusations or advice.

| Ticker | Flagged since (UTC) | Why | Mentions 24h | Baseline/day | Authors | Hype posts | Subreddits | Exchange | StockTwits | Example |
|---|---|---|---|---|---|---|---|---|---|---|
| AMZN | 2026-10-19 16:13 | mention spike | 77 | 22.0 | 43 | 0 | wallstreetbets 77 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xa66i7/) |
| CRWV | 2026-10-20 14:57 | mention spike | 189 | 78.86 | 90 | 0 | wallstreetbets 189 | Nasdaq | #1 | [link](https://www.reddit.com/r/wallstreetbets/comments/1xau0nd/) |
| GLD | 2026-10-19 16:13 | mention spike | 16 | 4.86 | 12 | 0 | wallstreetbets 16 | NYSE Arca |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xao1uu/comment/phwgpe2/) |
| HTZ | 2026-10-20 13:24 | mention spike | 22 | 6.86 | 13 | 1 | wallstreetbets 22 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xaqvd4/) |
| NFLX | 2026-10-19 19:31 | mention spike | 36 | 9.71 | 29 | 0 | wallstreetbets 36 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xa8tas/) |
| RIVN | 2026-10-19 18:51 | mention spike | 23 | 2.43 | 12 | 0 | wallstreetbets 23 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xao1uu/comment/phvvgmh/) |
| SPCX | 2026-10-20 10:18 | mention spike | 99 | 36.57 | 67 | 0 | wallstreetbets 99 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xad35t/) |
| APLD | 2026-10-20 04:07 | mention spike | 20 | 18.71 | 15 | 0 | wallstreetbets 20 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xamm2t/) |
| TCRT | 2026-10-19 14:18 | mention spike | 1 | 5.86 | 1 | 0 | pennystocks 1 | Nasdaq |  | [link](https://www.reddit.com/r/pennystocks/comments/1x9mwl7/comment/phpkaok/) |
| GOOG | 2026-10-19 22:36 | mention spike | 24 | 17.57 | 15 | 0 | wallstreetbets 24 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xao1uu/comment/phw7bv5/) |
| TQQQ | 2026-10-19 16:13 | mention spike | 8 | 8.43 | 8 | 1 | wallstreetbets 8 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xao1uu/comment/phv9dt7/) |

Full history: `episodes.csv` (one row per first flag, with the numbers known at that moment).
