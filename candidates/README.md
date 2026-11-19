# Stage 1 candidates

Updated 2026-11-19T01:40:31Z by run `44438245133`. A candidate is a ticker whose Reddit mentions (or hype-language
posts) in the last 24 hours jumped above its prior 7-day mean + 2 sd, with at least
10 mentions from 5 different authors. It stays listed until it goes
24 hours without a new flag. These are statistical flags, not accusations or advice.

| Ticker | Flagged since (UTC) | Why | Mentions 24h | Baseline/day | Authors | Hype posts | Subreddits | Exchange | StockTwits | Example |
|---|---|---|---|---|---|---|---|---|---|---|
| AMZN | 2026-11-19 00:49 | mention spike | 38 | 16.57 | 25 | 0 | wallstreetbets 38 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xzw3vl/) |
| ANT | 2026-11-19 00:42 | hype spike mention spike | 428 | 105.71 | 266 | 5 | wallstreetbets 428 | ? |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xzw3mg/) |
| LULU | 2026-11-19 00:49 | mention spike | 11 | 0.86 | 6 | 0 | wallstreetbets 11 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xzqpcz/comment/19su9qql77mpv/) |
| PANW | 2026-11-18 21:40 | mention spike | 41 | 2.86 | 31 | 1 | wallstreetbets 41 | Nasdaq | #2 | [link](https://www.reddit.com/r/wallstreetbets/comments/1xzqpcz/comment/19sueijzmvk5g/) |
| TTWO | 2026-11-19 00:42 | mention spike | 47 | 12.29 | 35 | 0 | wallstreetbets 47 | Nasdaq | #1 | [link](https://www.reddit.com/r/wallstreetbets/comments/1xzjf89/) |
| UNH | 2026-11-18 17:15 | mention spike | 22 | 2.14 | 12 | 0 | wallstreetbets 22 | NYSE | #6 | [link](https://www.reddit.com/r/wallstreetbets/comments/1xzqpcz/comment/19sucb46iczpd/) |
| GLD | 2026-11-19 00:42 | mention spike | 20 | 9.14 | 11 | 0 | wallstreetbets 20 | NYSE Arca | #4 | [link](https://www.reddit.com/r/wallstreetbets/comments/1xzcf9l/comment/19stwce75w6kh/) |
| SPCX | 2026-11-19 00:49 | mention spike | 72 | 48.71 | 65 | 0 | wallstreetbets 72 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xzw3vl/) |
| AAOI | 2026-11-17 23:46 | mention spike | 6 | 4.71 | 6 | 0 | wallstreetbets 6 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xzcf9l/comment/19stwasgs4n5v/) |
| SLS | 2026-11-17 12:33 | mention spike | 28 | 64.0 | 24 | 0 | wallstreetbets 23, pennystocks 3, smallstreetbets 2 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xzpncg/) |
| SOXX | 2026-11-17 18:16 | mention spike | 9 | 7.43 | 7 | 0 | wallstreetbets 9 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xzqpcz/comment/19sua1eyxyrph/) |
| HSBC | 2026-11-17 21:20 | mention spike | 2 | 3.86 | 2 | 0 | wallstreetbets 2 | NYSE |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xyotpf/comment/19stet972kuyt/) |
| SHAZ | 2026-11-17 10:45 | mention spike | 0 |  | 0 | 0 |  | Nasdaq |  |  |

Full history: `episodes.csv` (one row per first flag, with the numbers known at that moment).
