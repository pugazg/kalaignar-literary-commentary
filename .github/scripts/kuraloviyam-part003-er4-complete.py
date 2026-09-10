from pathlib import Path
import re
import subprocess

ROOT = Path('.')
PAGES = ROOT / 'works/kuraloviyam/translations/en/pages'


def replace_once(text: str, old: str, new: str, label: str) -> str:
    n = text.count(old)
    if n != 1:
        raise RuntimeError(f'{label}: expected exactly 1 match, found {n}')
    return text.replace(old, new, 1)


def regex_once(text: str, pattern: str, repl: str, label: str, flags=0) -> str:
    out, n = re.subn(pattern, repl, text, count=1, flags=flags)
    if n != 1:
        raise RuntimeError(f'{label}: expected exactly 1 regex match, found {n}')
    return out


def replace_tail(path: Path, marker_pattern: str, new_tail: str) -> None:
    text = path.read_text(encoding='utf-8')
    m = re.search(marker_pattern, text, flags=re.M)
    if not m:
        raise RuntimeError(f'{path}: tail marker not found: {marker_pattern!r}')
    path.write_text(text[:m.start()] + new_tail.rstrip() + '\n', encoding='utf-8')


WORDING_CHANGES = {
    322: [
        (
            'One day, a teacher was explaining to his students the Kurals in the chapter called “Knowing One\'s Strength,” which appears under the subject of politics in the Kural. Among his students was one with only half-baked understanding. The teacher explained that many scholars had interpreted the Kurals from different angles according to the learning they possessed and that, in keeping with Valluvar\'s own clear instruction—“Whatever a thing may be, and of whatever nature, wisdom is to discern its true substance”—one must acquire the intelligence to examine those interpretations and accept what is sound.',
            'One day, a teacher was explaining to his students the Kurals in the chapter “Knowing One\'s Strength,” under the Kural\'s heading of politics. Among his students was one with only half-baked understanding. The teacher explained that many scholars had interpreted the Kurals from different angles according to their learning and that, in keeping with Valluvar\'s own clear instruction—“Whatever a thing may be, and of whatever nature, wisdom is to discern its true substance”—one must develop the discernment to examine those interpretations and accept what is sound.'
        )
    ],
    323: [
        (
            'An administration must frame its programmes only after calculating whether the resources it already has, the resources it can create, and those it can earn in future will remain sufficient in the treasury to accomplish what it proposes. Otherwise, for the sake of attractive publicity and without considering the strength of the treasury, many have launched schemes with enthusiasm and drive, only to fail later because they had no means to complete them.',
            'An administration must frame its programmes only after calculating whether the resources it has, can create, and can earn in future will leave the treasury strong enough to accomplish what it proposes. Otherwise, for the sake of attractive publicity and without considering the strength of the treasury, many have launched schemes with enthusiasm and drive, only to fail later for lack of means to complete them.'
        )
    ],
    325: [
        (
            'She continued walking without saying anything in objection.',
            'She kept walking without voicing any objection.'
        ),
        (
            'Beside a boat, darkness was slowly spreading its rule.',
            'Near a boat, darkness was slowly spreading its rule.'
        )
    ],
    327: [
        (
            'Until now, you and I have only heard what is said about Yama.',
            'Until now, you and I have only heard people speak of Yama.'
        )
    ],
    329: [
        (
            'That is the story of a woman told by Valluvar.',
            'That is the story of a woman as Valluvar tells it.'
        )
    ],
    331: [
        (
            'But if he becomes ready to take any crooked path in order to obtain it, that desire makes him lose the respect of human society and climbs onto his head as a heavy burden.',
            'But if he becomes ready to take any crooked path in order to obtain it, that desire makes him lose the respect of human society and then climbs onto his head as a heavy burden.'
        )
    ],
    333: [
        (
            'The next target of that tiger-like crowd, enraged after marching on the prison, was the palace itself.',
            'The next target of that tiger-like crowd, now enraged after storming the prison, was the palace itself.'
        )
    ],
}

expected_pages = []
for scan in range(322, 334):
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

# Root handover headline.
path = ROOT / 'HANDOVER.md'
text = path.read_text(encoding='utf-8')
text = regex_once(
    text,
    r'^Last refreshed for Kuraloviyam .*$',
    'Last refreshed for Kuraloviyam **Part 003 Tamil ARCHIVAL-READY / CLOSED; English drafting + source-check + glossary + editorial review COMPLETE / CLOSED 111/111; Part-level English review next**: **2026-09-10**.',
    'root HANDOVER headline',
    flags=re.M,
)
path.write_text(text, encoding='utf-8')

# Work README: table row, heading, live-state tail.
path = ROOT / 'works/kuraloviyam/README.md'
text = path.read_text(encoding='utf-8')
text = regex_once(text, r'^\| 003 \| 223–333 \|.*$', '| 003 | 223–333 | **Tamil ARCHIVAL-READY / CLOSED; English drafting + source-check + glossary + editorial review COMPLETE / CLOSED — 111/111; Part-level English review next** |', 'work README Part003 row', flags=re.M)
text = regex_once(text, r'^## Part 003 —.*$', '## Part 003 — TAMIL ARCHIVAL-READY / CLOSED; ENGLISH DRAFTING + SOURCE-CHECK + GLOSSARY + EDITORIAL REVIEW COMPLETE / CLOSED — 111/111', 'work README Part003 heading', flags=re.M)
path.write_text(text, encoding='utf-8')
replace_tail(path, r'^## Current durable state$', '''## Current durable state

- Part 003 Tamil: **ARCHIVAL-READY / CLOSED — 111 textual verified + 111 visual verified / 0 exceptions**;
- Part 003 English drafting: **111/111 COMPLETE / CLOSED**;
- Part 003 English source-check: **111/111 COMPLETE / CLOSED**;
- Part 003 English glossary reconciliation: **111/111 COMPLETE / CLOSED**;
- Part 003 English editorial review: **111/111 COMPLETE / CLOSED**;
- current Part-003 English state: **111 `editorial-reviewed` + 0 `source-checked` / 0 `draft` / 0 source-limited / 0 blocked**;
- Part-level review / release: **not-started**.

## Current frontier

**Next activity: Part 003 whole-Part English review — scans 223–333 / printed 206–316, 111 pages.** Verify exact Tamil/English page inventory and alignment, final English statuses, controlled terminology and names, Chapter/Kural metadata, Kural-block separation, visual/non-body page functions, and all accumulated cross-page continuities. Create the durable review record under `works/kuraloviyam/translations/en/reviews/`. Do **not** promote pages to `release-ready` during Part-level review.

External **333→334** remains deferred until Part 004 source intake. Part 004 remains blocked until Part 003 completes Part-level review, release report/release-ready synchronization and the final Part closure checkpoint.''')

# Page map row.
path = ROOT / 'works/kuraloviyam/indexes/page-map.md'
text = path.read_text(encoding='utf-8')
text = regex_once(text, r'^\| 003 \| 223–333 \| 1–111 \|.*$', '| 003 | 223–333 | 1–111 | scan 223 / printed 206 through scan 333 / printed 316 | **Tamil ARCHIVAL-READY / CLOSED; English drafting + source-check + glossary reconciliation + editorial review COMPLETE / CLOSED — 111/111; Part-level English review next** |', 'page-map Part003 row', flags=re.M)
path.write_text(text, encoding='utf-8')

# Source metadata.
path = ROOT / 'works/kuraloviyam/metadata/source.md'
text = path.read_text(encoding='utf-8')
text = regex_once(text, r'^\| 003 \| 223–333 \| 111 \| `TVA_BOK_0065733_குறளோவியம்_part_003_pages_223-333\.pdf` \|.*$', '| 003 | 223–333 | 111 | `TVA_BOK_0065733_குறளோவியம்_part_003_pages_223-333.pdf` | **supplied; Tamil ARCHIVAL-READY / CLOSED; English drafting + source-check + glossary reconciliation + editorial review COMPLETE / CLOSED — 111/111; Part-level English review next** |', 'source metadata Part003 row', flags=re.M)
start = text.find('Historical Part-003 Pass-1 cadence was')
end = text.find('## Front-matter observations')
if start < 0 or end < 0 or end <= start:
    raise RuntimeError('source metadata live-progress markers not found')
new_progress = '''Historical Part-003 Pass-1 cadence was **11 physical scans per normal iteration**, followed by a one-page final remainder at scan 333. Pass 1, Pass 2A, Pass 2B and Pass 3 are complete; the Part audit passed; final metadata/status synchronization closed all 111 records as textual and visual `verified`; documentation synchronization and the separate Tamil archival-ready checkpoint are closed. The maintained English layer has completed first-pass drafting **111/111**, source-check **111/111**, glossary reconciliation **111/111**, and editorial review **111/111 COMPLETE / CLOSED**. The exact next gate is the **whole-Part English review for scans 223–333 / printed 206–316**. Release report/release-ready promotion remains not-started. External **333→334** remains deferred until Part 004 source intake.

'''
text = text[:start] + new_progress + text[end:]
path.write_text(text, encoding='utf-8')

# English README: normalize live state and replace editorial tail.
path = ROOT / 'works/kuraloviyam/translations/en/README.md'
text = path.read_text(encoding='utf-8')
text = text.replace('99 `editorial-reviewed` + 12 `source-checked`', '111 `editorial-reviewed` + 0 `source-checked`')
text = text.replace('editorial review: **IN PROGRESS — ER1 + ER2 + ER3 COMPLETE / PASS 99/111**;', 'editorial review: **111/111 COMPLETE / CLOSED**;')
path.write_text(text, encoding='utf-8')
replace_tail(path, r'^## Part 003 English editorial review — IN PROGRESS$', '''## Part 003 English editorial review — COMPLETE / CLOSED

- ER1 **223–255 / 206–238 — COMPLETE / PASS 33/33**;
- ER2 **256–288 / 239–271 — COMPLETE / PASS 33/33**;
- ER3 **289–321 / 272–304 — COMPLETE / PASS 33/33**;
- ER4 **322–333 / 305–316 — COMPLETE / PASS 12/12 / FINAL REMAINDER**;
- cumulative editorial review: **111/111 COMPLETE / CLOSED**;
- current English state: **111 `editorial-reviewed` + 0 `source-checked` / 0 `draft` / 0 source-limited / 0 blocked**;
- ER4 wording changes: **7 page files — scans 322, 323, 325, 327, 329, 331, 333**; the other 5 ER4 pages changed only by status promotion;
- no Tamil archival record changed in ER4.

ER4 preserved the clean incoming **321→322** boundary, the genuine **322→323** and **332→333** continuities, and the closed Part endpoint at scan **333 / printed 316**. External **333→334** remains deferred. No standard/published/web English wording was imported.

## Current frontier

Exact next activity: **Part 003 whole-Part English review — scans 223–333 / printed 206–316, 111 pages**.

Verify page inventory/alignment, exact final statuses, controlled terminology and names, Chapter/Kural numbering and labels, Kural-block separation, visual/non-body page functions, and accumulated continuities. Create `reviews/PART_003_ENGLISH_REVIEW.md` as the durable whole-Part review record. Do **not** promote pages to `release-ready` during this gate.

Part 004 remains blocked until Part 003 completes Part-level review, release report/release-ready synchronization and final Part closure.''')

# Translation status: normalize summary and replace editorial tail.
path = ROOT / 'works/kuraloviyam/translations/en/TRANSLATION_STATUS.md'
text = path.read_text(encoding='utf-8')
text = text.replace('- editorial review: **IN PROGRESS — ER1 + ER2 + ER3 COMPLETE / PASS 99/111**;', '- editorial review: **111/111 COMPLETE / CLOSED**;')
path.write_text(text, encoding='utf-8')
replace_tail(path, r'^## Part 003 English editorial review — IN PROGRESS$', '''## Part 003 English editorial review — COMPLETE / CLOSED

- **ER1: scans 223–255 / printed 206–238 — COMPLETE / PASS 33/33**;
- **ER2: scans 256–288 / printed 239–271 — COMPLETE / PASS 33/33**;
- **ER3: scans 289–321 / printed 272–304 — COMPLETE / PASS 33/33**;
- **ER4: scans 322–333 / printed 305–316 — COMPLETE / PASS 12/12 / FINAL REMAINDER**;
- cumulative editorial review: **111/111 COMPLETE / CLOSED**;
- remaining editorial-review pages: **0**;
- current Part-003 English state: **111 `editorial-reviewed` + 0 `source-checked` / 0 `draft` / 0 source-limited / 0 blocked**;
- ER1 wording changes: **3 page files — scans 246, 251, 255**;
- ER2 wording changes: **15 page files — scans 256, 258, 259, 260, 263, 264, 265, 269, 270, 273, 275, 279, 281, 285, 287**;
- ER3 wording changes: **14 page files — scans 289, 290, 292, 295, 298, 300, 304, 305, 308, 310, 313, 315, 316, 320**;
- ER4 wording changes: **7 page files — scans 322, 323, 325, 327, 329, 331, 333**;
- ER4 status-only promotions: **5 page files**;
- Tamil page / metadata changes during ER1–ER4: **0**;
- no standard/published/web English Kural wording, external terminology or remembered rendering was imported.

ER4 was a source-faithful readability pass against the audited Tamil final range. It preserved the clean **321→322** boundary; genuine **322→323** continuation; clean **323→324, 325→326, 327→328, 329→330, 331→332** boundaries; genuine **324→325, 326→327, 328→329, 330→331, 332→333** continuities; and the Part close at scan **333**. The final **332→333** severe-rule/famine vignette remains intact. External **333→334** remains deferred until Part 004 source intake.

## Current frontier — Part 003 whole-Part English review

Exact next activity: **review scans 223–333 / printed 206–316 as one whole Part**.

Verify the exact 111-page Tamil/English inventory and filename alignment, final status distribution, controlled terminology and names, Chapter/Kural metadata, Kural-block separation, visual/non-body page functions, and all accumulated continuities. Create a durable review record at `works/kuraloviyam/translations/en/reviews/PART_003_ENGLISH_REVIEW.md`. Do **not** promote any page to `release-ready` during Part-level review.

If the whole-Part review passes, the next gate is the Part 003 English release report. Part 004 remains blocked until release-ready synchronization and the final Part closure checkpoint are complete.''')

# Work handover.
path = ROOT / 'works/kuraloviyam/HANDOVER.md'
text = path.read_text(encoding='utf-8')
text = text.replace('99 `editorial-reviewed` + 12 `source-checked`', '111 `editorial-reviewed` + 0 `source-checked`')
text = text.replace('- editorial review: **IN PROGRESS — ER1 + ER2 + ER3 COMPLETE / PASS 99/111**;', '- editorial review: **111/111 COMPLETE / CLOSED**;')
path.write_text(text, encoding='utf-8')
replace_tail(path, r'^## Editorial review progress —.*$', '''## Editorial review progress — COMPLETE / CLOSED 111/111

- ER1 **223–255 / printed 206–238 — COMPLETE / PASS 33/33**;
- ER2 **256–288 / printed 239–271 — COMPLETE / PASS 33/33**;
- ER3 **289–321 / printed 272–304 — COMPLETE / PASS 33/33**;
- ER4 **322–333 / printed 305–316 — COMPLETE / PASS 12/12 / FINAL REMAINDER**;
- English state: **111 editorial-reviewed + 0 source-checked**;
- ER4 wording changes limited to scans **322, 323, 325, 327, 329, 331, 333**; the other five ER4 pages were status-only promotions;
- Tamil changes: **0**;
- clean/genuine page relationships through final **332→333** preserved; external **333→334** remains deferred.

## Exact next activity — Part 003 whole-Part English review

Review **scans 223–333 / printed 206–316 — all 111 page-aligned records as one Part**.

1. fetch live `main` first;
2. confirm Part 003 Tamil remains **ARCHIVAL-READY / CLOSED** and English drafting, source-check, glossary reconciliation and editorial review are each **111/111 COMPLETE / CLOSED**;
3. confirm all 111 English pages are `editorial-reviewed`, with 0 source-checked/draft/source-limited/blocked/release-ready;
4. verify exact Tamil/English inventory and filename alignment, controlled terminology/names, Chapter/Kural numbering and labels, Kural-block separation, visual/non-body page functions and accumulated continuities;
5. create `translations/en/reviews/PART_003_ENGLISH_REVIEW.md` as the durable review record;
6. do **not** change page status to `release-ready` and do not begin Part 004;
7. update controls and audit the exact changed-file set.

If Part-level review passes, the next gate is the **Part 003 English release report**. External **333→334** remains deferred until Part 004 source intake.''')

# Next-chat prompt.
path = ROOT / 'NEXT_CHAT_PROMPT_KURALOVIYAM.md'
text = path.read_text(encoding='utf-8')
text = text.replace('99 `editorial-reviewed` + 12 `source-checked`', '111 `editorial-reviewed` + 0 `source-checked`')
text = text.replace('- editorial review: **IN PROGRESS — ER1 + ER2 + ER3 COMPLETE / PASS 99/111**; Part review / release: **not-started**.', '- editorial review: **111/111 COMPLETE / CLOSED**; Part review / release: **not-started**.')
path.write_text(text, encoding='utf-8')
replace_tail(path, r'^## Editorial review progress$', '''## Editorial review progress

- ER1 **scans 223–255 / printed 206–238 — COMPLETE / PASS 33/33**;
- ER2 **scans 256–288 / printed 239–271 — COMPLETE / PASS 33/33**;
- ER3 **scans 289–321 / printed 272–304 — COMPLETE / PASS 33/33**;
- ER4 **scans 322–333 / printed 305–316 — COMPLETE / PASS 12/12 / FINAL REMAINDER**;
- cumulative editorial review **111/111 COMPLETE / CLOSED**;
- current page state **111 editorial-reviewed + 0 source-checked**;
- ER4 wording changes were limited to scans **322, 323, 325, 327, 329, 331, 333**; the other five pages were status-only promotions;
- no Tamil record changed;
- final-range continuities and clean boundaries are preserved through genuine **332→333**; external **333→334** remains deferred.

## Exact next activity — Part 003 whole-Part English review

Review **scans 223–333 / printed 206–316 — 111 page-aligned records as one Part**.

Requirements:

1. fetch live `main` first and preserve newer durable work;
2. confirm `PART_003_TAMIL_ARCHIVAL_READY.md` remains **PASS / CLOSED**;
3. confirm English drafting, source-check, glossary reconciliation and editorial review are each **111/111 COMPLETE / CLOSED**;
4. confirm exactly **111 `editorial-reviewed`** pages and zero `source-checked`, `draft`, source-limited, blocked or release-ready pages;
5. verify inventory/alignment, controlled terminology and names, Chapter/Kural metadata and labels, Kural-block separation, visual/non-body page functions and all accumulated continuities across the Part;
6. create durable review record `works/kuraloviyam/translations/en/reviews/PART_003_ENGLISH_REVIEW.md`;
7. do not promote pages to `release-ready` during Part-level review;
8. do not begin Part 004; external **333→334** remains deferred;
9. update `TRANSLATION_STATUS.md` and related live controls and audit the exact changed-file set.

If the Part-level review passes, the next gate is the **Part 003 English release report**. Part 004 remains blocked until release-ready synchronization and final Part closure.''')

# Archival guidelines frontier.
path = ROOT / 'KURALOVIYAM_ARCHIVAL_GUIDELINES.md'
text = path.read_text(encoding='utf-8')
text = text.replace('99 editorial-reviewed + 12 source-checked', '111 editorial-reviewed + 0 source-checked')
text = regex_once(text, r'^- English editorial review: .*$', '- English editorial review: **COMPLETE / CLOSED — 111/111**; current page state **111 editorial-reviewed + 0 source-checked**; Part review / release are not started.', 'guidelines editorial bullet', flags=re.M)
path.write_text(text, encoding='utf-8')
replace_tail(path, r'^### Exact next content stage$', '''### Exact next content stage

Perform the **Part 003 whole-Part English review — scans 223–333 / printed 206–316, 111 page-aligned records**. Verify inventory/alignment, final statuses, controlled terminology/names, Chapter/Kural metadata, Kural-block separation, visual/non-body page functions and accumulated continuities. Create the durable review record under `translations/en/reviews/`. Do **not** promote pages to `release-ready` during Part-level review and do not alter closed Tamil records.

If Part-level review passes, proceed next to the **Part 003 English release report**. Part 004 remains blocked until release-ready synchronization and the final Part closure checkpoint are complete.''')

# Invariant and changed-file gates.
for scan in range(322, 334):
    printed = scan - 17
    body = (PAGES / f'{scan:04d}-kuraloviyam-{printed}.md').read_text(encoding='utf-8')
    if body.count('status: "editorial-reviewed"') != 1 or 'status: "source-checked"' in body:
        raise RuntimeError(f'scan {scan}: final editorial status gate failed')
    if body.count('source_tamil_status: "verified"') != 1:
        raise RuntimeError(f'scan {scan}: Tamil-status reference drift')

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
    raise RuntimeError(f'changed-file gate failed; missing={sorted(expected-actual)}; extra={sorted(actual-expected)}')
if any(p.startswith('works/kuraloviyam/pages/') for p in actual):
    raise RuntimeError('Tamil page change detected')
if len(actual) != 21:
    raise RuntimeError(f'expected 21 durable changed files, found {len(actual)}')

print('ER4 prepared: 12/12 pages, 7 wording-change pages, 5 status-only pages, 9 control docs; 0 Tamil changes')
