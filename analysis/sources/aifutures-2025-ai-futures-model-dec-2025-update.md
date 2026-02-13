# Source Analysis: AI Futures Model — Dec 2025 Update

> **Claim types**: `[F]` fact, `[T]` theory, `[H]` hypothesis, `[P]` prediction, `[A]` assumption, `[C]` counterfactual, `[S]` speculation, `[X]` contradiction  
> **Evidence**: **E1** systematic review/meta-analysis; **E2** peer-reviewed/official stats; **E3** expert consensus/preprint/open data; **E4** credible journalism/industry/primary docs; **E5** forecast/analysis; **E6** unsupported/speculative

## Metadata

| Field | Value |
|---|---|
| **Source ID** | `aifutures-2025-ai-futures-model-dec-2025-update` |
| **Title** | AI Futures Model: Dec 2025 Update |
| **Author(s)** | Daniel Kokotajlo; Eli Lifland; Brendan Halstead; Alex Kastner |
| **Date** | 2025-12-31 |
| **Type** | BLOG (model update / methodology) |
| **URL** | https://blog.ai-futures.org/p/ai-futures-model-dec-2025-update |
| **Reliability** | 0.60 |
| **Rigor Level** | [REVIEWED] |
| **Bias Notes** | Produced by the same group that published AI 2027, with an explicit goal of forecasting fast AI timelines and takeoff dynamics. Strengths: unusually explicit operational definitions (AC/SAR/TED-AI/ASI), open acknowledgement of parameter uncertainty, and links to an interactive model site. Risks: (a) heavy reliance on a small set of trend proxies (notably METR time horizon), (b) substantial subjective parameterization (“intuitive guesses”), and (c) potential anchoring to the group’s earlier scenario framing. |

**Claims YAML**: `analysis/sources/aifutures-2025-ai-futures-model-dec-2025-update.yaml`

## Stage 1: Descriptive Analysis

### Core Thesis
The AI Futures Project presents a “unified” timelines + takeoff model (AI Futures Model) forecasting milestone arrival and post-coding-automation takeoff dynamics; they argue the model implies longer timelines than their April 2025 AI 2027-era model (roughly +3–5 years to full coding automation) primarily due to improved modeling of AI R&D automation rather than new empirical evidence.

### Summary (Neutral)
This post:
1) motivates why quantitative modeling is useful given lack of expert consensus and strong framing effects in surveys,
2) situates their approach among other forecasting methods (expert surveys, revenue extrapolation, compute anchored by brain, etc.),
3) introduces their model structure: staged milestones (AC → SAR → … → ASI) and Monte Carlo simulation of parameter uncertainty,
4) defines operational milestones (especially Automated Coder / AC), and
5) reports that improvements to their earlier model lengthen medians by several years.

The model’s early stage is explicitly anchored to **METR time-horizon trends** (agentic coding task length), with later stages modeling R&D automation dynamics (“research taste”) and eventual general-capability milestones (TED‑AI/ASI) via rough translation assumptions. The authors emphasize “all-things-considered” adjustments: they view the model outputs as evidence but allow intuitive overrides for omitted factors.

### Key Claims

| # | Claim | Claim ID | Layer | Actor | Scope | Quantifier | Type | Domain | Evid | Credence | Verified? | Falsifiable By |
|---:|---|---|---|---|---|---|---|---|---|---:|---|---|
| 1 | The authors report a “significant upgrade” to their unified timelines + takeoff model (AI Futures Model), intended to forecast milestone arrival (AC, SAR, TED‑AI, ASI) and takeoff speeds | META-2026-117 | PRACTICED | OTHER:AI Futures Project | who=AI Futures Project; what=model update; when=2025-12 | N/A | [F] | META | E4 | 0.85 | In-source | The post does not actually describe a new model or milestone/takeoff forecasting |
| 2 | They claim the AI Futures Model implies **~3–5 years longer** timelines to full coding automation (AC) than their April 2025 AI 2027-era timelines model, partly due to being less bullish on pre-AC AI R&D speedups | META-2026-118 | ASSERTED | OTHER:AI Futures Project | who=AI Futures Project; what=timeline revision; when=2025-12 | OTHER:+3–5 years | [F] | META | E4 | 0.75 | In-source | The post does not make this comparison or states a materially different shift |
| 3 | They claim the ~3–5 year median shift is **primarily** from improved modeling of AI R&D automation (not new empirical evidence) | META-2026-119 | ASSERTED | OTHER:AI Futures Project | who=AI Futures Project; what=attribution for shift; when=2025-12 | primary | [F] | META | E4 | 0.70 | In-source | The post attributes the shift mainly to new empirical evidence rather than modeling changes |
| 4 | They claim their previous model (median parameters) implied **superhuman coder (SC) medians ~2027–2028**, while the new model implies **~2032** | META-2026-120 | ASSERTED | OTHER:AI Futures Project | who=AI Futures Project; what=SC median comparison; when=2025-12 | OTHER:2027–2028 vs 2032 | [F] | META | E4 | 0.70 | In-source | The post reports materially different SC medians |
| 5 | They operationalize **Automated Coder (AC)** as a system that can fully automate an AGI project’s coding work (replacing the coding staff) using ~5% of the project’s compute supply | META-2026-121 | ASSERTED | OTHER:AI Futures Project | who=AI Futures Project; what=AC definition; where=milestone definitions | OTHER:5% compute | [F] | META | E4 | 0.85 | In-source | The post’s AC definition omits these elements or differs materially |
| 6 | In Eli’s all-things-considered adjustments (in this post), he reports increasing P(AC→ASI <1 year) from **26%→30%** and P(AC→ASI <3 years) from **43%→60%** | TRANS-2026-027 | ASSERTED | OTHER:AI Futures Project | who=Eli; what=takeoff probability adjustments; when=2025-12 | OTHER:26→30; 43→60 | [F] | TRANS | E4 | 0.65 | In-source | The post does not state these probability adjustments |

### Argument Structure

```
(1) Expert disagreement + framing effects → need explicit models
        ↓
(2) Anchor near-term to METR time-horizon trend
        ↓
(3) Model staged milestones (AC → SAR → …) with parameter uncertainty
        ↓
(4) Improved R&D automation modeling → longer coding-automation medians
        ↓
(5) Use all-things-considered adjustments for omitted factors
```

**Weakest links**:
- Mapping “time horizon on an eval suite” → “full coding automation in an AGI project.”
- Modeling “research taste” improvement and its causal impact on takeoff speed (weak direct measurement).

### Theoretical Lineage
- Quantitative trend extrapolation (METR time-horizon) combined with staged “software intelligence explosion” style dynamics.
- Forecast aggregation awareness (explicitly discusses framing effects in expert surveys).

### Scope & Limitations
- The post acknowledges many parameters are “intuitive guesses,” limiting inferential strength.
- The post is a methodology + model update; it is not an independent empirical evaluation of its own assumptions.

## Stage 2: Evaluative Analysis

### Internal Coherence
The post is internally coherent: it argues for explicit models, proposes a staged milestone framework, and acknowledges uncertainty/subjective adjustments. The largest coherence risk is the leap from a proxy trend (time horizon) to a high-level organizational capability (AC), plus the low measurability of “research taste.”

### Key Factual Claims Verified

| Claim (paraphrased) | Crux? | Source Says | Actual | External Source | Status |
|---|---:|---|---|---|---|
| The authors claim a ~3–5 year median shift to coding automation driven mainly by modeling changes | **Y** | “roughly 3–5 year shift … primarily … modeling of AI R&D automation” | Present in the post text | https://blog.ai-futures.org/p/ai-futures-model-dec-2025-update | ok (in-source) |

### Disconfirming Evidence Search

| Claim | Counterevidence Found | Alternative Explanation | Search Notes |
|---|---|---|---|
| METR time horizon trend can be extrapolated as a main driver to AC | METR itself notes protocol/task-suite sensitivity and potential saturation/measurement limits at the frontier. | Time-horizon trends may capture improved scaffolding on curated tasks rather than robust multi-month autonomy in real-world codebases. | Cross-referenced METR TH1.1 update (`metr-2026-time-horizon-1-1`) and its noted sensitivity. |

### Corrections & Updates

| Item | URL | Published | Corrected/Updated | What Changed | Impacted Claim IDs | Action Taken |
|---|---|---:|---:|---|---|---|
| “Added Jan 2026” clarification link in the post | https://blog.ai-futures.org/p/ai-futures-model-dec-2025-update | 2025-12-31 | 2026-01 (in-post note) | Post indicates later clarifications about forecast changes since AI 2027 | META-2026-118; META-2026-119 | Note as potential source of drift vs original post snapshot |

### Evidence Assessment
- Strong for: what the authors claim their model is and how it defines milestones (E4).
- Weak for: whether the model’s structure/parameters are empirically well-grounded (many explicitly are not).

### Credence Assessment
- **Overall Credence**: 0.70 that this post accurately represents the authors’ model updates and definitions; 0.40 that the model’s implied timeline shifts are well-calibrated vs reality.

## Stage 3: Dialectical Analysis

### Steelmanned Argument
The authors are doing unusually transparent forecasting work: they define operational milestones, admit uncertainty, and publish a model that can be critiqued. Updating timelines by multiple years based on recognizing earlier modeling errors is a sign of intellectual honesty, not weakness.

### Strongest Counterarguments
1. **Single-proxy overreliance**: time horizon is informative but may not scale linearly into AC-level organizational replacement.
2. **Taste bottleneck under-measured**: “research taste” is asserted as decisive but lacks clear, stable measurement.

### Synthesis Notes
This post is central to understanding why the AI Futures Project’s internal forecast medians moved later (relative to AI 2027) even without major new empirical evidence: their own story is that improved R&D automation modeling did much of the work.

---

### Claim Summary

| ID | Type | Domain | Layer | Actor | Scope | Quantifier | Evidence | Credence | Claim |
|---|---|---|---|---|---|---|---|---:|---|
| META-2026-117 | [F] | META | PRACTICED | OTHER:AI Futures Project | who=AI Futures Project; what=model update | N/A | E4 | 0.85 | Authors present an upgraded unified timelines + takeoff model. |
| META-2026-118 | [F] | META | ASSERTED | OTHER:AI Futures Project | who=AI Futures Project; what=timeline revision | OTHER:+3–5 years | E4 | 0.75 | Authors claim model implies ~3–5 years longer timelines to AC vs Apr 2025 model. |
| META-2026-119 | [F] | META | ASSERTED | OTHER:AI Futures Project | who=AI Futures Project; what=attribution | primary | E4 | 0.70 | Authors claim the shift is mainly from improved R&D automation modeling, not new evidence. |
| META-2026-120 | [F] | META | ASSERTED | OTHER:AI Futures Project | who=AI Futures Project; what=SC median comparison | OTHER:2027–2028 vs 2032 | E4 | 0.70 | Authors claim SC median moved from ~2027–2028 to ~2032. |
| META-2026-121 | [F] | META | ASSERTED | OTHER:AI Futures Project | who=AI Futures Project; what=AC definition | OTHER:5% compute | E4 | 0.85 | Authors operationalize AC as coding-staff replacement using ~5% compute. |
| TRANS-2026-027 | [F] | TRANS | ASSERTED | OTHER:AI Futures Project | who=Eli; what=takeoff probs | OTHER:26→30; 43→60 | E4 | 0.65 | Eli reports increasing fast-takeoff probability mass (AC→ASI <1y and <3y). |

### Claims to Register

```yaml
claims:
  - id: "META-2026-117"
    text: "The AI Futures Project’s Dec 2025 update announces a unified timelines-and-takeoff model (AI Futures Model) forecasting milestone arrival (e.g., AC, SAR, TED-AI, ASI) and takeoff speeds."
    type: "[F]"
    domain: "META"
    evidence_level: "E4"
    credence: 0.85
    operationalization: "Verify that the post describes the unified model and the milestone/takeoff forecast framing."
    assumptions: ["The published post reflects the authors’ intended model description."]
    falsifiers: ["The post does not actually describe a unified model or milestone/takeoff forecasts."]
    source_ids: ["aifutures-2025-ai-futures-model-dec-2025-update"]

  - id: "META-2026-118"
    text: "The AI Futures Project claims their AI Futures Model implies timelines to full coding automation (AC) that are about 3–5 years longer than their April 2025 AI 2027-era timelines model, partly because they are less bullish on pre-automation AI R&D speedups."
    type: "[F]"
    domain: "META"
    evidence_level: "E4"
    credence: 0.75
    operationalization: "Locate the stated 3–5 year shift claim and its attributed causes in the Dec 2025 update text."
    assumptions: ["The authors’ comparison refers to comparable milestone definitions across model versions."]
    falsifiers: ["The post does not state a 3–5 year shift, or attributes it differently."]
    source_ids: ["aifutures-2025-ai-futures-model-dec-2025-update"]

  - id: "META-2026-119"
    text: "The AI Futures Project claims the 3–5 year median shift to coding automation is primarily due to improved modeling of AI R&D automation, and is a larger change than what new empirical evidence caused."
    type: "[F]"
    domain: "META"
    evidence_level: "E4"
    credence: 0.70
    operationalization: "Locate the attribution statement (modeling vs new evidence) in the Dec 2025 update text."
    assumptions: ["The post distinguishes 'modeling improvements' from 'new empirical evidence' as causal attributions for forecast shifts."]
    falsifiers: ["The post attributes the forecast shift mainly to new empirical evidence rather than modeling changes."]
    source_ids: ["aifutures-2025-ai-futures-model-dec-2025-update"]

  - id: "META-2026-120"
    text: "The AI Futures Project claims their previous model (median parameters) predicted superhuman coder (SC) medians around 2027–2028, while their new model predicts around 2032."
    type: "[F]"
    domain: "META"
    evidence_level: "E4"
    credence: 0.70
    operationalization: "Locate the explicit comparison of SC medians between the old and new models in the post."
    assumptions: ["The 'SC' milestone is defined consistently in both comparisons."]
    falsifiers: ["The post reports materially different SC medians or no such comparison."]
    source_ids: ["aifutures-2025-ai-futures-model-dec-2025-update"]

  - id: "META-2026-121"
    text: "The AI Futures Project operationalizes the Automated Coder (AC) milestone as a system that can fully automate an AGI project’s coding work (replacing the coding staff) using about 5% of the project’s compute supply."
    type: "[F]"
    domain: "META"
    evidence_level: "E4"
    credence: 0.85
    operationalization: "Locate the AC definition and compute-budget constraint in the 'operationalizes AC' section of the post."
    assumptions: ["The definition is intended as an operational test, not merely a narrative label."]
    falsifiers: ["The post’s AC definition differs materially from the claim (e.g., no compute constraint, different replacement criterion)."]
    source_ids: ["aifutures-2025-ai-futures-model-dec-2025-update"]

  - id: "TRANS-2026-027"
    text: "In the Dec 2025 AI Futures Model update, Eli Lifland reports increasing his all-things-considered probability that AC→ASI happens in <1 year from 26% to 30%, and in <3 years from 43% to 60%."
    type: "[F]"
    domain: "TRANS"
    evidence_level: "E4"
    credence: 0.65
    operationalization: "Locate the passage describing the probability adjustments for AC→ASI takeoff speed."
    assumptions: ["Percentages refer to the author’s stated all-things-considered distribution at the time of publication."]
    falsifiers: ["The post does not include these probability adjustments or states different values."]
    source_ids: ["aifutures-2025-ai-futures-model-dec-2025-update"]
```

---

**Analysis Date**: 2026-02-13  
**Analyst**: codex (GPT-5.2)  
**Credence in Analysis**: 0.70

## Analysis Log

| Pass | Date | Tool | Model | Duration | Tokens | Cost | Notes |
|---:|---|---|---|---:|---:|---:|---|
| 1 | 2026-02-13 | codex | gpt-5.2 | — | — | — | Initial analysis |

