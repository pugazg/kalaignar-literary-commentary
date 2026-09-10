from pathlib import Path
import subprocess

PAGE_COMMIT = "1cc8d67b390345aee74ab4683f469c01f4dc4874"
PAGE_BASE = "c7690b5e1cd3d68cae9e95c36de21a902184e2a2"


def replace_once(text, old, new, label):
    count = text.count(old)
    if count != 1:
        raise SystemExit(f"{label}: replacement count={count} for {old!r}")
    return text.replace(old, new, 1)


def replace_tail(path, heading, new_tail):
    p = Path(path)
    text = p.read_text(encoding="utf-8")
    if heading not in text:
        raise SystemExit(f"missing heading in {path}: {heading!r}")
    p.write_text(text.split(heading, 1)[0] + new_tail, encoding="utf-8")


# TRANSLATION_STATUS.md
p = Path("works/kuraloviyam/translations/en/TRANSLATION_STATUS.md")
s = p.read_text(encoding="utf-8")
s = replace_once(
    s,
    "- source-check: **IN PROGRESS — 66/111 COMPLETE**;",
    "- source-check: **IN PROGRESS — 99/111 COMPLETE**;",
    "TRANSLATION_STATUS summary",
)
p.write_text(s, encoding="utf-8")
replace_tail(
    p,
    "## Part 003 English source-check — IN PROGRESS\n",
    f'''## Part 003 English source-check — IN PROGRESS

- **SC1: scans 223–255 / printed 206–238 — COMPLETE 33/33**;
- **SC2: scans 256–288 / printed 239–271 — COMPLETE 33/33**;
- **SC3: scans 289–321 / printed 272–304 — COMPLETE 33/33**;
- cumulative source-check: **99/111**;
- current Part-003 English state: **99 `source-checked` + 12 `draft` / 0 source-limited / 0 blocked**;
- remaining source-check pages: **12**.

SC1 and SC2 remain closed at their previously recorded checkpoints.

SC3 compared every English record against the audited Tamil counterpart paragraph-by-paragraph / block-by-block. All **33/33** pages passed after source-fidelity reconciliation. Corrections were limited to:

- scan **295 / printed 278 / Kural 1264** — restored the source's singular branch image, replacing the unsupported `branch after branch` expansion with `a branch`;
- scan **299 / printed 282** — replaced the unsupported saltiness inference with the source-faithful sense that her tears tasted sweet to him **without any sting**;
- scan **302 / printed 285** — restored the large red decorative pavilion/monument below the Chapter/Kural metadata as factual source page furniture, separate from body prose;
- scans **309→310 / printed 292→293** — repaired the physical-page continuation so the judge's decision begins on scan 310 where the audited Tamil record begins it, instead of being pulled backward onto scan 309;
- scan **320 / printed 303** — corrected `tongue-shaped feet` to the source-faithful `tongue-coloured feet`.

SC3 page commit: `{PAGE_COMMIT}` — `kuraloviyam: Source-check Part 003 English scans 289-321`.

The SC3 page-only comparison from `{PAGE_BASE}` to `{PAGE_COMMIT}` is **ahead / non-divergent** and contains exactly **33 modified English page records**, scans **289–321**, with no Tamil page or Tamil metadata change. Twenty-seven pages changed only by status promotion; six page files also contain the source-fidelity corrections above.

The incoming **288→289** relationship is a genuine continuation and remains preserved; scan 289 closes it. The outgoing **321→322 boundary is CLEAN**.

## Current frontier — Part 003 English Source-check SC4

Exact next activity: **source-check scans 322–333 / printed 305–316 — FINAL 12-PAGE REMAINDER**.

Compare each English page against its audited Tamil counterpart paragraph-by-paragraph / block-by-block for omissions, additions, meaning drift, names, titles, quotations, Kural blocks, visual/non-body page function and cross-page continuity. Only passing pages may move from `draft` to `source-checked`.

Do not perform glossary reconciliation or editorial review during SC4. Do not alter Tamil archival records. Preserve the CLEAN incoming **321→322** boundary, the genuine internal **332→333** continuation, and the Part ending at scan **333**. External **333→334** remains deferred until Part 004 source intake.

If SC4 passes, Part-003 English source-check becomes **111/111 COMPLETE / CLOSED** and the next gate is **glossary / recurring-terminology reconciliation**, using the current 33-page cadence.

Part 004 remains blocked until Part 003 completes its maintained English workflow and final Part closure checkpoint.
''',
)

# English README
p = Path("works/kuraloviyam/translations/en/README.md")
s = p.read_text(encoding="utf-8")
s = replace_once(
    s,
    "- source-check: **IN PROGRESS — SC1 + SC2 COMPLETE 66/111**;\n- current English state: **66 `source-checked` + 45 `draft` / 0 source-limited / 0 blocked**;",
    "- source-check: **IN PROGRESS — SC1 + SC2 + SC3 COMPLETE 99/111**;\n- current English state: **99 `source-checked` + 12 `draft` / 0 source-limited / 0 blocked**;",
    "README summary",
)
p.write_text(s, encoding="utf-8")
replace_tail(
    p,
    "## Part 003 English source-check\n",
    '''## Part 003 English source-check

- SC1 **223–255 / 206–238 — COMPLETE 33/33**;
- SC2 **256–288 / 239–271 — COMPLETE 33/33**;
- SC3 **289–321 / 272–304 — COMPLETE 33/33**;
- cumulative source-check: **99/111**;
- current English state: **99 `source-checked` + 12 `draft` / 0 source-limited / 0 blocked**.

SC3 source-fidelity reconciliation corrected the singular branch image on scan **295**, the tears/sting wording on **299**, source page-furniture metadata on **302**, the physical continuation across **309→310**, and `tongue-coloured feet` on **320**. No Tamil archival record changed. Incoming **288→289** remains the genuine continuation closed by scan 289; outgoing **321→322 is CLEAN**.

## Current frontier

Exact next activity: **Part 003 English source-check SC4 — scans 322–333 / printed 305–316, final 12 pages**.

Compare every English record against its audited Tamil counterpart paragraph-by-paragraph / block-by-block. Check omissions, additions, meaning drift, names, titles, quotations, Kural blocks, visual/non-body page function and cross-page continuity. Only passing pages may move from `draft` to `source-checked`.

If SC4 passes, source-check becomes **111/111 COMPLETE / CLOSED** and the next gate is **glossary / recurring-terminology reconciliation**. Preserve the genuine **332→333** continuation and keep external **333→334** deferred until Part 004 intake. Part 004 remains blocked until the maintained English workflow and final Part closure checkpoint are complete.

See `TRANSLATION_STATUS.md` for the authoritative detailed frontier.
''',
)

# Work HANDOVER
p = Path("works/kuraloviyam/HANDOVER.md")
s = p.read_text(encoding="utf-8")
s = replace_once(
    s,
    "- source-check: **IN PROGRESS — SC1 + SC2 COMPLETE 66/111**;\n- current English state: **66 `source-checked` + 45 `draft` / 0 source-limited / 0 blocked**;",
    "- source-check: **IN PROGRESS — SC1 + SC2 + SC3 COMPLETE 99/111**;\n- current English state: **99 `source-checked` + 12 `draft` / 0 source-limited / 0 blocked**;",
    "HANDOVER summary",
)
p.write_text(s, encoding="utf-8")
replace_tail(
    p,
    "## Source-check progress — SC1 + SC2 COMPLETE 66/111\n",
    f'''## Source-check progress — SC1 + SC2 + SC3 COMPLETE 99/111

- SC1 **223–255 / printed 206–238 — COMPLETE 33/33**;
- SC2 **256–288 / printed 239–271 — COMPLETE 33/33**;
- SC3 **289–321 / printed 272–304 — COMPLETE 33/33**.

All SC3 records now carry `status: "source-checked"`. Source-fidelity corrections were limited to scans **295, 299, 302, 309→310 and 320**. No Tamil file or metadata changed.

SC3 page commit: `{PAGE_COMMIT}`. The incoming **288→289** continuation remains genuine and closes on scan 289. Outgoing **321→322 is CLEAN**.

## Exact next activity — English Source-check SC4

Process **scans 322–333 / printed 305–316 — FINAL 12 PAGE-ALIGNED RECORDS**.

1. fetch live `main` first;
2. confirm `PART_003_TAMIL_ARCHIVAL_READY.md` remains **PASS / CLOSED**;
3. confirm `translations/en/TRANSLATION_STATUS.md` records source-check **99/111 cumulative**;
4. read English records **0322–0333** and matching audited Tamil records completely;
5. compare paragraph-by-paragraph / block-by-block for omissions, additions, meaning drift, names, titles, quotations, Kural blocks, visual/non-body page function and cross-page continuity;
6. preserve the audited Tamil wording as source authority; do not import standard/published/web English Kural text;
7. make only source-fidelity corrections needed to pass source-check;
8. only passing pages may move from `status: "draft"` to `status: "source-checked"`;
9. preserve incoming **321→322 CLEAN**, genuine internal **332→333** continuation, and the Part ending at scan **333**;
10. do not alter Tamil files;
11. do not begin glossary reconciliation or editorial review during SC4;
12. update `translations/en/TRANSLATION_STATUS.md` and audit the exact changed-file set.

If SC4 passes, source-check becomes **111/111 COMPLETE / CLOSED**. The next gate is **glossary / recurring-terminology reconciliation**, beginning at scans **223–255 / printed 206–238** under the current 33-page cadence.

External **333→334** remains deferred until Part 004 source intake. Part 004 remains blocked until Part 003 completes its maintained English workflow and final Part closure checkpoint.
''',
)

# NEXT_CHAT_PROMPT
p = Path("NEXT_CHAT_PROMPT_KURALOVIYAM.md")
s = p.read_text(encoding="utf-8")
s = replace_once(
    s,
    "- Part 003 English source-check SC1: **COMPLETE 33/33 — scans 223–255 / printed 206–238**.\n- Part 003 English source-check SC2: **COMPLETE 33/33 — scans 256–288 / printed 239–271**.\n- cumulative source-check: **66/111**.\n- current Part-003 English state: **66 `source-checked` + 45 `draft` / 0 source-limited / 0 blocked**.",
    "- Part 003 English source-check SC1: **COMPLETE 33/33 — scans 223–255 / printed 206–238**.\n- Part 003 English source-check SC2: **COMPLETE 33/33 — scans 256–288 / printed 239–271**.\n- Part 003 English source-check SC3: **COMPLETE 33/33 — scans 289–321 / printed 272–304**.\n- cumulative source-check: **99/111**.\n- current Part-003 English state: **99 `source-checked` + 12 `draft` / 0 source-limited / 0 blocked**.",
    "NEXT_CHAT durable state",
)
p.write_text(s, encoding="utf-8")
replace_tail(
    p,
    "## Source-check results through SC2 — COMPLETE / PASS\n",
    '''## Source-check results through SC3 — COMPLETE / PASS

- SC1 **223–255 / 206–238 — 33/33 source-checked**;
- SC2 **256–288 / 239–271 — 33/33 source-checked**;
- SC3 **289–321 / 272–304 — 33/33 source-checked**;
- cumulative source-check **99/111**;
- current English state **99 source-checked + 12 draft / 0 source-limited / 0 blocked**.

SC3 source-fidelity corrections were limited to scans **295, 299, 302, 309→310 and 320**. The page-only gate changed exactly 33 English records and no Tamil record. Incoming **288→289** remains a genuine continuation closed on scan 289. Outgoing **321→322 is CLEAN**.

## Exact next activity — Part 003 English Source-check SC4

Process **scans 322–333 / printed 305–316 — final 12 page-aligned records**.

Requirements:

1. fetch live `main` first and preserve newer durable work;
2. confirm `PART_003_TAMIL_ARCHIVAL_READY.md` remains **PASS / CLOSED**;
3. confirm `translations/en/TRANSLATION_STATUS.md` records source-check **99/111 cumulative**;
4. read English records **0322–0333** and matching audited Tamil records completely;
5. compare each page paragraph-by-paragraph / block-by-block for omissions, additions, meaning drift, names, titles, quotations, Kural wording/lineation, visual/non-body page function and cross-page continuity;
6. correct only source-fidelity issues supported by the audited Tamil records;
7. keep `source_tamil_status: "verified"` and promote only passing pages from `draft` to `source-checked`;
8. preserve incoming **321→322 CLEAN**, internal **332→333 genuine continuation**, and the Part end at scan **333**;
9. do not alter any Tamil page record or Tamil metadata;
10. do not begin glossary reconciliation or editorial review during SC4;
11. update `translations/en/TRANSLATION_STATUS.md` after the batch;
12. audit the exact changed-file set before advancing.

If SC4 passes, Part-003 English source-check becomes **111/111 COMPLETE / CLOSED**. The next gate is **glossary / recurring-terminology reconciliation**, beginning with **scans 223–255 / printed 206–238** under the current 33-page cadence.

External **333→334** remains deferred until Part 004 source intake. Part 004 remains blocked until Part 003 completes the maintained English workflow and final Part closure checkpoint.
''',
)

expected = {
    "works/kuraloviyam/translations/en/TRANSLATION_STATUS.md",
    "works/kuraloviyam/translations/en/README.md",
    "works/kuraloviyam/HANDOVER.md",
    "NEXT_CHAT_PROMPT_KURALOVIYAM.md",
}
changed = set(subprocess.check_output(["git", "diff", "--name-only"], text=True).splitlines())
if changed != expected:
    raise SystemExit(f"control changed-file audit failed: {sorted(changed ^ expected)}")
