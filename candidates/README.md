# Stage 1 candidates

Updated 2026-11-19T14:59:10Z by run `44548680443`. A candidate is a ticker whose Reddit mentions (or hype-language
posts) in the last 24 hours jumped above its prior 7-day mean + 2 sd, with at least
10 mentions from 5 different authors. It stays listed until it goes
24 hours without a new flag. These are statistical flags, not accusations or advice.

| Ticker | Flagged since (UTC) | Why | Mentions 24h | Baseline/day | Authors | Hype posts | Subreddits | Exchange | StockTwits | Example |
|---|---|---|---|---|---|---|---|---|---|---|
| AMZN | 2026-11-19 00:49 | mention spike | 32 | 17.86 | 26 | 0 | wallstreetbets 32 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xzw3vl/) |
| ANT | 2026-11-19 00:42 | hype spike mention spike | 451 | 126.0 | 308 | 1 | wallstreetbets 451 | ? |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1y0avst/) |
| PANW | 2026-11-18 21:40 | mention spike | 42 | 2.86 | 32 | 1 | wallstreetbets 42 | Nasdaq | #4 | [link](https://www.reddit.com/r/wallstreetbets/comments/1xzqpcz/comment/19sul3jt0chxh/) |
| UNH | 2026-11-18 17:15 | mention spike | 22 | 1.86 | 12 | 0 | wallstreetbets 22 | NYSE | #25 | [link](https://www.reddit.com/r/wallstreetbets/comments/1xzqpcz/comment/19sucb46iczpd/) |
| TTWO | 2026-11-19 00:42 | mention spike | 20 | 15.29 | 14 | 0 | wallstreetbets 20 | Nasdaq | #1 | [link](https://www.reddit.com/r/wallstreetbets/comments/1xzjf89/) |
| LULU | 2026-11-19 00:49 | mention spike | 10 | 1.14 | 4 | 0 | wallstreetbets 10 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xzqpcz/comment/19sunp5qplqdh/) |
| CRWD | 2026-11-19 03:02 | mention spike | 10 | 4.43 | 9 | 0 | wallstreetbets 10 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xzqpcz/comment/19sul3jt0chxh/) |
| SPCX | 2026-11-19 00:49 | mention spike | 56 | 50.29 | 53 | 0 | wallstreetbets 56 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1y0asod/) |
| MU | 2026-11-19 01:56 | mention spike | 9 | 5.0 | 7 | 0 | wallstreetbets 9 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xzqpcz/comment/19suaaqqtlmf5/) |
| GLD | 2026-11-19 00:42 | mention spike | 10 | 10.0 | 1 | 0 | wallstreetbets 10 | NYSE Arca |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xzcf9l/comment/19stwce75w6kh/) |
| AAOI | 2026-11-17 23:46 | mention spike | 1 | 5.43 | 1 | 0 | wallstreetbets 1 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xzcf9l/comment/19stwasgs4n5v/) |

Full history: `episodes.csv` (one row per first flag, with the numbers known at that moment).
