# Stage 2 market snapshots

Updated 2026-10-09T12:53:17Z. Each Stage 1 candidate's market data as of the moment it was flagged (price, volume vs
its 20-day average, float, short interest, SEC dilution filings), plus two matched controls nobody was talking
about. Full rows: `snapshots.csv`; definitions: docs/stage2.md on `main`. Statistical context, not advice.

70 candidates and 140 controls so far. Archetypes: other 67, low_float_runner 3.

| Ticker | Flagged (UTC) | Archetype | Venue | Price | Since close | 5 days | Rel. volume | Float | Short % float | Dilution filings 90d | Problems |
|---|---|---|---|---|---|---|---|---|---|---|---|
| DAL | 2026-10-09 12:52 | other | listed | 80.14 | -2.4% | -2.4% | 1.2x | 649.7M | 4.0% | 0 |  |
| TSM | 2026-10-09 12:39 | other | listed | 465.4 | +1.6% | -0.3% | 1.4x | 37.84B | 0.1% | 0 |  |
| HUM | 2026-10-09 12:39 | other | listed | 449 | +16.0% | +2.0% | 2.2x | 119.8M | 2.4% | 0 |  |
| ONDS | 2026-10-09 01:49 | other | listed | 6.874 | +0.4% | -3.8% | 1.0x | 533.4M | 44.5% | 5 |  |
| IBM | 2026-10-09 01:09 | other | listed | 225.5 | +2.3% | +0.3% | 0.6x | 940.2M | 2.4% | 2 |  |
| SOXL | 2026-10-09 00:30 | other | listed | 142.2 | -10.5% | +7.5% | 0.9x |  |  |  |  |
| MCD | 2026-10-09 00:16 | other | listed | 236.9 | +2.6% | -0.0% | 0.7x | 706.6M | 1.7% | 0 |  |
| CIFR | 2026-10-08 21:37 | other | listed | 13.55 | +0.4% | -12.7% | 1.7x | 344.1M | 21.2% | 0 |  |
| ASTS | 2026-10-08 21:11 | other | listed | 55.4 | -2.7% | -0.2% | 1.7x | 266.5M | 24.5% | 0 |  |
| AAOI | 2026-10-08 20:17 | other | listed | 106.8 | +0.8% | -1.3% | 2.4x | 80.6M | 15.3% | 1 |  |
| CMG | 2026-10-08 19:38 | other | listed | 32.94 | +7.0% | -3.7% | 0.8x | 1.26B | 3.2% | 0 |  |
| SBUX | 2026-10-08 18:59 | other | listed | 91.15 | -2.6% | -0.4% | 1.3x | 1.14B | 3.5% | 0 |  |
| USO | 2026-10-08 18:20 | other | listed | 149.1 | +3.6% | -1.2% | 0.5x |  |  | 0 |  |
| NBIS | 2026-10-08 18:05 | other | listed | 220.5 | -7.0% | +0.5% | 1.2x | 228.7M | 20.5% | 0 |  |
| DELL | 2026-10-08 17:52 | other | listed | 570.8 | -1.4% | +7.6% | 0.5x | 292.2M | 4.7% | 2 |  |
| ORCL | 2026-10-08 17:11 | other | listed | 136.4 | -5.0% | +4.6% | 0.4x | 1.86B | 2.7% | 0 |  |
| GME | 2026-10-08 16:17 | other | listed | 25.47 | +3.6% | -0.3% | 0.7x | 461.2M | 8.5% | 0 |  |
| BWET | 2026-10-08 15:51 | other | listed | 1,027 | +7.0% | +19.6% | 0.4x |  |  | 0 |  |
| META | 2026-10-08 13:39 | other | listed | 722.6 | +0.2% | -0.5% | 0.6x | 2.20B | 1.4% | 0 |  |
| TTWO | 2026-10-08 13:27 | other | listed | 204.2 | +0.1% | -1.7% | 0.9x | 186.1M | 4.4% | 0 |  |
| PLTR | 2026-10-08 13:12 | other | listed | 199.2 | +2.6% | +3.8% | 0.7x | 2.11B | 2.9% | 0 |  |
| ADBE | 2026-10-08 04:07 | other | listed | 232.5 | -0.1% | -3.0% | 1.2x | 388.1M | 4.8% | 0 |  |
| KEEL | 2026-10-08 03:01 | other | listed | 3.34 | +0.3% | -5.7% | 1.0x | 589.8M | 18.6% | 0 |  |
| UUUU | 2026-10-07 20:50 | other | listed | 10.26 | +0.0% | -7.0% | 1.8x | 248.2M | 22.4% | 0 |  |
| SMCI | 2026-10-07 20:50 | other | listed | 45 | +0.1% | +9.4% | 1.1x | 557.6M | 17.1% | 0 |  |
| LEVI | 2026-10-07 20:37 | other | listed | 19.16 | -1.8% | -1.0% | 5.8x | 93.0M | 8.7% | 0 |  |
| IREN | 2026-10-07 19:18 | other | listed | 38.77 | -6.1% | -0.2% | 1.0x | 346.2M | 24.0% | 1 |  |
| LLY | 2026-10-07 17:44 | other | listed | 1,196 | +3.4% | -2.3% | 0.9x | 889.0M | 0.8% | 0 |  |
| BIYA | 2026-10-07 16:38 | low float runner | listed | 2.11 | +54.6% | -33.4% | 12.7x | 3.0M | 2.1% | 2 |  |
| GLD | 2026-10-07 13:01 | other | listed | 374.7 | -2.0% | -0.2% | 0.9x |  |  | 0 |  |
