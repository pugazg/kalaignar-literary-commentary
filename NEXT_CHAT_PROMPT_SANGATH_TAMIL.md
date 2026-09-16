# NEXT CHAT PROMPT — சங்கத் தமிழ் / MAINTAINED ENGLISH D2

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
5. `works/sangatamil/README.md`
6. `works/sangatamil/GATE_I_FINAL_CLOSURE.md`
7. `works/sangatamil/indexes/section-register.md`
8. `works/sangatamil/indexes/source-citation-register.md`
9. root `HANDOVER.md`

## D1 closed state

Draft D1 scans **1–37 — COMPLETE / PASS**.

- English page records — **37/497**
- `draft` — **36**
- `source-limited` — **1** (scan 8 handwritten `முன்னுரை`)
- page-layer base — `2ffa826d436b8ac37940986a43bcf7d9f5b78bc1`
- page-layer endpoint — `1eb0df73d39545cea4e680048a58a4bff759990d`
- D1 changed files — **37 English page files only**
- canonical Tamil page changes — **0**

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

**Draft D2 — scans 38–74.**

Requirements:

- create matching files under `works/sangatamil/translations/en/pages/`;
- mirror Tamil filenames exactly;
- translate source order, prose, dialogue, quoted verse, source labels, provenance and visual descriptions faithfully;
- preserve cross-page continuation from scan 37 into scan 38 and all D2 internal continuities;
- copy factual Tamil status/visual-fidelity into `source_tamil_status` / `source_tamil_visual_fidelity`;
- use `status: "draft"` for safely translatable pages, preserving `source-limited` only where the Tamil record itself requires it;
- update `TRANSLATION_STATUS.md` after D2;
- audit the exact changed-file set;
- change **0 canonical Tamil page files**.

Do not begin source-check until the active first-pass drafting frontier is complete.
