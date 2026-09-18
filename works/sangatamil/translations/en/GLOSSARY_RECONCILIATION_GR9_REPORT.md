# Sangatamil — Maintained English Glossary Reconciliation GR9 Report

**Status: COMPLETE / PASS**

- date: **2026-09-18**
- repository: `pugazg/kalaignar-literary-commentary`
- branch: `main`
- batch: **GR9**
- physical scans: **297–333**
- base: `a32318a5238d957278ccf2bdf433529cbdcd9425`
- endpoint: `86e7f468cc905730b21787ccb7dba005af745973`

## Scope

GR9 reconciled recurring maintained-English terminology across scans **297–333** after source-check closure and GR1–GR8.

The range was checked paragraph-by-paragraph / block-by-block against the maintained canonical Tamil records for omissions, additions, meaning drift, names, titles, dialogue, quoted verse, source labels, provenance, visual/page function and cross-page continuity. The user-supplied controlling PDF slices covering scans **297–333** were also consulted for the physical page sequence and source context.

`GLOSSARY.md` remained a context-aware editorial control rather than a mechanical substitution table. No published Sangam English translation, web translation, external edition or remembered conventional wording was imported.

## GR9 result

Coverage — **37/37 scans reconciled**.

English page status state was deliberately unchanged:

- `source-checked` — **496**
- `source-limited` — **1** (scan 8)
- `draft` — **0**
- page status changes during GR9 — **0**

Cumulative glossary reconciliation after GR9 — **333/497**.

## Controlled glossary additions

GR9 added or expanded source-evidenced controls for:

- **Perumpanarruppatai** and the classical **arruppatai** guide-poem genre;
- `நாழி` → **nāzhi / grain measure**;
- `கடுவன்` → **kaduvan / male monkey** and `மந்தி` → **mandhi / female monkey**;
- `முரசு` → context-sensitive **war-drum / drum**;
- **Ilam Peruvazhuthi**;
- **Karumpillai Puthanar** and **Maruthuvan Nallachuthanar**;
- **Senguttuvan / Chera Senguttuvan**;
- **Ilaveyini**;
- **Peruncheral Irumporai**, including the source epithet identifying him as the one who destroyed **Thagadoor**;
- **Thirumudikkari**, **Malaiyaman**, **Thirukovalur**, and **Karur**;
- the existing **Adiyaman** control was expanded to preserve both the short and full **Adiyaman Neduman Anji** forms;
- the existing **Perungadungko** control was expanded to preserve the full epithet **Perungadungko who sang the Paalai**.

## English page terminology repairs

GR9 changed **10 English page files**:

1. scan **299** — **Nakkirar → Nakkeerar**.
2. scan **300** — **Nakkirar → Nakkeerar**.
3. scan **302** — provenance **Nakkiranar → Nakkeerar**.
4. scan **303** — legacy diacritic form **Paripādal → Paripadal** throughout the page.
5. scan **304** — legacy diacritic form **Paripādal → Paripadal** throughout the page.
6. scan **309** — place form **Tagadur → Thagadoor**.
7. scan **323** — royal-name form **Karikala Valavan → Karikal Valavan**.
8. scan **328** — reconciled **Athiyaman → Adiyaman**, **Tagadur → Thagadoor**, **Palaikkali → Paalai Kali**, **Perunkadungo who sang of the Palai → Perungadungko who sang of the Paalai**, and **Kurunthogai → Kuruntokai**.
9. scan **330** — **Perunkadungo who sang the Palai → Perungadungko who sang the Paalai**.
10. scan **332** — provenance **Perunkadungo who sang the Palai → Perungadungko who sang the Paalai**.

No other page wording in scans **297–333** required glossary reconciliation.

## Exact change-set audit

Compare:

`a32318a5238d957278ccf2bdf433529cbdcd9425...86e7f468cc905730b21787ccb7dba005af745973`

Result:

- compare status — **ahead / non-divergent**
- commits — **3**
- changed files — **11**
- English page files — **10**
- control glossary — **1**
- canonical Tamil page changes — **0**
- page status changes — **0**
- unrelated control/report changes in the GR9 content commits — **0**

GR9 content commits:

1. `d2393b638a185101d2c39cc4bbcf4ff1c66bdeb1` — scans **299–304** terminology reconciliation.
2. `b548e48aac65c037237ba10b3ecdd8fdafc735e3` — scans **309–332** terminology reconciliation.
3. `86e7f468cc905730b21787ccb7dba005af745973` — `GLOSSARY.md` control expansion.

## Tamil archive limitation

GR9 is an English terminology/consistency gate. It does **not** promote canonical Tamil status and does **not** establish whole-volume word-for-word scan verification.

## Next activity

**English Glossary Reconciliation GR10 — scans 334–370.**

Continue the same context-aware reconciliation. Preserve English page statuses and change **0 canonical Tamil page files**.
