# NEXT CHAT PROMPT — சங்கத் தமிழ் / WFV ADJUDICATION BATCH A

Continue only from live `main` in `pugazg/kalaignar-literary-commentary`. **LIVE MAIN IS AUTHORITATIVE.**

## Source re-audit — COMPLETE

R01 through R50 are complete.

Fresh physical source coverage:

- **497/497 scans — COMPLETE**
- current Tamil state — **452 verified / 44 needs-review / 1 partial**
- current visual-fidelity state — **452 verified / 45 needs-review**
- WFV-001 — **REJECTED**
- WFV-002 through WFV-056 — **55 PENDING USER ADJUDICATION rows across 44 pages**
- lexical substitutions made by R01–R50 — **0**
- maintained-English release-report gate — **PAUSED**

Do **not** restart the source re-audit.

## Governing rule

No pending WFV row may be applied without explicit user adjudication.

For each row:

1. show the canonical wording/placement;
2. show the direct source evidence already recorded in `LEXICAL_DISCREPANCY_LEDGER.md`;
3. identify the discrepancy type;
4. ask the user to choose **keep canonical** or **apply source** (or provide a different explicit reading);
5. do not modify the repository until the user adjudicates.

Historical-glyph evidence remains source evidence, not automatic permission to change canonical wording.

## Read first

1. `works/sangatamil/TAMIL_WORD_FOR_WORD_VERIFICATION.md`
2. `works/sangatamil/TAMIL_WORD_FOR_WORD_REAUDIT_R50_SCANS_491_497.md`
3. `works/sangatamil/LEXICAL_DISCREPANCY_LEDGER.md`
4. `works/sangatamil/HISTORICAL_TAMIL_GLYPH_TRANSCRIPTION_GUIDE.md`
5. `works/sangatamil/GEMINI_TEXT_LOCK.md`
6. `works/sangatamil/C2_SOURCE_CORRECTION_PROGRESS.md`
7. `works/sangatamil/README.md`
8. root `HANDOVER.md`
9. `works/sangatamil/translations/en/TRANSLATION_STATUS.md`

## Exact next activity — Adjudication Batch A

Present these earliest **10 held physical pages** in a compact comparison table:

| Scan | WFV |
|---:|---|
| 25 | WFV-006 |
| 30 | WFV-007, WFV-008 |
| 49 | WFV-009 |
| 55 | WFV-010 |
| 62 | WFV-002 |
| 67 | WFV-011 |
| 69 | WFV-003 |
| 83 | WFV-004 |
| 85 | WFV-012 |
| 87 | WFV-013 |

### Exact ledger evidence

- **WFV-006 / scan 25** — canonical `வளையாத முதுகெலும்பு பெற்றவனோ?`; source `வளையாத முதுகெலும்பு பெற்றவனே?`.
- **WFV-007 / scan 30** — quotation canonical `ஆள்அன்று என்று வாளின் தப்பார்;`; source `ஆளன்று என்று வாளின் தப்பார்;`.
- **WFV-008 / scan 30** — gloss canonical `ஆள்அன்று என்று வாளின் தப்பார் = ...`; source `ஆளன்று என்று வாளின் தப்பார் = ...`.
- **WFV-009 / scan 49** — quotation canonical `திண்டோர் நள்ளி கானத் தண்டர்`; source `திண்டேர் நள்ளி கானத் தண்டர்`.
- **WFV-010 / scan 55** — canonical `ஆன்றவிந் தடங்கிய மேலோர் புலவர் அவை கூடிற்றாம்!`; source `ஆன்றவிந் தடங்கிய மேலோர் புலவர் அவை கூடிற்றும்!`.
- **WFV-002 / scan 62** — canonical places `தனது` before `பலாமரத்து இலைச்சருகுகளில்`; source places the same token later as `படர்ந்துள்ள கொடியுதிர் மலர்களில் - தனது / பாதம்...`.
- **WFV-011 / scan 67** — canonical `அவசரமாய்ப் புறப்பட்டான் தேர்ஏறி!`; source `அவசரமாய்ப் புறப்பட்டான் தேரேறி!`.
- **WFV-003 / scan 69** — canonical `தலைமகனாம் என் கணவர்`; source `தலைமகனும் என் கணவர்`.
- **WFV-004 / scan 83** — canonical `மாலையாவதில்ல - ஆழல்`; source `மாலையாவதில்ல - ஆனால்`.
- **WFV-012 / scan 85** — canonical omits a right-offset `- அவர்கள்`; source visibly includes it between `வளர்ந்த மகன், மனைவியுடன் வயலுக்குச் சென்றுளான்` and `வருவதற்கு நேரமாகும்; அஞ்சாதே!`.
- **WFV-013 / scan 87** — canonical places `நல்ல` before `இலக்கிய மேதைகள்`; source places `நல்ல` with the trade line `இமிழ் கடல் தாண்டியும் புகழ் மணம் பரப்பி - நல்ல / அகில், மிளகு, முத்து வாணிபம் புரிவார்!`.

Do not apply any of these until the user replies with explicit adjudications.

## After user adjudication

For each accepted source correction:

- update only the exact affected Tamil page/placement;
- preserve all unrelated wording;
- update that WFV ledger row to the user's final disposition;
- promote the page to `verified` / visual `verified` only when all holds on that page are cleared;
- perform targeted English impact reconciliation if the Tamil change affects meaning or translation;
- synchronize tracker, README, HANDOVER, page-map, English status, ledger and this next-chat prompt.

For rejected source corrections, retain canonical wording and mark the WFV row rejected/resolved by user.

The maintained-English release-report gate remains **PAUSED** until all WFV rows are resolved.
