# Source Analysis: AI 2027 Predictions & Primary Resources (Independent scorecard)

> **Claim types**: `[F]` fact, `[T]` theory, `[H]` hypothesis, `[P]` prediction, `[A]` assumption, `[C]` counterfactual, `[S]` speculation, `[X]` contradiction  
> **Evidence**: **E1** systematic review/meta-analysis; **E2** peer-reviewed/official stats; **E3** expert consensus/preprint/open data; **E4** credible journalism/industry/primary docs; **E5** forecast/analysis; **E6** unsupported/speculative

## Metadata

| Field | Value |
|---|---|
| **Source ID** | `independent-2026-02-13-ai-2027-review` |
| **Title** | AI 2027 Predictions and Primary Resources (independent scorecard) |
| **Author(s)** | lhl (independent) |
| **Date** | 2026-02-13 |
| **Type** | REPORT (internal analysis memo) |
| **URL** | N/A (local memo) |
| **Reliability** | 0.65 |
| **Rigor Level** | [DRAFT] |
| **Bias Notes** | Internal synthesis memo combining primary sources, benchmark checks, and subjective weighting. Strength: explicit pace scorecard and separation of “inputs vs outputs vs autonomy.” Risks: selective metric choice, reliance on secondary benchmark snapshots, and subjective aggregation/weights. Treat as a hypothesis-generating synthesis, not a primary measurement source. |

**Captured artifact**: (moved from inbox) `reference/articles/independent-2026-02-13-ai-2027-review.md`

**Claims YAML**: `analysis/sources/independent-2026-02-13-ai-2027-review.yaml`

## Stage 1: Descriptive Analysis

### Core Thesis
The memo argues that, as of 2026-02-13, the world appears “behind schedule” relative to the original AI 2027 narrative, with a central “pace” estimate around 0.70×; it claims compute/capex are ahead, while robust long-horizon autonomy and real-world productivity evidence lag.

### Summary (Neutral)
The memo contains:
- a “prediction set” summary (milestones like AC/SC/SAR/TED‑AI/ASI and takeoff-speed distributions),
- quantitative scoring targets (SWE‑bench, OSWorld, METR horizons, revenue/valuation, compute),
- an “independent reality check” section organizing observations into descriptive/evaluative/dialectical framing,
- a weighted pace scorecard and sensitivity band,
- an extracted-claims table (with its own IDs and evidence/credence estimates).

### Key Claims

| # | Claim | Claim ID | Layer | Actor | Scope | Quantifier | Type | Domain | Evid | Credence | Verified? | Falsifiable By |
|---:|---|---|---|---|---|---|---|---|---|---:|---|---|
| 1 | The memo estimates overall pace vs the original AI 2027 schedule at **~0.70×** (sensitivity **~0.62×–0.78×**), concluding “behind schedule overall” | TRANS-2026-035 | ASSERTED | OTHER:Independent memo | who=global AI progress; what=pace vs AI 2027; when=2026-02-13 | OTHER:0.62–0.78× | [H] | TRANS | E5 | 0.60 | In-memo | Recomputing the memo’s scoring with the same inputs/weights yields a materially different pace estimate |
| 2 | The memo’s synthesis claim: “inputs are ahead, benchmark outputs are mixed, full-stack autonomy/productivity is behind” | TRANS-2026-036 | ASSERTED | OTHER:Independent memo | who=AI ecosystem; what=relative status; when=2026-02-13 | N/A | [T] | TRANS | E5 | 0.65 | In-memo | Independent evaluation finds autonomy/productivity indicators clearly ahead of schedule on robust measures |

## Stage 2: Evaluative Analysis

### Internal Coherence
The memo is internally coherent: it defines a pace scale, lists metrics, and computes a weighted score. The largest weakness is that weights and some “observed reality” inputs are subjective and not fully provenance-linked within the memo.

### Key Factual Claims Verified

| Claim (paraphrased) | Crux? | Source Says | Actual | External Source | Status |
|---|---:|---|---|---|---|
| The memo contains the stated pace estimate and scorecard framing | **Y** | Yes | Present in captured memo | `reference/articles/independent-2026-02-13-ai-2027-review.md` | ok |

### Disconfirming Evidence Search

| Claim | Counterevidence Found | Alternative Explanation | Search Notes |
|---|---|---|---|
| “0.70× pace overall” | Different weighting schemes and different choices of benchmark cutoffs could move the estimate; author’s score is explicitly sensitivity-banded. | Pace is multi-dimensional; a scalar “×” can hide cross-domain divergence (compute vs autonomy). | Compared memo’s scorecard dimensions to the AI Futures Project’s grading categories (benchmarks, time horizon, uplift, compute, salience). |

### Evidence Assessment
- This is **E5** (analysis memo) whose evidential strength depends on the quality of the underlying primary sources it references.

## Stage 3: Dialectical Analysis

### Steelmanned Argument
A scalar “pace” estimate is useful if it is transparent and sensitivity-banded; it forces explicit discussion of what matters (autonomy vs inputs) and can be updated as 2026 data arrives.

### Strongest Counterarguments
1. **Provenance gap**: without explicit citations for each “observed reality” cell, replication is hard.
2. **Metric mismatch**: many critical bottlenecks (research taste; reliability) are hard to measure; the memo may be forced into weak proxies.

### Synthesis Notes
Treat this memo as an internal triangulation that emphasizes autonomy/productivity as the decisive uncertainty, and use it alongside the AI Futures Project’s own grading spreadsheet (which provides auditable row-level values).

---

### Claim Summary

| ID | Type | Domain | Layer | Actor | Scope | Quantifier | Evidence | Credence | Claim |
|---|---|---|---|---|---|---|---|---:|---|
| TRANS-2026-035 | [H] | TRANS | ASSERTED | OTHER:Independent memo | who=global AI progress; what=pace | OTHER:0.62–0.78× | E5 | 0.60 | Memo estimates overall pace vs AI 2027 at ~0.70×. |
| TRANS-2026-036 | [T] | TRANS | ASSERTED | OTHER:Independent memo | who=AI ecosystem; what=inputs vs outputs vs autonomy | N/A | E5 | 0.65 | Memo claims inputs ahead; autonomy/productivity behind. |

### Claims to Register

```yaml
claims:
  - id: "TRANS-2026-035"
    text: "An internal independent scorecard memo estimates overall pace vs the original AI 2027 schedule at ~0.70× (sensitivity ~0.62×–0.78×), concluding progress is behind schedule overall as of 2026-02-13."
    type: "[H]"
    domain: "TRANS"
    evidence_level: "E5"
    credence: 0.60
    operationalization: "Reproduce the memo’s weighted pace score using the same inputs/weights and assess sensitivity to alternative weighting and updated benchmark values."
    assumptions: ["The memo’s selected metrics and weights are reasonable proxies for AI 2027’s core causal levers."]
    falsifiers: ["Reproduction fails or yields a materially different pace estimate given the same inputs/weights."]
    source_ids: ["independent-2026-02-13-ai-2027-review"]

  - id: "TRANS-2026-036"
    text: "An internal independent scorecard memo argues that by early 2026, compute/capex inputs are ahead of AI 2027 expectations, benchmark outputs are mixed, and full-stack autonomy/productivity evidence lags (overall: autonomy behind)."
    type: "[T]"
    domain: "TRANS"
    evidence_level: "E5"
    credence: 0.65
    operationalization: "Define input/output/autonomy indicators and score them against AI 2027’s dated expectations with explicit cutoffs; compare to memo’s qualitative conclusion."
    assumptions: ["Autonomy/productivity is the binding bottleneck for an AI 2027-style rapid takeoff path."]
    falsifiers: ["Robust autonomy/productivity indicators are clearly ahead of schedule on multiple independent measures."]
    source_ids: ["independent-2026-02-13-ai-2027-review"]
```

---

**Analysis Date**: 2026-02-13  
**Analyst**: codex (GPT-5.2)  
**Credence in Analysis**: 0.65

## Analysis Log

| Pass | Date | Tool | Model | Duration | Tokens | Cost | Notes |
|---:|---|---|---|---:|---:|---:|---|
| 1 | 2026-02-13 | codex | gpt-5.2 | — | — | — | Meta-analysis of internal memo |

