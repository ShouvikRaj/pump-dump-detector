# Stage 1 candidates

Updated 2026-11-03T17:35:08Z by run `41684546146`. A candidate is a ticker whose Reddit mentions (or hype-language
posts) in the last 24 hours jumped above its prior 7-day mean + 2 sd, with at least
10 mentions from 5 different authors. It stays listed until it goes
24 hours without a new flag. These are statistical flags, not accusations or advice.

| Ticker | Flagged since (UTC) | Why | Mentions 24h | Baseline/day | Authors | Hype posts | Subreddits | Exchange | StockTwits | Example |
|---|---|---|---|---|---|---|---|---|---|---|
| AAPL | 2026-11-02 20:10 | mention spike | 401 | 63.29 | 209 | 1 | wallstreetbets 400, smallstreetbets 1 | Nasdaq | #16 | [link](https://www.reddit.com/r/wallstreetbets/comments/1xmol2r/) |
| AEHR | 2026-11-03 15:08 | mention spike | 10 | 0.71 | 10 | 0 | wallstreetbets 10 | Nasdaq | #3 | [link](https://www.reddit.com/r/wallstreetbets/comments/1xjkxhl/comment/19s34i59ms2as/) |
| AMD | 2026-11-02 21:58 | mention spike | 319 | 65.86 | 233 | 1 | wallstreetbets 315, smallstreetbets 4 | Nasdaq | #18 | [link](https://www.reddit.com/r/smallstreetbets/comments/1xmw99c/) |
| ASTS | 2026-11-02 21:45 | mention spike | 45 | 18.0 | 37 | 0 | wallstreetbets 45 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xmq0vm/comment/19s31c96r002s/) |
| HTZ | 2026-11-02 21:29 | mention spike | 10 | 4.29 | 9 | 0 | wallstreetbets 7, pennystocks 3 | Nasdaq |  | [link](https://www.reddit.com/r/pennystocks/comments/1xmk38o/comment/19s34vbp3hwn4/) |
| IREN | 2026-11-03 08:03 | mention spike | 20 | 10.43 | 20 | 0 | wallstreetbets 20 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xjkxhl/comment/19s336ooh39nm/) |
| MSOS | 2026-10-31 21:03 | mention spike | 37 | 5.71 | 19 | 0 | wallstreetbets 37 | NYSE Arca |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xmwb04/) |
| MU | 2026-11-02 19:43 | mention spike | 30 | 10.43 | 11 | 0 | wallstreetbets 30 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xmq0vm/comment/19s34vb0qzyhx/) |
| OKLO | 2026-11-03 14:58 | mention spike | 11 | 2.29 | 8 | 0 | wallstreetbets 11 | NYSE | #14 | [link](https://www.reddit.com/r/wallstreetbets/comments/1xmq0vm/comment/19s36c81x7psw/) |
| PLTR | 2026-11-02 13:09 | mention spike | 232 | 20.86 | 142 | 1 | wallstreetbets 232 | Nasdaq | #1 | [link](https://www.reddit.com/r/wallstreetbets/comments/1xm7gzv/) |
| RKLB | 2026-11-02 15:08 | mention spike | 24 | 11.14 | 15 | 0 | wallstreetbets 24 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xmq0vm/comment/19s33lz30e34z/) |
| SMCI | 2026-11-02 18:46 | mention spike | 29 | 5.29 | 26 | 0 | wallstreetbets 29 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xm5n1m/) |
| WMT | 2026-11-02 20:10 | mention spike | 17 | 3.29 | 13 | 0 | wallstreetbets 17 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xmnwlb/comment/19s35zwd392rp/) |
| TSM | 2026-11-03 17:35 | mention spike | 13 | 5.14 | 6 | 0 | wallstreetbets 13 | NYSE |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xmq0vm/comment/19s36yznpbkv5/) |
| SOUN | 2026-11-02 17:39 | mention spike | 0 |  | 0 | 0 |  | Nasdaq |  |  |
| MRVL | 2026-11-02 21:05 | mention spike | 62 | 28.57 | 48 | 0 | wallstreetbets 59, smallstreetbets 3 | Nasdaq | #6 | [link](https://www.reddit.com/r/wallstreetbets/comments/1xmp5rp/) |
| AAOI | 2026-11-03 00:57 | mention spike | 17 | 8.29 | 10 | 0 | wallstreetbets 17 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xmeu2h/) |
| APLD | 2026-11-03 07:23 | mention spike | 8 | 3.57 | 7 | 0 | wallstreetbets 8 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xm9hzx/comment/19s2fiuhp2zur/) |
| LITE | 2026-11-02 21:16 | mention spike | 43 | 25.43 | 38 | 0 | wallstreetbets 43 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xmeu2h/) |
| ATC | 2026-11-02 07:17 | mention spike | 0 |  | 0 | 0 |  | Nasdaq |  |  |
| NNN | 2026-11-01 19:38 | mention spike | 5 | 3.29 | 5 | 0 | wallstreetbets 5 | NYSE |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xmq0vm/comment/19s368bpalmjm/) |

Full history: `episodes.csv` (one row per first flag, with the numbers known at that moment).
