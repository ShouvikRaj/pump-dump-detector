# Stage 4 labels

Updated 2026-10-28T02:21:25Z. Every candidate and control gets the same rule, `label-v1`, written down before any outcome was looked at (docs/stage4.md in the code branch). Sessions count from the flag; returns are against the price at the flag. All rows: `labels/labels.csv`.

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
| other | candidate | 2 | 37 | 110 | 7 of 117 (6%) | 84 | 0 |
| other | control | 0 | 41 | 217 | 1 of 226 (0%) | 199 | 0 |
| unknown | candidate | 0 | 0 | 0 | - | 0 | 1 |

Crash counts the snapshots whose crash label has settled.
87 of the labeled candidates were flagged in Stage 1's warm-up week (`warmup = 1`), when part of the chatter baseline was backfilled.

## Labeled so far

| Flagged (UTC) | Ticker | Role | Archetype | Label | Crash | Peak, 5 sessions | Drop from peak | Lowest close, 10 sessions | News filings |
|---|---|---|---|---|---|---|---|---|---|
| 2026-10-28 00:47 | ITW | control | other | real news |  |  |  |  | 8-K 2026-10-27T13:20 2.02,9.01 (news) |
| 2026-10-27 20:57 | BBAI | candidate | other | real news |  |  |  |  | 8-K 2026-10-27T20:10 2.02 (news) |
| 2026-10-27 00:43 | SOFI | candidate | other | real news |  |  |  |  | 8-K 2026-10-27T11:02 2.02,9.01 (news) |
| 2026-10-27 00:43 | AMKR | candidate | other | real news |  |  |  |  | 8-K 2026-10-26T20:07 2.02,9.01 (news) |
| 2026-10-26 19:24 | CLS | candidate | other | real news |  |  |  |  | 8-K 2026-10-26T20:23 2.02,9.01 (news); 8-K 2026-10-27T11:17 7.01,9.01 |
| 2026-10-26 13:24 | ANT | candidate | unknown | unknown (no price at the flag) |  |  |  |  |  |
| 2026-10-23 20:37 | WELL | control | other | real news |  |  |  |  | 8-K 2026-10-26T20:33 2.02,7.01,9.01 (news) |
| 2026-10-23 20:37 | DOV | control | other | real news |  |  |  |  | 8-K 2026-10-22T15:01 2.02,7.01,9.01 (news) |
| 2026-10-23 20:37 | DHR | control | other | real news |  |  |  |  | 8-K 2026-10-21T01:43 2.02,9.01 (news) |
| 2026-10-23 16:35 | BFC | control | other | real news |  |  |  |  | 8-K 2026-10-21T00:01 2.02,9.01 (news) |
| 2026-10-23 15:42 | BE | candidate | other | real news |  |  |  |  | 8-K 2026-10-23T00:09 2.02,7.01,9.01 (news) |
| 2026-10-23 15:42 | COR | control | other | real news |  |  |  |  | 8-K 2026-10-21T15:48 2.02,7.01,9.01 (news) |
| 2026-10-23 03:07 | RS | control | other | real news |  |  |  |  | 8-K 2026-10-22T00:20 2.02,9.01 (news) |
| 2026-10-23 02:14 | LNN | control | other | real news |  |  |  |  | 8-K 2026-10-22T10:45 2.02,5.02,9.01 (news) |
| 2026-10-22 22:49 | SSB | control | other | real news |  |  |  |  | 8-K 2026-10-22T00:07 2.02,7.01,8.01,9.01 (news) |
| 2026-10-22 22:06 | LMT | candidate | other | real news |  |  |  |  | 8-K 2026-10-22T10:26 2.02,9.01 (news) |
| 2026-10-22 22:06 | HLT | control | other | real news |  |  |  |  | 8-K 2026-10-20T15:31 3.01,7.01,9.01; 8-K 2026-10-27T10:01 2.02,9.01 (news) |
| 2026-10-22 19:45 | IQV | control | other | real news |  |  |  |  | 8-K 2026-10-27T11:08 2.02,9.01 (news) |
| 2026-10-22 19:30 | TMO | control | other | real news |  |  |  |  | 8-K 2026-10-21T14:03 2.02,9.01 (news) |
| 2026-10-22 17:45 | XXII | candidate | other | real news | yes |  |  |  | 8-K 2026-10-22T14:35 2.02,8.01,9.01 (news); 8-K 2026-10-23T21:23 8.01,9.01 |
| 2026-10-22 16:39 | FPS | candidate | other | real news |  |  |  |  | 8-K 2026-10-22T11:00 5.02,7.01,9.01; 8-K/A 2026-10-22T19:11 5.02; 8-K 2026-10-22T20:17 2.02,9.01 (news) |
| 2026-10-22 15:59 | PM | control | other | real news |  |  |  |  | 8-K 2026-10-21T15:04 2.02,9.01 (news) |
| 2026-10-22 15:59 | ELV | control | other | real news |  |  |  |  | 8-K 2026-10-21T14:01 2.02,9.01 (news) |
| 2026-10-22 14:55 | WDC | candidate | other | real news |  |  |  |  | 8-K 2026-10-22T20:04 2.02,9.01 (news) |
| 2026-10-22 14:55 | NSC | control | other | real news |  |  |  |  | 8-K 2026-10-22T12:20 2.02,7.01,9.01 (news) |
| 2026-10-22 14:12 | HTZ | candidate | other | real news |  |  |  |  | 8-K 2026-10-20T15:05 1.01,7.01,9.01 (news) |
| 2026-10-22 07:27 | TSLA | candidate | other | real news |  |  |  |  | 8-K 2026-10-22T00:41 2.02,9.01 (news) |
| 2026-10-22 07:27 | KNSL | control | other | real news |  |  |  |  | 8-K 2026-10-22T20:11 2.02,9.01 (news); 8-K 2026-10-22T20:13 5.02,8.01,9.01 |
| 2026-10-21 19:47 | CCI | control | other | real news |  | +16% |  |  | 8-K 2026-10-21T20:17 2.02,7.01,9.01 (news) |
| 2026-10-21 19:47 | BX | control | other | real news |  | +10% |  |  | 8-K 2026-10-22T10:55 2.02,9.01 (news); 8-K 2026-10-27T13:01 8.01,9.01 |
| 2026-10-21 18:15 | IBM | candidate | other | real news |  | +4% |  |  | 8-K 2026-10-21T20:19 2.02,9.01 (news) |
| 2026-10-21 18:15 | UNP | control | other | real news |  | +4% |  |  | 8-K 2026-10-22T11:46 2.02,9.01 (news) |
| 2026-10-21 18:15 | BA | control | other | real news |  | +0% |  |  | 8-K 2026-10-27T11:30 2.02,9.01 (news) |
| 2026-10-21 11:34 | META | candidate | other | real news |  | +3% |  |  | 8-K 2026-10-21T20:03 1.01,2.02,8.01,9.01 (news) |
| 2026-10-21 11:34 | MCO | control | other | real news |  | +7% |  |  | 8-K 2026-10-21T10:57 2.02,7.01,9.01 (news) |
| 2026-10-20 23:18 | HLT | control | other | real news |  | +1% |  |  | 8-K 2026-10-20T11:31 3.01,7.01,9.01; 8-K 2026-10-27T10:01 2.02,9.01 (news) |
| 2026-10-20 23:18 | AMT | control | other | real news |  | +10% |  |  | 8-K 2026-10-27T11:03 2.02,9.01 (news) |
| 2026-10-20 21:06 | SMCI | candidate | other | real news |  | +2% |  |  | 8-K 2026-10-20T20:44 2.02,9.01 (news) |
| 2026-10-20 16:42 | LRCX | candidate | other | real news |  | +2% |  |  | 8-K 2026-10-21T20:13 2.02,9.01 (news) |
| 2026-10-20 16:03 | IWM | candidate | other | not pump |  | +1% |  |  |  |
| 2026-10-20 13:24 | HTZ | candidate | other | real news |  | +16% |  |  | 8-K 2026-10-20T11:05 1.01,7.01,9.01 (news) |
| 2026-10-20 13:24 | MYGN | control | other | real news |  | +16% |  |  | 8-K 2026-10-20T12:36 1.01,7.01,9.01 (news) |
| 2026-10-20 10:18 | SPCX | candidate | other | real news |  | +13% |  |  | 8-K 2026-10-20T20:00 2.02,9.01 (news); 8-K 2026-10-26T12:00 8.01 |
| 2026-10-19 22:36 | CB | control | other | real news |  | +2% |  |  | 8-K 2026-10-20T21:24 2.02,9.01 (news) |
| 2026-10-19 19:31 | NFLX | candidate | other | real news |  | +1% |  |  | 8-K 2026-10-20T20:01 2.02,9.01 (news) |
| 2026-10-19 18:51 | KEY | control | other | real news |  | +7% |  |  | 8-K 2026-10-20T10:30 2.02,9.01 (news) |
| 2026-10-19 16:13 | TQQQ | candidate | other | not pump |  | +2% |  |  |  |
| 2026-10-19 16:13 | MCO | control | other | real news |  | +3% |  |  | 8-K 2026-10-21T10:57 2.02,7.01,9.01 (news) |
| 2026-10-19 06:00 | WDC | candidate | other | real news |  | +17% |  |  | 8-K 2026-10-22T20:04 2.02,9.01 (news) |
| 2026-10-19 06:00 | NSC | control | other | real news |  | +3% |  |  | 8-K 2026-10-22T12:20 2.02,7.01,9.01 (news) |

378 older rows are in `labels/labels.csv`.
