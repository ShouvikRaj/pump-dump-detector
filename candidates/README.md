# Stage 1 candidates

Updated 2026-11-18T16:35:06Z by run `44348401279`. A candidate is a ticker whose Reddit mentions (or hype-language
posts) in the last 24 hours jumped above its prior 7-day mean + 2 sd, with at least
10 mentions from 5 different authors. It stays listed until it goes
24 hours without a new flag. These are statistical flags, not accusations or advice.

| Ticker | Flagged since (UTC) | Why | Mentions 24h | Baseline/day | Authors | Hype posts | Subreddits | Exchange | StockTwits | Example |
|---|---|---|---|---|---|---|---|---|---|---|
| AAOI | 2026-11-17 23:46 | mention spike | 15 | 2.57 | 12 | 0 | wallstreetbets 15 | Nasdaq | #12 | [link](https://www.reddit.com/r/wallstreetbets/comments/1xyw3ym/comment/19ssttybldo84/) |
| SLS | 2026-11-17 12:33 | mention spike | 36 | 59.0 | 32 | 1 | wallstreetbets 30, smallstreetbets 4, pennystocks 2 | Nasdaq | #21 | [link](https://www.reddit.com/r/smallstreetbets/comments/1xz35cy/) |
| SOXX | 2026-11-17 18:16 | mention spike | 4 | 6.57 | 3 | 0 | wallstreetbets 4 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xytkey/) |
| HSBC | 2026-11-17 21:20 | mention spike | 2 | 3.57 | 2 | 0 | wallstreetbets 2 | NYSE |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xyotpf/comment/19ssd6bzfveth/) |
| SHAZ | 2026-11-17 10:45 | mention spike | 3 | 1.71 | 3 | 0 | wallstreetbets 3 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xy69bm/comment/19ss7ome8ctb7/) |
| RCAT | 2026-11-16 22:11 | mention spike | 2 | 4.57 | 2 | 0 | pennystocks 1, wallstreetbets 1 | Nasdaq |  | [link](https://www.reddit.com/r/pennystocks/comments/1xzgmm7/) |
| VOO | 2026-11-17 00:31 | mention spike | 6 | 18.43 | 6 | 0 | wallstreetbets 6 | NYSE Arca |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xzcf9l/comment/19stnv8zs5t1f/) |
| SPAI | 2026-11-17 14:06 | mention spike | 1 | 1.57 | 1 | 0 | pennystocks 1 | Nasdaq |  | [link](https://www.reddit.com/r/pennystocks/comments/1xybo6o/comment/19ss6ec32jk69/) |
| HOOD | 2026-11-16 15:08 | mention spike | 6 | 8.0 | 6 | 0 | wallstreetbets 6 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xyprx3/) |
| ROPE | 2026-11-17 06:59 | mention spike | 1 | 4.0 | 1 | 0 | wallstreetbets 1 | NYSE Arca |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xyw3ym/comment/19ssgj9tbkfz5/) |
| ANT | 2026-11-16 16:34 | mention spike | 83 | 103.57 | 67 | 3 | wallstreetbets 81, pennystocks 2 | ? |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xzg98t/) |
| DXYZ | 2026-11-14 23:53 | mention spike | 4 | 12.71 | 2 | 0 | wallstreetbets 4 | NYSE | #19 | [link](https://www.reddit.com/r/wallstreetbets/comments/1xys9s8/) |
| SPCX | 2026-11-17 16:08 | mention spike | 20 | 51.29 | 18 | 0 | wallstreetbets 20 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xzcf9l/comment/19stn0bs5ym9x/) |
| TQQQ | 2026-11-17 01:13 | mention spike | 11 | 7.71 | 7 | 0 | wallstreetbets 10, smallstreetbets 1 | Nasdaq |  | [link](https://www.reddit.com/r/smallstreetbets/comments/1xz5vej/) |
| ASTS | 2026-11-17 03:28 | mention spike | 17 | 38.43 | 16 | 0 | wallstreetbets 17 | Nasdaq | #13 | [link](https://www.reddit.com/r/wallstreetbets/comments/1xyu4sn/) |
| INTC | 2026-11-17 00:48 | mention spike | 5 | 21.86 | 4 | 0 | wallstreetbets 5 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xyw3ym/comment/19ssvl1ol0noj/) |
| SNDK | 2026-11-17 10:05 | mention spike | 6 | 39.57 | 6 | 0 | wallstreetbets 6 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xyuerk/) |

Full history: `episodes.csv` (one row per first flag, with the numbers known at that moment).
