# Stage 1 candidates

Updated 2026-11-19T16:42:10Z by run `44568678139`. A candidate is a ticker whose Reddit mentions (or hype-language
posts) in the last 24 hours jumped above its prior 7-day mean + 2 sd, with at least
10 mentions from 5 different authors. It stays listed until it goes
24 hours without a new flag. These are statistical flags, not accusations or advice.

| Ticker | Flagged since (UTC) | Why | Mentions 24h | Baseline/day | Authors | Hype posts | Subreddits | Exchange | StockTwits | Example |
|---|---|---|---|---|---|---|---|---|---|---|
| ANT | 2026-11-19 00:42 | hype spike mention spike | 397 | 132.14 | 278 | 0 | wallstreetbets 397 | ? | #2 | [link](https://www.reddit.com/r/wallstreetbets/comments/1y0cds6/) |
| PANW | 2026-11-18 21:40 | mention spike | 36 | 3.71 | 29 | 1 | wallstreetbets 36 | Nasdaq | #15 | [link](https://www.reddit.com/r/wallstreetbets/comments/1xzqpcz/comment/19sul3jt0chxh/) |
| UNH | 2026-11-18 17:15 | mention spike | 11 | 3.43 | 8 | 0 | wallstreetbets 11 | NYSE | #3 | [link](https://www.reddit.com/r/wallstreetbets/comments/1xzqpcz/comment/19sucb46iczpd/) |
| AMZN | 2026-11-19 00:49 | mention spike | 25 | 17.86 | 21 | 0 | wallstreetbets 25 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xzw3vl/) |
| TTWO | 2026-11-19 00:42 | mention spike | 8 | 16.43 | 7 | 0 | wallstreetbets 8 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1y06n5x/comment/19svfs5wc8kci/) |
| LULU | 2026-11-19 00:49 | mention spike | 4 | 1.86 | 3 | 0 | wallstreetbets 4 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xzqpcz/comment/19sunp5qplqdh/) |
| CRWD | 2026-11-19 03:02 | mention spike | 9 | 4.57 | 8 | 0 | wallstreetbets 9 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xzqpcz/comment/19sul3jt0chxh/) |
| SPCX | 2026-11-19 00:49 | mention spike | 34 | 53.29 | 33 | 0 | wallstreetbets 34 | Nasdaq | #18 | [link](https://www.reddit.com/r/wallstreetbets/comments/1y0asod/) |
| MU | 2026-11-19 01:56 | mention spike | 3 | 5.43 | 2 | 0 | wallstreetbets 3 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xzqpcz/comment/19suaaqqtlmf5/) |
| GLD | 2026-11-19 00:42 | mention spike | 0 |  | 0 | 0 |  | NYSE Arca | #16 |  |
| AAOI | 2026-11-17 23:46 | mention spike | 0 |  | 0 | 0 |  | Nasdaq |  |  |

Full history: `episodes.csv` (one row per first flag, with the numbers known at that moment).
