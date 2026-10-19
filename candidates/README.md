# Stage 1 candidates

Updated 2026-10-19T20:12:24Z by run `39317085645`. A candidate is a ticker whose Reddit mentions (or hype-language
posts) in the last 24 hours jumped above its prior 7-day mean + 2 sd, with at least
10 mentions from 5 different authors. It stays listed until it goes
24 hours without a new flag. These are statistical flags, not accusations or advice.

| Ticker | Flagged since (UTC) | Why | Mentions 24h | Baseline/day | Authors | Hype posts | Subreddits | Exchange | StockTwits | Example |
|---|---|---|---|---|---|---|---|---|---|---|
| AMZN | 2026-10-19 16:13 | mention spike | 54 | 20.29 | 35 | 0 | wallstreetbets 54 | Nasdaq | #16 | [link](https://www.reddit.com/r/wallstreetbets/comments/1xa66i7/) |
| GLD | 2026-10-19 16:13 | mention spike | 19 | 4.0 | 13 | 0 | wallstreetbets 19 | NYSE Arca |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1x9guju/) |
| NFLX | 2026-10-19 19:31 | mention spike | 19 | 9.29 | 18 | 0 | wallstreetbets 19 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1x9ss3y/comment/phrcjit/) |
| RIVN | 2026-10-19 18:51 | mention spike | 13 | 2.57 | 9 | 0 | wallstreetbets 13 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xa2z09/comment/phqz762/) |
| TQQQ | 2026-10-19 16:13 | mention spike | 18 | 6.86 | 17 | 0 | wallstreetbets 18 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1x9guju/) |
| TCRT | 2026-10-19 14:18 | mention spike | 13 | 4.14 | 6 | 0 | pennystocks 13 | Nasdaq |  | [link](https://www.reddit.com/r/pennystocks/comments/1x9mwl7/comment/phpkaok/) |
| WDC | 2026-10-19 06:00 | mention spike | 13 | 11.86 | 12 | 0 | wallstreetbets 13 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xa2deu/) |
| VTI | 2026-10-18 05:58 | mention spike | 5 | 4.0 | 5 | 0 | wallstreetbets 5 | NYSE Arca |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xa0bbn/comment/phr7yfr/) |
| SCHD | 2026-10-17 04:49 | mention spike | 8 | 6.43 | 7 | 0 | wallstreetbets 8 | NYSE Arca |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1x8t7xg/comment/phqshfm/) |

Full history: `episodes.csv` (one row per first flag, with the numbers known at that moment).
