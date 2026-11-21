# Stage 2 market snapshots

Updated 2026-11-21T00:47:22Z. Each Stage 1 candidate's market data as of the moment it was flagged (price, volume vs
its 20-day average, float, short interest, SEC dilution filings), plus two matched controls nobody was talking
about. Full rows: `snapshots.csv`; definitions: docs/stage2.md on `main`. Statistical context, not advice.

504 candidates and 997 controls so far. Archetypes: other 482, low_float_runner 16, unknown 5, otc_penny 1.

| Ticker | Flagged (UTC) | Archetype | Venue | Price | Since close | 5 days | Rel. volume | Float | Short % float | Dilution filings 90d | Problems |
|---|---|---|---|---|---|---|---|---|---|---|---|
| VWAV | 2026-11-21 00:46 | other | listed | 0.13 | -28.6% | -54.9% | 50.3x | 0.0M | 9966.0% | 2 |  |
| SNDK | 2026-11-21 00:46 | other | listed | 81.22 | +2.5% | -28.4% | 1.2x | 1.12B | 0.4% | 0 |  |
| TLT | 2026-11-20 18:35 | other | listed | 81.29 | +1.2% | +0.8% | 1.1x |  |  |  |  |
| ORCL | 2026-11-20 17:56 | other | listed | 102.4 | -7.4% | -13.0% | 0.7x | 1.89B | 2.4% | 5 |  |
| SGOV | 2026-11-20 14:10 | other | listed | 100.6 | +0.0% | +0.1% | 1.2x |  |  |  |  |
| AMD | 2026-11-20 14:10 | other | listed | 467.5 | -4.4% | -16.4% | 1.9x | 1.63B | 2.4% | 0 |  |
| ROPE | 2026-11-20 03:06 | other | listed | 30.1 | +0.0% | -3.9% | 1.4x |  |  |  |  |
| INTU | 2026-11-20 03:06 | other | listed | 279.7 | -9.8% | -8.9% | 1.6x | 260.9M | 3.4% | 1 |  |
| OPEX | 2026-11-20 00:51 | other | listed | 1.21 | +10.0% | +25.0% | 3.1x |  |  |  |  |
| GME | 2026-11-20 00:51 | other | listed | 27.1 | +0.6% | +5.1% | 2.8x | 460.4M | 9.2% | 0 |  |
| CRWD | 2026-11-19 03:02 | other | listed | 251.2 | +6.0% | +3.5% | 1.3x | 1.01B | 2.2% | 1 |  |
| MU | 2026-11-19 01:56 | other | listed | 718.4 | +0.8% | -1.8% | 1.1x | 1.13B | 2.1% | 0 |  |
| SPCX | 2026-11-19 00:49 | other | listed | 145 | +1.1% | +2.7% | 0.8x | 3.05B | 4.6% | 0 |  |
| LULU | 2026-11-19 00:49 | other | listed | 110.1 | -0.6% | +3.1% | 1.2x | 101.7M | 13.7% | 0 |  |
| AMZN | 2026-11-19 00:49 | other | listed | 272 | +1.6% | +0.6% | 0.8x | 9.84B | 1.0% | 2 |  |
| TTWO | 2026-11-19 00:42 | other | listed | 222.7 | +2.8% | -6.4% | 3.2x | 186.4M | 5.0% | 0 |  |
| GLD | 2026-11-19 00:42 | other | listed | 343.3 | +0.6% | -6.6% | 1.3x |  |  | 0 |  |
| ANT | 2026-11-19 00:42 | unknown | listed |  |  |  |  | 965.7M |  | 5 |  |
| PANW | 2026-11-18 21:40 | other | listed | 375.1 | +10.3% | +1.6% | 2.3x | 812.5M | 2.5% | 0 |  |
| UNH | 2026-11-18 17:15 | other | listed | 356.8 | -8.4% | -3.8% | 1.6x | 893.4M | 1.6% | 0 |  |
| AAOI | 2026-11-17 23:46 | other | listed | 41.72 | -7.7% | -6.4% | 1.2x | 86.8M | 20.8% | 2 |  |
| HSBC | 2026-11-17 21:20 | other | listed | 87.28 | +0.0% | -2.9% | 0.9x | 13.55B | 0.0% | 6 |  |
| SOXX | 2026-11-17 18:16 | other | listed | 139.3 | -1.4% | -3.8% | 0.9x |  |  |  |  |
| SPCX | 2026-11-17 16:08 | other | listed | 140.6 | +2.3% | -3.3% | 0.9x | 3.05B | 4.6% | 0 |  |
| SPAI | 2026-11-17 14:06 | low float runner | listed | 2.99 | +21.1% | -24.7% | 24.0x | 11.6M | 5.4% | 0 |  |
| SLS | 2026-11-17 12:33 | other | listed | 8 | +7.1% | -12.9% | 1.0x | 203.1M | 28.1% | 0 |  |
| SHAZ | 2026-11-17 10:45 | other | listed | 19.41 | -3.6% | -15.9% | 2.2x | 19.4M | 23.2% | 10 |  |
| SNDK | 2026-11-17 10:05 | other | listed | 795.9 | -1.6% | -8.7% | 1.0x | 140.4M | 3.5% | 0 |  |
| JPM | 2026-11-17 10:05 | other | listed | 336 | -0.7% | -1.1% | 1.1x | 2.64B | 0.9% | 5870 |  |
| ROPE | 2026-11-17 06:59 | other | listed | 31.25 | +0.0% | +0.1% | 1.0x |  |  |  |  |
