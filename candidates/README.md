# Stage 1 candidates

Updated 2026-11-03T12:26:08Z by run `41635186327`. A candidate is a ticker whose Reddit mentions (or hype-language
posts) in the last 24 hours jumped above its prior 7-day mean + 2 sd, with at least
10 mentions from 5 different authors. It stays listed until it goes
24 hours without a new flag. These are statistical flags, not accusations or advice.

| Ticker | Flagged since (UTC) | Why | Mentions 24h | Baseline/day | Authors | Hype posts | Subreddits | Exchange | StockTwits | Example |
|---|---|---|---|---|---|---|---|---|---|---|
| AAOI | 2026-11-03 00:57 | mention spike | 20 | 7.57 | 11 | 1 | wallstreetbets 20 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xmeu2h/) |
| AAPL | 2026-11-02 20:10 | mention spike | 426 | 57.71 | 216 | 1 | wallstreetbets 423, smallstreetbets 3 | Nasdaq | #9 | [link](https://www.reddit.com/r/wallstreetbets/comments/1xmol2r/) |
| AMD | 2026-11-02 21:58 | mention spike | 253 | 59.29 | 187 | 1 | wallstreetbets 252, smallstreetbets 1 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xmqlo9/) |
| ASTS | 2026-11-02 21:45 | mention spike | 54 | 17.29 | 41 | 0 | wallstreetbets 54 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xmq0vm/comment/19s2t8tfeo3ts/) |
| IREN | 2026-11-03 08:03 | mention spike | 24 | 10.14 | 21 | 0 | wallstreetbets 24 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xm2b50/) |
| LITE | 2026-11-02 21:16 | mention spike | 93 | 17.43 | 66 | 0 | wallstreetbets 93 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xmeu2h/) |
| MRVL | 2026-11-02 21:05 | mention spike | 109 | 19.71 | 73 | 0 | wallstreetbets 107, smallstreetbets 2 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xmp5rp/) |
| MSOS | 2026-10-31 21:03 | mention spike | 37 | 2.86 | 25 | 0 | wallstreetbets 37 | NYSE Arca |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xkftz6/comment/19s241f4nl4kk/) |
| MU | 2026-11-02 19:43 | mention spike | 33 | 10.0 | 11 | 0 | wallstreetbets 33 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xm9hzx/comment/19s2l0gih2o00/) |
| PLTR | 2026-11-02 13:09 | mention spike | 238 | 17.29 | 150 | 1 | wallstreetbets 238 | Nasdaq | #1 | [link](https://www.reddit.com/r/wallstreetbets/comments/1xm7gzv/) |
| RKLB | 2026-11-02 15:08 | mention spike | 23 | 10.71 | 14 | 0 | wallstreetbets 23 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xm9hzx/comment/19s2l5kgjn2f6/) |
| SMCI | 2026-11-02 18:46 | mention spike | 22 | 5.14 | 21 | 0 | wallstreetbets 22 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xm5n1m/) |
| SOUN | 2026-11-02 17:39 | mention spike | 26 | 0.86 | 5 | 1 | wallstreetbets 26 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xlu7un/comment/19s1f33538jmq/) |
| WMT | 2026-11-02 20:10 | mention spike | 16 | 3.14 | 11 | 0 | wallstreetbets 16 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xm9hzx/comment/19s2mb1mobeo4/) |
| APLD | 2026-11-03 07:23 | mention spike | 10 | 4.0 | 9 | 0 | wallstreetbets 10 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xm9hzx/comment/19s2fiuhp2zur/) |
| HTZ | 2026-11-02 21:29 | mention spike | 8 | 3.71 | 8 | 0 | wallstreetbets 6, pennystocks 2 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xm9hzx/comment/19s1pb71a711f/) |
| ATC | 2026-11-02 07:17 | mention spike | 0 |  | 0 | 0 |  | Nasdaq |  |  |
| NNN | 2026-11-01 19:38 | mention spike | 6 | 3.0 | 5 | 0 | wallstreetbets 6 | NYSE |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xm9hzx/comment/19s1yzfqqzpq9/) |

Full history: `episodes.csv` (one row per first flag, with the numbers known at that moment).
