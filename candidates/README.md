# Stage 1 candidates

Updated 2026-10-19T17:18:44Z by run `39292924320`. A candidate is a ticker whose Reddit mentions (or hype-language
posts) in the last 24 hours jumped above its prior 7-day mean + 2 sd, with at least
10 mentions from 5 different authors. It stays listed until it goes
24 hours without a new flag. These are statistical flags, not accusations or advice.

| Ticker | Flagged since (UTC) | Why | Mentions 24h | Baseline/day | Authors | Hype posts | Subreddits | Exchange | StockTwits | Example |
|---|---|---|---|---|---|---|---|---|---|---|
| AMZN | 2026-10-19 16:13 | mention spike | 41 | 20.29 | 29 | 0 | wallstreetbets 41 | Nasdaq | #3 | [link](https://www.reddit.com/r/wallstreetbets/comments/1x9ox1r/) |
| GLD | 2026-10-19 16:13 | mention spike | 15 | 4.0 | 11 | 0 | wallstreetbets 15 | NYSE Arca |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1x9guju/) |
| TQQQ | 2026-10-19 16:13 | mention spike | 17 | 6.86 | 16 | 0 | wallstreetbets 17 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1x9guju/) |
| TCRT | 2026-10-19 14:18 | mention spike | 13 | 4.14 | 6 | 0 | pennystocks 13 | Nasdaq |  | [link](https://www.reddit.com/r/pennystocks/comments/1x9mwl7/comment/phpkaok/) |
| WDC | 2026-10-19 06:00 | mention spike | 17 | 11.29 | 16 | 0 | wallstreetbets 17 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xa2deu/) |
| VTI | 2026-10-18 05:58 | mention spike | 3 | 4.14 | 3 | 0 | wallstreetbets 3 | NYSE Arca |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1x825kl/comment/phpskva/) |
| SCHD | 2026-10-17 04:49 | mention spike | 5 | 6.43 | 4 | 0 | wallstreetbets 5 | NYSE Arca |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1x8t7xg/comment/pho8eri/) |

Full history: `episodes.csv` (one row per first flag, with the numbers known at that moment).
