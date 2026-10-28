# Stage 1 candidates

Updated 2026-10-28T18:03:08Z by run `40741359012`. A candidate is a ticker whose Reddit mentions (or hype-language
posts) in the last 24 hours jumped above its prior 7-day mean + 2 sd, with at least
10 mentions from 5 different authors. It stays listed until it goes
24 hours without a new flag. These are statistical flags, not accusations or advice.

| Ticker | Flagged since (UTC) | Why | Mentions 24h | Baseline/day | Authors | Hype posts | Subreddits | Exchange | StockTwits | Example |
|---|---|---|---|---|---|---|---|---|---|---|
| DJT | 2026-10-28 17:04 | mention spike | 10 | 2.29 | 10 | 0 | smallstreetbets 6, wallstreetbets 4 | Nasdaq | #3 | [link](https://www.reddit.com/r/wallstreetbets/comments/1xhjw4l/comment/19rsgbiojns9u/) |
| ENPH | 2026-10-28 16:10 | mention spike | 10 | 0.29 | 9 | 0 | wallstreetbets 10 | Nasdaq | #6 | [link](https://www.reddit.com/r/wallstreetbets/comments/1xdjnsl/comment/19rse288cx9t0/) |
| HOOD | 2026-10-27 03:54 | mention spike | 229 | 12.71 | 137 | 0 | wallstreetbets 228, smallstreetbets 1 | Nasdaq |  | [link](https://www.reddit.com/r/smallstreetbets/comments/1xhun0g/) |
| MSFT | 2026-10-27 00:09 | mention spike | 61 | 31.57 | 54 | 0 | wallstreetbets 61 | Nasdaq | #19 | [link](https://www.reddit.com/r/wallstreetbets/comments/1xhdv4f/) |
| SKHY | 2026-10-27 19:51 | mention spike | 111 | 10.0 | 62 | 0 | wallstreetbets 111 | Nasdaq | #8 | [link](https://www.reddit.com/r/wallstreetbets/comments/1xhu3mt/) |
| SLS | 2026-10-28 13:05 | mention spike | 57 | 4.14 | 36 | 0 | wallstreetbets 51, pennystocks 6 | Nasdaq | #2 | [link](https://www.reddit.com/r/wallstreetbets/comments/1xhv9n1/) |
| STX | 2026-10-27 19:12 | mention spike | 84 | 4.71 | 54 | 0 | wallstreetbets 84 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xhjw4l/comment/19rsie0378uzo/) |
| VRT | 2026-10-28 11:39 | mention spike | 17 | 1.0 | 16 | 1 | wallstreetbets 17 | NYSE | #11 | [link](https://www.reddit.com/r/wallstreetbets/comments/1xhljnz/) |
| BRAI | 2026-10-27 17:53 | mention spike | 9 | 1.43 | 6 | 0 | pennystocks 4, wallstreetbets 4, smallstreetbets 1 | Nasdaq |  | [link](https://www.reddit.com/r/pennystocks/comments/1xhqjzw/) |
| INOD | 2026-10-27 14:48 | mention spike | 13 | 2.57 | 8 | 0 | wallstreetbets 13 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xh4cqy/) |
| BBAI | 2026-10-27 20:57 | mention spike | 7 | 1.29 | 7 | 0 | wallstreetbets 5, pennystocks 1, smallstreetbets 1 | NYSE |  | [link](https://www.reddit.com/r/smallstreetbets/comments/1xfx4u9/comment/19rrmythf3zi9/) |
| USAR | 2026-10-27 17:13 | mention spike | 11 | 4.29 | 9 | 0 | wallstreetbets 11 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xh322j/comment/19rsfuxrzwlgh/) |
| GLD | 2026-10-28 00:47 | mention spike | 12 | 6.43 | 8 | 0 | wallstreetbets 12 | NYSE Arca |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xhjw4l/comment/19rsi7ud3pp0l/) |
| SOFI | 2026-10-27 00:43 | mention spike | 29 | 9.71 | 17 | 0 | wallstreetbets 27, smallstreetbets 2 | Nasdaq |  | [link](https://www.reddit.com/r/smallstreetbets/comments/1xh67vd/) |
| CLS | 2026-10-26 19:24 | mention spike | 1 | 8.29 | 1 | 0 | wallstreetbets 1 | NYSE | #15 | [link](https://www.reddit.com/r/wallstreetbets/comments/1xdjnsl/comment/19rqum1ev7hlt/) |
| RIVN | 2026-10-27 00:43 | mention spike | 8 | 5.86 | 7 | 0 | wallstreetbets 8 | Nasdaq | #26 | [link](https://www.reddit.com/r/wallstreetbets/comments/1xhjw4l/comment/19rsfw7ikq3tt/) |
| ASML | 2026-10-27 17:38 | mention spike | 1 | 3.57 | 1 | 0 | wallstreetbets 1 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xg90r5/comment/19rrtwku9l1d0/) |
| AMKR | 2026-10-27 00:43 | mention spike | 1 | 3.43 | 1 | 0 | wallstreetbets 1 | Nasdaq | #22 | [link](https://www.reddit.com/r/wallstreetbets/comments/1xh322j/comment/19rr7nj13q55v/) |
| GOOGL | 2026-10-27 13:39 | mention spike | 77 | 55.71 | 43 | 0 | wallstreetbets 77 | Nasdaq | #14 | [link](https://www.reddit.com/r/wallstreetbets/comments/1xhrwje/) |
| RDDT | 2026-10-26 14:04 | mention spike | 41 | 28.14 | 31 | 0 | wallstreetbets 41 | NYSE |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xhjw4l/comment/19rshvp6yyjmt/) |

Full history: `episodes.csv` (one row per first flag, with the numbers known at that moment).
