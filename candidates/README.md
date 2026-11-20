# Stage 1 candidates

Updated 2026-11-20T01:12:01Z by run `44650925909`. A candidate is a ticker whose Reddit mentions (or hype-language
posts) in the last 24 hours jumped above its prior 7-day mean + 2 sd, with at least
10 mentions from 5 different authors. It stays listed until it goes
24 hours without a new flag. These are statistical flags, not accusations or advice.

| Ticker | Flagged since (UTC) | Why | Mentions 24h | Baseline/day | Authors | Hype posts | Subreddits | Exchange | StockTwits | Example |
|---|---|---|---|---|---|---|---|---|---|---|
| ANT | 2026-11-19 00:42 | hype spike mention spike | 1191 | 189.57 | 723 | 3 | wallstreetbets 1186, pennystocks 3, smallstreetbets 2 | ? | #1 | [link](https://www.reddit.com/r/wallstreetbets/comments/1y0o3li/) |
| GME | 2026-11-20 00:51 | mention spike | 35 | 16.14 | 32 | 0 | wallstreetbets 32, pennystocks 2, smallstreetbets 1 | NYSE | #4 | [link](https://www.reddit.com/r/wallstreetbets/comments/1y0lyra/) |
| OPEX | 2026-11-20 00:51 | mention spike | 11 | 1.14 | 9 | 0 | wallstreetbets 11 | Cboe BZX |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1y0kpw2/comment/19sw70xog2e03/) |
| PANW | 2026-11-18 21:40 | mention spike | 5 | 11.57 | 5 | 0 | wallstreetbets 5 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1y0kpw2/comment/19sw23u1ms8dc/) |
| UNH | 2026-11-18 17:15 | mention spike | 19 | 9.29 | 16 | 0 | wallstreetbets 19 | NYSE |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1y0em9g/) |
| AMZN | 2026-11-19 00:49 | mention spike | 36 | 22.57 | 29 | 0 | wallstreetbets 36 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1y0kyvz/comment/19sw3102ah6e8/) |
| TTWO | 2026-11-19 00:42 | mention spike | 24 | 16.43 | 22 | 0 | wallstreetbets 24 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1y0eqrp/) |
| LULU | 2026-11-19 00:49 | mention spike | 4 | 2.86 | 3 | 0 | wallstreetbets 4 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xzpta7/comment/19svv61ikre0y/) |
| CRWD | 2026-11-19 03:02 | mention spike | 3 | 6.57 | 3 | 0 | wallstreetbets 3 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xzzr8r/comment/19svdb6gvk9ad/) |
| SPCX | 2026-11-19 00:49 | mention spike | 75 | 56.29 | 68 | 0 | wallstreetbets 74, pennystocks 1 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1y0lkw0/) |
| MU | 2026-11-19 01:56 | mention spike | 4 | 5.57 | 4 | 0 | wallstreetbets 4 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1y06n5x/comment/19svpev5rf7yb/) |

Full history: `episodes.csv` (one row per first flag, with the numbers known at that moment).
