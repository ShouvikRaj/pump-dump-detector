# Stage 1 candidates

Updated 2026-10-20T05:27:29Z by run `39374912112`. A candidate is a ticker whose Reddit mentions (or hype-language
posts) in the last 24 hours jumped above its prior 7-day mean + 2 sd, with at least
10 mentions from 5 different authors. It stays listed until it goes
24 hours without a new flag. These are statistical flags, not accusations or advice.

| Ticker | Flagged since (UTC) | Why | Mentions 24h | Baseline/day | Authors | Hype posts | Subreddits | Exchange | StockTwits | Example |
|---|---|---|---|---|---|---|---|---|---|---|
| AMZN | 2026-10-19 16:13 | mention spike | 66 | 20.29 | 39 | 0 | wallstreetbets 66 | Nasdaq | #24 | [link](https://www.reddit.com/r/wallstreetbets/comments/1xa66i7/) |
| APLD | 2026-10-20 04:07 | mention spike | 30 | 16.57 | 20 | 0 | wallstreetbets 29, smallstreetbets 1 | Nasdaq |  | [link](https://www.reddit.com/r/smallstreetbets/comments/1x9wz30/) |
| GLD | 2026-10-19 16:13 | mention spike | 18 | 4.57 | 12 | 0 | wallstreetbets 18 | NYSE Arca |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xa7cu6/comment/phszhop/) |
| NFLX | 2026-10-19 19:31 | mention spike | 26 | 10.0 | 22 | 0 | wallstreetbets 26 | Nasdaq | #4 | [link](https://www.reddit.com/r/wallstreetbets/comments/1xa8tas/) |
| RIVN | 2026-10-19 18:51 | mention spike | 23 | 2.57 | 13 | 0 | wallstreetbets 23 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xa7cu6/comment/phseny4/) |
| TCRT | 2026-10-19 14:18 | mention spike | 13 | 4.14 | 6 | 0 | pennystocks 13 | Nasdaq |  | [link](https://www.reddit.com/r/pennystocks/comments/1x9mwl7/comment/phpkaok/) |
| GOOG | 2026-10-19 22:36 | mention spike | 25 | 17.57 | 16 | 0 | wallstreetbets 25 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1x9ox1r/) |
| TQQQ | 2026-10-19 16:13 | mention spike | 8 | 8.43 | 8 | 0 | wallstreetbets 8 | Nasdaq | #23 | [link](https://www.reddit.com/r/wallstreetbets/comments/1x7chad/comment/phtstqk/) |
| WDC | 2026-10-19 06:00 | mention spike | 8 | 12.0 | 7 | 0 | wallstreetbets 8 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xa2deu/) |

Full history: `episodes.csv` (one row per first flag, with the numbers known at that moment).
