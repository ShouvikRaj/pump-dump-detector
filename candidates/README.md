# Stage 1 candidates

Updated 2026-10-05T21:39:52Z by run `37377267990`. A candidate is a ticker whose Reddit mentions (or hype-language
posts) in the last 24 hours jumped above its prior 7-day mean + 2 sd, with at least
10 mentions from 5 different authors. It stays listed until it goes
24 hours without a new flag. These are statistical flags, not accusations or advice.

Warm-up until 2026-10-12T22:41:09Z: part of the baseline was backfilled from the archive rather than
collected live, so flags in this period are marked `warmup=1` in episodes.csv.

| Ticker | Flagged since (UTC) | Why | Mentions 24h | Baseline/day | Authors | Hype posts | Subreddits | Exchange | StockTwits | Example |
|---|---|---|---|---|---|---|---|---|---|---|
| APLD | 2026-10-05 14:23 | mention spike | 40 | 11.14 | 25 | 0 | wallstreetbets 39, smallstreetbets 1 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1wyj9yn/) |
| DELL | 2026-10-05 16:38 | mention spike | 14 | 5.43 | 7 | 0 | wallstreetbets 14 | NYSE |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1wy4mk1/comment/pe2foyr/) |
| DRTS | 2026-10-04 23:23 | mention spike | 18 | 2.43 | 15 | 1 | wallstreetbets 18 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1wyin5e/comment/pe334cu/) |
| GME | 2026-10-05 16:24 | mention spike | 25 | 4.71 | 22 | 0 | wallstreetbets 24, smallstreetbets 1 | NYSE |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1wyb83x/) |
| IREN | 2026-10-05 17:49 | mention spike | 12 | 4.57 | 11 | 0 | wallstreetbets 12 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1wyin5e/comment/pe31di3/) |
| MSFT | 2026-10-05 21:14 | mention spike | 50 | 20.14 | 34 | 0 | wallstreetbets 50 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1wy8qku/) |
| PMI | 2026-10-05 13:55 | mention spike | 15 | 1.43 | 10 | 0 | wallstreetbets 13, pennystocks 2 | NYSE American |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1wy4mk1/comment/pe1hx05/) |
| QCOM | 2026-10-05 21:14 | mention spike | 11 | 1.86 | 10 | 0 | wallstreetbets 11 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1wy4jnf/) |
| SDEV | 2026-10-05 14:09 | mention spike | 20 | 5.29 | 14 | 0 | wallstreetbets 12, pennystocks 8 | NYSE American |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1wy4mk1/comment/pe2r5x8/) |
| SPCX | 2026-10-05 14:51 | mention spike | 173 | 29.29 | 105 | 1 | wallstreetbets 173 | Nasdaq | #1 | [link](https://www.reddit.com/r/wallstreetbets/comments/1wykai5/) |
| TSM | 2026-10-05 15:18 | mention spike | 16 | 4.14 | 12 | 0 | wallstreetbets 16 | NYSE | #24 | [link](https://www.reddit.com/r/wallstreetbets/comments/1wykai5/comment/pe3gzgl/) |
| VEEA | 2026-10-05 15:33 | mention spike | 22 | 3.57 | 13 | 0 | pennystocks 21, smallstreetbets 1 | Nasdaq |  | [link](https://www.reddit.com/r/smallstreetbets/comments/1wy88kg/) |
| VST | 2026-10-05 04:15 | mention spike | 46 | 6.29 | 25 | 0 | wallstreetbets 46 | NYSE | #25 | [link](https://www.reddit.com/r/wallstreetbets/comments/1wy4mk1/comment/pe2r92f/) |

Full history: `episodes.csv` (one row per first flag, with the numbers known at that moment).
