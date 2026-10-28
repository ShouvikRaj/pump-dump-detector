# Stage 1 candidates

Updated 2026-10-28T20:50:07Z by run `40765498616`. A candidate is a ticker whose Reddit mentions (or hype-language
posts) in the last 24 hours jumped above its prior 7-day mean + 2 sd, with at least
10 mentions from 5 different authors. It stays listed until it goes
24 hours without a new flag. These are statistical flags, not accusations or advice.

| Ticker | Flagged since (UTC) | Why | Mentions 24h | Baseline/day | Authors | Hype posts | Subreddits | Exchange | StockTwits | Example |
|---|---|---|---|---|---|---|---|---|---|---|
| BRAI | 2026-10-27 17:53 | mention spike | 11 | 1.43 | 6 | 0 | pennystocks 6, wallstreetbets 4, smallstreetbets 1 | Nasdaq |  | [link](https://www.reddit.com/r/pennystocks/comments/1xhqjzw/) |
| DJT | 2026-10-28 17:04 | mention spike | 11 | 2.29 | 11 | 0 | smallstreetbets 6, wallstreetbets 5 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xhjw4l/comment/19rsok8ay5ecl/) |
| GLD | 2026-10-28 00:47 | mention spike | 15 | 6.57 | 9 | 0 | wallstreetbets 15 | NYSE Arca |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xhjw4l/comment/19rsommwyekmc/) |
| HOOD | 2026-10-27 03:54 | mention spike | 143 | 26.43 | 85 | 0 | wallstreetbets 140, smallstreetbets 3 | Nasdaq |  | [link](https://www.reddit.com/r/smallstreetbets/comments/1xhxifo/) |
| MSFT | 2026-10-27 00:09 | mention spike | 94 | 32.0 | 78 | 1 | wallstreetbets 93, smallstreetbets 1 | Nasdaq | #5 | [link](https://www.reddit.com/r/wallstreetbets/comments/1xhdv4f/) |
| ORCL | 2026-10-28 18:38 | mention spike | 66 | 9.0 | 47 | 0 | wallstreetbets 66 | NYSE | #4 | [link](https://www.reddit.com/r/wallstreetbets/comments/1xhjw4l/comment/19rsojmvmr4kk/) |
| SKHY | 2026-10-27 19:51 | mention spike | 89 | 13.43 | 57 | 0 | wallstreetbets 89 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xhu3mt/) |
| SLS | 2026-10-28 13:05 | mention spike | 57 | 4.43 | 39 | 0 | wallstreetbets 51, pennystocks 6 | Nasdaq | #7 | [link](https://www.reddit.com/r/wallstreetbets/comments/1xhv9n1/) |
| USAR | 2026-10-27 17:13 | mention spike | 12 | 4.14 | 10 | 0 | wallstreetbets 12 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xhjw4l/comment/19rsmp62o2ztv/) |
| VRT | 2026-10-28 11:39 | mention spike | 20 | 1.0 | 17 | 1 | wallstreetbets 20 | NYSE |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xhljnz/) |
| GOOG | 2026-10-28 20:50 | mention spike | 158 | 69.29 | 107 | 2 | wallstreetbets 157, smallstreetbets 1 | Nasdaq | #1 | [link](https://www.reddit.com/r/wallstreetbets/comments/1xhzmym/) |
| STX | 2026-10-27 19:12 | mention spike | 37 | 11.57 | 28 | 0 | wallstreetbets 37 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xhjw4l/comment/19rsmdvb4u19e/) |
| ENPH | 2026-10-28 16:10 | mention spike | 8 | 0.57 | 8 | 0 | wallstreetbets 8 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xdjnsl/comment/19rse288cx9t0/) |
| INOD | 2026-10-27 14:48 | mention spike | 9 | 3.14 | 6 | 0 | wallstreetbets 9 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xhjw4l/comment/19rsf1d63tz35/) |
| BBAI | 2026-10-27 20:57 | mention spike | 4 | 1.71 | 4 | 0 | wallstreetbets 3, smallstreetbets 1 | NYSE |  | [link](https://www.reddit.com/r/smallstreetbets/comments/1xfx4u9/comment/19rrmythf3zi9/) |
| SOFI | 2026-10-27 00:43 | mention spike | 24 | 11.0 | 15 | 0 | wallstreetbets 22, smallstreetbets 2 | Nasdaq |  | [link](https://www.reddit.com/r/smallstreetbets/comments/1xh67vd/) |
| CLS | 2026-10-26 19:24 | mention spike | 0 |  | 0 | 0 |  | NYSE |  |  |
| RIVN | 2026-10-27 00:43 | mention spike | 4 | 6.43 | 4 | 0 | wallstreetbets 4 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xhjw4l/comment/19rsfw7ikq3tt/) |
| ASML | 2026-10-27 17:38 | mention spike | 1 | 3.57 | 1 | 0 | wallstreetbets 1 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xg90r5/comment/19rrtwku9l1d0/) |

Full history: `episodes.csv` (one row per first flag, with the numbers known at that moment).
