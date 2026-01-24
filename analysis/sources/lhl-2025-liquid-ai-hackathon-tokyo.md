# Source Analysis: `lhl/liquid-ai-hackathon-tokyo` (JA↔EN MT evaluation workflow)

> **Claim types**: `[F]` fact, `[T]` theory, `[H]` hypothesis, `[P]` prediction, `[A]` assumption, `[C]` counterfactual, `[S]` speculation, `[X]` contradiction  
> **Evidence**: **E1** systematic review/meta-analysis; **E2** peer-reviewed/official stats; **E3** expert consensus/preprint; **E4** credible journalism/industry; **E5** opinion/anecdote; **E6** unsupported/speculative

## Metadata

| Field | Value |
|---|---|
| **Source ID** | `lhl-2025-liquid-ai-hackathon-tokyo` |
| **Title** | Liquid AI Hackathon Tokyo (repo) |
| **Author(s)** | lhl (GitHub) |
| **Date** | 2025 |
| **Type** | KNOWLEDGE |
| **URL** | https://github.com/lhl/liquid-ai-hackathon-tokyo |
| **Reliability** | 0.78 |
| **Rigor Level** | `[REVIEWED]` |
| **Bias Notes** | First-party repo documenting an evaluation workflow and research notes. High reliability for “how this repo’s workflow works” claims; moderate bias risk in interpretive conclusions about model quality unless backed by published run artifacts. |

**Claims YAML**: [`analysis/sources/lhl-2025-liquid-ai-hackathon-tokyo.yaml`](lhl-2025-liquid-ai-hackathon-tokyo.yaml)

## Stage 1: Descriptive Analysis

### Core Thesis
The repo documents a practical evaluation stack for JA↔EN MT (built around llm-jp-eval and COMET), highlights limitations of standard MT metrics for Japanese, and captures operational lessons from running large-scale evaluations.

### Summary (Neutral)
This repository is a hackathon project focused on evaluating (and potentially adapting) LiquidAI’s translation-capable models for JA↔EN. The repo includes:
- A workflow for running the llm-jp-eval MT suite (ALT + WikiCorpus, both directions) with deterministic preprocessing and prompt construction.
- Research notes analyzing dataset properties, prompts (few-shot vs zero-shot), metric computation (BLEU, BERTScore, COMET WMT22), and operational issues (COMET GPU execution, OpenAI batch throughput).
- Prompt template tweaks for models expecting chat-style formats (e.g., an `lfm2` template).

The repo frames COMET as the headline metric for aggregated MT scoring while acknowledging limitations and the need for better significance testing and complementary evaluations.

### Key Claims

| # | Claim | Claim ID | Type | Domain | Evid | Credence | Verified? | Falsifiable By |
|---:|---|---|---|---|---|---:|---|---|
| 1 | The workflow evaluates four llm-jp-eval MT datasets (ALT and WikiCorpus in both directions) and uses COMET WMT22 as the headline metric for aggregation | TECH-2026-070 | [F] | TECH | E2 | 0.85 | ok | Repo does not use COMET as headline MT metric / does not use these datasets |
| 2 | ALT is evaluated with 4 few-shot exemplars while WikiCorpus is zero-shot; this can introduce few-shot asymmetry and bias comparisons | TECH-2026-071 | [F] | TECH | E2 | 0.85 | ok | Underlying pipeline uses matched prompting (both few-shot or both zero-shot) |
| 3 | COMET provides more spread than BLEU/BERTScore but can still cluster strong systems; confidence intervals / paired tests are needed for tight races | TECH-2026-072 | [H] | TECH | E5 | 0.60 | ? | Evidence that point estimates are sufficient and COMET variance is negligible for model selection |
| 4 | COMET may have weaker calibration for Japanese and can reward fluent hallucinations or penalize valid paraphrases; complementary checks are valuable | TECH-2026-073 | [H] | TECH | E5 | 0.55 | ? | Evidence that COMET WMT22 is well-calibrated for Japanese across domains and robust to hallucinations |
| 5 | The repo adds an `lfm2` prompt template to better match models expecting chat-style prompts for translation | TECH-2026-074 | [F] | TECH | E2 | 0.85 | ok | No such template exists or it does not affect prompt formatting |

### Argument Structure

```
(1) Need a scalable JA↔EN MT eval workflow
        ↓
(2) llm-jp-eval provides datasets + metrics (COMET-centered)
        ↓
(3) Operational + methodological caveats remain (prompt asymmetry, metric clustering)
        ↓
Conclusion: use the workflow, but add statistical rigor and complementary evals
```

### Theoretical Lineage
- WMT-style learned metrics (COMET) and their limitations.
- Practical benchmarking: prompt/normalization choices materially affect results.

### Scope & Limitations
- This is primarily a workflow and research-notes repo; not all claims are backed by published run artifacts in this source alone.
- The focus is evaluation engineering rather than MT theory.

## Stage 2: Evaluative Analysis

### Internal Coherence
The repo’s conclusions are internally consistent: if (a) metrics cluster and (b) prompts differ across datasets (few-shot vs zero-shot), then (c) comparisons can be noisy and require statistical and methodological care. The operational notes about COMET GPU behavior and large runs are plausible and actionable.

### Key Factual Claims Verified

| Claim (paraphrased) | Crux? | Source Says | Actual | External Source | Status |
|---|---:|---|---|---|---|
| llm-jp-eval MT stack uses COMET WMT22 and logs BLEU/BERTScore; COMET is the headline aggregation metric | **Y** | Documented in repo research notes | Repo’s `RESEARCH.llm-jp-eval-mt-analysis.md` states COMET WMT22 is headline and points to llm-jp-eval metric code paths | https://github.com/lhl/liquid-ai-hackathon-tokyo | ok |
| ALT uses 4-shot examples while WikiCorpus is zero-shot | **Y** | Documented | Repo research notes describe ALT exemplar injection vs WikiCorpus zero-shot (`run-mt.py` + dataset definitions) | https://github.com/lhl/liquid-ai-hackathon-tokyo | ok |
| `lfm2` prompt template exists for chat-style prompting | N | Mentioned | Repo contains `--prompt-template lfm2` and Jinja templates for Meta-style chat formatting (per research notes) | https://github.com/lhl/liquid-ai-hackathon-tokyo | ok |

### Disconfirming Evidence Search

| Claim | Counterevidence Found | Alternative Explanation | Search Notes |
|---|---|---|---|
| “COMET calibration dips on Japanese” | COMET variants differ; some may be better calibrated on JA; domain and reference quality matter | The issue may be less “Japanese” and more “high-quality regime + paraphrase flexibility + reference limitations” | Compared the repo’s cautionary notes to broader MT metric critique (also raised in JP-TL-Bench paper) |

### Evidence Assessment
- Strong for workflow mechanics and code-referenced claims.
- Moderate for metric calibration claims (plausible but needs external validation and quantitative audits).

### Credence Assessment
- **Overall Credence**: 0.72  
- **Reasoning**: The source is an engineering notebook with direct pointers to code paths; interpretive claims should be validated with controlled experiments and published artifacts.

## Stage 3: Dialectical Analysis

### Steelmanned Argument
If you want to evaluate translation at scale across thousands of examples, you need an automated metric pipeline. llm-jp-eval + COMET provides that, but Japanese introduces prompt- and context-sensitive failure modes, and small metric deltas are often not decision-grade without statistics and qualitative audits.

### Strongest Counterarguments
1. For some use cases, COMET on large datasets may be sufficient; adding more complex protocols (LLM judges, MQM) increases cost without proportional benefit.
2. The repo’s cautions may overgeneralize from a limited set of models or runs.

### Supporting Theories

| Theory/Framework | Source ID | How It Supports |
|---|---|---|
| COMET as scalable proxy for human judgments | `lhl-2025-liquid-ai-hackathon-tokyo` | Motivates COMET-centric evaluation for large-scale MT comparisons |

### Contradicting Theories

| Theory/Framework | Source ID | Point of Conflict |
|---|---|---|
| Pairwise LLM-judge ranking as primary | `lhl-2025-liquid-ai-hackathon-tokyo` | Repo treats COMET as headline; JP-TL-Bench argues for pairwise discrimination at top-end quality |

### Synthesis Notes
This repo is a useful comparator to JP-TL-Bench: it represents the “COMET-centered large-scale MT suite” approach. A synthesis should clarify when to prefer each: JP-TL-Bench for iteration among high-quality variants; llm-jp-eval for broad regression detection and large-sample stability.

### Claims to Cross-Reference
- Compare the same model set under both JP-TL-Bench LT and llm-jp-eval COMET to see where they agree/disagree.

---

### Claim Summary

| ID | Type | Domain | Evidence | Credence | Claim |
|---|---|---|---|---:|---|
| TECH-2026-070 | [F] | TECH | E2 | 0.85 | The repo evaluates ALT/WikiCorpus (both directions) and uses COMET WMT22 as headline MT metric |
| TECH-2026-071 | [F] | TECH | E2 | 0.85 | ALT is 4-shot while WikiCorpus is zero-shot, creating few-shot asymmetry risk |
| TECH-2026-072 | [H] | TECH | E5 | 0.60 | COMET still clusters strong systems; significance tests are needed for tight races |
| TECH-2026-073 | [H] | TECH | E5 | 0.55 | COMET may have weaker calibration for Japanese and can miss hallucinations/paraphrases |
| TECH-2026-074 | [F] | TECH | E2 | 0.85 | The repo adds an `lfm2` prompt template for chat-style translation prompting |

---

**Analysis Date**: 2026-01-24  
**Analyst**: gpt-5.2  
**Credence in Analysis**: 0.72

