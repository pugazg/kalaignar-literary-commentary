# Sangatamil — Maintained English Source-Check SC1 Report

**Status: COMPLETE / PASS**

- date: **2026-09-18**
- repository: `pugazg/kalaignar-literary-commentary`
- branch: `main`
- batch: **SC1**
- physical scans: **1–37**
- page-layer base: `b4ff1a8cb54c5b6db9da8921e73cc49fbe734d0a`
- page-layer endpoint: `6369adc94394ddc9c4a2917518d85fb9f614deea`

## Scope

SC1 compared the maintained-English page layer against the matching canonical Tamil records for scans **1–37**, paragraph-by-paragraph / block-by-block.

The review checked:

- omissions and additions;
- meaning drift;
- names and titles;
- dialogue and speaker attribution;
- quoted Sangam verse and fragments;
- source labels and provenance;
- visual / non-body page function;
- cross-page continuity.

No published Sangam English translation, web translation, external edition, or remembered conventional wording was imported.

Scan **8** remains the permanent description-only handwritten `முன்னுரை` exception. It was reviewed for page function and policy compliance, but its handwriting was **not** deciphered or reconstructed and its English status remains `source-limited`.

## SC1 result

Coverage — **37/37 scans reviewed**.

Page state after SC1:

- promoted `draft` → `source-checked` — **36**
- retained `source-limited` — **1** (scan 8)
- blocked — **0**

Cumulative maintained-English inventory after SC1:

- page records — **497/497**
- `draft` — **460**
- `source-checked` — **36**
- `source-limited` — **1**
- `editorial-reviewed` — **0**
- `release-ready` — **0**
- `blocked` — **0**

## Source-fidelity repairs

SC1 made source-fidelity wording repairs in **11 English page files**:

1. scan **13** — `தெவிட்டாத`: replaced “unfailing” with the source sense **“never cloys”**.
2. scan **19** — corrected the source-based transliteration of `பகன்றை` to **`paganrai`**.
3. scan **21** — removed a duplicated rendering around restored `காதலையும்` and realigned the `ஆக்கிக்கொண்டு` continuation without changing the canonical Tamil.
4. scan **25** — removed unsupported “marriage” from the rendering of `பஞ்சணை`; retained **“soft bed”**.
5. scan **28** — corrected `வெட்கம் துரத்த` from an implication of being driven onward to **shame pursuing them**.
6. scan **29** — corrected `சிங்க ஏறு` from “lion among bulls” to the source sense **“male lion”**.
7. scan **30** — repaired the closing quotation so `ஈன்மரோ` retains its birth / fate rhetorical sense instead of being silently dropped.
8. scan **33** — restored `பறவைகள்` as **“birds”**, not generic “beings”.
9. scan **34** — corrected `கொள்ளை இன்பம்`, `பின்னழகு`, and `தட்டிக் கொடுத்து` so the English preserves the intensity and physical action of the maintained Tamil.
10. scan **35** — preserved the canonical speaker attribution `என்றான்` as **“he said”** rather than silently regularizing the surrounding dialogue.
11. scan **36** — corrected `பதுமை` from “lotus” to **“doll”**.

These are English-layer fidelity repairs only. Canonical Tamil wording was not changed.

## Exact page-layer change-set audit

Compare:

`b4ff1a8cb54c5b6db9da8921e73cc49fbe734d0a...6369adc94394ddc9c4a2917518d85fb9f614deea`

Result:

- compare status — **ahead / non-divergent**
- commits — **9**
- changed files — **36**
- all changed files — English page records within scans **1–37**, excluding unchanged scan **8**
- canonical Tamil page changes — **0**
- non-English-page changes — **0**

SC1 page commits:

1. `04c344029da37020935884e1df38627fea60ab19` — scans **1–4**
2. `71ca854b6dddc1ee7b675ce8754cc728a0b8570a` — scans **5–9**, with scan **8** unchanged
3. `b0df917bd58f9429534f93e2a933071d6317727a` — scans **10–13**
4. `ae512b699bb0bea9b979ab09e7e9f427adceb267` — scans **14–17**
5. `62354261de26945d04e8a613af5af3174724d38c` — scans **18–21**
6. `8ddf219be241b5af9482f41d2709e4a6dd15d1a8` — scans **22–25**
7. `067c80d5174155c47aaff30fd1d09d0cfbb139cc` — scans **26–29**
8. `ca20bba9889f5cf338470ad1e0dece18d750d3d9` — scans **30–33**
9. `6369adc94394ddc9c4a2917518d85fb9f614deea` — scans **34–37**

## Tamil archive limitation

SC1 certifies English fidelity only against the maintained canonical Tamil records.

It does **not** promote the Tamil page statuses and does **not** establish whole-volume word-for-word scan verification. That claim remains **NOT MADE**.

## Next activity

**English Source-Check SC2 — scans 38–74.**

Continue the same paragraph-by-paragraph / block-by-block fidelity review. Do not begin glossary reconciliation until source-check closes through all **497** scans.
