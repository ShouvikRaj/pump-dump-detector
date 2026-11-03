# Stage 1 candidates

Updated 2026-11-03T17:49:10Z by run `41686689516`. A candidate is a ticker whose Reddit mentions (or hype-language
posts) in the last 24 hours jumped above its prior 7-day mean + 2 sd, with at least
10 mentions from 5 different authors. It stays listed until it goes
24 hours without a new flag. These are statistical flags, not accusations or advice.

| Ticker | Flagged since (UTC) | Why | Mentions 24h | Baseline/day | Authors | Hype posts | Subreddits | Exchange | StockTwits | Example |
|---|---|---|---|---|---|---|---|---|---|---|
| AAPL | 2026-11-02 20:10 | mention spike | 400 | 63.29 | 209 | 1 | wallstreetbets 399, smallstreetbets 1 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xmol2r/) |
| AEHR | 2026-11-03 15:08 | mention spike | 10 | 0.71 | 10 | 0 | wallstreetbets 10 | Nasdaq | #3 | [link](https://www.reddit.com/r/wallstreetbets/comments/1xjkxhl/comment/19s34i59ms2as/) |
| AMD | 2026-11-02 21:58 | mention spike | 325 | 66.29 | 236 | 1 | wallstreetbets 321, smallstreetbets 4 | Nasdaq | #23 | [link](https://www.reddit.com/r/smallstreetbets/comments/1xmw99c/) |
| ASTS | 2026-11-02 21:45 | mention spike | 45 | 18.0 | 37 | 0 | wallstreetbets 45 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xmq0vm/comment/19s31c96r002s/) |
| HTZ | 2026-11-02 21:29 | mention spike | 12 | 4.29 | 10 | 0 | wallstreetbets 9, pennystocks 3 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xmq0vm/comment/19s37ryuq8cip/) |
| IREN | 2026-11-03 08:03 | mention spike | 19 | 10.57 | 19 | 0 | wallstreetbets 19 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xjkxhl/comment/19s336ooh39nm/) |
| MSOS | 2026-10-31 21:03 | mention spike | 38 | 5.71 | 19 | 0 | wallstreetbets 38 | NYSE Arca |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xmwb04/) |
| MU | 2026-11-02 19:43 | mention spike | 30 | 10.43 | 11 | 0 | wallstreetbets 30 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xmq0vm/comment/19s34vb0qzyhx/) |
| OKLO | 2026-11-03 14:58 | mention spike | 10 | 2.43 | 8 | 0 | wallstreetbets 10 | NYSE |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xmq0vm/comment/19s36c81x7psw/) |
| PLTR | 2026-11-02 13:09 | mention spike | 230 | 21.14 | 142 | 1 | wallstreetbets 230 | Nasdaq | #1 | [link](https://www.reddit.com/r/wallstreetbets/comments/1xm7gzv/) |
| RKLB | 2026-11-02 15:08 | mention spike | 24 | 11.14 | 15 | 0 | wallstreetbets 24 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xmq0vm/comment/19s33lz30e34z/) |
| SMCI | 2026-11-02 18:46 | mention spike | 30 | 5.0 | 26 | 0 | wallstreetbets 30 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xm5n1m/) |
| TSM | 2026-11-03 17:35 | mention spike | 13 | 5.14 | 6 | 0 | wallstreetbets 13 | NYSE |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xmq0vm/comment/19s36yznpbkv5/) |
| WMT | 2026-11-02 20:10 | mention spike | 17 | 3.29 | 13 | 0 | wallstreetbets 17 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xmnwlb/comment/19s35zwd392rp/) |
| SOUN | 2026-11-02 17:39 | mention spike | 0 |  | 0 | 0 |  | Nasdaq |  |  |
| MRVL | 2026-11-02 21:05 | mention spike | 60 | 28.86 | 46 | 0 | wallstreetbets 57, smallstreetbets 3 | Nasdaq | #9 | [link](https://www.reddit.com/r/wallstreetbets/comments/1xmp5rp/) |
| AAOI | 2026-11-03 00:57 | mention spike | 16 | 8.29 | 10 | 0 | wallstreetbets 16 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xmeu2h/) |
| APLD | 2026-11-03 07:23 | mention spike | 8 | 3.57 | 7 | 0 | wallstreetbets 8 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xm9hzx/comment/19s2fiuhp2zur/) |
| LITE | 2026-11-02 21:16 | mention spike | 41 | 25.71 | 37 | 0 | wallstreetbets 41 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xmeu2h/) |
| ATC | 2026-11-02 07:17 | mention spike | 0 |  | 0 | 0 |  | Nasdaq |  |  |
| NNN | 2026-11-01 19:38 | mention spike | 5 | 3.29 | 5 | 0 | wallstreetbets 5 | NYSE |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xmq0vm/comment/19s368bpalmjm/) |

Full history: `episodes.csv` (one row per first flag, with the numbers known at that moment).
