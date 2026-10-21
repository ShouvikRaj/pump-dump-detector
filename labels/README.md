# Stage 4 labels

Updated 2026-10-21T23:24:29Z. Every candidate and control gets the same rule, `label-v1`, written down before any outcome was looked at (docs/stage4.md in the code branch). Sessions count from the flag; returns are against the price at the flag. All rows: `labels/labels.csv`.

- **pump**: up 50% or more within 5 sessions, then down 40% or more from that peak within the next 10
- **real news**: earnings, a completed acquisition, a change of control, bankruptcy or a material agreement that isn't a share sale, filed with the SEC (8-K) between 72 hours before the flag and session 5; it beats pump
- **not pump**: neither, once the windows have closed (10 sessions; 15 after a 50% rise)
- **crash** (a separate label, for the avoid signal): a close 40% or more below the flag price within 10 sessions

| Archetype | Role | Pump | Real news | Not pump | Crash | Pending | Unknown |
|---|---|---|---|---|---|---|---|
| low float runner | candidate | 0 | 1 | 3 | 3 of 5 (60%) | 5 | 0 |
| low float runner | control | 0 | 1 | 7 | 1 of 8 (12%) | 18 | 0 |
| other | candidate | 1 | 21 | 58 | 3 of 59 (5%) | 80 | 0 |
| other | control | 0 | 17 | 109 | 1 of 113 (1%) | 185 | 0 |

Crash counts the snapshots whose crash label has settled.
66 of the labeled candidates were flagged in Stage 1's warm-up week (`warmup = 1`), when part of the chatter baseline was backfilled.

## Labeled so far

| Flagged (UTC) | Ticker | Role | Archetype | Label | Crash | Peak, 5 sessions | Drop from peak | Lowest close, 10 sessions | News filings |
|---|---|---|---|---|---|---|---|---|---|
| 2026-10-21 11:34 | MCO | control | other | real news |  |  |  |  | 8-K 2026-10-21T10:57 2.02,7.01,9.01 (news) |
| 2026-10-20 21:06 | SMCI | candidate | other | real news |  |  |  |  | 8-K 2026-10-20T20:44 2.02,9.01 (news) |
| 2026-10-20 13:24 | HTZ | candidate | other | real news |  |  |  |  | 8-K 2026-10-20T11:05 1.01,7.01,9.01 (news) |
| 2026-10-20 13:24 | MYGN | control | other | real news |  |  |  |  | 8-K 2026-10-20T12:36 1.01,7.01,9.01 (news) |
| 2026-10-20 10:18 | SPCX | candidate | other | real news |  |  |  |  | 8-K 2026-10-20T20:00 2.02,9.01 (news) |
| 2026-10-19 22:36 | CB | control | other | real news |  |  |  |  | 8-K 2026-10-20T21:24 2.02,9.01 (news) |
| 2026-10-19 19:31 | NFLX | candidate | other | real news |  |  |  |  | 8-K 2026-10-20T20:01 2.02,9.01 (news) |
| 2026-10-19 18:51 | KEY | control | other | real news |  |  |  |  | 8-K 2026-10-20T10:30 2.02,9.01 (news) |
| 2026-10-19 16:13 | MCO | control | other | real news |  |  |  |  | 8-K 2026-10-21T10:57 2.02,7.01,9.01 (news) |
| 2026-10-17 17:37 | NFLX | candidate | other | real news |  |  |  |  | 8-K 2026-10-20T20:01 2.02,9.01 (news) |
| 2026-10-16 21:20 | XLAB | candidate | other | real news |  |  |  |  | 8-K 2026-10-15T04:17 1.01,9.01 (news) |
| 2026-10-16 19:34 | FDBC | control | other | real news |  |  |  |  | 8-K 2026-10-21T18:40 2.02,9.01 (news) |
| 2026-10-16 19:07 | FLEX | control | other | real news |  |  |  |  | 8-K 2026-10-14T16:13 1.01,2.01,2.03,8.01,9.01 (news) |
| 2026-10-16 18:27 | TRV | control | other | real news |  |  |  |  | 8-K 2026-10-16T10:58 2.02,9.01 (news) |
| 2026-10-16 13:35 | IBKR | candidate | other | real news |  |  |  |  | 8-K 2026-10-16T00:01 2.02,9.01 (news) |
| 2026-10-15 23:28 | BETR | candidate | other | real news |  |  |  |  | 8-K 2026-10-15T00:20 2.02,9.01 (news) |
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
| 2026-10-13 10:39 | JPM | candidate | other | real news |  | +6% |  |  | 8-K 2026-10-13T10:30 2.02,9.01 (news); 8-K 2026-10-13T13:38 7.01,9.01 |
| 2026-10-13 10:39 | HIFS | control | other | not pump |  | +2% |  |  |  |
| 2026-10-13 03:58 | FAST | control | other | real news |  | +3% |  |  | 8-K 2026-10-14T11:56 2.02,9.01 (news) |
| 2026-10-12 20:58 | BMBL | candidate | other | real news |  | +57% |  |  | 8-K 2026-10-13T12:56 1.01,7.01,9.01 (news) |
| 2026-10-12 20:32 | UNH | candidate | other | real news |  | +9% |  |  | 8-K 2026-10-13T10:14 2.02,9.01 (news) |
| 2026-10-12 14:20 | SOXX | candidate | other | not pump |  | +1% |  |  |  |
| 2026-10-09 13:59 | UNH | candidate | other | real news |  | +9% |  |  | 8-K 2026-10-13T10:14 2.02,9.01 (news) |
| 2026-10-09 12:52 | DAL | candidate | other | real news |  | +3% |  |  | 8-K 2026-10-09T10:30 2.02,9.01 (news) |
| 2026-10-09 12:52 | FAST | control | other | real news |  | +4% |  |  | 8-K 2026-10-14T11:56 2.02,9.01 (news) |
| 2026-10-09 01:49 | GBDC | control | other | real news |  | +2% |  |  | 8-K 2026-10-07T00:17 2.02,9.01 (news) |
| 2026-10-09 00:30 | SOXL | candidate | other | not pump |  | +4% |  |  |  |
| 2026-10-08 19:38 | CMG | candidate | other | not pump | no | +1% |  | -15% |  |
| 2026-10-08 19:38 | TRP | control | other | not pump | no | +4% |  | -1% | 8-K/6-K 2026-10-06T02:03 no items; 6-K 2026-10-13T21:25 no items |
| 2026-10-08 19:38 | IOT | control | other | not pump | no | +5% |  | -4% |  |
| 2026-10-08 18:59 | SBUX | candidate | other | not pump | no | +3% |  | -0% |  |
| 2026-10-08 18:59 | NEE | control | other | not pump | no | +3% |  | +0% | 8-K 2026-10-07T00:15 8.01,9.01 |
| 2026-10-08 18:59 | AEP | control | other | not pump | no | +3% |  | -0% |  |
| 2026-10-08 18:20 | USO | candidate | other | not pump | no | +4% |  | -1% |  |
| 2026-10-08 18:20 | LOPE | control | other | not pump | no | +2% |  | -0% |  |
| 2026-10-08 18:20 | ITRI | control | other | not pump | no | +3% |  | -3% |  |
| 2026-10-08 18:05 | NBIS | candidate | other | not pump | no | +6% |  | -25% |  |
| 2026-10-08 18:05 | CNI | control | other | not pump | no | +3% |  | -0% |  |

168 older rows are in `labels/labels.csv`.
