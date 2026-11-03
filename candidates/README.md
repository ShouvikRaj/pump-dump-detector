# Stage 1 candidates

Updated 2026-11-03T19:38:10Z by run `41703710028`. A candidate is a ticker whose Reddit mentions (or hype-language
posts) in the last 24 hours jumped above its prior 7-day mean + 2 sd, with at least
10 mentions from 5 different authors. It stays listed until it goes
24 hours without a new flag. These are statistical flags, not accusations or advice.

| Ticker | Flagged since (UTC) | Why | Mentions 24h | Baseline/day | Authors | Hype posts | Subreddits | Exchange | StockTwits | Example |
|---|---|---|---|---|---|---|---|---|---|---|
| AAPL | 2026-11-02 20:10 | mention spike | 375 | 67.29 | 200 | 1 | wallstreetbets 375 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xmol2r/) |
| AMD | 2026-11-02 21:58 | mention spike | 351 | 72.14 | 257 | 1 | wallstreetbets 347, smallstreetbets 4 | Nasdaq | #17 | [link](https://www.reddit.com/r/smallstreetbets/comments/1xmw99c/) |
| DDOG | 2026-11-03 18:57 | mention spike | 10 | 2.43 | 6 | 0 | wallstreetbets 10 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xmq0vm/comment/19s3chnrkktpf/) |
| HTZ | 2026-11-02 21:29 | mention spike | 12 | 4.29 | 10 | 0 | wallstreetbets 9, pennystocks 3 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xmq0vm/comment/19s37ryuq8cip/) |
| MSOS | 2026-10-31 21:03 | mention spike | 33 | 6.86 | 18 | 0 | wallstreetbets 33 | NYSE Arca |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xmwb04/) |
| PLTR | 2026-11-02 13:09 | mention spike | 215 | 23.57 | 137 | 1 | wallstreetbets 215 | Nasdaq | #6 | [link](https://www.reddit.com/r/wallstreetbets/comments/1xm7gzv/) |
| SMCI | 2026-11-02 18:46 | mention spike | 26 | 6.43 | 22 | 0 | wallstreetbets 26 | Nasdaq | #28 | [link](https://www.reddit.com/r/wallstreetbets/comments/1xmq0vm/comment/19s3cf9gp4cwy/) |
| ASTS | 2026-11-02 21:45 | mention spike | 40 | 18.86 | 34 | 0 | wallstreetbets 40 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xn27k9/comment/19s3casrhrz50/) |
| WMT | 2026-11-02 20:10 | mention spike | 11 | 4.14 | 9 | 0 | wallstreetbets 11 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xmnwlb/comment/19s35zwd392rp/) |
| AEHR | 2026-11-03 15:08 | mention spike | 8 | 1.0 | 8 | 0 | wallstreetbets 8 | Nasdaq | #1 | [link](https://www.reddit.com/r/wallstreetbets/comments/1xjkxhl/comment/19s34i59ms2as/) |
| MU | 2026-11-02 19:43 | mention spike | 19 | 12.29 | 9 | 0 | wallstreetbets 19 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xmq0vm/comment/19s39me9by6ap/) |
| OKLO | 2026-11-03 14:58 | mention spike | 7 | 2.86 | 7 | 0 | wallstreetbets 7 | NYSE |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xmq0vm/comment/19s36c81x7psw/) |
| IREN | 2026-11-03 08:03 | mention spike | 14 | 11.14 | 14 | 0 | wallstreetbets 14 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xjkxhl/comment/19s336ooh39nm/) |
| RKLB | 2026-11-02 15:08 | mention spike | 21 | 11.86 | 13 | 0 | wallstreetbets 21 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xmq0vm/comment/19s3cgpgjj52a/) |
| TSM | 2026-11-03 17:35 | mention spike | 11 | 5.29 | 6 | 0 | wallstreetbets 11 | NYSE |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xmq0vm/comment/19s36yznpbkv5/) |
| SOUN | 2026-11-02 17:39 | mention spike | 0 |  | 0 | 0 |  | Nasdaq |  |  |
| MRVL | 2026-11-02 21:05 | mention spike | 50 | 30.29 | 39 | 0 | wallstreetbets 47, smallstreetbets 3 | Nasdaq | #26 | [link](https://www.reddit.com/r/wallstreetbets/comments/1xmp5rp/) |
| AAOI | 2026-11-03 00:57 | mention spike | 14 | 8.43 | 10 | 0 | wallstreetbets 14 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xmeu2h/) |
| APLD | 2026-11-03 07:23 | mention spike | 4 | 4.14 | 3 | 0 | wallstreetbets 4 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xm9hzx/comment/19s2fiuhp2zur/) |
| LITE | 2026-11-02 21:16 | mention spike | 31 | 27.29 | 30 | 0 | wallstreetbets 31 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xmeu2h/) |
| ATC | 2026-11-02 07:17 | mention spike | 0 |  | 0 | 0 |  | Nasdaq |  |  |

Full history: `episodes.csv` (one row per first flag, with the numbers known at that moment).
