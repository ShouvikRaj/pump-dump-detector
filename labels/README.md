# Stage 4 labels

Updated 2026-11-21T04:00:17Z. Every candidate and control gets the same rule, `label-v1`, written down before any outcome was looked at (docs/stage4.md in the code branch). Sessions count from the flag; returns are against the price at the flag. All rows: `labels/labels.csv`.

- **pump**: up 50% or more within 5 sessions, then down 40% or more from that peak within the next 10
- **real news**: earnings, a completed acquisition, a change of control, bankruptcy or a material agreement that isn't a share sale, filed with the SEC (8-K) between 72 hours before the flag and session 5; it beats pump
- **not pump**: neither, once the windows have closed (10 sessions; 15 after a 50% rise)
- **crash** (a separate label, for the avoid signal): a close 40% or more below the flag price within 10 sessions

| Archetype | Role | Pump | Real news | Not pump | Crash | Pending | Unknown |
|---|---|---|---|---|---|---|---|
| low float runner | candidate | 1 | 4 | 10 | 7 of 13 (54%) | 1 | 0 |
| low float runner | control | 0 | 5 | 34 | 5 of 39 (13%) | 11 | 0 |
| otc penny | candidate | 0 | 0 | 1 | 0 of 1 (0%) | 0 | 0 |
| otc penny | control | 0 | 0 | 2 | 0 of 2 (0%) | 0 | 0 |
| other | candidate | 6 | 134 | 275 | 25 of 397 (6%) | 70 | 0 |
| other | control | 0 | 162 | 614 | 2 of 770 (0%) | 175 | 0 |
| unknown | candidate | 0 | 0 | 0 | - | 0 | 5 |

Crash counts the snapshots whose crash label has settled.
87 of the labeled candidates were flagged in Stage 1's warm-up week (`warmup = 1`), when part of the chatter baseline was backfilled.

## Labeled so far

| Flagged (UTC) | Ticker | Role | Archetype | Label | Crash | Peak, 5 sessions | Drop from peak | Lowest close, 10 sessions | News filings |
|---|---|---|---|---|---|---|---|---|---|
| 2026-11-21 00:55 | WWD | control | other | real news |  |  |  |  | 8-K 2026-11-18T21:00 2.02,9.01 (news) |
| 2026-11-20 03:06 | INTU | candidate | other | real news |  |  |  |  | 8-K 2026-11-19T22:26 1.01,8.01,9.01 (news) |
| 2026-11-19 00:42 | ANT | candidate | unknown | unknown (no price at the flag) |  |  |  |  |  |
| 2026-11-18 21:40 | PANW | candidate | other | real news |  |  |  |  | 8-K 2026-11-18T21:37 2.02,3.02,7.01,8.01,9.01 (news) |
| 2026-11-17 14:06 | SPAI | candidate | low float runner | real news |  |  |  |  | 8-K 2026-11-16T22:12 2.02,9.01 (news) |
| 2026-11-17 10:45 | SHAZ | candidate | other | real news |  |  |  |  | 8-K 2026-11-16T21:15 2.02,7.01,9.01 (news) |
| 2026-11-17 01:13 | VVV | control | other | real news |  |  |  |  | 8-K 2026-11-19T12:03 2.02,7.01,9.01 (news) |
| 2026-11-16 22:11 | RCAT | candidate | other | real news |  |  |  |  | 8-K 2026-11-16T21:06 2.02,9.01 (news) |
| 2026-11-16 20:09 | LXEO | candidate | other | real news |  | +32% |  |  | 8-K 2026-11-16T12:02 2.02,7.01,8.01,9.01 (news) |
| 2026-11-16 16:34 | ANT | candidate | unknown | unknown (no price at the flag) |  |  |  |  |  |
| 2026-11-16 07:17 | WMT | candidate | other | real news |  | +2% |  |  | 8-K 2026-11-16T12:58 5.02,9.01; 8-K 2026-11-19T11:58 2.02,9.01 (news) |
| 2026-11-14 02:06 | WMT | candidate | other | real news |  | +2% |  |  | 8-K 2026-11-16T12:58 5.02,9.01; 8-K 2026-11-19T11:58 2.02,9.01 (news) |
| 2026-11-14 00:36 | DHS | candidate | other | not pump |  | +0% |  |  |  |
| 2026-11-13 22:10 | ATC | candidate | other | not pump |  | -7% |  |  |  |
| 2026-11-13 19:02 | IWM | candidate | other | not pump |  | +1% |  |  |  |
| 2026-11-13 16:24 | ROLR | control | low float runner | real news |  | +8% |  |  | 8-K 2026-11-13T21:10 2.02,9.01 (news) |
| 2026-11-13 16:24 | KLXE | control | other | real news |  | +13% |  |  | 8-K 2026-11-10T21:12 2.02,7.01,9.01 (news) |
| 2026-11-13 14:07 | SMU | candidate | other | not pump | yes | -1% |  |  |  |
| 2026-11-13 13:30 | AIMD | candidate | other | real news |  | +60% |  |  | 8-K 2026-11-16T13:41 2.02,9.01 (news); 8-K 2026-11-17T13:30 1.01,7.01,9.01 (news) |
| 2026-11-13 01:09 | SLS | candidate | other | real news |  | +158% |  |  | 8-K 2026-11-12T21:07 2.02,9.01 (news); 8-K 2026-11-17T12:14 7.01,8.01,9.01 |
| 2026-11-12 21:20 | CSCO | candidate | other | real news |  | -4% |  |  | 8-K 2026-11-12T21:06 2.02,9.01 (news) |
| 2026-11-12 20:43 | TDG | control | other | real news |  | +3% |  |  | 8-K 2026-11-10T11:32 2.02,9.01 (news) |
| 2026-11-12 18:42 | AMAT | candidate | other | real news |  | +1% |  |  | 8-K 2026-11-12T21:02 2.02,9.01 (news) |
| 2026-11-12 17:34 | TRT | candidate | low float runner | real news |  | +4% |  |  | 8-K 2026-11-12T17:28 2.02,9.01 (news) |
| 2026-11-12 17:34 | PMN | control | low float runner | real news |  | +4% |  |  | 8-K 2026-11-12T13:00 7.01,9.01; 8-K 2026-11-12T21:17 2.02,9.01 (news) |
| 2026-11-12 17:34 | IMUX | control | low float runner | real news |  | +2% |  |  | 8-K 2026-11-13T13:00 2.02,9.01 (news) |
| 2026-11-12 17:04 | AIDX | control | other | real news |  | +6% |  |  | 8-K 2026-11-16T21:39 2.02,9.01 (news) |
| 2026-11-12 16:56 | CBRS | candidate | other | real news |  | +19% |  |  | 8-K 2026-11-12T21:03 2.02,9.01 (news) |
| 2026-11-12 14:43 | LUNR | candidate | other | real news |  | +5% |  |  | 8-K 2026-11-12T12:32 2.02,9.01 (news) |
| 2026-11-11 07:39 | NVDL | candidate | other | not pump | yes | +8% |  |  |  |
| 2026-11-10 21:21 | RGTI | candidate | other | real news |  | +13% |  |  | 8-K 2026-11-10T21:05 2.02,9.01 (news) |
| 2026-11-10 20:00 | CRWV | candidate | other | real news |  | +31% |  |  | 8-K 2026-11-10T21:05 2.02,9.01 (news) |
| 2026-11-10 16:24 | TTWO | candidate | other | real news |  | +8% |  |  | 8-K 2026-11-09T21:10 2.02,9.01 (news) |
| 2026-11-10 14:52 | ANT | candidate | unknown | unknown (no price at the flag) |  |  |  |  |  |
| 2026-11-09 22:33 | ASTS | candidate | other | real news |  | -1% |  |  | 8-K 2026-11-09T21:49 2.02,7.01,9.01 (news); 8-K 2026-11-10T13:00 7.01,9.01 |
| 2026-11-09 22:18 | IVF | candidate | low float runner | real news |  | +21% |  |  | 8-K 2026-11-16T15:30 2.02,9.01 (news) |
| 2026-11-09 22:18 | TDG | control | other | real news |  | +4% |  |  | 8-K 2026-11-10T11:32 2.02,9.01 (news) |
| 2026-11-09 21:25 | RKLB | candidate | other | real news |  | +24% |  |  | 8-K 2026-11-09T21:06 2.02,9.01 (news) |
| 2026-11-09 21:11 | TTD | candidate | other | real news |  | -13% |  |  | 8-K 2026-11-09T21:09 2.02,8.01,9.01 (news) |
| 2026-11-09 20:48 | ONDS | candidate | other | real news | no | +2% |  | -38% | 8-K 2026-11-12T13:24 2.02,9.01 (news) |
| 2026-11-09 20:48 | RGS | control | other | not pump | no | +1% |  | -20% | 8-K 2026-11-13T12:06 5.02 |
| 2026-11-09 20:48 | LBTYK | control | other | not pump | no | +10% |  | +1% |  |
| 2026-11-09 20:48 | CCU | control | other | not pump | no | +2% |  | -9% |  |
| 2026-11-09 20:48 | AUBN | control | other | not pump | no | +2% |  | -5% | 8-K 2026-11-10T21:33 8.01,9.01 |
| 2026-11-09 15:56 | AVGO | candidate | other | not pump | no | +16% |  | -5% |  |
| 2026-11-09 15:56 | PVLA | control | other | not pump | no | +2% |  | -19% |  |
| 2026-11-09 15:56 | AIT | control | other | not pump | no | +3% |  | -7% |  |
| 2026-11-09 15:04 | NNN | candidate | other | not pump | no | +2% |  | -3% |  |
| 2026-11-09 15:04 | GXO | control | other | not pump | no | +1% |  | -8% |  |
| 2026-11-09 15:04 | BETA | control | other | not pump | no | +5% |  | -38% |  |

1203 older rows are in `labels/labels.csv`.
