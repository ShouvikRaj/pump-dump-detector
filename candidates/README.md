# Stage 1 candidates

Updated 2026-11-19T11:50:08Z by run `44517978679`. A candidate is a ticker whose Reddit mentions (or hype-language
posts) in the last 24 hours jumped above its prior 7-day mean + 2 sd, with at least
10 mentions from 5 different authors. It stays listed until it goes
24 hours without a new flag. These are statistical flags, not accusations or advice.

| Ticker | Flagged since (UTC) | Why | Mentions 24h | Baseline/day | Authors | Hype posts | Subreddits | Exchange | StockTwits | Example |
|---|---|---|---|---|---|---|---|---|---|---|
| AMZN | 2026-11-19 00:49 | mention spike | 36 | 17.29 | 26 | 0 | wallstreetbets 36 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xzw3vl/) |
| ANT | 2026-11-19 00:42 | hype spike mention spike | 435 | 116.14 | 288 | 2 | wallstreetbets 435 | ? |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1y06x9o/) |
| PANW | 2026-11-18 21:40 | mention spike | 42 | 2.86 | 32 | 1 | wallstreetbets 42 | Nasdaq | #6 | [link](https://www.reddit.com/r/wallstreetbets/comments/1xzqpcz/comment/19sul3jt0chxh/) |
| TTWO | 2026-11-19 00:42 | mention spike | 40 | 12.86 | 28 | 0 | wallstreetbets 40 | Nasdaq | #5 | [link](https://www.reddit.com/r/wallstreetbets/comments/1xzjf89/) |
| UNH | 2026-11-18 17:15 | mention spike | 22 | 1.86 | 12 | 0 | wallstreetbets 22 | NYSE |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xzqpcz/comment/19sucb46iczpd/) |
| LULU | 2026-11-19 00:49 | mention spike | 10 | 1.14 | 4 | 0 | wallstreetbets 10 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xzqpcz/comment/19sunp5qplqdh/) |
| CRWD | 2026-11-19 03:02 | mention spike | 12 | 4.14 | 11 | 0 | wallstreetbets 12 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xzqpcz/comment/19sul3jt0chxh/) |
| SPCX | 2026-11-19 00:49 | mention spike | 61 | 50.14 | 55 | 0 | wallstreetbets 61 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xzw3vl/) |
| MU | 2026-11-19 01:56 | mention spike | 9 | 5.14 | 7 | 0 | wallstreetbets 9 | Nasdaq | #7 | [link](https://www.reddit.com/r/wallstreetbets/comments/1xzqpcz/comment/19suaaqqtlmf5/) |
| GLD | 2026-11-19 00:42 | mention spike | 11 | 9.86 | 2 | 0 | wallstreetbets 11 | NYSE Arca | #11 | [link](https://www.reddit.com/r/wallstreetbets/comments/1xzcf9l/comment/19stwce75w6kh/) |
| AAOI | 2026-11-17 23:46 | mention spike | 3 | 5.14 | 3 | 0 | wallstreetbets 3 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xzcf9l/comment/19stwasgs4n5v/) |
| SLS | 2026-11-17 12:33 | mention spike | 16 | 66.14 | 14 | 0 | wallstreetbets 13, pennystocks 3 | Nasdaq | #1 | [link](https://www.reddit.com/r/wallstreetbets/comments/1xzpncg/) |

Full history: `episodes.csv` (one row per first flag, with the numbers known at that moment).
