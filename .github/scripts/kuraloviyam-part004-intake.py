from pathlib import Path
import re

ROOT = Path('.')
BASE = 'c2c0485708740bf9adb6403eb67df13f37843b68'
SOURCE = 'TVA_BOK_0065733_குறளோவியம்_part_004_pages_334-444.pdf'
SIZE = 91513473
SHA256 = '5b7fcc65f19dc3d2a57bebb13cdfb02d0c83f70a5ccc9e537886790908674581'


def read(path):
    return Path(path).read_text(encoding='utf-8')


def write(path, text):
    Path(path).write_text(text, encoding='utf-8')


def replace_once(text, old, new, label):
    n = text.count(old)
    if n != 1:
        raise RuntimeError(f'{label}: expected exactly one match, found {n}')
    return text.replace(old, new, 1)


def replace_tail(path, marker_pattern, new_tail, label):
    text = read(path)
    m = re.search(marker_pattern, text, flags=re.M)
    if not m:
        raise RuntimeError(f'{label}: marker not found')
    write(path, text[:m.start()] + new_tail.rstrip() + '\n')

# Preconditions: Part 003 must be durably closed and Part 004 must not already have begun.
closure = read('works/kuraloviyam/PART_003_FINAL_CLOSURE.md')
for token in [
    '**PART 003 FINAL CHECKPOINT — PASS / CLOSED.**',
    '**PART 003 — TAMIL + MAINTAINED ENGLISH: CLOSED.**',
    '111/111',
]:
    if token not in closure:
        raise RuntimeError(f'Part 003 closure invariant missing: {token}')

if Path('works/kuraloviyam/SOURCE_INTAKE_PART_004.md').exists():
    raise RuntimeError('Part 004 source intake already exists')
if Path('works/kuraloviyam/PART_004_PASS1_PROGRESS.md').exists():
    raise RuntimeError('Part 004 Pass 1 progress already exists')
if list(Path('works/kuraloviyam/pages').glob('0334-kuraloviyam-*.md')):
    raise RuntimeError('Part 004 page records already exist unexpectedly')

# Durable source-intake record.
write('works/kuraloviyam/SOURCE_INTAKE_PART_004.md', f'''# Kuraloviyam — Source Intake — Part 004

Source: `{SOURCE}`

## Intake result

**PASS — Part 004 source unit resolved for archival processing.**

- local PDF pages: **111**;
- canonical overall scans: **334–444**;
- visible printed-page span: **317–427**;
- complete-source extent reported by user: **666 scans**;
- split design: **6 parts × 111 pages**;
- file size: **{SIZE:,} bytes**;
- SHA-256: `{SHA256}`;
- source text layer: **no usable parsed text**;
- controlling representation for transcription: **rendered scan images**.

## Identity and physical continuity

- source family: `TVA_BOK_0065733`;
- work: `குறளோவியம்`;
- author: `கலைஞர் மு. கருணாநிதி`;
- Part 004 local page 1 = overall scan **334** = printed page **317**;
- Part 004 local page 111 = overall scan **444** = printed page **427**;
- repository `scan_page` continues the overall 1–666 sequence and does not restart for this split.

## Resolved Part boundary — 333 → 334

The previously deferred split boundary is now source-resolved.

- closed Part 003 scan **333 / printed 316** closes the severe-rule / famine vignette with Chapter **57 — வெருவந்த செய்யாமை** / Kural **567**;
- Part 004 scan **334 / printed 317** begins a **new illustrated eye/blame lovers vignette**, opening `என் குற்றமல்ல மானே! என் குற்றமல்ல! என் கண்கள் செய்த குற்றம்!`;
- scan **335 / printed 318** continues and closes that new unit with Chapter **118 — கண்விதுப்பழிதல்** / Kural **1174**;
- therefore **333→334 is a CLEAN vignette boundary**, not a sentence or narrative continuation.

No text is reconstructed across the split.

## Part 004 ending observed at intake

- local page **110 / overall scan 443 / printed 426** closes the preceding Nallaan/Nagan `தீ நட்பு` unit with Chapter **82** / Kural **812**;
- local page **111 / overall scan 444 / printed 427** begins a new illustrated royal/court narrative and visibly ends within that narrative, with the final printed phrase `அத்துடன் நிறுத்தவில்லை`;
- the external **444→445** boundary remains **deferred** until the actual Part 005 source is supplied. No scan-445 wording, mapping or continuation text is inferred.

## Part 004 Pass 1 cadence

Continue the established Tamil capture cadence of **11 physical scans per normal Pass 1 iteration**, with a one-page final remainder:

- P4-01: scans **334–344 / printed 317–327**;
- P4-02: scans **345–355 / printed 328–338**;
- P4-03: scans **356–366 / printed 339–349**;
- P4-04: scans **367–377 / printed 350–360**;
- P4-05: scans **378–388 / printed 361–371**;
- P4-06: scans **389–399 / printed 372–382**;
- P4-07: scans **400–410 / printed 383–393**;
- P4-08: scans **411–421 / printed 394–404**;
- P4-09: scans **422–432 / printed 405–415**;
- P4-10: scans **433–443 / printed 416–426**;
- final remainder: scan **444 / printed 427**.

These are workflow boundaries only and must never create artificial textual boundaries. Inspect the first scan of the next batch only as a boundary witness when needed.

## Source-preservation decisions

1. The rendered scan is the lexical and structural authority.
2. Kural wording is copied only from this edition's visible scan; no canonical/web wording is substituted.
3. Illustrations, page furniture, stamps and other non-body marks remain separate from printed prose.
4. Pass 1 records begin `status: "needs-review"` / `visual_fidelity: "needs-review"`; source intake does not promote verification.
5. Parts 001–003 remain closed and are not reopened by Part 004 intake.
6. The outgoing **444→445** boundary remains deferred until Part 005 is actually supplied.

## Current gate

**Part 004 source intake: COMPLETE / PASS.**

Next: **P4-01 / Part 004 Pass 1 — scans 334–344 / printed 317–327**, using scan **345 / printed 328** only as a boundary witness when required.
''')

# Initialize Pass-1 progress before any page records are created.
write('works/kuraloviyam/PART_004_PASS1_PROGRESS.md', f'''# குறளோவியம் — Part 004 Pass 1 Progress

Controlling source: `{SOURCE}`

Overall scan range: **334–444**. Repository scan numbering never restarts per split.

Source intake: **PASS / COMPLETE** — 111 local pages, visible printed span **317–427**, {SIZE:,} bytes, SHA-256 `{SHA256}`; no usable parsed text layer.

Normal Part 004 Pass 1 iteration size: **11 physical scans**. Workflow boundaries do not create textual boundaries.

## Resolved incoming boundary

**333→334 is CLEAN.** Closed Part 003 scan 333 / printed 316 closes the severe-rule / famine vignette with Chapter 57 / Kural 567. Part 004 scan 334 / printed 317 starts a new illustrated eye/blame lovers vignette; scan 335 / printed 318 closes it with Chapter 118 — `கண்விதுப்பழிதல்` / Kural 1174.

## Pass 1 state

**0 / 111 page records captured.** Source intake alone does not create or verify Tamil page records.

Planned batches:

- P4-01: **334–344 / printed 317–327 — NEXT**;
- P4-02: **345–355 / printed 328–338**;
- P4-03: **356–366 / printed 339–349**;
- P4-04: **367–377 / printed 350–360**;
- P4-05: **378–388 / printed 361–371**;
- P4-06: **389–399 / printed 372–382**;
- P4-07: **400–410 / printed 383–393**;
- P4-08: **411–421 / printed 394–404**;
- P4-09: **422–432 / printed 405–415**;
- P4-10: **433–443 / printed 416–426**;
- final remainder: **444 / printed 427**.

At the supplied Part endpoint, scan 444 begins a new illustrated royal/court narrative and visibly remains open. **444→445 stays deferred until Part 005 source intake.**

## Exact next activity

Process **P4-01 — scans 334–344 / printed 317–327** as 11 page-aligned Tamil Pass-1 records. Inspect each rendered source page directly, preserve source wording/paragraphs/Kural blocks/visual relationships, use `needs-review` for both textual and visual status, and inspect scan 345 only if required to settle the outgoing batch boundary.
''')

# Root handover: refresh first line and replace the Kuraloviyam section with a compact current authority block.
p = Path('HANDOVER.md')
t = read(p)
t = re.sub(r'^Last refreshed for Kuraloviyam .*$', 'Last refreshed for Kuraloviyam **Part 004 SOURCE INTAKE PASS / COMPLETE — P4-01 scans 334–344 next**: **2026-09-10**.', t, count=1, flags=re.M)
m = re.search(r'^# Active source-ready work — குறளோவியம்$', t, flags=re.M)
if not m:
    raise RuntimeError('root Kuraloviyam section marker missing')
root_tail = f'''# Active source-ready work — குறளோவியம்

## LIVE MAIN IS AUTHORITATIVE

Fetch live `main` first. Parts **001–003 are CLOSED** and must not be reopened from stale prompts unless a genuinely new source/provenance/fidelity issue appears.

## Current Part 004 source

Controlling split: `{SOURCE}`

- source family: `TVA_BOK_0065733`;
- local pages: **111**;
- overall scans: **334–444**;
- visible printed pages: **317–427**;
- file size: **{SIZE:,} bytes**;
- SHA-256: `{SHA256}`;
- parsed text layer: **none usable**; rendered scans control transcription.

Part 004 source intake is **PASS / COMPLETE**. Durable records:

- `works/kuraloviyam/SOURCE_INTAKE_PART_004.md`;
- `works/kuraloviyam/PART_004_PASS1_PROGRESS.md`.

The previously deferred **333→334** boundary is now **CLEAN / source-resolved**: scan 333 closes the Part-003 Chapter 57 / Kural 567 vignette; scan 334 begins a new illustrated lovers/eye-blame vignette, which closes on scan 335 with Chapter 118 / Kural 1174.

External **444→445 remains deferred** until Part 005 is supplied.

## Exact next activity — குறளோவியம்

Process **Part 004 Pass 1 P4-01 — scans 334–344 / printed 317–327, 11 physical scans**. Use the supplied Part 004 PDF as controlling source, create one Tamil page record per physical scan with `status: "needs-review"` and `visual_fidelity: "needs-review"`, preserve source-visible Kural/page structure and illustrations, and inspect scan 345 only as a boundary witness if needed.
'''
write(p, t[:m.start()] + root_tail)

# Work-specific guidelines.
p = Path('KURALOVIYAM_ARCHIVAL_GUIDELINES.md')
t = read(p)
t = replace_once(t, 'Parts 001–003 expose no usable parsed text layer in the supplied file environment.', 'Parts 001–004 expose no usable parsed text layer in the supplied file environment.', 'guidelines text-layer extent')
t = replace_once(t, '**Current user directive for Part 003 Pass 1 and Pass 2A page-batched work: 11 physical scans per normal iteration**, with a shorter final remainder when necessary.', '**Current established Tamil cadence for Part 004 Pass 1 and Pass 2A page-batched work: 11 physical scans per normal iteration**, with a shorter final remainder when necessary.', 'guidelines cadence')
# Historical Part003 section can now record the resolved adjacent boundary.
t = replace_once(t, 'incoming **222→223: CLEAN**; internal **332→333** genuine continuation closes within the Part; external **333→334** remains deferred until Part 004 intake;', 'incoming **222→223: CLEAN**; internal **332→333** genuine continuation closes within the Part; adjacent **333→334: CLEAN / source-resolved at Part 004 intake**;', 'guidelines Part003 boundary')
write(p, t)
replace_tail(p, r'^### Exact next content stage$', f'''### Part 004 — overall scans 334–444

Controlling source: `{SOURCE}`.

- source intake: **PASS / COMPLETE**;
- local pages: **111**; visible printed span: **317–427**;
- SHA-256: `{SHA256}`;
- no usable parsed text layer; rendered scans control;
- incoming **333→334: CLEAN / source-resolved**;
- Tamil Pass 1: **0/111 — not started**;
- outgoing **444→445: deferred until Part 005 intake**.

### Exact next content stage

Perform **Part 004 Pass 1 P4-01 — scans 334–344 / printed 317–327, 11 scans**. Page records remain `needs-review` / `visual_fidelity: needs-review` after Pass 1. Do not begin Part 005 or resolve **444→445** without its actual controlling source.''', 'guidelines current frontier')

# Work README.
p = Path('works/kuraloviyam/README.md')
t = read(p)
t = replace_once(t, '| 004 | 334–444 | not-started |', '| 004 | 334–444 | **source intake PASS / COMPLETE; Pass 1 next — P4-01 scans 334–344** |', 'README table Part004')
# Part003 adjacent boundary is now known.
t = replace_once(t, 'The **222→223** boundary is resolved as **clean**. The external **333→334** boundary remains deferred until Part 004 is supplied.', 'The **222→223** boundary is resolved as **clean**. The adjacent **333→334** boundary is now also **CLEAN / source-resolved** from the supplied Part 004 source.', 'README Part003 boundary')
write(p, t)
replace_tail(p, r'^## Current durable state$', f'''## Part 004 — SOURCE INTAKE PASS / COMPLETE

Controlling source: `{SOURCE}`.

- local pages: **111**;
- overall scans: **334–444**;
- visible printed pages: **317–427**;
- file size: **{SIZE:,} bytes**;
- SHA-256: `{SHA256}`;
- parsed text: **none usable**;
- incoming **333→334: CLEAN / source-resolved**;
- Pass 1 page records: **0/111**;
- outgoing **444→445: deferred until Part 005 source intake**.

Durable intake: `SOURCE_INTAKE_PART_004.md`.  
Pass-1 tracker: `PART_004_PASS1_PROGRESS.md`.

## Current frontier

**Next activity: Part 004 Pass 1 P4-01 — scans 334–344 / printed 317–327, 11 physical scans.** Parts 001–003 remain closed. Do not infer or begin Part 005.''', 'README current state')

# Work handover: keep historical body, replace the current frontier tail and update startup list with Part004 controls.
p = Path('works/kuraloviyam/HANDOVER.md')
t = read(p)
t = replace_once(t, '15. `works/kuraloviyam/translations/en/reviews/PART_002_ENGLISH_RELEASE_REPORT.md`', '15. `works/kuraloviyam/PART_003_FINAL_CLOSURE.md`\n16. `works/kuraloviyam/SOURCE_INTAKE_PART_004.md`\n17. `works/kuraloviyam/PART_004_PASS1_PROGRESS.md`', 'handover startup current controls')
write(p, t)
replace_tail(p, r'^## Exact next activity — Part 004 source intake$', f'''## Part 004 source intake — PASS / COMPLETE

Controlling source: `{SOURCE}`.

- 111 local pages / overall scans **334–444** / visible printed **317–427**;
- {SIZE:,} bytes;
- SHA-256 `{SHA256}`;
- no usable parsed text layer;
- incoming **333→334 CLEAN / source-resolved**;
- Part 004 Pass 1: **0/111**;
- external **444→445 deferred** until Part 005 intake.

Durable intake: `works/kuraloviyam/SOURCE_INTAKE_PART_004.md`.  
Pass-1 tracker: `works/kuraloviyam/PART_004_PASS1_PROGRESS.md`.

## Exact next activity — Part 004 Pass 1 P4-01

Process **scans 334–344 / printed 317–327 — 11 page-aligned Tamil records**.

1. fetch live `main` and preserve Parts 001–003 closure plus this intake;
2. resolve the supplied Part 004 PDF and render scans directly;
3. create exactly one record for each scan 334–344 with correct `part: 4`, `part_page: 1–11`, printed page, source filename, `status: "needs-review"`, and `visual_fidelity: "needs-review"`;
4. preserve source wording, paragraph boundaries, Kural blocks, visual/page-furniture relationships and cross-page continuities;
5. inspect scan **345 / printed 328** only as a boundary witness if required;
6. update `PART_004_PASS1_PROGRESS.md` and live frontier controls, then audit the changed-file set;
7. do not start Pass 2A until all 111 Part-004 Pass-1 pages are captured; do not begin Part 005.''', 'handover frontier')

# Source metadata.
p = Path('works/kuraloviyam/metadata/source.md')
t = read(p)
t = replace_once(t, '| 004 | 334–444 | 111 | not yet supplied / exact filename not yet established | not-started |', f'| 004 | 334–444 | 111 | `{SOURCE}` | **supplied; source intake PASS / COMPLETE; Pass 1 next** |', 'source table Part004')
t = replace_once(t, 'Part 003 is fully closed. The next activity is **Part 004 source intake when its controlling source is supplied**. External **333→334** remains deferred until that intake.', 'Part 003 is fully closed. Part 004 is now supplied and its source intake is **PASS / COMPLETE**; **333→334 is CLEAN / source-resolved**. The next activity is **Part 004 Pass 1 P4-01 — scans 334–344 / printed 317–327**.', 'source Part003 next state')
part4_section = f'''## Part 004 source identity and provenance

Controlling split:

`{SOURCE}`

- local page count: **111**;
- overall scans: **334–444**;
- visible printed span: **317–427**;
- file size: **{SIZE:,} bytes**;
- SHA-256: `{SHA256}`;
- no usable parsed text layer is exposed; rendered page images remain controlling;
- local page 1 / overall scan **334** carries printed page **317**;
- local page 111 / overall scan **444** carries printed page **427**.

The previously deferred **333→334** boundary is source-resolved as **CLEAN**: scan 333 closes the severe-rule/famine Chapter 57 / Kural 567 unit, while scan 334 begins a new illustrated eye/blame lovers vignette; scan 335 closes that new unit with Chapter 118 / Kural 1174.

At the outgoing edge, scan 444 begins a new illustrated royal/court narrative and ends within it. The exact **444→445** relationship remains deferred until Part 005 is supplied.

Detailed Part 004 intake record:

`works/kuraloviyam/SOURCE_INTAKE_PART_004.md`

Part 004 Pass 1 begins next at **P4-01 scans 334–344 / printed 317–327** under the 11-scan Tamil capture cadence.

'''
marker = '## Front-matter observations\n'
if marker not in t:
    raise RuntimeError('source metadata front-matter marker missing')
t = t.replace(marker, part4_section + marker, 1)
t = replace_once(t, 'Parts 002 and 003 continue the main `கலைஞரின் குறளோவியம்` illustrated/body sequence.', 'Parts 002–004 continue the main `கலைஞரின் குறளோவியம்` illustrated/body sequence.', 'source body sequence')
t = replace_once(t, 'The supplied Part 001, Part 002 and Part 003 splits expose **no usable parsed text layer** in the file environment.', 'The supplied Part 001, Part 002, Part 003 and Part 004 splits expose **no usable parsed text layer** in the file environment.', 'source text-layer extent')
write(p, t)

# Page map: update Part004 table and replace stale verification/frontier tail with current compact state.
p = Path('works/kuraloviyam/indexes/page-map.md')
t = read(p)
t = replace_once(t, '| 004 | 334–444 | 1–111 | not yet inspected | not-started |', '| 004 | 334–444 | 1–111 | scan 334 / printed 317 through scan 444 / printed 427 | **source intake PASS / COMPLETE; Pass 1 0/111; P4-01 next** |', 'page-map Part004 table')
write(p, t)
replace_tail(p, r'^## Verification gates$', f'''## Part 004 boundary resolution and intake map

Controlling source: `{SOURCE}`.

- local pages: **111**;
- overall scans: **334–444**;
- visible printed pages: **317–427**;
- file size: **{SIZE:,} bytes**;
- SHA-256: `{SHA256}`;
- source text layer: **no usable parsed text**;
- **333→334 CLEAN / source-resolved**;
- scan 334 begins a new illustrated eye/blame lovers vignette; scan 335 closes it with Chapter 118 / Kural 1174;
- scan 444 begins a new illustrated royal/court narrative and ends within it; **444→445 remains deferred** until Part 005 intake.

Durable intake: `../SOURCE_INTAKE_PART_004.md`.  
Pass-1 tracker: `../PART_004_PASS1_PROGRESS.md`.

## Verification gates

Part 001: **Tamil + English CLOSED**.

Part 002: **Tamil + English CLOSED; final checkpoint PASS / CLOSED**.

Part 003: **Tamil + English CLOSED; final checkpoint PASS / CLOSED; 111/111 English release-ready**.

Part 004:

- source intake — **PASS / COMPLETE**;
- Pass 1 — **0/111, P4-01 next**;
- Pass 2A / Pass 2B / Pass 3 / audit / final sync / Tamil archival-ready / English / final Part closure — **not started**.

## Current frontier

**Part 004 Pass 1 P4-01 — scans 334–344 / printed 317–327, 11 scans.** Incoming **333→334 is CLEAN**. External **444→445 remains deferred** until Part 005 source intake.''', 'page-map verification tail')

# English README: Part004 English remains blocked, but intake/boundary are now known.
p = Path('works/kuraloviyam/translations/en/README.md')
replace_tail(p, r'^## Current frontier$', '''## Current frontier

Part 004 source intake is **PASS / COMPLETE**, and the incoming **333→334** boundary is now **CLEAN / source-resolved**. Part 004 English work remains blocked until the Part 004 Tamil archival workflow reaches ARCHIVAL-READY / CLOSED.

Immediate work-level next activity: **Part 004 Tamil Pass 1 P4-01 — scans 334–344 / printed 317–327**. Do not begin Part 004 English drafting early.''', 'English README frontier')

# English status current frontier.
p = Path('works/kuraloviyam/translations/en/TRANSLATION_STATUS.md')
replace_tail(p, r'^## Current frontier — Part 004 source intake$', '''## Current frontier — Part 004 Tamil archival workflow

Part 004 source intake is **PASS / COMPLETE**. Incoming **333→334 is CLEAN / source-resolved**. Part 004 English work remains **blocked by workflow order** until Part 004 Tamil reaches ARCHIVAL-READY / CLOSED.

The immediate work-level next activity is **Part 004 Tamil Pass 1 P4-01 — scans 334–344 / printed 317–327**. External **444→445** remains deferred until Part 005 source intake.''', 'English status frontier')

# Next-chat prompt: replace fully with concise live Part004 prompt.
write('NEXT_CHAT_PROMPT_KURALOVIYAM.md', f'''# Next Chat Prompt — குறளோவியம் / Part 004 Pass 1 P4-01

Continue directly in `pugazg/kalaignar-literary-commentary`, branch `main`, active work `works/kuraloviyam/`.

## LIVE MAIN IS AUTHORITATIVE

Fetch live `main` first and preserve newer durable work. Parts **001–003 are fully CLOSED**. Do not reopen them unless a genuinely new source/provenance/fidelity issue appears.

## Controlling Part 004 source

`{SOURCE}`

Confirmed intake identity:

- local PDF pages: **111**;
- overall scans: **334–444**;
- visible printed pages: **317–427**;
- file size: **{SIZE:,} bytes**;
- SHA-256: `{SHA256}`;
- no usable parsed text layer; rendered source scans are controlling.

Source intake: **PASS / COMPLETE**. Durable record: `works/kuraloviyam/SOURCE_INTAKE_PART_004.md`.

Pass-1 tracker: `works/kuraloviyam/PART_004_PASS1_PROGRESS.md` — **0/111 captured**.

## Boundary state

- **333→334 CLEAN / source-resolved**: scan 333 closes Part 003 Chapter 57 / Kural 567; scan 334 starts a new illustrated eye/blame lovers vignette; scan 335 closes it with Chapter 118 / Kural 1174.
- external **444→445 deferred** until Part 005 source intake.

## Mandatory startup

Read before source-dependent work:

1. `LITERARY_COMMENTARY_PROCESSING_GUIDE.md`
2. `KURALOVIYAM_ARCHIVAL_GUIDELINES.md`
3. root `HANDOVER.md`
4. this prompt
5. `works/kuraloviyam/HANDOVER.md`
6. `works/kuraloviyam/README.md`
7. `works/kuraloviyam/metadata/source.md`
8. `works/kuraloviyam/metadata/transcription-policy.md`
9. `works/kuraloviyam/indexes/page-map.md`
10. `works/kuraloviyam/PART_003_FINAL_CLOSURE.md`
11. `works/kuraloviyam/SOURCE_INTAKE_PART_004.md`
12. `works/kuraloviyam/PART_004_PASS1_PROGRESS.md`

## Exact next activity — P4-01

Process **Part 004 Pass 1 scans 334–344 / printed 317–327 — 11 physical scans**.

For each scan:

- inspect the rendered scan directly;
- create exactly one page-aligned Tamil record under `works/kuraloviyam/pages/`;
- set `part: 4` and `part_page: 1–11` respectively;
- use source-visible printed page numbers, not inferred corrections;
- preserve printed wording, paragraph/dialogue structure, Kural blocks and visual relationships;
- keep running headers/footer/page numbers as page furniture rather than body prose;
- set `status: "needs-review"` and `visual_fidelity: "needs-review"` after Pass 1;
- never substitute standard/web/memorized Kural wording;
- inspect scan **345 / printed 328** only as a boundary witness if P4-01 ends mid-unit.

After the 11 pages, synchronize `PART_004_PASS1_PROGRESS.md` and current frontier controls, audit the exact changed-file set, and stop. Do not begin Pass 2A until all 111 Part-004 Pass-1 records exist. Do not begin Part 005.
''')

# Validate durable working tree shape: 2 new records + 9 synchronized controls = 11.
import subprocess
changed = subprocess.check_output(['git', 'status', '--short'], text=True).splitlines()
paths = [line[3:] for line in changed]
expected = {
    'HANDOVER.md',
    'KURALOVIYAM_ARCHIVAL_GUIDELINES.md',
    'NEXT_CHAT_PROMPT_KURALOVIYAM.md',
    'works/kuraloviyam/HANDOVER.md',
    'works/kuraloviyam/README.md',
    'works/kuraloviyam/SOURCE_INTAKE_PART_004.md',
    'works/kuraloviyam/PART_004_PASS1_PROGRESS.md',
    'works/kuraloviyam/indexes/page-map.md',
    'works/kuraloviyam/metadata/source.md',
    'works/kuraloviyam/translations/en/README.md',
    'works/kuraloviyam/translations/en/TRANSLATION_STATUS.md',
}
if set(paths) != expected:
    raise RuntimeError(f'unexpected durable change set: {paths}')
if any(p.startswith('works/kuraloviyam/pages/') for p in paths):
    raise RuntimeError('source intake must not create Tamil page records')
print('PART004_INTAKE_READY', len(paths))
