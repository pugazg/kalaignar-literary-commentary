from pathlib import Path
import subprocess


def replace_tail(path, marker, tail):
    p = Path(path)
    text = p.read_text(encoding="utf-8")
    idx = text.find(marker)
    if idx < 0:
        raise SystemExit(f"marker not found in {path}: {marker}")
    p.write_text(text[:idx] + tail.rstrip() + "\n", encoding="utf-8")


p = Path("works/kuraloviyam/translations/en/TRANSLATION_STATUS.md")
s = p.read_text(encoding="utf-8")
s = s.replace(
    "- source-check: **IN PROGRESS — 33/111 COMPLETE**;",
    "- source-check: **IN PROGRESS — 66/111 COMPLETE**;",
    1,
)
p.write_text(s, encoding="utf-8")
replace_tail(
    p,
    "## Part 003 English source-check — IN PROGRESS",
    """## Part 003 English source-check — IN PROGRESS

- **SC1: scans 223–255 / printed 206–238 — COMPLETE 33/33**;
- **SC2: scans 256–288 / printed 239–271 — COMPLETE 33/33**;
- cumulative source-check: **66/111**;
- current Part-003 English state: **66 `source-checked` + 45 `draft` / 0 source-limited / 0 blocked**;
- remaining source-check pages: **45**.

SC1 passed all 33 pages after its recorded source-fidelity reconciliation.

SC2 compared every page paragraph-by-paragraph / block-by-block against the audited Tamil records. All **33/33** pages passed after source-fidelity reconciliation. Corrections were limited to:

- scans **257, 267 and 277** — restored the source pages' small red decorative monument as factual visual-material metadata;
- scan **274 / printed 257** — repaired the split return-from-enemy-stronghold sentence so the English preserves the source sense that the prince entered the enemy stronghold stealthily in darkness and is now returning victorious.

SC2 page commit: `4438c820a0ea018acfb7b4b8d7bf03d1b2428120` — `kuraloviyam: Source-check Part 003 English scans 256-288`.

The SC2 page gate changes exactly **33 English page records**, scans **256–288**, and no Tamil page or Tamil metadata. The incoming **255→256 boundary is CLEAN**. The outgoing **288→289** relationship is a genuine continuation and remains preserved; scan 289 closes the renunciation vignette.

## Current frontier — Part 003 English Source-check SC3

Exact next activity: **source-check scans 289–321 / printed 272–304 — 33 page-aligned records**.

Compare each English page against its audited Tamil counterpart paragraph-by-paragraph / block-by-block for omissions, additions, meaning drift, names, titles, quotations, Kural blocks, visual/non-body page function and cross-page continuity. Only passing pages may move from `draft` to `source-checked`.

Do not perform glossary reconciliation or editorial review during SC3. Do not alter Tamil archival records. Preserve the genuine incoming **288→289** continuation and the CLEAN outgoing **321→322** boundary. If SC3 passes, cumulative source-check becomes **99/111** and SC4 will be the final **scans 322–333 / printed 305–316 — 12-page remainder**.

Part 004 remains blocked until Part 003 completes its maintained English workflow and final Part closure checkpoint.""",
)

p = Path("works/kuraloviyam/translations/en/README.md")
s = p.read_text(encoding="utf-8")
s = s.replace(
    "- source-check: **IN PROGRESS — SC1 COMPLETE 33/111**;\n- current English state: **33 `source-checked` + 78 `draft` / 0 source-limited / 0 blocked**;",
    "- source-check: **IN PROGRESS — SC1 + SC2 COMPLETE 66/111**;\n- current English state: **66 `source-checked` + 45 `draft` / 0 source-limited / 0 blocked**;",
    1,
)
p.write_text(s, encoding="utf-8")
replace_tail(
    p,
    "## Part 003 English source-check",
    """## Part 003 English source-check

- SC1 **223–255 / 206–238 — COMPLETE 33/33**;
- SC2 **256–288 / 239–271 — COMPLETE 33/33**;
- cumulative source-check: **66/111**;
- current English state: **66 `source-checked` + 45 `draft` / 0 source-limited / 0 blocked**.

SC2 source-fidelity reconciliation restored the small red decorative monument metadata on scans **257, 267 and 277** and repaired scan **274**'s return-from-enemy-stronghold sentence. No Tamil archival record changed. Incoming **255→256** is CLEAN; outgoing **288→289** is a genuine continuation preserved into SC3.

## Current frontier

Exact next activity: **Part 003 English source-check SC3 — scans 289–321 / printed 272–304, 33 pages**.

Compare every English record against its audited Tamil counterpart paragraph-by-paragraph / block-by-block. Check omissions, additions, meaning drift, names, titles, quotations, Kural blocks, visual/non-body page function and cross-page continuity. Only passing pages may move from `draft` to `source-checked`.

If SC3 passes, cumulative source-check becomes **99/111** and SC4 will be **322–333 / printed 305–316 — final 12 pages**. Do not begin glossary reconciliation until all Part-003 source-check batches are complete. Part 004 remains blocked until the Part-003 maintained English workflow and final Part closure checkpoint are complete.

See `TRANSLATION_STATUS.md` for the authoritative detailed frontier.""",
)

p = Path("works/kuraloviyam/HANDOVER.md")
s = p.read_text(encoding="utf-8")
s = s.replace(
    "- source-check: **IN PROGRESS — SC1 COMPLETE 33/111**;\n- current English state: **33 `source-checked` + 78 `draft` / 0 source-limited / 0 blocked**;",
    "- source-check: **IN PROGRESS — SC1 + SC2 COMPLETE 66/111**;\n- current English state: **66 `source-checked` + 45 `draft` / 0 source-limited / 0 blocked**;",
    1,
)
p.write_text(s, encoding="utf-8")
replace_tail(
    p,
    "## Source-check SC1 — COMPLETE 33/33",
    """## Source-check progress — SC1 + SC2 COMPLETE 66/111

SC1 covers **223–255 / printed 206–238 — COMPLETE 33/33**.

SC2 covers **256–288 / printed 239–271 — COMPLETE 33/33**. All SC2 records now carry `status: \"source-checked\"`. Source-fidelity corrections were limited to visual-material restoration on scans **257, 267, 277** and the return-from-enemy-stronghold sentence on **274**. No Tamil file or metadata changed.

SC2 page commit: `4438c820a0ea018acfb7b4b8d7bf03d1b2428120`. Incoming **255→256 is CLEAN**. Outgoing **288→289 is a genuine continuation**; scan 289 closes that renunciation vignette.

## Exact next activity — English Source-check SC3

Process **scans 289–321 / printed 272–304 — 33 page-aligned records**.

1. fetch live `main` first;
2. confirm `PART_003_TAMIL_ARCHIVAL_READY.md` remains **PASS / CLOSED**;
3. confirm `translations/en/TRANSLATION_STATUS.md` records source-check **66/111 cumulative**;
4. read English records **0289–0321** and matching audited Tamil records completely;
5. compare paragraph-by-paragraph / block-by-block for omissions, additions, meaning drift, names, titles, quotations, Kural blocks, visual/non-body page function and cross-page continuity;
6. preserve the audited Tamil wording as source authority; do not import standard/published/web English Kural text;
7. make only source-fidelity corrections needed to pass source-check;
8. only passing pages may move from `status: \"draft\"` to `status: \"source-checked\"`;
9. preserve the genuine incoming **288→289** continuation and CLEAN outgoing **321→322** boundary;
10. do not alter Tamil files;
11. do not begin glossary reconciliation or editorial review during SC3;
12. update `translations/en/TRANSLATION_STATUS.md` and audit the exact changed-file set.

If SC3 passes, source-check becomes **99/111** and SC4 will be the final **scans 322–333 / printed 305–316 — 12 pages**.

Part 004 remains blocked until Part 003 completes its maintained English workflow and final Part closure checkpoint.""",
)

p = Path("NEXT_CHAT_PROMPT_KURALOVIYAM.md")
s = p.read_text(encoding="utf-8")
s = s.replace(
    "- Part 003 English source-check SC1: **COMPLETE 33/33 — scans 223–255 / printed 206–238**.\n- cumulative source-check: **33/111**.\n- current Part-003 English state: **33 `source-checked` + 78 `draft` / 0 source-limited / 0 blocked**.",
    "- Part 003 English source-check SC1: **COMPLETE 33/33 — scans 223–255 / printed 206–238**.\n- Part 003 English source-check SC2: **COMPLETE 33/33 — scans 256–288 / printed 239–271**.\n- cumulative source-check: **66/111**.\n- current Part-003 English state: **66 `source-checked` + 45 `draft` / 0 source-limited / 0 blocked**.",
    1,
)
p.write_text(s, encoding="utf-8")
replace_tail(
    p,
    "## SC1 result — COMPLETE / PASS",
    """## Source-check results through SC2 — COMPLETE / PASS

- SC1 **223–255 / 206–238 — 33/33 source-checked**;
- SC2 **256–288 / 239–271 — 33/33 source-checked**;
- cumulative source-check **66/111**;
- current English state **66 source-checked + 45 draft / 0 source-limited / 0 blocked**.

SC2 source-fidelity corrections were limited to scans **257, 267, 277** (small red decorative monument visual metadata) and **274** (return-from-enemy-stronghold sentence). No Tamil record changed. **255→256 is CLEAN**. **288→289 is a genuine continuation** and must remain continuous into SC3.

## Exact next activity — Part 003 English Source-check SC3

Process **scans 289–321 / printed 272–304 — 33 page-aligned records**.

Requirements:

1. fetch live `main` first and preserve newer durable work;
2. confirm `PART_003_TAMIL_ARCHIVAL_READY.md` remains **PASS / CLOSED**;
3. confirm `translations/en/TRANSLATION_STATUS.md` records source-check **66/111 cumulative**;
4. read English records **0289–0321** and the matching audited Tamil records completely;
5. compare each page paragraph-by-paragraph / block-by-block for omissions, additions, meaning drift, names, titles, quotations, Kural wording/lineation, visual/non-body page function and cross-page continuity;
6. correct only source-fidelity issues supported by the audited Tamil records;
7. keep `source_tamil_status: \"verified\"` and promote only passing pages from `draft` to `source-checked`;
8. preserve incoming **288→289 genuine continuation** and outgoing **321→322 CLEAN**;
9. do not alter any Tamil page record or Tamil metadata;
10. do not begin glossary reconciliation or editorial review during SC3;
11. update `translations/en/TRANSLATION_STATUS.md` after the batch;
12. audit the exact changed-file set before advancing.

If SC3 passes, Part-003 English source-check becomes **99/111**. The next batch will be **SC4: scans 322–333 / printed 305–316 — final 12 pages**.

Part 004 remains blocked until Part 003 completes the maintained English workflow and final Part closure checkpoint.""",
)

expected = {
    "NEXT_CHAT_PROMPT_KURALOVIYAM.md",
    "works/kuraloviyam/HANDOVER.md",
    "works/kuraloviyam/translations/en/README.md",
    "works/kuraloviyam/translations/en/TRANSLATION_STATUS.md",
}
changed = set(subprocess.check_output(["git", "diff", "--name-only"], text=True).splitlines())
if changed != expected:
    raise SystemExit(f"control changed-file audit failed: {sorted(changed ^ expected)}")
