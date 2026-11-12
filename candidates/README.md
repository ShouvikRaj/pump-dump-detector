# Stage 1 candidates

Updated 2026-11-12T08:41:23Z by run `43183841146`. A candidate is a ticker whose Reddit mentions (or hype-language
posts) in the last 24 hours jumped above its prior 7-day mean + 2 sd, with at least
10 mentions from 5 different authors. It stays listed until it goes
24 hours without a new flag. These are statistical flags, not accusations or advice.

| Ticker | Flagged since (UTC) | Why | Mentions 24h | Baseline/day | Authors | Hype posts | Subreddits | Exchange | StockTwits | Example |
|---|---|---|---|---|---|---|---|---|---|---|
| AMD | 2026-11-12 05:14 | mention spike | 386 | 145.71 | 288 | 2 | wallstreetbets 377, smallstreetbets 7, pennystocks 2 | Nasdaq | #6 | [link](https://www.reddit.com/r/pennystocks/comments/1xu7dbj/) |
| AVGO | 2026-11-09 15:56 | mention spike | 60 | 17.14 | 48 | 0 | wallstreetbets 59, smallstreetbets 1 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xttio6/comment/19siknjdk8w1w/) |
| GME | 2026-11-12 01:54 | mention spike | 21 | 9.71 | 18 | 1 | wallstreetbets 20, pennystocks 1 | NYSE |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xu1nxu/) |
| NBIS | 2026-11-11 12:32 | mention spike | 212 | 54.57 | 131 | 1 | wallstreetbets 209, smallstreetbets 3 | Nasdaq | #15 | [link](https://www.reddit.com/r/wallstreetbets/comments/1xu2e03/) |
| NVDA | 2026-11-09 00:16 | hype spike mention spike | 1705 | 557.29 | 976 | 3 | wallstreetbets 1674, smallstreetbets 30, pennystocks 1 | Nasdaq | #1 | [link](https://www.reddit.com/r/wallstreetbets/comments/1xu6uhn/) |
| NVDL | 2026-11-11 07:39 | mention spike | 15 | 3.14 | 12 | 0 | wallstreetbets 14, smallstreetbets 1 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xttio6/comment/19sien28rjxoh/) |
| NXXT | 2026-11-12 03:27 | mention spike | 17 | 0.0 | 16 | 1 | pennystocks 15, wallstreetbets 2 | Nasdaq |  | [link](https://www.reddit.com/r/pennystocks/comments/1xtysur/) |
| NYT | 2026-11-12 01:02 | mention spike | 66 | 4.43 | 54 | 0 | wallstreetbets 66 | NYSE |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xtvbiz/) |
| OUST | 2026-11-12 01:02 | mention spike | 11 | 0.14 | 11 | 0 | wallstreetbets 11 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xttio6/comment/19shvfoxgaudf/) |
| SLI | 2026-11-12 05:40 | mention spike | 12 | 0.43 | 11 | 0 | wallstreetbets 12 | NYSE American |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xtwcpr/) |
| ANT | 2026-11-10 14:52 | mention spike | 78 | 40.71 | 67 | 0 | wallstreetbets 76, pennystocks 1, smallstreetbets 1 | ? |  | [link](https://www.reddit.com/r/pennystocks/comments/1xty013/) |
| CRWV | 2026-11-10 20:00 | mention spike | 186 | 86.14 | 117 | 0 | wallstreetbets 184, smallstreetbets 2 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xtoxn0/) |
| RGTI | 2026-11-10 21:21 | mention spike | 2 | 5.0 | 2 | 0 | wallstreetbets 2 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xtexaq/comment/19sham8gm7kdg/) |
| GEV | 2026-11-10 15:44 | mention spike | 9 | 5.29 | 6 | 0 | wallstreetbets 9 | NYSE | #16 | [link](https://www.reddit.com/r/wallstreetbets/comments/1xtexaq/comment/19shiwgpl0cm8/) |
| MSFT | 2026-11-11 15:26 | mention spike | 72 | 57.57 | 56 | 0 | wallstreetbets 71, smallstreetbets 1 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xtpc8j/) |
| MSTR | 2026-11-10 19:20 | mention spike | 9 | 5.43 | 5 | 0 | wallstreetbets 9 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xtvna6/) |

Full history: `episodes.csv` (one row per first flag, with the numbers known at that moment).
