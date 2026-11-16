# Stage 1 candidates

Updated 2026-11-16T23:53:08Z by run `43982382573`. A candidate is a ticker whose Reddit mentions (or hype-language
posts) in the last 24 hours jumped above its prior 7-day mean + 2 sd, with at least
10 mentions from 5 different authors. It stays listed until it goes
24 hours without a new flag. These are statistical flags, not accusations or advice.

| Ticker | Flagged since (UTC) | Why | Mentions 24h | Baseline/day | Authors | Hype posts | Subreddits | Exchange | StockTwits | Example |
|---|---|---|---|---|---|---|---|---|---|---|
| ANT | 2026-11-16 16:34 | mention spike | 207 | 69.43 | 137 | 1 | wallstreetbets 204, smallstreetbets 2, pennystocks 1 | ? |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xy3do2/) |
| DXYZ | 2026-11-14 23:53 | mention spike | 39 | 6.14 | 19 | 0 | wallstreetbets 38, pennystocks 1 | NYSE | #29 | [link](https://www.reddit.com/r/wallstreetbets/comments/1xy3do2/) |
| HOOD | 2026-11-16 15:08 | mention spike | 26 | 4.0 | 22 | 0 | wallstreetbets 26 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xy146v/comment/19sqs2r5om01x/) |
| IREN | 2026-11-16 18:57 | mention spike | 41 | 11.29 | 33 | 0 | wallstreetbets 41 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xxnvng/) |
| LXEO | 2026-11-16 20:09 | mention spike | 10 | 0.0 | 7 | 0 | pennystocks 8, smallstreetbets 1, wallstreetbets 1 | Nasdaq |  | [link](https://www.reddit.com/r/pennystocks/comments/1xxs8on/) |
| RCAT | 2026-11-16 22:11 | mention spike | 13 | 0.71 | 11 | 0 | wallstreetbets 12, pennystocks 1 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xy146v/comment/19sqryyudl8zp/) |
| WMT | 2026-11-16 07:17 | mention spike | 24 | 3.86 | 17 | 0 | wallstreetbets 24 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xy146v/comment/19squklj78sld/) |
| MSTR | 2026-11-13 06:20 | mention spike | 21 | 12.86 | 17 | 0 | wallstreetbets 21 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xy146v/comment/19sqr3qq1lr5t/) |
| PLTR | 2026-11-16 23:04 | mention spike | 9 | 4.57 | 7 | 0 | wallstreetbets 9 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xy3al4/) |
| ASML | 2026-11-15 23:05 | mention spike | 1 | 8.29 | 1 | 0 | wallstreetbets 1 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xxmkhj/comment/19sqglnoa8jid/) |

Full history: `episodes.csv` (one row per first flag, with the numbers known at that moment).
