# Stage 1 candidates

Updated 2026-10-19T17:58:40Z by run `39298560005`. A candidate is a ticker whose Reddit mentions (or hype-language
posts) in the last 24 hours jumped above its prior 7-day mean + 2 sd, with at least
10 mentions from 5 different authors. It stays listed until it goes
24 hours without a new flag. These are statistical flags, not accusations or advice.

| Ticker | Flagged since (UTC) | Why | Mentions 24h | Baseline/day | Authors | Hype posts | Subreddits | Exchange | StockTwits | Example |
|---|---|---|---|---|---|---|---|---|---|---|
| AMZN | 2026-10-19 16:13 | mention spike | 43 | 20.14 | 30 | 0 | wallstreetbets 43 | Nasdaq | #10 | [link](https://www.reddit.com/r/wallstreetbets/comments/1x9ox1r/) |
| GLD | 2026-10-19 16:13 | mention spike | 16 | 4.0 | 12 | 0 | wallstreetbets 16 | NYSE Arca |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1x9guju/) |
| TQQQ | 2026-10-19 16:13 | mention spike | 17 | 6.86 | 16 | 0 | wallstreetbets 17 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1x9guju/) |
| TCRT | 2026-10-19 14:18 | mention spike | 13 | 4.14 | 6 | 0 | pennystocks 13 | Nasdaq |  | [link](https://www.reddit.com/r/pennystocks/comments/1x9mwl7/comment/phpkaok/) |
| WDC | 2026-10-19 06:00 | mention spike | 16 | 11.43 | 15 | 0 | wallstreetbets 16 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xa2deu/) |
| VTI | 2026-10-18 05:58 | mention spike | 4 | 4.14 | 4 | 0 | wallstreetbets 4 | NYSE Arca |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1x8t7xg/comment/phqjudf/) |
| SCHD | 2026-10-17 04:49 | mention spike | 6 | 6.43 | 5 | 0 | wallstreetbets 6 | NYSE Arca |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1x8t7xg/comment/phqjudf/) |

Full history: `episodes.csv` (one row per first flag, with the numbers known at that moment).
