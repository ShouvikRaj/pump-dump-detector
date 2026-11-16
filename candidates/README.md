# Stage 1 candidates

Updated 2026-11-16T19:29:09Z by run `43938626771`. A candidate is a ticker whose Reddit mentions (or hype-language
posts) in the last 24 hours jumped above its prior 7-day mean + 2 sd, with at least
10 mentions from 5 different authors. It stays listed until it goes
24 hours without a new flag. These are statistical flags, not accusations or advice.

| Ticker | Flagged since (UTC) | Why | Mentions 24h | Baseline/day | Authors | Hype posts | Subreddits | Exchange | StockTwits | Example |
|---|---|---|---|---|---|---|---|---|---|---|
| ANT | 2026-11-16 16:34 | mention spike | 177 | 68.14 | 117 | 1 | wallstreetbets 174, smallstreetbets 2, pennystocks 1 | ? |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xxfkdl/) |
| HOOD | 2026-11-16 15:08 | mention spike | 15 | 3.86 | 15 | 0 | wallstreetbets 15 | Nasdaq | #6 | [link](https://www.reddit.com/r/wallstreetbets/comments/1xxmkhj/comment/19sqipn3ca7y9/) |
| IREN | 2026-11-16 18:57 | mention spike | 30 | 11.57 | 25 | 0 | wallstreetbets 30 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xxnvng/) |
| MSTR | 2026-11-13 06:20 | mention spike | 26 | 11.71 | 18 | 0 | wallstreetbets 26 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xxmkhj/comment/19sqg4mwkp96q/) |
| WMT | 2026-11-16 07:17 | mention spike | 20 | 3.86 | 15 | 0 | wallstreetbets 20 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xxmkhj/comment/19sqeb7vi03b4/) |
| ASML | 2026-11-15 23:05 | mention spike | 2 | 8.14 | 2 | 0 | wallstreetbets 2 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xxmkhj/comment/19sqglnoa8jid/) |
| DXYZ | 2026-11-14 23:53 | mention spike | 20 | 6.0 | 14 | 0 | wallstreetbets 20 | NYSE |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xxmkhj/comment/19sqj0y8jh6ma/) |
| COIN | 2026-11-15 21:05 | mention spike | 8 | 2.0 | 7 | 0 | wallstreetbets 8 | Nasdaq |  | [link](https://www.reddit.com/r/wallstreetbets/comments/1xxmkhj/comment/19sqd28qleuh0/) |

Full history: `episodes.csv` (one row per first flag, with the numbers known at that moment).
