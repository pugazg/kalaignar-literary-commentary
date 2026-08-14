# திருக்குறள் — கலைஞர் உரை

கலைஞர் மு. கருணாநிதியின் **திருக்குறள் — கலைஞர் உரை** நூலை மூல ஸ்கேன்களை controlling source ஆகக் கொண்டு பக்கவாரியாக மின்னாக்கும் பகுதி.

## கிடைத்துள்ள மூலத் தொகுதிகள்

| Part | Source file | Local pages | Overall scans | நிலை |
|---|---|---:|---:|---|
| 001 | `திருக்குறள்_கலைஞர்_உரை_part_001_pages_1-20.pdf` | 20 | 1–20 | audited / archival-ready; scan 8 documented partial |
| 002 | `திருக்குறள்_கலைஞர்_உரை_part_002_pages_21-41.pdf` | 21 | 21–41 | audited / **ARCHIVAL-READY** |
| 003 | `திருக்குறள்_கலைஞர்_உரை_part_003_pages_42-62.pdf` | 21 | 42–62 | **14/21 records created; scans 42–55 needs-review** |

Part 003 local page 1 visibly carries printed page **9**, directly after Part 002 scan 41 / printed page **8**. The supplied Part 003 scan continues without a gap through printed page **29**.

## Edition metadata

Part 001-ல் தெரியும் edition information:

- முதற் பதிப்பு — **டிசம்பர் 2007**
- இரண்டாவது பதிப்பு — **மார்ச் 2010**
- Publisher — **பூம்புகார் பதிப்பகம், சென்னை**
- விலை — **ரூ. 180/-**

Parts 002–003 contain no new edition statement; publication metadata-க்கு Part 001 தான் ஆதாரம்.

## Part 001

- page records: **20 / 20**
- `verified`: **19**
- `partial`: **1** — scan 8 handwritten facsimile
- Audit: [`AUDIT_PART_001.md`](AUDIT_PART_001.md)
- Release decision: **ARCHIVAL-READY WITH ONE DOCUMENTED PARTIAL FACSIMILE**

## Part 002

- page records: **21 / 21**
- `verified`: **21 / 21**
- unresolved: **0**
- Audit: [`AUDIT_PART_002.md`](AUDIT_PART_002.md)
- Release decision: **ARCHIVAL-READY**

## Part 003 — current state

Part 003 contains **21 pages**, overall scans **42–62**, printed pages **9–29**, covering Kural **41–145**.

- page records: **14 / 21**
- `needs-review`: **14** — scans 42–55
- `not-started`: **7** — scans 56–62
- `verified`: **0**

### Structure

| Overall scan | உள்ளடக்கம் | நிலை |
|---:|---|---|
| 42–43 | `5. இல்வாழ்க்கை` — குறள் 41–50 + கலைஞர் உரை | first-pass complete; needs-review |
| 44–45 | `6. வாழ்க்கைத் துணைநலம்` — குறள் 51–60 + உரை | first-pass complete; needs-review |
| 46–47 | `7. மக்கட்பேறு` — குறள் 61–70 + உரை | first-pass complete; needs-review |
| 48–49 | `8. அன்புடைமை` — குறள் 71–80 + உரை | first-pass complete; needs-review |
| 50–51 | `9. விருந்தோம்பல்` — குறள் 81–90 + உரை | first-pass complete; needs-review |
| 52–53 | `10. இனியவை கூறல்` — குறள் 91–100 + உரை | first-pass complete; needs-review |
| 54–55 | `11. செய்ந்நன்றியறிதல்` — குறள் 101–110 + உரை | first-pass complete; needs-review |
| 56–57 | `12. நடுவு நிலைமை` — குறள் 111–120 | not-started |
| 58–59 | `13. அடக்கம் உடைமை` — குறள் 121–130 | not-started |
| 60–61 | `14. ஒழுக்கம் உடைமை` — குறள் 131–140 | not-started |
| 62 | `15. பிறனில் விழையாமை` — குறள் 141–145 | not-started |

The second Part 003 first-pass batch added scans 49–55, covering the completion of `அன்புடைமை`, all of `விருந்தோம்பல்`, all of `இனியவை கூறல்`, and all of `செய்ந்நன்றியறிதல்`.

## Part 003 first-pass rule

Every newly created Part 003 record uses:

- `status: "needs-review"`
- `transcription_method: "first-pass direct visual transcription from source scan; source scan remains authoritative"`
- `part: 3`
- explicit `part_page`
- overall scan / Part 003 local page / printed-page source marker

No Part 003 page will be promoted to `verified` until a separate source-comparison pass.

## Source-first rule

> **ஸ்கேன் தான் controlling source. Markdown பாதுகாப்பு அடுக்கு; corrected edition அல்ல.**

அமைதியாக modernize / normalize / reconstruct / internet-text substitution செய்யக்கூடாது. Kural wording, spacing, line breaks and Kalaignar commentary are preserved from this scan even where another edition may differ.

## அடுத்த செயல்

Finish the Part 003 first pass with **scans 56–62**:

1. scans 56–57 — `நடுவு நிலைமை`, குறள் 111–120;
2. scans 58–59 — `அடக்கம் உடைமை`, குறள் 121–130;
3. scans 60–61 — `ஒழுக்கம் உடைமை`, குறள் 131–140;
4. scan 62 — `பிறனில் விழையாமை`, குறள் 141–145.

After all scans 42–62 have first-pass records, run a separate Part 003 visual-verification cycle and then `AUDIT_PART_003.md`.

விரிவான page-level நிலை: [`indexes/page-map.md`](indexes/page-map.md).
