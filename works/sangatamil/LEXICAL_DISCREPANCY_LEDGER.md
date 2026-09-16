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
