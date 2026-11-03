# Stage 1 candidates

Updated 2026-11-03T14:58:07Z by run `41657381059`. A candidate is a ticker whose Reddit mentions (or hype-language
posts) in the last 24 hours jumped above its prior 7-day mean + 2 sd, with at least
10 mentions from 5 different authors. It stays listed until it goes
24 hours without a new flag. These are statistical flags, not accusations or advice.

| Ticker | Flagged since (UTC) | Why | Mentions 24h | Baseline/day | Authors | Hype posts | Subreddits | Exchange | StockTwits | Example |
|---|---|---|---|---|---|---|---|---|---|---|
| AAPL | 2026-11-02 20:10 | mention spike | 424 | 59.14 | 220 | 1 | wallstreetbets 421, smallstreetbets 3 | Nasdaq | #11 | [link](https://www.reddit.com/r/wallstreetbets/comments/1xmol2r/) |
| AMD | 2026-11-02 21:58 | mention spike | 283 | 59.57 | 205 | 1 | wallstreetbets 282, smallstreetbets 1 | Nasdaq | #12 | [link](https://www.reddit.com/r/wallstreetbets/comments/1xmqlo9/) |
| ASTS | 2026-11-02 21:45 | mention spike | 49 | 17.57 | 38 | 0 | wallstreetbets 49 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xmrw7a/comment/19s2ymfxmfc3o/) |
| IREN | 2026-11-03 08:03 | mention spike | 22 | 10.43 | 21 | 0 | wallstreetbets 22 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xm2b50/) |
| MSOS | 2026-10-31 21:03 | mention spike | 37 | 4.29 | 20 | 0 | wallstreetbets 37 | NYSE Arca |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xmq0vm/comment/19s2zolsuftyc/) |
| MU | 2026-11-02 19:43 | mention spike | 32 | 9.86 | 11 | 0 | wallstreetbets 32 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xmq0vm/comment/19s2ze431fko3/) |
| PLTR | 2026-11-02 13:09 | mention spike | 239 | 18.29 | 147 | 1 | wallstreetbets 239 | Nasdaq | #7 | [link](https://www.reddit.com/r/wallstreetbets/comments/1xm7gzv/) |
| SMCI | 2026-11-02 18:46 | mention spike | 24 | 5.43 | 22 | 0 | wallstreetbets 24 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xm5n1m/) |
| SOUN | 2026-11-02 17:39 | mention spike | 26 | 0.86 | 5 | 1 | wallstreetbets 26 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xlu7un/comment/19s1f33538jmq/) |
| WMT | 2026-11-02 20:10 | mention spike | 17 | 3.14 | 12 | 0 | wallstreetbets 17 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xmq0vm/comment/19s2zywfitfts/) |
| OKLO | 2026-11-03 14:58 | mention spike | 10 | 2.43 | 7 | 0 | wallstreetbets 10 | NYSE |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xmq0vm/comment/19s2zsranf7mp/) |
| RKLB | 2026-11-02 15:08 | mention spike | 21 | 11.14 | 14 | 0 | wallstreetbets 21 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xmrw7a/comment/19s2ymfxmfc3o/) |
| MRVL | 2026-11-02 21:05 | mention spike | 80 | 24.14 | 53 | 0 | wallstreetbets 77, smallstreetbets 3 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xmp5rp/) |
| AAOI | 2026-11-03 00:57 | mention spike | 18 | 7.86 | 10 | 1 | wallstreetbets 18 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xmeu2h/) |
| APLD | 2026-11-03 07:23 | mention spike | 9 | 3.43 | 8 | 0 | wallstreetbets 9 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xm9hzx/comment/19s2fiuhp2zur/) |
| LITE | 2026-11-02 21:16 | mention spike | 69 | 21.0 | 51 | 0 | wallstreetbets 69 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xmeu2h/) |
| HTZ | 2026-11-02 21:29 | mention spike | 5 | 4.29 | 5 | 0 | wallstreetbets 3, pennystocks 2 | Nasdaq |  | [link](https://www.reddit.com/r/pennystocks/comments/1xmk38o/comment/19s2vnf8evkas/) |
| ATC | 2026-11-02 07:17 | mention spike | 0 |  | 0 | 0 |  | Nasdaq |  |  |
| NNN | 2026-11-01 19:38 | mention spike | 6 | 3.0 | 5 | 0 | wallstreetbets 6 | NYSE |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xm9hzx/comment/19s1yzfqqzpq9/) |

Full history: `episodes.csv` (one row per first flag, with the numbers known at that moment).
