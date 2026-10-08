# Stage 4 labels

Updated 2026-10-08T23:23:01Z. Every candidate and control gets the same rule, `label-v1`, written down before any outcome was looked at (docs/stage4.md in the code branch). Sessions count from the flag; returns are against the price at the flag. All rows: `labels/labels.csv`.

- **pump**: up 50% or more within 5 sessions, then down 40% or more from that peak within the next 10
- **real news**: earnings, a completed acquisition, a change of control, bankruptcy or a material agreement that isn't a share sale, filed with the SEC (8-K) between 72 hours before the flag and session 5; it beats pump
- **not pump**: neither, once the windows have closed (10 sessions; 15 after a 50% rise)
- **crash** (a separate label, for the avoid signal): a close 40% or more below the flag price within 10 sessions

| Archetype | Role | Pump | Real news | Not pump | Crash | Pending | Unknown |
|---|---|---|---|---|---|---|---|
| low float runner | candidate | 0 | 0 | 0 | - | 3 | 0 |
| low float runner | control | 0 | 0 | 0 | - | 7 | 0 |
| other | candidate | 0 | 5 | 0 | 1 of 1 (100%) | 55 | 0 |
| other | control | 0 | 2 | 0 | - | 117 | 0 |

Crash counts the snapshots whose crash label has settled.
5 of the labeled candidates were flagged in Stage 1's warm-up week (`warmup = 1`), when part of the chatter baseline was backfilled.

## Labeled so far

| Flagged (UTC) | Ticker | Role | Archetype | Label | Crash | Peak, 5 sessions | Drop from peak | Lowest close, 10 sessions | News filings |
|---|---|---|---|---|---|---|---|---|---|
| 2026-10-07 20:37 | LEVI | candidate | other | real news |  |  |  |  | 8-K 2026-10-07T20:12 2.02,9.01 (news) |
| 2026-10-07 12:08 | NSLRL | control | other | real news |  |  |  |  | 8-K 2026-10-06T00:05 2.02,8.01,9.01 (news) |
| 2026-10-06 18:01 | PENG | candidate | other | real news |  |  |  |  | 8-K 2026-10-06T20:27 2.02,9.01 (news); 8-K 2026-10-06T20:34 2.02,5.02,7.01,9.01 (news) |
| 2026-10-06 11:49 | REGN | control | other | real news |  |  |  |  | 8-K 2026-10-06T11:51 1.01,2.02,8.01 (news) |
| 2026-10-05 23:41 | ALEC | candidate | other | real news |  |  |  |  | 8-K 2026-10-05T11:00 1.01,2.02,7.01,8.01,9.01 (news) |
| 2026-10-05 14:23 | APLD | candidate | other | real news |  |  |  |  | 8-K 2026-10-07T20:43 2.02,9.01 (news) |
| 2026-10-05 14:09 | SDEV | candidate | other | real news | yes |  |  |  | 8-K 2026-10-05T12:05 2.02,8.01,9.01 (news) |
