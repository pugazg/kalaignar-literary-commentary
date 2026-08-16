# திருக்குறள் — Part 009 archival audit

Audit date: **2026-08-16**

Source: `திருக்குறள்_கலைஞர்_உரை_part_009_pages_170-191.pdf`

A conversation or Library copy may carry a duplicate suffix such as `(1)`; the source identity above is the canonical project filename. The controlling authority is the supplied scan, not the attachment decoration or any external Thirukkural edition.

## Release decision

**ARCHIVAL-READY**

Part 009 passes the repository's source-first Tamil archival gate for the supplied material. All **22** physical source pages have corresponding Tamil Markdown records; all **22** records completed direct visual comparison with the controlling scans; overall scan, Part-local-page and printed-page numbering are continuous; Kural numbering is continuous from **671 through 780**; all chapter and running-header transitions are represented at the source-supported points; the one real correction found during direct visual verification is retained; three deliberately unusual source readings were confirmed from the scan and preserved without normalization; and there are no remaining `needs-review`, `partial`, `blocked`, or missing Part 009 records.

## Audit scope

This audit checked:

1. one-record-per-scan coverage for overall scans **170–191**;
2. Part 009 local-page continuity **1–22**;
3. printed-page continuity **137–158**;
4. source filename, work identity, section metadata and page-type metadata;
5. final `status` and `transcription_method` consistency across all 22 records;
6. Kural-number continuity **671–780**;
7. chapter continuity from chapter 68 `வினை செயல்வகை` through chapter 78 `படைச் செருக்கு`;
8. the Part 008 → Part 009 boundary at printed page **136 → 137** / Kural **670 → 671**;
9. the Part 009 → Part 010 intake boundary at printed page **158 → 159** / Kural **780 → 781**, confirmed from the supplied Part 010 scan without beginning Part 010 transcription;
10. the source-visible structural sequence `அமைச்சியல்` → `அரணியல்` → `கூழியல்` → `படையியல்`;
11. retention of the scan-190 / Kural-771 direct-verification correction;
12. retention of the visually confirmed source-sensitive readings at Kural 717, Kural 725 commentary and Kural 733 commentary;
13. absence of unsupported modernization, normalization, external-edition substitution or reconstruction;
14. unresolved items and limits of the supplied Part 009 material.

## 1. Scan coverage — PASS

The repository contains exactly one Part 009 Tamil page record for every expected overall scan from **170 through 191**.

Total Part 009 page records audited: **22 / 22**.

Coverage is continuous:

- `0170-porul-vinai-seyalvagai-01.md`
- `0171-porul-vinai-seyalvagai-02.md`
- `0172-porul-thoothu-01.md`
- `0173-porul-thoothu-02.md`
- `0174-porul-mannarai-sernthu-ozhugal-01.md`
- `0175-porul-mannarai-sernthu-ozhugal-02.md`
- `0176-porul-kuripparithal-01.md`
- `0177-porul-kuripparithal-02.md`
- `0178-porul-avai-arithal-01.md`
- `0179-porul-avai-arithal-02.md`
- `0180-porul-avai-anjaamai-01.md`
- `0181-porul-avai-anjaamai-02.md`
- `0182-porul-naadu-01.md`
- `0183-porul-naadu-02.md`
- `0184-porul-aran-01.md`
- `0185-porul-aran-02.md`
- `0186-porul-porul-seyalvagai-01.md`
- `0187-porul-porul-seyalvagai-02.md`
- `0188-porul-padai-maatchi-01.md`
- `0189-porul-padai-maatchi-02.md`
- `0190-porul-padai-serukku-01.md`
- `0191-porul-padai-serukku-02.md`

No Part 009 scan number is missing or duplicated.

## 2. Overall scan / Part-local-page continuity — PASS

Part 009 maps continuously as:

- local page 1 → overall scan 170;
- local page 2 → overall scan 171;
- …
- local page 22 → overall scan 191.

Every record carries `part: 9` with the corresponding `part_page` value **1–22**.

## 3. Printed-page continuity — PASS

The controlling Part 009 source contains a continuous printed-page sequence from **137 through 158**.

The repository metadata matches that sequence:

- scan 170 / local page 1 → printed page **137**;
- …
- scan 191 / local page 22 → printed page **158**.

There is no unexplained printed-page gap or unnumbered leaf inside Part 009.

## 4. Source identity / metadata — PASS

All 22 audited records consistently identify:

- `work: "thirukkural"`;
- `part: 9`;
- `language: "ta"`;
- `page_type: "commentary"`;
- `source_filename: "திருக்குறள்_கலைஞர்_உரை_part_009_pages_170-191.pdf"`;
- final `status: "verified"`;
- `transcription_method: "direct visual comparison with source scan"`.

The boundary records confirm the expected physical and textual range:

- scan 170 / local page 1 / printed page 137 begins with Kural **671**;
- scan 191 / local page 22 / printed page 158 ends with Kural **780**.

## 5. Final status consistency — PASS

Final Part 009 Tamil state at the audit gate:

- `verified`: **22**;
- `needs-review`: **0**;
- `partial`: **0**;
- `blocked`: **0**;
- missing/uncreated records: **0**.

Every Part 009 page record has completed the separate direct visual verification gate. No record remains in first-pass-only state.

## 6. Kural and chapter continuity — PASS

The supplied Part 009 source contains a continuous Kural sequence from **671 through 780**. No Kural number is omitted or duplicated within the supplied part.

Chapter coverage is:

- `68. வினை செயல்வகை` — Kural **671–680** — scans 170–171;
- `69. தூது` — **681–690** — scans 172–173;
- `70. மன்னரைச் சேர்ந்து ஒழுகல்` — **691–700** — scans 174–175;
- `71. குறிப்பறிதல்` — **701–710** — scans 176–177;
- `72. அவை அறிதல்` — **711–720** — scans 178–179;
- `73. அவை அஞ்சாமை` — **721–730** — scans 180–181;
- `74. நாடு` — **731–740** — scans 182–183;
- `75. அரண்` — **741–750** — scans 184–185;
- `76. பொருள் செயல்வகை` — **751–760** — scans 186–187;
- `77. படை மாட்சி` — **761–770** — scans 188–189;
- `78. படைச் செருக்கு` — **771–780** — scans 190–191.

Each chapter is complete within this supplied Part 009 unit.

## 7. Part 008 → Part 009 continuity — PASS

The processing-unit boundary is continuous and source-supported:

- Part 008 scan 169 / printed page **136** ends with Kural **670**;
- Part 009 scan 170 / printed page **137** begins chapter 68 `வினை செயல்வகை` with Kural **671**.

There is therefore no missing or duplicated printed page or Kural at the Part 008 → Part 009 boundary.

## 8. Part 009 → Part 010 intake continuity — PASS

The supplied Part 010 source was inspected only to establish the adjacent intake boundary. Its first physical page visibly carries printed page **159**, chapter **79. நட்பு**, and begins with Kural **781**.

Part 009 ends at:

- scan 191 / printed page **158** / Kural **780**.

The next supplied source therefore continues at:

- expected overall scan 192 / printed page **159** / Kural **781**.

This establishes continuous printed-page and Kural intake boundaries of **158 → 159** and **780 → 781**.

This audit does **not** transcribe, verify, audit or otherwise advance Part 010.

## 9. Structural transitions — PASS

The source's running-header hierarchy changes within Part 009 and the verified metadata preserves those distinctions rather than flattening them:

1. scans **170–181** — `பொருள் — அமைச்சியல்` with chapters 68–73;
2. scan **182 / printed page 149 / Kural 731** — transition to `பொருள் — அரணியல் — நாடு`;
3. scans **184–185** remain `பொருள் — அரணியல் — அரண்`;
4. scan **186 / printed page 153 / Kural 751** — transition to `பொருள் — கூழியல் — பொருள் செயல்வகை`;
5. scan **188 / printed page 155 / Kural 761** — transition to `பொருள் — படையியல் — படை மாட்சி`;
6. scan **190 / printed page 157 / Kural 771** — `பொருள் — படையியல் — படைச் செருக்கு`.

These are source-visible structural changes, not project-created classifications.

## 10. Direct visual-verification outcome — PASS

Direct visual verification was completed for all scans **170–191** before this audit.

One real first-pass body-text error was identified and corrected from the controlling scan:

- scan **190 / printed page 157 / Kural 771 commentary**
  - first pass: `நடுகல்லைப் போனவர்கள்`
  - verified source: **`நடுகல்லாய்ப் போனவர்கள்`**.

The audited record retains the verified source wording.

No other Part 009 body-text correction was required during direct visual verification.

## 11. Source-sensitive readings — PASS / PROTECTED

Three readings were deliberately held for image-level verification because they could easily be replaced by a familiar or grammatically expected form. The supplied scan confirms all three, and the verified records retain them exactly.

### Kural 717 — scan 179 / printed page 146

Confirmed source text:

```text
கற்றறிந்தார் கல்வி விளங்கும் கசடறச்
சொற்றெரிதல் முன்னர் இழுக்கு.
```

This source reading must not be silently replaced by a memorized or external-edition Kural.

### Kural 725 commentary — scan 180 / printed page 147

Confirmed source phrase:

`தருக்கமென்படும் அளவைக் திறமும்`

The archive preserves this printed wording without grammatical normalization.

### Kural 733 commentary — scan 182 / printed page 149

Confirmed source phrase:

`மளவுக்கு வளம்`

The archive preserves this printed wording rather than reconstructing a smoother phrase from context.

## 12. Source-fidelity / normalization check — PASS

The audited records preserve source-supported Tamil forms, line structure and commentary instead of silently replacing them with remembered, web, later-edition or normalized wording.

The audit specifically confirms retention of:

- the unusual Kural 717 wording printed in this source;
- `தருக்கமென்படும் அளவைக் திறமும்` in Kural 725 commentary;
- `மளவுக்கு வளம்` in Kural 733 commentary;
- `நடுகல்லாய்ப் போனவர்கள்` in the corrected Kural 771 commentary;
- the distinct source section labels `அமைச்சியல்`, `அரணியல்`, `கூழியல்`, and `படையியல்`.

Kalaignar's commentary has not been silently modernized, harmonized with another commentator or replaced with an external standard interpretation.

## 13. Source condition / non-text artefacts — PASS

The supplied 22-page Part 009 scan is readable for the archived text. Reverse-side show-through / bleed-through is visible on pages but is distinguishable from current-page printed text and has not been transcribed as body content.

No handwriting, stamp, page damage or scanner artefact in Part 009 creates an unresolved textual reading requiring `partial` or `blocked` status.

## 14. Unresolved items — NONE IN PART 009

Part 009 has no remaining unreadable page, unresolved character, partial transcription, blocked record, `needs-review` page or missing scan record.

This release decision applies only to the supplied Part 009 Tamil source segment. It does not release any English translation and does not advance Part 010 beyond the boundary inspection described above.

## Final Part 009 state

Part 009 satisfies the repository's source-first Tamil archival requirements:

- complete **22/22** physical-page coverage;
- continuous overall scans **170–191**;
- continuous local pages **1–22**;
- continuous printed pages **137–158**;
- continuous Kural range **671–780**;
- chapters **68–78** complete;
- all 22 records directly visually verified;
- source hierarchy `அமைச்சியல்` → `அரணியல்` → `கூழியல்` → `படையியல்` correctly represented;
- Part 008 → Part 009 and Part 009 → Part 010 intake continuity checked;
- the scan-190 / Kural-771 correction retained;
- all three unusual source-sensitive readings explicitly confirmed and protected;
- no unsupported normalization or external-edition substitution;
- no unresolved review state.

**Part 009 may therefore be treated as ARCHIVAL-READY.**

## Next activity

Tamil Parts **001–009** are now archival-ready continuously through overall scan **191** / printed page **158** / Kural **780**.

The next separate activity is **Part 009 English project translation — first pass** for the aligned pages covering scans **170–191 / Kural 671–780**.

Before beginning the English stage, fresh-read `translations/en/TRANSLATION_GUIDE.md`, `translations/en/GLOSSARY.md`, `translations/en/TRANSLATION_STATUS.md`, and the latest completed Part 008 English review/release artefacts. Create aligned English pages as `draft` only, retain Kalaignar's wording, images, institutional/social vocabulary and interpretive direction, and protect the source-sensitive Part 009 readings documented above.

Do not begin Part 010 Tamil transcription as part of this audit activity.