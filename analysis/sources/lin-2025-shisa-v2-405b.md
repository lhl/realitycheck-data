# Source Analysis: Shisa V2 405B (model release post)

> **Claim types**: `[F]` fact, `[T]` theory, `[H]` hypothesis, `[P]` prediction, `[A]` assumption, `[C]` counterfactual, `[S]` speculation, `[X]` contradiction  
> **Evidence**: **E1** systematic review/meta-analysis; **E2** peer-reviewed/official stats; **E3** expert consensus/preprint; **E4** credible journalism/industry; **E5** opinion/anecdote; **E6** unsupported/speculative

## Metadata

| Field | Value |
|---|---|
| **Source ID** | `lin-2025-shisa-v2-405b` |
| **Title** | Shisa V2 405B: Japan’s Highest Performing LLM |
| **Author(s)** | Leonard Lin |
| **Date** | 2025-06-03 |
| **Type** | BLOG |
| **URL** | https://shisa.ai/posts/shisa-v2-405b/ |
| **Reliability** | 0.68 |
| **Rigor Level** | `[REVIEWED]` |
| **Bias Notes** | First-party model release and positioning (“highest performing LLM ever trained in Japan”). High bias risk for comparative claims vs frontier models and for national “best” framing; moderate reliability for technical lineage (base model) and for references to published evaluation tables on the model card. |

**Claims YAML**: [`analysis/sources/lin-2025-shisa-v2-405b.yaml`](lin-2025-shisa-v2-405b.yaml)

## Stage 1: Descriptive Analysis

### Core Thesis
Shisa V2 405B is a large JA/EN-centric open model (based on Llama 3.1 405B) that the authors claim is exceptionally strong on Japanese evaluations, competitive with leading frontier models, and evidence that small Japan-based labs can reach top-tier performance.

### Summary (Neutral)
The post announces a new Shisa V2 family member built from the Llama 3.1 405B Instruct base model. It claims substantially higher training compute than the team’s 70B model, and argues that performance improvements are visible across the team’s evaluation suite, including Japanese MT-Bench and other English/Japanese benchmarks. The post also motivates the work in the context of “sovereign AI” and open-source AI development.

It highlights that common Japanese eval suites may miss important downstream use cases, and reiterates the importance of Shisa’s own evaluation tooling and benchmarks (including the translation benchmark later released as JP-TL-Bench). It points readers to the Hugging Face model card for the full score table.

### Key Claims

| # | Claim | Claim ID | Type | Domain | Evid | Credence | Verified? | Falsifiable By |
|---:|---|---|---|---|---|---:|---|---|
| 1 | Shisa V2 405B is based on `meta-llama/Llama-3.1-405B-Instruct` and uses the Shisa V2 post-training data mix (plus some extra KO/ZH-TW data) | TECH-2026-060 | [F] | TECH | E4 | 0.80 | ok | Model card does not list the base model lineage/dataset mix |
| 2 | Training Shisa V2 405B required >50× compute vs the 70B version for SFT+DPO | TECH-2026-061 | [F] | TECH | E5 | 0.55 | ? | Compute accounting contradicts the claimed magnitude difference |
| 3 | Shisa V2 405B outperforms GPT‑4 (0613) and GPT‑4 Turbo (2024‑04‑09) on the authors’ JA/EN eval suites and is competitive with GPT‑4o and DeepSeek‑V3 on JA MT‑Bench | TECH-2026-062 | [H] | TECH | E4 | 0.50 | ? | Independent replication or matched-eval comparisons refute the stated ranking/competitiveness |
| 4 | Common Japanese evals miss downstream use cases; custom Japanese evals (incl. translation) are needed to track real-world performance | TECH-2026-063 | [A] | TECH | E5 | 0.60 | ? | Evidence that existing public Japanese evals already capture the claimed downstream phenomena adequately |
| 5 | The full detailed score table is published on the Shisa V2 405B model card | TECH-2026-064 | [F] | TECH | E2 | 0.95 | ok | Model card lacks the promised full table |

### Argument Structure

```
(1) Japan needs strong, open models (sovereign AI framing)
        ↓
(2) Scaling post-training to 405B yields large gains
        ↓
(3) Eval suite shows competitiveness with frontier models
        ↓
Conclusion: Shisa V2 405B is a top-tier Japan-trained LLM and open-source path works
```

### Theoretical Lineage
- Scaling and post-training of instruction-tuned LLMs.
- MT/Japanese eval critique: standard suites may not capture key Japanese downstream tasks.

### Scope & Limitations
- The “highest performing” claim is ambiguous without a clear benchmark set and matched evaluation conditions.
- Many comparisons are based on the authors’ internal eval battery and/or LLM judges.

## Stage 2: Evaluative Analysis

### Internal Coherence
The technical narrative (bigger base model + similar recipe + more compute → better performance) is coherent. The weakness is evidential: without standardized third-party evaluations, “highest performing in Japan” is hard to substantiate and may not be falsifiable unless the benchmark set and evaluation protocols are pinned down.

### Key Factual Claims Verified

| Claim (paraphrased) | Crux? | Source Says | Actual | External Source | Status |
|---|---:|---|---|---|---|
| Base model is Llama 3.1 405B Instruct | **Y** | Uses Llama 3.1 405B Instruct | The Hugging Face model card lists `meta-llama/Llama-3.1-405B-Instruct` as the base model | https://huggingface.co/shisa-ai/shisa-v2-llama3.1-405b | ok |
| Full evaluation table is on the model card | N | “full table … on model card” | The model card includes multiple evaluation tables and comparisons (and is the authoritative place for detailed numbers) | https://huggingface.co/shisa-ai/shisa-v2-llama3.1-405b | ok |

### Disconfirming Evidence Search

| Claim | Counterevidence Found | Alternative Explanation | Search Notes |
|---|---|---|---|
| “Highest performing LLM ever trained in Japan” | “Ever trained in Japan” is hard to define (training location, lab HQ, staff nationality). “Highest performing” depends on benchmark choice and evaluation protocol | The claim may be intended as marketing shorthand: “among open-weight JA-focused models we evaluated” | Considered definitional ambiguity and protocol dependence; would need a pinned benchmark suite and explicit comparison set |

### Evidence Assessment
- Technical lineage claims are reasonably supported via the model card.
- Comparative performance claims remain underdetermined without matched third-party evaluation protocols and public reproduction.

### Credence Assessment
- **Overall Credence**: 0.60  
- **Reasoning**: The factual lineage is credible; the “best in Japan” and frontier comparisons should be treated as tentative marketing claims unless the evaluation protocol is pinned and independently replicated.

## Stage 3: Dialectical Analysis

### Steelmanned Argument
Scaling post-training to frontier-scale open weights can produce models that compete with closed models on the target language (Japanese), and releasing such models helps Japanese-language capability diffuse broadly. Because standard Japanese evals can miss important downstream quality issues, it’s rational to build new evaluations and show improvements on them.

### Strongest Counterarguments
1. **Benchmark arbitrariness**: internal suites can overstate improvements or reflect idiosyncratic preferences.
2. **Comparative claims require matched settings**: “goes toe-to-toe” is not meaningful unless prompts, judges, and datasets are matched and publicly reproducible.

### Supporting Theories

| Theory/Framework | Source ID | How It Supports |
|---|---|---|
| Scaling + post-training improves task performance | `lin-2025-shisa-v2-405b` | Larger base model and more compute plausibly improve Japanese tasks under a consistent recipe |

### Contradicting Theories

| Theory/Framework | Source ID | Point of Conflict |
|---|---|---|
| Public standardized benchmarks should be primary | `lin-2025-shisa-v2-405b` | The post leans on internal eval suites and LLM judges; critics will demand WMT/MQM-style evidence |

### Synthesis Notes
For the JP-TL-Bench story, this post matters mainly because it motivates *why* Shisa built a translation benchmark (to differentiate close ablations) and because it provides a concrete anchor-model context (`shisa-v2-llama3.1-405b` appears in JP-TL-Bench’s base set).

### Claims to Cross-Reference
- Cross-reference Shisa 405B translation performance via JP-TL-Bench and compare to TranslateGemma and LiquidAI LFM2 models.

---

### Claim Summary

| ID | Type | Domain | Evidence | Credence | Claim |
|---|---|---|---|---:|---|
| TECH-2026-060 | [F] | TECH | E4 | 0.80 | Shisa V2 405B is based on Llama 3.1 405B Instruct and uses the Shisa V2 post-training mix (plus extra KO/ZH-TW data) |
| TECH-2026-061 | [F] | TECH | E5 | 0.55 | Training Shisa V2 405B required >50× compute vs the 70B version for SFT+DPO |
| TECH-2026-062 | [H] | TECH | E4 | 0.50 | Shisa V2 405B outperforms GPT‑4 (0613)/GPT‑4 Turbo and is competitive with GPT‑4o/DeepSeek‑V3 on Japanese benchmarks (per authors’ evals) |
| TECH-2026-063 | [A] | TECH | E5 | 0.60 | Common Japanese evals miss downstream use cases; custom Japanese evals (incl. translation) are needed |
| TECH-2026-064 | [F] | TECH | E2 | 0.95 | The full detailed evaluation table is published on the Shisa V2 405B model card |

---

**Analysis Date**: 2026-01-24  
**Analyst**: gpt-5.2  
**Credence in Analysis**: 0.60

