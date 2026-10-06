# Stage 1 candidates

Updated 2026-10-06T05:25:42Z by run `37418434447`. A candidate is a ticker whose Reddit mentions (or hype-language
posts) in the last 24 hours jumped above its prior 7-day mean + 2 sd, with at least
10 mentions from 5 different authors. It stays listed until it goes
24 hours without a new flag. These are statistical flags, not accusations or advice.

Warm-up until 2026-10-12T22:41:09Z: part of the baseline was backfilled from the archive rather than
collected live, so flags in this period are marked `warmup=1` in episodes.csv.

| Ticker | Flagged since (UTC) | Why | Mentions 24h | Baseline/day | Authors | Hype posts | Subreddits | Exchange | StockTwits | Example |
|---|---|---|---|---|---|---|---|---|---|---|
| ALEC | 2026-10-05 23:41 | mention spike | 10 | 0.0 | 7 | 0 | pennystocks 10 | Nasdaq |  | [link](https://www.reddit.com/r/pennystocks/comments/1wxyz2p/comment/pe48x59/) |
| APLD | 2026-10-05 14:23 | mention spike | 39 | 13.14 | 21 | 0 | wallstreetbets 39 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1wyj9yn/) |
| DRTS | 2026-10-04 23:23 | mention spike | 14 | 3.0 | 11 | 0 | wallstreetbets 14 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1wyin5e/comment/pe334cu/) |
| GME | 2026-10-05 16:24 | mention spike | 24 | 5.29 | 21 | 0 | wallstreetbets 24 | NYSE |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1wyrlbr/) |
| MSFT | 2026-10-05 21:14 | mention spike | 46 | 19.43 | 32 | 0 | wallstreetbets 46 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1wy8qku/) |
| QCOM | 2026-10-05 21:14 | mention spike | 10 | 2.0 | 9 | 0 | wallstreetbets 10 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1wy4jnf/) |
| SPCX | 2026-10-05 14:51 | mention spike | 204 | 29.57 | 123 | 1 | wallstreetbets 204 | Nasdaq | #1 | [link](https://www.reddit.com/r/wallstreetbets/comments/1wyqxxo/) |
| TSM | 2026-10-05 15:18 | mention spike | 17 | 4.14 | 13 | 0 | wallstreetbets 17 | NYSE |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1wyin5e/comment/pe4sehv/) |
| VEEA | 2026-10-05 15:33 | mention spike | 24 | 3.57 | 14 | 0 | pennystocks 23, smallstreetbets 1 | Nasdaq |  | [link](https://www.reddit.com/r/smallstreetbets/comments/1wy88kg/) |
| IREN | 2026-10-05 17:49 | mention spike | 9 | 5.0 | 9 | 0 | wallstreetbets 9 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1wyin5e/comment/pe31di3/) |
| PMI | 2026-10-05 13:55 | mention spike | 2 | 0.29 | 1 | 0 | pennystocks 2 | NYSE American |  | [link](https://www.reddit.com/r/pennystocks/comments/1wxyz2p/comment/pe0qett/) |
| VST | 2026-10-05 04:15 | mention spike | 19 | 10.43 | 14 | 0 | wallstreetbets 19 | NYSE |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1wyin5e/comment/pe5pwnh/) |
| IWM | 2026-10-06 00:59 | mention spike | 14 | 6.71 | 8 | 0 | wallstreetbets 13, smallstreetbets 1 | NYSE Arca | #2 | [link](https://www.reddit.com/r/smallstreetbets/comments/1wsgx9d/comment/pe4l50h/) |
| DELL | 2026-10-05 16:38 | mention spike | 8 | 6.29 | 6 | 0 | wallstreetbets 8 | NYSE |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1wy4mk1/comment/pe2foyr/) |
| SDEV | 2026-10-05 14:09 | mention spike | 16 | 5.86 | 10 | 0 | wallstreetbets 11, pennystocks 5 | NYSE American |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1wy4mk1/comment/pe2r5x8/) |

Full history: `episodes.csv` (one row per first flag, with the numbers known at that moment).
