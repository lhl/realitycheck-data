# Source Analysis: Mafin 2.5 FinanceBench results (GitHub repository)

> **Claim types**: `[F]` fact, `[T]` theory, `[H]` hypothesis, `[P]` prediction, `[A]` assumption, `[C]` counterfactual, `[S]` speculation, `[X]` contradiction
> **Evidence**: **E1** systematic review/meta-analysis; **E2** peer-reviewed/official stats; **E3** expert consensus/preprint; **E4** credible journalism/industry; **E5** opinion/anecdote; **E6** unsupported/speculative

## Metadata

| Field | Value |
|---|---|
| **Source ID** | `vectifyai-2025-mafin25-financebench` |
| **Title** | Mafin2.5-FinanceBench (published evaluation results) |
| **Author(s)** | VectifyAI (GitHub org) |
| **Date** | 2025-02-19 |
| **Type** | KNOWLEDGE |
| **URL** | https://github.com/VectifyAI/Mafin2.5-FinanceBench |
| **Reliability** | 0.55 |
| **Rigor Level** | [REVIEWED] |
| **Bias Notes** | Vendor-published benchmark claims with open code and answer dumps, but judged via LLM-as-judge and not a preregistered, third-party evaluation. No clear repository license file observed (limits reuse). |

**Claims YAML**: [`analysis/sources/vectifyai-2025-mafin25-financebench.yaml`](vectifyai-2025-mafin25-financebench.yaml)

## Stage 1: Descriptive Analysis

### Core Thesis
VectifyAI reports that its “Mafin 2.5” system (built on PageIndex) achieves very high FinanceBench accuracy (98.7%), and provides evaluation code and answer outputs to support the claim.

### Key Claims

| # | Claim | Claim ID | Type | Domain | Evidence | Credence | Verified? | Falsifiable By |
|---|-------|----------|------|--------|----------|----------:|-----------|----------------|
| 1 | The repository reports that Mafin 2.5 achieves 98.7% accuracy on the FinanceBench public set and claims full benchmark coverage | TECH-2026-025 | [F] | TECH | E4 | 0.80 | ✓ | Repo does not state this, or the released artifacts do not correspond to the claim |
| 2 | The provided evaluation script uses LLM-as-judge (default GPT-4o) with permissive equivalence criteria (allowing inference/rounding flexibility) to score answers | TECH-2026-026 | [F] | TECH | E2 | 0.90 | ✓ | eval.py uses a strict deterministic scorer or a substantially different judging procedure |
| 3 | Because the official FinanceBench paper reports much lower success rates under human evaluation, Mafin’s 98.7% (LLM-judge) result is not directly comparable without protocol matching | TECH-2026-027 | [H] | TECH | E4 | 0.70 | ? | Independent reproduction under a matched human-eval protocol confirms ~98% success and establishes SOTA comparability |

### Argument Structure

```
(1) FinanceBench is a realistic benchmark for financial QA
        ↓
(2) Evaluate Mafin 2.5 against FinanceBench public set
        ↓
(3) Report 98.7% accuracy (and comparisons vs competitors)
        ↓
Conclusion: Mafin 2.5 / PageIndex is SOTA for FinanceBench-style financial doc QA
```

### Scope & Limitations
- This source is **evaluation artifacts**, not a peer-reviewed evaluation.
- The scoring definition (“accuracy”) is dependent on an LLM judge prompt that appears deliberately lenient.

## Stage 2: Evaluative Analysis

### Internal Coherence
The repo coherently describes an evaluation setup and provides code and answer dumps. The central weakness is comparability: the judge’s permissive criteria and the lack of human-eval reproduction make “SOTA” a strong claim.

### Key Factual Claims Verified

| Claim (paraphrased) | Crux? | Source Says | Actual | External Source | Status |
|---------------------|-------|-------------|--------|-----------------|--------|
| Repo reports 98.7% accuracy for Mafin 2.5 on FinanceBench public set | **Y** | “98.7% accuracy” | README explicitly states 98.7% and includes result JSON files | https://github.com/VectifyAI/Mafin2.5-FinanceBench | ok |
| Evaluation uses LLM-as-judge and allows broad equivalence/inference | **Y** | “open-sourced evaluation code” | `eval.py` calls a chat model to judge equivalence and explicitly permits inferable/rounded numbers | https://github.com/VectifyAI/Mafin2.5-FinanceBench/blob/main/eval.py | ok |

### Disconfirming Evidence Search

| Claim | Counterevidence Found | Alternative Explanation | Search Notes |
|-------|----------------------|-------------------------|--------------|
| “98.7% accuracy implies SOTA” | FinanceBench paper reports much lower baseline success under human eval (e.g., long-context ~79%, oracle ~85% on sample) | Different judging strictness (LLM vs human), different corpora (single DB), and different prompts/tools can yield non-comparable metrics | Compared against `islam-2023-financebench` claims |
| “Independent of base model” | Repo claims identical 98.7% for GPT-4o and Deepseek v3; no independent audit | System may be heavily retrieval/tool-driven with a forgiving judge; base-model differences may be masked | Looked for reproducible scripts/seed control; not present in repo |

### Evidence Assessment
- **Strengths**: shares artifacts (answers) and code; makes evaluation inspectable.
- **Weaknesses**: judge prompt is very permissive; no license file; no third-party replication; “market competitor” comparisons cite heterogeneous sources/coverage.

### Credence Assessment
- **Overall Credence**: 0.55
- **Reasoning**: High confidence that the repo *reports* 98.7% under its judge; lower confidence that this establishes cross-protocol SOTA.

## Stage 3: Dialectical Analysis

### Steelmanned Argument
Publishing code and outputs is better than unverifiable marketing. Even if the judge is permissive, the end-to-end system might genuinely be strong at financial doc QA, and the public artifacts allow others to replicate or critique.

### Strongest Counterarguments
1. A permissive LLM judge can turn partially correct or vague answers into “correct,” inflating accuracy.
2. Without matched-protocol baselines and human evaluation, cross-system comparisons are not meaningful.

### Synthesis Notes
Treat 98.7% as **“vendor-reported under a lenient LLM-judge protocol”** until reproduced under a clearly matched FinanceBench protocol (ideally with human evaluation, or at least a stricter rubric).

### Claim Summary

| ID | Type | Domain | Evidence | Credence | Claim |
|----|------|--------|----------|----------:|-------|
| TECH-2026-025 | [F] | TECH | E4 | 0.80 | Repo reports Mafin 2.5 reaches 98.7% FinanceBench accuracy (full coverage claimed) |
| TECH-2026-026 | [F] | TECH | E2 | 0.90 | eval.py uses LLM-as-judge with permissive equivalence criteria |
| TECH-2026-027 | [H] | TECH | E4 | 0.70 | 98.7% is not directly comparable to FinanceBench paper baselines without protocol matching |

### Claims to Register

```yaml
claims:
  - id: "TECH-2026-025"
    text: >-
      The VectifyAI Mafin2.5-FinanceBench repository reports that Mafin 2.5 achieves 98.7% accuracy on the FinanceBench
      public set and claims full benchmark coverage.
    type: "[F]"
    domain: "TECH"
    evidence_level: "E4"
    credence: 0.80
    source_ids: ["vectifyai-2025-mafin25-financebench"]
    operationalization: >-
      Inspect the published artifacts (README, result JSONs) and independently reproduce the scoring with a clearly
      specified judge/rubric.
    assumptions:
      - Published artifacts correspond to the claimed evaluation run.
    falsifiers:
      - Artifacts are missing/inconsistent or reproduction fails under the stated protocol.

  - id: "TECH-2026-026"
    text: >-
      The evaluation script in VectifyAI/Mafin2.5-FinanceBench uses an LLM-as-judge (default GPT-4o) and applies
      permissive equivalence criteria (allowing rounding flexibility and inferable numeric conclusions) to score answers.
    type: "[F]"
    domain: "TECH"
    evidence_level: "E2"
    credence: 0.90
    source_ids: ["vectifyai-2025-mafin25-financebench"]
    operationalization: "Read eval.py and confirm the judge prompt, model choice, and decision rule."
    assumptions:
      - The repository’s eval.py reflects the method used to produce the reported score.
    falsifiers:
      - eval.py uses a strict deterministic scorer or materially different judging criteria than described.

  - id: "TECH-2026-027"
    text: >-
      Because the FinanceBench paper reports much lower success rates under human evaluation for strong baselines,
      Mafin’s reported 98.7% (LLM-judge) score is not directly comparable to “SOTA” without protocol matching.
    type: "[H]"
    domain: "TECH"
    evidence_level: "E4"
    credence: 0.70
    source_ids: ["vectifyai-2025-mafin25-financebench"]
    operationalization: >-
      Re-evaluate the published answers under the FinanceBench paper’s human rubric (or a close proxy) and compare
      to baseline systems under the same corpus and subset.
    assumptions:
      - Judge strictness and subset/corpus choices materially affect reported accuracy.
    falsifiers:
      - Matched-protocol evaluation confirms ~98% success and establishes comparable SOTA status.
```

---
**Analysis Date**: 2026-01-24
**Analyst**: gpt-5.2
**Credence in Analysis**: 0.70

