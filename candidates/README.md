# Stage 1 candidates

Updated 2026-10-21T19:34:10Z by run `39661564607`. A candidate is a ticker whose Reddit mentions (or hype-language
posts) in the last 24 hours jumped above its prior 7-day mean + 2 sd, with at least
10 mentions from 5 different authors. It stays listed until it goes
24 hours without a new flag. These are statistical flags, not accusations or advice.

| Ticker | Flagged since (UTC) | Why | Mentions 24h | Baseline/day | Authors | Hype posts | Subreddits | Exchange | StockTwits | Example |
|---|---|---|---|---|---|---|---|---|---|---|
| AMOD | 2026-10-21 16:41 | mention spike | 21 | 0.43 | 8 | 0 | pennystocks 21 | Nasdaq |  | [link](https://www.reddit.com/r/pennystocks/comments/1xbpwyi/) |
| GOOG | 2026-10-19 22:36 | mention spike | 95 | 19.43 | 60 | 0 | wallstreetbets 94, smallstreetbets 1 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xb4ajv/) |
| GOOGL | 2026-10-20 18:16 | mention spike | 65 | 22.14 | 38 | 0 | wallstreetbets 65 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xbj0tb/comment/19rg4idkz6vyd/) |
| IBM | 2026-10-21 18:15 | mention spike | 18 | 2.71 | 15 | 1 | wallstreetbets 18 | NYSE | #13 | [link](https://www.reddit.com/r/wallstreetbets/comments/1xbj0tb/comment/19rg5a2b63n7n/) |
| LRCX | 2026-10-20 16:42 | mention spike | 27 | 3.43 | 15 | 0 | wallstreetbets 27 | Nasdaq | #6 | [link](https://www.reddit.com/r/wallstreetbets/comments/1xbj0tb/comment/19rg57v4zgjlw/) |
| META | 2026-10-21 11:34 | mention spike | 135 | 30.43 | 90 | 0 | wallstreetbets 134, smallstreetbets 1 | Nasdaq | #1 | [link](https://www.reddit.com/r/wallstreetbets/comments/1xbe5uu/) |
| MRNA | 2026-10-20 23:18 | mention spike | 27 | 8.71 | 21 | 0 | wallstreetbets 27 | Nasdaq | #12 | [link](https://www.reddit.com/r/wallstreetbets/comments/1xb2qdl/) |
| NFLX | 2026-10-19 19:31 | mention spike | 233 | 19.71 | 170 | 0 | wallstreetbets 228, smallstreetbets 5 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xbqi72/) |
| OKLO | 2026-10-20 21:21 | mention spike | 16 | 5.86 | 15 | 0 | wallstreetbets 16 | NYSE |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xbcbq2/) |
| SLS | 2026-10-21 08:01 | mention spike | 13 | 5.57 | 10 | 1 | wallstreetbets 12, smallstreetbets 1 | Nasdaq | #23 | [link](https://www.reddit.com/r/wallstreetbets/comments/1xb2ztj/comment/19rg4zp2i1l6t/) |
| SMCI | 2026-10-20 21:06 | mention spike | 109 | 6.14 | 69 | 1 | wallstreetbets 108, smallstreetbets 1 | Nasdaq | #19 | [link](https://www.reddit.com/r/smallstreetbets/comments/1xbi8mj/) |
| SPCX | 2026-10-20 10:18 | mention spike | 467 | 51.71 | 276 | 2 | wallstreetbets 465, smallstreetbets 2 | Nasdaq | #2 | [link](https://www.reddit.com/r/smallstreetbets/comments/1xbph9h/) |
| PAC | 2026-10-21 02:19 | mention spike | 6 | 0.86 | 6 | 0 | smallstreetbets 6 | NYSE |  | [link](https://www.reddit.com/r/smallstreetbets/comments/1xay6zv/comment/phyzgua/) |
| HTZ | 2026-10-20 13:24 | mention spike | 7 | 8.86 | 5 | 0 | wallstreetbets 7 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xbj0tb/comment/pi0szjg/) |

Full history: `episodes.csv` (one row per first flag, with the numbers known at that moment).
