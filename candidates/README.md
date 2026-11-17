# Stage 1 candidates

Updated 2026-11-17T01:25:10Z by run `43994895970`. A candidate is a ticker whose Reddit mentions (or hype-language
posts) in the last 24 hours jumped above its prior 7-day mean + 2 sd, with at least
10 mentions from 5 different authors. It stays listed until it goes
24 hours without a new flag. These are statistical flags, not accusations or advice.

| Ticker | Flagged since (UTC) | Why | Mentions 24h | Baseline/day | Authors | Hype posts | Subreddits | Exchange | StockTwits | Example |
|---|---|---|---|---|---|---|---|---|---|---|
| ANT | 2026-11-16 16:34 | mention spike | 218 | 70.0 | 145 | 1 | wallstreetbets 215, smallstreetbets 2, pennystocks 1 | ? |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xy3do2/) |
| DXYZ | 2026-11-14 23:53 | mention spike | 42 | 6.14 | 21 | 0 | wallstreetbets 41, pennystocks 1 | NYSE |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xy57tm/) |
| HOOD | 2026-11-16 15:08 | mention spike | 27 | 4.0 | 22 | 0 | wallstreetbets 27 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xy146v/comment/19sqxh0nd8erm/) |
| INTC | 2026-11-17 00:48 | mention spike | 43 | 18.0 | 32 | 0 | wallstreetbets 43 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xy146v/comment/19sqynxzq26yt/) |
| IREN | 2026-11-16 18:57 | mention spike | 45 | 11.29 | 36 | 0 | wallstreetbets 45 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xxnvng/) |
| LXEO | 2026-11-16 20:09 | mention spike | 10 | 0.0 | 7 | 0 | pennystocks 8, smallstreetbets 1, wallstreetbets 1 | Nasdaq |  | [link](https://www.reddit.com/r/pennystocks/comments/1xxs8on/) |
| RCAT | 2026-11-16 22:11 | mention spike | 18 | 0.71 | 15 | 0 | wallstreetbets 17, pennystocks 1 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xy146v/comment/19sqxbogdhio0/) |
| TQQQ | 2026-11-17 01:13 | mention spike | 17 | 6.57 | 12 | 0 | wallstreetbets 16, smallstreetbets 1 | Nasdaq |  | [link](https://www.reddit.com/r/smallstreetbets/comments/1xxs7fo/comment/19sqvxtlmjjj9/) |
| VOO | 2026-11-17 00:31 | mention spike | 31 | 14.29 | 28 | 0 | wallstreetbets 30, smallstreetbets 1 | NYSE Arca |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xxdbjy/) |
| WMT | 2026-11-16 07:17 | mention spike | 23 | 4.0 | 16 | 0 | wallstreetbets 23 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xy146v/comment/19squklj78sld/) |
| MSTR | 2026-11-13 06:20 | mention spike | 18 | 13.29 | 14 | 0 | wallstreetbets 18 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xy146v/comment/19sqr3qq1lr5t/) |
| PLTR | 2026-11-16 23:04 | mention spike | 9 | 4.29 | 7 | 0 | wallstreetbets 9 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xy3al4/) |

Full history: `episodes.csv` (one row per first flag, with the numbers known at that moment).
