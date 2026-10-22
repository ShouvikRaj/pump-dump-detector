# Stage 4 labels

Updated 2026-10-22T23:28:36Z. Every candidate and control gets the same rule, `label-v1`, written down before any outcome was looked at (docs/stage4.md in the code branch). Sessions count from the flag; returns are against the price at the flag. All rows: `labels/labels.csv`.

- **pump**: up 50% or more within 5 sessions, then down 40% or more from that peak within the next 10
- **real news**: earnings, a completed acquisition, a change of control, bankruptcy or a material agreement that isn't a share sale, filed with the SEC (8-K) between 72 hours before the flag and session 5; it beats pump
- **not pump**: neither, once the windows have closed (10 sessions; 15 after a 50% rise)
- **crash** (a separate label, for the avoid signal): a close 40% or more below the flag price within 10 sessions

| Archetype | Role | Pump | Real news | Not pump | Crash | Pending | Unknown |
|---|---|---|---|---|---|---|---|
| low float runner | candidate | 0 | 1 | 3 | 3 of 5 (60%) | 6 | 0 |
| low float runner | control | 0 | 1 | 7 | 1 of 8 (12%) | 20 | 0 |
| otc penny | candidate | 0 | 0 | 0 | - | 1 | 0 |
| otc penny | control | 0 | 0 | 0 | - | 2 | 0 |
| other | candidate | 1 | 29 | 72 | 5 of 72 (7%) | 88 | 0 |
| other | control | 0 | 26 | 132 | 1 of 138 (1%) | 213 | 0 |

Crash counts the snapshots whose crash label has settled.
75 of the labeled candidates were flagged in Stage 1's warm-up week (`warmup = 1`), when part of the chatter baseline was backfilled.

## Labeled so far

| Flagged (UTC) | Ticker | Role | Archetype | Label | Crash | Peak, 5 sessions | Drop from peak | Lowest close, 10 sessions | News filings |
|---|---|---|---|---|---|---|---|---|---|
| 2026-10-22 22:06 | LMT | candidate | other | real news |  |  |  |  | 8-K 2026-10-22T10:26 2.02,9.01 (news) |
| 2026-10-22 19:30 | TMO | control | other | real news |  |  |  |  | 8-K 2026-10-21T14:03 2.02,9.01 (news) |
| 2026-10-22 17:45 | XXII | candidate | other | real news |  |  |  |  | 8-K 2026-10-22T14:35 2.02,8.01,9.01 (news) |
| 2026-10-22 15:59 | PM | control | other | real news |  |  |  |  | 8-K 2026-10-21T15:04 2.02,9.01 (news) |
| 2026-10-22 15:59 | ELV | control | other | real news |  |  |  |  | 8-K 2026-10-21T14:01 2.02,9.01 (news) |
| 2026-10-22 14:55 | NSC | control | other | real news |  |  |  |  | 8-K 2026-10-22T12:20 2.02,7.01,9.01 (news) |
| 2026-10-22 14:12 | HTZ | candidate | other | real news |  |  |  |  | 8-K 2026-10-20T15:05 1.01,7.01,9.01 (news) |
| 2026-10-22 07:27 | TSLA | candidate | other | real news |  |  |  |  | 8-K 2026-10-22T00:41 2.02,9.01 (news) |
| 2026-10-21 19:47 | CCI | control | other | real news |  |  |  |  | 8-K 2026-10-21T20:17 2.02,7.01,9.01 (news) |
| 2026-10-21 19:47 | BX | control | other | real news |  |  |  |  | 8-K 2026-10-22T10:55 2.02,9.01 (news) |
| 2026-10-21 18:15 | IBM | candidate | other | real news |  |  |  |  | 8-K 2026-10-21T20:19 2.02,9.01 (news) |
| 2026-10-21 18:15 | UNP | control | other | real news |  |  |  |  | 8-K 2026-10-22T11:46 2.02,9.01 (news) |
| 2026-10-21 11:34 | META | candidate | other | real news |  |  |  |  | 8-K 2026-10-21T20:03 1.01,2.02,8.01,9.01 (news) |
| 2026-10-21 11:34 | MCO | control | other | real news |  |  |  |  | 8-K 2026-10-21T10:57 2.02,7.01,9.01 (news) |
| 2026-10-20 21:06 | SMCI | candidate | other | real news |  |  |  |  | 8-K 2026-10-20T20:44 2.02,9.01 (news) |
| 2026-10-20 16:42 | LRCX | candidate | other | real news |  |  |  |  | 8-K 2026-10-21T20:13 2.02,9.01 (news) |
| 2026-10-20 13:24 | HTZ | candidate | other | real news |  |  |  |  | 8-K 2026-10-20T11:05 1.01,7.01,9.01 (news) |
| 2026-10-20 13:24 | MYGN | control | other | real news |  |  |  |  | 8-K 2026-10-20T12:36 1.01,7.01,9.01 (news) |
| 2026-10-20 10:18 | SPCX | candidate | other | real news |  |  |  |  | 8-K 2026-10-20T20:00 2.02,9.01 (news) |
| 2026-10-19 22:36 | CB | control | other | real news |  |  |  |  | 8-K 2026-10-20T21:24 2.02,9.01 (news) |
| 2026-10-19 19:31 | NFLX | candidate | other | real news |  |  |  |  | 8-K 2026-10-20T20:01 2.02,9.01 (news) |
| 2026-10-19 18:51 | KEY | control | other | real news |  |  |  |  | 8-K 2026-10-20T10:30 2.02,9.01 (news) |
| 2026-10-19 16:13 | MCO | control | other | real news |  |  |  |  | 8-K 2026-10-21T10:57 2.02,7.01,9.01 (news) |
| 2026-10-19 06:00 | NSC | control | other | real news |  |  |  |  | 8-K 2026-10-22T12:20 2.02,7.01,9.01 (news) |
| 2026-10-17 17:37 | NFLX | candidate | other | real news |  |  |  |  | 8-K 2026-10-20T20:01 2.02,9.01 (news) |
| 2026-10-17 04:49 | DOW | control | other | real news |  |  |  |  | 8-K 2026-10-22T10:57 2.02,9.01 (news) |
| 2026-10-16 21:20 | XLAB | candidate | other | real news |  |  |  |  | 8-K 2026-10-15T04:17 1.01,9.01 (news) |
| 2026-10-16 19:34 | SOXS | candidate | other | not pump |  | +13% |  |  |  |
| 2026-10-16 19:34 | FDBC | control | other | real news |  | +9% |  |  | 8-K 2026-10-21T18:40 2.02,9.01 (news) |
| 2026-10-16 19:07 | VOO | candidate | other | not pump |  | +2% |  |  |  |
| 2026-10-16 19:07 | OPEX | candidate | other | not pump |  | +29% |  |  |  |
| 2026-10-16 19:07 | FLEX | control | other | real news |  | +7% |  |  | 8-K 2026-10-14T16:13 1.01,2.01,2.03,8.01,9.01 (news) |
| 2026-10-16 18:54 | TQQQ | candidate | other | not pump |  | +8% |  |  |  |
| 2026-10-16 18:27 | QQQ | candidate | other | not pump |  | +2% |  |  |  |
| 2026-10-16 18:27 | TRV | control | other | real news |  | +5% |  |  | 8-K 2026-10-16T10:58 2.02,9.01 (news) |
| 2026-10-16 13:35 | IBKR | candidate | other | real news |  | +3% |  |  | 8-K 2026-10-16T00:01 2.02,9.01 (news) |
| 2026-10-16 07:11 | TSLA | candidate | other | real news |  | +7% |  |  | 8-K 2026-10-21T20:41 2.02,9.01 (news) |
| 2026-10-15 23:28 | BETR | candidate | other | real news |  | +61% |  |  | 8-K 2026-10-15T00:20 2.02,9.01 (news) |
| 2026-10-15 15:04 | SOXS | candidate | other | not pump |  | +11% |  |  |  |
| 2026-10-14 19:11 | LQDA | candidate | other | real news |  | +14% |  |  | 8-K 2026-10-14T01:49 1.01,1.02,7.01,8.01,9.01 (news) |
| 2026-10-14 18:31 | TLT | candidate | other | not pump |  | +2% |  |  |  |
| 2026-10-14 17:34 | VOO | candidate | other | not pump |  | +1% |  |  |  |
| 2026-10-14 13:12 | TCRT | candidate | low float runner | real news | yes | +14% |  |  | 8-K 2026-10-13T17:28 1.01,2.01,3.02,5.02,5.03,7.01,9.01 (news) |
| 2026-10-14 11:39 | CLF | candidate | other | real news |  | +13% |  |  | 8-K 2026-10-19T10:52 2.02,9.01 (news) |
| 2026-10-14 00:41 | RSP | candidate | other | not pump |  | +1% |  |  |  |
| 2026-10-13 22:51 | SOXL | candidate | other | not pump |  | -7% |  |  |  |
| 2026-10-13 20:37 | BAC | candidate | other | real news |  | -1% |  |  | 8-K 2026-10-14T10:44 2.02,7.01,9.01 (news) |
| 2026-10-13 20:37 | CMC | control | other | real news |  | +7% |  |  | 8-K 2026-10-13T13:00 8.01,9.01; 8-K 2026-10-15T12:01 2.02,7.01,9.01 (news) |
| 2026-10-13 18:51 | MLCI | control | low float runner | real news |  | +8% |  |  | 8-K 2026-10-15T21:21 1.01,1.02,9.01 (news) |
| 2026-10-13 13:59 | TRV | control | other | real news |  | +5% |  |  | 8-K 2026-10-16T10:58 2.02,9.01 (news) |

222 older rows are in `labels/labels.csv`.
