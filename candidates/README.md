# Stage 1 candidates

Updated 2026-11-03T18:27:08Z by run `41693147703`. A candidate is a ticker whose Reddit mentions (or hype-language
posts) in the last 24 hours jumped above its prior 7-day mean + 2 sd, with at least
10 mentions from 5 different authors. It stays listed until it goes
24 hours without a new flag. These are statistical flags, not accusations or advice.

| Ticker | Flagged since (UTC) | Why | Mentions 24h | Baseline/day | Authors | Hype posts | Subreddits | Exchange | StockTwits | Example |
|---|---|---|---|---|---|---|---|---|---|---|
| AAPL | 2026-11-02 20:10 | mention spike | 387 | 65.43 | 205 | 1 | wallstreetbets 386, smallstreetbets 1 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xmol2r/) |
| AEHR | 2026-11-03 15:08 | mention spike | 10 | 0.71 | 10 | 0 | wallstreetbets 10 | Nasdaq | #1 | [link](https://www.reddit.com/r/wallstreetbets/comments/1xjkxhl/comment/19s34i59ms2as/) |
| AMD | 2026-11-02 21:58 | mention spike | 335 | 69.0 | 243 | 1 | wallstreetbets 331, smallstreetbets 4 | Nasdaq | #20 | [link](https://www.reddit.com/r/smallstreetbets/comments/1xmw99c/) |
| ASTS | 2026-11-02 21:45 | mention spike | 43 | 18.29 | 36 | 0 | wallstreetbets 43 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xmq0vm/comment/19s31c96r002s/) |
| HTZ | 2026-11-02 21:29 | mention spike | 12 | 4.29 | 10 | 0 | wallstreetbets 9, pennystocks 3 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xmq0vm/comment/19s37ryuq8cip/) |
| MSOS | 2026-10-31 21:03 | mention spike | 36 | 6.0 | 18 | 0 | wallstreetbets 36 | NYSE Arca |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xmwb04/) |
| MU | 2026-11-02 19:43 | mention spike | 26 | 11.43 | 11 | 0 | wallstreetbets 26 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xmq0vm/comment/19s39me9by6ap/) |
| OKLO | 2026-11-03 14:58 | mention spike | 10 | 2.43 | 8 | 0 | wallstreetbets 10 | NYSE |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xmq0vm/comment/19s36c81x7psw/) |
| PLTR | 2026-11-02 13:09 | mention spike | 222 | 22.14 | 140 | 1 | wallstreetbets 222 | Nasdaq | #5 | [link](https://www.reddit.com/r/wallstreetbets/comments/1xm7gzv/) |
| SMCI | 2026-11-02 18:46 | mention spike | 25 | 5.57 | 21 | 0 | wallstreetbets 25 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xm5n1m/) |
| WMT | 2026-11-02 20:10 | mention spike | 16 | 3.43 | 12 | 0 | wallstreetbets 16 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xmnwlb/comment/19s35zwd392rp/) |
| IREN | 2026-11-03 08:03 | mention spike | 17 | 10.86 | 17 | 0 | wallstreetbets 17 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xjkxhl/comment/19s336ooh39nm/) |
| RKLB | 2026-11-02 15:08 | mention spike | 21 | 11.57 | 15 | 0 | wallstreetbets 21 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xmq0vm/comment/19s33lz30e34z/) |
| TSM | 2026-11-03 17:35 | mention spike | 13 | 5.0 | 6 | 0 | wallstreetbets 13 | NYSE |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xmq0vm/comment/19s36yznpbkv5/) |
| SOUN | 2026-11-02 17:39 | mention spike | 0 |  | 0 | 0 |  | Nasdaq |  |  |
| MRVL | 2026-11-02 21:05 | mention spike | 59 | 29.0 | 46 | 0 | wallstreetbets 56, smallstreetbets 3 | Nasdaq | #28 | [link](https://www.reddit.com/r/wallstreetbets/comments/1xmp5rp/) |
| AAOI | 2026-11-03 00:57 | mention spike | 16 | 8.29 | 10 | 0 | wallstreetbets 16 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xmeu2h/) |
| APLD | 2026-11-03 07:23 | mention spike | 7 | 3.71 | 6 | 0 | wallstreetbets 7 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xm9hzx/comment/19s2fiuhp2zur/) |
| LITE | 2026-11-02 21:16 | mention spike | 39 | 26.0 | 36 | 0 | wallstreetbets 39 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xmeu2h/) |
| ATC | 2026-11-02 07:17 | mention spike | 0 |  | 0 | 0 |  | Nasdaq |  |  |
| NNN | 2026-11-01 19:38 | mention spike | 5 | 3.29 | 5 | 0 | wallstreetbets 5 | NYSE |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xmq0vm/comment/19s368bpalmjm/) |

Full history: `episodes.csv` (one row per first flag, with the numbers known at that moment).
