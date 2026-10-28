# Stage 1 candidates

Updated 2026-10-28T20:03:08Z by run `40759555103`. A candidate is a ticker whose Reddit mentions (or hype-language
posts) in the last 24 hours jumped above its prior 7-day mean + 2 sd, with at least
10 mentions from 5 different authors. It stays listed until it goes
24 hours without a new flag. These are statistical flags, not accusations or advice.

| Ticker | Flagged since (UTC) | Why | Mentions 24h | Baseline/day | Authors | Hype posts | Subreddits | Exchange | StockTwits | Example |
|---|---|---|---|---|---|---|---|---|---|---|
| BRAI | 2026-10-27 17:53 | mention spike | 10 | 1.43 | 6 | 0 | pennystocks 5, wallstreetbets 4, smallstreetbets 1 | Nasdaq |  | [link](https://www.reddit.com/r/pennystocks/comments/1xhqjzw/) |
| DJT | 2026-10-28 17:04 | mention spike | 10 | 2.29 | 10 | 0 | smallstreetbets 6, wallstreetbets 4 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xh6799/comment/19rsoc867sjvl/) |
| ENPH | 2026-10-28 16:10 | mention spike | 10 | 0.29 | 9 | 0 | wallstreetbets 10 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xdjnsl/comment/19rse288cx9t0/) |
| HOOD | 2026-10-27 03:54 | mention spike | 207 | 17.14 | 121 | 0 | wallstreetbets 204, smallstreetbets 3 | Nasdaq |  | [link](https://www.reddit.com/r/smallstreetbets/comments/1xhxifo/) |
| MSFT | 2026-10-27 00:09 | mention spike | 78 | 32.43 | 64 | 1 | wallstreetbets 77, smallstreetbets 1 | Nasdaq | #2 | [link](https://www.reddit.com/r/wallstreetbets/comments/1xhdv4f/) |
| ORCL | 2026-10-28 18:38 | mention spike | 66 | 9.0 | 46 | 0 | wallstreetbets 66 | NYSE | #1 | [link](https://www.reddit.com/r/wallstreetbets/comments/1xhjw4l/comment/19rso6xyhwfz7/) |
| SKHY | 2026-10-27 19:51 | mention spike | 100 | 11.86 | 61 | 0 | wallstreetbets 100 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xhu3mt/) |
| SLS | 2026-10-28 13:05 | mention spike | 57 | 4.29 | 38 | 0 | wallstreetbets 51, pennystocks 6 | Nasdaq | #4 | [link](https://www.reddit.com/r/wallstreetbets/comments/1xhv9n1/) |
| STX | 2026-10-27 19:12 | mention spike | 80 | 5.43 | 55 | 0 | wallstreetbets 80 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xhjw4l/comment/19rsmdvb4u19e/) |
| VRT | 2026-10-28 11:39 | mention spike | 20 | 1.0 | 17 | 1 | wallstreetbets 20 | NYSE | #30 | [link](https://www.reddit.com/r/wallstreetbets/comments/1xhljnz/) |
| INOD | 2026-10-27 14:48 | mention spike | 10 | 3.0 | 7 | 0 | wallstreetbets 10 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xh4cqy/) |
| BBAI | 2026-10-27 20:57 | mention spike | 7 | 1.29 | 7 | 0 | wallstreetbets 5, pennystocks 1, smallstreetbets 1 | NYSE |  | [link](https://www.reddit.com/r/smallstreetbets/comments/1xfx4u9/comment/19rrmythf3zi9/) |
| USAR | 2026-10-27 17:13 | mention spike | 12 | 4.29 | 10 | 0 | wallstreetbets 12 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xhjw4l/comment/19rsmp62o2ztv/) |
| GLD | 2026-10-28 00:47 | mention spike | 13 | 6.57 | 8 | 0 | wallstreetbets 13 | NYSE Arca |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xhjw4l/comment/19rsn1l4pvaw0/) |
| SOFI | 2026-10-27 00:43 | mention spike | 29 | 10.14 | 18 | 0 | wallstreetbets 27, smallstreetbets 2 | Nasdaq | #26 | [link](https://www.reddit.com/r/smallstreetbets/comments/1xh67vd/) |
| CLS | 2026-10-26 19:24 | mention spike | 0 |  | 0 | 0 |  | NYSE |  |  |
| RIVN | 2026-10-27 00:43 | mention spike | 4 | 6.43 | 4 | 0 | wallstreetbets 4 | Nasdaq | #28 | [link](https://www.reddit.com/r/wallstreetbets/comments/1xhjw4l/comment/19rsfw7ikq3tt/) |
| ASML | 2026-10-27 17:38 | mention spike | 1 | 3.57 | 1 | 0 | wallstreetbets 1 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xg90r5/comment/19rrtwku9l1d0/) |

Full history: `episodes.csv` (one row per first flag, with the numbers known at that moment).
