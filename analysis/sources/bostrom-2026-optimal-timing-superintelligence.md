# Source Analysis: Optimal Timing for Superintelligence (Bostrom, 2026)

> **Claim types**: `[F]` fact, `[T]` theory, `[H]` hypothesis, `[P]` prediction, `[A]` assumption, `[C]` counterfactual, `[S]` speculation, `[X]` contradiction
> **Evidence**: **E1** systematic review/meta-analysis; **E2** peer-reviewed/official stats; **E3** expert consensus/preprint; **E4** credible journalism/industry/primary docs; **E5** opinion/forecast/models; **E6** unsupported/speculative

## Metadata

| Field | Value |
|---|---|
| **Source ID** | `bostrom-2026-optimal-timing-superintelligence` |
| **Title** | Optimal Timing for Superintelligence: Mundane Considerations for Existing People |
| **Author(s)** | Nick Bostrom |
| **Date** | 2026 (working paper v1.0; PDF metadata created 2026-01-20) |
| **Type** | PAPER (working paper) |
| **URL** | https://nickbostrom.com/optimal.pdf |
| **Reliability** | 0.60 |
| **Rigor Level** | `[REVIEWED]` |
| **Bias Notes** | Person-affecting framing (explicitly deprioritizes “impersonal” future-generations welfare), and heavy reliance on stylized models with poorly identified parameters (P(doom), rate/shape of safety progress, feasibility/risks of pauses). The paper’s qualitative conclusions are plausible under its assumptions, but policy implications are highly sensitive to omitted governance/game-theoretic dynamics and to how quickly/credibly “superintelligence” would translate into real-world mortality reduction. |

**Claims YAML**: [`analysis/sources/bostrom-2026-optimal-timing-superintelligence.yaml`](bostrom-2026-optimal-timing-superintelligence.yaml)

## Stage 1: Descriptive Analysis

### Core Thesis
From a person-affecting perspective focused on currently existing people (and restricting attention to “mundane” considerations), Bostrom argues that AI-timeline policy should trade off catastrophic AI risk against the ongoing harms of the status quo, especially near-certain death from aging/disease. In stylized models that include safety progress, temporal discounting, quality-of-life improvements, diminishing marginal utility, and post-capability “safety windfalls,” optimal delays are often modest; a common pattern is to reach AGI capability quickly, then consider a short, carefully implemented pause prior to full deployment (“swift to harbor, slow to berth”).

### Summary (Neutral)
The paper begins by reframing “pause vs proceed” as a comparison between two risky trajectories: (1) continued high baseline mortality and other background risks without superintelligence, versus (2) a transition that could bring radical mortality reduction and quality-of-life improvement but also introduces catastrophic AI failure risk.

It then develops a sequence of increasingly elaborate models:
- A **go/no-go model** where launching now is compared to never launching, producing a high implied “risk tolerance” for AI catastrophe probability under assumptions of large life-extension upside.
- A **timing model** where waiting can reduce risk via safety progress but costs lives and delays benefits.
- Extensions adding **temporal discounting**, **quality-of-life uplift**, and **diminishing marginal utility/risk aversion** in QALYs.
- A **multiphase model** that separates time-to-capability (Phase 1) from an optional post-capability pause (Phase 2), motivated by a post-capability “safety windfall” (faster safety progress once the artifact exists) with diminishing returns.
- A **safety testing** variation treating risk as uncertain and tests as information that enables an evidence-conditional policy (launch when tests pass, delay when they fail).
- **Distributional/prioritarian** discussion: different demographics (old/sick vs young/secure) have different prudential preferences; prioritarian weighting tends to shorten “socially optimal” timelines under the person-affecting frame.

Finally, the paper emphasizes “theory of second best”: even if an abstractly optimal pause exists, real-world implementation risks (e.g., selection effects, militarization, overhangs, governance drift) can make actual pause policies net harmful.

### Key Claims

| # | Claim | Claim ID | Layer | Actor | Scope | Quantifier | Type | Domain | Evid | Credence | Verified? | Falsifiable By |
|---:|---|---|---|---|---|---|---|---|---|---:|---|---|
| 1 | Under a simple go/no-go model with large mortality-reduction upside, launching superintelligence can increase expected remaining lifespan for existing people even if extinction risk at launch is very high (e.g., cutoff ~97% under one set of assumptions) | RISK-2026-928 | ASSERTED | OTHER:Bostrom | who=existing people; model=go/no-go; outcome=expected remaining lifespan; risk=P(extinction at launch) | can | [T] | RISK | E5 | 0.85 | In-source (Sec. “A simple go/no-go model”) | Replication of the model shows the cutoff is materially different under the stated assumptions |
| 2 | In a timing model with safety progress, optimal delays are usually modest; very long waits appear only when initial risk is extremely high and safety progress lies in an intermediate range (both very fast and very slow progress favor earlier launch) | TRANS-2026-021 | ASSERTED | OTHER:Bostrom | who=decision-maker; model=safety progress vs mortality; output=optimal delay | often | [T] | TRANS | E5 | 0.65 | In-source (Sec. “Incorporating time and safety progress”) | Alternative model structures (e.g., non-monotone risk, governance/game theory) robustly yield long optimal delays across broad parameter ranges |
| 3 | Temporal discounting typically pushes toward later launch when pre/post-AGI quality is similar, but can push toward earlier launch when post-AGI quality is sufficiently higher (discounting penalizes delaying the “higher-quality era”) | TRANS-2026-022 | ASSERTED | OTHER:Bostrom | who=decision-maker; model=discounting + QoL differential | sometimes | [T] | TRANS | E5 | 0.60 | In-source (Secs. “Temporal discounting”; “Quality of life adjustment”) | Reproduction shows the sign flip does not occur under reasonable discount/QoL parameters |
| 4 | In a multiphase model with a post-capability “safety windfall,” an optimal policy often includes a short but non-zero deliberate pause after AGI capability is reached (months to a small number of years) | TRANS-2026-024 | ASSERTED | OTHER:Bostrom | who=decision-maker; model=Phase1+Phase2; intervention=post-capability pause | often | [H] | TRANS | E5 | 0.55 | In-source (Secs. “Changing rates of safety progress”; “Conclusions”) | Evidence that post-capability safety progress is not front-loaded (or that pausing increases risk via overhang/competition) |
| 5 | With uncertain intrinsic system risk and informative tests, the relevant decision object is an evidence-conditional policy; safety testing increases expected utility versus no testing | RISK-2026-932 | ASSERTED | OTHER:Bostrom | who=decision-maker; model=POMDP; intervention=testing; outcome=expected utility | generally | [T] | RISK | E5 | 0.65 | In-source (Sec. “Safety testing”) | Demonstration that testing (with realistic test properties) does not improve expected outcomes or is dominated by fixed-delay rules |
| 6 | The paper’s abstract recommendation (“swift to harbor, slow to berth”) does not directly imply a specific pause policy because real-world attempts to slow AI can backfire via second-best effects | RISK-2026-933 | ASSERTED | OTHER:Bostrom | who=policymakers; where=global; what=pause policies; risk=implementation failure modes | often | [H] | RISK | E5 | 0.55 | In-source (Sec. “Theory of second best”; “Conclusions”) | Historical or modeled evidence that pauses reliably reduce catastrophic risk without major offsetting harms |
| 7 | Global life expectancy at birth is ~73 years and the world median age is ~30, motivating a simplified “~40 years remaining life expectancy” baseline for existing people | SOC-2026-022 | ASSERTED | OTHER:Bostrom | who=global population; when=~2024; metrics=life expectancy, median age | ~ | [F] | SOC | E2 | 0.85 | External (UN/OWID) | Official stats show materially different global life expectancy/median age for the referenced period |
| 8 | Annual mortality risk for (healthy) 20–25-year-olds in developed countries is on the order of ~0.05–0.08%/year; treating that as constant implies expected lifespan ~1/0.0007 ≈ 1,400 years | SOC-2026-023 | ASSERTED | OTHER:Bostrom | who=healthy 20–25; where=developed countries; metric=annual mortality hazard | ~ | [F] | SOC | E2 | 0.70 | External (CDC life tables for US females) | Age-specific death probabilities in developed-country life tables are far from this range, or the “constant hazard ⇒ 1,400y” approximation is shown to be misapplied |

### Argument Structure

```
(1) Status quo for existing people includes large, ongoing mortality + background catastrophic risks
        ↓
(2) Aligned superintelligence could sharply reduce mortality + improve quality of life
        ↓
(3) But deploying it introduces catastrophic AI risk that may decline with safety progress/testing
        ↓
(4) Waiting trades off: fewer AI risks later vs more deaths/discounted value meanwhile
        ↓
(5) Under many plausible parameterizations, optimal delays are modest; post-capability “windfall” motivates short targeted pauses and evidence-based deployment policies
        ↓
(6) Real-world policy must account for “second-best” implementation risks; abstract optimum ≠ best feasible policy
```

**Weakest links**:
- The magnitude and timing of “post-AGI mortality reduction” (life-extension feasibility and speed).
- The shape and controllability of safety progress (and whether a “windfall” is real).
- Whether a meaningful “pause” can be implemented without offsetting selection effects, militarization, or overhang dynamics.

### Theoretical Lineage
- **Ethics**: person-affecting views vs impersonal/total-utilitarian views; prioritarian social welfare functions (Parfit tradition).
- **Growth and longevity**: “value of life years” work (Hall & Jones); diminishing marginal utility and health economics.
- **Existential risk + growth**: “time of perils” and “safety as a luxury good” traditions; timing models trading background vs transition risk (Binder-style framing).
- **AI governance discourse**: moratoria/pause proposals vs “race to build” critiques; international coordination and selection effects.

### Scope & Limitations
- Explicitly **person-affecting** and **mundane** (sets aside impersonal longtermism, simulation hypotheses, and other “arcane” considerations).
- Stylized “launch” framing abstracts from incremental deployment and heterogeneous actors; “knob-turning” optimal timing is not directly implementable.
- Key parameters (P(doom), safety progress rates, pause feasibility) are uncertain and likely endogenous to strategic interaction.
- Tables/equations in the PDF are not fully machine-extractable in this pass; this analysis relies on the text narrative and the paper’s qualitative summaries.

## Stage 2: Evaluative Analysis

### Internal Coherence
Within its stated scope (person-affecting, mundane, stylized), the argument is coherent: it cleanly frames the tradeoff between background mortality and AI catastrophe risk, then studies how adding plausible “realism knobs” (discounting, QoL, concavity, multiphase progress, tests, distributional weights) predictably shifts optimal timing. The main coherence risk is scope-sensitive: once you relax the “single decision-maker with a timing knob” abstraction and allow strategic, institutional, and technological feedback loops, some of the qualitative conclusions (especially about the desirability of “pauses”) could flip.

### Key Factual Claims Verified

| Claim (paraphrased) | Crux? | Source Says | Actual | External Source | Status |
|---|---:|---|---|---|---|
| Mortality hazard for 20–25-year-olds can be ~0.05–0.08%/year in developed-country settings | **Y** | ~0.05–0.08% annually (healthy 20–25) | CDC 2021 life table for **US females** shows qx ≈ 0.00058–0.00077 (~0.058–0.077%) for ages 21–26 | https://stacks.cdc.gov/view/cdc/132418 | ok (matches range for females; “healthy” qualifier unverified) |
| Global life expectancy at birth is ~73 years; world median age is a little over 30 | N | ~73 and “a little over 30” | UN reports 2024 life expectancy ≈ 73.3; OWID/UN WPP median age (World) ≈ 30.6 in 2024 | https://www.un.org/en/global-issues/population ; https://ourworldindata.org/grapher/median-age.csv?tab=chart&stackMode=absolute&region=World | ok |
| Citation URL for “U.S. State Life Tables, 2021 (NVSR 73(6))” | N | Links to `nvsr73-06.pdf` | As of 2026-02-13, `nvsr73-06.pdf` is an unrelated NVSR issue (“births to U.S. teenagers”) | https://www.cdc.gov/nchs/data/nvsr/nvsr73/nvsr73-06.pdf | x (link mismatch) |

### Disconfirming Evidence Search

| Claim | Counterevidence Found | Alternative Explanation | Search Notes |
|---|---|---|---|
| “Large, near-term mortality reduction is a central upside” | No decisive counterevidence; broad uncertainty dominates | Superintelligence might not translate into rapid biomedical breakthroughs, or benefits could be delayed by regulation/manufacturing/clinical trials; upside may be smaller for existing cohorts | Looked for near-term longevity “escape velocity” evidence; mostly speculative/forecast literature; no clear empirical anchor |
| “Short post-capability pauses are often optimal” | Real-world pause feasibility is contested; many governance analyses emphasize race dynamics and defection/selection effects | Even if abstractly optimal, a pause attempt could shift work underground, increase militarization, or create overhangs | Looked for pause proposals and critiques; found mostly argument-level rather than quantified models with consensus parameterization |
| “Person-affecting stance changes the calculus materially” | Ethical literature contains sustained critiques of person-affecting restrictions (especially for existential risk) | Under impersonal/longtermist perspectives, even small increases in extinction risk can dominate the calculus, yielding much stronger “wait/stop” pressure | Focused on whether Bostrom’s “person-affecting” restriction is widely accepted; found disagreement rather than convergence |

### Corrections & Updates

| Item | URL | Published | Corrected/Updated | What Changed | Impacted Claim IDs | Action Taken |
|---|---|---:|---:|---|---|---|
| CDC life-table citation mismatch | https://www.cdc.gov/nchs/data/nvsr/nvsr73/nvsr73-06.pdf | 2024-07-24 (NVSR issue) | 2026-02-13 | The URL cited in the paper’s bibliography does not correspond to the referenced “U.S. State Life Tables, 2021” report | SOC-2026-023 | Verified mortality rates using CDC “United States Life Tables, 2021” (NVSR 72(12)) instead; noted mismatch explicitly |

### Internal Tensions / Self-Contradictions

| Tension | Parts in Conflict | Implication |
|---|---|---|
| “Mundane, person-affecting only” vs repeated reliance on extinction framing | The analysis is person-affecting yet uses P(extinction) as a central risk metric and motivates urgency with civilization-scale stakes | Suggests the conclusions may shift under alternative ethical framings (e.g., impersonal), and that the person-affecting restriction is doing substantial work |
| “Swift to harbor” vs “pause could help most at final stage” | Push toward faster capability development while also suggesting deliberate delay at/near deployment can be valuable | Highlights that the most decision-relevant lever might be post-capability deployment governance rather than pre-capability R&D throttling |

### Persuasion Techniques

| Technique | Example from Source | Effect on Reader |
|---|---|---|
| Analogy reframing | “Not Russian roulette; more like risky surgery for a fatal condition” | Normalizes higher risk tolerance by making the baseline feel urgent and non-neutral |
| Salience via background mortality | Emphasizes near-certainty of death absent transformative intervention | Shifts attention from tail risks to expected-life-years framing |
| Pre-bunking | Explicitly lists second-best failure modes for pauses | Defuses “therefore: pause now” inference from abstract optima |

### Unstated Assumptions

| Assumption | Claim ID | Critical? | Problematic? |
|---|---|---:|---:|
| “Aligned superintelligence” yields large mortality reduction on timescales relevant to existing people | RISK-2026-928 | Y | Y |
| Catastrophe risk declines monotonically with time spent on “safety work” (and can be purchased by waiting) | TRANS-2026-021 | Y | Y |
| Post-capability “safety windfall” exists and is front-loaded (Phase 2a/2b) | TRANS-2026-024 | Y | ? |
| Pause policies can be selectively applied to “dangerous scaleup/deployment” without broadly blocking beneficial applications | RISK-2026-933 | Y | Y |

### Evidence Assessment
This is a theoretically driven, parameterized decision-analysis paper. Its strongest contributions are (a) clarifying the structure of tradeoffs under a person-affecting perspective, and (b) showing how adding standard economic/decision-theoretic ingredients moves optima in predictable ways. Its weakest evidential points are those requiring empirical grounding: the magnitude of superintelligence upside for existing people; credible ranges for catastrophe probability; and the extent to which real governance mechanisms can produce “well-timed” pauses rather than blunt or counterproductive slowdowns.

### Credence Assessment
- **Overall Credence**: 0.50
- **Reasoning**: High confidence that the qualitative results follow from the paper’s stylized models; moderate confidence that these models highlight real considerations often missing in “pause now” discourse; low-to-moderate confidence that the implied policy posture (accelerate capability, then brief pause) is robust to strategic/implementation dynamics and to uncertainty about the speed of biomedical upside.

## Stage 3: Dialectical Analysis

### Steelmanned Argument
Even if superintelligence poses serious catastrophic risk, the “do nothing / slow down indefinitely” baseline is not ethically neutral for existing people: it locks in near-certain death for today’s population and leaves many other global risks unmitigated. Rational policy should therefore treat AGI development as a high-stakes intervention with both large upside and large downside, and optimize timing rather than defaulting to blanket delays. If safety progress is likely to accelerate once a capable system exists (via access to the artifact and AI-assisted alignment), then the best moment to “buy safety time” may be near deployment—where information and leverage are greatest—rather than through earlier, longer moratoria that are hard to implement and risk harmful side effects.

### Strongest Counterarguments
1. **Ethics scope objection**: If one gives significant moral weight to future generations (impersonal/total views), small changes in extinction risk can dominate, making much longer delays (or non-development) optimal.
2. **Upside realism objection**: “Superintelligence ⇒ rapid longevity escape” is speculative; if benefits are smaller or slower, the “fatal condition” analogy weakens and optimal delay lengthens substantially.
3. **Governance objection**: The “pause at the dock” strategy assumes unusually fine-grained control and coordination; in competitive multipolar reality, attempts to accelerate capability may increase tail risk more than the model captures.
4. **Endogeneity objection**: Risk isn’t a simple decreasing function of time; racing dynamics, overhangs, and security externalities can make waiting/coordination more valuable than the paper’s independent-parameter models suggest.

### Supporting Theories

| Theory/Framework | Source ID | How It Supports |
|---|---|---|
| Value of information | N/A | Motivates testing/information gathering as improving decision quality relative to fixed rules |
| Safety-as-luxury / time-of-perils | N/A | Supports the idea that faster progress through “perilous” phases can increase long-run survival in some models |

### Contradicting Theories

| Theory/Framework | Source ID | Point of Conflict |
|---|---|---|
| Precautionary principle / maxipok-style reasoning | N/A | Would reject high catastrophe probabilities even with large personal upside |
| Impersonal longtermism | N/A | Treats extinction risk as overriding due to vast expected future value |

### Synthesis Notes
This paper is most valuable as a corrective to an implicit “safe baseline” assumption in some pause advocacy: under person-affecting ethics, the status quo contains an enormous, ongoing harm stream. However, the key question for decision-making is not whether the paper’s stylized optima exist (they do), but whether real institutions can approximate the “good” parts of the recommendation (targeted, information-sensitive deployment gating) without triggering the “second-best” failure modes that could worsen outcomes.

### Claims to Cross-Reference
- Empirical plausibility and timelines for radical longevity improvement without AGI.
- Models of strategic race dynamics under pauses (defection, selection effects, and “overhang” risk).
- Estimates of AI catastrophe probability distributions and how they respond to marginal safety effort.

---

### Claim Summary

| ID | Type | Domain | Layer | Actor | Scope | Quantifier | Evidence | Credence | Claim |
|---|---|---|---|---|---|---|---|---:|---|
| SOC-2026-022 | [F] | SOC | ASSERTED | OTHER:Bostrom | who=global population; when=~2024; metrics=life expectancy, median age | ~ | E2 | 0.85 | Global life expectancy at birth is ~73 years and world median age is ~30, motivating a simplified ~40-year remaining-life baseline |
| SOC-2026-023 | [F] | SOC | ASSERTED | OTHER:Bostrom | who=healthy 20–25; where=developed countries; metric=annual mortality hazard | ~ | E2 | 0.70 | Annual mortality risk for 20–25-year-olds is ~0.05–0.08%/year; constant hazard implies expected lifespan ~1/0.0007 ≈ 1,400 years |
| RISK-2026-928 | [T] | RISK | ASSERTED | OTHER:Bostrom | who=existing people; model=go/no-go | can | E5 | 0.85 | Under one simple model, launching increases expected lifespan iff extinction risk at launch is below ~97% |
| RISK-2026-929 | [T] | RISK | ASSERTED | OTHER:Bostrom | who=existing people; framing=baseline risk vs transition risk | N/A | E5 | 0.60 | Baseline is not safe; superintelligence development is better analogized to risky surgery for a fatal condition than Russian roulette |
| RISK-2026-930 | [H] | RISK | ASSERTED | OTHER:Bostrom | who=decision-maker; models=QALY/discounting/safety progress | often | E5 | 0.55 | Across many parameter settings, even high catastrophe probabilities are worth accepting under the person-affecting objective |
| RISK-2026-931 | [T] | RISK | ASSERTED | OTHER:Bostrom | who=decision-maker; model=CRRA/QALY concavity | N/A | E5 | 0.60 | Risk aversion makes the decision more conservative but does not radically change the qualitative pattern |
| RISK-2026-932 | [T] | RISK | ASSERTED | OTHER:Bostrom | who=decision-maker; model=POMDP; intervention=testing | generally | E5 | 0.65 | With uncertainty and informative tests, an evidence-conditional policy dominates fixed delays; testing raises expected utility |
| RISK-2026-933 | [H] | RISK | ASSERTED | OTHER:Bostrom | who=policymakers; what=pauses; risks=second-best effects | often | E5 | 0.55 | Poorly implemented pauses can backfire; abstract timing analysis doesn’t directly yield a pause policy recommendation |
| TRANS-2026-021 | [T] | TRANS | ASSERTED | OTHER:Bostrom | model=safety progress vs mortality | often | E5 | 0.65 | Optimal delays are typically modest except when initial risk is very high and safety progress intermediate |
| TRANS-2026-022 | [T] | TRANS | ASSERTED | OTHER:Bostrom | model=discounting + QoL gap | sometimes | E5 | 0.60 | Discounting can push later with low QoL gap, but earlier with high QoL gap |
| TRANS-2026-023 | [T] | TRANS | ASSERTED | OTHER:Bostrom | model=QoL uplift | N/A | E5 | 0.70 | QoL uplift effect saturates; bounded risk threshold limits how much uplift favors immediate launch |
| TRANS-2026-024 | [H] | TRANS | ASSERTED | OTHER:Bostrom | model=multiphase safety windfall; intervention=Phase 2 pause | often | E5 | 0.55 | Multiphase “windfall” model often recommends a short non-zero post-capability pause |
| TRANS-2026-025 | [H] | TRANS | ASSERTED | OTHER:Bostrom | model=joint optimization over Phase 1 and Phase 2 | sometimes | E5 | 0.50 | Joint optimization can favor accelerating to capability and then pausing briefly; Phase 2 time can be especially valuable |
| TRANS-2026-026 | [T] | TRANS | ASSERTED | OTHER:Bostrom | who=heterogeneous population; ethics=prioritarian | likely | E5 | 0.55 | Prioritarian weighting and demographic heterogeneity shift the person-affecting social optimum toward shorter delays |

### Claims to Register

```yaml
claims:
  - id: "SOC-2026-022"
    text: >-
      Global life expectancy at birth is roughly 73 years and the world median age is a little over 30; using
      ~40 years as a simplified average remaining life expectancy for the current global population is a plausible
      approximation for timing calculations.
    type: "[F]"
    domain: "SOC"
    evidence_level: "E2"
    credence: 0.85
    operationalization: >-
      Check UN/UN WPP (or equivalent official statistics) for global life expectancy at birth and global median
      age for ~2024; evaluate whether the implied remaining-life-expectancy approximation is directionally
      reasonable for the current population age structure.
    assumptions:
      - Using median age as a proxy for “average person alive today” is acceptable for a simplified model.
      - Life expectancy at birth is a reasonable anchor for back-of-envelope remaining-life calculations.
    falsifiers:
      - Official statistics show global life expectancy or median age materially different from the cited ranges.
    source_ids: ["bostrom-2026-optimal-timing-superintelligence"]

  - id: "SOC-2026-023"
    text: >-
      In developed countries, annual mortality rates for 20–25-year-olds can be on the order of ~0.05–0.08% per
      year; if mortality were held constant at ~0.0007 per year throughout life, expected remaining lifespan
      would be approximately 1/0.0007 ≈ 1,400 years.
    type: "[F]"
    domain: "SOC"
    evidence_level: "E2"
    credence: 0.70
    operationalization: >-
      Use developed-country life tables to estimate annual death probability (qx) for ages ~20–25 (optionally
      stratified by sex and health status); confirm the 1/hazard approximation used for constant-hazard expected
      lifespan.
    assumptions:
      - “Healthy” 20–25-year-olds have death probabilities similar to the lower end of developed-country life
        tables (e.g., female/general-population rates).
      - Treating the hazard as constant is a simplifying approximation for illustrative modeling.
    falsifiers:
      - Life tables show substantially higher/lower death probabilities for the relevant ages in developed
        countries, or the hazard-to-life-expectancy mapping is misapplied.
    source_ids: ["bostrom-2026-optimal-timing-superintelligence"]

  - id: "RISK-2026-928"
    text: >-
      In a simple go/no-go model where existing people have ~40 years remaining life expectancy without
      superintelligence and ~1,400 years with successfully aligned superintelligence, launching immediately
      increases expected remaining life expectancy iff the extinction probability at launch is below ~97%.
    type: "[T]"
    domain: "RISK"
    evidence_level: "E5"
    credence: 0.85
    operationalization: >-
      Reproduce the model derivation with the stated inputs (m0, m1, q0, q1) and verify the cutoff probability;
      vary assumptions (life-extension magnitude, quality-of-life weights) to test sensitivity.
    assumptions:
      - “Failure” corresponds to immediate death (or equivalently to losing all remaining lifespan value).
      - The post-success mortality hazard is approximately constant at the chosen low level.
    falsifiers:
      - Independent reproduction finds the stated cutoff does not follow from the stated assumptions.
    source_ids: ["bostrom-2026-optimal-timing-superintelligence"]

  - id: "RISK-2026-929"
    text: >-
      From a person-affecting perspective, the status quo is not a safe baseline because it includes high ongoing
      mortality and other background risks; thus developing superintelligence is better analogized to risky
      surgery for a fatal condition than to playing Russian roulette from a safe baseline.
    type: "[T]"
    domain: "RISK"
    evidence_level: "E5"
    credence: 0.60
    operationalization: >-
      Formalize the baseline risk/benefit comparison for a representative existing person (mortality + background
      catastrophic risks vs transition risks); test whether the analogy aligns with the implied utility model and
      decision recommendations under plausible inputs.
    assumptions:
      - Existing-person welfare is reasonably proxied by (discounted, quality-adjusted) expected remaining life.
    falsifiers:
      - A better-calibrated decision model shows the surgery analogy systematically misleads relative to the
        Russian-roulette framing in the relevant policy regime.
    source_ids: ["bostrom-2026-optimal-timing-superintelligence"]

  - id: "RISK-2026-930"
    text: >-
      Under person-affecting models that incorporate safety progress, discounting, quality-of-life differentials,
      and QALY concavity, there exist broad parameter settings where accepting even high probabilities of
      catastrophic AI failure is optimal relative to delaying or forgoing superintelligence.
    type: "[H]"
    domain: "RISK"
    evidence_level: "E5"
    credence: 0.55
    operationalization: >-
      Reproduce the paper’s parameter sweeps; define “broad” parameter regimes and test robustness to
      alternative functional forms (risk decline over time, hazard changes, benefit ramp-up delays).
    assumptions:
      - Parameter ranges explored are within the plausible range for real-world decisions.
      - Benefits from success are realized on timescales relevant to existing people.
    falsifiers:
      - Under more realistic benefit delays or risk dynamics, high-catastrophe-probability optima disappear for
        most plausible parameterizations.
    source_ids: ["bostrom-2026-optimal-timing-superintelligence"]

  - id: "RISK-2026-931"
    text: >-
      Adding diminishing marginal utility (risk aversion/concavity) over quality-adjusted life years shrinks the
      region of “launch immediately” recommendations and lowers risk-at-launch somewhat, but does not
      radically change the paper’s qualitative conclusions about generally modest optimal delays.
    type: "[T]"
    domain: "RISK"
    evidence_level: "E5"
    credence: 0.60
    operationalization: >-
      Implement CRRA (or alternative concave) utility over QALYs and compare optimal launch times/risk-at-launch
      against the linear (risk-neutral) baseline across parameter grids.
    assumptions:
      - The chosen concavity parameters are representative of plausible preferences over lifespan/QALYs.
    falsifiers:
      - Plausible concavity parameters systematically imply very long delays or never-launch policies across most
        parameter ranges.
    source_ids: ["bostrom-2026-optimal-timing-superintelligence"]

  - id: "RISK-2026-932"
    text: >-
      If intrinsic catastrophic risk is uncertain and safety tests provide information about that risk, then the
      optimal decision is an evidence-conditional policy (launch when evidence is favorable, delay when it is
      not), and such testing increases expected utility relative to having the same prior uncertainty but no tests.
    type: "[T]"
    domain: "RISK"
    evidence_level: "E5"
    credence: 0.65
    operationalization: >-
      Model the setting as a POMDP with explicit priors and test sensitivity/specificity; compare optimal policy
      value with and without tests holding other assumptions fixed; stress-test under alternative testing regimes.
    assumptions:
      - Tests are informative enough to meaningfully update posterior beliefs about catastrophe probability.
      - Decision-makers can credibly commit to act on test outcomes.
    falsifiers:
      - Under realistic tests and governance constraints, evidence-conditioned policies are infeasible or do not
        improve expected outcomes.
    source_ids: ["bostrom-2026-optimal-timing-superintelligence"]

  - id: "RISK-2026-933"
    text: >-
      Real-world efforts to pause or slow AI development can be net harmful via second-best effects (e.g.,
      shifting development to less cooperative actors, militarization, selection effects, compute/algorithm
      overhangs, ossified relinquishment), so abstract optimal-timing analyses do not straightforwardly imply
      support for any particular pause policy.
    type: "[H]"
    domain: "RISK"
    evidence_level: "E5"
    credence: 0.55
    operationalization: >-
      Build strategic and institutional models of pause implementation under multipolar competition; evaluate
      whether typical pause designs reduce overall catastrophe risk after accounting for displacement, secrecy,
      and overhang dynamics.
    assumptions:
      - Second-best effects are large enough to matter relative to the direct “more time for safety” benefit.
    falsifiers:
      - Evidence from historical analogues or strong models indicates pauses reliably reduce net risk with minimal
        offsetting harms.
    source_ids: ["bostrom-2026-optimal-timing-superintelligence"]

  - id: "TRANS-2026-021"
    text: >-
      In a timing model where waiting reduces catastrophic AI risk via safety progress but imposes ongoing
      mortality and discounting costs, optimal delays are generally modest; very long delays appear mainly when
      initial risk is extremely high and safety progress is neither very fast nor very slow (an intermediate range).
    type: "[T]"
    domain: "TRANS"
    evidence_level: "E5"
    credence: 0.65
    operationalization: >-
      Reproduce the optimal-delay surfaces over (initial risk, safety progress rate) and test alternative risk
      decline functional forms; evaluate robustness of “intermediate range → longest delays” claim.
    assumptions:
      - Risk decreases smoothly with safety progress and does not have major discontinuities.
    falsifiers:
      - Alternative plausible models imply long optimal delays across wide parameter ranges, not only in a narrow
        “intermediate progress” band.
    source_ids: ["bostrom-2026-optimal-timing-superintelligence"]

  - id: "TRANS-2026-022"
    text: >-
      Adding temporal discounting tends to push optimal launch times later when pre/post-AGI quality is similar,
      but can push optimal launch times earlier when post-AGI life is sufficiently higher quality (because
      discounting penalizes delaying the onset of that higher-quality existence).
    type: "[T]"
    domain: "TRANS"
    evidence_level: "E5"
    credence: 0.60
    operationalization: >-
      Implement discounting plus quality weights and compute optimal timing across a grid of discount rates and
      quality ratios; identify where the comparative statics flip sign.
    assumptions:
      - Discounting is exponential and represents “pure time preference” (mortality handled separately).
    falsifiers:
      - Under reasonable discounting/quality-weight parameters, the sign flip does not occur.
    source_ids: ["bostrom-2026-optimal-timing-superintelligence"]

  - id: "TRANS-2026-023"
    text: >-
      Quality-of-life uplift after AGI expands the region where immediate launch is optimal and shortens optimal
      delays, but this effect saturates: because the “launch-asap” risk bar is bounded above, arbitrarily large
      quality improvements cannot make immediate launch optimal for all initial-risk/safety-progress settings.
    type: "[T]"
    domain: "TRANS"
    evidence_level: "E5"
    credence: 0.70
    operationalization: >-
      Analyze the model’s decision boundary as a function of the quality ratio q1/q0 and show it approaches a
      limit; reproduce the saturation behavior numerically.
    assumptions:
      - Model structure implies an upper bound on the launch-asap risk threshold.
    falsifiers:
      - Under correct analysis of the stated model, increasing q1/q0 can push all cases to immediate launch.
    source_ids: ["bostrom-2026-optimal-timing-superintelligence"]

  - id: "TRANS-2026-024"
    text: >-
      If safety progress accelerates once an AGI-capable artifact exists (“safety windfall”) and then faces
      diminishing returns, optimal timing often involves reaching AGI capability quickly (Phase 1) and then
      pausing for a short but non-zero period prior to full deployment (Phase 2), typically on the order of months
      to a small number of years.
    type: "[H]"
    domain: "TRANS"
    evidence_level: "E5"
    credence: 0.55
    operationalization: >-
      Specify plausible subphase rates (2a–2d) and compute optimal Phase-2 pause durations; evaluate sensitivity
      to alternative “windfall” assumptions and to governance feasibility constraints.
    assumptions:
      - Post-capability safety progress is front-loaded and meaningfully faster than pre-capability progress.
    falsifiers:
      - Empirical/organizational evidence indicates post-capability safety progress is not front-loaded, or that
        pausing increases net risk via displacement/overhang.
    source_ids: ["bostrom-2026-optimal-timing-superintelligence"]

  - id: "TRANS-2026-025"
    text: >-
      In joint optimization over time-to-capability (Phase 1) and post-capability pause time (Phase 2), it is often
      optimal to accelerate Phase 1 relative to the default scenario and then use a short Phase-2 pause to gain
      a large share of the available safety improvements; small changes to Phase 2 can matter more than similarly
      small changes to Phase 1.
    type: "[H]"
    domain: "TRANS"
    evidence_level: "E5"
    credence: 0.50
    operationalization: >-
      Compute optimal (t1, t2) for scenario grids with separate levers; compare marginal value of time in Phase 1
      vs early Phase 2 under windfall assumptions.
    assumptions:
      - Phase-2 early time yields disproportionately high safety gains per unit time.
    falsifiers:
      - Joint optimization under plausible assumptions does not favor acceleration + short pause, or Phase-1 time
        is consistently more valuable than Phase-2 time.
    source_ids: ["bostrom-2026-optimal-timing-superintelligence"]

  - id: "TRANS-2026-026"
    text: >-
      Because different demographics have different prudential interests (e.g., higher near-term mortality for the
      old/sick and worse baseline welfare for the poor), applying prioritarian weighting in a person-affecting
      social welfare function tends to shift the optimal timeline toward shorter delays to superintelligence.
    type: "[T]"
    domain: "TRANS"
    evidence_level: "E5"
    credence: 0.55
    operationalization: >-
      Specify demographic mortality/QoL distributions and a prioritarian social welfare function; compute the
      socially optimal timing and compare to the neutral-utilitarian person-affecting baseline.
    assumptions:
      - Worse-off groups systematically benefit more from earlier transition (higher mortality/low QoL now).
    falsifiers:
      - With plausible demographics and prioritarian parameters, the weighted optimum instead implies longer
        delays than the neutral baseline.
    source_ids: ["bostrom-2026-optimal-timing-superintelligence"]
```

---

**Analysis Date**: 2026-02-13  
**Analyst**: codex (`gpt-5.2`)  
**Credence in Analysis**: 0.75

**Credence Reasoning**:
- High confidence the descriptive summary and extracted claim inventory reflect the paper.
- Moderate confidence in the evaluation given limited ability to validate the paper’s key free parameters (P(doom), safety progress functions, feasibility of targeted pauses).
- Main uncertainty is external validity: whether real institutions can implement the fine-grained “dock” controls implied by the stylized optimum.

## Analysis Log

| Pass | Date | Tool | Model | Duration | Tokens | Cost | Notes |
|---:|---|---|---|---:|---:|---:|---|
| 1 | 2026-02-13 | codex | gpt-5.2 | ~1m | ? | ? | Superseded: started without usage session ID (token tracking) |
| 2 | 2026-02-13 | codex | gpt-5.2 | 24m57s | 6088110 | ? | Initial 3-stage analysis + claim extraction + DB registration |

### Revision Notes

**Pass 2**:
- Created initial source analysis with 3-stage methodology.
- Extracted 14 registerable claims (SOC/TRANS/RISK).
- Verified two key quantitative inputs against UN/OWID and CDC life tables; noted CDC citation URL mismatch in the paper’s bibliography.
