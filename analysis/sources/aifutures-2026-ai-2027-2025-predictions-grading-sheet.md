# Source Analysis: AI 2027 “2025 Predictions” Grading Spreadsheet (AI Futures Project)

> **Claim types**: `[F]` fact, `[T]` theory, `[H]` hypothesis, `[P]` prediction, `[A]` assumption, `[C]` counterfactual, `[S]` speculation, `[X]` contradiction  
> **Evidence**: **E1** systematic review/meta-analysis; **E2** peer-reviewed/official stats; **E3** expert consensus/preprint/open data; **E4** credible journalism/industry/primary docs; **E5** forecast/analysis; **E6** unsupported/speculative

## Metadata

| Field | Value |
|---|---|
| **Source ID** | `aifutures-2026-ai-2027-2025-predictions-grading-sheet` |
| **Title** | AI 2027 “2025 Predictions” grading spreadsheet (captured as CSV) |
| **Author(s)** | Eli Lifland; Daniel Kokotajlo |
| **Date** | 2026-02-12 (published/linked alongside grading post; captured 2026-02-13) |
| **Type** | DATA (spreadsheet → CSV capture) |
| **URL** | https://docs.google.com/spreadsheets/d/1Ncol1SYIeLhGKdOUHKSYPxCTjkUwQVxkIbp393hveyA/edit?gid=145629229 |
| **Reliability** | 0.65 |
| **Rigor Level** | [REVIEWED] |
| **Bias Notes** | Self-produced scoring sheet for AI 2027. Strength: row-level disclosure of targets, “actual” values, and pace multipliers. Risks: discretionary choices about cutoffs, “SOTA” definitions, and how to estimate private quantities (compute, revenue). Treat as *their* grading ledger; independent verification requires checking each cited reference. |

**Captured artifact**: `reference/data/aifutures-2026-ai-2027-2025-predictions-grading-sheet.csv`

**Claims YAML**: `analysis/sources/aifutures-2026-ai-2027-2025-predictions-grading-sheet.yaml`

## Stage 1: Descriptive Analysis

### Core Thesis
The spreadsheet provides the AI Futures Project’s row-level “pace of progress” scoring for AI 2027’s 2025 quantitative predictions, plus multiple aggregation schemes (category vs individual-row; “capabilities indicators only” vs “all”).

### Summary (Neutral)
The sheet lists quantitative predictions (benchmarks, time horizons, R&D uplift, economic value, compute, public salience), and for each row:
- states a **baseline** (Apr 2025),
- states a **predicted value** and target timing (“AI 2027 predicted…”),
- chooses an **actual resolution value** and corresponding “time achieved in reality,” and
- computes a **pace multiplier** (higher = faster progress relative to AI 2027’s trajectory).

At the bottom, it includes a dedicated **Aggregations** section with:
- category means/medians (e.g., “Mid 2025 benchmarks”, “Coding time horizon”, …),
- “Capabilities indicators only” aggregate (mean-of-means / median-of-medians), and
- “All” aggregates (both category-level and individual-row level).

### Key Claims

| # | Claim | Claim ID | Layer | Actor | Scope | Quantifier | Type | Domain | Evid | Credence | Verified? | Falsifiable By |
|---:|---|---|---|---|---|---|---|---|---|---:|---|---|
| 1 | The captured CSV includes aggregation rows reporting “Capabilities indicators only” aggregates of **0.58** (mean-of-means) and **0.66** (median-of-medians), and “All (individual values …)” aggregates of **0.75** (mean) and **0.84** (median) | META-2026-124 | PRACTICED | OTHER:AI Futures Project | who=AI Futures Project; what=scoring spreadsheet aggregates; when=2026-02 | OTHER:0.58/0.66/0.75/0.84 | [F] | META | E4 | 0.85 | In-artifact | Captured CSV lacks these rows/values |
| 2 | In the spreadsheet, SWE-bench Verified is scored at pace **0.18×**, using predicted **0.85** (mid-2025) vs “actual SOTA” **0.745** (Aug 2025) | TECH-2025-072 | ASSERTED | OTHER:AI Futures Project | who=SWE-bench Verified; what=score; when=mid-2025 | OTHER:0.18× | [F] | TECH | E4 | 0.70 | In-artifact | Row values in captured CSV differ |
| 3 | In the spreadsheet, OSWorld-Verified is scored at pace **0.84×**, using predicted **0.65** (mid-2025) vs “actual SOTA” **0.608** (Aug 2025) | TECH-2025-073 | ASSERTED | OTHER:AI Futures Project | who=OSWorld-Verified; what=score; when=mid-2025 | OTHER:0.84× | [F] | TECH | E4 | 0.70 | In-artifact | Row values in captured CSV differ |
| 4 | In the spreadsheet, METR’s 80% coding time horizon is scored at pace **1.04×** vs a “model trajectory,” and **0.66×** vs an “erroneous graph trajectory” | TECH-2025-074 | ASSERTED | OTHER:AI Futures Project | who=METR time horizon; what=pace; when=late-2025 | OTHER:1.04× / 0.66× | [F] | TECH | E4 | 0.70 | In-artifact | Row values in captured CSV differ |
| 5 | In the spreadsheet, “OpenBrain annualized revenue” is scored at pace **1.16×**, with “actual” **$20B** annualized (end of 2025) | ECON-2026-916 | ASSERTED | OTHER:AI Futures Project | who=leading AGI company; what=revenue proxy; when=late-2025 | OTHER:1.16× | [F] | ECON | E4 | 0.55 | In-artifact | Row values in captured CSV differ |
| 6 | In the spreadsheet, “OpenBrain valuation” is scored at pace **0.44×**, with “actual” **$500B** (Oct 2, 2025) | ECON-2026-917 | ASSERTED | OTHER:AI Futures Project | who=leading AGI company; what=valuation proxy; when=late-2025 | OTHER:0.44× | [F] | ECON | E4 | 0.60 | In-artifact | Row values in captured CSV differ |

### Argument Structure
This artifact is a ledger rather than an argument; the implied argument is:

```
Choose proxies + resolve values
        ↓
Compute row-level pace multipliers
        ↓
Aggregate into summary pace estimates
        ↓
Use pace to update scenario timing
```

### Theoretical Lineage
- Forecast verification via metric resolution (proxied by benchmarks, economics, and compute).

### Scope & Limitations
- “Actual” values for private quantities (compute budgets; leading-company stats) are uncertain and may require substantial independent audit.
- Several rows rely on interpolation (implied timing) and logistic/exponential assumptions, which can be fragile.

## Stage 2: Evaluative Analysis

### Internal Coherence
As an internal scorecard, the sheet is coherent: it defines baselines, targets, resolutions, and a pace score. The core risk is not arithmetic but the *choice of proxies* and the *resolution definitions*.

### Key Factual Claims Verified

| Claim (paraphrased) | Crux? | Source Says | Actual | External Source | Status |
|---|---:|---|---|---|---|
| The sheet contains “Capabilities indicators only” and “All (individual values …)” aggregate rows with the stated values | **Y** | 0.58/0.66 and 0.75/0.84 | Present in captured CSV under “Aggregations” | `reference/data/aifutures-2026-ai-2027-2025-predictions-grading-sheet.csv` | ok |

### Disconfirming Evidence Search

| Claim | Counterevidence Found | Alternative Explanation | Search Notes |
|---|---|---|---|
| Pace multipliers meaningfully track “overall AI progress” | The sheet itself shows wide sensitivity to aggregation method and category selection. | The sheet may be best seen as a *partial proxy dashboard* rather than a scalar summary of “progress toward takeoff.” | Reviewed multiple aggregation rows in captured CSV; compared “capabilities only” vs “all”. |

### Corrections & Updates

| Item | URL | Published | Corrected/Updated | What Changed | Impacted Claim IDs | Action Taken |
|---|---|---:|---:|---|---|---|
| Captured the Google Sheet as a stable CSV snapshot | (see URL above) | — | 2026-02-13 | Exported `gid=145629229` sheet to CSV in-repo | All | Treat captured CSV as audit basis; do not rely on live sheet for reproducibility |

### Evidence Assessment
- **E4** for “what the sheet contains” (we have the captured artifact).
- For claims about the real world (SWE-bench SOTA, OSWorld SOTA, revenue/valuation, compute budgets), the sheet provides references but independent verification is separate work.

## Stage 3: Dialectical Analysis

### Steelmanned Argument
Publishing a row-level scoring sheet is a strong practice: it invites external audit, reduces post-hoc rationalization, and makes disagreements concrete (which row, which proxy, which cutoff, which reference).

### Strongest Counterarguments
1. **Proxy fragility**: small definitional changes (what counts as “SOTA”; what date counts as “mid-2025”) can swing pace multipliers.
2. **Endogeneity**: some “resolution” values (especially uplift) can be the authors’ own model estimates rather than external measurements.

### Synthesis Notes
This spreadsheet is the key *reproducibility anchor* for the grading post; it should be used as the auditable substrate for any dispute about “what they scored” (separate from whether the scoring is epistemically valid).

---

### Claim Summary

| ID | Type | Domain | Layer | Actor | Scope | Quantifier | Evidence | Credence | Claim |
|---|---|---|---|---|---|---|---|---:|---|
| META-2026-124 | [F] | META | PRACTICED | OTHER:AI Futures Project | who=AI Futures Project; what=spreadsheet aggregates | OTHER:0.58/0.66/0.75/0.84 | E4 | 0.85 | Captured CSV contains stated aggregation rows/values. |
| TECH-2025-072 | [F] | TECH | ASSERTED | OTHER:AI Futures Project | who=SWE-bench; what=pace score | OTHER:0.18× | E4 | 0.70 | Spreadsheet scores SWE-bench at pace 0.18× (0.85 predicted vs 0.745 actual). |
| TECH-2025-073 | [F] | TECH | ASSERTED | OTHER:AI Futures Project | who=OSWorld-Verified; what=pace score | OTHER:0.84× | E4 | 0.70 | Spreadsheet scores OSWorld-Verified at pace 0.84× (0.65 predicted vs 0.608 actual). |
| TECH-2025-074 | [F] | TECH | ASSERTED | OTHER:AI Futures Project | who=METR time horizon; what=pace score | OTHER:1.04×/0.66× | E4 | 0.70 | Spreadsheet scores time-horizon pace at 1.04× (model traj) and 0.66× (erroneous graph). |
| ECON-2026-916 | [F] | ECON | ASSERTED | OTHER:AI Futures Project | who=OpenAI proxy; what=revenue | OTHER:1.16× | E4 | 0.55 | Spreadsheet scores annualized revenue at pace 1.16× with $20B actual. |
| ECON-2026-917 | [F] | ECON | ASSERTED | OTHER:AI Futures Project | who=OpenAI proxy; what=valuation | OTHER:0.44× | E4 | 0.60 | Spreadsheet scores valuation at pace 0.44× with $500B actual. |

### Claims to Register

```yaml
claims:
  - id: "META-2026-124"
    text: "The captured AI Futures Project grading CSV contains aggregation rows reporting: (a) “Capabilities indicators only” = 0.58 (mean-of-means) and 0.66 (median-of-medians), and (b) “All (individual values …)” = 0.75 (mean) and 0.84 (median)."
    type: "[F]"
    domain: "META"
    evidence_level: "E4"
    credence: 0.85
    operationalization: "Open the captured CSV and confirm the aggregation rows and values under the “Aggregations” section."
    assumptions: ["The captured CSV is a faithful export of the referenced Google Sheet at capture time."]
    falsifiers: ["The captured CSV does not contain the referenced aggregation rows/values."]
    source_ids: ["aifutures-2026-ai-2027-2025-predictions-grading-sheet"]

  - id: "TECH-2025-072"
    text: "In the AI Futures Project grading spreadsheet, SWE-bench Verified is scored at pace 0.18×, using predicted 0.85 (mid-2025) vs “actual SOTA” 0.745 (Aug 2025)."
    type: "[F]"
    domain: "TECH"
    evidence_level: "E4"
    credence: 0.70
    operationalization: "Locate the SWE-bench Verified row in the captured CSV and confirm the pace, predicted value, and actual SOTA."
    assumptions: ["The row correctly reflects the benchmark variant and date cutoffs."]
    falsifiers: ["Row values differ in the captured CSV, or the cited benchmark source contradicts the row’s resolution value/date."]
    source_ids: ["aifutures-2026-ai-2027-2025-predictions-grading-sheet"]

  - id: "TECH-2025-073"
    text: "In the AI Futures Project grading spreadsheet, OSWorld-Verified is scored at pace 0.84×, using predicted 0.65 (mid-2025) vs “actual SOTA” 0.608 (Aug 2025)."
    type: "[F]"
    domain: "TECH"
    evidence_level: "E4"
    credence: 0.70
    operationalization: "Locate the OSWorld row in the captured CSV and confirm the pace, predicted value, and actual SOTA."
    assumptions: ["The row correctly reflects OSWorld-Verified and its resolution value by date."]
    falsifiers: ["Row values differ in the captured CSV, or cited OSWorld sources contradict the row’s resolution value/date."]
    source_ids: ["aifutures-2026-ai-2027-2025-predictions-grading-sheet"]

  - id: "TECH-2025-074"
    text: "In the AI Futures Project grading spreadsheet, METR’s 80% coding time horizon is scored at pace 1.04× vs a “model trajectory” and 0.66× vs an “erroneous graph trajectory.”"
    type: "[F]"
    domain: "TECH"
    evidence_level: "E4"
    credence: 0.70
    operationalization: "Locate the two coding time-horizon rows in the captured CSV and confirm the pace multipliers."
    assumptions: ["The methodology adjustment (TH1.0→TH1.1) is applied consistently as described in the row notes."]
    falsifiers: ["Row values differ in the captured CSV, or the referenced METR time-horizon sources contradict the inputs."]
    source_ids: ["aifutures-2026-ai-2027-2025-predictions-grading-sheet"]

  - id: "ECON-2026-916"
    text: "In the AI Futures Project grading spreadsheet, leading-company annualized revenue is scored at pace 1.16×, using “actual” $20B annualized revenue for OpenAI at end of 2025."
    type: "[F]"
    domain: "ECON"
    evidence_level: "E4"
    credence: 0.55
    operationalization: "Locate the “OpenBrain annualized revenue” row in the captured CSV and confirm the pace and resolution value."
    assumptions: ["OpenAI revenue estimates are accurate and comparable to the model’s proxy definition."]
    falsifiers: ["Row values differ in the captured CSV, or referenced sources materially contradict the claimed revenue."]
    source_ids: ["aifutures-2026-ai-2027-2025-predictions-grading-sheet"]

  - id: "ECON-2026-917"
    text: "In the AI Futures Project grading spreadsheet, leading-company valuation is scored at pace 0.44×, using “actual” $500B valuation for OpenAI as of Oct 2, 2025."
    type: "[F]"
    domain: "ECON"
    evidence_level: "E4"
    credence: 0.60
    operationalization: "Locate the “OpenBrain valuation” row in the captured CSV and confirm the pace and resolution value/date."
    assumptions: ["The referenced valuation estimates are accurate and comparable to the model’s proxy definition."]
    falsifiers: ["Row values differ in the captured CSV, or referenced sources materially contradict the claimed valuation/date."]
    source_ids: ["aifutures-2026-ai-2027-2025-predictions-grading-sheet"]
```

---

**Analysis Date**: 2026-02-13  
**Analyst**: codex (GPT-5.2)  
**Credence in Analysis**: 0.75

## Analysis Log

| Pass | Date | Tool | Model | Duration | Tokens | Cost | Notes |
|---:|---|---|---|---:|---:|---:|---|
| 1 | 2026-02-13 | codex | gpt-5.2 | — | — | — | Captured CSV audited for key rows + aggregates |

