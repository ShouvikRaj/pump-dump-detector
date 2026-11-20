# Stage 1 candidates

Updated 2026-11-20T00:30:08Z by run `44645725841`. A candidate is a ticker whose Reddit mentions (or hype-language
posts) in the last 24 hours jumped above its prior 7-day mean + 2 sd, with at least
10 mentions from 5 different authors. It stays listed until it goes
24 hours without a new flag. These are statistical flags, not accusations or advice.

| Ticker | Flagged since (UTC) | Why | Mentions 24h | Baseline/day | Authors | Hype posts | Subreddits | Exchange | StockTwits | Example |
|---|---|---|---|---|---|---|---|---|---|---|
| ANT | 2026-11-19 00:42 | hype spike mention spike | 605 | 153.57 | 410 | 2 | wallstreetbets 604, pennystocks 1 | ? | #1 | [link](https://www.reddit.com/r/wallstreetbets/comments/1y0o3li/) |
| PANW | 2026-11-18 21:40 | mention spike | 1 | 8.71 | 1 | 0 | wallstreetbets 1 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xzqpcz/comment/19sul3jt0chxh/) |
| UNH | 2026-11-18 17:15 | mention spike | 7 | 5.0 | 7 | 0 | wallstreetbets 7 | NYSE |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1y0em9g/) |
| AMZN | 2026-11-19 00:49 | mention spike | 16 | 17.57 | 14 | 0 | wallstreetbets 16 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xzw3vl/) |
| TTWO | 2026-11-19 00:42 | mention spike | 7 | 15.86 | 6 | 0 | wallstreetbets 7 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1y0eqrp/) |
| LULU | 2026-11-19 00:49 | mention spike | 1 | 2.29 | 1 | 0 | wallstreetbets 1 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xzqpcz/comment/19sunp5qplqdh/) |
| CRWD | 2026-11-19 03:02 | mention spike | 1 | 5.71 | 1 | 0 | wallstreetbets 1 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xzqpcz/comment/19sul3jt0chxh/) |
| SPCX | 2026-11-19 00:49 | mention spike | 30 | 52.57 | 28 | 0 | wallstreetbets 30 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1y0lkw0/) |
| MU | 2026-11-19 01:56 | mention spike | 3 | 5.29 | 3 | 0 | wallstreetbets 3 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1y06n5x/comment/19svpev5rf7yb/) |
| GLD | 2026-11-19 00:42 | mention spike | 1 | 10.57 | 1 | 0 | wallstreetbets 1 | NYSE Arca | #2 | [link](https://www.reddit.com/r/wallstreetbets/comments/1y0kpw2/comment/19sw6nzb7jejo/) |

Full history: `episodes.csv` (one row per first flag, with the numbers known at that moment).
