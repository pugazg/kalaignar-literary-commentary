# சங்கத் தமிழ் — Gate C2 Source Correction Progress

## Scope and authority

Gate C2 is **not a whole-volume source-correction authorization**.

The user explicitly opened C2 in manual batches and supplied adjudications that control correction decisions:

- **C2-01 — scans 1–25**
- **C2-02 — scans 26–50**
- **C2-03 — scans 51–75**

The historical Gate-C ledger remains an audit record. Where the user's manual C2 adjudication disagrees with the earlier Gate-C interpretation, **the user's adjudication controls**.

Scans **76–497 remain Gemini-lexical-locked** until the user supplies further instructions.

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

## Cumulative C2 state

- user-adjudicated scans — **75/497**
- modified canonical page files — **12**
- literary/source corrections applied — scans **7, 21, 28, 29, 35, 47, 51, 59, 64, 70**
- facsimile-description policy applied — scan **8**
- stale divergence metadata cleaned without body change — scan **40**
- protected Gemini-correct findings — scans **5, 9, 11, 13, 19, 29, 39, 40, 47, 53, 58, 64**
- scans **76–497** — **LOCKED / C2 NOT AUTHORIZED**
- whole-volume word-for-word verification — **NOT CLAIMED**
- Gate G — **DEFERRED**

## Next activity

Wait for the user's C2 findings/instructions for **scans 76–100**. Do not modify that batch from the historical ledger alone.
