# Stage 1 candidates

Updated 2026-11-12T02:34:18Z by run `43140880928`. A candidate is a ticker whose Reddit mentions (or hype-language
posts) in the last 24 hours jumped above its prior 7-day mean + 2 sd, with at least
10 mentions from 5 different authors. It stays listed until it goes
24 hours without a new flag. These are statistical flags, not accusations or advice.

| Ticker | Flagged since (UTC) | Why | Mentions 24h | Baseline/day | Authors | Hype posts | Subreddits | Exchange | StockTwits | Example |
|---|---|---|---|---|---|---|---|---|---|---|
| AVGO | 2026-11-09 15:56 | mention spike | 54 | 17.14 | 43 | 0 | wallstreetbets 53, smallstreetbets 1 | Nasdaq | #22 | [link](https://www.reddit.com/r/wallstreetbets/comments/1xttio6/comment/19si3lyo7e2px/) |
| NBIS | 2026-11-11 12:32 | mention spike | 193 | 54.0 | 121 | 1 | wallstreetbets 191, smallstreetbets 2 | Nasdaq | #10 | [link](https://www.reddit.com/r/smallstreetbets/comments/1xtqx9q/) |
| NVDL | 2026-11-11 07:39 | mention spike | 13 | 3.0 | 11 | 0 | wallstreetbets 12, smallstreetbets 1 | Nasdaq | #3 | [link](https://www.reddit.com/r/wallstreetbets/comments/1xttio6/comment/19si2m9799s8z/) |
| NYT | 2026-11-12 01:02 | mention spike | 48 | 4.43 | 41 | 0 | wallstreetbets 48 | NYSE |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xtvbiz/) |
| OUST | 2026-11-12 01:02 | mention spike | 11 | 0.14 | 11 | 0 | wallstreetbets 11 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xttio6/comment/19shvfoxgaudf/) |
| GME | 2026-11-12 01:54 | mention spike | 17 | 9.71 | 14 | 1 | wallstreetbets 16, pennystocks 1 | NYSE |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xtqcn7/) |
| ANT | 2026-11-10 14:52 | mention spike | 83 | 39.86 | 66 | 0 | wallstreetbets 81, pennystocks 1, smallstreetbets 1 | ? |  | [link](https://www.reddit.com/r/pennystocks/comments/1xty013/) |
| CRWV | 2026-11-10 20:00 | mention spike | 214 | 81.0 | 136 | 1 | wallstreetbets 212, smallstreetbets 2 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xtoxn0/) |
| RGTI | 2026-11-10 21:21 | mention spike | 2 | 5.0 | 2 | 0 | wallstreetbets 2 | Nasdaq | #16 | [link](https://www.reddit.com/r/wallstreetbets/comments/1xtexaq/comment/19sham8gm7kdg/) |
| NVDA | 2026-11-09 00:16 | hype spike mention spike | 1408 | 543.71 | 816 | 3 | wallstreetbets 1392, smallstreetbets 16 | Nasdaq | #1 | [link](https://www.reddit.com/r/smallstreetbets/comments/1xu0fw1/) |
| GEV | 2026-11-10 15:44 | mention spike | 10 | 5.14 | 7 | 0 | wallstreetbets 10 | NYSE |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xtexaq/comment/19shiwgpl0cm8/) |
| MSFT | 2026-11-11 15:26 | mention spike | 70 | 57.14 | 54 | 0 | wallstreetbets 69, smallstreetbets 1 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xtpc8j/) |
| MSTR | 2026-11-10 19:20 | mention spike | 10 | 5.43 | 6 | 0 | wallstreetbets 10 | Nasdaq | #29 | [link](https://www.reddit.com/r/wallstreetbets/comments/1xtvna6/) |

Full history: `episodes.csv` (one row per first flag, with the numbers known at that moment).
