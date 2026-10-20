# Stage 4 labels

Updated 2026-10-20T01:52:43Z. Every candidate and control gets the same rule, `label-v1`, written down before any outcome was looked at (docs/stage4.md in the code branch). Sessions count from the flag; returns are against the price at the flag. All rows: `labels/labels.csv`.

- **pump**: up 50% or more within 5 sessions, then down 40% or more from that peak within the next 10
- **real news**: earnings, a completed acquisition, a change of control, bankruptcy or a material agreement that isn't a share sale, filed with the SEC (8-K) between 72 hours before the flag and session 5; it beats pump
- **not pump**: neither, once the windows have closed (10 sessions; 15 after a 50% rise)
- **crash** (a separate label, for the avoid signal): a close 40% or more below the flag price within 10 sessions

| Archetype | Role | Pump | Real news | Not pump | Crash | Pending | Unknown |
|---|---|---|---|---|---|---|---|
| low float runner | candidate | 0 | 1 | 1 | 2 of 4 (50%) | 6 | 0 |
| low float runner | control | 0 | 1 | 4 | 1 of 5 (20%) | 20 | 0 |
| other | candidate | 0 | 16 | 32 | 2 of 34 (6%) | 97 | 0 |
| other | control | 0 | 11 | 66 | 1 of 67 (1%) | 204 | 0 |

Crash counts the snapshots whose crash label has settled.
42 of the labeled candidates were flagged in Stage 1's warm-up week (`warmup = 1`), when part of the chatter baseline was backfilled.

## Labeled so far

| Flagged (UTC) | Ticker | Role | Archetype | Label | Crash | Peak, 5 sessions | Drop from peak | Lowest close, 10 sessions | News filings |
|---|---|---|---|---|---|---|---|---|---|
| 2026-10-16 21:20 | XLAB | candidate | other | real news |  |  |  |  | 8-K 2026-10-15T04:17 1.01,9.01 (news) |
| 2026-10-16 19:07 | FLEX | control | other | real news |  |  |  |  | 8-K 2026-10-14T16:13 1.01,2.01,2.03,8.01,9.01 (news) |
| 2026-10-16 18:27 | TRV | control | other | real news |  |  |  |  | 8-K 2026-10-16T10:58 2.02,9.01 (news) |
| 2026-10-16 13:35 | IBKR | candidate | other | real news |  |  |  |  | 8-K 2026-10-16T00:01 2.02,9.01 (news) |
| 2026-10-15 23:28 | BETR | candidate | other | real news |  |  |  |  | 8-K 2026-10-15T00:20 2.02,9.01 (news) |
| 2026-10-14 19:11 | LQDA | candidate | other | real news |  |  |  |  | 8-K 2026-10-14T01:49 1.01,1.02,7.01,8.01,9.01 (news) |
| 2026-10-14 13:12 | TCRT | candidate | low float runner | real news | yes |  |  |  | 8-K 2026-10-13T17:28 1.01,2.01,3.02,5.02,5.03,7.01,9.01 (news) |
| 2026-10-14 11:39 | CLF | candidate | other | real news |  |  |  |  | 8-K 2026-10-19T10:52 2.02,9.01 (news) |
| 2026-10-13 20:37 | BAC | candidate | other | real news |  |  |  |  | 8-K 2026-10-14T10:44 2.02,7.01,9.01 (news) |
| 2026-10-13 20:37 | CMC | control | other | real news |  |  |  |  | 8-K 2026-10-13T13:00 8.01,9.01; 8-K 2026-10-15T12:01 2.02,7.01,9.01 (news) |
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
| 2026-10-08 17:52 | GS | control | other | real news |  | +6% |  |  | 8-K 2026-10-13T11:32 2.02,7.01,9.01 (news) |
| 2026-10-08 04:07 | EOG | control | other | real news |  | +7% |  |  | 8-K 2026-10-08T20:17 2.02 (news) |
| 2026-10-07 20:37 | LEVI | candidate | other | real news |  | +3% |  |  | 8-K 2026-10-07T20:12 2.02,9.01 (news) |
| 2026-10-07 12:34 | SOXL | candidate | other | not pump |  | +4% |  |  |  |
| 2026-10-07 12:08 | SOXS | candidate | other | not pump |  | +31% |  |  |  |
| 2026-10-07 12:08 | NSLRL | control | other | real news |  | +0% |  |  | 8-K 2026-10-06T00:05 2.02,8.01,9.01 (news) |
| 2026-10-06 19:34 | AVGO | candidate | other | not pump | no | +1% |  | -13% |  |
| 2026-10-06 19:34 | SLAB | control | other | not pump | no | +0% |  | -1% |  |
| 2026-10-06 19:34 | HUBB | control | other | not pump | no | +1% |  | -5% |  |
| 2026-10-06 18:54 | SKHY | candidate | other | not pump | no | +4% |  | -26% |  |
| 2026-10-06 18:54 | WDFC | control | other | not pump | no | +1% |  | -2% |  |
| 2026-10-06 18:54 | OPY | control | other | not pump | no | +2% |  | -19% |  |
| 2026-10-06 18:28 | INTC | candidate | other | not pump | no | +3% |  | -22% |  |
| 2026-10-06 18:28 | HLI | control | other | not pump | no | +2% |  | -3% | 8-K 2026-10-06T01:08 5.02 |
| 2026-10-06 18:28 | BANF | control | other | not pump | no | +2% |  | -1% |  |
| 2026-10-06 18:14 | OKLO | candidate | other | not pump | no | +1% |  | -30% |  |
| 2026-10-06 18:14 | INGM | control | other | not pump | no | +1% |  | -5% |  |
| 2026-10-06 18:14 | BRX | control | other | not pump | no | +1% |  | -1% |  |
| 2026-10-06 18:01 | PENG | candidate | other | real news | no | +40% |  | -1% | 8-K 2026-10-06T20:27 2.02,9.01 (news); 8-K 2026-10-06T20:34 2.02,5.02,7.01,9.01 (news) |
| 2026-10-06 18:01 | YETI | control | other | not pump | no | +1% |  | -3% |  |
| 2026-10-06 18:01 | CXT | control | other | not pump | no | +4% |  | -3% | 8-K 2026-10-07T11:31 5.02,9.01 |
| 2026-10-06 17:21 | TEAD | control | other | not pump | no | +5% |  | -30% | 8-K 2026-10-06T01:28 1.01,2.03,9.01 |
| 2026-10-06 17:21 | GCL | control | other | not pump | no | +23% |  | +1% |  |
| 2026-10-06 17:08 | SPY | candidate | other | not pump | no | +0% |  | -2% |  |
| 2026-10-06 17:08 | UI | control | other | not pump | no | +7% |  | -5% |  |
| 2026-10-06 17:08 | DE | control | other | not pump | no | +2% |  | -9% |  |
| 2026-10-06 16:43 | INFQ | candidate | other | not pump | no | +4% |  | -33% |  |

82 older rows are in `labels/labels.csv`.
