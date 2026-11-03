# Stage 2 market snapshots

Updated 2026-11-03T17:35:37Z. Each Stage 1 candidate's market data as of the moment it was flagged (price, volume vs
its 20-day average, float, short interest, SEC dilution filings), plus two matched controls nobody was talking
about. Full rows: `snapshots.csv`; definitions: docs/stage2.md on `main`. Statistical context, not advice.

331 candidates and 659 controls so far. Archetypes: other 318, low_float_runner 11, otc_penny 1, unknown 1.

| Ticker | Flagged (UTC) | Archetype | Venue | Price | Since close | 5 days | Rel. volume | Float | Short % float | Dilution filings 90d | Problems |
|---|---|---|---|---|---|---|---|---|---|---|---|
| TSM | 2026-11-03 17:35 | other | listed | 405.1 | +1.6% | -6.1% | 1.1x | 37.84B | 0.1% | 0 |  |
| AEHR | 2026-11-03 15:08 | other | listed | 62.42 | +21.3% | -9.1% | 1.6x | 31.2M | 18.0% | 0 |  |
| OKLO | 2026-11-03 14:58 | other | listed | 24.05 | +2.3% | -9.3% | 0.9x | 157.4M | 22.8% | 1 |  |
| IREN | 2026-11-03 08:03 | other | listed | 22.42 | +1.8% | -13.4% | 0.9x | 385.8M | 24.5% | 0 |  |
| APLD | 2026-11-03 07:23 | other | listed | 16.41 | +1.2% | -9.0% | 0.8x | 261.2M | 25.1% | 0 |  |
| AAOI | 2026-11-03 00:57 | other | listed | 63.56 | +1.7% | -13.1% | 1.2x | 80.8M | 20.2% | 1 |  |
| AMD | 2026-11-02 21:58 | other | listed | 469.1 | +0.5% | -12.1% | 1.5x | 1.62B | 2.3% | 3 |  |
| ASTS | 2026-11-02 21:45 | other | listed | 36.86 | +1.5% | -7.9% | 1.0x | 266.5M | 24.7% | 0 |  |
| HTZ | 2026-11-02 21:29 | other | listed | 1.959 | +0.5% | +0.5% | 0.7x | 170.6M | 74.2% | 0 |  |
| LITE | 2026-11-02 21:16 | other | listed | 690.2 | +0.8% | -16.3% | 2.9x | 89.2M | 8.7% | 0 |  |
| MRVL | 2026-11-02 21:05 | other | listed | 172.3 | +0.5% | -26.7% | 2.6x | 873.8M | 2.8% | 0 |  |
| WMT | 2026-11-02 20:10 | other | listed | 127.3 | +3.1% | +3.0% | 1.5x | 4.85B | 1.6% | 4 |  |
| AAPL | 2026-11-02 20:10 | other | listed | 339 | -1.6% | -0.9% | 1.8x | 14.57B | 0.9% | 0 |  |
| MU | 2026-11-02 19:43 | other | listed | 837.1 | -5.4% | +0.8% | 1.2x | 1.13B | 2.0% | 0 |  |
| SMCI | 2026-11-02 18:46 | other | listed | 31.17 | -5.4% | +0.0% | 1.1x | 557.7M | 14.4% | 0 |  |
| SOUN | 2026-11-02 17:39 | other | listed | 4.285 | +1.5% | -4.7% | 1.1x | 401.1M | 42.6% | 1 |  |
| RKLB | 2026-11-02 15:08 | other | listed | 54.11 | -1.1% | +4.0% | 0.8x | 556.9M | 8.1% | 2 |  |
| PLTR | 2026-11-02 13:09 | other | listed | 186.4 | +1.2% | -6.4% | 1.2x | 2.11B | 2.7% | 0 |  |
| ATC | 2026-11-02 07:17 | other | listed | 21.59 | -0.0% | -7.6% | 0.2x |  |  |  |  |
| NNN | 2026-11-01 19:38 | other | listed | 41 | +0.0% | -1.7% | 1.1x | 179.7M | 3.9% | 2 |  |
| MSOS | 2026-10-31 21:03 | other | listed | 3.95 | +0.3% | +0.8% | 1.3x |  |  |  |  |
| INO | 2026-10-31 02:57 | other | listed | 2.06 | +243.3% | -33.3% | 15.5x | 95.8M | 22.2% | 0 |  |
| GLD | 2026-10-31 00:58 | other | listed | 356.1 | -3.4% | -0.1% | 1.2x |  |  | 0 |  |
| AAOI | 2026-10-31 00:51 | other | listed | 69.39 | -12.4% | +16.3% | 0.8x | 80.8M | 20.2% | 1 |  |
| QCOM | 2026-10-31 00:21 | other | listed | 165.3 | -10.8% | +7.3% | 0.8x | 1.05B | 2.8% | 1 |  |
| TLT | 2026-10-30 22:07 | other | listed | 81.67 | -0.2% | +0.6% | 1.0x |  |  |  |  |
| SOXL | 2026-10-30 19:57 | other | listed | 71.7 | -30.0% | +24.7% | 1.1x |  |  |  |  |
| SOXX | 2026-10-30 19:04 | other | listed | 461.9 | -10.1% | +8.0% | 0.7x |  |  |  |  |
| TQQQ | 2026-10-30 18:26 | other | listed | 60.62 | -12.5% | +4.3% | 1.2x |  |  |  |  |
| INTL | 2026-10-30 17:43 | other | listed | 29.19 | -2.0% | +1.4% | 2.6x |  |  |  |  |
