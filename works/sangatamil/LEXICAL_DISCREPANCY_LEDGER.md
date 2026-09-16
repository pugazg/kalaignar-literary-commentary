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


# C02 — scans 26–50

**Status: COMPLETE / PASS**

- date: **2026-09-16**
- audited scans: **26–50 / 25**
- source: `TVA_BOK_0042551_சங்கத்_தமிழ்_part_001_pages_1-50.pdf`
- locked comparison layer: current canonical page records under `works/sangatamil/pages/`
- substantive discrepancy records: **9**
- scans containing discrepancies: **6**
- scans with no new substantive lexical discrepancy: **19**
- canonical page files changed: **0**
- Gate C2 corrections: **0**

Clean / no-new-substantive-discrepancy scans:

**26, 27, 30–34, 36–38, 41–46, 48–50**

Special handling:
- scans **26, 32, 38, 44, 48** are full-page illustrations and contain no literary body text;
- punctuation-only, line-wrap, running-header, quotation-layout and other purely structural differences were not entered unless they materially altered lexical interpretation.

## C02 discrepancy records

| ID | Scan | Printed page | Canonical page | Locked repository wording | Source-visible wording | Classification | Gate-B exception already documented? | Notes |
|---|---:|---:|---|---|---|---|---|---|
| C02-001 | 28 | 13 | `0028-maanangkaatha-maravan-04.md` | `அட்டா; அவனைச் சோழமன்னன்` | `அடடா; அவனைச் சோழமன்னன்` | `likely-gemini-error` | no | Source interjection is visibly `அடடா`; locked wording has `அட்டா`. |
| C02-002 | 29 | 14 | `0029-maanangkaatha-maravan-05.md` | `வந்துதித்த நானோ` | `வந்துதித்த நானே` | `likely-gemini-error` | no | Source has emphatic `நானே`; locked wording changes the vowel and sense to `நானோ`. |
| C02-003 | 29 | 14 | `0029-maanangkaatha-maravan-05.md` | `அந்தப் மனப் பண்பாட்டு மரபு...` / next line `புண்பட்டு...` | `அந்தப் / பண்பாட்டு மரபு... நானே - மனப் / புண்பட்டு...` | `repository-only-divergence` | no | The same locked token `மனப்` is materially displaced before `பண்பாட்டு`; in the source it qualifies `புண்பட்டு`. Because the placement changes the lexical reading, it is recorded in Gate C even though ordinary placement-only differences are excluded. |
| C02-004 | 35 | 20 | `0035-thunai-nindraar-thozhi-05.md` | `குன்றெடுக்கும் நெடுந்தோள் கொண்டவனே! வீணே பகையை` while the earlier question lacks `வீணே` | source: `தேன் குடிக்கப் போகின்ற வண்டை - வீணே / ஏன் தடுக்கின்றாய்?`; later `குன்றெடுக்கும் நெடுந்தோள் கொண்டவனே! - பகையை` | `repository-only-divergence` | no | `வீணே` exists in both layers but is attached to the wrong sentence in the locked page, materially changing the meaning of both clauses. |
| C02-005 | 39 | 24 | `0039-sumanthavan-sumantha-sogam-03.md` | `ஔவைக்குக்` | `ஒளவைக்குக்` | `old-or-uncommon-form` | no | This edition prints the historical/name form `ஒளவை`; locked wording normalizes this occurrence to `ஔவை`. |
| C02-006 | 40 | 25 | `0040-sumanthavan-sumantha-sogam-04.md` | `ஔவைப் பிராட்டி` | `ஒளவைப் பிராட்டி` | `old-or-uncommon-form` | no | Same edition-specific name-form divergence as scan 39. |
| C02-007 | 40 | 25 | `0040-sumanthavan-sumantha-sogam-04.md` | `வெள்ளை வெள்யாட்டுச் செச்சை போலத்` | `வெள்ளை வெள்ளாட்டுச் செச்சை போலத்` | `likely-gemini-error` | **yes — B02** | B02 already documented this locked quote discrepancy. The source gloss on scan 41 also reads `வெள்ளாட்டுச் செச்சை`, corroborating the source form. |
| C02-008 | 47 | 32 | `0047-kaakkaikku-nandri-kaatta-01.md` | heading `காக்கைக்கு` | heading `காக்கைக்கு நன்றி காட்ட...` | `likely-gemini-error` | **yes — B02** | File1/locked body supplies only the first heading word; the source-visible heading remainder remains unrecovered under the lock. |
| C02-009 | 47 | 32 | `0047-kaakkaikku-nandri-kaatta-01.md` | `அப்படியொரு காகம் கரைந்திற்றாங்கே!` | `அப்படியொரு காகம் கரைந்திற்றங்கே!` | `likely-gemini-error` | no | Source lacks the additional long `ஆ` present in the locked form. |

## C02 closure audit

C02 is an **audit-only closure**.

- source scans **26–50** were visually inspected against the preserved locked page layer;
- **9** substantive discrepancy records were entered;
- **0** canonical page records were edited;
- no Gate-B page was reopened;
- no lexical correction was promoted;
- wording state remains **Gemini-lexical-locked / not word-for-word scan verified**.

## Gate C cumulative state after C02

- completed Gate-C batches: **C01–C02**
- audited scans: **50/497**
- cumulative substantive discrepancy records: **20**
- remaining scans: **447**
- next frontier: **scan 51**
- Gate C2: **NOT STARTED / NOT AUTHORIZED**

## Exact next activity

Process **Gate C C03 — scans 51–75**.

Required source pair from the durable Gate-B mapping:

- `TVA_BOK_0042551_சங்கத்_தமிழ்_part_002_pages_51-100.pdf`
- `File2.md` when directly available; otherwise the current canonical wording remains the preserved Gemini-lock comparison layer.

At C03 close:
1. append only substantive lexical discrepancies to this ledger;
2. verify **0 canonical page files changed**;
3. advance the Gate-C frontier to **scan 76**;
4. do not start Gate C2.


# C03 — scans 51–75

**Status: COMPLETE / PASS**

- date: **2026-09-16**
- audited scans: **51–75 / 25**
- source: Library original `TVA_BOK_0042551_சங்கத்_தமிழ்.pdf`, physical scans **51–75**
- requested split `TVA_BOK_0042551_சங்கத்_தமிழ்_part_002_pages_51-100.pdf` was not directly available in the active attachment/library set; the full original source was used instead
- locked comparison layer: current canonical page records under `works/sangatamil/pages/`
- `File2.md` was not directly available; it was not reconstructed or inferred
- substantive discrepancy records: **7**
- scans containing discrepancies: **6**
- scans with no new substantive lexical discrepancy: **19**
- canonical page files changed: **0**
- Gate C2 corrections: **0**

Clean / no-new-substantive-discrepancy scans:

**52, 54–57, 60–63, 65–69, 71–75**

Special handling:
- scans **52, 56, 60, 66, 72** are full-page illustrations and contain no literary body text;
- punctuation-only, line-wrap, running-header/footer, quotation-layout and purely structural differences were excluded unless they materially altered lexical interpretation;
- older pre-lock fast-transcription variants were treated only as candidate witnesses and were not accepted where the source image did not support them confidently.

## C03 discrepancy records

| ID | Scan | Printed page | Canonical page | Locked repository wording | Source-visible wording | Classification | Gate-B exception already documented? | Notes |
|---|---:|---:|---|---|---|---|---|---|
| C03-001 | 51 | 36 | `0051-maatharin-kanda-malargal-02.md` | `எதிரிகளைக` | `எதிரிகளைக்` | `likely-gemini-error` | no | The source visibly carries the final consonant marker; the locked form drops it. |
| C03-002 | 53 | 38 | `0053-maatharin-kanda-malargal-04.md` | `விருப்பைச்` | `இருப்பைச்` | `likely-gemini-error` | no | The source quote reads `இருப்பைச்`; the glossary on scan 54 also has `இருப்பை = இலுப்பை மரம்`, corroborating the source reading. |
| C03-003 | 58 | 43 | `0058-nellum-uyir-anre-neerum-uyir-anre-04.md` | `வேந்தர்க்குக்` | `வேந்தற்குக்` | `likely-gemini-error` | no | The printed Sangam quotation uses `வேந்தற்குக்`; the locked repository wording inserts an additional `ர்`. |
| C03-004 | 59 | 44 | `0059-oorin-perumai-unarnthavar-oruthi-01.md` | `முன்னைக் கொடியும்` | `முஞ்ஞைக் கொடியும்` | `likely-gemini-error` | no | The source-visible form is `முஞ்ஞைக்`; the later source quotation on scan 63 likewise has `முஞ்ஞையொடு`. |
| C03-005 | 64 | 49 | `0064-oorin-perumai-unarnthavar-oruthi-06.md` | `கனைதுல் = மிக உறக்கம்` | `கனைதுயில் = மிக உறக்கம்` | `likely-gemini-error` | no | The gloss source visibly reads `கனைதுயில்`; the quotation on scan 63 also contains `கனைதுயில்`. |
| C03-006 | 64 | 49 | `0064-oorin-perumai-unarnthavar-oruthi-06.md` | `ஔவை துரைசாமிப் பிள்ளை` | `ஒளவை துரைசாமிப் பிள்ளை` | `old-or-uncommon-form` | no | This edition prints the name form `ஒளவை`, consistent with the same edition-form divergence already observed in C02. |
| C03-007 | 70 | 55 | `0070-oru-vaathu-magal-in-pulambal-01.md` | heading `பொது மகளின் புலம்பல்!` | heading `ஒரு பொது மகளின் புலம்பல்!` | `likely-gemini-error` | **yes — B03** | B03 already documented that File2/locked wording omits the leading source-visible word `ஒரு`. |

## C03 closure audit

C03 is an **audit-only closure**.

- source scans **51–75** were inspected against the preserved locked page layer;
- **7** substantive discrepancy records were entered;
- **0** canonical page records were edited;
- no Gate-B page was reopened;
- no lexical correction was promoted;
- wording state remains **Gemini-lexical-locked / not word-for-word scan verified**.

## Gate C cumulative state after C03

- completed Gate-C batches: **C01–C03**
- audited scans: **75/497**
- cumulative substantive discrepancy records: **27**
- remaining scans: **422**
- next frontier: **scan 76**
- Gate C2: **NOT STARTED / NOT AUTHORIZED**

## Exact next activity

Process **Gate C C04 — scans 76–100**.

Controlling source:
- Library original `TVA_BOK_0042551_சங்கத்_தமிழ்.pdf`, physical scans **76–100**;
- matching lexical witness `File2.md` if it becomes directly available; otherwise current canonical wording remains the preserved Gemini-lock comparison layer.

At C04 close:
1. append only substantive lexical discrepancies to this ledger;
2. verify **0 canonical page files changed**;
3. advance the Gate-C frontier to **scan 101**;
4. do not start Gate C2.
