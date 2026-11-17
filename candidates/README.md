# Stage 1 candidates

Updated 2026-11-17T14:17:11Z by run `44100438720`. A candidate is a ticker whose Reddit mentions (or hype-language
posts) in the last 24 hours jumped above its prior 7-day mean + 2 sd, with at least
10 mentions from 5 different authors. It stays listed until it goes
24 hours without a new flag. These are statistical flags, not accusations or advice.

| Ticker | Flagged since (UTC) | Why | Mentions 24h | Baseline/day | Authors | Hype posts | Subreddits | Exchange | StockTwits | Example |
|---|---|---|---|---|---|---|---|---|---|---|
| ANT | 2026-11-16 16:34 | mention spike | 209 | 79.86 | 148 | 0 | wallstreetbets 205, smallstreetbets 3, pennystocks 1 | ? |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xyjhd5/) |
| ASTS | 2026-11-17 03:28 | mention spike | 94 | 37.71 | 66 | 0 | wallstreetbets 94 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xxvao9/) |
| DXYZ | 2026-11-14 23:53 | mention spike | 39 | 6.86 | 20 | 0 | wallstreetbets 38, pennystocks 1 | NYSE |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xy57tm/) |
| HOOD | 2026-11-16 15:08 | mention spike | 22 | 4.86 | 17 | 0 | wallstreetbets 22 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xy146v/comment/19sr069pulcqr/) |
| IREN | 2026-11-16 18:57 | mention spike | 35 | 12.71 | 31 | 1 | wallstreetbets 35 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xy146v/comment/19srfzqfuiock/) |
| JPM | 2026-11-17 10:05 | mention spike | 10 | 2.71 | 9 | 0 | wallstreetbets 10 | NYSE | #15 | [link](https://www.reddit.com/r/wallstreetbets/comments/1xy71g4/) |
| RCAT | 2026-11-16 22:11 | mention spike | 25 | 0.71 | 21 | 0 | wallstreetbets 24, pennystocks 1 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xyhl51/comment/19srxdas2z95v/) |
| ROPE | 2026-11-17 06:59 | mention spike | 11 | 2.57 | 10 | 0 | wallstreetbets 10, smallstreetbets 1 | NYSE Arca |  | [link](https://www.reddit.com/r/smallstreetbets/comments/1xycnfi/comment/19srdtonkjoma/) |
| SHAZ | 2026-11-17 10:45 | mention spike | 12 | 0.0 | 12 | 0 | wallstreetbets 12 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xyhl51/comment/19srtudesy3oj/) |
| SLS | 2026-11-17 12:33 | mention spike | 200 | 6.71 | 119 | 0 | wallstreetbets 193, pennystocks 7 | Nasdaq | #1 | [link](https://www.reddit.com/r/wallstreetbets/comments/1xylejl/) |
| SNDK | 2026-11-17 10:05 | mention spike | 71 | 34.57 | 48 | 0 | wallstreetbets 68, smallstreetbets 2, pennystocks 1 | Nasdaq |  | [link](https://www.reddit.com/r/pennystocks/comments/1xxs4cy/) |
| SPAI | 2026-11-17 14:06 | mention spike | 10 | 0.14 | 5 | 0 | pennystocks 9, wallstreetbets 1 | Nasdaq |  | [link](https://www.reddit.com/r/pennystocks/comments/1xybo6o/comment/19srx84qjhk2t/) |
| TQQQ | 2026-11-17 01:13 | mention spike | 19 | 6.14 | 13 | 0 | wallstreetbets 17, smallstreetbets 2 | Nasdaq |  | [link](https://www.reddit.com/r/smallstreetbets/comments/1xyad7h/) |
| VOO | 2026-11-17 00:31 | mention spike | 36 | 14.14 | 31 | 0 | wallstreetbets 35, smallstreetbets 1 | NYSE Arca |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xy0xor/comment/19srvgke0p32c/) |
| WMT | 2026-11-16 07:17 | mention spike | 21 | 5.14 | 13 | 0 | wallstreetbets 21 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xyhl51/comment/19srs37lxdq8x/) |
| INTC | 2026-11-17 00:48 | mention spike | 36 | 18.57 | 30 | 0 | wallstreetbets 36 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xyc42m/) |
| LXEO | 2026-11-16 20:09 | mention spike | 7 | 0.43 | 6 | 0 | pennystocks 5, smallstreetbets 1, wallstreetbets 1 | Nasdaq |  | [link](https://www.reddit.com/r/pennystocks/comments/1xxs8on/) |
| RSP | 2026-11-17 03:38 | mention spike | 8 | 2.57 | 8 | 0 | wallstreetbets 8 | NYSE Arca |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xy9o6m/comment/19sr5333e4x1c/) |
| MSTR | 2026-11-13 06:20 | mention spike | 12 | 13.86 | 10 | 0 | wallstreetbets 12 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xy146v/comment/19sr614ae7mwy/) |
| PLTR | 2026-11-16 23:04 | mention spike | 6 | 4.71 | 6 | 0 | wallstreetbets 6 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xy3al4/) |

Full history: `episodes.csv` (one row per first flag, with the numbers known at that moment).
