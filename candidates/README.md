# Stage 1 candidates

Updated 2026-11-16T17:30:07Z by run `43917702837`. A candidate is a ticker whose Reddit mentions (or hype-language
posts) in the last 24 hours jumped above its prior 7-day mean + 2 sd, with at least
10 mentions from 5 different authors. It stays listed until it goes
24 hours without a new flag. These are statistical flags, not accusations or advice.

| Ticker | Flagged since (UTC) | Why | Mentions 24h | Baseline/day | Authors | Hype posts | Subreddits | Exchange | StockTwits | Example |
|---|---|---|---|---|---|---|---|---|---|---|
| ANT | 2026-11-16 16:34 | mention spike | 146 | 67.71 | 102 | 1 | wallstreetbets 143, smallstreetbets 2, pennystocks 1 | ? |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xxfkdl/) |
| HOOD | 2026-11-16 15:08 | mention spike | 13 | 3.86 | 13 | 0 | wallstreetbets 13 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xxmkhj/comment/19sqdq7xgziyo/) |
| WMT | 2026-11-16 07:17 | mention spike | 19 | 3.86 | 15 | 0 | wallstreetbets 19 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xxmkhj/comment/19sqd615w0req/) |
| ASML | 2026-11-15 23:05 | mention spike | 2 | 8.0 | 2 | 0 | wallstreetbets 2 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xwa164/comment/19sp0fwp4wjl0/) |
| DXYZ | 2026-11-14 23:53 | mention spike | 12 | 6.0 | 9 | 0 | wallstreetbets 12 | NYSE |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xxmkhj/comment/19sqdvqcmde4l/) |
| MSTR | 2026-11-13 06:20 | mention spike | 24 | 12.0 | 17 | 0 | wallstreetbets 24 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xxmkhj/comment/19sqcyhjmi2f9/) |
| COIN | 2026-11-15 21:05 | mention spike | 8 | 2.0 | 7 | 0 | wallstreetbets 8 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xxmkhj/comment/19sqd28qleuh0/) |

Full history: `episodes.csv` (one row per first flag, with the numbers known at that moment).
