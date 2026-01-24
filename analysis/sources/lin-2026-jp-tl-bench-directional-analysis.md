# Source Analysis: JP-TL-Bench “Why Translation Direction Matters” (JA↔EN)

> **Claim types**: `[F]` fact, `[T]` theory, `[H]` hypothesis, `[P]` prediction, `[A]` assumption, `[C]` counterfactual, `[S]` speculation, `[X]` contradiction  
> **Evidence**: **E1** systematic review/meta-analysis; **E2** peer-reviewed/official stats; **E3** expert consensus/preprint; **E4** credible journalism/industry; **E5** opinion/anecdote; **E6** unsupported/speculative

## Metadata

| Field | Value |
|---|---|
| **Source ID** | `lin-2026-jp-tl-bench-directional-analysis` |
| **Title** | JP-TL-Bench: Why Translation Direction Matters (JA↔︎EN) |
| **Author(s)** | Leonard Lin |
| **Date** | 2026-01-12 |
| **Type** | BLOG |
| **URL** | https://shisa.ai/posts/jp-tl-bench-directional-analysis/ |
| **Reliability** | 0.74 |
| **Rigor Level** | `[REVIEWED]` |
| **Bias Notes** | First-party analysis using the authors’ own benchmark outputs. Strong for concrete numeric claims that can be checked against published artifacts; higher bias risk for interpretation of qualitative examples (selected excerpts) and implied generalization beyond the base set. |

**Claims YAML**: [`analysis/sources/lin-2026-jp-tl-bench-directional-analysis.yaml`](lin-2026-jp-tl-bench-directional-analysis.yaml)

## Stage 1: Descriptive Analysis

### Core Thesis
For Japanese↔English MT, many models are directionally asymmetric (EN→JA vs JA→EN) and difficulty-dependent; aggregating into one score can hide large capability gaps that matter in production.

### Summary (Neutral)
The post follows the JP-TL-Bench release and drills into one specific empirical observation: some models perform well in one translation direction but poorly in the reverse direction. It uses Base Set v1.0 scores (Gemini-2.5-Flash judge) and qualitative output excerpts to illustrate the kinds of errors that appear when a model is “good enough” in one direction but fails in the other.

The post provides a small table of example directional gaps (e.g., Llama 3.1 8B and Swallow v0.5) and argues that JP-TL-Bench’s slice reporting (direction × difficulty) makes these failure modes visible and actionable.

### Key Claims

| # | Claim | Claim ID | Type | Domain | Evid | Credence | Verified? | Falsifiable By |
|---:|---|---|---|---|---|---:|---|---|
| 1 | Translation direction matters substantially for many models; a single “JA↔EN score” hides large asymmetries | TECH-2026-045 | [T] | TECH | E4 | 0.75 | ? | Large-scale evaluation showing direction gaps are consistently negligible for JA↔EN across model families |
| 2 | Llama 3.1 8B scores ~4.52 on JA→EN but ~1.40 on EN→JA on Base Set v1.0 (Gemini-2.5-Flash judge) | TECH-2026-046 | [F] | TECH | E2 | 0.95 | ok | Base set score report shows materially different slice scores |
| 3 | Swallow v0.5 shows the opposite pattern (~8.80 EN→JA vs ~5.96 JA→EN) | TECH-2026-047 | [F] | TECH | E2 | 0.95 | ok | Base set score report contradicts the reported slice scores |
| 4 | LFM2-2.6B has a notable Easy/Hard gap on EN→JA (e.g., ~6.38 easy vs ~4.06 hard) | TECH-2026-048 | [F] | TECH | E2 | 0.95 | ok | Base set score report contradicts the reported slice scores |
| 5 | JP-TL-Bench supports slice reporting by direction and difficulty, enabling targeted debugging of failure modes | TECH-2026-049 | [F] | TECH | E2 | 0.90 | ok | Benchmark artifacts do not include slice-level scores |

### Argument Structure

```
(1) JA↔EN translation contains asymmetric challenges
        ↓
(2) Models often learn these asymmetrically (data/prompt/tokenization/training)
        ↓
(3) Aggregate scores hide asymmetry
        ↓
Conclusion: evaluate direction × difficulty slices and inspect outputs
```

### Theoretical Lineage
- Prior work on directionality and domain effects in MT evaluation.
- Document/context sensitivity: direction differences can manifest through pro-drop/honorific control, among other phenomena.

### Scope & Limitations
- The quantitative evidence is bounded by Base Set v1.0 and the chosen judge model.
- The qualitative examples are illustrative but cherry-pick risk is real (stronger evidence is distributional analysis across many items/models).

## Stage 2: Evaluative Analysis

### Internal Coherence
The argument is plausible and matches known MT behavior: translation directions can differ due to training data balance, tokenization efficiency, and modeling of target-language generation constraints (e.g., producing appropriate Japanese register vs producing fluent English). The post’s strongest support is the concrete slice-score artifacts.

### Key Factual Claims Verified

| Claim (paraphrased) | Crux? | Source Says | Actual | External Source | Status |
|---|---:|---|---|---|---|
| Llama 3.1 8B slice scores: JA→EN ~4.52, EN→JA ~1.40 | **Y** | Reported in the post | Confirmed in `baseset/v1.0/reports/base_set.gemini-2.5-flash_scores.json` | https://github.com/shisa-ai/jp-tl-bench | ok |
| Swallow v0.5 slice scores: EN→JA ~8.80, JA→EN ~5.96 | N | Reported in the post | Confirmed in the same base set score report | https://github.com/shisa-ai/jp-tl-bench | ok |
| LFM2-2.6B EN→JA easy/hard gap: ~6.38 vs ~4.06 | N | Reported in the post | Confirmed in the same base set score report | https://github.com/shisa-ai/jp-tl-bench | ok |

### Disconfirming Evidence Search

| Claim | Counterevidence Found | Alternative Explanation | Search Notes |
|---|---|---|---|
| “Direction matters a lot for JA↔EN in general” | Some model families (especially explicitly bilingual/translation-trained) may be more balanced; direction gaps may shrink with better prompting or longer context | The observed asymmetries may be partially *prompt-protocol artifacts* rather than “intrinsic capability” | Compared the post’s narrative to the benchmark’s multiple prompt variants (full vs low vs ultra-low context) and noted protocol sensitivity as a likely moderator |

### Evidence Assessment
- Numeric slice-score claims are strongly supported by public artifacts.
- Generalizations about “many models” and mechanisms need broader sampling and controls (judge choice, prompt style, domain shift).

### Credence Assessment
- **Overall Credence**: 0.78  
- **Reasoning**: Verified slice-score claims are solid; the broader “direction matters for many models” claim is likely true but degree varies by model and prompting.

## Stage 3: Dialectical Analysis

### Steelmanned Argument
If you’re building a translation system, you must ship both directions (user text → translated output). A model that looks “fine” on an aggregate metric might still be unusable for EN→JA in real contexts because it chooses wrong register/honorifics or loses nuance, while being perfectly adequate for JA→EN. Slice-wise evaluation reveals these gaps and prevents false confidence.

### Strongest Counterarguments
1. **Judge + prompt dependence**: A direction gap could shrink or reverse under different prompting or a different judge; so the observed asymmetry may not reflect user outcomes.
2. **Selection bias**: Highlighted examples can overstate the importance of directionality if they focus on hard items.

### Supporting Theories

| Theory/Framework | Source ID | How It Supports |
|---|---|---|
| Slice-wise benchmarking (direction × difficulty) | `lin-2026-jp-tl-bench-directional-analysis` | Directly operationalizes the claim that aggregate scores can hide important failures |

### Contradicting Theories

| Theory/Framework | Source ID | Point of Conflict |
|---|---|---|
| Aggregate single-number metrics as adequate | `lin-2026-jp-tl-bench-directional-analysis` | If aggregate metrics are sufficient, direction-specific diagnostics would rarely change decisions |

### Synthesis Notes
This post provides a compelling “why slices matter” argument with verifiable numerical examples. For stronger external credibility, it would be useful to show judge-sensitivity analyses and/or correlate slice LT with human MQM judgments for a subset of items.

### Claims to Cross-Reference
- Correlate direction-slice LT with COMET (ALT/WikiCorpus) and with human MQM where feasible.

---

### Claim Summary

| ID | Type | Domain | Evidence | Credence | Claim |
|---|---|---|---|---:|---|
| TECH-2026-045 | [T] | TECH | E4 | 0.75 | Translation direction can matter substantially for JA↔EN and a single score can hide asymmetries |
| TECH-2026-046 | [F] | TECH | E2 | 0.95 | Llama 3.1 8B has ~4.52 (JA→EN) vs ~1.40 (EN→JA) on Base Set v1.0 (Gemini-2.5-Flash judge) |
| TECH-2026-047 | [F] | TECH | E2 | 0.95 | Swallow v0.5 has ~8.80 (EN→JA) vs ~5.96 (JA→EN) on Base Set v1.0 |
| TECH-2026-048 | [F] | TECH | E2 | 0.95 | LFM2-2.6B shows an EN→JA Easy/Hard gap (~6.38 vs ~4.06) on Base Set v1.0 |
| TECH-2026-049 | [F] | TECH | E2 | 0.90 | JP-TL-Bench provides slice reporting by direction and difficulty |

---

**Analysis Date**: 2026-01-24  
**Analyst**: gpt-5.2  
**Credence in Analysis**: 0.78

