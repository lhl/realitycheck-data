# Source Analysis: Timelines Forecast — AI 2027 (Research Note)

> **Claim types**: `[F]` fact, `[T]` theory, `[H]` hypothesis, `[P]` prediction, `[A]` assumption, `[C]` counterfactual, `[S]` speculation, `[X]` contradiction  
> **Evidence**: **E1** systematic review/meta-analysis; **E2** peer-reviewed/official stats; **E3** expert consensus/preprint/open data; **E4** credible journalism/industry/primary docs; **E5** forecast/analysis; **E6** unsupported/speculative

## Metadata

| Field | Value |
|---|---|
| **Source ID** | `aifutures-2025-ai-2027-timelines-forecast` |
| **Title** | Timelines Forecast — AI 2027 |
| **Author(s)** | Eli Lifland; Nikola Jurkovic; FutureSearch |
| **Date** | 2025-04 (page header: April 2025; includes May/Dec 2025 updates) |
| **Type** | REPORT (forecast methodology + distributions) |
| **URL** | https://ai-2027.com/research/timelines-forecast |
| **Reliability** | 0.55 |
| **Rigor Level** | [REVIEWED] |
| **Bias Notes** | Produced by the AI Futures Project. Strengths: defines a concrete “superhuman coder” milestone; shows multiple methods + an all-things-considered forecast; includes parameter ranges and code links. Risks: strong conditional assumptions (no catastrophe, no slowdown, no supply-chain disruptions), heavy reliance on sparse proxy trends, and post-hoc edits (May/Dec updates) that complicate “what was believed when.” |

**Claims YAML**: `analysis/sources/aifutures-2025-ai-2027-timelines-forecast.yaml`

## Stage 1: Descriptive Analysis

### Core Thesis
The authors forecast the arrival time distribution for a “superhuman coder” (SC) milestone, using (1) a time-horizon extrapolation anchored to METR and (2) a benchmarks-and-gaps model anchored to RE‑Bench, then provide an all-things-considered forecast; they assert meaningful probability mass on SC by 2027 under strong “no catastrophe / no slowdown” assumptions.

### Summary (Neutral)
This research note is one of the quantitative backbones of AI 2027’s narrative timing. It:
- defines **Superhuman Coder (SC)** operationally (30× agents, 30× speed, under a 5% compute budget),
- presents two forecasting methods (time horizon extension; benchmarks-and-gaps),
- summarizes output distributions (medians + 80% credible intervals for some forecasts),
- adds updates (May 2025 and Dec 2025) that lengthen timelines and disclose model caveats/bugs, and
- provides an all-things-considered adjustment intended to incorporate extra-model factors (geopolitics, macro).

The note is explicit about being conditional: it assumes no large-scale catastrophes, no government/self-imposed slowdown, and no significant supply-chain disruptions.

### Key Claims

| # | Claim | Claim ID | Layer | Actor | Scope | Quantifier | Type | Domain | Evid | Credence | Verified? | Falsifiable By |
|---:|---|---|---|---|---|---|---|---|---|---:|---|---|
| 1 | The note states that (under its strong “no catastrophe / no slowdown” assumptions) its forecasts give a **substantial chance** of superhuman coding arriving “by and in 2027” | META-2026-125 | ASSERTED | OTHER:AI Futures Project | who=leading AGI company; what=SC arrival; when=by 2027; condition=no catastrophe/slowdown | OTHER:substantial chance | [P] | META | E5 | 0.35 | In-source | The note does not make this claim or materially weakens it |
| 2 | Time-horizon-extension model (Apr 2025): Eli’s SC forecast median **2027** with 80% CI **2025–2039**; Nikola’s 80% CI **2025–2033** | TRANS-2026-030 | ASSERTED | OTHER:AI Futures Project | who=leading AGI company; what=SC; when=2025–2039; method=time-horizon extension | N/A | [P] | TRANS | E5 | 0.35 | In-source | The summary table does not contain these values |
| 3 | All-things-considered forecast (Apr 2025): Eli SC median **2030** with 80% CI **2026–>2050**; Nikola SC 80% CI **2026–2040**; FutureSearch aggregate 80% CI **2027–>2050** | TRANS-2026-031 | ASSERTED | OTHER:AI Futures Project | who=leading AGI company; what=SC; when=2026–>2050; method=ATC adjustment | N/A | [P] | TRANS | E5 | 0.35 | In-source | The summary table does not contain these values |
| 4 | SC is operationalized as: with ~5% of compute, run ~30× as many agents as human research engineers, each doing AI-research coding tasks at ~30× the speed of the company’s best engineer (across any researcher’s area) | TECH-2025-075 | ASSERTED | OTHER:AI Futures Project | who=SC system; what=definition; where=AGI project coding | OTHER:30× agents; 30× speed; 5% compute | [F] | TECH | E4 | 0.80 | In-source | The note’s SC definition differs materially |
| 5 | The note sets a current (Mar 2025) **80% time-horizon doubling time** assumption of **4.5 months** with 80% CI **[2.5, 9] months**, citing METR and noting faster recent periods with few data points | TECH-2025-076 | ASSERTED | OTHER:AI Futures Project | who=frontier models; what=time-horizon doubling time assumption; when=Mar 2025 | OTHER:4.5 months | [F] | TECH | E4 | 0.65 | In-source | The note does not state this assumption/range |
| 6 | The note discloses a bug in their progress-multiplier interpolation (missing “−1/+1” transform), and claims it **overestimated intermediate speedups** with about a **9‑month impact** on SC median | META-2026-126 | ASSERTED | OTHER:AI Futures Project | who=AI Futures Project; what=model bug; effect=SC median shift | OTHER:~9 months | [F] | META | E4 | 0.70 | In-source | The bug description/effect is absent or materially different |
| 7 | Disclaimer added Dec 2025: the forecast relies substantially on **intuitive judgment** due to insufficient evidence for conclusive extrapolation | META-2026-127 | PRACTICED | OTHER:AI Futures Project | who=AI Futures Project; what=disclaimer; when=Dec 2025 | N/A | [F] | META | E4 | 0.85 | In-source | The disclaimer is not present on the page |
| 8 | The note predicts RE‑Bench “saturation” sometime in **2026**, citing an 80% CI of **[2025‑09‑01, 2031‑01‑01]** | TRANS-2026-032 | ASSERTED | OTHER:AI Futures Project | who=AI R&D benchmark; what=saturation; when=2025–2031 | N/A | [P] | TRANS | E5 | 0.30 | In-source | The note does not state this CI or does not predict 2026 central tendency |

### Argument Structure

```
(1) Define a concrete milestone: SC
        ↓
(2) Extrapolate time-horizon trend (METR) → SC arrival distribution
        ↓
(3) Alternative: anchor to RE‑Bench + gap model → SC distribution
        ↓
(4) Adjust outside-model factors → all-things-considered distribution
```

**Weakest links**:
- The mapping from eval “time horizon” to real-world “AI research engineer” work distribution.
- The validity/stability of “RE‑Bench saturation → real-world SC” gap modeling.

### Theoretical Lineage
- Exponential trend extrapolation as a default for capability proxies.
- “Milestones as regime shifts” framing for takeoff dynamics.

### Scope & Limitations
- Strong conditioning assumptions (no catastrophe/slowdown/disruptions) likely inflate “by 2027” probability mass relative to unconditional reality.
- Post-publication edits (May/Dec 2025) complicate scoring “what was predicted when.”
- The note itself acknowledges reliance on intuitive judgment.

## Stage 2: Evaluative Analysis

### Internal Coherence
The note is coherent as a forecasting exercise: define SC, run two models, then combine with an all-things-considered adjustment. The main epistemic fragility is that the hardest parts are the least measurable (research taste, autonomy reliability, integration).

### Key Factual Claims Verified

| Claim (paraphrased) | Crux? | Source Says | Actual | External Source | Status |
|---|---:|---|---|---|---|
| The note’s summary table reports SC medians / 80% CIs for multiple methods (including ATC) | **Y** | 2027 / 2030 medians with stated CIs | Present in extracted page text | https://ai-2027.com/research/timelines-forecast | ok (in-source) |
| The note discloses a “progress multiplier interpolation” bug with ~9-month impact | N | Bug + effect stated | Present in extracted page text | https://ai-2027.com/research/timelines-forecast | ok (in-source) |

### Disconfirming Evidence Search

| Claim | Counterevidence Found | Alternative Explanation | Search Notes |
|---|---|---|---|
| “Substantial chance” of SC by 2027 (conditional) | The AI Futures Project’s later model update (Dec 31, 2025) reports longer medians to coding automation and acknowledges major modeling issues in pre-automation speedups. | Even if proxy trends are steep, translation to “superhuman SWE in real orgs” may be bottlenecked by reliability, specification, and integration costs. | Cross-referenced `aifutures-2025-ai-futures-model-dec-2025-update` and METR time-horizon sensitivity (`metr-2026-time-horizon-1-1`). |

### Corrections & Updates

| Item | URL | Published | Corrected/Updated | What Changed | Impacted Claim IDs | Action Taken |
|---|---|---:|---:|---|---|---|
| May 7, 2025 update note | https://ai-2027.com/research/timelines-forecast | 2025-05-07 | 2025-05-07 | “Noticeably but not greatly” lengthened Eli’s timelines; lower but still substantial probability on SC by 2027 | TRANS-2026-030; TRANS-2026-031 | Treat as within-source revision note (not independently audited) |
| Dec 31, 2025 update note + disclaimer | https://ai-2027.com/research/timelines-forecast | 2025-12-31 | 2025-12-31 | Links to revamped model; adds disclaimer about intuitive judgment; discloses code bug | META-2026-126; META-2026-127 | Record as self-correction; downgrade confidence in stability of early forecasts |

### Evidence Assessment
- This is an **E5** forecast artifact; evidence strength is about transparency of assumptions and reproducibility, not empirical validation.

### Credence Assessment
- **Overall Credence**: 0.70 that the page reports the stated distributions/assumptions; 0.25–0.40 that the “by 2027” probability mass is well-calibrated unconditionally.

## Stage 3: Dialectical Analysis

### Steelmanned Argument
Defining SC concretely and tying it to measurable proxy trends (time horizon, benchmark saturation) is a good-faith attempt to operationalize a fuzzy milestone. Using multiple methods and disclosing uncertainty/edits provides a path for external critique and iterative improvement.

### Strongest Counterarguments
1. **Overfitting to a thin proxy**: time-horizon extrapolation may not capture real-world SWE bottlenecks.
2. **Conditional assumptions hide base-rate risks**: catastrophes, slowdowns, and supply-chain disruptions are not negligible.
3. **Model instability**: disclosed bugs and edits show high sensitivity of outputs to implementation details.

### Synthesis Notes
This note is best treated as the “quantitative backbone” of the original AI 2027 timing claim—*but* with major caveats: it is conditional, sensitive, and partly revised after publication.

---

### Claim Summary

| ID | Type | Domain | Layer | Actor | Scope | Quantifier | Evidence | Credence | Claim |
|---|---|---|---|---|---|---|---|---:|---|
| META-2026-125 | [P] | META | ASSERTED | OTHER:AI Futures Project | who=leading AGI company; what=SC arrival; when=by 2027 | OTHER:substantial chance | E5 | 0.35 | Forecasts give a substantial chance of SC arriving by/in 2027 under strong assumptions. |
| TRANS-2026-030 | [P] | TRANS | ASSERTED | OTHER:AI Futures Project | who=leading AGI company; what=SC; when=2025–2039 | N/A | E5 | 0.35 | Time-horizon-extension model outputs SC median 2027 with stated 80% CIs. |
| TRANS-2026-031 | [P] | TRANS | ASSERTED | OTHER:AI Futures Project | who=leading AGI company; what=SC; when=2026–>2050 | N/A | E5 | 0.35 | ATC SC forecast outputs stated medians/CIs. |
| TECH-2025-075 | [F] | TECH | ASSERTED | OTHER:AI Futures Project | who=SC system; what=definition | OTHER:30×/30×/5% | E4 | 0.80 | SC is defined via 30× agents, 30× speed, under 5% compute budget. |
| TECH-2025-076 | [F] | TECH | ASSERTED | OTHER:AI Futures Project | who=frontier models; what=TH doubling-time assumption | OTHER:4.5 months | E4 | 0.65 | Note states a 4.5-month doubling-time assumption with CI [2.5, 9]. |
| META-2026-126 | [F] | META | ASSERTED | OTHER:AI Futures Project | who=AI Futures Project; what=model bug | OTHER:~9 months | E4 | 0.70 | Note discloses a bug causing ~9-month effect on SC median. |
| META-2026-127 | [F] | META | PRACTICED | OTHER:AI Futures Project | who=AI Futures Project; what=disclaimer | N/A | E4 | 0.85 | Note includes a disclaimer about reliance on intuitive judgment. |
| TRANS-2026-032 | [P] | TRANS | ASSERTED | OTHER:AI Futures Project | who=RE‑Bench; what=saturation; when=2025–2031 | N/A | E5 | 0.30 | Note predicts RE‑Bench saturation in ~2026 with stated 80% CI. |

### Claims to Register

```yaml
claims:
  - id: "META-2026-125"
    text: "The AI 2027 timelines-forecast note states that, under its strong assumptions (no catastrophes/slowdown/supply-chain disruptions), its forecasts give a substantial chance of superhuman coding (SC) arriving by and in 2027."
    type: "[P]"
    domain: "META"
    evidence_level: "E5"
    credence: 0.35
    operationalization: "Define 'substantial chance' as a numeric threshold (e.g., ≥10%) and inspect the page’s stated distributions/wording for SC-by-2027 probability mass."
    assumptions: ["The conditional assumptions are satisfied."]
    falsifiers: ["The page’s distributions/wording do not support ≥10% probability mass on SC by end of 2027."]
    source_ids: ["aifutures-2025-ai-2027-timelines-forecast"]

  - id: "TRANS-2026-030"
    text: "In the AI 2027 timelines-forecast note’s Apr 2025 time-horizon-extension model, Eli’s superhuman-coder (SC) forecast has median 2027 with 80% CI 2025–2039; Nikola’s SC forecast has 80% CI 2025–2033."
    type: "[P]"
    domain: "TRANS"
    evidence_level: "E5"
    credence: 0.35
    operationalization: "Read the summary table for the time-horizon-extension model in the note and confirm the medians/CIs."
    assumptions: ["The summary table is interpreted correctly (median vs CI bounds)."]
    falsifiers: ["The table does not report these values."]
    source_ids: ["aifutures-2025-ai-2027-timelines-forecast"]

  - id: "TRANS-2026-031"
    text: "In the AI 2027 timelines-forecast note’s Apr 2025 all-things-considered forecast, Eli’s SC forecast has median 2030 with 80% CI 2026–>2050; Nikola’s SC forecast has 80% CI 2026–2040; FutureSearch aggregate has 80% CI 2027–>2050."
    type: "[P]"
    domain: "TRANS"
    evidence_level: "E5"
    credence: 0.35
    operationalization: "Read the all-things-considered section of the summary table and confirm the reported values."
    assumptions: ["The CI notation '>2050' is interpreted as open-ended tail beyond 2050."]
    falsifiers: ["The table does not report these values."]
    source_ids: ["aifutures-2025-ai-2027-timelines-forecast"]

  - id: "TECH-2025-075"
    text: "The AI 2027 timelines-forecast note defines a superhuman coder (SC) as: using ~5% of compute budget, run ~30× as many coding agents as human research engineers, each doing AI-research coding tasks at ~30× the speed of the company’s best engineer across any researcher’s area of expertise."
    type: "[F]"
    domain: "TECH"
    evidence_level: "E4"
    credence: 0.80
    operationalization: "Locate the SC definition section in the note and confirm the 5% compute / 30× agents / 30× speed elements."
    assumptions: ["The definition is intended as an operational capability threshold."]
    falsifiers: ["The note’s SC definition differs materially from this description."]
    source_ids: ["aifutures-2025-ai-2027-timelines-forecast"]

  - id: "TECH-2025-076"
    text: "The AI 2027 timelines-forecast note sets a Mar 2025 assumption that the 80% coding time-horizon doubling time is 4.5 months with an 80% CI of [2.5, 9] months (while noting different recent-period estimates with few data points)."
    type: "[F]"
    domain: "TECH"
    evidence_level: "E4"
    credence: 0.65
    operationalization: "Locate the 'Time horizon doubling time' parameter in the note and confirm the point estimate and CI."
    assumptions: ["The parameter corresponds to the authors’ modeling assumption, not a direct empirical estimate."]
    falsifiers: ["The note does not state this point estimate/CI."]
    source_ids: ["aifutures-2025-ai-2027-timelines-forecast"]

  - id: "META-2026-126"
    text: "The AI 2027 timelines-forecast note reports a code bug in interpolating the progress multiplier (missing a −1/+1 transform) that overestimated intermediate speedups and shifted the model’s SC median by about 9 months."
    type: "[F]"
    domain: "META"
    evidence_level: "E4"
    credence: 0.70
    operationalization: "Locate the 'bug in our code' paragraph and confirm the described bug and stated impact size."
    assumptions: ["The stated impact is computed relative to the prior (buggy) version of their model."]
    falsifiers: ["The note does not include this bug description or impact estimate."]
    source_ids: ["aifutures-2025-ai-2027-timelines-forecast"]

  - id: "META-2026-127"
    text: "The AI 2027 timelines-forecast note includes a Dec 2025 disclaimer that the forecast relies substantially on intuitive judgment due to insufficient evidence for conclusive extrapolation."
    type: "[F]"
    domain: "META"
    evidence_level: "E4"
    credence: 0.85
    operationalization: "Locate the Dec 2025 disclaimer text on the page and confirm its content."
    assumptions: ["The disclaimer was present on the page at access time."]
    falsifiers: ["The disclaimer text is not present on the page."]
    source_ids: ["aifutures-2025-ai-2027-timelines-forecast"]

  - id: "TRANS-2026-032"
    text: "The AI 2027 timelines-forecast note predicts RE‑Bench saturation sometime in 2026, citing an 80% CI of [2025‑09‑01, 2031‑01‑01]."
    type: "[P]"
    domain: "TRANS"
    evidence_level: "E5"
    credence: 0.30
    operationalization: "Locate the RE‑Bench saturation section and confirm the cited CI and stated central tendency."
    assumptions: ["The 'saturation' definition (score 1.5) is stable and meaningful."]
    falsifiers: ["The note does not cite this CI or does not predict 2026 central tendency."]
    source_ids: ["aifutures-2025-ai-2027-timelines-forecast"]
```

---

**Analysis Date**: 2026-02-13  
**Analyst**: codex (GPT-5.2)  
**Credence in Analysis**: 0.70

## Analysis Log

| Pass | Date | Tool | Model | Duration | Tokens | Cost | Notes |
|---:|---|---|---|---:|---:|---:|---|
| 1 | 2026-02-13 | codex | gpt-5.2 | — | — | — | Initial analysis |

