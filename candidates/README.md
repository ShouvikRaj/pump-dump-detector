# Stage 1 candidates

Updated 2026-11-19T23:10:09Z by run `44634593543`. A candidate is a ticker whose Reddit mentions (or hype-language
posts) in the last 24 hours jumped above its prior 7-day mean + 2 sd, with at least
10 mentions from 5 different authors. It stays listed until it goes
24 hours without a new flag. These are statistical flags, not accusations or advice.

| Ticker | Flagged since (UTC) | Why | Mentions 24h | Baseline/day | Authors | Hype posts | Subreddits | Exchange | StockTwits | Example |
|---|---|---|---|---|---|---|---|---|---|---|
| ANT | 2026-11-19 00:42 | hype spike mention spike | 606 | 152.0 | 405 | 1 | wallstreetbets 605, pennystocks 1 | ? | #1 | [link](https://www.reddit.com/r/wallstreetbets/comments/1y0kb9y/) |
| PANW | 2026-11-18 21:40 | mention spike | 2 | 8.57 | 2 | 0 | wallstreetbets 2 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xzqpcz/comment/19sul3jt0chxh/) |
| UNH | 2026-11-18 17:15 | mention spike | 7 | 5.0 | 7 | 0 | wallstreetbets 7 | NYSE |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1y0em9g/) |
| AMZN | 2026-11-19 00:49 | mention spike | 20 | 17.43 | 17 | 0 | wallstreetbets 20 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xzw3vl/) |
| TTWO | 2026-11-19 00:42 | mention spike | 7 | 16.0 | 6 | 0 | wallstreetbets 7 | Nasdaq | #22 | [link](https://www.reddit.com/r/wallstreetbets/comments/1y0eqrp/) |
| LULU | 2026-11-19 00:49 | mention spike | 1 | 2.29 | 1 | 0 | wallstreetbets 1 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xzqpcz/comment/19sunp5qplqdh/) |
| CRWD | 2026-11-19 03:02 | mention spike | 1 | 5.71 | 1 | 0 | wallstreetbets 1 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xzqpcz/comment/19sul3jt0chxh/) |
| SPCX | 2026-11-19 00:49 | mention spike | 29 | 52.57 | 27 | 0 | wallstreetbets 29 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1y0lkw0/) |
| MU | 2026-11-19 01:56 | mention spike | 3 | 5.29 | 3 | 0 | wallstreetbets 3 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1y06n5x/comment/19svpev5rf7yb/) |
| GLD | 2026-11-19 00:42 | mention spike | 0 |  | 0 | 0 |  | NYSE Arca | #5 |  |

Full history: `episodes.csv` (one row per first flag, with the numbers known at that moment).
