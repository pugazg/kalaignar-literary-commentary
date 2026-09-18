# Sangatamil — Maintained English Glossary Reconciliation GR1 Report

**Status: COMPLETE / PASS**

- date: **2026-09-18**
- repository: `pugazg/kalaignar-literary-commentary`
- branch: `main`
- batch: **GR1**
- physical scans: **1–37**
- base: `f3bc58a661f4207de576044bf602731d1ed45b25`
- endpoint: `191f773fbd74160f20aae10958a58b4d1c6783dd`

## Scope

GR1 reconciled recurring maintained-English terminology across scans **1–37** after full source-check closure.

The gate reviewed recurring:

- names and proper names;
- Sangam anthology/work titles;
- classical literary categories;
- landscape terms;
- front-matter/source labels;
- repeated maintained-English section/title forms.

`GLOSSARY.md` was used as a context-aware editorial control, not as a mechanical substitution table. No published English Sangam translation, web translation, external edition or remembered conventional wording was imported.

Scan **8** remained the permanent description-only `source-limited` exception and was not reconstructed.

## GR1 result

Coverage — **37/37 scans reconciled**.

English page status state was deliberately unchanged:

- `source-checked` — **496**
- `source-limited` — **1** (scan 8)
- `draft` — **0**
- page status changes during GR1 — **0**

Cumulative glossary reconciliation after GR1 — **37/497**.

## Controlled glossary additions

GR1 expanded the glossary with source-evidenced controls for:

- front matter: `அணிந்துரை` → **Foreword**, `பதிப்புரை` → **Publisher's Note**;
- literary categories: **akam**, **puram**, and context-sensitive `களவு`;
- Sangam/work titles including **Tolkappiyam, Agathiyam, Ettuthogai, Pattuppattu, Pathinenkilkanakku, Paripadal, Purananuru, Pathitrupathu, Natrinai, Kuruntokai, Akananuru, Ainkurunuru, Kalithogai, Kurinjippattu, Kalavazhi Narpadu**;
- landscape terms **neydhal, marudham, kurinji, mullai, paalai**;
- recurring proper names including **Kapilar, Cheraman Kanaikkal Irumporai, Ammuvanar**;
- the publisher proper name **Rock Fort Publications (P) Ltd.**;
- the recurring short-epic title **One-Sided Love**.

The glossary also records that the source's `கணியன் பூங்குன்றன் / கணியன் பூங்குன்றனார்` honorific variation is preserved rather than mechanically flattened.

## English page terminology repairs

GR1 changed **6 English page files**:

1. scan **2** — `Rockfort` → **Rock Fort**.
2. scan **5** — `Rockfort Publications` → **Rock Fort Publications**.
3. scan **7** — `Rockfort Publications (P) Ltd.` → **Rock Fort Publications (P) Ltd.**
4. scan **11** — legacy `Kurunthogai` → controlled **Kuruntokai**.
5. scan **12** — legacy `Kurunthogai` → controlled **Kuruntokai**; recurring title `One-sided Love` → **One-Sided Love**.
6. scan **14** — `Rockfort Publications (P) Ltd` → **Rock Fort Publications (P) Ltd**.

The **Rock Fort** spacing is supported internally by the source's recurring publisher identity, including the explicit English `ROCK FORT Publications (P) Ltd.` form at the physical back cover. The **Kuruntokai** form is the maintained project form used elsewhere in the already source-checked English layer. No external terminology source was used.

## Exact change-set audit

Compare:

`f3bc58a661f4207de576044bf602731d1ed45b25...191f773fbd74160f20aae10958a58b4d1c6783dd`

Result:

- compare status — **ahead / non-divergent**
- commits — **1**
- changed files — **7**
- English page files — **6**
- control glossary — **1**
- canonical Tamil page changes — **0**
- page status changes — **0**
- unrelated control/report changes in the GR1 content commit — **0**

GR1 content commit:

- `191f773fbd74160f20aae10958a58b4d1c6783dd` — scans **1–37** terminology reconciliation + `GLOSSARY.md`.

## Tamil archive limitation

GR1 is an English terminology/consistency gate. It does **not** promote canonical Tamil status and does **not** establish whole-volume word-for-word scan verification.

## Next activity

**English Glossary Reconciliation GR2 — scans 38–74.**

Continue the same context-aware reconciliation. Preserve English page statuses and change **0 canonical Tamil page files**.
