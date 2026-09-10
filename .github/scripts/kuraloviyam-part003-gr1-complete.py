from pathlib import Path
import subprocess

ROOT = Path('works/kuraloviyam')
EN = ROOT / 'translations/en/pages'
TA = ROOT / 'pages'


def replace_once(path, old, new, label):
    p = Path(path)
    text = p.read_text(encoding='utf-8')
    count = text.count(old)
    if count != 1:
        raise SystemExit(f'{label}: replacement count={count} for {old!r}')
    p.write_text(text.replace(old, new, 1), encoding='utf-8')


def replace_tail(path, heading, new_tail, label):
    p = Path(path)
    text = p.read_text(encoding='utf-8')
    count = text.count(heading)
    if count != 1:
        raise SystemExit(f'{label}: heading count={count} for {heading!r}')
    p.write_text(text.split(heading, 1)[0] + new_tail, encoding='utf-8')

# Gate preconditions: GR1 covers 33 page-aligned records; no page is modified at this gate.
for scan in range(223, 256):
    printed = scan - 17
    ta = TA / f'{scan:04d}-kuraloviyam-{printed}.md'
    en = EN / f'{scan:04d}-kuraloviyam-{printed}.md'
    if not ta.exists() or not en.exists():
        raise SystemExit(f'missing GR1 page pair at scan {scan}')
    tt = ta.read_text(encoding='utf-8')
    et = en.read_text(encoding='utf-8')
    if 'status: "verified"' not in tt or 'visual_fidelity: "verified"' not in tt:
        raise SystemExit(f'Tamil archival precondition failed at scan {scan}')
    if et.count('status: "source-checked"') != 1:
        raise SystemExit(f'English source-check precondition failed at scan {scan}')
    if et.count('source_tamil_status: "verified"') != 1:
        raise SystemExit(f'English Tamil-status precondition failed at scan {scan}')

# GLOSSARY — contextual refinement + Part 003 GR1 source-evidenced chapter labels.
replace_once(
    ROOT / 'translations/en/GLOSSARY.md',
    "| ஊடல் | lovers' quarrel | Controlled contextual rendering in the love-poetics discussion. |",
    "| ஊடல் | lovers' quarrel / sulking | Context-aware. Use **lovers' quarrel** for reciprocal love-poetics contexts; Part 003 scan 253 uses **sulking** for the state of offended withdrawal in the wife/field analogy. |",
    'GLOSSARY oodal'
)
replace_once(
    ROOT / 'translations/en/GLOSSARY.md',
    '| நலம் புனைந்துரைத்தல் | Praising Her Beauty | Chapter 112 label on scans 55 and 71. |',
    '| நலம் புனைந்துரைத்தல் / நலம்புனைந்துரைத்தல் | Praising Her Beauty | Chapter 112 label on scans 55 and 71; Part 003 scan 238 uses the closed source form `நலம்புனைந்துரைத்தல்`. |',
    'GLOSSARY chapter112 variant'
)
review_marker = '## Review rule\n'
glossary = (ROOT / 'translations/en/GLOSSARY.md').read_text(encoding='utf-8')
if glossary.count(review_marker) != 1:
    raise SystemExit('GLOSSARY review marker mismatch')
part3_block = '''## Thirukkural chapter labels first encountered in Part 003 through GR1\n\n| Tamil | Default English | Editorial note |\n|---|---|---|\n| பேதைமை | Folly | Chapter 84 label on scan 224. |\n| பொறையுடைமை | Forbearance | Chapter 16 label on scan 228. |\n| வரைவின் மகளிர் | Women of Mercenary Love | Chapter 92 label on scan 232. |\n| விருந்தோம்பல் | Hospitality | Chapter 9 label on scan 236. |\n| கள்ளுண்ணாமை | Abstaining from Liquor | Chapter 93 label on scan 240. |\n| உழவு | Agriculture | Chapter 104 label on scans 244 and 253. |\n\nThe Chapter 112 source variant `நலம்புனைந்துரைத்தல்` on scan **238** is mapped to the existing controlled **Praising Her Beauty** label rather than creating a duplicate English chapter title. Existing controls reused unchanged in GR1 include **Lamenting the Absent Lover**, **Subtleties of Lovers' Quarrel**, **Loss of Restraint**, **Refraining from Slander**, **Speaking with the Heart**, **Reproaching the Eyes**, **Suffering from Pallor**, **The Blessing of Children**, **Lovers' Sulking**, **False Conduct**, and **Yearning for Union**.\n\n## Part 003 GR1 reconciliation record — scans 223–255\n\nGR1 processed **33 consecutive pages: scans 223–255 / printed 206–238**.\n\n- scans **223–255** — glossary / recurring-terminology reconciliation **PASS, 33/33**;\n- all **20** Chapter/Kural metadata lines in the range were checked against their audited Tamil counterparts with **0 chapter-number, Kural-number, or controlled-label mismatches**;\n- source-evidenced chapter controls added in this gate: **Folly**, **Forbearance**, **Women of Mercenary Love**, **Hospitality**, **Abstaining from Liquor**, and **Agriculture**;\n- the closed source variant `நலம்புனைந்துரைத்தல்` is now explicitly mapped to **Praising Her Beauty**;\n- `ஊடல்` is retained contextually as **lovers' quarrel / sulking**, with scan **253** establishing the latter sense in the wife/field analogy rather than forcing one English wording mechanically;\n- contextual review confirmed that scan **223** `செங்கோல்` is naturally **royal sceptre** in the madman's self-styled-king speech, scan **235** `கல்வி` is ordinary study/education rather than a Chapter-40 label, scan **243** `வீரன்` is the common noun **warrior**, and scan **247** `விளக்கம்` is naturally expressed by **explained**; no page wording change was required for those contexts;\n- English page wording corrections required solely for GR1 terminology consistency: **none**;\n- all 33 English pages remain `source-checked`; this gate makes **no status promotion**;\n- no Tamil archival record changed and no external/published/web English terminology was imported.\n\n'''
(ROOT / 'translations/en/GLOSSARY.md').write_text(glossary.replace(review_marker, part3_block + review_marker, 1), encoding='utf-8')

# Authoritative English status — close GR1 and advance to GR2.
replace_once(
    ROOT / 'translations/en/TRANSLATION_STATUS.md',
    '- glossary reconciliation: **not-started**;',
    '- glossary reconciliation: **IN PROGRESS — GR1 COMPLETE 33/111**;',
    'TRANSLATION_STATUS summary'
)
replace_tail(
    ROOT / 'translations/en/TRANSLATION_STATUS.md',
    '## Current frontier — Part 003 English glossary reconciliation GR1\n',
    '''## Part 003 English glossary reconciliation — IN PROGRESS\n\n- **GR1: scans 223–255 / printed 206–238 — COMPLETE / PASS 33/33**;\n- cumulative glossary reconciliation: **33/111**;\n- English page state remains **111 `source-checked` / 0 `draft` / 0 source-limited / 0 blocked**;\n- page wording changes during GR1: **0**;\n- page status changes during GR1: **0**;\n- Tamil page / metadata changes during GR1: **0**.\n\nGR1 checked recurring names, structural/literary terms, chapter labels and Kural citation metadata against `GLOSSARY.md` and the audited Tamil context. All **20** Chapter/Kural metadata lines in scans **223–255** reconcile without numeric or controlled-label mismatch. Six Part-003-first chapter labels were added to the glossary: **Folly**, **Forbearance**, **Women of Mercenary Love**, **Hospitality**, **Abstaining from Liquor**, and **Agriculture**. The scan-238 closed source form `நலம்புனைந்துரைத்தல்` is mapped to the existing **Praising Her Beauty** control, and `ஊடல்` is now explicitly context-aware as **lovers' quarrel / sulking**.\n\n## Current frontier — Part 003 English glossary reconciliation GR2\n\nExact next activity: **glossary / recurring-terminology reconciliation scans 256–288 / printed 239–271 — 33 page-aligned records**.\n\nCompare recurring names, work/section names, controlled literary terms, publication names, chapter labels, citation metadata and repeated English renderings against `GLOSSARY.md` and audited Tamil context. Update `GLOSSARY.md` only for terms actually evidenced in the active source. Do not mechanically force one English word where context requires a different rendering, and do not import terminology from external editions, web sources or memory.\n\nThis gate does **not** promote `source-checked` pages to `editorial-reviewed`; passing pages remain `source-checked` until the later editorial-review gate. If GR2 passes, cumulative glossary reconciliation becomes **66/111**. Do not begin editorial review during GR2.\n\nPart 004 remains blocked until Part 003 completes glossary reconciliation, editorial review, Part review, release report/release-ready synchronization and the final Part closure checkpoint.\n''',
    'TRANSLATION_STATUS frontier'
)

# English README.
replace_once(
    ROOT / 'translations/en/README.md',
    '- glossary reconciliation: **NEXT / not-started**;\n- editorial review / Part review / release: **not-started**.',
    '- glossary reconciliation: **IN PROGRESS — GR1 COMPLETE 33/111**;\n- editorial review / Part review / release: **not-started**.',
    'English README summary'
)
replace_tail(
    ROOT / 'translations/en/README.md',
    '## Current frontier\n',
    '''## Part 003 English glossary reconciliation — IN PROGRESS\n\n- GR1 **223–255 / 206–238 — COMPLETE / PASS 33/33**;\n- cumulative glossary reconciliation: **33/111**;\n- English pages remain **111 `source-checked`**; GR1 made **0 page wording changes and 0 status changes**.\n\nGR1 added the Part-003-first chapter controls **Folly**, **Forbearance**, **Women of Mercenary Love**, **Hospitality**, **Abstaining from Liquor**, and **Agriculture**; mapped source variant `நலம்புனைந்துரைத்தல்` to existing **Praising Her Beauty**; and refined `ஊடல்` contextually as **lovers' quarrel / sulking**. No Tamil archival record changed.\n\n## Current frontier\n\nExact next activity: **Part 003 English glossary reconciliation GR2 — scans 256–288 / printed 239–271, 33 pages**.\n\nUse `GLOSSARY.md` and audited Tamil context to reconcile recurring names, literary/structural terms, publication names, chapter labels, citation metadata and repeated English renderings. Add glossary entries only when evidenced in the active source. This gate does **not** promote pages to `editorial-reviewed`; pages remain `source-checked` until editorial review.\n\nIf GR2 passes, cumulative glossary reconciliation becomes **66/111**. Part 004 remains blocked until the maintained Part-003 English workflow and final Part closure checkpoint are complete.\n\nSee `TRANSLATION_STATUS.md` for the authoritative detailed frontier.\n''',
    'English README frontier'
)

# Work handover.
replace_tail(
    ROOT / 'HANDOVER.md',
    '## Exact next activity — English Glossary Reconciliation GR1\n',
    '''## Glossary reconciliation progress — GR1 COMPLETE / PASS 33/111\n\n- GR1 **223–255 / printed 206–238 — COMPLETE / PASS 33/33**;\n- cumulative glossary reconciliation: **33/111**;\n- all English pages remain `source-checked`; GR1 made **0 English page wording changes / 0 status changes**;\n- all **20** Chapter/Kural metadata lines in the GR1 range reconcile with the audited Tamil records;\n- six Part-003-first chapter controls were added: **Folly**, **Forbearance**, **Women of Mercenary Love**, **Hospitality**, **Abstaining from Liquor**, **Agriculture**;\n- source variant `நலம்புனைந்துரைத்தல்` is mapped to existing **Praising Her Beauty**; `ஊடல்` is explicitly context-aware as **lovers' quarrel / sulking**;\n- no Tamil file or metadata changed.\n\n## Exact next activity — English Glossary Reconciliation GR2\n\nProcess **scans 256–288 / printed 239–271 — 33 PAGE-ALIGNED RECORDS**.\n\n1. fetch live `main` first;\n2. confirm Part 003 Tamil remains **ARCHIVAL-READY / CLOSED**, English source-check remains **111/111 COMPLETE / CLOSED**, and GR1 remains **33/111 COMPLETE**;\n3. read `translations/en/GLOSSARY.md` and the relevant English/Tamil records;\n4. compare recurring names, work/section names, controlled literary terms, publication names, chapter labels, citation metadata and repeated English renderings against the glossary and audited Tamil context;\n5. update `GLOSSARY.md` only for terms actually evidenced in Part 003;\n6. do not mechanically force one English word where context requires another rendering;\n7. do not import standard/published/web English wording or terminology from memory;\n8. this gate does **not** promote `source-checked` pages to `editorial-reviewed`;\n9. do not alter Tamil files;\n10. do not begin editorial review during GR2;\n11. update `TRANSLATION_STATUS.md` and audit the exact changed-file set.\n\nIf GR2 passes, cumulative glossary reconciliation becomes **66/111**. External **333→334** remains deferred until Part 004 source intake. Part 004 remains blocked until the maintained English workflow and final Part closure checkpoint are complete.\n''',
    'work HANDOVER frontier'
)

# Next-chat prompt.
replace_tail(
    Path('NEXT_CHAT_PROMPT_KURALOVIYAM.md'),
    '## Exact next activity — Part 003 English Glossary Reconciliation GR1\n',
    '''## Glossary reconciliation results through GR1 — COMPLETE / PASS\n\n- GR1 **223–255 / printed 206–238 — 33/33 PASS**;\n- cumulative glossary reconciliation **33/111**;\n- current English page state remains **111 source-checked / 0 draft / 0 source-limited / 0 blocked**;\n- GR1 page wording changes **0**; page status changes **0**; Tamil changes **0**.\n\nGR1 verified all 20 Chapter/Kural metadata lines in its range and added six Part-003-first chapter controls: **Folly**, **Forbearance**, **Women of Mercenary Love**, **Hospitality**, **Abstaining from Liquor**, and **Agriculture**. It also maps source variant `நலம்புனைந்துரைத்தல்` to **Praising Her Beauty** and records `ஊடல்` contextually as **lovers' quarrel / sulking**.\n\n## Exact next activity — Part 003 English Glossary Reconciliation GR2\n\nProcess **scans 256–288 / printed 239–271 — 33 page-aligned records**.\n\nRequirements:\n\n1. fetch live `main` first and preserve newer durable work;\n2. confirm `PART_003_TAMIL_ARCHIVAL_READY.md` remains **PASS / CLOSED**;\n3. confirm `translations/en/TRANSLATION_STATUS.md` records source-check **111/111 COMPLETE / CLOSED** and glossary reconciliation **33/111**;\n4. read `translations/en/GLOSSARY.md` and English records **0256–0288** with their matching audited Tamil records;\n5. reconcile recurring names, work/section names, controlled literary terms, publication names, chapter labels, citation metadata and repeated English renderings against the glossary and audited Tamil context;\n6. update `GLOSSARY.md` only for terms actually evidenced in Part 003;\n7. do not mechanically force one English rendering where context requires a different one;\n8. do not import standard/published/web English Kural wording, another edition's terminology, or memory;\n9. this gate does **not** promote `source-checked` pages to `editorial-reviewed`;\n10. do not alter any Tamil page record or Tamil metadata;\n11. do not begin editorial review during GR2;\n12. update `translations/en/TRANSLATION_STATUS.md` and audit the exact changed-file set before advancing.\n\nIf GR2 passes, cumulative glossary reconciliation becomes **66/111**. Part 004 remains blocked until Part 003 completes glossary reconciliation, editorial review, Part review, release report/release-ready synchronization and final Part closure. External **333→334** remains deferred until Part 004 source intake.\n''',
    'NEXT_CHAT frontier'
)

# Work README was stale from the pre-English frontier; synchronize current state.
replace_tail(
    ROOT / 'README.md',
    '## Current frontier\n',
    '''## Current durable state\n\n- Part 003 Tamil: **ARCHIVAL-READY / CLOSED — 111 textual verified + 111 visual verified / 0 exceptions**;\n- Part 003 English drafting: **111/111 COMPLETE / CLOSED**;\n- Part 003 English source-check: **111/111 COMPLETE / CLOSED**;\n- Part 003 English glossary reconciliation: **IN PROGRESS — GR1 COMPLETE 33/111**;\n- all 111 English pages remain `source-checked`; editorial review has not started.\n\n## Current frontier\n\n**Next activity: Part 003 English glossary reconciliation GR2 — scans 256–288 / printed 239–271, 33 pages.** Reconcile recurring terminology, names, chapter labels and citation metadata against `translations/en/GLOSSARY.md` and the audited Tamil context. The glossary gate does not promote English page statuses. Do not alter closed Tamil records or begin editorial review. External **333→334** remains deferred until Part 004 source intake.\n''',
    'work README stale frontier'
)

# Source/provenance metadata live state.
replace_once(
    ROOT / 'metadata/source.md',
    '| 003 | 223–333 | 111 | `TVA_BOK_0065733_குறளோவியம்_part_003_pages_223-333.pdf` | **supplied; source intake + Pass 1 + Pass 2A + Pass 2B + Pass 3 COMPLETE; audit PASS; final status sync PASS / CLOSED; documentation sync COMPLETE; Tamil archival-ready NEXT** |',
    '| 003 | 223–333 | 111 | `TVA_BOK_0065733_குறளோவியம்_part_003_pages_223-333.pdf` | **supplied; Tamil ARCHIVAL-READY / CLOSED; English drafting + source-check COMPLETE / CLOSED; glossary reconciliation IN PROGRESS — GR1 33/111 COMPLETE** |',
    'metadata source table'
)
replace_once(
    ROOT / 'metadata/source.md',
    'Historical Part-003 Pass-1 cadence was **11 physical scans per normal iteration**, followed by a one-page final remainder at scan 333. Pass 1, Pass 2A, Pass 2B and Pass 3 are now complete; the Part audit passed; final metadata/status synchronization closed all 111 records as textual and visual `verified`; documentation synchronization is complete. The next gate is the separate Tamil archival-ready checkpoint.',
    'Historical Part-003 Pass-1 cadence was **11 physical scans per normal iteration**, followed by a one-page final remainder at scan 333. Pass 1, Pass 2A, Pass 2B and Pass 3 are complete; the Part audit passed; final metadata/status synchronization closed all 111 records as textual and visual `verified`; documentation synchronization and the separate Tamil archival-ready checkpoint are closed. The maintained English layer has completed first-pass drafting **111/111** and source-check **111/111**; glossary reconciliation is now in progress with **GR1 scans 223–255 / printed 206–238 COMPLETE 33/33**, cumulative **33/111**.',
    'metadata source Part003 state'
)

# Page-map current inventory sentence was stale after the status gate.
replace_once(
    ROOT / 'indexes/page-map.md',
    'Current Part 003 Pass-1 inventory: **111 / 111 records captured — scans 223–333 / printed 206–316**. All remain `needs-review` / `visual_fidelity: needs-review` pending final metadata/status synchronization.',
    'Current Part 003 archival inventory: **111 / 111 records — scans 223–333 / printed 206–316**. Final metadata/status synchronization set all records to `status: "verified"` / `visual_fidelity: "verified"`; Tamil is **ARCHIVAL-READY / CLOSED** with 0 exceptions.',
    'page-map current inventory'
)

# Root handover: preserve unrelated Sangath Tamil material, but synchronize Kuraloviyam live frontier.
replace_once(
    Path('HANDOVER.md'),
    'Last refreshed for Kuraloviyam **Part 003 documentation synchronization COMPLETE — 111/111 textual + visual verified; Tamil archival-ready checkpoint next**: **2026-09-10**. Sangath Tamil workflow state below is retained from its latest dedicated handover and live `main` remains authoritative.',
    'Last refreshed for Kuraloviyam **Part 003 Tamil ARCHIVAL-READY / CLOSED; English drafting + source-check CLOSED; glossary GR1 COMPLETE 33/111, GR2 next**: **2026-09-10**. Sangath Tamil workflow state below is retained from its latest dedicated handover and live `main` remains authoritative.',
    'root HANDOVER header'
)
replace_tail(
    Path('HANDOVER.md'),
    '# Exact next activity — குறளோவியம்\n',
    '''# Part 003 maintained English state — குறளோவியம்\n\n- Tamil: **ARCHIVAL-READY / CLOSED — 111 textual verified + 111 visual verified / 0 exceptions**;\n- English first-pass drafting: **111/111 COMPLETE / CLOSED**;\n- English source-check: **111/111 COMPLETE / CLOSED**;\n- English glossary reconciliation: **IN PROGRESS — GR1 scans 223–255 / printed 206–238 COMPLETE / PASS 33/33**;\n- cumulative glossary reconciliation: **33/111**;\n- all 111 English pages remain `source-checked`; editorial review is not started;\n- GR1 changed no English page wording or status and no Tamil record.\n\n# Exact next activity — குறளோவியம்\n\nPerform **Part 003 English Glossary Reconciliation GR2 — scans 256–288 / printed 239–271, 33 pages**.\n\n1. fetch live `main`;\n2. read the Kuraloviyam mandatory controls, English `TRANSLATION_GUIDE.md`, `TRANSLATION_STATUS.md`, and `GLOSSARY.md`;\n3. confirm Tamil remains closed, source-check remains 111/111 closed, and GR1 remains 33/111 complete;\n4. reconcile recurring names, structural/literary terms, chapter labels, citation metadata and repeated renderings against the audited Tamil context;\n5. update the glossary only for source-evidenced terms;\n6. do not import external/published/web terminology or remembered Kural wording;\n7. do not promote page statuses or begin editorial review during GR2;\n8. do not alter Tamil records;\n9. audit the exact changed-file set before advancing.\n\nIf GR2 passes, cumulative glossary reconciliation becomes **66/111**. Part 004 remains blocked until the maintained Part-003 English workflow and final Part closure checkpoint are complete. External **333→334** remains deferred until Part 004 source intake.\n''',
    'root HANDOVER Kural frontier'
)

expected = {
    'HANDOVER.md',
    'NEXT_CHAT_PROMPT_KURALOVIYAM.md',
    'works/kuraloviyam/HANDOVER.md',
    'works/kuraloviyam/README.md',
    'works/kuraloviyam/indexes/page-map.md',
    'works/kuraloviyam/metadata/source.md',
    'works/kuraloviyam/translations/en/GLOSSARY.md',
    'works/kuraloviyam/translations/en/README.md',
    'works/kuraloviyam/translations/en/TRANSLATION_STATUS.md',
}
changed = set(subprocess.check_output(['git', 'diff', '--name-only'], text=True).splitlines())
if changed != expected:
    raise SystemExit(f'GR1 durable changed-file audit failed: expected={sorted(expected)} actual={sorted(changed)} delta={sorted(expected ^ changed)}')
if any(p.startswith('works/kuraloviyam/pages/') or p.startswith('works/kuraloviyam/translations/en/pages/') for p in changed):
    raise SystemExit('GR1 unexpectedly changed a page record')
print('GR1 completion validation PASS')
print('\n'.join(sorted(changed)))
