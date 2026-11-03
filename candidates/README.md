# Stage 1 candidates

Updated 2026-11-03T16:55:10Z by run `41677929202`. A candidate is a ticker whose Reddit mentions (or hype-language
posts) in the last 24 hours jumped above its prior 7-day mean + 2 sd, with at least
10 mentions from 5 different authors. It stays listed until it goes
24 hours without a new flag. These are statistical flags, not accusations or advice.

| Ticker | Flagged since (UTC) | Why | Mentions 24h | Baseline/day | Authors | Hype posts | Subreddits | Exchange | StockTwits | Example |
|---|---|---|---|---|---|---|---|---|---|---|
| AAPL | 2026-11-02 20:10 | mention spike | 407 | 62.57 | 212 | 1 | wallstreetbets 406, smallstreetbets 1 | Nasdaq | #10 | [link](https://www.reddit.com/r/wallstreetbets/comments/1xmol2r/) |
| AEHR | 2026-11-03 15:08 | mention spike | 10 | 0.71 | 10 | 0 | wallstreetbets 10 | Nasdaq | #3 | [link](https://www.reddit.com/r/wallstreetbets/comments/1xjkxhl/comment/19s34i59ms2as/) |
| AMD | 2026-11-02 21:58 | mention spike | 318 | 63.71 | 234 | 1 | wallstreetbets 314, smallstreetbets 4 | Nasdaq |  | [link](https://www.reddit.com/r/smallstreetbets/comments/1xmw99c/) |
| ASTS | 2026-11-02 21:45 | mention spike | 47 | 17.71 | 38 | 0 | wallstreetbets 47 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xmq0vm/comment/19s31c96r002s/) |
| HTZ | 2026-11-02 21:29 | mention spike | 10 | 4.29 | 9 | 0 | wallstreetbets 7, pennystocks 3 | Nasdaq |  | [link](https://www.reddit.com/r/pennystocks/comments/1xmk38o/comment/19s34vbp3hwn4/) |
| IREN | 2026-11-03 08:03 | mention spike | 21 | 10.43 | 21 | 0 | wallstreetbets 21 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xjkxhl/comment/19s336ooh39nm/) |
| MSOS | 2026-10-31 21:03 | mention spike | 36 | 5.57 | 18 | 0 | wallstreetbets 36 | NYSE Arca |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xmwb04/) |
| MU | 2026-11-02 19:43 | mention spike | 31 | 10.29 | 11 | 0 | wallstreetbets 31 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xmq0vm/comment/19s34vb0qzyhx/) |
| OKLO | 2026-11-03 14:58 | mention spike | 10 | 2.29 | 7 | 0 | wallstreetbets 10 | NYSE |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xmq0vm/comment/19s2zsranf7mp/) |
| PLTR | 2026-11-02 13:09 | mention spike | 232 | 20.43 | 140 | 1 | wallstreetbets 232 | Nasdaq | #1 | [link](https://www.reddit.com/r/wallstreetbets/comments/1xm7gzv/) |
| RKLB | 2026-11-02 15:08 | mention spike | 24 | 11.14 | 15 | 0 | wallstreetbets 24 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xmq0vm/comment/19s33lz30e34z/) |
| SMCI | 2026-11-02 18:46 | mention spike | 28 | 5.29 | 25 | 0 | wallstreetbets 28 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xm5n1m/) |
| WMT | 2026-11-02 20:10 | mention spike | 17 | 3.14 | 12 | 0 | wallstreetbets 17 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xmq0vm/comment/19s2zywfitfts/) |
| SOUN | 2026-11-02 17:39 | mention spike | 2 | 4.29 | 2 | 0 | wallstreetbets 2 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xlu7un/comment/19s1f33538jmq/) |
| MRVL | 2026-11-02 21:05 | mention spike | 71 | 27.14 | 51 | 0 | wallstreetbets 68, smallstreetbets 3 | Nasdaq | #2 | [link](https://www.reddit.com/r/wallstreetbets/comments/1xmp5rp/) |
| AAOI | 2026-11-03 00:57 | mention spike | 16 | 8.14 | 10 | 0 | wallstreetbets 16 | Nasdaq | #27 | [link](https://www.reddit.com/r/wallstreetbets/comments/1xmeu2h/) |
| APLD | 2026-11-03 07:23 | mention spike | 9 | 3.43 | 8 | 0 | wallstreetbets 9 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xm9hzx/comment/19s2fiuhp2zur/) |
| LITE | 2026-11-02 21:16 | mention spike | 47 | 25.0 | 40 | 0 | wallstreetbets 47 | Nasdaq | #29 | [link](https://www.reddit.com/r/wallstreetbets/comments/1xmeu2h/) |
| ATC | 2026-11-02 07:17 | mention spike | 0 |  | 0 | 0 |  | Nasdaq |  |  |
| NNN | 2026-11-01 19:38 | mention spike | 4 | 3.29 | 4 | 0 | wallstreetbets 4 | NYSE |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xm9hzx/comment/19s1yzfqqzpq9/) |

Full history: `episodes.csv` (one row per first flag, with the numbers known at that moment).
