# Stage 1 candidates

Updated 2026-11-12T08:16:52Z by run `43180245175`. A candidate is a ticker whose Reddit mentions (or hype-language
posts) in the last 24 hours jumped above its prior 7-day mean + 2 sd, with at least
10 mentions from 5 different authors. It stays listed until it goes
24 hours without a new flag. These are statistical flags, not accusations or advice.

| Ticker | Flagged since (UTC) | Why | Mentions 24h | Baseline/day | Authors | Hype posts | Subreddits | Exchange | StockTwits | Example |
|---|---|---|---|---|---|---|---|---|---|---|
| AMD | 2026-11-12 05:14 | mention spike | 385 | 145.71 | 287 | 2 | wallstreetbets 377, smallstreetbets 7, pennystocks 1 | Nasdaq | #10 | [link](https://www.reddit.com/r/wallstreetbets/comments/1xu2e03/) |
| AVGO | 2026-11-09 15:56 | mention spike | 59 | 17.29 | 48 | 0 | wallstreetbets 58, smallstreetbets 1 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xttio6/comment/19sidvr13v70i/) |
| GME | 2026-11-12 01:54 | mention spike | 22 | 9.57 | 19 | 1 | wallstreetbets 21, pennystocks 1 | NYSE |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xu1nxu/) |
| NBIS | 2026-11-11 12:32 | mention spike | 211 | 54.43 | 130 | 1 | wallstreetbets 208, smallstreetbets 3 | Nasdaq | #30 | [link](https://www.reddit.com/r/wallstreetbets/comments/1xu2e03/) |
| NVDA | 2026-11-09 00:16 | hype spike mention spike | 1697 | 556.43 | 971 | 4 | wallstreetbets 1666, smallstreetbets 30, pennystocks 1 | Nasdaq | #1 | [link](https://www.reddit.com/r/wallstreetbets/comments/1xu6uhn/) |
| NVDL | 2026-11-11 07:39 | mention spike | 15 | 3.14 | 12 | 0 | wallstreetbets 14, smallstreetbets 1 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xttio6/comment/19sien28rjxoh/) |
| NXXT | 2026-11-12 03:27 | mention spike | 17 | 0.0 | 16 | 1 | pennystocks 15, wallstreetbets 2 | Nasdaq |  | [link](https://www.reddit.com/r/pennystocks/comments/1xtysur/) |
| NYT | 2026-11-12 01:02 | mention spike | 66 | 4.43 | 54 | 0 | wallstreetbets 66 | NYSE |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xtvbiz/) |
| OUST | 2026-11-12 01:02 | mention spike | 11 | 0.14 | 11 | 0 | wallstreetbets 11 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xttio6/comment/19shvfoxgaudf/) |
| SLI | 2026-11-12 05:40 | mention spike | 12 | 0.43 | 11 | 0 | wallstreetbets 12 | NYSE American |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xtwcpr/) |
| ANT | 2026-11-10 14:52 | mention spike | 77 | 40.71 | 66 | 0 | wallstreetbets 75, pennystocks 1, smallstreetbets 1 | ? |  | [link](https://www.reddit.com/r/pennystocks/comments/1xty013/) |
| CRWV | 2026-11-10 20:00 | mention spike | 190 | 85.57 | 120 | 0 | wallstreetbets 188, smallstreetbets 2 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xtoxn0/) |
| RGTI | 2026-11-10 21:21 | mention spike | 2 | 5.0 | 2 | 0 | wallstreetbets 2 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xtexaq/comment/19sham8gm7kdg/) |
| GEV | 2026-11-10 15:44 | mention spike | 9 | 5.29 | 6 | 0 | wallstreetbets 9 | NYSE | #7 | [link](https://www.reddit.com/r/wallstreetbets/comments/1xtexaq/comment/19shiwgpl0cm8/) |
| MSFT | 2026-11-11 15:26 | mention spike | 72 | 57.57 | 56 | 0 | wallstreetbets 71, smallstreetbets 1 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xtpc8j/) |
| MSTR | 2026-11-10 19:20 | mention spike | 9 | 5.57 | 5 | 0 | wallstreetbets 9 | Nasdaq | #11 | [link](https://www.reddit.com/r/wallstreetbets/comments/1xtvna6/) |

Full history: `episodes.csv` (one row per first flag, with the numbers known at that moment).
