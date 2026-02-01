# Source Analysis: Reality Check Knowledge Base (README)

> **Claim types**: `[F]` fact, `[T]` theory, `[H]` hypothesis, `[P]` prediction, `[A]` assumption, `[C]` counterfactual, `[S]` speculation, `[X]` contradiction
> **Evidence**: **E1** systematic review/meta-analysis; **E2** peer-reviewed/official stats/law/code+tests; **E3** expert consensus/preprint; **E4** credible journalism/industry; **E5** opinion/anecdote; **E6** unsupported/speculative

## Metadata

| Field | Value |
|-------|-------|
| **Source ID** | `lhl-2026-realitycheck-data-readme` |
| **Title** | Reality Check Knowledge Base |
| **Author(s)** | Leonard Lin (repo maintainer) |
| **Date** | 2026-02-01 |
| **Type** | KNOWLEDGE |
| **URL** | https://raw.githubusercontent.com/lhl/realitycheck-data/main/README.md |
| **Reliability** | 0.80 |
| **Rigor Level** | [REVIEWED] |
| **Bias Notes** | Self-authored dataset README; status metrics appear derived from the underlying database and are likely accurate at time of commit, but will drift as the dataset updates. |

**Primary capture note**: Captured via GitHub raw view; no paywall/JS gating observed.

**Claims YAML**: [`analysis/sources/lhl-2026-realitycheck-data-readme.yaml`](lhl-2026-realitycheck-data-readme.yaml)

## Stage 1: Descriptive Analysis

### Core Thesis
The `realitycheck-data` repository is presented as a public, DB-backed knowledge base built using the Reality Check framework, containing a growing set of analyzed sources, extracted claims, predictions, and syntheses across multiple domains.

### Summary (Neutral)
The README provides a “Current Status” snapshot (counts of claims, sources, chains, predictions) and then offers navigation links to indexes (claims statistics, sources index, predictions dashboard, YAML exports, and a meta-analysis document). It includes tables indexing syntheses and source analyses, and it documents the repository’s directory structure (database under `data/`, analysis outputs under `analysis/`, prediction tracking under `tracking/`, and staging/filing under `inbox/` + `reference/`).

### Key Claims

| # | Claim | Claim ID | Layer | Actor | Scope | Quantifier | Type | Domain | Evid | Credence | Verified? | Falsifiable By |
|---|-------|----------|-------|-------|-------|------------|------|--------|------|----------:|-----------|----------------|
| 1 | `realitycheck-data` is a unified knowledge base built with the Reality Check framework | META-2026-033 | PRACTICED | OTHER:realitycheck-data repo | who=maintainers; where=Git repo; when=2026; predicate=uses Reality Check framework | N/A | [F] | META | E2 | 0.85 | ? | Repo lacks Reality Check project config / DB / expected structure |
| 2 | At time of the README, the DB contains 385 claims, 107 sources, 4 argument chains, and 26 predictions tracked | META-2026-034 | PRACTICED | OTHER:realitycheck-data repo | who=maintainers; where=db; when=2026-02-01; predicate=status counts | N/A | [F] | META | E2 | 0.90 | ? | DB stats materially differ from the README snapshot (at the referenced commit) |
| 3 | The repo provides navigation to source index, predictions dashboard, claim registry export, and source registry export | META-2026-035 | PRACTICED | OTHER:realitycheck-data repo | who=users; where=repo; when=2026; predicate=has navigation/index files | N/A | [F] | META | E2 | 0.85 | ? | Referenced index files are missing or inconsistent with described roles |
| 4 | The repo contains individual source analyses and cross-source syntheses under `analysis/` | META-2026-036 | PRACTICED | OTHER:realitycheck-data repo | who=analysts; where=analysis/; when=2026; predicate=stores analyses+syntheses | N/A | [F] | META | E2 | 0.90 | ? | `analysis/sources` or `analysis/syntheses` absent / empty |
| 5 | `claims/registry.yaml` and `reference/sources.yaml` are YAML exports of the claim/source registries | META-2026-037 | PRACTICED | OTHER:realitycheck-data repo | who=users; where=repo; when=2026; process=export; predicate=YAML exports exist | N/A | [F] | META | E2 | 0.75 | ? | YAML files do not exist or are not derived from the underlying DB |
| 6 | The repository includes a LanceDB database at `data/realitycheck.lance/` and a staging+filing workflow via `inbox/` and `reference/` | META-2026-038 | PRACTICED | OTHER:realitycheck-data repo | who=analysts; where=repo; when=2026; process=storage+filing; predicate=db+inbox/reference structure | N/A | [F] | META | E2 | 0.85 | ? | Repo lacks `data/realitycheck.lance/` and/or `inbox/`+`reference/` structure |

### Argument Structure

```
[Want a public example of the Reality Check framework in use]
    | motivates
    v
[Maintain a dataset repo with DB + analyses + exports]
    | requires
    v
[Navigation indexes + stable structure]
    | enables
    v
[Reviewing/adding sources and claims over time]
```

### Theoretical Lineage
- **Reproducible research repositories**: treat analyses and their underlying claim registry as versioned artifacts.
- **Open knowledge base practice**: publishing structured claims + provenance as a public dataset for critique and reuse.

### Scope & Limitations
- This README is a snapshot and index; it is not itself an argument for any substantive worldview claims in the database.
- Status counts will drift quickly as new analyses are added; the README should be interpreted at the commit date.

## Stage 2: Evaluative Analysis

### Internal Coherence
The structure is coherent: a DB provides the source of truth; Markdown/YAML exports and indexes provide human navigation; analyses and syntheses accumulate over time.

### Key Factual Claims Verified

| Claim (paraphrased) | Crux? | Source Says | Actual | External Source | Status |
|---------------------|-------|-------------|--------|-----------------|--------|
| The DB contains 385 claims, 107 sources, 4 chains, 26 predictions | **Y** | Status table shows these counts | `rc-db stats` reports claims=385, sources=107, chains=4, predictions=26 on 2026-02-01 | local run: `REALITYCHECK_DATA=... rc-db stats` | ok |
| The repo contains analyses under `analysis/sources` and syntheses under `analysis/syntheses` | **Y** | Tables + tree show these folders | Both directories exist and contain multiple `.md` entries | local repo tree; GitHub repo | ok |
| The repo includes a LanceDB database at `data/realitycheck.lance/` | **Y** | Tree shows `data/realitycheck.lance/` | Directory exists and contains Lance table subdirectories | local repo tree | ok |
| The README’s navigation links point to real files (e.g., `tracking/predictions.md`) | N | Navigation section links | Referenced files exist in the repo | local repo tree | ok |
| YAML registries exist as exported artifacts | N | Links labeled “YAML export” | Files exist; this analysis does not re-derive them from DB | local repo tree | ? |

### Disconfirming Evidence Search

| Claim | Counterevidence Found | Alternative Explanation | Search Notes |
|-------|----------------------|-------------------------|--------------|
| Status counts remain correct over time | Counts are time-dependent and will change with each added analysis | README is intended as a snapshot and is updated periodically via scripts | Compared README counts to live DB stats at HEAD; they matched on 2026-02-01 |
| YAML exports are the “source of truth” | Framework workflow emphasizes LanceDB as source of truth (YAML is export/legacy) | README labels them as exports; readers might still treat them as authoritative | Looked for export tooling and framework guidance; treated YAML as convenience output |

### Corrections & Updates

| Item | URL | Published | Corrected/Updated | What Changed | Impacted Claim IDs | Action Taken |
|------|-----|-----------|-------------------|--------------|--------------------|-------------|
| N/A | N/A | 2026-02-01 | N/A | No corrections/updates observed in this pass (single README capture) | N/A | N/A |

### Internal Tensions / Self-Contradictions

| Tension | Parts in Conflict | Implication |
|--------|-------------------|-------------|
| “YAML registry” discoverability vs DB source of truth | README prominently links YAML registries; core tooling expects the DB as authoritative | Readers may update YAML manually unless clearly told it’s an export; could be mitigated via clearer labels and/or regeneration guidance |

### Persuasion Techniques

| Technique | Example from Source | Effect on Reader |
|----------|----------------------|------------------|
| Status snapshot | Counts of claims/sources/predictions | Conveys momentum and concreteness without requiring readers to inspect the DB |

### Unstated Assumptions

| Assumption | Claim ID | Critical? | Problematic? |
|------------|----------|-----------|--------------|
| Publishing a public claim database yields useful feedback and reuse | META-2026-033 | Y | ? |
| A DB + exports + indexes is the right tradeoff for public distribution | META-2026-034..META-2026-038 | Y | ? |

### Evidence Assessment
- Status counts are strong (directly queryable from the DB).
- Claims about “export” status are plausible but ideally verified by regeneration diffs (not done here).

### Credence Assessment
- **Overall credence**: 0.85
- **Reasoning**: Repository structure and DB counts are directly verifiable; the main uncertainty is interpretive (how readers treat YAML exports and how quickly snapshots drift).

## Stage 3: Dialectical Analysis

### Steelmanned Argument
A public dataset built on a strict analysis workflow makes epistemic work auditable: readers can see which sources were analyzed, which claims were extracted, what credence was assigned, and how evidence links and reasoning trails support that credence. Publishing both the DB and the human-readable artifacts makes the system usable by humans while remaining queryable by tools.

### Strongest Counterarguments
1. **Distribution friction**: Shipping a DB repo (vs just Markdown) increases size, tooling requirements, and chances of versioning pain.
2. **Privacy and security**: A public “inbox” workflow risks leaking unreviewed materials if not carefully managed.
3. **Maintenance burden**: Keeping indexes, exports, and the DB consistent requires scripts and discipline.

### Supporting Theories

| Theory/Framework | Source ID | How It Supports |
|------------------|-----------|-----------------|
| Open science / reproducible research | (general) | Versioned artifacts enable critique and improvement |

### Contradicting Theories

| Theory/Framework | Source ID | Point of Conflict |
|------------------|-----------|-------------------|
| “Publish just the narrative” | (general) | Suggests most users prefer curated posts over DB-style datasets |

### Synthesis Notes
The dataset README is a useful “front door” and appears consistent with the live DB at HEAD (as of 2026-02-01). Its main risk is user misunderstanding of YAML exports vs DB truth, which is mitigated when workflows emphasize LanceDB as authoritative.

### Claims to Cross-Reference
- Framework README: `lhl-2026-realitycheck-readme`
- Existing meta-analysis: `analysis/meta/framework-efficacy-greenland-test.md`

---

### Claim Summary

| ID | Type | Domain | Layer | Actor | Scope | Quantifier | Evidence | Credence | Claim |
|----|------|--------|-------|-------|-------|------------|----------|----------:|-------|
| META-2026-033 | [F] | META | PRACTICED | OTHER:realitycheck-data repo | who=maintainers; where=Git repo; when=2026; predicate=uses Reality Check framework | N/A | E2 | 0.85 | `realitycheck-data` is a unified knowledge base built with the Reality Check framework |
| META-2026-034 | [F] | META | PRACTICED | OTHER:realitycheck-data repo | who=maintainers; where=db; when=2026-02-01; predicate=status counts | N/A | E2 | 0.90 | At time of the README, the DB contains 385 claims, 107 sources, 4 argument chains, and 26 predictions tracked |
| META-2026-035 | [F] | META | PRACTICED | OTHER:realitycheck-data repo | who=users; where=repo; when=2026; predicate=has navigation/index files | N/A | E2 | 0.85 | The repo provides navigation to source index, predictions dashboard, claim registry export, and source registry export |
| META-2026-036 | [F] | META | PRACTICED | OTHER:realitycheck-data repo | who=analysts; where=analysis/; when=2026; predicate=stores analyses+syntheses | N/A | E2 | 0.90 | The repo contains individual source analyses and cross-source syntheses under `analysis/` |
| META-2026-037 | [F] | META | PRACTICED | OTHER:realitycheck-data repo | who=users; where=repo; when=2026; process=export; predicate=YAML exports exist | N/A | E2 | 0.75 | `claims/registry.yaml` and `reference/sources.yaml` are YAML exports of the claim/source registries |
| META-2026-038 | [F] | META | PRACTICED | OTHER:realitycheck-data repo | who=analysts; where=repo; when=2026; process=storage+filing; predicate=db+inbox/reference structure | N/A | E2 | 0.85 | The repository includes a LanceDB database at `data/realitycheck.lance/` and a staging+filing workflow via `inbox/` and `reference/` |

### Claims to Register

```yaml
claims:
  - id: "META-2026-033"
    text: "`realitycheck-data` is a unified knowledge base built with the Reality Check framework."
    type: "[F]"
    domain: "META"
    evidence_level: "E2"
    credence: 0.85
    operationalization: "Verify presence of .realitycheck.yaml project config and LanceDB tables; verify repo structure matches framework conventions."
    assumptions: ["Repo structure is generated/maintained via Reality Check tooling."]
    falsifiers: ["Repo lacks project config/DB or diverges materially from framework structure."]
    source_ids: ["lhl-2026-realitycheck-data-readme"]

  - id: "META-2026-034"
    text: "At the time of the README, the DB contains 385 claims, 107 sources, 4 argument chains, and 26 predictions tracked."
    type: "[F]"
    domain: "META"
    evidence_level: "E2"
    credence: 0.90
    operationalization: "Run rc-db stats against the referenced commit’s DB and compare to README snapshot."
    assumptions: ["The README snapshot corresponds to the DB state at the referenced commit."]
    falsifiers: ["DB stats at that commit differ materially from the README snapshot."]
    source_ids: ["lhl-2026-realitycheck-data-readme"]

  - id: "META-2026-035"
    text: "The repo provides navigation to a sources index, a predictions dashboard, and YAML exports of claim and source registries."
    type: "[F]"
    domain: "META"
    evidence_level: "E2"
    credence: 0.85
    operationalization: "Confirm linked files exist and their contents match the described role (index/dashboard/export)."
    assumptions: ["Linked files are maintained and updated alongside the DB."]
    falsifiers: ["Linked files are missing or do not correspond to the described artifact type."]
    source_ids: ["lhl-2026-realitycheck-data-readme"]

  - id: "META-2026-036"
    text: "The repo contains individual source analyses under `analysis/sources/` and cross-source syntheses under `analysis/syntheses/`."
    type: "[F]"
    domain: "META"
    evidence_level: "E2"
    credence: 0.90
    operationalization: "Confirm these directories exist and contain analysis documents; compare to README tables."
    assumptions: ["Analyses are kept in sync with the DB registrations."]
    falsifiers: ["Directories are missing/empty or not used for analysis artifacts."]
    source_ids: ["lhl-2026-realitycheck-data-readme"]

  - id: "META-2026-037"
    text: "`claims/registry.yaml` and `reference/sources.yaml` are YAML exports of the claim/source registries."
    type: "[F]"
    domain: "META"
    evidence_level: "E2"
    credence: 0.75
    operationalization: "Regenerate exports from the DB (rc-export yaml claims/sources) and diff for equivalence."
    assumptions: ["Exports are generated mechanically from the DB rather than edited by hand."]
    falsifiers: ["Exports differ materially from DB-derived exports or contain manual-only fields."]
    source_ids: ["lhl-2026-realitycheck-data-readme"]

  - id: "META-2026-038"
    text: "The repository includes a LanceDB database at `data/realitycheck.lance/` and a staging+filing workflow via `inbox/` and `reference/`."
    type: "[F]"
    domain: "META"
    evidence_level: "E2"
    credence: 0.85
    operationalization: "Confirm directories exist; confirm DB contains expected tables; confirm filing destinations exist under reference/."
    assumptions: ["In practice, analysts use inbox→reference filing alongside DB registration."]
    falsifiers: ["Repo lacks these directories or the workflow is not used/maintained."]
    source_ids: ["lhl-2026-realitycheck-data-readme"]
```

---

**Analysis Date**: 2026-02-01
**Analyst**: codex (gpt-5.2)
**Credence in Analysis**: 0.85

**Credence Reasoning**:
- Repo structure and DB counts were verified locally at HEAD.
- “Export” semantics for YAML registries were treated as plausible but not fully re-derived in this pass.

## Analysis Log

| Pass | Date | Tool | Model | Duration | Tokens | Cost | Notes |
|------|------|------|-------|----------|--------|------|-------|
| 1 | 2026-02-01 | codex | gpt-5.2 | ? | ? | ? | Initial 3-stage analysis + claim extraction |

