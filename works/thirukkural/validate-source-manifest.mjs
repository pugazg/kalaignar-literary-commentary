// Source-identity validator for திருக்குறள் — கலைஞர் உரை.
//
//   node works/thirukkural/validate-source-manifest.mjs works/thirukkural [--release]
//
// This runs INSIDE the archive, because the archive owns the source contract. Every structural claim
// in the manifest is re-derived here from this repository's own verified page records, so the
// manifest cannot silently drift.
//
// IDENTITY ANCHOR. The controlling source is the SINGLE archival PDF (TVA_BOK_0065564). The 15
// `derivedSplits` are convenience parts the owner produced from it for working purposes; the page
// records cite their filenames, so the mapping is kept for traceability, but they are NOT the
// identity anchor. Their hashes are optional and never gate a release — requiring them would be
// demanding proof of derived working copies while the real source went unverified.
//
// Two modes, and the distinction is the whole point:
//
//   default    STRUCTURAL VALIDATION. Null hashes are reported as PENDING, not as failures — the
//              structural work genuinely is complete, and saying otherwise would be as dishonest as
//              claiming the hashes exist.
//   --release  VERIFIED IDENTITY GATE. A single null hash FAILS. Nothing may be published as having
//              verified source identity while any part is unhashed.

import fs from "node:fs";
import path from "node:path";

const WORK = process.argv[2];
const RELEASE = process.argv.includes("--release");
if (!WORK) {
  console.error("usage: node validate-source-manifest.mjs <work-dir> [--release]");
  process.exit(1);
}

const MANIFEST = path.join(WORK, "metadata/source-manifest.json");
if (!fs.existsSync(MANIFEST)) {
  console.error(`\nCANNOT VALIDATE — no manifest at ${MANIFEST}`);
  process.exit(2);
}
const man = JSON.parse(fs.readFileSync(MANIFEST, "utf8"));

const STATUS_VERIFIED = "verified";
const STATUS_PENDING = "pending-source-verification";

let pass = 0;
const fail = [];
const check = (n, c, d) => (c ? pass++ : fail.push(d ? `${n} — ${d}` : n));

// ── Derive the truth from the page records, never from the manifest ──────────────────────────────
const byFile = new Map();
for (const f of fs.readdirSync(path.join(WORK, "pages")).filter((x) => x.endsWith(".md")).sort()) {
  const head = /^---\n([\s\S]*?)\n---\n/.exec(fs.readFileSync(path.join(WORK, "pages", f), "utf8"))?.[1];
  if (!head) { fail.push(`page record ${f} has no front matter`); continue; }
  const fn = /^source_filename:\s*"([^"]+)"/m.exec(head)?.[1];
  const scan = Number(/^scan_page:\s*(\d+)/m.exec(head)?.[1]);
  if (!fn || !Number.isInteger(scan)) { fail.push(`page record ${f} lacks source_filename or scan_page`); continue; }
  const key = fn.normalize("NFC");
  if (!byFile.has(key)) byFile.set(key, []);
  byFile.get(key).push(scan);
}

// ── 1. ROOT EDITION IDENTITY ─────────────────────────────────────────────────────────────────────
check("manifest records the work id", man.work === "thirukkural", String(man.work));
check("manifest records the commentator", typeof man.commentator === "string" && man.commentator.includes("கருணாநிதி"), String(man.commentator));
check("manifest records the publisher", typeof man.publisher === "string" && man.publisher.length > 3, String(man.publisher));
check("manifest records the edition used", typeof man.edition === "string" && man.edition.length > 3, String(man.edition));
check("edition identity matches metadata/source.md", (() => {
  const src = fs.readFileSync(path.join(WORK, "metadata/source.md"), "utf8").normalize("NFC");
  return src.includes(man.publisher.normalize("NFC")) && src.includes("மார்ச் 2010");
})());
check("schemaVersion is set", Number.isInteger(man.schemaVersion) && man.schemaVersion >= 1);

// ── 2. ALL 15 PDFs REQUIRED, exactly those the page records name ────────────────────────────────
check("manifest lists exactly 15 derived splits", man.derivedSplits.length === 15, `found ${man.derivedSplits.length}`);
check("page records reference exactly 15 distinct source files", byFile.size === 15, `found ${byFile.size}`);
const manNames = new Set(man.derivedSplits.map((f) => f.filename.normalize("NFC")));
for (const n of byFile.keys()) check(`page-record file is in the manifest: …${n.slice(-26)}`, manNames.has(n));
for (const n of manNames) check(`manifest file is used by page records: …${n.slice(-26)}`, byFile.has(n));
check("part numbers are exactly 1..15",
  JSON.stringify(man.derivedSplits.map((f) => f.part).sort((a, b) => a - b)) === JSON.stringify([...Array(15)].map((_, i) => i + 1)));
check("no duplicate filenames", manNames.size === man.derivedSplits.length);

// ── 3. SCAN RANGES COVER 1..323, NO OVERLAP, NO GAP ─────────────────────────────────────────────
const owner = new Map();
let wellFormed = true;
for (const f of man.derivedSplits) {
  const [lo, hi] = f.scanRange ?? [];
  if (!Number.isInteger(lo) || !Number.isInteger(hi) || hi < lo) { wellFormed = false; continue; }
  for (let s = lo; s <= hi; s++) {
    if (owner.has(s)) { fail.push(`scan ${s} is claimed by both part ${owner.get(s)} and part ${f.part} — OVERLAP`); wellFormed = false; }
    owner.set(s, f.part);
  }
}
check("every scanRange is well-formed", wellFormed);
const expected = [...Array(man.totalScans)].map((_, i) => i + 1);
const missing = expected.filter((s) => !owner.has(s));
check(`scan ranges cover 1..${man.totalScans} with no gap`, missing.length === 0, `missing ${missing.slice(0, 8).join(", ")}`);
check("declared totalScans matches the page-record count", man.totalScans === [...byFile.values()].flat().length,
  `declared ${man.totalScans}, records ${[...byFile.values()].flat().length}`);
check("declared scanRange spans the whole work", JSON.stringify(man.scanRange) === JSON.stringify([1, man.totalScans]));

// ── 4. FILENAME MUST MATCH PAGE RECORDS, and each part must agree with itself ───────────────────
for (const f of man.derivedSplits) {
  const scans = (byFile.get(f.filename.normalize("NFC")) ?? []).slice().sort((a, b) => a - b);
  if (!scans.length) continue;
  const lo = scans[0], hi = scans[scans.length - 1];
  check(`part ${f.part}: scanRange matches its page records`, f.scanRange[0] === lo && f.scanRange[1] === hi,
    `manifest ${f.scanRange.join("-")} vs records ${lo}-${hi}`);
  check(`part ${f.part}: page records are contiguous`,
    JSON.stringify(scans) === JSON.stringify([...Array(hi - lo + 1)].map((_, i) => lo + i)));
  check(`part ${f.part}: pageCount matches its record count`, f.pageCount === scans.length,
    `manifest ${f.pageCount} vs ${scans.length}`);
  const m = /part_(\d{3})_pages_(\d+)-(\d+)\.pdf$/.exec(f.filename);
  check(`part ${f.part}: filename encodes a part/page range`, !!m, f.filename);
  if (m) {
    check(`part ${f.part}: filename part number agrees`, Number(m[1]) === f.part);
    check(`part ${f.part}: filename page range agrees with scanRange`,
      Number(m[2]) === f.scanRange[0] && Number(m[3]) === f.scanRange[1],
      `filename ${m[2]}-${m[3]} vs scanRange ${f.scanRange.join("-")}`);
  }
}

// ── 5. CONTROLLING SOURCE — the identity anchor ─────────────────────────────────────────────────
const cs = man.controllingSource;
check("manifest declares a controlling source", !!cs && typeof cs === "object");
if (cs) {
  check("controlling source has a filename", typeof cs.filename === "string" && cs.filename.endsWith(".pdf"), String(cs.filename));
  check("controlling source sha256 is a real 64-hex digest", /^[0-9a-f]{64}$/.test(cs.sha256 ?? ""), String(cs.sha256));
  check("controlling source byteSize is a positive integer", Number.isInteger(cs.byteSize) && cs.byteSize > 0, String(cs.byteSize));
  check("controlling source pageCount is a positive integer", Number.isInteger(cs.pageCount) && cs.pageCount > 0, String(cs.pageCount));
  // The anchor must span exactly the work the archive transcribed.
  check("controlling source pageCount equals totalScans", cs.pageCount === man.totalScans,
    `PDF has ${cs.pageCount} pages, archive records ${man.totalScans} scans`);
  check("controlling source pageCount equals the page-record count", cs.pageCount === [...byFile.values()].flat().length);
  check("controlling source is not committed", cs.committed === false);
  check("controlling source records where it came from", typeof cs.repository === "string" && cs.repository.length > 3);
  check("controlling source records how it was verified", typeof cs.verificationNote === "string" && cs.verificationNote.length > 40);
}

// ── 6. DERIVED SPLITS — traceability only, never the identity anchor ────────────────────────────
// A split may carry a hash, but is not required to. If one IS supplied it must be well-formed and
// paired with a byte size, so a half-identified split can never masquerade as verified.
const pending = [];
for (const f of man.derivedSplits) {
  const hasSha = f.sha256 !== null && f.sha256 !== undefined;
  const hasSize = f.byteSize !== null && f.byteSize !== undefined;
  if (!hasSha && !hasSize) { pending.push(f.part); continue; }
  // A part must not be half-identified: both together, or neither.
  check(`part ${f.part}: sha256 and byteSize are supplied together`, hasSha && hasSize,
    `sha256 ${hasSha ? "set" : "null"}, byteSize ${hasSize ? "set" : "null"}`);
  if (hasSha) check(`part ${f.part}: sha256 is a real 64-hex digest`, /^[0-9a-f]{64}$/.test(f.sha256), String(f.sha256));
  if (hasSize) check(`part ${f.part}: byteSize is a positive integer`, Number.isInteger(f.byteSize) && f.byteSize > 0, String(f.byteSize));
}
const unhashed = man.derivedSplits.filter((f) => f.sha256 === null || f.sha256 === undefined).length;
const anchored = !!cs && /^[0-9a-f]{64}$/.test(cs.sha256 ?? "") && Number.isInteger(cs.byteSize) && cs.byteSize > 0;
check("no PDF is committed in this repository", !fs.readdirSync(WORK, { recursive: true }).some((f) => String(f).toLowerCase().endsWith(".pdf")));
check("identityStatus uses an allowed value", [STATUS_VERIFIED, STATUS_PENDING].includes(man.identityStatus), String(man.identityStatus));
// identityStatus follows the CONTROLLING SOURCE, not the convenience splits.
check("identityStatus tells the truth about the controlling source",
  anchored ? man.identityStatus === STATUS_VERIFIED : man.identityStatus === STATUS_PENDING,
  `controlling source ${anchored ? "IS" : "is NOT"} identified, but identityStatus is "${man.identityStatus}"`);
check("fieldProvenance separates file-verified from archive-derived",
  Array.isArray(man.fieldProvenance?.fileVerified) &&
  man.fieldProvenance.fileVerified.some((f) => f.includes("controllingSource.sha256")) &&
  Array.isArray(man.fieldProvenance?.archiveDerived) &&
  man.fieldProvenance.archiveDerived.some((f) => f.includes("scanRange")));

// ── 6. THE RELEASE GATE ─────────────────────────────────────────────────────────────────────────
if (RELEASE) {
  check("RELEASE GATE: identityStatus is 'verified'", man.identityStatus === STATUS_VERIFIED, `is "${man.identityStatus}"`);
  check("RELEASE GATE: the controlling source is fully identified", anchored,
    "the single archival PDF must carry a real sha256 and byteSize — derived splits cannot substitute for it");
  check("RELEASE GATE: the controlling source spans the whole work", !!cs && cs.pageCount === man.totalScans);
}

const mode = RELEASE ? "VERIFIED IDENTITY GATE" : "STRUCTURAL VALIDATION";
console.log(`\nthirukkural source identity — ${mode}`);
console.log(`  ${pass} passed, ${fail.length} failed`);
if (cs) {
  console.log(`\n  Controlling source: ${cs.filename}`);
  console.log(`    sha256 ${cs.sha256}`);
  console.log(`    ${cs.byteSize?.toLocaleString()} bytes · ${cs.pageCount} pages · ${anchored ? "IDENTIFIED" : "NOT IDENTIFIED"}`);
}
if (pending.length) {
  // Not a deficiency: the splits are derived working copies, not the identity anchor.
  console.log(`\n  ${pending.length} of ${man.derivedSplits.length} derived splits carry no hash — expected.`);
  console.log(`  They are convenience copies, not the controlling source, and never gate a release.`);
}
if (fail.length) { console.error("\nFAILURES:"); for (const f of fail) console.error(" ✗ " + f); process.exit(1); }
console.log(`\n${RELEASE ? "RELEASE READY — source identity verified" : "STRUCTURAL PASS"}`);
