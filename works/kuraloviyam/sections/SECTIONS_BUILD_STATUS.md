# Kuraloviyam Derived Sections — Build Status

## S1 — Structural scaffold COMPLETE / PASS

- base maintained-work closure — `2069436456f9501cc5ade59fade19c4df51aaf14`;
- S1 section-layer commit — `b29cb2e5d25904250ca69ad2c0bc085666685b01`;
- derived files created — **156**;
- audited Tamil page changes — **0**;
- maintained English page changes — **0**.

## S2 — Entry-to-Adhikaram crosswalk COMPLETE / PASS WITH TWO SOURCE-METADATA LIMITATIONS

S2 processed the exact source contents entries **1–300**.

Final disposition:

- entries processed — **300/300**;
- fully resolved — **298**;
- partial source metadata — **2**: entries **46, 104**;
- unresolved — **0**;
- source-evidenced Chapter numbers — **121/133**;
- Chapter numbers not evidenced by the 300 entry closures — **1, 18, 22, 25, 44, 52, 70, 76, 86, 91, 106, 107**.

### Source-metadata limitations

- entry **46**: the first quoted Kural `என்பு இலதனை...` is present, but its Chapter/Kural number is not explicitly supplied in the audited page record; the second quotation closes with Chapter 83 / Kural 828.
- entry **104**: the first quoted Kural `உழுதுண்டு வாழ்வாரே...` is present, but its Chapter/Kural number is not explicitly supplied in the audited page record; the second quotation closes with Chapter 28 / Kural 273.

No external numbering was inferred.

### Shared-page correction

Entry **202** continues through printed page **435 / scan 452**, which is also the locator page for entry 203. S2 therefore preserves an overlapping entry span where the audited source proves it.

### Durable outputs

- `crosswalk/S2_MASTER_CROSSWALK.tsv`;
- `crosswalk/S2_EXCEPTION_AUDIT.md`;
- 121 source-evidenced Adhikaram files populated with linked contents entries;
- refreshed Iyal indexes;
- `ADHIKARAM_COVERAGE.md`.

## Result

The requested hierarchy is now operational:

**Book → Iyal → Adhikaram → Kuraloviyam contents entry**

with **0 mutations** to the closed Tamil or English page layers.

## Next optional downstream activity

**S3 — individual entry leaf records / web-ready navigation index**, if required.

S3 is optional; S2 already completes the requested section hierarchy.
