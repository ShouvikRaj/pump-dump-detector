# Stage 1 candidates

Updated 2026-11-12T01:02:24Z by run `43130187483`. A candidate is a ticker whose Reddit mentions (or hype-language
posts) in the last 24 hours jumped above its prior 7-day mean + 2 sd, with at least
10 mentions from 5 different authors. It stays listed until it goes
24 hours without a new flag. These are statistical flags, not accusations or advice.

| Ticker | Flagged since (UTC) | Why | Mentions 24h | Baseline/day | Authors | Hype posts | Subreddits | Exchange | StockTwits | Example |
|---|---|---|---|---|---|---|---|---|---|---|
| AVGO | 2026-11-09 15:56 | mention spike | 54 | 16.71 | 41 | 0 | wallstreetbets 53, smallstreetbets 1 | Nasdaq | #10 | [link](https://www.reddit.com/r/wallstreetbets/comments/1xtv0ox/comment/19shwlumaur6o/) |
| NBIS | 2026-11-11 12:32 | mention spike | 189 | 53.14 | 119 | 1 | wallstreetbets 187, smallstreetbets 2 | Nasdaq | #3 | [link](https://www.reddit.com/r/smallstreetbets/comments/1xtqx9q/) |
| NVDL | 2026-11-11 07:39 | mention spike | 13 | 2.71 | 11 | 0 | wallstreetbets 12, smallstreetbets 1 | Nasdaq | #6 | [link](https://www.reddit.com/r/wallstreetbets/comments/1xttio6/comment/19si0u17m37t1/) |
| NYT | 2026-11-12 01:02 | mention spike | 32 | 4.43 | 28 | 0 | wallstreetbets 32 | NYSE |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xtvbiz/) |
| OUST | 2026-11-12 01:02 | mention spike | 11 | 0.14 | 11 | 0 | wallstreetbets 11 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xttio6/comment/19shvfoxgaudf/) |
| ANT | 2026-11-10 14:52 | mention spike | 95 | 38.0 | 77 | 0 | wallstreetbets 93, pennystocks 1, smallstreetbets 1 | ? |  | [link](https://www.reddit.com/r/pennystocks/comments/1xty013/) |
| CRWV | 2026-11-10 20:00 | mention spike | 229 | 78.43 | 146 | 1 | wallstreetbets 227, smallstreetbets 2 | Nasdaq | #4 | [link](https://www.reddit.com/r/wallstreetbets/comments/1xtoxn0/) |
| RGTI | 2026-11-10 21:21 | mention spike | 2 | 5.0 | 2 | 0 | wallstreetbets 2 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xtexaq/comment/19sham8gm7kdg/) |
| NVDA | 2026-11-09 00:16 | hype spike mention spike | 1286 | 534.0 | 728 | 3 | wallstreetbets 1276, smallstreetbets 10 | Nasdaq | #1 | [link](https://www.reddit.com/r/wallstreetbets/comments/1xtywoo/) |
| GEV | 2026-11-10 15:44 | mention spike | 12 | 4.86 | 7 | 0 | wallstreetbets 12 | NYSE |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xtexaq/comment/19shiwgpl0cm8/) |
| MSFT | 2026-11-11 15:26 | mention spike | 69 | 57.14 | 54 | 0 | wallstreetbets 68, smallstreetbets 1 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xtpc8j/) |
| MSTR | 2026-11-10 19:20 | mention spike | 9 | 5.43 | 6 | 0 | wallstreetbets 9 | Nasdaq | #28 | [link](https://www.reddit.com/r/wallstreetbets/comments/1xtvna6/) |

Full history: `episodes.csv` (one row per first flag, with the numbers known at that moment).
