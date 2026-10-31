# Stage 2 market snapshots

Updated 2026-10-31T00:52:17Z. Each Stage 1 candidate's market data as of the moment it was flagged (price, volume vs
its 20-day average, float, short interest, SEC dilution filings), plus two matched controls nobody was talking
about. Full rows: `snapshots.csv`; definitions: docs/stage2.md on `main`. Statistical context, not advice.

308 candidates and 613 controls so far. Archetypes: other 295, low_float_runner 11, otc_penny 1, unknown 1.

| Ticker | Flagged (UTC) | Archetype | Venue | Price | Since close | 5 days | Rel. volume | Float | Short % float | Dilution filings 90d | Problems |
|---|---|---|---|---|---|---|---|---|---|---|---|
| AAOI | 2026-10-31 00:51 | other | listed | 69.39 | -12.4% | +16.3% | 0.8x | 80.8M | 20.2% | 1 |  |
| QCOM | 2026-10-31 00:21 | other | listed | 165.3 | -10.8% | +7.3% | 0.8x | 1.05B | 2.8% | 1 |  |
| TLT | 2026-10-30 22:07 | other | listed | 81.67 | -0.2% | +0.6% | 1.0x |  |  |  |  |
| SOXL | 2026-10-30 19:57 | other | listed | 71.7 | -30.0% | +24.7% | 1.1x |  |  |  |  |
| SOXX | 2026-10-30 19:04 | other | listed | 461.9 | -10.1% | +8.0% | 0.7x |  |  |  |  |
| TQQQ | 2026-10-30 18:26 | other | listed | 60.62 | -12.5% | +4.3% | 1.2x |  |  |  |  |
| INTL | 2026-10-30 17:43 | other | listed | 29.19 | -2.0% | +1.4% | 2.6x |  |  |  |  |
| SPY | 2026-10-30 17:00 | other | listed | 756.1 | -1.7% | +0.7% | 1.1x |  |  | 0 |  |
| SBUX | 2026-10-30 17:00 | other | listed | 103 | -2.4% | +3.5% | 1.2x | 1.14B | 3.8% | 0 |  |
| APP | 2026-10-30 17:00 | other | listed | 233.7 | -8.3% | -3.5% | 1.0x | 265.4M | 4.2% | 0 |  |
| WMT | 2026-10-30 16:45 | other | listed | 124 | +2.3% | +0.1% | 0.8x | 4.85B | 1.6% | 4 |  |
| RSP | 2026-10-30 16:45 | other | listed | 218.6 | -0.7% | +0.8% | 1.0x |  |  |  |  |
| SOXS | 2026-10-30 15:55 | other | listed | 52.02 | +24.8% | -22.0% | 1.0x |  |  |  |  |
| USO | 2026-10-30 15:15 | other | listed | 170.6 | +1.4% | +3.5% | 0.9x |  |  | 0 |  |
| SGOV | 2026-10-30 15:02 | other | listed | 100.7 | +0.0% | +0.1% | 1.0x |  |  |  |  |
| SQQQ | 2026-10-30 14:50 | other | listed | 40.77 | +7.8% | -4.5% | 1.0x |  |  |  |  |
| QQQ | 2026-10-30 14:19 | other | listed | 694.2 | -2.9% | +1.5% | 1.0x |  |  |  |  |
| COIN | 2026-10-30 14:07 | other | listed | 142.7 | -11.2% | -5.0% | 1.1x | 219.8M | 10.8% | 0 |  |
| TSM | 2026-10-30 13:54 | other | listed | 415.6 | -3.8% | +4.7% | 0.7x | 37.84B | 0.1% | 0 |  |
| SMCI | 2026-10-30 13:42 | other | listed | 32.76 | -4.9% | +2.1% | 0.7x | 557.7M | 14.4% | 0 |  |
| AMD | 2026-10-30 13:25 | other | listed | 512 | -9.6% | +11.5% | 0.8x | 1.62B | 2.3% | 3 |  |
| NVDA | 2026-10-30 11:53 | other | listed | 206.8 | -3.2% | +0.7% | 0.8x | 23.13B | 1.3% | 0 |  |
| ARM | 2026-10-30 11:00 | other | listed | 208.5 | -8.9% | +8.9% | 1.0x | 142.6M | 12.4% | 0 |  |
| BURU | 2026-10-30 10:30 | other | listed | 0.5403 | +45.2% | -9.3% | 192.8x | 8.4M | 18.2% | 2 |  |
| NKE | 2026-10-30 09:12 | other | listed | 38.91 | +1.3% | +0.3% | 0.5x | 1.18B | 8.8% | 0 |  |
| PLTR | 2026-10-30 08:33 | other | listed | 193.7 | -1.4% | +0.1% | 0.9x | 2.11B | 2.7% | 0 |  |
| SCHD | 2026-10-30 05:02 | other | listed | 35.83 | +0.6% | +0.6% | 1.1x |  |  |  |  |
| VOO | 2026-10-30 04:49 | other | listed | 703 | -0.6% | +0.7% | 0.9x |  |  |  |  |
| DJT | 2026-10-30 01:20 | other | listed | 5.67 | -5.0% | -10.4% | 1.8x | 160.9M | 10.9% | 0 |  |
| DELL | 2026-10-30 00:42 | other | listed | 443.2 | -10.3% | +1.6% | 0.6x | 292.1M | 4.2% | 2 |  |
