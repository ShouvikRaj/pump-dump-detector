# Stage 1 candidates

Updated 2026-11-19T17:10:06Z by run `44573563656`. A candidate is a ticker whose Reddit mentions (or hype-language
posts) in the last 24 hours jumped above its prior 7-day mean + 2 sd, with at least
10 mentions from 5 different authors. It stays listed until it goes
24 hours without a new flag. These are statistical flags, not accusations or advice.

| Ticker | Flagged since (UTC) | Why | Mentions 24h | Baseline/day | Authors | Hype posts | Subreddits | Exchange | StockTwits | Example |
|---|---|---|---|---|---|---|---|---|---|---|
| ANT | 2026-11-19 00:42 | hype spike mention spike | 744 | 133.43 | 472 | 1 | wallstreetbets 744 | ? | #1 | [link](https://www.reddit.com/r/wallstreetbets/comments/1y0efjx/) |
| PANW | 2026-11-18 21:40 | mention spike | 36 | 3.71 | 29 | 1 | wallstreetbets 36 | Nasdaq | #7 | [link](https://www.reddit.com/r/wallstreetbets/comments/1xzqpcz/comment/19sul3jt0chxh/) |
| UNH | 2026-11-18 17:15 | mention spike | 10 | 4.57 | 10 | 0 | wallstreetbets 10 | NYSE | #5 | [link](https://www.reddit.com/r/wallstreetbets/comments/1y0em9g/) |
| AMZN | 2026-11-19 00:49 | mention spike | 27 | 17.86 | 23 | 0 | wallstreetbets 27 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xzw3vl/) |
| TTWO | 2026-11-19 00:42 | mention spike | 8 | 16.14 | 7 | 0 | wallstreetbets 8 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1y06n5x/comment/19svfs5wc8kci/) |
| LULU | 2026-11-19 00:49 | mention spike | 3 | 2.0 | 2 | 0 | wallstreetbets 3 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xzqpcz/comment/19sunp5qplqdh/) |
| CRWD | 2026-11-19 03:02 | mention spike | 9 | 4.57 | 8 | 0 | wallstreetbets 9 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xzqpcz/comment/19sul3jt0chxh/) |
| SPCX | 2026-11-19 00:49 | mention spike | 39 | 53.86 | 37 | 0 | wallstreetbets 39 | Nasdaq | #12 | [link](https://www.reddit.com/r/wallstreetbets/comments/1y0asod/) |
| MU | 2026-11-19 01:56 | mention spike | 5 | 5.29 | 4 | 0 | wallstreetbets 5 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1y06n5x/comment/19svpev5rf7yb/) |
| GLD | 2026-11-19 00:42 | mention spike | 0 |  | 0 | 0 |  | NYSE Arca | #22 |  |
| AAOI | 2026-11-17 23:46 | mention spike | 1 | 5.29 | 1 | 0 | wallstreetbets 1 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1y0eg3e/) |

Full history: `episodes.csv` (one row per first flag, with the numbers known at that moment).
