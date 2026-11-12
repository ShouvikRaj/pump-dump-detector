# Stage 1 candidates

Updated 2026-11-12T12:12:07Z by run `43214773218`. A candidate is a ticker whose Reddit mentions (or hype-language
posts) in the last 24 hours jumped above its prior 7-day mean + 2 sd, with at least
10 mentions from 5 different authors. It stays listed until it goes
24 hours without a new flag. These are statistical flags, not accusations or advice.

| Ticker | Flagged since (UTC) | Why | Mentions 24h | Baseline/day | Authors | Hype posts | Subreddits | Exchange | StockTwits | Example |
|---|---|---|---|---|---|---|---|---|---|---|
| AMD | 2026-11-12 05:14 | mention spike | 413 | 145.29 | 318 | 2 | wallstreetbets 404, smallstreetbets 7, pennystocks 2 | Nasdaq | #6 | [link](https://www.reddit.com/r/wallstreetbets/comments/1xu9rfx/) |
| AVGO | 2026-11-09 15:56 | mention spike | 63 | 17.29 | 51 | 0 | wallstreetbets 62, smallstreetbets 1 | Nasdaq | #15 | [link](https://www.reddit.com/r/wallstreetbets/comments/1xtqcn7/comment/19siur0rxlecl/) |
| NBIS | 2026-11-11 12:32 | mention spike | 240 | 56.57 | 150 | 1 | wallstreetbets 237, smallstreetbets 3 | Nasdaq | #2 | [link](https://www.reddit.com/r/wallstreetbets/comments/1xu2e03/) |
| NVDA | 2026-11-09 00:16 | hype spike mention spike | 1790 | 568.29 | 1017 | 2 | wallstreetbets 1760, smallstreetbets 29, pennystocks 1 | Nasdaq | #1 | [link](https://www.reddit.com/r/wallstreetbets/comments/1xua9iu/) |
| NVDL | 2026-11-11 07:39 | mention spike | 15 | 3.14 | 12 | 0 | wallstreetbets 14, smallstreetbets 1 | Nasdaq | #28 | [link](https://www.reddit.com/r/wallstreetbets/comments/1xttio6/comment/19sien28rjxoh/) |
| NXXT | 2026-11-12 03:27 | mention spike | 16 | 0.14 | 15 | 1 | pennystocks 14, wallstreetbets 2 | Nasdaq |  | [link](https://www.reddit.com/r/pennystocks/comments/1xtysur/) |
| NYT | 2026-11-12 01:02 | mention spike | 72 | 4.43 | 56 | 0 | wallstreetbets 72 | NYSE |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xu7xyx/) |
| OUST | 2026-11-12 01:02 | mention spike | 11 | 0.14 | 11 | 0 | wallstreetbets 11 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xttio6/comment/19shvfoxgaudf/) |
| SLI | 2026-11-12 05:40 | mention spike | 14 | 0.43 | 13 | 0 | wallstreetbets 13, smallstreetbets 1 | NYSE American |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xtwcpr/) |
| GME | 2026-11-12 01:54 | mention spike | 20 | 9.86 | 17 | 1 | wallstreetbets 19, pennystocks 1 | NYSE |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xu1nxu/) |
| ANT | 2026-11-10 14:52 | mention spike | 77 | 41.43 | 67 | 0 | wallstreetbets 75, pennystocks 1, smallstreetbets 1 | ? |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xu8yp4/) |
| CRWV | 2026-11-10 20:00 | mention spike | 171 | 89.0 | 107 | 0 | wallstreetbets 170, smallstreetbets 1 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xtoxn0/) |
| RGTI | 2026-11-10 21:21 | mention spike | 2 | 5.0 | 2 | 0 | wallstreetbets 2 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xtexaq/comment/19sham8gm7kdg/) |
| GEV | 2026-11-10 15:44 | mention spike | 8 | 5.57 | 6 | 0 | wallstreetbets 8 | NYSE |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xu9wsm/comment/19siulzjvk6ao/) |
| MSFT | 2026-11-11 15:26 | mention spike | 75 | 57.43 | 58 | 0 | wallstreetbets 74, smallstreetbets 1 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xtpc8j/) |
| MSTR | 2026-11-10 19:20 | mention spike | 7 | 5.57 | 5 | 0 | wallstreetbets 7 | Nasdaq | #12 | [link](https://www.reddit.com/r/wallstreetbets/comments/1xtvna6/) |

Full history: `episodes.csv` (one row per first flag, with the numbers known at that moment).
