# Stage 1 candidates

Updated 2026-11-18T13:02:08Z by run `44309271253`. A candidate is a ticker whose Reddit mentions (or hype-language
posts) in the last 24 hours jumped above its prior 7-day mean + 2 sd, with at least
10 mentions from 5 different authors. It stays listed until it goes
24 hours without a new flag. These are statistical flags, not accusations or advice.

| Ticker | Flagged since (UTC) | Why | Mentions 24h | Baseline/day | Authors | Hype posts | Subreddits | Exchange | StockTwits | Example |
|---|---|---|---|---|---|---|---|---|---|---|
| AAOI | 2026-11-17 23:46 | mention spike | 16 | 2.71 | 13 | 0 | wallstreetbets 16 | Nasdaq | #2 | [link](https://www.reddit.com/r/wallstreetbets/comments/1xyw3ym/comment/19ssttybldo84/) |
| SLS | 2026-11-17 12:33 | mention spike | 353 | 13.57 | 194 | 1 | wallstreetbets 337, pennystocks 11, smallstreetbets 5 | Nasdaq |  | [link](https://www.reddit.com/r/smallstreetbets/comments/1xz35cy/) |
| SOXX | 2026-11-17 18:16 | mention spike | 7 | 6.43 | 5 | 0 | wallstreetbets 7 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xytkey/) |
| HSBC | 2026-11-17 21:20 | mention spike | 2 | 3.57 | 2 | 0 | wallstreetbets 2 | NYSE |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xyotpf/comment/19ssd6bzfveth/) |
| SHAZ | 2026-11-17 10:45 | mention spike | 3 | 1.71 | 3 | 0 | wallstreetbets 3 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xy69bm/comment/19ss7ome8ctb7/) |
| RCAT | 2026-11-16 22:11 | mention spike | 8 | 3.57 | 8 | 0 | wallstreetbets 7, smallstreetbets 1 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xyhl51/comment/19ss66e2zkd9h/) |
| VOO | 2026-11-17 00:31 | mention spike | 9 | 18.0 | 9 | 0 | wallstreetbets 9 | NYSE Arca |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xyw3ym/comment/19ssjsq5f5rds/) |
| SPAI | 2026-11-17 14:06 | mention spike | 2 | 1.43 | 2 | 0 | pennystocks 2 | Nasdaq |  | [link](https://www.reddit.com/r/pennystocks/comments/1xybo6o/comment/19ss6ec32jk69/) |
| HOOD | 2026-11-16 15:08 | mention spike | 7 | 7.86 | 7 | 0 | wallstreetbets 7 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xyprx3/) |
| ROPE | 2026-11-17 06:59 | mention spike | 3 | 3.71 | 3 | 0 | wallstreetbets 3 | NYSE Arca |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xyw3ym/comment/19ssgj9tbkfz5/) |
| ANT | 2026-11-16 16:34 | mention spike | 92 | 104.14 | 76 | 2 | wallstreetbets 90, pennystocks 2 | ? |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xz744l/) |
| DXYZ | 2026-11-14 23:53 | mention spike | 8 | 12.29 | 6 | 0 | wallstreetbets 8 | NYSE |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xys9s8/) |
| SPCX | 2026-11-17 16:08 | mention spike | 33 | 53.29 | 30 | 0 | wallstreetbets 33 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xyw3ym/comment/19sthab5zs1d1/) |
| TQQQ | 2026-11-17 01:13 | mention spike | 14 | 7.29 | 9 | 0 | wallstreetbets 13, smallstreetbets 1 | Nasdaq |  | [link](https://www.reddit.com/r/smallstreetbets/comments/1xz5vej/) |
| ASTS | 2026-11-17 03:28 | mention spike | 24 | 38.57 | 20 | 0 | wallstreetbets 24 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xyu4sn/) |
| INTC | 2026-11-17 00:48 | mention spike | 10 | 21.57 | 9 | 0 | wallstreetbets 10 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xyw3ym/comment/19ssvl1ol0noj/) |
| SNDK | 2026-11-17 10:05 | mention spike | 20 | 38.29 | 15 | 0 | wallstreetbets 20 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xyuerk/) |
| WMT | 2026-11-16 07:17 | mention spike | 4 | 7.86 | 4 | 0 | wallstreetbets 4 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xyw3ym/comment/19ssttzowvi01/) |
| IREN | 2026-11-16 18:57 | mention spike | 11 | 17.29 | 8 | 0 | wallstreetbets 11 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xyqacj/) |
| JPM | 2026-11-17 10:05 | mention spike | 0 |  | 0 | 0 |  | NYSE |  |  |

Full history: `episodes.csv` (one row per first flag, with the numbers known at that moment).
