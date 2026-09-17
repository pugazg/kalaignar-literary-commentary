# NEXT CHAT PROMPT — சங்கத் தமிழ் / MAINTAINED ENGLISH D8

Continue only from live `main` in `pugazg/kalaignar-literary-commentary`. **LIVE MAIN IS AUTHORITATIVE.**

## Tamil archive — FROZEN

Gates **A–I are COMPLETE / PASS**. Gate C2 is **COMPLETE / APPLIED 140/140** and post-C2 reconciliation R1 is **COMPLETE / PASS**.

Do not reopen canonical Tamil wording, structure, section ranges, provenance, metadata/status or navigation merely for English translation.

Whole-volume word-for-word scan verification is **NOT CLAIMED**.

## Maintained English authority

Read first:

1. `works/sangatamil/translations/en/TRANSLATION_GUIDE.md`
2. `works/sangatamil/translations/en/GLOSSARY.md`
3. `works/sangatamil/translations/en/TRANSLATION_STATUS.md`
4. `works/sangatamil/translations/en/DRAFT_D1_REPORT.md`
5. `works/sangatamil/translations/en/DRAFT_D2_REPORT.md`
6. `works/sangatamil/translations/en/DRAFT_D3_REPORT.md`
7. `works/sangatamil/translations/en/DRAFT_D4_REPORT.md`
8. `works/sangatamil/translations/en/DRAFT_D5_REPORT.md`
9. `works/sangatamil/translations/en/DRAFT_D6_REPORT.md`
10. `works/sangatamil/translations/en/DRAFT_D7_REPORT.md`
11. `works/sangatamil/README.md`
12. `works/sangatamil/GATE_I_FINAL_CLOSURE.md`
13. `works/sangatamil/indexes/section-register.md`
14. `works/sangatamil/indexes/source-citation-register.md`
15. root `HANDOVER.md` — historical/background context; if its maintained-English frontier line lags, `TRANSLATION_STATUS.md` and this prompt control the live English frontier.

## Drafting closed state

D1 scans **1–37 — COMPLETE / PASS**.  
D2 scans **38–74 — COMPLETE / PASS**.  
D3 scans **75–111 — COMPLETE / PASS**.  
D4 scans **112–148 — COMPLETE / PASS**.  
D5 scans **149–185 — COMPLETE / PASS**.  
D6 scans **186–222 — COMPLETE / PASS**.  
D7 scans **223–259 — COMPLETE / PASS**.

Cumulative English state:

- page records — **259/497**
- `draft` — **258**
- `source-limited` — **1** (scan 8)
- source-check — **0/497**
- canonical Tamil page changes from English drafting — **0**

D7 page-layer endpoint: `b63efa7cef0971dee26a79544fb9975fd0429884`.

## Translation identity

This is a **project-created maintained English translation**, not an official/publisher English edition.

Every English page must contain:

```yaml
translation_type: "project_translation"
```

Do not import published Sangam translations, web text, another commentator or remembered conventional wording.

English review certifies fidelity to the maintained canonical Tamil record; it does not promote the underlying Tamil page status or imply exhaustive scan-level Tamil verification.

## Workflow

**draft → source-check → glossary reconciliation → editorial review → review → release report → release-ready**

Normal page-batched cadence: **37 physical scans**.

## Exact next activity

**Draft D8 — scans 260–296.**

Requirements:

- begin by preserving the continuation from scan **259** into scan **260** (`0260-panjanaiyil-arasi-paasaraiyil-mannan-03.md`);
- create matching files under `works/sangatamil/translations/en/pages/`;
- mirror Tamil filenames exactly;
- translate source order, prose, dialogue, quoted verse, source labels, provenance and visual descriptions faithfully;
- preserve all cross-page continuities;
- copy factual Tamil status/visual-fidelity into `source_tamil_status` / `source_tamil_visual_fidelity`;
- use `status: "draft"` for safely translatable pages, preserving `source-limited` only where the Tamil record itself requires it;
- do not silently repair awkward or unresolved canonical Tamil wording; leave it for source-check;
- update `TRANSLATION_STATUS.md` after D8;
- audit the exact changed-file set;
- change **0 canonical Tamil page files**.

Do not begin source-check until the active first-pass drafting frontier is complete.
