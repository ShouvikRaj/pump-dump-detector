# Stage 4 labels

Updated 2026-11-05T03:31:20Z. Every candidate and control gets the same rule, `label-v1`, written down before any outcome was looked at (docs/stage4.md in the code branch). Sessions count from the flag; returns are against the price at the flag. All rows: `labels/labels.csv`.

- **pump**: up 50% or more within 5 sessions, then down 40% or more from that peak within the next 10
- **real news**: earnings, a completed acquisition, a change of control, bankruptcy or a material agreement that isn't a share sale, filed with the SEC (8-K) between 72 hours before the flag and session 5; it beats pump
- **not pump**: neither, once the windows have closed (10 sessions; 15 after a 50% rise)
- **crash** (a separate label, for the avoid signal): a close 40% or more below the flag price within 10 sessions

| Archetype | Role | Pump | Real news | Not pump | Crash | Pending | Unknown |
|---|---|---|---|---|---|---|---|
| low float runner | candidate | 1 | 1 | 8 | 5 of 11 (45%) | 2 | 0 |
| low float runner | control | 0 | 1 | 27 | 2 of 28 (7%) | 8 | 0 |
| otc penny | candidate | 0 | 0 | 1 | 0 of 1 (0%) | 0 | 0 |
| otc penny | control | 0 | 0 | 1 | 0 of 1 (0%) | 1 | 0 |
| other | candidate | 2 | 88 | 156 | 9 of 184 (5%) | 103 | 0 |
| other | control | 0 | 105 | 325 | 1 of 357 (0%) | 255 | 0 |
| unknown | candidate | 0 | 0 | 0 | - | 0 | 1 |

Crash counts the snapshots whose crash label has settled.
87 of the labeled candidates were flagged in Stage 1's warm-up week (`warmup = 1`), when part of the chatter baseline was backfilled.

## Labeled so far

| Flagged (UTC) | Ticker | Role | Archetype | Label | Crash | Peak, 5 sessions | Drop from peak | Lowest close, 10 sessions | News filings |
|---|---|---|---|---|---|---|---|---|---|
| 2026-11-04 22:27 | BROS | candidate | other | real news |  |  |  |  | 8-K 2026-11-04T21:15 2.02,7.01,9.01 (news) |
| 2026-11-04 22:27 | PCVX | control | other | real news |  |  |  |  | 8-K 2026-11-04T21:08 2.02,9.01 (news) |
| 2026-11-04 21:19 | COHR | candidate | other | real news |  |  |  |  | 8-K 2026-11-04T21:05 2.02,7.01,9.01 (news) |
| 2026-11-04 21:19 | APP | candidate | other | real news |  |  |  |  | 8-K 2026-11-04T21:08 2.02,5.07,9.01 (news) |
| 2026-11-04 21:19 | LNG | control | other | real news |  |  |  |  | 8-K 2026-11-03T13:14 1.01,7.01,9.01 (news) |
| 2026-11-04 19:21 | MCD | candidate | other | real news |  |  |  |  | 8-K 2026-11-04T12:01 2.02,9.01 (news) |
| 2026-11-04 18:32 | RVTY | control | other | real news |  |  |  |  | 8-K 2026-11-03T13:16 2.02,8.01,9.01 (news) |
| 2026-11-04 18:08 | SHC | control | other | real news |  |  |  |  | 8-K 2026-11-03T13:11 2.02,9.01 (news) |
| 2026-11-04 15:47 | DUOL | candidate | other | real news |  |  |  |  | 8-K 2026-11-03T21:06 2.02,9.01 (news) |
| 2026-11-04 15:47 | MCY | control | other | real news |  |  |  |  | 8-K 2026-11-03T21:07 2.02,9.01 (news) |
| 2026-11-04 15:47 | BR | control | other | real news |  |  |  |  | 8-K 2026-11-03T13:10 2.02,9.01 (news) |
| 2026-11-04 15:35 | UBER | candidate | other | real news |  |  |  |  | 8-K 2026-11-04T11:55 2.02,5.02,9.01 (news) |
| 2026-11-03 23:11 | NVTS | candidate | other | real news |  |  |  |  | 8-K 2026-11-03T21:08 2.02,7.01,9.01 (news) |
| 2026-11-03 21:29 | ANET | candidate | other | real news |  |  |  |  | 8-K 2026-11-03T21:10 2.02,9.01 (news) |
| 2026-11-03 21:29 | ALAB | candidate | other | real news |  |  |  |  | 8-K 2026-11-03T21:09 2.02,9.01 (news) |
| 2026-11-03 18:57 | DDOG | candidate | other | real news |  |  |  |  | 8-K 2026-11-04T12:11 2.02,9.01 (news) |
| 2026-11-03 15:08 | AEHR | candidate | other | real news |  |  |  |  | 8-K 2026-11-02T21:21 2.02,9.01 (news) |
| 2026-11-02 21:58 | AMD | candidate | other | real news |  |  |  |  | 8-K 2026-11-03T21:16 2.02,7.01,9.01 (news) |
| 2026-11-02 21:29 | TBLA | control | other | real news |  |  |  |  | 8-K 2026-11-04T11:02 2.02,7.01,9.01 (news) |
| 2026-11-02 21:16 | LITE | candidate | other | real news |  |  |  |  | 8-K 2026-11-02T13:39 1.01,5.02,7.01,9.01 (news) |
| 2026-11-02 21:05 | MRVL | candidate | other | real news |  |  |  |  | 8-K 2026-11-02T13:09 1.01,9.01 (news) |
| 2026-11-02 20:10 | AAPL | candidate | other | real news |  |  |  |  | 8-K 2026-11-02T21:30 2.02,9.01 (news) |
| 2026-11-02 20:10 | IT | control | other | real news |  |  |  |  | 8-K 2026-11-03T13:05 2.02,7.01,9.01 (news) |
| 2026-11-02 18:46 | SMCI | candidate | other | real news |  |  |  |  | 8-K 2026-11-03T21:31 2.02,8.01,9.01 (news) |
| 2026-11-02 13:09 | PLTR | candidate | other | real news |  |  |  |  | 8-K 2026-11-02T21:06 2.02,7.01,9.01 (news) |
| 2026-11-02 13:09 | IT | control | other | real news |  |  |  |  | 8-K 2026-11-03T13:05 2.02,7.01,9.01 (news) |
| 2026-11-02 07:17 | VNO | control | other | real news |  |  |  |  | 8-K 2026-11-02T21:40 2.02,9.01 (news) |
| 2026-11-01 19:38 | NNN | candidate | other | real news |  |  |  |  | 8-K 2026-11-04T13:30 2.02,9.01 (news) |
| 2026-10-30 22:07 | INSP | control | other | real news |  |  |  |  | 8-K 2026-11-02T21:29 2.02,7.01,9.01 (news) |
| 2026-10-30 17:43 | OMCL | control | other | real news |  |  |  |  | 8-K 2026-10-29T10:35 2.02,9.01 (news) |
| 2026-10-30 17:00 | SBUX | candidate | other | real news |  |  |  |  | 8-K 2026-10-29T20:07 2.02,9.01 (news) |
| 2026-10-30 16:45 | CVSA | control | other | real news |  |  |  |  | 8-K 2026-10-29T20:16 2.02,9.01 (news) |
| 2026-10-30 15:55 | INDV | control | other | real news |  |  |  |  | 8-K 2026-10-29T11:00 2.02,9.01 (news); 8-K 2026-11-02T14:27 1.01,2.01,2.03,5.02,5.03,7.01,9.01 (news) |
| 2026-10-30 15:55 | CBLL | control | other | real news |  |  |  |  | 8-K 2026-11-03T21:36 2.02,9.01 (news) |
| 2026-10-30 15:15 | MSGR | control | other | real news |  |  |  |  | 8-K 2026-10-27T20:21 1.01,5.02,5.03,8.01,9.01 (news) |
| 2026-10-30 14:07 | COIN | candidate | other | real news |  |  |  |  | 8-K 2026-10-29T20:09 2.02,9.01 (news) |
| 2026-10-30 13:42 | SMCI | candidate | other | real news |  |  |  |  | 8-K 2026-11-03T21:31 2.02,8.01,9.01 (news) |
| 2026-10-30 13:42 | NI | control | other | real news |  |  |  |  | 8-K 2026-10-28T10:35 2.02,9.01 (news) |
| 2026-10-30 13:42 | CNA | control | other | real news |  |  |  |  | 8-K 2026-11-02T11:09 2.02,9.01 (news) |
| 2026-10-30 13:25 | AMD | candidate | other | real news |  |  |  |  | 8-K 2026-11-03T21:16 2.02,7.01,9.01 (news) |
| 2026-10-30 13:25 | TT | control | other | real news |  |  |  |  | 8-K 2026-10-29T10:40 2.02,9.01 (news) |
| 2026-10-30 13:25 | SAIA | control | other | real news |  |  |  |  | 8-K 2026-10-29T11:45 2.02,5.02,7.01,8.01,9.01 (news) |
| 2026-10-30 09:12 | FE | control | other | real news |  |  |  |  | 8-K 2026-10-27T20:31 2.02,7.01,9.01 (news) |
| 2026-10-30 08:33 | PLTR | candidate | other | real news |  |  |  |  | 8-K 2026-11-02T21:06 2.02,7.01,9.01 (news) |
| 2026-10-30 08:33 | EHC | control | other | real news |  |  |  |  | 8-K 2026-10-28T20:26 2.02,7.01,9.01 (news) |
| 2026-10-30 08:33 | BOOT | control | other | real news |  |  |  |  | 8-K 2026-10-28T20:04 2.02,7.01,9.01 (news) |
| 2026-10-30 00:00 | VTR | control | other | real news |  |  |  |  | 8-K 2026-10-27T20:32 2.02,9.01 (news) |
| 2026-10-29 22:53 | AAPL | candidate | other | real news |  |  |  |  | 8-K 2026-11-02T21:30 2.02,9.01 (news) |
| 2026-10-29 22:53 | PAG | control | other | real news |  |  |  |  | 8-K 2026-10-28T13:04 2.02,7.01,9.01 (news) |
| 2026-10-29 22:12 | PINS | candidate | other | real news |  |  |  |  | 8-K 2026-10-29T20:07 2.02,9.01 (news) |

667 older rows are in `labels/labels.csv`.
