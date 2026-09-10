from pathlib import Path
import subprocess

ROOT = Path('.')
PAGES = ROOT / 'works/kuraloviyam/translations/en/pages'


def replace_once(text: str, old: str, new: str, label: str) -> str:
    count = text.count(old)
    if count != 1:
        raise RuntimeError(f'{label}: expected exactly 1 match, found {count}')
    return text.replace(old, new, 1)


def replace_tail(path: Path, marker: str, new_tail: str) -> None:
    text = path.read_text(encoding='utf-8')
    idx = text.find(marker)
    if idx < 0:
        raise RuntimeError(f'{path}: tail marker not found: {marker!r}')
    if text.find(marker, idx + 1) >= 0:
        raise RuntimeError(f'{path}: tail marker occurs more than once: {marker!r}')
    path.write_text(text[:idx] + new_tail.rstrip() + '\n', encoding='utf-8')


# ER2 page wording changes. Every other page in 256–288 receives status promotion only.
WORDING_CHANGES = {
    256: [
        (
            'Rather than calling the suffering of poverty merely suffering, Valluvar speaks movingly of the “fire of poverty.” The fire of poverty kindles the fire of hunger in the belly, and there are many histories in the world in which that has turned into a fire of revolution. Though it is called a fire, Valluvar has pictured for us how it is crueller even than fire itself.',
            'Rather than calling the suffering of poverty simply “suffering,” Valluvar movingly calls it the “fire of poverty.” The fire of poverty kindles the fire of hunger in the belly, and world history offers many instances of that fire turning into a fire of revolution. Though poverty is called a fire, Valluvar depicts it as crueller even than fire itself.'
        )
    ],
    258: [
        (
            'An indefinable sorrow lies upon her face. What else could it be but the longing that she still has not seen her lover—',
            'An indefinable sorrow lies upon her face. The longing that she still has not seen her lover—'
        )
    ],
    259: [
        (
            'What else could it be but longing? The friend from the neighbouring house comes to tease her.',
            '—what else could it be? The friend from the neighbouring house comes to tease her.'
        )
    ],
    260: [
        (
            'At that tender age itself he had lost both mother and father.',
            'At that tender age he had lost both mother and father.'
        )
    ],
    263: [
        (
            'Who is standing together on the bank and laughing? Ah, the young men of the village? Seeing me suffer from separation in love and speak to you without knowing myself, they stand on the bank clapping and laughing. Do you see?',
            'Who are those standing together on the bank and laughing? Ah, the young men of the village? Seeing me suffer the anguish of separation in love and speak to you beside myself, they stand on the bank clapping and laughing. Do you see?'
        )
    ],
    264: [
        (
            'Meanwhile, from the top of the tree—',
            'Meanwhile, from the tree—'
        )
    ],
    265: [
        (
            'Vallaan, from the top of the tree, called to Nallaan:',
            '—top, Vallaan called to Nallaan:'
        )
    ],
    269: [
        (
            'But his heart, full of complete refinement, had not decayed to that level.',
            'But his heart, rich in the fullness of refinement, had not fallen to that level.'
        )
    ],
    270: [
        (
            'Thinking that he should work carefully without feeling fatigue, Thirumathi brought him a cup of buttermilk and stood beside him.',
            'Wanting him to do his careful work without tiring, Thirumathi brought him a cup of buttermilk and stood beside him.'
        )
    ],
    273: [
        (
            'What she desired took place.',
            'What she desired came to pass.'
        )
    ],
    275: [
        (
            'The prince is coming as the supporting branch for that vine-like waist of yours which can be seen only when you walk swaying.',
            'The prince is coming like a supporting branch to hold up that vine-like waist of yours, visible only when you walk with a sway.'
        )
    ],
    279: [
        (
            '“This is the same as your story of conducting a lovers\' quarrel, friend! Have you not read the Kural in which Valluvar says that the condition of a man who tries to quarrel even though he knows the quarrel will not work is like that of someone who leaps into a river knowing the flood will sweep him away?” asked Nalli.',
            '“This is just like your lovers\'-quarrel story, friend! Have you not read the Kural in which Valluvar says that the condition of a man who tries to quarrel even though he knows the quarrel will not work is like that of someone who leaps into a river knowing the flood will sweep him away?” asked Nalli.'
        )
    ],
    281: [
        (
            'Cleanliness and he had no fellowship.',
            'He and cleanliness had nothing in common.'
        ),
        (
            'as though he knows everything!',
            'as though he knew everything!'
        )
    ],
    285: [
        (
            'Only today, after many days, have I seen your country and found a little consolation in happiness.',
            'Only today, after many long days, have I seen your country and found a little solace in the joy it gives me.'
        ),
        (
            'No one has the courage to stand across his path.',
            'No one has the courage to stand in his way.'
        )
    ],
    287: [
        (
            'The struggle I had expected to end within a countable time has continued for years.',
            'The struggle I had expected to end within a finite time has gone on for years.'
        ),
        (
            'Even if he shows me no compassion sufficient to return alive out of love for me, when the village and the world praise him for refusing to surrender to his enemies, I forget even that he is separated from me and delight rises in my ears.',
            'Even if his love for me does not move him to return alive, when the village and the world praise him for refusing to surrender to his enemies, I forget even that he is separated from me, and delight rises in my ears.'
        )
    ],
}

changed_wording_pages = set(WORDING_CHANGES)
expected_pages = []
for scan in range(256, 289):
    printed = scan - 17
    path = PAGES / f'{scan:04d}-kuraloviyam-{printed}.md'
    expected_pages.append(str(path))
    text = path.read_text(encoding='utf-8')
    if text.count('status: "source-checked"') != 1:
        raise RuntimeError(f'{path}: expected exactly one source-checked status')
    if 'status: "editorial-reviewed"' in text:
        raise RuntimeError(f'{path}: already editorial-reviewed unexpectedly')
    text = text.replace('status: "source-checked"', 'status: "editorial-reviewed"', 1)
    for i, (old, new) in enumerate(WORDING_CHANGES.get(scan, []), start=1):
        text = replace_once(text, old, new, f'{path} wording replacement {i}')
    if text.count('source_tamil_status: "verified"') != 1:
        raise RuntimeError(f'{path}: source_tamil_status invariant failed')
    path.write_text(text, encoding='utf-8')

# Outgoing ER2 boundary witness must remain untouched/source-checked.
scan289 = PAGES / '0289-kuraloviyam-272.md'
if 'status: "source-checked"' not in scan289.read_text(encoding='utf-8'):
    raise RuntimeError('scan 289 is not source-checked as expected')

# Root handover headline.
path = ROOT / 'HANDOVER.md'
text = path.read_text(encoding='utf-8')
text = replace_once(
    text,
    'Last refreshed for Kuraloviyam **Part 003 Tamil ARCHIVAL-READY / CLOSED; English drafting + source-check + glossary CLOSED; editorial review ER1 COMPLETE / PASS 33/111, ER2 next**: **2026-09-10**.',
    'Last refreshed for Kuraloviyam **Part 003 Tamil ARCHIVAL-READY / CLOSED; English drafting + source-check + glossary CLOSED; editorial review ER1 + ER2 COMPLETE / PASS 66/111, ER3 next**: **2026-09-10**.',
    'root HANDOVER headline'
)
path.write_text(text, encoding='utf-8')

# Kuraloviyam work README: top state + replace stale live-state tail.
path = ROOT / 'works/kuraloviyam/README.md'
text = path.read_text(encoding='utf-8')
text = replace_once(
    text,
    '| 003 | 223–333 | **Tamil ARCHIVAL-READY / CLOSED; English drafting + source-check + glossary COMPLETE / CLOSED; editorial review IN PROGRESS — ER1 COMPLETE / PASS 33/111; ER2 next** |',
    '| 003 | 223–333 | **Tamil ARCHIVAL-READY / CLOSED; English drafting + source-check + glossary COMPLETE / CLOSED; editorial review IN PROGRESS — ER1 + ER2 COMPLETE / PASS 66/111; ER3 next** |',
    'work README Part003 row'
)
text = replace_once(
    text,
    '## Part 003 — TAMIL ARCHIVAL-READY / CLOSED; ENGLISH DRAFTING + SOURCE-CHECK + GLOSSARY CLOSED; EDITORIAL REVIEW IN PROGRESS — ER1 33/111',
    '## Part 003 — TAMIL ARCHIVAL-READY / CLOSED; ENGLISH DRAFTING + SOURCE-CHECK + GLOSSARY CLOSED; EDITORIAL REVIEW IN PROGRESS — ER1 + ER2 66/111',
    'work README Part003 heading'
)
path.write_text(text, encoding='utf-8')
replace_tail(
    path,
    '## Current durable state',
    '''## Current durable state

- Part 003 Tamil: **ARCHIVAL-READY / CLOSED — 111 textual verified + 111 visual verified / 0 exceptions**;
- Part 003 English drafting: **111/111 COMPLETE / CLOSED**;
- Part 003 English source-check: **111/111 COMPLETE / CLOSED**;
- Part 003 English glossary reconciliation: **111/111 COMPLETE / CLOSED**;
- Part 003 English editorial review: **IN PROGRESS — ER1 + ER2 COMPLETE / PASS 66/111**;
- current Part-003 English state: **66 `editorial-reviewed` + 45 `source-checked` / 0 `draft` / 0 source-limited / 0 blocked**;
- Part-level review / release: **not-started**.

## Current frontier

**Next activity: Part 003 English Editorial Review ER3 — scans 289–321 / printed 272–304, 33 pages.** Review readability, controlled terminology, names, repeated phrasing, quotations, Kural blocks, page function and cross-page continuity against the controlled glossary and audited Tamil context. Passing pages may move from `source-checked` to `editorial-reviewed`. Do not alter closed Tamil records or begin Part-level review/release work during ER3.

If ER3 passes, cumulative editorial review reaches **99/111** and the final remainder is **ER4 scans 322–333 / printed 305–316, 12 pages**. External **333→334** remains deferred until Part 004 source intake. Part 004 remains blocked until the maintained Part-003 English workflow and final Part closure checkpoint are complete.'''
)

# Page map frontier row.
path = ROOT / 'works/kuraloviyam/indexes/page-map.md'
text = path.read_text(encoding='utf-8')
text = replace_once(
    text,
    '| 003 | 223–333 | 1–111 | scan 223 / printed 206 through scan 333 / printed 316 | **Tamil ARCHIVAL-READY / CLOSED; English drafting + source-check + glossary reconciliation COMPLETE / CLOSED — 111/111; editorial review ER1 COMPLETE / PASS — 33/111; ER2 next** |',
    '| 003 | 223–333 | 1–111 | scan 223 / printed 206 through scan 333 / printed 316 | **Tamil ARCHIVAL-READY / CLOSED; English drafting + source-check + glossary reconciliation COMPLETE / CLOSED — 111/111; editorial review ER1 + ER2 COMPLETE / PASS — 66/111; ER3 next** |',
    'page-map Part003 row'
)
path.write_text(text, encoding='utf-8')

# Source metadata: top row + live progress paragraph.
path = ROOT / 'works/kuraloviyam/metadata/source.md'
text = path.read_text(encoding='utf-8')
text = replace_once(
    text,
    '| 003 | 223–333 | 111 | `TVA_BOK_0065733_குறளோவியம்_part_003_pages_223-333.pdf` | **supplied; Tamil ARCHIVAL-READY / CLOSED; English drafting + source-check COMPLETE / CLOSED; glossary reconciliation COMPLETE / CLOSED — 111/111; editorial review ER1 COMPLETE / PASS — 33/111; ER2 next** |',
    '| 003 | 223–333 | 111 | `TVA_BOK_0065733_குறளோவியம்_part_003_pages_223-333.pdf` | **supplied; Tamil ARCHIVAL-READY / CLOSED; English drafting + source-check + glossary reconciliation COMPLETE / CLOSED — 111/111; editorial review ER1 + ER2 COMPLETE / PASS — 66/111; ER3 next** |',
    'source metadata Part003 row'
)
start = text.find('Historical Part-003 Pass-1 cadence was')
end = text.find('## Front-matter observations')
if start < 0 or end < 0 or end <= start:
    raise RuntimeError('source metadata live-progress replacement markers not found')
new_progress = '''Historical Part-003 Pass-1 cadence was **11 physical scans per normal iteration**, followed by a one-page final remainder at scan 333. Pass 1, Pass 2A, Pass 2B and Pass 3 are complete; the Part audit passed; final metadata/status synchronization closed all 111 records as textual and visual `verified`; documentation synchronization and the separate Tamil archival-ready checkpoint are closed. The maintained English layer has completed first-pass drafting **111/111**, source-check **111/111**, and glossary reconciliation **111/111**. Editorial review is **IN PROGRESS — ER1 + ER2 COMPLETE / PASS, 66/111**, leaving **45** source-checked pages. The exact next editorial batch is **ER3 scans 289–321 / printed 272–304, 33 pages**; if it passes, the final editorial remainder is **ER4 scans 322–333 / printed 305–316, 12 pages**. Part-level review and release remain not-started. External **333→334** remains deferred until Part 004 source intake.

'''
text = text[:start] + new_progress + text[end:]
path.write_text(text, encoding='utf-8')

# English README: repair stale live summary and advance editorial tail.
path = ROOT / 'works/kuraloviyam/translations/en/README.md'
text = path.read_text(encoding='utf-8')
old_chunk = '''- source-check: **111/111 COMPLETE / CLOSED**;
- current English state: **111 `source-checked` / 0 `draft` / 0 source-limited / 0 blocked**;
- glossary reconciliation: **IN PROGRESS — GR1 + GR2 + GR3 COMPLETE / PASS, 99/111**;
- editorial review / Part review / release: **not-started**.'''
new_chunk = '''- source-check: **111/111 COMPLETE / CLOSED**;
- current English state: **66 `editorial-reviewed` + 45 `source-checked` / 0 `draft` / 0 source-limited / 0 blocked**;
- glossary reconciliation: **111/111 COMPLETE / CLOSED**;
- editorial review: **IN PROGRESS — ER1 + ER2 COMPLETE / PASS 66/111**;
- Part review / release: **not-started**.'''
text = replace_once(text, old_chunk, new_chunk, 'English README live summary')
path.write_text(text, encoding='utf-8')
replace_tail(
    path,
    '## Part 003 English editorial review — IN PROGRESS',
    '''## Part 003 English editorial review — IN PROGRESS

- ER1 **223–255 / 206–238 — COMPLETE / PASS 33/33**;
- ER2 **256–288 / 239–271 — COMPLETE / PASS 33/33**;
- cumulative editorial review: **66/111**;
- remaining editorial-review pages: **45**;
- current English state: **66 `editorial-reviewed` + 45 `source-checked`**;
- ER1 wording changes: **scans 246, 251, 255 only**;
- ER2 wording changes: **15 page files — scans 256, 258, 259, 260, 263, 264, 265, 269, 270, 273, 275, 279, 281, 285, 287**; the other 18 ER2 pages changed only by status promotion;
- no Tamil archival record changed in ER1 or ER2.

ER2 preserved the clean incoming **255→256** boundary, repaired the exact source-supported physical continuations **258→259** and **264→265**, preserved the clean **277→278** boundary, and retained genuine **288→289** for the next batch. No standard/published/web English wording was imported.

## Current frontier

Exact next activity: **Part 003 English Editorial Review ER3 — scans 289–321 / printed 272–304, 33 pages**.

Review readability, controlled terminology, names, repeated phrasing, quotations, Kural blocks, page function and cross-page continuity. Consult audited Tamil whenever an editorial change could affect meaning. Passing pages may move from `source-checked` to `editorial-reviewed`.

If ER3 passes, cumulative editorial review becomes **99/111** and the final editorial batch is **ER4 — scans 322–333 / printed 305–316, 12 pages**. Part 004 remains blocked until the maintained Part-003 English workflow and final Part closure checkpoint are complete.'''
)

# Detailed translation status: advance summary and replace editorial tail.
path = ROOT / 'works/kuraloviyam/translations/en/TRANSLATION_STATUS.md'
text = path.read_text(encoding='utf-8')
text = replace_once(
    text,
    '- editorial review: **IN PROGRESS — ER1 COMPLETE / PASS 33/111**;',
    '- editorial review: **IN PROGRESS — ER1 + ER2 COMPLETE / PASS 66/111**;',
    'translation status early editorial summary'
)
path.write_text(text, encoding='utf-8')
replace_tail(
    path,
    '## Part 003 English editorial review — IN PROGRESS',
    '''## Part 003 English editorial review — IN PROGRESS

- **ER1: scans 223–255 / printed 206–238 — COMPLETE / PASS 33/33**;
- **ER2: scans 256–288 / printed 239–271 — COMPLETE / PASS 33/33**;
- cumulative editorial review: **66/111**;
- remaining editorial-review pages: **45**;
- current Part-003 English state: **66 `editorial-reviewed` + 45 `source-checked` / 0 `draft` / 0 source-limited / 0 blocked**;
- ER1 English wording changes: **3 page files — scans 246, 251, 255**;
- ER2 English wording changes: **15 page files — scans 256, 258, 259, 260, 263, 264, 265, 269, 270, 273, 275, 279, 281, 285, 287**;
- ER2 status-only promotions: **18 page files**;
- Tamil page / metadata changes during ER1 + ER2: **0**;
- no standard/published/web English Kural wording, external terminology or remembered rendering was imported.

ER2 editorial changes were source-faithful readability/continuity improvements only. In particular, the exact Tamil page split across **258→259** (`...காதலனை இன்னும் காணவில்லையே என்ற / ஏக்கத்தைத் தவிர...`) is now mirrored without duplicated English wording; the exact **264→265** split (`மரத்தின் / உச்சியிலிருந்த வல்லான்...`) is likewise preserved. The clean **277→278** boundary remains intact, and the genuine outgoing **288→289** continuation remains open into ER3. Kural blocks, Chapter/Kural metadata, visual/non-body page functions and controlled names/terms remain unchanged except for prose-level editorial smoothing supported by the audited Tamil records.

## Current frontier — Part 003 English Editorial Review ER3

Exact next activity: **editorial review scans 289–321 / printed 272–304 — 33 page-aligned records**.

Review readability, controlled terminology, names, repeated phrasing, quotations, Kural blocks, page function and cross-page continuity. Consult the matching audited Tamil whenever an editorial change could affect meaning. Make only source-faithful editorial improvements. Passing pages may move from `source-checked` to `editorial-reviewed`.

Do not begin Part-level review or release work during ER3. If ER3 passes, cumulative editorial review becomes **99/111** and the final batch is **ER4 scans 322–333 / printed 305–316, 12 pages**.

Part 004 remains blocked until Part 003 completes editorial review, Part review, release report/release-ready synchronization and the final Part closure checkpoint.'''
)

# Work-specific handover: live state and editorial tail.
path = ROOT / 'works/kuraloviyam/HANDOVER.md'
text = path.read_text(encoding='utf-8')
text = replace_once(
    text,
    '- current English state: **33 `editorial-reviewed` + 78 `source-checked` / 0 `draft` / 0 source-limited / 0 blocked**;',
    '- current English state: **66 `editorial-reviewed` + 45 `source-checked` / 0 `draft` / 0 source-limited / 0 blocked**;',
    'work handover English state'
)
text = replace_once(
    text,
    '- editorial review: **IN PROGRESS — ER1 COMPLETE / PASS 33/111**;',
    '- editorial review: **IN PROGRESS — ER1 + ER2 COMPLETE / PASS 66/111**;',
    'work handover editorial summary'
)
path.write_text(text, encoding='utf-8')
replace_tail(
    path,
    '## Editorial review progress — ER1 COMPLETE / PASS 33/111',
    '''## Editorial review progress — ER1 + ER2 COMPLETE / PASS 66/111

- ER1 **223–255 / printed 206–238 — COMPLETE / PASS 33/33**;
- ER2 **256–288 / printed 239–271 — COMPLETE / PASS 33/33**;
- English state: **66 editorial-reviewed + 45 source-checked**;
- ER1 wording changes limited to scans **246, 251, 255**;
- ER2 wording changes limited to scans **256, 258, 259, 260, 263, 264, 265, 269, 270, 273, 275, 279, 281, 285, 287**;
- the other **18 ER2 pages** changed only by status promotion;
- Tamil changes: **0**;
- source-supported Kural blocks, page functions and range continuities preserved, including repaired exact physical joins **258→259** and **264→265**, clean **277→278**, and genuine outgoing **288→289**.

## Exact next activity — English Editorial Review ER3

Process **scans 289–321 / printed 272–304 — 33 PAGE-ALIGNED RECORDS**.

1. fetch live `main` first;
2. confirm Part 003 Tamil remains **ARCHIVAL-READY / CLOSED** and English drafting, source-check and glossary reconciliation remain **111/111 COMPLETE / CLOSED**;
3. confirm editorial review is **66/111** with scans **223–288** `editorial-reviewed`;
4. read `translations/en/TRANSLATION_GUIDE.md`, `TRANSLATION_STATUS.md`, `GLOSSARY.md`, and English records **0289–0321**, consulting matching audited Tamil wherever an editorial choice could affect meaning;
5. review readability, controlled terminology, names, repeated phrasing, quotations, Kural blocks, page function and cross-page continuity;
6. make only source-faithful editorial improvements; do not import standard/published/web English wording or terminology from memory;
7. passing pages may move from `source-checked` to `editorial-reviewed`;
8. do not alter Tamil files;
9. do not begin Part-level review or release work during ER3;
10. update `TRANSLATION_STATUS.md` and audit the exact changed-file set.

If ER3 passes, cumulative editorial review becomes **99/111** and the next activity is **Editorial Review ER4 — scans 322–333 / printed 305–316, final 12 pages**. External **333→334** remains deferred until Part 004 source intake. Part 004 remains blocked until the maintained English workflow and final Part closure checkpoint are complete.'''
)

# Next-chat prompt: advance durable state and replace editorial frontier tail.
path = ROOT / 'NEXT_CHAT_PROMPT_KURALOVIYAM.md'
text = path.read_text(encoding='utf-8')
text = replace_once(
    text,
    '- current Part-003 English state: **33 `editorial-reviewed` + 78 `source-checked` / 0 `draft` / 0 source-limited / 0 blocked**.',
    '- current Part-003 English state: **66 `editorial-reviewed` + 45 `source-checked` / 0 `draft` / 0 source-limited / 0 blocked**.',
    'next prompt English state'
)
text = replace_once(
    text,
    '- editorial review: **IN PROGRESS — ER1 COMPLETE / PASS 33/111**; Part review / release: **not-started**.',
    '- editorial review: **IN PROGRESS — ER1 + ER2 COMPLETE / PASS 66/111**; Part review / release: **not-started**.',
    'next prompt editorial summary'
)
path.write_text(text, encoding='utf-8')
replace_tail(
    path,
    '## Editorial review progress',
    '''## Editorial review progress

- ER1 **scans 223–255 / printed 206–238 — COMPLETE / PASS 33/33**;
- ER2 **scans 256–288 / printed 239–271 — COMPLETE / PASS 33/33**;
- cumulative editorial review **66/111**;
- current page state **66 editorial-reviewed + 45 source-checked**;
- ER1 wording changes were limited to scans **246, 251, 255**;
- ER2 wording changes were limited to scans **256, 258, 259, 260, 263, 264, 265, 269, 270, 273, 275, 279, 281, 285, 287**; the other **18** pages were status-only promotions;
- no Tamil record changed;
- exact physical continuations **258→259** and **264→265** were editorially aligned to the audited Tamil page splits; clean **277→278** remains clean; genuine **288→289** remains preserved into ER3.

## Exact next activity — Part 003 English Editorial Review ER3

Process **scans 289–321 / printed 272–304 — 33 page-aligned records**.

Requirements:

1. fetch live `main` first and preserve newer durable work;
2. confirm `PART_003_TAMIL_ARCHIVAL_READY.md` remains **PASS / CLOSED**;
3. confirm English drafting, source-check and glossary reconciliation are each **111/111 COMPLETE / CLOSED**, and editorial review is **66/111**;
4. read `translations/en/TRANSLATION_GUIDE.md`, `GLOSSARY.md`, and English records **0289–0321** with matching audited Tamil wherever meaning-sensitive editorial decisions arise;
5. review readability, controlled terminology, names, repeated phrasing, quotations, Kural blocks, page function and cross-page continuity;
6. make only source-faithful editorial improvements; do not import standard/published/web English Kural wording, another edition's terminology, or memory;
7. passing pages may move from `source-checked` to `editorial-reviewed`;
8. do not alter any Tamil page record or Tamil metadata;
9. do not begin Part-level review or release work during ER3;
10. update `TRANSLATION_STATUS.md` and audit the exact changed-file set before advancing.

If ER3 passes, cumulative editorial review becomes **99/111** and the next activity is **Editorial Review ER4 — scans 322–333 / printed 305–316, final 12 pages**. Part 004 remains blocked until Part 003 completes editorial review, Part review, release report/release-ready synchronization and final Part closure. External **333→334** remains deferred until Part 004 source intake.'''
)

# Archival guideline current frontier; also correct the stale ER1 wording in that frontier.
path = ROOT / 'KURALOVIYAM_ARCHIVAL_GUIDELINES.md'
text = path.read_text(encoding='utf-8')
text = replace_once(
    text,
    '- English editorial review: **IN PROGRESS — ER1 COMPLETE / PASS 33/111**; current page state **33 editorial-reviewed + 78 source-checked**; Part review / release are not started.',
    '- English editorial review: **IN PROGRESS — ER1 + ER2 COMPLETE / PASS 66/111**; current page state **66 editorial-reviewed + 45 source-checked**; Part review / release are not started.',
    'guidelines editorial frontier bullet'
)
path.write_text(text, encoding='utf-8')
replace_tail(
    path,
    '### Exact next content stage',
    '''### Exact next content stage

Perform **Part 003 English Editorial Review ER3 — scans 289–321 / printed 272–304, 33 page-aligned records**. Review readability and consistency against the controlled glossary and audited Tamil context; consult Tamil whenever a change could affect meaning; passing pages may move from `source-checked` to `editorial-reviewed`; do not begin Part-level review or release work during ER3; do not alter closed Tamil records.

If ER3 passes, continue with the final **English Editorial Review ER4 — scans 322–333 / printed 305–316, 12 pages**. Part 004 remains blocked until the maintained Part-003 English workflow and final Part closure checkpoint are complete.'''
)

# Assert live-control strings are present after synchronization.
checks = {
    ROOT / 'HANDOVER.md': ['ER1 + ER2 COMPLETE / PASS 66/111, ER3 next'],
    ROOT / 'works/kuraloviyam/HANDOVER.md': ['66 editorial-reviewed + 45 source-checked', 'Editorial Review ER3'],
    ROOT / 'NEXT_CHAT_PROMPT_KURALOVIYAM.md': ['cumulative editorial review **66/111**', 'Editorial Review ER3'],
    ROOT / 'KURALOVIYAM_ARCHIVAL_GUIDELINES.md': ['ER1 + ER2 COMPLETE / PASS 66/111', 'Editorial Review ER3'],
    ROOT / 'works/kuraloviyam/README.md': ['ER1 + ER2 COMPLETE / PASS 66/111', 'Editorial Review ER3'],
    ROOT / 'works/kuraloviyam/indexes/page-map.md': ['ER1 + ER2 COMPLETE / PASS — 66/111; ER3 next'],
    ROOT / 'works/kuraloviyam/metadata/source.md': ['ER1 + ER2 COMPLETE / PASS — 66/111; ER3 next'],
    ROOT / 'works/kuraloviyam/translations/en/README.md': ['cumulative editorial review: **66/111**', 'Editorial Review ER3'],
    ROOT / 'works/kuraloviyam/translations/en/TRANSLATION_STATUS.md': ['cumulative editorial review: **66/111**', 'Editorial Review ER3'],
}
for p, needles in checks.items():
    body = p.read_text(encoding='utf-8')
    for needle in needles:
        if needle not in body:
            raise RuntimeError(f'{p}: expected synchronized text missing: {needle!r}')

# Exact changed-file gate: 33 ER2 English pages + 9 durable controls, no Tamil.
control_files = [
    'HANDOVER.md',
    'KURALOVIYAM_ARCHIVAL_GUIDELINES.md',
    'NEXT_CHAT_PROMPT_KURALOVIYAM.md',
    'works/kuraloviyam/HANDOVER.md',
    'works/kuraloviyam/README.md',
    'works/kuraloviyam/indexes/page-map.md',
    'works/kuraloviyam/metadata/source.md',
    'works/kuraloviyam/translations/en/README.md',
    'works/kuraloviyam/translations/en/TRANSLATION_STATUS.md',
]
expected = set(expected_pages + control_files)
actual = set(subprocess.check_output(['git', 'diff', '--name-only'], text=True).splitlines())
if actual != expected:
    missing = sorted(expected - actual)
    extra = sorted(actual - expected)
    raise RuntimeError(f'changed-file gate failed; missing={missing}; extra={extra}')
if any(p.startswith('works/kuraloviyam/pages/') for p in actual):
    raise RuntimeError('Tamil page change detected')
if len(actual) != 42:
    raise RuntimeError(f'expected 42 durable changed files, found {len(actual)}')

# Confirm all ER2 pages promoted and wording-change count remains the intended 15 files.
for scan in range(256, 289):
    printed = scan - 17
    body = (PAGES / f'{scan:04d}-kuraloviyam-{printed}.md').read_text(encoding='utf-8')
    if body.count('status: "editorial-reviewed"') != 1 or 'status: "source-checked"' in body:
        raise RuntimeError(f'scan {scan}: final editorial status gate failed')
if changed_wording_pages != {256, 258, 259, 260, 263, 264, 265, 269, 270, 273, 275, 279, 281, 285, 287}:
    raise RuntimeError('wording-change page inventory drifted')

print('ER2 prepared: 33/33 pages, 15 wording-change pages, 18 status-only pages, 9 control docs; 0 Tamil changes')
