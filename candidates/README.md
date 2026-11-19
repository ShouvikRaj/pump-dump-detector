# Stage 1 candidates

Updated 2026-11-19T03:12:10Z by run `44449477547`. A candidate is a ticker whose Reddit mentions (or hype-language
posts) in the last 24 hours jumped above its prior 7-day mean + 2 sd, with at least
10 mentions from 5 different authors. It stays listed until it goes
24 hours without a new flag. These are statistical flags, not accusations or advice.

| Ticker | Flagged since (UTC) | Why | Mentions 24h | Baseline/day | Authors | Hype posts | Subreddits | Exchange | StockTwits | Example |
|---|---|---|---|---|---|---|---|---|---|---|
| AMZN | 2026-11-19 00:49 | mention spike | 41 | 16.29 | 27 | 0 | wallstreetbets 41 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xzw3vl/) |
| ANT | 2026-11-19 00:42 | hype spike mention spike | 478 | 106.71 | 290 | 5 | wallstreetbets 478 | ? |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xzw3mg/) |
| CRWD | 2026-11-19 03:02 | mention spike | 13 | 4.0 | 12 | 0 | wallstreetbets 13 | Nasdaq | #7 | [link](https://www.reddit.com/r/wallstreetbets/comments/1xzqpcz/comment/19sul3jt0chxh/) |
| LULU | 2026-11-19 00:49 | mention spike | 12 | 0.86 | 6 | 0 | wallstreetbets 12 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xzqpcz/comment/19sunp5qplqdh/) |
| PANW | 2026-11-18 21:40 | mention spike | 42 | 2.86 | 32 | 1 | wallstreetbets 42 | Nasdaq | #5 | [link](https://www.reddit.com/r/wallstreetbets/comments/1xzqpcz/comment/19sul3jt0chxh/) |
| TTWO | 2026-11-19 00:42 | mention spike | 51 | 12.29 | 37 | 0 | wallstreetbets 51 | Nasdaq | #1 | [link](https://www.reddit.com/r/wallstreetbets/comments/1xzjf89/) |
| UNH | 2026-11-18 17:15 | mention spike | 22 | 2.0 | 12 | 0 | wallstreetbets 22 | NYSE | #3 | [link](https://www.reddit.com/r/wallstreetbets/comments/1xzqpcz/comment/19sucb46iczpd/) |
| SPCX | 2026-11-19 00:49 | mention spike | 73 | 49.29 | 66 | 0 | wallstreetbets 73 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xzw3vl/) |
| MU | 2026-11-19 01:56 | mention spike | 11 | 4.86 | 8 | 0 | wallstreetbets 11 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xzqpcz/comment/19suaaqqtlmf5/) |
| GLD | 2026-11-19 00:42 | mention spike | 16 | 9.71 | 7 | 0 | wallstreetbets 16 | NYSE Arca | #17 | [link](https://www.reddit.com/r/wallstreetbets/comments/1xzcf9l/comment/19stwce75w6kh/) |
| AAOI | 2026-11-17 23:46 | mention spike | 5 | 4.86 | 5 | 0 | wallstreetbets 5 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xzcf9l/comment/19stwasgs4n5v/) |
| SLS | 2026-11-17 12:33 | mention spike | 25 | 64.43 | 21 | 0 | wallstreetbets 22, pennystocks 2, smallstreetbets 1 | Nasdaq | #6 | [link](https://www.reddit.com/r/wallstreetbets/comments/1xzpncg/) |
| SOXX | 2026-11-17 18:16 | mention spike | 9 | 7.43 | 7 | 0 | wallstreetbets 9 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xzqpcz/comment/19sua1eyxyrph/) |
| HSBC | 2026-11-17 21:20 | mention spike | 2 | 3.86 | 2 | 0 | wallstreetbets 2 | NYSE |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xyotpf/comment/19stet972kuyt/) |
| SHAZ | 2026-11-17 10:45 | mention spike | 0 |  | 0 | 0 |  | Nasdaq |  |  |

Full history: `episodes.csv` (one row per first flag, with the numbers known at that moment).
