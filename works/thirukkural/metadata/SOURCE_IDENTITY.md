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

## Hierarchy

```
Controlling source PDF          ← the single archival identity anchor
        |
        +── Derived processing files   (15 convenience splits)
                |
                +── Page records       (323, one per scan)
                |
                +── Imported reading data
```

**The controlling archival identity is the single Tamil Digital Library PDF. The split PDFs are
derived processing files created for workflow convenience and are not independent archival identity
anchors.**

## The controlling source, and the 15 derived files

The identity anchor is a **single archival PDF**:

| | |
|---|---|
| Filename | `TVA_BOK_0065564_திருக்குறள்_கலைஞர்_உரை.pdf` |
| SHA-256 | `765d0c73bce13c71e2e595e38f5216a3551c4dc94a315a0e2264a1a2630c3c56` |
| Byte size | 712,210,007 |
| Pages | 323 |
| Repository | Tamil Digital Library — நூல் 65564 |
| Committed | no |

### Derived processing files

The **15 `part_NNN` PDFs are processing splits** the owner produced from that single file for
workflow convenience. In the manifest they appear under `derivedFiles`, each carrying
`"role": "processing-split"`.

They:

- exist **only** for processing convenience;
- are **not independent editions** and carry no separate archival identity;
- **do not require archival hashing** — they are reproducible from the controlling source;
- take their traceability from **filename + scan mapping**, because the 323 page records cite those
  filenames.

Their filenames are therefore required and are validated against the page records, but a missing
`sha256` on a derived file is expected and never gates a release. Requiring proof of derived working
copies while the real source went unverified would have been precisely backwards. The single file is
what a future reader can obtain and re-check.

## Page correspondence

```
PDF page N = archive scan N
```

This holds across the whole work: the file's 323 pages match the archive's 323 page records
one-to-one. It is recorded in the manifest under `pageCorrespondence` so that future importers and
validators inherit the fact instead of rediscovering it.

Page count alone would prove little, so content was checked at both boundaries.

**Beginning**

```
PDF page 34
Archive scan 34
Printed page 1
Kurals 1–5 with Kalaignar Urai
```

Running head `அறம் - பாயிரம் - வழிபாடு`, heading `1. வழிபாடு` — matching page record `0034` exactly.

**End**

```
PDF page 303
Archive scan 303
Printed page 270
Kurals 1326–1330
```

Running head `திருக்குறள் - கலைஞர் உரை`, the work ending at Kural 1330 — matching page record `0303`
exactly.

The validator re-checks each sample's `printedPage` against the archive's own record for that scan,
so a sample cannot drift from the page records it claims to corroborate.

## Verification level

`identityStatus` says *whether* identity is established. `identityVerification.level` says **how far
the verification actually went**, so a reviewer can tell at a glance what was and was not done.

| Level | Meaning |
|---|---|
| `recorded` | the values are written down but were never checked against the file |
| `file-verified` | SHA-256, byte size and page count were recomputed **from the controlling file** |
| `content-correspondence-verified` | file-verified, **and** the file's pages were matched to the archive's page records by printed content |

**This work is at `content-correspondence-verified`**, because verification included all four:

1. **source hash** — SHA-256 recomputed from the file
2. **byte size** — recomputed from the file
3. **page count** — 323, read from the file and equal to the archive's scan count
4. **page correspondence validation** — two boundary pages matched to their page records by content

### What this level does *not* claim

It claims a whole-file identity match plus page-level correspondence **at the verified samples**. It
does **not** claim that all 323 pages were individually re-read. The manifest says so in
`identityVerification.note`, and the level names exactly what was done — nothing more.

The release gate requires this strongest level: `recorded` and `file-verified` both fail it. The
validator also refuses a level that its own evidence does not support — claiming
`content-correspondence-verified` without recorded samples, or without listing
`page-correspondence-samples` among the methods, fails.

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

Identity is already recorded. The validator can re-check it **against the actual file**:

```bash
node works/thirukkural/validate-source-manifest.mjs --verify-file /path/to/TVA_BOK_0065564_திருக்குறள்_கலைஞர்_உரை.pdf --release
# expect: file content RE-VERIFIED against the supplied PDF
#         RELEASE READY — source identity verified
```

Without `--verify-file`, a recorded hash can only be checked for **shape**, never for correctness —
a plausible but wrong 64-hex string is indistinguishable from the right one. The report says so
explicitly rather than implying the value was checked:

```
recorded identity NOT re-checked against the file (pass --verify-file <pdf> to do so)
```

To confirm the values by hand:

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

## Optionally hashing the derived processing files

Not required, and not a release gate — they are reproducible derivatives, not archival anchors. If
you ever do record them, supply `sha256` **and** `byteSize` together; the validator rejects a
half-identified derived file, so one can never masquerade as verified.
Do not edit `filename`, `pageCount` or `scanRange`: those are archive-derived, and if one looks wrong
the page records are the thing to investigate, not the manifest.

## If a hash ever fails to match later

That is a finding, not a nuisance. It means the file in hand is not the file that was transcribed.
Do not update the manifest to match the new file. Stop, and establish which file is the controlling
source — the page records were verified against one specific set of bytes, and that relationship is
the whole point of recording identity.

The same applies if a re-render of PDF page N ever stops matching page record N. The correspondence
recorded above is a claim about *this* file, and it is meant to be falsifiable.
