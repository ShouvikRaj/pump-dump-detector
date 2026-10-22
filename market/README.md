# Stage 2 market snapshots

Updated 2026-10-22T14:13:06Z. Each Stage 1 candidate's market data as of the moment it was flagged (price, volume vs
its 20-day average, float, short interest, SEC dilution filings), plus two matched controls nobody was talking
about. Full rows: `snapshots.csv`; definitions: docs/stage2.md on `main`. Statistical context, not advice.

178 candidates and 355 controls so far. Archetypes: other 169, low_float_runner 9.

| Ticker | Flagged (UTC) | Archetype | Venue | Price | Since close | 5 days | Rel. volume | Float | Short % float | Dilution filings 90d | Problems |
|---|---|---|---|---|---|---|---|---|---|---|---|
| IWM | 2026-10-22 14:12 | other | listed | 276.2 | -0.1% | +1.9% | 0.6x |  |  |  |  |
| HTZ | 2026-10-22 14:12 | other | listed | 2.375 | +14.7% | +11.9% | 1.1x | 170.6M | 72.3% | 0 |  |
| AVGO | 2026-10-22 14:12 | other | listed | 329.2 | -2.5% | -2.4% | 0.8x | 4.72B | 1.1% | 1 |  |
| AVEX | 2026-10-22 11:25 | other | listed | 10.6 | +9.5% | -31.7% | 7.3x | 19.9M | 18.1% | 0 |  |
| TSLA | 2026-10-22 07:27 | other | listed | 373.6 | -3.3% | +5.3% | 1.4x | 2.82B | 2.5% | 0 |  |
| SDEV | 2026-10-22 07:27 | other | listed | 1.21 | +10.0% | +11.1% | 3.1x | 49.3M | 7.0% | 3 |  |
| NOK | 2026-10-22 05:55 | other | listed | 9.22 | -0.3% | -1.6% | 1.1x | 4.45B | 1.9% | 0 |  |
| BABA | 2026-10-22 02:50 | other | listed | 104 | -0.4% | -6.1% | 1.5x | 2.22B | 1.7% | 0 |  |
| RDDT | 2026-10-21 22:45 | other | listed | 153.5 | +0.1% | +3.1% | 0.8x | 140.7M | 15.7% | 0 |  |
| MSTR | 2026-10-21 19:47 | other | listed | 153.1 | +7.3% | -6.2% | 1.0x | 363.6M | 8.1% | 0 |  |
| IBM | 2026-10-21 18:15 | other | listed | 245.6 | +1.5% | +4.8% | 1.1x | 940.2M | 2.6% | 2 |  |
| AMOD | 2026-10-21 16:41 | low float runner | listed | 1.91 | +48.1% | -21.3% | 0.0x | 1.1M | 3.6% | 4 |  |
| META | 2026-10-21 11:34 | other | listed | 690.9 | -0.5% | -9.0% | 0.8x | 2.20B | 1.5% | 0 |  |
| SLS | 2026-10-21 08:01 | other | listed | 11.97 | -0.1% | -3.5% | 1.9x | 201.1M | 27.4% | 0 |  |
| PAC | 2026-10-21 02:19 | other | listed | 217.4 | +0.0% | +9.3% | 1.0x | 5.51B | 0.0% | 0 |  |
| MRNA | 2026-10-20 23:18 | other | listed | 241.5 | -0.2% | +11.9% | 0.9x | 372.0M | 8.3% | 0 |  |
| OKLO | 2026-10-20 21:21 | other | listed | 27.92 | +1.6% | -13.5% | 0.8x | 157.4M | 20.8% | 1 |  |
| SMCI | 2026-10-20 21:06 | other | listed | 36.6 | +12.7% | -16.9% | 1.1x | 557.7M | 15.7% | 0 |  |
| GOOGL | 2026-10-20 18:16 | other | listed | 340.8 | -1.0% | -2.4% | 0.8x | 10.88B | 0.7% | 3 |  |
| LRCX | 2026-10-20 16:42 | other | listed | 264.7 | -2.8% | -12.1% | 1.2x | 1.25B | 2.1% | 0 |  |
| IWM | 2026-10-20 16:03 | other | listed | 275.8 | +1.7% | -2.4% | 0.7x |  |  |  |  |
| CRWV | 2026-10-20 14:57 | other | listed | 63.86 | +4.5% | -23.8% | 2.5x | 328.3M | 18.3% | 1 |  |
| HTZ | 2026-10-20 13:24 | other | listed | 2.108 | +14.6% | -0.5% | 0.8x | 170.6M | 72.3% | 0 |  |
| SPCX | 2026-10-20 10:18 | other | listed | 146.8 | -0.8% | -9.5% | 0.9x | 4.97B | 3.6% | 0 |  |
| APLD | 2026-10-20 04:07 | other | listed | 19.34 | +0.5% | -17.2% | 1.5x | 261.4M | 21.7% | 0 |  |
| GOOG | 2026-10-19 22:36 | other | listed | 340.1 | -0.0% | -2.5% | 0.7x | 10.88B | 0.5% | 3 |  |
| NFLX | 2026-10-19 19:31 | other | listed | 69.83 | -1.0% | +0.3% | 1.1x | 4.13B | 2.0% | 1 |  |
| RIVN | 2026-10-19 18:51 | other | listed | 12.29 | -1.1% | -11.0% | 1.0x | 945.4M | 17.9% | 0 |  |
| TQQQ | 2026-10-19 16:13 | other | listed | 71.72 | +5.1% | -16.1% | 1.7x |  |  |  |  |
| GLD | 2026-10-19 16:13 | other | listed | 379.6 | -0.6% | -0.7% | 1.2x |  |  | 0 |  |
