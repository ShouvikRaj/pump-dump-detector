# Stage 1 candidates

Updated 2026-11-16T15:08:10Z by run `43890972663`. A candidate is a ticker whose Reddit mentions (or hype-language
posts) in the last 24 hours jumped above its prior 7-day mean + 2 sd, with at least
10 mentions from 5 different authors. It stays listed until it goes
24 hours without a new flag. These are statistical flags, not accusations or advice.

| Ticker | Flagged since (UTC) | Why | Mentions 24h | Baseline/day | Authors | Hype posts | Subreddits | Exchange | StockTwits | Example |
|---|---|---|---|---|---|---|---|---|---|---|
| WMT | 2026-11-16 07:17 | mention spike | 13 | 3.71 | 12 | 0 | wallstreetbets 13 | Nasdaq | #29 | [link](https://www.reddit.com/r/wallstreetbets/comments/1xxmkhj/comment/19sq6vzgdtlfm/) |
| HOOD | 2026-11-16 15:08 | mention spike | 11 | 3.86 | 11 | 0 | wallstreetbets 11 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xxmkhj/comment/19sq7c5vprg05/) |
| ASML | 2026-11-15 23:05 | mention spike | 3 | 7.86 | 3 | 0 | wallstreetbets 3 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xwa164/comment/19sp0fwp4wjl0/) |
| DXYZ | 2026-11-14 23:53 | mention spike | 8 | 6.0 | 7 | 0 | wallstreetbets 8 | NYSE | #12 | [link](https://www.reddit.com/r/wallstreetbets/comments/1xxmkhj/comment/19sq72ymj9i2p/) |
| MSTR | 2026-11-13 06:20 | mention spike | 19 | 12.0 | 14 | 0 | wallstreetbets 19 | Nasdaq | #30 | [link](https://www.reddit.com/r/wallstreetbets/comments/1xxmkhj/comment/19sq2s7k2cjb5/) |
| COIN | 2026-11-15 21:05 | mention spike | 8 | 1.71 | 7 | 0 | wallstreetbets 8 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xxmkhj/comment/19sq7c5vprg05/) |

Full history: `episodes.csv` (one row per first flag, with the numbers known at that moment).
