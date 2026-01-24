# Source Analysis: Shisa V2 (model release post)

> **Claim types**: `[F]` fact, `[T]` theory, `[H]` hypothesis, `[P]` prediction, `[A]` assumption, `[C]` counterfactual, `[S]` speculation, `[X]` contradiction  
> **Evidence**: **E1** systematic review/meta-analysis; **E2** peer-reviewed/official stats; **E3** expert consensus/preprint; **E4** credible journalism/industry; **E5** opinion/anecdote; **E6** unsupported/speculative

## Metadata

| Field | Value |
|---|---|
| **Source ID** | `lin-2025-shisa-v2` |
| **Title** | Shisa V2 |
| **Author(s)** | Leonard Lin |
| **Date** | 2025-04-14 |
| **Type** | BLOG |
| **URL** | https://shisa.ai/posts/shisa-v2/ |
| **Reliability** | 0.70 |
| **Rigor Level** | `[REVIEWED]` |
| **Bias Notes** | First-party model release post for Shisa.AI. High bias risk for “SOTA”/comparative performance claims; moderate reliability for factual model lineup and licensing claims, especially where corroborated by model cards. |

**Claims YAML**: [`analysis/sources/lin-2025-shisa-v2.yaml`](lin-2025-shisa-v2.yaml)

## Stage 1: Descriptive Analysis

### Core Thesis
Shisa V2 is a family of open-weight JA/EN bilingual models (7B–70B) that achieves strong Japanese benchmark performance across size classes and is intended for real-world Japanese-language use.

### Summary (Neutral)
The post announces the Shisa V2 model family and emphasizes performance gains on Japanese benchmarks relative to base models, across multiple sizes and base-model licenses. It frames these gains as coming from improved data and post-training rather than continued pretraining or tokenizer extension. The post also highlights a commitment to releasing models under permissive licenses where the base model allows, and previews internal benchmarks designed to better measure Japanese real-world use cases, including a translation benchmark (later released as JP-TL-Bench).

### Key Claims

| # | Claim | Claim ID | Type | Domain | Evid | Credence | Verified? | Falsifiable By |
|---:|---|---|---|---|---|---:|---|---|
| 1 | Shisa V2 is a family of JA/EN bilingual chat models spanning ~7B–70B parameters with published JA AVG / EN AVG scores per model | TECH-2026-059 | [F] | TECH | E4 | 0.85 | ok | Model cards do not list the lineup and the claimed average scores |
| 2 | The post claims Shisa V2 sets SOTA (or near-SOTA) Japanese benchmark performance across size classes | TECH-2026-055 | [H] | TECH | E4 | 0.55 | ? | Independent benchmark comparisons show multiple open models dominate Shisa V2 across relevant Japanese evaluations for the same sizes |
| 3 | Shisa V2 reports large JA performance lifts vs base models (e.g., +32.6% for Llama 3.1 8B class) | TECH-2026-056 | [F] | TECH | E4 | 0.65 | ? | Reanalysis under matched evaluation settings shows materially smaller or inconsistent gains |
| 4 | Shisa V2 developed new Japanese evaluations targeting downstream use cases, including a translation benchmark later open-sourced as JP-TL-Bench | TECH-2026-057 | [F] | TECH | E4 | 0.75 | ? | No evidence of the described new evaluations existing or being used in development |
| 5 | Shisa V2 prioritizes permissive licensing (Apache 2.0 / MIT) where base model licenses allow | TECH-2026-058 | [F] | TECH | E4 | 0.80 | ok | Model releases are not under the stated permissive licenses where possible |

### Argument Structure

```
(1) Baseline JP capability improved but gaps remain
        ↓
(2) Post-training + refined data can close gaps across sizes
        ↓
(3) Shisa V2 shows large benchmark uplifts and robust scaling
        ↓
Conclusion: Shisa V2 offers strong open JA/EN models for real-world use
```

### Theoretical Lineage
- Open-weight model improvement via data curation + post-training (SFT/DPO/RL-like stages).
- Evaluation critique: standard Japanese evals may miss real-world tasks (roleplay, instruction following, translation).

### Scope & Limitations
- This is a release announcement, not a peer-reviewed audit.
- Performance claims depend on the authors’ evaluation suite and model-judge choices.

## Stage 2: Evaluative Analysis

### Internal Coherence
The post’s internal story (“data + post-training can yield broad gains without continued pretraining”) is plausible and consistent with contemporary LLM development. The key uncertainty is comparability: what benchmarks were used, how were they scored, and how representative are they of deployed use cases?

### Key Factual Claims Verified

| Claim (paraphrased) | Crux? | Source Says | Actual | External Source | Status |
|---|---:|---|---|---|---|
| Shisa V2 publishes a lineup with JA AVG / EN AVG values per model size | **Y** | Table in the blog post | The Shisa V2 model card includes the same lineup and JA/EN averages (e.g., Llama3.3-70B: JA AVG 79.72, EN AVG 67.71) | https://huggingface.co/shisa-ai/shisa-v2-llama3.3-70b | ok |
| Shisa V2 releases models under licenses constrained by base models (Apache/MIT where possible) | N | “permissive where possible” | The lineup table in the model card includes license labels per model (Apache 2.0 / MIT / Llama) consistent with base constraints | https://huggingface.co/shisa-ai/shisa-v2-llama3.3-70b | ok |

### Disconfirming Evidence Search

| Claim | Counterevidence Found | Alternative Explanation | Search Notes |
|---|---|---|---|
| “SOTA across all size classes” | “SOTA” is benchmark- and date-dependent; other Japanese-focused labs (e.g., domestic Japanese model efforts) may lead on some tasks | Shisa may be SOTA on their chosen suite and slices, but not globally across all Japanese tasks | Considered that the post references internal “new evals” not widely standardized; comparability to public leaderboards can be limited |

### Evidence Assessment
- Stronger for lineup/licensing (public model cards).
- Weaker for broad “SOTA” and “real-world” claims without third-party replication and clarity about evaluation protocols.

### Credence Assessment
- **Overall Credence**: 0.65  
- **Reasoning**: Factual release details are corroborated; comparative claims should be treated as provisional and protocol-specific.

## Stage 3: Dialectical Analysis

### Steelmanned Argument
If you care about Japanese capability in open models, baseline multilingual LLMs often underperform on culturally and linguistically grounded Japanese tasks. A targeted post-training pipeline guided by a broad Japanese eval battery can systematically raise performance across sizes without needing expensive continued pretraining.

### Strongest Counterarguments
1. **Benchmark overfitting / protocol dependence**: “JA AVG” is a composite that may not reflect production tasks; LLM-judge benchmarks can be biased.
2. **SOTA ambiguity**: Claims of “SOTA” require precise benchmark definitions and matched evaluation conditions.

### Supporting Theories

| Theory/Framework | Source ID | How It Supports |
|---|---|---|
| Post-training-driven gains | `lin-2025-shisa-v2` | Explains how a family of models can see consistent improvements across sizes |
| Task-specific evaluation design | `lin-2025-shisa-v2` | Motivates building evaluations that target real-world Japanese tasks (incl. translation) |

### Contradicting Theories

| Theory/Framework | Source ID | Point of Conflict |
|---|---|---|
| “Only continued pretraining moves the needle” | `lin-2025-shisa-v2` | Shisa argues post-training + data suffices for large gains on Japanese tasks |

### Synthesis Notes
This source is primarily context: JP-TL-Bench is presented as one of the “missing evals” for Japanese downstream tasks. The strongest actionable claims here are the published lineup and licensing; performance assertions should be triangulated with independent benchmarks and with JP-TL-Bench + llm-jp-eval results.

### Claims to Cross-Reference
- Compare Shisa V2 translation performance on JP-TL-Bench vs COMET-centered llm-jp-eval MT.

---

### Claim Summary

| ID | Type | Domain | Evidence | Credence | Claim |
|---|---|---|---|---:|---|
| TECH-2026-055 | [H] | TECH | E4 | 0.55 | Shisa V2 is SOTA/near-SOTA on Japanese benchmarks across size classes |
| TECH-2026-056 | [F] | TECH | E4 | 0.65 | Shisa V2 reports large JA benchmark lifts vs base models (e.g., +32.6% for Llama 3.1 8B class) |
| TECH-2026-057 | [F] | TECH | E4 | 0.75 | Shisa V2 developed new Japanese evaluations including a translation benchmark later open-sourced as JP-TL-Bench |
| TECH-2026-058 | [F] | TECH | E4 | 0.80 | Shisa V2 prioritizes permissive licensing (Apache 2.0 / MIT) where base licenses allow |
| TECH-2026-059 | [F] | TECH | E4 | 0.85 | Shisa V2 publishes a JA/EN lineup spanning 7B–70B with reported JA AVG / EN AVG values |

---

**Analysis Date**: 2026-01-24  
**Analyst**: gpt-5.2  
**Credence in Analysis**: 0.65

