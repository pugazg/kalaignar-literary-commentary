# Source identity — திருக்குறள்: கலைஞர் உரை

## Where source identity belongs

**The archive owns source identity. The application consumes it.**

This repository holds the controlling scans and the verified page records derived from them. It is
the only place that can answer *"which exact file was transcribed?"* — so it is the only place that
may **assert** the answer.

`pugazg/kalaignar-autobiography` (the Reading Room) does the opposite. It reads a **pinned commit**
of this repository, copies the recorded identity into its released provenance, and republishes it for
readers. It never computes, supplements or corrects that identity.

The reason is falsifiability, not tidiness. If the application recorded a checksum of its own, it
would be asserting a fact about a file it has never seen and cannot re-check — exactly the kind of
unfalsifiable claim this project exists to avoid. With identity held here, the chain is followable
end to end:

```
published page → app provenance → pinned archive commit → source-manifest.json → the original PDF
```

Every link is checkable, and the last link is checkable **only here**.

It also keeps a single writer. Two repositories recording the same checksum would eventually
disagree, and nothing would arbitrate. One authority, one copy, one direction of travel.

## Why the PDFs are not committed

The supplied scans stay outside Git, as with every other work in this project. Identity therefore
travels as **filename + SHA-256 + byte size + page count** rather than as bytes. That is what makes
`source-manifest.json` load-bearing: it is the only durable link between this repository and the
files it preserves.

## The controlling source, and the 15 splits

The identity anchor is a **single archival PDF**:

| | |
|---|---|
| Filename | `TVA_BOK_0065564_திருக்குறள்_கலைஞர்_உரை.pdf` |
| SHA-256 | `765d0c73bce13c71e2e595e38f5216a3551c4dc94a315a0e2264a1a2630c3c56` |
| Byte size | 712,210,007 |
| Pages | 323 |
| Repository | Tamil Digital Library — நூல் 65564 |
| Committed | no |

The **15 `part_NNN` PDFs are a convenience split** the owner produced from that file for working
purposes. They are *not* the controlling source. The 323 page records cite their filenames, so the
mapping is preserved here for traceability, but their hashes are optional and never gate a release.

Requiring hashes for derived working copies while the real source went unverified would have been
precisely backwards. The single file is what a future reader can obtain and re-check.

### How the correspondence was established

Page count alone would prove little, so content was checked at both boundaries:

- **PDF page 34** → running head `அறம் - பாயிரம் - வழிபாடு`, printed page `1`, heading `1. வழிபாடு`,
  Kurals 1–5 each followed by Kalaignar's urai — matching page record `0034` exactly.
- **PDF page 303** → running head `திருக்குறள் - கலைஞர் உரை`, printed page `270`, Kurals 1326–1330,
  ending at 1330 — matching page record `0303` exactly.

**PDF page N corresponds to archive scan N**, and the file's 323 pages match the archive's 323 page
records.

## `identityStatus`

Exactly two values are allowed:

| Value | Meaning |
|---|---|
| `pending-source-verification` | the controlling source has no SHA-256/byte size. File identity is **NOT** verified. |
| `verified` | the controlling source carries a real SHA-256 and byte size computed from the file itself. |

`identityStatus` follows the **controlling source only**. Unhashed derived splits do not make the
work pending — they are expected to be unhashed.

`sha256: null` and `byteSize: null` mean **NOT YET VERIFIED**. They do not mean *"absent and
acceptable"*, and they must never be read as *"this file has no checksum"*.

Fabricating, guessing, or back-filling these values from any other copy of the edition is
**prohibited**. A wrong checksum is far worse than a missing one: a missing one is honest, a wrong
one silently certifies the wrong file forever.

The validator enforces the correspondence in both directions — `identityStatus` may not say
`verified` while any hash is null, and may not say `pending-source-verification` once every hash is
present.

## Which fields need the PDFs, and which do not

| Field | Basis | Re-checkable without the PDF? |
|---|---|---|
| `derivedSplits[].filename` | the 323 verified page records | **yes** |
| `derivedSplits[].pageCount` | count of page records for that file | **yes** |
| `derivedSplits[].scanRange` | first/last `scan_page` for that file | **yes** |
| `controllingSource.sha256` | the archival PDF | no |
| `controllingSource.byteSize` | the archival PDF | no |
| `controllingSource.pageCount` | the archival PDF | no |

The archive-derived fields are re-derived on **every** validation run, so the manifest cannot
silently drift. The controlling source's identity anchors the whole work.

## How this is enforced

`works/thirukkural/validate-source-manifest.mjs` has two modes, and the distinction is the point.

**Default — structural validation:**

```bash
node works/thirukkural/validate-source-manifest.mjs works/thirukkural
```

Verifies root edition identity; that all 15 parts are present and named exactly as the page records
name them; that scan ranges tile 1–323 with no gap or overlap; that each part's `pageCount`,
`scanRange` and embedded filename range agree with its records; that any *present* hash is a real
64-hex digest and is accompanied by a byte size; and that `identityStatus` and `sourcePdfCommitted`
tell the truth. Null hashes are reported as **PENDING**, not as failures — the structural work
genuinely is complete, and failing it would be as dishonest as claiming the hashes exist.

**`--release` — verified identity gate:**

```bash
node works/thirukkural/validate-source-manifest.mjs works/thirukkural --release
```

A single null hash **fails**. Nothing may be published as having verified source identity while any
part is unhashed.

## Re-verifying the controlling source

Identity is already recorded. To re-confirm it against a copy of the file:

```bash
# macOS
shasum -a 256 TVA_BOK_0065564_திருக்குறள்_கலைஞர்_உரை.pdf
stat -f '%z' TVA_BOK_0065564_திருக்குறள்_கலைஞர்_உரை.pdf

# GNU/Linux
sha256sum TVA_BOK_0065564_திருக்குறள்_கலைஞர்_உரை.pdf
stat -c '%s' TVA_BOK_0065564_திருக்குறள்_கலைஞர்_உரை.pdf
```

Expected:

```
765d0c73bce13c71e2e595e38f5216a3551c4dc94a315a0e2264a1a2630c3c56
712210007
```

Then confirm the gate:

```bash
node works/thirukkural/validate-source-manifest.mjs works/thirukkural --release
# expect: RELEASE READY — source identity verified
```

## Optionally hashing the derived splits

Not required, and not a release gate. If you ever do record them, supply `sha256` **and** `byteSize`
together — the validator rejects a half-identified split, so one can never masquerade as verified.
Do not edit `filename`, `pageCount` or `scanRange`: those are archive-derived, and if one looks wrong
the page records are the thing to investigate, not the manifest.

## If a hash ever fails to match later

That is a finding, not a nuisance. It means the file in hand is not the file that was transcribed.
Do not update the manifest to match the new file. Stop, and establish which file is the controlling
source — the page records were verified against one specific set of bytes, and that relationship is
the whole point of recording identity.

The same applies if a re-render of PDF page N ever stops matching page record N. The correspondence
recorded above is a claim about *this* file, and it is meant to be falsifiable.
