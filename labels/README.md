# Stage 4 labels

Updated 2026-10-31T02:27:47Z. Every candidate and control gets the same rule, `label-v1`, written down before any outcome was looked at (docs/stage4.md in the code branch). Sessions count from the flag; returns are against the price at the flag. All rows: `labels/labels.csv`.

- **pump**: up 50% or more within 5 sessions, then down 40% or more from that peak within the next 10
- **real news**: earnings, a completed acquisition, a change of control, bankruptcy or a material agreement that isn't a share sale, filed with the SEC (8-K) between 72 hours before the flag and session 5; it beats pump
- **not pump**: neither, once the windows have closed (10 sessions; 15 after a 50% rise)
- **crash** (a separate label, for the avoid signal): a close 40% or more below the flag price within 10 sessions

| Archetype | Role | Pump | Real news | Not pump | Crash | Pending | Unknown |
|---|---|---|---|---|---|---|---|
| low float runner | candidate | 1 | 1 | 6 | 4 of 9 (44%) | 3 | 0 |
| low float runner | control | 0 | 1 | 24 | 2 of 25 (8%) | 6 | 0 |
| otc penny | candidate | 0 | 0 | 0 | - | 1 | 0 |
| otc penny | control | 0 | 0 | 0 | - | 2 | 0 |
| other | candidate | 2 | 64 | 133 | 9 of 148 (6%) | 97 | 0 |
| other | control | 0 | 90 | 263 | 1 of 279 (0%) | 229 | 0 |
| unknown | candidate | 0 | 0 | 0 | - | 0 | 1 |

Crash counts the snapshots whose crash label has settled.
87 of the labeled candidates were flagged in Stage 1's warm-up week (`warmup = 1`), when part of the chatter baseline was backfilled.

## Labeled so far

| Flagged (UTC) | Ticker | Role | Archetype | Label | Crash | Peak, 5 sessions | Drop from peak | Lowest close, 10 sessions | News filings |
|---|---|---|---|---|---|---|---|---|---|
| 2026-10-30 17:43 | OMCL | control | other | real news |  |  |  |  | 8-K 2026-10-29T10:35 2.02,9.01 (news) |
| 2026-10-30 17:00 | SBUX | candidate | other | real news |  |  |  |  | 8-K 2026-10-29T20:07 2.02,9.01 (news) |
| 2026-10-30 16:45 | CVSA | control | other | real news |  |  |  |  | 8-K 2026-10-29T20:16 2.02,9.01 (news) |
| 2026-10-30 15:55 | INDV | control | other | real news |  |  |  |  | 8-K 2026-10-29T11:00 2.02,9.01 (news) |
| 2026-10-30 15:15 | MSGR | control | other | real news |  |  |  |  | 8-K 2026-10-27T20:21 1.01,5.02,5.03,8.01,9.01 (news) |
| 2026-10-30 14:07 | COIN | candidate | other | real news |  |  |  |  | 8-K 2026-10-29T20:09 2.02,9.01 (news) |
| 2026-10-30 13:42 | NI | control | other | real news |  |  |  |  | 8-K 2026-10-28T10:35 2.02,9.01 (news) |
| 2026-10-30 13:25 | TT | control | other | real news |  |  |  |  | 8-K 2026-10-29T10:40 2.02,9.01 (news) |
| 2026-10-30 13:25 | SAIA | control | other | real news |  |  |  |  | 8-K 2026-10-29T11:45 2.02,5.02,7.01,8.01,9.01 (news) |
| 2026-10-30 09:12 | FE | control | other | real news |  |  |  |  | 8-K 2026-10-27T20:31 2.02,7.01,9.01 (news) |
| 2026-10-30 08:33 | EHC | control | other | real news |  |  |  |  | 8-K 2026-10-28T20:26 2.02,7.01,9.01 (news) |
| 2026-10-30 08:33 | BOOT | control | other | real news |  |  |  |  | 8-K 2026-10-28T20:04 2.02,7.01,9.01 (news) |
| 2026-10-30 00:00 | VTR | control | other | real news |  |  |  |  | 8-K 2026-10-27T20:32 2.02,9.01 (news) |
| 2026-10-29 22:53 | PAG | control | other | real news |  |  |  |  | 8-K 2026-10-28T13:04 2.02,7.01,9.01 (news) |
| 2026-10-29 22:12 | PINS | candidate | other | real news |  |  |  |  | 8-K 2026-10-29T20:07 2.02,9.01 (news) |
| 2026-10-29 22:12 | CRI | control | other | real news |  |  |  |  | 8-K 2026-10-30T10:11 2.02,5.02,8.01 (news) |
| 2026-10-29 21:35 | CROX | candidate | other | real news |  |  |  |  | 8-K 2026-10-29T11:02 2.02,9.01 (news) |
| 2026-10-29 20:27 | SNDK | candidate | other | real news |  |  |  |  | 8-K 2026-10-29T20:13 2.02,8.01,9.01 (news) |
| 2026-10-29 19:09 | GPI | control | other | real news |  |  |  |  | 8-K 2026-10-28T10:30 2.02,9.01 (news) |
| 2026-10-29 14:09 | LLY | candidate | other | real news |  |  |  |  | 8-K 2026-10-29T11:03 2.02,9.01 (news) |
| 2026-10-29 14:06 | RDDT | candidate | other | real news |  |  |  |  | 8-K 2026-10-29T20:08 2.02,9.01 (news) |
| 2026-10-29 14:06 | AMZN | candidate | other | real news |  |  |  |  | 8-K 2026-10-29T20:05 2.02,9.01 (news) |
| 2026-10-29 14:06 | TXT | control | other | real news |  |  |  |  | 8-K 2026-10-29T10:39 2.02,9.01 (news) |
| 2026-10-29 14:06 | NXT | control | other | real news |  |  |  |  | 8-K 2026-10-28T20:06 2.02,5.02,9.01 (news) |
| 2026-10-29 14:06 | LGND | control | other | real news |  |  |  |  | 8-K 2026-10-29T11:14 2.02,9.01 (news) |
| 2026-10-29 13:37 | PGC | control | other | real news |  |  |  |  | 8-K 2026-10-27T20:39 2.02,7.01,9.01 (news) |
| 2026-10-29 11:49 | INTC | candidate | other | real news |  |  |  |  | 8-K 2026-10-29T20:08 2.02,9.01 (news) |
| 2026-10-29 11:49 | CINF | control | other | real news |  |  |  |  | 8-K 2026-10-26T20:07 2.02,9.01 (news) |
| 2026-10-29 04:39 | PCAR | control | other | real news |  |  |  |  | 8-K 2026-10-27T12:05 2.02,9.01 (news) |
| 2026-10-29 04:06 | CVNA | candidate | other | real news |  |  |  |  | 8-K 2026-10-28T20:05 2.02,9.01 (news) |
| 2026-10-29 00:52 | FLS | control | other | real news |  |  |  |  | 8-K 2026-10-28T20:18 2.02,7.01,9.01 (news) |
| 2026-10-28 23:40 | VMC | control | other | real news |  |  |  |  | 8-K 2026-10-29T10:55 2.02,9.01 (news) |
| 2026-10-28 22:11 | CFFI | control | other | real news |  |  |  |  | 8-K 2026-10-26T20:24 2.02,9.01 (news) |
| 2026-10-28 21:57 | NOW | candidate | other | real news |  |  |  |  | 8-K 2026-10-28T21:10 2.02,9.01 (news) |
| 2026-10-28 21:46 | GOOGL | candidate | other | real news |  |  |  |  | 8-K 2026-10-28T20:01 2.02,9.01 (news) |
| 2026-10-28 21:20 | FTNT | candidate | other | real news |  |  |  |  | 8-K 2026-10-28T20:09 2.02,9.01 (news) |
| 2026-10-28 21:20 | NUE | control | other | real news |  |  |  |  | 8-K 2026-10-26T20:54 2.02,7.01,9.01 (news) |
| 2026-10-28 20:50 | GOOG | candidate | other | real news |  |  |  |  | 8-K 2026-10-28T20:01 2.02,9.01 (news) |
| 2026-10-28 16:10 | ENPH | candidate | other | real news |  |  |  |  | 8-K 2026-10-27T20:07 2.02,9.01 (news); 8-K 2026-10-29T20:06 8.01 |
| 2026-10-28 16:10 | PECO | control | other | real news |  |  |  |  | 8-K 2026-10-26T20:18 2.02,7.01,9.01 (news) |
| 2026-10-28 16:10 | EFOR | control | other | real news |  |  |  |  | 8-K 2026-10-28T20:09 2.02,9.01 (news) |
| 2026-10-28 11:39 | VRT | candidate | other | real news |  |  |  |  | 8-K 2026-10-28T10:02 2.02,7.01,9.01 (news) |
| 2026-10-28 11:39 | PSA | control | other | real news |  |  |  |  | 8-K 2026-10-26T20:11 2.02,9.01 (news) |
| 2026-10-28 00:47 | ITW | control | other | real news |  |  |  |  | 8-K 2026-10-27T13:20 2.02,9.01 (news) |
| 2026-10-27 20:57 | BBAI | candidate | other | real news |  |  |  |  | 8-K 2026-10-27T20:10 2.02 (news); 8-K/A 2026-10-27T22:20 2.02,9.01 |
| 2026-10-27 19:51 | AJG | control | other | real news |  |  |  |  | 8-K 2026-10-29T20:19 2.02,7.01 (news) |
| 2026-10-27 19:12 | STX | candidate | other | real news |  |  |  |  | 8-K 2026-10-27T20:12 2.02,7.01,9.01 (news); 8-K 2026-10-27T22:56 5.07 |
| 2026-10-27 19:12 | EQIX | control | other | real news |  |  |  |  | 8-K 2026-10-28T20:12 2.02,9.01 (news) |
| 2026-10-27 17:38 | GHC | control | other | real news |  |  |  |  | 8-K 2026-10-29T12:31 2.02,9.01 (news) |
| 2026-10-27 17:13 | MCHB | control | other | real news |  |  |  |  | 8-K 2026-10-28T20:28 2.02,7.01,9.01 (news) |

536 older rows are in `labels/labels.csv`.
