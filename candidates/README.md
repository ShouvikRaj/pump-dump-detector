# Stage 1 candidates

Updated 2026-11-16T21:12:09Z by run `43950234771`. A candidate is a ticker whose Reddit mentions (or hype-language
posts) in the last 24 hours jumped above its prior 7-day mean + 2 sd, with at least
10 mentions from 5 different authors. It stays listed until it goes
24 hours without a new flag. These are statistical flags, not accusations or advice.

| Ticker | Flagged since (UTC) | Why | Mentions 24h | Baseline/day | Authors | Hype posts | Subreddits | Exchange | StockTwits | Example |
|---|---|---|---|---|---|---|---|---|---|---|
| ANT | 2026-11-16 16:34 | mention spike | 190 | 69.14 | 127 | 1 | wallstreetbets 187, smallstreetbets 2, pennystocks 1 | ? |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xxfkdl/) |
| HOOD | 2026-11-16 15:08 | mention spike | 18 | 4.0 | 17 | 0 | wallstreetbets 18 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xy0xor/comment/19sqnq6r7sssk/) |
| IREN | 2026-11-16 18:57 | mention spike | 31 | 11.29 | 26 | 0 | wallstreetbets 31 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xxnvng/) |
| LXEO | 2026-11-16 20:09 | mention spike | 10 | 0.0 | 7 | 0 | pennystocks 8, smallstreetbets 1, wallstreetbets 1 | Nasdaq |  | [link](https://www.reddit.com/r/pennystocks/comments/1xxs8on/) |
| WMT | 2026-11-16 07:17 | mention spike | 22 | 3.86 | 16 | 0 | wallstreetbets 22 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xy146v/comment/19sqnv4s8a30j/) |
| MSTR | 2026-11-13 06:20 | mention spike | 24 | 12.14 | 18 | 0 | wallstreetbets 24 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xy0xor/comment/19sqnq6r7sssk/) |
| ASML | 2026-11-15 23:05 | mention spike | 2 | 8.14 | 2 | 0 | wallstreetbets 2 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xxmkhj/comment/19sqglnoa8jid/) |
| DXYZ | 2026-11-14 23:53 | mention spike | 27 | 6.14 | 16 | 0 | wallstreetbets 27 | NYSE | #28 | [link](https://www.reddit.com/r/wallstreetbets/comments/1xy146v/comment/19sqnupybhebo/) |
| COIN | 2026-11-15 21:05 | mention spike | 7 | 2.14 | 6 | 0 | wallstreetbets 7 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xxmkhj/comment/19sqd28qleuh0/) |

Full history: `episodes.csv` (one row per first flag, with the numbers known at that moment).
