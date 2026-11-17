# Stage 1 candidates

Updated 2026-11-17T12:43:11Z by run `44085065105`. A candidate is a ticker whose Reddit mentions (or hype-language
posts) in the last 24 hours jumped above its prior 7-day mean + 2 sd, with at least
10 mentions from 5 different authors. It stays listed until it goes
24 hours without a new flag. These are statistical flags, not accusations or advice.

| Ticker | Flagged since (UTC) | Why | Mentions 24h | Baseline/day | Authors | Hype posts | Subreddits | Exchange | StockTwits | Example |
|---|---|---|---|---|---|---|---|---|---|---|
| ANT | 2026-11-16 16:34 | mention spike | 215 | 76.71 | 150 | 0 | wallstreetbets 211, smallstreetbets 3, pennystocks 1 | ? |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xyea8h/) |
| DXYZ | 2026-11-14 23:53 | mention spike | 40 | 6.57 | 19 | 0 | wallstreetbets 39, pennystocks 1 | NYSE |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xy57tm/) |
| HOOD | 2026-11-16 15:08 | mention spike | 25 | 4.43 | 20 | 0 | wallstreetbets 25 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xy146v/comment/19sr069pulcqr/) |
| IREN | 2026-11-16 18:57 | mention spike | 36 | 12.57 | 32 | 1 | wallstreetbets 36 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xy146v/comment/19srfzqfuiock/) |
| JPM | 2026-11-17 10:05 | mention spike | 10 | 2.71 | 9 | 0 | wallstreetbets 10 | NYSE |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xy71g4/) |
| RCAT | 2026-11-16 22:11 | mention spike | 21 | 0.71 | 18 | 0 | wallstreetbets 20, pennystocks 1 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xyhl51/comment/19srqnx00649x/) |
| ROPE | 2026-11-17 06:59 | mention spike | 11 | 2.57 | 10 | 0 | wallstreetbets 10, smallstreetbets 1 | NYSE Arca |  | [link](https://www.reddit.com/r/smallstreetbets/comments/1xycnfi/comment/19srdtonkjoma/) |
| SHAZ | 2026-11-17 10:45 | mention spike | 11 | 0.0 | 11 | 0 | wallstreetbets 11 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xy69bm/comment/19srpiygei06c/) |
| SLS | 2026-11-17 12:33 | mention spike | 43 | 6.43 | 29 | 0 | wallstreetbets 42, pennystocks 1 | Nasdaq | #1 | [link](https://www.reddit.com/r/wallstreetbets/comments/1xyhl51/comment/19srtih5lebkx/) |
| SNDK | 2026-11-17 10:05 | mention spike | 68 | 34.57 | 47 | 0 | wallstreetbets 65, smallstreetbets 2, pennystocks 1 | Nasdaq | #16 | [link](https://www.reddit.com/r/pennystocks/comments/1xxs4cy/) |
| TQQQ | 2026-11-17 01:13 | mention spike | 18 | 6.14 | 13 | 0 | wallstreetbets 16, smallstreetbets 2 | Nasdaq |  | [link](https://www.reddit.com/r/smallstreetbets/comments/1xyad7h/) |
| VOO | 2026-11-17 00:31 | mention spike | 35 | 14.29 | 30 | 0 | wallstreetbets 34, smallstreetbets 1 | NYSE Arca |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xyhl51/comment/19srtbpicoyzp/) |
| WMT | 2026-11-16 07:17 | mention spike | 23 | 4.86 | 15 | 0 | wallstreetbets 23 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xyhl51/comment/19srs37lxdq8x/) |
| INTC | 2026-11-17 00:48 | mention spike | 36 | 18.43 | 30 | 0 | wallstreetbets 36 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xyc42m/) |
| LXEO | 2026-11-16 20:09 | mention spike | 9 | 0.14 | 7 | 0 | pennystocks 7, smallstreetbets 1, wallstreetbets 1 | Nasdaq |  | [link](https://www.reddit.com/r/pennystocks/comments/1xxs8on/) |
| ASTS | 2026-11-17 03:28 | mention spike | 92 | 38.14 | 62 | 0 | wallstreetbets 92 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xxvao9/) |
| RSP | 2026-11-17 03:38 | mention spike | 8 | 2.57 | 8 | 0 | wallstreetbets 8 | NYSE Arca |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xy9o6m/comment/19sr5333e4x1c/) |
| MSTR | 2026-11-13 06:20 | mention spike | 13 | 13.71 | 10 | 0 | wallstreetbets 13 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xy146v/comment/19sr614ae7mwy/) |
| PLTR | 2026-11-16 23:04 | mention spike | 7 | 4.57 | 6 | 0 | wallstreetbets 7 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xy3al4/) |

Full history: `episodes.csv` (one row per first flag, with the numbers known at that moment).
