# Stage 1 candidates

Updated 2026-10-24T19:01:11Z by run `40122895881`. A candidate is a ticker whose Reddit mentions (or hype-language
posts) in the last 24 hours jumped above its prior 7-day mean + 2 sd, with at least
10 mentions from 5 different authors. It stays listed until it goes
24 hours without a new flag. These are statistical flags, not accusations or advice.

| Ticker | Flagged since (UTC) | Why | Mentions 24h | Baseline/day | Authors | Hype posts | Subreddits | Exchange | StockTwits | Example |
|---|---|---|---|---|---|---|---|---|---|---|
| USO | 2026-10-23 16:35 | mention spike | 19 | 17.43 | 17 | 0 | wallstreetbets 19 | NYSE Arca |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xdof8h/comment/19rldexwyjpr5/) |
| CRDO | 2026-10-23 12:23 | mention spike | 2 | 5.29 | 2 | 0 | wallstreetbets 2 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xdof8h/comment/19rkv8jmr8qhv/) |
| MSFT | 2026-10-23 06:51 | mention spike | 22 | 23.57 | 17 | 1 | wallstreetbets 21, pennystocks 1 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xe985s/) |
| CRWD | 2026-10-23 20:37 | mention spike | 5 | 4.29 | 5 | 0 | wallstreetbets 5 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xdof8h/comment/19rjwkjkz934y/) |
| LUNR | 2026-10-23 18:21 | mention spike | 3 | 2.86 | 3 | 0 | wallstreetbets 3 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xdof8h/comment/19rkcp2vo5u05/) |
| NVDA | 2026-10-23 02:14 | mention spike | 27 | 64.14 | 22 | 0 | wallstreetbets 24, pennystocks 3 | Nasdaq |  | [link](https://www.reddit.com/r/pennystocks/comments/1xakpd0/comment/19rl85dava0hw/) |
| RDDT | 2026-10-23 20:37 | mention spike | 13 | 12.14 | 10 | 0 | wallstreetbets 13 | NYSE |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xe985s/) |
| ASTS | 2026-10-23 13:45 | mention spike | 17 | 37.71 | 15 | 0 | wallstreetbets 17 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xe9fc7/comment/19rlcpyrpl3y8/) |
| SCHD | 2026-10-22 21:05 | mention spike | 0 |  | 0 | 0 |  | NYSE Arca |  |  |
| INTC | 2026-10-22 21:18 | mention spike | 7 | 11.43 | 6 | 0 | wallstreetbets 7 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xe6k9o/) |
| WDC | 2026-10-22 14:55 | mention spike | 9 | 38.86 | 9 | 0 | wallstreetbets 8, smallstreetbets 1 | Nasdaq |  | [link](https://www.reddit.com/r/smallstreetbets/comments/1xdogpu/comment/19rlcrzloi084/) |
| BE | 2026-10-23 15:42 | mention spike | 0 |  | 0 | 0 |  | NYSE |  |  |
| AAPL | 2026-10-23 00:03 | mention spike | 10 | 28.43 | 9 | 0 | wallstreetbets 10 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xe41cr/) |
| LULU | 2026-10-22 20:12 | mention spike | 0 |  | 0 | 0 |  | Nasdaq |  |  |
| SOXL | 2026-10-22 15:59 | mention spike | 13 | 55.29 | 12 | 0 | wallstreetbets 13 | NYSE Arca |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xdof8h/comment/19rlgk9uosy05/) |
| FPS | 2026-10-22 16:39 | mention spike | 0 |  | 0 | 0 |  | NYSE |  |  |

Full history: `episodes.csv` (one row per first flag, with the numbers known at that moment).
