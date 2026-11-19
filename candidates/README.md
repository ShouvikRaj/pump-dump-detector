# Stage 1 candidates

Updated 2026-11-19T08:47:08Z by run `44489782336`. A candidate is a ticker whose Reddit mentions (or hype-language
posts) in the last 24 hours jumped above its prior 7-day mean + 2 sd, with at least
10 mentions from 5 different authors. It stays listed until it goes
24 hours without a new flag. These are statistical flags, not accusations or advice.

| Ticker | Flagged since (UTC) | Why | Mentions 24h | Baseline/day | Authors | Hype posts | Subreddits | Exchange | StockTwits | Example |
|---|---|---|---|---|---|---|---|---|---|---|
| AMZN | 2026-11-19 00:49 | mention spike | 38 | 16.86 | 25 | 0 | wallstreetbets 38 | Nasdaq | #7 | [link](https://www.reddit.com/r/wallstreetbets/comments/1xzw3vl/) |
| ANT | 2026-11-19 00:42 | hype spike mention spike | 429 | 112.43 | 274 | 5 | wallstreetbets 429 | ? |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1y02lrs/) |
| PANW | 2026-11-18 21:40 | mention spike | 42 | 2.86 | 32 | 1 | wallstreetbets 42 | Nasdaq | #5 | [link](https://www.reddit.com/r/wallstreetbets/comments/1xzqpcz/comment/19sul3jt0chxh/) |
| TTWO | 2026-11-19 00:42 | mention spike | 51 | 11.43 | 37 | 0 | wallstreetbets 51 | Nasdaq | #2 | [link](https://www.reddit.com/r/wallstreetbets/comments/1xzjf89/) |
| UNH | 2026-11-18 17:15 | mention spike | 22 | 2.0 | 12 | 0 | wallstreetbets 22 | NYSE | #10 | [link](https://www.reddit.com/r/wallstreetbets/comments/1xzqpcz/comment/19sucb46iczpd/) |
| LULU | 2026-11-19 00:49 | mention spike | 10 | 1.14 | 4 | 0 | wallstreetbets 10 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xzqpcz/comment/19sunp5qplqdh/) |
| CRWD | 2026-11-19 03:02 | mention spike | 12 | 4.14 | 11 | 0 | wallstreetbets 12 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xzqpcz/comment/19sul3jt0chxh/) |
| SPCX | 2026-11-19 00:49 | mention spike | 65 | 50.0 | 59 | 0 | wallstreetbets 65 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xzw3vl/) |
| MU | 2026-11-19 01:56 | mention spike | 9 | 5.14 | 7 | 0 | wallstreetbets 9 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xzqpcz/comment/19suaaqqtlmf5/) |
| GLD | 2026-11-19 00:42 | mention spike | 13 | 9.71 | 4 | 0 | wallstreetbets 13 | NYSE Arca |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xzcf9l/comment/19stwce75w6kh/) |
| AAOI | 2026-11-17 23:46 | mention spike | 4 | 5.0 | 4 | 0 | wallstreetbets 4 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xzcf9l/comment/19stwasgs4n5v/) |
| SLS | 2026-11-17 12:33 | mention spike | 16 | 65.86 | 13 | 0 | wallstreetbets 13, pennystocks 2, smallstreetbets 1 | Nasdaq | #1 | [link](https://www.reddit.com/r/wallstreetbets/comments/1xzpncg/) |
| SOXX | 2026-11-17 18:16 | mention spike | 6 | 7.71 | 5 | 0 | wallstreetbets 6 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xzqpcz/comment/19sua1eyxyrph/) |

Full history: `episodes.csv` (one row per first flag, with the numbers known at that moment).
