# Stage 1 candidates

Updated 2026-11-12T20:43:10Z by run `43301095470`. A candidate is a ticker whose Reddit mentions (or hype-language
posts) in the last 24 hours jumped above its prior 7-day mean + 2 sd, with at least
10 mentions from 5 different authors. It stays listed until it goes
24 hours without a new flag. These are statistical flags, not accusations or advice.

| Ticker | Flagged since (UTC) | Why | Mentions 24h | Baseline/day | Authors | Hype posts | Subreddits | Exchange | StockTwits | Example |
|---|---|---|---|---|---|---|---|---|---|---|
| AMAT | 2026-11-12 18:42 | mention spike | 20 | 2.71 | 16 | 0 | wallstreetbets 20 | Nasdaq | #7 | [link](https://www.reddit.com/r/wallstreetbets/comments/1xpjj4e/comment/19sjhbso8a89v/) |
| AMD | 2026-11-12 05:14 | mention spike | 550 | 122.29 | 422 | 1 | wallstreetbets 540, smallstreetbets 8, pennystocks 2 | Nasdaq | #8 | [link](https://www.reddit.com/r/wallstreetbets/comments/1xumy47/) |
| AVGO | 2026-11-09 15:56 | mention spike | 66 | 19.0 | 54 | 0 | wallstreetbets 66 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xuk703/) |
| CBRS | 2026-11-12 16:56 | mention spike | 21 | 3.71 | 17 | 0 | wallstreetbets 21 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xu9wsm/comment/19sjg0zit24f8/) |
| GLD | 2026-11-12 18:15 | mention spike | 16 | 7.43 | 10 | 0 | wallstreetbets 16 | NYSE Arca |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xu9wsm/comment/19sjbixcwwfs2/) |
| LUNR | 2026-11-12 14:43 | mention spike | 15 | 5.57 | 12 | 0 | wallstreetbets 14, pennystocks 1 | Nasdaq | #23 | [link](https://www.reddit.com/r/wallstreetbets/comments/1xu9wsm/comment/19sjgnaidheck/) |
| NBIS | 2026-11-11 12:32 | mention spike | 409 | 68.14 | 210 | 0 | wallstreetbets 406, smallstreetbets 3 | Nasdaq | #6 | [link](https://www.reddit.com/r/wallstreetbets/comments/1xuk7ku/) |
| NVDA | 2026-11-09 00:16 | hype spike mention spike | 2502 | 606.57 | 1372 | 1 | wallstreetbets 2459, smallstreetbets 41, pennystocks 2 | Nasdaq | #1 | [link](https://www.reddit.com/r/wallstreetbets/comments/1xuntwf/) |
| NXXT | 2026-11-12 03:27 | mention spike | 11 | 1.0 | 10 | 1 | pennystocks 10, wallstreetbets 1 | Nasdaq |  | [link](https://www.reddit.com/r/pennystocks/comments/1xtysur/) |
| NYT | 2026-11-12 01:02 | mention spike | 85 | 4.43 | 66 | 0 | wallstreetbets 84, smallstreetbets 1 | NYSE |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xuj9zl/) |
| OUST | 2026-11-12 01:02 | mention spike | 12 | 0.14 | 12 | 0 | wallstreetbets 12 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xuc70t/) |
| PARA | 2026-11-12 17:04 | mention spike | 16 | 0.57 | 10 | 0 | pennystocks 13, wallstreetbets 3 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xunfq3/) |
| PLCE | 2026-11-12 16:04 | mention spike | 16 | 0.57 | 12 | 0 | pennystocks 11, wallstreetbets 4, smallstreetbets 1 | Nasdaq |  | [link](https://www.reddit.com/r/smallstreetbets/comments/1xun5ay/) |
| SLI | 2026-11-12 05:40 | mention spike | 17 | 0.43 | 16 | 0 | wallstreetbets 16, smallstreetbets 1 | NYSE American |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xtwcpr/) |
| SMCI | 2026-11-12 17:47 | mention spike | 55 | 13.43 | 37 | 0 | wallstreetbets 55 | Nasdaq | #4 | [link](https://www.reddit.com/r/wallstreetbets/comments/1xu9wsm/comment/19sjegrhxh1pe/) |
| TRT | 2026-11-12 17:34 | mention spike | 11 | 0.57 | 7 | 0 | wallstreetbets 11 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xu9wsm/comment/19sjewtez9dk4/) |
| ASML | 2026-11-12 20:43 | mention spike | 10 | 3.71 | 9 | 0 | wallstreetbets 10 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xudez8/comment/19sjh4mfzo08y/) |
| NVDL | 2026-11-11 07:39 | mention spike | 12 | 3.57 | 10 | 0 | wallstreetbets 11, smallstreetbets 1 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xu9wsm/comment/19sj4wtquo2cj/) |
| GME | 2026-11-12 01:54 | mention spike | 16 | 10.29 | 15 | 1 | wallstreetbets 14, pennystocks 2 | NYSE |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xu1nxu/) |

Full history: `episodes.csv` (one row per first flag, with the numbers known at that moment).
