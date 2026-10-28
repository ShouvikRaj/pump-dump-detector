# Stage 1 candidates

Updated 2026-10-28T11:03:06Z by run `40676276071`. A candidate is a ticker whose Reddit mentions (or hype-language
posts) in the last 24 hours jumped above its prior 7-day mean + 2 sd, with at least
10 mentions from 5 different authors. It stays listed until it goes
24 hours without a new flag. These are statistical flags, not accusations or advice.

| Ticker | Flagged since (UTC) | Why | Mentions 24h | Baseline/day | Authors | Hype posts | Subreddits | Exchange | StockTwits | Example |
|---|---|---|---|---|---|---|---|---|---|---|
| BBAI | 2026-10-27 20:57 | mention spike | 14 | 0.29 | 10 | 0 | pennystocks 8, wallstreetbets 5, smallstreetbets 1 | NYSE |  | [link](https://www.reddit.com/r/smallstreetbets/comments/1xfx4u9/comment/19rrmythf3zi9/) |
| BRAI | 2026-10-27 17:53 | mention spike | 12 | 0.29 | 5 | 0 | pennystocks 9, wallstreetbets 2, smallstreetbets 1 | Nasdaq |  | [link](https://www.reddit.com/r/pennystocks/comments/1xgyubd/) |
| GLD | 2026-10-28 00:47 | mention spike | 17 | 5.86 | 6 | 0 | wallstreetbets 17 | NYSE Arca |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xh322j/comment/19rru96sh15lw/) |
| HOOD | 2026-10-27 03:54 | mention spike | 216 | 9.57 | 138 | 0 | wallstreetbets 216 | Nasdaq | #3 | [link](https://www.reddit.com/r/wallstreetbets/comments/1xhjw4l/comment/19rs04v43m484/) |
| INOD | 2026-10-27 14:48 | mention spike | 26 | 0.0 | 10 | 0 | wallstreetbets 26 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xh4cqy/) |
| SKHY | 2026-10-27 19:51 | mention spike | 95 | 9.14 | 56 | 0 | wallstreetbets 95 | Nasdaq | #11 | [link](https://www.reddit.com/r/wallstreetbets/comments/1xhjw4l/comment/19rs0dxp8oyqs/) |
| SOFI | 2026-10-27 00:43 | mention spike | 57 | 5.14 | 38 | 0 | wallstreetbets 55, smallstreetbets 2 | Nasdaq |  | [link](https://www.reddit.com/r/smallstreetbets/comments/1xh67vd/) |
| STX | 2026-10-27 19:12 | mention spike | 78 | 3.86 | 56 | 0 | wallstreetbets 78 | Nasdaq | #6 | [link](https://www.reddit.com/r/wallstreetbets/comments/1xhjw4l/comment/19rrzhu3ea868/) |
| USAR | 2026-10-27 17:13 | mention spike | 12 | 3.43 | 6 | 0 | wallstreetbets 12 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xhjw4l/comment/19rrybu22gt7n/) |
| MSFT | 2026-10-27 00:09 | mention spike | 52 | 29.29 | 49 | 0 | wallstreetbets 52 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xhdv4f/) |
| CLS | 2026-10-26 19:24 | mention spike | 12 | 6.71 | 10 | 0 | wallstreetbets 12 | NYSE |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xdjnsl/comment/19rqum1ev7hlt/) |
| RIVN | 2026-10-27 00:43 | mention spike | 5 | 6.0 | 4 | 0 | wallstreetbets 5 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xh322j/comment/19rrhp24dgsyr/) |
| ASML | 2026-10-27 17:38 | mention spike | 6 | 3.0 | 5 | 0 | wallstreetbets 6 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xg90r5/comment/19rrtwku9l1d0/) |
| AMKR | 2026-10-27 00:43 | mention spike | 4 | 3.0 | 3 | 0 | wallstreetbets 4 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xh322j/comment/19rr7nj13q55v/) |
| GOOGL | 2026-10-27 13:39 | mention spike | 86 | 53.14 | 50 | 0 | wallstreetbets 86 | Nasdaq | #16 | [link](https://www.reddit.com/r/wallstreetbets/comments/1xhdxs0/) |
| RDDT | 2026-10-26 14:04 | mention spike | 45 | 25.43 | 30 | 0 | wallstreetbets 45 | NYSE |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xgus2q/) |
| GOOG | 2026-10-27 00:43 | mention spike | 122 | 61.0 | 67 | 1 | wallstreetbets 122 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xhjw4l/comment/19rrzd4q1myn5/) |
| ANT | 2026-10-26 13:24 | mention spike | 9 | 4.43 | 9 | 0 | wallstreetbets 9 | ? |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xgt876/) |
| DXYZ | 2026-10-27 00:43 | mention spike | 3 | 1.86 | 2 | 0 | wallstreetbets 3 | NYSE |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xh322j/comment/19rrgvsj5imjo/) |
| PBR | 2026-10-26 09:22 | mention spike | 2 | 6.14 | 2 | 0 | wallstreetbets 2 | NYSE |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xe9fc7/comment/19rroiilkm5a9/) |

Full history: `episodes.csv` (one row per first flag, with the numbers known at that moment).
