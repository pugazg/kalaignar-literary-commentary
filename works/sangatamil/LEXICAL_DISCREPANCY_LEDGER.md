# சங்கத் தமிழ் — Lexical Discrepancy Ledger

This ledger is the durable output of **Gate C — lexical discrepancy audit under the current Gemini lock**.

## Gate-C rule

Gate C is **audit-only**.

- compare the source-visible lexical text against the preserved Gemini-locked repository wording;
- record substantive lexical discrepancies only;
- do **not** edit canonical page wording;
- ignore harmless spacing, line-wrap, punctuation-only, running-header/footer placement, and purely visual differences unless they materially change the lexical reading;
- Gate C2 source correction is forbidden outside the batches and individual findings explicitly adjudicated by the user.

### Classification vocabulary

- `likely-gemini-error`
- `source-damaged-or-unclear`
- `old-or-uncommon-form`
- `missing-whole-lexical-block`
- `repository-only-divergence`


## Gate C2 superseding adjudication

Gate C is a historical audit record. C2 disposition is now complete through **scan 497**: all 140 historical Gate-C discrepancy records have been manually adjudicated; scans 126–150 contained no discrepancy records and required no page action. Those manual rulings supersede the earlier automated interpretation for correction decisions.

Durable Gate-C2 record: `C2_SOURCE_CORRECTION_PROGRESS.md`.

Important:
- C2-01 scans **1–25 — COMPLETE / APPLIED**;
- C2-02 scans **26–50 — COMPLETE / APPLIED**;
- C2-03 scans **51–75 — COMPLETE / APPLIED**;
- C2-04 scans **76–100 — COMPLETE / APPLIED**;
- C2-05 scans **101–125 — COMPLETE / APPLIED**;
- C2-06 scans **126–150 — COMPLETE / NO DISCREPANCY RECORDS / NO PAGE ACTION**;
- C2-07 scans **151–175 — COMPLETE / APPLIED**;
- C2-08 scans **176–200 — COMPLETE / APPLIED**;
- C2-09 scans **201–225 — COMPLETE / APPLIED**;
- C2-10 scans **226–250 — COMPLETE / APPLIED**;
- C2-11 scans **251–275 — COMPLETE / APPLIED**;
- C2-12 scans **276–300 — COMPLETE / APPLIED**;
- C2-13 scans **301–325 — COMPLETE / APPLIED**;
- C2-14 scans **326–350 — COMPLETE / APPLIED**;
- C2-15 scans **351–375 — COMPLETE / APPLIED**;
- C2-16 scans **376–400 — COMPLETE / APPLIED**;
- C2-17 scans **401–425 — COMPLETE / APPLIED**;
- C2-18 scans **426–450 — COMPLETE / APPLIED**;
- C2-19 scans **451–475 — COMPLETE / APPLIED**;
- C2-20 scans **476–497 — COMPLETE / APPLIED — FINAL C2 BATCH**;
- entries the user marks **Gemini is correct** are protected and must not be source-corrected;
- scan **8** is a handwritten letter/facsimile and is description-only by user instruction;
- **no scan range remains C2-locked**; all historical Gate-C discrepancy rows are dispositioned. Historical rows remain preserved as audit evidence.


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


# C04 — scans 76–100

**Status: COMPLETE / PASS**

- date: **2026-09-16**
- audited scans: **76–100 / 25**
- source: Library original `TVA_BOK_0042551_சங்கத்_தமிழ்.pdf`, physical scans **76–100**
- locked comparison layer: current canonical page records under `works/sangatamil/pages/`
- `File2.md` was not directly available; it was not reconstructed or inferred
- substantive discrepancy records: **5**
- scans containing discrepancies: **4**
- scans with no new substantive lexical discrepancy: **21**
- canonical page files changed: **0**
- Gate C2 corrections: **0**

Clean / no-new-substantive-discrepancy scans:

**76, 78–82, 84–86, 88–95, 97–100**

Special handling:
- scans **76, 82, 86, 92, 98** are full-page illustrations and contain no literary body text;
- punctuation-only, line-wrap, running-header/footer, quotation-layout and purely structural differences were excluded unless they materially altered lexical interpretation;
- older pre-lock fast-transcription text was used only as a candidate witness and was accepted into the ledger only where the source-visible reading was sufficiently clear;
- the two durable Gate-B discrepancies already carried forward at scans **83** and **96** were explicitly resolved into Gate-C ledger records, without changing the page layer.

## C04 discrepancy records

| ID | Scan | Printed page | Canonical page | Locked repository wording | Source-visible wording | Classification | Gate-B exception already documented? | Notes |
|---|---:|---:|---|---|---|---|---|---|
| C04-001 | 77 | 62 | `0077-pisiranthaiyar-1-02.md` | `பாண்டுநாட்டுச் சிற்றூரில்` | `பாண்டிநாட்டுச் சிற்றூரில்` | `likely-gemini-error` | no | The source-visible place-name form is `பாண்டிநாட்டுச்`; the locked layer substitutes `பாண்டு`. |
| C04-002 | 83 | 68 | `0083-pisiranthaiyar-2-02.md` | locked body begins directly with `அன்னச்சேவலே! அன்னச்சேவலே!` | source contains a substantial introductory prose block before the quotation, beginning `அன்னச்சேவலை மையமாய் வைத்து...` and ending with the thought that the Chola king's generosity and affection became the song's subject | `missing-whole-lexical-block` | **yes — B04** | B04 already documented that File2 omits this source-visible prose. Gate C records the omission but does not reconstruct the missing block into the canonical page. |
| C04-003 | 87 | 72 | `0087-pisirandhaiyar-3-02.md` | `சந்தையில் தொலைத்துவிட்ட பொருளாயிற்றே தமது மகிழ்ச்சி` | `சிந்தையில் தொலைத்துவிட்ட பொருளாயிற்றே தமது மகிழ்ச்சி` | `likely-gemini-error` | no | The source reads `சிந்தையில்`; the locked `சந்தையில்` changes “in the mind” into “in the market.” |
| C04-004 | 96 | 81 | `0096-ulaik-kaathu-irumbum-oru-thaniveeran-01.md` | heading `லேக் களத்து ளில் இரும்பும் ஒரு துளிநீரும்!` | heading `உலைக் களத்து இரும்பும் ஒரு துளிநீரும்!` | `likely-gemini-error` | **yes — B04** | B04 already carried this malformed File2 heading forward for Gate C. The source section identity is already preserved in metadata, but the locked body heading remains unchanged. |
| C04-005 | 96 | 81 | `0096-ulaik-kaathu-irumbum-oru-thaniveeran-01.md` | `சிவகெங்கைச் சீமை` | `சிவகங்கைச் சீமை` | `likely-gemini-error` | no | The source-visible place name is `சிவகங்கை`; the locked layer has `சிவகெங்கை`. |

## C04 closure audit

C04 is an **audit-only closure**.

- source scans **76–100** were inspected against the preserved locked page layer;
- **5** substantive discrepancy records were entered;
- **0** canonical page records were edited;
- no Gate-B page was reopened;
- no lexical correction was promoted;
- wording state remains **Gemini-lexical-locked / not word-for-word scan verified**.

## Gate C cumulative state after C04

- completed Gate-C batches: **C01–C04**
- audited scans: **100/497**
- cumulative substantive discrepancy records: **32**
- remaining scans: **397**
- next frontier: **scan 101**
- Gate C2: **NOT STARTED / NOT AUTHORIZED**

## Exact next activity

Process **Gate C C05 — scans 101–125**.

Controlling source:
- Library original `TVA_BOK_0042551_சங்கத்_தமிழ்.pdf`, physical scans **101–125**;
- matching lexical witness `File3.md` if it becomes directly available; otherwise current canonical wording remains the preserved Gemini-lock comparison layer.

At C05 close:
1. append only substantive lexical discrepancies to this ledger;
2. verify **0 canonical page files changed**;
3. advance the Gate-C frontier to **scan 126**;
4. do not start Gate C2.


# C05 — scans 101–125

**Status: COMPLETE / PASS**

- date: **2026-09-16**
- audited scans: **101–125 / 25**
- controlling source: user-supplied `TVA_BOK_0042551_சங்கத்_தமிழ்_part_003_pages_101-150.pdf`, physical scans **101–125**
- direct Gemini lexical witness: user-supplied `File3.md`, Pages **101–125**
- locked comparison layer: current canonical page records under `works/sangatamil/pages/`
- substantive discrepancy records: **4**
- scans containing discrepancies: **4**
- scans with no new substantive lexical discrepancy: **21**
- canonical page files changed: **0**
- Gate C2 corrections: **0**

Clean / no-new-substantive-discrepancy scans:

**101–111, 114–119, 121–122, 124–125**

Special handling:
- scans **104, 108, 114, 118, 122** are full-page illustrations and contain no literary body text;
- the direct File3 witness was used for this batch rather than relying only on the preserved repository lock;
- known non-source extraction debris already excluded during Gate B — scan 103 stray `ரீ`, scan 120 malformed punctuation in `மகிழ்ச்ச.ி`, and scan 121 stray heading token `G` — was not re-entered as a Gate-C discrepancy because the canonical preservation layer already excludes it;
- punctuation-only, spacing, line-wrap, running-header/footer and structural-placement differences were not ledgered unless they changed lexical content.

## C05 discrepancy records

| ID | Scan | Printed page | Canonical page | Locked File3 / repository wording | Source-visible wording | Classification | Gate-B exception already documented? | Notes |
|---|---:|---:|---|---|---|---|---|---|
| C05-001 | 112 | 97 | `0112-purinthukondaan-pirinthu-sendraal-01.md` | heading `புரிந்துகொண்டான், பிரிந்துசென்றார்!` | heading `புரிந்துகொண்டான், பிரிந்து சென்றாள்!` | `likely-gemini-error` | **yes — B05** | The source decorative title ends in singular feminine `சென்றாள்`; File3 locks plural/honorific `சென்றார்` and merges the preceding word boundary. Gate B preserved the File3 body heading while keeping the source section identity in metadata. |
| C05-002 | 113 | 98 | `0113-purinthukondaan-pirinthu-sendraal-02.md` | File3 ends the prose with `புரிந்து கொண்டான் அவள் உள்ளம்; பின்னர் பிரிந்து சென்றார் புன்னகை புரிந்தவாறே!` and then `அக்கேள்வி!`; the source-visible first stanza of the following Kalithogai quotation is absent | source contains the opening quotation stanza after the prose, continuing across the illustration boundary to the quotation preserved on scan 115 | `missing-whole-lexical-block` | **yes — B05** | The missing block was already carried forward by Gate B. Gate C records the omission only; no reconstruction was inserted into the canonical page. |
| C05-003 | 120 | 105 | `0120-muyangaa-vaazhkkai-maravan-neeye-04.md` | note names the poet as `ஊன்பொழிப் பசுங்குடையார்` | source note reads `ஊன்பொதிப் பசுங்குடையார்` | `likely-gemini-error` | no | The source form also matches the poet-name form used in the surrounding narrative. File3 changes `பொதிப்` to `பொழிப்`. |
| C05-004 | 123 | 108 | `0123-vandu-vanthathu-enadi-02.md` | File3 begins the page body with the terminal `சென்றனள்!` | source contains an opening prose block before that terminal, beginning `அடுத்தநாள் காலை...` and describing the mother in the kitchen and the daughter carrying out chores before `சென்றாள்/சென்றனள்!` | `missing-whole-lexical-block` | **yes — B05** | Gate B already documented the source-visible opening block omitted by File3 and retained only the locked terminal at the source-supported position. Gate C records the omission without reconstructing the block. |

## C05 closure audit

C05 is an **audit-only closure**.

- source scans **101–125** were inspected against both the direct File3 witness and the preserved canonical lock;
- **4** substantive discrepancy records were entered;
- **0** canonical page records were edited;
- no Gate-B page was reopened;
- no lexical correction was promoted;
- wording state remains **Gemini-lexical-locked / not word-for-word scan verified**.

## Gate C cumulative state after C05

- completed Gate-C batches: **C01–C05**
- audited scans: **125/497**
- cumulative substantive discrepancy records: **36**
- remaining scans: **372**
- next frontier: **scan 126**
- Gate C2: **NOT STARTED / NOT AUTHORIZED**

## Exact next activity

Process **Gate C C06 — scans 126–150**.

Available direct source pair:
- user-supplied `TVA_BOK_0042551_சங்கத்_தமிழ்_part_003_pages_101-150.pdf`, split pages **26–50** / physical scans **126–150**;
- user-supplied `File3.md`, Pages **126–150**.

At C06 close:
1. append only substantive lexical discrepancies to this ledger;
2. verify **0 canonical page files changed**;
3. advance the Gate-C frontier to **scan 151**;
4. do not start Gate C2.


# C06 — scans 126–150

**Status: COMPLETE / PASS — CLEAN BATCH**

- date: **2026-09-16**
- audited scans: **126–150 / 25**
- controlling source: user-supplied `TVA_BOK_0042551_சங்கத்_தமிழ்_part_003_pages_101-150.pdf`, split pages **26–50**
- direct Gemini lexical witness: user-supplied `File3.md`, Pages **126–150**
- locked comparison layer: current canonical page records under `works/sangatamil/pages/`
- substantive discrepancy records: **0**
- scans containing discrepancies: **0**
- scans with no new substantive lexical discrepancy: **25**
- canonical page files changed: **0**
- Gate C2 corrections: **0**

Clean scans:

**126–150**

Special handling:
- scans **128, 132, 138** are full-page illustrations and contain no literary body text;
- scan **143** is a two-page physical spread preserved as one canonical physical record;
- known File3 extraction debris already excluded during Gate B was rechecked and not promoted into Gate C:
  - scan **130** stray numeric `6` in `வலவன் =6`;
  - scan **131** stray title token `மு`;
  - scan **137** malformed heading extraction `அதில் ... தி ... வி`;
  - scan **143** stray `A...` and malformed `மேமதிலி`;
- placement-only differences controlled by the PDF, including scan **149** `மன்னன்!` placement and scan **150** physical boundary at `பட்டமும்`, are structural rather than lexical discrepancies and were not ledgered;
- punctuation-only, spacing, line-wrap, running-header/footer and structural-placement differences were excluded unless they changed lexical content.

## C06 closure audit

C06 is an **audit-only closure**.

- source scans **126–150** were inspected against the direct File3 witness and preserved canonical lock;
- **0** substantive source/File3 lexical discrepancies were found that meet Gate-C ledger criteria;
- **0** canonical page records were edited;
- no Gate-B page was reopened;
- no lexical correction was promoted;
- wording state remains **Gemini-lexical-locked / not word-for-word scan verified**.

## Gate C cumulative state after C06

- completed Gate-C batches: **C01–C06**
- audited scans: **150/497**
- cumulative substantive discrepancy records: **36**
- remaining scans: **347**
- next frontier: **scan 151**
- Gate C2: **NOT STARTED / NOT AUTHORIZED**

## Exact next activity

Process **Gate C C07 — scans 151–175**.

Required source pair:
- controlling PDF covering physical scans **151–175**;
- matching direct Gemini lexical witness `File4.md` when available; otherwise current canonical wording remains the preserved Gemini-lock comparison layer.

At C07 close:
1. append only substantive lexical discrepancies to this ledger;
2. verify **0 canonical page files changed**;
3. advance the Gate-C frontier to **scan 176**;
4. do not start Gate C2.


# C07 — scans 151–175

**Status: COMPLETE / PASS**

- date: **2026-09-16**
- audited scans: **151–175 / 25**
- controlling source: user-supplied `TVA_BOK_0042551_சங்கத்_தமிழ்_part_004_pages_151-200.pdf`, split pages **1–25**
- direct Gemini lexical witness: user-supplied `File4.md`, mapped material for physical scans **151–175**
- locked comparison layer: current canonical page records under `works/sangatamil/pages/`
- substantive discrepancy records: **4**
- scans containing discrepancies: **4**
- scans with no new substantive lexical discrepancy: **21**
- canonical page files changed: **0**
- Gate C2 corrections: **0**

Clean / no-new-substantive-discrepancy scans:

**151–162, 164, 166–173**

Special handling:
- scans **156, 160, 166, 172** are full-page illustrations and contain no literary body text;
- known File4 extraction debris already excluded during Gate B — scan 151 duplicate fragment `மேருமை`, scan 155 stray `64`, scan 157 embedded printed-page number `144`, scan 158 stray numeric `6`, scan 167 terminal punctuation contamination, and scan 174 stray numeric `6` — was not re-entered as Gate-C lexical discrepancy;
- source-controlled placement differences, including displaced carryovers and quotation/provenance/gloss ordering, remain structural and were not ledgered;
- scan **175** crosses File4's phase wrapper: its source page is physical scan 175 / printed page 162, while the matching lexical material begins in File4's following phase block. The malformed decorative-heading extraction was audited against the source-visible title rather than treated as a physical-page remap;
- punctuation-only, spacing, line-wrap, running-header/footer and purely structural differences were excluded unless they changed lexical content.

## C07 discrepancy records

| ID | Scan | Printed page | Canonical page | Locked File4 / repository wording | Source-visible wording | Classification | Gate-B exception already documented? | Notes |
|---|---:|---:|---|---|---|---|---|---|
| C07-001 | 163 | 150 | `0163-pathilai-neruppaaga-umizhndha-paavaanar-05.md` | `கொங்கர்க் குடகடல் ஓடிய ஞான்றைத்` | `கொங்கர்க் குடகடல் ஓட்டிய ஞான்றைத்` | `likely-gemini-error` | no | In the Purananuru 130 quotation, File4 drops the `ட்ட` reading present in the printed source. The canonical locked quotation remains unchanged. |
| C07-002 | 165 | 152 | `0165-kaavaippor-kanduvandha-kanavan-01.md` | body heading `காடைப் போர் இகண்டுவந்த கணவன்!` | decorative/source heading `காடைப் போர் கண்டுவந்த கணவன்!` | `likely-gemini-error` | **yes — B07** | Gate B already preserved the source section identity in metadata while retaining File4's extra initial `இ` in the body heading. Gate C records the lexical disagreement only. |
| C07-003 | 174 | 161 | `0174-thagadooraan-thandha-kani-04.md` | `சிறுயிலை நெல்லித் தீங்கனி குறியாது` | `சிறியிலை நெல்லித் தீங்கனி குறியாது` | `likely-gemini-error` | no | The Purananuru quotation visibly reads `சிறியிலை`; File4 locks `சிறுயிலை`. No source correction is promoted under the current lock. |
| C07-004 | 175 | 162 | `0175-neermagal-neerinum-kulirndha-nenjam-01.md` | File4 decorative-heading extraction is malformed as `நிலமலை / லம் / நீரினும் / குளிர்ந்த / நெஞ்சம்!)`; canonical body therefore contains no recovered heading | source decorative heading `நீர்மகள் நீரினும் குளிர்ந்த நெஞ்சம்!` | `missing-or-malformed-heading-lexical-block` | **yes — B07** | Gate B recorded the source section identity only in metadata and explicitly deferred lexical resolution. Gate C records the missing/malformed heading without inserting source wording into the canonical body. |

## C07 closure audit

C07 is an **audit-only closure**.

- source scans **151–175** were inspected against the direct File4 witness and preserved canonical lock;
- **4** substantive discrepancy records were entered;
- **0** canonical page records were edited;
- no Gate-B page was reopened;
- no lexical correction was promoted;
- wording state remains **Gemini-lexical-locked / not word-for-word scan verified**.

## Gate C cumulative state after C07

- completed Gate-C batches: **C01–C07**
- audited scans: **175/497**
- cumulative substantive discrepancy records: **40**
- remaining scans: **322**
- next frontier: **scan 176**
- Gate C2: **NOT STARTED / NOT AUTHORIZED**

## Exact next activity

Process **Gate C C08 — scans 176–200**.

Available direct source pair:
- user-supplied `TVA_BOK_0042551_சங்கத்_தமிழ்_part_004_pages_151-200.pdf`, split pages **26–50** / physical scans **176–200**;
- user-supplied `File4.md`, matching continuation material for scans **176–200**.

At C08 close:
1. append only substantive lexical discrepancies to this ledger;
2. verify **0 canonical page files changed**;
3. advance the Gate-C frontier to **scan 201**;
4. do not start Gate C2.


# C08 — scans 176–200

**Status: COMPLETE / PASS**

- date: **2026-09-16**
- audited scans: **176–200 / 25**
- controlling source: user-supplied `TVA_BOK_0042551_சங்கத்_தமிழ்_part_004_pages_151-200.pdf`, split pages **26–50**
- direct Gemini lexical witness: user-supplied `File4.md`, matching continuation material for physical scans **176–200**
- locked comparison layer: current canonical page records under `works/sangatamil/pages/`
- substantive discrepancy records: **7**
- scans containing discrepancies: **5**
- scans with no new substantive lexical discrepancy: **20**
- canonical page files changed: **0**
- Gate C2 corrections: **0**

Clean / no-new-substantive-discrepancy scans:

**176–179, 181–187, 189–191, 193–194, 196–198, 200**

Special handling:
- scans **176, 184, 190, 194, 200** are full-page illustrations and contain no literary body text;
- known File4 extraction debris already excluded during Gate B — scan 177 numeric `10000`, scan 178 `CC`, scan 181 numeric `6`, scan 182 numeric `66`, scan 183 bullet/page-furniture debris, scan 185 `2` / `...` / `00` / `64`, scan 188 `கு` / duplicated `ரத்து` / `66`, scan 191 duplicate `66`, scan 192 trailing Markdown `**`, scan 193 duplicate `என்`, scan 195 merged printed page number `182`, and scan 199 merged printed page number `186` — was not re-entered as Gate-C lexical discrepancy;
- scan **197** preserves File4's spaced `என் றூழ்`; this is treated as presentation/segmentation of the source lexical sequence `என்றூழ்`, not as a substantive Gate-C discrepancy;
- punctuation-only, spacing, line-wrap, running-header/footer and purely structural differences were excluded unless they changed lexical content.

## C08 discrepancy records

| ID | Scan | Printed page | Canonical page | Locked File4 / repository wording | Source-visible wording | Classification | Gate-B exception already documented? | Notes |
|---|---:|---:|---|---|---|---|---|---|
| C08-001 | 180 | 167 | `0180-neermagal-neerinum-kulirndha-nenjam-06.md` | quotation `... வானி நீரினும் தீந்தன் சாயலன் ...` | `... வானி நீரினும் தீந்தண் சாயலன் ...` | `likely-gemini-error` | no | File4 changes the final retroflex `ண்` of `தீந்தண்` to dental `ன்`. The immediately following source glossary also explains `தீந்தண் சாயலன்`; canonical quote remains locked. |
| C08-002 | 188 | 175 | `0188-aval-neelamagal-avan-mazhaiyaanan-01.md` | body heading `அவள் நிலமானாள்; அவன் மழையானன்!` | decorative/source heading `அவள் நிலமானாள்; அவன் மழையானான்!` | `likely-gemini-error` | **yes — B08** | Gate B already recorded the metadata/body authority split: source section identity uses `மழையானான்!`, while File4 body locks `மழையானன்!`. |
| C08-003 | 192 | 179 | `0192-aval-neelamagal-avan-mazhaiyaanan-05.md` | `அறிந்திட விருமபாமலே அறிமுகமானோம்!` | `அறிந்திட விரும்பாமலே அறிமுகமானோம்!` | `likely-gemini-error` | no | File4 omits the `்`/consonant sequence needed for source `விரும்பாமலே`, yielding malformed `விருமபாமலே`. |
| C08-004 | 195 | 182 | `0195-aatchiyum-maatchiyum-03.md` | `முடி புனைந்த முத்தோர் மறைந்து; அவர்` | `முடி புனைந்த மூத்தோர் மறைந்து; அவர்` | `likely-gemini-error` | no | The source-visible prose uses `மூத்தோர்`; File4 shortens the long vowel to `முத்தோர்`. The following Sangam quotation also contains `மூத்தோர்`, but Gate C records only the source-visible disagreement on scan 195. |
| C08-005 | 199 | 186 | `0199-parambumalaip-paavendhar-02.md` | `கிழங்களின் குறும்புதான் என்னே...` | `கிழங்குகளின் குறும்புதான் என்னே...` | `likely-gemini-error` | no | File4 drops `ங்கு` from the source-visible `கிழங்குகளின்`; the surrounding sentence continues with `கிழங்கினை வள்ளியென்றே...`. |
| C08-006 | 199 | 186 | `0199-parambumalaip-paavendhar-02.md` | Purananuru 109 quotation `தீஞ்சுனைப் பலவின் பழம்` | `தீஞ்சுளைப் பலவின் பழம்` | `likely-gemini-error` | no | File4 reads `ன` where the printed quotation shows `ள`. No source correction is promoted. |
| C08-007 | 199 | 186 | `0199-parambumalaip-paavendhar-02.md` | `கலைஉளமும் பெற்றதாலே கபிலர்க்கு உயிரே ஆனான்` | `கலைவளமும் பெற்றதாலே கபிலர்க்கு உயிரே ஆனான்` | `likely-gemini-error` | no | The source-visible parallel sequence is `மலைவளமும் மனவளமும் ... கலைவளமும்`; File4 drops the `வ` in the final compound. |

## C08 closure audit

C08 is an **audit-only closure**.

- source scans **176–200** were inspected against the direct File4 witness and preserved canonical lock;
- **7** substantive discrepancy records were entered;
- **0** canonical page records were edited;
- no Gate-B page was reopened;
- no lexical correction was promoted;
- wording state remains **Gemini-lexical-locked / not word-for-word scan verified**.

## Gate C cumulative state after C08

- completed Gate-C batches: **C01–C08**
- audited scans: **200/497**
- cumulative substantive discrepancy records: **47**
- remaining scans: **297**
- next frontier: **scan 201**
- Gate C2: **NOT STARTED / NOT AUTHORIZED**

## Exact next activity

Process **Gate C C09 — scans 201–225**.

Required source pair:
- controlling PDF covering physical scans **201–225**;
- matching direct Gemini lexical witness `File5.md` when available; otherwise current canonical wording remains the preserved Gemini-lock comparison layer.

At C09 close:
1. append only substantive lexical discrepancies to this ledger;
2. verify **0 canonical page files changed**;
3. advance the Gate-C frontier to **scan 226**;
4. do not start Gate C2.


# C09 — scans 201–225

**Status: COMPLETE / PASS**

- date: **2026-09-16**
- audited scans: **201–225 / 25**
- controlling source: user-supplied `TVA_BOK_0042551_சங்கத்_தமிழ்_part_005_pages_201-250.pdf`, split pages **1–25**
- direct Gemini lexical witness: user-supplied `File5.md`, Book Pages **188–212**
- locked comparison layer: current canonical page records under `works/sangatamil/pages/`
- substantive discrepancy records: **3**
- scans containing discrepancies: **3**
- scans with no new substantive lexical discrepancy: **22**
- canonical page files changed: **0**
- Gate C2 corrections: **0**

Clean / no-new-substantive-discrepancy scans:

**201–207, 209–220, 222, 224–225**

Special handling:
- scans **204, 210, 216, 220, 224** are full-page illustrations and contain no literary body text;
- known File5 extraction debris already excluded during Gate B — scan 203 numeric `000008`, scan 206 numeric `66`, scan 213 numeric `66`, scan 214 numeric `66`, scan 219 extraction marker `⚬` plus merged printed page number `206`, scan 222 numeric `66`, and scan 223 merged printed page number `210` — was not re-entered as Gate-C lexical discrepancy;
- structural carryover placement and verse/provenance/gloss lineation remain PDF-controlled and were not treated as lexical differences;
- punctuation-only, spacing, line-wrap, running-header/footer and purely structural differences were excluded unless they changed lexical content.

## C09 discrepancy records

| ID | Scan | Printed page | Canonical page | Locked File5 / repository wording | Source-visible wording | Classification | Gate-B exception already documented? | Notes |
|---|---:|---:|---|---|---|---|---|---|
| C09-001 | 208 | 195 | `0208-kaaviri-naadan-karikaalan-01.md` | body heading `காவிரிநாடன் / கபிகாலன்!` | decorative/source heading `காவிரிநாடன் கரிகாலன்!` | `likely-gemini-error` | **yes — B09** | Gate B already preserved the source section identity in metadata while retaining File5's `கபிகாலன்!` in the body heading. Gate C records the lexical title disagreement only. |
| C09-002 | 221 | 208 | `0221-porthisai-nokkiya-pulippoththu-04.md` | Purananuru 284 quotation `தனக்கு இரித்தானைப் பெயர்புறம் நகுமே` | `தனக்கு இரிந்தானைப் பெயர்புறம் நகுமே` | `likely-gemini-error` | no | The source-visible quotation uses `இரிந்தானைப்`; the same printed page's glossary explains `இரிந்தான் = அஞ்சி ஓடியவன்`. File5 instead locks `இரித்தானைப்`. |
| C09-003 | 223 | 210 | `0223-ingae-vendaam-thangai-irukkindraal-02.md` | displaced locked carryover `எனை` | source-visible carryover `ஏனோ` before `நாணம் வந்து தடுப்பதாலே` | `likely-gemini-error` | **yes — B09** | Gate B explicitly recorded that File5's `எனை` differs from the scan and preserved it under the lexical lock. Gate C resolves the visible source reading for the discrepancy ledger only; canonical wording is not changed. |

## C09 closure audit

C09 is an **audit-only closure**.

- source scans **201–225** were inspected against the direct File5 witness and preserved canonical lock;
- **3** substantive discrepancy records were entered;
- **0** canonical page records were edited;
- no Gate-B page was reopened;
- no lexical correction was promoted;
- wording state remains **Gemini-lexical-locked / not word-for-word scan verified**.

## Gate C cumulative state after C09

- completed Gate-C batches: **C01–C09**
- audited scans: **225/497**
- cumulative substantive discrepancy records: **50**
- remaining scans: **272**
- next frontier: **scan 226**
- Gate C2: **NOT STARTED / NOT AUTHORIZED**

## Exact next activity

Process **Gate C C10 — scans 226–250**.

Available direct source pair:
- user-supplied `TVA_BOK_0042551_சங்கத்_தமிழ்_part_005_pages_201-250.pdf`, split pages **26–50** / physical scans **226–250**;
- user-supplied `File5.md`, Phase 13 / Book Pages **213–237**.

At C10 close:
1. append only substantive lexical discrepancies to this ledger;
2. verify **0 canonical page files changed**;
3. advance the Gate-C frontier to **scan 251**;
4. do not start Gate C2.


# C10 — scans 226–250

**Status: COMPLETE / PASS**

- date: **2026-09-16**
- audited scans: **226–250 / 25**
- controlling source: user-supplied `TVA_BOK_0042551_சங்கத்_தமிழ்_part_005_pages_201-250.pdf`, split pages **26–50**
- direct Gemini lexical witness: user-supplied `File5.md`, Phase 13 / Book Pages **213–237**
- locked comparison layer: current canonical page records under `works/sangatamil/pages/`
- substantive discrepancy records: **5**
- scans containing discrepancies: **5**
- scans with no new substantive lexical discrepancy: **20**
- canonical page files changed: **0**
- Gate C2 corrections: **0**

Clean / no-new-substantive-discrepancy scans:

**227–229, 231–236, 238–239, 241–247, 249–250**

Special handling:
- scans **228, 232, 238, 242, 246, 250** are full-page illustrations and contain no literary body text;
- File5 Phase 13 / Book Pages **213–237** map one-to-one to physical scans **226–250** in this source block;
- known File5 extraction debris already excluded during Gate B — scan 234 extraction bullet markers, scan 239 flattened extraction marker / merged printed-page furniture, scan 240 stray numeric / quote-marker debris, scans 241/243/244 stray `66` or quote-marker debris, and scan 249 stray heading fragment `இ` — was not re-entered as Gate-C lexical discrepancy;
- source-controlled placement and quotation/provenance/gloss structure remain structural rather than lexical;
- scans **240** and **248** contain repository-only lexical omissions where File5 and the source scan agree; these are ledgered without modifying the canonical page records;
- scan **244** locked `அழுவதேனோ` was not ledgered: the earlier provisional source capture `அழுவதேன்` is insufficient by itself to override the direct File5 lock without a clearer visual discrepancy;
- punctuation-only, spacing, line-wrap, running-header/footer and purely structural differences were excluded unless they changed lexical content.

## C10 discrepancy records

| ID | Scan | Printed page | Canonical page | Locked File5 / repository wording | Source-visible / source-aligned wording | Classification | Gate-B exception already documented? | Notes |
|---|---:|---:|---|---|---|---|---|---|
| C10-001 | 226 | 213 | `0226-paari-magalir-paadiya-seyyul-01.md` | decorative body heading `பாபி மகளிர் / பாடிய செய்யுள்` | source section heading `பாரி மகளிர் பாடிய செய்யுள்` | `likely-gemini-error` | **yes — B10** | Gate B already preserved the source section identity in metadata while retaining File5's `பாபி` in the locked body heading. Gate C records the lexical title disagreement only. |
| C10-002 | 230 | 217 | `0230-thaamaraip-poigaiyil-thavazhnthathu-nilavu-01.md` | `அந்துவன் சாத்தனையும் ஆதன் இழிசையையும்` | `அந்துவன் சாத்தனையும் ஆதன் அழிசையையும்` | `likely-gemini-error` | no | The earlier source-aligned physical capture reads `ஆதன் அழிசையையும்`. File5's own later Purananuru quotation on the same section independently has the proper name `ஆதன் அழிசியும்`, supporting the source-name reading and exposing `இழிசையையும்` as the locked error. |
| C10-003 | 237 | 224 | `0237-kaattil-pirantha-kavithai-02.md` | `அன்னத்தின் கூட்டமொன்று ஓடையில படகாகி` | `அன்னத்தின் கூட்டமொன்று ஓடையில் படகாகி` | `likely-gemini-error` | no | The earlier source-aligned physical capture preserves the locative form `ஓடையில்`; File5 drops the terminal `்` and locks `ஓடையில`. No canonical correction is made in Gate C. |
| C10-004 | 240 | 227 | `0240-kaattil-pirantha-kavithai-05.md` | canonical glossary omits the locked continuations `தாவும் தன்மையும் உடைய ஆண் குரங்கு மரணம் உற்றதென்று.` and `கற்றிடாத வலிய குட்டியை சுற்றத்திடம் சேர்த்துவிட்டு.` | File5 and the source scan both contain both continuation lines in `பொருள் விளக்கம்` | `repository-only-divergence` | no | This is not a scan/Gemini disagreement: the direct lexical witness and source agree, but the canonical page record dropped two complete glossary continuation lines. Gate C records the omission only; the page file remains unchanged as required for this audit-only batch. |
| C10-005 | 248 | 235 | `0248-vaalinge-avan-naakkenge-04.md` | canonical glossary omits `வயிறுடைய கிழவி.` and `மாண்டான்.` | File5 and the source scan preserve `வயிறுடைய கிழவி.` after `தாமரைபோல் ஒட்டிய` and `மாண்டான்.` after `படைகண்டு அஞ்சிப் புறங்கொண்டு` | `repository-only-divergence` | no | Two complete glossary continuation lines present in both the locked witness and scan are absent from the canonical page record. Recorded as repository-only divergence; no page wording is changed in Gate C. |

## C10 closure audit

C10 is an **audit-only closure**.

- source scans **226–250** were inspected against the direct File5 witness and preserved canonical lock;
- **5** substantive discrepancy records were entered;
- **0** canonical page records were edited;
- no Gate-B page was reopened;
- no lexical correction was promoted;
- wording state remains **Gemini-lexical-locked / not word-for-word scan verified**.

## Gate C cumulative state after C10

- completed Gate-C batches: **C01–C10**
- audited scans: **250/497**
- cumulative substantive discrepancy records: **55**
- remaining scans: **247**
- next frontier: **scan 251**
- Gate C2: **NOT STARTED / NOT AUTHORIZED**

## Exact next activity

Process **Gate C C11 — scans 251–275**.

Available direct source pair:
- user-supplied `TVA_BOK_0042551_சங்கத்_தமிழ்_part_006_pages_251-300.pdf`, split pages **1–25** / physical scans **251–275**;
- user-supplied `File6.md`, Phase 14 / Book Pages **238–262**.

At C11 close:
1. append only substantive lexical discrepancies to this ledger;
2. verify **0 canonical page files changed**;
3. advance the Gate-C frontier to **scan 276**;
4. do not start Gate C2.


# C11 — scans 251–275

**Status: COMPLETE / PASS**

- date: **2026-09-16**
- audited scans: **251–275 / 25**
- controlling source: user-supplied `TVA_BOK_0042551_சங்கத்_தமிழ்_part_006_pages_251-300.pdf`, split pages **1–25**
- direct Gemini lexical witness: user-supplied `File6.md`, Phase 14 / Book Pages **238–262**
- locked comparison layer: current canonical page records under `works/sangatamil/pages/`
- substantive discrepancy records: **6**
- scans containing discrepancies: **3**
- scans with no new substantive lexical discrepancy: **22**
- canonical page files changed: **0**
- Gate C2 corrections: **0**

Clean / no-new-substantive-discrepancy scans:

**251–253, 255–256, 258–273, 275**

Special handling:
- scans **256, 265, 271, 275** are full-page colour illustrations and contain no source-visible literary body text;
- scan **259** is the two-page illustrated spread carrying text for printed pages **246–247**; File6 folds that material into its Book Page 248 extraction, so the already-closed Gate-B physical mapping was preserved and not treated as a lexical discrepancy;
- known File6 extraction debris already excluded during Gate B — scan 261 numeric `66` / extraction prefix, scan 262 unsupported `பாசறையை!`, scan 264 numeric `66`, scan 267 numeric `66`, scan 273 decorative-heading fragment `வி`, and scan 274 numeric `66` — was not re-entered as Gate-C discrepancy;
- scan **254** contains a repository-only duplicate lexical token: File6 and the source each contain one `இந்தச்`, while the canonical page currently contains it twice;
- scan **257** contains both scan/Gemini lexical disagreements and one repository-only divergence;
- punctuation-only, spacing, line-wrap, running-header/footer and purely structural differences were excluded unless they changed lexical content.

## C11 discrepancy records

| ID | Scan | Printed page | Canonical page | Locked File6 / repository wording | Source-visible / source-aligned wording | Classification | Gate-B exception already documented? | Notes |
|---|---:|---:|---|---|---|---|---|---|
| C11-001 | 254 | 241 | `0254-kuppai-kozhiyaar-01.md` | canonical body contains `இந்தச்` twice: once as a standalone line and again after `சிற்றூர் முதல் பேரூர் நகரங்கள் வரை -` | File6 contains one displaced `இந்தச்`; the source contains one `இந்தச்` after `சிற்றூர் முதல் பேரூர் நகரங்கள் வரை -` | `repository-only-divergence` | no | Gate C records the duplicated lexical token only. The canonical page is not repaired in this audit-only gate. |
| C11-002 | 257 | 244 | `0257-kuppai-kozhiyaar-04.md` | quotation `காம ஒளிஎரி` | quotation `காம ஒள்ளெரி` | `likely-gemini-error` | **yes — B11** | The source visibly preserves the classical form `ஒள்ளெரி`; File6 changes it to the segmented/altered `ஒளிஎரி`. |
| C11-003 | 257 | 244 | `0257-kuppai-kozhiyaar-04.md` | quotation `என்புஉற நலியினும்` | quotation `என்புற நலியினும்` | `likely-gemini-error` | **yes — B11** | The source prints the compact classical form `என்புற`; File6 splits/changes the lexical form to `என்புஉற`. |
| C11-004 | 257 | 244 | `0257-kuppai-kozhiyaar-04.md` | canonical quotation `பிரித்திடை களையார்` | File6 and source: `பிரித்துஇடை களையார்` | `repository-only-divergence` | no | File6 and the scan agree on `பிரித்துஇடை`; the canonical page drops the `உ`, materially altering the preserved lexical sequence. |
| C11-005 | 257 | 244 | `0257-kuppai-kozhiyaar-04.md` | glossary `காம ஒள்எரி = காமமெனும் ஒளிபொருந்திய தீ.` | glossary `காம ஒள்ளெரி = காமமெனும் ஒளிபொருந்திய தீ.` | `likely-gemini-error` | **yes — B11** | This is the glossary occurrence of the same source term; File6 independently alters it to `ஒள்எரி`. |
| C11-006 | 274 | 262 | `0274-andraikke-oru-kannagi-02.md` | `பொன்மானின் துயர்துடைக்கப் புறப்படுக மன்னா; என்றார்!` | `பொன்மானின் துயர்துடைக்கப் புறப்படுக மன்னு; என்றார்!` | `old-or-uncommon-form` | no | The scan clearly prints `மன்னு`; File6/canonical normalize or alter it to `மன்னா`. Gate C preserves the lock and records the source form only. |

## C11 closure audit

C11 is an **audit-only closure**.

- source scans **251–275** were visually inspected against the direct File6 witness and the preserved canonical lock;
- **6** substantive discrepancy records were entered across **3** scans;
- **0** canonical page records were edited;
- no Gate-B page was reopened;
- no lexical correction was promoted;
- wording state remains **Gemini-lexical-locked / not word-for-word scan verified**.

## Gate C cumulative state after C11

- completed Gate-C batches: **C01–C11**
- audited scans: **275/497**
- cumulative substantive discrepancy records: **61**
- remaining scans: **222**
- next frontier: **scan 276**
- Gate C2: **NOT STARTED / NOT AUTHORIZED**

## Exact next activity

Process **Gate C C12 — scans 276–300**.

Available direct source pair:
- user-supplied `TVA_BOK_0042551_சங்கத்_தமிழ்_part_006_pages_251-300.pdf`, split pages **26–50** / physical scans **276–300**;
- user-supplied `File6.md`, Phase 15 / Book Pages **264–288**.

At C12 close:
1. append only substantive lexical discrepancies to this ledger;
2. verify **0 canonical page files changed**;
3. advance the Gate-C frontier to **scan 301**;
4. do not start Gate C2.


# C12 — scans 276–300

**Status: COMPLETE / PASS**

- date: **2026-09-16**
- audited scans: **276–300 / 25**
- controlling source: user-supplied `TVA_BOK_0042551_சங்கத்_தமிழ்_part_006_pages_251-300.pdf`, split pages **26–50**
- direct Gemini lexical witness: user-supplied `File6.md`, Phase 15 / Book Pages **264–288**
- locked comparison layer: current canonical page records under `works/sangatamil/pages/`
- substantive discrepancy records: **6**
- scans containing discrepancies: **6**
- scans with no new substantive lexical discrepancy: **19**
- canonical page files changed: **0**
- Gate C2 corrections: **0**

Clean / no-new-substantive-discrepancy scans:

**276–280, 282–287, 289, 291, 293, 295, 297–300**

Special handling:
- scans **279, 283, 286, 289, 293, 297** are full-page colour illustrations and contain no source-visible literary body text;
- File6 Phase 15 omits the illustration-only physical pages, so Book Pages **264–288** map across physical scans **276–300** with those six source illustration gaps preserved;
- known File6 extraction debris already excluded during Gate B — scan 281 stray numeric `2`, scan 287 duplicated separator/extraction artefact, scans 288/291 stray numeric `66`, and scan 300 extraction marker / merged printed-page furniture — was not re-entered as Gate-C discrepancy;
- harmless segmentation/spacing differences were excluded, including scan 277 `எ மக்குத்` / `எமக்குத்`, scan 278 `கழா அலின்` / `கழாஅலின்`, scan 284 `மகா அர்அன்ன` / `மகாஅர் அன்ன` (same concatenated character sequence), scan 290 `தெய்வத்தின்சேட்டையெனச்` / `தெய்வத்தின் சேட்டையெனச்`, and scan 294 compound-spacing differences;
- scan **294** is nevertheless substantive because the canonical page drops the lexical/sandhi character `ப்` from source/File6 `ஒல்லையூர்ப் பகுதி`;
- scan **281** and scan **296** each contain a source-visible decorative heading whose locked File6 extraction is materially missing/malformed; each heading is recorded as one lexical-block discrepancy rather than multiple token-level rows;
- punctuation-only, line-wrap, running-header/footer and purely structural differences were excluded unless they materially altered lexical interpretation.

## C12 discrepancy records

| ID | Scan | Printed page | Canonical page | Locked File6 / repository wording | Source-visible / source-aligned wording | Classification | Gate-B exception already documented? | Notes |
|---|---:|---:|---|---|---|---|---|---|
| C12-001 | 281 | 269 | `0281-kilu-kiluppai-vazhangum-kirukiruppu-01.md` | File6/canonical decorative body heading `வழங்கும் / கிறுகிறப்பு!`; File6 also carries stray numeric `2` | source decorative heading `கிலு கிலுப்பை / வழங்கும் / கிறுகிறுப்பு!` | `missing-or-malformed-heading-lexical-block` | **yes — B12** | File6 omits the opening `கிலு கிலுப்பை` and changes `கிறுகிறுப்பு` to `கிறுகிறப்பு`. The numeric `2` is extraction debris and is not itself a lexical record. No source heading is inserted into the canonical body in Gate C. |
| C12-002 | 288 | 276 | `0288-veriyaadum-velan-etharkaaga-01.md` | decorative body heading `இவறியாடும் / வேலன் / எதற்காக?` | source heading `வெறியாடும் / வேலன் / எதற்காக?` | `likely-gemini-error` | **yes — B12** | Metadata already preserves the source section identity while the body retains the File6 lock. Gate C records the initial-word corruption only. |
| C12-003 | 290 | 278 | `0290-veriyaadum-velan-etharkaaga-03.md` | File6 `முறித்துப் போட்டதுபோல் நெளிகின்றாள், வளைகிறாள்!` | source/canonical `முறித்துப் போட்டதுபோல் நெளிகின்றாள், வளைகின்றாள்!` | `likely-gemini-error` | no | File6 shortens the second verb from `வளைகின்றாள்` to `வளைகிறாள்`. The canonical record happens to remain source-aligned; Gate C makes no page edit. |
| C12-004 | 292 | 280 | `0292-ollaiyooril-mullaiyo-01.md` | decorative body heading `ஒல்லையூபில் / முல்லையோ?` | source heading `ஒல்லையூரில் / முல்லையோ?` | `likely-gemini-error` | **yes — B12** | The source place-name contains `ரில்`; File6 corrupts it to `பில்`. Metadata/body authority split remains unchanged. |
| C12-005 | 294 | 282 | `0294-ollaiyooril-mullaiyo-03.md` | canonical `ஒல்லையூர் பகுதி எல்லையிலே` | File6 and source `ஒல்லையூர்ப் பகுதி எல்லையிலே` | `repository-only-divergence` | no | The direct witness and scan agree; the canonical page drops the terminal sandhi `ப்`. Recorded audit-only without repairing the page record. |
| C12-006 | 296 | 284 | `0296-maru-pirappu-undendraal-marakkap-neridumo-01.md` | File6 heading is malformed as `மறு பிறப்பு / உண்டென்றால் / மறக்க ரூ / நேபிடுமோ?`; canonical body intentionally carries no recovered heading | source decorative heading `மறு பிறப்பு / உண்டென்றால் / மறக்க / நேரிடுமோ?` | `missing-or-malformed-heading-lexical-block` | **yes — B12** | Gate B deferred lexical heading resolution rather than source-recovering it. Gate C records the malformed/missing heading block only; canonical body remains unchanged. |

## C12 closure audit

C12 is an **audit-only closure**.

- source scans **276–300** were visually inspected against the direct File6 witness and the preserved canonical layer;
- **6** substantive discrepancy records were entered across **6** scans;
- **0** canonical page records were edited;
- no Gate-B page was reopened;
- no lexical correction was promoted;
- wording state remains **Gemini-lexical-locked / not word-for-word scan verified**.

## Gate C cumulative state after C12

- completed Gate-C batches: **C01–C12**
- audited scans: **300/497**
- cumulative substantive discrepancy records: **67**
- remaining scans: **197**
- next frontier: **scan 301**
- Gate C2: **NOT STARTED / NOT AUTHORIZED**

## Exact next activity

Process **Gate C C13 — scans 301–325**.

Available direct source pair:
- user-supplied `TVA_BOK_0042551_சங்கத்_தமிழ்_part_007_pages_301-350.pdf`, split pages **1–25** / physical scans **301–325**;
- user-supplied `File7.md`, Phase 16 / Book Pages **290–314**.

At C13 close:
1. append only substantive lexical discrepancies to this ledger;
2. verify **0 canonical page files changed**;
3. advance the Gate-C frontier to **scan 326**;
4. do not start Gate C2.


# C13 — scans 301–325

**Status: COMPLETE / PASS**

- date: **2026-09-16**
- audited scans: **301–325 / 25**
- controlling source: user-supplied `TVA_BOK_0042551_சங்கத்_தமிழ்_part_007_pages_301-350.pdf`, split pages **1–25**
- direct Gemini lexical witness: user-supplied `File7.md`, Phase 16 / Book Pages **290–314**
- locked comparison layer: current canonical page records under `works/sangatamil/pages/`
- substantive discrepancy records: **7**
- scans containing discrepancies: **6**
- scans with no new substantive lexical discrepancy: **19**
- canonical page files changed: **0**
- Gate C2 corrections: **0**

Clean / no-new-substantive-discrepancy scans:

**301–303, 305–306, 308, 310–311, 314–320, 322–325**

Special handling:
- scans **301, 305, 311, 315, 319, 325** are full-page colour illustrations and contain no source-visible literary body text;
- File7 Phase 16 omits the illustration-only physical pages, so Book Pages **290–314** map across physical scans **301–325** with those six source illustration gaps preserved;
- known File7 extraction debris already excluded during Gate B — scan 302 numeric `6`, scan 303 heading numeric `2`, scan 306 page-wrapper fragment `ம` / checkbox-like marker, scan 316 page-wrapper fragment `கோன்` / numeric `66`, scan 317 glossary numeric `61`, scan 321 numeric `66`, and scan 323 displaced carryovers — was not re-entered as Gate-C discrepancy unless real lexical content was thereby lost;
- scan **304** contains a repository-only omission: the second line of the File7/source quotation, `தாள் தாமரை தோள் தமனியக் கயமலர்`, is absent from the canonical page;
- scan **307** contains a malformed mixed-script File7 token corresponding to a real source word; the canonical page omits the token because Gate B treated the malformed witness as extraction debris;
- scan **321** contains a File7 omission of the second source-visible `இவ்வாறு`; the canonical page is source-aligned and retains it;
- punctuation-only, spacing, line-wrap, running-header/footer and purely structural differences were excluded unless they materially altered lexical interpretation.

## C13 discrepancy records

| ID | Scan | Printed page | Canonical page | Locked File7 / repository wording | Source-visible / source-aligned wording | Classification | Gate-B exception already documented? | Notes |
|---|---:|---:|---|---|---|---|---|---|
| C13-001 | 304 | 292 | `0304-paripaadal-panmalar-poongaa-02.md` | canonical quotation ends this scan with `ஆயிதழ் உண்கண் அலர் முகத் தாமரை` | File7 and source continue on the same scan with `தாள் தாமரை தோள் தமனியக் கயமலர்` | `repository-only-divergence` | no | The direct witness and scan agree on the complete two-line quotation opening, but the canonical page dropped the second line. Audit-only: no page repair is made here. |
| C13-002 | 307 | 295 | `0307-paripaadal-panmalar-poongaa-05.md` | File7 `யாருக்கும் அடங்காமல் பிOPற்றங்கே!`; canonical omits the malformed token after `யாருக்கும் அடங்காமல்` | source reads `யாருக்கும் அடங்காமல் பிளிறிற்றங்கே!` | `likely-gemini-error` | **yes — B13** | File7's mixed-script corruption replaces a real lexical word. Gate B correctly refused to invent a recovery into the canonical layer; Gate C records the source disagreement without changing the page. |
| C13-003 | 309 | 297 | `0309-murasu-kattilil-mosukeeranar-01.md` | decorative body heading `முரசு கட்டிலில் / மோசுகீானர்!` | source heading `முரசு கட்டிலில் / மோசுகீரனார்!` | `likely-gemini-error` | **yes — B13** | The source poet-name is clear; File7 corrupts the medial letters. Metadata/body authority split remains unchanged. |
| C13-004 | 312 | 300 | `0312-murasu-kattilil-mosukeeranar-04.md` | `குளிர் சாமரம் வீசுகின்ற காட்சி என்னே? என்றர்ந்தார்` | source `குளிர் சாமரம் வீசுகின்ற காட்சி என்னே? என்றுயர்ந்தார்` | `likely-gemini-error` | **yes — B13** | File7 drops the `உய` sequence from the source verb. Canonical remains locked to File7. |
| C13-005 | 312 | 300 | `0312-murasu-kattilil-mosukeeranar-04.md` | `நான் செய்த தொண்டு இஃதெ` | source `நான் செய்த தொண்டு இஃதே` | `likely-gemini-error` | **yes — B13** | File7 shortens the final long-vowel form. Canonical remains unchanged in Gate C. |
| C13-006 | 313 | 301 | `0313-murasu-kattilil-mosukeeranar-05.md` | File7 quotation `அதூவும் சாலும், நற் றமிழ் முழுது அறிதல்;` | source/canonical `அதூவும் சாலும், நற் தமிழ் முழுது அறிதல்;` | `likely-gemini-error` | no | File7 introduces an extra initial `ற` into `தமிழ்`; the canonical page is already source-aligned. No page edit is needed. |
| C13-007 | 321 | 309 | `0321-kal-unda-kaduvan-04.md` | File7 has the first `இவ்வாறு` before the paraphrase but goes directly from the paraphrase ending to `கபிலர் மலை நாட்டுச் செழுமையினை...` | source/canonical contain a second `இவ்வாறு` immediately before `கபிலர் மலை நாட்டுச் செழுமையினை...` | `likely-gemini-error` | no | The second transition word is source-visible but omitted by File7. The canonical page already preserves the source word. |

## C13 closure audit

C13 is an **audit-only closure**.

- source scans **301–325** were visually inspected against the direct File7 witness and the preserved canonical layer;
- **7** substantive discrepancy records were entered across **6** scans;
- **0** canonical page records were edited;
- no Gate-B page was reopened;
- no lexical correction was promoted;
- wording state remains **Gemini-lexical-locked / not word-for-word scan verified**.

## Gate C cumulative state after C13

- completed Gate-C batches: **C01–C13**
- audited scans: **325/497**
- cumulative substantive discrepancy records: **74**
- remaining scans: **172**
- next frontier: **scan 326**
- Gate C2: **NOT STARTED / NOT AUTHORIZED**

## Exact next activity

Process **Gate C C14 — scans 326–350**.

Available direct source pair:
- user-supplied `TVA_BOK_0042551_சங்கத்_தமிழ்_part_007_pages_301-350.pdf`, split pages **26–50** / physical scans **326–350**;
- user-supplied `File7.md`, Phase 16 / Book Pages **314–338**.

At C14 close:
1. append only substantive lexical discrepancies to this ledger;
2. verify **0 canonical page files changed**;
3. advance the Gate-C frontier to **scan 351**;
4. do not start Gate C2.


# C14 — scans 326–350

**Status: COMPLETE / PASS**

- date: **2026-09-16**
- audited scans: **326–350 / 25**
- controlling source: user-supplied `TVA_BOK_0042551_சங்கத்_தமிழ்_part_007_pages_301-350.pdf`, split pages **26–50**
- direct Gemini lexical witness: user-supplied `File7.md`, Phase 16 / Book Pages **314–338**
- locked comparison layer: current canonical page records under `works/sangatamil/pages/`
- substantive discrepancy records: **5**
- scans containing discrepancies: **4**
- scans with no new substantive lexical discrepancy: **21**
- canonical page files changed: **0**
- Gate C2 corrections: **0**

Clean / no-new-substantive-discrepancy scans:

**327, 329–330, 332–339, 341–350**

Special handling:
- scans **329, 335, 339, 343, 349** are full-page colour illustrations and contain no source-visible literary body text;
- File7 Phase 16 omits the illustration-only physical pages, so Book Pages **314–338** map across physical scans **326–350** with those five source illustration gaps preserved;
- known File7 extraction debris already excluded during Gate B — scan 328 Bengali-like wrapper token, scan 331 numeric `66`, scan 334 numeric `66` tokens, scan 340 wrapper fragment `கள`, scan 341 numeric `66` tokens, scan 344 wrapper `吗。。`, scan 346 quotation bullet, and scan 350 wrapper `Po` / numeric `66` — was not entered as Gate-C discrepancy;
- scan **326** was rechecked visually because B14 had treated File7 `என்றார்!` as unsupported extraction. The source visibly contains `என்றார்!`; therefore C14 records its canonical omission as a repository-only divergence. The same scan also confirms source/canonical `ஒலியோ - ஒரு`, where File7 omits `ஒரு`;
- scan **334** was rechecked against the source: the source itself reads `உடன் சென்று துணை நிற்க வேண்டு`, matching File7/canonical. The prior B14 note suggesting a fuller source form is not promoted into Gate C and no discrepancy is recorded;
- scan **340** was rechecked visually because B14 had treated File7 `போரில்` as unsupported. The source visibly contains the lexical token `போரில்` later in the same passage; File7 displaced it, while the canonical page omitted it. C14 records the canonical omission without reopening Gate B;
- punctuation-only, spacing, line-wrap, running-header/footer and purely structural differences were excluded unless they materially altered lexical interpretation.

## C14 discrepancy records

| ID | Scan | Printed page | Canonical page | Locked File7 / repository wording | Source-visible / source-aligned wording | Classification | Gate-B exception already documented? | Notes |
|---|---:|---:|---|---|---|---|---|---|
| C14-001 | 326 | 314 | `0326-oru-kodi-vaazhththuk-kooriduvom-04.md` | File7 contains displaced `என்றார்!`; canonical page omits the token | source visibly contains `என்றார்!` immediately after the quoted `...அதனைப் பருகலாம்` passage | `repository-only-divergence` | **yes — B14, but classified there as extraction debris** | Direct visual recheck shows the token is literary source text, not debris. Gate C records the omission only; canonical wording is not repaired. |
| C14-002 | 326 | 314 | `0326-oru-kodi-vaazhththuk-kooriduvom-04.md` | File7 `கடையும்போது கயிற்றால் எழுகின்ற ஒலியோ / காட்டில் உறுமுகின்ற புலிபோல...` | source/canonical `கடையும்போது கயிற்றால் எழுகின்ற ஒலியோ - ஒரு / காட்டில் உறுமுகின்ற புலிபோல...` | `likely-gemini-error` | no | File7 omits the lexical word `ஒரு`; the canonical page is already source-aligned. |
| C14-003 | 328 | 316 | `0328-veeranai-paadiya-cheran-01.md` | decorative body heading `வானைப் பாடிய / சோன்!` | source decorative heading `வீரனைப் பாடிய / சேரன்!` | `missing-or-malformed-heading-lexical-block` | **yes — B14** | Both lexical components of the decorative heading are corrupted in File7. Metadata preserves the source section identity; body wording remains locked. |
| C14-004 | 331 | 319 | `0331-veeranai-paadiya-cheran-04.md` | `படைக்கலன் தடுக்கும் அவன் கேடயம்தனையும்` | source `படைக்கலன் தடுக்கும் அவன் கேடயத்தினையும்` | `likely-gemini-error` | **yes — B14** | The scan clearly reads `கேடயத்தினையும்`; File7/canonical alter the internal morphology to `கேடயம்தனையும்`. |
| C14-005 | 340 | 328 | `0340-tamil-nenjangal-pootriya-thalaiyalangaanaththaan-03.md` | File7 contains `போரில்` displaced before the quotation; canonical omits it | source visibly contains `போரில்` in the quotation passage after `குருதிநீர் பொங்குகின்ற உலையில் -` | `repository-only-divergence` | **yes — B14, but classified there as extraction debris** | File7 preserves the lexical token but at the wrong position. Gate C records the canonical omission only; no page repair or Gate-B reopen is performed. |

## C14 closure audit

C14 is an **audit-only closure**.

- source scans **326–350** were visually inspected against the direct File7 witness and the preserved canonical layer;
- **5** substantive discrepancy records were entered across **4** scans;
- **0** canonical page records were edited;
- no Gate-B page was reopened;
- no lexical correction was promoted;
- wording state remains **Gemini-lexical-locked / not word-for-word scan verified**.

## Gate C cumulative state after C14

- completed Gate-C batches: **C01–C14**
- audited scans: **350/497**
- cumulative substantive discrepancy records: **79**
- remaining scans: **147**
- next frontier: **scan 351**
- Gate C2: **NOT STARTED / NOT AUTHORIZED**

## Exact next activity

Process **Gate C C15 — scans 351–375**.

Available direct source pair:
- user-supplied `TVA_BOK_0042551_சங்கத்_தமிழ்_part_008_pages_351-400.pdf`, split pages **1–25** / physical scans **351–375**;
- user-supplied `File8.md`, Phase 17 / Book Pages **339–363**.

At C15 close:
1. append only substantive lexical discrepancies to this ledger;
2. verify **0 canonical page files changed**;
3. advance the Gate-C frontier to **scan 376**;
4. do not start Gate C2.


# C15 — scans 351–375

**Status: COMPLETE / PASS**

- date: **2026-09-16**
- audited scans: **351–375 / 25**
- controlling source: user-supplied `TVA_BOK_0042551_சங்கத்_தமிழ்_part_008_pages_351-400.pdf`, split pages **1–25**
- direct Gemini lexical witness: user-supplied `File8.md`, Phase 17 / Book Pages **339–363**
- locked comparison layer: current canonical page records under `works/sangatamil/pages/`
- substantive discrepancy records: **10**
- scans containing discrepancies: **9**
- scans with no new substantive lexical discrepancy: **16**
- canonical page files changed: **0**
- Gate C2 corrections: **0**

Clean / no-new-substantive-discrepancy scans:

**351, 353–358, 362, 365, 367–369, 371–372, 374–375**

Special handling:
- full-page illustration scans: **353, 356, 365, 368, 371, 375**;
- mixed text/illustration scans: **358, 359**; scan **359** remains text-bearing and must not regress to illustration-only;
- File8 page 348 collapses wording physically distributed across scans **358–360**; C15 therefore used the PDF only to resolve physical placement while preserving File8 as the locked lexical witness;
- scan **352** confirms the source decorative heading includes `மங்கை`, while File8/canonical body heading omits it;
- scan **363** confirms the source glossary expands `இத்திப் புகர்படு நீழல்` as `இத்தி மரத்தின் புள்ளிகள் பொருந்திய நிழல்`; File8/canonical omit the second `இத்தி` after the equals sign;
- harmless spacing/segmentation differences were excluded, including scan 363 source `கெடாத கள்` vs locked `கெடாதகள்`;
- scan **366** was rechecked visually: source `சாய்ந்திடிலோ` agrees with the locked layer, so only the differing `கொங்கையிலே` / `கொங்கையினை` reading is recorded;
- punctuation-only, line-wrap, running-header/footer and purely structural differences were excluded unless they materially altered lexical interpretation.

## C15 discrepancy records

| ID | Scan | Printed page | Canonical page | Locked File8 / repository wording | Source-visible / source-aligned wording | Classification | Gate-B exception already documented? | Notes |
|---|---:|---:|---|---|---|---|---|---|
| C15-001 | 352 | 340 | `0352-mangai-kanda-magizhchi-01.md` | File8/canonical body heading `கண்ட மகிழ்ச்சி!` | source decorative heading `மங்கை கண்ட மகிழ்ச்சி!` | `missing-or-malformed-heading-lexical-block` | **yes — B15** | File8 omits the opening lexical word `மங்கை`. Metadata preserves the source section identity; canonical body remains unchanged. |
| C15-002 | 359 | unnumbered | `0359-saanru-koorum-sariththira-varigal-illustration.md` | `குடவோலை முறையினாலே - நன்கு` | source `குடவோலை முறையினிலே - நன்கு` | `likely-gemini-error` | **yes — B15** | The visible source has `முறையினிலே`; File8/canonical use `முறையினாலே`. |
| C15-003 | 360 | 348 | `0360-saanru-koorum-sariththira-varigal-03.md` | `தான் கடந்து செலஇருந்த தடங் குறித்துத்` | source `தான் கடந்து செல்லிருந்த தடங் குறித்துத்` | `likely-gemini-error` | **yes — B15** | File8 splits/corrupts the verb form as `செலஇருந்த`; direct visual inspection shows `செல்லிருந்த`. |
| C15-004 | 361 | 349 | `0361-saanru-koorum-sariththira-varigal-04.md` | `விரோதிகளை வீழ்த்துக்கின்ற சேரமானின் தளபதியாம்` | source `விரோதிகளை வீழ்த்துகின்ற சேரமானின் தளபதியாம்` | `likely-gemini-error` | **yes — B15** | File8/canonical insert `க்` into the verb form; source reads `வீழ்த்துகின்ற`. |
| C15-005 | 363 | 351 | `0363-saanru-koorum-sariththira-varigal-06.md` | `இத்திப் புகர்படு நீழல் = மரத்தின் புள்ளிகள் பொருந்திய நிழல்` | source `இத்திப் புகர்படு நீழல் = இத்தி மரத்தின் புள்ளிகள் பொருந்திய நிழல்` | `likely-gemini-error` | **yes — B15** | File8/canonical omit the second lexical `இத்தி` in the gloss definition. Gate C records the omission only. |
| C15-006 | 364 | 352 | `0364-parisappanam-vendaam-parisupporul-idho-01.md` | `சற்று முகம் சுளீப்பீர்!` | source `சற்று முகம் சுளிப்பீர்!` | `likely-gemini-error` | **yes — B15** | File8/canonical introduce an extra long-vowel sign in the verb. |
| C15-007 | 366 | 354 | `0366-parisappanam-vendaam-parisupporul-idho-03.md` | `கொஞ்சி மகிழும் குமரியின் கொங்கையினை அவள் காதலன்;` | source `கொஞ்சி மகிழும் குமரியின் கொங்கையிலே அவள் காதலன்;` | `likely-gemini-error` | **yes — B15** | The source locative form is `கொங்கையிலே`; File8/canonical substitute `கொங்கையினை`. |
| C15-008 | 370 | 358 | `0370-kankanda-saatchi-undo-01.md` | `கணப்பொழுதும் அகலாதிரு கண்ணா என;` | source `கணப்பொழுதும் அகலாதிரு கண்ணே என;` | `likely-gemini-error` | **yes — B15** | Direct source inspection confirms vocative `கண்ணே`, not locked `கண்ணா`. |
| C15-009 | 370 | 358 | `0370-kankanda-saatchi-undo-01.md` | `ஓருயிராய் நாங்களாகி உலகத்தை மறந்ததும் பொய்யா?` | source `ஒருயிராய் நாங்களாகி உலகத்தை மறந்ததும் பொய்யா?` | `likely-gemini-error` | **yes — B15** | File8/canonical lengthen the initial vowel; source reads short-vowel `ஒருயிராய்`. |
| C15-010 | 373 | 361 | `0373-or-uvamai-iru-kaatchi-01.md` | decorative body heading `ஒர் உவமை; இரு காட்சி!` | source decorative heading `ஓர் உவமை; இரு காட்சி!` | `likely-gemini-error` | **yes — B15** | Metadata retains the source identity while the body preserves the File8 lock. |

## C15 closure audit

C15 is an **audit-only closure**.

- source scans **351–375** were visually inspected against the direct File8 witness and the preserved canonical layer;
- **10** substantive discrepancy records were entered across **9** scans;
- **0** canonical page records were edited;
- no Gate-B page was reopened;
- no lexical correction was promoted;
- wording state remains **Gemini-lexical-locked / not word-for-word scan verified**.

## Gate C cumulative state after C15

- completed Gate-C batches: **C01–C15**
- audited scans: **375/497**
- cumulative substantive discrepancy records: **89**
- remaining scans: **122**
- next frontier: **scan 376**
- Gate C2: **NOT STARTED / NOT AUTHORIZED**

## Exact next activity

Process **Gate C C16 — scans 376–400**.

Available direct source pair:
- user-supplied `TVA_BOK_0042551_சங்கத்_தமிழ்_part_008_pages_351-400.pdf`, split pages **26–50** / physical scans **376–400**;
- user-supplied `File8.md`, Book Pages **364–388**.

At C16 close:
1. append only substantive lexical discrepancies to this ledger;
2. verify **0 canonical page files changed**;
3. advance the Gate-C frontier to **scan 401**;
4. do not start Gate C2.


# C16 — scans 376–400

**Status: COMPLETE / PASS**

- date: **2026-09-16**
- audited scans: **376–400 / 25**
- controlling source: user-supplied `TVA_BOK_0042551_சங்கத்_தமிழ்_part_008_pages_351-400.pdf`, split pages **26–50**
- direct Gemini lexical witness: user-supplied `File8.md`, Book Pages **364–388**
- locked comparison layer: current canonical page records under `works/sangatamil/pages/`
- substantive discrepancy records: **3**
- scans containing discrepancies: **2**
- scans with no new substantive lexical discrepancy: **23**
- canonical page files changed: **0**
- Gate C2 corrections: **0**

Clean / no-new-substantive-discrepancy scans:

**376, 378–382, 384–400**

Special handling:
- full-page illustration scans: **378, 381, 385, 388, 391, 394, 397, 400**;
- scan **382** retains the Gate-B decision that File8-only `நும் காதல்` is unsupported extraction debris; it is not entered as a source discrepancy because the canonical layer correctly excludes it;
- scan **379** source/File8 differences around `ஊன் செத்துப்` are spacing/segmentation only and are excluded from Gate C;
- scan **383** was rechecked at high resolution. The source narrative reads `நீண்ட அறிவுரைகளே நீட்டி முழக்குகின்றாய்!`, while File8/canonical use `அறிவுரைகளை`. In the Kuruntokai quotation the source reads `நுங்குறை ஆகம் நிறுக்கல்...`; File8/canonical quote uses `நும்குறை`, while `நிறுக்கல்` itself agrees with the source and is not a discrepancy;
- scan **389** source glossary `உடைபெரும் செல்வர்` agrees with File8/canonical;
- scan **395** File8 `இரும்பாலா` remains unsupported extraction debris, while source/File8 `இறந் தோரே` is not treated as substantive because the difference is only spacing/segmentation;
- scan **396** source `திசிர ஆதி` vs locked `திசிரஆதி` is spacing only and is excluded;
- punctuation-only, line-wrap, running-header/footer and purely structural differences were excluded unless they materially altered lexical interpretation.

## C16 discrepancy records

| ID | Scan | Printed page | Canonical page | Locked File8 / repository wording | Source-visible / source-aligned wording | Classification | Gate-B exception already documented? | Notes |
|---|---:|---:|---|---|---|---|---|---|
| C16-001 | 377 | 365 | `0377-uchchikkuch-sendra-nocchi-01.md` | `அகன்ற வாய்ப் பருந்துக்களும் வட்டமிட்டுச் சூழ்ந்தபோது;` | source `அகன்ற வாய்ப் பருந்துகளும் வட்டமிட்டுச் சூழ்ந்தபோது;` | `likely-gemini-error` | **yes — B16** | File8/canonical insert an extra `க்` in `பருந்துக்களும்`; direct visual inspection shows source `பருந்துகளும்`. |
| C16-002 | 383 | 371 | `0383-paaraiyil-urugudhu-pasu-venney-04.md` | `நீண்ட அறிவுரைகளை நீட்டி முழக்குகின்றாய்!` | source `நீண்ட அறிவுரைகளே நீட்டி முழக்குகின்றாய்!` | `likely-gemini-error` | **yes — B16** | The source has emphatic `அறிவுரைகளே`; File8/canonical use accusative `அறிவுரைகளை`. |
| C16-003 | 383 | 371 | `0383-paaraiyil-urugudhu-pasu-venney-04.md` | quotation `இடிக்கும் கேளிர்! நும்குறை ஆகம் நிறுக்கல்...` | source quotation `இடிக்கும் கேளிர்! நுங்குறை ஆகம் நிறுக்கல்...` | `likely-gemini-error` | **yes — B16** | Source and the page glossary support `நுங்குறை`; only the locked quotation uses `நும்குறை`. `நிறுக்கல்` is source-supported and is not separately logged. |

## C16 closure audit

C16 is an **audit-only closure**.

- source scans **376–400** were visually inspected against the direct File8 witness and the preserved canonical layer;
- **3** substantive discrepancy records were entered across **2** scans;
- **0** canonical page records were edited;
- no Gate-B page was reopened;
- no lexical correction was promoted;
- wording state remains **Gemini-lexical-locked / not word-for-word scan verified**.

## Gate C cumulative state after C16

- completed Gate-C batches: **C01–C16**
- audited scans: **400/497**
- cumulative substantive discrepancy records: **92**
- remaining scans: **97**
- next frontier: **scan 401**
- Gate C2: **NOT STARTED / NOT AUTHORIZED**

## Exact next activity

Process **Gate C C17 — scans 401–425**.

Available direct source pair:
- user-supplied `TVA_BOK_0042551_சங்கத்_தமிழ்_part_009_pages_401-450.pdf`, split pages **1–25** / physical scans **401–425**;
- user-supplied `File9.md`, Phase 19 / Book Pages **389–413**.

Important carry-forward:
- scans **413–424** have a documented File9 segmentation/replacement anomaly; do not fabricate a one-to-one lexical mapping. Audit source-visible text against the preserved repository layer and record only demonstrable substantive discrepancies.

At C17 close:
1. append only substantive lexical discrepancies to this ledger;
2. verify **0 canonical page files changed**;
3. advance the Gate-C frontier to **scan 426**;
4. do not start Gate C2.


# C17 — scans 401–425

**Status: COMPLETE / PASS**

- date: **2026-09-16**
- audited scans: **401–425 / 25**
- controlling source: user-supplied `TVA_BOK_0042551_சங்கத்_தமிழ்_part_009_pages_401-450.pdf`, split pages **1–25**
- direct Gemini lexical witness: user-supplied `File9.md`, Phase 19 / Book Pages **389–413**, only where the File9 block is demonstrably reliable
- locked comparison layer: current canonical page records under `works/sangatamil/pages/`
- substantive discrepancy records: **8**
- scans containing discrepancies: **7**
- scans with no new substantive lexical discrepancy: **18**
- canonical page files changed: **0**
- Gate C2 corrections: **0**

Clean / no-new-substantive-discrepancy scans:

**401, 403, 405–409, 411–412, 414–419, 423–425**

Special handling:
- full-page illustration scans: **403, 407, 411, 415, 419, 423**;
- scan **425** is a decorative divider and visibly reads `ஒருதலைக் காதல்`; the canonical divider wording agrees;
- scans **413–424** retain the durable File9 segmentation/replacement anomaly documented in B17. No synthetic one-to-one File9 mapping was created. For those scans, C17 compared the source scan directly against the preserved repository layer and recorded only demonstrable lexical divergences;
- scan **402** source visibly contains an additional `உன்` after `கண்ணா!`; File9/canonical omit it;
- scan **404** was rechecked at high resolution. Source `போல்` agrees with File9/canonical; the earlier B17 note suggesting a visible-source alternative for `போல்` is not promoted into Gate C. Source `அருகில்`, however, differs from locked `கருகில்` and is recorded;
- scan **406** File9 mixed-script corruption around `காயமுற்றோர்க்கு` remains extraction debris; canonical/source usable Tamil agrees;
- scan **410** File9 duplicated fragment `னார்` remains extraction debris and is not recorded. The substantive source/lock difference is `கொலையேறு` vs `கொலைஏறு`;
- punctuation-only, spacing-only, line-wrap, running-header/footer and purely structural differences were excluded unless they materially altered lexical interpretation.

## C17 discrepancy records

| ID | Scan | Printed page | Canonical page | Locked File9 / repository wording | Source-visible / source-aligned wording | Classification | Gate-B exception already documented? | Notes |
|---|---:|---:|---|---|---|---|---|---|
| C17-001 | 402 | 390 | `0402-nenjam-inikkiradhu-thanjam-pugath-thudikkiradhu-01.md` | `வஞ்சமின்றி வழங்கிடுவேன் உனக்காகக் கண்ணா!` followed directly by `மஞ்சத்து மயிலாக...` | source `வஞ்சமின்றி வழங்கிடுவேன் உனக்காகக் கண்ணா! - உன் / மஞ்சத்து மயிலாக...` | `likely-gemini-error` | **yes — B17** | File9/canonical omit the lexical token `உன்`. |
| C17-002 | 404 | 392 | `0404-nenjam-inikkiradhu-thanjam-pugath-thudikkiradhu-03.md` | `கருகில் வரமுடியாமல் ஏங்கத்தான் வேண்டும்!` | source `அருகில் வரமுடியாமல் ஏங்கத்தான் வேண்டும்!` | `likely-gemini-error` | **yes — B17** | High-resolution source recheck confirms `அருகில்`. Source `போல்` elsewhere on the same page agrees with the locked layer and is not logged. |
| C17-003 | 410 | 398 | `0410-aayamaghan-kuzhaloodhinaan-02.md` | `முலைவேதின் ஒற்றி முயங்கிப் பொதிவேம் / கொலைஏறு சாடிய புண்ணை......` | source `முலைவேதின் ஒற்றி முயங்கிப் பொதிவேம் / கொலையேறு சாடிய புண்ணை......` | `likely-gemini-error` | **yes — B17** | This is a substantive sandhi/spelling difference, not mere whitespace. |
| C17-004 | 413 | 401 | `0413-solven-keladi-thozhi-01.md` | `மாயமாய் வந்து அவைகளப் பறிப்பான்!` | source `மாயமாய் வந்து அவைகளைப் பறிப்பான்!` | `repository-only-divergence` | **B17 anomaly range** | File9 has no reliable one-to-one block for this physical scan; direct source/repository comparison shows the missing `ை` in the canonical wording. |
| C17-005 | 413 | 401 | `0413-solven-keladi-thozhi-01.md` | `தாயும் ஏன அருந்துவதற்கு “மகனே” என்றாள்!` | source `தாயும் எனை அருகழைத்து “மகளே” என்றாள்!` | `repository-only-divergence` | **B17 anomaly range** | Direct visual recheck shows a materially corrupted canonical phrase across multiple lexical tokens. |
| C17-006 | 420 | 408 | `0420-iruvizhi-mazhaiyum-idhaya-magizhvvum-04.md` | `களிமிகுந்து பந்தாடிப் பழவிகளிடப் பஞ்சராகிக்` | source `களிறுகளைப் பந்தாடிப் புரவிகளைப் பஞ்சராக்கிக்` | `repository-only-divergence` | **B17 anomaly range** | The entire lexical line is materially corrupted in the preservation layer; no repair is made at Gate C. |
| C17-007 | 421 | 409 | `0421-inba-vilakkettra-eppodhu-varuvaaro-01.md` | `கார் காலம் திலைகாட்டத் தொடங்கு முன்னர்` | source `கார் காலம் தலைகாட்டத் தொடங்கு முன்னர்` | `repository-only-divergence` | **B17 anomaly range** | Direct source/repository comparison confirms `தலைகாட்டத்`. |
| C17-008 | 422 | 410 | `0422-inba-vilakkettra-eppodhu-varuvaaro-02.md` | `புத்திட்ட முல்லையிலே அமர்ந்து தேன் மொண்டு,` | source `பூத்திட்ட முல்லையிலே அமர்ந்து தேன் மொண்டு,` | `repository-only-divergence` | **B17 anomaly range** | Direct source/repository comparison confirms the long-vowel form `பூத்திட்ட`. |

## C17 closure audit

C17 is an **audit-only closure**.

- source scans **401–425** were visually inspected against File9 where reliable and against the preserved repository layer where File9 is anomalous;
- **8** substantive discrepancy records were entered across **7** scans;
- **0** canonical page records were edited;
- no Gate-B page was reopened;
- no lexical correction was promoted;
- wording state remains **Gemini-lexical-locked / not word-for-word scan verified**.

## Gate C cumulative state after C17

- completed Gate-C batches: **C01–C17**
- audited scans: **425/497**
- cumulative substantive discrepancy records: **100**
- remaining scans: **72**
- next frontier: **scan 426**
- Gate C2: **NOT STARTED / NOT AUTHORIZED**

## Exact next activity

Process **Gate C C18 — scans 426–450**.

Available direct source pair:
- user-supplied `TVA_BOK_0042551_சங்கத்_தமிழ்_part_009_pages_401-450.pdf`, split pages **26–50** / physical scans **426–450**;
- user-supplied `File9.md`, Phase 20 only where a reliable block actually exists.

Important carry-forward:
- usable File9 Page **414–425** blocks map to physical scans **426–437**;
- File9 Phase 20 contains **no lexical blocks for physical scans 438–450 / printed pages 426–438** despite its advertised range;
- for scans **438–450**, do not fabricate a lexical mapping. Audit the source scan directly against the preserved repository layer and record only demonstrable substantive divergences.

At C18 close:
1. append only substantive lexical discrepancies to this ledger;
2. verify **0 canonical page files changed**;
3. advance the Gate-C frontier to **scan 451**;
4. do not start Gate C2.


# C18 — scans 426–450

**Status: COMPLETE / PASS**

- date: **2026-09-16**
- audited scans: **426–450 / 25**
- controlling source: user-supplied `TVA_BOK_0042551_சங்கத்_தமிழ்_part_009_pages_401-450.pdf`, split pages **26–50**
- direct Gemini lexical witness: user-supplied `File9.md`, Phase 20 only where a reliable block actually exists
- reliable File9 mapping: Pages **414–425 → physical scans 426–437**
- scans **438–450**: **no File9 lexical blocks**; audited directly against the preserved repository layer
- substantive discrepancy records: **18**
- scans containing discrepancies: **9**
- scans with no new substantive lexical discrepancy: **16**
- canonical page files changed: **0**
- Gate C2 corrections: **0**

Clean / no-new-substantive-discrepancy scans:

**426–428, 432–433, 437–440, 443–447, 449–450**

Special handling:
- full-page illustration scans: **427, 433, 439, 447**;
- File9 Page **413** remains a carry-forward note only and is not mapped to scan 426;
- usable File9 Pages **414–425** were used only for physical scans **426–437**;
- File9 provides no lexical block for scans **438–450 / printed 426–438**; C18 therefore made no synthetic lock alignment for that tail;
- scan **430** File9 `விரைந்தோடிிட` remains a malformed extraction token; source/canonical usable `விரைந்தோடிட` is retained and no discrepancy is recorded for that defect;
- punctuation-only, spacing-only, line-wrap, running-header/footer and purely structural differences were excluded unless they materially altered lexical interpretation.

## C18 discrepancy records

| ID | Scan | Printed page | Canonical page | Locked File9 / repository wording | Source-visible / source-aligned wording | Classification | Gate-B exception already documented? | Notes |
|---|---:|---:|---|---|---|---|---|---|
| C18-001 | 429 | 417 | `0429-oruthalaik-kaadhal-01-04.md` | `விண்ணில் நட்சத்திரமொன்று வீழ்கின்ற வேகத்தில்` | source `விண்ணில் நட்சத்திரமொன்று விழுகின்ற வேகத்தில்` | `likely-gemini-error` | **yes — B18** | File9/canonical lengthen/alter the verb; direct visual source reads `விழுகின்ற`. |
| C18-002 | 430 | 418 | `0430-oruthalaik-kaadhal-01-05.md` | sequence proceeds from `கட்டிய மனையாள் பேற்று வலியால் பெரிதும்` directly to `சேதி வந்து...` | source includes `துடிப்பதாய்ச்` before `சேதி வந்து...` | `likely-gemini-error` | **yes — B18** | File9/canonical omit the source-visible lexical token `துடிப்பதாய்ச்`. |
| C18-003 | 431 | 419 | `0431-oruthalaik-kaadhal-01-06.md` | `ஊசியினும் வேகமாயப் போரை முடித்து` | source `ஊசியினும் வேகமாய்ப் போரை முடித்து` | `likely-gemini-error` | **yes — B18** | Source has the conjunct form `வேகமாய்ப்`; locked layer has `வேகமாயப்`. |
| C18-004 | 431 | 419 | `0431-oruthalaik-kaadhal-01-06.md` | paragraph begins directly `முத்தமிழ் வித்தகரின் பாமாலைக்கும்...` | source has standalone lexical transition `இவ்வாறு` before that paragraph | `likely-gemini-error` | **yes — B18** | File9/canonical omit source-visible `இவ்வாறு`. |
| C18-005 | 434 | 422 | `0434-oruthalaik-kaadhal-02-03.md` | `சுடுங்காதல் நெருப்பாலே சுவைப்பண்டம் சமைத்து` | source `கடுங்காதல் நெருப்பாலே சுவைப்பண்டம் சமைத்து` | `likely-gemini-error` | **yes — B18** | Direct source inspection confirms initial `கடு-`, not locked `சுடு-`. |
| C18-006 | 435 | 423 | `0435-oruthalaik-kaadhal-02-04.md` | `கடுந்தமிழ்ச் சொல்லாலே இப்பாடல் இயுள்ளேன்.` | source `கடுந்தமிழ்ச் சொல்லாலே இப்பாடல் இயற்றியுள்ளேன்.` | `likely-gemini-error` | **yes — B18** | Locked layer drops the internal `ற்றிய` sequence. |
| C18-007 | 435 | 423 | `0435-oruthalaik-kaadhal-02-04.md` | `வாட்டும் காதல் நிறைவேற வழியொரு சொல்லென்று` | source `வாட்டும் காதல் நிறைவேற வழியொன்று சொல்லென்று` | `likely-gemini-error` | **yes — B18** | Source reads `வழியொன்று`; File9/canonical use `வழியொரு`. |
| C18-008 | 436 | 424 | `0436-oruthalaik-kaadhal-02-05.md` | `“மகளே; நற்கண்ணை!” என்றழைத்துவாறு` | source `“மகளே; நற்கண்ணை!” என்றழைத்தவாறு` | `likely-gemini-error` | **yes — B18** | Locked `து` differs from source `த` in the verb form. |
| C18-009 | 441 | 429 | `0441-oruthalaik-kaadhal-03-03.md` | `“சொல்” என்று கோபம் வருவதற்குள்...` | source `“சுள்” என்று கோபம் வருவதற்குள்...` | `repository-only-divergence` | **B18 no-File9 tail** | The source uses the onomatopoeic `சுள்`; repository substitutes lexical `சொல்`. |
| C18-010 | 441 | 429 | `0441-oruthalaik-kaadhal-03-03.md` | `... உண்மையைச் சொல்லிவிடு” என்றுரைத்தாள்!` | source `... உண்மையைச் சொல்லிவிடு” என்றாள்!` | `repository-only-divergence` | **B18 no-File9 tail** | Repository adds lexical `உரைத்த` not present in source. |
| C18-011 | 441 | 429 | `0441-oruthalaik-kaadhal-03-03.md` | `நன்னுளாம் நாளை விருந்துக்கு வருகின்ற கிள்ளியிடம்` | source `நன்னாளாம் நாளை விருந்துக்கு வருகின்ற கிள்ளியிடம்` | `repository-only-divergence` | **B18 no-File9 tail** | Direct visual source confirms `நன்னாளாம்`. |
| C18-012 | 441 | 429 | `0441-oruthalaik-kaadhal-03-03.md` | `குறித்த நேரம் தவறுமல் ஊர்ச் சேவல் கூவியது!` | source `குறித்த நேரம் தவறாமல் ஊர்ச் சேவல் கூவியது!` | `repository-only-divergence` | **B18 no-File9 tail** | Repository omits the long-vowel sign in `தவறாமல்`. |
| C18-013 | 442 | 430 | `0442-oruthalaik-kaadhal-03-04.md` | `உப்பு மட்டும் போதற்கு மறந்திடாதீர்!` | source `உப்பு மட்டும் போடுதற்கு மறந்திடாதீர்!` | `repository-only-divergence` | **B18 no-File9 tail** | Source contains the full verb form `போடுதற்கு`. |
| C18-014 | 442 | 430 | `0442-oruthalaik-kaadhal-03-04.md` | `காங்குவித்து ஒருவருக்கொருவர் வணக்கம் செய்து` | source `கரங்குவித்து ஒருவருக்கொருவர் வணக்கம் செய்து` | `repository-only-divergence` | **B18 no-File9 tail** | Direct visual source confirms `கரங்குவித்து`. |
| C18-015 | 442 | 430 | `0442-oruthalaik-kaadhal-03-04.md` | `கனிந்த அன்பைப் பாரிமாறிக்கொண்டு` | source `கனிந்த அன்பைப் பரிமாறிக்கொண்டு` | `repository-only-divergence` | **B18 no-File9 tail** | Repository alters the initial vowel/consonant sequence of `பரிமாறிக்கொண்டு`. |
| C18-016 | 442 | 430 | `0442-oruthalaik-kaadhal-03-04.md` | `வேங்கைகளிற் கிள்ளியிடம் விரைந்து வந்தாள் நற்கண்ணை!` | source `வேங்கைநிகர்க் கிள்ளியிடம் விரைந்து வந்தாள் நற்கண்ணை!` | `repository-only-divergence` | **B18 no-File9 tail** | The source has the compound `வேங்கைநிகர்க்`; repository text is materially corrupted. |
| C18-017 | 442 | 430 | `0442-oruthalaik-kaadhal-03-04.md` | `ஒவ்வொருக்கும்போது படித்தால் போதும்!` | source `ஓய்விருக்கும்போது படித்தால் போதும்!` | `repository-only-divergence` | **B18 no-File9 tail** | Direct visual source confirms `ஓய்விருக்கும்போது`. |
| C18-018 | 448 | 436 | `0448-oruthalaik-kaadhal-04-03.md` | `“கருந்தைப் போர் வெல்க!” என்றாள்!` | source `“கரந்தைப் போர் வெல்க!” என்றாள்!` | `repository-only-divergence` | **B18 no-File9 tail** | Source uses the battle-name form `கரந்தை`, consistent with the earlier section wording. |

## C18 closure audit

C18 is an **audit-only closure**.

- source scans **426–450** were visually inspected;
- File9 was used only for reliable mapped scans **426–437**;
- scans **438–450** were audited directly against the source and preserved repository layer because File9 supplies no lexical blocks for that tail;
- **18** substantive discrepancy records were entered across **9** scans;
- **0** canonical page records were edited;
- no Gate-B page was reopened;
- no lexical correction was promoted;
- wording state remains **Gemini-lexical-locked / not word-for-word scan verified**.

## Gate C cumulative state after C18

- completed Gate-C batches: **C01–C18**
- audited scans: **450/497**
- cumulative substantive discrepancy records: **118**
- remaining scans: **47**
- next frontier: **scan 451**
- Gate C2: **NOT STARTED / NOT AUTHORIZED**

## Exact next activity

Process **Gate C C19 — scans 451–475**.

Available direct source pair:
- user-supplied `TVA_BOK_0042551_சங்கத்_தமிழ்_part_010_pages_451-497.pdf`, split pages **1–25** / physical scans **451–475**;
- user-supplied `File10.md` where a reliable lexical block exists.

Mapping / anomaly rules from B19:
- scans **451–461** map to File10 comments **439–449**;
- File10 Page **449** is reliable only through `இனி ஆற்றுவதுதான் எவ்வாறு தோழி?`; its tail is replacement material;
- scan **462 / printed 450** has **no reliable File10 lexical block**;
- scans **463–468** map to File10 comments **450–455**;
- File10 Page **456** is a phantom image marker and must be ignored;
- scans **469–475** map to File10 comments **457–463**;
- do not fabricate lexical alignment for any missing/replaced segment.

At C19 close:
1. append only substantive lexical discrepancies to this ledger;
2. verify **0 canonical page files changed**;
3. advance the Gate-C frontier to **scan 476**;
4. do not start Gate C2.


# C19 — scans 451–475

**Status: COMPLETE / PASS**

- date: **2026-09-16**
- audited scans: **451–475 / 25**
- controlling source: user-supplied `TVA_BOK_0042551_சங்கத்_தமிழ்_part_010_pages_451-497.pdf`, split pages **1–25**
- direct Gemini lexical witness: user-supplied `File10.md`, only where the B19-resolved block is reliable
- substantive discrepancy records: **16**
- scans containing discrepancies: **11**
- scans with no new substantive lexical discrepancy: **14**
- canonical page files changed: **0**
- Gate C2 corrections: **0**

Clean / no-new-substantive-discrepancy scans:

**452–453, 457, 459–462, 464–466, 469, 471, 474–475**

Special handling:
- full-page illustration scans: **453, 457, 465, 471**;
- scans **451–461** were mapped against File10 comments **439–449**;
- File10 Page **449** was used only through `இனி ஆற்றுவதுதான் எவ்வாறு தோழி?`; its replacement-material tail was not used as lexical authority;
- scan **462 / printed 450** has no reliable File10 lexical block and was audited directly against the source/repository preservation layer;
- scans **463–468** were mapped against File10 comments **450–455**;
- File10 Page **456** is a phantom image marker with no corresponding physical scan and was ignored;
- scans **469–475** were mapped against File10 comments **457–463**;
- documented extraction defects such as scan 451 stray `ற`, scan 456 `மிகக்குடிக்குமோ`, scan 460 `புக்பாட்டு`, scan 463 stray `தன்`, and scan 469 `போட்டுடைட்டதேனோ` were not promoted into lexical discrepancy records;
- punctuation-only, spacing-only, line-wrap, running-header/footer and purely structural differences were excluded unless they materially altered lexical interpretation.

## C19 discrepancy records

| ID | Scan | Printed page | Canonical page | Locked File10 / repository wording | Source-visible / source-aligned wording | Classification | Gate-B exception already documented? | Notes |
|---|---:|---:|---|---|---|---|---|---|
| C19-001 | 451 | 439 | `0451-oruthalaik-kaadhal-05-01.md` | `உறையூரின் சோழன் போர்முனைக்குச் செல்லும்போது` | source `உறையூரின் சோழமகன் போர்முனைக்குச் செல்லும்போது` | `likely-gemini-error` | **yes — B19** | File10/canonical omit the lexical component `மகன்` from `சோழமகன்`. |
| C19-002 | 451 | 439 | `0451-oruthalaik-kaadhal-05-01.md` | `அறிவுரை புகன்ற அன்னை, அவனை விட்டகன்றபின்னே` | source `அறிவுரை புகன்ற அன்னை, அவளை விட்டகன்றபின்னே` | `likely-gemini-error` | **yes — B19** | Source object pronoun is feminine `அவளை`; locked layer has `அவனை`. |
| C19-003 | 454 | 442 | `0454-oruthalaik-kaadhal-05-03.md` | `கின்னியென்னையும் கனவொன்று மெய்மறக்கச்` | source `கன்னியென்னையும் கனவொன்று மெய்மறக்கச்` | `likely-gemini-error` | **yes — B19** | Direct visual source confirms `கன்னியென்னையும்`. |
| C19-004 | 455 | 443 | `0455-oruthalaik-kaadhal-05-04.md` | `காதலரிருவர் கட்டுண்டு மகிழ்ந்திருப்போம்!` | source `காதலிருவர் கட்டுண்டு மகிழ்ந்திருப்போம்!` | `likely-gemini-error` | **yes — B19** | Source reads `காதலிருவர்`, without the locked medial `ர்`. |
| C19-005 | 455 | 443 | `0455-oruthalaik-kaadhal-05-04.md` | `கண்கள் செய்த தவறாலே விழித்துக் கொண்டேன்;` | source `கண்கள் செய்த தவறிலே விழித்துக் கொண்டேன்;` | `likely-gemini-error` | **yes — B19** | Source locative form is `தவறிலே`; locked layer has `தவறாலே`. |
| C19-006 | 456 | 444 | `0456-oruthalaik-kaadhal-06-01.md` | `“வேறு யாருக்குப் கிட்டும்?”` | source `“வேறு யாருக்குக் கிட்டும்?”` | `likely-gemini-error` | **yes — B19** | Direct visual source confirms the conjunct `யாருக்குக்`. |
| C19-007 | 456 | 444 | `0456-oruthalaik-kaadhal-06-01.md` | `முகம், மழிக்க நேரமில்லை போலும்` | source `முகம், மழிக்க நேரமில்லே போலும்` | `old-or-uncommon-form` | **yes — B19** | The source uses the colloquial/older-looking `நேரமில்லே`; File10/canonical normalize it to `நேரமில்லை`. |
| C19-008 | 458 | 446 | `0458-oruthalaik-kaadhal-06-02.md` | `கொலைக்காடாய் ஆக்குகின்ற போர் ஒன்று தேவைதானா?` | source `கொலைக்காடாய் ஆக்குகின்ற போர் ஒன்று தேவைதானு?` | `old-or-uncommon-form` | **yes — B19** | High-resolution source recheck confirms the final `தேவைதானு?` form. |
| C19-009 | 463 | 451 | `0463-oruthalaik-kaadhal-07-01.md` | `சோகத்தின் ஆழத்திலிருந்து கண்ணோளியைப் பாயவிட்டு` | source `சோகத்தின் ஆழத்திலிருந்து கண்ணொளியைப் பாயவிட்டு` | `likely-gemini-error` | **yes — B19** | Source reads `கண்ணொளியைப்`; locked layer has `கண்ணோளியைப்`. |
| C19-010 | 467 | 455 | `0467-oruthalaik-kaadhal-07-04.md` | `இறாமீனின் உடல்போன்றுச் சொரசொரப்புக் கொண்ட` | source `இறுமீனின் உடல்போன்றுச் சொரசொரப்புக் கொண்ட` | `likely-gemini-error` | **yes — B19** | Direct source inspection confirms `இறுமீனின்`. |
| C19-011 | 467 | 455 | `0467-oruthalaik-kaadhal-07-04.md` | `சுறாமீனின் முகத்தில் நீண்ட கொம்புகள் போல்` | source `சுறுமீனின் முகத்தில் நீண்ட கொம்புகள் போல்` | `likely-gemini-error` | **yes — B19** | Direct source inspection confirms `சுறுமீனின்`. |
| C19-012 | 468 | 456 | `0468-oruthalaik-kaadhal-07-05.md` | glossary `இறவு = இறாமீன்.` | source glossary `இறவு = இறுமீன்.` | `likely-gemini-error` | **yes — B19** | Same lexical divergence is repeated in the source glossary. |
| C19-013 | 468 | 456 | `0468-oruthalaik-kaadhal-07-05.md` | glossary `சுறவு = சுறாமீன்.` | source glossary `சுறவு = சுறுமீன்.` | `likely-gemini-error` | **yes — B19** | Same lexical divergence is repeated in the source glossary. |
| C19-014 | 470 | 458 | `0470-oruthalaik-kaadhal-08-02.md` | `கவிகற்ற உன்நெஞ்சுக் கென்நிலை புரியுமம்மா!` | source `கவிகற்ற உன்நெஞ்சுக் கெந்நிலை புரியுமம்மா!` | `likely-gemini-error` | **yes — B19** | Source has assimilated `கெந்நிலை`; locked layer has `கென்நிலை`. |
| C19-015 | 472 | 460 | `0472-oruthalaik-kaadhal-08-03.md` | `மதுவூரும் கவிமலரால் புகழ்ந்தார் தித்தனை!` | source `மதுவூறும் கவிமலரால் புகழ்ந்தார் தித்தனை!` | `likely-gemini-error` | **yes — B19** | Source verb is `மதுவூறும்`; locked layer changes `ற` to `ர`. |
| C19-016 | 473 | 461 | `0473-oruthalaik-kaadhal-08-04.md` | `ஒலையில் உள்ள குறிப்பில்;` | source `ஓலையில் உள்ள குறிப்பில்;` | `likely-gemini-error` | **yes — B19** | Source noun is `ஓலை`; locked layer shortens the initial vowel. |

## C19 closure audit

C19 is an **audit-only closure**.

- source scans **451–475** were visually inspected against File10 only where the B19-resolved lexical block is reliable;
- missing/replaced/phantom File10 segments were not assigned synthetic mappings;
- **16** substantive discrepancy records were entered across **11** scans;
- **0** canonical page records were edited;
- no Gate-B page was reopened;
- no lexical correction was promoted;
- wording state remains **Gemini-lexical-locked / not word-for-word scan verified**.

## Gate C cumulative state after C19

- completed Gate-C batches: **C01–C19**
- audited scans: **475/497**
- cumulative substantive discrepancy records: **134**
- remaining scans: **22**
- next frontier: **scan 476**
- Gate C2: **NOT STARTED / NOT AUTHORIZED**

## Exact next activity

Process **Gate C C20 — final remainder scans 476–497**.

Available direct source pair:
- user-supplied `TVA_BOK_0042551_சங்கத்_தமிழ்_part_010_pages_451-497.pdf`, split pages **26–47** / physical scans **476–497**;
- user-supplied `File10.md`, resolved scan-by-scan against the PDF.

B20 mapping:
- scan **476 / printed 464** → File10 Page **464**;
- scan **477** → File10 Page **465** `(Image Page)`;
- scans **478–484 / printed 466–472** → File10 Pages **466–472**;
- scan **485** → File10 Page **473** `(Image Page)`;
- scans **486–492 / printed 474–480** → File10 Pages **474–480**;
- scan **493** → File10 Page **481** `(Image Page)`;
- scans **494–496 / printed 482–484** → File10 Pages **482–484**;
- scan **497** is the physical back cover; File10 has only a trailing publisher extraction after Page 484 and no separate physical-page comment.

At C20 close:
1. append only substantive lexical discrepancies to this ledger;
2. verify **0 canonical page files changed**;
3. close Gate C at **497/497 audited**;
4. do not start Gate C2 unless explicitly authorized by the user;
5. derive the next non-C2 activity from the productive completion plan and synchronize all operational docs.


# C20 — scans 476–497

**Status: COMPLETE / PASS — FINAL GATE-C BATCH**

- date: **2026-09-16**
- audited scans: **476–497 / 22**
- controlling source: user-supplied `TVA_BOK_0042551_சங்கத்_தமிழ்_part_010_pages_451-497.pdf`, split pages **26–47**
- direct Gemini lexical witness: user-supplied `File10.md`, resolved scan-by-scan against the PDF
- substantive discrepancy records: **6**
- scans containing discrepancies: **5**
- scans with no new substantive lexical discrepancy: **17**
- canonical page files changed: **0**
- Gate C2 corrections: **0**

Clean / no-new-substantive-discrepancy scans:

**476–477, 479–480, 482–491, 493, 496–497**

Special handling:
- full-page illustration scans: **477, 485, 493**;
- scan **497** is the physical back cover; the PDF-visible imprint is `ROCKFORT Publications (P) Ltd.`; File10's trailing publisher extraction is not a separate physical-page lexical block;
- B20 mapping was retained exactly: 476→464; 477→465 image; 478–484→466–472; 485→473 image; 486–492→474–480; 493→481 image; 494–496→482–484;
- documented extraction defects were excluded from the discrepancy count: scan 487 `விட்டீர்கீர்களா` / stray `சிறிட`; scan 488 mixed-script `செவிலித்தாய다தானே`; scan 489 `உடலகத்து`; scan 491 `எடுத்துக்காட்டாயைச்` / `பாற்குடயங்கள்`; scan 492 duplicated `விளக்கொன்றை`; scan 496 mixed-script `ஒன்றை만을ப்`;
- source/File10-aligned historical forms restored during B20, including scan 479 `நல்லவைகளாயிருக்கட்டு” மென்றான்` and scan 484 `வேண்டு” மென்று`, are not discrepancies;
- punctuation-only, spacing-only, line-wrap, running-header/footer and purely structural differences were excluded unless they materially altered lexical interpretation.

## C20 discrepancy records

| ID | Scan | Printed page | Canonical page | Locked File10 / repository wording | Source-visible / source-aligned wording | Classification | Gate-B exception already documented? | Notes |
|---|---:|---:|---|---|---|---|---|---|
| C20-001 | 478 | 466 | `0478-oruthalaik-kaadhal-09-02.md` | `... புறங்கொடாத / புலிப்போத்து / பாணன் வீரத்தைக் ...` | source `... புறங்கொடாத / புலிப்போத்து / என்று / பாணன் வீரத்தைக் ...` | `likely-gemini-error` | **yes — B20** | Reliable File10 Page 466 omits source-visible lexical token `என்று`; B20 deliberately retained the lock. |
| C20-002 | 481 | 469 | `0481-oruthalaik-kaadhal-09-05.md` | quoted Sangam block ends at `விழவு அயர்ந் தன்ன கொழும்பில் திற்றி........` | source quotation continues with `எழாஅப் பாணன்........` | `missing-whole-lexical-block` | **yes — B20** | Source-visible quoted wording is absent from the reliable File10 Page-469 block; the glossary later preserves `எழாஅப் பாணன் = புறங்கொடாத பாணன்`. |
| C20-003 | 492 | 480 | `0492-oruthalaik-kaadhal-11-02.md` | `ஆரணங்கின் குரல் என உணர்ந்து` | source `ஆரணங்கின் குரலாய் இருப்பதை உணர்ந்து` | `likely-gemini-error` | **yes — B20** | B20 restored the File10 lock over the earlier source-aligned repository phrase. |
| C20-004 | 494 | 482 | `0494-oruthalaik-kaadhal-11-03.md` | `எடுத்தெறிந்து பேசினாரே, நற்கிள்ளி!` | source `எடுத்தெறிந்து பேசினீரே, நற்கிள்ளி!` | `likely-gemini-error` | **yes — B20** | Direct visual source and the pre-B20 source-aligned layer read second-person honorific `பேசினீரே`. |
| C20-005 | 494 | 482 | `0494-oruthalaik-kaadhal-11-03.md` | `எமாந்துபோனார் உன் அண்ணன்!` | source `ஏமாந்துபோனார் உன் அண்ணன்!` | `likely-gemini-error` | **yes — B20** | File10/canonical shorten the initial vowel; source-aligned pre-B20 layer retained `ஏமாந்துபோனார்`. |
| C20-006 | 495 | 483 | `0495-oruthalaik-kaadhal-11-04.md` | `இனியவரே! இன்றென்காதல் கைகூடியது! எனை,` | source `இனியவரே! இன்றென்காதல் கைகூடியது! ஏன,` | `likely-gemini-error` | **yes — B20** | B20 restored File10 `எனை`; direct visual source and the pre-B20 source-aligned layer read `ஏன`. |

## C20 closure audit

C20 is an **audit-only closure**.

- source scans **476–497** were visually inspected against File10 under the documented B20 mapping;
- **6** substantive discrepancy records were entered across **5** scans;
- **0** canonical page records were edited;
- no Gate-B page was reopened;
- no lexical correction was promoted;
- Gate C2 remains **NOT STARTED / NOT AUTHORIZED**.

# Gate C final closure

**Gate C — COMPLETE / PASS**

- completed batches: **C01–C20**
- audited scans: **497/497**
- cumulative substantive discrepancy records: **140**
- remaining scans: **0**
- canonical page wording changes during Gate C: **0**
- wording state remains **Gemini-lexical-locked / not word-for-word scan verified**
- Gate C2: **NOT STARTED / NOT AUTHORIZED**

Gate C is now closed. The discrepancy ledger is complete for the current locked wording state.

## Exact next activity

Proceed to **Gate D — Physical / visual / continuity closure**.

Gate D must audit all **497 physical scans** for:
- one scan → one canonical record;
- covers / blanks / illustrations / dividers / end matter;
- printed pagination;
- running headers / footers;
- meaningful alignment;
- continuation relationships;
- cross-page sentence / verse continuity;
- shared-page or boundary anomalies.

Durable Gate-D output:

`works/sangatamil/PHYSICAL_CONTINUITY_AUDIT.md`

Do **not** start Gate C2 unless explicitly authorized.


## Final Gate C2 state — 2026-09-16

- C2 disposition coverage — **scans 1–497 / COMPLETE**
- C2-01 through C2-20 — **COMPLETE / APPLIED**
- historical discrepancy records dispositioned — **140/140**
- historical discrepancy records remaining — **0**
- no scan range remains C2-locked
- correction authority — user's manual findings; historical Gate-C classifications remain audit history
- durable correction record — `C2_SOURCE_CORRECTION_PROGRESS.md`
- whole-volume word-for-word scan verification — **NOT CLAIMED**
- exact next gate — **Gate G metadata/status closure**


# Post-C2 word-for-word audit additions — 2026-09-19

**Status: ACTIVE / AUDIT-ONLY**

The user re-confirmed the governing lexical rule on 2026-09-19:

> Compare every word, but **do not correct words directly**. Any new word-level difference must be recorded in this Gemini discrepancy ledger and left for explicit user adjudication.

These rows are therefore **not correction authorizations**. Canonical wording stays unchanged unless the user later adjudicates an individual row.

| ID | Scan | Printed page | Canonical page | Locked repository wording | Source-visible wording | Classification | Disposition |
|---|---:|---:|---|---|---|---|---|
| WFV-001 | 7 | II | `0007-publication-details.md` | `ராக்போர்ட்` | `ராக்ஃபோர்ட்` | `likely-gemini-error` | **PENDING USER ADJUDICATION — do not change word** |
| WFV-002 | 62 | 47 | `0062-oorin-perumai-unarnthavar-oruthi-04.md` | after `படர்ந்துள்ள கொடியுதிர் மலர்களில்` canonical proceeds to `பாதம் படுகின்ற...` | source visibly contains intervening lexical token `தனது` | `likely-gemini-error` | **PENDING USER ADJUDICATION — do not add word** |
| WFV-003 | 69 | 54 | `0069-vaanan-manandha-vannath-thirumagal-05.md` | `தலைமகனாம் என் கணவர்` | `தலைமகனும் என் கணவர்` | `likely-gemini-error` | **PENDING USER ADJUDICATION — do not change word** |
| WFV-004 | 83 | 68 | `0083-pisiranthaiyar-2-02.md` | `மாலையாவதில்ல - ஆழல்` | `மாலையாவதில்ல - ஆனால்` | `likely-gemini-error` | **PENDING USER ADJUDICATION — do not change word** |
| WFV-005 | 91 | 76 | `0091-pisirandhaiyar-4-01.md` | `வாராத காரணம்தான்` | `வராத காரணம்தான்` | `likely-gemini-error` | **PENDING USER ADJUDICATION — do not change word** |

Non-lexical observations from the same review, such as token placement, lineation or punctuation, are not entered here unless they change the lexical reading.

Higher-resolution review rejected earlier provisional suspicions on scans **59, 73, 78 and 79**; no new lexical discrepancy row is created for those scans.

## Current exact frontier

- Part001 scans **1–50** — audit complete; scan 7 remains a lexical hold.
- Part002 scans **51–96** — compared.
- Part002 scans **97–100** — exact next review range.
- canonical lexical page changes authorized by these WFV rows — **0**.
