# சங்கத் தமிழ் — Lexical Discrepancy Ledger

This ledger is the durable output of **Gate C — lexical discrepancy audit under the current Gemini lock**.

## Gate-C rule

Gate C is **audit-only**.

- compare the source-visible lexical text against the preserved Gemini-locked repository wording;
- record substantive lexical discrepancies only;
- do **not** edit canonical page wording;
- ignore harmless spacing, line-wrap, punctuation-only, running-header/footer placement, and purely visual differences unless they materially change the lexical reading;
- Gate C2 source correction is forbidden unless explicitly authorized by the user.

### Classification vocabulary

- `likely-gemini-error`
- `source-damaged-or-unclear`
- `old-or-uncommon-form`
- `missing-whole-lexical-block`
- `repository-only-divergence`

## Execution note

For C01, the controlling source supplied in-chat was:

`TVA_BOK_0042551_சங்கத்_தமிழ்_part_001_pages_1-50.pdf`

covering physical scans **1–50**.

`File1.md` itself was not present in the current conversation attachment set. Because the repository is already frozen under `GEMINI_TEXT_LOCK.md`, the **current canonical page wording is used as the durable preserved Gemini-lock layer** for this audit. This does not authorize any page correction.

# C01 — scans 1–25

**Status: COMPLETE / PASS**

- date: **2026-09-16**
- audited scans: **1–25 / 25**
- source: `TVA_BOK_0042551_சங்கத்_தமிழ்_part_001_pages_1-50.pdf`
- locked comparison layer: current canonical page records under `works/sangatamil/pages/`
- substantive discrepancy records: **11**
- scans containing discrepancies: **8**
- scans with no substantive lexical discrepancy recorded: **17**
- canonical page files changed: **0**
- Gate C2 corrections: **0**

Clean / no-new-substantive-discrepancy scans:

**1–4, 6, 10, 12, 14–18, 20, 22–25**

Special handling:
- scan **3** is a later library sticker / provenance leaf, not continuous literary body text;
- scan **15** is blank;
- scans **18** and **22** are full-page illustrations;
- scan **8** is a handwritten facsimile and is separately ledgered because its continuous body text remains untranscribed.

## C01 discrepancy records

| ID | Scan | Printed page | Canonical page | Locked repository wording | Source-visible wording | Classification | Gate-B exception already documented? | Notes |
|---|---:|---:|---|---|---|---|---|---|
| C01-001 | 5 | — | `0005-blank-ruled.md` | `வெளியீட்டாளர்` | `வெளியிட்டாளர்` | `likely-gemini-error` | no | Source heading on the lower-left publisher leaf visibly uses the shorter `வெளியிட்டாளர்` form. No page correction made. |
| C01-002 | 7 | II | `0007-publication-details.md` | `அளவு : 14 x 21 1/2` | `அளவு : 14 x 21½ சி.எம்.` | `likely-gemini-error` | **yes — B01** | The source-visible unit `சி.எம்.` is absent from the locked wording. B01 already preserved this as an unrecovered lexical omission. |
| C01-003 | 8 | III | `0008-munnurai-handwritten-facsimile.md` | no continuous handwritten body transcription | full-page handwritten `முன்னுரை` body | `missing-whole-lexical-block` | **yes — B01 special-page handling** | The page preserves a handwritten facsimile, but its continuous lexical body remains intentionally untranscribed because a safe letter-by-letter reading was not established. Requires a dedicated manual/palaeographic transcription if later authorized. |
| C01-004 | 9 | IV | `0009-e-ramalinganar-madal.md` | `தங்கள் கட்டளையை ஒருவாறு நிறைவேற்றினேன்` | `தங்கள் கட்டளையை ஒருவாறு நிறைவேற்றிவிட்டேன்` | `likely-gemini-error` | no | The source visibly contains the additional lexical element `விட்டேன்`. A pre-lock source-led Pass-2 commit had also identified this reading; current locked wording intentionally remains unchanged. |
| C01-005 | 11 | VI | `0011-aninthurai-02.md` | `ஆண்பாலர் பதினால்வர்` | `ஆண்பாலர் பதினுலவர்` | `likely-gemini-error` | no | The printed source reads `பதினுலவர்`, not the locked `பதினால்வர்`. |
| C01-006 | 13 | VIII | `0013-aninthurai-04.md` | `அதனைக் களைகின்ற திறல் மிக்க` | `அதனைக் களைவதிறல் மிக்க` | `likely-gemini-error` | no | Continuous source prose visibly reads the compound `களைவதிறல்`. |
| C01-007 | 13 | VIII | `0013-aninthurai-04.md` | `சொல் நயத்தை மற்றாரும் நுகரும் வண்ணம்` | `சொல் நயத்தை மற்றரும் நுகரும் வண்ணம்` | `likely-gemini-error` | no | Source uses `மற்றரும்`; locked repository uses `மற்றாரும்`. |
| C01-008 | 19 | 4 | `0019-malarmari-pozhiginren-02.md` | `அரும்பு, அமர் ஆத்தி` | `அடும்பு, அமர் ஆத்தி` | `likely-gemini-error` | no | In the printed Kurinjippattu flower list, the source visibly reads `அடும்பு`. |
| C01-009 | 21 | 6 | `0021-yaathum-oore-yaavarum-kelir-02.md` | body begins `சங்கத் தமிழ் அரசர்களின் அவைக்களத்தில்...` | body begins `அரசர்களின் அவைக்களத்தில்...`; `சங்கத் தமிழ்` appears only as the running header | `repository-only-divergence` | no | The running header has been incorporated into the first body line in the canonical record. Gate C records it only; Gate B is not reopened. |
| C01-010 | 21 | 6 | `0021-yaathum-oore-yaavarum-kelir-02.md` | `ஏடுகொள்ளா இலக்கியங்கள் காதலையும் களம்புகுவோர் / எடுத்தியம்பும் காரணத்தால்...` | `ஏடுகொள்ளா இலக்கியங்கள் காதலையும் களம்புகுவோர் / காதலையும் / எடுத்தியம்பும் காரணத்தால்...` | `likely-gemini-error` | no | Source contains a right-aligned continuation `காதலையும்` that is absent from the locked page body. |
| C01-011 | 21 | 6 | `0021-yaathum-oore-yaavarum-kelir-02.md` | `எடுத்தியம்பும் காரணத்தால் என்வழியைத் தனிவழியாய் / எல்லா ஊரும்...` | `எடுத்தியம்பும் காரணத்தால் என்வழியைத் தனிவழியாய் / ஆக்கிக்கொண்டு / எல்லா ஊரும்...` | `likely-gemini-error` | no | Source contains the right-aligned continuation `ஆக்கிக்கொண்டு`, absent from the locked repository wording. |

## C01 closure audit

C01 is an **audit-only closure**.

- source scans **1–25** were inspected;
- **11** substantive discrepancy records were entered;
- **0** canonical page records were edited;
- no Gate-B structural page was reopened;
- no lexical correction was promoted;
- wording state remains **Gemini-lexical-locked / not word-for-word scan verified**.

## Gate C cumulative state after C01

- completed Gate-C batches: **C01**
- audited scans: **25/497**
- remaining: **472**
- next frontier: **scan 26**
- Gate C2: **NOT STARTED / NOT AUTHORIZED**

## Exact next activity

Process **Gate C C02 — scans 26–50** using the already supplied:

`TVA_BOK_0042551_சங்கத்_தமிழ்_part_001_pages_1-50.pdf`

and the preserved canonical Gemini-locked wording for scans 26–50.

If `File1.md` becomes available, it may be used as an additional direct lock witness; until then, do not infer or reconstruct it.

At C02 close:
1. append only substantive lexical discrepancies to this ledger;
2. verify **0 canonical page files changed**;
3. advance the Gate-C frontier to **scan 51**;
4. do not start Gate C2.
