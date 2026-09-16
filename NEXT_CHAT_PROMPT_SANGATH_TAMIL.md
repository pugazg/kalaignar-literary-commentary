# NEXT CHAT PROMPT — சங்கத் தமிழ் / MAINTAINED ENGLISH D3

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
6. `works/sangatamil/README.md`
7. `works/sangatamil/GATE_I_FINAL_CLOSURE.md`
8. `works/sangatamil/indexes/section-register.md`
9. `works/sangatamil/indexes/source-citation-register.md`
10. root `HANDOVER.md`

## Drafting closed state

D1 scans **1–37 — COMPLETE / PASS**.  
D2 scans **38–74 — COMPLETE / PASS**.

Cumulative English state:

- page records — **74/497**
- `draft` — **73**
- `source-limited` — **1** (scan 8)
- source-check — **0/497**
- canonical Tamil page changes from English drafting — **0**

D2 page-layer endpoint: `4bc4dbf888ef6227ef93779eefef7bf13b2c7ccc`.

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

**Draft D3 — scans 75–111.**

Requirements:

- create matching files under `works/sangatamil/translations/en/pages/`;
- mirror Tamil filenames exactly;
- translate source order, prose, dialogue, quoted verse, source labels, provenance and visual descriptions faithfully;
- preserve all cross-page continuities;
- copy factual Tamil status/visual-fidelity into `source_tamil_status` / `source_tamil_visual_fidelity`;
- use `status: "draft"` for safely translatable pages, preserving `source-limited` only where the Tamil record itself requires it;
- update `TRANSLATION_STATUS.md` after D3;
- audit the exact changed-file set;
- change **0 canonical Tamil page files**.

Do not begin source-check until the active first-pass drafting frontier is complete.
