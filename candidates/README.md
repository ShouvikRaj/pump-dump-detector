# Stage 1 candidates

Updated 2026-11-12T06:07:22Z by run `43164410955`. A candidate is a ticker whose Reddit mentions (or hype-language
posts) in the last 24 hours jumped above its prior 7-day mean + 2 sd, with at least
10 mentions from 5 different authors. It stays listed until it goes
24 hours without a new flag. These are statistical flags, not accusations or advice.

| Ticker | Flagged since (UTC) | Why | Mentions 24h | Baseline/day | Authors | Hype posts | Subreddits | Exchange | StockTwits | Example |
|---|---|---|---|---|---|---|---|---|---|---|
| AMD | 2026-11-12 05:14 | mention spike | 358 | 146.0 | 271 | 2 | wallstreetbets 351, smallstreetbets 7 | Nasdaq | #6 | [link](https://www.reddit.com/r/wallstreetbets/comments/1xu2e03/) |
| AVGO | 2026-11-09 15:56 | mention spike | 62 | 17.0 | 51 | 0 | wallstreetbets 61, smallstreetbets 1 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xttio6/comment/19sidvr13v70i/) |
| GME | 2026-11-12 01:54 | mention spike | 21 | 9.57 | 18 | 1 | wallstreetbets 20, pennystocks 1 | NYSE |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xu1nxu/) |
| NBIS | 2026-11-11 12:32 | mention spike | 209 | 54.0 | 128 | 1 | wallstreetbets 206, smallstreetbets 3 | Nasdaq | #11 | [link](https://www.reddit.com/r/wallstreetbets/comments/1xu2e03/) |
| NVDA | 2026-11-09 00:16 | hype spike mention spike | 1599 | 553.43 | 918 | 4 | wallstreetbets 1571, smallstreetbets 28 | Nasdaq | #1 | [link](https://www.reddit.com/r/wallstreetbets/comments/1xu4e2l/) |
| NVDL | 2026-11-11 07:39 | mention spike | 15 | 3.0 | 12 | 0 | wallstreetbets 14, smallstreetbets 1 | Nasdaq | #8 | [link](https://www.reddit.com/r/wallstreetbets/comments/1xttio6/comment/19si53al9kmkj/) |
| NXXT | 2026-11-12 03:27 | mention spike | 10 | 0.0 | 10 | 1 | pennystocks 8, wallstreetbets 2 | Nasdaq |  | [link](https://www.reddit.com/r/pennystocks/comments/1xtysur/) |
| NYT | 2026-11-12 01:02 | mention spike | 60 | 4.43 | 51 | 0 | wallstreetbets 60 | NYSE |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xtvbiz/) |
| OUST | 2026-11-12 01:02 | mention spike | 11 | 0.14 | 11 | 0 | wallstreetbets 11 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xttio6/comment/19shvfoxgaudf/) |
| SLI | 2026-11-12 05:40 | mention spike | 11 | 0.43 | 10 | 0 | wallstreetbets 11 | NYSE American |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xtwcpr/) |
| ANT | 2026-11-10 14:52 | mention spike | 76 | 41.0 | 65 | 0 | wallstreetbets 74, pennystocks 1, smallstreetbets 1 | ? |  | [link](https://www.reddit.com/r/pennystocks/comments/1xty013/) |
| CRWV | 2026-11-10 20:00 | mention spike | 190 | 85.43 | 120 | 0 | wallstreetbets 188, smallstreetbets 2 | Nasdaq | #12 | [link](https://www.reddit.com/r/wallstreetbets/comments/1xtoxn0/) |
| RGTI | 2026-11-10 21:21 | mention spike | 2 | 5.0 | 2 | 0 | wallstreetbets 2 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xtexaq/comment/19sham8gm7kdg/) |
| GEV | 2026-11-10 15:44 | mention spike | 9 | 5.29 | 6 | 0 | wallstreetbets 9 | NYSE |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xtexaq/comment/19shiwgpl0cm8/) |
| MSFT | 2026-11-11 15:26 | mention spike | 73 | 57.14 | 57 | 0 | wallstreetbets 72, smallstreetbets 1 | Nasdaq | #15 | [link](https://www.reddit.com/r/wallstreetbets/comments/1xtpc8j/) |
| MSTR | 2026-11-10 19:20 | mention spike | 9 | 5.57 | 5 | 0 | wallstreetbets 9 | Nasdaq | #2 | [link](https://www.reddit.com/r/wallstreetbets/comments/1xtvna6/) |

Full history: `episodes.csv` (one row per first flag, with the numbers known at that moment).
