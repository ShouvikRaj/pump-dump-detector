# Stage 1 candidates

Updated 2026-11-17T15:42:10Z by run `44115334852`. A candidate is a ticker whose Reddit mentions (or hype-language
posts) in the last 24 hours jumped above its prior 7-day mean + 2 sd, with at least
10 mentions from 5 different authors. It stays listed until it goes
24 hours without a new flag. These are statistical flags, not accusations or advice.

| Ticker | Flagged since (UTC) | Why | Mentions 24h | Baseline/day | Authors | Hype posts | Subreddits | Exchange | StockTwits | Example |
|---|---|---|---|---|---|---|---|---|---|---|
| ANT | 2026-11-16 16:34 | mention spike | 201 | 83.0 | 144 | 0 | wallstreetbets 198, smallstreetbets 3 | ? |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xymw8a/) |
| DXYZ | 2026-11-14 23:53 | mention spike | 40 | 7.14 | 22 | 0 | wallstreetbets 39, pennystocks 1 | NYSE |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xy57tm/) |
| HOOD | 2026-11-16 15:08 | mention spike | 19 | 5.57 | 16 | 0 | wallstreetbets 19 | Nasdaq | #17 | [link](https://www.reddit.com/r/wallstreetbets/comments/1xyhl51/comment/19ss0nmqijrc2/) |
| RCAT | 2026-11-16 22:11 | mention spike | 26 | 0.71 | 22 | 0 | wallstreetbets 25, pennystocks 1 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xyhl51/comment/19ss0cmn0xsm8/) |
| ROPE | 2026-11-17 06:59 | mention spike | 12 | 2.57 | 11 | 0 | wallstreetbets 11, smallstreetbets 1 | NYSE Arca |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xyhl51/comment/19sry11oto7xf/) |
| SHAZ | 2026-11-17 10:45 | mention spike | 12 | 0.0 | 12 | 0 | wallstreetbets 12 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xyhl51/comment/19srtudesy3oj/) |
| SLS | 2026-11-17 12:33 | mention spike | 354 | 6.86 | 178 | 0 | wallstreetbets 345, pennystocks 9 | Nasdaq | #1 | [link](https://www.reddit.com/r/wallstreetbets/comments/1xyneg2/) |
| SNDK | 2026-11-17 10:05 | mention spike | 73 | 34.29 | 45 | 0 | wallstreetbets 72, smallstreetbets 1 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xyhl51/comment/19ss10vux3675/) |
| SPAI | 2026-11-17 14:06 | mention spike | 10 | 0.14 | 5 | 0 | pennystocks 9, wallstreetbets 1 | Nasdaq |  | [link](https://www.reddit.com/r/pennystocks/comments/1xybo6o/comment/19srx84qjhk2t/) |
| TQQQ | 2026-11-17 01:13 | mention spike | 18 | 5.86 | 13 | 0 | wallstreetbets 16, smallstreetbets 2 | Nasdaq |  | [link](https://www.reddit.com/r/smallstreetbets/comments/1xyad7h/) |
| VOO | 2026-11-17 00:31 | mention spike | 40 | 14.0 | 34 | 0 | wallstreetbets 39, smallstreetbets 1 | NYSE Arca |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xyhl51/comment/19ss0s09n9qub/) |
| WMT | 2026-11-16 07:17 | mention spike | 18 | 5.57 | 13 | 0 | wallstreetbets 18 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xyhl51/comment/19sryd6u0pqn7/) |
| ASTS | 2026-11-17 03:28 | mention spike | 92 | 37.86 | 66 | 0 | wallstreetbets 92 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xxvao9/) |
| INTC | 2026-11-17 00:48 | mention spike | 35 | 18.57 | 30 | 0 | wallstreetbets 35 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xyc42m/) |
| IREN | 2026-11-16 18:57 | mention spike | 28 | 13.57 | 25 | 1 | wallstreetbets 28 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xy146v/comment/19srfzqfuiock/) |
| JPM | 2026-11-17 10:05 | mention spike | 8 | 3.0 | 8 | 0 | wallstreetbets 8 | NYSE |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xy71g4/) |
| LXEO | 2026-11-16 20:09 | mention spike | 4 | 1.0 | 2 | 0 | pennystocks 4 | Nasdaq |  | [link](https://www.reddit.com/r/pennystocks/comments/1xybo6o/comment/19sry43krvffp/) |
| RSP | 2026-11-17 03:38 | mention spike | 6 | 2.86 | 6 | 0 | wallstreetbets 6 | NYSE Arca |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xy9o6m/comment/19sr5333e4x1c/) |
| MSTR | 2026-11-13 06:20 | mention spike | 12 | 13.86 | 10 | 0 | wallstreetbets 12 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xyhl51/comment/19ss0ix9wj9k3/) |
| PLTR | 2026-11-16 23:04 | mention spike | 6 | 4.71 | 6 | 0 | wallstreetbets 6 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xy3al4/) |

Full history: `episodes.csv` (one row per first flag, with the numbers known at that moment).
