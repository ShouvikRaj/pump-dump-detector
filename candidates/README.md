# Stage 1 candidates

Updated 2026-11-12T01:54:37Z by run `43136321915`. A candidate is a ticker whose Reddit mentions (or hype-language
posts) in the last 24 hours jumped above its prior 7-day mean + 2 sd, with at least
10 mentions from 5 different authors. It stays listed until it goes
24 hours without a new flag. These are statistical flags, not accusations or advice.

| Ticker | Flagged since (UTC) | Why | Mentions 24h | Baseline/day | Authors | Hype posts | Subreddits | Exchange | StockTwits | Example |
|---|---|---|---|---|---|---|---|---|---|---|
| AVGO | 2026-11-09 15:56 | mention spike | 53 | 17.14 | 42 | 0 | wallstreetbets 52, smallstreetbets 1 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xttio6/comment/19si2e9hr1qo5/) |
| NBIS | 2026-11-11 12:32 | mention spike | 187 | 54.0 | 116 | 1 | wallstreetbets 185, smallstreetbets 2 | Nasdaq | #3 | [link](https://www.reddit.com/r/smallstreetbets/comments/1xtqx9q/) |
| NVDL | 2026-11-11 07:39 | mention spike | 14 | 2.86 | 12 | 0 | wallstreetbets 13, smallstreetbets 1 | Nasdaq | #4 | [link](https://www.reddit.com/r/wallstreetbets/comments/1xttio6/comment/19si2m9799s8z/) |
| NYT | 2026-11-12 01:02 | mention spike | 46 | 4.43 | 40 | 0 | wallstreetbets 46 | NYSE |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xtvbiz/) |
| OUST | 2026-11-12 01:02 | mention spike | 11 | 0.14 | 11 | 0 | wallstreetbets 11 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xttio6/comment/19shvfoxgaudf/) |
| GME | 2026-11-12 01:54 | mention spike | 17 | 9.71 | 14 | 1 | wallstreetbets 16, pennystocks 1 | NYSE |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xtqcn7/) |
| ANT | 2026-11-10 14:52 | mention spike | 83 | 39.29 | 68 | 0 | wallstreetbets 81, pennystocks 1, smallstreetbets 1 | ? |  | [link](https://www.reddit.com/r/pennystocks/comments/1xty013/) |
| CRWV | 2026-11-10 20:00 | mention spike | 215 | 80.43 | 135 | 1 | wallstreetbets 213, smallstreetbets 2 | Nasdaq | #26 | [link](https://www.reddit.com/r/wallstreetbets/comments/1xtoxn0/) |
| RGTI | 2026-11-10 21:21 | mention spike | 2 | 5.0 | 2 | 0 | wallstreetbets 2 | Nasdaq | #8 | [link](https://www.reddit.com/r/wallstreetbets/comments/1xtexaq/comment/19sham8gm7kdg/) |
| NVDA | 2026-11-09 00:16 | hype spike mention spike | 1365 | 541.0 | 791 | 3 | wallstreetbets 1351, smallstreetbets 14 | Nasdaq | #1 | [link](https://www.reddit.com/r/wallstreetbets/comments/1xtzy1i/) |
| GEV | 2026-11-10 15:44 | mention spike | 11 | 5.0 | 7 | 0 | wallstreetbets 11 | NYSE | #22 | [link](https://www.reddit.com/r/wallstreetbets/comments/1xtexaq/comment/19shiwgpl0cm8/) |
| MSFT | 2026-11-11 15:26 | mention spike | 69 | 57.14 | 53 | 0 | wallstreetbets 68, smallstreetbets 1 | Nasdaq | #29 | [link](https://www.reddit.com/r/wallstreetbets/comments/1xtpc8j/) |
| MSTR | 2026-11-10 19:20 | mention spike | 9 | 5.43 | 6 | 0 | wallstreetbets 9 | Nasdaq | #24 | [link](https://www.reddit.com/r/wallstreetbets/comments/1xtvna6/) |

Full history: `episodes.csv` (one row per first flag, with the numbers known at that moment).
