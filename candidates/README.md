# Stage 1 candidates

Updated 2026-11-19T21:21:10Z by run `44617549698`. A candidate is a ticker whose Reddit mentions (or hype-language
posts) in the last 24 hours jumped above its prior 7-day mean + 2 sd, with at least
10 mentions from 5 different authors. It stays listed until it goes
24 hours without a new flag. These are statistical flags, not accusations or advice.

| Ticker | Flagged since (UTC) | Why | Mentions 24h | Baseline/day | Authors | Hype posts | Subreddits | Exchange | StockTwits | Example |
|---|---|---|---|---|---|---|---|---|---|---|
| ANT | 2026-11-19 00:42 | hype spike mention spike | 713 | 137.57 | 464 | 1 | wallstreetbets 712, pennystocks 1 | ? | #1 | [link](https://www.reddit.com/r/wallstreetbets/comments/1y0kb9y/) |
| PANW | 2026-11-18 21:40 | mention spike | 17 | 6.43 | 15 | 1 | wallstreetbets 17 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xzqpcz/comment/19sul3jt0chxh/) |
| UNH | 2026-11-18 17:15 | mention spike | 9 | 4.71 | 9 | 0 | wallstreetbets 9 | NYSE |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1y0em9g/) |
| AMZN | 2026-11-19 00:49 | mention spike | 23 | 17.0 | 20 | 0 | wallstreetbets 23 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xzw3vl/) |
| TTWO | 2026-11-19 00:42 | mention spike | 8 | 16.0 | 7 | 0 | wallstreetbets 8 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1y0eqrp/) |
| LULU | 2026-11-19 00:49 | mention spike | 3 | 2.0 | 2 | 0 | wallstreetbets 3 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xzqpcz/comment/19sunp5qplqdh/) |
| CRWD | 2026-11-19 03:02 | mention spike | 5 | 5.14 | 5 | 0 | wallstreetbets 5 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xzqpcz/comment/19sul3jt0chxh/) |
| SPCX | 2026-11-19 00:49 | mention spike | 35 | 53.29 | 33 | 0 | wallstreetbets 35 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1y0asod/) |
| MU | 2026-11-19 01:56 | mention spike | 4 | 5.14 | 4 | 0 | wallstreetbets 4 | Nasdaq | #19 | [link](https://www.reddit.com/r/wallstreetbets/comments/1y06n5x/comment/19svpev5rf7yb/) |
| GLD | 2026-11-19 00:42 | mention spike | 0 |  | 0 | 0 |  | NYSE Arca | #20 |  |
| AAOI | 2026-11-17 23:46 | mention spike | 1 | 5.29 | 1 | 0 | wallstreetbets 1 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1y0eg3e/) |

Full history: `episodes.csv` (one row per first flag, with the numbers known at that moment).
