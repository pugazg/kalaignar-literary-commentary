# HANDOVER — Kalaignar Literary Commentary Archive

## Repository

`pugazg/kalaignar-literary-commentary`

## Core source rule

The supplied scans are the controlling sources. Do not silently modernize, normalize, correct, reconstruct or improve Tamil. Preserve source-specific Kural spelling, joining, spacing, punctuation, line breaks and Kalaignar commentary exactly as printed.

The English layer is a **project-created translation**, not an official/publisher English edition. It must retain Kalaignar's own language, images, emphases and interpretive direction and must not import external English Kural wording or another commentator's interpretation.

Permanent cadence:

**Tamil transcription → Tamil direct visual verification → Tamil audit / archival-ready → English draft → English source-check → English editorial review → English release report.**

# திருக்குறள் — established archival state

- Part 001 — scans 1–20: **ARCHIVAL-READY WITH ONE DOCUMENTED PARTIAL FACSIMILE**; 19 verified + scan 8 partial.
- Part 002 — scans 21–41: **ARCHIVAL-READY**, 21/21 verified.
- Part 003 — scans 42–62: **ARCHIVAL-READY**, 21/21 verified; printed pages 9–29; Kural 41–145.
- Part 004 — scans 63–84: **ARCHIVAL-READY**, 22/22 verified and audited; printed pages 30–51; Kural 146–255.

Do not redo or renumber Parts 001–004.

English project translation currently released:

- Part 001 — 19 `release-ready` + scan 8 `source-limited`;
- Part 002 — 21/21 `release-ready`;
- Part 003 — 21/21 `release-ready`.

Part 004 English is eligible because its Tamil archive is archival-ready.

# Part 005 Tamil — FULLY VERIFIED / AUDIT PENDING

Source filename:

`திருக்குறள்_கலைஞர்_உரை_part_005_pages_85-106.pdf`

Confirmed supplied source range:

- local PDF pages: **22**;
- overall scans: **85–106**;
- printed pages: **52–73**;
- Kural range: **256–365**;
- scan 85 begins with Kural **256**, directly continuing Part 004 scan 84 / Kural 255;
- scan 106 ends with Kural **365**, midway through chapter 37 `அவா அறுத்தல்`.

Current repository state for Part 005:

- page records: **22 / 22**;
- first-pass transcription: **22 / 22 complete**;
- direct visual verification: **22 / 22 complete**;
- `verified`: **22**;
- `needs-review`: **0**;
- uncreated records: **0**;
- no Part 005 audit exists yet.

Every Part 005 record now uses:

`status: "verified"`

and:

`transcription_method: "direct visual comparison with source scan"`

## Verification result

All scans **85–106** were compared directly with the supplied source images.

- scans **85–98 and 100–106** required no source-text correction;
- scan **99 / Kural 329 commentary** required one source-supported correction:
  - first pass: `பகுத்தறிவு மிகுந்த செயல்படும்`
  - controlling scan: **`பகுத்தறிவு இழந்து செயல்படும்`**

The corrected wording is now stored in `0099-aram-kollaamai-02.md`.

Chapter coverage:

- completion of `26. புலால் மறுத்தல்` — 256–260;
- `27. தவம்` — 261–270;
- `28. கூடா ஒழுக்கம்` — 271–280;
- `29. கள்ளாமை` — 281–290;
- `30. வாய்மை` — 291–300;
- `31. வெகுளாமை` — 301–310;
- `32. இன்னா செய்யாமை` — 311–320;
- `33. கொல்லாமை` — 321–330;
- `34. நிலையாமை` — 331–340;
- `35. துறவு` — 341–350;
- `36. மெய்யுணர்தல்` — 351–360;
- beginning of `37. அவா அறுத்தல்` — 361–365.

Part 005 is **fully verified but not yet archival-ready** because the separate archival audit is still pending.

# Exact next activity

Perform the **Part 005 Tamil archival audit** across all 22 verified records.

Create:

`works/thirukkural/AUDIT_PART_005.md`

Audit gates:

1. confirm exactly 22 one-to-one records for scans 85–106;
2. confirm local pages 1–22 and printed pages 52–73 without gap or duplication;
3. confirm continuous Kural numbering 256–365 with no missing or duplicate number;
4. confirm Part 004→005 continuity at Kural 255→256;
5. confirm chapter continuity from completion of `புலால் மறுத்தல்` through the supplied beginning of `அவா அறுத்தல்`;
6. confirm all 22 records have `status: "verified"` and `transcription_method: "direct visual comparison with source scan"`;
7. reconfirm the scan-99 correction `பகுத்தறிவு இழந்து செயல்படும்` against the source;
8. confirm no standard/web Kural text or unsourced normalization was substituted.

If all gates pass, mark Part 005 **ARCHIVAL-READY**, synchronize `works/thirukkural/README.md`, root `README.md`, and this handover, then stop.

**Do not begin Part 004 English translation in the same audit activity.**
