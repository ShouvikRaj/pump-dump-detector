# Stage 1 candidates

Updated 2026-11-20T02:53:08Z by run `44663666143`. A candidate is a ticker whose Reddit mentions (or hype-language
posts) in the last 24 hours jumped above its prior 7-day mean + 2 sd, with at least
10 mentions from 5 different authors. It stays listed until it goes
24 hours without a new flag. These are statistical flags, not accusations or advice.

| Ticker | Flagged since (UTC) | Why | Mentions 24h | Baseline/day | Authors | Hype posts | Subreddits | Exchange | StockTwits | Example |
|---|---|---|---|---|---|---|---|---|---|---|
| ANT | 2026-11-19 00:42 | hype spike mention spike | 1104 | 201.86 | 690 | 3 | wallstreetbets 1099, pennystocks 3, smallstreetbets 2 | ? | #1 | [link](https://www.reddit.com/r/wallstreetbets/comments/1y0sab3/) |
| GME | 2026-11-20 00:51 | mention spike | 37 | 16.14 | 34 | 0 | wallstreetbets 33, pennystocks 2, smallstreetbets 2 | NYSE | #6 | [link](https://www.reddit.com/r/wallstreetbets/comments/1y0qtxp/) |
| OPEX | 2026-11-20 00:51 | mention spike | 11 | 1.14 | 9 | 0 | wallstreetbets 11 | Cboe BZX |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1y0kpw2/comment/19sw70xog2e03/) |
| PANW | 2026-11-18 21:40 | mention spike | 3 | 11.86 | 3 | 0 | wallstreetbets 3 | Nasdaq | #28 | [link](https://www.reddit.com/r/wallstreetbets/comments/1y0kpw2/comment/19sw23u1ms8dc/) |
| UNH | 2026-11-18 17:15 | mention spike | 19 | 9.29 | 16 | 0 | wallstreetbets 19 | NYSE |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1y0em9g/) |
| AMZN | 2026-11-19 00:49 | mention spike | 32 | 23.0 | 26 | 0 | wallstreetbets 32 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1y0kyvz/comment/19sw3102ah6e8/) |
| TTWO | 2026-11-19 00:42 | mention spike | 20 | 17.0 | 20 | 0 | wallstreetbets 20 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1y0eqrp/) |
| LULU | 2026-11-19 00:49 | mention spike | 3 | 3.0 | 3 | 0 | wallstreetbets 3 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xzpta7/comment/19svv61ikre0y/) |
| CRWD | 2026-11-19 03:02 | mention spike | 2 | 6.71 | 2 | 0 | wallstreetbets 2 | Nasdaq | #27 | [link](https://www.reddit.com/r/wallstreetbets/comments/1xzzr8r/comment/19svdb6gvk9ad/) |

Full history: `episodes.csv` (one row per first flag, with the numbers known at that moment).
