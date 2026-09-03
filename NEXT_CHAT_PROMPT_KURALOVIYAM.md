# Next Chat Prompt — குறளோவியம் archival project

Continue the Kalaignar Literary Commentary archival project directly in:

`pugazg/kalaignar-literary-commentary`

Branch: `main`

Active work: `works/kuraloviyam/`

Current controlling split source:

`TVA_BOK_0065733_குறளோவியம்_part_001_pages_1-111.pdf`

## LIVE MAIN IS AUTHORITATIVE

Fetch live `main` first and preserve the newest durable state. Do not reset or repeat completed work because this prompt contains an older checkpoint.

## Mandatory startup

Before any repository change, read completely:

1. `LITERARY_COMMENTARY_PROCESSING_GUIDE.md`
2. `KURALOVIYAM_ARCHIVAL_GUIDELINES.md`
3. root `HANDOVER.md`
4. this `NEXT_CHAT_PROMPT_KURALOVIYAM.md`
5. `works/kuraloviyam/README.md`
6. `works/kuraloviyam/SOURCE_INTAKE_PART_001.md`
7. `works/kuraloviyam/metadata/source.md`
8. `works/kuraloviyam/metadata/transcription-policy.md`
9. `works/kuraloviyam/indexes/page-map.md`

Then inspect the actual supplied source scans before writing.

## Source identity

The user reports the complete original Kuraloviyam PDF as **666 physical pages**, manually split into **six parts of 111 pages** because the original exceeds the upload limit.

Canonical overall scan mapping:

- Part 001: 1–111
- Part 002: 112–222
- Part 003: 223–333
- Part 004: 334–444
- Part 005: 445–555
- Part 006: 556–666

Repository `scan_page` never restarts for a split PDF.

Part 001 has no usable parsed text layer; the rendered source scan is controlling.

## Completed state

Part 001 source intake is complete:

- local page count: **111/111**;
- scans 1–3: cover/title/publication matter;
- scans 4–17: front matter;
- scan 18: main body begins at printed page 1, heading `பேராசிரியர்`;
- scan 111: printed page 94.

Part 001 Pass 1 is complete continuously through **overall scan 60**:

- scans **1–3** — cover / title-publisher / edition-imprint;
- scans **4–8 / printed iii–vii** — `முகப்புரை`;
- scans **9–12 / printed viii–xi** — `மதிப்புரை` through its conclusion;
- scans **13–15 / printed xii–xiv** — handwritten/facsimile prefaces; intentionally `partial` where handwriting cannot safely be established word-for-word;
- scan **16 / printed xv** — first-edition photograph and commemorative note;
- scan **17 / printed xvi** — `ஆறாம் பதிப்பின் பதிப்புரை`;
- scans **18–20 / printed 1–3** — `பேராசிரியர்`;
- scan **21 / printed 4** — `மகா வித்துவான் தண்டபாணி தேசிகர்`;
- scans **22–23 / printed 5–6** — `டாக்டர் வ.சுப.மாணிக்கம்`;
- scan **24 / printed 7** — `மதுரை யாதவர் கல்லூரி முதல்வர் தமிழ்க்குடிமகன்`;
- scan **25 / printed 8** — `காசி ஆனந்தன்`;
- scans **26–27 / printed 9–10** — `ஆட்சிமொழிக் காவலர் இராமலிங்கனார்`;
- scan **28 / printed 11** — `ஆசிரியர் சாவி`;
- scan **29 / printed 12** — `டாக்டர் மெ.சுந்தரம்`;
- scan **30 / printed 13** — `டாக்டர் மா.நன்னன்`;
- scan **31 / printed 14** — `கலைஞர் ஏற்புரை`;
- scan **32** — `கலைஞரின் குறளோவியம்` section-title leaf; no printed page number claimed;
- scan **33 / printed 16** — blank source-side page with reverse-side show-through only;
- scans **34–40 / printed 17–23** — opening illustrated/body sequence of `கலைஞரின் குறளோவியம்`;
- scans **41–42 / printed 24–25** — education/rebirth and `மெய்யுணர்தல்` discussion;
- scans **43–44 / printed 26–27** — lover/beloved gaze vignette;
- scans **45–47 / printed 28–30** — boastful-youth / promised-feats vignette;
- scans **48–49 / printed 31–32** — heart/dream vignette;
- scans **50–51 / printed 33–34** — palanquin vignette and Valluvar's correction, ending with `அறத்தாறு இதுவென வேண்டா சிவிகை...`;
- scans **52–53 / printed 35–36** — Ilango/Chenguttuvan renunciation vignette;
- scans **54–55 / printed 37–38** — moon/maiden and beloved-shoulder vignette;
- scans **56–57 / printed 39–40** — Valluvar/student discussion of sword-like and kin-like enemies;
- scans **58–59 / printed 41–42** — interpretation of `தெய்வந் தொழாஅள்...` and rain imagery;
- scan **60 / printed 43** — martial-history vignette begins and continues into scan 61.

Exactly **60 page-aligned records** now exist continuously for scans 1–60. Pass-1 printed-text records remain `needs-review` / `visual_fidelity: needs-review`; scans 13–15 are source-limited `partial` and must not be silently reconstructed.

Latest page-batch audit:

`6b78e804788c22f292ead41bbcfd9a9c4c70cdfa` → `c49f14637143ee40862b295d8888619a5bd95345`

The comparison confirmed **10 sequential page commits** adding exactly scans 51–60 before documentation synchronization.

## Exact next activity

If live `main` has not advanced beyond this frontier:

1. continue **Part 001 Pass 1**;
2. process **overall scans 61–70**;
3. create exactly one Markdown record per physical scan under `works/kuraloviyam/pages/`;
4. continue directly from the martial-history vignette at printed page 43 into the next source pages and preserve physical-page continuity;
5. transcribe only source-supported visible text;
6. preserve source-supported illustration/text relationships and printed pagination;
7. distinguish printed prose from signatures, handwriting, stamps, photographs and illustrations;
8. use overall `scan_page`, `part: 1`, and local `part_page`;
9. normally leave new records `needs-review` / `visual_fidelity: needs-review`;
10. do not replace printed Kural or quoted wording from memory/web sources;
11. audit the changed-file set, then record the next frontier.

Do not reopen scans 1–60 merely for stylistic harmonization during Pass 1. Do not jump to textual verification, visual verification, part audit or English translation before Pass 1 capture for the relevant source unit is complete.
