# திருக்குறள் — கலைஞர் உரை

கலைஞர் மு. கருணாநிதியின் **திருக்குறள் — கலைஞர் உரை** நூலை மூல ஸ்கேன்களை controlling source ஆகக் கொண்டு பக்கவாரியாக மின்னாக்கும் பகுதி.

Last synchronized with actual `main` repository state: **2026-08-17**.

## கிடைத்துள்ள மூலத் தொகுதிகள்

| Part | Source file | Local pages | Overall scans | Tamil state | English project translation |
|---|---|---:|---:|---|---|
| 001 | `திருக்குறள்_கலைஞர்_உரை_part_001_pages_1-20.pdf` | 20 | 1–20 | archival-ready; scan 8 documented partial | released with source limitation |
| 002 | `திருக்குறள்_கலைஞர்_உரை_part_002_pages_21-41.pdf` | 21 | 21–41 | **ARCHIVAL-READY** | **RELEASE-READY 21/21** |
| 003 | `திருக்குறள்_கலைஞர்_உரை_part_003_pages_42-62.pdf` | 21 | 42–62 | **ARCHIVAL-READY** | **RELEASE-READY 21/21** |
| 004 | `திருக்குறள்_கலைஞர்_உரை_part_004_pages_63-84.pdf` | 22 | 63–84 | **ARCHIVAL-READY** | **RELEASE-READY 22/22** |
| 005 | `திருக்குறள்_கலைஞர்_உரை_part_005_pages_85-106.pdf` | 22 | 85–106 | **ARCHIVAL-READY** | **RELEASE-READY 22/22** |
| 006 | `திருக்குறள்_கலைஞர்_உரை_part_006_pages_107-127.pdf` | 21 | 107–127 | **ARCHIVAL-READY** | **RELEASE-READY 21/21** |
| 007 | `திருக்குறள்_கலைஞர்_உரை_part_007_pages_128-148.pdf` | 21 | 128–148 | **ARCHIVAL-READY** | **RELEASE-READY 21/21** |
| 008 | `திருக்குறள்_கலைஞர்_உரை_part_008_pages_149-169.pdf` | 21 | 149–169 | **ARCHIVAL-READY** | **RELEASE-READY 21/21** |
| 009 | `திருக்குறள்_கலைஞர்_உரை_part_009_pages_170-191.pdf` | 22 | 170–191 | **ARCHIVAL-READY** | **RELEASE-READY 22/22** |
| 010 | `திருக்குறள்_கலைஞர்_உரை_part_010_pages_192-214.pdf` | 23 | 192–214 | **ARCHIVAL-READY — 23/23 verified** | **RELEASE-READY 23/23** |
| 011 | `திருக்குறள்_கலைஞர்_உரை_part_011_pages_215-237.pdf` | 23 | 215–237 | **ARCHIVAL-READY — 23/23 verified** | **RELEASE-READY 23/23** |
| 012 | `திருக்குறள்_கலைஞர்_உரை_part_012_pages_238-260.pdf` | 23 | 238–260 | **ARCHIVAL-READY — 23/23 verified** | **RELEASE-READY 23/23** |
| 013 | `திருக்குறள்_கலைஞர்_உரை_part_013_pages_261-282.pdf` | 22 | 261–282 | **ARCHIVAL-READY — 22/22 verified** | **RELEASE-READY 22/22** |
| 014 | `திருக்குறள்_கலைஞர்_உரை_part_014_pages_283-302.pdf` | 20 | 283–302 | **ARCHIVAL-READY — 20/20 verified** | **RELEASE-READY 20/20** |
| 015 | `திருக்குறள்_கலைஞர்_உரை_part_015_pages_303-323.pdf` | 21 | 303–323 | **FIRST PASS COMPLETE 21/21; scans 303–306 verified; scans 307–323 needs-review** | not started |

## Canonical continuity

Tamil Parts **001–014 are archival-ready continuously** through:

- overall scan **302**;
- printed page **269**;
- Kural **1325**.

English Parts **001–014 are released continuously** through the same boundary. Part 014 English passed its source-check, editorial review and separate release gate; all 20 aligned pages are `release-ready`.

## Part 015 source-confirmed structure

The supplied Part 015 scan has **21 physical pages**, overall scans **303–323**.

- scan **303 / printed page 270** continues chapter 133 `ஊடலுவகை` with Kurals **1326–1330** and reaches the end of the Thirukkural commentary;
- scans **304–321 / printed pages 271–288** contain `குறள் முதற்குறிப்பு அகரவரிசை`;
- scan **322** is an unnumbered blank leaf;
- scan **323** is the back cover.

The Part 014 → Part 015 textual boundary is source-confirmed as **1325 → 1326**.

## Part 015 Tamil current state

All **21/21** physical page records now exist under `works/thirukkural/pages/`:

- `0303-inbam-oodaluvagai-02.md` — verified;
- `0304-kural-mutharkurippu-01.md` — verified;
- `0305-kural-mutharkurippu-02.md` — verified;
- `0306-kural-mutharkurippu-03.md` — verified;
- scans **307–321** — first-pass index transcriptions, `needs-review`;
- scan **322** — blank-page record, `needs-review`;
- scan **323** — back-cover record, `needs-review`.

Therefore Part 015 is **not yet ARCHIVAL-READY**. `AUDIT_PART_015.md` must not be created until scans 307–323 have completed direct visual verification.

## Repository-state discipline

When old saved prompts, continuation documents or README snapshots conflict with actual current progress, use this precedence:

**actual page files on `main` → completed audits/review/release reports → `translations/en/TRANSLATION_STATUS.md` → current handover/READMEs → older historical status snapshots.**

Permanent source-preservation rules in older guides remain binding even when their progress snapshots are obsolete.

## அடுத்த செயல்

Perform **Part 015 Tamil direct visual verification for scans 307–323**. Compare each index row and Kural-number reference directly with the controlling scan; verify scan 322 as blank and scan 323 as the back cover. Correct only source-supported differences and promote each passing record to `verified`.

After all 21 Part 015 records are resolved, perform the separate Part 015 audit and only then begin any Part 015 English work.
