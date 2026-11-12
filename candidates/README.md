# Stage 1 candidates

Updated 2026-11-12T16:56:10Z by run `43262115258`. A candidate is a ticker whose Reddit mentions (or hype-language
posts) in the last 24 hours jumped above its prior 7-day mean + 2 sd, with at least
10 mentions from 5 different authors. It stays listed until it goes
24 hours without a new flag. These are statistical flags, not accusations or advice.

| Ticker | Flagged since (UTC) | Why | Mentions 24h | Baseline/day | Authors | Hype posts | Subreddits | Exchange | StockTwits | Example |
|---|---|---|---|---|---|---|---|---|---|---|
| AMD | 2026-11-12 05:14 | mention spike | 507 | 121.86 | 392 | 1 | wallstreetbets 496, smallstreetbets 9, pennystocks 2 | Nasdaq | #5 | [link](https://www.reddit.com/r/wallstreetbets/comments/1xuho8m/) |
| AVGO | 2026-11-09 15:56 | mention spike | 65 | 18.57 | 52 | 0 | wallstreetbets 64, smallstreetbets 1 | Nasdaq | #27 | [link](https://www.reddit.com/r/wallstreetbets/comments/1xu9wsm/comment/19sj71hok33ds/) |
| GME | 2026-11-12 01:54 | mention spike | 19 | 9.71 | 16 | 1 | wallstreetbets 17, pennystocks 2 | NYSE |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xu1nxu/) |
| LUNR | 2026-11-12 14:43 | mention spike | 16 | 5.57 | 11 | 0 | wallstreetbets 15, pennystocks 1 | Nasdaq | #4 | [link](https://www.reddit.com/r/wallstreetbets/comments/1xu9wsm/comment/19sj5uj3zb0th/) |
| NBIS | 2026-11-11 12:32 | mention spike | 430 | 62.57 | 224 | 1 | wallstreetbets 425, smallstreetbets 5 | Nasdaq | #3 | [link](https://www.reddit.com/r/smallstreetbets/comments/1xuf16g/) |
| NVDA | 2026-11-09 00:16 | hype spike mention spike | 2271 | 595.86 | 1256 | 1 | wallstreetbets 2233, smallstreetbets 36, pennystocks 2 | Nasdaq | #1 | [link](https://www.reddit.com/r/wallstreetbets/comments/1xuhr5t/) |
| NVDL | 2026-11-11 07:39 | mention spike | 14 | 3.29 | 11 | 0 | wallstreetbets 13, smallstreetbets 1 | Nasdaq | #16 | [link](https://www.reddit.com/r/wallstreetbets/comments/1xu9wsm/comment/19sj4wtquo2cj/) |
| NXXT | 2026-11-12 03:27 | mention spike | 14 | 0.43 | 13 | 1 | pennystocks 12, wallstreetbets 2 | Nasdaq |  | [link](https://www.reddit.com/r/pennystocks/comments/1xtysur/) |
| NYT | 2026-11-12 01:02 | mention spike | 77 | 4.43 | 60 | 0 | wallstreetbets 77 | NYSE |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xuf1vc/) |
| OUST | 2026-11-12 01:02 | mention spike | 12 | 0.14 | 12 | 0 | wallstreetbets 12 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xuc70t/) |
| PLCE | 2026-11-12 16:04 | mention spike | 12 | 0.57 | 10 | 0 | pennystocks 8, wallstreetbets 4 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xuhtjg/) |
| SLI | 2026-11-12 05:40 | mention spike | 16 | 0.43 | 15 | 0 | wallstreetbets 15, smallstreetbets 1 | NYSE American |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xtwcpr/) |
| CBRS | 2026-11-12 16:56 | mention spike | 11 | 4.0 | 7 | 0 | wallstreetbets 11 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xpjj4e/comment/19sj7c7qym2jk/) |
| ANT | 2026-11-10 14:52 | mention spike | 56 | 44.57 | 49 | 0 | wallstreetbets 54, pennystocks 1, smallstreetbets 1 | ? |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xuf1vc/) |
| CRWV | 2026-11-10 20:00 | mention spike | 119 | 96.57 | 83 | 0 | wallstreetbets 118, smallstreetbets 1 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xtoxn0/) |
| RGTI | 2026-11-10 21:21 | mention spike | 1 | 5.29 | 1 | 0 | wallstreetbets 1 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xu9wsm/comment/19sj4s1x740rk/) |
| GEV | 2026-11-10 15:44 | mention spike | 3 | 5.43 | 3 | 0 | wallstreetbets 3 | NYSE |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xu9wsm/comment/19siulzjvk6ao/) |
| MSFT | 2026-11-11 15:26 | mention spike | 48 | 56.86 | 40 | 0 | wallstreetbets 47, smallstreetbets 1 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xtpc8j/) |

Full history: `episodes.csv` (one row per first flag, with the numbers known at that moment).
