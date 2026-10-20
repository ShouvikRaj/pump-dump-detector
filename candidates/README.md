# Stage 1 candidates

Updated 2026-10-20T16:56:37Z by run `39461668291`. A candidate is a ticker whose Reddit mentions (or hype-language
posts) in the last 24 hours jumped above its prior 7-day mean + 2 sd, with at least
10 mentions from 5 different authors. It stays listed until it goes
24 hours without a new flag. These are statistical flags, not accusations or advice.

| Ticker | Flagged since (UTC) | Why | Mentions 24h | Baseline/day | Authors | Hype posts | Subreddits | Exchange | StockTwits | Example |
|---|---|---|---|---|---|---|---|---|---|---|
| AMZN | 2026-10-19 16:13 | mention spike | 65 | 24.43 | 33 | 0 | wallstreetbets 65 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xa66i7/) |
| CRWV | 2026-10-20 14:57 | mention spike | 189 | 80.14 | 88 | 0 | wallstreetbets 189 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xau0nd/) |
| HTZ | 2026-10-20 13:24 | mention spike | 23 | 6.86 | 14 | 1 | wallstreetbets 23 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xaqvd4/) |
| LRCX | 2026-10-20 16:42 | mention spike | 11 | 1.86 | 5 | 0 | wallstreetbets 11 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xao1uu/comment/phx0wj9/) |
| NFLX | 2026-10-19 19:31 | mention spike | 46 | 9.57 | 36 | 0 | wallstreetbets 46 | Nasdaq | #6 | [link](https://www.reddit.com/r/wallstreetbets/comments/1xa8tas/) |
| RIVN | 2026-10-19 18:51 | mention spike | 20 | 2.71 | 12 | 0 | wallstreetbets 20 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xao1uu/comment/phvvgmh/) |
| SPCX | 2026-10-20 10:18 | mention spike | 106 | 38.0 | 74 | 0 | wallstreetbets 106 | Nasdaq | #19 | [link](https://www.reddit.com/r/wallstreetbets/comments/1xad35t/) |
| GLD | 2026-10-19 16:13 | mention spike | 11 | 5.71 | 9 | 0 | wallstreetbets 11 | NYSE Arca |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xao1uu/comment/phwxa0y/) |
| IWM | 2026-10-20 16:03 | mention spike | 11 | 4.86 | 10 | 0 | wallstreetbets 11 | NYSE Arca |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xao1uu/comment/phwslve/) |
| APLD | 2026-10-20 04:07 | mention spike | 22 | 18.86 | 18 | 0 | wallstreetbets 22 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xamm2t/) |
| TCRT | 2026-10-19 14:18 | mention spike | 0 |  | 0 | 0 |  | Nasdaq |  |  |
| GOOG | 2026-10-19 22:36 | mention spike | 26 | 17.57 | 17 | 0 | wallstreetbets 26 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xao1uu/comment/phx4fla/) |
| TQQQ | 2026-10-19 16:13 | mention spike | 5 | 8.86 | 5 | 1 | wallstreetbets 5 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xao1uu/comment/phv9dt7/) |

Full history: `episodes.csv` (one row per first flag, with the numbers known at that moment).
