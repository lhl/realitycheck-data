# Source Analysis: How StrongDM’s AI team build serious software without even looking at the code

> **Claim types**: `[F]` fact, `[T]` theory, `[H]` hypothesis, `[P]` prediction, `[A]` assumption, `[C]` counterfactual, `[S]` speculation, `[X]` contradiction
> **Evidence**: **E1** systematic review/meta-analysis; **E2** peer-reviewed/official stats; **E3** expert consensus/preprint; **E4** credible journalism/industry; **E5** opinion/anecdote; **E6** unsupported/speculative

## Metadata

| Field | Value |
|---|---|
| **Source ID** | `willison-2026-strongdm-software-factory` |
| **Title** | How StrongDM’s AI team build serious software without even looking at the code |
| **Author(s)** | Simon Willison |
| **Date** | 2026-02-07 |
| **Type** | BLOG |
| **URL** | https://simonwillison.net/2026/Feb/7/software-factory/ |
| **Reliability** | 0.70 |
| **Rigor Level** | [REVIEWED] |
| **Bias Notes** | Enthusiastic practitioner commentary with quotes and links; relies on a demo + StrongDM’s self-description. High signal for “what is being claimed and how it is framed,” weaker as evidence for effectiveness or generality. |

**Claims YAML**: [`analysis/sources/willison-2026-strongdm-software-factory.yaml`](willison-2026-strongdm-software-factory.yaml)

## Stage 1: Descriptive Analysis

### Core Thesis
Willison reports seeing a demo of “Dark Factory” software development (no human looks at the code), identifies the team as StrongDM, and highlights StrongDM’s public “Software Factory” write-up and Attractor specifications as a concrete glimpse of a potential future: engineers build and monitor systems that build software.

### Summary (Neutral)
The post connects three threads:
- **Shapiro’s “Dark Factory”**: a level of AI adoption where humans do not read the produced code.
- **StrongDM’s Software Factory**: a public description of a non-interactive, harness-driven workflow (specs + scenarios → agent loops).
- **Attractor**: an open GitHub repository that contains natural-language specifications (not code) for building a “non-interactive coding agent” / software factory.

Willison emphasizes the importance of scenarios as “holdout sets” (not accessible to the coding agents), framing this as a way to imitate aggressive external QA. He closes by describing the workflow as engineers transitioning from writing code to building systems that generate code, calling it “the Dark Factory.”

### Key Claims

| # | Claim | Claim ID | Type | Domain | Evidence | Credence | Verified? | Falsifiable By |
|---|-------|----------|------|--------|----------|----------:|-----------|----------------|
| 1 | The `strongdm/attractor` repository contains no implementation code and instead publishes natural-language specs (Markdown) plus instructions to implement Attractor using a modern coding agent | TECH-2026-978 | [F] | TECH | E2 | 0.90 | GitHub | Repo contents change materially (implementation code appears) or README no longer instructs agent-based implementation |
| 2 | A “spec-first” software-factory workflow inverts typical artifacts: natural-language specs and validation scenarios become the primary governance surface; code becomes an intermediate artifact produced by agents | INST-2026-914 | [T] | INST | E5 | 0.60 | ? | Real deployments show specs/scenarios do not become primary governance artifacts; code review remains dominant |
| 3 | Willison’s “Dark Factory” framing suggests near-term role transition: software engineers shift from writing code to building and semi-monitoring the systems that generate code | TRANS-2026-019 | [H] | TRANS | E5 | 0.55 | ? | Labor data shows no such role shift, or it remains niche despite agent advances |

### Argument Structure

```
(1) A “dark factory” demo exists (StrongDM)
        ↓
(2) StrongDM publicly documents its workflow
        ↓
(3) “Holdout scenario” testing is a key primitive
        ↓
(4) Attractor specs show a spec-driven, agent-executed pipeline
        ↓
(5) Implication: engineers build/monitor software-generating systems
```

### Theoretical Lineage
- **Acceptance testing as governance**: holdout scenarios as external QA analogue.
- **Program synthesis / agentic loops**: code as a byproduct of search + validation.
- **Infrastructure-first engineering**: build harnesses/tools rather than hand-authoring artifacts.

### Scope & Limitations
- The post is not a controlled evaluation; “serious software” is not operationalized.
- It reports on a demo and public docs; effectiveness claims remain unverified.

## Stage 2: Evaluative Analysis

### Internal Coherence
The post’s framing is coherent: if you want to avoid reading code, you need strong validation primitives (holdout scenarios) and durable specification artifacts. Publishing “spec-only repos” is an extreme but consistent consequence: the spec itself becomes the product.

### Key Factual Claims Verified

| Claim (paraphrased) | Crux? | Source Says | Actual | External Source | Status |
|---------------------|-------|-------------|--------|-----------------|--------|
| `strongdm/attractor` contains only specs (Markdown) and instructs readers to use a coding agent to implement it | **Y** | Repo contains no code; specs are the artifact | GitHub API shows five files (LICENSE + 4 Markdown). README includes “Supply the following prompt…” | https://github.com/strongdm/attractor ; https://raw.githubusercontent.com/strongdm/attractor/main/README.md | ok |
| StrongDM publicly promotes the “$1,000/day tokens per engineer” heuristic | N | Quotes the heuristic | The line exists on StrongDM’s public page | https://factory.strongdm.ai/ | ok |

### Disconfirming Evidence Search

| Claim | Counterevidence Found | Alternative Explanation | Search Notes |
|-------|----------------------|-------------------------|--------------|
| INST-2026-914 (spec/scenario becomes primary governance) | Many orgs cannot drop code review due to audit, security, and accountability needs | Spec-first may be viable only for internal tools or low-regret domains; high-risk domains keep review | Searched for “spec-only repo” adoption patterns and “no code review” production processes; evidence is sparse and anecdotal |
| TRANS-2026-019 (role transition) | Current job roles still emphasize coding and review in most orgs | The transition may appear as a specialization (harness engineers, agent-ops) rather than a full role replacement | Looked for labor-market data on “agent harness engineer” roles; early signals exist but not systematic |

### Internal Tensions / Self-Contradictions

| Tension | Parts in Conflict | Implication |
|---------|-------------------|-------------|
| “No one looks at the code” vs “debugging reality” | Many failures require deep investigation | “No code review” likely depends on unusually strong harnesses and/or narrow domains |

### Persuasion Techniques

| Technique | Example from Source | Effect on Reader |
|-----------|---------------------|------------------|
| Future glimpse framing | “It felt like a glimpse of one potential future…” | Encourages treating anecdote as trend signal |
| Highlighting novelty artifacts | “Repo contains no code at all” | Makes the concept concrete and memorable |

### Unstated Assumptions

| Assumption | Claim ID | Critical? | Problematic? |
|------------|----------|-----------|--------------|
| Holdout scenarios can be made comprehensive enough to govern production software | INST-2026-914 | High | Yes |
| Organizations will accept “system-generated code” accountability models | TRANS-2026-019 | Medium | Mixed |

### Evidence Assessment
- Strong evidence for the existence and structure of the Attractor spec repo (verifiable).
- Weak evidence for general effectiveness; most claims are interpretive.

### Credence Assessment
- **Overall Credence**: 0.65
- **Reasoning**: High confidence about the artifact claims; moderate confidence about role-transition extrapolation.

## Stage 3: Dialectical Analysis

### Steelmanned Argument
Attractor’s spec-only form factor is a rational interface for coding agents: it is compact, readable, and directly consumable. If the ultimate governance mechanism is scenarios/harnesses, then distributing specs rather than code is sensible—code can be regenerated as long as the harness ensures correctness. In that world, the engineer’s work becomes building and maintaining the harness and the agentic loop.

### Strongest Counterarguments
1. **Specs are incomplete**: many requirements are tacit; without human judgment, scenario suites may miss critical edges.
2. **Security/compliance**: spec-only pipelines still need provenance and audit; “no review” is often unacceptable.
3. **Economic inefficiency**: regenerating code repeatedly can be wasteful and unstable under changing dependencies.

### Supporting Theories

| Theory/Framework | Source ID | How It Supports |
|------------------|-----------|-----------------|
| Harness-governed non-interactive loops | `strongdm-2026-software-factory-principles` | Provides the explicit seed→harness→feedback loop with holdout criterion |

### Contradicting Theories

| Theory/Framework | Source ID | Point of Conflict |
|------------------|-----------|------------------|
| Orchestration bottleneck and “code distance” | `appleton-2026-gastown-agent-patterns` | Suggests human closeness to code is a design axis; spec-only may not dominate |

### Synthesis Notes
Willison’s key contribution is making the “dark factory” concrete via a public artifact (Attractor specs). It is one of the clearest publicly inspectable examples of a “code is disposable; specs + harness are primary” posture.

### Claims to Cross-Reference
- TECH-2026-978: watch whether Attractor evolves into a code repo or remains a spec-only interface.
- TRANS-2026-019: track whether “agent harness engineer” roles emerge as distinct job categories.

### Claim Summary

| ID | Type | Domain | Evidence | Credence | Claim |
|----|------|--------|----------|----------:|-------|
| TECH-2026-978 | [F] | TECH | E2 | 0.90 | `strongdm/attractor` publishes spec-only artifacts and instructs agent-based implementation |
| INST-2026-914 | [T] | INST | E5 | 0.60 | Spec + scenarios become primary governance artifacts; code becomes intermediate output |
| TRANS-2026-019 | [H] | TRANS | E5 | 0.55 | Engineers shift from writing code to building/monitoring code-generating systems |

### Claims to Register

```yaml
claims:
  - id: "TECH-2026-978"
    text: >-
      The `strongdm/attractor` repository contains no implementation code and instead publishes natural-language
      specifications (Markdown) plus instructions to implement Attractor using a modern coding agent.
    type: "[F]"
    domain: "TECH"
    evidence_level: "E2"
    credence: 0.90
    source_ids: ["willison-2026-strongdm-software-factory"]
    operationalization: >-
      Periodically snapshot repo contents and diff file types/structure; classify whether it remains “spec-only”
      or evolves into an implementation.
    assumptions:
      - GitHub snapshots accurately reflect the intended public artifact.
    falsifiers:
      - Repository evolves into a conventional code implementation with specs as ancillary.

  - id: "INST-2026-914"
    text: >-
      In “software factory” workflows, natural-language specs and validation scenarios become the primary
      governance surface, while code becomes an intermediate artifact produced (and potentially regenerated)
      by agents.
    type: "[T]"
    domain: "INST"
    evidence_level: "E5"
    credence: 0.60
    source_ids: ["willison-2026-strongdm-software-factory"]
    operationalization: >-
      Observe organizations adopting spec-driven agent loops and measure artifact primacy: what gets reviewed,
      versioned, and used for acceptance (specs/scenarios vs code diffs).
    assumptions:
      - Specs/scenarios can be kept aligned with actual system behavior.
    falsifiers:
      - Code review and manual debugging remain the dominant governance mechanism even in agent-heavy teams.

  - id: "TRANS-2026-019"
    text: >-
      As agentic “dark factory” workflows mature, software engineers will increasingly shift from writing code
      to building and semi-monitoring the systems (harnesses, loops, tooling) that generate code.
    type: "[H]"
    domain: "TRANS"
    evidence_level: "E5"
    credence: 0.55
    source_ids: ["willison-2026-strongdm-software-factory"]
    operationalization: >-
      Track job postings and internal role definitions over 2026–2028 for growth in “agent harness/orchestration”
      roles and declining share of roles centered on manual implementation.
    assumptions:
      - Autonomy and validation tooling improve enough to make monitoring/harness roles valuable.
    falsifiers:
      - No meaningful labor-market shift occurs despite continued improvements in agentic coding tools.
```

---

**Analysis Date**: 2026-02-09
**Analyst**: gpt-5.2
**Credence in Analysis**: 0.70

**Credence Reasoning**:
- High confidence on verifiable artifact claims (Attractor repo structure).
- Moderate confidence on extrapolations about governance surfaces and labor transitions.

## Analysis Log

| Pass | Date | Tool | Model | Duration | Tokens | Cost | Notes |
|------|------|------|-------|----------|--------|------|-------|
| 1 | 2026-02-09 | codex | gpt-5.2 | ? | ? | ? | Initial 3-stage analysis + extracted claims; imported to DB. |

### Revision Notes

**Pass 1**: Initial 3-stage analysis + extracted claims.
