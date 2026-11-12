# Stage 1 candidates

Updated 2026-11-12T11:18:09Z by run `43207131939`. A candidate is a ticker whose Reddit mentions (or hype-language
posts) in the last 24 hours jumped above its prior 7-day mean + 2 sd, with at least
10 mentions from 5 different authors. It stays listed until it goes
24 hours without a new flag. These are statistical flags, not accusations or advice.

| Ticker | Flagged since (UTC) | Why | Mentions 24h | Baseline/day | Authors | Hype posts | Subreddits | Exchange | StockTwits | Example |
|---|---|---|---|---|---|---|---|---|---|---|
| AMD | 2026-11-12 05:14 | mention spike | 409 | 145.71 | 310 | 2 | wallstreetbets 400, smallstreetbets 7, pennystocks 2 | Nasdaq | #3 | [link](https://www.reddit.com/r/wallstreetbets/comments/1xu9rfx/) |
| AVGO | 2026-11-09 15:56 | mention spike | 62 | 17.29 | 50 | 0 | wallstreetbets 61, smallstreetbets 1 | Nasdaq | #11 | [link](https://www.reddit.com/r/wallstreetbets/comments/1xu60ht/comment/19siqybydmotg/) |
| GME | 2026-11-12 01:54 | mention spike | 21 | 9.71 | 18 | 1 | wallstreetbets 20, pennystocks 1 | NYSE |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xu1nxu/) |
| NBIS | 2026-11-11 12:32 | mention spike | 231 | 55.86 | 144 | 1 | wallstreetbets 228, smallstreetbets 3 | Nasdaq | #2 | [link](https://www.reddit.com/r/wallstreetbets/comments/1xu2e03/) |
| NVDA | 2026-11-09 00:16 | hype spike mention spike | 1767 | 564.43 | 1000 | 3 | wallstreetbets 1737, smallstreetbets 29, pennystocks 1 | Nasdaq | #1 | [link](https://www.reddit.com/r/wallstreetbets/comments/1xua015/) |
| NVDL | 2026-11-11 07:39 | mention spike | 15 | 3.14 | 12 | 0 | wallstreetbets 14, smallstreetbets 1 | Nasdaq | #14 | [link](https://www.reddit.com/r/wallstreetbets/comments/1xttio6/comment/19sien28rjxoh/) |
| NXXT | 2026-11-12 03:27 | mention spike | 17 | 0.0 | 16 | 1 | pennystocks 15, wallstreetbets 2 | Nasdaq |  | [link](https://www.reddit.com/r/pennystocks/comments/1xtysur/) |
| NYT | 2026-11-12 01:02 | mention spike | 71 | 4.43 | 56 | 0 | wallstreetbets 71 | NYSE |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xu7xyx/) |
| OUST | 2026-11-12 01:02 | mention spike | 11 | 0.14 | 11 | 0 | wallstreetbets 11 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xttio6/comment/19shvfoxgaudf/) |
| SLI | 2026-11-12 05:40 | mention spike | 14 | 0.43 | 13 | 0 | wallstreetbets 13, smallstreetbets 1 | NYSE American |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xtwcpr/) |
| ANT | 2026-11-10 14:52 | mention spike | 80 | 41.0 | 69 | 0 | wallstreetbets 78, pennystocks 1, smallstreetbets 1 | ? |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xu8yp4/) |
| CRWV | 2026-11-10 20:00 | mention spike | 174 | 88.14 | 109 | 0 | wallstreetbets 173, smallstreetbets 1 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xtoxn0/) |
| RGTI | 2026-11-10 21:21 | mention spike | 2 | 5.0 | 2 | 0 | wallstreetbets 2 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xtexaq/comment/19sham8gm7kdg/) |
| GEV | 2026-11-10 15:44 | mention spike | 6 | 5.57 | 4 | 0 | wallstreetbets 6 | NYSE |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xtexaq/comment/19shiwgpl0cm8/) |
| MSFT | 2026-11-11 15:26 | mention spike | 73 | 57.57 | 57 | 0 | wallstreetbets 72, smallstreetbets 1 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xtpc8j/) |
| MSTR | 2026-11-10 19:20 | mention spike | 9 | 5.29 | 5 | 0 | wallstreetbets 9 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xtvna6/) |

Full history: `episodes.csv` (one row per first flag, with the numbers known at that moment).
