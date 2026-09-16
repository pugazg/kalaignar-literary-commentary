# NEXT CHAT PROMPT — சங்கத் தமிழ் / MAINTAINED ENGLISH D1

Continue only from live `main` in `pugazg/kalaignar-literary-commentary`. **LIVE MAIN IS AUTHORITATIVE.**

## Tamil archive — FROZEN

Gates **A–I are COMPLETE / PASS**. Gate C2 is **COMPLETE / APPLIED 140/140** and post-C2 reconciliation R1 is **COMPLETE / PASS**.

Do not reopen canonical Tamil wording, structure, section ranges, provenance, metadata/status or navigation merely for English translation.

Final Tamil page state:

- `verified` — **43**
- `needs-review` — **453**
- `partial` — **1** (scan 8 handwritten `முன்னுரை`, description-only)

Whole-volume word-for-word scan verification is **NOT CLAIMED**.

## Maintained English authority

Read first:

1. `works/sangatamil/translations/en/TRANSLATION_GUIDE.md`
2. `works/sangatamil/translations/en/GLOSSARY.md`
3. `works/sangatamil/translations/en/TRANSLATION_STATUS.md`
4. `works/sangatamil/README.md`
5. `works/sangatamil/GATE_I_FINAL_CLOSURE.md`
6. `works/sangatamil/indexes/section-register.md`
7. `works/sangatamil/indexes/source-citation-register.md`
8. root `HANDOVER.md`

## Translation identity

This is a **project-created maintained English translation**, not an official/publisher English edition.

Every English page must contain:

```yaml
translation_type: "project_translation"
```

Do not import published Sangam translations, web text, another commentator or remembered conventional wording.

English review certifies fidelity to the **maintained canonical Tamil record**; it does not promote the underlying Tamil page status or imply exhaustive scan-level Tamil verification.

## Workflow

**draft → source-check → glossary reconciliation → editorial review → review → release report → release-ready**

Normal page-batched cadence: **37 physical scans**.

## Exact next activity

**Draft D1 — scans 1–37.**

Requirements:

- create matching files under `works/sangatamil/translations/en/pages/`;
- mirror Tamil filenames exactly;
- translate source order, prose, dialogue, quoted verse, source labels, provenance and visual descriptions faithfully;
- preserve cross-page continuation;
- copy factual Tamil status/visual-fidelity into `source_tamil_status` / `source_tamil_visual_fidelity`;
- use `status: "draft"` for safely translatable pages;
- scan **8** must be `source-limited`, translating only the secure archival description; do **not** decipher/reconstruct its handwriting;
- update `TRANSLATION_STATUS.md` after D1;
- audit the exact changed-file set;
- change **0 canonical Tamil page files**.
