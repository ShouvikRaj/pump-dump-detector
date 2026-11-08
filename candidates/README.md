# Stage 1 candidates

Updated 2026-11-08T14:43:11Z by run `42490732642`. A candidate is a ticker whose Reddit mentions (or hype-language
posts) in the last 24 hours jumped above its prior 7-day mean + 2 sd, with at least
10 mentions from 5 different authors. It stays listed until it goes
24 hours without a new flag. These are statistical flags, not accusations or advice.

| Ticker | Flagged since (UTC) | Why | Mentions 24h | Baseline/day | Authors | Hype posts | Subreddits | Exchange | StockTwits | Example |
|---|---|---|---|---|---|---|---|---|---|---|
| GRND | 2026-11-06 18:01 | mention spike | 2 | 3.43 | 2 | 0 | wallstreetbets 2 | NYSE |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xpgjl2/comment/19sb84c91xm91/) |
| ORCL | 2026-11-06 18:13 | mention spike | 3 | 21.43 | 3 | 0 | wallstreetbets 3 | NYSE |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xqttdj/comment/19sbh91zyfxno/) |
| LUNR | 2026-11-06 20:47 | mention spike | 0 |  | 0 | 0 |  | Nasdaq |  |  |
| SPCE | 2026-11-07 02:18 | mention spike | 0 |  | 0 | 0 |  | NYSE |  |  |
| RKLB | 2026-11-07 03:40 | mention spike | 6 | 20.57 | 5 | 0 | wallstreetbets 6 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xpo1gj/comment/19sbesn3tya3n/) |
| OKLO | 2026-11-05 13:17 | mention spike | 3 | 8.57 | 3 | 0 | wallstreetbets 3 | NYSE |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xpo1gj/comment/19sbqffg8jpnm/) |
| WDC | 2026-11-06 16:54 | mention spike | 5 | 4.86 | 4 | 0 | wallstreetbets 5 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xqddim/) |
| VIVK | 2026-11-06 18:22 | mention spike | 0 |  | 0 | 0 |  | Nasdaq |  |  |

Full history: `episodes.csv` (one row per first flag, with the numbers known at that moment).
