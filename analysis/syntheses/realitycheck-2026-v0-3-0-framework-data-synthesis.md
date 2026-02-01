# Synthesis Analysis: Reality Check v0.3.0 — Framework + Public Dataset + Rigor-v1 Adoption (Feb 2026)

> **Source IDs**: `lhl-2026-realitycheck-readme`, `lhl-2026-realitycheck-data-readme`, `lee-2026-minnesota-trump-immigration-conflict`, `stross-2025-the-pivot-1`
> **Analysis Date**: 2026-02-01
> **Analyst**: codex (gpt-5.2)
> **Rigor Level**: `[DRAFT]`
> **Type**: Cross-source synthesis

---

## Overview

This synthesis triangulates:

1. The Reality Check framework’s README (v0.3.0) as the “interface spec” for the system’s intended primitives and rigor tooling.
2. The public `realitycheck-data` README as the “front door” to a real dataset instance.
3. Two dataset examples to probe **rigor-v1 adoption**: a recent rigor-v1 analysis and an older pre–rigor-v1 analysis.

The practical question for “testing $check v0.3.0 on itself” is: *Can the current workflow produce new analyses that pass rigor-v1 checks while remaining compatible with older analyses, and can the dataset be kept internally consistent (DB, exports, indexes)?*

---

## Sources (This Synthesis)

| Source ID | Role | Date | What it contributes |
|-----------|------|------|---------------------|
| `lhl-2026-realitycheck-readme` | Framework spec | 2026-02-01 | Declared primitives: claims/sources/predictions/chains; v0.3.0 emphasis on rigor-v1 + inbox workflow |
| `lhl-2026-realitycheck-data-readme` | Dataset spec | 2026-02-01 | Status snapshot + navigation + repository layout for public KB |
| `lee-2026-minnesota-trump-immigration-conflict` | Rigor-v1 example | 2026-01-31 | Shows a recent analysis using Layer/Actor/Scope/Quantifier columns and Corrections & Updates |
| `stross-2025-the-pivot-1` | Legacy example | 2025 | Illustrates a non–rigor-v1 analysis that still exists in the dataset |

---

## Key Findings

1. **Framework claims are mostly “spec + code-backed”**: the v0.3.0 README’s core primitives map cleanly onto the DB schema + CLI surface (claims, sources, chains, predictions, evidence links, reasoning trails, semantic search).
2. **The dataset is internally consistent and queryable**: `realitycheck-data`’s snapshot counts match the live DB at HEAD as of 2026-02-01 (after this run’s imports).
3. **Rigor-v1 is “new default”, but legacy remains**: newer analyses (e.g., `lee-2026-minnesota-trump-immigration-conflict`) meet rigor-v1 requirements; older analyses (e.g., `stross-2025-the-pivot-1`) fail `--rigor` validation but remain valid under non-rigor validation.

---

## Rigor-v1 Adoption Snapshot

### What “rigor-v1” materially adds

Compared to earlier analysis templates, rigor-v1 requires:
- Explicit **Layer/Actor/Scope/Quantifier** columns in key claim tables and claim summaries.
- A **Corrections & Updates** section to record capture failures and post-publication changes.

### Dataset examples

| Example | Rigor-v1 outcome | What it suggests |
|---------|------------------|------------------|
| `lee-2026-minnesota-trump-immigration-conflict` | Passes | Recent analyses appear written to the current output contract |
| `stross-2025-the-pivot-1` | Fails (`--rigor`) | Historical analyses predate rigor-v1 and need manual upgrade (or should continue to be treated as “legacy-valid”) |

This supports the workflow principle that **`--rigor` should be opt-in strictness**, not retroactively enforced against the full historical corpus without a backfill effort.

---

## Operational Notes: Running a “Self-Check” Against Reality Check

This run added two new sources (framework README + dataset README) and registered new META claims describing the system:

- Source analyses:
  - `analysis/sources/lhl-2026-realitycheck-readme.md`
  - `analysis/sources/lhl-2026-realitycheck-data-readme.md`
- Imported claim IDs:
  - Framework: META-2026-024..032
  - Dataset: META-2026-033..038

To keep DB integrity clean under v0.3.0 validation rules, the run also added:
- evidence links for each new high-credence/E2 claim (to satisfy “has backing” requirements)
- reasoning trails for each new claim (to satisfy provenance requirements)

---

## Open Issues / Follow-Ups

1. **Clarify which command owns `--rigor`**: The analysis-file validator (`analysis_validator.py`) clearly implements `--rigor` checks; DB validation (`rc-validate`) is oriented around referential integrity and high-credence provenance warnings. Documentation should be explicit about which “validator” is being invoked in workflows.
2. **Legacy backfill strategy**: Decide whether to:
   - keep legacy analyses indefinitely as “WARN-only” under default validation, or
   - backfill selected legacy analyses to rigor-v1 (starting with high-impact sources and/or those feeding chains/syntheses).

---

## Recommendations

- Treat **rigor-v1** as the default expectation for *new* analyses going forward.
- Keep **legacy compatibility** for historical analyses, with explicit tooling support:
  - default validation: allow legacy
  - `--rigor` validation: enforce rigor-v1 for new work or for targeted backfills
- Prioritize backfill for:
  - sources that anchor chains, or
  - sources supporting high-credence claims without provenance

