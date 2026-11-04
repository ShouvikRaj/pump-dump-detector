# Stage 2 market snapshots

Updated 2026-11-04T18:32:52Z. Each Stage 1 candidate's market data as of the moment it was flagged (price, volume vs
its 20-day average, float, short interest, SEC dilution filings), plus two matched controls nobody was talking
about. Full rows: `snapshots.csv`; definitions: docs/stage2.md on `main`. Statistical context, not advice.

354 candidates and 705 controls so far. Archetypes: other 340, low_float_runner 12, otc_penny 1, unknown 1.

| Ticker | Flagged (UTC) | Archetype | Venue | Price | Since close | 5 days | Rel. volume | Float | Short % float | Dilution filings 90d | Problems |
|---|---|---|---|---|---|---|---|---|---|---|---|
| USO | 2026-11-04 18:32 | other | listed | 145.7 | -7.9% | -3.5% | 0.9x |  |  | 0 |  |
| NBIS | 2026-11-04 18:32 | other | listed | 141.4 | -6.8% | -11.0% | 0.7x | 228.7M | 20.8% | 0 |  |
| QCOM | 2026-11-04 18:08 | other | listed | 168.4 | +2.4% | -10.7% | 1.1x | 1.05B | 2.8% | 1 |  |
| IREN | 2026-11-04 18:08 | other | listed | 21.94 | -10.3% | -10.9% | 1.0x | 385.8M | 24.5% | 0 |  |
| CRWV | 2026-11-04 18:08 | other | listed | 48.82 | -9.2% | -9.8% | 0.6x | 328.3M | 21.3% | 1 |  |
| VST | 2026-11-04 15:47 | other | listed | 119.3 | -14.6% | -4.8% | 0.8x | 313.0M | 3.2% | 3 |  |
| DUOL | 2026-11-04 15:47 | other | listed | 167.7 | +31.0% | -9.4% | 2.9x | 40.0M | 17.8% | 0 |  |
| UBER | 2026-11-04 15:35 | other | listed | 71.52 | +7.4% | +1.2% | 1.3x | 2.04B | 2.4% | 2 |  |
| DJT | 2026-11-04 14:40 | other | listed | 5.3 | -10.9% | -6.4% | 0.9x | 160.9M | 10.9% | 0 |  |
| TSLA | 2026-11-04 14:27 | other | listed | 380 | -4.6% | -2.2% | 0.7x | 2.82B | 2.5% | 0 |  |
| TLT | 2026-11-04 13:44 | other | listed | 81.39 | +0.3% | -0.6% | 0.8x |  |  |  |  |
| PARA | 2026-11-04 13:44 | low float runner | listed | 1.17 | -57.0% | +540.0% | 146.8x | 0.3M | 76.2% | 4 |  |
| MRNA | 2026-11-04 13:20 | other | listed | 234.8 | +2.8% | +9.8% | 0.5x | 372.0M | 8.8% | 0 |  |
| DXYZ | 2026-11-04 12:50 | other | listed | 26.61 | -0.2% | -5.2% | 0.7x |  |  | 2 |  |
| FSLR | 2026-11-04 07:16 | other | listed | 191 | +2.7% | +5.7% | 1.6x | 101.7M | 11.4% | 0 |  |
| SPCX | 2026-11-04 05:49 | other | listed | 138.8 | -1.7% | -4.9% | 0.7x | 3.05B | 5.5% | 0 |  |
| SGOV | 2026-11-04 01:25 | other | listed | 100.4 | +0.0% | -0.2% | 1.8x |  |  |  |  |
| NVTS | 2026-11-03 23:11 | other | listed | 9.14 | +6.8% | -8.4% | 1.3x | 242.9M | 21.0% | 0 |  |
| DAMD | 2026-11-03 22:03 | other | listed | 10.54 | -15.9% | +26.4% | 2.8x |  |  |  |  |
| ANET | 2026-11-03 21:29 | other | listed | 182.9 | +7.6% | -9.1% | 1.8x | 1.05B | 1.2% | 0 |  |
| AMC | 2026-11-03 21:29 | other | listed | 3.28 | +0.0% | +9.7% | 1.4x | 835.3M | 5.7% | 0 |  |
| ALAB | 2026-11-03 21:29 | other | listed | 231.6 | -0.9% | -18.5% | 1.2x | 156.0M | 5.1% | 0 |  |
| DDOG | 2026-11-03 18:57 | other | listed | 219.5 | +1.6% | -22.9% | 1.6x | 333.0M | 3.0% | 0 |  |
| TSM | 2026-11-03 17:35 | other | listed | 405.1 | +1.6% | -6.1% | 1.1x | 37.84B | 0.1% | 0 |  |
| AEHR | 2026-11-03 15:08 | other | listed | 62.42 | +21.3% | -9.1% | 1.6x | 31.2M | 18.0% | 0 |  |
| OKLO | 2026-11-03 14:58 | other | listed | 24.05 | +2.3% | -9.3% | 0.9x | 157.4M | 22.8% | 1 |  |
| IREN | 2026-11-03 08:03 | other | listed | 22.42 | +1.8% | -13.4% | 0.9x | 385.8M | 24.5% | 0 |  |
| APLD | 2026-11-03 07:23 | other | listed | 16.41 | +1.2% | -9.0% | 0.8x | 261.2M | 25.1% | 0 |  |
| AAOI | 2026-11-03 00:57 | other | listed | 63.56 | +1.7% | -13.1% | 1.2x | 80.8M | 20.2% | 1 |  |
| AMD | 2026-11-02 21:58 | other | listed | 469.1 | +0.5% | -12.1% | 1.5x | 1.62B | 2.3% | 3 |  |
