# Stage 1 candidates

Updated 2026-10-28T11:39:08Z by run `40681474966`. A candidate is a ticker whose Reddit mentions (or hype-language
posts) in the last 24 hours jumped above its prior 7-day mean + 2 sd, with at least
10 mentions from 5 different authors. It stays listed until it goes
24 hours without a new flag. These are statistical flags, not accusations or advice.

| Ticker | Flagged since (UTC) | Why | Mentions 24h | Baseline/day | Authors | Hype posts | Subreddits | Exchange | StockTwits | Example |
|---|---|---|---|---|---|---|---|---|---|---|
| BBAI | 2026-10-27 20:57 | mention spike | 14 | 0.29 | 10 | 0 | pennystocks 8, wallstreetbets 5, smallstreetbets 1 | NYSE |  | [link](https://www.reddit.com/r/smallstreetbets/comments/1xfx4u9/comment/19rrmythf3zi9/) |
| BRAI | 2026-10-27 17:53 | mention spike | 11 | 0.43 | 5 | 0 | pennystocks 8, wallstreetbets 2, smallstreetbets 1 | Nasdaq |  | [link](https://www.reddit.com/r/pennystocks/comments/1xgyubd/) |
| GLD | 2026-10-28 00:47 | mention spike | 17 | 5.86 | 6 | 0 | wallstreetbets 17 | NYSE Arca |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xh322j/comment/19rru96sh15lw/) |
| HOOD | 2026-10-27 03:54 | mention spike | 217 | 9.57 | 137 | 0 | wallstreetbets 217 | Nasdaq | #3 | [link](https://www.reddit.com/r/wallstreetbets/comments/1xhjw4l/comment/19rs0yon1vzdu/) |
| INOD | 2026-10-27 14:48 | mention spike | 26 | 0.0 | 10 | 0 | wallstreetbets 26 | Nasdaq | #14 | [link](https://www.reddit.com/r/wallstreetbets/comments/1xh4cqy/) |
| MSFT | 2026-10-27 00:09 | mention spike | 52 | 29.29 | 49 | 0 | wallstreetbets 52 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xhdv4f/) |
| SKHY | 2026-10-27 19:51 | mention spike | 94 | 9.14 | 55 | 0 | wallstreetbets 94 | Nasdaq | #2 | [link](https://www.reddit.com/r/wallstreetbets/comments/1xhjw4l/comment/19rs0dxp8oyqs/) |
| SOFI | 2026-10-27 00:43 | mention spike | 51 | 6.0 | 33 | 0 | wallstreetbets 49, smallstreetbets 2 | Nasdaq |  | [link](https://www.reddit.com/r/smallstreetbets/comments/1xh67vd/) |
| STX | 2026-10-27 19:12 | mention spike | 80 | 3.86 | 57 | 0 | wallstreetbets 80 | Nasdaq | #17 | [link](https://www.reddit.com/r/wallstreetbets/comments/1xhjw4l/comment/19rs1ahxs9kv7/) |
| USAR | 2026-10-27 17:13 | mention spike | 12 | 3.43 | 6 | 0 | wallstreetbets 12 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xhjw4l/comment/19rrybu22gt7n/) |
| VRT | 2026-10-28 11:39 | mention spike | 10 | 1.0 | 10 | 0 | wallstreetbets 10 | NYSE | #1 | [link](https://www.reddit.com/r/wallstreetbets/comments/1xhljnz/) |
| CLS | 2026-10-26 19:24 | mention spike | 9 | 7.14 | 8 | 0 | wallstreetbets 9 | NYSE |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xdjnsl/comment/19rqum1ev7hlt/) |
| RIVN | 2026-10-27 00:43 | mention spike | 5 | 6.0 | 4 | 0 | wallstreetbets 5 | Nasdaq | #11 | [link](https://www.reddit.com/r/wallstreetbets/comments/1xh322j/comment/19rrhp24dgsyr/) |
| ASML | 2026-10-27 17:38 | mention spike | 6 | 3.0 | 5 | 0 | wallstreetbets 6 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xg90r5/comment/19rrtwku9l1d0/) |
| AMKR | 2026-10-27 00:43 | mention spike | 4 | 3.0 | 3 | 0 | wallstreetbets 4 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xh322j/comment/19rr7nj13q55v/) |
| GOOGL | 2026-10-27 13:39 | mention spike | 83 | 53.57 | 49 | 0 | wallstreetbets 83 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xhdxs0/) |
| RDDT | 2026-10-26 14:04 | mention spike | 46 | 25.71 | 31 | 0 | wallstreetbets 46 | NYSE | #28 | [link](https://www.reddit.com/r/wallstreetbets/comments/1xgus2q/) |
| GOOG | 2026-10-27 00:43 | mention spike | 118 | 61.71 | 63 | 0 | wallstreetbets 118 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xhjw4l/comment/19rs0lbxqc82r/) |
| ANT | 2026-10-26 13:24 | mention spike | 9 | 4.43 | 9 | 0 | wallstreetbets 9 | ? |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xgt876/) |
| DXYZ | 2026-10-27 00:43 | mention spike | 3 | 1.86 | 2 | 0 | wallstreetbets 3 | NYSE |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xh322j/comment/19rrgvsj5imjo/) |

Full history: `episodes.csv` (one row per first flag, with the numbers known at that moment).
