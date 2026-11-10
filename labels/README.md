# Stage 4 labels

Updated 2026-11-10T04:39:20Z. Every candidate and control gets the same rule, `label-v1`, written down before any outcome was looked at (docs/stage4.md in the code branch). Sessions count from the flag; returns are against the price at the flag. All rows: `labels/labels.csv`.

- **pump**: up 50% or more within 5 sessions, then down 40% or more from that peak within the next 10
- **real news**: earnings, a completed acquisition, a change of control, bankruptcy or a material agreement that isn't a share sale, filed with the SEC (8-K) between 72 hours before the flag and session 5; it beats pump
- **not pump**: neither, once the windows have closed (10 sessions; 15 after a 50% rise)
- **crash** (a separate label, for the avoid signal): a close 40% or more below the flag price within 10 sessions

| Archetype | Role | Pump | Real news | Not pump | Crash | Pending | Unknown |
|---|---|---|---|---|---|---|---|
| low float runner | candidate | 1 | 1 | 8 | 6 of 12 (50%) | 3 | 0 |
| low float runner | control | 0 | 2 | 27 | 2 of 28 (7%) | 11 | 0 |
| otc penny | candidate | 0 | 0 | 1 | 0 of 1 (0%) | 0 | 0 |
| otc penny | control | 0 | 0 | 2 | 0 of 2 (0%) | 0 | 0 |
| other | candidate | 3 | 110 | 197 | 16 of 238 (7%) | 88 | 0 |
| other | control | 0 | 148 | 391 | 2 of 454 (0%) | 242 | 0 |
| unknown | candidate | 0 | 0 | 0 | - | 0 | 2 |

Crash counts the snapshots whose crash label has settled.
87 of the labeled candidates were flagged in Stage 1's warm-up week (`warmup = 1`), when part of the chatter baseline was backfilled.

## Labeled so far

| Flagged (UTC) | Ticker | Role | Archetype | Label | Crash | Peak, 5 sessions | Drop from peak | Lowest close, 10 sessions | News filings |
|---|---|---|---|---|---|---|---|---|---|
| 2026-11-09 22:33 | ASTS | candidate | other | real news |  |  |  |  | 8-K 2026-11-09T21:49 2.02,7.01,9.01 (news) |
| 2026-11-09 21:25 | RKLB | candidate | other | real news |  |  |  |  | 8-K 2026-11-09T21:06 2.02,9.01 (news) |
| 2026-11-09 21:11 | TTD | candidate | other | real news |  |  |  |  | 8-K 2026-11-09T21:09 2.02,8.01,9.01 (news) |
| 2026-11-09 11:01 | FLR | control | other | real news |  |  |  |  | 8-K 2026-11-06T12:04 2.02,9.01 (news) |
| 2026-11-07 02:18 | TMCI | control | other | real news |  |  |  |  | 8-K 2026-11-06T12:05 2.02,9.01 (news) |
| 2026-11-06 20:47 | TALO | control | other | real news |  |  |  |  | 8-K 2026-11-03T22:05 2.02,7.01,9.01 (news) |
| 2026-11-06 18:01 | GRND | candidate | other | real news |  |  |  |  | 8-K 2026-11-05T21:18 2.02,9.01 (news) |
| 2026-11-06 18:01 | ZLAB | control | other | real news |  |  |  |  | 8-K 2026-11-05T11:36 2.02,9.01 (news) |
| 2026-11-06 16:54 | SPG | control | other | real news |  |  |  |  | 8-K 2026-11-05T21:08 2.02,7.01,9.01 (news) |
| 2026-11-06 15:46 | INOD | candidate | other | real news |  |  |  |  | 8-K 2026-11-05T21:07 2.02,9.01 (news) |
| 2026-11-06 15:46 | LBRX | control | other | real news |  |  |  |  | 8-K 2026-11-05T21:16 2.02,9.01 (news) |
| 2026-11-06 14:52 | DKNG | candidate | other | real news |  |  |  |  | 8-K 2026-11-06T11:50 2.02,9.01 (news) |
| 2026-11-06 09:05 | DCH | control | other | real news |  |  |  |  | 8-K 2026-11-06T13:00 2.02,7.01,9.01 (news) |
| 2026-11-05 23:26 | DTE | control | other | real news |  |  |  |  | 8-K 2026-11-05T12:05 1.01,9.01 (news); 8-K 2026-11-06T21:18 2.02,9.01 (news); 8-K 2026-11-06T21:28 7.01,9.01 |
| 2026-11-05 22:33 | IONQ | candidate | other | real news |  |  |  |  | 8-K 2026-11-05T21:07 2.01,2.02,3.02,7.01,9.01 (news) |
| 2026-11-05 22:33 | ABNB | candidate | other | real news |  |  |  |  | 8-K 2026-11-05T21:02 2.02,9.01 (news) |
| 2026-11-05 22:06 | ANT | candidate | unknown | unknown (no price at the flag) |  |  |  |  |  |
| 2026-11-05 19:19 | TGLS | control | other | real news |  |  |  |  | 8-K 2026-11-05T12:10 2.02,9.01 (news) |
| 2026-11-05 19:19 | OPCH | control | other | real news |  |  |  |  | 8-K 2026-11-04T11:55 2.02,9.01 (news) |
| 2026-11-05 16:25 | DNUT | candidate | other | real news |  |  |  |  | 8-K 2026-11-05T11:53 2.02 (news); 8-K 2026-11-05T21:44 5.02 |
| 2026-11-05 13:17 | XNCR | control | other | real news |  |  |  |  | 8-K 2026-11-04T21:01 2.02,9.01 (news) |
| 2026-11-05 13:17 | CLDX | control | other | real news |  |  |  |  | 8-K 2026-11-05T21:01 2.02,9.01 (news) |
| 2026-11-05 09:54 | AGO | control | other | real news |  |  |  |  | 8-K 2026-11-05T21:21 2.02,9.01 (news); 8-K 2026-11-06T14:07 7.01 |
| 2026-11-05 08:22 | OVV | control | other | real news |  |  |  |  | 8-K 2026-11-03T22:04 2.02,8.01,9.01 (news) |
| 2026-11-05 04:50 | URGN | control | other | real news |  |  |  |  | 8-K 2026-11-04T13:08 2.02,9.01 (news) |
| 2026-11-05 00:45 | UI | control | other | real news |  |  |  |  | 8-K 2026-11-06T12:10 2.02,9.01 (news) |
| 2026-11-04 22:27 | BROS | candidate | other | real news |  |  |  |  | 8-K 2026-11-04T21:15 2.02,7.01,9.01 (news); 8-K 2026-11-06T21:07 5.02,7.01,9.01 |
| 2026-11-04 22:27 | SPNT | control | other | real news |  |  |  |  | 8-K 2026-11-03T21:21 5.02; 8-K 2026-11-05T21:11 2.02,7.01,8.01,9.01 (news) |
| 2026-11-04 22:27 | PCVX | control | other | real news |  |  |  |  | 8-K 2026-11-04T21:08 2.02,9.01 (news) |
| 2026-11-04 21:19 | COHR | candidate | other | real news |  |  |  |  | 8-K 2026-11-04T21:05 2.02,7.01,9.01 (news) |
| 2026-11-04 21:19 | APP | candidate | other | real news |  |  |  |  | 8-K 2026-11-04T21:08 2.02,5.07,9.01 (news) |
| 2026-11-04 21:19 | ROK | control | other | real news |  |  |  |  | 8-K 2026-11-05T12:02 2.02,9.01 (news) |
| 2026-11-04 21:19 | MET | control | other | real news |  |  |  |  | 8-K 2026-11-04T21:22 2.02,7.01,8.01,9.01 (news) |
| 2026-11-04 21:19 | LNG | control | other | real news |  |  |  |  | 8-K 2026-11-03T13:14 1.01,7.01,9.01 (news) |
| 2026-11-04 21:07 | RLJ | control | other | real news |  |  |  |  | 8-K 2026-11-04T22:21 2.02,9.01 (news) |
| 2026-11-04 19:48 | PH | control | other | real news |  |  |  |  | 8-K 2026-11-03T21:04 5.07; 8-K 2026-11-05T12:52 2.02,9.01 (news) |
| 2026-11-04 19:21 | MCD | candidate | other | real news |  |  |  |  | 8-K 2026-11-04T12:01 2.02,9.01 (news) |
| 2026-11-04 18:32 | RVTY | control | other | real news |  |  |  |  | 8-K 2026-11-03T13:16 2.02,8.01,9.01 (news) |
| 2026-11-04 18:08 | QCOM | candidate | other | real news |  |  |  |  | 8-K 2026-11-04T21:03 2.02,9.01 (news) |
| 2026-11-04 18:08 | IREN | candidate | other | real news |  |  |  |  | 8-K 2026-11-05T21:03 2.02,9.01 (news) |
| 2026-11-04 18:08 | WES | control | other | real news |  |  |  |  | 8-K 2026-11-04T21:11 2.02,9.01 (news) |
| 2026-11-04 18:08 | SHC | control | other | real news |  |  |  |  | 8-K 2026-11-03T13:11 2.02,9.01 (news) |
| 2026-11-04 15:47 | VST | candidate | other | real news |  |  |  |  | 8-K 2026-11-05T11:02 2.01,2.03,3.02,7.01,9.01 (news); 8-K 2026-11-06T12:01 2.02,9.01 (news) |
| 2026-11-04 15:47 | DUOL | candidate | other | real news |  |  |  |  | 8-K 2026-11-03T21:06 2.02,9.01 (news) |
| 2026-11-04 15:47 | SRE | control | other | real news |  |  |  |  | 8-K 2026-11-05T15:53 2.02,9.01 (news) |
| 2026-11-04 15:47 | MCY | control | other | real news |  |  |  |  | 8-K 2026-11-03T21:07 2.02,9.01 (news) |
| 2026-11-04 15:47 | IPAR | control | other | real news |  |  |  |  | 8-K 2026-11-04T21:49 2.02,7.01,8.01,9.01 (news) |
| 2026-11-04 15:47 | BR | control | other | real news |  |  |  |  | 8-K 2026-11-03T13:10 2.02,9.01 (news) |
| 2026-11-04 15:35 | UBER | candidate | other | real news |  |  |  |  | 8-K 2026-11-04T11:55 2.02,5.02,9.01 (news) |
| 2026-11-04 14:27 | MSGK | control | other | real news |  |  |  |  | 8-K 2026-11-06T12:35 2.02,9.01 (news) |

843 older rows are in `labels/labels.csv`.
