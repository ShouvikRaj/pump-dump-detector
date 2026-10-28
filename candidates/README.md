# Stage 1 candidates

Updated 2026-10-28T18:57:06Z by run `40749599087`. A candidate is a ticker whose Reddit mentions (or hype-language
posts) in the last 24 hours jumped above its prior 7-day mean + 2 sd, with at least
10 mentions from 5 different authors. It stays listed until it goes
24 hours without a new flag. These are statistical flags, not accusations or advice.

| Ticker | Flagged since (UTC) | Why | Mentions 24h | Baseline/day | Authors | Hype posts | Subreddits | Exchange | StockTwits | Example |
|---|---|---|---|---|---|---|---|---|---|---|
| BRAI | 2026-10-27 17:53 | mention spike | 10 | 1.43 | 6 | 0 | pennystocks 5, wallstreetbets 4, smallstreetbets 1 | Nasdaq |  | [link](https://www.reddit.com/r/pennystocks/comments/1xhqjzw/) |
| DJT | 2026-10-28 17:04 | mention spike | 10 | 2.14 | 10 | 0 | smallstreetbets 6, wallstreetbets 4 | Nasdaq | #24 | [link](https://www.reddit.com/r/wallstreetbets/comments/1xhjw4l/comment/19rsgbiojns9u/) |
| ENPH | 2026-10-28 16:10 | mention spike | 10 | 0.29 | 9 | 0 | wallstreetbets 10 | Nasdaq | #16 | [link](https://www.reddit.com/r/wallstreetbets/comments/1xdjnsl/comment/19rse288cx9t0/) |
| HOOD | 2026-10-27 03:54 | mention spike | 223 | 14.0 | 134 | 0 | wallstreetbets 222, smallstreetbets 1 | Nasdaq |  | [link](https://www.reddit.com/r/smallstreetbets/comments/1xhun0g/) |
| MSFT | 2026-10-27 00:09 | mention spike | 59 | 32.14 | 53 | 0 | wallstreetbets 59 | Nasdaq | #7 | [link](https://www.reddit.com/r/wallstreetbets/comments/1xhdv4f/) |
| ORCL | 2026-10-28 18:38 | mention spike | 43 | 9.0 | 31 | 0 | wallstreetbets 43 | NYSE | #1 | [link](https://www.reddit.com/r/wallstreetbets/comments/1xhjw4l/comment/19rskkb0g3ch0/) |
| SKHY | 2026-10-27 19:51 | mention spike | 110 | 10.14 | 62 | 0 | wallstreetbets 110 | Nasdaq | #10 | [link](https://www.reddit.com/r/wallstreetbets/comments/1xhu3mt/) |
| SLS | 2026-10-28 13:05 | mention spike | 57 | 4.14 | 37 | 0 | wallstreetbets 51, pennystocks 6 | Nasdaq | #4 | [link](https://www.reddit.com/r/wallstreetbets/comments/1xhv9n1/) |
| STX | 2026-10-27 19:12 | mention spike | 84 | 4.71 | 54 | 0 | wallstreetbets 84 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xhjw4l/comment/19rsie0378uzo/) |
| VRT | 2026-10-28 11:39 | mention spike | 18 | 1.0 | 16 | 1 | wallstreetbets 18 | NYSE | #18 | [link](https://www.reddit.com/r/wallstreetbets/comments/1xhljnz/) |
| INOD | 2026-10-27 14:48 | mention spike | 11 | 2.86 | 8 | 0 | wallstreetbets 11 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xh4cqy/) |
| BBAI | 2026-10-27 20:57 | mention spike | 7 | 1.29 | 7 | 0 | wallstreetbets 5, pennystocks 1, smallstreetbets 1 | NYSE |  | [link](https://www.reddit.com/r/smallstreetbets/comments/1xfx4u9/comment/19rrmythf3zi9/) |
| USAR | 2026-10-27 17:13 | mention spike | 11 | 4.29 | 9 | 0 | wallstreetbets 11 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xh322j/comment/19rsfuxrzwlgh/) |
| GLD | 2026-10-28 00:47 | mention spike | 12 | 6.43 | 8 | 0 | wallstreetbets 12 | NYSE Arca | #13 | [link](https://www.reddit.com/r/wallstreetbets/comments/1xhjw4l/comment/19rsi7ud3pp0l/) |
| SOFI | 2026-10-27 00:43 | mention spike | 26 | 10.14 | 16 | 0 | wallstreetbets 24, smallstreetbets 2 | Nasdaq |  | [link](https://www.reddit.com/r/smallstreetbets/comments/1xh67vd/) |
| CLS | 2026-10-26 19:24 | mention spike | 1 | 8.29 | 1 | 0 | wallstreetbets 1 | NYSE |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xdjnsl/comment/19rqum1ev7hlt/) |
| RIVN | 2026-10-27 00:43 | mention spike | 6 | 6.14 | 6 | 0 | wallstreetbets 6 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xhjw4l/comment/19rsfw7ikq3tt/) |
| ASML | 2026-10-27 17:38 | mention spike | 1 | 3.57 | 1 | 0 | wallstreetbets 1 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xg90r5/comment/19rrtwku9l1d0/) |
| AMKR | 2026-10-27 00:43 | mention spike | 1 | 3.43 | 1 | 0 | wallstreetbets 1 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xh322j/comment/19rr7nj13q55v/) |
| GOOGL | 2026-10-27 13:39 | mention spike | 71 | 55.29 | 40 | 0 | wallstreetbets 71 | Nasdaq | #21 | [link](https://www.reddit.com/r/wallstreetbets/comments/1xhrwje/) |

Full history: `episodes.csv` (one row per first flag, with the numbers known at that moment).
