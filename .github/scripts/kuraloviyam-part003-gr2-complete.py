from pathlib import Path
import re

ROOT = Path('works/kuraloviyam')
ENROOT = ROOT / 'translations/en'


def read(p):
    return Path(p).read_text(encoding='utf-8')


def write(p, s):
    Path(p).write_text(s, encoding='utf-8')


def replace_once(path, old, new, label):
    p = Path(path)
    s = p.read_text(encoding='utf-8')
    n = s.count(old)
    if n != 1:
        raise SystemExit(f'{label}: expected 1 occurrence, found {n}')
    p.write_text(s.replace(old, new, 1), encoding='utf-8')


def replace_regex(path, pattern, replacement, label, flags=re.S):
    p = Path(path)
    s = p.read_text(encoding='utf-8')
    ns, n = re.subn(pattern, replacement, s, count=1, flags=flags)
    if n != 1:
        raise SystemExit(f'{label}: regex replacement count={n}')
    p.write_text(ns, encoding='utf-8')

# Gate preconditions: Tamil stays closed; all active English pages remain source-checked.
arch = read(ROOT / 'PART_003_TAMIL_ARCHIVAL_READY.md')
if 'PART 003 TAMIL ARCHIVAL-READY — PASS / CLOSED' not in arch:
    raise SystemExit('Tamil archival-ready precondition failed')
for scan in range(256, 289):
    printed = scan - 17
    ta = ROOT / 'pages' / f'{scan:04d}-kuraloviyam-{printed}.md'
    en = ENROOT / 'pages' / f'{scan:04d}-kuraloviyam-{printed}.md'
    if not ta.exists() or not en.exists():
        raise SystemExit(f'missing GR2 page pair {scan}')
    tt = ta.read_text(encoding='utf-8')
    et = en.read_text(encoding='utf-8')
    if 'status: "verified"' not in tt or 'visual_fidelity: "verified"' not in tt:
        raise SystemExit(f'Tamil closed-state precondition failed {scan}')
    if et.count('status: "source-checked"') != 1 or et.count('source_tamil_status: "verified"') != 1:
        raise SystemExit(f'English source-check precondition failed {scan}')

findings = read('.github/tmp/kuraloviyam-part003-gr2-findings.txt')
if 'CHAPTER / CONTROL FLAGS: 0' not in findings:
    raise SystemExit('GR2 audit contains chapter/control flags')

G = ENROOT / 'GLOSSARY.md'

# Context-aware term refinements evidenced in GR2.
replace_once(
    G,
    '| பாவம் / புண்ணியம் | sin / merit | Preserve the contrast when the source discusses the palanquin interpretation on scans 50–51; do not infer doctrine beyond the audited passage. |',
    '| பாவம் | sin / poor thing / alas | Context-aware. Use **sin** in the conceptual/ethical sense; Part 003 GR2 scans 267, 275 and 279 use the exclamatory/pity sense naturally rendered **poor thing** or **alas**. |\n| புண்ணியம் | merit | Preserve the ethical contrast with `பாவம்` where the source explicitly pairs the concepts, as in scans 50–51. |',
    'glossary paavam refinement'
)
replace_once(
    G,
    '| தேன்மொழி | Thenmozhi | Married woman named in the scan 92 vignette. |',
    '| தேன்மொழி | Thenmozhi / honey-voiced | Context-aware. `தேன்மொழி` is the married woman\'s name in scan 92; Part 003 scan 275 uses it descriptively in `தேன்மொழி பொருத்தி`, rendered naturally as **honey-voiced woman** rather than forcing the personal-name form. |',
    'glossary Thenmozhi refinement'
)
replace_once(
    G,
    '| புணர்ச்சி மகிழ்தல் | The Joy of Union | Chapter 111 label on scan 55. |',
    '| புணர்ச்சி மகிழ்தல் | The Joy of Union / joy of union | **The Joy of Union** is the controlled Chapter 111 title (scan 55; reused later). Part 003 scan 282 uses the same words descriptively in prose, where lowercase **joy of union** is natural. |',
    'glossary union refinement'
)

# Source-form variants mapped to established chapter controls.
replace_once(
    G,
    '| காதற் சிறப்புரைத்தல் | Declaring Love\'s Excellence | Chapter 113 label on scan 71. |',
    '| காதற் சிறப்புரைத்தல் / காதற்சிறப்புரைத்தல் | Declaring Love\'s Excellence | Chapter 113; scan 71 uses the spaced form and Part 003 scan 259 uses the closed source form `காதற்சிறப்புரைத்தல்`. |',
    'chapter 113 source variant'
)
replace_once(
    G,
    '| கனவு நிலையுரைத்தல் / கனவுநிலையுரைத்தல் | Speaking of the Dream State | Chapter 122; source spacing variants occur on scans 63 and 86. Part 001 GR6 reconciled scan 86 to this controlled English label. |',
    '| கனவு நிலையுரைத்தல் / கனவுநிலையுரைத்தல் / கனவுநிலை உரைத்தல் | Speaking of the Dream State | Chapter 122; source spacing variants occur on scans 63 and 86, and Part 003 scan 267 carries `கனவுநிலை உரைத்தல்`. All map to the same controlled label. |',
    'chapter 122 source variant'
)
replace_once(
    G,
    '| அவர்வயின் விதும்பல் | Longing for His Return | Chapter 127 label on scan 108. |',
    '| அவர்வயின் விதும்பல் / அவர்வயின்விதும்பல் | Longing for His Return | Chapter 127; scan 108 uses the spaced form and Part 003 scan 275 carries the closed source form `அவர்வயின்விதும்பல்`. |',
    'chapter 127 source variant'
)

# Extend the Part-003 chapter-control table through GR2.
replace_once(
    G,
    '## Thirukkural chapter labels first encountered in Part 003 through GR1',
    '## Thirukkural chapter labels first encountered in Part 003 through GR2',
    'Part003 chapter heading'
)
replace_once(
    G,
    '| உழவு | Agriculture | Chapter 104 label on scans 244 and 253. |\n\nThe Chapter 112 source variant',
    '| உழவு | Agriculture | Chapter 104 label on scans 244 and 253. |\n| நல்குரவு | Poverty | Chapter 105 label on scan 257. |\n| அடக்கமுடைமை | Self-Control | Chapter 13 label on scan 261. |\n| நாணுத் துறவுரைத்தல் | Renouncing Modesty | Chapter 114 label on scan 263. |\n| ஒழுக்கமுடைமை | Good Conduct | Chapter 14 label on scan 273. |\n| வலியறிதல் | Knowing One\'s Strength | Chapter 48 label on scan 277. |\n| பெரியாரைத் துணைக்கோடல் | Seeking the Support of the Great | Chapter 45 label on scan 285. |\n\nThe Chapter 112 source variant',
    'Part003 GR2 chapter rows'
)

# Add source-evidenced narrative/literary names and the GR2 durable record immediately before the review rule.
marker = '## Review rule\n'
g = G.read_text(encoding='utf-8')
if g.count(marker) != 1:
    raise SystemExit('glossary review-rule marker mismatch')
insert = '''## People / role / literary references first encountered in Part 003 through GR2\n\n| Tamil | Default English form | Editorial note |\n|---|---|---|\n| அழகன் | Alagan | Orphan/warrior character across scans 260–261. |\n| நல்லான் | Nallaan | Traveller/friend in the bear vignette across scans 264–265. |\n| வல்லான் | Vallaan | Nallaan's companion in the bear vignette across scans 264–265. |\n| இளமதி | Ilamathi | Young goldsmith in the lovers' quarrel vignette across scans 270–271. |\n| திருமதி | Thirumathi | Ilamathi's wife and named character across scans 270–271; do not mechanically treat the same Tamil form as a generic honorific outside this vignette. |\n| பாகவதர் | Bhagavathar | Ramayana kathakalakshepam performer/role across scans 272–273; retain the source-checked transliteration in this narrative context. |\n| இராமன் | Rama | Ramayana figure named in scan 272. |\n| சீதை | Sita | Ramayana figure named in scans 272–273. |\n| இலக்குவன் | Lakshmana | Ramayana figure named in scan 272. |\n| இராவணன் | Ravana | Ramayana figure named in scan 272. |\n| கிள்ளி | Killi | Friend/husband character across scans 278–279. |\n| நல்லி | Nalli | Killi's friend across scans 278–279. |\n\n## Part 003 GR2 reconciliation record — scans 256–288\n\nGR2 processed **33 consecutive pages: scans 256–288 / printed 239–271**.\n\n- scans **256–288** — glossary / recurring-terminology reconciliation **PASS, 33/33**;\n- all **16** Chapter/Kural metadata records in the range were checked against their audited Tamil counterparts with **0 chapter-number, Kural-number, or controlled-label mismatches**;\n- source-evidenced Part-003-first chapter controls added in this gate: **Poverty**, **Self-Control**, **Renouncing Modesty**, **Good Conduct**, **Knowing One's Strength**, and **Seeking the Support of the Great**;\n- source variants `காதற்சிறப்புரைத்தல்`, `கனவுநிலை உரைத்தல்`, and `அவர்வயின்விதும்பல்` are mapped to the established controls **Declaring Love's Excellence**, **Speaking of the Dream State**, and **Longing for His Return** rather than creating duplicate English chapter titles;\n- recurring narrative/literary forms established in this range include **Alagan**, **Nallaan**, **Vallaan**, **Ilamathi**, **Thirumathi**, **Bhagavathar**, **Rama**, **Sita**, **Lakshmana**, **Ravana**, **Killi**, and **Nalli**;\n- `பாவம்` is now explicitly context-aware: ethical **sin** versus the GR2 narrative exclamation **poor thing / alas**; `தேன்மொழி` remains **Thenmozhi** when it is the scan-92 personal name but is descriptive **honey-voiced** on scan 275;\n- scan **282** uses `புணர்ச்சி மகிழ்தல்` descriptively as **joy of union**, while the controlled Chapter 111 title remains **The Joy of Union**;\n- English page wording corrections required solely for GR2 terminology consistency: **none**;\n- all 33 English pages remain `source-checked`; this gate makes **no status promotion**;\n- no Tamil archival record changed and no external/published/web English terminology was imported.\n\n'''
G.write_text(g.replace(marker, insert + marker, 1), encoding='utf-8')

# Authoritative status: close GR2 and advance to GR3.
status_path = ENROOT / 'TRANSLATION_STATUS.md'
status = status_path.read_text(encoding='utf-8')
pattern = r'## Part 003 English glossary reconciliation — IN PROGRESS\n.*\Z'
replacement = '''## Part 003 English glossary reconciliation — IN PROGRESS\n\n- **GR1: scans 223–255 / printed 206–238 — COMPLETE / PASS 33/33**;\n- **GR2: scans 256–288 / printed 239–271 — COMPLETE / PASS 33/33**;\n- cumulative glossary reconciliation: **66/111**;\n- remaining glossary-reconciliation pages: **45**;\n- English page state remains **111 `source-checked` / 0 `draft` / 0 source-limited / 0 blocked**;\n- English page wording changes during GR1+GR2: **0**;\n- page status changes during GR1+GR2: **0**;\n- Tamil page / metadata changes during GR1+GR2: **0**.\n\nGR2 checked all **16** Chapter/Kural metadata records in scans **256–288** with **0 numeric or controlled-label mismatches**. Six Part-003-first chapter controls were added: **Poverty**, **Self-Control**, **Renouncing Modesty**, **Good Conduct**, **Knowing One's Strength**, and **Seeking the Support of the Great**. Existing controls were extended to the source forms `காதற்சிறப்புரைத்தல்`, `கனவுநிலை உரைத்தல்`, and `அவர்வயின்விதும்பல்`. Contextual controls were refined for `பாவம்`, `தேன்மொழி`, and descriptive `புணர்ச்சி மகிழ்தல்`, and recurring GR2 narrative/literary names were recorded. No English page wording required correction.\n\n## Current frontier — Part 003 English glossary reconciliation GR3\n\nExact next activity: **glossary / recurring-terminology reconciliation scans 289–321 / printed 272–304 — 33 page-aligned records**.\n\nCompare recurring names, work/section names, controlled literary terms, publication names, chapter labels, citation metadata and repeated English renderings against `GLOSSARY.md` and audited Tamil context. Update `GLOSSARY.md` only for terms actually evidenced in the active source. Do not mechanically force one English word where context requires a different rendering, and do not import terminology from external editions, web sources or memory.\n\nThis gate does **not** promote `source-checked` pages to `editorial-reviewed`; passing pages remain `source-checked` until the later editorial-review gate. If GR3 passes, cumulative glossary reconciliation becomes **99/111**, leaving the final **12-page GR4 remainder scans 322–333 / printed 305–316**. Do not begin editorial review during GR3.\n\nPart 004 remains blocked until Part 003 completes glossary reconciliation, editorial review, Part review, release report/release-ready synchronization and the final Part closure checkpoint.\n'''
ns, n = re.subn(pattern, replacement, status, count=1, flags=re.S)
if n != 1:
    raise SystemExit(f'TRANSLATION_STATUS tail replacement count={n}')
status_path.write_text(ns, encoding='utf-8')

# English README current progress/frontier.
replace_regex(
    ENROOT / 'README.md',
    r'## Part 003 English glossary reconciliation — IN PROGRESS\n.*?See `TRANSLATION_STATUS.md` for the authoritative detailed frontier\.\n?',
    '''## Part 003 English glossary reconciliation — IN PROGRESS\n\n- GR1 **223–255 / 206–238 — COMPLETE / PASS 33/33**;\n- GR2 **256–288 / 239–271 — COMPLETE / PASS 33/33**;\n- cumulative glossary reconciliation: **66/111**;\n- English pages remain **111 `source-checked`**; GR1+GR2 made **0 page wording changes and 0 status changes**.\n\nGR2 added the Part-003-first chapter controls **Poverty**, **Self-Control**, **Renouncing Modesty**, **Good Conduct**, **Knowing One's Strength**, and **Seeking the Support of the Great**; mapped three source-form variants to existing chapter controls; refined context for `பாவம்`, `தேன்மொழி`, and descriptive `புணர்ச்சி மகிழ்தல்`; and recorded recurring GR2 narrative/literary names. No Tamil archival record changed.\n\n## Current frontier\n\nExact next activity: **Part 003 English glossary reconciliation GR3 — scans 289–321 / printed 272–304, 33 pages**.\n\nUse `GLOSSARY.md` and audited Tamil context to reconcile recurring names, literary/structural terms, publication names, chapter labels, citation metadata and repeated English renderings. Add glossary entries only when evidenced in the active source. This gate does **not** promote pages to `editorial-reviewed`; pages remain `source-checked` until editorial review.\n\nIf GR3 passes, cumulative glossary reconciliation becomes **99/111** and the final GR4 remainder is **scans 322–333 / printed 305–316, 12 pages**. Part 004 remains blocked until the maintained Part-003 English workflow and final Part closure checkpoint are complete.\n\nSee `TRANSLATION_STATUS.md` for the authoritative detailed frontier.\n''',
    'English README GR2 sync'
)

# Work handover: replace glossary/current-frontier tail.
replace_regex(
    ROOT / 'HANDOVER.md',
    r'## Glossary reconciliation progress — GR1 COMPLETE / PASS 33/111\n.*\Z',
    '''## Glossary reconciliation progress — GR2 COMPLETE / PASS 66/111\n\n- GR1 **223–255 / printed 206–238 — COMPLETE / PASS 33/33**;\n- GR2 **256–288 / printed 239–271 — COMPLETE / PASS 33/33**;\n- cumulative glossary reconciliation: **66/111**;\n- all English pages remain `source-checked`; GR1+GR2 made **0 English page wording changes / 0 status changes**;\n- GR2 checked all **16** Chapter/Kural metadata records with **0 numeric or controlled-label mismatches**;\n- six Part-003-first chapter controls were added in GR2: **Poverty**, **Self-Control**, **Renouncing Modesty**, **Good Conduct**, **Knowing One's Strength**, **Seeking the Support of the Great**;\n- source-form variants and contextual controls for `பாவம்`, `தேன்மொழி`, and descriptive `புணர்ச்சி மகிழ்தல்` were reconciled without changing page wording;\n- recurring GR2 narrative/literary names were recorded;\n- no Tamil file or metadata changed.\n\n## Exact next activity — English Glossary Reconciliation GR3\n\nProcess **scans 289–321 / printed 272–304 — 33 PAGE-ALIGNED RECORDS**.\n\n1. fetch live `main` first;\n2. confirm Part 003 Tamil remains **ARCHIVAL-READY / CLOSED**, English source-check remains **111/111 COMPLETE / CLOSED**, and glossary reconciliation remains **66/111 COMPLETE**;\n3. read `translations/en/GLOSSARY.md` and the matching English/Tamil records **0289–0321**;\n4. compare recurring names, work/section names, controlled literary terms, publication names, chapter labels, citation metadata and repeated English renderings against the glossary and audited Tamil context;\n5. update `GLOSSARY.md` only for terms actually evidenced in Part 003;\n6. do not mechanically force one English word where context requires another rendering;\n7. do not import standard/published/web English wording or terminology from memory;\n8. this gate does **not** promote `source-checked` pages to `editorial-reviewed`;\n9. do not alter Tamil files;\n10. do not begin editorial review during GR3;\n11. update `TRANSLATION_STATUS.md` and audit the exact changed-file set.\n\nIf GR3 passes, cumulative glossary reconciliation becomes **99/111** and GR4 is the final **12-page remainder scans 322–333 / printed 305–316**. External **333→334** remains deferred until Part 004 source intake. Part 004 remains blocked until the maintained English workflow and final Part closure checkpoint are complete.\n''',
    'work handover GR2 sync'
)

# Next-chat prompt: replace GR1 results / GR2-next tail.
replace_regex(
    'NEXT_CHAT_PROMPT_KURALOVIYAM.md',
    r'## Glossary reconciliation results through GR1 — COMPLETE / PASS\n.*\Z',
    '''## Glossary reconciliation results through GR2 — COMPLETE / PASS\n\n- GR1 **223–255 / printed 206–238 — 33/33 PASS**;\n- GR2 **256–288 / printed 239–271 — 33/33 PASS**;\n- cumulative glossary reconciliation **66/111**;\n- current English page state remains **111 source-checked / 0 draft / 0 source-limited / 0 blocked**;\n- GR1+GR2 page wording changes **0**; page status changes **0**; Tamil changes **0**.\n\nGR2 verified all 16 Chapter/Kural metadata records in its range with 0 numeric or controlled-label mismatch. It added six Part-003-first chapter controls, mapped the GR2 source-form variants to established labels, refined contextual handling of `பாவம்`, `தேன்மொழி`, and descriptive `புணர்ச்சி மகிழ்தல்`, and recorded the recurring GR2 narrative/literary names.\n\n## Exact next activity — Part 003 English Glossary Reconciliation GR3\n\nProcess **scans 289–321 / printed 272–304 — 33 page-aligned records**.\n\nRequirements:\n\n1. fetch live `main` first and preserve newer durable work;\n2. confirm `PART_003_TAMIL_ARCHIVAL_READY.md` remains **PASS / CLOSED**;\n3. confirm `translations/en/TRANSLATION_STATUS.md` records source-check **111/111 COMPLETE / CLOSED** and glossary reconciliation **66/111**;\n4. read `translations/en/GLOSSARY.md` and English records **0289–0321** with their matching audited Tamil records;\n5. reconcile recurring names, work/section names, controlled literary terms, publication names, chapter labels, citation metadata and repeated English renderings against the glossary and audited Tamil context;\n6. update `GLOSSARY.md` only for terms actually evidenced in Part 003;\n7. do not mechanically force one English rendering where context requires a different one;\n8. do not import standard/published/web English Kural wording, another edition's terminology, or memory;\n9. this gate does **not** promote `source-checked` pages to `editorial-reviewed`;\n10. do not alter any Tamil page record or Tamil metadata;\n11. do not begin editorial review during GR3;\n12. update `translations/en/TRANSLATION_STATUS.md` and audit the exact changed-file set before advancing.\n\nIf GR3 passes, cumulative glossary reconciliation becomes **99/111**. GR4 is then the final **12-page remainder scans 322–333 / printed 305–316**. Part 004 remains blocked until Part 003 completes glossary reconciliation, editorial review, Part review, release report/release-ready synchronization and final Part closure. External **333→334** remains deferred until Part 004 source intake.\n''',
    'next prompt GR2 sync'
)

# Root handover maintained-English state and exact next activity.
replace_regex(
    'HANDOVER.md',
    r'# Part 003 maintained English state — குறளோவியம்\n.*\Z',
    '''# Part 003 maintained English state — குறளோவியம்\n\n- Tamil: **ARCHIVAL-READY / CLOSED — 111 textual verified + 111 visual verified / 0 exceptions**;\n- English first-pass drafting: **111/111 COMPLETE / CLOSED**;\n- English source-check: **111/111 COMPLETE / CLOSED**;\n- English glossary reconciliation: **IN PROGRESS — GR1 + GR2 COMPLETE / PASS, 66/111**;\n- all 111 English pages remain `source-checked`; editorial review is not started;\n- GR1+GR2 changed no English page wording or status and no Tamil record.\n\n# Exact next activity — குறளோவியம்\n\nPerform **Part 003 English Glossary Reconciliation GR3 — scans 289–321 / printed 272–304, 33 pages**.\n\n1. fetch live `main`;\n2. read the Kuraloviyam mandatory controls, English `TRANSLATION_GUIDE.md`, `TRANSLATION_STATUS.md`, and `GLOSSARY.md`;\n3. confirm Tamil remains closed, source-check remains 111/111 closed, and glossary reconciliation remains 66/111 complete;\n4. reconcile recurring names, structural/literary terms, chapter labels, citation metadata and repeated renderings against the audited Tamil context;\n5. update the glossary only for source-evidenced terms;\n6. do not import external/published/web terminology or remembered Kural wording;\n7. do not promote page statuses or begin editorial review during GR3;\n8. do not alter Tamil records;\n9. audit the exact changed-file set before advancing.\n\nIf GR3 passes, cumulative glossary reconciliation becomes **99/111**; GR4 is the final **12-page remainder scans 322–333 / printed 305–316**. Part 004 remains blocked until the maintained Part-003 English workflow and final Part closure checkpoint are complete. External **333→334** remains deferred until Part 004 source intake.\n''',
    'root handover GR2 sync'
)

# Work README live table/header/frontier only; preserve historical pass records.
replace_once(
    ROOT / 'README.md',
    '| 003 | 223–333 | **source intake + Pass 1 + Pass 2A + Pass 2B + Pass 3 COMPLETE — 111/111; Part audit PASS; final metadata/status sync PASS / CLOSED — 111/111 textual + visual verified; documentation sync COMPLETE; Tamil archival-ready NEXT** |',
    '| 003 | 223–333 | **Tamil ARCHIVAL-READY / CLOSED; English drafting + source-check COMPLETE / CLOSED; glossary reconciliation IN PROGRESS — GR1 + GR2 COMPLETE / PASS, 66/111; GR3 next** |',
    'work README Part003 table row'
)
replace_once(
    ROOT / 'README.md',
    '## Part 003 — SOURCE INTAKE + PASS 1 + PASS 2A + PASS 2B + PASS 3 COMPLETE / AUDIT PASS / FINAL STATUS SYNC PASS / DOCUMENTATION SYNC COMPLETE / TAMIL ARCHIVAL-READY NEXT',
    '## Part 003 — TAMIL ARCHIVAL-READY / CLOSED; ENGLISH DRAFTING + SOURCE-CHECK CLOSED; GLOSSARY RECONCILIATION IN PROGRESS',
    'work README Part003 heading'
)
replace_regex(
    ROOT / 'README.md',
    r'\*\*Next activity: Part 003 English glossary reconciliation GR2 — scans 256–288 / printed 239–271, 33 pages\.\*\*.*\Z',
    '**Next activity: Part 003 English glossary reconciliation GR3 — scans 289–321 / printed 272–304, 33 pages.** Reconcile recurring terminology, names, chapter labels and citation metadata against `translations/en/GLOSSARY.md` and the audited Tamil context. The glossary gate does not promote English page statuses. Do not alter closed Tamil records or begin editorial review. If GR3 passes, cumulative glossary reconciliation reaches **99/111** and the final GR4 remainder is **scans 322–333 / printed 305–316, 12 pages**. External **333→334** remains deferred until Part 004 source intake.\n',
    'work README frontier'
)

# Source metadata live state.
replace_once(
    ROOT / 'metadata/source.md',
    '| 003 | 223–333 | 111 | `TVA_BOK_0065733_குறளோவியம்_part_003_pages_223-333.pdf` | **supplied; Tamil ARCHIVAL-READY / CLOSED; English drafting + source-check COMPLETE / CLOSED; glossary reconciliation IN PROGRESS — GR1 33/111 COMPLETE** |',
    '| 003 | 223–333 | 111 | `TVA_BOK_0065733_குறளோவியம்_part_003_pages_223-333.pdf` | **supplied; Tamil ARCHIVAL-READY / CLOSED; English drafting + source-check COMPLETE / CLOSED; glossary reconciliation IN PROGRESS — GR1 + GR2 COMPLETE / PASS, 66/111; GR3 next** |',
    'source metadata Part003 table row'
)
replace_once(
    ROOT / 'metadata/source.md',
    'The maintained English layer has completed first-pass drafting **111/111** and source-check **111/111**; glossary reconciliation is now in progress with **GR1 scans 223–255 / printed 206–238 COMPLETE 33/33**, cumulative **33/111**.',
    'The maintained English layer has completed first-pass drafting **111/111** and source-check **111/111**; glossary reconciliation is now in progress with **GR1 scans 223–255 / printed 206–238 COMPLETE 33/33** and **GR2 scans 256–288 / printed 239–271 COMPLETE 33/33**, cumulative **66/111**. The exact next glossary batch is **GR3 scans 289–321 / printed 272–304**.',
    'source metadata English progress'
)

# Page-map live verification/current frontier: fix the stale pre-archival-ready statements.
replace_regex(
    ROOT / 'indexes/page-map.md',
    r'Part 003:\n\n- source intake — \*\*PASS / COMPLETE\*\*;.*\Z',
    '''Part 003:\n\n- source intake — **PASS / COMPLETE**;\n- Pass 1 — **COMPLETE, 111/111 captured through scan 333 / printed 316**;\n- Pass 2A — **COMPLETE, 111/111 verified through scan 333 / printed 316**;\n- Pass 2B — **COMPLETE, 111/111 independently re-read through scan 333 / printed 316**;\n- Pass 3 — **COMPLETE, 111/111 through scan 333 / printed 316**;\n- Part audit — **PASS**;\n- final metadata/status synchronization — **PASS / CLOSED, 111 textual verified + 111 visual verified / 0 exceptions**;\n- documentation synchronization — **COMPLETE**;\n- Tamil archival-ready — **PASS / CLOSED**;\n- English drafting — **111/111 COMPLETE / CLOSED**;\n- English source-check — **111/111 COMPLETE / CLOSED**;\n- English glossary reconciliation — **IN PROGRESS: GR1 + GR2 COMPLETE / PASS, 66/111**;\n- English editorial review / Part review / release — **not-started**.\n\n## Current frontier\n\n**Part 001: CLOSED.**\n\n**Part 002: Tamil + English CLOSED.**\n\n**Part 003: TAMIL ARCHIVAL-READY / CLOSED; ENGLISH DRAFTING + SOURCE-CHECK COMPLETE / CLOSED; GLOSSARY RECONCILIATION IN PROGRESS — GR1 + GR2 COMPLETE / PASS, 66/111.**\n\nExact next activity: **Part 003 English glossary reconciliation GR3 — scans 289–321 / printed 272–304, 33 pages**. If GR3 passes, cumulative glossary reconciliation becomes **99/111** and GR4 is the final **12-page remainder scans 322–333 / printed 305–316**. External **333→334** remains deferred until Part 004 source intake.\n''',
    'page-map live frontier sync'
)

# Work-specific archival guide had a stale Part003 frontier; synchronize only its live frontier section.
replace_regex(
    'KURALOVIYAM_ARCHIVAL_GUIDELINES.md',
    r'### Part 003 — overall scans 223–333\n.*\Z',
    '''### Part 003 — overall scans 223–333\n\nControlling source: `TVA_BOK_0065733_குறளோவியம்_part_003_pages_223-333.pdf`.\n\n- Tamil source intake / Pass 1 / Pass 2A / Pass 2B / Pass 3 / audit / final metadata-status sync / documentation sync: **COMPLETE / PASS**;\n- Tamil archival-ready checkpoint: **PASS / CLOSED — 111 textual verified + 111 visual verified / 0 exceptions**;\n- incoming **222→223: CLEAN**; internal **332→333** genuine continuation closes within the Part; external **333→334** remains deferred until Part 004 intake;\n- project-created English drafting: **111/111 COMPLETE / CLOSED**;\n- English source-check: **111/111 COMPLETE / CLOSED**;\n- English glossary reconciliation: **IN PROGRESS — GR1 + GR2 COMPLETE / PASS, 66/111**;\n- all English pages remain `source-checked`; editorial review / Part review / release are not started.\n\n### Exact next content stage\n\nPerform **Part 003 English glossary reconciliation GR3 — scans 289–321 / printed 272–304, 33 page-aligned records**. Use the audited Tamil records and `GLOSSARY.md`; add or refine only source-evidenced terminology; do not import external/published/web wording; do not promote English statuses or begin editorial review; do not alter closed Tamil records.\n\nIf GR3 passes, cumulative glossary reconciliation becomes **99/111** and the final GR4 remainder is **scans 322–333 / printed 305–316, 12 pages**. Part 004 remains blocked until the maintained Part-003 English workflow and final Part closure checkpoint are complete.\n''',
    'archival guide live frontier sync'
)

print('GR2 completion updates prepared successfully')
