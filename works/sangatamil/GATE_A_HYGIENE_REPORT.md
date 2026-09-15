# Sangath Tamil — Gate A Source Bundle / Repository Hygiene

## Decision

**GATE A — COMPLETE / PASS.**

## Source bundle

Controlling source:

`TVA_BOK_0042551_சங்கத்_தமிழ்.pdf`

Physical boundary:

- scans **1–497**;
- scan **497** — back cover.

User-supplied lexical scaffold:

- `File1.md` … `File10.md`;
- complete sequence reaches the final block covering Book Pages **414–484 / PDF scans 426–497**.

## Pre-cleanup repository inventory

At Gate-A start:

- Markdown files under `works/sangatamil/pages/` — **511**;
- unique scan prefixes — **497**;
- missing scan prefixes — **0**;
- duplicate aliases — **14**, affecting scans **61–74**.

The duplicates came from overlapping historical capture/reconciliation paths. Gate A preserved the newest user-policy-compliant record and removed only the stale alias.

## Duplicate alias cleanup

Removed stale aliases for:

- scans **61–64** — older `oorin-perumai-unarthinal...` aliases;
- scans **65–69** — older `vaanin-maraintha...` aliases;
- scan **70** — older pre-lock `oru-pothu...` alias, preserving the later Gemini-lock record;
- scans **71–74** — older direct-transcription `oru-vaathu...` aliases, preserving the newer Gemini-scaffold structural records.

No canonical scan was deleted.

## Post-cleanup audit

Live repository after cleanup:

- page files — **497**;
- unique scan prefixes — **497**;
- duplicate scan aliases — **0**;
- missing scans — **0**.

Therefore the physical page layer now satisfies:

**497/497 physical scans → exactly one canonical page record each.**

## Remaining known structural state

- existing section READMEs — **9** only;
- whole-volume section reconstruction is therefore still incomplete;
- source-citation register is also not yet whole-volume complete.

Those are later gates and were intentionally not mixed into Gate A.

## Closure

**Gate A CLOSED / PASS.**

Exact next gate:

**Gate B — Gemini-locked structural fidelity, scans 1–25.**

Rules remain:

- Gemini words are locked;
- PDF controls structure/presentation;
- no silent lexical source correction;
- batch size normally **25 scans**.
