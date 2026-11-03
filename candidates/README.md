# Stage 1 candidates

Updated 2026-11-03T15:20:09Z by run `41661987791`. A candidate is a ticker whose Reddit mentions (or hype-language
posts) in the last 24 hours jumped above its prior 7-day mean + 2 sd, with at least
10 mentions from 5 different authors. It stays listed until it goes
24 hours without a new flag. These are statistical flags, not accusations or advice.

| Ticker | Flagged since (UTC) | Why | Mentions 24h | Baseline/day | Authors | Hype posts | Subreddits | Exchange | StockTwits | Example |
|---|---|---|---|---|---|---|---|---|---|---|
| AAPL | 2026-11-02 20:10 | mention spike | 424 | 59.71 | 219 | 1 | wallstreetbets 421, smallstreetbets 3 | Nasdaq | #2 | [link](https://www.reddit.com/r/wallstreetbets/comments/1xmol2r/) |
| AEHR | 2026-11-03 15:08 | mention spike | 11 | 0.43 | 10 | 0 | wallstreetbets 11 | Nasdaq | #4 | [link](https://www.reddit.com/r/wallstreetbets/comments/1xmq0vm/comment/19s3130fgp8io/) |
| AMD | 2026-11-02 21:58 | mention spike | 293 | 59.71 | 211 | 1 | wallstreetbets 292, smallstreetbets 1 | Nasdaq | #13 | [link](https://www.reddit.com/r/wallstreetbets/comments/1xmqlo9/) |
| ASTS | 2026-11-02 21:45 | mention spike | 48 | 17.43 | 38 | 0 | wallstreetbets 48 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xmrw7a/comment/19s2ymfxmfc3o/) |
| IREN | 2026-11-03 08:03 | mention spike | 23 | 10.0 | 23 | 0 | wallstreetbets 23 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xm2b50/) |
| MSOS | 2026-10-31 21:03 | mention spike | 38 | 4.43 | 20 | 0 | wallstreetbets 38 | NYSE Arca |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xmq0vm/comment/19s31647o4aqr/) |
| MU | 2026-11-02 19:43 | mention spike | 32 | 9.86 | 10 | 0 | wallstreetbets 32 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xmq0vm/comment/19s30q4j6t2ed/) |
| OKLO | 2026-11-03 14:58 | mention spike | 10 | 2.29 | 7 | 0 | wallstreetbets 10 | NYSE |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xmq0vm/comment/19s2zsranf7mp/) |
| PLTR | 2026-11-02 13:09 | mention spike | 237 | 19.0 | 144 | 1 | wallstreetbets 237 | Nasdaq | #1 | [link](https://www.reddit.com/r/wallstreetbets/comments/1xm7gzv/) |
| RKLB | 2026-11-02 15:08 | mention spike | 22 | 11.0 | 14 | 0 | wallstreetbets 22 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xmq0vm/comment/19s317e9v7q74/) |
| SMCI | 2026-11-02 18:46 | mention spike | 26 | 5.43 | 23 | 0 | wallstreetbets 26 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xm5n1m/) |
| SOUN | 2026-11-02 17:39 | mention spike | 26 | 0.86 | 5 | 1 | wallstreetbets 26 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xlu7un/comment/19s1f33538jmq/) |
| WMT | 2026-11-02 20:10 | mention spike | 17 | 3.14 | 12 | 0 | wallstreetbets 17 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xmq0vm/comment/19s2zywfitfts/) |
| MRVL | 2026-11-02 21:05 | mention spike | 78 | 25.14 | 53 | 0 | wallstreetbets 75, smallstreetbets 3 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xmp5rp/) |
| AAOI | 2026-11-03 00:57 | mention spike | 18 | 7.86 | 10 | 1 | wallstreetbets 18 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xmeu2h/) |
| APLD | 2026-11-03 07:23 | mention spike | 9 | 3.43 | 8 | 0 | wallstreetbets 9 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xm9hzx/comment/19s2fiuhp2zur/) |
| LITE | 2026-11-02 21:16 | mention spike | 62 | 22.29 | 47 | 0 | wallstreetbets 62 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xmeu2h/) |
| HTZ | 2026-11-02 21:29 | mention spike | 6 | 4.29 | 6 | 0 | wallstreetbets 5, pennystocks 1 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xmq0vm/comment/19s30nn0atdgg/) |
| ATC | 2026-11-02 07:17 | mention spike | 0 |  | 0 | 0 |  | Nasdaq |  |  |
| NNN | 2026-11-01 19:38 | mention spike | 6 | 3.0 | 5 | 0 | wallstreetbets 6 | NYSE |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xm9hzx/comment/19s1yzfqqzpq9/) |

Full history: `episodes.csv` (one row per first flag, with the numbers known at that moment).
