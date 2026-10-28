# Stage 1 candidates

Updated 2026-10-28T16:10:06Z by run `40722116206`. A candidate is a ticker whose Reddit mentions (or hype-language
posts) in the last 24 hours jumped above its prior 7-day mean + 2 sd, with at least
10 mentions from 5 different authors. It stays listed until it goes
24 hours without a new flag. These are statistical flags, not accusations or advice.

| Ticker | Flagged since (UTC) | Why | Mentions 24h | Baseline/day | Authors | Hype posts | Subreddits | Exchange | StockTwits | Example |
|---|---|---|---|---|---|---|---|---|---|---|
| BBAI | 2026-10-27 20:57 | mention spike | 10 | 0.86 | 9 | 0 | wallstreetbets 5, pennystocks 4, smallstreetbets 1 | NYSE |  | [link](https://www.reddit.com/r/smallstreetbets/comments/1xfx4u9/comment/19rrmythf3zi9/) |
| BRAI | 2026-10-27 17:53 | mention spike | 12 | 1.0 | 7 | 0 | pennystocks 7, wallstreetbets 4, smallstreetbets 1 | Nasdaq |  | [link](https://www.reddit.com/r/pennystocks/comments/1xhqjzw/) |
| HOOD | 2026-10-27 03:54 | mention spike | 233 | 11.43 | 142 | 0 | wallstreetbets 233 | Nasdaq | #14 | [link](https://www.reddit.com/r/wallstreetbets/comments/1xhjw4l/comment/19rsdu2sstfxg/) |
| SKHY | 2026-10-27 19:51 | mention spike | 109 | 9.57 | 63 | 0 | wallstreetbets 109 | Nasdaq | #3 | [link](https://www.reddit.com/r/wallstreetbets/comments/1xhjw4l/comment/19rsc5umgxi3n/) |
| SLS | 2026-10-28 13:05 | mention spike | 54 | 4.14 | 34 | 0 | wallstreetbets 50, pennystocks 4 | Nasdaq | #1 | [link](https://www.reddit.com/r/wallstreetbets/comments/1xhpxe6/) |
| STX | 2026-10-27 19:12 | mention spike | 84 | 4.14 | 57 | 0 | wallstreetbets 84 | Nasdaq | #12 | [link](https://www.reddit.com/r/wallstreetbets/comments/1xhjw4l/comment/19rsbxhc7kov5/) |
| USAR | 2026-10-27 17:13 | mention spike | 12 | 4.0 | 8 | 0 | wallstreetbets 12 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xhjw4l/comment/19rs9hycfx78g/) |
| VRT | 2026-10-28 11:39 | mention spike | 17 | 1.0 | 16 | 1 | wallstreetbets 17 | NYSE | #8 | [link](https://www.reddit.com/r/wallstreetbets/comments/1xhljnz/) |
| ENPH | 2026-10-28 16:10 | mention spike | 10 | 0.29 | 9 | 0 | wallstreetbets 10 | Nasdaq | #4 | [link](https://www.reddit.com/r/wallstreetbets/comments/1xdjnsl/comment/19rse288cx9t0/) |
| GLD | 2026-10-28 00:47 | mention spike | 13 | 6.57 | 7 | 0 | wallstreetbets 13 | NYSE Arca |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xhjw4l/comment/19rs8zspc74dh/) |
| INOD | 2026-10-27 14:48 | mention spike | 14 | 2.29 | 8 | 0 | wallstreetbets 14 | Nasdaq | #18 | [link](https://www.reddit.com/r/wallstreetbets/comments/1xh4cqy/) |
| SOFI | 2026-10-27 00:43 | mention spike | 33 | 9.0 | 20 | 0 | wallstreetbets 31, smallstreetbets 2 | Nasdaq |  | [link](https://www.reddit.com/r/smallstreetbets/comments/1xh67vd/) |
| MSFT | 2026-10-27 00:09 | mention spike | 54 | 30.71 | 48 | 0 | wallstreetbets 54 | Nasdaq | #16 | [link](https://www.reddit.com/r/wallstreetbets/comments/1xhdv4f/) |
| CLS | 2026-10-26 19:24 | mention spike | 1 | 8.29 | 1 | 0 | wallstreetbets 1 | NYSE | #22 | [link](https://www.reddit.com/r/wallstreetbets/comments/1xdjnsl/comment/19rqum1ev7hlt/) |
| RIVN | 2026-10-27 00:43 | mention spike | 7 | 5.86 | 6 | 0 | wallstreetbets 7 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xhjw4l/comment/19rsa551rxn1h/) |
| ASML | 2026-10-27 17:38 | mention spike | 4 | 3.14 | 3 | 0 | wallstreetbets 4 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xg90r5/comment/19rrtwku9l1d0/) |
| AMKR | 2026-10-27 00:43 | mention spike | 1 | 3.43 | 1 | 0 | wallstreetbets 1 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xh322j/comment/19rr7nj13q55v/) |
| GOOGL | 2026-10-27 13:39 | mention spike | 70 | 55.57 | 43 | 0 | wallstreetbets 70 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xhrwje/) |
| RDDT | 2026-10-26 14:04 | mention spike | 40 | 27.86 | 32 | 0 | wallstreetbets 40 | NYSE |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xhjw4l/comment/19rsc7pztlale/) |
| GOOG | 2026-10-27 00:43 | mention spike | 103 | 66.71 | 63 | 0 | wallstreetbets 103 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xhjw4l/comment/19rse0283thpe/) |

Full history: `episodes.csv` (one row per first flag, with the numbers known at that moment).
