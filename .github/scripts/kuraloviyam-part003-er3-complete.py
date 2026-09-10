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


# ER3 page wording changes. Every other page in 289–321 receives status promotion only.
# Meaning-sensitive changes below were checked against the matching audited Tamil records.
WORDING_CHANGES = {
    289: [
        (
            '“Only now he told me to let go of attachment; already he says ‘cling.’ What contradiction is this?” he wondered.',
            '“He only just told me to let go of attachment, and already he says ‘cling.’ What contradiction is this?” he wondered.'
        )
    ],
    290: [
        (
            'Ponni, with great effort, gathered a smile upon her face, but it vanished at once like a flash of lightning.',
            'With great effort, Ponni managed to summon a smile, but it vanished at once like a flash of lightning.'
        )
    ],
    292: [
        (
            'I am not one who fails to understand that the beauty of a steadfast mind lies in accepting suffering with the same cheerfulness with which we accept pleasure.',
            'I understand that the beauty of a steadfast mind lies in accepting suffering with the same cheerfulness with which we accept pleasure.'
        )
    ],
    295: [
        (
            'After a long while he returned. Instead of coming from the front, he came from behind, rested his head on her shoulder and caught her neck with his lips.',
            'After a long while he returned. Instead of coming from the front, he came from behind, rested his head on her shoulder and pressed his lips to her neck.'
        )
    ],
    298: [
        (
            'Those young hearts longed to spend every hour as food for one another.',
            "Those young hearts longed to spend every moment as each other's feast."
        )
    ],
    300: [
        (
            'But now you say Thirumagal is the younger and Moodevi the elder, throwing a challenge at my very rationalism!”',
            'But now you say Thirumagal is the younger and Moodevi the elder, challenging my very rationalism!”'
        )
    ],
    304: [
        (
            "Milk stripped of its covering and cow's milk waited beside the bed. Male and female blossomed together as one flower upon the bed.",
            "An uncovered breast and cow's milk waited beside the bed. Male and female blossomed together as one flower upon the bed."
        )
    ],
    305: [
        (
            'Ezhini, who had composed songs of awakening, also became the intermediary in that act and went on betraying the Valanadu that had sustained him.',
            'Ezhini, who had composed songs of awakening, became the intermediary in that bribery and went on betraying the Valanadu that had sustained him.'
        )
    ],
    308: [
        (
            'As though frightened of her, darkness rushed in. Kaali slipped out like a thieving cat—between the heap of harvested paddy and the stack of straw left after threshing. The one who came as a cat stood there transformed into a flower.',
            'As though frightened of her, darkness rushed in. Like a thieving cat, Kaali slipped stealthily between the heap of harvested paddy and the stack of straw left after threshing. She had come like a cat; there she stood transformed into a flower.'
        )
    ],
    310: [
        (
            '—and the judge too gave his decision that he was not a thief, and that the very people who had called him a thief were the ones who killed him. Even beyond that decision, those in government bent justice.',
            '—but the judge ruled that he was no thief and that the very people who had called him a thief were the ones who killed him. Even after that ruling, those in government bent justice.'
        )
    ],
    313: [
        (
            'Karmegam replied irritably, “Marriage or nonsense! Don\'t such things require money for the expenses? What do I have?”',
            'Karmegam replied irritably, “Marriage or nonsense! Doesn\'t all that require money for expenses? What do I have?”'
        )
    ],
    315: [
        (
            'Seyizhai owns lips that shine with smiles.',
            'Seyizhai has lips lit by smiles.'
        ),
        (
            'Between white eyes like rounded jasmine blossoms, dark pupils like bees dance—',
            'Within eyes white as rounded jasmine blossoms, dark pupils like bees dance—'
        )
    ],
    316: [
        (
            'Her grandmother is an old fruit with age.',
            'Her grandmother is an old woman ripened by age.'
        )
    ],
    320: [
        (
            '—her tongue-coloured feet had reddened like hibiscus flowers. She stood with her waist resting against the parapet of the outer terrace adjoining the bedchamber, her red-lily fingers weary as they propped up her moon-face, staring into the sky and asking angrily with her eyes, “O cool moon that burns, why do you scorch only me?”',
            '—her tongue-coloured feet had reddened like hibiscus flowers. She stood with her waist resting against the parapet of the outer terrace adjoining the bedchamber, her red-lily fingers weary from propping up her moon-face. Staring into the sky, she asked angrily with her eyes, “O cool moon that burns, why do you scorch only me?”'
        )
    ],
}

changed_wording_pages = set(WORDING_CHANGES)
expected_pages = []
for scan in range(289, 322):
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

# Boundary invariants: incoming ER2 page is reviewed; outgoing ER4 witness remains untouched/source-checked.
scan288 = PAGES / '0288-kuraloviyam-271.md'
if 'status: "editorial-reviewed"' not in scan288.read_text(encoding='utf-8'):
    raise RuntimeError('scan 288 is not editorial-reviewed as expected')
scan322 = PAGES / '0322-kuraloviyam-305.md'
if 'status: "source-checked"' not in scan322.read_text(encoding='utf-8'):
    raise RuntimeError('scan 322 is not source-checked as expected')

# Root handover headline.
path = ROOT / 'HANDOVER.md'
text = path.read_text(encoding='utf-8')
text = replace_once(
    text,
    'Last refreshed for Kuraloviyam **Part 003 Tamil ARCHIVAL-READY / CLOSED; English drafting + source-check + glossary CLOSED; editorial review ER1 + ER2 COMPLETE / PASS 66/111, ER3 next**: **2026-09-10**.',
    'Last refreshed for Kuraloviyam **Part 003 Tamil ARCHIVAL-READY / CLOSED; English drafting + source-check + glossary CLOSED; editorial review ER1 + ER2 + ER3 COMPLETE / PASS 99/111, ER4 next**: **2026-09-10**.',
    'root HANDOVER headline'
)
path.write_text(text, encoding='utf-8')

# Kuraloviyam work README: top state + replace live-state tail.
path = ROOT / 'works/kuraloviyam/README.md'
text = path.read_text(encoding='utf-8')
text = replace_once(
    text,
    '| 003 | 223–333 | **Tamil ARCHIVAL-READY / CLOSED; English drafting + source-check + glossary COMPLETE / CLOSED; editorial review IN PROGRESS — ER1 + ER2 COMPLETE / PASS 66/111; ER3 next** |',
    '| 003 | 223–333 | **Tamil ARCHIVAL-READY / CLOSED; English drafting + source-check + glossary COMPLETE / CLOSED; editorial review IN PROGRESS — ER1 + ER2 + ER3 COMPLETE / PASS 99/111; ER4 next** |',
    'work README Part003 row'
)
text = replace_once(
    text,
    '## Part 003 — TAMIL ARCHIVAL-READY / CLOSED; ENGLISH DRAFTING + SOURCE-CHECK + GLOSSARY CLOSED; EDITORIAL REVIEW IN PROGRESS — ER1 + ER2 66/111',
    '## Part 003 — TAMIL ARCHIVAL-READY / CLOSED; ENGLISH DRAFTING + SOURCE-CHECK + GLOSSARY CLOSED; EDITORIAL REVIEW IN PROGRESS — ER1 + ER2 + ER3 99/111',
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
- Part 003 English editorial review: **IN PROGRESS — ER1 + ER2 + ER3 COMPLETE / PASS 99/111**;
- current Part-003 English state: **99 `editorial-reviewed` + 12 `source-checked` / 0 `draft` / 0 source-limited / 0 blocked**;
- Part-level review / release: **not-started**.

## Current frontier

**Next activity: Part 003 English Editorial Review ER4 — scans 322–333 / printed 305–316, final 12 pages.** Review readability, controlled terminology, names, repeated phrasing, quotations, Kural blocks, page function and cross-page continuity against the controlled glossary and audited Tamil context. Passing pages may move from `source-checked` to `editorial-reviewed`. Do not alter closed Tamil records or begin Part-level review/release work during ER4.

If ER4 passes, editorial review becomes **111/111 COMPLETE / CLOSED** and the next formal gate is the **whole-Part Part-level English review** for scans 223–333. External **333→334** remains deferred until Part 004 source intake. Part 004 remains blocked until the maintained Part-003 English workflow and final Part closure checkpoint are complete.'''
)

# Page map frontier row.
path = ROOT / 'works/kuraloviyam/indexes/page-map.md'
text = path.read_text(encoding='utf-8')
text = replace_once(
    text,
    '| 003 | 223–333 | 1–111 | scan 223 / printed 206 through scan 333 / printed 316 | **Tamil ARCHIVAL-READY / CLOSED; English drafting + source-check + glossary reconciliation COMPLETE / CLOSED — 111/111; editorial review ER1 + ER2 COMPLETE / PASS — 66/111; ER3 next** |',
    '| 003 | 223–333 | 1–111 | scan 223 / printed 206 through scan 333 / printed 316 | **Tamil ARCHIVAL-READY / CLOSED; English drafting + source-check + glossary reconciliation COMPLETE / CLOSED — 111/111; editorial review ER1 + ER2 + ER3 COMPLETE / PASS — 99/111; ER4 next** |',
    'page-map Part003 row'
)
path.write_text(text, encoding='utf-8')

# Source metadata: top row + live progress paragraph.
path = ROOT / 'works/kuraloviyam/metadata/source.md'
text = path.read_text(encoding='utf-8')
text = replace_once(
    text,
    '| 003 | 223–333 | 111 | `TVA_BOK_0065733_குறளோவியம்_part_003_pages_223-333.pdf` | **supplied; Tamil ARCHIVAL-READY / CLOSED; English drafting + source-check + glossary reconciliation COMPLETE / CLOSED — 111/111; editorial review ER1 + ER2 COMPLETE / PASS — 66/111; ER3 next** |',
    '| 003 | 223–333 | 111 | `TVA_BOK_0065733_குறளோவியம்_part_003_pages_223-333.pdf` | **supplied; Tamil ARCHIVAL-READY / CLOSED; English drafting + source-check + glossary reconciliation COMPLETE / CLOSED — 111/111; editorial review ER1 + ER2 + ER3 COMPLETE / PASS — 99/111; ER4 next** |',
    'source metadata Part003 row'
)
start = text.find('Historical Part-003 Pass-1 cadence was')
end = text.find('## Front-matter observations')
if start < 0 or end < 0 or end <= start:
    raise RuntimeError('source metadata live-progress replacement markers not found')
new_progress = '''Historical Part-003 Pass-1 cadence was **11 physical scans per normal iteration**, followed by a one-page final remainder at scan 333. Pass 1, Pass 2A, Pass 2B and Pass 3 are complete; the Part audit passed; final metadata/status synchronization closed all 111 records as textual and visual `verified`; documentation synchronization and the separate Tamil archival-ready checkpoint are closed. The maintained English layer has completed first-pass drafting **111/111**, source-check **111/111**, and glossary reconciliation **111/111**. Editorial review is **IN PROGRESS — ER1 + ER2 + ER3 COMPLETE / PASS, 99/111**, leaving **12** source-checked pages. The exact next editorial batch is the final remainder **ER4 scans 322–333 / printed 305–316, 12 pages**. Part-level review and release remain not-started. External **333→334** remains deferred until Part 004 source intake.

'''
text = text[:start] + new_progress + text[end:]
path.write_text(text, encoding='utf-8')

# English README: advance live summary and editorial tail.
path = ROOT / 'works/kuraloviyam/translations/en/README.md'
text = path.read_text(encoding='utf-8')
old_chunk = '''- source-check: **111/111 COMPLETE / CLOSED**;
- current English state: **66 `editorial-reviewed` + 45 `source-checked` / 0 `draft` / 0 source-limited / 0 blocked**;
- glossary reconciliation: **111/111 COMPLETE / CLOSED**;
- editorial review: **IN PROGRESS — ER1 + ER2 COMPLETE / PASS 66/111**;
- Part review / release: **not-started**.'''
new_chunk = '''- source-check: **111/111 COMPLETE / CLOSED**;
- current English state: **99 `editorial-reviewed` + 12 `source-checked` / 0 `draft` / 0 source-limited / 0 blocked**;
- glossary reconciliation: **111/111 COMPLETE / CLOSED**;
- editorial review: **IN PROGRESS — ER1 + ER2 + ER3 COMPLETE / PASS 99/111**;
- Part review / release: **not-started**.'''
text = replace_once(text, old_chunk, new_chunk, 'English README live summary')
path.write_text(text, encoding='utf-8')
replace_tail(
    path,
    '## Part 003 English editorial review — IN PROGRESS',
    '''## Part 003 English editorial review — IN PROGRESS

- ER1 **223–255 / 206–238 — COMPLETE / PASS 33/33**;
- ER2 **256–288 / 239–271 — COMPLETE / PASS 33/33**;
- ER3 **289–321 / 272–304 — COMPLETE / PASS 33/33**;
- cumulative editorial review: **99/111**;
- remaining editorial-review pages: **12**;
- current English state: **99 `editorial-reviewed` + 12 `source-checked`**;
- ER1 wording changes: **scans 246, 251, 255 only**;
- ER2 wording changes: **15 page files — scans 256, 258, 259, 260, 263, 264, 265, 269, 270, 273, 275, 279, 281, 285, 287**;
- ER3 wording changes: **14 page files — scans 289, 290, 292, 295, 298, 300, 304, 305, 308, 310, 313, 315, 316, 320**; the other **19 ER3 pages** changed only by status promotion;
- no Tamil archival record changed in ER1, ER2 or ER3.

ER3 preserved the genuine incoming **288→289** continuation and closed it on scan 289, preserved all Kural blocks and Chapter/Kural metadata, and left the clean outgoing **321→322** boundary intact. Meaning-sensitive smoothing on scans **295, 298, 304, 305, 308, 310, 313, 315–316** was checked against the audited Tamil records. No standard/published/web English wording was imported.

## Current frontier

Exact next activity: **Part 003 English Editorial Review ER4 — scans 322–333 / printed 305–316, final 12 pages**.

Review readability, controlled terminology, names, repeated phrasing, quotations, Kural blocks, page function and cross-page continuity. Consult audited Tamil whenever an editorial change could affect meaning. Passing pages may move from `source-checked` to `editorial-reviewed`.

If ER4 passes, editorial review becomes **111/111 COMPLETE / CLOSED** and the next formal gate is the **whole-Part Part-level English review**. Part 004 remains blocked until the maintained Part-003 English workflow and final Part closure checkpoint are complete.'''
)

# Detailed translation status: advance summary and replace editorial tail.
path = ROOT / 'works/kuraloviyam/translations/en/TRANSLATION_STATUS.md'
text = path.read_text(encoding='utf-8')
text = replace_once(
    text,
    '- editorial review: **IN PROGRESS — ER1 + ER2 COMPLETE / PASS 66/111**;',
    '- editorial review: **IN PROGRESS — ER1 + ER2 + ER3 COMPLETE / PASS 99/111**;',
    'translation status early editorial summary'
)
path.write_text(text, encoding='utf-8')
replace_tail(
    path,
    '## Part 003 English editorial review — IN PROGRESS',
    '''## Part 003 English editorial review — IN PROGRESS

- **ER1: scans 223–255 / printed 206–238 — COMPLETE / PASS 33/33**;
- **ER2: scans 256–288 / printed 239–271 — COMPLETE / PASS 33/33**;
- **ER3: scans 289–321 / printed 272–304 — COMPLETE / PASS 33/33**;
- cumulative editorial review: **99/111**;
- remaining editorial-review pages: **12**;
- current Part-003 English state: **99 `editorial-reviewed` + 12 `source-checked` / 0 `draft` / 0 source-limited / 0 blocked**;
- ER1 English wording changes: **3 page files — scans 246, 251, 255**;
- ER2 English wording changes: **15 page files — scans 256, 258, 259, 260, 263, 264, 265, 269, 270, 273, 275, 279, 281, 285, 287**;
- ER3 English wording changes: **14 page files — scans 289, 290, 292, 295, 298, 300, 304, 305, 308, 310, 313, 315, 316, 320**;
- ER3 status-only promotions: **19 page files**;
- Tamil page / metadata changes during ER1 + ER2 + ER3: **0**;
- no standard/published/web English Kural wording, external terminology or remembered rendering was imported.

ER3 was a source-faithful readability and continuity pass. The genuine **288→289** continuation remains intact and closes on scan 289; the clean **321→322** boundary remains clean. Kural blocks, Chapter/Kural metadata, visual/non-body page functions and controlled names/terms were preserved. Meaning-sensitive changes were checked against the audited Tamil, including the neck-embrace wording on **295**, the mutual-feast metaphor on **298**, the `பால்` wordplay on **304**, Ezhini's intermediary role on **305**, the cat/flower sequence on **308**, the judge-ruling continuation on **310**, Karmegam's expense sentence on **313**, the Seyizhai description across **315→316**, and the terrace sentence on **320**.

## Current frontier — Part 003 English Editorial Review ER4

Exact next activity: **editorial review scans 322–333 / printed 305–316 — final 12 page-aligned records**.

Review readability, controlled terminology, names, repeated phrasing, quotations, Kural blocks, page function and cross-page continuity. Consult the matching audited Tamil whenever an editorial change could affect meaning. Make only source-faithful editorial improvements. Passing pages may move from `source-checked` to `editorial-reviewed`.

Do not begin Part-level review or release work during ER4. If ER4 passes, editorial review becomes **111/111 COMPLETE / CLOSED** and the next gate is **whole-Part Part-level English review** for scans 223–333.

Part 004 remains blocked until Part 003 completes Part review, release report/release-ready synchronization and the final Part closure checkpoint.'''
)

# Work-specific handover: live state and editorial tail.
path = ROOT / 'works/kuraloviyam/HANDOVER.md'
text = path.read_text(encoding='utf-8')
text = replace_once(
    text,
    '- current English state: **66 `editorial-reviewed` + 45 `source-checked` / 0 `draft` / 0 source-limited / 0 blocked**;',
    '- current English state: **99 `editorial-reviewed` + 12 `source-checked` / 0 `draft` / 0 source-limited / 0 blocked**;',
    'work handover English state'
)
text = replace_once(
    text,
    '- editorial review: **IN PROGRESS — ER1 + ER2 COMPLETE / PASS 66/111**;',
    '- editorial review: **IN PROGRESS — ER1 + ER2 + ER3 COMPLETE / PASS 99/111**;',
    'work handover editorial summary'
)
path.write_text(text, encoding='utf-8')
replace_tail(
    path,
    '## Editorial review progress — ER1 + ER2 COMPLETE / PASS 66/111',
    '''## Editorial review progress — ER1 + ER2 + ER3 COMPLETE / PASS 99/111

- ER1 **223–255 / printed 206–238 — COMPLETE / PASS 33/33**;
- ER2 **256–288 / printed 239–271 — COMPLETE / PASS 33/33**;
- ER3 **289–321 / printed 272–304 — COMPLETE / PASS 33/33**;
- English state: **99 editorial-reviewed + 12 source-checked**;
- ER1 wording changes limited to scans **246, 251, 255**;
- ER2 wording changes limited to scans **256, 258, 259, 260, 263, 264, 265, 269, 270, 273, 275, 279, 281, 285, 287**;
- ER3 wording changes limited to scans **289, 290, 292, 295, 298, 300, 304, 305, 308, 310, 313, 315, 316, 320**;
- the other **19 ER3 pages** changed only by status promotion;
- Tamil changes: **0**;
- source-supported Kural blocks, page functions and range continuities preserved, including genuine incoming **288→289** and clean outgoing **321→322**.

## Exact next activity — English Editorial Review ER4

Process **scans 322–333 / printed 305–316 — FINAL 12 PAGE-ALIGNED RECORDS**.

1. fetch live `main` first;
2. confirm Part 003 Tamil remains **ARCHIVAL-READY / CLOSED** and English drafting, source-check and glossary reconciliation remain **111/111 COMPLETE / CLOSED**;
3. confirm editorial review is **99/111** with scans **223–321** `editorial-reviewed`;
4. read `translations/en/TRANSLATION_GUIDE.md`, `TRANSLATION_STATUS.md`, `GLOSSARY.md`, and English records **0322–0333**, consulting matching audited Tamil wherever an editorial choice could affect meaning;
5. review readability, controlled terminology, names, repeated phrasing, quotations, Kural blocks, page function and cross-page continuity;
6. make only source-faithful editorial improvements; do not import standard/published/web English wording or terminology from memory;
7. passing pages may move from `source-checked` to `editorial-reviewed`;
8. do not alter Tamil files;
9. do not begin Part-level review or release work during ER4;
10. update `TRANSLATION_STATUS.md` and audit the exact changed-file set.

If ER4 passes, editorial review becomes **111/111 COMPLETE / CLOSED** and the next activity is the **whole-Part Part-level English review — scans 223–333 / printed 206–316**. External **333→334** remains deferred until Part 004 source intake. Part 004 remains blocked until the maintained English workflow and final Part closure checkpoint are complete.'''
)

# Next-chat prompt: advance durable state and replace editorial frontier tail.
path = ROOT / 'NEXT_CHAT_PROMPT_KURALOVIYAM.md'
text = path.read_text(encoding='utf-8')
text = replace_once(
    text,
    '- current Part-003 English state: **66 `editorial-reviewed` + 45 `source-checked` / 0 `draft` / 0 source-limited / 0 blocked**.',
    '- current Part-003 English state: **99 `editorial-reviewed` + 12 `source-checked` / 0 `draft` / 0 source-limited / 0 blocked**.',
    'next prompt English state'
)
text = replace_once(
    text,
    '- editorial review: **IN PROGRESS — ER1 + ER2 COMPLETE / PASS 66/111**; Part review / release: **not-started**.',
    '- editorial review: **IN PROGRESS — ER1 + ER2 + ER3 COMPLETE / PASS 99/111**; Part review / release: **not-started**.',
    'next prompt editorial summary'
)
path.write_text(text, encoding='utf-8')
replace_tail(
    path,
    '## Editorial review progress',
    '''## Editorial review progress

- ER1 **scans 223–255 / printed 206–238 — COMPLETE / PASS 33/33**;
- ER2 **scans 256–288 / printed 239–271 — COMPLETE / PASS 33/33**;
- ER3 **scans 289–321 / printed 272–304 — COMPLETE / PASS 33/33**;
- cumulative editorial review **99/111**;
- current page state **99 editorial-reviewed + 12 source-checked**;
- ER1 wording changes were limited to scans **246, 251, 255**;
- ER2 wording changes were limited to scans **256, 258, 259, 260, 263, 264, 265, 269, 270, 273, 275, 279, 281, 285, 287**;
- ER3 wording changes were limited to scans **289, 290, 292, 295, 298, 300, 304, 305, 308, 310, 313, 315, 316, 320**; the other **19** pages were status-only promotions;
- no Tamil record changed;
- genuine **288→289** remains preserved and closes on scan 289; clean **321→322** remains clean.

## Exact next activity — Part 003 English Editorial Review ER4

Process **scans 322–333 / printed 305–316 — final 12 page-aligned records**.

Requirements:

1. fetch live `main` first and preserve newer durable work;
2. confirm `PART_003_TAMIL_ARCHIVAL_READY.md` remains **PASS / CLOSED**;
3. confirm English drafting, source-check and glossary reconciliation are each **111/111 COMPLETE / CLOSED**, and editorial review is **99/111**;
4. read `translations/en/TRANSLATION_GUIDE.md`, `GLOSSARY.md`, and English records **0322–0333** with matching audited Tamil wherever meaning-sensitive editorial decisions arise;
5. review readability, controlled terminology, names, repeated phrasing, quotations, Kural blocks, page function and cross-page continuity;
6. make only source-faithful editorial improvements; do not import standard/published/web English Kural wording, another edition's terminology, or memory;
7. passing pages may move from `source-checked` to `editorial-reviewed`;
8. do not alter any Tamil page record or Tamil metadata;
9. do not begin Part-level review or release work during ER4;
10. update `TRANSLATION_STATUS.md` and audit the exact changed-file set before advancing.

If ER4 passes, editorial review becomes **111/111 COMPLETE / CLOSED** and the next activity is the **whole-Part Part-level English review — scans 223–333 / printed 206–316**. Part 004 remains blocked until Part 003 completes Part review, release report/release-ready synchronization and final Part closure. External **333→334** remains deferred until Part 004 source intake.'''
)

# Archival guideline current frontier.
path = ROOT / 'KURALOVIYAM_ARCHIVAL_GUIDELINES.md'
text = path.read_text(encoding='utf-8')
text = replace_once(
    text,
    '- English editorial review: **IN PROGRESS — ER1 + ER2 COMPLETE / PASS 66/111**; current page state **66 editorial-reviewed + 45 source-checked**; Part review / release are not started.',
    '- English editorial review: **IN PROGRESS — ER1 + ER2 + ER3 COMPLETE / PASS 99/111**; current page state **99 editorial-reviewed + 12 source-checked**; Part review / release are not started.',
    'guidelines editorial frontier bullet'
)
path.write_text(text, encoding='utf-8')
replace_tail(
    path,
    '### Exact next content stage',
    '''### Exact next content stage

Perform **Part 003 English Editorial Review ER4 — scans 322–333 / printed 305–316, final 12 page-aligned records**. Review readability and consistency against the controlled glossary and audited Tamil context; consult Tamil whenever a change could affect meaning; passing pages may move from `source-checked` to `editorial-reviewed`; do not begin Part-level review or release work during ER4; do not alter closed Tamil records.

If ER4 passes, editorial review becomes **111/111 COMPLETE / CLOSED** and the next formal gate is the **whole-Part Part-level English review**. Part 004 remains blocked until the maintained Part-003 English workflow and final Part closure checkpoint are complete.'''
)

# Assert live-control strings are present after synchronization.
checks = {
    ROOT / 'HANDOVER.md': ['ER1 + ER2 + ER3 COMPLETE / PASS 99/111, ER4 next'],
    ROOT / 'works/kuraloviyam/HANDOVER.md': ['99 editorial-reviewed + 12 source-checked', 'Editorial Review ER4'],
    ROOT / 'NEXT_CHAT_PROMPT_KURALOVIYAM.md': ['cumulative editorial review **99/111**', 'Editorial Review ER4'],
    ROOT / 'KURALOVIYAM_ARCHIVAL_GUIDELINES.md': ['ER1 + ER2 + ER3 COMPLETE / PASS 99/111', 'Editorial Review ER4'],
    ROOT / 'works/kuraloviyam/README.md': ['ER1 + ER2 + ER3 COMPLETE / PASS 99/111', 'Editorial Review ER4'],
    ROOT / 'works/kuraloviyam/indexes/page-map.md': ['ER1 + ER2 + ER3 COMPLETE / PASS — 99/111; ER4 next'],
    ROOT / 'works/kuraloviyam/metadata/source.md': ['ER1 + ER2 + ER3 COMPLETE / PASS — 99/111; ER4 next'],
    ROOT / 'works/kuraloviyam/translations/en/README.md': ['cumulative editorial review: **99/111**', 'Editorial Review ER4'],
    ROOT / 'works/kuraloviyam/translations/en/TRANSLATION_STATUS.md': ['cumulative editorial review: **99/111**', 'Editorial Review ER4'],
}
for p, needles in checks.items():
    body = p.read_text(encoding='utf-8')
    for needle in needles:
        if needle not in body:
            raise RuntimeError(f'{p}: expected synchronized text missing: {needle!r}')

# Exact changed-file gate: 33 ER3 English pages + 9 durable controls, no Tamil.
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

# Confirm all ER3 pages promoted and wording-change count remains the intended 14 files.
for scan in range(289, 322):
    printed = scan - 17
    body = (PAGES / f'{scan:04d}-kuraloviyam-{printed}.md').read_text(encoding='utf-8')
    if body.count('status: "editorial-reviewed"') != 1 or 'status: "source-checked"' in body:
        raise RuntimeError(f'scan {scan}: final editorial status gate failed')
if changed_wording_pages != {289, 290, 292, 295, 298, 300, 304, 305, 308, 310, 313, 315, 316, 320}:
    raise RuntimeError('wording-change page inventory drifted')

print('ER3 prepared: 33/33 pages, 14 wording-change pages, 19 status-only pages, 9 control docs; 0 Tamil changes')
