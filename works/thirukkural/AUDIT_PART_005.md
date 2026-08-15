# திருக்குறள் — Part 005 archival audit

Audit date: **2026-08-15**

Source: `திருக்குறள்_கலைஞர்_உரை_part_005_pages_85-106.pdf`

## Release decision

**ARCHIVAL-READY**

Part 005 passes the repository's source-first Tamil archival gate for the supplied material. All 22 supplied scan pages have one corresponding Tamil Markdown record, all 22 records have completed direct visual comparison against the controlling scans, metadata is continuous and internally consistent, Kural numbering is continuous from 256 through 365, and there are no remaining `needs-review`, `partial`, `blocked`, or uncreated Part 005 records.

## Audit scope

This audit checked:

1. one-record-per-scan coverage for overall scans 85–106;
2. Part 005 local-page continuity 1–22;
3. printed-page continuity 52–73;
4. source filename, work identity, section metadata and source markers;
5. final `status` and `transcription_method` consistency;
6. Kural-number continuity 256–365;
7. chapter continuity across the supplied segment;
8. the Part 004 → Part 005 boundary at Kural 255 → 256;
9. retention of the scan-supported correction made during visual verification at scan 99 / Kural 329 commentary;
10. absence of unsupported normalization, external-edition substitution or reconstruction;
11. unresolved items and limits of the supplied Part 005 material.

## 1. Scan coverage — PASS

The repository contains exactly one Part 005 page record for every overall scan from **85 through 106**.

Total Part 005 page records: **22 / 22**.

Coverage is continuous:

- `0085-aram-pulaal-maruththal-02.md`
- `0086-aram-thavam-01.md`
- `0087-aram-thavam-02.md`
- `0088-aram-koodaa-ozhukkam-01.md`
- `0089-aram-koodaa-ozhukkam-02.md`
- `0090-aram-kallaamai-01.md`
- `0091-aram-kallaamai-02.md`
- `0092-aram-vaaymai-01.md`
- `0093-aram-vaaymai-02.md`
- `0094-aram-vegulaamai-01.md`
- `0095-aram-vegulaamai-02.md`
- `0096-aram-innaa-seyyaamai-01.md`
- `0097-aram-innaa-seyyaamai-02.md`
- `0098-aram-kollaamai-01.md`
- `0099-aram-kollaamai-02.md`
- `0100-aram-nilaiyaamai-01.md`
- `0101-aram-nilaiyaamai-02.md`
- `0102-aram-thuravu-01.md`
- `0103-aram-thuravu-02.md`
- `0104-aram-meyyunarthal-01.md`
- `0105-aram-meyyunarthal-02.md`
- `0106-aram-avaa-aruththal-01.md`

No Part 005 scan number is missing or duplicated.

## 2. Overall scan / local-page continuity — PASS

Part 005 maps continuously as:

- local page 1 → overall scan 85;
- local page 2 → overall scan 86;
- ...
- local page 22 → overall scan 106.

Every record carries `part: 5` with the corresponding `part_page` value 1–22.

## 3. Printed-page continuity — PASS

The supplied source continues directly from Part 004:

- Part 004 scan 84 ends at printed page **51** / Kural **255**;
- Part 005 scan 85 begins at printed page **52** / Kural **256**.

Part 005 then proceeds continuously through printed page **73** at scan 106.

No printed-page gap or duplication is present inside Part 005.

## 4. Source identity / metadata — PASS

Part 005 records consistently identify:

- work: `thirukkural`;
- language: `ta`;
- source filename: `திருக்குறள்_கலைஞர்_உரை_part_005_pages_85-106.pdf`;
- overall scan range: **85–106**;
- Part 005 local pages: **1–22**;
- printed-page range: **52–73**;
- content range: Kural **256–365** with Kalaignar's commentary.

The first and last verified records confirm the expected metadata boundary:

- scan 85 / local 1 / printed 52 begins at Kural 256;
- scan 106 / local 22 / printed 73 ends at Kural 365.

## 5. Final status consistency — PASS

Final Part 005 state:

- `verified`: **22**
- `needs-review`: **0**
- `partial`: **0**
- `blocked`: **0**
- uncreated records: **0**

Every Part 005 page record uses:

`transcription_method: "direct visual comparison with source scan"`

No Part 005 record remains in first-pass-only status.

## 6. Source-page markers — PASS

Each Part 005 record retains the repository-standard source marker containing:

- overall scan page;
- Part 005 local page;
- printed page.

Pattern:

`<!-- மூல ஸ்கேன் பக்கம்: N; Part 005 உள்ளூர் பக்கம்: M; அச்சுப் பக்கம்: P -->`

The marker sequence aligns continuously with scans 85–106, local pages 1–22 and printed pages 52–73.

## 7. Kural continuity — PASS

The supplied Part 005 material contains a continuous Kural sequence from **256 through 365**.

No Kural number is omitted or duplicated in the Part 005 mapping.

Chapter coverage is:

- `26. புலால் மறுத்தல்` — Kural 256–260 in this part, completing the chapter begun in Part 004;
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
- `37. அவா அறுத்தல்` — Kural 361–365 supplied here.

Chapter 37 is intentionally incomplete in Part 005 because the supplied PDF ends at Kural 365. The archive does not import Kural 366 onward from another source into this part.

## 8. Part 004 → Part 005 continuity — PASS

The archival boundary is continuous and source-supported:

- Part 004 scan 84 / printed page 51 contains Kural 251–255, beginning `26. புலால் மறுத்தல்`;
- Part 005 scan 85 / printed page 52 continues the same chapter with Kural 256–260;
- Part 005 therefore completes chapter 26 without duplication or missing Kural numbers.

The repository keeps the two PDFs as separate processing units while preserving the book's continuous printed-page and Kural sequence.

## 9. Direct visual-verification outcome — PASS

Verification was completed against the actual supplied Part 005 scan images for all scans **85–106**.

Outcome:

- scans **85–98 and 100–106** matched the first-pass transcription without source-text correction;
- scan **99 / Kural 329 commentary** required one source-supported correction:
  - first pass: `பகுத்தறிவு மிகுந்த செயல்படும்`
  - controlling scan: **`பகுத்தறிவு இழந்து செயல்படும்`**

The corrected verified record now reads:

`பகுத்தறிவு இழந்து செயல்படும் கொலைகாரர்களைச் சான்றோர் உள்ளம், இழிதகைப் பிறவிகளாகவே கருதும்.`

No unresolved character uncertainty remains in Part 005.

## 10. Source-fidelity / normalization check — PASS

The final verified records preserve the supplied edition's source-specific Tamil rather than silently substituting a standard/web Kural text.

Source-specific printed forms retained in the verified Part 005 records include examples such as:

- `புலாஅல்`;
- `வேட்டலின்`;
- `தவமுந் தவமுடையார்க்`;
- `படிற்றொழுக்கம்`;
- `புத்தே ளுலகு`;
- `அறவினை யாதெனின்`;
- `நல்லா றெனப்படுவ`;
- `நெருந லுளனொருவன்`;
- `வேண்டினுண் டாகத்`;
- `தூஉய்மை`;
- `வாஅய்மை`;
- `அவாவென்ப எல்லா உயிர்க்குமெஞ் ஞான்றுந்`.

Kalaignar's commentary is retained as source text and has not been silently modernized, doctrinally harmonized, or replaced with another commentator's explanation.

## 11. Unresolved items — NONE IN PART 005

Part 005 has no remaining unreadable page, unresolved character, partial transcription, blocked record, or `needs-review` page.

This decision applies only to the supplied Part 005 segment. It does **not** imply that the complete Thirukkural commentary book or chapter 37 has been supplied.

The supplied source currently stops at overall scan **106** / printed page **73** / Kural **365**.

## Final Part 005 state

Part 005 satisfies the repository's source-first Tamil archival requirements for the supplied segment:

- complete **22/22** scan coverage;
- continuous overall scans **85–106**;
- continuous local pages **1–22**;
- continuous printed pages **52–73**;
- continuous Kural range **256–365**;
- all 22 records directly visually verified;
- source markers and metadata consistent;
- Part 004 → Part 005 continuity correctly represented;
- chapter continuity correctly represented;
- scan-99 correction retained;
- no unsupported normalization or external-edition substitution;
- no unresolved review state.

**Part 005 may therefore be treated as ARCHIVAL-READY.**

## Next activity

Part 005 Tamil archival processing is complete. Parts **001–005** are now archival-ready for all currently supplied Tamil source material, reaching Kural **365**.

The next source-first Tamil activity requires the next supplied scan/PDF beginning after overall scan 106 / printed page 73 / Kural 365.

Separately, **Part 004 English project translation is eligible to begin** because Part 004 Tamil is already archival-ready. Keep the existing translation rule: retain Kalaignar's language, images and interpretive direction; do not substitute standard external Thirukkural interpretations.
