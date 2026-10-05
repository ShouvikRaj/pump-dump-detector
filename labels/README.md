# Stage 4 labels

Updated 2026-10-05T21:46:18Z. Every candidate and control gets the same rule, `label-v1`, written down before any outcome was looked at (docs/stage4.md in the code branch). Sessions count from the flag; returns are against the price at the flag. All rows: `labels/labels.csv`.

- **pump**: up 50% or more within 5 sessions, then down 40% or more from that peak within the next 10
- **real news**: earnings, a completed acquisition, a change of control, bankruptcy or a material agreement that isn't a share sale, filed with the SEC (8-K) between 72 hours before the flag and session 5; it beats pump
- **not pump**: neither, once the windows have closed (10 sessions; 15 after a 50% rise)
- **crash** (a separate label, for the avoid signal): a close 40% or more below the flag price within 10 sessions

| Archetype | Role | Pump | Real news | Not pump | Crash | Pending | Unknown |
|---|---|---|---|---|---|---|---|
| low float runner | candidate | 0 | 0 | 0 | - | 2 | 0 |
| low float runner | control | 0 | 0 | 0 | - | 4 | 0 |
| other | candidate | 0 | 1 | 0 | 1 of 1 (100%) | 10 | 0 |
| other | control | 0 | 0 | 0 | - | 22 | 0 |

Crash counts the snapshots whose crash label has settled.
1 of the labeled candidates was flagged in Stage 1's warm-up week (`warmup = 1`), when part of the chatter baseline was backfilled.

## Labeled so far

| Flagged (UTC) | Ticker | Role | Archetype | Label | Crash | Peak, 5 sessions | Drop from peak | Lowest close, 10 sessions | News filings |
|---|---|---|---|---|---|---|---|---|---|
| 2026-10-05 14:09 | SDEV | candidate | other | real news | yes |  |  |  | 8-K 2026-10-05T12:05 2.02,8.01,9.01 (news) |
