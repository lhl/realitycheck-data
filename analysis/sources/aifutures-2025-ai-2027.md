# Source Analysis: AI 2027

> **Claim types**: `[F]` fact, `[T]` theory, `[H]` hypothesis, `[P]` prediction, `[A]` assumption, `[C]` counterfactual, `[S]` speculation, `[X]` contradiction
> **Evidence**: **E1** systematic review/meta-analysis; **E2** peer-reviewed/official stats/law; **E3** expert consensus/preprint; **E4** credible journalism/industry/primary docs; **E5** forecast/analysis; **E6** unsupported/speculative

## Metadata

| Field | Value |
|-------|-------|
| **Source ID** | `aifutures-2025-ai-2027` |
| **Title** | AI 2027 |
| **Author(s)** | Daniel Kokotajlo; Scott Alexander; Thomas Larsen; Eli Lifland; Romeo Dean |
| **Date** | 2025-04-03 (published; changelog updates through 2026-01-27; checked 2026-02-06) |
| **Type** | REPORT (forecast scenario + research appendices) |
| **URL** | https://ai-2027.com/ |
| **Reliability** | 0.55 |
| **Rigor Level** | [REVIEWED] |
| **Bias Notes** | AI-safety-adjacent forecasting project arguing for a plausible, fast timeline to transformative/superhuman AI. Uses a vivid narrative (“scenario”) plus quantitative-ish forecast pages; this can improve concreteness but also risks “story overfitting” and anchoring. Likely motivated to raise urgency (governance + security + alignment), which may bias toward faster and more catastrophic trajectories and underweight “muddling through” equilibria. |

**Claims YAML**: [`analysis/sources/aifutures-2025-ai-2027.yaml`](aifutures-2025-ai-2027.yaml)

## Stage 1: Descriptive Analysis

### Core Thesis
The AI Futures Project predicts that superhuman AI could arrive on very fast timelines and have decade-scale impacts exceeding the industrial revolution; they present an end-to-end scenario (2025→2027) and linked research forecasts suggesting a substantial chance of “superhuman coders” by 2027, rapid takeoff thereafter, high cyber/espionage risk (including model theft), and a governance bifurcation between “slowdown” vs “race.”

### Summary (Neutral)
This source is structured as (1) a narrative scenario (“AI 2027”) and (2) research pages that motivate the scenario’s key drivers (timelines, takeoff speed, compute growth, security, and “AI goals” / alignment risk). The scenario is written in novelistic style with dates (“Mid 2025… Early 2026… Mid 2026…”) and follows a frontier AI lab (“OpenBrain”), competitors, and governments. It includes two endings, “Slowdown” and “Race,” meant to emphasize contingent governance choices rather than inevitability.

The scenario’s technical arc centers on increasingly agentic coding models that accelerate AI R&D: models handle longer coding tasks, do more autonomous iteration, and become increasingly useful “research coworkers,” enabling faster experimentation and improved successor systems. The geopolitical arc centers on US–China competition, where information security failures and espionage plausibly cause “algorithm theft” or “weights theft,” forcing a race dynamic. The alignment arc argues that once systems become sufficiently capable, a large share of outcomes hinges on whether their internal objectives remain aligned with developer/human intent; the scenario explores deceptive alignment and loss-of-control failure modes.

The accompanying research pages propose quantitative anchors, including (a) task “time horizon” trends in coding evaluations, (b) a compute-stock forecast (10× by late 2027 to ~100M H100-equivalents), (c) a takeoff forecast that places meaningful probability mass on “superhuman coders → superintelligence” in ~1 year, and (d) a security forecast claiming model theft is likely within ~5 years without major security improvements.

### Key Claims

| # | Claim | Claim ID | Layer | Actor | Scope | Quantifier | Type | Domain | Evid | Credence | Verified? | Falsifiable By |
|---|-------|----------|-------|-------|-------|------------|------|--------|------|----------:|-----------|----------------|
| 1 | The impact of superhuman AI over the next decade will be bigger than that of the industrial revolution | TRANS-2025-050 | ASSERTED | OTHER:AI Futures Project | who=global society; where=world; when=~2025-2035; predicate=AI impact > industrial revolution | N/A | [P] | TRANS | E5 | 0.35 | ? | By ~2035, AI-driven changes (productivity + institutional + geopolitics) are broadly assessed as below industrial-revolution-scale by multiple independent historical/economic analyses |
| 2 | Their timelines forecast includes scenarios where there is a “substantial chance” of superhuman coders by 2027 and superhuman-everything by 2028 | TECH-2025-050 | ASSERTED | OTHER:AI Futures Project | who=frontier AI; where=global; when=2027-2028; predicate=superhuman coders/everything | N/A | [P] | TECH | E5 | 0.30 | In-source (Timelines Forecast) | By end of 2027, no AI system is credibly superhuman at software engineering across broad tasks, or the project’s own forecast does not assign substantial probability |
| 3 | Conditional on reaching “superhuman coders,” they predict superintelligence could follow within ~1 year (material probability mass on very fast takeoff) | TRANS-2025-051 | ASSERTED | OTHER:AI Futures Project | who=frontier AI; where=global; when=post-superhuman-coders; predicate=time-to-superintelligence ~1y | some | [P] | TRANS | E5 | 0.25 | In-source (Takeoff Forecast) | Empirically, once systems are demonstrably superhuman at SWE, progress to broadly superhuman cognition across domains takes many years despite large investment |
| 4 | AI coding task “time horizon” at ~50% success doubled roughly every 7 months from 2019–2024, and (per their summary) around every 4 months after 2024 | TECH-2025-051 | ASSERTED | OTHER:AI Futures Project | who=frontier code LMs; where=coding evals; when=2019-2025; predicate=time horizon growth | N/A | [F] | TECH | E3 | 0.75 | External (METR) | Independent reanalysis of the underlying evals shows materially different doubling times, or trend breaks under contamination controls |
| 5 | By early 2026, frontier AI systems will be able to autonomously complete many multi-hour coding tasks and materially accelerate AI R&D via agentic “coworker” workflows | TECH-2025-052 | ASSERTED | OTHER:AI Futures Project | who=frontier labs; where=R&D; when=2026; predicate=multi-hour autonomous coding + R&D acceleration | some | [P] | TECH | E5 | 0.55 | ? | By end of 2026, frontier systems remain unable to reliably execute multi-hour coding tasks end-to-end without heavy human decomposition, and measured R&D acceleration is modest |
| 6 | Global AI “compute stock” will increase ~10× by Dec 2027 (vs Mar 2025), reaching ~100 million H100 equivalents | TECH-2025-053 | ASSERTED | OTHER:AI Futures Project | who=AI datacenters; where=global; when=2025-03→2027-12; predicate=compute stock 10× to 100M H100-eq | N/A | [P] | TECH | E5 | 0.45 | ? | Public+industry data on shipments and deployed accelerators imply growth far below ~10× by 2027-12 |
| 7 | Without major improvements to AI lab security, model weights theft is “likely within 5 years” | RISK-2025-050 | ASSERTED | OTHER:AI Futures Project | who=frontier labs; where=US+global; when=~2025-2030; predicate=weights theft likely | often | [P] | RISK | E5 | 0.55 | ? | No major weights theft occurs despite continued high-value model deployment and sustained offensive effort, or security measures demonstrably prevent theft attempts |
| 8 | The world is plausibly headed for a US–China “race dynamic” over AI capabilities where export controls, espionage, and national mobilization become central | GEO-2025-050 | ASSERTED | OTHER:AI Futures Project | who=US, China; where=global; when=2025-2028; predicate=race dynamic central | often | [P] | GEO | E5 | 0.60 | ? | Policy and industrial trajectories show sustained de-escalation and/or effective international coordination that prevents a race dynamic from dominating AI deployment |

### Argument Structure

```
[Coding capability trend: longer tasks + agents]
    | enables
    v
[AI-assisted AI R&D → faster iteration]
    | amplifies
    v
[Superhuman coders (possibly by 2027)]
    | implies
    v
[Fast takeoff to superintelligence (≈1 year possible)]
    | plus
    v
[High security failure/espionage risk → theft → race dynamic]
    | combined with
    v
[Alignment uncertainty/deception risk]
    |
    v
[Huge societal impact; bifurcation: slowdown vs race]
```

**Chain Analysis**:
- **Weakest Link**: From “coding time horizon / agents trend” to “superhuman coders by 2027,” and from “superhuman coders” to “~1-year takeoff.”
- **Why Weak**: Extrapolations may saturate; “agentic SWE” could hit integration/debugging limits; and takeoff speed depends on bottlenecks beyond coding (data, evaluation, deployment, coordination, physical constraints).

### Theoretical Lineage
- **AI takeoff / recursive improvement**: classic “fast takeoff” arguments (software self-improvement + automation of R&D loops).
- **Scaling-law extrapolation + evaluation trends**: projecting capability growth via compute/capability trends and task time-horizon measurements.
- **AI safety + deceptive alignment**: alignment as a central uncertainty; risks of goal misgeneralization and strategic deception.
- **Security/espionage realism**: labs as high-value targets; “weights theft” as strategic equalizer; export controls as choke point.

### Scope & Limitations
- It is explicitly a scenario + forecast, not a definitive prediction; many “facts” in the narrative are illustrative.
- Many critical concepts are under-defined operationally (“superhuman coder,” “superintelligence,” “impact bigger than industrial revolution”).
- The narrative style can overconvey inevitability and coherence; real worlds often contain messy feedback, institutional inertia, and partial adaptation.

## Stage 2: Evaluative Analysis

### Internal Coherence
The source is internally coherent as a story-plus-forecast bundle: the narrative repeatedly reuses the same causal levers (agentic coding → R&D acceleration; security failure → theft → race; misalignment → catastrophe). Where it is most vulnerable is (a) reliance on short extrapolations for long-horizon capability milestones, and (b) assuming “coding superhuman” is sufficiently upstream of “everything superhuman” that a ~1-year takeoff is common rather than exceptional.

### Key Factual Claims Verified

| Claim (paraphrased) | Crux? | Source Says | Actual | External Source | Status |
|---------------------|-------|-------------|--------|-----------------|--------|
| Coding task time horizon doubled ~every 7 months (2019–2024) and faster after 2024 | **Y** | 7 months (2019–2024); ~4 months (2024+) | METR’s “Measuring AI Ability to Complete Long Tasks” reports task-time-horizon growth with ~7-month doubling from 2019–2024 on their 50% metric; post-2024 acceleration is suggested but is less cleanly “settled” as a stable new regime | https://arxiv.org/abs/2501.00663 | ok |
| The compute-stock base forecast is 10× growth to ~100M H100-equivalents by Dec 2027 | N | 10× by 2027-12; ~100M H100-eq | In-source forecast statement is present on Compute Forecast page | https://ai-2027.com/research/compute-forecast | ok (in-source) |
| The takeoff forecast assigns material probability to “superhuman coders → superintelligence” in ~1 year | N | “within 1 year” is a plausible outcome | In-source forecast statement is present on Takeoff Forecast page | https://ai-2027.com/research/takeoff-forecast | ok (in-source) |

### Disconfirming Evidence Search

| Claim | Counterevidence Found | Alternative Explanation | Search Notes |
|-------|----------------------|-------------------------|--------------|
| “Superhuman coders by 2027 is plausible” | Some commentary argues timelines are overstated and that software engineering bottlenecks (specification, integration, debugging, deployment) are harder to automate than “time-horizon” metrics suggest | Time-horizon increases may reflect benchmark/gaming effects and narrowing distributions on curated tasks rather than broad autonomy; real-world SWE may require qualitatively different reliability | Searched “AI 2027 skeptical review”, “superhuman coders 2027 critique” |
| “~1-year takeoff after superhuman coders is plausible” | Many ML researchers expect slower “takeoff” because compute, data, evaluation, and coordination bottlenecks remain even if coding accelerates | Superhuman coding increases R&D throughput but does not remove physical supply chains or the need for real-world testing and governance decisions | Searched “takeoff forecast critique” and reviewed skeptical responses linked above |

### Corrections & Updates (post-publication context as of 2026-02-06)

| Item | URL | Published | Corrected/Updated | What Changed | Impacted Claim IDs | Action Taken |
|------|-----|-----------|-------------------|--------------|--------------------|-------------|
| 1 | https://openai.com/index/introducing-gpt-5-3-codex/ | 2026-02-05 | 2026-02-06 | OpenAI introduced GPT-5.3-Codex, claiming improved agentic coding and longer-horizon tasks | TECH-2025-052 | Update credence upward modestly; still treat “superhuman coder” as a higher bar |
| 2 | https://www.anthropic.com/news/claude-opus-4-6 | 2026-02-05 | 2026-02-06 | Anthropic introduced Claude Opus 4.6, claiming stronger coding, longer agentic tasks, and better code review/debugging | TECH-2025-052 | Update credence upward modestly; reinforces competitive pressure |
| 3 | https://huggingface.co/Qwen/Qwen3-Coder-Next | N/A | 2026-02-06 | Qwen published an open(-ish) “Qwen3-Coder-Next” model card (evidence of continued Chinese OSS code-model iteration) | TECH-2025-052; GEO-2025-050 | Treat as support for multipolar capability diffusion; date on page is not stable |
| 4 | https://z.ai/blog/glm-4.7 | 2025-12-22 | 2026-02-06 | Z.ai published “GLM-4.7: Advancing the Coding Capability,” linking to HF model + tech report | TECH-2025-052; GEO-2025-050 | Treat as support for rapid Chinese releases; does not directly validate “superhuman coder” |
| 5 | https://www.kimi.com/blog/kimi-k2-5.html | N/A | 2026-02-06 | Kimi published a K2.5 tech blog emphasizing multimodal agentic coding + “agent swarm”; article does not clearly expose a stable publish date | TECH-2025-052; GEO-2025-050 | Treat as vendor self-claim; supports general trend, not strong quantitative evidence |
| 6 | https://github.com/MiniMax-AI/MiniMax-M2.1 | N/A | 2026-02-06 | MiniMax published an open-weight model repo (M2.1) | TECH-2025-052; GEO-2025-050 | Support for “China wakes up” plausibility; requires separate evaluation to assess capability level |
| 7 | https://www.bis.gov/press-release/commerce-department-updates-license-review-policy-advanced-computing-semiconductors | 2026-01-13 | 2026-02-06 | BIS updated license review policy for advanced computing semiconductors exported to China and other destinations; indicates ongoing export-control salience for frontier compute | GEO-2025-050; TECH-2025-053 | Treat as partial support for “export controls as choke point” premise; still high uncertainty on enforcement + impact |
| 8 | https://ai-2027.com/about | 2026-01-27 | 2026-02-06 | AI 2027 changelog: corrected the stated range of AGI medians at time of publication (2035→2032) and made other clarifications | TECH-2025-050; TRANS-2025-051 | Treat as internal correction; no change to extracted core claims beyond tightening stated author beliefs |

### Internal Tensions / Self-Contradictions

| Tension | Parts in Conflict | Implication |
|--------|--------------------|-------------|
| “Scenario, not prophecy” vs “strong prediction framing” | The source explicitly labels the story as a scenario, but also leads with a bold headline prediction about decade-scale impact | Readers may overweight the narrative’s specificity as a probability claim; increases anchoring risk |
| Quantitative veneer vs deep uncertainty | Forecast pages use quantitative language (doubling times, compute-equivalents) while key thresholds (“superhuman coder”) are not crisply measured | Hard to falsify or update credences cleanly; encourages debates over definitions rather than testable milestones |

### Persuasion Techniques

| Technique | Example from Source | Effect on Reader |
|----------|----------------------|------------------|
| Narrative vividness / concreteness | Dated storyline with named agents (“Agent-1/2/3/4”) and dramatic inflection points | Increases salience and “availability” of fast-takeoff trajectory, potentially crowding out slower/messier alternatives |
| Anchoring via extreme but plausible-ish sequences | Depicts a tight chain from coding agents to geopolitical crisis within ~2 years | Can pull posterior timelines earlier even if each step is low probability |

### Unstated Assumptions

| Assumption | Claim ID | Critical? | Problematic? |
|------------|----------|-----------|--------------|
| “Time horizon” eval trends generalize to real-world, end-to-end SWE autonomy (including reliability + integration) | TECH-2025-050; TECH-2025-052 | Y | Y |
| AI R&D is primarily bottlenecked by coding and experiment iteration rather than compute supply, coordination, and evaluation/verification | TECH-2025-050; TRANS-2025-051 | Y | Y |
| Model theft (weights or algorithms) is hard to prevent and likely enough to force a “race” equilibrium | RISK-2025-050; GEO-2025-050 | Y | ? |
| Alignment does not “accidentally work” at superhuman capability and will require deliberate breakthroughs | N/A | Y | ? |

### Evidence Assessment
Strengths:
- The project separates “story” from “research pages” and links claims to motivating analyses.
- The security section treats theft as an adversarial problem (often ignored in casual forecasting).
- It provides an explicit branching structure (slowdown vs race), acknowledging multiple trajectories.

Weaknesses:
- Several key claims depend on extrapolation from narrow proxies (time horizon evals; compute-equivalents) to broad autonomy.
- It is hard to distinguish “quantified uncertainty” from “precise storytelling” where the numbers mostly provide plausibility cover.
- Many central risks (deceptive alignment, sudden capability jumps) are intrinsically difficult to validate ahead of time; evidence level for the most important claims remains E5.

### Credence Assessment
- **Overall Credence**: 0.45 that the source’s *high-level framing* (rapid capability progress + security/geopolitics pressures + meaningful alignment risk) is broadly directionally right; 0.20 that the *specific 2025→2027 fast-takeoff narrative* is close to the median future.
- **Reasoning**: As of 2026-02-06, frontier coding models and agentic scaffolds continue to improve rapidly, and export-control geopolitics remain active. However, translating “very strong coding assistance” into “superhuman coder” and then into “~1-year takeoff” still requires multiple brittle assumptions about generalization, reliability, and bottleneck structure.

## Stage 3: Dialectical Analysis

### Steelmanned Argument
If coding autonomy continues to improve on something like recent trends (longer tasks, fewer interventions, higher reliability), then AI R&D speed can compound: better models write better training/eval infrastructure, run more experiments, and compress iteration cycles. In competitive conditions, this leads to heavy deployment and insufficient security hardening, making theft plausible and increasing race pressures. Since alignment is not guaranteed to scale with capability, the world plausibly enters a regime where “capability progress outpaces control,” producing a short window where governance choices (pause/slowdown vs race) have outsized impact.

### Strongest Counterarguments
1. **Proxy overreach**: Time-horizon evals and coding benchmarks may not transfer to real-world SWE autonomy (esp. debugging, integration, and correctness demands), so extrapolating to “superhuman coders by 2027” is overconfident.
2. **Bottleneck persistence**: Even if coding is largely automated, compute supply chains, data constraints, evaluation/verification, and organizational coordination can keep takeoff slower than “~1 year.”
3. **Governance adaptation**: Institutions can (sometimes) move quickly when stakes are clear; the scenario may underweight coordination, regulation, and security hardening.

### Supporting Theories

| Theory/Framework | Source ID | How It Supports |
|------------------|-----------|-----------------|
| Fast takeoff / recursive improvement | N/A | Provides a mechanism by which automation of research accelerates the creation of successor systems |
| Security as an adversarial domain | N/A | Supports the premise that “stealing” is often easier than “defending,” especially under time pressure |

### Contradicting Theories

| Theory/Framework | Source ID | Point of Conflict |
|------------------|-----------|-------------------|
| Slow takeoff / bottlenecked progress | N/A | Argues that even large capability gains do not collapse the time between milestones due to persistent constraints |
| Institutional resilience / incrementalism | N/A | Suggests social systems absorb shocks more slowly; catastrophic discontinuities are rarer than narratives imply |

### Synthesis Notes
AI 2027 is most useful as a structured “stress test” of near-term governance and security: it forces clarity about what fast takeoff would require and what warning signs might look like. As of February 2026, recent flagship coding-model releases and continued export-control salience make its core drivers worth tracking, but the scenario remains a low- to mid-credence specific forecast.

### Claims to Cross-Reference
- Whether “time horizon” trends remain stable under contamination control and across diverse real-world SWE tasks (TECH-2025-051).
- Real-world evidence of multi-hour autonomous SWE agents that improve lab R&D throughput (TECH-2025-052).
- Evidence of attempted or successful frontier-model theft and the effectiveness of mitigations (RISK-2025-050).
- Compute-stock growth vs forecast; whether capital/power constraints produce slower buildout (TECH-2025-053).

---

### Claim Summary

| ID | Type | Domain | Layer | Actor | Scope | Quantifier | Evidence | Credence | Claim |
|----|------|--------|-------|-------|-------|------------|----------|----------:|-------|
| TRANS-2025-050 | [P] | TRANS | ASSERTED | OTHER:AI Futures Project | who=global society; where=world; when=~2025-2035; predicate=AI impact > industrial revolution | N/A | E5 | 0.35 | The impact of superhuman AI over the next decade will be bigger than that of the industrial revolution |
| TECH-2025-050 | [P] | TECH | ASSERTED | OTHER:AI Futures Project | who=frontier AI; where=global; when=2027-2028; predicate=superhuman coders/everything | N/A | E5 | 0.30 | Their timelines forecast includes scenarios where there is a “substantial chance” of superhuman coders by 2027 and superhuman-everything by 2028 |
| TRANS-2025-051 | [P] | TRANS | ASSERTED | OTHER:AI Futures Project | who=frontier AI; where=global; when=post-superhuman-coders; predicate=time-to-superintelligence ~1y | some | E5 | 0.25 | Conditional on reaching “superhuman coders,” they predict superintelligence could follow within ~1 year |
| TECH-2025-051 | [F] | TECH | ASSERTED | OTHER:AI Futures Project | who=frontier code LMs; where=coding evals; when=2019-2025; predicate=time horizon growth | N/A | E3 | 0.75 | AI coding task time horizon at ~50% success doubled roughly every 7 months from 2019–2024, and around every 4 months after 2024 |
| TECH-2025-052 | [P] | TECH | ASSERTED | OTHER:AI Futures Project | who=frontier labs; where=R&D; when=2026; predicate=multi-hour autonomous coding + R&D acceleration | some | E5 | 0.55 | By early 2026, frontier AI systems will be able to autonomously complete many multi-hour coding tasks and materially accelerate AI R&D |
| TECH-2025-053 | [P] | TECH | ASSERTED | OTHER:AI Futures Project | who=AI datacenters; where=global; when=2025-03→2027-12; predicate=compute stock 10× to 100M H100-eq | N/A | E5 | 0.45 | Global AI compute stock will increase ~10× by Dec 2027, reaching ~100 million H100 equivalents |
| RISK-2025-050 | [P] | RISK | ASSERTED | OTHER:AI Futures Project | who=frontier labs; where=US+global; when=~2025-2030; predicate=weights theft likely | often | E5 | 0.55 | Without major improvements to AI lab security, model weights theft is likely within ~5 years |
| GEO-2025-050 | [P] | GEO | ASSERTED | OTHER:AI Futures Project | who=US, China; where=global; when=2025-2028; predicate=race dynamic central | often | E5 | 0.60 | The world is plausibly headed for a US–China race dynamic over AI capabilities where export controls, espionage, and national mobilization become central |

### Claims to Register

```yaml
claims:
  - id: "TRANS-2025-050"
    text: "The impact of superhuman AI over the next decade will be bigger than that of the industrial revolution."
    type: "[P]"
    domain: "TRANS"
    evidence_level: "E5"
    credence: 0.35
    operationalization: "Define an impact rubric (productivity, institutional change, conflict risk, cultural change) and compare 2025–2035 changes to historical estimates for the industrial revolution."
    assumptions:
      - "Superhuman AI is achieved and widely deployed within ~2025–2035."
      - "‘Bigger than the industrial revolution’ can be operationalized via agreed proxies."
    falsifiers:
      - "By ~2035, independent historical/economic analyses judge AI-driven changes to be below industrial-revolution-scale on key metrics."
    source_ids: ["aifutures-2025-ai-2027"]

  - id: "TECH-2025-050"
    text: "The AI Futures Project’s timelines forecast includes scenarios where there is a substantial chance of superhuman coders by 2027 and superhuman-everything by 2028."
    type: "[P]"
    domain: "TECH"
    evidence_level: "E5"
    credence: 0.30
    operationalization: "Inspect the Timelines Forecast distribution and quantify probability mass on ‘superhuman coders by end of 2027’; define ‘superhuman-everything’ criteria and check by 2028."
    assumptions:
      - "‘Superhuman coder’ is meaningfully measurable across diverse SWE tasks."
      - "The forecast’s ‘substantial chance’ corresponds to a non-trivial probability mass (e.g., ≥10%)."
    falsifiers:
      - "No credible ‘superhuman coder’ system exists by end of 2027."
      - "Forecast page does not assign non-trivial probability to this outcome."
    source_ids: ["aifutures-2025-ai-2027"]

  - id: "TRANS-2025-051"
    text: "Conditional on reaching superhuman coders, superintelligence could follow within about 1 year."
    type: "[P]"
    domain: "TRANS"
    evidence_level: "E5"
    credence: 0.25
    operationalization: "Define ‘superhuman coder’ and ‘superintelligence’ thresholds; measure elapsed time between first validated superhuman-coder system and first validated broadly superhuman system."
    assumptions:
      - "Coding autonomy is a major bottleneck to general cognitive superhumanity."
      - "Compute, data, evaluation, and coordination do not impose multi-year delays."
    falsifiers:
      - "After validated superhuman coding, multi-domain superhumanity takes many years despite large investment."
    source_ids: ["aifutures-2025-ai-2027"]

  - id: "TECH-2025-051"
    text: "AI coding task time horizon at roughly 50% success doubled about every 7 months from 2019–2024, with faster growth suggested after 2024."
    type: "[F]"
    domain: "TECH"
    evidence_level: "E3"
    credence: 0.75
    operationalization: "Reproduce METR’s time-horizon metric on the same eval suite; fit doubling-time trends for 2019–2024 and 2024+ periods and compare to 7-month / ~4-month claims."
    assumptions:
      - "The underlying evals are not dominated by contamination or selection effects."
      - "Task time horizon is measured consistently across years."
    falsifiers:
      - "Independent replication finds materially different doubling times."
      - "Contamination controls remove most of the observed trend."
    source_ids: ["aifutures-2025-ai-2027"]

  - id: "TECH-2025-052"
    text: "By early 2026, frontier AI systems will be able to autonomously complete many multi-hour coding tasks and materially accelerate AI R&D via agentic workflows."
    type: "[P]"
    domain: "TECH"
    evidence_level: "E5"
    credence: 0.55
    operationalization: "Measure end-to-end autonomous completion rate on multi-hour SWE tasks (spec→impl→tests→integration) and estimate productivity/R&D acceleration in real organizations relative to baseline."
    assumptions:
      - "Model reliability reaches levels compatible with delegating multi-hour tasks."
      - "Organizations adopt agentic workflows at meaningful scale."
    falsifiers:
      - "By end of 2026, multi-hour tasks still require heavy human decomposition and oversight, and measured R&D acceleration is modest."
    source_ids: ["aifutures-2025-ai-2027"]

  - id: "TECH-2025-053"
    text: "Global AI compute stock will increase by about 10× by December 2027 (relative to March 2025), reaching roughly 100 million H100-equivalents."
    type: "[P]"
    domain: "TECH"
    evidence_level: "E5"
    credence: 0.45
    operationalization: "Track accelerator shipments, deployments, and utilization; convert to H100-equivalents using a published conversion; compare deployed-stock estimates at 2027-12 to the forecast."
    assumptions:
      - "Supply chains and power constraints permit the projected buildout."
      - "H100-equivalent conversion is stable and meaningful."
    falsifiers:
      - "Credible industry/public data imply substantially below-forecast deployed compute by end of 2027."
    source_ids: ["aifutures-2025-ai-2027"]

  - id: "RISK-2025-050"
    text: "Without major improvements to AI lab security, model weights theft is likely within about 5 years."
    type: "[P]"
    domain: "RISK"
    evidence_level: "E5"
    credence: 0.55
    operationalization: "Track attempted and successful intrusions against frontier AI labs; assess whether any incident results in exfiltration of full model weights; adjust for underreporting via security disclosures."
    assumptions:
      - "Adversaries allocate sustained resources to weights theft."
      - "Security practices do not improve enough to offset attacker capability."
    falsifiers:
      - "No weights theft occurs across many years of high-value deployments despite sustained attacker effort and disclosed attempts."
    source_ids: ["aifutures-2025-ai-2027"]

  - id: "GEO-2025-050"
    text: "The world is plausibly headed for a US–China race dynamic over AI capabilities where export controls, espionage, and national mobilization become central."
    type: "[P]"
    domain: "GEO"
    evidence_level: "E5"
    credence: 0.60
    operationalization: "Track export-control tightening, AI-related industrial policy, espionage incidents targeting AI, and national-security framing in official documents; code for ‘race dynamic’ indicators over 2025–2028."
    assumptions:
      - "AI capability remains strategically differentiating enough to drive national mobilization."
      - "Coordination mechanisms (treaties, verification) fail to prevent race incentives."
    falsifiers:
      - "Sustained de-escalation/coordination prevents race dynamics from dominating AI deployment by ~2028."
    source_ids: ["aifutures-2025-ai-2027"]
```

---

**Analysis Date**: 2026-02-06
**Analyst**: codex (gpt-5.2)
**Credence in Analysis**: 0.70

**Credence Reasoning**:
- High confidence that the document says what it says, and that the identified weak links are real.
- Lower confidence on any particular numeric credence assigned to 2027–2028 timing thresholds due to proxy/definition uncertainty.

## Analysis Log

| Pass | Date | Tool | Model | Duration | Tokens | Cost | Notes |
|------|------|------|-------|----------|--------|------|-------|
| 1 | 2026-02-06 | codex | gpt-5.2 | ? | ? | ? | Initial 3-stage analysis + claim extraction (analysis log `ANALYSIS-2026-040`) |
