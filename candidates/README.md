# Stage 1 candidates

Updated 2026-11-18T17:15:11Z by run `44356008751`. A candidate is a ticker whose Reddit mentions (or hype-language
posts) in the last 24 hours jumped above its prior 7-day mean + 2 sd, with at least
10 mentions from 5 different authors. It stays listed until it goes
24 hours without a new flag. These are statistical flags, not accusations or advice.

| Ticker | Flagged since (UTC) | Why | Mentions 24h | Baseline/day | Authors | Hype posts | Subreddits | Exchange | StockTwits | Example |
|---|---|---|---|---|---|---|---|---|---|---|
| AAOI | 2026-11-17 23:46 | mention spike | 16 | 2.43 | 13 | 0 | wallstreetbets 16 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xzcf9l/comment/19stwasgs4n5v/) |
| UNH | 2026-11-18 17:15 | mention spike | 11 | 2.29 | 8 | 0 | wallstreetbets 11 | NYSE | #3 | [link](https://www.reddit.com/r/wallstreetbets/comments/1xzcf9l/comment/19stx62yn4z7n/) |
| SLS | 2026-11-17 12:33 | mention spike | 27 | 60.57 | 23 | 0 | wallstreetbets 21, smallstreetbets 4, pennystocks 2 | Nasdaq | #4 | [link](https://www.reddit.com/r/smallstreetbets/comments/1xz35cy/) |
| SOXX | 2026-11-17 18:16 | mention spike | 4 | 6.71 | 3 | 0 | wallstreetbets 4 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xytkey/) |
| HSBC | 2026-11-17 21:20 | mention spike | 1 | 3.71 | 1 | 0 | wallstreetbets 1 | NYSE |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xyotpf/comment/19ssd6bzfveth/) |
| SHAZ | 2026-11-17 10:45 | mention spike | 3 | 1.71 | 3 | 0 | wallstreetbets 3 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xy69bm/comment/19ss7ome8ctb7/) |
| RCAT | 2026-11-16 22:11 | mention spike | 2 | 4.57 | 2 | 0 | pennystocks 1, wallstreetbets 1 | Nasdaq |  | [link](https://www.reddit.com/r/pennystocks/comments/1xzgmm7/) |
| VOO | 2026-11-17 00:31 | mention spike | 7 | 18.43 | 7 | 0 | wallstreetbets 7 | NYSE Arca |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xzcf9l/comment/19stwe2hbffb7/) |
| SPAI | 2026-11-17 14:06 | mention spike | 1 | 1.57 | 1 | 0 | pennystocks 1 | Nasdaq |  | [link](https://www.reddit.com/r/pennystocks/comments/1xybo6o/comment/19ss6ec32jk69/) |
| HOOD | 2026-11-16 15:08 | mention spike | 4 | 8.29 | 4 | 0 | wallstreetbets 4 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xzcf9l/comment/19stmyv50hxz6/) |
| ROPE | 2026-11-17 06:59 | mention spike | 1 | 4.0 | 1 | 0 | wallstreetbets 1 | NYSE Arca |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xyw3ym/comment/19ssgj9tbkfz5/) |
| ANT | 2026-11-16 16:34 | mention spike | 121 | 103.43 | 92 | 4 | wallstreetbets 119, pennystocks 2 | ? |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xzg98t/) |
| DXYZ | 2026-11-14 23:53 | mention spike | 4 | 12.71 | 2 | 0 | wallstreetbets 4 | NYSE |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xys9s8/) |
| SPCX | 2026-11-17 16:08 | mention spike | 24 | 51.43 | 22 | 0 | wallstreetbets 24 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xzcf9l/comment/19stx8amhb8sk/) |
| TQQQ | 2026-11-17 01:13 | mention spike | 7 | 8.29 | 5 | 0 | wallstreetbets 6, smallstreetbets 1 | Nasdaq |  | [link](https://www.reddit.com/r/smallstreetbets/comments/1xz5vej/) |
| ASTS | 2026-11-17 03:28 | mention spike | 17 | 38.29 | 16 | 0 | wallstreetbets 17 | Nasdaq | #2 | [link](https://www.reddit.com/r/wallstreetbets/comments/1xyu4sn/) |
| INTC | 2026-11-17 00:48 | mention spike | 5 | 21.86 | 4 | 0 | wallstreetbets 5 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xyw3ym/comment/19ssvl1ol0noj/) |

Full history: `episodes.csv` (one row per first flag, with the numbers known at that moment).
