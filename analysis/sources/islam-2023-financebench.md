# Source Analysis: FinanceBench (financial QA benchmark)

> **Claim types**: `[F]` fact, `[T]` theory, `[H]` hypothesis, `[P]` prediction, `[A]` assumption, `[C]` counterfactual, `[S]` speculation, `[X]` contradiction
> **Evidence**: **E1** systematic review/meta-analysis; **E2** peer-reviewed/official stats; **E3** expert consensus/preprint; **E4** credible journalism/industry; **E5** opinion/anecdote; **E6** unsupported/speculative

## Metadata

| Field | Value |
|---|---|
| **Source ID** | `islam-2023-financebench` |
| **Title** | FinanceBench: A New Benchmark for Financial Question Answering |
| **Author(s)** | Pranab Islam; Anand Kannappan; Douwe Kiela; Rebecca Qian; Nino Scherrer; Bertie Vidgen |
| **Date** | 2023-11-20 |
| **Type** | PAPER |
| **URL** | https://arxiv.org/abs/2311.11944 |
| **Reliability** | 0.75 |
| **Rigor Level** | [REVIEWED] |
| **Bias Notes** | Benchmark/measurement work from authors affiliated with Patronus AI / Contextual AI / Stanford; strong incentives to highlight failure modes and need for better evaluation. Dataset licensing terms are not clearly visible from the paper itself; treat “open-source” as “publicly available” unless licensing is verified. |

**Claims YAML**: [`analysis/sources/islam-2023-financebench.yaml`](islam-2023-financebench.yaml)

## Stage 1: Descriptive Analysis

### Core Thesis
The paper introduces FinanceBench, an open-book financial question-answering benchmark, and reports that state-of-the-art LLM configurations (with retrieval and long-context prompting) still fail frequently, implying that reliable financial QA remains unsolved and requires better retrieval, reasoning, and evaluation.

### Key Claims

| # | Claim | Claim ID | Type | Domain | Evidence | Credence | Verified? | Falsifiable By |
|---|-------|----------|------|--------|----------|----------:|-----------|----------------|
| 1 | FinanceBench comprises 10,231 open-book financial QA questions with answers and evidence strings; the authors provide an open-source evaluation subset of 150 cases | TECH-2026-015 | [F] | TECH | E2 | 0.90 | ? | Public release does not contain the claimed dataset size/subset, or docs materially contradict these counts |
| 2 | On the FinanceBench human-eval sample (n=150), GPT-4-Turbo with a shared vector store retrieval setup “incorrectly answered or refused to answer” ~81% of questions; an oracle setup with access to evidence pages achieves ~85% success | TECH-2026-016 | [F] | TECH | E2 | 0.85 | ✓ | Updated paper/erratum or a re-analysis shows materially different rates under the stated evaluation setup |

### Argument Structure

```
Need: evaluate LLMs for high-stakes financial QA
        ↓
Build FinanceBench (questions + answers + evidence strings)
        ↓
Evaluate multiple model + retrieval configurations on sample
        ↓
Observe high failure rates (wrong answers / refusals)
        ↓
Conclusion: current LLM+retrieval setups are unreliable; better retrieval/reasoning + better evaluation needed
```

### Theoretical Lineage
- **Open-book QA**: evaluation where relevant evidence exists in a provided/document corpus (retrieval is part of the task).
- **RAG evaluation**: benchmarking end-to-end systems (retrieval + generation) rather than the base model alone.
- **Safety/enterprise reliability framing**: refusals vs incorrect answers and risk of misplaced trust.

### Scope & Limitations
- Results reported for a **human-evaluated sample (n=150)**, not necessarily representative of all question types.
- Evaluation depends on prompt/setup details; comparisons across third-party “FinanceBench accuracy” claims can be **non-comparable** without matching protocol, corpus, and judging method.

## Stage 2: Evaluative Analysis

### Internal Coherence
The paper’s logic is coherent: define a domain-specific benchmark with evidence strings; test plausible enterprise-like configurations; report failure modes; argue for improved retrieval/reasoning and better evaluation practices.

### Key Factual Claims Verified

| Claim (paraphrased) | Crux? | Source Says | Actual | External Source | Status |
|---------------------|-------|-------------|--------|-----------------|--------|
| FinanceBench uses 10,231 questions and provides a 150-case evaluation set open-source | N | 10,231 total; 150-case eval set available open-source | The GitHub repository exists and is publicly accessible; dataset licensing is unclear from repo metadata alone | https://github.com/patronus-ai/financebench | ? |
| GPT-4-Turbo + shared vector store fails (wrong/refusal) ~81% on human-eval sample; oracle reaches ~85% success | **Y** | Stated in abstract/main text and in the “Model performance” discussion | Consistent with the paper PDF text (Table 2 discussion, Figure 2) | https://arxiv.org/pdf/2311.11944.pdf | ok |

### Disconfirming Evidence Search

| Claim | Counterevidence Found | Alternative Explanation | Search Notes |
|-------|----------------------|-------------------------|--------------|
| “Current LLM+retrieval systems fail frequently on financial QA” | Many vendor blogs report much higher “FinanceBench accuracy” numbers, often with LLM-as-judge and unclear protocol | “Accuracy” claims may differ by subset, corpus scope, allowed tools, and judging strictness; direct comparison often invalid | Searched for “FinanceBench accuracy 90%” style claims; most were marketing-style and did not match the paper’s human-eval protocol |
| “Retrieval correctness is critical” | Some failures appear to be reasoning/numerical errors even when evidence is present | The task is jointly retrieval + numerical reasoning + instruction following; improving retrieval alone may not close the gap | Interpreted from paper discussion of incorrect answers vs refusals and limitations |

### Evidence Assessment
- **Strengths**: explicit benchmark framing; clear statement of failure modes; human evaluation on a sizable cross-product of configs (n=2,400 judgments).
- **Weaknesses**: sample-based evaluation; comparisons with later, non-identical protocols are easy to misinterpret.

### Credence Assessment
- **Overall Credence**: 0.75
- **Reasoning**: Direct primary-source paper; key quantitative claims are inspectable in the PDF; remaining uncertainty is generalizability and protocol matching for comparisons.

## Stage 3: Dialectical Analysis

### Steelmanned Argument
Finance requires high precision and auditability; therefore, domain-specific benchmarks with evidence strings and human evaluation are necessary to prevent overconfidence in RAG systems and to quantify progress under realistic constraints.

### Strongest Counterarguments
1. The evaluated “enterprise-realistic” configurations may underutilize domain-specific tooling (tables, parsers, deterministic calculators) that materially changes performance.
2. A 150-case sample may not reflect the distribution of real analyst questions and workflows (selection effects).

### Synthesis Notes
Use FinanceBench as a **baseline anchor** when evaluating “vectorless RAG” performance claims: require protocol matching (corpus scope, subset, and judging method) before interpreting headline accuracy.

### Claim Summary

| ID | Type | Domain | Evidence | Credence | Claim |
|----|------|--------|----------|----------:|-------|
| TECH-2026-015 | [F] | TECH | E2 | 0.90 | FinanceBench comprises 10,231 open-book financial QA questions with answers and evidence strings; an open-source evaluation subset of 150 cases is available |
| TECH-2026-016 | [F] | TECH | E2 | 0.85 | On the FinanceBench human-eval sample (n=150), GPT-4-Turbo + shared vector store fails (wrong/refusal) ~81%; oracle with evidence pages achieves ~85% success |

### Claims to Register

```yaml
sources:
  - id: "islam-2023-financebench"
    type: "PAPER"
    title: "FinanceBench: A New Benchmark for Financial Question Answering"
    author:
      - "Pranab Islam"
      - "Anand Kannappan"
      - "Douwe Kiela"
      - "Rebecca Qian"
      - "Nino Scherrer"
      - "Bertie Vidgen"
    year: 2023
    url: "https://arxiv.org/abs/2311.11944"
    accessed: "2026-01-24"
    status: "analyzed"
    analysis_file: "analysis/sources/islam-2023-financebench.md"
    reliability: 0.75
    bias_notes: >-
      Benchmark/measurement work from authors affiliated with Patronus AI / Contextual AI / Stanford; strong
      incentives to highlight failure modes and need for better evaluation. Dataset licensing terms are not
      clearly visible from the paper itself; treat “open-source” as “publicly available” unless licensing is verified.
    topics: ["finance", "benchmark", "rag", "retrieval", "evaluation"]
    domains: ["TECH"]
    claims_extracted: ["TECH-2026-015", "TECH-2026-016"]

claims:
  - id: "TECH-2026-015"
    text: >-
      FinanceBench comprises 10,231 open-book financial QA questions with corresponding answers and evidence
      strings, and the authors provide an open-source evaluation subset of 150 cases.
    type: "[F]"
    domain: "TECH"
    evidence_level: "E2"
    credence: 0.90
    source_ids: ["islam-2023-financebench"]
    operationalization: >-
      Inspect the public FinanceBench release to confirm total question count, schema (answers + evidence strings),
      and availability of the 150-case evaluation subset.
    assumptions:
      - The public release corresponds to the dataset described in the paper.
    falsifiers:
      - Public release does not contain the claimed counts or lacks evidence strings/labels described in the paper.

  - id: "TECH-2026-016"
    text: >-
      On the FinanceBench human-evaluated sample (n=150), GPT-4-Turbo with a shared vector store retrieval setup
      incorrectly answered or refused to answer about 81% of questions, while an oracle setup with access to evidence
      pages achieved about 85% success.
    type: "[F]"
    domain: "TECH"
    evidence_level: "E2"
    credence: 0.85
    source_ids: ["islam-2023-financebench"]
    operationalization: >-
      Reproduce the paper’s evaluation setup and compute refusal + incorrect rates and oracle success on the same
      150-case sample.
    assumptions:
      - The paper’s evaluation prompts/configs are implemented as described.
    falsifiers:
      - A faithful reproduction yields materially different failure/success rates for the stated configurations.
```

---
**Analysis Date**: 2026-01-24
**Analyst**: gpt-5.2
**Credence in Analysis**: 0.75

