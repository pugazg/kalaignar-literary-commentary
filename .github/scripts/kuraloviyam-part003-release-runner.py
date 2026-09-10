from pathlib import Path

p = Path('.github/scripts/kuraloviyam-part003-release.py')
source = p.read_text(encoding='utf-8')
subs = [
    (
        "'- English editorial review: **COMPLETE / CLOSED — 111/111**; current page state **111 editorial-reviewed + 0 source-checked**; Part review / release are not started.'",
        "'- English editorial review: **COMPLETE / CLOSED — 111/111**; current page state **111 editorial-reviewed + 0 source-checked**; Part-level English review: **PASS / CLOSED**; release report: **next**.'"
    ),
    (
        "old = 'The maintained English layer has completed first-pass drafting **111/111**, source-check **111/111**, glossary reconciliation **111/111**, editorial review **111/111 COMPLETE / CLOSED**, and Part-level English review **PASS / CLOSED**. The exact next gate is the **Part 003 English release report**.'\nnew = 'The maintained English layer has completed first-pass drafting **111/111**, source-check **111/111**, glossary reconciliation **111/111**, editorial review **111/111 COMPLETE / CLOSED**, Part-level English review **PASS / CLOSED**, and English release **APPROVED / CLOSED — 111/111 release-ready**. The exact next gate is the **final Part 003 closure checkpoint/documentation confirmation**.'",
        "old = 'The maintained English layer has completed first-pass drafting **111/111**, source-check **111/111**, glossary reconciliation **111/111**, editorial review **111/111**, and the whole-Part English review is **PASS / CLOSED**. The exact next gate is the **Part 003 English release report**; pre-release state remains **111 editorial-reviewed / 0 release-ready**. External **333→334** remains deferred until Part 004 source intake.'\nnew = 'The maintained English layer has completed first-pass drafting **111/111**, source-check **111/111**, glossary reconciliation **111/111**, editorial review **111/111**, Part-level English review **PASS / CLOSED**, and English release **APPROVED / CLOSED — 111/111 release-ready**. The exact next gate is the **final Part 003 closure checkpoint/documentation confirmation**. External **333→334** remains deferred until Part 004 source intake.'"
    ),
    (
        "'- Part review / release: **not-started**.'",
        "'- Part-level English review: **PASS / CLOSED**; release report / release-ready: **not-started**.'"
    ),
    (
        "r'^## Exact next activity — Part 003 whole-Part English review$'",
        "r'^## Exact next activity — Part 003 English release report$'"
    ),
    (
        "'- Part-level review: **PASS / CLOSED**; release report / release-ready: **not-started**.'",
        "'- Part-level review: **PASS / CLOSED**; release report / release-ready: **not-started**.'"
    ),
    (
        "'- editorial review: **111/111 COMPLETE / CLOSED**; Part review / release: **not-started**.'",
        "'- editorial review: **111/111 COMPLETE / CLOSED**; Part-level English review: **PASS / CLOSED**; release report / release-ready: **not-started**.'"
    ),
]
for old, new in subs:
    if old == new:
        continue
    if old not in source:
        raise RuntimeError(f'compatibility patch target not found: {old[:120]}')
    source = source.replace(old, new, 1)

# There are two frontier-marker occurrences in the original script (work handover and next-chat prompt).
# Both must target the current release-report frontier.
source = source.replace("r'^## Exact next activity — Part 003 whole-Part English review$'", "r'^## Exact next activity — Part 003 English release report$'")

exec(compile(source, str(p), 'exec'), {'__name__': '__main__', '__file__': str(p)})
