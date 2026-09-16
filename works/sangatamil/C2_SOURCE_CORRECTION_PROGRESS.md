# சங்கத் தமிழ் — Gate C2 Source Correction Progress

## Scope and authority

Gate C2 is **not a whole-volume source-correction authorization**.

The user explicitly opened C2 in manual batches and supplied adjudications that control correction decisions:

- **C2-01 — scans 1–25**
- **C2-02 — scans 26–50**
- **C2-03 — scans 51–75**
- **C2-04 — scans 76–100**
- **C2-05 — scans 101–125**
- **C2-06 — scans 126–150** — no Gate-C discrepancy records / no page action
- **C2-07 — scans 151–175**
- **C2-08 — scans 176–200**

The historical Gate-C ledger remains an audit record. Where the user's manual C2 adjudication disagrees with the earlier Gate-C interpretation, **the user's adjudication controls**.

Scans **201–497 remain Gemini-lexical-locked** until the user supplies further instructions.

## C2-01 — scans 1–25

**Status: COMPLETE / APPLIED**

| Gate-C ID | Scan | User adjudication | Repository action |
|---|---:|---|---|
| C01-001 | 5 | `வெளியீட்டாளர்` — Gemini is correct | no change |
| C01-002 | 7 | source `அளவு : 14 x 21½ சி.எம்.` — Gemini error | corrected `0007-publication-details.md` |
| C01-003 | 8 | handwritten முன்னுரை — description-only is sufficient | no handwritten transcription; page simplified to identify a handwritten letter |
| C01-004 | 9 | `தங்கள் கட்டளையை ஒருவாறு நிறைவேற்றினேன்` — Gemini is correct | no change |
| C01-005 | 11 | `ஆண்பாலர் பதினால்வர்` — Gemini is correct | no change |
| C01-006 | 13 | `அதனைக் களைகின்ற திறல் மிக்க` — Gemini is correct | no change |
| C01-007 | 13 | `சொல் நயத்தை மற்றாரும் நுகரும் வண்ணம்` — Gemini is correct | no change |
| C01-008 | 19 | `அரும்பு, அமர் ஆத்தி` — Gemini is correct | no change |
| C01-009 | 21 | `சங்கத் தமிழ்` is running header only | removed from literary body start |
| C01-010 | 21 | missing source-visible `காதலையும்` | restored at source-supported continuation position |
| C01-011 | 21 | missing source-visible `ஆக்கிக்கொண்டு` | restored at source-supported continuation position |

C2-01 page files modified: **7, 8, 21**.

## C2-02 — scans 26–50

**Status: COMPLETE / APPLIED**

| Gate-C ID | Scan | User adjudication | Repository action |
|---|---:|---|---|
| C02-001 | 28 | source `அடடா; அவனைச் சோழமன்னன்` — Gemini error | `அட்டா` → `அடடா` |
| C02-002 | 29 | `வந்துதித்த நானோ` — Gemini is correct | retained `நானோ` |
| C02-003 | 29 | source placement `அந்தப் / பண்பாட்டு... / ... மனப் / புண்பட்டு...` — repository-only divergence | moved existing `மனப்` to source-supported position while retaining user-confirmed `நானோ` |
| C02-004 | 35 | `வீணே` belongs with `தேன் குடிக்கப் போகின்ற வண்டை - வீணே / ஏன் தடுக்கின்றாய்?` | moved existing token; later clause now `குன்றெடுக்கும் நெடுந்தோள் கொண்டவனே! - பகையை` |
| C02-005 | 39 | `ஔவைக்குக்` — Gemini is correct | no change |
| C02-006 | 40 | `ஔவைப் பிராட்டி` — Gemini is correct | no body change; stale divergence note removed |
| C02-007 | 40 | `வெள்ளை வெள்யாட்டுச் செச்சை போலத்` — Gemini is correct | no body change; stale divergence note removed |
| C02-008 | 47 | heading `காக்கைக்கு நன்றி காட்ட...` — Gemini error | full heading restored |
| C02-009 | 47 | `அப்படியொரு காகம் கரைந்திற்றாங்கே!` — Gemini is correct | retained |

C2-02 page files modified: **28, 29, 35, 40, 47**. Scan 40 modification is documentation/metadata cleanup only; literary wording is unchanged.


## C2-03 — scans 51–75

**Status: COMPLETE / APPLIED**

| Gate-C ID | Scan | User adjudication | Repository action |
|---|---:|---|---|
| C03-001 | 51 | source `எதிரிகளைக்` — Gemini error | corrected `எதிரிகளைக` → `எதிரிகளைக்` |
| C03-002 | 53 | `விருப்பைச்` — Gemini is correct | no change |
| C03-003 | 58 | `வேந்தர்க்குக்` — Gemini is correct | no change |
| C03-004 | 59 | both earlier candidate readings are incorrect; user-authorized reading `முசுண்டை கொடியும்` | replaced only the disputed first phrase `முன்னைக் கொடியும்` → `முசுண்டை கொடியும்`; adjacent locked wording left unchanged |
| C03-005 | 64 | source `கனைதுயில் = மிக உறக்கம்` — Gemini error | corrected `கனைதுல்` → `கனைதுயில்` |
| C03-006 | 64 | `ஔவை துரைசாமிப் பிள்ளை` — Gemini is correct | no change; protected |
| C03-007 | 70 | heading `ஒரு பொது மகளின் புலம்பல்!` — Gemini error | restored leading `ஒரு` in canonical body heading |

C2-03 page files modified: **51, 59, 64, 70**.


## C2-04 — scans 76–100

**Status: COMPLETE / APPLIED**

| Gate-C ID | Scan | User adjudication | Repository action |
|---|---:|---|---|
| C04-001 | 77 | source `பாண்டிநாட்டுச் சிற்றூரில்` — Gemini error | corrected `பாண்டுநாட்டுச் சிற்றூரில்` → `பாண்டிநாட்டுச் சிற்றூரில்` |
| C04-002 | 83 | source introductory prose before the quotation is a true missing whole lexical block | restored the exact pre-quotation block from pre-lock direct-source capture commit `9b8ce8497a374f58d4b4b4f23c293491b3c13c02`; existing Gemini/File2 quotation left unchanged |
| C04-003 | 87 | `சந்தையில் தொலைத்துவிட்ட பொருளாயிற்றே தமது மகிழ்ச்சி` — Gemini is correct | no change; protected |
| C04-004 | 96 | heading `உலைக் களத்து இரும்பும் ஒரு துளிநீரும்!` — Gemini error | corrected malformed body heading to the user-authorized source heading |
| C04-005 | 96 | `சிவகெங்கைச் சீமை` — Gemini is correct | no change; protected |

C2-04 page files modified: **77, 83, 96**.


## C2-05 — scans 101–125

**Status: COMPLETE / APPLIED**

| Gate-C ID | Scan | User adjudication | Repository action |
|---|---:|---|---|
| C05-001 | 112 | both historical candidate headings are incorrect; exact heading is `புரிந்துகொண்டான்; பிரிந்துசென்றார்!` | body heading already matched; corrected stale `section` metadata on scan 112 to the exact user-confirmed heading |
| C05-002 | 113 | source opening quotation stanza after the prose is a true missing whole lexical block | restored the exact source-visible Kalithogai opening stanza from the supplied scan; continuation remains across scan 114 to scan 115 |
| C05-003 | 120 | note `ஊன்பொழிப் பசுங்குடையார்` — Gemini is correct | no change; protected |
| C05-004 | 123 | source opening prose before terminal `சென்றனள்!` is a true missing whole lexical block | restored exact source-visible lines `அடுத்தநாள் காலை...` / `எடுத்தும் கொடுத்தும்...` before the already-correct `சென்றனள்!` |

C2-05 page files modified: **112, 113, 123**.


## C2-06 — scans 126–150

**Status: COMPLETE / NO DISCREPANCY RECORDS / NO PAGE ACTION**

Historical Gate C contains **0 substantive discrepancy records** for C06. No canonical page wording was changed. The batch is closed without inventing user rulings where no ledger findings exist.

## C2-07 — scans 151–175

**Status: COMPLETE / APPLIED**

| Gate-C ID | Scan | User adjudication | Repository action |
|---|---:|---|---|
| C07-001 | 163 | source `கொங்கர்க் குடகடல் ஓட்டிய ஞான்றைத்` — Gemini error | corrected `குடகடல் ஓடிய ஞான்றைத்` → `குடகடல் ஓட்டிய ஞான்றைத்` |
| C07-002 | 165 | decorative/source heading `காடைப் போர் கண்டுவந்த கணவன்!` — Gemini error | corrected body heading token `இகண்டுவந்த` → `கண்டுவந்த`; preserved decorative three-line layout |
| C07-003 | 174 | `சிறுயிலை நெல்லித் தீங்கனி குறியாது` — Gemini is correct | no change; protected |
| C07-004 | 175 | both historical heading candidates incorrect; exact heading `நீலமலை நீரினும் குளிர்ந்த நெஞ்சம்!` | restored exact heading in canonical body and corrected scan-175 section metadata; scan 176+ left locked |

C2-07 page files modified: **163, 165, 175**.


## C2-08 — scans 176–200

**Status: COMPLETE / APPLIED**

| Gate-C ID | Scan | User adjudication | Repository action |
|---|---:|---|---|
| C08-001 | 180 | quotation `... வானி நீரினும் தீந்தன் சாயலன் ...` — Gemini is correct | no change; protected |
| C08-002 | 188 | decorative/source heading `அவள் நிலமானாள்; அவன் மழையானான்!` — Gemini error | corrected body heading `மழையானன்!` → `மழையானான்!` |
| C08-003 | 192 | source `அறிந்திட விரும்பாமலே அறிமுகமானோம்!` — Gemini error | corrected malformed `விருமபாமலே` → `விரும்பாமலே` |
| C08-004 | 195 | source `முடி புனைந்த மூத்தோர் மறைந்து; அவர்` — Gemini error | corrected `முத்தோர்` → `மூத்தோர்` |
| C08-005 | 199 | locked `கிழங்களின் குறும்புதான் என்னே...` — Gemini error | corrected to historical Gate-C source-visible `கிழங்குகளின் குறும்புதான் என்னே...` |
| C08-006 | 199 | Purananuru 109 quotation `தீஞ்சுனைப் பலவின் பழம்` — Gemini is correct | no change; protected |
| C08-007 | 199 | `கலைஉளமும் பெற்றதாலே கபிலர்க்கு உயிரே ஆனான்` — Gemini is correct | no change; protected |

C2-08 page files modified: **188, 192, 195, 199**.

## Cumulative C2 state

- C2 disposition coverage — **200/497 scans** (C06 closed with 0 discrepancy records)
- modified canonical page files — **25**
- literary/source corrections applied — scans **7, 21, 28, 29, 35, 47, 51, 59, 64, 70, 77, 83, 96, 113, 123, 163, 165, 175, 188, 192, 195, 199**
- facsimile-description policy applied — scan **8**
- stale divergence / section-title metadata cleaned without body change — scans **40, 112**
- protected Gemini-correct findings — scans **5, 9, 11, 13, 19, 29, 39, 40, 47, 53, 58, 64, 87, 96, 120, 174, 180, 199**
- scans **201–497** — **LOCKED / C2 NOT AUTHORIZED**
- whole-volume word-for-word verification — **NOT CLAIMED**
- Gate G — **DEFERRED**

## Next activity

Wait for the user's C2 findings/instructions for **scans 201–225**. Do not modify that batch from the historical ledger alone.
