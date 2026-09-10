# குறளோவியம் — Transcription Policy

## Authority

The rendered scan is the lexical, structural and physical-page authority.

Parts 001–003 have no usable parsed text layer. Do not treat OCR, inferred text or model memory as source text.

## Pass 1

Pass 1 is physical capture/transcription only.

For each scan:

- create exactly one page record;
- use overall `scan_page` numbering across 1–666;
- record `part` and local `part_page`;
- record printed pagination only when source-supported;
- transcribe visible printed text without normalization;
- preserve obvious paragraph, dialogue, verse and heading structure;
- record illustrations/photos/handwriting/stamps separately from printed prose;
- use factual `visual_notes` when useful;
- normally set `status: "needs-review"` and `visual_fidelity: "needs-review"`.

Do not perform a hidden verification pass while transcribing.

## Kural text

Any quoted Kural must be copied from this edition's scan. Do not import a canonical or memorized reading.

Preserve:

- Kural line breaks;
- chapter/`அதிகாரம்` labels and numbers;
- printed Kural/song-number references;
- quotation punctuation and separators.

## Prose

Preserve source-supported paragraph boundaries and dialogue/speaker presentation. Markdown wrapping may differ, but paragraph order may not.

## Non-text and visual material

Illustrations, photographs and decorative artwork are not transcribed as prose. Describe them factually where they matter to page identity or text relationship.

Handwriting/signatures/library marks are separate from printed text. If handwriting is unclear, do not guess it.

## Later gates

`verified` is unavailable until textual verification, independent lexical-fidelity verification, meaningful visual-text verification and the Part audit have closed, followed by the dedicated final metadata/status synchronization.

A 111-page Part becomes archival-ready only after its audit, final metadata/status synchronization and documentation synchronization have all closed and the separate Tamil archival-ready checkpoint passes.