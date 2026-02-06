# Source Analysis: How Does Time Horizon Vary Across Domains? (METR)

> **Claim types**: `[F]` fact, `[T]` theory, `[H]` hypothesis, `[P]` prediction, `[A]` assumption, `[C]` counterfactual, `[S]` speculation, `[X]` contradiction
> **Evidence**: **E1** systematic review/meta-analysis; **E2** peer-reviewed/official stats; **E3** expert consensus/preprint/open data; **E4** credible journalism/industry/primary docs; **E5** opinion/forecast; **E6** unsupported/speculative

## Metadata

| Field | Value |
|---|---|
| **Source ID** | `metr-2025-time-horizon-vary-across-domains` |
| **Title** | How Does Time Horizon Vary Across Domains? |
| **Author(s)** | METR |
| **Date** | 2025-07-14 |
| **Type** | ARTICLE (research blog post) |
| **URL** | https://metr.org/blog/2025-07-14-how-does-time-horizon-vary-across-domains/ |
| **Reliability** | 0.70 |
| **Rigor Level** | [REVIEWED] |
| **Bias Notes** | METR is extending a metric it introduced earlier (time horizon) to additional benchmarks. The post’s strength is that it operationalizes cross-domain comparisons with published code and (in many cases) public leaderboard data. Main risks: apples-to-oranges comparisons across benchmarks (tooling, agents, evaluation protocols), reliance on assumed parameters when only aggregate performance is available, and “benchmark availability bias” (domains with good public data are not necessarily the domains that matter for real-world automation or risk). |

**Claims YAML**: [`analysis/sources/metr-2025-time-horizon-vary-across-domains.yaml`](metr-2025-time-horizon-vary-across-domains.yaml)

## Stage 1: Descriptive Analysis

### Core Thesis
Time horizon estimates and growth rates are not uniform across domains: METR argues that many “texty”/tool-friendly domains show fast (often exponential) horizon growth, while agentic GUI tasks and self-driving show much shorter horizons and/or slower progress—implying that capability bottlenecks may be domain-specific.

### Summary (Neutral)
Building on METR’s time horizon metric (p50 task length a model can complete), this post asks whether similar trends hold outside software/research tasks. METR estimates horizons for additional benchmarks by fitting the same logistic model when human task time estimates and performance across difficulty splits are available; when only overall performance is available, they assume a value of the difficulty slope parameter (β), producing noisier estimates.

They compile and plot time horizon trends across several benchmarks (coding, QA, math contests, agentic GUI/computer use, self-driving, etc.) and claim they observe exponential or super-exponential growth in many “LLM-friendly” domains, but substantial variation in both absolute horizons and growth rates. A headline comparison: coding/math/QA show horizons on the order of tens to hundreds of minutes and doubling times of a few months, whereas OSWorld (GUI agents) shows horizons that are orders of magnitude shorter, and Tesla FSD improves more slowly than the LLM domains in their comparison.

### Key Claims

| # | Claim | Claim ID | Layer | Actor | Scope | Quantifier | Type | Domain | Evid | Credence | Verified? | Falsifiable By |
|---:|---|---|---|---|---|---|---|---|---|---:|---|---|
| 1 | METR extends the time-horizon method to other benchmarks by fitting the same logistic model via MLE when (a) human task lengths and (b) split-by-difficulty performance data exist; otherwise it assumes β, giving noisier horizons | META-2025-003 | ASSERTED | OTHER:METR | who=METR; what=method extension; inputs=human time + split scores; alt=assume β | N/A | [F] | META | E4 | 0.75 | In-source (Methodology) | Released code/post uses different method or does not require splits |
| 2 | METR claims it finds exponential or super-exponential growth in time-horizon trends “everywhere we look,” with large spread across domains | TECH-2025-058 | ASSERTED | OTHER:METR | who=benchmarks; what=growth form; where=multiple domains; when=2019–2025-ish | OTHER:exp/super-exp | [H] | TECH | E3 | 0.60 | In-source (Conclusion) | Reanalysis of the same datasets finds mostly non-exponential trends |
| 3 | Coding, math contest, and QA benchmarks show ~30–200+ minute horizons doubling roughly every ~2–6 months (with METR-HRS “middle of the pack”) | TECH-2025-059 | ASSERTED | OTHER:METR | who=benchmarks; what=absolute horizons + doubling times; where=coding/math/QA | OTHER:~2–6 months | [F] | TECH | E3 | 0.65 | In-source (Conclusion/Results) | Cross-domain-horizon data or replications show substantially different horizons/doubling times |
| 4 | Agentic GUI tasks (OSWorld) have horizons ~100× shorter than coding or math | TECH-2025-060 | ASSERTED | OTHER:METR | who=OSWorld; what=horizon relative scale; compare=coding/math | OTHER:~100× | [F] | TECH | E3 | 0.70 | In-source (Conclusion) | OSWorld horizon estimates are comparable in magnitude to coding/math (not orders smaller) |
| 5 | Tesla self-driving progress (in their chosen proxy) has improved much slower than the LLM benchmark domains | TECH-2025-061 | ASSERTED | OTHER:METR | who=Tesla FSD; what=rate of improvement; compare=LLM benchmarks | OTHER:much slower | [H] | TECH | E4 | 0.55 | In-source (Conclusion) | Alternative measures show Tesla improving at similar rates; or METR proxy is invalid |
| 6 | The time-horizon metric is only sound when task length correlates with difficulty; this can fail via label noise, “reward-hackable” tasks, or weakly length-related difficulty | META-2025-004 | ASSERTED | OTHER:METR | who=time-horizon metric; what=soundness condition; failure modes=multiple | N/A | [T] | META | E4 | 0.70 | In-source (Soundness section) | Demonstrations that length–difficulty correlation is unnecessary for horizon validity |
| 7 | Current evidence still comes from a limited set of domains where AIs are relatively strong; measuring more “short-horizon” domains could clarify bottlenecks to dangerous capabilities and AI R&D automation | META-2025-005 | ASSERTED | OTHER:METR | who=benchmarks; what=domain coverage limitation; why=bottleneck evidence | N/A | [H] | META | E5 | 0.60 | In-source (Limitations) | Broader domain measurements show no such bottleneck pattern |

### Argument Structure

```
(1) Time horizon is a useful autonomy-oriented metric
        ↓
(2) METR-HRS is software/research-heavy → domain bias concern
        ↓
(3) Estimate horizons on other benchmarks (MLE where possible; otherwise assume β)
        ↓
(4) Result: big domain variation (coding/math/QA high & fast; OSWorld low; Tesla slow)
        ↓
(5) Therefore: interpret capability trajectories + bottlenecks in a domain-specific way
```

**Weakest links**:
- (3): comparability across benchmarks; reliance on assumed β when only aggregate scores exist.
- (4): whether “time horizon” has the same meaning across domains with different evaluation structures.

### Theoretical Lineage
- **Benchmark-to-impact translation**: tries to map benchmark scores to a more interpretable “ability to sustain action” quantity.
- **Forecasting + risk management**: emphasizes identifying bottleneck domains relevant to “dangerous capabilities” and R&D automation.

### Scope & Limitations
- Uses a patchwork of benchmarks with different designs, agents, and tooling; comparisons are inherently protocol-dependent.
- Evidence is constrained by what has public leaderboards and human-time proxies.
- Some domains (e.g., physical-world tasks, organizational work) are underrepresented.

## Stage 2: Evaluative Analysis

### Internal Coherence
The post is coherent in separating (a) estimating horizons and (b) interpreting cross-domain differences. The main fragility is that cross-domain comparisons inherit unmodeled differences in evaluation protocols (tools, agents, budgets) and that assumed-β estimates can be more “modeling priors” than measurements.

### Key Factual Claims Verified

| Claim (paraphrased) | Crux? | Source Says | Actual | External Source | Status |
|---|---:|---|---|---|---|
| OSWorld horizons are ~orders of magnitude smaller than coding/math horizons | **Y** | OSWorld ~100× shorter | In METR’s released `cross-domain-horizon` repo (commit `e97c024…`), the computed OSWorld horizons for top models are ~1–2 minutes (e.g., ~1.79), while coding-like horizons on HCAST-RS are tens to ~100+ minutes (e.g., ~117) and math horizons can be ~100–300+ minutes (e.g., ~178–364). Ratios are ~60× to ~200× depending on comparator. | https://github.com/METR/cross-domain-horizon | ok (direction + magnitude) |
| METR provides public code/data artifacts for the cross-domain horizon estimates | N | analysis code available | The `cross-domain-horizon` repo contains benchmark configuration + processed horizon CSVs under `data/horizons/` and raw score artifacts for several domains. | https://github.com/METR/cross-domain-horizon | ok |
| The extension method uses frontier-only regression and only includes models with intermediate accuracy ranges | N | filters/assumptions described | The repo README states: frontier-only fit; only models with 10–90% benchmark performance; “best agent” per model. | https://github.com/METR/cross-domain-horizon | ok (as implemented/documented) |

### Disconfirming Evidence Search

| Claim | Counterevidence Found | Alternative Explanation | Search Notes |
|---|---|---|---|
| “Super-exponential” is common | The post’s own robustness/limitations sections highlight noise and method sensitivity | Apparent super-exponential regions can arise from sparse data, regime changes (agent scaffolds), or saturation effects in benchmark scoring | Reviewed internal caveats; did not locate an external replication in this pass |
| Tesla is “much slower” | Tesla proxy data contain missing values and may not reflect the right “time horizon” construct | Different progress metrics (interventions/mile, safety outcomes) could show different trends; comparisons may be apples-to-oranges vs LLM benchmarks | Inspected `data/horizons/tesla_fsd.csv`; treated as suggestive rather than definitive |
| OSWorld is “~100× shorter” | Ratio depends on which comparator benchmark/model you pick | OSWorld may be bottlenecked by UI grounding and tool reliability; horizon is short even when reasoning is strong | Verified direction with repo-provided horizons; note comparator sensitivity |

### Corrections & Updates

| Item | URL | Published | Corrected/Updated | What Changed | Impacted Claim IDs | Action Taken |
|---|---|---:|---:|---|---|---|
| N/A | N/A | N/A | N/A | No corrections observed during capture | N/A | None |

### Internal Tensions / Self-Contradictions

| Tension | Parts in Conflict | Implication |
|---|---|---|
| “Same logistic model everywhere” vs domain heterogeneity | Method assumes a common form, but benchmarks differ radically | Cross-domain “horizon” may not be a single comparable quantity without extra normalization |

### Persuasion Techniques

| Technique | Example from Source | Effect on Reader |
|---|---|---|
| Many trend lines on one chart | Multi-domain overlay plots | Creates strong “universal acceleration” gestalt even when some lines are noisy or assumption-driven |
| Domain bottleneck framing | OSWorld/Tesla as laggards | Encourages a “single bottleneck” story; may underweight partial automation in mixed workflows |

### Unstated Assumptions

| Assumption | Claim ID | Critical? | Problematic? |
|---|---|---:|---:|
| The “frontier-only” envelope is the relevant object for forecasting | TECH-2025-058 | Y | ? |
| Benchmarks’ human-time proxies correspond to real-world time | META-2025-003 | Y | Y |
| Using different “best agents” per model preserves comparability | META-2025-003 | Y | Y |

### Evidence Assessment
Strengths: links to a public analysis repo that includes processed horizon tables enabling partial independent checks; and it explicitly discusses soundness conditions and limitations. Weaknesses: comparability is protocol-dependent, and some domains rely on assumed parameters due to missing task-level data.

### Credence Assessment
- **Overall Credence**: 0.68
- **Reasoning**: High confidence in the directional claim that agentic GUI horizons are far shorter than coding/math in the provided cross-domain artifacts. Moderate confidence in specific doubling-time numbers across each benchmark (method sensitivity). Lower confidence in “Tesla much slower” as a general capability comparison due to proxy ambiguity.

## Stage 3: Dialectical Analysis

### Steelmanned Argument
If you want to forecast when AIs can automate dangerous or economically important work, you should identify which *domains* have long horizons and fast growth. Cross-domain horizon estimates provide evidence that LLM-centric domains (coding/math/QA) are accelerating quickly, while UI-grounding and embodied/real-world feedback loops remain bottlenecks. This helps prioritize evaluation design and policy: don’t assume “coding trend” transfers to everything.

### Strongest Counterarguments
1. **Cross-domain incomparability**: “horizon” may not be comparable across benchmarks with different scoring and agent/tooling constraints.
2. **Assumption-driven estimates**: when only aggregate performance exists, β assumptions can dominate.
3. **Selection bias**: benchmarks are chosen because they exist and are popular; missing domains might dominate real-world automation/risk.

### Supporting Theories

| Theory/Framework | Source ID | How It Supports |
|---|---|---|
| Domain-specific bottlenecks | N/A | Different tool/environment grounding tasks can dominate autonomy limits |

### Contradicting Theories

| Theory/Framework | Source ID | Point of Conflict |
|---|---|---|
| “Single scaling law” expectations | N/A | Cross-domain variation suggests multiple bottlenecks, not one smooth capability axis |

### Synthesis Notes
This post is valuable for preventing “single trendline” overreach: even if coding horizons are rising quickly, GUI grounding (and likely other real-world interaction domains) may lag by orders of magnitude, shaping what “autonomy” looks like in practice.

### Claims to Cross-Reference
- `TECH-2025-055` / METR’s within-domain ~7-month doubling claim.
- Task-suite/protocol sensitivity documented in TH1.1 update (`metr-2026-time-horizon-1-1`).

---

### Claim Summary

| ID | Type | Domain | Layer | Actor | Scope | Quantifier | Evidence | Credence | Claim |
|---|---|---|---|---|---|---|---|---:|---|
| META-2025-003 | [F] | META | ASSERTED | OTHER:METR | who=METR; what=MLE vs assumed-β estimation | N/A | E4 | 0.75 | METR extends horizon estimation across benchmarks via MLE when human times + splits exist; otherwise assumes β |
| TECH-2025-058 | [H] | TECH | ASSERTED | OTHER:METR | who=benchmarks; what=exp/super-exp growth | OTHER:exp/super-exp | E3 | 0.60 | METR claims exp/super-exp horizon growth across many domains |
| TECH-2025-059 | [F] | TECH | ASSERTED | OTHER:METR | who=coding/math/QA; what=30–200+ min and ~2–6 month doubling | OTHER:~2–6 months | E3 | 0.65 | Coding/math/QA show 30–200+ minute horizons doubling every ~2–6 months |
| TECH-2025-060 | [F] | TECH | ASSERTED | OTHER:METR | who=OSWorld; what=~100× shorter vs coding/math | OTHER:~100× | E3 | 0.70 | OSWorld horizons are ~100× shorter than coding/math horizons |
| TECH-2025-061 | [H] | TECH | ASSERTED | OTHER:METR | who=Tesla FSD; what=slower improvement | OTHER:much slower | E4 | 0.55 | Tesla self-driving improved much slower than LLM benchmark domains (per their proxy) |
| META-2025-004 | [T] | META | ASSERTED | OTHER:METR | who=metric; what=soundness condition | N/A | E4 | 0.70 | Metric soundness depends on task length correlating with difficulty; can fail via noise/hacking/etc |
| META-2025-005 | [H] | META | ASSERTED | OTHER:METR | who=benchmarks; what=limited domain evidence; why=bottleneck insight | N/A | E5 | 0.60 | Evidence still limited; more domains could clarify bottlenecks to dangerous capabilities/R&D automation |

### Claims to Register

```yaml
claims:
  - id: "META-2025-003"
    text: "METR extends its time-horizon method across benchmarks by fitting the same logistic model via MLE when human task lengths and split-by-difficulty performance data exist; when only aggregate performance exists, METR assumes a value for the difficulty slope parameter (β), yielding noisier horizon estimates."
    type: "[F]"
    domain: "META"
    evidence_level: "E4"
    credence: 0.75
    operationalization: "Inspect METR’s cross-domain code and confirm which benchmarks use full MLE with task-length/split data vs assumed-β methods."
    assumptions: []
    falsifiers: ["The released code does not use MLE on log(human time) as described, or does not assume β in the stated cases."]
    source_ids: ["metr-2025-time-horizon-vary-across-domains"]

  - id: "TECH-2025-058"
    text: "METR claims to observe exponential or super-exponential growth in time-horizon trends across many benchmarks/domains it examined, though with large variation in rates."
    type: "[H]"
    domain: "TECH"
    evidence_level: "E3"
    credence: 0.60
    operationalization: "For each benchmark, fit a log-linear trend to frontier horizon points over time and test whether growth is approximately exponential vs better explained by other forms or regime changes."
    assumptions: ["Frontier-only envelope is the correct object for trend fitting."]
    falsifiers: ["Across benchmarks, trend fits are inconsistent with exponential-like growth once protocol changes and noise are modeled."]
    source_ids: ["metr-2025-time-horizon-vary-across-domains"]

  - id: "TECH-2025-059"
    text: "METR reports that coding, math contest, and QA benchmarks show time horizons on the order of ~30–200+ minutes for strong models, with horizon doubling times roughly ~2–6 months (with METR-HRS in the middle of the pack)."
    type: "[F]"
    domain: "TECH"
    evidence_level: "E3"
    credence: 0.65
    operationalization: "From METR’s cross-domain data, extract per-benchmark horizon estimates and estimate doubling times using consistent regression windows and frontier selection rules."
    assumptions: ["Horizon values computed for each benchmark are comparable within that benchmark over time."]
    falsifiers: ["Recomputed horizons/doubling times fall substantially outside the stated ranges for most benchmarks."]
    source_ids: ["metr-2025-time-horizon-vary-across-domains"]

  - id: "TECH-2025-060"
    text: "METR reports that agentic GUI/computer-use tasks (OSWorld) have time horizons roughly ~100× shorter than coding or math benchmarks."
    type: "[F]"
    domain: "TECH"
    evidence_level: "E3"
    credence: 0.70
    operationalization: "Compare OSWorld horizon estimates to coding/math horizon estimates computed under METR’s cross-domain methodology for comparable model snapshots."
    assumptions: ["OSWorld’s horizon definition is meaningfully comparable (as a proxy) to other benchmarks’ horizon definitions."]
    falsifiers: ["OSWorld horizon estimates are within the same order of magnitude as coding/math horizons under consistent computation."]
    source_ids: ["metr-2025-time-horizon-vary-across-domains"]

  - id: "TECH-2025-061"
    text: "METR claims Tesla self-driving (under its chosen proxy) has improved much more slowly than the time-horizon trends on LLM benchmark domains like coding, math, and QA."
    type: "[H]"
    domain: "TECH"
    evidence_level: "E4"
    credence: 0.55
    operationalization: "Recompute Tesla proxy trend with documented data source; compare its implied growth rate to the LLM benchmark horizons under the same trend-fitting rules."
    assumptions: ["The Tesla proxy is a meaningful measure of autonomy/time horizon for driving-related capability."]
    falsifiers: ["Alternative validated driving metrics show similar or faster improvement rates than the LLM benchmarks in the same period."]
    source_ids: ["metr-2025-time-horizon-vary-across-domains"]

  - id: "META-2025-004"
    text: "METR argues the time-horizon metric is only sound when task length correlates with difficulty; this can fail due to label noise, reward-hackable tasks, or weak relationships between time and difficulty."
    type: "[T]"
    domain: "META"
    evidence_level: "E4"
    credence: 0.70
    operationalization: "For each benchmark, estimate correlation between human time and empirical difficulty, and test sensitivity of horizon to known label noise and reward-hackability."
    assumptions: ["Time-horizon aims to approximate a difficulty axis rather than an arbitrary rescaling of benchmark score."]
    falsifiers: ["Demonstrations show time-horizon remains stable and meaningful even when time–difficulty correlation is weak or absent."]
    source_ids: ["metr-2025-time-horizon-vary-across-domains"]

  - id: "META-2025-005"
    text: "METR claims existing cross-domain evidence still comes from a limited set of domains where AIs are relatively strong, and that measuring more (especially shorter-horizon) domains could clarify bottlenecks to dangerous capabilities and AI R&D automation."
    type: "[H]"
    domain: "META"
    evidence_level: "E5"
    credence: 0.60
    operationalization: "Expand evaluations into domains where current models have short horizons (minutes or less) and test whether horizon growth is bottlenecked by specific interaction/grounding constraints."
    assumptions: ["Missing domains could be more bottlenecked than the currently measured ones."]
    falsifiers: ["Broad domain expansion shows similar horizon growth rates and little evidence of domain-specific bottlenecks."]
    source_ids: ["metr-2025-time-horizon-vary-across-domains"]
```

---

**Analysis Date**: 2026-02-06
**Analyst**: codex (gpt-5.2)
**Credence in Analysis**: 0.68

**Credence Reasoning**:
- Cross-domain-horizon repo artifacts support the headline “OSWorld much shorter” claim.
- Many other domain comparisons depend on proxy choices and assumption-heavy estimation (assumed β).

## Analysis Log

| Pass | Date | Tool | Model | Duration | Tokens | Cost | Notes |
|---:|---|---|---|---:|---:|---:|---|
| 1 | 2026-02-06 | codex-cli | gpt-5.2 | ? | ? | ? | Initial 3-stage analysis with spot-check of `cross-domain-horizon` processed horizon tables |

