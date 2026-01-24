# Source Analysis: StrataLens AI (GitHub repository)

> **Claim types**: `[F]` fact, `[T]` theory, `[H]` hypothesis, `[P]` prediction, `[A]` assumption, `[C]` counterfactual, `[S]` speculation, `[X]` contradiction
> **Evidence**: **E1** systematic review/meta-analysis; **E2** peer-reviewed/official stats; **E3** expert consensus/preprint; **E4** credible journalism/industry; **E5** opinion/anecdote; **E6** unsupported/speculative

## Metadata

| Field | Value |
|---|---|
| **Source ID** | `kamathhrishi-2025-stratalens-ai` |
| **Title** | StrataLens AI (open source equity research platform) |
| **Author(s)** | kamathhrishi (GitHub user) |
| **Date** | 2025-12-06 |
| **Type** | KNOWLEDGE |
| **URL** | https://github.com/kamathhrishi/stratalens-ai |
| **Reliability** | 0.50 |
| **Rigor Level** | [REVIEWED] |
| **Bias Notes** | Single-maintainer repo for a live product; detailed architecture docs but limited independent validation. Benchmark claim is self-reported and no eval artifacts are provided in-repo. Repository licensing appears inconsistent (README claims MIT but no LICENSE file found). |

**Claims YAML**: [`analysis/sources/kamathhrishi-2025-stratalens-ai.yaml`](kamathhrishi-2025-stratalens-ai.yaml)

## Stage 1: Descriptive Analysis

### Core Thesis
StrataLens is an applied financial QA product built with a conventional hybrid RAG architecture (pgvector + keyword search + reranking), plus tool routing and iterative self-reflection, targeting earnings transcripts, SEC filings, and news.

### Key Claims

| # | Claim | Claim ID | Type | Domain | Evidence | Credence | Verified? | Falsifiable By |
|---|-------|----------|------|--------|----------|----------:|-----------|----------------|
| 1 | StrataLens uses a traditional hybrid RAG stack: PostgreSQL+pgvector embeddings with keyword search and reranking, plus LLM-based routing for SEC sections/tables | TECH-2026-028 | [F] | TECH | E2 | 0.85 | ✓ | Repo documentation or code contradicts the described architecture |
| 2 | The StrataLens README claims ~85% FinanceBench accuracy on SEC filings only, evaluated via LLM-as-judge | TECH-2026-029 | [F] | TECH | E5 | 0.60 | ✓ | README does not claim this, or subsequent documentation retracts it |
| 3 | The repository lacks a LICENSE file despite stating “MIT License” in the README, making licensing unclear | TECH-2026-030 | [F] | TECH | E2 | 0.95 | ✓ | A LICENSE file exists or GitHub metadata clearly specifies a license |

### Argument Structure

```
User question
   ↓
LLM parses intent (ticker/time/source)
   ↓
Route to tool: transcripts / SEC filings / news
   ↓
Retrieve evidence (hybrid search + rerank + table selection)
   ↓
Generate answer with citations, iterate via self-reflection
```

### Theoretical Lineage
- **Hybrid retrieval**: combine lexical + semantic retrieval plus reranking.
- **Section routing**: select the relevant report section(s) before retrieval (structure-aware but vector-based).
- **Agentic iteration**: self-critique loop for answer quality.

### Scope & Limitations
- This is an **application** (equity research assistant), not a new retrieval paradigm.
- Performance claims depend on undisclosed evaluation protocol and dataset subset.

## Stage 2: Evaluative Analysis

### Internal Coherence
The described architecture is plausible and aligns with common production RAG patterns (hybrid search + rerank + routing). The credibility bottlenecks are (a) licensing ambiguity and (b) lack of published evaluation artifacts.

### Key Factual Claims Verified

| Claim (paraphrased) | Crux? | Source Says | Actual | External Source | Status |
|---------------------|-------|-------------|--------|-----------------|--------|
| Repo uses pgvector + hybrid search + reranking + SEC section routing | **Y** | Architecture docs describe this | `agent/README.md` describes 70/30 vector/keyword hybrid search, cross-encoder reranking, and LLM section routing | https://github.com/kamathhrishi/stratalens-ai/blob/main/agent/README.md | ok |
| Repo claims 85% FinanceBench accuracy (SEC filings only) | N | “Benchmark: 85% accuracy…” | Statement is present in README, but no scoring code or outputs are provided | https://github.com/kamathhrishi/stratalens-ai | ? |
| Repo is MIT licensed | **Y** | README claims MIT | No LICENSE file found in repo root and GitHub metadata shows no license | https://github.com/kamathhrishi/stratalens-ai | x |

### Disconfirming Evidence Search

| Claim | Counterevidence Found | Alternative Explanation | Search Notes |
|-------|----------------------|-------------------------|--------------|
| “85% FinanceBench accuracy” | No published eval artifacts in repo; FinanceBench paper shows strong baselines vary widely by protocol | Claim may be true under an LLM-as-judge and a constrained subset/corpus, but is not auditable | Looked for `eval`, `financebench`, or result dumps in repo; none found |
| “MIT license” | Missing LICENSE file contradicts the claim | License may exist elsewhere (website) or was omitted accidentally | Checked repository root listing and GitHub API license field |

### Evidence Assessment (Project Credibility / Maturity)
- **Green flags**: unusually detailed agent architecture documentation; clear descriptions of retrieval/routing; live deployment indicated.
- **Red flags**: license inconsistency; single-contributor codebase; benchmark claim not backed by reproducible artifacts.

### Credence Assessment
- **Overall Credence**: 0.50
- **Reasoning**: Architecture descriptions are credible; licensing and benchmark claims are currently not robust.

## Stage 3: Dialectical Analysis

### Steelmanned Argument
StrataLens reflects a practical production pattern: hybrid retrieval + reranking + routing, which is often “good enough” and cost-effective compared to heavy multi-step reasoning traversal. For financial QA across many companies and documents, this scaling-friendly approach is likely to be operationally attractive.

### Strongest Counterarguments
1. Without licensing clarity, adoption/reuse is risky regardless of technical merit.
2. Without published eval artifacts, accuracy claims are not decision-grade.

### Synthesis Notes (vs PageIndex)
StrataLens already does some structure-aware routing (SEC section routing + table selection), which overlaps with PageIndex’s “structure-first” motivation while keeping embeddings and standard infra.

### Claim Summary

| ID | Type | Domain | Evidence | Credence | Claim |
|----|------|--------|----------|----------:|-------|
| TECH-2026-028 | [F] | TECH | E2 | 0.85 | StrataLens uses hybrid RAG with pgvector + keyword search + reranking + section routing |
| TECH-2026-029 | [F] | TECH | E5 | 0.60 | StrataLens claims 85% FinanceBench accuracy on SEC filings only (LLM-judge) |
| TECH-2026-030 | [F] | TECH | E2 | 0.95 | StrataLens repo lacks a LICENSE file despite claiming MIT in README |

### Claims to Register

```yaml
claims:
  - id: "TECH-2026-028"
    text: >-
      StrataLens AI uses a traditional hybrid RAG architecture: PostgreSQL with pgvector embeddings plus keyword search
      and reranking, and includes LLM-based routing for SEC filing sections and table selection.
    type: "[F]"
    domain: "TECH"
    evidence_level: "E2"
    credence: 0.85
    source_ids: ["kamathhrishi-2025-stratalens-ai"]
    operationalization: "Inspect repository docs and code to confirm retrieval components and configured weights/models."
    assumptions:
      - Documentation accurately reflects the deployed system.
    falsifiers:
      - Code/docs show a materially different retrieval approach (e.g., no pgvector, no hybrid search, no reranking).

  - id: "TECH-2026-029"
    text: >-
      The StrataLens README claims about 85% accuracy on FinanceBench (SEC filings only), evaluated using LLM-as-a-judge.
    type: "[F]"
    domain: "TECH"
    evidence_level: "E5"
    credence: 0.60
    source_ids: ["kamathhrishi-2025-stratalens-ai"]
    operationalization: "Locate the claim in README and request or reproduce evaluation artifacts under a specified protocol."
    assumptions:
      - The author’s stated benchmark corresponds to a real evaluation run.
    falsifiers:
      - No evaluation can be produced, or reproduction fails under a clearly specified FinanceBench subset/protocol.

  - id: "TECH-2026-030"
    text: >-
      The stratalens-ai repository lacks a LICENSE file despite stating “MIT License” in the README, so the licensing
      status is unclear.
    type: "[F]"
    domain: "TECH"
    evidence_level: "E2"
    credence: 0.95
    source_ids: ["kamathhrishi-2025-stratalens-ai"]
    operationalization: "Check repository root and GitHub license metadata for an explicit license grant."
    assumptions:
      - Absence of an explicit license implies no clear permission to reuse beyond default copyright.
    falsifiers:
      - A LICENSE file exists or a clear license grant is published in the repo/history and reflected in metadata.
```

---
**Analysis Date**: 2026-01-24
**Analyst**: gpt-5.2
**Credence in Analysis**: 0.75

