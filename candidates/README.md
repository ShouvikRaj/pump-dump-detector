# Stage 1 candidates

Updated 2026-11-17T10:05:10Z by run `44060562131`. A candidate is a ticker whose Reddit mentions (or hype-language
posts) in the last 24 hours jumped above its prior 7-day mean + 2 sd, with at least
10 mentions from 5 different authors. It stays listed until it goes
24 hours without a new flag. These are statistical flags, not accusations or advice.

| Ticker | Flagged since (UTC) | Why | Mentions 24h | Baseline/day | Authors | Hype posts | Subreddits | Exchange | StockTwits | Example |
|---|---|---|---|---|---|---|---|---|---|---|
| ANT | 2026-11-16 16:34 | mention spike | 216 | 74.57 | 148 | 1 | wallstreetbets 212, smallstreetbets 3, pennystocks 1 | ? |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xyea8h/) |
| ASTS | 2026-11-17 03:28 | mention spike | 94 | 37.57 | 64 | 0 | wallstreetbets 94 | Nasdaq | #8 | [link](https://www.reddit.com/r/wallstreetbets/comments/1xxvao9/) |
| DXYZ | 2026-11-14 23:53 | mention spike | 40 | 6.57 | 19 | 0 | wallstreetbets 39, pennystocks 1 | NYSE |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xy57tm/) |
| HOOD | 2026-11-16 15:08 | mention spike | 25 | 4.43 | 20 | 0 | wallstreetbets 25 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xy146v/comment/19sr069pulcqr/) |
| INTC | 2026-11-17 00:48 | mention spike | 41 | 17.86 | 32 | 0 | wallstreetbets 41 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xyc42m/) |
| IREN | 2026-11-16 18:57 | mention spike | 46 | 11.14 | 38 | 1 | wallstreetbets 46 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xxnvng/) |
| LXEO | 2026-11-16 20:09 | mention spike | 10 | 0.0 | 7 | 0 | pennystocks 8, smallstreetbets 1, wallstreetbets 1 | Nasdaq |  | [link](https://www.reddit.com/r/pennystocks/comments/1xxs8on/) |
| RCAT | 2026-11-16 22:11 | mention spike | 18 | 0.71 | 15 | 0 | wallstreetbets 17, pennystocks 1 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xy146v/comment/19sqxbogdhio0/) |
| ROPE | 2026-11-17 06:59 | mention spike | 11 | 2.57 | 10 | 0 | wallstreetbets 10, smallstreetbets 1 | NYSE Arca |  | [link](https://www.reddit.com/r/smallstreetbets/comments/1xycnfi/comment/19srdtonkjoma/) |
| TQQQ | 2026-11-17 01:13 | mention spike | 18 | 6.43 | 13 | 0 | wallstreetbets 16, smallstreetbets 2 | Nasdaq |  | [link](https://www.reddit.com/r/smallstreetbets/comments/1xyad7h/) |
| VOO | 2026-11-17 00:31 | mention spike | 35 | 14.14 | 30 | 0 | wallstreetbets 34, smallstreetbets 1 | NYSE Arca |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xy146v/comment/19srlm9did96r/) |
| WMT | 2026-11-16 07:17 | mention spike | 19 | 4.86 | 13 | 0 | wallstreetbets 19 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xy146v/comment/19srevgx2gurn/) |
| JPM | 2026-11-17 10:05 | mention spike | 10 | 2.71 | 9 | 0 | wallstreetbets 10 | NYSE |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xy71g4/) |
| SNDK | 2026-11-17 10:05 | mention spike | 66 | 34.0 | 48 | 0 | wallstreetbets 63, smallstreetbets 2, pennystocks 1 | Nasdaq | #1 | [link](https://www.reddit.com/r/pennystocks/comments/1xxs4cy/) |
| RSP | 2026-11-17 03:38 | mention spike | 9 | 2.43 | 9 | 0 | wallstreetbets 9 | NYSE Arca |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xy9o6m/comment/19sr5333e4x1c/) |
| MSTR | 2026-11-13 06:20 | mention spike | 14 | 13.86 | 11 | 0 | wallstreetbets 14 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xy146v/comment/19sr614ae7mwy/) |
| PLTR | 2026-11-16 23:04 | mention spike | 7 | 4.57 | 6 | 0 | wallstreetbets 7 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xy3al4/) |

Full history: `episodes.csv` (one row per first flag, with the numbers known at that moment).
