# Section-Build Policy

## Non-destructive rule

The `sections/` tree is derived metadata/navigation only. It must never be treated as source authority over the audited page records.

## Source authority

For Tamil wording, scan mapping, Chapter/Kural metadata and source limitations, authority remains:

1. audited records under `../pages/`;
2. the controlling scan when a genuinely new fidelity issue requires reopening;
3. maintained English records only for the project-created English layer.

## Navigation-only Book/Iyal placement

Book/Iyal placement in this directory uses the conventional Thirukkural chapter-range schema as an explicit navigation aid. This is outside the literal Kuraloviyam contents transcription and is therefore labelled **derived navigation**.

Adhikaram labels themselves are taken only from source-evidenced project controls.

## No silent canonical repair

Do not:

- add a missing Chapter merely because another Thirukkural edition contains it;
- change a source Chapter number to a conventionally expected number;
- replace a source Tamil form with a normalized spelling;
- manufacture an entry-to-Chapter relation from memory.

The source-number conflict at Chapter 26 is intentionally retained.

## Entry-level target

The intended final hierarchy is:

**Book → Iyal → Adhikaram → contents entry**

The 300 source contents entries are already preserved under `04-contents/`. Entry-to-Adhikaram crosslinks should be added only after a direct audit of the entry's page span and its closing Chapter/Kural metadata.
