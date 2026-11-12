# Stage 1 candidates

Updated 2026-11-12T15:37:11Z by run `43247633076`. A candidate is a ticker whose Reddit mentions (or hype-language
posts) in the last 24 hours jumped above its prior 7-day mean + 2 sd, with at least
10 mentions from 5 different authors. It stays listed until it goes
24 hours without a new flag. These are statistical flags, not accusations or advice.

| Ticker | Flagged since (UTC) | Why | Mentions 24h | Baseline/day | Authors | Hype posts | Subreddits | Exchange | StockTwits | Example |
|---|---|---|---|---|---|---|---|---|---|---|
| AMD | 2026-11-12 05:14 | mention spike | 465 | 124.29 | 361 | 2 | wallstreetbets 456, smallstreetbets 7, pennystocks 2 | Nasdaq | #23 | [link](https://www.reddit.com/r/wallstreetbets/comments/1xuf1vc/) |
| AVGO | 2026-11-09 15:56 | mention spike | 65 | 18.29 | 50 | 0 | wallstreetbets 64, smallstreetbets 1 | Nasdaq | #13 | [link](https://www.reddit.com/r/wallstreetbets/comments/1xu9wsm/comment/19sj33jxl32e8/) |
| GME | 2026-11-12 01:54 | mention spike | 20 | 9.71 | 17 | 2 | wallstreetbets 18, pennystocks 2 | NYSE |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xu1nxu/) |
| LUNR | 2026-11-12 14:43 | mention spike | 15 | 5.43 | 12 | 0 | wallstreetbets 14, pennystocks 1 | Nasdaq | #5 | [link](https://www.reddit.com/r/wallstreetbets/comments/1xu9wsm/comment/19sj2n3jz7ie8/) |
| NBIS | 2026-11-11 12:32 | mention spike | 430 | 61.29 | 220 | 1 | wallstreetbets 425, smallstreetbets 5 | Nasdaq | #2 | [link](https://www.reddit.com/r/smallstreetbets/comments/1xuf16g/) |
| NVDA | 2026-11-09 00:16 | hype spike mention spike | 2125 | 589.57 | 1188 | 2 | wallstreetbets 2088, smallstreetbets 35, pennystocks 2 | Nasdaq | #1 | [link](https://www.reddit.com/r/wallstreetbets/comments/1xuf8dj/) |
| NVDL | 2026-11-11 07:39 | mention spike | 13 | 3.43 | 11 | 0 | wallstreetbets 12, smallstreetbets 1 | Nasdaq | #11 | [link](https://www.reddit.com/r/wallstreetbets/comments/1xttio6/comment/19sien28rjxoh/) |
| NXXT | 2026-11-12 03:27 | mention spike | 15 | 0.29 | 14 | 1 | pennystocks 13, wallstreetbets 2 | Nasdaq |  | [link](https://www.reddit.com/r/pennystocks/comments/1xtysur/) |
| NYT | 2026-11-12 01:02 | mention spike | 76 | 4.43 | 59 | 0 | wallstreetbets 76 | NYSE |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xuf1vc/) |
| OUST | 2026-11-12 01:02 | mention spike | 12 | 0.14 | 12 | 0 | wallstreetbets 12 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xuc70t/) |
| SLI | 2026-11-12 05:40 | mention spike | 16 | 0.43 | 15 | 0 | wallstreetbets 15, smallstreetbets 1 | NYSE American |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xtwcpr/) |
| ANT | 2026-11-10 14:52 | mention spike | 68 | 43.29 | 59 | 0 | wallstreetbets 66, pennystocks 1, smallstreetbets 1 | ? |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xuf1vc/) |
| CRWV | 2026-11-10 20:00 | mention spike | 135 | 94.86 | 94 | 0 | wallstreetbets 134, smallstreetbets 1 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xtoxn0/) |
| RGTI | 2026-11-10 21:21 | mention spike | 0 |  | 0 | 0 |  | Nasdaq |  |  |
| GEV | 2026-11-10 15:44 | mention spike | 3 | 5.71 | 3 | 0 | wallstreetbets 3 | NYSE |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xu9wsm/comment/19siulzjvk6ao/) |
| MSFT | 2026-11-11 15:26 | mention spike | 64 | 56.0 | 50 | 0 | wallstreetbets 63, smallstreetbets 1 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xtpc8j/) |

Full history: `episodes.csv` (one row per first flag, with the numbers known at that moment).
