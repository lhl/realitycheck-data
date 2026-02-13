# Source Analysis: Grading AI 2027’s 2025 Predictions (AI Futures Project)

> **Claim types**: `[F]` fact, `[T]` theory, `[H]` hypothesis, `[P]` prediction, `[A]` assumption, `[C]` counterfactual, `[S]` speculation, `[X]` contradiction  
> **Evidence**: **E1** systematic review/meta-analysis; **E2** peer-reviewed/official stats; **E3** expert consensus/preprint/open data; **E4** credible journalism/industry/primary docs; **E5** forecast/analysis; **E6** unsupported/speculative

## Metadata

| Field | Value |
|---|---|
| **Source ID** | `aifutures-2026-grading-ai-2027-2025-predictions` |
| **Title** | Grading AI 2027’s 2025 Predictions |
| **Author(s)** | Eli Lifland; Daniel Kokotajlo |
| **Date** | 2026-02-12 |
| **Type** | BLOG (self-evaluation / forecast review) |
| **URL** | https://blog.ai-futures.org/p/grading-ai-2027s-2025-predictions |
| **Reliability** | 0.60 |
| **Rigor Level** | [REVIEWED] |
| **Bias Notes** | Self-grading by the original forecasters. Strengths: unusually concrete metrics + a published grading spreadsheet. Risks: selection effects (which metrics count), definitional drift (“what counts as SOTA”), and circularity where “resolution” uses the authors’ own later model estimates. Treat quantitative rows as *their* best-effort scoring, not independent ground truth. |

**Claims YAML**: `analysis/sources/aifutures-2026-grading-ai-2027-2025-predictions.yaml`

## Stage 1: Descriptive Analysis

### Core Thesis
The AI Futures Project claims that, relative to the AI 2027 scenario’s 2025 quantitative predictions, observed progress is ~0.6–0.7× (they summarize as ~65% pace), while most qualitative predictions are “on pace”; they then translate this pace into a later “takeoff window” than the original 2027 narrative.

### Summary (Neutral)
This post evaluates a subset of AI 2027’s predictions intended to be checkable by early 2026. The authors define a “pace multiplier” for quantitative predictions (1× = on pace, 0.5× = half as fast, 2× = twice as fast) and report aggregated results using two approaches:
- **Category aggregation** (their preferred method): compute pace within each category, then aggregate across categories to avoid overweighting compute (which has many rows).
- **Individual-row aggregation** (their disfavored method): aggregate across all prediction rows directly.

They claim quantitative progress is substantially slower than AI 2027’s depicted trajectory, while most qualitative narrative elements are broadly consistent with reality so far. They then use the implied pace to shift the scenario’s timing: if the AI 2027 narrative was roughly “coding automation → superintelligence” during 2027, then at 0.65× pace it would shift later; they additionally adjust further using their newer AI Futures Model (including assumptions about compute/labor slowdowns).

### Key Claims

| # | Claim | Claim ID | Layer | Actor | Scope | Quantifier | Type | Domain | Evid | Credence | Verified? | Falsifiable By |
|---:|---|---|---|---|---|---|---|---|---|---:|---|---|
| 1 | The authors’ preferred category-aggregated “pace of progress” for quantitative metrics is **0.58–0.66×** (summarized as “~65% pace”) | META-2026-122 | ASSERTED | OTHER:AI Futures Project | who=AI Futures Project; what=quantitative pace scoring; when=2026-02; basis=category aggregation | OTHER:0.58–0.66× | [F] | META | E4 | 0.75 | Spreadsheet cross-check | Captured spreadsheet lacks the stated aggregate values or yields materially different aggregates under the stated method |
| 2 | Aggregating over individual prediction rows yields higher aggregates (mean **0.75×**, median **0.84×**), but they argue this is misleading because compute predictions are 7/15 rows | META-2026-123 | ASSERTED | OTHER:AI Futures Project | who=AI Futures Project; what=alternative aggregation + critique; when=2026-02 | OTHER:mean 0.75; median 0.84 | [F] | META | E4 | 0.75 | Spreadsheet cross-check | Captured spreadsheet lacks these aggregates or compute-row share, or they do not match the post |
| 3 | If progress continues at ~0.65× pace, the AI 2027 narrative’s 2027 “takeoff” would shift to **late 2027–mid 2029** | TRANS-2026-028 | ASSERTED | OTHER:AI Futures Project | who=AI progress; what=takeoff window shift; when=2027–2029; condition=pace stays ~0.65× | OTHER:late 2027–mid 2029 | [P] | TRANS | E5 | 0.40 | In-source | Their own arithmetic mapping from pace→dates is inconsistent or uses unstated assumptions that materially change the window |
| 4 | Adjusting for compute/labor slowdowns using the AI Futures Model yields a later implied takeoff window of **mid 2028–mid 2030** | TRANS-2026-029 | ASSERTED | OTHER:AI Futures Project | who=AI progress; what=takeoff window shift; when=2028–2030; method=AI Futures Model slowdown adjustment | OTHER:mid 2028–mid 2030 | [P] | TRANS | E5 | 0.40 | In-source | The cited model adjustment does not, under the stated assumptions, imply this timing range |

### Argument Structure

```
(1) AI 2027 included quantitative + qualitative predictions
        ↓
(2) Score quantitative rows as pace multipliers (0.5×, 1×, 2×, ...)
        ↓
(3) Aggregate by category (preferred) → ~0.58–0.66× pace
        ↓
(4) Map pace to scenario timing → takeoff shifts later
        ↓
(5) Further adjust using AI Futures Model slowdown assumptions
```

**Weakest links**:
- Category selection and operationalization (what gets counted; how “SOTA” is defined; which dates/cutoffs).
- The mapping from “pace on chosen proxies” → “pace of full-stack autonomy” (external validity).

### Theoretical Lineage
- **Forecast auditing**: treating forecasts as hypotheses and periodically scoring them against resolvable metrics.
- **Scenario-to-metric translation**: operationalizing narrative predictions into measurable proxies (always partially lossy).

### Scope & Limitations
- This is explicitly a *partial* scorecard (only predictions they wrote down and could resolve early).
- Several rows rely on proxies (e.g., revenue/valuation; compute estimates) with high uncertainty and definitional ambiguity.
- Some “resolutions” (notably R&D uplift) are partially endogenous to the authors’ own later modeling.

## Stage 2: Evaluative Analysis

### Internal Coherence
The post is coherent as a “forecast audit”: define a scoring function, compute pace multipliers, and map pace into timing shifts. The largest coherence risk is mixing levels of analysis: (a) quantitative proxies chosen for checkability vs (b) the scenario’s core bottleneck (robust autonomous R&D), which may not be well-measured by the selected metrics.

### Key Factual Claims Verified

| Claim (paraphrased) | Crux? | Source Says | Actual | External Source | Status |
|---|---:|---|---|---|---|
| Category-aggregated quantitative pace is ~0.58–0.66× | **Y** | “between 58–66% … roughly 65%” | Captured grading CSV includes “Capabilities indicators only (mean of means / median of medians) = 0.58 / 0.66” | `reference/data/aifutures-2026-ai-2027-2025-predictions-grading-sheet.csv` | ok |
| Individual-row aggregation gives mean ~0.75×, median ~0.84× | N | “mean 75%, median 84%” | Captured grading CSV includes “All (individual values …) = 0.75 / 0.84” | `reference/data/aifutures-2026-ai-2027-2025-predictions-grading-sheet.csv` | ok |

### Disconfirming Evidence Search

| Claim | Counterevidence Found | Alternative Explanation | Search Notes |
|---|---|---|---|
| “~65% pace” is a good summary of AI progress vs AI 2027 | The estimate is highly sensitive to metric selection and aggregation (the post itself shows large shifts between category vs row aggregation; compute is excluded from “capabilities indicators only”). | The chosen metrics may measure *inputs* (compute, revenue) and *short-horizon* capability proxies better than they measure long-horizon autonomy and organizational integration. | Searched within the captured CSV for aggregation definitions; compared “capabilities only” vs “all” aggregates and noted sensitivity. |

### Corrections & Updates

| Item | URL | Published | Corrected/Updated | What Changed | Impacted Claim IDs | Action Taken |
|---|---|---:|---:|---|---|---|
| Grading spreadsheet captured as CSV for reproducibility | https://docs.google.com/spreadsheets/d/1Ncol1SYIeLhGKdOUHKSYPxCTjkUwQVxkIbp393hveyA/edit | 2026-02-12 (post) | 2026-02-13 (capture) | Captured the linked spreadsheet as `reference/data/...csv` | META-2026-122; META-2026-123 | Use captured CSV as the auditable basis for aggregate verification |

### Internal Tensions / Self-Contradictions

| Tension | Parts in Conflict | Implication |
|---|---|---|
| “Compute not central to uncertainty” vs compute-heavy quantitative scorecard | They argue row-aggregation overweight compute, but compute is still a large share of individual rows and plausibly dominates “inputs” | The scoring methodology is sensitive to normative judgments about what *should* be weighted |

### Persuasion Techniques

| Technique | Example from Source | Effect on Reader |
|---|---|---|
| Credibility via falsifiability emphasis | “concrete, falsifiable predictions” framing | Encourages trust in the overall approach even if the mapping from proxies→scenario is lossy |

### Unstated Assumptions

| Assumption | Claim ID | Critical? | Problematic? |
|---|---|---:|---:|
| Selected quantitative proxies track the scenario’s key bottleneck (autonomous R&D) | TRANS-2026-028; TRANS-2026-029 | Y | Y |

### Evidence Assessment
- **Strengths**: Published numeric scorecard + explicit aggregation discussion + a spreadsheet with row-level details.
- **Weaknesses**: Several rows encode discretionary choices (cutoff date, what counts as SOTA, how to handle tool scaffolds), and at least one key category (R&D uplift) is partly resolved by the authors’ own later model estimates.

### Credence Assessment
- **Overall Credence**: 0.65 that the *reported* aggregates match their spreadsheet; 0.45 that the aggregates are a good proxy for “progress toward AI 2027-style takeoff.”

## Stage 3: Dialectical Analysis

### Steelmanned Argument
If you write down clear quantitative proxies that (imperfectly) track important capability drivers, then early resolution of those proxies is informative. A 0.6–0.7× pace estimate provides a disciplined way to update timelines away from overly vivid narrative anchoring while remaining grounded in checkable data.

### Strongest Counterarguments
1. **Proxy mismatch**: the scenario’s key causal lever is long-horizon autonomy and research taste; selected proxies may not measure this directly.
2. **Endogeneity/circularity**: resolving R&D uplift using the authors’ newer model risks “grading with the same model family.”

### Supporting Theories

| Theory/Framework | Source ID | How It Supports |
|---|---|---|
| Forecast auditing improves calibration | `aifutures-2026-grading-ai-2027-2025-predictions` | Treats forecasts as hypotheses and updates based on scored outcomes |

### Contradicting Theories

| Theory/Framework | Source ID | Point of Conflict |
|---|---|---|
| “Benchmarks are not deployment” critique | `marcus-2025-ai-2027-scenario-how-realistic` (planned) | Argues narrative/benchmark proxies can mislead about real-world autonomy and impact |

### Synthesis Notes
This post is a valuable artifact because it externalizes (and partially quantifies) a timeline update. Its “~65% pace” figure is best treated as: *a transparent, reproducible scoring of a specific proxy set*, not a definitive measure of “how close we are to AI 2027.”

### Claims to Cross-Reference
- Link aggregate-pace claims to the captured grading spreadsheet rows for auditability.
- Compare time-horizon-related pace to METR’s TH1.1 methodology update (`metr-2026-time-horizon-1-1`).

---

### Claim Summary

| ID | Type | Domain | Layer | Actor | Scope | Quantifier | Evidence | Credence | Claim |
|---|---|---|---|---|---|---|---|---:|---|
| META-2026-122 | [F] | META | ASSERTED | OTHER:AI Futures Project | who=AI Futures Project; what=quantitative pace scoring; when=2026-02 | OTHER:0.58–0.66× | E4 | 0.75 | Category-aggregated quantitative “pace of progress” is 0.58–0.66× (~65%). |
| META-2026-123 | [F] | META | ASSERTED | OTHER:AI Futures Project | who=AI Futures Project; what=alternative aggregation; when=2026-02 | OTHER:mean 0.75; median 0.84 | E4 | 0.75 | Individual-row aggregation yields mean 0.75×, median 0.84×; compute overweight makes it misleading. |
| TRANS-2026-028 | [P] | TRANS | ASSERTED | OTHER:AI Futures Project | who=AI progress; what=takeoff window shift; when=2027–2029 | OTHER:late 2027–mid 2029 | E5 | 0.40 | If progress stays ~0.65×, takeoff shifts to late 2027–mid 2029. |
| TRANS-2026-029 | [P] | TRANS | ASSERTED | OTHER:AI Futures Project | who=AI progress; what=takeoff window shift; when=2028–2030 | OTHER:mid 2028–mid 2030 | E5 | 0.40 | With slowdown adjustment, takeoff shifts to mid 2028–mid 2030. |

### Claims to Register

```yaml
claims:
  - id: "META-2026-122"
    text: "The AI Futures Project reports that, using category aggregation, quantitative progress vs AI 2027 is at roughly 0.58–0.66× pace (summarized as ~65%)."
    type: "[F]"
    domain: "META"
    evidence_level: "E4"
    credence: 0.75
    operationalization: "Recompute the category means/medians from the published grading spreadsheet (captured) and confirm the reported aggregate range."
    assumptions:
      - "The grading spreadsheet’s aggregation rows match the post’s stated method."
    falsifiers:
      - "Recomputing the aggregates from the spreadsheet does not yield values in the stated range."
    source_ids: ["aifutures-2026-grading-ai-2027-2025-predictions"]

  - id: "META-2026-123"
    text: "The AI Futures Project reports that aggregating over individual prediction rows yields higher aggregates (mean ~0.75×, median ~0.84×), but argues this is a worse indicator because compute predictions are 7 of 15 rows."
    type: "[F]"
    domain: "META"
    evidence_level: "E4"
    credence: 0.75
    operationalization: "Count compute-related rows in the grading spreadsheet and reproduce mean/median across individual rows."
    assumptions:
      - "The set of rows included as 'individual predictions' is stable and clearly defined."
    falsifiers:
      - "Row counts or mean/median aggregates do not match the post."
    source_ids: ["aifutures-2026-grading-ai-2027-2025-predictions"]

  - id: "TRANS-2026-028"
    text: "The AI Futures Project predicts that if progress continues at ~0.65× of the AI 2027 pace, the scenario’s takeoff would shift to late-2027 through mid-2029."
    type: "[P]"
    domain: "TRANS"
    evidence_level: "E5"
    credence: 0.40
    operationalization: "Define the original AI 2027 takeoff window and apply a consistent time-rescaling using the stated pace multiplier; compare to the post’s window."
    assumptions:
      - "A single scalar pace multiplier is meaningful across the whole takeoff sequence."
    falsifiers:
      - "The mapping from the pace multiplier to dates is inconsistent with the post or depends on omitted assumptions."
    source_ids: ["aifutures-2026-grading-ai-2027-2025-predictions"]

  - id: "TRANS-2026-029"
    text: "The AI Futures Project predicts that after adjusting for compute/labor slowdowns using the AI Futures Model, takeoff would shift to mid-2028 through mid-2030."
    type: "[P]"
    domain: "TRANS"
    evidence_level: "E5"
    credence: 0.40
    operationalization: "Reproduce the AI Futures Model timing adjustment described in the post (with/without slowdown links) and confirm the implied timing range."
    assumptions:
      - "The slowdown adjustment procedure is implemented as described."
    falsifiers:
      - "The model outputs under the stated procedure do not match the timing range."
    source_ids: ["aifutures-2026-grading-ai-2027-2025-predictions"]
```

---

**Analysis Date**: 2026-02-13  
**Analyst**: codex (GPT-5.2)  
**Credence in Analysis**: 0.70

## Analysis Log

| Pass | Date | Tool | Model | Duration | Tokens | Cost | Notes |
|---:|---|---|---|---:|---:|---:|---|
| 1 | 2026-02-13 | codex | gpt-5.2 | — | — | — | Initial analysis (includes spreadsheet cross-check) |

