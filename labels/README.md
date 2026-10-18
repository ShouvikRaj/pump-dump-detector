# Stage 4 labels

Updated 2026-10-18T23:23:11Z. Every candidate and control gets the same rule, `label-v1`, written down before any outcome was looked at (docs/stage4.md in the code branch). Sessions count from the flag; returns are against the price at the flag. All rows: `labels/labels.csv`.

- **pump**: up 50% or more within 5 sessions, then down 40% or more from that peak within the next 10
- **real news**: earnings, a completed acquisition, a change of control, bankruptcy or a material agreement that isn't a share sale, filed with the SEC (8-K) between 72 hours before the flag and session 5; it beats pump
- **not pump**: neither, once the windows have closed (10 sessions; 15 after a 50% rise)
- **crash** (a separate label, for the avoid signal): a close 40% or more below the flag price within 10 sessions

| Archetype | Role | Pump | Real news | Not pump | Crash | Pending | Unknown |
|---|---|---|---|---|---|---|---|
| low float runner | candidate | 0 | 1 | 1 | 1 of 3 (33%) | 5 | 0 |
| low float runner | control | 0 | 1 | 4 | 0 of 4 (0%) | 18 | 0 |
| other | candidate | 0 | 15 | 14 | 2 of 10 (20%) | 109 | 0 |
| other | control | 0 | 11 | 18 | 1 of 19 (5%) | 238 | 0 |

Crash counts the snapshots whose crash label has settled.
24 of the labeled candidates were flagged in Stage 1's warm-up week (`warmup = 1`), when part of the chatter baseline was backfilled.

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
| 2026-10-13 20:37 | BAC | candidate | other | real news |  |  |  |  | 8-K 2026-10-14T10:44 2.02,7.01,9.01 (news) |
| 2026-10-13 20:37 | CMC | control | other | real news |  |  |  |  | 8-K 2026-10-13T13:00 8.01,9.01; 8-K 2026-10-15T12:01 2.02,7.01,9.01 (news) |
| 2026-10-13 18:51 | MLCI | control | low float runner | real news |  |  |  |  | 8-K 2026-10-15T21:21 1.01,1.02,9.01 (news) |
| 2026-10-13 13:59 | TRV | control | other | real news |  |  |  |  | 8-K 2026-10-16T10:58 2.02,9.01 (news) |
| 2026-10-13 10:39 | JPM | candidate | other | real news |  |  |  |  | 8-K 2026-10-13T10:30 2.02,9.01 (news); 8-K 2026-10-13T13:38 7.01,9.01 |
| 2026-10-13 03:58 | FAST | control | other | real news |  |  |  |  | 8-K 2026-10-14T11:56 2.02,9.01 (news) |
| 2026-10-12 20:58 | BMBL | candidate | other | real news |  |  |  |  | 8-K 2026-10-13T12:56 1.01,7.01,9.01 (news) |
| 2026-10-12 20:32 | UNH | candidate | other | real news |  |  |  |  | 8-K 2026-10-13T10:14 2.02,9.01 (news) |
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
| 2026-10-06 18:01 | PENG | candidate | other | real news |  | +40% |  |  | 8-K 2026-10-06T20:27 2.02,9.01 (news); 8-K 2026-10-06T20:34 2.02,5.02,7.01,9.01 (news) |
| 2026-10-06 16:15 | VOO | candidate | other | not pump |  | +0% |  |  |  |
| 2026-10-06 11:49 | QQQ | candidate | other | not pump |  | +0% |  |  |  |
| 2026-10-06 11:49 | REGN | control | other | real news |  | +5% |  |  | 8-K 2026-10-06T11:51 1.01,2.02,8.01 (news) |
| 2026-10-06 00:59 | IWM | candidate | other | not pump |  | +1% |  |  |  |
| 2026-10-05 23:41 | ALEC | candidate | other | real news |  | +14% |  |  | 8-K 2026-10-05T11:00 1.01,2.02,7.01,8.01,9.01 (news) |
| 2026-10-05 17:49 | IREN | candidate | other | not pump | no | +5% |  | -33% |  |
| 2026-10-05 17:49 | NI | control | other | not pump | no | +3% |  | -0% |  |
| 2026-10-05 17:49 | AMRZ | control | other | not pump | no | +1% |  | -3% |  |
| 2026-10-05 16:38 | DELL | candidate | other | not pump | no | +7% |  | -19% |  |
| 2026-10-05 16:38 | PWR | control | other | not pump | no | +5% |  | -8% |  |
| 2026-10-05 16:38 | ADI | control | other | not pump | no | +2% |  | -5% |  |
| 2026-10-05 16:24 | GME | candidate | other | not pump | no | +5% |  | -4% |  |
| 2026-10-05 16:24 | SOBO | control | other | not pump | no | +1% |  | -2% | 6-K 2026-10-07T21:06 no items |
| 2026-10-05 16:24 | BEN | control | other | not pump | no | +1% |  | -7% |  |
| 2026-10-05 15:33 | VEEA | candidate | low float runner | not pump | no | +40% |  | -24% | 8-K 2026-10-02T20:30 1.01,2.03,9.01; 8-K 2026-10-06T21:25 8.01 |
| 2026-10-05 15:33 | MPU | control | low float runner | not pump | no | +8% |  | -8% |  |
| 2026-10-05 15:33 | FIEE | control | low float runner | not pump | no | +2% |  | -2% | 8-K 2026-10-02T20:05 5.02 |
| 2026-10-05 15:18 | TSM | candidate | other | not pump | no | +1% |  | -15% | 6-K 2026-10-08T10:12 no items |
| 2026-10-05 15:18 | SAIA | control | other | not pump | no | +4% |  | -3% |  |
| 2026-10-05 15:18 | MYRG | control | other | not pump | no | +8% |  | -9% |  |
| 2026-10-05 14:51 | SPCX | candidate | other | not pump | no | +6% |  | -13% |  |
| 2026-10-05 14:51 | TEL | control | other | not pump | no | +2% |  | -4% | 8-K 2026-10-07T10:23 5.02 |

15 older rows are in `labels/labels.csv`.
