# Source Analysis: Time Horizon 1.1 (METR)

> **Claim types**: `[F]` fact, `[T]` theory, `[H]` hypothesis, `[P]` prediction, `[A]` assumption, `[C]` counterfactual, `[S]` speculation, `[X]` contradiction
> **Evidence**: **E1** systematic review/meta-analysis; **E2** peer-reviewed/official stats; **E3** expert consensus/preprint/open data; **E4** credible journalism/industry/primary docs; **E5** opinion/forecast; **E6** unsupported/speculative

## Metadata

| Field | Value |
|---|---|
| **Source ID** | `metr-2026-time-horizon-1-1` |
| **Title** | Time Horizon 1.1 |
| **Author(s)** | METR |
| **Date** | 2026-01-29 |
| **Type** | ARTICLE (release announcement / methodology update) |
| **URL** | https://metr.org/blog/2026-1-29-time-horizon-1-1/ |
| **Reliability** | 0.78 |
| **Rigor Level** | [REVIEWED] |
| **Bias Notes** | METR is publishing an update to an in-house capability metric. Strength: this post is unusually specific about task-suite diffs and links to public code/data; we can independently verify many “counts” and some fitted-trend claims. Risks: (a) the measured quantity is sensitive to task distribution and protocol changes (which the post acknowledges), (b) newer-model horizons can saturate a fixed suite, and (c) cross-version comparisons can conflate changes in task suite, agent scaffold, and infra. |

**Claims YAML**: [`analysis/sources/metr-2026-time-horizon-1-1.yaml`](metr-2026-time-horizon-1-1.yaml)

## Stage 1: Descriptive Analysis

### Core Thesis
METR’s updated “Time Horizon 1.1” measurement uses a larger task suite and a new evaluation framework (Inspect) to reduce uncertainty at the frontier and extend measurement headroom; the update broadly preserves the qualitative “fast exponential growth” story while showing meaningful sensitivity to task-suite composition and re-estimating recent growth rates.

### Summary (Neutral)
This post announces TH1.1, described as an update to METR’s time horizon estimates using more tasks and a new evaluation infrastructure. METR reports that many model horizons were re-estimated and generally fall within prior confidence intervals, but the trendline changes somewhat due to older models shifting down and recent models shifting up.

Two major changes are described:
1) **Task suite expansion/curation**: the suite grows from 170 to 228 tasks, adding many HCAST tasks, removing and updating some tasks (including time estimates), and increasing long (8h+) tasks from 14 to 31.
2) **Infrastructure migration**: evaluations move from METR’s internal Vivaria framework to Inspect (UK AI Security Institute’s open-source evaluation framework).

METR argues that more long tasks tighten frontier confidence intervals but notes that many long tasks still rely on estimated (not measured) human times. They present comparisons of doubling-time estimates under TH1 vs TH1.1, including a hybrid fit that keeps earlier TH1-only models and a post-2023 comparison where both methods exist, and claim TH1.1 implies somewhat faster post-2023 and post-2024 growth.

### Key Claims

| # | Claim | Claim ID | Layer | Actor | Scope | Quantifier | Type | Domain | Evid | Credence | Verified? | Falsifiable By |
|---:|---|---|---|---|---|---|---|---|---|---:|---|---|
| 1 | METR released TH1.1 using more tasks and a new eval infrastructure; many model horizons were updated and generally fall within prior TH1 confidence intervals | TECH-2026-921 | ASSERTED | OTHER:METR | who=METR; what=TH1.1 release; where=time-horizon; when=2026-01 | N/A | [F] | TECH | E4 | 0.80 | In-source (intro) | Public data contradict “within CI” summary for many models |
| 2 | Task suite increased from 170→228: +73 tasks (from HCAST), -15 removed, 53 updated; long (8h+) tasks increased 14→31 | TECH-2026-922 | ASSERTED | OTHER:METR | who=task suite; what=counts/changes; when=TH1→TH1.1 | N/A | [F] | TECH | E3 | 0.90 | In-source (change list) | Task/run data show different unique-task counts or long-task counts |
| 3 | METR migrated evaluation infrastructure from Vivaria to Inspect (UK AI Security Institute’s open-source eval framework) | TECH-2026-923 | PRACTICED | OTHER:METR | who=METR; what=infra migration; from=Vivaria; to=Inspect | N/A | [F] | TECH | E4 | 0.85 | In-source (change list) | METR releases show they did not adopt Inspect for TH1.1 |
| 4 | METR re-estimated horizons for 14 models (vs 33 prior) due to availability/scaffold/“not frontier” reasons | TECH-2026-924 | ASSERTED | OTHER:METR | who=models; what=re-estimated subset; why=constraints | N/A | [F] | TECH | E3 | 0.85 | In-source (model coverage) | Released TH1.1 run data show a substantially different model set/size |
| 5 | More tasks (especially long ones) yields tighter confidence intervals; example: Opus 4.5’s CI upper-bound/point-estimate ratio drops from ~4.4× to ~2.3× | TECH-2026-925 | ASSERTED | OTHER:METR | who=Opus 4.5; what=CI tightening; where=TH1 vs TH1.1 | OTHER:~4.4→2.3× | [F] | TECH | E3 | 0.60 | In-source (CI example) | Bootstrap replication does not show this CI tightening |
| 6 | METR measured human baseline times for only 5 of 31 long (8h+) tasks; the rest use estimated times | TECH-2026-926 | ASSERTED | OTHER:METR | who=long tasks; what=measured vs estimated; where=TH1.1 | OTHER:5/31 | [F] | TECH | E4 | 0.70 | In-source (note) | Task metadata show substantially more measured long-task times |
| 7 | A “hybrid” trend (TH1 for early missing models + TH1.1 for later) yields the same doubling time as TH1: 196 days (~7 months) | TECH-2026-927 | ASSERTED | OTHER:METR | who=frontier trend; what=hybrid doubling time; when=2019–2025 | OTHER:196 days | [F] | TECH | E3 | 0.70 | In-source (trend comparison) | Refit using released horizons yields materially different doubling time |
| 8 | Post-2023 doubling time is ~131 days under TH1.1 vs ~165 days under TH1; since 2024, ~89 days under TH1.1 vs ~109 under TH1 | TECH-2026-928 | ASSERTED | OTHER:METR | who=frontier trend; what=post-window doubling times; when=2023+ / 2024+ | OTHER:131/165/89/109 | [F] | TECH | E3 | 0.65 | In-source (trend comparison) | Refit yields substantially different post-window doubling estimates |
| 9 | Trend changes because older-model horizons shift down and newer-model horizons shift up (e.g., GPT-4 versions down ~35–57%, GPT-5 up ~55%, Opus 4.5 up ~11%) | TECH-2026-929 | ASSERTED | OTHER:METR | who=models; what=relative shifts; where=TH1→TH1.1 | OTHER:percent shifts | [F] | TECH | E3 | 0.70 | In-source (trend explanation) | Recomputed shifts show opposite direction or much smaller magnitude |
| 10 | Time-horizon trend is sensitive to task composition; updating suites without rigid selection criteria can change the underlying quantity being estimated | META-2026-039 | ASSERTED | OTHER:METR | who=metric; what=sensitivity to task distribution; why=protocol drift | N/A | [T] | META | E4 | 0.75 | In-source (discussion) | Demonstrated invariance of trend to suite updates under broad conditions |
| 11 | TH1.1 has relatively few tasks that the strongest models cannot do successfully; METR is prioritizing raising the “ceiling” by updating evals and adding more long tasks | TECH-2026-930 | ASSERTED | OTHER:METR | who=eval suite; what=saturation/ceiling; action=raise ceiling | N/A | [H] | TECH | E4 | 0.70 | In-source (future work) | New task additions show no such saturation pressure |

### Argument Structure

```
(1) Time horizon is useful, but frontier uncertainty + saturation are increasing concerns
        ↓
(2) Improve task suite (more + longer tasks) and migrate infra (Vivaria → Inspect)
        ↓
(3) Re-estimate horizons for a subset of models under TH1.1
        ↓
(4) Result: many estimates within old CIs, but trendlines change somewhat
        ↓
(5) Therefore: treat trend as real-but-sensitive; keep updating suite to measure strong models
```

**Weakest links**:
- Whether suite updates preserve comparability over time (task distribution drift).
- Whether post-2024 slope estimates are stable vs sensitive to small model-set changes.

### Theoretical Lineage
- **Benchmark maintenance**: “raising the ceiling” and avoiding saturation is a common issue in fast-moving capability evaluation.
- **Open evaluation frameworks**: migration to a shared eval framework (Inspect) aligns with standardization/interoperability goals.

### Scope & Limitations
- TH1.1 covers fewer models than TH1; earlier-model trend comparisons are partly hybridized.
- Long-task human time estimates are often estimated rather than measured, affecting absolute horizons.
- Reported post-2024 doubling times depend on small samples and may be unstable.

## Stage 2: Evaluative Analysis

### Internal Coherence
The post is unusually explicit that (a) the metric is sensitive to task composition and (b) it is difficult to keep measuring fast-improving models without saturation. The change narrative (more tasks + Inspect migration) coheres with that motivation. The main evidential question is whether the reported “trendline shifts” and “doubling time” deltas are reproducible from the released artifacts.

### Key Factual Claims Verified

| Claim (paraphrased) | Crux? | Source Says | Actual | External Source | Status |
|---|---:|---|---|---|---|
| Task suite increased 170→228 and long (8h+) tasks increased 14→31 | **Y** | 228 tasks; 31 long | Verified directly from METR’s released TH1.0 vs TH1.1 raw runs: unique `task_id` count is 170 vs 228; tasks with `human_minutes ≥ 480` are 14 vs 31. | https://github.com/METR/eval-analysis-public (commit `8d68adb…`) | ok |
| TH1.1 re-estimated 14 models (vs 33 prior) | N | 14 models; 33 prior | TH1.0 raw runs contain 33 model aliases (plus `human`), and TH1.1 contains 14 model aliases (plus `human`). | https://github.com/METR/eval-analysis-public (commit `8d68adb…`) | ok |
| Post-2023 doubling time under TH1.1 is ~131 days | **Y** | 131 days | A simple reproduction from TH1.1 raw runs (logistic fit of success vs log2(human_minutes) per model, frontier-envelope trend fit) yields ~132 days doubling (R²≈0.90). | https://github.com/METR/eval-analysis-public (commit `8d68adb…`) | ok (direction + magnitude) |
| Older models shift down; newer shift up (e.g., GPT-5 up; Opus 4.5 up) | **Y** | down for older GPT-4; up for GPT-5/Opus 4.5 | Comparing p50 horizons from TH1.0 vs TH1.1 (Inspect-stripped mapping) shows older models down ~35–49% (e.g., GPT‑4 0314 −35%, GPT‑4 1106 −49%), and newer models up (e.g., GPT‑5 +62%, Opus 4.5 +11%). | https://github.com/METR/eval-analysis-public (commit `8d68adb…`) | ok (close to quoted magnitudes) |
| Inspect is created by UK AI Security Institute and is an open-source eval framework | N | Inspect by UK AISI | Inspect docs state it is “created by the UK AI Security Institute” and cite the open-source GitHub project. | https://inspect.aisi.org.uk/ | ok |

### Disconfirming Evidence Search

| Claim | Counterevidence Found | Alternative Explanation | Search Notes |
|---|---|---|---|
| “TH1.1 is within prior CIs” as a general statement | Many point estimates shift substantially (older down, newer up) even if within wide CIs | The statement can be true while still meaning “CI widths were very large” | Checked direction/magnitude of shifts from released runs-derived p50 fits |
| Post-2024 doubling time ~89 days | Simple reproduction gave ~100 days (cut window + method differences) | Different cutoff date, weighting, bootstrap sampling, or frontier selection can shift estimates | Ran simple reproduction and noted sensitivity; did not fully replicate METR’s bootstrap procedure |
| Infrastructure change is “small share” of horizon changes | Not fully tested here | Most change may indeed come from task suite changes rather than Inspect migration | Would require matched runs on same suite under both infra, which is beyond this pass |

### Corrections & Updates

| Item | URL | Published | Corrected/Updated | What Changed | Impacted Claim IDs | Action Taken |
|---|---|---:|---:|---|---|---|
| N/A | N/A | N/A | N/A | No corrections observed during capture | N/A | None |

### Internal Tensions / Self-Contradictions

| Tension | Parts in Conflict | Implication |
|---|---|---|
| “Trend preserved” vs large sensitivity | Claims overall story holds, yet suite updates change point estimates non-trivially | Reinforces that the trend is not a fixed “law of nature” but a measurement over a chosen task distribution |

### Persuasion Techniques

| Technique | Example from Source | Effect on Reader |
|---|---|---|
| “Within confidence intervals” framing | Highlights continuity | Can downplay that CIs may be so wide that “within” is not very informative |
| Quantitative deltas | Percent-shift examples, doubling-time comparisons | Improves transparency but can over-precision small-sample slope estimates |

### Unstated Assumptions

| Assumption | Claim ID | Critical? | Problematic? |
|---|---|---:|---:|
| The updated suite better reflects “important” tasks than the prior suite | TECH-2026-922 | Y | ? |
| Estimated long-task human times are accurate enough not to distort trend slope | TECH-2026-926 | Y | Y |
| Frontier-envelope fitting is a stable object across suite updates | TECH-2026-927, TECH-2026-928 | Y | ? |

### Evidence Assessment
This post is unusually verifiable for a capabilities-trend claim: public raw run data enable checking task counts, long-task counts, model coverage, approximate doubling times, and direction/magnitude of horizon shifts. The least verifiable pieces without further computation are bootstrap-derived CI tightening claims and the decomposition of change into “suite vs infrastructure” contributions.

### Credence Assessment
- **Overall Credence**: 0.76
- **Reasoning**: Many key quantitative statements can be independently checked against released run data (and match). Residual uncertainty is concentrated in post-2024 doubling-time precision and in causal attribution of why shifts occurred.

## Stage 3: Dialectical Analysis

### Steelmanned Argument
If time horizon is to serve as a forecasting anchor, it must remain measurable at the frontier. That requires continually refreshing the task suite (more long tasks, fewer reward-hackable tasks) and using robust, open evaluation infrastructure. TH1.1 is a maintenance update that preserves the core exponential-growth signal while increasing measurement resolution, and it correctly highlights that “the trend” is a property of a task distribution that must be specified and defended.

### Strongest Counterarguments
1. **Moving target**: Updating suites without rigid selection criteria makes “time horizon” a shifting construct; trend comparisons become partly subjective.
2. **Human-time estimation error**: Using estimated times for most 8h+ tasks could distort both absolute horizons and slope.
3. **Small-sample slope sensitivity**: Post-2024 doubling times may be dominated by a handful of models and protocol decisions.

### Supporting Theories

| Theory/Framework | Source ID | How It Supports |
|---|---|---|
| Benchmark ceiling maintenance | N/A | Keeping tasks ahead of model capability avoids saturation and preserves measurement sensitivity |

### Contradicting Theories

| Theory/Framework | Source ID | Point of Conflict |
|---|---|---|
| “Metric invariance” skepticism | N/A | If the measured quantity changes with suite updates, it may not support long-run extrapolation |

### Synthesis Notes
TH1.1 is important primarily as a **methodology update**: it makes clearer that time-horizon trendlines are conditional on task distribution choices and that frontier measurement is an ongoing “eval engineering” project. For AI-2027-style forecasting, this both strengthens the empirical anchor (open data + fast growth) and strengthens caution (protocol sensitivity + saturation).

### Claims to Cross-Reference
- `TECH-2025-051` (AI 2027’s citation of METR time-horizon doubling) and `TECH-2025-055` (METR blog trend claim).
- Cross-domain bottleneck comparisons (`TECH-2025-060`).

---

### Claim Summary

| ID | Type | Domain | Layer | Actor | Scope | Quantifier | Evidence | Credence | Claim |
|---|---|---|---|---|---|---|---|---:|---|
| TECH-2026-921 | [F] | TECH | ASSERTED | OTHER:METR | who=METR; what=TH1.1 release + “within CI” summary | N/A | E4 | 0.80 | METR released TH1.1 with more tasks and new infra; many horizons updated and generally within prior CIs |
| TECH-2026-922 | [F] | TECH | ASSERTED | OTHER:METR | who=suite; what=170→228 and long 14→31 plus add/remove/update counts | N/A | E3 | 0.90 | Task suite expanded and changed (including long-task count increase) |
| TECH-2026-923 | [F] | TECH | PRACTICED | OTHER:METR | who=METR; what=Vivaria→Inspect | N/A | E4 | 0.85 | METR migrated evaluation infrastructure from Vivaria to Inspect |
| TECH-2026-924 | [F] | TECH | ASSERTED | OTHER:METR | who=models; what=14 re-estimated vs 33 prior | N/A | E3 | 0.85 | TH1.1 re-estimated horizons for 14 models (subset of TH1’s 33) |
| TECH-2026-925 | [F] | TECH | ASSERTED | OTHER:METR | who=Opus 4.5; what=CI tightening example | OTHER:~4.4→2.3× | E3 | 0.60 | More tasks tighten CIs; example Opus 4.5 upper-bound ratio drops ~4.4×→~2.3× |
| TECH-2026-926 | [F] | TECH | ASSERTED | OTHER:METR | who=long tasks; what=measured vs estimated times | OTHER:5/31 | E4 | 0.70 | Only 5/31 long tasks have measured human times; rest estimated |
| TECH-2026-927 | [F] | TECH | ASSERTED | OTHER:METR | who=trend; what=hybrid doubling=196 days | OTHER:196 days | E3 | 0.70 | Hybrid trend yields 196-day doubling (same as TH1) |
| TECH-2026-928 | [F] | TECH | ASSERTED | OTHER:METR | who=trend; what=post-window doubling times | OTHER:131/165/89/109 | E3 | 0.65 | Post-2023 and post-2024 doubling times differ between TH1 and TH1.1 |
| TECH-2026-929 | [F] | TECH | ASSERTED | OTHER:METR | who=models; what=direction/magnitude of shifts | OTHER:% shifts | E3 | 0.70 | Older-model horizons shift down while newer models shift up (examples given) |
| META-2026-039 | [T] | META | ASSERTED | OTHER:METR | who=metric; what=task-distribution sensitivity | N/A | E4 | 0.75 | Time-horizon trends are sensitive to task composition; must define target task distribution |
| TECH-2026-930 | [H] | TECH | ASSERTED | OTHER:METR | who=suite; what=saturation pressure + ceiling-raising plans | N/A | E4 | 0.70 | TH1.1 is close to saturation for strongest models; METR prioritizes raising the ceiling with more long tasks |

### Claims to Register

```yaml
claims:
  - id: "TECH-2026-921"
    text: "METR released a new version of its time horizon estimates (TH1.1) using more tasks and a new evaluation infrastructure, and reports that re-estimated time horizons generally fall within the confidence intervals from TH1."
    type: "[F]"
    domain: "TECH"
    evidence_level: "E4"
    credence: 0.80
    operationalization: "Compare TH1 vs TH1.1 point estimates and confidence intervals for overlapping models using released data and check the fraction of TH1.1 estimates within prior TH1 CIs."
    assumptions: ["Confidence intervals are comparable across versions and computed consistently."]
    falsifiers: ["Many overlapping models’ TH1.1 point estimates fall outside TH1 confidence intervals under the released artifacts."]
    source_ids: ["metr-2026-time-horizon-1-1"]

  - id: "TECH-2026-922"
    text: "METR increased its time-horizon task suite from 170 to 228 tasks by adding 73 HCAST tasks, removing 15 tasks, and updating 53 tasks; the count of long tasks (estimated 8+ hours for humans) increased from 14 to 31."
    type: "[F]"
    domain: "TECH"
    evidence_level: "E3"
    credence: 0.90
    operationalization: "Count unique tasks and long-task thresholds in METR’s released TH1 and TH1.1 run data/task metadata; verify add/remove/update counts from repo diffs."
    assumptions: ["`human_minutes` reflects the intended human-time estimate per task and is stable per task_id."]
    falsifiers: ["Released TH1/TH1.1 artifacts show materially different unique-task or long-task counts than claimed."]
    source_ids: ["metr-2026-time-horizon-1-1"]

  - id: "TECH-2026-923"
    text: "METR moved its time-horizon evaluation infrastructure from its in-house Vivaria framework to Inspect, an open-source evaluation framework created by the UK AI Security Institute."
    type: "[F]"
    domain: "TECH"
    evidence_level: "E4"
    credence: 0.85
    operationalization: "Verify that TH1.1 runs use Inspect-based scaffolding and that Inspect is a UK AI Security Institute project (docs/repo)."
    assumptions: []
    falsifiers: ["TH1.1 runs do not use Inspect or Inspect is not attributable to UK AISI."]
    source_ids: ["metr-2026-time-horizon-1-1"]

  - id: "TECH-2026-924"
    text: "METR re-estimated time horizons for 14 models under TH1.1 (compared to 33 models under TH1), citing model availability, scaffold/tooling changes, and non-frontier status as reasons for omissions."
    type: "[F]"
    domain: "TECH"
    evidence_level: "E3"
    credence: 0.85
    operationalization: "Count unique non-human model aliases in TH1 and TH1.1 released run data and check documented reasons for missing models."
    assumptions: []
    falsifiers: ["Released TH1.1 run data contain a substantially different number of models or include most pre-2023 models claimed missing."]
    source_ids: ["metr-2026-time-horizon-1-1"]

  - id: "TECH-2026-925"
    text: "METR claims that expanding the task suite (especially adding more 8h+ tasks) yields tighter confidence intervals on frontier model horizons; it gives an example where Opus 4.5’s CI upper-bound/point-estimate ratio decreases from ~4.4× (TH1) to ~2.3× (TH1.1)."
    type: "[F]"
    domain: "TECH"
    evidence_level: "E3"
    credence: 0.60
    operationalization: "Re-run METR’s hierarchical bootstrap CI procedure on TH1 and TH1.1 and compare CI widths for the same model; reproduce the Opus 4.5 ratio example."
    assumptions: ["Bootstrap procedures and model/task weighting are comparable across TH1 and TH1.1."]
    falsifiers: ["Reproductions show similar or wider CIs under TH1.1, or the quoted ratios do not match computed values."]
    source_ids: ["metr-2026-time-horizon-1-1"]

  - id: "TECH-2026-926"
    text: "METR measured human baseline times for only 5 of its 31 long (8h+) tasks in TH1.1; the remainder of long-task times are estimates."
    type: "[F]"
    domain: "TECH"
    evidence_level: "E4"
    credence: 0.70
    operationalization: "Inspect task metadata and determine which long tasks have measured vs estimated human times."
    assumptions: []
    falsifiers: ["Task metadata show substantially more than 5 measured long-task times."]
    source_ids: ["metr-2026-time-horizon-1-1"]

  - id: "TECH-2026-927"
    text: "METR reports that a hybrid trendline (using TH1 estimates for early models missing from TH1.1 and TH1.1 estimates for later models) yields the same frontier time-horizon doubling time as TH1: 196 days (~7 months)."
    type: "[F]"
    domain: "TECH"
    evidence_level: "E3"
    credence: 0.70
    operationalization: "Fit log-linear trendlines to the frontier envelope using the specified hybrid model set and compute doubling time in days."
    assumptions: ["Hybridization does not introduce discontinuities that invalidate trend fitting."]
    falsifiers: ["Refit doubling time differs materially from ~196 days under the specified hybrid dataset."]
    source_ids: ["metr-2026-time-horizon-1-1"]

  - id: "TECH-2026-928"
    text: "METR reports post-2023 doubling time is ~131 days under TH1.1 vs ~165 days under TH1; and since 2024, ~89 days under TH1.1 vs ~109 days under TH1."
    type: "[F]"
    domain: "TECH"
    evidence_level: "E3"
    credence: 0.65
    operationalization: "Using consistent cutoff dates and frontier selection rules, recompute post-window trend slopes for TH1 and TH1.1 and compare doubling-time estimates."
    assumptions: ["Cutoff dates and frontier selection are implemented consistently with METR’s intent."]
    falsifiers: ["Recomputed post-window doubling times differ substantially from the stated values under reasonable reproductions."]
    source_ids: ["metr-2026-time-horizon-1-1"]

  - id: "TECH-2026-929"
    text: "METR attributes the TH1→TH1.1 trend change to older models’ horizons shifting down and recent models’ horizons shifting up (e.g., some GPT-4 versions down ~35–57%, GPT-5 up ~55%, Opus 4.5 up ~11%)."
    type: "[F]"
    domain: "TECH"
    evidence_level: "E3"
    credence: 0.70
    operationalization: "Compute per-model p50 horizons under TH1 and TH1.1 for overlapping model snapshots and calculate percent changes."
    assumptions: ["The compared model snapshots are meaningfully equivalent across infrastructures (or differences are documented)."]
    falsifiers: ["Recomputed percent changes are opposite in direction or far from the stated magnitudes."]
    source_ids: ["metr-2026-time-horizon-1-1"]

  - id: "META-2026-039"
    text: "METR argues the time-horizon trendline is sensitive to task-suite composition; updating the suite without rigid selection criteria changes the underlying quantity being estimated and highlights the need to define the target task distribution."
    type: "[T]"
    domain: "META"
    evidence_level: "E4"
    credence: 0.75
    operationalization: "Quantify sensitivity of estimated doubling time to task subsampling and suite updates; assess whether a principled suite definition stabilizes the trend."
    assumptions: []
    falsifiers: ["Demonstrations show estimated doubling time is largely invariant to broad task-suite changes under realistic update processes."]
    source_ids: ["metr-2026-time-horizon-1-1"]

  - id: "TECH-2026-930"
    text: "METR reports the TH1.1 suite is close to saturation for the strongest models and that it is prioritizing updates (including more long tasks) to raise the measurement ceiling."
    type: "[H]"
    domain: "TECH"
    evidence_level: "E4"
    credence: 0.70
    operationalization: "Measure the fraction of TH1.1 tasks that frontier models solve successfully and track whether additional long/harder tasks restore discrimination between models."
    assumptions: ["Saturation is primarily driven by task difficulty ceilings rather than scoring artifacts."]
    falsifiers: ["Additional tasks do not meaningfully reduce saturation or improve discrimination at the frontier."]
    source_ids: ["metr-2026-time-horizon-1-1"]
```

---

**Analysis Date**: 2026-02-06
**Analyst**: codex (gpt-5.2)
**Credence in Analysis**: 0.76

**Credence Reasoning**:
- Core quantitative “counts” and the post-2023 doubling-time claim are directly reproducible (approximately) from METR’s released run data.
- Precision claims about post-2024 doubling and CI-width improvements remain more method-sensitive without a full bootstrap replication.

## Analysis Log

| Pass | Date | Tool | Model | Duration | Tokens | Cost | Notes |
|---:|---|---|---|---:|---:|---:|---|
| 1 | 2026-02-06 | codex-cli | gpt-5.2 | ? | ? | ? | Initial 3-stage analysis with multiple independent spot-checks against released TH1.0/TH1.1 run data and Inspect docs |

