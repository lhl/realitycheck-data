# Source Analysis: Reality Check (README)

> **Claim types**: `[F]` fact, `[T]` theory, `[H]` hypothesis, `[P]` prediction, `[A]` assumption, `[C]` counterfactual, `[S]` speculation, `[X]` contradiction
> **Evidence**: **E1** systematic review/meta-analysis; **E2** peer-reviewed/official stats/law/code+tests; **E3** expert consensus/preprint; **E4** credible journalism/industry; **E5** opinion/anecdote; **E6** unsupported/speculative

## Metadata

| Field | Value |
|-------|-------|
| **Source ID** | `lhl-2026-realitycheck-readme` |
| **Title** | Reality Check |
| **Author(s)** | Leonard Lin (repo maintainer) |
| **Date** | 2026-02-01 |
| **Type** | KNOWLEDGE |
| **URL** | https://raw.githubusercontent.com/lhl/realitycheck/main/README.md |
| **Reliability** | 0.75 |
| **Rigor Level** | [REVIEWED] |
| **Bias Notes** | Self-authored project README; likely accurate about scope and shipped CLI surface area, but subject to promotional framing and omission of limitations. |

**Primary capture note**: Captured via GitHub raw view; no paywall/JS gating observed.

**Claims YAML**: [`analysis/sources/lhl-2026-realitycheck-readme.yaml`](lhl-2026-realitycheck-readme.yaml)

## Stage 1: Descriptive Analysis

### Core Thesis
In an environment saturated with misinformation and low-effort “hot takes”, a structured framework that records claims, links them to evidence and sources, and tracks predictions can help maintain a coherent, auditable knowledge base; Reality Check is presented as that framework.

### Summary (Neutral)
The README presents Reality Check as a “unified knowledge base” system organized around structured claims and analyses. It highlights a set of primitives (claims, sources, evidence links, reasoning trails, predictions, argument chains) and a 3-stage analysis workflow (descriptive → evaluative → dialectical). It also emphasizes semantic search over the knowledge base and references a public dataset repository (`realitycheck-data`) as an example.

The “Status” section asserts that v0.3.0 focuses on “analysis rigor” (Layer/Actor/Scope/Quantifier columns and a `--rigor` mode) and an “inbox workflow”, and it references the size of the test suite.

### Key Claims

| # | Claim | Claim ID | Layer | Actor | Scope | Quantifier | Type | Domain | Evid | Credence | Verified? | Falsifiable By |
|---|-------|----------|-------|-------|-------|------------|------|--------|------|----------:|-----------|----------------|
| 1 | Reality Check provides a claim registry that tracks claims with evidence levels, credence scores, and relationships | META-2026-024 | PRACTICED | OTHER:Reality Check framework | who=researchers; where=local repo; when=2026; process=claim registry; predicate=store+relate claims | N/A | [F] | META | E2 | 0.90 | ? | DB/CLI lacks fields for credence/evidence/relationships |
| 2 | Reality Check supports a structured 3-stage source analysis methodology: descriptive → evaluative → dialectical | META-2026-025 | PRACTICED | OTHER:Reality Check framework | who=analysts; where=analysis/sources; when=2026; process=3-stage analysis; predicate=standardized sections | N/A | [F] | META | E2 | 0.85 | ? | No documented template/validator for 3-stage structure exists |
| 3 | Reality Check supports evidence links that connect claims to sources with location and strength metadata | META-2026-026 | PRACTICED | OTHER:Reality Check framework | who=analysts; where=db+analysis; when=2026; process=evidence link; predicate=connect claim↔source | N/A | [F] | META | E2 | 0.90 | ? | Evidence link table/CLI does not exist |
| 4 | Reality Check supports reasoning trails that document why a credence was assigned (epistemic provenance) | META-2026-027 | PRACTICED | OTHER:Reality Check framework | who=analysts; where=db+analysis; when=2026; process=reasoning trail; predicate=record justification | N/A | [F] | META | E2 | 0.90 | ? | Reasoning trail table/CLI does not exist |
| 5 | Reality Check supports prediction tracking tied to falsification criteria and status updates | META-2026-028 | PRACTICED | OTHER:Reality Check framework | who=analysts; where=tracking/ + db; when=2026; process=prediction tracking; predicate=track [P] claims | N/A | [F] | META | E2 | 0.85 | ? | No prediction records or CLI exist; [P] claims cannot be tracked |
| 6 | Reality Check supports “argument chains” to map logical dependencies and identify weak links | META-2026-029 | PRACTICED | OTHER:Reality Check framework | who=analysts; where=claims/chains + db; when=2026; process=argument chain; predicate=encode dependencies | N/A | [F] | META | E2 | 0.80 | ? | No chain schema/CLI exists |
| 7 | Reality Check supports semantic search to find related claims across the knowledge base | META-2026-030 | PRACTICED | OTHER:Reality Check framework | who=users; where=db; when=2026; process=semantic search; predicate=retrieve similar claims | N/A | [F] | META | E2 | 0.80 | ? | Search command absent or produces no results without manual workarounds |
| 8 | v0.3.0 introduces “rigor-v1” analysis tables (Layer/Actor/Scope/Quantifier columns) and a `--rigor` enforcement mode in the analysis validator | META-2026-031 | PRACTICED | OTHER:Reality Check validator | who=analysts; where=analysis files; when=2026-02; process=analysis validation; predicate=rigor-v1 requirements | N/A | [F] | META | E2 | 0.85 | ? | Validator does not implement a rigor mode and/or does not check these columns |
| 9 | The v0.3.0 repository test suite contains 401 pytest-collected tests | META-2026-032 | PRACTICED | OTHER:Reality Check repo | who=maintainers; where=tests/; when=2026-02-01; process=pytest; predicate=collected test count | N/A | [F] | META | E2 | 0.90 | ? | Running pytest collects materially fewer/more than 401 tests |

### Argument Structure

The README is primarily a product framing argument:

```
[Information environment is noisy: misinformation + hot takes + AI content]
    | motivates
    v
[Need a structured, auditable knowledge base for claims]
    | suggests
    v
[Adopt a framework with: claim IDs, evidence levels, provenance, and analysis templates]
    | implemented by
    v
[Reality Check: DB-backed CLI + analysis output contract + optional tool integrations]
    | yields
    v
[Searchable repository of claims/sources/predictions (example: realitycheck-data)]
```

**Weakest link**: The README largely asserts usefulness; effectiveness depends on consistent analyst behavior and on the costs of structure not exceeding the benefits.

### Theoretical Lineage
- **Structured argument mapping**: formalizing claim dependencies (argument chains) resembles IBIS/argumentation mapping traditions.
- **Forecasting discipline**: prediction tracking echoes Tetlock-style “forecasting + falsification” norms.
- **Knowledge management / personal knowledge bases**: similar goals to Zettelkasten and “second brain” systems, but with stronger schema and provenance expectations.

### Scope & Limitations
- This source is documentation, not an external evaluation; it is most reliable for “what the project intends to provide” and “what CLI surface exists”.
- Claims about usefulness, completeness, and maturity are only weakly evidenced in the README itself.
- Some referenced features (e.g., “inbox workflow”) are not fully specified in the overview section and require reading workflow docs/tests to understand the intended behavior.

## Stage 2: Evaluative Analysis

### Internal Coherence
The high-level story is coherent: if you want an auditable knowledge base, you need (a) a schema for claims and sources, (b) a structured analysis template, (c) provenance and prediction tracking, and (d) retrieval/search across the growing repository. The main vulnerability is incentive/overhead: the system’s value depends on consistent, time-intensive usage.

### Key Factual Claims Verified

| Claim (paraphrased) | Crux? | Source Says | Actual | External Source | Status |
|---------------------|-------|-------------|--------|-----------------|--------|
| The repository requires Python 3.11+ | N | Python 3.11+ prerequisite | `requires-python = ">=3.11"` | https://github.com/lhl/realitycheck/blob/main/pyproject.toml | ok |
| The project provides a LanceDB-backed CLI for claims, sources, chains, predictions, evidence links, and reasoning trails | **Y** | Unified knowledge base + CLI primitives | `rc-db` is an entry point to `scripts/db.py`; CLI includes subcommands `claim`, `source`, `chain`, `prediction`, `evidence`, `reasoning` | https://github.com/lhl/realitycheck/blob/main/pyproject.toml ; https://github.com/lhl/realitycheck/blob/main/scripts/db.py | ok |
| The project includes semantic search and embedding management | **Y** | “Semantic Search” feature | `rc-db search` command exists; `rc-embed` provides `status/generate/regenerate` | https://github.com/lhl/realitycheck/blob/main/scripts/db.py ; https://github.com/lhl/realitycheck/blob/main/scripts/embed.py | ok |
| The analysis validator implements `--rigor` mode requiring Layer/Actor/Scope/Quantifier columns and Corrections & Updates section | **Y** | `--rigor` flag in v0.3.0 | `scripts/analysis_validator.py --help` shows `--rigor` with described behavior | https://github.com/lhl/realitycheck/blob/main/scripts/analysis_validator.py | ok |
| The test suite contains 401 pytest-collected tests | N | “401 tests” | `uv run pytest -q` collected 401 items (384 passed, 17 skipped) on 2026-02-01 | local run: `REALITYCHECK_EMBED_SKIP=1 uv run pytest -q` | ok |

### Disconfirming Evidence Search

| Claim | Counterevidence Found | Alternative Explanation | Search Notes |
|-------|----------------------|-------------------------|--------------|
| `--rigor` mode is exposed via `rc-validate` (as implied in some release docs) | `rc-validate --help` in this environment shows no `--rigor` flag | The rigor gate may be intended specifically for analysis-file validation (`analysis_validator.py`), while `rc-validate` remains DB-integrity focused | Checked installed `rc-validate --help` and source `scripts/validate.py`; neither exposes `--rigor` |
| Semantic search works “out of the box” for all repos | Search depends on embeddings existing; for new projects, embeddings may need generation and model download | README describes capabilities but does not foreground embedding setup costs | Searched for embedding guidance; README includes `rc-embed` tooling and GPU notes; actual usability depends on environment |
| “Unified knowledge base” solves misinformation/quality issues by itself | None direct; this is a value claim | The framework may mainly improve *auditability* rather than *truth* without additional verification work | Evaluated README framing vs the amount of manual verification required in typical analyses |

### Corrections & Updates

| Item | URL | Published | Corrected/Updated | What Changed | Impacted Claim IDs | Action Taken |
|------|-----|-----------|-------------------|--------------|--------------------|-------------|
| N/A | N/A | 2026-02-01 | N/A | No corrections/updates observed in this pass (single README capture) | N/A | N/A |

### Internal Tensions / Self-Contradictions

| Tension | Parts in Conflict | Implication |
|--------|-------------------|-------------|
| “`--rigor` flag” labeling ambiguity | README advertises `--rigor` in v0.3.0; the DB validator (`rc-validate`) does not expose `--rigor`, while the analysis-file validator does | Readers may misinterpret which validator is “strict”; workflow docs may need to be explicit about which command enforces rigor-v1 |

### Persuasion Techniques

| Technique | Example from Source | Effect on Reader |
|----------|----------------------|------------------|
| Problem salience framing | “hot takes… misinformation… AI-generated content” | Increases perceived need/urgency for a formal framework |
| Feature checklist | Long list of capabilities | Creates an impression of completeness and maturity even if some features are shallow/early |

### Unstated Assumptions

| Assumption | Claim ID | Critical? | Problematic? |
|------------|----------|-----------|--------------|
| Analysts will consistently do the extra work required for structured claims, provenance, and verification | META-2026-024..META-2026-031 | Y | ? |
| The benefits of structure outweigh the time/maintenance costs for the intended user | META-2026-024 | Y | ? |

### Evidence Assessment
- For “what exists in the repo”, evidence is strong (code + test suite).
- For “what works well in practice”, evidence is limited in this source; it relies on user adoption and workflow fit.

### Credence Assessment
- **Overall credence**: 0.80
- **Reasoning**: The README’s concrete claims about CLI surface area and validation tooling are corroborated by repository contents and test execution. The broader usefulness/maturity claims are plausible but under-evidenced here.

## Stage 3: Dialectical Analysis

### Steelmanned Argument
If you want your analysis work to remain useful over time, you need more than prose: you need stable IDs, explicit uncertainty, and the ability to query and cross-reference claims. A small amount of enforced structure (tables, validators, provenance) can turn an ad-hoc reading log into a durable knowledge base where claims can be revised, contradicted, and linked to evidence.

### Strongest Counterarguments
1. **Overhead and “false precision” risk**: People may fill tables mechanically, producing a facade of rigor without real verification.
2. **Tooling lock-in**: A DB-backed schema can increase maintenance costs and make migration harder than plain Markdown.
3. **Marginal returns**: For many tasks, lightweight note-taking or smaller, purpose-built tools may produce 80% of the value with 20% of the effort.

### Supporting Theories

| Theory/Framework | Source ID | How It Supports |
|------------------|-----------|-----------------|
| Forecasting as calibration discipline | (general) | Prediction records + falsifiers enforce measurable commitments and post-hoc evaluation |
| Argument mapping / dependency graphs | (general) | Chains and claim relationships enable “weakest link” reasoning |

### Contradicting Theories

| Theory/Framework | Source ID | Point of Conflict |
|------------------|-----------|-------------------|
| “Tools don’t create rigor” | (general) | Claims that epistemic quality comes from incentives, not schemas/validators |
| Minimalist PKM | (general) | Suggests heavy structure reduces throughput and creativity |

### Synthesis Notes
This README is best treated as an “interface spec”: it’s strong evidence of intended primitives and current CLI entry points. It is weak evidence for whether Reality Check improves decision quality without complementary verification habits and strong incentives.

### Claims to Cross-Reference
- Meta-analysis of framework efficacy in this dataset: `analysis/meta/framework-efficacy-greenland-test.md`
- Validator evolution: `docs/CHANGELOG.md` and `scripts/analysis_validator.py` in the framework repo

---

### Claim Summary

| ID | Type | Domain | Layer | Actor | Scope | Quantifier | Evidence | Credence | Claim |
|----|------|--------|-------|-------|-------|------------|----------|----------:|-------|
| META-2026-024 | [F] | META | PRACTICED | OTHER:Reality Check framework | who=researchers; where=local repo; when=2026; process=claim registry; predicate=store+relate claims | N/A | E2 | 0.90 | Reality Check provides a claim registry that tracks claims with evidence levels, credence scores, and relationships |
| META-2026-025 | [F] | META | PRACTICED | OTHER:Reality Check framework | who=analysts; where=analysis/sources; when=2026; process=3-stage analysis; predicate=standardized sections | N/A | E2 | 0.85 | Reality Check supports a structured 3-stage source analysis methodology: descriptive → evaluative → dialectical |
| META-2026-026 | [F] | META | PRACTICED | OTHER:Reality Check framework | who=analysts; where=db+analysis; when=2026; process=evidence link; predicate=connect claim↔source | N/A | E2 | 0.90 | Reality Check supports evidence links that connect claims to sources with location and strength metadata |
| META-2026-027 | [F] | META | PRACTICED | OTHER:Reality Check framework | who=analysts; where=db+analysis; when=2026; process=reasoning trail; predicate=record justification | N/A | E2 | 0.90 | Reality Check supports reasoning trails that document why a credence was assigned (epistemic provenance) |
| META-2026-028 | [F] | META | PRACTICED | OTHER:Reality Check framework | who=analysts; where=tracking/ + db; when=2026; process=prediction tracking; predicate=track [P] claims | N/A | E2 | 0.85 | Reality Check supports prediction tracking tied to falsification criteria and status updates |
| META-2026-029 | [F] | META | PRACTICED | OTHER:Reality Check framework | who=analysts; where=claims/chains + db; when=2026; process=argument chain; predicate=encode dependencies | N/A | E2 | 0.80 | Reality Check supports “argument chains” to map logical dependencies and identify weak links |
| META-2026-030 | [F] | META | PRACTICED | OTHER:Reality Check framework | who=users; where=db; when=2026; process=semantic search; predicate=retrieve similar claims | N/A | E2 | 0.80 | Reality Check supports semantic search to find related claims across the knowledge base |
| META-2026-031 | [F] | META | PRACTICED | OTHER:Reality Check validator | who=analysts; where=analysis files; when=2026-02; process=analysis validation; predicate=rigor-v1 requirements | N/A | E2 | 0.85 | v0.3.0 introduces “rigor-v1” analysis tables (Layer/Actor/Scope/Quantifier columns) and a `--rigor` enforcement mode in the analysis validator |
| META-2026-032 | [F] | META | PRACTICED | OTHER:Reality Check repo | who=maintainers; where=tests/; when=2026-02-01; process=pytest; predicate=collected test count | N/A | E2 | 0.90 | The v0.3.0 repository test suite contains 401 pytest-collected tests |

### Claims to Register

```yaml
claims:
  - id: "META-2026-024"
    text: "Reality Check provides a claim registry that tracks claims with evidence levels, credence scores, and relationships."
    type: "[F]"
    domain: "META"
    evidence_level: "E2"
    credence: 0.90
    operationalization: "Verify rc-db claim schema includes evidence_level/credence and relationship fields; confirm CRUD exists in scripts/db.py."
    assumptions: ["The README reflects shipped CLI+DB schema rather than aspirational features."]
    falsifiers: ["DB schema or CLI lacks credence/evidence/relationship fields or operations."]
    source_ids: ["lhl-2026-realitycheck-readme"]

  - id: "META-2026-025"
    text: "Reality Check supports a structured 3-stage source analysis methodology: descriptive → evaluative → dialectical."
    type: "[F]"
    domain: "META"
    evidence_level: "E2"
    credence: 0.85
    operationalization: "Confirm workflow docs/templates and analysis validator expect three stages or an equivalent output contract."
    assumptions: ["The methodology is represented in docs/templates, not only implied in README prose."]
    falsifiers: ["No 3-stage structure exists in methodology docs/templates/validators."]
    source_ids: ["lhl-2026-realitycheck-readme"]

  - id: "META-2026-026"
    text: "Reality Check supports evidence links that connect claims to sources with location and strength metadata."
    type: "[F]"
    domain: "META"
    evidence_level: "E2"
    credence: 0.90
    operationalization: "Confirm evidence_links table exists and rc-db has evidence add/list/get operations."
    assumptions: ["Evidence links are first-class records (not only narrative references in Markdown)."]
    falsifiers: ["No evidence_links table/CLI exists or it lacks location/strength metadata."]
    source_ids: ["lhl-2026-realitycheck-readme"]

  - id: "META-2026-027"
    text: "Reality Check supports reasoning trails that document why a credence was assigned (epistemic provenance)."
    type: "[F]"
    domain: "META"
    evidence_level: "E2"
    credence: 0.90
    operationalization: "Confirm reasoning_trails table exists and rc-db has reasoning add/get/history operations."
    assumptions: ["Reasoning trails are stored as structured records in the DB."]
    falsifiers: ["No reasoning_trails table/CLI exists or it does not store credence justification."]
    source_ids: ["lhl-2026-realitycheck-readme"]

  - id: "META-2026-028"
    text: "Reality Check supports prediction tracking tied to falsification criteria and status updates."
    type: "[F]"
    domain: "META"
    evidence_level: "E2"
    credence: 0.85
    operationalization: "Confirm predictions table and rc-db prediction operations exist; verify validation checks that [P] claims have prediction records."
    assumptions: ["Prediction tracking is integrated with claim types/statuses rather than a separate, manual process only."]
    falsifiers: ["No predictions table/CLI exists or predictions cannot be linked to [P] claims."]
    source_ids: ["lhl-2026-realitycheck-readme"]

  - id: "META-2026-029"
    text: "Reality Check supports “argument chains” to map logical dependencies and identify weak links."
    type: "[F]"
    domain: "META"
    evidence_level: "E2"
    credence: 0.80
    operationalization: "Confirm chains schema and rc-db chain operations; verify chains reference claim IDs and support dependency traversal."
    assumptions: ["Chains are represented as structured objects rather than only prose documents."]
    falsifiers: ["No chain schema/CLI exists or chains cannot reference claims."]
    source_ids: ["lhl-2026-realitycheck-readme"]

  - id: "META-2026-030"
    text: "Reality Check supports semantic search to find related claims across the knowledge base."
    type: "[F]"
    domain: "META"
    evidence_level: "E2"
    credence: 0.80
    operationalization: "Confirm rc-db search exists and returns nearest-neighbor results from embedded claim text."
    assumptions: ["Embeddings can be generated and stored for claims in the DB."]
    falsifiers: ["Search command absent or never returns similarity-ranked results even with embeddings present."]
    source_ids: ["lhl-2026-realitycheck-readme"]

  - id: "META-2026-031"
    text: "Reality Check v0.3.0 introduces “rigor-v1” analysis tables (Layer/Actor/Scope/Quantifier columns) and a `--rigor` enforcement mode in the analysis validator."
    type: "[F]"
    domain: "META"
    evidence_level: "E2"
    credence: 0.85
    operationalization: "Confirm scripts/analysis_validator.py defines --rigor and checks for Layer/Actor/Scope/Quantifier columns and Corrections & Updates."
    assumptions: ["The validator is used (directly or indirectly) in the intended check workflow."]
    falsifiers: ["No --rigor option exists or it does not enforce rigor-v1 requirements."]
    source_ids: ["lhl-2026-realitycheck-readme"]

  - id: "META-2026-032"
    text: "The Reality Check v0.3.0 repository test suite contains 401 pytest-collected tests."
    type: "[F]"
    domain: "META"
    evidence_level: "E2"
    credence: 0.90
    operationalization: "Run pytest (with REALITYCHECK_EMBED_SKIP=1 if needed) and confirm collected test count."
    assumptions: ["Test collection count is stable for a given commit/tag."]
    falsifiers: ["Running pytest at the referenced commit collects materially fewer/more tests."]
    source_ids: ["lhl-2026-realitycheck-readme"]
```

---

**Analysis Date**: 2026-02-01
**Analyst**: codex (gpt-5.2)
**Credence in Analysis**: 0.80

**Credence Reasoning**:
- High confidence in repo-surface claims (validated via code and tests).
- Lower confidence in real-world effectiveness claims (not empirically evaluated here).

## Analysis Log

| Pass | Date | Tool | Model | Duration | Tokens | Cost | Notes |
|------|------|------|-------|----------|--------|------|-------|
| 1 | 2026-02-01 | codex | gpt-5.2 | ? | ? | ? | Initial 3-stage analysis + claim extraction |

