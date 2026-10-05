# Stage 1 candidates

Updated 2026-10-05T19:29:28Z by run `37363568864`. A candidate is a ticker whose Reddit mentions (or hype-language
posts) in the last 24 hours jumped above its prior 7-day mean + 2 sd, with at least
10 mentions from 5 different authors. It stays listed until it goes
24 hours without a new flag. These are statistical flags, not accusations or advice.

Warm-up until 2026-10-12T22:41:09Z: part of the baseline was backfilled from the archive rather than
collected live, so flags in this period are marked `warmup=1` in episodes.csv.

| Ticker | Flagged since (UTC) | Why | Mentions 24h | Baseline/day | Authors | Hype posts | Subreddits | Exchange | StockTwits | Example |
|---|---|---|---|---|---|---|---|---|---|---|
| APLD | 2026-10-05 14:23 | mention spike | 35 | 11.14 | 21 | 0 | wallstreetbets 34, smallstreetbets 1 | Nasdaq | #5 | [link](https://www.reddit.com/r/wallstreetbets/comments/1wxycup/) |
| DELL | 2026-10-05 16:38 | mention spike | 14 | 5.43 | 7 | 0 | wallstreetbets 14 | NYSE |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1wy4mk1/comment/pe2foyr/) |
| DRTS | 2026-10-04 23:23 | mention spike | 18 | 2.0 | 16 | 1 | wallstreetbets 18 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1wxl6cr/comment/pe28r62/) |
| GME | 2026-10-05 16:24 | mention spike | 24 | 4.71 | 21 | 0 | wallstreetbets 23, smallstreetbets 1 | NYSE |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1wyb83x/) |
| IREN | 2026-10-05 17:49 | mention spike | 11 | 4.43 | 9 | 0 | wallstreetbets 11 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1wy4mk1/comment/pe2oqsm/) |
| PMI | 2026-10-05 13:55 | mention spike | 15 | 1.43 | 10 | 0 | wallstreetbets 13, pennystocks 2 | NYSE American |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1wy4mk1/comment/pe1hx05/) |
| SDEV | 2026-10-05 14:09 | mention spike | 20 | 5.29 | 14 | 0 | wallstreetbets 12, pennystocks 8 | NYSE American |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1wy4mk1/comment/pe2r5x8/) |
| SPCX | 2026-10-05 14:51 | mention spike | 119 | 29.14 | 72 | 1 | wallstreetbets 119 | Nasdaq | #4 | [link](https://www.reddit.com/r/wallstreetbets/comments/1wybz2w/) |
| TSM | 2026-10-05 15:18 | mention spike | 14 | 4.29 | 11 | 0 | wallstreetbets 14 | NYSE | #9 | [link](https://www.reddit.com/r/wallstreetbets/comments/1wy4mk1/comment/pe2luu3/) |
| VEEA | 2026-10-05 15:33 | mention spike | 21 | 3.43 | 12 | 0 | pennystocks 20, smallstreetbets 1 | Nasdaq |  | [link](https://www.reddit.com/r/smallstreetbets/comments/1wy88kg/) |
| VST | 2026-10-05 04:15 | mention spike | 47 | 6.14 | 25 | 0 | wallstreetbets 47 | NYSE | #24 | [link](https://www.reddit.com/r/wallstreetbets/comments/1wy4mk1/comment/pe2r92f/) |

Full history: `episodes.csv` (one row per first flag, with the numbers known at that moment).
