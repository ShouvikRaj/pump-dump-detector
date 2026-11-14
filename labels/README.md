# Stage 4 labels

Updated 2026-11-14T03:21:26Z. Every candidate and control gets the same rule, `label-v1`, written down before any outcome was looked at (docs/stage4.md in the code branch). Sessions count from the flag; returns are against the price at the flag. All rows: `labels/labels.csv`.

- **pump**: up 50% or more within 5 sessions, then down 40% or more from that peak within the next 10
- **real news**: earnings, a completed acquisition, a change of control, bankruptcy or a material agreement that isn't a share sale, filed with the SEC (8-K) between 72 hours before the flag and session 5; it beats pump
- **not pump**: neither, once the windows have closed (10 sessions; 15 after a 50% rise)
- **crash** (a separate label, for the avoid signal): a close 40% or more below the flag price within 10 sessions

| Archetype | Role | Pump | Real news | Not pump | Crash | Pending | Unknown |
|---|---|---|---|---|---|---|---|
| low float runner | candidate | 1 | 2 | 9 | 7 of 13 (54%) | 3 | 0 |
| low float runner | control | 0 | 4 | 31 | 3 of 34 (9%) | 13 | 0 |
| otc penny | candidate | 0 | 0 | 1 | 0 of 1 (0%) | 0 | 0 |
| otc penny | control | 0 | 0 | 2 | 0 of 2 (0%) | 0 | 0 |
| other | candidate | 3 | 126 | 238 | 20 of 311 (6%) | 71 | 0 |
| other | control | 0 | 159 | 493 | 2 of 602 (0%) | 205 | 0 |
| unknown | candidate | 0 | 0 | 0 | - | 0 | 3 |

Crash counts the snapshots whose crash label has settled.
87 of the labeled candidates were flagged in Stage 1's warm-up week (`warmup = 1`), when part of the chatter baseline was backfilled.

## Labeled so far

| Flagged (UTC) | Ticker | Role | Archetype | Label | Crash | Peak, 5 sessions | Drop from peak | Lowest close, 10 sessions | News filings |
|---|---|---|---|---|---|---|---|---|---|
| 2026-11-13 16:24 | KLXE | control | other | real news |  |  |  |  | 8-K 2026-11-10T21:12 2.02,7.01,9.01 (news) |
| 2026-11-13 01:09 | SLS | candidate | other | real news |  |  |  |  | 8-K 2026-11-12T21:07 2.02,9.01 (news) |
| 2026-11-12 21:20 | CSCO | candidate | other | real news |  |  |  |  | 8-K 2026-11-12T21:06 2.02,9.01 (news) |
| 2026-11-12 20:43 | TDG | control | other | real news |  |  |  |  | 8-K 2026-11-10T11:32 2.02,9.01 (news) |
| 2026-11-12 18:42 | AMAT | candidate | other | real news |  |  |  |  | 8-K 2026-11-12T21:02 2.02,9.01 (news) |
| 2026-11-12 17:34 | TRT | candidate | low float runner | real news |  |  |  |  | 8-K 2026-11-12T17:28 2.02,9.01 (news) |
| 2026-11-12 17:34 | PMN | control | low float runner | real news |  |  |  |  | 8-K 2026-11-12T13:00 7.01,9.01; 8-K 2026-11-12T21:17 2.02,9.01 (news) |
| 2026-11-12 17:34 | IMUX | control | low float runner | real news |  |  |  |  | 8-K 2026-11-13T13:00 2.02,9.01 (news) |
| 2026-11-12 16:56 | CBRS | candidate | other | real news |  |  |  |  | 8-K 2026-11-12T21:03 2.02,9.01 (news) |
| 2026-11-12 14:43 | LUNR | candidate | other | real news |  |  |  |  | 8-K 2026-11-12T12:32 2.02,9.01 (news) |
| 2026-11-10 21:21 | RGTI | candidate | other | real news |  |  |  |  | 8-K 2026-11-10T21:05 2.02,9.01 (news) |
| 2026-11-10 20:00 | CRWV | candidate | other | real news |  |  |  |  | 8-K 2026-11-10T21:05 2.02,9.01 (news) |
| 2026-11-10 16:24 | TTWO | candidate | other | real news |  |  |  |  | 8-K 2026-11-09T21:10 2.02,9.01 (news) |
| 2026-11-10 14:52 | ANT | candidate | unknown | unknown (no price at the flag) |  |  |  |  |  |
| 2026-11-09 22:33 | ASTS | candidate | other | real news |  |  |  |  | 8-K 2026-11-09T21:49 2.02,7.01,9.01 (news); 8-K 2026-11-10T13:00 7.01,9.01 |
| 2026-11-09 22:18 | TDG | control | other | real news |  |  |  |  | 8-K 2026-11-10T11:32 2.02,9.01 (news) |
| 2026-11-09 21:25 | RKLB | candidate | other | real news |  |  |  |  | 8-K 2026-11-09T21:06 2.02,9.01 (news) |
| 2026-11-09 21:11 | TTD | candidate | other | real news |  |  |  |  | 8-K 2026-11-09T21:09 2.02,8.01,9.01 (news) |
| 2026-11-09 20:48 | ONDS | candidate | other | real news |  | +2% |  |  | 8-K 2026-11-12T13:24 2.02,9.01 (news) |
| 2026-11-09 11:01 | FLR | control | other | real news |  | +11% |  |  | 8-K 2026-11-06T12:04 2.02,9.01 (news) |
| 2026-11-07 03:40 | RKLB | candidate | other | real news |  | +27% |  |  | 8-K 2026-11-09T21:06 2.02,9.01 (news) |
| 2026-11-07 02:18 | SPCE | candidate | other | real news |  | +7% |  |  | 8-K 2026-11-12T21:31 2.02,7.01,8.01,9.01 (news); 8-K 2026-11-13T13:39 3.02,8.01 |
| 2026-11-07 02:18 | TMCI | control | other | real news |  | +32% |  |  | 8-K 2026-11-06T12:05 2.02,9.01 (news) |
| 2026-11-07 02:18 | RCKT | control | other | real news |  | +8% |  |  | 8-K 2026-11-12T21:15 2.02,9.01 (news) |
| 2026-11-06 20:47 | LUNR | candidate | other | real news |  | +40% |  |  | 8-K 2026-11-12T12:32 2.02,9.01 (news) |
| 2026-11-06 20:47 | TALO | control | other | real news |  | +8% |  |  | 8-K 2026-11-03T22:05 2.02,7.01,9.01 (news) |
| 2026-11-06 18:01 | GRND | candidate | other | real news |  | +8% |  |  | 8-K 2026-11-05T21:18 2.02,9.01 (news) |
| 2026-11-06 18:01 | ZLAB | control | other | real news |  | +14% |  |  | 8-K 2026-11-05T11:36 2.02,9.01 (news) |
| 2026-11-06 16:54 | SPG | control | other | real news |  | +4% |  |  | 8-K 2026-11-05T21:08 2.02,7.01,9.01 (news) |
| 2026-11-06 15:46 | INOD | candidate | other | real news |  | +14% |  |  | 8-K 2026-11-05T21:07 2.02,9.01 (news) |
| 2026-11-06 15:46 | LBRX | control | other | real news |  | +16% |  |  | 8-K 2026-11-05T21:16 2.02,9.01 (news) |
| 2026-11-06 14:52 | DKNG | candidate | other | real news |  | +16% |  |  | 8-K 2026-11-06T11:50 2.02,9.01 (news) |
| 2026-11-06 09:05 | KORU | candidate | other | not pump |  | +25% |  |  |  |
| 2026-11-06 09:05 | DCH | control | other | real news |  | +8% |  |  | 8-K 2026-11-06T13:00 2.02,7.01,9.01 (news) |
| 2026-11-06 09:05 | CCAP | control | other | real news |  | +10% |  |  | 8-K 2026-11-09T21:10 2.02,9.01 (news) |
| 2026-11-06 07:56 | TQQQ | candidate | other | not pump |  | +21% |  |  |  |
| 2026-11-06 07:56 | ASTS | candidate | other | real news |  | +24% |  |  | 8-K 2026-11-06T22:00 7.01,9.01; 8-K 2026-11-09T21:49 2.02,7.01,9.01 (news); 8-K 2026-11-10T13:00 7.01,9.01 |
| 2026-11-06 04:28 | LABT | candidate | other | real news | yes | -4% |  |  | 8-K 2026-11-10T22:20 1.01,7.01,9.01 (news) |
| 2026-11-06 03:36 | AROC | control | other | real news |  | +10% |  |  | 8-K 2026-11-04T13:59 7.01; 8-K 2026-11-10T21:24 1.01,7.01,9.01 (news) |
| 2026-11-06 02:44 | QQQ | candidate | other | not pump |  | +7% |  |  |  |
| 2026-11-06 02:44 | TDG | control | other | real news |  | +6% |  |  | 8-K 2026-11-10T11:32 2.02,9.01 (news) |
| 2026-11-06 00:59 | EWY | candidate | other | not pump |  | +13% |  |  |  |
| 2026-11-05 23:26 | SGOV | candidate | other | not pump |  | +0% |  |  |  |
| 2026-11-05 23:26 | DTE | control | other | real news |  | +4% |  |  | 8-K 2026-11-05T12:05 1.01,9.01 (news); 8-K 2026-11-06T21:18 2.02,9.01 (news); 8-K 2026-11-06T21:28 7.01,9.01 |
| 2026-11-05 23:10 | VTI | candidate | other | not pump |  | +5% |  |  |  |
| 2026-11-05 22:33 | IONQ | candidate | other | real news |  | +33% |  |  | 8-K 2026-11-05T21:07 2.01,2.02,3.02,7.01,9.01 (news) |
| 2026-11-05 22:33 | ABNB | candidate | other | real news |  | +6% |  |  | 8-K 2026-11-05T21:02 2.02,9.01 (news) |
| 2026-11-05 22:33 | HRB | control | other | real news |  | -2% |  |  | 8-K 2026-11-09T21:11 2.02,7.01,9.01 (news) |
| 2026-11-05 22:19 | VOO | candidate | other | not pump |  | +4% |  |  |  |
| 2026-11-05 22:06 | ANT | candidate | unknown | unknown (no price at the flag) |  |  |  |  |  |

1022 older rows are in `labels/labels.csv`.
