# HANDOVER — Kalaignar Literary Commentary Archive

## Repository

`pugazg/kalaignar-literary-commentary`

Active work:

`works/thirukkural/`

## Mandatory startup in a new chat

Before making any change:

1. read `THIRUKKURAL_ARCHIVAL_GUIDELINES.md` completely;
2. read `LITERARY_COMMENTARY_PROCESSING_GUIDE.md` completely;
3. read this `HANDOVER.md` completely;
4. read `works/thirukkural/README.md`;
5. inspect the existing target files before creating or updating anything;
6. for later English work, additionally read:
   - `works/thirukkural/translations/en/TRANSLATION_GUIDE.md`;
   - `works/thirukkural/translations/en/GLOSSARY.md`;
   - `works/thirukkural/translations/en/TRANSLATION_STATUS.md`;
   - the latest completed review/release artefacts, currently `PART_008_REVIEW.md` and `PART_008_RELEASE_REPORT.md`.

The repository state is authoritative for workflow status.

## Core source rule

The supplied scans are the controlling sources. Do not silently modernize, normalize, correct, reconstruct or improve Tamil.

The source PDFs are working/control sources and are **not to be uploaded into this GitHub repository** unless the user explicitly changes that instruction.

OCR or parsed text may assist but is never authoritative. Direct scan inspection controls Tamil transcription and verification.

## English identity and fidelity rule

The English layer is a **project-created translation**, not an official/publisher English edition.

Every aligned English page must identify:

```yaml
translation_type: "project_translation"
```

The audited Tamil Markdown page is the working translation basis; the Tamil scan remains the ultimate source authority.

The English must retain Kalaignar's language, examples, images, political/social vocabulary, emphases and interpretive direction. Do not substitute another commentator's reading or familiar standard English Kural wording.

Permanent protected examples include:

- chapter 38 `ஊழ்` → **Oozh**, with Kalaignar's `இயற்கை நிலை` → **natural condition**;
- Kural 543: Kalaignar explains `அந்தணர் நூற்கும்` as `அறவோர் நூல்களுக்கும்`; retain **the books of the virtuous**, not an automatic caste-specific “Brahmin(s)” rendering;
- preserve his governance, citizens, treasury, revenue, justice, public-resource and working-people language when it occurs;
- preserve direct source-supported comparisons rather than sanitizing them;
- preserve rational/inquiry framing when Kalaignar explicitly uses it.

## Permanent workflow

**Tamil transcription → Tamil direct visual verification → Tamil audit / archival-ready → English draft → English source-check → English editorial review → English release gate.**

These are separate gates. Do not collapse them.

# Established completed state

## Tamil

Parts **001–008 are audited / ARCHIVAL-READY** through:

- overall scan **169**;
- printed page **136**;
- Kural **670**.

Part 008 audit record:

`works/thirukkural/AUDIT_PART_008.md`

Part 009 first-pass transcription is now complete but **not verified and not audited**.

## English project translation

Parts **001–008 are fully released** continuously through Kural **670**.

Released Parts 001–008 must not be revised merely because later parts introduce similar terminology. Any project-wide change must be deliberate, source-supported and documented.

# Part 008 — CLOSED BASELINE

Part 008 Tamil is complete / **ARCHIVAL-READY** for scans **149–169 / printed pages 116–136 / Kural 566–670**.

Part 008 English is **RELEASE COMPLETE 21/21**.

Completed English artefacts:

- `works/thirukkural/translations/en/reviews/PART_008_REVIEW.md`
- `works/thirukkural/translations/en/reviews/PART_008_RELEASE_REPORT.md`

The released structural term is:

`அமைச்சியல்` → **Ministerial Affairs**

with metadata transition:

`Porul — Statecraft` → **`Porul — Ministerial Affairs`**.

Permanent Part 008 protections include Kalaignar's government/intelligence vocabulary, Kural 589's independent-spies logic, Kural 610's untiring-ruler explanation, Kural 615's relatives/friends/people-of-the-country circle, Kurals 618–620's rational/inquiry framing including **“God!”** and **Oozh**, Kural 632's council-of-ministers/citizens language, Kural 639's **seventy crore**, and direct images including the unbaked clay pot and chariot linchpin.

# Part 009 Tamil — FIRST-PASS COMPLETE / VERIFICATION PENDING

## Controlling source

`திருக்குறள்_கலைஞர்_உரை_part_009_pages_170-191.pdf`

The actual source was directly inspected before transcription. It contains **22 physical pages**.

Physical/content scope:

- overall scans **170–191**;
- printed pages **137–158**;
- Kural **671–780**;
- chapters **68–78**.

Current Part 009 Tamil state:

- first-pass transcription: **22 / 22 complete**;
- `needs-review`: **22 / 22**;
- `verified`: **0**;
- `partial`: **0**;
- `blocked`: **0**;
- direct visual verification: **not started**;
- Tamil audit: **not started**.

Every Part 009 page record uses:

```yaml
status: "needs-review"
transcription_method: "manual transcription from source scan; direct visual verification pending"
```

Do not promote a page to `verified` unless it has been directly compared with the controlling scan during the separate verification gate.

## Part 009 page/chapter map

| Scans | Printed pages | Chapter | Kural |
|---:|---:|---|---:|
| 170–171 | 137–138 | 68. `வினை செயல்வகை` | 671–680 |
| 172–173 | 139–140 | 69. `தூது` | 681–690 |
| 174–175 | 141–142 | 70. `மன்னரைச் சேர்ந்து ஒழுகல்` | 691–700 |
| 176–177 | 143–144 | 71. `குறிப்பறிதல்` | 701–710 |
| 178–179 | 145–146 | 72. `அவை அறிதல்` | 711–720 |
| 180–181 | 147–148 | 73. `அவை அஞ்சாமை` | 721–730 |
| 182–183 | 149–150 | 74. `நாடு` | 731–740 |
| 184–185 | 151–152 | 75. `அரண்` | 741–750 |
| 186–187 | 153–154 | 76. `பொருள் செயல்வகை` | 751–760 |
| 188–189 | 155–156 | 77. `படை மாட்சி` | 761–770 |
| 190–191 | 157–158 | 78. `படைச் செருக்கு` | 771–780 |

## Part 009 source-visible structural transitions

The first-pass metadata preserves these directly visible running-header changes:

1. scans **170–181** — `பொருள் — அமைச்சியல்`;
2. scan **182 / printed page 149 / Kural 731** — `பொருள் — அரணியல் — நாடு`;
3. scan **186 / printed page 153 / Kural 751** — `பொருள் — கூழியல் — பொருள் செயல்வகை`;
4. scan **188 / printed page 155 / Kural 761** — `பொருள் — படையியல் — படை மாட்சி`;
5. scan **190 / printed page 157 / Kural 771** — `பொருள் — படையியல் — படைச் செருக்கு`.

Do not flatten these distinct source sections during verification or later English work.

## Verification-sensitive first-pass readings

The following require deliberate image-level checking during the next gate. They are **not invitations to normalize from memory**.

### Scan 179 / Kural 717

The supplied scan visibly appears to print:

```text
கற்றறிந்தார் கல்வி விளங்கும் கசடறச்
சொற்றெரிதல் முன்னர் இழுக்கு.
```

This differs from familiar wording one might expect. The first-pass record deliberately preserves the scan reading. Verify letter-for-letter from the source and retain it if the image confirms it.

### Scan 180 / Kural 725 commentary

The first pass currently contains the awkward phrase:

`தருக்கமென்படும் அளவைக் திறமும்`

Verify the exact letters/spacing from the scan. Do not silently repair the prose according to expected grammar.

### Scan 182 / Kural 733 commentary

The first pass currently contains a visually uncertain phrase around:

`மளவுக்கு வளம்`

Resolve this from the scan itself during verification. Do not reconstruct from contextual expectation or another edition.

## Part 009 files created

All 22 page-aligned records now exist under `works/thirukkural/pages/`:

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

# Exact next activity

Perform the separate **Part 009 Tamil direct visual verification** for all **22 `needs-review` pages**, scans **170–191 / printed pages 137–158 / Kural 671–780**.

## Required procedure

1. fresh-read this handover and `works/thirukkural/README.md`;
2. use the actual Part 009 source scan as controlling authority;
3. compare each of the 22 Markdown records directly against its corresponding page image;
4. check Kural text **letter-for-letter**, including source joins/spacing and the two-line structure;
5. check every Kalaignar commentary sentence, punctuation and paragraph boundary;
6. check chapter title, running header, scan page, Part local page and printed page metadata;
7. explicitly resolve the verification-sensitive readings at scan 179 / Kural 717, scan 180 / Kural 725 commentary and scan 182 / Kural 733 commentary from the scan itself;
8. document every real correction found during verification;
9. promote only passing pages from `needs-review` to `verified` and change `transcription_method` to reflect direct visual comparison;
10. synchronize `works/thirukkural/README.md`, root `README.md` and this handover at the end of the verification gate;
11. stop after direct visual verification.

## Do not start alongside Part 009 verification unless explicitly requested

Do **not**:

- create `AUDIT_PART_009.md` during verification;
- call Part 009 archival-ready merely because all pages become verified;
- begin Part 009 English translation;
- begin Part 010 transcription;
- alter released English Parts 001–008.

# After Part 009 direct visual verification

If all 22 pages resolve to `verified` with no blockers, the next separate activity is the **Part 009 Tamil audit / archival-ready gate**. Only after that audit passes may Part 009 English translation begin.
