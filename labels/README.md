# Stage 4 labels

Updated 2026-10-29T02:28:50Z. Every candidate and control gets the same rule, `label-v1`, written down before any outcome was looked at (docs/stage4.md in the code branch). Sessions count from the flag; returns are against the price at the flag. All rows: `labels/labels.csv`.

- **pump**: up 50% or more within 5 sessions, then down 40% or more from that peak within the next 10
- **real news**: earnings, a completed acquisition, a change of control, bankruptcy or a material agreement that isn't a share sale, filed with the SEC (8-K) between 72 hours before the flag and session 5; it beats pump
- **not pump**: neither, once the windows have closed (10 sessions; 15 after a 50% rise)
- **crash** (a separate label, for the avoid signal): a close 40% or more below the flag price within 10 sessions

| Archetype | Role | Pump | Real news | Not pump | Crash | Pending | Unknown |
|---|---|---|---|---|---|---|---|
| low float runner | candidate | 1 | 1 | 4 | 3 of 7 (43%) | 4 | 0 |
| low float runner | control | 0 | 1 | 13 | 2 of 14 (14%) | 14 | 0 |
| otc penny | candidate | 0 | 0 | 0 | - | 1 | 0 |
| otc penny | control | 0 | 0 | 0 | - | 2 | 0 |
| other | candidate | 2 | 46 | 117 | 7 of 120 (6%) | 82 | 0 |
| other | control | 0 | 51 | 223 | 1 of 232 (0%) | 211 | 0 |
| unknown | candidate | 0 | 0 | 0 | - | 0 | 1 |

Crash counts the snapshots whose crash label has settled.
87 of the labeled candidates were flagged in Stage 1's warm-up week (`warmup = 1`), when part of the chatter baseline was backfilled.

## Labeled so far

| Flagged (UTC) | Ticker | Role | Archetype | Label | Crash | Peak, 5 sessions | Drop from peak | Lowest close, 10 sessions | News filings |
|---|---|---|---|---|---|---|---|---|---|
| 2026-10-29 00:52 | FLS | control | other | real news |  |  |  |  | 8-K 2026-10-28T20:18 2.02,7.01,9.01 (news) |
| 2026-10-28 22:11 | CFFI | control | other | real news |  |  |  |  | 8-K 2026-10-26T20:24 2.02,9.01 (news) |
| 2026-10-28 21:57 | NOW | candidate | other | real news |  |  |  |  | 8-K 2026-10-28T21:10 2.02,9.01 (news) |
| 2026-10-28 21:46 | GOOGL | candidate | other | real news |  |  |  |  | 8-K 2026-10-28T20:01 2.02,9.01 (news) |
| 2026-10-28 21:20 | FTNT | candidate | other | real news |  |  |  |  | 8-K 2026-10-28T20:09 2.02,9.01 (news) |
| 2026-10-28 21:20 | NUE | control | other | real news |  |  |  |  | 8-K 2026-10-26T20:54 2.02,7.01,9.01 (news) |
| 2026-10-28 20:50 | GOOG | candidate | other | real news |  |  |  |  | 8-K 2026-10-28T20:01 2.02,9.01 (news) |
| 2026-10-28 16:10 | ENPH | candidate | other | real news |  |  |  |  | 8-K 2026-10-27T20:07 2.02,9.01 (news) |
| 2026-10-28 16:10 | PECO | control | other | real news |  |  |  |  | 8-K 2026-10-26T20:18 2.02,7.01,9.01 (news) |
| 2026-10-28 11:39 | VRT | candidate | other | real news |  |  |  |  | 8-K 2026-10-28T10:02 2.02,7.01,9.01 (news) |
| 2026-10-28 11:39 | PSA | control | other | real news |  |  |  |  | 8-K 2026-10-26T20:11 2.02,9.01 (news) |
| 2026-10-28 00:47 | ITW | control | other | real news |  |  |  |  | 8-K 2026-10-27T13:20 2.02,9.01 (news) |
| 2026-10-27 20:57 | BBAI | candidate | other | real news |  |  |  |  | 8-K 2026-10-27T20:10 2.02 (news); 8-K/A 2026-10-27T22:20 2.02,9.01 |
| 2026-10-27 19:12 | STX | candidate | other | real news |  |  |  |  | 8-K 2026-10-27T20:12 2.02,7.01,9.01 (news); 8-K 2026-10-27T22:56 5.07 |
| 2026-10-27 03:54 | HOOD | candidate | other | real news |  |  |  |  | 8-K 2026-10-27T20:06 2.02,9.01 (news); 8-K/A 2026-10-28T00:46 2.02,9.01 |
| 2026-10-27 00:43 | SOFI | candidate | other | real news |  |  |  |  | 8-K 2026-10-27T11:02 2.02,9.01 (news) |
| 2026-10-27 00:43 | AMKR | candidate | other | real news |  |  |  |  | 8-K 2026-10-26T20:07 2.02,9.01 (news) |
| 2026-10-26 19:24 | CLS | candidate | other | real news |  |  |  |  | 8-K 2026-10-26T20:23 2.02,9.01 (news); 8-K 2026-10-27T11:17 7.01,9.01 |
| 2026-10-26 19:24 | FFIV | control | other | real news |  |  |  |  | 8-K 2026-10-27T20:09 2.02,8.01,9.01 (news) |
| 2026-10-26 13:24 | ANT | candidate | unknown | unknown (no price at the flag) |  |  |  |  |  |
| 2026-10-23 20:37 | WELL | control | other | real news |  |  |  |  | 8-K 2026-10-26T20:33 2.02,7.01,9.01 (news); 8-K 2026-10-27T20:43 8.01,9.01 |
| 2026-10-23 20:37 | DOV | control | other | real news |  |  |  |  | 8-K 2026-10-22T15:01 2.02,7.01,9.01 (news) |
| 2026-10-23 20:37 | DHR | control | other | real news |  |  |  |  | 8-K 2026-10-21T01:43 2.02,9.01 (news) |
| 2026-10-23 16:35 | BFC | control | other | real news |  |  |  |  | 8-K 2026-10-21T00:01 2.02,9.01 (news) |
| 2026-10-23 15:42 | BE | candidate | other | real news |  |  |  |  | 8-K 2026-10-23T00:09 2.02,7.01,9.01 (news) |
| 2026-10-23 15:42 | COR | control | other | real news |  |  |  |  | 8-K 2026-10-21T15:48 2.02,7.01,9.01 (news) |
| 2026-10-23 06:51 | CLH | control | other | real news |  |  |  |  | 8-K 2026-10-28T12:17 2.02,7.01,9.01 (news) |
| 2026-10-23 03:07 | RS | control | other | real news |  |  |  |  | 8-K 2026-10-22T00:20 2.02,9.01 (news) |
| 2026-10-23 02:14 | LNN | control | other | real news |  |  |  |  | 8-K 2026-10-22T10:45 2.02,5.02,9.01 (news) |
| 2026-10-22 22:49 | SSB | control | other | real news |  |  |  |  | 8-K 2026-10-22T00:07 2.02,7.01,8.01,9.01 (news) |
| 2026-10-22 22:06 | LMT | candidate | other | real news |  |  |  |  | 8-K 2026-10-22T10:26 2.02,9.01 (news) |
| 2026-10-22 22:06 | HLT | control | other | real news |  |  |  |  | 8-K 2026-10-20T15:31 3.01,7.01,9.01; 8-K 2026-10-27T10:01 2.02,9.01 (news) |
| 2026-10-22 22:06 | FRAF | control | other | real news |  |  |  |  | 8-K 2026-10-27T20:05 2.02,9.01 (news) |
| 2026-10-22 21:05 | CSTM | control | other | real news |  |  |  |  | 8-K 2026-10-28T10:14 2.02,9.01 (news) |
| 2026-10-22 19:45 | QQQ | candidate | other | not pump |  | +3% |  |  |  |
| 2026-10-22 19:45 | IQV | control | other | real news |  | +3% |  |  | 8-K 2026-10-27T11:08 2.02,9.01 (news) |
| 2026-10-22 19:30 | TMO | control | other | real news |  | +5% |  |  | 8-K 2026-10-21T14:03 2.02,9.01 (news) |
| 2026-10-22 18:52 | SOXX | candidate | other | not pump |  | +10% |  |  |  |
| 2026-10-22 18:38 | RSP | candidate | other | not pump |  | +1% |  |  |  |
| 2026-10-22 17:45 | XXII | candidate | other | real news | yes | +76% |  |  | 8-K 2026-10-22T14:35 2.02,8.01,9.01 (news); 8-K 2026-10-23T21:23 8.01,9.01; 8-K 2026-10-28T10:10 1.01,9.01 |
| 2026-10-22 16:39 | FPS | candidate | other | real news |  | +19% |  |  | 8-K 2026-10-22T11:00 5.02,7.01,9.01; 8-K/A 2026-10-22T19:11 5.02; 8-K 2026-10-22T20:17 2.02,9.01 (news) |
| 2026-10-22 15:59 | SOXL | candidate | other | not pump |  | +28% |  |  |  |
| 2026-10-22 15:59 | GEV | candidate | other | real news |  | +10% |  |  | 8-K 2026-10-28T10:16 2.02,9.01 (news) |
| 2026-10-22 15:59 | PM | control | other | real news |  | +1% |  |  | 8-K 2026-10-21T15:04 2.02,9.01 (news) |
| 2026-10-22 15:59 | ELV | control | other | real news |  | +0% |  |  | 8-K 2026-10-21T14:01 2.02,9.01 (news) |
| 2026-10-22 14:55 | WDC | candidate | other | real news |  | +13% |  |  | 8-K 2026-10-22T20:04 2.02,9.01 (news) |
| 2026-10-22 14:55 | NSC | control | other | real news |  | +3% |  |  | 8-K 2026-10-22T12:20 2.02,7.01,9.01 (news) |
| 2026-10-22 14:55 | ADP | control | other | real news |  | +2% |  |  | 8-K 2026-10-28T10:55 2.02,9.01 (news) |
| 2026-10-22 14:12 | IWM | candidate | other | not pump |  | +2% |  |  |  |
| 2026-10-22 14:12 | HTZ | candidate | other | real news |  | +3% |  |  | 8-K 2026-10-20T15:05 1.01,7.01,9.01 (news) |

410 older rows are in `labels/labels.csv`.
