# Stage 4 labels

Updated 2026-11-28T04:45:13Z. Every candidate and control gets the same rule, `label-v1`, written down before any outcome was looked at (docs/stage4.md in the code branch). Sessions count from the flag; returns are against the price at the flag. All rows: `labels/labels.csv`.

- **pump**: up 50% or more within 5 sessions, then down 40% or more from that peak within the next 10
- **real news**: earnings, a completed acquisition, a change of control, bankruptcy or a material agreement that isn't a share sale, filed with the SEC (8-K) between 72 hours before the flag and session 5; it beats pump
- **not pump**: neither, once the windows have closed (10 sessions; 15 after a 50% rise)
- **crash** (a separate label, for the avoid signal): a close 40% or more below the flag price within 10 sessions

| Archetype | Role | Pump | Real news | Not pump | Crash | Pending | Unknown |
|---|---|---|---|---|---|---|---|
| low float runner | candidate | 1 | 4 | 11 | 7 of 15 (47%) | 2 | 0 |
| low float runner | control | 0 | 5 | 42 | 5 of 48 (10%) | 7 | 0 |
| otc penny | candidate | 0 | 0 | 1 | 0 of 1 (0%) | 0 | 0 |
| otc penny | control | 0 | 0 | 2 | 0 of 2 (0%) | 0 | 0 |
| other | candidate | 7 | 138 | 310 | 27 of 435 (6%) | 47 | 0 |
| other | control | 1 | 164 | 686 | 2 of 846 (0%) | 134 | 0 |
| unknown | candidate | 0 | 0 | 0 | - | 0 | 5 |

Crash counts the snapshots whose crash label has settled.
87 of the labeled candidates were flagged in Stage 1's warm-up week (`warmup = 1`), when part of the chatter baseline was backfilled.

## Labeled so far

| Flagged (UTC) | Ticker | Role | Archetype | Label | Crash | Peak, 5 sessions | Drop from peak | Lowest close, 10 sessions | News filings |
|---|---|---|---|---|---|---|---|---|---|
| 2026-11-24 21:15 | DELL | candidate | other | real news |  |  |  |  | 8-K 2026-11-24T21:09 2.02,9.01 (news) |
| 2026-11-24 00:45 | HPE | candidate | other | real news |  |  |  |  | 8-K 2026-11-23T21:12 2.02,7.01,9.01 (news) |
| 2026-11-21 00:55 | CRWD | candidate | other | real news |  |  |  |  | 8-K 2026-11-23T11:04 2.02,9.01 (news); 8-K 2026-11-23T11:15 1.01,7.01,9.01 (news) |
| 2026-11-21 00:55 | WWD | control | other | real news |  |  |  |  | 8-K 2026-11-18T21:00 2.02,9.01 (news) |
| 2026-11-20 18:35 | TLT | candidate | other | not pump |  | +2% |  |  |  |
| 2026-11-20 14:10 | SGOV | candidate | other | not pump |  | +0% |  |  |  |
| 2026-11-20 14:10 | DE | control | other | real news |  | +7% |  |  | 8-K 2026-11-25T11:00 2.02,7.01,9.01 (news) |
| 2026-11-20 03:06 | ROPE | candidate | other | not pump |  | +3% |  |  |  |
| 2026-11-20 03:06 | INTU | candidate | other | real news |  | +7% |  |  | 8-K 2026-11-19T22:26 1.01,8.01,9.01 (news) |
| 2026-11-20 03:06 | ADSK | control | other | real news |  | +8% |  |  | 8-K 2026-11-24T21:05 2.02,7.01,9.01 (news) |
| 2026-11-20 00:51 | OPEX | candidate | other | not pump | yes | +11% |  |  |  |
| 2026-11-19 03:02 | CRWD | candidate | other | real news |  | +2% |  |  | 8-K 2026-11-23T11:04 2.02,9.01 (news); 8-K 2026-11-23T11:15 1.01,7.01,9.01 (news) |
| 2026-11-19 00:42 | ANT | candidate | unknown | unknown (no price at the flag) |  |  |  |  |  |
| 2026-11-18 21:40 | PANW | candidate | other | real news |  | -1% |  |  | 8-K 2026-11-18T21:37 2.02,3.02,7.01,8.01,9.01 (news) |
| 2026-11-17 18:16 | SOXX | candidate | other | not pump |  | +7% |  |  |  |
| 2026-11-17 14:06 | SPAI | candidate | low float runner | real news |  | +13% |  |  | 8-K 2026-11-16T22:12 2.02,9.01 (news) |
| 2026-11-17 10:45 | SHAZ | candidate | other | real news |  | +27% |  |  | 8-K 2026-11-16T21:15 2.02,7.01,9.01 (news) |
| 2026-11-17 06:59 | ROPE | candidate | other | not pump |  | -0% |  |  |  |
| 2026-11-17 03:38 | RSP | candidate | other | not pump |  | +0% |  |  |  |
| 2026-11-17 01:13 | TQQQ | candidate | other | not pump |  | +6% |  |  |  |
| 2026-11-17 01:13 | VVV | control | other | real news |  | +11% |  |  | 8-K 2026-11-19T12:03 2.02,7.01,9.01 (news) |
| 2026-11-17 00:31 | VOO | candidate | other | not pump |  | -0% |  |  |  |
| 2026-11-16 22:11 | RCAT | candidate | other | real news |  | +0% |  |  | 8-K 2026-11-16T21:06 2.02,9.01 (news) |
| 2026-11-16 20:09 | LXEO | candidate | other | real news |  | +32% |  |  | 8-K 2026-11-16T12:02 2.02,7.01,8.01,9.01 (news) |
| 2026-11-16 16:34 | ANT | candidate | unknown | unknown (no price at the flag) |  |  |  |  |  |
| 2026-11-16 07:17 | WMT | candidate | other | real news |  | +2% |  |  | 8-K 2026-11-16T12:58 5.02,9.01; 8-K 2026-11-19T11:58 2.02,9.01 (news) |
| 2026-11-14 02:06 | WMT | candidate | other | real news |  | +2% |  |  | 8-K 2026-11-16T12:58 5.02,9.01; 8-K 2026-11-19T11:58 2.02,9.01 (news) |
| 2026-11-14 00:36 | DHS | candidate | other | not pump |  | +0% |  |  |  |
| 2026-11-13 22:10 | ATC | candidate | other | not pump |  | -7% |  |  |  |
| 2026-11-13 19:02 | IWM | candidate | other | not pump | no | +1% |  | -7% |  |
| 2026-11-13 19:02 | VSEC | control | other | not pump | no | +3% |  | -6% |  |
| 2026-11-13 19:02 | BURL | control | other | not pump | no | +4% |  | -3% |  |
| 2026-11-13 16:24 | XLAB | candidate | other | not pump | no | +49% |  | -36% |  |
| 2026-11-13 16:24 | ROLR | control | low float runner | real news | no | +8% |  | -31% | 8-K 2026-11-13T21:10 2.02,9.01 (news) |
| 2026-11-13 16:24 | KLXE | control | other | real news | no | +13% |  | -21% | 8-K 2026-11-10T21:12 2.02,7.01,9.01 (news) |
| 2026-11-13 15:04 | TSLA | candidate | other | not pump | no | +3% |  | -12% |  |
| 2026-11-13 15:04 | VRSN | control | other | not pump | no | +1% |  | -3% |  |
| 2026-11-13 15:04 | RMD | control | other | not pump | no | +2% |  | -2% |  |
| 2026-11-13 14:07 | SMU | candidate | other | not pump | yes | -1% |  | -58% |  |
| 2026-11-13 14:07 | WIA | control | other | not pump | no | -0% |  | -2% |  |
| 2026-11-13 14:07 | MFIC | control | other | not pump | no | +1% |  | -3% |  |
| 2026-11-13 13:30 | AIMD | candidate | other | real news | no | +60% |  | +3% | 8-K 2026-11-16T13:41 2.02,9.01 (news); 8-K 2026-11-17T13:30 1.01,7.01,9.01 (news) |
| 2026-11-13 13:30 | LGPS | control | other | not pump | no | +6% |  | -8% |  |
| 2026-11-13 13:30 | ACXP | control | low float runner | not pump | no | +3% |  | -13% | 8-K 2026-11-13T21:30 5.02 |
| 2026-11-13 13:15 | ARM | candidate | other | not pump | no | -0% |  | -24% |  |
| 2026-11-13 13:15 | CB | control | other | not pump | no | +3% |  | -1% |  |
| 2026-11-13 13:15 | BKNG | control | other | not pump | no | +1% |  | -10% | 8-K 2026-11-13T22:12 1.01,2.03,8.01,9.01 |
| 2026-11-13 10:58 | CRWD | candidate | other | not pump | no | +9% |  | -11% |  |
| 2026-11-13 10:58 | TD | control | other | not pump | no | +0% |  | -9% |  |
| 2026-11-13 10:58 | SCCO | control | other | not pump | no | +0% |  | -20% |  |

1327 older rows are in `labels/labels.csv`.
