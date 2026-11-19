# Stage 1 candidates

Updated 2026-11-19T00:42:59Z by run `44429572970`. A candidate is a ticker whose Reddit mentions (or hype-language
posts) in the last 24 hours jumped above its prior 7-day mean + 2 sd, with at least
10 mentions from 5 different authors. It stays listed until it goes
24 hours without a new flag. These are statistical flags, not accusations or advice.

| Ticker | Flagged since (UTC) | Why | Mentions 24h | Baseline/day | Authors | Hype posts | Subreddits | Exchange | StockTwits | Example |
|---|---|---|---|---|---|---|---|---|---|---|
| PANW | 2026-11-18 21:40 | mention spike | 29 | 2.86 | 22 | 0 | wallstreetbets 29 | Nasdaq | #2 | [link](https://www.reddit.com/r/wallstreetbets/comments/1xzqpcz/comment/19sueijzmvk5g/) |
| UNH | 2026-11-18 17:15 | mention spike | 20 | 2.14 | 10 | 0 | wallstreetbets 20 | NYSE | #7 | [link](https://www.reddit.com/r/wallstreetbets/comments/1xzqpcz/comment/19su8gt7rh1ok/) |
| ANT | 2026-11-19 00:42 | hype spike mention spike | 353 | 104.43 | 223 | 5 | wallstreetbets 353 | ? |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xzua1i/) |
| GLD | 2026-11-19 00:42 | mention spike | 23 | 8.71 | 14 | 0 | wallstreetbets 23 | NYSE Arca | #5 | [link](https://www.reddit.com/r/wallstreetbets/comments/1xzcf9l/comment/19stwce75w6kh/) |
| TTWO | 2026-11-19 00:42 | mention spike | 46 | 12.43 | 34 | 0 | wallstreetbets 46 | Nasdaq | #1 | [link](https://www.reddit.com/r/wallstreetbets/comments/1xzjf89/) |
| AAOI | 2026-11-17 23:46 | mention spike | 6 | 4.71 | 6 | 0 | wallstreetbets 6 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xzcf9l/comment/19stwasgs4n5v/) |
| SLS | 2026-11-17 12:33 | mention spike | 28 | 63.71 | 24 | 0 | wallstreetbets 22, pennystocks 3, smallstreetbets 3 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xzpncg/) |
| SOXX | 2026-11-17 18:16 | mention spike | 10 | 7.14 | 8 | 0 | wallstreetbets 10 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xzqpcz/comment/19su91fc87qh1/) |
| HSBC | 2026-11-17 21:20 | mention spike | 2 | 3.86 | 2 | 0 | wallstreetbets 2 | NYSE |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xyotpf/comment/19stet972kuyt/) |
| SHAZ | 2026-11-17 10:45 | mention spike | 0 |  | 0 | 0 |  | Nasdaq |  |  |

Full history: `episodes.csv` (one row per first flag, with the numbers known at that moment).
