# Stage 1 candidates

Updated 2026-11-03T20:28:05Z by run `41712098363`. A candidate is a ticker whose Reddit mentions (or hype-language
posts) in the last 24 hours jumped above its prior 7-day mean + 2 sd, with at least
10 mentions from 5 different authors. It stays listed until it goes
24 hours without a new flag. These are statistical flags, not accusations or advice.

| Ticker | Flagged since (UTC) | Why | Mentions 24h | Baseline/day | Authors | Hype posts | Subreddits | Exchange | StockTwits | Example |
|---|---|---|---|---|---|---|---|---|---|---|
| AAPL | 2026-11-02 20:10 | mention spike | 356 | 70.29 | 195 | 1 | wallstreetbets 356 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xmol2r/) |
| AMD | 2026-11-02 21:58 | mention spike | 403 | 73.86 | 278 | 1 | wallstreetbets 399, smallstreetbets 4 | Nasdaq | #3 | [link](https://www.reddit.com/r/smallstreetbets/comments/1xmw99c/) |
| HTZ | 2026-11-02 21:29 | mention spike | 11 | 4.43 | 9 | 0 | wallstreetbets 8, pennystocks 3 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xmq0vm/comment/19s37ryuq8cip/) |
| MSOS | 2026-10-31 21:03 | mention spike | 36 | 6.86 | 19 | 0 | wallstreetbets 36 | NYSE Arca |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xmwb04/) |
| PLTR | 2026-11-02 13:09 | mention spike | 198 | 26.29 | 129 | 1 | wallstreetbets 198 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xmq0vm/comment/19s3eu8i6gz1e/) |
| SMCI | 2026-11-02 18:46 | mention spike | 35 | 6.29 | 29 | 0 | wallstreetbets 35 | Nasdaq | #2 | [link](https://www.reddit.com/r/wallstreetbets/comments/1xn333e/) |
| ASTS | 2026-11-02 21:45 | mention spike | 35 | 19.86 | 29 | 0 | wallstreetbets 35 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xmq0vm/comment/19s3djt8jf3oh/) |
| DDOG | 2026-11-03 18:57 | mention spike | 9 | 2.57 | 6 | 0 | wallstreetbets 9 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xmq0vm/comment/19s3chnrkktpf/) |
| WMT | 2026-11-02 20:10 | mention spike | 8 | 4.57 | 7 | 0 | wallstreetbets 8 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xmnwlb/comment/19s35zwd392rp/) |
| AEHR | 2026-11-03 15:08 | mention spike | 8 | 1.0 | 8 | 0 | wallstreetbets 8 | Nasdaq | #13 | [link](https://www.reddit.com/r/wallstreetbets/comments/1xjkxhl/comment/19s34i59ms2as/) |
| MU | 2026-11-02 19:43 | mention spike | 22 | 11.86 | 9 | 0 | wallstreetbets 22 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xmq0vm/comment/19s3ejxwc25b6/) |
| OKLO | 2026-11-03 14:58 | mention spike | 8 | 2.71 | 7 | 0 | wallstreetbets 8 | NYSE |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xmq0vm/comment/19s3dqlvqwtia/) |
| IREN | 2026-11-03 08:03 | mention spike | 12 | 11.29 | 12 | 0 | wallstreetbets 12 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xjkxhl/comment/19s336ooh39nm/) |
| RKLB | 2026-11-02 15:08 | mention spike | 19 | 12.14 | 12 | 0 | wallstreetbets 19 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xmq0vm/comment/19s3cgpgjj52a/) |
| TSM | 2026-11-03 17:35 | mention spike | 11 | 5.29 | 6 | 0 | wallstreetbets 11 | NYSE |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xmq0vm/comment/19s3cx5r4s40y/) |
| SOUN | 2026-11-02 17:39 | mention spike | 0 |  | 0 | 0 |  | Nasdaq |  |  |
| MRVL | 2026-11-02 21:05 | mention spike | 42 | 31.57 | 33 | 0 | wallstreetbets 38, smallstreetbets 4 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xmp5rp/) |
| AAOI | 2026-11-03 00:57 | mention spike | 13 | 8.71 | 9 | 0 | wallstreetbets 13 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xmeu2h/) |
| APLD | 2026-11-03 07:23 | mention spike | 3 | 4.29 | 2 | 0 | wallstreetbets 3 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xm9hzx/comment/19s2fiuhp2zur/) |
| LITE | 2026-11-02 21:16 | mention spike | 25 | 28.14 | 24 | 0 | wallstreetbets 25 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xmeu2h/) |
| ATC | 2026-11-02 07:17 | mention spike | 0 |  | 0 | 0 |  | Nasdaq |  |  |

Full history: `episodes.csv` (one row per first flag, with the numbers known at that moment).
