from pathlib import Path

p = Path('.github/scripts/kuraloviyam-part003-release.py')
source = p.read_text(encoding='utf-8')

# Reconcile the release runner with the durable Part-review control state that
# advanced after the first version of the temporary release script was written.
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
        "t = replace_once(t, '- Part review / release: **not-started**.', '- Part-level review: **PASS / CLOSED**; release report: **APPROVED / CLOSED**; release-ready: **111/111**.', 'work handover gates')",
        "t = replace_once(t, '- Part-level English review: **PASS / CLOSED**; release report / release-ready: **not-started**.', '- Part-level review: **PASS / CLOSED**; release report: **APPROVED / CLOSED**; release-ready: **111/111**.', 'work handover gates')"
    ),
    (
        "t = replace_once(t, '- Part review / release: **not-started**.', '- Part-level review: **PASS / CLOSED**; release report: **APPROVED / CLOSED**; release-ready: **111/111 COMPLETE / CLOSED**.', 'English README gates')",
        "t = replace_once(t, '- Part-level review: **PASS / CLOSED**; release report / release-ready: **not-started**.', '- Part-level review: **PASS / CLOSED**; release report: **APPROVED / CLOSED**; release-ready: **111/111 COMPLETE / CLOSED**.', 'English README gates')"
    ),
    (
        "t = replace_once(t, '- editorial review: **111/111 COMPLETE / CLOSED**; Part review / release: **not-started**.', '- editorial review: **111/111 COMPLETE / CLOSED**; Part-level review: **PASS / CLOSED**; English release: **APPROVED / CLOSED — 111/111 release-ready**.', 'next prompt gate summary')",
        "t = replace_once(t, '- editorial review: **111/111 COMPLETE / CLOSED**; Part-level English review: **PASS / CLOSED**; release report / release-ready: **not-started**.', '- editorial review: **111/111 COMPLETE / CLOSED**; Part-level review: **PASS / CLOSED**; English release: **APPROVED / CLOSED — 111/111 release-ready**.', 'next prompt gate summary')"
    ),
]
for old, new in subs:
    if old not in source:
        raise RuntimeError(f'compatibility patch target not found: {old[:140]}')
    source = source.replace(old, new, 1)

# The release script originally used the now-stale Part-review frontier marker twice
# (work handover + next-chat prompt). Point both at the current release frontier.
source = source.replace(
    "r'^## Exact next activity — Part 003 whole-Part English review$'",
    "r'^## Exact next activity — Part 003 English release report$'"
)

# English README contains the same live-state sentence in two maintained sections.
# Promote both copies so the post-release documentation has no stale 'current state'.
old_call = "t = replace_once(t, '- current English state: **111 `editorial-reviewed` + 0 `source-checked` / 0 `draft` / 0 source-limited / 0 blocked**;', '- current English state: **111 `release-ready` / 0 `editorial-reviewed` / 0 `source-checked` / 0 `draft` / 0 source-limited / 0 blocked**;', 'English README state')"
new_call = "old_state = '- current English state: **111 `editorial-reviewed` + 0 `source-checked` / 0 `draft` / 0 source-limited / 0 blocked**;'\nnew_state = '- current English state: **111 `release-ready` / 0 `editorial-reviewed` / 0 `source-checked` / 0 `draft` / 0 source-limited / 0 blocked**;'\nif t.count(old_state) != 2:\n    raise RuntimeError(f'English README state: expected 2 matches, found {t.count(old_state)}')\nt = t.replace(old_state, new_state)"
if old_call not in source:
    raise RuntimeError('English README multi-state patch target not found')
source = source.replace(old_call, new_call, 1)

exec(compile(source, str(p), 'exec'), {'__name__': '__main__', '__file__': str(p)})
