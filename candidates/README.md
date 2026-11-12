# Stage 1 candidates

Updated 2026-11-12T17:47:08Z by run `43271589346`. A candidate is a ticker whose Reddit mentions (or hype-language
posts) in the last 24 hours jumped above its prior 7-day mean + 2 sd, with at least
10 mentions from 5 different authors. It stays listed until it goes
24 hours without a new flag. These are statistical flags, not accusations or advice.

| Ticker | Flagged since (UTC) | Why | Mentions 24h | Baseline/day | Authors | Hype posts | Subreddits | Exchange | StockTwits | Example |
|---|---|---|---|---|---|---|---|---|---|---|
| AMD | 2026-11-12 05:14 | mention spike | 523 | 121.86 | 404 | 1 | wallstreetbets 512, smallstreetbets 9, pennystocks 2 | Nasdaq | #5 | [link](https://www.reddit.com/r/wallstreetbets/comments/1xuho8m/) |
| AVGO | 2026-11-09 15:56 | mention spike | 63 | 19.14 | 51 | 0 | wallstreetbets 63 | Nasdaq | #25 | [link](https://www.reddit.com/r/wallstreetbets/comments/1xu9wsm/comment/19sj913r551ia/) |
| CBRS | 2026-11-12 16:56 | mention spike | 12 | 4.14 | 8 | 0 | wallstreetbets 12 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xu9wsm/comment/19sj81eztq8rn/) |
| GME | 2026-11-12 01:54 | mention spike | 19 | 9.71 | 16 | 1 | wallstreetbets 17, pennystocks 2 | NYSE |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xu1nxu/) |
| LUNR | 2026-11-12 14:43 | mention spike | 16 | 5.43 | 11 | 0 | wallstreetbets 15, pennystocks 1 | Nasdaq | #6 | [link](https://www.reddit.com/r/wallstreetbets/comments/1xu9wsm/comment/19sj5uj3zb0th/) |
| NBIS | 2026-11-11 12:32 | mention spike | 429 | 63.86 | 221 | 1 | wallstreetbets 425, smallstreetbets 4 | Nasdaq | #3 | [link](https://www.reddit.com/r/smallstreetbets/comments/1xuf16g/) |
| NVDA | 2026-11-09 00:16 | hype spike mention spike | 2303 | 600.29 | 1278 | 1 | wallstreetbets 2264, smallstreetbets 37, pennystocks 2 | Nasdaq | #2 | [link](https://www.reddit.com/r/smallstreetbets/comments/1xuikke/) |
| NVDL | 2026-11-11 07:39 | mention spike | 13 | 3.43 | 10 | 0 | wallstreetbets 12, smallstreetbets 1 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xu9wsm/comment/19sj4wtquo2cj/) |
| NXXT | 2026-11-12 03:27 | mention spike | 13 | 0.71 | 12 | 1 | pennystocks 11, wallstreetbets 2 | Nasdaq |  | [link](https://www.reddit.com/r/pennystocks/comments/1xtysur/) |
| NYT | 2026-11-12 01:02 | mention spike | 77 | 4.43 | 60 | 0 | wallstreetbets 77 | NYSE |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xuf1vc/) |
| OUST | 2026-11-12 01:02 | mention spike | 12 | 0.14 | 12 | 0 | wallstreetbets 12 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xuc70t/) |
| PARA | 2026-11-12 17:04 | mention spike | 10 | 0.57 | 7 | 0 | pennystocks 10 | Nasdaq |  | [link](https://www.reddit.com/r/pennystocks/comments/1xu7anw/) |
| PLCE | 2026-11-12 16:04 | mention spike | 14 | 0.57 | 11 | 0 | pennystocks 10, wallstreetbets 4 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xuhtjg/) |
| SLI | 2026-11-12 05:40 | mention spike | 16 | 0.43 | 15 | 0 | wallstreetbets 15, smallstreetbets 1 | NYSE American |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xtwcpr/) |
| TRT | 2026-11-12 17:34 | mention spike | 10 | 0.57 | 6 | 0 | wallstreetbets 10 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xu9wsm/comment/19sj8mddviq5e/) |
| SMCI | 2026-11-12 17:47 | mention spike | 43 | 14.86 | 30 | 0 | wallstreetbets 43 | Nasdaq | #1 | [link](https://www.reddit.com/r/wallstreetbets/comments/1xu9wsm/comment/19sj9oaxi7k69/) |
| ANT | 2026-11-10 14:52 | mention spike | 54 | 45.14 | 47 | 0 | wallstreetbets 52, pennystocks 1, smallstreetbets 1 | ? |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xuf1vc/) |
| CRWV | 2026-11-10 20:00 | mention spike | 105 | 98.86 | 74 | 0 | wallstreetbets 105 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xtoxn0/) |
| RGTI | 2026-11-10 21:21 | mention spike | 1 | 5.29 | 1 | 0 | wallstreetbets 1 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xu9wsm/comment/19sj4s1x740rk/) |
| GEV | 2026-11-10 15:44 | mention spike | 3 | 5.43 | 3 | 0 | wallstreetbets 3 | NYSE |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xu9wsm/comment/19siulzjvk6ao/) |

Full history: `episodes.csv` (one row per first flag, with the numbers known at that moment).
