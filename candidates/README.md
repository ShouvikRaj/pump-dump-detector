# Stage 1 candidates

Updated 2026-11-19T13:36:11Z by run `44534710841`. A candidate is a ticker whose Reddit mentions (or hype-language
posts) in the last 24 hours jumped above its prior 7-day mean + 2 sd, with at least
10 mentions from 5 different authors. It stays listed until it goes
24 hours without a new flag. These are statistical flags, not accusations or advice.

| Ticker | Flagged since (UTC) | Why | Mentions 24h | Baseline/day | Authors | Hype posts | Subreddits | Exchange | StockTwits | Example |
|---|---|---|---|---|---|---|---|---|---|---|
| AMZN | 2026-11-19 00:49 | mention spike | 38 | 17.43 | 28 | 0 | wallstreetbets 38 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xzw3vl/) |
| ANT | 2026-11-19 00:42 | hype spike mention spike | 494 | 119.57 | 329 | 1 | wallstreetbets 494 | ? |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1y08zhi/) |
| PANW | 2026-11-18 21:40 | mention spike | 42 | 2.86 | 32 | 1 | wallstreetbets 42 | Nasdaq | #4 | [link](https://www.reddit.com/r/wallstreetbets/comments/1xzqpcz/comment/19sul3jt0chxh/) |
| UNH | 2026-11-18 17:15 | mention spike | 22 | 1.86 | 12 | 0 | wallstreetbets 22 | NYSE | #17 | [link](https://www.reddit.com/r/wallstreetbets/comments/1xzqpcz/comment/19sucb46iczpd/) |
| TTWO | 2026-11-19 00:42 | mention spike | 31 | 14.29 | 25 | 0 | wallstreetbets 31 | Nasdaq | #3 | [link](https://www.reddit.com/r/wallstreetbets/comments/1xzjf89/) |
| LULU | 2026-11-19 00:49 | mention spike | 10 | 1.14 | 4 | 0 | wallstreetbets 10 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xzqpcz/comment/19sunp5qplqdh/) |
| CRWD | 2026-11-19 03:02 | mention spike | 11 | 4.29 | 10 | 0 | wallstreetbets 11 | Nasdaq | #20 | [link](https://www.reddit.com/r/wallstreetbets/comments/1xzqpcz/comment/19sul3jt0chxh/) |
| SPCX | 2026-11-19 00:49 | mention spike | 59 | 50.43 | 55 | 0 | wallstreetbets 59 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xzw3vl/) |
| MU | 2026-11-19 01:56 | mention spike | 9 | 5.0 | 7 | 0 | wallstreetbets 9 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xzqpcz/comment/19suaaqqtlmf5/) |
| GLD | 2026-11-19 00:42 | mention spike | 10 | 10.0 | 1 | 0 | wallstreetbets 10 | NYSE Arca |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xzcf9l/comment/19stwce75w6kh/) |
| AAOI | 2026-11-17 23:46 | mention spike | 3 | 5.14 | 3 | 0 | wallstreetbets 3 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xzcf9l/comment/19stwasgs4n5v/) |
| SLS | 2026-11-17 12:33 | mention spike | 14 | 66.86 | 14 | 0 | wallstreetbets 11, pennystocks 3 | Nasdaq | #27 | [link](https://www.reddit.com/r/wallstreetbets/comments/1xzpncg/) |

Full history: `episodes.csv` (one row per first flag, with the numbers known at that moment).
