# Stage 1 candidates

Updated 2026-11-12T02:47:36Z by run `43142453102`. A candidate is a ticker whose Reddit mentions (or hype-language
posts) in the last 24 hours jumped above its prior 7-day mean + 2 sd, with at least
10 mentions from 5 different authors. It stays listed until it goes
24 hours without a new flag. These are statistical flags, not accusations or advice.

| Ticker | Flagged since (UTC) | Why | Mentions 24h | Baseline/day | Authors | Hype posts | Subreddits | Exchange | StockTwits | Example |
|---|---|---|---|---|---|---|---|---|---|---|
| AVGO | 2026-11-09 15:56 | mention spike | 56 | 17.14 | 44 | 0 | wallstreetbets 55, smallstreetbets 1 | Nasdaq | #19 | [link](https://www.reddit.com/r/wallstreetbets/comments/1xttio6/comment/19si4xish5ute/) |
| NBIS | 2026-11-11 12:32 | mention spike | 198 | 54.0 | 124 | 1 | wallstreetbets 195, smallstreetbets 3 | Nasdaq |  | [link](https://www.reddit.com/r/smallstreetbets/comments/1xtqx9q/) |
| NVDL | 2026-11-11 07:39 | mention spike | 15 | 3.0 | 12 | 0 | wallstreetbets 14, smallstreetbets 1 | Nasdaq | #3 | [link](https://www.reddit.com/r/wallstreetbets/comments/1xttio6/comment/19si53al9kmkj/) |
| NYT | 2026-11-12 01:02 | mention spike | 48 | 4.43 | 41 | 0 | wallstreetbets 48 | NYSE |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xtvbiz/) |
| OUST | 2026-11-12 01:02 | mention spike | 11 | 0.14 | 11 | 0 | wallstreetbets 11 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xttio6/comment/19shvfoxgaudf/) |
| GME | 2026-11-12 01:54 | mention spike | 17 | 9.71 | 14 | 1 | wallstreetbets 16, pennystocks 1 | NYSE |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xtqcn7/) |
| ANT | 2026-11-10 14:52 | mention spike | 85 | 40.0 | 67 | 0 | wallstreetbets 83, pennystocks 1, smallstreetbets 1 | ? |  | [link](https://www.reddit.com/r/pennystocks/comments/1xty013/) |
| CRWV | 2026-11-10 20:00 | mention spike | 209 | 81.86 | 133 | 1 | wallstreetbets 207, smallstreetbets 2 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xtoxn0/) |
| RGTI | 2026-11-10 21:21 | mention spike | 2 | 5.0 | 2 | 0 | wallstreetbets 2 | Nasdaq | #11 | [link](https://www.reddit.com/r/wallstreetbets/comments/1xtexaq/comment/19sham8gm7kdg/) |
| NVDA | 2026-11-09 00:16 | hype spike mention spike | 1431 | 544.14 | 825 | 3 | wallstreetbets 1413, smallstreetbets 18 | Nasdaq | #1 | [link](https://www.reddit.com/r/wallstreetbets/comments/1xu0xr6/) |
| GEV | 2026-11-10 15:44 | mention spike | 10 | 5.14 | 7 | 0 | wallstreetbets 10 | NYSE |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xtexaq/comment/19shiwgpl0cm8/) |
| MSFT | 2026-11-11 15:26 | mention spike | 70 | 57.14 | 54 | 0 | wallstreetbets 69, smallstreetbets 1 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xtpc8j/) |
| MSTR | 2026-11-10 19:20 | mention spike | 9 | 5.57 | 5 | 0 | wallstreetbets 9 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xtvna6/) |

Full history: `episodes.csv` (one row per first flag, with the numbers known at that moment).
