# Source Analysis: Semantica (GitHub repo @ `b4cfb6d`)

> **Claim types**: `[F]` fact, `[T]` theory, `[H]` hypothesis, `[P]` prediction, `[A]` assumption, `[C]` counterfactual, `[S]` speculation, `[X]` contradiction  
> **Evidence**: **E1** systematic review/meta-analysis; **E2** peer-reviewed/official stats/law/code+tests; **E3** expert consensus/preprint; **E4** credible journalism/industry; **E5** opinion/anecdote; **E6** unsupported/speculative

## Metadata

| Field | Value |
|-------|-------|
| **Source ID** | `hawksightai-2026-semantica` |
| **Title** | Semantica |
| **Author(s)** | Hawksight AI (Semantica contributors) |
| **Date** | 2026-02-07 |
| **Type** | KNOWLEDGE |
| **URL** | https://github.com/Hawksight-AI/semantica |
| **Reliability** | 0.70 |
| **Rigor Level** | [REVIEWED] |
| **Bias Notes** | Self-authored OSS project docs + codebase. Code and tests are strong evidence for *existence/shape* of features, but README/docs are marketing-forward and can overstate real-world guarantees (“trustworthy”, “compliance”, “production-grade”). |

**Capture note**: Analysis performed on local checkout at commit `b4cfb6df15379ae2b86884029550e9df5d53d6a7` (describes itself as `0.2.6`, with `v0.2.6-36-gb4cfb6d` per `git describe`).

**Claims YAML**: [`analysis/sources/hawksightai-2026-semantica.yaml`](hawksightai-2026-semantica.yaml)

## Stage 1: Descriptive Analysis

### Core Thesis
High-stakes AI requires *meaning-aware* representations and auditability (entities, relationships, ontologies, reasoning traces, provenance), not just vector similarity; Semantica positions itself as a modular “semantic layer” that provides those building blocks end-to-end.

### Summary (Neutral)
Semantica is a Python package organized as many modules (ingest/parse/normalize/split; semantic extraction; knowledge graphs; ontologies; reasoning; vector/graph/triplet stores; deduplication/conflicts; change management; provenance; visualization; pipelines; CLI/server/worker). The README and docs emphasize use cases like GraphRAG, agent memory, and compliance-oriented audit trails.

The repo includes extensive documentation (`docs/`, `cookbook/`) and a sizable test suite (`tests/`). Release notes in `CHANGELOG.md` claim recent work focused on provenance (W3C PROV-O mapping + module wrappers) and change management (KG/ontology versioning with checksums), plus ingestion/parsing expansions.

### Key Claims

| # | Claim | Claim ID | Layer | Actor | Scope | Quantifier | Type | Domain | Evid | Credence | Verified? | Falsifiable By |
|---|-------|----------|-------|-------|-------|------------|------|--------|------|----------:|-----------|----------------|
| 1 | Semantica provides a unified provenance system (PROV-O concepts mapped into a schema) with in-memory + SQLite storage and SHA-256 integrity checks | META-2026-101 | PRACTICED | OTHER:Semantica framework | who=developers; where=Python pkg; when=2025-2026; process=provenance tracking; predicate=store lineage+checksums | N/A | [F] | META | E2 | 0.90 | local code+tests | Missing provenance schemas/storage/checksums or failing provenance tests |
| 2 | Semantica ships provenance-enabled wrappers for 17 modules (ingest/parse/normalize/extract/KG/stores/etc.) | META-2026-102 | PRACTICED | OTHER:Semantica framework | who=developers; where=Python pkg; when=2026; process=provenance integration; predicate=module wrappers exist | N/A | [F] | META | E2 | 0.90 | local code | Fewer wrappers exist or wrappers don’t import |
| 3 | Semantica provides change management (versioning/diffs/checksums) for knowledge graphs and ontologies with SQLite/in-memory backends | META-2026-103 | PRACTICED | OTHER:Semantica framework | who=developers; where=Python pkg; when=2026; process=change management; predicate=version snapshots+diffs+checksums | N/A | [F] | META | E2 | 0.90 | local tests | Change management code absent or tests fail materially |
| 4 | Semantica provides deduplication + conflict-resolution tooling (including Jaro-Winkler similarity and configurable strategies) | META-2026-104 | PRACTICED | OTHER:Semantica framework | who=developers; where=Python pkg; when=2025-2026; process=QA; predicate=detect+resolve duplicates/conflicts | N/A | [F] | META | E2 | 0.85 | local tests | Dedup/conflict modules absent or tests fail materially |
| 5 | Semantica includes a reasoning module implementing forward chaining, backward chaining, and a Rete engine | META-2026-105 | PRACTICED | OTHER:Semantica framework | who=developers; where=Python pkg; when=2026; process=rule reasoning; predicate=derive facts/prove goals | N/A | [F] | META | E2 | 0.85 | local tests | Reasoning module absent or tests fail materially |
| 6 | Semantica supports multi-format ingestion + parsing (PDF/DOCX/PPTX/XLSX/HTML/JSON/CSV, plus web/db/feeds), with optional Docling integration | META-2026-106 | PRACTICED | OTHER:Semantica framework | who=developers; where=Python pkg; when=2025-2026; process=ingest+parse; predicate=multi-format pipeline | N/A | [F] | META | E2 | 0.75 | partial local tests | Import failures for key formats or missing declared dependencies |
| 7 | Semantica provides LLM provider wrappers (Groq/OpenAI/HuggingFace/LiteLLM) used for LLM-assisted extraction and GraphRAG-style querying | META-2026-107 | PRACTICED | OTHER:Semantica framework | who=developers; where=Python pkg; when=2025-2026; process=LLM calls; predicate=provider wrappers exist | N/A | [F] | META | E2 | 0.75 | partial local tests | Providers absent or wrapper API non-functional without major rework |
| 8 | Semantica supports graph backends including Amazon Neptune with IAM auth, plus Neo4j/FalkorDB | META-2026-108 | PRACTICED | OTHER:Semantica framework | who=developers; where=Python pkg; when=2026; process=graph storage; predicate=backend adapters exist | N/A | [F] | META | E2 | 0.70 | code present | Backend adapters missing or unusable without undocumented pieces |
| 9 | Semantica defaults to FastEmbed-based embeddings and supports multiple vector-store backends (FAISS + hosted stores) | META-2026-109 | PRACTICED | OTHER:Semantica framework | who=developers; where=Python pkg; when=2026; process=embeddings+vector stores; predicate=providers exist | N/A | [F] | META | E2 | 0.70 | partial local tests | Embeddings/vector-store code absent or tests show material breakage |

### Argument Structure

Semantica’s README/docs are framed as a “gap argument”:

```
[High-stakes AI needs explanations + audit trails]
    | claims
    v
[Vector similarity RAG is insufficient for meaning/relationships]
    | motivates
    v
[Need a semantic layer: entities + relations + ontologies + provenance + reasoning]
    | therefore
    v
[Provide modular framework that builds + stores these artifacts]
```

### Theoretical Lineage
- **Knowledge graphs / semantic web**: RDF, SPARQL, OWL.
- **Provenance**: W3C PROV-O vocabulary (conceptual mapping).
- **GraphRAG**: combine retrieval with graph structure and traversal/reasoning.
- **Knowledge engineering**: schemas, ontologies, validation, governance.

### Scope & Limitations
- The repo is strong evidence for the *existence* of modules and APIs; it is weaker evidence for the *real-world outcomes* implied by marketing terms (“trustworthy”, “compliance-ready”, “production-grade”).
- Many features depend on optional providers/infrastructure (LLM APIs, Neo4j/Neptune, doc parsers, etc.), so “works out of the box” varies by environment.

## Stage 2: Evaluative Analysis

### Internal Coherence
The architecture is internally coherent: ingestion/parse/normalize/split → extract entities/relations → build KG/ontology → store (graph/triplet/vector) → QA (dedup/conflicts) → query/reason (GraphRAG) with provenance/change management layered across.

### Key Factual Claims Verified

| Claim (paraphrased) | Crux? | Source Says | Actual | External Source | Status |
|---------------------|-------|-------------|--------|-----------------|--------|
| Provenance system exists with PROV-O-mapped schema, storage backends, and checksums; provenance wrappers exist across modules | **Y** | “W3C PROV-O… 17 module integrations… storage backends… SHA-256” | `semantica/provenance/*` implements schemas/storage/checksum; 17 `*_provenance.py` modules exist; `python -m pytest -q tests/provenance -m "not integration"` → **205 passed, 32 skipped** (=237) | local code + tests | ok |
| Change-management module exists and is heavily tested | **Y** | “Enhanced change management… 104 tests” | `python -m pytest -q tests/change_management -m "not integration"` → **104 passed** | local tests | ok |
| Reasoning includes forward/backward chaining + Rete engine | N | “Forward/backward chaining… Rete algorithm” | `semantica/reasoning/reasoner.py`, `semantica/reasoning/rete_engine.py`; `python -m pytest -q tests/reasoning -m "not integration"` → **15 passed** | local code + tests | ok |
| Multi-format ingest/parse is implemented and tested for several paths | N | “PDF/DOCX/HTML/JSON/CSV… web ingest…” | `python -m pytest -q tests/ingest -m "not integration"` → **98 passed**; `python -m pytest -q tests/parse -m "not integration"` → **6 passed** | local tests | ok |
| Repo health is strong and test suite is green at HEAD | **Y** | Implied “production-grade” maturity | Several suites currently fail at HEAD in this environment (e.g., `tests/embeddings`, `tests/visualization`, some `tests/semantic_extract`, plus smaller failures in `tests/normalize`, `tests/seed`, `tests/triplet_store`) | local tests | ? |

### Disconfirming Evidence Search

| Claim | Counterevidence Found | Alternative Explanation | Search Notes |
|-------|----------------------|-------------------------|--------------|
| “Production-grade” / “trustworthy” framing implies broad stability | Multiple unit-test failures at HEAD (notably embeddings + visualization), and a concurrency failure in `tests/triplet_store` | The repo may be moving quickly; some tests lag behind API changes or require extra optional deps | Ran per-module unit tests with `-m "not integration"`; recorded pass/fail outcomes |
| “Multi-format parsing” is a core capability | `semantica.parse.pdf_parser` imports `pdfplumber`, but `pyproject.toml` does not list `pdfplumber` as a dependency in this checkout | The project may rely on CI/environment installs or intended optional extras; dependency declarations may be in flux | Verified import path and installed `pdfplumber` to run parse tests |
| “Thread-safe” framing (appears in some module docs) | `tests/triplet_store/test_jena_store_empty_graph.py::test_empty_graph_with_concurrent_operations` fails: concurrent adds yielded fewer triplets than expected | Thread safety may be a goal rather than fully achieved; rdflib Graph operations are not inherently thread-safe | Ran `python -m pytest -q tests/triplet_store -m "not integration"` |

### Corrections & Updates

| Item | URL | Published | Corrected/Updated | What Changed | Impacted Claim IDs | Action Taken |
|------|-----|-----------|-------------------|--------------|--------------------|-------------|
| Version vs HEAD delta | https://github.com/Hawksight-AI/semantica | 2026-02-03 (tag v0.2.6) | 2026-02-07 (HEAD) | HEAD is `v0.2.6-36-gb4cfb6d` with CI/dependency fixes post-tag | META-2026-106..META-2026-111 | Treated analysis as “HEAD snapshot”; avoided assuming PyPI parity |

### Internal Tensions / Self-Contradictions

| Tension | Parts in Conflict | Implication |
|--------|-------------------|-------------|
| “Safe default dependencies” vs install footprint | `pyproject.toml` lists heavyweight ML deps (torch/transformers/etc.) in core dependencies | Higher friction for adoption; more dependency/ABI conflicts; harder to run in minimal environments |
| Broad feature list vs uneven test health | Strong passing suites (provenance/change mgmt) alongside failing suites (embeddings/visualization) | Suggests uneven maturity across modules; users may need to “choose stable subset” |

### Persuasion Techniques

| Technique | Example from Source | Effect on Reader |
|----------|----------------------|------------------|
| High-stakes framing | “Designed for high-stakes domains… compliance… audit trails” | Raises urgency and perceived necessity |
| Feature checklist | Long tables of “auditable/explainable/governed/version control” | Implies completeness; may obscure optionality/edge cases |

### Unstated Assumptions

| Assumption | Claim ID | Critical? | Problematic? |
|------------|----------|-----------|--------------|
| Adding structure (KG/ontology/provenance) materially improves correctness, not just auditability | META-2026-100, META-2026-116 | Y | ? |
| Users can absorb operational complexity (deps, backends, pipelines) in return for governance | META-2026-106..META-2026-109 | Y | ? |

### Evidence Assessment
- For *existence of modules*: strong (repo code structure).
- For *correctness of several core modules*: mixed; many unit suites pass, but important areas (embeddings/visualization) have failing tests at this snapshot.
- For *real-world outcome claims*: weak in-repo evidence (mostly conceptual/marketing).

### Credence Assessment
- **Overall credence**: 0.75
- **Reasoning**: Semantica clearly implements a large portion of its claimed surface area, and some headline modules are well-tested (provenance, change management). However, test failures and dependency/packaging rough edges reduce confidence in “production-grade” framing and in some subsystems (notably embeddings/visualization and some integration/performance expectations).

## Stage 3: Dialectical Analysis

### Steelmanned Argument
Most AI systems are not audit-ready: they treat text as bags of tokens and retrieve by similarity, which fails to represent relationships, rules, and provenance. By explicitly extracting entities/relations, encoding domain constraints in ontologies, tracking lineage end-to-end, and enabling graph reasoning, you can build systems that are inspectable and governable—especially where failure costs are high. Semantica provides modular components so teams can adopt only the parts they need while maintaining an integrated path to GraphRAG and agent memory.

### Strongest Counterarguments
1. **Complexity tax**: The scope (many modules + heavy dependencies + optional backends) may exceed what most teams can maintain; simpler approaches may outperform in total cost.
2. **Auditability ≠ truth**: Provenance and explanations can make errors easier to diagnose, but do not guarantee correctness; governance needs human process and incentives.
3. **Uneven maturity risk**: A framework can be “wide” before it’s “deep”; weak points (embeddings, visualization, concurrency) can undermine end-to-end reliability.

### Supporting Theories

| Theory/Framework | Source ID | How It Supports |
|------------------|-----------|-----------------|
| Semantic web / knowledge engineering | (general) | Formal schemas + relationships enable richer queries and validation |
| Provenance as a governance primitive | (general) | Lineage supports auditing, debugging, and compliance evidence |

### Contradicting Theories

| Theory/Framework | Source ID | Point of Conflict |
|------------------|-----------|-------------------|
| “Keep it simple” engineering | (general) | Argues complex frameworks reduce adoption and increase failure surface |
| Pure vector RAG pragmatism | (general) | Claims most value comes from good retrieval + prompting, not full semantic layers |

### Synthesis Notes
Semantica is a broad, fast-moving “semantic layer” framework with strong evidence of significant implementation effort and meaningful test coverage in several headline areas (provenance + change management). The main risks are operational (dependency footprint, optional backends), maturity variance across modules, and the gap between auditability claims and real-world correctness/compliance outcomes.

### Claims to Cross-Reference
- Provenance claims vs formal PROV-O/RDF interoperability expectations (outside this repo).
- Comparisons with an epistemic-credence claim registry approach (Reality Check): see synthesis `analysis/syntheses/semantica-vs-realitycheck-synthesis.md`.

---

### Claim Summary

| ID | Type | Domain | Layer | Actor | Scope | Quantifier | Evidence | Credence | Claim |
|----|------|--------|-------|-------|-------|------------|----------|----------:|-------|
| META-2026-100 | [F] | META | PRACTICED | OTHER:Semantica framework | who=developers; where=Python pkg; when=2025-2026; predicate=modular semantic-layer framework exists | N/A | E2 | 0.85 | Semantica is an open-source Python framework for building semantic layers and knowledge-engineering systems, with modules spanning ingestion, parsing, extraction, KGs, ontologies, reasoning, and storage backends. |
| META-2026-101 | [F] | META | PRACTICED | OTHER:Semantica framework | who=developers; where=Python pkg; when=2026; predicate=provenance system exists | N/A | E2 | 0.90 | Semantica provides a unified provenance system (PROV-O concepts mapped into a schema) with in-memory + SQLite storage and SHA-256 integrity checks. |
| META-2026-102 | [F] | META | PRACTICED | OTHER:Semantica framework | who=developers; where=Python pkg; when=2026; predicate=17 provenance wrappers exist | N/A | E2 | 0.90 | Semantica ships provenance-enabled wrappers for 17 modules. |
| META-2026-103 | [F] | META | PRACTICED | OTHER:Semantica framework | who=developers; where=Python pkg; when=2026; predicate=KG+ontology versioning exists | N/A | E2 | 0.90 | Semantica provides change management/version control for knowledge graphs and ontologies with SQLite/in-memory storage, diffs, and checksum verification. |
| META-2026-104 | [F] | META | PRACTICED | OTHER:Semantica framework | who=developers; where=Python pkg; when=2025-2026; predicate=dedup+conflict modules exist | N/A | E2 | 0.85 | Semantica provides deduplication and conflict-resolution tooling, including Jaro-Winkler similarity and configurable strategies. |
| META-2026-105 | [F] | META | PRACTICED | OTHER:Semantica framework | who=developers; where=Python pkg; when=2026; predicate=rule reasoning exists | N/A | E2 | 0.85 | Semantica includes a reasoning module implementing forward chaining, backward chaining, and a Rete engine. |
| META-2026-106 | [F] | META | PRACTICED | OTHER:Semantica framework | who=developers; where=Python pkg; when=2025-2026; predicate=multi-format ingest+parse exists | N/A | E2 | 0.75 | Semantica supports multi-format ingestion and parsing (files/web/db/feeds; PDF/DOCX/PPTX/XLSX/HTML/JSON/CSV), with optional Docling integration. |
| META-2026-107 | [F] | META | PRACTICED | OTHER:Semantica framework | who=developers; where=Python pkg; when=2025-2026; predicate=LLM providers exist | N/A | E2 | 0.75 | Semantica provides LLM provider wrappers (Groq, OpenAI, HuggingFace, LiteLLM) used for LLM-assisted extraction and GraphRAG-style querying. |
| META-2026-108 | [F] | META | PRACTICED | OTHER:Semantica framework | who=developers; where=Python pkg; when=2026; predicate=graph backend adapters exist | N/A | E2 | 0.70 | Semantica supports graph backends including Amazon Neptune with IAM authentication, plus Neo4j and FalkorDB. |
| META-2026-109 | [F] | META | PRACTICED | OTHER:Semantica framework | who=developers; where=Python pkg; when=2026; predicate=embeddings+vector stores exist | N/A | E2 | 0.70 | Semantica defaults to FastEmbed-based embeddings and supports multiple vector-store backends (FAISS and optional hosted stores). |
| META-2026-110 | [F] | META | PRACTICED | OTHER:Semantica repo | who=maintainers; where=tests/; when=2026-02-07; predicate=test suites run | N/A | E2 | 0.90 | Semantica’s provenance and change-management modules have extensive automated tests (237 and 104 respectively) that pass in this environment when run as unit tests. |
| META-2026-111 | [F] | META | PRACTICED | OTHER:Semantica repo | who=maintainers; where=tests/; when=2026-02-07; predicate=some tests fail at HEAD | N/A | E2 | 0.85 | In this checkout, several test suites fail (notably embeddings and visualization), alongside smaller failures (LLM extraction caching expectations, relative date normalization, seed CSV loading, and triplet-store concurrency). |
| META-2026-112 | [F] | META | PRACTICED | OTHER:Semantica packaging | who=users; where=Python deps; when=2026; predicate=core deps are heavy | N/A | E2 | 0.85 | Semantica’s core dependency set is large (e.g., torch/transformers/sentence-transformers/fastembed/faiss-cpu), increasing installation footprint and dependency-conflict risk. |
| META-2026-113 | [F] | META | PRACTICED | OTHER:Semantica repo | who=maintainers; where=git history; when=2025-06..2026-02; predicate=active development | N/A | E2 | 0.90 | Semantica is actively developed (initial commit 2025-06-25; 942 commits; tags through v0.2.6; HEAD is 36 commits past v0.2.6 as of 2026-02-07). |
| META-2026-115 | [H] | META | ASSERTED | OTHER:Semantica framework | who=users; where=agent frameworks; when=2026; predicate=complements frameworks | N/A | E5 | 0.55 | Semantica can be used alongside agentic frameworks (e.g., LangChain/LlamaIndex) to add auditability, provenance, and semantic reasoning. |
| META-2026-116 | [T] | META | ASSERTED | OTHER:Semantica docs | who=practitioners; where=high-stakes AI; when=2026; predicate=semantic gap thesis | N/A | E5 | 0.60 | High-stakes AI systems that rely primarily on text similarity (vector retrieval) will fail to meet requirements for meaning, governance, and auditability without a semantic layer (entities/relations/ontologies/provenance). |

### Claims to Register

```yaml
sources:
  - id: "hawksightai-2026-semantica"
    type: "KNOWLEDGE"
    title: "Semantica"
    author: ["Hawksight AI"]
    year: 2026
    url: "https://github.com/Hawksight-AI/semantica"
    accessed: "2026-02-07"
    status: "analyzed"
    analysis_file: "analysis/sources/hawksightai-2026-semantica.md"
claims:
  - id: "META-2026-101"
    text: "Semantica provides a unified provenance system (PROV-O concepts mapped into a schema) with in-memory + SQLite storage and SHA-256 integrity checks."
    type: "[F]"
    domain: "META"
    evidence_level: "E2"
    credence: 0.90
    operationalization: "Verify semantica/provenance schemas/storage/checksum implementations exist and provenance unit tests pass."
    assumptions: ["Repo code at HEAD reflects the intended feature set described in README/docs."]
    falsifiers: ["Provenance modules absent or provenance tests fail materially."]
    source_ids: ["hawksightai-2026-semantica"]
```

---

**Analysis Date**: 2026-02-07  
**Analyst**: codex (gpt-5.2)  
**Credence in Analysis**: 0.78

## Analysis Log

| Pass | Date | Tool | Model | Duration | Tokens | Cost | Notes |
|------|------|------|-------|----------|--------|------|-------|
| 1 | 2026-02-07 | codex | gpt-5.2 | ? | ? | ? | Initial 3-stage analysis + claim extraction; verified key modules via unit tests |
