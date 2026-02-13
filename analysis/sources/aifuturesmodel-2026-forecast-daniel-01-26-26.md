# Source Analysis: AI Futures Model — Forecasts (Daniel 01-26-26)

> **Claim types**: `[F]` fact, `[T]` theory, `[H]` hypothesis, `[P]` prediction, `[A]` assumption, `[C]` counterfactual, `[S]` speculation, `[X]` contradiction  
> **Evidence**: **E1** systematic review/meta-analysis; **E2** peer-reviewed/official stats; **E3** expert consensus/preprint/open data; **E4** credible journalism/industry/primary docs; **E5** forecast/analysis; **E6** unsupported/speculative

## Metadata

| Field | Value |
|---|---|
| **Source ID** | `aifuturesmodel-2026-forecast-daniel-01-26-26` |
| **Title** | AI Futures Model — Forecasts (Daniel 01-26-26; compare Eli 01-26-26) |
| **Author(s)** | AI Futures Project (Daniel Kokotajlo; Eli Lifland) |
| **Date** | 2026-01-26 (forecast snapshot) |
| **Type** | KNOWLEDGE (interactive forecast dashboard) |
| **URL** | https://www.aifuturesmodel.com/forecast/daniel-01-26-26?cmode=forecaster&csim=eli-01-26-26&ctype=atc |
| **Reliability** | 0.58 |
| **Rigor Level** | [REVIEWED] |
| **Bias Notes** | Primary source for what the authors’ “all-things-considered” forecast distributions are at the stated snapshot date. Risks: interactive UI + dynamic charting makes capture fragile; values may change over time; and the “ATC” layer is explicitly subjective adjustment. Treat this as a disclosure artifact, not independent evidence about the world. |

**Claims YAML**: `analysis/sources/aifuturesmodel-2026-forecast-daniel-01-26-26.yaml`

## Stage 1: Descriptive Analysis

### Core Thesis
This page publishes the AI Futures Project’s milestone-arrival distributions and takeoff-speed distributions (model outputs and “all-things-considered” distributions) and provides a short changelog of forecast updates and bug fixes.

### Summary (Neutral)
The page:
- frames forecasts as probability distributions (via Monte Carlo simulation and subjective “ATC”),
- provides a change history (e.g., Dec 31, 2025 bug fix affecting TED‑AI/ASI thresholds in rare rollouts; Jan 26, 2026 numerical underflow bug fix),
- shows at least one explicitly listed ATC distribution for **Automated Coder (AC)** for Daniel and Eli (p10/p50/p90),
- discusses that the authors adjust outside the model based on intuition and omitted factors.

Because the UI is interactive, text extraction may not capture all milestone distributions (SC, SAR, TED‑AI, ASI) unless rendered as plain text; the captured excerpt includes AC p10/p50/p90 values.

### Key Claims

| # | Claim | Claim ID | Layer | Actor | Scope | Quantifier | Type | Domain | Evid | Credence | Verified? | Falsifiable By |
|---:|---|---|---|---|---|---|---|---|---|---:|---|---|
| 1 | The page states it shows model outputs + “all-things-considered” distributions and that it will be kept up to date as predictions change | META-2026-128 | PRACTICED | OTHER:AI Futures Project | who=AI Futures Project; what=forecast dashboard disclosure | N/A | [F] | META | E4 | 0.80 | In-source | The page does not describe model vs ATC forecasts or update intent |
| 2 | Daniel’s 01-26-26 **ATC** forecast for AC is (p10 **Feb 2027**, p50 **Dec 2029**, p90 **Jul 2043**) | TRANS-2026-033 | ASSERTED | OTHER:AI Futures Project | who=Daniel; what=AC distribution; when=2026-01-26 | OTHER:p10/p50/p90 | [P] | TRANS | E5 | 0.35 | In-source | Extracted text does not include these percentiles |
| 3 | Eli’s 01-26-26 **ATC** forecast for AC is (p10 **May 2027**, p50 **Mar 2032**, p90 **Jan 2125**) | TRANS-2026-034 | ASSERTED | OTHER:AI Futures Project | who=Eli; what=AC distribution; when=2026-01-26 | OTHER:p10/p50/p90 | [P] | TRANS | E5 | 0.35 | In-source | Extracted text does not include these percentiles |
| 4 | Dec 31, 2025: the changelog claims a bug fix slightly increases takeoff-speed probabilities (e.g., Eli P(AC→ASI <1y) **26.3→27.1%**, Daniel **36.7→37.1%**) | META-2026-129 | ASSERTED | OTHER:AI Futures Project | who=AI Futures Project; what=bug fix + probability deltas; when=2025-12-31 | OTHER:26.3→27.1; 36.7→37.1 | [F] | META | E4 | 0.70 | In-source | The changelog does not include these probability deltas |
| 5 | Jan 26, 2026: the changelog claims a minor numerical underflow bug fix (≈3% of rollouts; negligible effect) and reports that Eli updated his ATC views (AC median **Jul 2032→Mar 2032**; P(AC in 2026) **4%→6%**; P(takeoff <0.5y) **18%→25%**; P(takeoff <10y) **85%→83%**) | META-2026-130 | ASSERTED | OTHER:AI Futures Project | who=AI Futures Project; what=bug fix + ATC adjustments; when=2026-01-26 | OTHER:values as stated | [F] | META | E4 | 0.65 | In-source | The changelog does not include these adjustments |

### Argument Structure
This is primarily a disclosure dashboard; the implied argument is:

```
Model + parameter uncertainty → Monte Carlo distributions
        ↓
ATC adjustments for omitted factors → published ATC distributions
        ↓
Changelog documents bug fixes and forecast shifts
```

### Scope & Limitations
- Interactive UI capture may omit distributions not rendered as plain text.
- “ATC” is explicitly subjective; it is evidence of the authors’ beliefs, not evidence of truth.

## Stage 2: Evaluative Analysis

### Internal Coherence
The changelog + disclosure framing is coherent. The key limitation is epistemic: the page is about forecasts, not about new empirical evidence; and the ATC layer is intentionally non-mechanical.

### Key Factual Claims Verified

| Claim (paraphrased) | Crux? | Source Says | Actual | External Source | Status |
|---|---:|---|---|---|---|
| Daniel and Eli AC ATC p10/p50/p90 values are stated on the page | **Y** | Percentiles shown in text | Present in extracted page text | https://www.aifuturesmodel.com/forecast/daniel-01-26-26 | ok (in-source capture) |

### Disconfirming Evidence Search

| Claim | Counterevidence Found | Alternative Explanation | Search Notes |
|---|---|---|---|
| “Changelog bug fixes are negligible” | Without access to code + reproducible runs, we can’t independently confirm the magnitude of impact. | The stated % of affected rollouts may be correct, but impact depends on tail behavior and correlations. | Searched within extracted text for quantitative deltas; noted lack of independently checkable replication in this artifact alone. |

### Corrections & Updates

| Item | URL | Published | Corrected/Updated | What Changed | Impacted Claim IDs | Action Taken |
|---|---|---:|---:|---|---|---|
| Capture limitation: interactive charts | https://www.aifuturesmodel.com/forecast/daniel-01-26-26 | — | 2026-02-13 | Text extraction captured AC percentiles but not all milestone distributions | TRANS-2026-033; TRANS-2026-034 | Note as partial capture; rely on stated text only |

### Evidence Assessment
- **E4** for the dashboard’s textual changelog and displayed percentiles (primary source for their stated beliefs).
- **E5** for the forecast distributions as claims about the future.

## Stage 3: Dialectical Analysis

### Steelmanned Argument
Publishing ATC percentiles and a changelog is unusually transparent: it gives outside observers a concrete snapshot of the authors’ beliefs and how those beliefs update after fixes and reflection.

### Strongest Counterarguments
1. **UI capture fragility**: key values may not be stable or may be hidden behind interactive elements.
2. **Forecast ≠ evidence**: distributions reflect beliefs contingent on model assumptions, not independent measurements.

### Synthesis Notes
Use this dashboard as a “state of belief” snapshot (especially AC percentiles and takeoff-probability deltas) when synthesizing how AI 2027-era views evolved into 2026 forecasts.

---

### Claim Summary

| ID | Type | Domain | Layer | Actor | Scope | Quantifier | Evidence | Credence | Claim |
|---|---|---|---|---|---|---|---|---:|---|
| META-2026-128 | [F] | META | PRACTICED | OTHER:AI Futures Project | who=AI Futures Project; what=dashboard disclosure | N/A | E4 | 0.80 | Page states it shows model+ATC forecasts and will be kept updated. |
| TRANS-2026-033 | [P] | TRANS | ASSERTED | OTHER:AI Futures Project | who=Daniel; what=AC percentiles | OTHER:p10/p50/p90 | E5 | 0.35 | Daniel AC ATC p10/p50/p90 = Feb 2027 / Dec 2029 / Jul 2043. |
| TRANS-2026-034 | [P] | TRANS | ASSERTED | OTHER:AI Futures Project | who=Eli; what=AC percentiles | OTHER:p10/p50/p90 | E5 | 0.35 | Eli AC ATC p10/p50/p90 = May 2027 / Mar 2032 / Jan 2125. |
| META-2026-129 | [F] | META | ASSERTED | OTHER:AI Futures Project | who=AI Futures Project; what=bug fix deltas | OTHER:26.3→27.1; 36.7→37.1 | E4 | 0.70 | Dec 31 bug fix slightly increases fast-takeoff probabilities. |
| META-2026-130 | [F] | META | ASSERTED | OTHER:AI Futures Project | who=AI Futures Project; what=bug fix + ATC updates | OTHER:values as stated | E4 | 0.65 | Jan 26 bug fix + Eli ATC updates (AC median, takeoff probabilities). |

### Claims to Register

```yaml
claims:
  - id: "META-2026-128"
    text: "The AI Futures Model forecast dashboard states it shows Monte Carlo model outputs alongside subjective all-things-considered (ATC) distributions, and that it will be kept up to date as predictions change."
    type: "[F]"
    domain: "META"
    evidence_level: "E4"
    credence: 0.80
    operationalization: "Confirm the dashboard’s explanatory text about model outputs vs ATC and update intent."
    assumptions: ["The extracted page text reflects the dashboard content at access time."]
    falsifiers: ["The page does not contain this explanatory text."]
    source_ids: ["aifuturesmodel-2026-forecast-daniel-01-26-26"]

  - id: "TRANS-2026-033"
    text: "On the AI Futures Model dashboard (Daniel 01-26-26 snapshot), Daniel’s all-things-considered forecast for Automated Coder (AC) is p10 Feb 2027, p50 Dec 2029, p90 Jul 2043."
    type: "[P]"
    domain: "TRANS"
    evidence_level: "E5"
    credence: 0.35
    operationalization: "Locate the 'Daniel’s 01-26-26 all-things-considered forecast for AC' line and confirm percentiles."
    assumptions: ["Percentiles refer to the ATC distribution displayed for the stated snapshot."]
    falsifiers: ["The extracted page text does not include these percentiles."]
    source_ids: ["aifuturesmodel-2026-forecast-daniel-01-26-26"]

  - id: "TRANS-2026-034"
    text: "On the AI Futures Model dashboard (Daniel 01-26-26 snapshot), Eli’s all-things-considered forecast for Automated Coder (AC) is p10 May 2027, p50 Mar 2032, p90 Jan 2125."
    type: "[P]"
    domain: "TRANS"
    evidence_level: "E5"
    credence: 0.35
    operationalization: "Locate the 'Eli’s 01-26-26 all-things-considered forecast for AC' line and confirm percentiles."
    assumptions: ["Percentiles refer to the ATC distribution displayed for the stated snapshot."]
    falsifiers: ["The extracted page text does not include these percentiles."]
    source_ids: ["aifuturesmodel-2026-forecast-daniel-01-26-26"]

  - id: "META-2026-129"
    text: "On the AI Futures Model dashboard changelog, the Dec 31, 2025 entry reports a bug fix that slightly increases takeoff-speed probabilities (e.g., Eli P(AC→ASI<1y) 26.3→27.1% and Daniel 36.7→37.1%)."
    type: "[F]"
    domain: "META"
    evidence_level: "E4"
    credence: 0.70
    operationalization: "Locate the Dec 31, 2025 changelog entry and confirm the stated probability deltas."
    assumptions: ["The changelog text is accurate and pertains to the stated snapshot history."]
    falsifiers: ["The changelog entry does not include these deltas or reports different values."]
    source_ids: ["aifuturesmodel-2026-forecast-daniel-01-26-26"]

  - id: "META-2026-130"
    text: "On the AI Futures Model dashboard changelog, the Jan 26, 2026 entry reports a minor numerical underflow bug fix (≈3% of rollouts; negligible effect) and that Eli updated his ATC views (AC median Jul 2032→Mar 2032; P(AC in 2026) 4%→6%; P(takeoff<0.5y) 18%→25%; P(takeoff<10y) 85%→83%)."
    type: "[F]"
    domain: "META"
    evidence_level: "E4"
    credence: 0.65
    operationalization: "Locate the Jan 26, 2026 changelog entry and confirm the stated bug description and ATC adjustments."
    assumptions: ["The changelog text is accurate and pertains to the stated snapshot history."]
    falsifiers: ["The changelog entry does not include these adjustments or reports different values."]
    source_ids: ["aifuturesmodel-2026-forecast-daniel-01-26-26"]
```

---

**Analysis Date**: 2026-02-13  
**Analyst**: codex (GPT-5.2)  
**Credence in Analysis**: 0.70

## Analysis Log

| Pass | Date | Tool | Model | Duration | Tokens | Cost | Notes |
|---:|---|---|---|---:|---:|---:|---|
| 1 | 2026-02-13 | codex | gpt-5.2 | — | — | — | Initial analysis (partial text capture) |

