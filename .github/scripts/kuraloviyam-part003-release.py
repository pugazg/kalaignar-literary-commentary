from pathlib import Path
import re, subprocess

ROOT = Path('.')
PAGES = ROOT / 'works/kuraloviyam/translations/en/pages'
BASE = '933ae23e405f13f014cd9c1fa93b575699c0c9d2'
REVIEW = ROOT / 'works/kuraloviyam/translations/en/reviews/PART_003_ENGLISH_REVIEW.md'
REPORT = ROOT / 'works/kuraloviyam/translations/en/reviews/PART_003_ENGLISH_RELEASE_REPORT.md'


def replace_once(text, old, new, label):
    n = text.count(old)
    if n != 1:
        raise RuntimeError(f'{label}: expected 1 match, found {n}')
    return text.replace(old, new, 1)


def regex_once(text, pattern, repl, label, flags=0):
    out, n = re.subn(pattern, repl, text, count=1, flags=flags)
    if n != 1:
        raise RuntimeError(f'{label}: expected 1 regex match, found {n}')
    return out


def replace_tail(path, marker, new_tail):
    text = path.read_text(encoding='utf-8')
    m = re.search(marker, text, flags=re.M)
    if not m:
        raise RuntimeError(f'{path}: tail marker not found')
    path.write_text(text[:m.start()] + new_tail.rstrip() + '\n', encoding='utf-8')

# Gate authority.
review_text = REVIEW.read_text(encoding='utf-8')
for token in ['**PASS**', 'PART 003 PART-LEVEL ENGLISH REVIEW: PASS', '111 `editorial-reviewed`', '`release-ready` remains **0/111**']:
    if token not in review_text:
        raise RuntimeError(f'review gate missing token: {token}')

# Release promotion: exactly one status-token change per page.
page_paths = []
originals = {}
for scan in range(223, 334):
    printed = scan - 17
    path = PAGES / f'{scan:04d}-kuraloviyam-{printed}.md'
    if not path.exists():
        raise RuntimeError(f'missing English page {path}')
    text = path.read_text(encoding='utf-8')
    originals[path] = text
    checks = [
        f'source_scan_page: {scan}',
        f'printed_page: "{printed}"',
        'translation_type: "project_translation"',
        'source_tamil_status: "verified"',
    ]
    for c in checks:
        if c not in text:
            raise RuntimeError(f'{path}: missing invariant {c}')
    if text.count('status: "editorial-reviewed"') != 1 or 'status: "release-ready"' in text:
        raise RuntimeError(f'{path}: invalid pre-release status')
    new = text.replace('status: "editorial-reviewed"', 'status: "release-ready"', 1)
    if new.replace('status: "release-ready"', 'status: "editorial-reviewed"', 1) != text:
        raise RuntimeError(f'{path}: status-only invariant failed')
    path.write_text(new, encoding='utf-8')
    page_paths.append(str(path))

# Durable release report.
REPORT.write_text(f'''# Part 003 English Release Report — Kuraloviyam

## Decision

**APPROVED FOR RELEASE**

This report closes the Part 003 English release-report gate for `குறளோவியம்`, overall scans **223–333 / printed 206–316**.

Release base / clean authoritative prior-gate HEAD: `{BASE}`

Authoritative prior gate: `works/kuraloviyam/translations/en/reviews/PART_003_ENGLISH_REVIEW.md` — **PASS / CLOSED**.

## Release scope

- English page records in Part 003: **111**
- eligible for `release-ready`: **111**
- source-limited: **0**
- blocked: **0**
- body-text changes in this release gate: **0**
- Tamil page changes: **0**
- glossary changes: **0**

The Part-level review established a complete pre-release state of exactly **111 `editorial-reviewed`** pages with inventory/alignment, terminology, Chapter/Kural metadata, Kural-block separation, visual/non-body handling, and accumulated continuity checks all passing.

## Release promotion — PASS

All **111** eligible English page records, scans **223–333**, were promoted from:

`status: "editorial-reviewed"`

to:

`status: "release-ready"`

Approved English wording is unchanged. Every page-layer modification in this gate is the single status-token replacement only.

## Source and terminology integrity

The release preserves the controls already closed by source-check, glossary reconciliation, editorial review and Part-level review. Translation identity remains project-created; no standard/published/web English Kural wording, external edition prose, another commentator or remembered conventional rendering was imported. Controlled terminology, names and Chapter/Kural labels remain as approved in `GLOSSARY.md`; Kural blocks remain distinct from surrounding prose; visual and non-body material remain separately represented where required.

## Part boundary

Scan **333 / printed 316** closes the supplied Part 003 severe-rule / famine vignette. The adjacent **333→334** split boundary remains explicitly deferred until Part 004 source intake. This release does not infer scan 334.

## Final Part 003 English state

- `release-ready`: **111**
- `editorial-reviewed`: **0**
- `source-checked`: **0**
- `draft`: **0**
- `source-limited`: **0**
- `blocked`: **0**

Part 003 Tamil remains **ARCHIVAL-READY / CLOSED — 111 textual verified + 111 visual verified / 0 exceptions**.

## Release decision

**PART 003 ENGLISH RELEASE: APPROVED / CLOSED — 111/111 `release-ready`.**

This gate does not begin Part 004. The exact next activity is the **final Part 003 closure checkpoint/documentation confirmation**. Only after that checkpoint is closed may Part 004 source intake begin, and only when its controlling source is supplied.
''', encoding='utf-8')

# Root handover.
p = ROOT / 'HANDOVER.md'; t = p.read_text(encoding='utf-8')
t = regex_once(t, r'^Last refreshed for Kuraloviyam .*$', 'Last refreshed for Kuraloviyam **Part 003 Tamil ARCHIVAL-READY / CLOSED; English workflow RELEASE COMPLETE / CLOSED — 111/111 release-ready; final Part 003 closure checkpoint next**: **2026-09-10**.', 'root handover', re.M)
p.write_text(t, encoding='utf-8')

# Archival guidelines: Part003 live bullet + frontier tail.
p = ROOT / 'KURALOVIYAM_ARCHIVAL_GUIDELINES.md'; t = p.read_text(encoding='utf-8')
t = replace_once(t, '- English editorial review: **COMPLETE / CLOSED — 111/111**; current page state **111 editorial-reviewed + 0 source-checked**; Part review / release are not started.', '- English editorial review: **COMPLETE / CLOSED — 111/111**; Part-level English review: **PASS / CLOSED**; English release: **APPROVED / CLOSED — 111/111 release-ready**; final Part 003 closure checkpoint next.', 'guidelines Part003 English state')
p.write_text(t, encoding='utf-8')
replace_tail(p, r'^### Exact next content stage$', '''### Exact next content stage

Perform the **final Part 003 closure checkpoint/documentation confirmation**. Confirm Tamil remains ARCHIVAL-READY / CLOSED, the maintained English workflow is RELEASE COMPLETE / CLOSED at **111/111 `release-ready`**, the Part-level review and release report both pass, live controls agree, and there are no residual temporary execution files or open Part-003 gates.

Do not begin Part 004 inside this checkpoint. External **333→334** remains deferred until Part 004 source intake. After the final Part 003 checkpoint closes, Part 004 may begin only when its controlling source is supplied.''')

# Work README.
p = ROOT / 'works/kuraloviyam/README.md'; t = p.read_text(encoding='utf-8')
t = regex_once(t, r'^\| 003 \| 223–333 \|.*$', '| 003 | 223–333 | **Tamil ARCHIVAL-READY / CLOSED; English RELEASE COMPLETE / CLOSED — 111/111 release-ready; final Part 003 closure checkpoint next** |', 'work README row', re.M)
t = regex_once(t, r'^## Part 003 —.*$', '## Part 003 — TAMIL ARCHIVAL-READY / CLOSED; ENGLISH RELEASE COMPLETE / CLOSED — 111/111', 'work README heading', re.M)
p.write_text(t, encoding='utf-8')
replace_tail(p, r'^## Current durable state$', '''## Current durable state

- Part 003 Tamil: **ARCHIVAL-READY / CLOSED — 111 textual verified + 111 visual verified / 0 exceptions**;
- Part 003 English drafting: **111/111 COMPLETE / CLOSED**;
- source-check: **111/111 COMPLETE / CLOSED**;
- glossary reconciliation: **111/111 COMPLETE / CLOSED**;
- editorial review: **111/111 COMPLETE / CLOSED**;
- Part-level English review: **PASS / CLOSED**;
- release report: **APPROVED / CLOSED**;
- current English state: **111 `release-ready` / 0 editorial-reviewed / 0 source-checked / 0 draft / 0 source-limited / 0 blocked**.

## Current frontier

**Next activity: final Part 003 closure checkpoint/documentation confirmation.** Confirm every Part-003 Tamil and English gate is durably closed, the release report is present, all 111 English pages are release-ready, controls are synchronized, and temporary execution files are absent.

External **333→334** remains deferred until Part 004 source intake. Do not begin Part 004 until this final checkpoint closes and the Part 004 source is supplied.''')

# Page map.
p = ROOT / 'works/kuraloviyam/indexes/page-map.md'; t = p.read_text(encoding='utf-8')
t = regex_once(t, r'^\| 003 \| 223–333 \| 1–111 \|.*$', '| 003 | 223–333 | 1–111 | scan 223 / printed 206 through scan 333 / printed 316 | **Tamil ARCHIVAL-READY / CLOSED; English RELEASE COMPLETE / CLOSED — 111/111 release-ready; final Part 003 closure checkpoint next** |', 'page map row', re.M)
p.write_text(t, encoding='utf-8')

# Source metadata.
p = ROOT / 'works/kuraloviyam/metadata/source.md'; t = p.read_text(encoding='utf-8')
t = regex_once(t, r'^\| 003 \| 223–333 \| 111 \| `TVA_BOK_0065733_குறளோவியம்_part_003_pages_223-333\.pdf` \|.*$', '| 003 | 223–333 | 111 | `TVA_BOK_0065733_குறளோவியம்_part_003_pages_223-333.pdf` | **supplied; Tamil ARCHIVAL-READY / CLOSED; English RELEASE COMPLETE / CLOSED — 111/111 release-ready; final Part 003 closure checkpoint next** |', 'source row', re.M)
old = 'The maintained English layer has completed first-pass drafting **111/111**, source-check **111/111**, glossary reconciliation **111/111**, editorial review **111/111 COMPLETE / CLOSED**, and Part-level English review **PASS / CLOSED**. The exact next gate is the **Part 003 English release report**.'
new = 'The maintained English layer has completed first-pass drafting **111/111**, source-check **111/111**, glossary reconciliation **111/111**, editorial review **111/111 COMPLETE / CLOSED**, Part-level English review **PASS / CLOSED**, and English release **APPROVED / CLOSED — 111/111 release-ready**. The exact next gate is the **final Part 003 closure checkpoint/documentation confirmation**.'
t = replace_once(t, old, new, 'source progress')
p.write_text(t, encoding='utf-8')

# Work handover: replace frontier tail.
p = ROOT / 'works/kuraloviyam/HANDOVER.md'; t = p.read_text(encoding='utf-8')
t = replace_once(t, '- current English state: **111 `editorial-reviewed` + 0 `source-checked` / 0 `draft` / 0 source-limited / 0 blocked**;', '- current English state: **111 `release-ready` / 0 `editorial-reviewed` / 0 `source-checked` / 0 `draft` / 0 source-limited / 0 blocked**;', 'work handover state')
t = replace_once(t, '- Part review / release: **not-started**.', '- Part-level review: **PASS / CLOSED**; release report: **APPROVED / CLOSED**; release-ready: **111/111**.', 'work handover gates')
p.write_text(t, encoding='utf-8')
replace_tail(p, r'^## Exact next activity — Part 003 whole-Part English review$', '''## Part 003 Part-level English review — PASS / CLOSED

Durable record: `works/kuraloviyam/translations/en/reviews/PART_003_ENGLISH_REVIEW.md`.

Whole-Part inventory/alignment, statuses, controlled terminology/names, Chapter/Kural metadata, Kural-block separation, visual/non-body functions and accumulated continuities all passed. The review changed no page wording, page status or Tamil record.

## Part 003 English release — APPROVED / CLOSED

Durable report: `works/kuraloviyam/translations/en/reviews/PART_003_ENGLISH_RELEASE_REPORT.md`.

All **111** eligible English pages were promoted from `editorial-reviewed` to `release-ready` with status-token-only changes. Approved body wording changed on **0** pages; Tamil changes: **0**.

## Exact next activity — final Part 003 closure checkpoint

Confirm the full Part 003 workflow is durably closed: Tamil archival-ready, English drafting/source-check/glossary/editorial review complete, Part-level review PASS, release APPROVED, exactly **111 `release-ready`** English pages, synchronized controls, and no temporary execution files.

Do not begin Part 004 during this checkpoint. External **333→334** remains deferred until Part 004 source intake. After closure, Part 004 may begin only when its controlling source is supplied.''')

# English README frontier.
p = ROOT / 'works/kuraloviyam/translations/en/README.md'; t = p.read_text(encoding='utf-8')
t = replace_once(t, '- current English state: **111 `editorial-reviewed` + 0 `source-checked` / 0 `draft` / 0 source-limited / 0 blocked**;', '- current English state: **111 `release-ready` / 0 `editorial-reviewed` / 0 `source-checked` / 0 `draft` / 0 source-limited / 0 blocked**;', 'English README state')
t = replace_once(t, '- Part review / release: **not-started**.', '- Part-level review: **PASS / CLOSED**; release report: **APPROVED / CLOSED**; release-ready: **111/111 COMPLETE / CLOSED**.', 'English README gates')
p.write_text(t, encoding='utf-8')
replace_tail(p, r'^## Current frontier$', '''## Part 003 Part-level English review — PASS / CLOSED

Durable record: `reviews/PART_003_ENGLISH_REVIEW.md`.

## Part 003 English release — APPROVED / CLOSED

Durable release report: `reviews/PART_003_ENGLISH_RELEASE_REPORT.md`.

All **111/111** eligible Part-003 English pages are now `release-ready`. The release changed only the page status token; approved wording and all Tamil records remain unchanged.

## Current frontier

Exact next activity: **final Part 003 closure checkpoint/documentation confirmation**. Verify all gates and controls agree on the closed state and no temporary execution files remain. Do not begin Part 004 in this gate; external **333→334** remains deferred until Part 004 intake.''')

# Translation status frontier.
p = ROOT / 'works/kuraloviyam/translations/en/TRANSLATION_STATUS.md'; t = p.read_text(encoding='utf-8')
replace_tail(p, r'^## Current frontier — Part 003 English release report$', f'''## Part 003 English release — APPROVED / CLOSED

Durable report: `works/kuraloviyam/translations/en/reviews/PART_003_ENGLISH_RELEASE_REPORT.md`.

Release base / clean prior-gate HEAD: `{BASE}`.

Final result:

- eligible pages: **111/111**;
- `release-ready`: **111/111**;
- `editorial-reviewed`: **0**;
- `source-checked`: **0**;
- `draft`: **0**;
- `source-limited`: **0**;
- `blocked`: **0**;
- body-text changes during release: **0**;
- Tamil page changes during release: **0**.

All 111 page-layer modifications are status-token-only promotions from `editorial-reviewed` to `release-ready`. The Part 003 internal ending at scan 333 remains closed; external **333→334** remains deferred until Part 004 source intake.

## Current frontier — final Part 003 closure checkpoint

Confirm all Tamil and maintained-English gates are closed, the review and release reports are present, all 111 English pages are release-ready, live documentation is synchronized, and no temporary execution files remain. Do not begin Part 004 inside this checkpoint.''')

# Next-chat prompt: replace final exact-activity tail and normalize durable state.
p = ROOT / 'NEXT_CHAT_PROMPT_KURALOVIYAM.md'; t = p.read_text(encoding='utf-8')
t = replace_once(t, '- current Part-003 English state: **111 `editorial-reviewed` + 0 `source-checked` / 0 `draft` / 0 source-limited / 0 blocked**.', '- current Part-003 English state: **111 `release-ready` / 0 `editorial-reviewed` / 0 `source-checked` / 0 `draft` / 0 source-limited / 0 blocked**.', 'next prompt state')
t = replace_once(t, '- editorial review: **111/111 COMPLETE / CLOSED**; Part review / release: **not-started**.', '- editorial review: **111/111 COMPLETE / CLOSED**; Part-level review: **PASS / CLOSED**; English release: **APPROVED / CLOSED — 111/111 release-ready**.', 'next prompt gate summary')
p.write_text(t, encoding='utf-8')
replace_tail(p, r'^## Exact next activity — Part 003 whole-Part English review$', '''## Part 003 Part-level review and release — CLOSED

- Part-level review: **PASS / CLOSED**; durable record `works/kuraloviyam/translations/en/reviews/PART_003_ENGLISH_REVIEW.md`.
- release report: **APPROVED / CLOSED**; durable record `works/kuraloviyam/translations/en/reviews/PART_003_ENGLISH_RELEASE_REPORT.md`.
- final English state: **111/111 `release-ready`**; release body-text changes **0**; Tamil changes **0**.

## Exact next activity — final Part 003 closure checkpoint

1. fetch live `main` first and preserve newer durable work;
2. confirm Part 003 Tamil remains ARCHIVAL-READY / CLOSED at 111 textual + 111 visual verified / 0 exceptions;
3. confirm English drafting, source-check, glossary reconciliation and editorial review are each 111/111 COMPLETE / CLOSED;
4. confirm `PART_003_ENGLISH_REVIEW.md` is PASS and `PART_003_ENGLISH_RELEASE_REPORT.md` is APPROVED / CLOSED;
5. confirm exactly 111 English pages are `release-ready`, with zero pages in every earlier status;
6. confirm all live controls agree and temporary execution files are absent;
7. record the final Part 003 closure checkpoint without changing Tamil or approved English wording;
8. do not begin Part 004 in the same gate; external **333→334** remains deferred until Part 004 source intake.

After the checkpoint closes, Part 004 may begin only when its controlling source is supplied/onboarded.''')

# Validate exact durable change-set: 111 pages + 9 controls + report = 121.
expected = set(page_paths) | {
    'HANDOVER.md', 'KURALOVIYAM_ARCHIVAL_GUIDELINES.md', 'NEXT_CHAT_PROMPT_KURALOVIYAM.md',
    'works/kuraloviyam/HANDOVER.md', 'works/kuraloviyam/README.md',
    'works/kuraloviyam/indexes/page-map.md', 'works/kuraloviyam/metadata/source.md',
    'works/kuraloviyam/translations/en/README.md',
    'works/kuraloviyam/translations/en/TRANSLATION_STATUS.md',
    str(REPORT),
}
actual = set(subprocess.check_output(['git','diff','--name-only'], text=True).splitlines())
actual |= set(subprocess.check_output(['git','ls-files','--others','--exclude-standard'], text=True).splitlines())
actual = {x for x in actual if not x.startswith('.github/')}
if actual != expected:
    raise RuntimeError(f'changed-file gate failed missing={sorted(expected-actual)} extra={sorted(actual-expected)}')
if any(x.startswith('works/kuraloviyam/pages/') for x in actual):
    raise RuntimeError('Tamil page changed')
for path in [Path(x) for x in page_paths]:
    new = path.read_text(encoding='utf-8')
    old = originals[path]
    if new.replace('status: "release-ready"','status: "editorial-reviewed"',1) != old:
        raise RuntimeError(f'non-status page change: {path}')

print(f'PART003_RELEASE_PASS pages={len(page_paths)} release_ready=111 body_changes=0 tamil_changes=0 durable_changed={len(actual)}')
