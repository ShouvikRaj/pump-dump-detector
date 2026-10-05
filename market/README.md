# Stage 2 market snapshots

Updated 2026-10-05T16:39:15Z. Each Stage 1 candidate's market data as of the moment it was flagged (price, volume vs
its 20-day average, float, short interest, SEC dilution filings), plus two matched controls nobody was talking
about. Full rows: `snapshots.csv`; definitions: docs/stage2.md on `main`. Statistical context, not advice.

10 candidates and 20 controls so far. Archetypes: other 8, low_float_runner 2.

| Ticker | Flagged (UTC) | Archetype | Venue | Price | Since close | 5 days | Rel. volume | Float | Short % float | Dilution filings 90d | Problems |
|---|---|---|---|---|---|---|---|---|---|---|---|
| DELL | 2026-10-05 16:38 | other | listed | 554.8 | -1.4% | -0.1% | 0.6x | 292.2M | 4.7% | 2 |  |
| GME | 2026-10-05 16:24 | other | listed | 25.55 | +3.4% | +5.6% | 1.3x | 461.2M | 8.5% | 0 |  |
| VEEA | 2026-10-05 15:33 | low float runner | listed | 5.06 | +52.0% | +8.1% | 0.1x | 1.5M | 80.0% | 1 |  |
| TSM | 2026-10-05 15:18 | other | listed | 483.2 | +2.2% | +4.9% | 1.0x | 37.84B | 0.1% | 0 |  |
| SPCX | 2026-10-05 14:51 | other | listed | 166.9 | +5.0% | +6.9% | 1.3x | 4.34B | 3.7% | 0 |  |
| APLD | 2026-10-05 14:23 | other | listed | 24.68 | -2.8% | -3.3% | 1.7x | 250.7M | 23.1% | 0 |  |
| SDEV | 2026-10-05 14:09 | other | listed | 6.85 | -8.4% | +402.0% | 8.0x | 22.6M | 5.4% | 2 |  |
| PMI | 2026-10-05 13:55 | low float runner | listed | 6.16 | +6.6% | +25.1% | 4.2x | 1.3M | 18.1% | 0 |  |
| VST | 2026-10-05 04:15 | other | listed | 144 | +2.8% | +1.1% | 2.6x | 312.9M | 3.1% | 3 |  |
| DRTS | 2026-10-04 23:23 | other | listed | 14.51 | -1.7% | +1.6% | 0.6x | 64.1M | 5.4% | 0 |  |
