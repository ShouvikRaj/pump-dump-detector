# Stage 1 candidates

Updated 2026-11-17T13:40:08Z by run `44093634290`. A candidate is a ticker whose Reddit mentions (or hype-language
posts) in the last 24 hours jumped above its prior 7-day mean + 2 sd, with at least
10 mentions from 5 different authors. It stays listed until it goes
24 hours without a new flag. These are statistical flags, not accusations or advice.

| Ticker | Flagged since (UTC) | Why | Mentions 24h | Baseline/day | Authors | Hype posts | Subreddits | Exchange | StockTwits | Example |
|---|---|---|---|---|---|---|---|---|---|---|
| ANT | 2026-11-16 16:34 | mention spike | 210 | 79.29 | 148 | 0 | wallstreetbets 206, smallstreetbets 3, pennystocks 1 | ? |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xyjhd5/) |
| DXYZ | 2026-11-14 23:53 | mention spike | 40 | 6.57 | 19 | 0 | wallstreetbets 39, pennystocks 1 | NYSE |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xy57tm/) |
| HOOD | 2026-11-16 15:08 | mention spike | 23 | 4.71 | 18 | 0 | wallstreetbets 23 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xy146v/comment/19sr069pulcqr/) |
| INTC | 2026-11-17 00:48 | mention spike | 37 | 18.43 | 31 | 0 | wallstreetbets 37 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xyc42m/) |
| IREN | 2026-11-16 18:57 | mention spike | 35 | 12.71 | 31 | 1 | wallstreetbets 35 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xy146v/comment/19srfzqfuiock/) |
| JPM | 2026-11-17 10:05 | mention spike | 10 | 2.71 | 9 | 0 | wallstreetbets 10 | NYSE | #10 | [link](https://www.reddit.com/r/wallstreetbets/comments/1xy71g4/) |
| RCAT | 2026-11-16 22:11 | mention spike | 23 | 0.71 | 20 | 0 | wallstreetbets 22, pennystocks 1 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xyhl51/comment/19srvueyecxlt/) |
| ROPE | 2026-11-17 06:59 | mention spike | 11 | 2.57 | 10 | 0 | wallstreetbets 10, smallstreetbets 1 | NYSE Arca |  | [link](https://www.reddit.com/r/smallstreetbets/comments/1xycnfi/comment/19srdtonkjoma/) |
| SHAZ | 2026-11-17 10:45 | mention spike | 12 | 0.0 | 12 | 0 | wallstreetbets 12 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xyhl51/comment/19srtudesy3oj/) |
| SLS | 2026-11-17 12:33 | mention spike | 86 | 6.57 | 57 | 0 | wallstreetbets 81, pennystocks 5 | Nasdaq | #1 | [link](https://www.reddit.com/r/pennystocks/comments/1xybo6o/comment/19srw1txk6fab/) |
| SNDK | 2026-11-17 10:05 | mention spike | 73 | 34.43 | 50 | 0 | wallstreetbets 70, smallstreetbets 2, pennystocks 1 | Nasdaq |  | [link](https://www.reddit.com/r/pennystocks/comments/1xxs4cy/) |
| TQQQ | 2026-11-17 01:13 | mention spike | 18 | 6.14 | 13 | 0 | wallstreetbets 16, smallstreetbets 2 | Nasdaq |  | [link](https://www.reddit.com/r/smallstreetbets/comments/1xyad7h/) |
| VOO | 2026-11-17 00:31 | mention spike | 36 | 14.43 | 31 | 0 | wallstreetbets 35, smallstreetbets 1 | NYSE Arca |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xy0xor/comment/19srvgke0p32c/) |
| WMT | 2026-11-16 07:17 | mention spike | 22 | 5.0 | 14 | 0 | wallstreetbets 22 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xyhl51/comment/19srs37lxdq8x/) |
| LXEO | 2026-11-16 20:09 | mention spike | 9 | 0.14 | 7 | 0 | pennystocks 7, smallstreetbets 1, wallstreetbets 1 | Nasdaq |  | [link](https://www.reddit.com/r/pennystocks/comments/1xxs8on/) |
| ASTS | 2026-11-17 03:28 | mention spike | 92 | 37.86 | 63 | 0 | wallstreetbets 92 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xxvao9/) |
| RSP | 2026-11-17 03:38 | mention spike | 8 | 2.57 | 8 | 0 | wallstreetbets 8 | NYSE Arca |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xy9o6m/comment/19sr5333e4x1c/) |
| MSTR | 2026-11-13 06:20 | mention spike | 12 | 13.86 | 10 | 0 | wallstreetbets 12 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xy146v/comment/19sr614ae7mwy/) |
| PLTR | 2026-11-16 23:04 | mention spike | 6 | 4.71 | 6 | 0 | wallstreetbets 6 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xy3al4/) |

Full history: `episodes.csv` (one row per first flag, with the numbers known at that moment).
