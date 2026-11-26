# Stage 2 market snapshots

Updated 2026-11-26T00:55:00Z. Each Stage 1 candidate's market data as of the moment it was flagged (price, volume vs
its 20-day average, float, short interest, SEC dilution filings), plus two matched controls nobody was talking
about. Full rows: `snapshots.csv`; definitions: docs/stage2.md on `main`. Statistical context, not advice.

525 candidates and 1039 controls so far. Archetypes: other 501, low_float_runner 18, unknown 5, otc_penny 1.

| Ticker | Flagged (UTC) | Archetype | Venue | Price | Since close | 5 days | Rel. volume | Float | Short % float | Dilution filings 90d | Problems |
|---|---|---|---|---|---|---|---|---|---|---|---|
| VTI | 2026-11-26 00:54 | other | listed | 355.2 | +0.6% | -1.7% | 1.3x |  |  |  |  |
| META | 2026-11-26 00:54 | other | listed | 612.5 | +0.4% | -1.1% | 1.0x | 2.21B | 2.7% | 9 |  |
| AAPL | 2026-11-26 00:54 | other | listed | 355.3 | -0.1% | +0.9% | 1.0x | 14.51B | 1.0% | 2 |  |
| SOXS | 2026-11-26 00:44 | other | listed | 59.32 | -4.5% | +6.4% | 1.4x |  |  |  |  |
| SOXL | 2026-11-26 00:44 | other | listed | 33.45 | +4.5% | -35.0% | 2.0x |  |  |  |  |
| NRSN | 2026-11-26 00:44 | low float runner | listed | 1.83 | +4.0% | +28.5% | 1883.0x | 1.2M | 2.5% | 0 |  |
| SGOV | 2026-11-25 21:55 | other | listed | 100.7 | +0.0% | +0.1% | 1.1x |  |  |  |  |
| BENF | 2026-11-25 00:43 | other | listed | 0.805 | -12.0% | +63.1% | 1818.5x | 3.9M | 6.6% | 0 |  |
| DELL | 2026-11-24 21:15 | other | listed | 289.4 | -2.0% | -8.5% | 2.0x | 292.2M | 3.6% | 2 |  |
| SOAR | 2026-11-24 00:45 | other | listed | 0.1985 | -0.6% | +16.7% | 66.2x | 38.4M | 6.7% | 0 |  |
| NYT | 2026-11-24 00:45 | other | listed | 68.32 | +0.0% | -7.0% | 0.7x | 132.0M | 14.1% | 0 |  |
| MSS | 2026-11-24 00:45 | low float runner | listed | 1.32 | +10.0% | +53.3% | 2.1x | 0.4M | 14.7% | 0 |  |
| IVVD | 2026-11-24 00:45 | other | listed | 0.4911 | +1.2% | -9.8% | 16.6x | 221.7M | 16.3% | 0 |  |
| HPE | 2026-11-24 00:45 | other | listed | 44.66 | -7.0% | +3.1% | 3.0x | 1.32B | 3.5% | 0 |  |
| DJT | 2026-11-24 00:45 | other | listed | 3.96 | +1.9% | -4.8% | 0.6x | 161.3M | 12.2% | 1 |  |
| SMCI | 2026-11-23 00:51 | other | listed | 22.16 | +2.4% | -19.4% | 1.1x | 560.0M | 13.4% | 0 |  |
| NYT | 2026-11-22 00:48 | other | listed | 68.62 | +0.0% | -5.8% | 1.0x | 132.0M | 14.1% | 0 |  |
| MSTR | 2026-11-22 00:48 | other | listed | 79.5 | +2.2% | -30.3% | 2.0x | 401.8M | 6.7% | 5 |  |
| ASML | 2026-11-21 03:02 | other | listed | 1,292 | +2.0% | -15.3% | 1.9x | 21.28B | 0.0% | 0 |  |
| VOO | 2026-11-21 00:55 | other | listed | 641.2 | +0.9% | -8.3% | 4.0x |  |  |  |  |
| CRWD | 2026-11-21 00:55 | other | listed | 217.8 | -5.1% | +1.2% | 1.4x | 1.01B | 2.2% | 1 |  |
| VWAV | 2026-11-21 00:46 | other | listed | 0.13 | -28.6% | -54.9% | 50.3x | 0.0M | 9966.0% | 2 |  |
| SNDK | 2026-11-21 00:46 | other | listed | 81.22 | +2.5% | -28.4% | 1.2x | 1.12B | 0.4% | 0 |  |
| TLT | 2026-11-20 18:35 | other | listed | 81.29 | +1.2% | +0.8% | 1.1x |  |  |  |  |
| ORCL | 2026-11-20 17:56 | other | listed | 102.4 | -7.4% | -13.0% | 0.7x | 1.89B | 2.4% | 5 |  |
| SGOV | 2026-11-20 14:10 | other | listed | 100.6 | +0.0% | +0.1% | 1.2x |  |  |  |  |
| AMD | 2026-11-20 14:10 | other | listed | 467.5 | -4.4% | -16.4% | 1.9x | 1.63B | 2.4% | 0 |  |
| ROPE | 2026-11-20 03:06 | other | listed | 30.1 | +0.0% | -3.9% | 1.4x |  |  |  |  |
| INTU | 2026-11-20 03:06 | other | listed | 279.7 | -9.8% | -8.9% | 1.6x | 260.9M | 3.4% | 1 |  |
| OPEX | 2026-11-20 00:51 | other | listed | 1.21 | +10.0% | +25.0% | 3.1x |  |  |  |  |
