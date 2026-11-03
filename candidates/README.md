# Stage 1 candidates

Updated 2026-11-03T08:39:08Z by run `41604574377`. A candidate is a ticker whose Reddit mentions (or hype-language
posts) in the last 24 hours jumped above its prior 7-day mean + 2 sd, with at least
10 mentions from 5 different authors. It stays listed until it goes
24 hours without a new flag. These are statistical flags, not accusations or advice.

| Ticker | Flagged since (UTC) | Why | Mentions 24h | Baseline/day | Authors | Hype posts | Subreddits | Exchange | StockTwits | Example |
|---|---|---|---|---|---|---|---|---|---|---|
| AAOI | 2026-11-03 00:57 | mention spike | 20 | 7.57 | 11 | 1 | wallstreetbets 20 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xmeu2h/) |
| AAPL | 2026-11-02 20:10 | mention spike | 411 | 57.43 | 211 | 1 | wallstreetbets 408, smallstreetbets 3 | Nasdaq | #1 | [link](https://www.reddit.com/r/wallstreetbets/comments/1xm9hzx/comment/19s2geu2kdvyb/) |
| AMD | 2026-11-02 21:58 | mention spike | 238 | 59.71 | 175 | 1 | wallstreetbets 237, smallstreetbets 1 | Nasdaq | #6 | [link](https://www.reddit.com/r/wallstreetbets/comments/1xmcf27/) |
| APLD | 2026-11-03 07:23 | mention spike | 11 | 3.86 | 10 | 0 | wallstreetbets 11 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xm9hzx/comment/19s2fiuhp2zur/) |
| ASTS | 2026-11-02 21:45 | mention spike | 53 | 17.14 | 39 | 0 | wallstreetbets 53 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xm9hzx/comment/19s2dn3otq32d/) |
| IREN | 2026-11-03 08:03 | mention spike | 22 | 10.71 | 19 | 0 | wallstreetbets 22 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xm2b50/) |
| LITE | 2026-11-02 21:16 | mention spike | 95 | 17.14 | 68 | 0 | wallstreetbets 95 | Nasdaq | #20 | [link](https://www.reddit.com/r/wallstreetbets/comments/1xmeu2h/) |
| MRVL | 2026-11-02 21:05 | mention spike | 113 | 18.86 | 75 | 0 | wallstreetbets 111, smallstreetbets 2 | Nasdaq | #3 | [link](https://www.reddit.com/r/smallstreetbets/comments/1xmlwif/) |
| MSOS | 2026-10-31 21:03 | mention spike | 38 | 2.71 | 25 | 0 | wallstreetbets 38 | NYSE Arca |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xkftz6/comment/19s241f4nl4kk/) |
| MU | 2026-11-02 19:43 | mention spike | 31 | 10.0 | 11 | 0 | wallstreetbets 31 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xm9hzx/comment/19s2di860tvya/) |
| PLTR | 2026-11-02 13:09 | mention spike | 223 | 17.0 | 143 | 1 | wallstreetbets 223 | Nasdaq | #2 | [link](https://www.reddit.com/r/wallstreetbets/comments/1xm7gzv/) |
| RKLB | 2026-11-02 15:08 | mention spike | 23 | 10.71 | 14 | 0 | wallstreetbets 23 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xm9hzx/comment/19s2adohh84qq/) |
| SMCI | 2026-11-02 18:46 | mention spike | 21 | 5.14 | 20 | 0 | wallstreetbets 21 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xm5n1m/) |
| SOUN | 2026-11-02 17:39 | mention spike | 26 | 0.86 | 5 | 1 | wallstreetbets 26 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xlu7un/comment/19s1f33538jmq/) |
| WMT | 2026-11-02 20:10 | mention spike | 15 | 3.14 | 11 | 0 | wallstreetbets 15 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xm9hzx/comment/19s1zm3ks48ar/) |
| HTZ | 2026-11-02 21:29 | mention spike | 8 | 4.0 | 8 | 0 | wallstreetbets 6, pennystocks 2 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xm9hzx/comment/19s1pb71a711f/) |
| ATC | 2026-11-02 07:17 | mention spike | 0 |  | 0 | 0 |  | Nasdaq |  |  |
| NNN | 2026-11-01 19:38 | mention spike | 6 | 3.0 | 5 | 0 | wallstreetbets 6 | NYSE |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xm9hzx/comment/19s1yzfqqzpq9/) |

Full history: `episodes.csv` (one row per first flag, with the numbers known at that moment).
