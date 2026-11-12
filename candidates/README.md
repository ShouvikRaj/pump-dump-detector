# Stage 1 candidates

Updated 2026-11-12T21:09:12Z by run `43305434597`. A candidate is a ticker whose Reddit mentions (or hype-language
posts) in the last 24 hours jumped above its prior 7-day mean + 2 sd, with at least
10 mentions from 5 different authors. It stays listed until it goes
24 hours without a new flag. These are statistical flags, not accusations or advice.

| Ticker | Flagged since (UTC) | Why | Mentions 24h | Baseline/day | Authors | Hype posts | Subreddits | Exchange | StockTwits | Example |
|---|---|---|---|---|---|---|---|---|---|---|
| AMAT | 2026-11-12 18:42 | mention spike | 22 | 2.71 | 18 | 0 | wallstreetbets 22 | Nasdaq | #7 | [link](https://www.reddit.com/r/wallstreetbets/comments/1xu9wsm/comment/19sji6ezay8ys/) |
| AMD | 2026-11-12 05:14 | mention spike | 559 | 121.57 | 427 | 2 | wallstreetbets 549, smallstreetbets 8, pennystocks 2 | Nasdaq | #21 | [link](https://www.reddit.com/r/wallstreetbets/comments/1xumy47/) |
| ASML | 2026-11-12 20:43 | mention spike | 10 | 3.71 | 9 | 0 | wallstreetbets 10 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xudez8/comment/19sjh4mfzo08y/) |
| AVGO | 2026-11-09 15:56 | mention spike | 66 | 18.86 | 54 | 0 | wallstreetbets 66 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xuk703/) |
| CBRS | 2026-11-12 16:56 | mention spike | 24 | 3.57 | 19 | 0 | wallstreetbets 24 | Nasdaq | #6 | [link](https://www.reddit.com/r/wallstreetbets/comments/1xu9wsm/comment/19sji8x15x6g4/) |
| GLD | 2026-11-12 18:15 | mention spike | 17 | 7.43 | 10 | 0 | wallstreetbets 17 | NYSE Arca |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xu9wsm/comment/19sjidfr61p7k/) |
| LUNR | 2026-11-12 14:43 | mention spike | 15 | 5.57 | 12 | 0 | wallstreetbets 14, pennystocks 1 | Nasdaq | #9 | [link](https://www.reddit.com/r/wallstreetbets/comments/1xu9wsm/comment/19sjgnaidheck/) |
| MSFT | 2026-11-12 20:54 | mention spike | 120 | 53.86 | 87 | 0 | wallstreetbets 119, smallstreetbets 1 | Nasdaq | #15 | [link](https://www.reddit.com/r/wallstreetbets/comments/1xuocan/) |
| NBIS | 2026-11-11 12:32 | mention spike | 412 | 67.71 | 212 | 0 | wallstreetbets 409, smallstreetbets 3 | Nasdaq | #5 | [link](https://www.reddit.com/r/wallstreetbets/comments/1xuo3r4/) |
| NVDA | 2026-11-09 00:16 | hype spike mention spike | 2548 | 601.86 | 1388 | 1 | wallstreetbets 2503, smallstreetbets 43, pennystocks 2 | Nasdaq | #1 | [link](https://www.reddit.com/r/wallstreetbets/comments/1xuofnd/) |
| NXXT | 2026-11-12 03:27 | mention spike | 10 | 1.14 | 9 | 1 | pennystocks 9, wallstreetbets 1 | Nasdaq |  | [link](https://www.reddit.com/r/pennystocks/comments/1xtysur/) |
| NYT | 2026-11-12 01:02 | mention spike | 85 | 4.43 | 66 | 0 | wallstreetbets 84, smallstreetbets 1 | NYSE |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xuj9zl/) |
| OUST | 2026-11-12 01:02 | mention spike | 12 | 0.14 | 12 | 0 | wallstreetbets 12 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xuc70t/) |
| PARA | 2026-11-12 17:04 | mention spike | 16 | 0.57 | 10 | 0 | pennystocks 13, wallstreetbets 3 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xunfq3/) |
| PLCE | 2026-11-12 16:04 | mention spike | 16 | 0.57 | 12 | 0 | pennystocks 11, wallstreetbets 4, smallstreetbets 1 | Nasdaq |  | [link](https://www.reddit.com/r/smallstreetbets/comments/1xun5ay/) |
| SLI | 2026-11-12 05:40 | mention spike | 17 | 0.43 | 16 | 0 | wallstreetbets 16, smallstreetbets 1 | NYSE American |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xtwcpr/) |
| SMCI | 2026-11-12 17:47 | mention spike | 56 | 13.43 | 38 | 0 | wallstreetbets 56 | Nasdaq | #14 | [link](https://www.reddit.com/r/wallstreetbets/comments/1xu9wsm/comment/19sjhlwe21e5h/) |
| TRT | 2026-11-12 17:34 | mention spike | 11 | 0.57 | 7 | 0 | wallstreetbets 11 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xu9wsm/comment/19sjewtez9dk4/) |
| NVDL | 2026-11-11 07:39 | mention spike | 12 | 3.57 | 10 | 0 | wallstreetbets 11, smallstreetbets 1 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xu9wsm/comment/19sj4wtquo2cj/) |
| GME | 2026-11-12 01:54 | mention spike | 16 | 10.14 | 15 | 1 | wallstreetbets 14, pennystocks 2 | NYSE |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xu1nxu/) |

Full history: `episodes.csv` (one row per first flag, with the numbers known at that moment).
