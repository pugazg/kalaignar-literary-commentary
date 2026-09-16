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
- **C2-09 — scans 201–225**
- **C2-10 — scans 226–250**
- **C2-11 — scans 251–275**
- **C2-12 — scans 276–300**
- **C2-13 — scans 301–325**
- **C2-14 — scans 326–350**
- **C2-15 — scans 351–375**
- **C2-16 — scans 376–400**
- **C2-17 — scans 401–425**
- **C2-18 — scans 426–450**
- **C2-19 — scans 451–475**

The historical Gate-C ledger remains an audit record. Where the user's manual C2 adjudication disagrees with the earlier Gate-C interpretation, **the user's adjudication controls**.

Scans **476–497 remain Gemini-lexical-locked** until the user supplies further instructions.

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


## C2-09 — scans 201–225

**Status: COMPLETE / APPLIED**

| Gate-C ID | Scan | User adjudication | Repository action |
|---|---:|---|---|
| C09-001 | 208 | decorative/source heading `காவிரிநாடன் கரிகாலன்!` — Gemini error | corrected body heading `கபிகாலன்!` → `கரிகாலன்!`; preserved decorative two-line layout |
| C09-002 | 221 | source `தனக்கு இரிந்தானைப் பெயர்புறம் நகுமே` — Gemini error | corrected quotation `இரித்தானைப்` → `இரிந்தானைப்` |
| C09-003 | 223 | source-visible carryover `எனை` belongs before `நாணம் வந்து தடுப்பதாலே` — Gemini error | moved existing `எனை` to the user-authorized source position; lexical token unchanged |

C2-09 page files modified: **208, 221, 223**.


## C2-10 — scans 226–250

**Status: COMPLETE / APPLIED**

| Gate-C ID | Scan | User adjudication | Repository action |
|---|---:|---|---|
| C10-001 | 226 | source section heading `பாரி மகளிர் பாடிய செய்யுள்` — Gemini error | corrected decorative body heading `பாபி மகளிர்` → `பாரி மகளிர்`; preserved two-line layout |
| C10-002 | 230 | source `அந்துவன் சாத்தனையும் ஆதன் அழிசையையும்` — Gemini error | corrected `இழிசையையும்` → `அழிசையையும்` |
| C10-003 | 237 | source `அன்னத்தின் கூட்டமொன்று ஓடையில் படகாகி` — Gemini error | corrected `ஓடையில` → `ஓடையில்` |
| C10-004 | 240 | File5/source both contain two glossary continuation lines omitted by canonical page | restored `தாவும் தன்மையும் உடைய ஆண் குரங்கு மரணம் உற்றதென்று.` and `கற்றிடாத வலிய குட்டியை சுற்றத்திடம் சேர்த்துவிட்டு.` in their glossary positions |
| C10-005 | 248 | File5/source both contain `வயிறுடைய கிழவி.` and `மாண்டான்.` omitted by canonical page | restored `வயிறுடைய கிழவி.` after `தாமரைபோல் ஒட்டிய` and `மாண்டான்.` after `படைகண்டு அஞ்சிப் புறங்கொண்டு` |

C2-10 page files modified: **226, 230, 237, 240, 248**.


## C2-11 — scans 251–275

**Status: COMPLETE / APPLIED**

| Gate-C ID | Scan | User adjudication | Repository action |
|---|---:|---|---|
| C11-001 | 254 | File6/source contain one `இந்தச்`, source-supported after `சிற்றூர் முதல் பேரூர் நகரங்கள் வரை -`; canonical duplicate is repository error | removed duplicate standalone `இந்தச்`; retained the single source-supported occurrence |
| C11-002 | 257 | both historical candidates incorrect; exact poem term is `காம ஒள்எரி` | corrected poem `காம ஒளிஎரி` → `காம ஒள்எரி` |
| C11-003 | 257 | quotation `என்புஉற நலியினும்` — Gemini correct | no change; protected |
| C11-004 | 257 | File6/source `பிரித்துஇடை களையார்` — repository-only divergence / Gemini error | corrected canonical `பிரித்திடை` → `பிரித்துஇடை` |
| C11-005 | 257 | glossary `காம ஒள்எரி = காமமெனும் ஒளிபொருந்திய தீ.` — Gemini is correct | no change; protected |
| C11-006 | 274 | `பொன்மானின் துயர்துடைக்கப் புறப்படுக மன்னா; என்றார்!` — Gemini is correct | no change; protected |

C2-11 page files modified: **254, 257**.


## C2-12 — scans 276–300

**Status: COMPLETE / APPLIED**

| Gate-C ID | Scan | User adjudication | Repository action |
|---|---:|---|---|
| C12-001 | 281 | exact source decorative heading `கிலு கிலுப்பை / வழங்கும் / கிறுகிறுப்பு!` — Gemini error | restored missing `கிலு கிலுப்பை` and corrected `கிறுகிறப்பு!` → `கிறுகிறுப்பு!` |
| C12-002 | 288 | source heading `வெறியாடும் / வேலன் / எதற்காக?` — Gemini error | corrected `இவறியாடும்` → `வெறியாடும்`; preserved three-line layout |
| C12-003 | 290 | source/canonical `முறித்துப் போட்டதுபோல் நெளிகின்றாள், வளைகின்றாள்!` — File6/Gemini error | no canonical change; page already source-aligned |
| C12-004 | 292 | source heading `ஒல்லையூரில் / முல்லையோ?` — Gemini error | corrected `ஒல்லையூபில்` → `ஒல்லையூரில்` |
| C12-005 | 294 | File6/source `ஒல்லையூர்ப் பகுதி எல்லையிலே` — repository-only divergence / Gemini error | restored missing sandhi `ப்`: `ஒல்லையூர் பகுதி` → `ஒல்லையூர்ப் பகுதி` |
| C12-006 | 296 | exact source heading `மறு பிறப்பு / உண்டென்றால் / மறக்க / நேரிடுமோ?` — Gemini error | restored the complete four-line decorative heading in canonical body |

C2-12 page files modified: **281, 288, 292, 294, 296**. Scan **290** required no canonical edit because the repository already held the source-aligned wording.


## C2-13 — scans 301–325

**Status: COMPLETE / APPLIED**

| Gate-C ID | Scan | User adjudication | Repository action |
|---|---:|---|---|
| C13-001 | 304 | File7/source continue quotation with `தாள் தாமரை தோள் தமனியக் கயமலர்` — repository-only divergence | restored the missing second quotation line after `ஆயிதழ் உண்கண் அலர் முகத் தாமரை` |
| C13-002 | 307 | source `யாருக்கும் அடங்காமல் பிளிறிற்றங்கே!` — Gemini error | restored source-visible `பிளிறிற்றங்கே!` after `யாருக்கும் அடங்காமல்` |
| C13-003 | 309 | source heading `முரசு கட்டிலில் / மோசுகீரனார்!` — Gemini error | corrected decorative heading `மோசுகீானர்!` → `மோசுகீரனார்!` |
| C13-004 | 312 | both historical candidates incorrect; exact user reading `குளிர் சாமரம் வீசுகின்ற காட்சி என்னே? என்றயர்ந்தார்` | corrected `என்றர்ந்தார்` → `என்றயர்ந்தார்`, preserving surrounding quotation punctuation |
| C13-005 | 312 | `நான் செய்த தொண்டு இஃதெ` — Gemini is correct | no lexical change; protected |
| C13-006 | 313 | File7 quotation `அதூவும் சாலும், நற் றமிழ் முழுது அறிதல்;` — Gemini is correct | changed canonical `நற் தமிழ்` back to the user-confirmed Gemini form `நற் றமிழ்` |
| C13-007 | 321 | source/canonical second `இவ்வாறு` before `கபிலர் மலை நாட்டுச் செழுமையினை...` — File7/Gemini error | no canonical change; repository already source-aligned |

C2-13 page files modified: **304, 307, 309, 312, 313**. Scan **321** required no page edit because the canonical page already preserves the second `இவ்வாறு`.


## C2-14 — scans 326–350

**Status: COMPLETE / APPLIED**

| Gate-C ID | Scan | User adjudication | Repository action |
|---|---:|---|---|
| C14-001 | 326 | source visibly contains `என்றார்!` immediately after quoted `...அதனைப் பருகலாம்` — repository-only divergence / Gemini error | restored `என்றார்!` immediately after the quoted passage |
| C14-002 | 326 | source/canonical `கடையும்போது கயிற்றால் எழுகின்ற ஒலியோ - ஒரு / காட்டில் உறுமுகின்ற புலிபோல...` — File7/Gemini error | no canonical change; repository already source-aligned |
| C14-003 | 328 | source decorative heading `வீரனைப் பாடிய / சேரன்!` — Gemini error | replaced malformed body heading `வானைப் பாடிய / சோன்!` with exact source heading |
| C14-004 | 331 | `படைக்கலன் தடுக்கும் அவன் கேடயம்தனையும்` — Gemini is correct | no change; protected |
| C14-005 | 340 | source visibly contains `போரில்` after `குருதிநீர் பொங்குகின்ற உலையில் -` — repository-only divergence / Gemini error | restored `போரில்` at the user-authorized source position |

C2-14 page files modified: **326, 328, 340**. C14-002 and C14-004 required no canonical edits.


## C2-15 — scans 351–375

**Status: COMPLETE / APPLIED**

| Gate-C ID | Scan | User adjudication | Repository action |
|---|---:|---|---|
| C15-001 | 352 | both historical heading candidates incorrect; exact heading `மாமழை கண்ட மகிழ்ச்சி!` | replaced body heading and section metadata with exact user ruling |
| C15-002 | 359 | `குடவோலை முறையினாலே - நன்கு` — Gemini is correct | no change; protected |
| C15-003 | 360 | `தான் கடந்து செலஇருந்த தடங் குறித்துத்` — Gemini is correct | no change; protected |
| C15-004 | 361 | source `விரோதிகளை வீழ்த்துகின்ற சேரமானின் தளபதியாம்` — Gemini error | corrected `வீழ்த்துக்கின்ற` → `வீழ்த்துகின்ற` |
| C15-005 | 363 | source glossary `இத்திப் புகர்படு நீழல் = இத்தி மரத்தின் புள்ளிகள் பொருந்திய நிழல்` — Gemini error | restored omitted second `இத்தி` in the glossary definition |
| C15-006 | 364 | `சற்று முகம் சுளீப்பீர்!` — Gemini is correct | no change; protected |
| C15-007 | 366 | `கொஞ்சி மகிழும் குமரியின் கொங்கையினை அவள் காதலன்;` — Gemini is correct | no change; protected |
| C15-008 | 370 | `கணப்பொழுதும் அகலாதிரு கண்ணா என;` — Gemini is correct | no change; protected |
| C15-009 | 370 | `ஓருயிராய் நாங்களாகி உலகத்தை மறந்ததும் பொய்யா?` — Gemini is correct | no change; protected |
| C15-010 | 373 | source decorative heading `ஓர் உவமை; இரு காட்சி!` — Gemini error | corrected body heading `ஒர் உவமை; இரு காட்சி!` → `ஓர் உவமை; இரு காட்சி!` |

C2-15 page files modified: **352, 361, 363, 373**.


## C2-16 — scans 376–400

**Status: COMPLETE / APPLIED**

| Gate-C ID | Scan | User adjudication | Repository action |
|---|---:|---|---|
| C16-001 | 377 | source `அகன்ற வாய்ப் பருந்துகளும் வட்டமிட்டுச் சூழ்ந்தபோது;` — Gemini error | corrected `பருந்துக்களும்` → `பருந்துகளும்` |
| C16-002 | 383 | `நீண்ட அறிவுரைகளை நீட்டி முழக்குகின்றாய்!` — Gemini is correct | no change; protected |
| C16-003 | 383 | source quotation `இடிக்கும் கேளிர்! நுங்குறை ஆகம் நிறுக்கல்...` — Gemini error | corrected quotation `நும்குறை` → `நுங்குறை`; retained source-supported `நிறுக்கல்` |

C2-16 page files modified: **377, 383**.


## C2-17 — scans 401–425

**Status: COMPLETE / APPLIED**

| Gate-C ID | Scan | User adjudication | Repository action |
|---|---:|---|---|
| C17-001 | 402 | source `வஞ்சமின்றி வழங்கிடுவேன் உனக்காகக் கண்ணா! - உன் / மஞ்சத்து மயிலாக...` — Gemini error | restored omitted `- உன்` after `கண்ணா!` |
| C17-002 | 404 | source `அருகில் வரமுடியாமல் ஏங்கத்தான் வேண்டும்!` — Gemini error | corrected `கருகில்` → `அருகில்` |
| C17-003 | 410 | `முலைவேதின் ஒற்றி முயங்கிப் பொதிவேம் / கொலைஏறு சாடிய புண்ணை......` — Gemini is correct | no change; protected |
| C17-004 | 413 | source `மாயமாய் வந்து அவைகளைப் பறிப்பான்!` — repository-only divergence / Gemini error | corrected `அவைகளப்` → `அவைகளைப்` |
| C17-005 | 413 | source `தாயும் எனை அருகழைத்து “மகளே” என்றாள்!` — repository-only divergence / Gemini error | replaced corrupted canonical phrase with exact user-authorized source wording |
| C17-006 | 420 | both prior candidates incorrect; exact user reading `களிறுகளைப் பந்தாடிப் புரவிகளைப் பஞ்சாக்கிக்` | replaced corrupted canonical line with exact user ruling |
| C17-007 | 421 | source `கார் காலம் தலைகாட்டத் தொடங்கு முன்னர்` — repository-only divergence / Gemini error | corrected `திலைகாட்டத்` → `தலைகாட்டத்` |
| C17-008 | 422 | source `பூத்திட்ட முல்லையிலே அமர்ந்து தேன் மொண்டு,` — repository-only divergence / Gemini error | corrected `புத்திட்ட` → `பூத்திட்ட` |

C2-17 page files modified: **402, 404, 413, 420, 421, 422**. Scan **410** required no edit.


## C2-18 — scans 426–450

**Status: COMPLETE / APPLIED**

| Gate-C ID | Scan | User adjudication | Repository action |
|---|---:|---|---|
| C18-001 | 429 | `விண்ணில் நட்சத்திரமொன்று வீழ்கின்ற வேகத்தில்` — Gemini is correct | no change; protected |
| C18-002 | 430 | source includes `துடிப்பதாய்ச்` before `சேதி வந்து...` — Gemini error | restored `துடிப்பதாய்ச்` |
| C18-003 | 431 | source `ஊசியினும் வேகமாய்ப் போரை முடித்து` — Gemini error | corrected `வேகமாயப்` → `வேகமாய்ப்` |
| C18-004 | 431 | source has standalone transition `இவ்வாறு` before `முத்தமிழ் வித்தகரின் பாமாலைக்கும்...` — Gemini error | restored standalone `இவ்வாறு` |
| C18-005 | 434 | `சுடுங்காதல் நெருப்பாலே சுவைப்பண்டம் சமைத்து` — Gemini is correct | no change; protected |
| C18-006 | 435 | source `கடுந்தமிழ்ச் சொல்லாலே இப்பாடல் இயற்றியுள்ளேன்.` — Gemini error | corrected `இயுள்ளேன்` → `இயற்றியுள்ளேன்` |
| C18-007 | 435 | source `வாட்டும் காதல் நிறைவேற வழியொன்று சொல்லென்று` — Gemini error | corrected `வழியொரு` → `வழியொன்று` |
| C18-008 | 436 | source `“மகளே; நற்கண்ணை!” என்றழைத்தவாறு` — Gemini error | corrected `என்றழைத்துவாறு` → `என்றழைத்தவாறு` |
| C18-009 | 441 | source `“சுள்” என்று கோபம் வருவதற்குள்...` — repository-only divergence / Gemini error | corrected `“சொல்”` → `“சுள்”` |
| C18-010 | 441 | source `... உண்மையைச் சொல்லிவிடு” என்றாள்!` — repository-only divergence / Gemini error | corrected `என்றுரைத்தாள்!` → `என்றாள்!` |
| C18-011 | 441 | source `நன்னாளாம் நாளை விருந்துக்கு வருகின்ற கிள்ளியிடம்` — repository-only divergence / Gemini error | corrected `நன்னுளாம்` → `நன்னாளாம்` |
| C18-012 | 441 | source `குறித்த நேரம் தவறாமல் ஊர்ச் சேவல் கூவியது!` — repository-only divergence / Gemini error | corrected `தவறுமல்` → `தவறாமல்` |
| C18-013 | 442 | source `உப்பு மட்டும் போடுதற்கு மறந்திடாதீர்!` — repository-only divergence / Gemini error | corrected `போதற்கு` → `போடுதற்கு` |
| C18-014 | 442 | source `கரங்குவித்து ஒருவருக்கொருவர் வணக்கம் செய்து` — repository-only divergence / Gemini error | corrected `காங்குவித்து` → `கரங்குவித்து` |
| C18-015 | 442 | source `கனிந்த அன்பைப் பரிமாறிக்கொண்டு` — repository-only divergence / Gemini error | corrected `பாரிமாறிக்கொண்டு` → `பரிமாறிக்கொண்டு` |
| C18-016 | 442 | source `வேங்கைநிகர்க் கிள்ளியிடம் விரைந்து வந்தாள் நற்கண்ணை!` — repository-only divergence / Gemini error | corrected corrupted compound to `வேங்கைநிகர்க்` |
| C18-017 | 442 | source `ஓய்விருக்கும்போது படித்தால் போதும்!` — repository-only divergence / Gemini error | corrected `ஒவ்வொருக்கும்போது` → `ஓய்விருக்கும்போது` |
| C18-018 | 448 | source `“கரந்தைப் போர் வெல்க!” என்றாள்!` — repository-only divergence / Gemini error | corrected `கருந்தைப்` → `கரந்தைப்` |

C2-18 page files modified: **430, 431, 435, 436, 441, 442, 448**. Scans **429** and **434** required no edits.


## C2-19 — scans 451–475

**Status: COMPLETE / APPLIED**

| Gate-C ID | Scan | User adjudication | Repository action |
|---|---:|---|---|
| C19-001 | 451 | source `உறையூரின் சோழமகன் போர்முனைக்குச் செல்லும்போது` — Gemini error | corrected `சோழன்` → `சோழமகன்` |
| C19-002 | 451 | source `அறிவுரை புகன்ற அன்னை, அவளை விட்டகன்றபின்னே` — Gemini error | corrected `அவனை` → `அவளை` |
| C19-003 | 454 | source `கன்னியென்னையும் கனவொன்று மெய்மறக்கச்` — Gemini error | corrected `கின்னியென்னையும்` → `கன்னியென்னையும்` |
| C19-004 | 455 | `காதலரிருவர் கட்டுண்டு மகிழ்ந்திருப்போம்!` — Gemini is correct | no change; protected |
| C19-005 | 455 | `கண்கள் செய்த தவறாலே விழித்துக் கொண்டேன்;` — Gemini is correct | no change; protected |
| C19-006 | 456 | source `“வேறு யாருக்குக் கிட்டும்?”` — Gemini error | corrected `யாருக்குப்` → `யாருக்குக்` |
| C19-007 | 456 | `முகம், மழிக்க நேரமில்லை போலும்` — Gemini is correct | no change; protected |
| C19-008 | 458 | `கொலைக்காடாய் ஆக்குகின்ற போர் ஒன்று தேவைதானா?` — Gemini is correct | no change; protected |
| C19-009 | 463 | `சோகத்தின் ஆழத்திலிருந்து கண்ணோளியைப் பாயவிட்டு` — Gemini is correct | no change; protected |
| C19-010 | 467 | `இறாமீனின் உடல்போன்றுச் சொரசொரப்புக் கொண்ட` — Gemini is correct | no change; protected |
| C19-011 | 467 | `சுறாமீனின் முகத்தில் நீண்ட கொம்புகள் போல்` — Gemini is correct | no change; protected |
| C19-012 | 468 | glossary `இறவு = இறாமீன்.` — Gemini is correct | no change; protected |
| C19-013 | 468 | glossary `சுறவு = சுறாமீன்.` — Gemini is correct | no change; protected |
| C19-014 | 470 | `கவிகற்ற உன்நெஞ்சுக் கென்நிலை புரியுமம்மா!` — Gemini is correct | no change; protected |
| C19-015 | 472 | source `மதுவூறும் கவிமலரால் புகழ்ந்தார் தித்தனை!` — Gemini error | corrected `மதுவூரும்` → `மதுவூறும்` |
| C19-016 | 473 | source `ஓலையில் உள்ள குறிப்பில்;` — Gemini error | corrected `ஒலையில்` → `ஓலையில்` |

C2-19 page files modified: **451, 454, 456, 472, 473**.

## Cumulative C2 state

- C2 disposition coverage — **475/497 scans** (C06 closed with 0 discrepancy records)
- modified canonical page files — **72**
- literary/source corrections applied — scans **7, 21, 28, 29, 35, 47, 51, 59, 64, 70, 77, 83, 96, 113, 123, 163, 165, 175, 188, 192, 195, 199, 208, 221, 223, 226, 230, 237, 240, 248, 254, 257, 281, 288, 292, 294, 296, 304, 307, 309, 312, 313, 326, 328, 340, 352, 361, 363, 373, 377, 383, 402, 404, 413, 420, 421, 422, 430, 431, 435, 436, 441, 442, 448, 451, 454, 456, 472, 473**
- facsimile-description policy applied — scan **8**
- stale divergence / section-title metadata cleaned without body change — scans **40, 112**
- protected Gemini-correct findings — scans **5, 9, 11, 13, 19, 29, 39, 40, 47, 53, 58, 64, 87, 96, 120, 174, 180, 199, 257, 274, 312, 313, 331, 359, 360, 364, 366, 370, 383, 410, 429, 434, 455, 456, 458, 463, 467, 468, 470**
- scans **476–497** — **LOCKED / C2 NOT AUTHORIZED**
- whole-volume word-for-word verification — **NOT CLAIMED**
- Gate G — **DEFERRED**

## Next activity

Wait for the user's C2 findings/instructions for **scans 476–497**. Do not modify that batch from the historical ledger alone.
