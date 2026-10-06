# Stage 1 candidates

Updated 2026-10-06T02:20:00Z by run `37403563675`. A candidate is a ticker whose Reddit mentions (or hype-language
posts) in the last 24 hours jumped above its prior 7-day mean + 2 sd, with at least
10 mentions from 5 different authors. It stays listed until it goes
24 hours without a new flag. These are statistical flags, not accusations or advice.

Warm-up until 2026-10-12T22:41:09Z: part of the baseline was backfilled from the archive rather than
collected live, so flags in this period are marked `warmup=1` in episodes.csv.

| Ticker | Flagged since (UTC) | Why | Mentions 24h | Baseline/day | Authors | Hype posts | Subreddits | Exchange | StockTwits | Example |
|---|---|---|---|---|---|---|---|---|---|---|
| ALEC | 2026-10-05 23:41 | mention spike | 10 | 0.0 | 7 | 0 | pennystocks 10 | Nasdaq |  | [link](https://www.reddit.com/r/pennystocks/comments/1wxyz2p/comment/pe48x59/) |
| APLD | 2026-10-05 14:23 | mention spike | 33 | 12.43 | 21 | 0 | wallstreetbets 33 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1wyj9yn/) |
| DRTS | 2026-10-04 23:23 | mention spike | 16 | 2.71 | 13 | 0 | wallstreetbets 16 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1wyin5e/comment/pe334cu/) |
| GME | 2026-10-05 16:24 | mention spike | 23 | 5.14 | 21 | 0 | wallstreetbets 23 | NYSE |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1wyb83x/) |
| MSFT | 2026-10-05 21:14 | mention spike | 49 | 18.71 | 34 | 0 | wallstreetbets 49 | Nasdaq | #5 | [link](https://www.reddit.com/r/wallstreetbets/comments/1wy8qku/) |
| PMI | 2026-10-05 13:55 | mention spike | 15 | 1.43 | 10 | 0 | wallstreetbets 13, pennystocks 2 | NYSE American |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1wy4mk1/comment/pe1hx05/) |
| QCOM | 2026-10-05 21:14 | mention spike | 11 | 1.86 | 10 | 0 | wallstreetbets 11 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1wy4jnf/) |
| SPCX | 2026-10-05 14:51 | mention spike | 199 | 29.0 | 121 | 1 | wallstreetbets 199 | Nasdaq | #1 | [link](https://www.reddit.com/r/wallstreetbets/comments/1wyqxxo/) |
| TSM | 2026-10-05 15:18 | mention spike | 17 | 4.14 | 13 | 0 | wallstreetbets 17 | NYSE |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1wyin5e/comment/pe4sehv/) |
| VEEA | 2026-10-05 15:33 | mention spike | 23 | 3.57 | 14 | 0 | pennystocks 22, smallstreetbets 1 | Nasdaq |  | [link](https://www.reddit.com/r/smallstreetbets/comments/1wy88kg/) |
| VST | 2026-10-05 04:15 | mention spike | 30 | 8.57 | 16 | 0 | wallstreetbets 30 | NYSE |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1wy4mk1/comment/pe2r92f/) |
| IWM | 2026-10-06 00:59 | mention spike | 14 | 6.71 | 8 | 0 | wallstreetbets 13, smallstreetbets 1 | NYSE Arca |  | [link](https://www.reddit.com/r/smallstreetbets/comments/1wsgx9d/comment/pe4l50h/) |
| DELL | 2026-10-05 16:38 | mention spike | 8 | 6.29 | 6 | 0 | wallstreetbets 8 | NYSE |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1wy4mk1/comment/pe2foyr/) |
| SDEV | 2026-10-05 14:09 | mention spike | 17 | 5.71 | 11 | 0 | wallstreetbets 11, pennystocks 6 | NYSE American |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1wy4mk1/comment/pe2r5x8/) |
| IREN | 2026-10-05 17:49 | mention spike | 11 | 4.71 | 10 | 0 | wallstreetbets 11 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1wyin5e/comment/pe31di3/) |

Full history: `episodes.csv` (one row per first flag, with the numbers known at that moment).
