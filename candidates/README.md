# Stage 1 candidates

Updated 2026-11-12T05:14:33Z by run `43158509081`. A candidate is a ticker whose Reddit mentions (or hype-language
posts) in the last 24 hours jumped above its prior 7-day mean + 2 sd, with at least
10 mentions from 5 different authors. It stays listed until it goes
24 hours without a new flag. These are statistical flags, not accusations or advice.

| Ticker | Flagged since (UTC) | Why | Mentions 24h | Baseline/day | Authors | Hype posts | Subreddits | Exchange | StockTwits | Example |
|---|---|---|---|---|---|---|---|---|---|---|
| AVGO | 2026-11-09 15:56 | mention spike | 57 | 17.0 | 47 | 0 | wallstreetbets 56, smallstreetbets 1 | Nasdaq | #23 | [link](https://www.reddit.com/r/wallstreetbets/comments/1xu1hjy/comment/19siboqvyo7s1/) |
| GME | 2026-11-12 01:54 | mention spike | 20 | 9.57 | 17 | 1 | wallstreetbets 19, pennystocks 1 | NYSE |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xu1nxu/) |
| NBIS | 2026-11-11 12:32 | mention spike | 205 | 54.0 | 125 | 1 | wallstreetbets 202, smallstreetbets 3 | Nasdaq | #15 | [link](https://www.reddit.com/r/wallstreetbets/comments/1xu2e03/) |
| NVDA | 2026-11-09 00:16 | hype spike mention spike | 1563 | 551.29 | 912 | 4 | wallstreetbets 1535, smallstreetbets 28 | Nasdaq | #1 | [link](https://www.reddit.com/r/wallstreetbets/comments/1xu2n60/) |
| NVDL | 2026-11-11 07:39 | mention spike | 15 | 3.0 | 12 | 0 | wallstreetbets 14, smallstreetbets 1 | Nasdaq | #4 | [link](https://www.reddit.com/r/wallstreetbets/comments/1xttio6/comment/19si53al9kmkj/) |
| NXXT | 2026-11-12 03:27 | mention spike | 10 | 0.0 | 10 | 1 | pennystocks 8, wallstreetbets 2 | Nasdaq |  | [link](https://www.reddit.com/r/pennystocks/comments/1xtysur/) |
| NYT | 2026-11-12 01:02 | mention spike | 58 | 4.43 | 49 | 0 | wallstreetbets 58 | NYSE |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xtvbiz/) |
| OUST | 2026-11-12 01:02 | mention spike | 11 | 0.14 | 11 | 0 | wallstreetbets 11 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xttio6/comment/19shvfoxgaudf/) |
| AMD | 2026-11-12 05:14 | mention spike | 343 | 145.71 | 261 | 2 | wallstreetbets 336, smallstreetbets 7 | Nasdaq | #9 | [link](https://www.reddit.com/r/wallstreetbets/comments/1xu2e03/) |
| ANT | 2026-11-10 14:52 | mention spike | 75 | 41.0 | 64 | 0 | wallstreetbets 73, pennystocks 1, smallstreetbets 1 | ? |  | [link](https://www.reddit.com/r/pennystocks/comments/1xty013/) |
| CRWV | 2026-11-10 20:00 | mention spike | 188 | 85.14 | 121 | 0 | wallstreetbets 186, smallstreetbets 2 | Nasdaq | #20 | [link](https://www.reddit.com/r/wallstreetbets/comments/1xtoxn0/) |
| RGTI | 2026-11-10 21:21 | mention spike | 2 | 5.0 | 2 | 0 | wallstreetbets 2 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xtexaq/comment/19sham8gm7kdg/) |
| GEV | 2026-11-10 15:44 | mention spike | 10 | 5.14 | 7 | 0 | wallstreetbets 10 | NYSE |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xtexaq/comment/19shiwgpl0cm8/) |
| MSFT | 2026-11-11 15:26 | mention spike | 72 | 57.29 | 57 | 0 | wallstreetbets 71, smallstreetbets 1 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xtpc8j/) |
| MSTR | 2026-11-10 19:20 | mention spike | 9 | 5.57 | 5 | 0 | wallstreetbets 9 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xtvna6/) |

Full history: `episodes.csv` (one row per first flag, with the numbers known at that moment).
