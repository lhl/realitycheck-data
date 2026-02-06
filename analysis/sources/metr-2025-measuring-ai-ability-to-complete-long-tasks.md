# Source Analysis: Measuring AI Ability to Complete Long Tasks (METR blog)

> **Claim types**: `[F]` fact, `[T]` theory, `[H]` hypothesis, `[P]` prediction, `[A]` assumption, `[C]` counterfactual, `[S]` speculation, `[X]` contradiction
> **Evidence**: **E1** systematic review/meta-analysis; **E2** peer-reviewed/official stats; **E3** expert consensus/preprint/open data; **E4** credible journalism/industry/primary docs; **E5** opinion/forecast; **E6** unsupported/speculative

## Metadata

| Field | Value |
|---|---|
| **Source ID** | `metr-2025-measuring-ai-ability-to-complete-long-tasks` |
| **Title** | Measuring AI Ability to Complete Long Tasks |
| **Author(s)** | METR (Thomas Kwa et al.) |
| **Date** | 2025-03-19 |
| **Type** | ARTICLE (research blog post) |
| **URL** | https://metr.org/blog/2025-03-19-measuring-ai-ability-to-complete-long-tasks/ |
| **Reliability** | 0.75 |
| **Rigor Level** | [REVIEWED] |
| **Bias Notes** | METR is an eval-focused org with incentives to (a) frame its measurement approach as useful and (b) emphasize the interpretability/forecasting relevance of observed capability trends. The post’s empirical backbone is backed by a linked preprint + released code/data, but the key generalization step (“benchmarks → real-world autonomy”) is uncertain and could bias narratives toward faster timelines. The page also includes a “do not train” data warning/canary (avoid copying canary text). |

**Claims YAML**: [`analysis/sources/metr-2025-measuring-ai-ability-to-complete-long-tasks.yaml`](metr-2025-measuring-ai-ability-to-complete-long-tasks.yaml)

## Stage 1: Descriptive Analysis

### Core Thesis
METR proposes measuring agentic capability by the *length (human time)* of tasks a model can complete reliably, argues this “time horizon” has grown roughly exponentially (doubling on the order of months), and suggests this provides a more decision-relevant anchor for forecasting than many benchmark scores.

### Summary (Neutral)
The post motivates a metric intended to map benchmark performance into something closer to “real-world autonomy”: how long a qualified human takes to complete tasks that the AI can complete with a given probability (e.g., 50%). The core methodological move is to (i) collect tasks with human time estimates, (ii) run model agents on those tasks, (iii) fit a logistic success curve against (log) human time, and (iv) read off the task duration corresponding to a fixed success probability as the model’s “time horizon.”

Empirically, METR reports that human task time is strongly predictive of model success on their task suite, and that frontier models historically perform near-perfectly on very short tasks and poorly on multi-hour tasks. They present time horizon estimates for models released since 2019 and argue the frontier 50%-time-horizon has been rising roughly exponentially with a ~7-month doubling time (with wide confidence intervals and potential recent acceleration). The post then extrapolates this trend (conditional on generalization) to argue that multi-day/week and potentially month-long autonomy may be reachable within years, with major implications for forecasting and risk management.

### Key Claims

| # | Claim | Claim ID | Layer | Actor | Scope | Quantifier | Type | Domain | Evid | Credence | Verified? | Falsifiable By |
|---:|---|---|---|---|---|---|---|---|---|---:|---|---|
| 1 | METR defines a model’s 50% “task-completion time horizon” as the human task duration where the model succeeds with 50% probability | META-2025-001 | ASSERTED | OTHER:METR | who=models; what=definition of time horizon; success=50%; duration=human minutes | N/A | [F] | META | E4 | 0.90 | In-source (definition/summary) | METR paper/docs define time horizon differently |
| 2 | METR estimates time horizons by fitting a logistic success curve as a function of (log) human task time and reading off the duration at a fixed success probability | META-2025-002 | ASSERTED | OTHER:METR | who=METR; what=logistic fit; x=human time; y=success; output=horizon | N/A | [F] | META | E4 | 0.85 | In-source (methods description) | Released code/paper uses materially different estimation procedure |
| 3 | On METR’s suite, human task time strongly predicts model success; for a current frontier model at the time of writing, success is ~100% for tasks <4 min and <10% for tasks >4 hours | TECH-2025-054 | ASSERTED | OTHER:METR | who=frontier agents; what=success rates vs duration; where=METR-HRS-like suite; when=~2024-2025 | OTHER:<4 min vs >4 h | [F] | TECH | E3 | 0.80 | In-source (results narrative) | Released run data show materially different success vs duration relationship |
| 4 | METR reports frontier 50%-time-horizon has doubled roughly every ~7 months over ~2019–2025, with 95% CI via hierarchical bootstrap over task families/tasks/attempts | TECH-2025-055 | ASSERTED | OTHER:METR | who=frontier models; what=p50 horizon trend; when=2019-2025; ci=hierarchical bootstrap | OTHER:~7 months | [F] | TECH | E3 | 0.75 | In-source (figure caption/summary) | Independent reanalysis of released data yields materially different doubling time |
| 5 | METR claims fits focused on 2024–2025 imply faster progress, shortening the estimated date for month-long (p50) autonomy by ~2.5 years vs longer-history fits | TECH-2025-056 | ASSERTED | OTHER:METR | who=frontier models; what=recent-period fit; when=2024-2025; target=~month tasks; delta≈2.5y | OTHER:recent-only fit | [F] | TECH | E3 | 0.60 | In-source (extrapolation discussion) | Reproductions of their fit do not show this shift |
| 6 | Conditional on generalization to real-world SWE tasks, extrapolating the trend suggests within years-to-<10 years models could autonomously complete many tasks that take humans days/weeks (and potentially month-scale tasks within ~5 years) | TECH-2025-057 | ASSERTED | OTHER:METR | who=future frontier models; what=autonomous completion; tasks=days/weeks/month; when=~by 2030s | OTHER:<10y | [P] | TECH | E5 | 0.40 | In-source (forecasting implications) | Trend slows/plateaus; or real-world tasks don’t match benchmark distribution |
| 7 | METR has released analysis code and raw run data publicly (and invites replication/extension) | INST-2025-002 | PRACTICED | OTHER:METR | who=METR; what=open-source release; where=GitHub; when=2025+ | N/A | [F] | INST | E4 | 0.85 | In-source (links) | Repos/data are removed or are not sufficient to reproduce plots |

### Argument Structure

```
(1) Benchmark scores are hard to interpret for real-world autonomy
        ↓
(2) Human time-to-complete is a natural “difficulty” axis for multi-step tasks
        ↓
(3) Fit success vs (log) human time ⇒ define “time horizon” at fixed success probability
        ↓
(4) Time horizon has risen ~exponentially (≈7-month doubling) with wide CIs
        ↓
(5) If this generalizes, extrapolation implies rapid approach to multi-hour/day/week autonomy
```

**Weakest links**:
- (2–3): whether human time is a stable, transferable “difficulty” axis across task distributions and over time (and whether “agent scaffold” changes confound the curve).
- (5): external validity and “trend extrapolation” risk (distribution shift, ceiling effects, changing evaluation protocols).

### Theoretical Lineage
- **t-AGI / time-to-complete framing**: connects capability to elapsed time and autonomous action sequences rather than static QA accuracy.
- **Agentic evaluation tradition**: multi-step tasks with tool use; success/failure trajectories; focus on reliability under compounding errors.
- **Forecasting anchors**: the post explicitly links the approach to forecasting work (e.g., “Bio Anchors”-style reasoning) where “time to do real work” is salient.

### Scope & Limitations
- **Domain narrowness**: tasks are largely software/research-style tasks (METR-HRS family); generalization to other domains is unknown.
- **Scaffold confounds**: measured horizon can reflect tooling, agent scaffolds, and prompting policies, not just base-model capability.
- **Time-estimate quirks**: human time estimation choices (e.g., excluding codebase familiarization) can bias absolute durations and trend slope.
- **Protocol evolution**: METR updates task suites/infrastructure (later TH1.1), complicating trend comparisons and increasing “moving target” risk.

## Stage 2: Evaluative Analysis

### Internal Coherence
The conceptual path from “long tasks are hard” → “measure capability by task length” is coherent, and logistic “success vs duration” curves are a plausible summary statistic. The main fragility is interpretive: the metric’s usefulness for *forecasting real autonomy* depends on whether the benchmark’s task distribution and the deployed agent scaffolds are representative (and stable) enough to extrapolate.

### Key Factual Claims Verified

| Claim (paraphrased) | Crux? | Source Says | Actual | External Source | Status |
|---|---:|---|---|---|---|
| Frontier 50%-time-horizon doubled ~every 7 months since 2019 | **Y** | ~7-month doubling | The linked arXiv preprint abstract states “doubling approximately every seven months since 2019.” A quick independent re-fit using METR’s released TH1.0 raw runs (`eval-analysis-public`, commit `8d68adb…`) gives ~197 days doubling (R²≈0.98) when fitting a log-linear trend to the frontier envelope of per-model p50 horizons. | https://arxiv.org/abs/2503.14499 ; https://github.com/METR/eval-analysis-public | ok (direction + magnitude match) |
| “<4 min ≈100% success; >4 hours <10% success” holds for a frontier model around early 2025 | N | near-100% for short tasks; <10% for >4h | Using METR’s released TH1.0 runs for **Claude 3.7 Sonnet** (released 2025-02-24), success on tasks <4 min is 100% (n=584) and on tasks >4h is ~4.1% (n=195). | `eval-analysis-public` TH1.0 `runs.jsonl` (commit `8d68adb…`) | ok (for Claude 3.7 Sonnet; later models differ) |
| METR released code + raw run data publicly | **Y** | analysis code + raw data available | Public repo contains analysis code and raw runs JSONL for TH1.0 (~23MB) and TH1.1 (~9.7MB), plus release dates file. | https://github.com/METR/eval-analysis-public | ok |

### Disconfirming Evidence Search

| Claim | Counterevidence Found | Alternative Explanation | Search Notes |
|---|---|---|---|
| “Time horizon” meaningfully tracks real autonomy | No direct refutation located in this pass; main issues are external-validity concerns | Benchmarks may overstate progress if they concentrate on tool-friendly tasks or if agent scaffolds improve faster than underlying models | Looked for explicit critiques; noted METR itself flags external validity limits in the linked preprint |
| ~7-month doubling persists | METR’s later TH1.1 update reports some sensitivity to task composition/protocols; extrapolation is risky | The trend could be “partly real” but not stable: protocol updates, task suite drift, and saturation could change slope | Checked TH1.1 update post; replicated TH1.0/TH1.1 slopes from released data (see other analysis) |
| Near-term month-scale autonomy extrapolation | No direct counter-study found in this pass | Even with exponential trend in benchmarks, real-world month projects may fail due to coordination/requirements ambiguity/security constraints | General forecasting caveat; not a specific refutation |

### Corrections & Updates

| Item | URL | Published | Corrected/Updated | What Changed | Impacted Claim IDs | Action Taken |
|---|---|---:|---:|---|---|---|
| Page now functions as a “live dashboard” landing page referencing TH1.1 and TH1.0 | https://metr.org/blog/2025-03-19-measuring-ai-ability-to-complete-long-tasks/ | 2025-03-19 | (observed) 2026-02-06 | The top of the page includes “Time Horizon 1.1 (Current)” and links to updated computations, suggesting the page content is evolving beyond the original publication date | TECH-2025-055, TECH-2025-056 | Treat as a living artifact; prefer citing arXiv + pinned repo commits for stable references |

### Internal Tensions / Self-Contradictions

| Tension | Parts in Conflict | Implication |
|---|---|---|
| “Models can’t do substantive projects” vs aggressive extrapolation | Post notes current agents can’t do full projects; later extrapolation points toward month-scale tasks soon | Highlights that extrapolation depends on stability of failure modes and task distribution, not only average success rates |

### Persuasion Techniques

| Technique | Example from Source | Effect on Reader |
|---|---|---|
| Exponential-growth framing | “doubling time of around 7 months” + “under a decade” | Encourages “near-vertical” intuition on linear plots; can over-anchor on trend continuation |
| “Real-world interpretation” emphasis | Frames metric as mapping directly to autonomy | Risks overstating external validity relative to standard benchmarks |
| Error-bar de-emphasis | Wide CIs exist but the headline is the point estimate trend | Readers may underweight the uncertainty from task suite choices and bootstrap variance |

### Unstated Assumptions

| Assumption | Claim ID | Critical? | Problematic? |
|---|---|---:|---:|
| Human time is a stable proxy for task difficulty across time and domains | META-2025-001, TECH-2025-054 | Y | ? |
| Agent scaffolds are comparable across model generations | TECH-2025-055 | Y | Y |
| The measured task distribution approximates the “important” real-world task distribution | TECH-2025-057 | Y | Y |
| Short-horizon competence composes into long-horizon autonomy smoothly as horizon grows | TECH-2025-057 | Y | ? |

### Evidence Assessment
Strengths: linked preprint, released analysis code, and released raw run data enable partial independent checks. Weaknesses: the “forecasting implications” step relies on extrapolation and external validity; and the metric is sensitive to task suite design and protocol changes.

### Credence Assessment
- **Overall Credence**: 0.72
- **Reasoning**: High confidence that METR’s definition/method and the empirical “~7-month doubling” claim reflect their reported analyses (and the raw data broadly supports this). Moderate confidence that the metric is a useful forecasting anchor beyond the studied task distribution. Low-to-moderate confidence in aggressive extrapolations to month-scale real-world autonomy without further evidence.

## Stage 3: Dialectical Analysis

### Steelmanned Argument
Autonomy failures often come from compounding small errors across long action sequences. A metric explicitly tied to *task length* is therefore closer to real impact than exam-style accuracy. If time horizon has been improving exponentially for years across a diverse suite, that is a rare, quantitative, decision-relevant trendline. Even with uncertainty, it provides a grounded way to discuss “how close are we to models doing meaningful projects?” and to update forecasts as new model runs arrive.

### Strongest Counterarguments
1. **External validity is the crux**: The task distribution is not the real world; organizational tasks include ambiguity, coordination, and environment complexity not captured by benchmark tasks.
2. **Scaffold confounding**: Measured horizon can grow due to better agent frameworks/tooling rather than core model capability.
3. **Protocol drift / saturation**: Updating task suites and infra changes the measured quantity; near-frontier saturation can make trends look steeper or noisier.

### Supporting Theories

| Theory/Framework | Source ID | How It Supports |
|---|---|---|
| “Time-to-do-work” as capability anchor | N/A | Treats capability as ability to sustain coherent action for longer periods |
| t-AGI framing | N/A | Places timelines in terms of task duration rather than abstract “AGI” definitions |

### Contradicting Theories

| Theory/Framework | Source ID | Point of Conflict |
|---|---|---|
| “Benchmarks don’t predict deployment” skepticism | N/A | Even good trends can fail to map to real organizational automation |
| Verification bottleneck | ronacher-2026-agent-psychosis | If verification dominates cost, longer-horizon autonomy may not translate into net automation |

### Synthesis Notes
This source is most useful as a *quantitative anchor* for “how long can agents reliably act?” It provides evidence for an exponential capability trend in one family of tasks, but the key uncertainty is how quickly that translates into real-world project autonomy (and which domains are bottlenecking).

### Claims to Cross-Reference
- AI-2027-style timeline arguments that cite ~7-month doubling for coding autonomy (e.g., `TECH-2025-051` in `aifutures-2025-ai-2027`).
- Cross-domain time-horizon comparisons (METR follow-up post; see `metr-2025-time-horizon-vary-across-domains`).

---

### Claim Summary

| ID | Type | Domain | Layer | Actor | Scope | Quantifier | Evidence | Credence | Claim |
|---|---|---|---|---|---|---|---|---:|---|
| META-2025-001 | [F] | META | ASSERTED | OTHER:METR | who=models; what=definition; success=50% | N/A | E4 | 0.90 | METR defines 50% time horizon as the human duration where a model succeeds with 50% probability |
| META-2025-002 | [F] | META | ASSERTED | OTHER:METR | who=METR; what=logistic fit; x=human time; y=success | N/A | E4 | 0.85 | METR estimates time horizons by fitting a logistic success curve vs (log) human time |
| TECH-2025-054 | [F] | TECH | ASSERTED | OTHER:METR | who=frontier agents; what=success vs duration | OTHER:<4 min vs >4 h | E3 | 0.80 | On the suite, short tasks are near-certain and >4h tasks are <10% success for early-2025 frontier models |
| TECH-2025-055 | [F] | TECH | ASSERTED | OTHER:METR | who=frontier models; what=p50 horizon trend; when=2019-2025 | OTHER:~7 months | E3 | 0.75 | METR reports frontier p50 horizon doubled ~every 7 months (2019–2025) with bootstrapped CIs |
| TECH-2025-056 | [F] | TECH | ASSERTED | OTHER:METR | who=frontier models; what=recent-only fit; when=2024-2025 | OTHER:~2.5y shift | E3 | 0.60 | Recent-only fits imply faster progress, shortening month-scale autonomy estimates by ~2.5 years |
| TECH-2025-057 | [P] | TECH | ASSERTED | OTHER:METR | who=future models; what=days/weeks/month autonomy; when=~<10y | OTHER:<10y | E5 | 0.40 | Conditional extrapolation suggests days/weeks tasks within <10 years (month-scale within ~5 years) |
| INST-2025-002 | [F] | INST | PRACTICED | OTHER:METR | who=METR; what=released code+data | N/A | E4 | 0.85 | METR released analysis code and raw run data publicly |

### Claims to Register

```yaml
claims:
  - id: "META-2025-001"
    text: "METR defines a model’s 50% task-completion time horizon as the human task duration at which the model completes tasks with 50% success probability."
    type: "[F]"
    domain: "META"
    evidence_level: "E4"
    credence: 0.90
    operationalization: "Check METR’s paper/blog definitions and confirm the mapping from success probability to a duration derived from the fitted success curve."
    assumptions: []
    falsifiers: ["METR’s formal definition uses a different success threshold-to-duration mapping or different x-axis than human time."]
    source_ids: ["metr-2025-measuring-ai-ability-to-complete-long-tasks"]

  - id: "META-2025-002"
    text: "METR estimates model time horizons by fitting a logistic model of success probability as a function of (log) human task time and reading off the duration at a fixed success probability (e.g., 50%)."
    type: "[F]"
    domain: "META"
    evidence_level: "E4"
    credence: 0.85
    operationalization: "Inspect METR’s released analysis code and paper methods; verify logistic-regression fitting against log2(human_minutes) and horizon extraction at p=0.5."
    assumptions: ["The released code corresponds to the plots/results described in the blog post."]
    falsifiers: ["Released code/paper uses a materially different fitting procedure or horizon definition."]
    source_ids: ["metr-2025-measuring-ai-ability-to-complete-long-tasks"]

  - id: "TECH-2025-054"
    text: "On METR’s time-horizon task suite, human task duration is strongly predictive of model success; for an early-2025 frontier model, tasks under ~4 minutes are near-certain while tasks over ~4 hours succeed under ~10% of the time."
    type: "[F]"
    domain: "TECH"
    evidence_level: "E3"
    credence: 0.80
    operationalization: "Using METR’s released runs data, compute success rates by bins of human_minutes for a frontier model near March 2025 (e.g., Claude 3.7 Sonnet) and test the <4 min and >4 h claims."
    assumptions: ["The selected model is representative of the frontier at the time of the claim."]
    falsifiers: ["Released data show materially higher >4h success or materially lower <4min success for frontier models in that period."]
    source_ids: ["metr-2025-measuring-ai-ability-to-complete-long-tasks"]

  - id: "TECH-2025-055"
    text: "METR reports that the frontier 50%-task-completion time horizon doubled roughly every ~7 months over ~2019–2025, with uncertainty estimated via hierarchical bootstrap across task families, tasks, and attempts."
    type: "[F]"
    domain: "TECH"
    evidence_level: "E3"
    credence: 0.75
    operationalization: "Re-fit a trendline to the frontier envelope of per-model p50 horizons from METR’s released data and compare doubling-time estimates to ~7 months; check that uncertainty is derived via hierarchical bootstrap."
    assumptions: ["Model release dates and horizon estimates are measured consistently across the time series."]
    falsifiers: ["Independent reanalysis of the released data yields a substantially different doubling-time estimate or shows that the reported CI method is inconsistent with hierarchical bootstrap."]
    source_ids: ["metr-2025-measuring-ai-ability-to-complete-long-tasks"]

  - id: "TECH-2025-056"
    text: "METR claims that fitting time-horizon trends using only 2024–2025 measurements implies faster progress, shortening the estimated date for month-long (p50) task autonomy by about 2.5 years compared to fits over a longer history."
    type: "[F]"
    domain: "TECH"
    evidence_level: "E3"
    credence: 0.60
    operationalization: "Reproduce METR’s historical-vs-recent trend fits and compare predicted dates for reaching ~1-month p50 time horizon."
    assumptions: ["The post’s comparison uses comparable model sets and consistent horizon computation."]
    falsifiers: ["Reproduction finds no meaningful shift between recent-only and full-history extrapolations (or opposite direction)."]
    source_ids: ["metr-2025-measuring-ai-ability-to-complete-long-tasks"]

  - id: "TECH-2025-057"
    text: "Conditional on generalization of the benchmark trend to real-world software tasks, extrapolating METR’s time-horizon growth suggests models could autonomously complete many tasks that take humans days or weeks within under a decade (and potentially month-scale tasks within around five years)."
    type: "[P]"
    domain: "TECH"
    evidence_level: "E5"
    credence: 0.40
    operationalization: "Track p50 time-horizon estimates over time and test whether they reach multi-day/week/month durations; separately test external validity by measuring autonomous completion on real-world SWE tasks of known human duration."
    assumptions: ["The observed exponential trend continues and transfers to real-world task distributions."]
    falsifiers: ["Time-horizon growth slows materially, or real-world month-scale SWE projects remain far below the benchmark-implied capability even if benchmark horizons rise."]
    source_ids: ["metr-2025-measuring-ai-ability-to-complete-long-tasks"]

  - id: "INST-2025-002"
    text: "METR released its time-horizon analysis code and raw run data publicly (and invites replication and extension)."
    type: "[F]"
    domain: "INST"
    evidence_level: "E4"
    credence: 0.85
    operationalization: "Verify that the public repository contains runnable analysis code and includes or references the raw run data needed to reproduce key plots."
    assumptions: []
    falsifiers: ["The referenced repos/data are removed, gated, or insufficient to reproduce headline figures."]
    source_ids: ["metr-2025-measuring-ai-ability-to-complete-long-tasks"]
```

---

**Analysis Date**: 2026-02-06
**Analyst**: codex (gpt-5.2)
**Credence in Analysis**: 0.72

**Credence Reasoning**:
- Strong verification that METR’s reported ~7-month doubling is consistent with the linked preprint abstract and is reproducible (approximately) from released raw run data.
- Remaining uncertainty is dominated by external validity, protocol drift, and scaffold/task-distribution confounds.

## Analysis Log

| Pass | Date | Tool | Model | Duration | Tokens | Cost | Notes |
|---:|---|---|---|---:|---:|---:|---|
| 1 | 2026-02-06 | codex-cli | gpt-5.2 | ? | ? | ? | Initial 3-stage analysis with partial independent reproduction using METR’s public code/data |

