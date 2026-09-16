# மின்னாக்கக் கொள்கை — சங்கத் தமிழ்

## அதிகார வரிசை

தற்போதைய user-approved workflow:

1. Gemini File1.md … File10.md — lexical wording lock
2. மூல PDF scan — physical page / structure / presentation authority
3. repository — preservation layer

Gate B-ல் scan-ஐ பார்த்து legitimate Gemini lexical word-ஐ அமைதியாக மாற்றக் கூடாது. Scan/Gemini lexical வேறுபாடு இருந்தால் பதிவு செய்ய வேண்டும்; source-correction Gate C2 user authorization இல்லாமல் செய்யக் கூடாது.

Canonical execution plan: ../PRODUCTIVE_COMPLETION_PLAN.md

## நிலைகள்

- not-started — record exists but usable content not captured
- partial — securely readable portions only
- needs-review — archival capture exists but later gates remain
- verified — required designated verification gates passed
- blocked — source defect prevents safe completion

Gate-B structural correction மட்டும் verified promotion அல்ல.

## source boundary

- physical scans — 1–497
- scan 497 — back cover
- scan 498+ உருவாக்கக் கூடாது
- printed page number scan-ல் தெரிந்தால் மட்டும் பதிவு செய்ய வேண்டும்
- scan number / printed page number இரண்டு வேறு coordinate systems

Gate A is closed at 497/497 canonical records / 0 duplicates / 0 missing.

## Gate B — Gemini-locked structural fidelity

ஒவ்வொரு scan-க்கும்:

1. live main fetch செய்
2. current canonical page record fetch செய்
3. controlling scan inspect செய்
4. matching Gemini locked text align செய்
5. legitimate Gemini lexical wording preserve செய்
6. scan ஆதாரத்தில் மட்டும் structure/presentation சரி செய்: page placement, printed-page metadata, heading hierarchy, paragraph order/boundaries, punctuation, quotation/dialogue structure, verse lineation, spacing/alignment, separators, continuation order, provenance / பொருள் விளக்கம் placement
7. non-source extraction debris body-ல் இருந்தால் நீக்கு
8. scan-ல் lexical text இருந்தும் Gemini-ல் இல்லையெனில் flag செய்; silently recover செய்ய வேண்டாம்
9. structural correction காரணமாக status promote செய்ய வேண்டாம்

Normal batch: 25 physical scans.

## செய்யக் கூடாதவை

- legitimate Gemini word-ஐ scan பார்த்து silently source-correct செய்தல்
- modern spelling-ஆக normalize செய்தல்
- web/critical edition-இல் இருந்து Sangam verse மாற்றிப் பதித்தல்
- source-ல் தெரியாத printed page number infer செய்தல்
- cropped/damaged text-ஐ context மூலம் invent செய்தல்
- illustration-ல் label இல்லாத real person-ஐ appearance மூலம் identify செய்தல்
- Gemini omission-ஐ Gate B-ல் source transcription மூலம் silently fill செய்தல்

## Non-source debris

Body text-ல் சேரக்கூடாதவை: accession/library stamps, handwriting OCR garbage, scanner artefacts, bleed-through, merged running header/footer/page number, extraction wrappers, mixed-script unsupported fragments and duplicated non-source tokens.

## Later gates

- Gate C — lexical discrepancy audit
- Gate C2 — source lexical correction, user explicitly authorizes only
- Gate D — physical/visual/continuity closure
- Gate E — section reconstruction
- Gate F — provenance audit
- Gate G — metadata/status closure
- Gate H — derived navigation
- Gate I — final synchronization

## Documentation discipline

ஒவ்வொரு completed Gate-B batch-க்கும் live frontier stale ஆகாமல் update செய்ய வேண்டிய operational docs:

- STRUCTURAL_FIDELITY_PROGRESS.md
- root NEXT_CHAT_PROMPT_SANGATH_TAMIL.md
- root SANGATH_TAMIL_ARCHIVAL_GUIDELINES.md
- root HANDOVER.md
- works/sangatamil/README.md
- root README.md

Section/provenance derived indexes designated later gates-ல் canonical completion பெறும்.

## தற்போதைய செயல்பாட்டு எல்லை — 2026-09-16

- Gate A — **COMPLETE / PASS**
- Gate B — **COMPLETE / PASS — 497/497**
- Gate C — **COMPLETE / PASS — 497/497 / 140 historical discrepancy records**
- Gate C2 — **COMPLETE / APPLIED — 140/140 adjudicated**
- Gate D — **COMPLETE / PASS — 497/497 physical/visual/continuity**
- Gate E — **COMPLETE / PASS — 104 section-role entries / 497/497 assigned**
- Gate F — **COMPLETE / PASS — 115 formal provenance units + 4 source-note-only**
- Post-C2 reconciliation R1 — **COMPLETE / PASS**
- Gate G — **COMPLETE / PASS — 497/497 metadata/status audited / 11 missing visual-fidelity fields repaired / 0 unresolved**
- current next gate — **Gate H — derived navigation**
- whole-volume word-for-word scan verification — **NOT CLAIMED**

Durable Gate-G record: `../GATE_G_METADATA_STATUS_AUDIT.md`.

Durable B15 correction remains: scans **358–359** are mixed text/illustration; scan **359** is not illustration-only.

Durable File9 exception remains: Book Pages **401–412** are not reliable one-to-one lexical blocks for physical scans **413–424**; do not fabricate alignment.
