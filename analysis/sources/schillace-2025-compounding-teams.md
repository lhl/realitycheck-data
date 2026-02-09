# Source Analysis: I have seen the compounding teams

> **Claim types**: `[F]` fact, `[T]` theory, `[H]` hypothesis, `[P]` prediction, `[A]` assumption, `[C]` counterfactual, `[S]` speculation, `[X]` contradiction
> **Evidence**: **E1** systematic review/meta-analysis; **E2** peer-reviewed/official stats; **E3** expert consensus/preprint; **E4** credible journalism/industry; **E5** opinion/anecdote; **E6** unsupported/speculative

## Metadata

| Field | Value |
|---|---|
| **Source ID** | `schillace-2025-compounding-teams` |
| **Title** | I have seen the compounding teams |
| **Author(s)** | Sam Schillace |
| **Date** | 2025-09-28 |
| **Type** | BLOG |
| **URL** | https://sundaylettersfromsam.substack.com/p/i-have-seen-the-compounding-teams |
| **Reliability** | 0.60 |
| **Rigor Level** | [REVIEWED] |
| **Bias Notes** | Newsletter-style practitioner note based on limited but direct observation (“two or three teams”). Strong on pattern recognition and workflow hypotheses; weak on quantification and selection bias (seeing unusually successful early adopters). |

**Claims YAML**: [`analysis/sources/schillace-2025-compounding-teams.yaml`](schillace-2025-compounding-teams.yaml)

## Stage 1: Descriptive Analysis

### Core Thesis
Schillace claims he has observed “compounding teams” whose output grows superlinearly because they build a framework around models (not just use out-of-the-box tools) and adopt a recursive “build tools that build tools” mindset. These teams rely heavily on filesystem+git artifacts, constant executable validation, and tight modular boundaries, and they shift the bottleneck to human attention rather than implementation labor.

### Summary (Neutral)
The post contrasts ordinary “vibe coding” tool adoption (short-term productivity boost) with a deeper pattern: teams that build custom agent frameworks with tool-calling, hooks, flow control, and proactive strategies. He emphasizes low-level programmer tools (filesystem, git, markdown, Kubernetes, XML) as “good infrastructure for model-based action,” because models already use them effectively.

He claims compounding comes from recursion: teams tell the system “you’ll need a tool for that—build it,” then check it into git as a permanent capability improvement. Reported operational hallmarks include running many parallel processes, high API/token spend (hundreds of dollars/day, with a goal of $1,000/day for one team), and norms against humans touching code (“code review” as “firing offense”).

Schillace argues coordination becomes the central challenge: modular boundaries matter; small teams of high-level designers outperform large mixed teams; and it is difficult to mix AI-driven and hand-coded styles in the same repo. Validation is continuous because models are not trusted—software must execute and acceptance tests are meaningful and constant.

### Key Claims

| # | Claim | Claim ID | Type | Domain | Evidence | Credence | Verified? | Falsifiable By |
|---|-------|----------|------|--------|----------|----------:|-----------|----------------|
| 1 | “Compounding teams” achieve superlinear productivity by building frameworks around models (tool calling, hooks, flow control, strategies) rather than using out-of-the-box coding assistants | INST-2025-003 | [H] | INST | E5 | 0.55 | ? | Surveys show no meaningful advantage of custom frameworks over commodity tools after controlling for team skill |
| 2 | These teams rely heavily on filesystem+git (+ common programmer tools) as durable infrastructure for model-based action and self-modification | TECH-2025-066 | [H] | TECH | E5 | 0.60 | ? | High-performing compounding teams predominantly use alternative memory substrates (databases/CRDTs) and do not rely on filesystem+git artifacts |
| 3 | Compounding comes from recursion: teams instruct the coding system to build tools it needs, then check them into git as durable improvements (“build a tool for making a tool”) | INST-2025-004 | [T] | INST | E5 | 0.60 | ? | Longitudinal observation shows tool-building recursion does not compound and instead plateaus due to maintenance burden |
| 4 | In observed compounding teams, the bottleneck shifts from implementation to human attention; multiple processes run in parallel and ideas outstrip review capacity | LABOR-2025-001 | [H] | LABOR | E5 | 0.55 | ? | Time-allocation data shows implementation remains the bottleneck; attention and coordination do not dominate |
| 5 | API/token spend is routinely hundreds of dollars/day for these teams, with one team targeting ~$1,000/day; some teams report not directly touching code for months | ECON-2025-003 | [F] | ECON | E5 | 0.50 | ? | Independent accounting logs contradict these spend/behavior claims |
| 6 | Continuous executable validation (acceptance tests) is central because models are not trusted; problems must be broken into solvable pieces with meaningful gates | TECH-2025-067 | [T] | TECH | E5 | 0.65 | ? | Teams succeed with high autonomy without constant acceptance testing or decomposition discipline |

### Argument Structure

```
(1) Out-of-box tools give a short-term boost
        ↓ but
(2) Compounding requires building a framework around the model
        ↓ enabled by
(3) Durable infrastructure (filesystem+git) + recursive tool-building
        ↓ leads to
(4) Much higher throughput → bottleneck shifts to attention/coordination
        ↓ requires
(5) Modular boundaries + continuous executable validation
```

### Theoretical Lineage
- **Meta-tooling**: “build systems that build systems” recursion (automation of automation).
- **External memory**: durable artifacts for state across sessions (git logs, markdown, structured files).
- **Bottleneck shift**: as implementation gets cheap, attention/coordination and evaluation become scarce.

### Scope & Limitations
- The post reports on a small N of observed teams; selection bias is likely.
- “Exponential output” is not measured; could be “rapid linear” experienced subjectively.
- The described tool stack may reflect what Schillace personally encounters (filesystem/git-centric engineering culture).

## Stage 2: Evaluative Analysis

### Internal Coherence
The compounding story is coherent as a feedback loop: invest in tooling and representations that allow the system to operate more independently; reuse those tools; and iterate. The emphasis on executable validation and modular boundaries is consistent with known failure modes in agentic coding (drift, hallucinated “done,” integration failures).

The weakest link is the claim of *superlinear* scaling: coordination and maintenance burdens often scale poorly, and “tool-building recursion” can easily create a fragile tower of internal tools.

### Key Factual Claims Verified

| Claim (paraphrased) | Crux? | Source Says | Actual | External Source | Status |
|---------------------|-------|-------------|--------|-----------------|--------|
| The post is authored by Sam Schillace and published Sep 28, 2025 | N | Byline + date | JSON-LD includes author “Sam Schillace” and `datePublished` 2025-09-28 | https://sundaylettersfromsam.substack.com/p/i-have-seen-the-compounding-teams | ok |
| A “$1,000/day token spend” target is consistent with at least one publicly documented “software factory” doctrine | N | One team targets ~$1,000/day | StrongDM publicly promotes a $1,000/day token heuristic | https://factory.strongdm.ai/ | ok (corroborated) |

### Disconfirming Evidence Search

| Claim | Counterevidence Found | Alternative Explanation | Search Notes |
|-------|----------------------|------------------------|--------------|
| INST-2025-003 (custom frameworks are required to compound) | Many teams report meaningful productivity gains with commodity tools alone, especially on well-scoped tasks | “Compounding” may reflect team skill + process discipline more than bespoke frameworks | Looked for systematic studies comparing bespoke harnesses vs off-the-shelf tools; found mostly anecdote and vendor claims |
| LABOR-2025-001 (attention becomes bottleneck) | Some reports suggest verification/review/compliance becomes the bottleneck more than ideation | The bottleneck may split: attention for steering + verification attention for trust | Considered adjacent sources emphasizing verification bottlenecks; treated as plausible but domain-dependent |

### Internal Tensions / Self-Contradictions

| Tension | Parts in Conflict | Implication |
|---------|-------------------|-------------|
| “Not touching code” vs “models aren’t trusted” | If models aren’t trusted, removing code inspection increases reliance on harnesses | Supports the strong requirement for acceptance tests and modular decomposition |

### Persuasion Techniques

| Technique | Example from Source | Effect on Reader |
|-----------|---------------------|------------------|
| Future-tech epiphany | “like seeing a PC… for the first time” | Increases perceived inevitability and urgency |
| Salient anecdotes | “code review is a firing offense” | Creates vivid identity signals that substitute for measurement |

### Unstated Assumptions

| Assumption | Claim ID | Critical? | Problematic? |
|------------|----------|-----------|--------------|
| Recursive tool-building yields net positive compounding rather than fragile complexity | INST-2025-004 | High | Yes |
| Modular boundaries can be maintained as throughput rises | LABOR-2025-001 | Medium | Mixed |

### Evidence Assessment
- The strongest elements are mechanism sketches that align with other accounts (external artifacts, validation gates, modular boundaries).
- The weakest elements are prevalence/scale claims and “exponential output” framing without measurement.

### Credence Assessment
- **Overall Credence**: 0.60
- **Reasoning**: The workflow pattern is plausible and partially corroborated by other sources (StrongDM), but magnitude and generality remain uncertain.

## Stage 3: Dialectical Analysis

### Steelmanned Argument
Out-of-box AI coding tools help, but they do not transform the organization because they leave the core workflow unchanged. Compounding teams instead treat the model as a component inside a larger system: durable memory artifacts, tool-use primitives, proactive strategies, and continuous executable validation. They recursively automate their own automation, baking improvements into the repo. This yields a flywheel: each new tool reduces the marginal cost of the next tool, allowing output to scale until the bottleneck becomes attention and coordination.

### Strongest Counterarguments
1. **Complexity debt**: recursive tool-building creates an internal platform that itself requires maintenance, documentation, and governance.
2. **Goodharting**: acceptance tests can be gamed; compounding might be “compounding on the harness,” not on real-world outcomes.
3. **Organizational limits**: mixing styles may be hard, but forbidding code review could be unacceptable in many domains.

### Supporting Theories

| Theory/Framework | Source ID | How It Supports |
|------------------|-----------|-----------------|
| Software factory doctrine (holdouts, harness, tokens) | `strongdm-2026-software-factory-principles` | Corroborates high token spend, harness primacy, and the centrality of validation |
| Harness artifacts across context windows | `anthropic-2025-effective-harnesses-long-running-agents` | Provides an explicit harness recipe (progress logs, git commits) consistent with Schillace’s “filesystem-based” claim |

### Contradicting Theories

| Theory/Framework | Source ID | Point of Conflict |
|------------------|-----------|------------------|
| Maintainer-externality critique | `ronacher-2026-agent-psychosis` | Warns that increased output can create social and quality externalities without strong gating norms |

### Synthesis Notes
Schillace is a bridge between “control plane” and “correctness plane” framings: he emphasizes custom orchestration frameworks and durable tool substrates (control plane), but also stresses constant executable validation (correctness plane) and modular boundaries (institutional coordination).

### Claims to Cross-Reference
- INST-2025-003/004: do frameworks actually compound output over months, or do they plateau as complexity debt accumulates?
- LABOR-2025-001: does attention become the bottleneck, or is verification/compliance the binding constraint in most domains?
- ECON-2025-003 vs ECON-2026-912: do high-token-spend regimes persist as pricing changes, or are they a subsidy-era artifact?

### Claim Summary

| ID | Type | Domain | Evidence | Credence | Claim |
|----|------|--------|----------|----------:|-------|
| INST-2025-003 | [H] | INST | E5 | 0.55 | Compounding requires bespoke frameworks around models, not just commodity tools |
| TECH-2025-066 | [H] | TECH | E5 | 0.60 | Filesystem+git infrastructure is a core substrate for compounding teams |
| INST-2025-004 | [T] | INST | E5 | 0.60 | Recursive “build tools that build tools” mindset produces compounding capability |
| LABOR-2025-001 | [H] | LABOR | E5 | 0.55 | Bottleneck shifts to human attention; many parallel processes run |
| ECON-2025-003 | [F] | ECON | E5 | 0.50 | Token spend hundreds/day; one team targets ~$1,000/day; some don’t touch code for months |
| TECH-2025-067 | [T] | TECH | E5 | 0.65 | Continuous executable validation and decomposition gates are central because models aren’t trusted |

### Claims to Register

```yaml
claims:
  - id: "INST-2025-003"
    text: >-
      “Compounding teams” achieve superlinear productivity by building frameworks around models (tool calling, hooks,
      flow control, strategies) rather than using out-of-the-box coding assistants alone.
    type: "[H]"
    domain: "INST"
    evidence_level: "E5"
    credence: 0.55
    source_ids: ["schillace-2025-compounding-teams"]
    operationalization: >-
      Compare teams using commodity tools vs bespoke frameworks, controlling for team skill and task mix; measure
      long-run throughput, defect rates, and maintenance burden over 6–12 months.
    assumptions:
      - “Compounding” can be operationalized as increasing output per unit input over time.
    falsifiers:
      - After controls, bespoke frameworks do not outperform commodity tools on long-run outcomes.

  - id: "TECH-2025-066"
    text: >-
      High-performing “compounding teams” rely heavily on filesystem and git (plus common programmer tools) as durable
      infrastructure for model-based action and self-modification.
    type: "[H]"
    domain: "TECH"
    evidence_level: "E5"
    credence: 0.60
    source_ids: ["schillace-2025-compounding-teams"]
    operationalization: >-
      Survey compounding-style teams and categorize memory substrates (filesystem/git, DBs, vector stores, CRDTs);
      correlate substrate choice with reliability and coordination outcomes.
    assumptions:
      - Substrate use can be measured and compared meaningfully across organizations.
    falsifiers:
      - Most successful teams do not rely on filesystem/git artifacts as the primary substrate.

  - id: "INST-2025-004"
    text: >-
      Compounding productivity can come from a recursive mindset: automate everything possible and instruct the coding
      system to build tools it needs, checking them into git as durable improvements (“build a tool for making a tool”).
    type: "[T]"
    domain: "INST"
    evidence_level: "E5"
    credence: 0.60
    source_ids: ["schillace-2025-compounding-teams"]
    operationalization: >-
      Track tool creation and reuse over time in compounding teams; measure whether new tools reduce marginal cost
      and increase output, net of maintenance effort.
    assumptions:
      - Tool reuse is frequent enough to amortize creation cost.
    falsifiers:
      - Tool-building recursion increases complexity and does not produce sustained throughput gains.

  - id: "LABOR-2025-001"
    text: >-
      In “compounding teams,” the bottleneck shifts from implementation to human attention: throughput increases such
      that ideas and parallel processes outstrip steering and review capacity.
    type: "[H]"
    domain: "LABOR"
    evidence_level: "E5"
    credence: 0.55
    source_ids: ["schillace-2025-compounding-teams"]
    operationalization: >-
      Measure time allocation and queueing delays (ideation/steering vs implementation vs verification) in teams
      using high-autonomy agents; test whether attention becomes dominant constraint.
    assumptions:
      - Implementation time decreases substantially relative to steering capacity.
    falsifiers:
      - Verification/compliance or integration remains the dominant bottleneck rather than attention.

  - id: "ECON-2025-003"
    text: >-
      Schillace reports that compounding teams have API/token spend routinely in the hundreds of dollars per day (with
      one team aiming for ~$1,000/day), and that some shipping-product teams have not directly touched or looked at code
      in multiple months.
    type: "[F]"
    domain: "ECON"
    evidence_level: "E5"
    credence: 0.50
    source_ids: ["schillace-2025-compounding-teams"]
    operationalization: >-
      Collect accounting logs from such teams and measure spend per engineer per day; instrument code interaction
      events (edits/reviews) over time to validate “not touching code” claims.
    assumptions:
      - Teams can provide trustworthy accounting and telemetry.
    falsifiers:
      - Measured spend is far lower/higher and/or teams routinely touch code despite the claim.

  - id: "TECH-2025-067"
    text: >-
      Continuous executable validation (acceptance tests) and decomposition into solvable pieces are central to
      compounding-team workflows because models are not trusted and correctness must be enforced by execution.
    type: "[T]"
    domain: "TECH"
    evidence_level: "E5"
    credence: 0.65
    source_ids: ["schillace-2025-compounding-teams"]
    operationalization: >-
      Compare incident/defect rates for teams with strong executable acceptance gates vs weaker gates under similar
      autonomy; measure whether stronger gates enable longer autonomous runs safely.
    assumptions:
      - Acceptance tests can be designed to reflect real-world correctness.
    falsifiers:
      - Teams succeed with long autonomy without continuous acceptance testing or decomposition discipline.
```

---

**Analysis Date**: 2026-02-09
**Analyst**: gpt-5.2
**Credence in Analysis**: 0.70

**Credence Reasoning**:
- Moderate confidence the reported patterns are real for some early-adopter teams.
- Low confidence on prevalence and superlinear scaling magnitude; high selection bias risk.

## Analysis Log

| Pass | Date | Tool | Model | Duration | Tokens | Cost | Notes |
|------|------|------|-------|----------|--------|------|-------|
| 1 | 2026-02-09 | codex | gpt-5.2 | ? | ? | ? | Initial 3-stage analysis + extracted claims; imported to DB. |

### Revision Notes

**Pass 1**: Initial 3-stage analysis + extracted claims.
