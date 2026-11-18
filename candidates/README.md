# Stage 1 candidates

Updated 2026-11-18T17:57:06Z by run `44363412205`. A candidate is a ticker whose Reddit mentions (or hype-language
posts) in the last 24 hours jumped above its prior 7-day mean + 2 sd, with at least
10 mentions from 5 different authors. It stays listed until it goes
24 hours without a new flag. These are statistical flags, not accusations or advice.

| Ticker | Flagged since (UTC) | Why | Mentions 24h | Baseline/day | Authors | Hype posts | Subreddits | Exchange | StockTwits | Example |
|---|---|---|---|---|---|---|---|---|---|---|
| AAOI | 2026-11-17 23:46 | mention spike | 16 | 2.43 | 13 | 0 | wallstreetbets 16 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xzcf9l/comment/19stwasgs4n5v/) |
| UNH | 2026-11-18 17:15 | mention spike | 11 | 2.29 | 8 | 0 | wallstreetbets 11 | NYSE | #2 | [link](https://www.reddit.com/r/wallstreetbets/comments/1xzcf9l/comment/19stx62yn4z7n/) |
| SLS | 2026-11-17 12:33 | mention spike | 24 | 60.86 | 20 | 0 | wallstreetbets 18, smallstreetbets 4, pennystocks 2 | Nasdaq | #8 | [link](https://www.reddit.com/r/smallstreetbets/comments/1xz35cy/) |
| SOXX | 2026-11-17 18:16 | mention spike | 3 | 6.86 | 2 | 0 | wallstreetbets 3 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xytkey/) |
| HSBC | 2026-11-17 21:20 | mention spike | 1 | 3.71 | 1 | 0 | wallstreetbets 1 | NYSE |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xyotpf/comment/19ssd6bzfveth/) |
| SHAZ | 2026-11-17 10:45 | mention spike | 0 |  | 0 | 0 |  | Nasdaq |  |  |
| RCAT | 2026-11-16 22:11 | mention spike | 1 | 4.71 | 1 | 0 | pennystocks 1 | Nasdaq |  | [link](https://www.reddit.com/r/pennystocks/comments/1xzgmm7/) |
| VOO | 2026-11-17 00:31 | mention spike | 6 | 18.29 | 6 | 0 | wallstreetbets 6 | NYSE Arca |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xzcf9l/comment/19stwe2hbffb7/) |
| SPAI | 2026-11-17 14:06 | mention spike | 0 |  | 0 | 0 |  | Nasdaq |  |  |
| HOOD | 2026-11-16 15:08 | mention spike | 2 | 8.57 | 2 | 0 | wallstreetbets 2 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xzcf9l/comment/19stmyv50hxz6/) |
| ROPE | 2026-11-17 06:59 | mention spike | 1 | 4.0 | 1 | 0 | wallstreetbets 1 | NYSE Arca |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xyw3ym/comment/19ssgj9tbkfz5/) |
| ANT | 2026-11-16 16:34 | mention spike | 109 | 104.29 | 86 | 4 | wallstreetbets 108, pennystocks 1 | ? |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xzg98t/) |
| DXYZ | 2026-11-14 23:53 | mention spike | 3 | 12.86 | 2 | 0 | wallstreetbets 3 | NYSE |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xys9s8/) |
| SPCX | 2026-11-17 16:08 | mention spike | 19 | 51.43 | 18 | 0 | wallstreetbets 19 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xzcf9l/comment/19stx8amhb8sk/) |
| TQQQ | 2026-11-17 01:13 | mention spike | 7 | 8.29 | 5 | 0 | wallstreetbets 6, smallstreetbets 1 | Nasdaq |  | [link](https://www.reddit.com/r/smallstreetbets/comments/1xz5vej/) |
| ASTS | 2026-11-17 03:28 | mention spike | 16 | 37.86 | 16 | 0 | wallstreetbets 16 | Nasdaq | #1 | [link](https://www.reddit.com/r/wallstreetbets/comments/1xzkt71/) |

Full history: `episodes.csv` (one row per first flag, with the numbers known at that moment).
