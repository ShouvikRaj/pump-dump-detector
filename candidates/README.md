# Stage 1 candidates

Updated 2026-11-08T08:18:07Z by run `42462005840`. A candidate is a ticker whose Reddit mentions (or hype-language
posts) in the last 24 hours jumped above its prior 7-day mean + 2 sd, with at least
10 mentions from 5 different authors. It stays listed until it goes
24 hours without a new flag. These are statistical flags, not accusations or advice.

| Ticker | Flagged since (UTC) | Why | Mentions 24h | Baseline/day | Authors | Hype posts | Subreddits | Exchange | StockTwits | Example |
|---|---|---|---|---|---|---|---|---|---|---|
| GRND | 2026-11-06 18:01 | mention spike | 2 | 3.43 | 2 | 0 | wallstreetbets 2 | NYSE |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xpgjl2/comment/19sb84c91xm91/) |
| ORCL | 2026-11-06 18:13 | mention spike | 5 | 21.0 | 3 | 0 | wallstreetbets 5 | NYSE |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xoj597/comment/19sam6ng7avi8/) |
| LUNR | 2026-11-06 20:47 | mention spike | 1 | 4.43 | 1 | 0 | wallstreetbets 1 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xpjj4e/comment/19sa3dpxndq3k/) |
| SPCE | 2026-11-07 02:18 | mention spike | 1 | 3.0 | 1 | 0 | wallstreetbets 1 | NYSE |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xpjj4e/comment/19sa3dpxndq3k/) |
| RKLB | 2026-11-07 03:40 | mention spike | 12 | 19.86 | 10 | 0 | wallstreetbets 11, smallstreetbets 1 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xpo1gj/comment/19sbesn3tya3n/) |
| OKLO | 2026-11-05 13:17 | mention spike | 2 | 8.57 | 2 | 0 | wallstreetbets 2 | NYSE | #2 | [link](https://www.reddit.com/r/wallstreetbets/comments/1xpo1gj/comment/19sbesn3tya3n/) |
| WDC | 2026-11-06 16:54 | mention spike | 6 | 4.71 | 5 | 0 | wallstreetbets 6 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xqddim/) |
| VIVK | 2026-11-06 18:22 | mention spike | 0 |  | 0 | 0 |  | Nasdaq |  |  |
| DKNG | 2026-11-06 14:52 | mention spike | 1 | 2.57 | 1 | 0 | pennystocks 1 | Nasdaq |  | [link](https://www.reddit.com/r/pennystocks/comments/1xpy130/comment/19s9xztdhcf1d/) |
| GME | 2026-11-07 11:05 | mention spike | 3 | 9.43 | 3 | 0 | wallstreetbets 3 | NYSE |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xotkmz/comment/19saqjzm28483/) |
| INOD | 2026-11-06 15:46 | mention spike | 0 |  | 0 | 0 |  | Nasdaq |  |  |

Full history: `episodes.csv` (one row per first flag, with the numbers known at that moment).
