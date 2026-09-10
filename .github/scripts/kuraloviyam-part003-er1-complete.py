from pathlib import Path
import re

ROOT = Path('works/kuraloviyam')
EN = ROOT / 'translations/en'


def replace_once(text, old, new, label):
    n = text.count(old)
    if n != 1:
        raise SystemExit(f'{label}: expected exactly 1 occurrence, found {n}: {old[:140]!r}')
    return text.replace(old, new, 1)


def replace_if_present(text, old, new):
    return text.replace(old, new) if old in text else text

# 1. Editorial-review the exact ER1 page range.
for scan in range(223, 256):
    printed = scan - 17
    p = EN / 'pages' / f'{scan:04d}-kuraloviyam-{printed}.md'
    if not p.exists():
        raise SystemExit(f'missing ER1 page {p}')
    s = p.read_text(encoding='utf-8')
    if s.count('status: "source-checked"') != 1:
        raise SystemExit(f'{p}: expected one source-checked status')
    if s.count('source_tamil_status: "verified"') != 1:
        raise SystemExit(f'{p}: source Tamil state not verified')
    s = s.replace('status: "source-checked"', 'status: "editorial-reviewed"', 1)

    if scan == 246:
        s = replace_once(
            s,
            'In bodily union my husband carries me into a very realm of pleasure.',
            'In bodily union my husband carries me into the very realm of pleasure.',
            'scan 246 editorial wording',
        )
    elif scan == 251:
        s = replace_once(
            s,
            "Through two lovers who spent the entire night embraced without even an embrace's breadth of space between them, reaching the peak of pleasure and returning, Valluvar also makes them tell us how lovers' quarrel itself ran away.",
            "Valluvar also has two lovers—who spent the entire night embraced without even the slightest space between them, reaching the peak of pleasure and returning—tell us how lovers' quarrel itself ran away.",
            'scan 251 editorial wording',
        )
    elif scan == 255:
        s = replace_once(
            s,
            '“Woman! Unmarried maiden! Even if you protect the door called restraint by placing me upon it as the bolt called modesty, one day the axe called desire will break that door open.”',
            '“Woman! Unmarried maiden! Even if you guard the door called chastity by using me as the bolt called modesty, one day the axe called desire will break that door open.”',
            'scan 255 fidelity/editorial wording',
        )
    p.write_text(s, encoding='utf-8')

# 2. Authoritative English status.
sp = EN / 'TRANSLATION_STATUS.md'
s = sp.read_text(encoding='utf-8')
s = replace_once(s, '- editorial review: **not-started**;', '- editorial review: **IN PROGRESS — ER1 COMPLETE / PASS 33/111**;', 'status summary editorial state')

front = '## Current frontier — Part 003 English Editorial Review ER1\n\nExact next activity: **editorial review scans 223–255 / printed 206–238 — 33 page-aligned records**.\n\nReview readability, controlled terminology, names, repeated phrasing, quotations, Kural blocks, page function and cross-page continuity. Consult the matching audited Tamil whenever an editorial change could affect meaning. Make only source-faithful editorial improvements. Passing pages may move from `source-checked` to `editorial-reviewed`.\n\nDo not begin Part-level review or release work during ER1. After ER1 passes, the next editorial batch is **ER2 scans 256–288 / printed 239–271, 33 pages**.\n\n'
if front not in s:
    raise SystemExit('authoritative status ER1 frontier not found')
editorial = '''## Part 003 English editorial review — IN PROGRESS\n\n- **ER1: scans 223–255 / printed 206–238 — COMPLETE / PASS 33/33**;\n- cumulative editorial review: **33/111**;\n- remaining editorial-review pages: **78**;\n- current Part-003 English state: **33 `editorial-reviewed` + 78 `source-checked` / 0 `draft` / 0 source-limited / 0 blocked**;\n- ER1 English wording changes: **3 page files — scans 246, 251, 255**;\n- scan **246**: grammatical smoothing only, `a very realm of pleasure` → `the very realm of pleasure`;\n- scan **251**: restructured the opening sentence for readable English while preserving the all-night embrace / peak-of-pleasure / quarrel-running-away sense;\n- scan **255**: reconciled the heart's source wording `கற்பு எனப்படும் கதவு` to **the door called chastity** and smoothed the bolt metaphor; the later Kural-level `நிறை` → **restraint** distinction remains intact;\n- Tamil page / metadata changes during ER1: **0**;\n- no standard/published/web English Kural wording, external terminology or remembered rendering was imported.\n\nThe ER1 range preserves all source-supported Kural blocks, page functions and continuities, including genuine **233→234** and clean **244→245** / **255→256** boundaries.\n\n## Current frontier — Part 003 English Editorial Review ER2\n\nExact next activity: **editorial review scans 256–288 / printed 239–271 — 33 page-aligned records**.\n\nReview readability, controlled terminology, names, repeated phrasing, quotations, Kural blocks, page function and cross-page continuity. Consult the matching audited Tamil whenever an editorial change could affect meaning. Make only source-faithful editorial improvements. Passing pages may move from `source-checked` to `editorial-reviewed`.\n\nDo not begin Part-level review or release work during ER2. If ER2 passes, cumulative editorial review becomes **66/111** and the next batch is **ER3 scans 289–321 / printed 272–304, 33 pages**.\n\n'''
s = s.replace(front, editorial, 1)
sp.write_text(s, encoding='utf-8')

# 3. English README.
rp = EN / 'README.md'
r = rp.read_text(encoding='utf-8')
old_front = '''## Current frontier\n\nExact next activity: **Part 003 English Editorial Review ER1 — scans 223–255 / printed 206–238, 33 pages**.\n\nReview readability, controlled terminology, names, repeated phrasing, quotations, Kural blocks, page function and cross-page continuity. Consult audited Tamil whenever an editorial change could affect meaning. Passing pages may move from `source-checked` to `editorial-reviewed`.\n\nIf ER1 passes, the next editorial batch is **ER2 — scans 256–288 / printed 239–271, 33 pages**. Part 004 remains blocked until the maintained Part-003 English workflow and final Part closure checkpoint are complete.\n'''
new_front = '''## Part 003 English editorial review — IN PROGRESS\n\n- ER1 **223–255 / 206–238 — COMPLETE / PASS 33/33**;\n- cumulative editorial review: **33/111**;\n- current English state: **33 `editorial-reviewed` + 78 `source-checked`**;\n- ER1 wording changes: **scans 246, 251, 255 only**; no Tamil record changed.\n\n## Current frontier\n\nExact next activity: **Part 003 English Editorial Review ER2 — scans 256–288 / printed 239–271, 33 pages**.\n\nReview readability, controlled terminology, names, repeated phrasing, quotations, Kural blocks, page function and cross-page continuity. Consult audited Tamil whenever an editorial change could affect meaning. Passing pages may move from `source-checked` to `editorial-reviewed`.\n\nIf ER2 passes, cumulative editorial review becomes **66/111** and the next editorial batch is **ER3 — scans 289–321 / printed 272–304, 33 pages**. Part 004 remains blocked until the maintained Part-003 English workflow and final Part closure checkpoint are complete.\n'''
r = replace_once(r, old_front, new_front, 'English README frontier')
rp.write_text(r, encoding='utf-8')

# 4. Work handover.
hp = ROOT / 'HANDOVER.md'
h = hp.read_text(encoding='utf-8')
h = replace_if_present(h, '- current English state: **111 `source-checked` / 0 `draft` / 0 source-limited / 0 blocked**;', '- current English state: **33 `editorial-reviewed` + 78 `source-checked` / 0 `draft` / 0 source-limited / 0 blocked**;')
h = replace_if_present(h, '- glossary reconciliation: **IN PROGRESS — GR1 + GR2 + GR3 COMPLETE / PASS, 99/111**;', '- glossary reconciliation: **COMPLETE / CLOSED — 111/111**;')
h = replace_if_present(h, '- editorial review: **not-started**;', '- editorial review: **IN PROGRESS — ER1 COMPLETE / PASS 33/111**;')
marker = '## Exact next activity — English Editorial Review ER1\n'
if marker not in h:
    raise SystemExit('work handover ER1 marker missing')
prefix = h.split(marker, 1)[0]
new_tail = '''## Editorial review progress — ER1 COMPLETE / PASS 33/111\n\n- ER1 **223–255 / printed 206–238 — COMPLETE / PASS 33/33**;\n- English state: **33 editorial-reviewed + 78 source-checked**;\n- wording changes limited to scans **246, 251, 255**;\n- Tamil changes: **0**;\n- source-supported Kural blocks and range continuities preserved.\n\n## Exact next activity — English Editorial Review ER2\n\nProcess **scans 256–288 / printed 239–271 — 33 PAGE-ALIGNED RECORDS**.\n\n1. fetch live `main` first;\n2. confirm Part 003 Tamil remains **ARCHIVAL-READY / CLOSED** and English drafting, source-check and glossary reconciliation remain **111/111 COMPLETE / CLOSED**;\n3. confirm editorial review is **33/111** with scans **223–255** `editorial-reviewed`;\n4. read `translations/en/TRANSLATION_GUIDE.md`, `TRANSLATION_STATUS.md`, `GLOSSARY.md`, and English records **0256–0288**, consulting matching audited Tamil wherever an editorial choice could affect meaning;\n5. review readability, controlled terminology, names, repeated phrasing, quotations, Kural blocks, page function and cross-page continuity;\n6. make only source-faithful editorial improvements; do not import standard/published/web English wording or terminology from memory;\n7. passing pages may move from `source-checked` to `editorial-reviewed`;\n8. do not alter Tamil files;\n9. do not begin Part-level review or release work during ER2;\n10. update `TRANSLATION_STATUS.md` and audit the exact changed-file set.\n\nIf ER2 passes, cumulative editorial review becomes **66/111** and the next activity is **Editorial Review ER3 — scans 289–321 / printed 272–304, 33 pages**. External **333→334** remains deferred until Part 004 source intake. Part 004 remains blocked until the maintained English workflow and final Part closure checkpoint are complete.\n'''
hp.write_text(prefix + new_tail, encoding='utf-8')

# 5. Next-chat prompt — replace the current ER1 gate with ER2 and synchronize headline state.
np = Path('NEXT_CHAT_PROMPT_KURALOVIYAM.md')
n = np.read_text(encoding='utf-8')
n = replace_if_present(n, '- current Part-003 English state: **111 `source-checked` / 0 `draft` / 0 source-limited / 0 blocked**.', '- current Part-003 English state: **33 `editorial-reviewed` + 78 `source-checked` / 0 `draft` / 0 source-limited / 0 blocked**.')
n = replace_if_present(n, '- glossary reconciliation: **IN PROGRESS — GR1 + GR2 + GR3 COMPLETE / PASS, 99/111**.', '- glossary reconciliation: **111/111 COMPLETE / CLOSED**.')
n = replace_if_present(n, '- editorial review / Part review / release: **not-started**.', '- editorial review: **IN PROGRESS — ER1 COMPLETE / PASS 33/111**; Part review / release: **not-started**.')
marker = '## Exact next activity — Part 003 English Editorial Review ER1\n'
if marker not in n:
    raise SystemExit('next prompt ER1 marker missing')
prefix = n.split(marker, 1)[0]
next_tail = '''## Editorial review progress\n\n- ER1 **scans 223–255 / printed 206–238 — COMPLETE / PASS 33/33**;\n- cumulative editorial review **33/111**;\n- current page state **33 editorial-reviewed + 78 source-checked**;\n- ER1 wording changes were limited to scans **246, 251 and 255**;\n- no Tamil record changed.\n\n## Exact next activity — Part 003 English Editorial Review ER2\n\nProcess **scans 256–288 / printed 239–271 — 33 page-aligned records**.\n\nRequirements:\n\n1. fetch live `main` first and preserve newer durable work;\n2. confirm `PART_003_TAMIL_ARCHIVAL_READY.md` remains **PASS / CLOSED**;\n3. confirm English drafting, source-check and glossary reconciliation are each **111/111 COMPLETE / CLOSED**, and editorial review is **33/111**;\n4. read `translations/en/TRANSLATION_GUIDE.md`, `GLOSSARY.md`, and English records **0256–0288** with matching audited Tamil wherever meaning-sensitive editorial decisions arise;\n5. review readability, controlled terminology, names, repeated phrasing, quotations, Kural blocks, page function and cross-page continuity;\n6. make only source-faithful editorial improvements; do not import standard/published/web English Kural wording, another edition's terminology, or memory;\n7. passing pages may move from `source-checked` to `editorial-reviewed`;\n8. do not alter any Tamil page record or Tamil metadata;\n9. do not begin Part-level review or release work during ER2;\n10. update `TRANSLATION_STATUS.md` and audit the exact changed-file set before advancing.\n\nIf ER2 passes, cumulative editorial review becomes **66/111** and the next activity is **Editorial Review ER3 — scans 289–321 / printed 272–304, 33 pages**. Part 004 remains blocked until Part 003 completes editorial review, Part review, release report/release-ready synchronization and final Part closure. External **333→334** remains deferred until Part 004 source intake.\n'''
np.write_text(prefix + next_tail, encoding='utf-8')

# 6. Work README headline/current state.
wp = ROOT / 'README.md'
w = wp.read_text(encoding='utf-8')
w = replace_if_present(w, '**Tamil ARCHIVAL-READY / CLOSED; English drafting + source-check COMPLETE / CLOSED; glossary reconciliation COMPLETE / CLOSED — 111/111; editorial review ER1 next**', '**Tamil ARCHIVAL-READY / CLOSED; English drafting + source-check + glossary COMPLETE / CLOSED; editorial review IN PROGRESS — ER1 COMPLETE / PASS 33/111; ER2 next**')
w = replace_if_present(w, '## Part 003 — TAMIL ARCHIVAL-READY / CLOSED; ENGLISH DRAFTING + SOURCE-CHECK CLOSED; GLOSSARY RECONCILIATION CLOSED; EDITORIAL REVIEW NEXT', '## Part 003 — TAMIL ARCHIVAL-READY / CLOSED; ENGLISH DRAFTING + SOURCE-CHECK + GLOSSARY CLOSED; EDITORIAL REVIEW IN PROGRESS — ER1 33/111')
wp.write_text(w, encoding='utf-8')

# 7. Page map and source metadata current-state lines.
pp = ROOT / 'indexes/page-map.md'
p = pp.read_text(encoding='utf-8')
p = replace_if_present(p, '**Tamil ARCHIVAL-READY / CLOSED; English drafting + source-check COMPLETE / CLOSED; glossary COMPLETE / CLOSED — 111/111; editorial review ER1 next**', '**Tamil ARCHIVAL-READY / CLOSED; English drafting + source-check + glossary COMPLETE / CLOSED; editorial review ER1 COMPLETE / PASS — 33/111; ER2 next**')
pp.write_text(p, encoding='utf-8')

mp = ROOT / 'metadata/source.md'
m = mp.read_text(encoding='utf-8')
m = replace_if_present(m, 'glossary reconciliation COMPLETE / CLOSED — 111/111; editorial review ER1 next', 'glossary reconciliation COMPLETE / CLOSED — 111/111; editorial review ER1 COMPLETE / PASS — 33/111; ER2 next')
mp.write_text(m, encoding='utf-8')

# 8. Work-specific guidelines current frontier.
gp = Path('KURALOVIYAM_ARCHIVAL_GUIDELINES.md')
g = gp.read_text(encoding='utf-8')
g = replace_if_present(g, '- all English pages remain `source-checked`; editorial review / Part review / release are not started.', '- English editorial review: **IN PROGRESS — ER1 COMPLETE / PASS 33/111**; current page state **33 editorial-reviewed + 78 source-checked**; Part review / release are not started.')
g = replace_if_present(g, 'Perform **Part 003 English Editorial Review ER1 — scans 223–255 / printed 206–238, 33 page-aligned records**.', 'Perform **Part 003 English Editorial Review ER2 — scans 256–288 / printed 239–271, 33 page-aligned records**.')
g = replace_if_present(g, 'If ER1 passes, the next editorial batch is **ER2 scans 256–288 / printed 239–271, 33 pages**.', 'If ER2 passes, cumulative editorial review becomes **66/111** and the next editorial batch is **ER3 scans 289–321 / printed 272–304, 33 pages**.')
gp.write_text(g, encoding='utf-8')

# 9. Root handover headline only; detailed active Sangath Tamil state is intentionally untouched.
rhp = Path('HANDOVER.md')
rh = rhp.read_text(encoding='utf-8')
rh = replace_if_present(
    rh,
    'Last refreshed for Kuraloviyam **Part 003 Tamil ARCHIVAL-READY / CLOSED; English drafting + source-check CLOSED; glossary GR1–GR3 COMPLETE / PASS 99/111, GR4 next**: **2026-09-10**.',
    'Last refreshed for Kuraloviyam **Part 003 Tamil ARCHIVAL-READY / CLOSED; English drafting + source-check + glossary CLOSED; editorial review ER1 COMPLETE / PASS 33/111, ER2 next**: **2026-09-10**.'
)
rhp.write_text(rh, encoding='utf-8')

# Final local gate.
for scan in range(223, 256):
    printed = scan - 17
    s = (EN / 'pages' / f'{scan:04d}-kuraloviyam-{printed}.md').read_text(encoding='utf-8')
    if s.count('status: "editorial-reviewed"') != 1 or 'status: "source-checked"' in s:
        raise SystemExit(f'ER1 promotion gate failed scan {scan}')

for scan in range(256, 334):
    printed = scan - 17
    s = (EN / 'pages' / f'{scan:04d}-kuraloviyam-{printed}.md').read_text(encoding='utf-8')
    if s.count('status: "source-checked"') != 1:
        raise SystemExit(f'non-ER1 page state drift scan {scan}')

print('ER1_COMPLETE=33/33')
print('EDITORIAL_REVIEW=33/111')
print('PAGE_WORDING_CHANGES=246,251,255')
print('NEXT=ER2 scans 256-288 / printed 239-271')
