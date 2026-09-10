from pathlib import Path
import re, subprocess

ROOT = Path('.')
BASE = 'da1b878a81af513ecb73d9c6843ab49dde2a2190'
RELEASE_COMMIT = '5b1969b1498ae5a8f4d44b45a696017b10e12f10'
PAGES = ROOT / 'works/kuraloviyam/translations/en/pages'
CLOSURE = ROOT / 'works/kuraloviyam/PART_003_FINAL_CLOSURE.md'


def read(path):
    return Path(path).read_text(encoding='utf-8')


def write(path, text):
    Path(path).write_text(text, encoding='utf-8')


def regex_once(text, pattern, repl, label, flags=0):
    out, n = re.subn(pattern, repl, text, count=1, flags=flags)
    if n != 1:
        raise RuntimeError(f'{label}: expected 1 match, found {n}')
    return out


def replace_once(text, old, new, label):
    n = text.count(old)
    if n != 1:
        raise RuntimeError(f'{label}: expected 1 match, found {n}')
    return text.replace(old, new, 1)


def replace_tail(path, marker_pattern, new_tail, label):
    text = read(path)
    m = re.search(marker_pattern, text, flags=re.M)
    if not m:
        raise RuntimeError(f'{label}: marker not found')
    write(path, text[:m.start()] + new_tail.rstrip() + '\n')

# ---- Gate verification ----------------------------------------------------

tamil = read('works/kuraloviyam/PART_003_TAMIL_ARCHIVAL_READY.md')
for token in [
    '**PART 003 TAMIL ARCHIVAL-READY — PASS / CLOSED.**',
    '**111/111 verified Tamil page records**',
    '**111/111 verified visual-fidelity records**',
    'external **333→334** remaining intentionally deferred until Part 004 source intake',
]:
    if token not in tamil:
        raise RuntimeError(f'Tamil closure token missing: {token}')

review = read('works/kuraloviyam/translations/en/reviews/PART_003_ENGLISH_REVIEW.md')
for token in ['**PASS**', 'PART 003 PART-LEVEL ENGLISH REVIEW: PASS', 'release-ready` remains **0/111**']:
    if token not in review:
        raise RuntimeError(f'Part-review token missing: {token}')

release = read('works/kuraloviyam/translations/en/reviews/PART_003_ENGLISH_RELEASE_REPORT.md')
for token in ['**APPROVED FOR RELEASE**', 'PART 003 ENGLISH RELEASE: APPROVED / CLOSED — 111/111 `release-ready`', 'body-text changes in this release gate: **0**', 'Tamil page changes: **0**']:
    if token not in release:
        raise RuntimeError(f'Release token missing: {token}')

# Release must be the only page-layer change since the clean pre-release base.
# The cleanup commits after RELEASE_COMMIT must not have changed any page file.
post_release_page_diff = subprocess.check_output(
    ['git', 'diff', '--name-only', RELEASE_COMMIT, '--', 'works/kuraloviyam/translations/en/pages'],
    text=True,
).strip()
if post_release_page_diff:
    raise RuntimeError(f'English page drift after release commit: {post_release_page_diff}')

count = 0
for scan in range(223, 334):
    printed = scan - 17
    p = PAGES / f'{scan:04d}-kuraloviyam-{printed}.md'
    if not p.exists():
        raise RuntimeError(f'missing Part 003 English page: {p}')
    t = read(p)
    required = [
        f'source_scan_page: {scan}',
        f'printed_page: "{printed}"',
        'translation_type: "project_translation"',
        'source_tamil_status: "verified"',
        'status: "release-ready"',
    ]
    for token in required:
        if token not in t:
            raise RuntimeError(f'{p}: missing invariant {token}')
    for forbidden in ['status: "editorial-reviewed"', 'status: "source-checked"', 'status: "draft"', 'status: "source-limited"', 'status: "blocked"']:
        if forbidden in t:
            raise RuntimeError(f'{p}: stale English status {forbidden}')
    count += 1
if count != 111:
    raise RuntimeError(f'expected 111 Part 003 English pages, got {count}')

# No Part 004 page records or source-intake record may already exist.
for pattern in [
    'works/kuraloviyam/pages/0334-kuraloviyam-*',
    'works/kuraloviyam/translations/en/pages/0334-kuraloviyam-*',
    'works/kuraloviyam/SOURCE_INTAKE_PART_004.md',
]:
    if list(ROOT.glob(pattern)):
        raise RuntimeError(f'Part 004 appears to have started unexpectedly: {pattern}')

# Release/part-review temporary execution files must already be gone.
for temp in [
    '.github/scripts/kuraloviyam-part003-release.py',
    '.github/scripts/kuraloviyam-part003-release-runner.py',
    '.github/workflows/kuraloviyam-part003-release.yml',
    '.github/scripts/kuraloviyam-part003-part-review.py',
    '.github/scripts/kuraloviyam-part003-part-review-runner.py',
    '.github/workflows/kuraloviyam-part003-part-review.yml',
]:
    if Path(temp).exists():
        raise RuntimeError(f'stale temporary execution file remains: {temp}')

# ---- Durable final closure record ----------------------------------------
CLOSURE.write_text(f'''# Part 003 Final Closure — Kuraloviyam

## Declaration

**PART 003 FINAL CHECKPOINT — PASS / CLOSED.**

This checkpoint closes the complete maintained Part 003 workflow for `குறளோவியம்`, overall scans **223–333 / printed 206–316**.

Clean pre-checkpoint HEAD: `{BASE}`.

## Tamil archival layer — CLOSED

Durable Tamil checkpoint: `works/kuraloviyam/PART_003_TAMIL_ARCHIVAL_READY.md`.

- Tamil textual status: **111/111 verified**;
- visual fidelity: **111/111 verified**;
- partial / source-limited / needs-review / unresolved exceptions: **0**;
- Tamil body or metadata changes during final Part closure: **0**.

## Maintained English layer — RELEASE COMPLETE / CLOSED

Durable Part-level review: `works/kuraloviyam/translations/en/reviews/PART_003_ENGLISH_REVIEW.md` — **PASS / CLOSED**.

Durable release report: `works/kuraloviyam/translations/en/reviews/PART_003_ENGLISH_RELEASE_REPORT.md` — **APPROVED / CLOSED**.

Final English state:

- `release-ready`: **111/111**;
- `editorial-reviewed`: **0**;
- `source-checked`: **0**;
- `draft`: **0**;
- `source-limited`: **0**;
- `blocked`: **0**.

The release promotion was status-token-only. Approved English body wording changed on **0** pages during release, and this final closure checkpoint changes **0** English page records.

## Closed English evidence chain

- first-pass drafting: **111/111 COMPLETE / CLOSED**;
- source-check: **111/111 COMPLETE / CLOSED**;
- glossary reconciliation: **111/111 COMPLETE / CLOSED**;
- editorial review: **111/111 COMPLETE / CLOSED**;
- Part-level review: **PASS / CLOSED**;
- release report: **APPROVED / CLOSED**;
- release-ready synchronization: **111/111 COMPLETE / CLOSED**.

## Structural boundary state

The Part 003 internal ending at scan **333 / printed 316** is closed. The known final **332→333** continuation remains preserved.

The external **333→334** boundary is **not** resolved by this checkpoint. It remains deferred until the actual Part 004 controlling source is supplied and onboarded. No scan-334 text, filename, printed-page mapping, continuation, or source identity is inferred here.

## Repository hygiene — PASS

The final checkpoint confirms:

- no Part 003 release or Part-review temporary workflow/script remains;
- no Part 004 page record or source-intake record has been started;
- no Part 003 Tamil or English page record is modified by this checkpoint;
- live control documents are synchronized to the closed Part 003 state.

## Final decision

**PART 003 — TAMIL + MAINTAINED ENGLISH: CLOSED.**

The exact next content activity is **Part 004 source intake, only when the Part 004 controlling source is supplied**. At that intake, fetch live `main`, establish exact source identity, continue overall scan numbering at **334**, and resolve the deferred **333→334** boundary from the actual adjacent source before transcription.
''', encoding='utf-8')

# ---- Control synchronization ---------------------------------------------

# Root HANDOVER.
p = ROOT / 'HANDOVER.md'
t = read(p)
t = regex_once(
    t,
    r'^Last refreshed for Kuraloviyam .*$',
    'Last refreshed for Kuraloviyam **Part 003 TAMIL + ENGLISH CLOSED — final checkpoint PASS / CLOSED; Part 004 source intake next when supplied**: **2026-09-10**.',
    'root handover first line',
    re.M,
)
write(p, t)

# Archival guidelines: current Part 003 state and frontier.
p = ROOT / 'KURALOVIYAM_ARCHIVAL_GUIDELINES.md'
t = read(p)
t = regex_once(
    t,
    r'- English editorial review: \*\*COMPLETE / CLOSED — 111/111\*\*; Part-level English review: \*\*PASS / CLOSED\*\*; English release: \*\*APPROVED / CLOSED — 111/111 release-ready\*\*; final Part 003 closure checkpoint next\.',
    '- English editorial review: **COMPLETE / CLOSED — 111/111**; Part-level English review: **PASS / CLOSED**; English release: **APPROVED / CLOSED — 111/111 release-ready**; final Part checkpoint: **PASS / CLOSED**.',
    'guidelines Part003 state',
)
write(p, t)
replace_tail(p, r'^### Exact next content stage$', '''### Exact next content stage

**Part 003 is fully CLOSED — Tamil + maintained English.** Durable final checkpoint: `works/kuraloviyam/PART_003_FINAL_CLOSURE.md`.

The next content stage is **Part 004 source intake, only when its controlling source is supplied/onboarded**. At intake, establish the exact Part 004 source identity and local page count, continue repository `scan_page` at overall scan **334**, and resolve the deferred **333→334** split boundary from the actual adjacent source before transcription.

Do not infer Part 004 filename, printed-page boundary, body text, illustration state or continuity before that source is supplied.''', 'guidelines frontier')

# Work README.
p = ROOT / 'works/kuraloviyam/README.md'
t = read(p)
t = regex_once(t, r'^\| 003 \| 223–333 \|.*$', '| 003 | 223–333 | **Tamil + English CLOSED — final Part checkpoint PASS / CLOSED; 111/111 English release-ready** |', 'README Part003 row', re.M)
t = regex_once(t, r'^## Part 003 —.*$', '## Part 003 — TAMIL + ENGLISH CLOSED', 'README Part003 heading', re.M)
write(p, t)
replace_tail(p, r'^## Current durable state$', '''## Current durable state

Part 003 final closure record: `PART_003_FINAL_CLOSURE.md` — **PASS / CLOSED**.

- Tamil: **ARCHIVAL-READY / CLOSED — 111 textual verified + 111 visual verified / 0 exceptions**;
- English drafting: **111/111 COMPLETE / CLOSED**;
- source-check: **111/111 COMPLETE / CLOSED**;
- glossary reconciliation: **111/111 COMPLETE / CLOSED**;
- editorial review: **111/111 COMPLETE / CLOSED**;
- Part-level English review: **PASS / CLOSED**;
- English release: **APPROVED / CLOSED — 111/111 release-ready**;
- final Part checkpoint: **PASS / CLOSED**.

## Current frontier

**Next activity: Part 004 source intake when the controlling source is supplied.** Do not infer the Part 004 filename or content beforehand. At intake, continue overall scan numbering at **334** and resolve the deferred **333→334** boundary against the actual adjacent source.''', 'README frontier')

# Work HANDOVER.
p = ROOT / 'works/kuraloviyam/HANDOVER.md'
t = read(p)
t = t.replace('- current English state: **111 `release-ready` / 0 `editorial-reviewed` / 0 `source-checked` / 0 `draft` / 0 source-limited / 0 blocked**;', '- current English state: **111 `release-ready` / 0 `editorial-reviewed` / 0 `source-checked` / 0 `draft` / 0 source-limited / 0 blocked**;', 1)
write(p, t)
replace_tail(p, r'^## Exact next activity — final Part 003 closure checkpoint$', '''## Part 003 final closure — PASS / CLOSED

Durable final checkpoint: `works/kuraloviyam/PART_003_FINAL_CLOSURE.md`.

Part 003 Tamil and maintained English are now fully closed. English is **111/111 `release-ready`**; the Part-level review is PASS; the release report is APPROVED / CLOSED; no Tamil or English page record changed during the final checkpoint.

## Exact next activity — Part 004 source intake

Part 004 is **not started**. Begin it only when the controlling Part 004 source is supplied/onboarded.

At intake:

1. fetch live `main` and preserve this Part 003 closure;
2. establish the exact supplied Part 004 filename, local page count, byte size and SHA-256;
3. map it to overall scans beginning at **334** without restarting `scan_page`;
4. compare the actual first Part 004 scan with closed scan 333 and resolve **333→334**;
5. only then begin Part 004 Tamil source intake / archival workflow;
6. do not reopen Parts 001–003 unless a genuinely new source/provenance/fidelity issue appears.''', 'work handover frontier')

# Page map.
p = ROOT / 'works/kuraloviyam/indexes/page-map.md'
t = read(p)
t = regex_once(t, r'^\| 003 \| 223–333 \| 1–111 \|.*$', '| 003 | 223–333 | 1–111 | scan 223 / printed 206 through scan 333 / printed 316 | **Tamil + English CLOSED — final checkpoint PASS / CLOSED; 111/111 English release-ready** |', 'page-map Part003 row', re.M)
write(p, t)

# Source metadata.
p = ROOT / 'works/kuraloviyam/metadata/source.md'
t = read(p)
t = regex_once(t, r'^\| 003 \| 223–333 \| 111 \| `TVA_BOK_0065733_குறளோவியம்_part_003_pages_223-333\.pdf` \|.*$', '| 003 | 223–333 | 111 | `TVA_BOK_0065733_குறளோவியம்_part_003_pages_223-333.pdf` | **supplied; Tamil + English CLOSED — final checkpoint PASS / CLOSED; 111/111 English release-ready** |', 'source Part003 row', re.M)
t = regex_once(
    t,
    r'The maintained English layer has completed first-pass drafting \*\*111/111\*\*, source-check \*\*111/111\*\*, glossary reconciliation \*\*111/111\*\*, editorial review \*\*111/111\*\*, Part-level English review \*\*PASS / CLOSED\*\*, and English release \*\*APPROVED / CLOSED — 111/111 release-ready\*\*\. The exact next gate is the \*\*final Part 003 closure checkpoint/documentation confirmation\*\*\. External \*\*333→334\*\* remains deferred until Part 004 source intake\.',
    'The maintained English layer has completed first-pass drafting **111/111**, source-check **111/111**, glossary reconciliation **111/111**, editorial review **111/111**, Part-level English review **PASS / CLOSED**, English release **APPROVED / CLOSED — 111/111 release-ready**, and final Part 003 closure **PASS / CLOSED**. Part 003 is fully closed. The next activity is **Part 004 source intake when its controlling source is supplied**. External **333→334** remains deferred until that intake.',
    'source progress paragraph',
)
write(p, t)

# English README.
p = ROOT / 'works/kuraloviyam/translations/en/README.md'
t = read(p)
replace_tail(p, r'^## Current frontier$', '''## Part 003 final closure — PASS / CLOSED

Durable final checkpoint: `../../PART_003_FINAL_CLOSURE.md`.

Part 003 maintained English is **RELEASE COMPLETE / CLOSED — 111/111 `release-ready`**. The final checkpoint changed no English page wording/status and no Tamil record.

## Current frontier

Part 004 English work is blocked until Part 004 completes its Tamil archival workflow. The immediate next activity for the work is **Part 004 source intake when the controlling source is supplied**. External **333→334** remains deferred until that intake.''', 'English README frontier')

# Translation status.
p = ROOT / 'works/kuraloviyam/translations/en/TRANSLATION_STATUS.md'
replace_tail(p, r'^## Current frontier — final Part 003 closure checkpoint$', '''## Part 003 final closure — PASS / CLOSED

Durable final checkpoint: `works/kuraloviyam/PART_003_FINAL_CLOSURE.md`.

Final Part 003 English state remains:

- `release-ready`: **111/111**;
- `editorial-reviewed`: **0**;
- `source-checked`: **0**;
- `draft`: **0**;
- `source-limited`: **0**;
- `blocked`: **0**.

No English page record or Tamil record changed during the final closure checkpoint. The Part-level review and release report remain **PASS / APPROVED / CLOSED**.

## Current frontier — Part 004 source intake

Part 004 has not started. Its English layer remains blocked until the Part 004 controlling source is supplied, source intake is completed, and the Tamil archival layer reaches its required checkpoint. External **333→334** remains deferred until the actual Part 004 intake.''', 'translation status frontier')

# Translation guide: add the closed Part 003 durable record.
p = ROOT / 'works/kuraloviyam/translations/en/TRANSLATION_GUIDE.md'
t = read(p)
if '## 15. Part 003 closed English record' in t:
    raise RuntimeError('Translation guide already contains Part 003 closed record')
t = t.rstrip() + '''\n\n## 15. Part 003 closed English record\n\nPart 003 covers scans **223–333 / printed 206–316**.\n\n- Tamil: **ARCHIVAL-READY / CLOSED — 111/111 textual + visual verified / 0 exceptions**;\n- first-pass drafting: **COMPLETE / CLOSED 111/111**;\n- source-check: **COMPLETE / CLOSED 111/111**;\n- glossary reconciliation: **COMPLETE / CLOSED 111/111**;\n- editorial review: **COMPLETE / CLOSED 111/111**;\n- Part-level review: **PASS / CLOSED**;\n- release report: **APPROVED / CLOSED**;\n- release-ready: **111/111 COMPLETE / CLOSED**;\n- final Part checkpoint: **PASS / CLOSED**.\n\nDurable records:\n\n- `reviews/PART_003_ENGLISH_REVIEW.md`;\n- `reviews/PART_003_ENGLISH_RELEASE_REPORT.md`;\n- `../../PART_003_FINAL_CLOSURE.md`.\n\nAll release page changes were status-token-only; approved English wording and Tamil archival records were unchanged. The internal Part ending at scan **333** is closed. External **333→334** remains deferred until Part 004 source intake.\n\nThe next content stage is **Part 004 source intake when the controlling source is supplied**, after which the same permanent Tamil→English gate order applies.\n'''
write(p, t)

# Next-chat prompt.
p = ROOT / 'NEXT_CHAT_PROMPT_KURALOVIYAM.md'
t = read(p)
t = replace_once(t, '- current Part-003 English state: **111 `release-ready` / 0 `editorial-reviewed` / 0 `source-checked` / 0 `draft` / 0 source-limited / 0 blocked**.', '- current Part-003 English state: **111 `release-ready` / 0 `editorial-reviewed` / 0 `source-checked` / 0 `draft` / 0 source-limited / 0 blocked**; final Part checkpoint **PASS / CLOSED**.', 'next prompt state')
write(p, t)
replace_tail(p, r'^## Exact next activity — final Part 003 closure checkpoint$', '''## Part 003 final closure — PASS / CLOSED

Durable record: `works/kuraloviyam/PART_003_FINAL_CLOSURE.md`.

Part 003 Tamil + maintained English are fully closed. English final state is **111/111 `release-ready`**. No Tamil or English page record changed during final closure.

## Exact next activity — Part 004 source intake, when supplied

Do **not** invent the Part 004 filename or begin source-dependent work until its controlling source is supplied/onboarded.

When it is supplied:

1. fetch live `main` first and preserve the Part 003 final closure;
2. establish exact filename, page count, byte size and SHA-256;
3. confirm repository scan numbering continues at overall scan **334**;
4. inspect the actual first Part 004 scan against closed scan 333 and resolve **333→334**;
5. then begin Part 004 Tamil source intake and continue the permanent archival workflow;
6. keep Parts 001–003 closed unless a genuinely new provenance/fidelity issue appears.''', 'next prompt frontier')

# Exact durable changed-file gate: final closure record + ten live controls.
expected = {
    'HANDOVER.md',
    'KURALOVIYAM_ARCHIVAL_GUIDELINES.md',
    'NEXT_CHAT_PROMPT_KURALOVIYAM.md',
    'works/kuraloviyam/HANDOVER.md',
    'works/kuraloviyam/README.md',
    'works/kuraloviyam/PART_003_FINAL_CLOSURE.md',
    'works/kuraloviyam/indexes/page-map.md',
    'works/kuraloviyam/metadata/source.md',
    'works/kuraloviyam/translations/en/README.md',
    'works/kuraloviyam/translations/en/TRANSLATION_GUIDE.md',
    'works/kuraloviyam/translations/en/TRANSLATION_STATUS.md',
}
actual = set(subprocess.check_output(['git', 'diff', '--name-only'], text=True).splitlines())
actual |= set(subprocess.check_output(['git', 'ls-files', '--others', '--exclude-standard'], text=True).splitlines())
actual = {x for x in actual if not x.startswith('.github/')}
if actual != expected:
    raise RuntimeError(f'closure changed-file gate failed; missing={sorted(expected-actual)}; extra={sorted(actual-expected)}')
if any(p.startswith('works/kuraloviyam/pages/') or p.startswith('works/kuraloviyam/translations/en/pages/') for p in actual):
    raise RuntimeError('final closure must not change Tamil or English page records')

print('PART003_FINAL_CLOSURE_PASS english_release_ready=111 tamil_verified=111 visual_verified=111 changed_files=11 part004_started=0')
