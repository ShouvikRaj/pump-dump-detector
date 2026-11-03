# Stage 1 candidates

Updated 2026-11-03T14:16:09Z by run `41650837384`. A candidate is a ticker whose Reddit mentions (or hype-language
posts) in the last 24 hours jumped above its prior 7-day mean + 2 sd, with at least
10 mentions from 5 different authors. It stays listed until it goes
24 hours without a new flag. These are statistical flags, not accusations or advice.

| Ticker | Flagged since (UTC) | Why | Mentions 24h | Baseline/day | Authors | Hype posts | Subreddits | Exchange | StockTwits | Example |
|---|---|---|---|---|---|---|---|---|---|---|
| AAPL | 2026-11-02 20:10 | mention spike | 431 | 57.43 | 218 | 1 | wallstreetbets 428, smallstreetbets 3 | Nasdaq | #14 | [link](https://www.reddit.com/r/wallstreetbets/comments/1xmol2r/) |
| AMD | 2026-11-02 21:58 | mention spike | 273 | 59.0 | 200 | 1 | wallstreetbets 272, smallstreetbets 1 | Nasdaq | #10 | [link](https://www.reddit.com/r/wallstreetbets/comments/1xmqlo9/) |
| ASTS | 2026-11-02 21:45 | mention spike | 50 | 17.57 | 39 | 0 | wallstreetbets 50 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xmrw7a/comment/19s2v560aemte/) |
| IREN | 2026-11-03 08:03 | mention spike | 23 | 10.14 | 21 | 0 | wallstreetbets 23 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xm2b50/) |
| MRVL | 2026-11-02 21:05 | mention spike | 90 | 22.57 | 62 | 0 | wallstreetbets 87, smallstreetbets 3 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xmp5rp/) |
| MSOS | 2026-10-31 21:03 | mention spike | 36 | 3.71 | 23 | 0 | wallstreetbets 36 | NYSE Arca |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xmq0vm/comment/19s2y0ox011sx/) |
| MU | 2026-11-02 19:43 | mention spike | 34 | 9.86 | 11 | 0 | wallstreetbets 34 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xmq0vm/comment/19s2uwzoh4ehx/) |
| PLTR | 2026-11-02 13:09 | mention spike | 237 | 18.0 | 147 | 1 | wallstreetbets 237 | Nasdaq | #9 | [link](https://www.reddit.com/r/wallstreetbets/comments/1xm7gzv/) |
| RKLB | 2026-11-02 15:08 | mention spike | 23 | 10.86 | 14 | 0 | wallstreetbets 23 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xmrw7a/comment/19s2v560aemte/) |
| SMCI | 2026-11-02 18:46 | mention spike | 23 | 5.29 | 21 | 0 | wallstreetbets 23 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xm5n1m/) |
| SOUN | 2026-11-02 17:39 | mention spike | 26 | 0.86 | 5 | 1 | wallstreetbets 26 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xlu7un/comment/19s1f33538jmq/) |
| WMT | 2026-11-02 20:10 | mention spike | 17 | 3.0 | 12 | 0 | wallstreetbets 17 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xmq0vm/comment/19s2xwvwha737/) |
| AAOI | 2026-11-03 00:57 | mention spike | 19 | 7.71 | 10 | 1 | wallstreetbets 19 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xmeu2h/) |
| APLD | 2026-11-03 07:23 | mention spike | 10 | 3.71 | 9 | 0 | wallstreetbets 10 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xm9hzx/comment/19s2fiuhp2zur/) |
| LITE | 2026-11-02 21:16 | mention spike | 80 | 19.29 | 58 | 0 | wallstreetbets 80 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xmeu2h/) |
| HTZ | 2026-11-02 21:29 | mention spike | 8 | 3.86 | 7 | 0 | wallstreetbets 5, pennystocks 3 | Nasdaq |  | [link](https://www.reddit.com/r/pennystocks/comments/1xmk38o/comment/19s2vnf8evkas/) |
| ATC | 2026-11-02 07:17 | mention spike | 0 |  | 0 | 0 |  | Nasdaq |  |  |
| NNN | 2026-11-01 19:38 | mention spike | 6 | 3.0 | 5 | 0 | wallstreetbets 6 | NYSE |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xm9hzx/comment/19s1yzfqqzpq9/) |

Full history: `episodes.csv` (one row per first flag, with the numbers known at that moment).
