# Source Analysis: "The Impact of AI on Developer Productivity: Evidence from GitHub Copilot" — Peng et al. (2023)

> **Claim types**: `[F]` fact, `[T]` theory, `[H]` hypothesis, `[P]` prediction, `[A]` assumption, `[C]` counterfactual, `[S]` speculation, `[X]` contradiction
> **Evidence**: **E1** systematic review/meta-analysis; **E2** peer-reviewed/official stats; **E3** expert consensus/preprint; **E4** credible journalism/industry; **E5** opinion/anecdote; **E6** unsupported/speculative


## Metadata

- **Source ID**: peng-2023-copilot-productivity
- **Author(s)**: Sida Peng; Eirini Kalliamvakou; Peter Cihon; Mert Demirer
- **Date**: 2023-02-13
- **Type**: PAPER (arXiv preprint)
- **URL**: https://arxiv.org/abs/2302.06590v1
- **Reliability**: 0.75
- **Rigor Level**: [REVIEWED]
- **Media Artifacts**: PDF (arXiv)

> **Evidence Strength (E-level)**: E1=Strong empirical (replicated) | E2=Moderate empirical | E3=Strong theoretical | E4=Weak theoretical | E5=Opinion/forecast | E6=Unsupported assertion

## Stage 1: Descriptive Analysis
### Core Thesis

The authors report a randomized controlled trial measuring the effect of GitHub Copilot (an “AI pair programmer”) on software-development task completion time. In a single programming task (implementing an HTTP server in JavaScript), participants with access to Copilot completed the task substantially faster than those without.

### Study Design (as described)

- Randomized assignment into control vs treatment.
- 95 professional programmers recruited via Upwork (May–June 2022).
- Task: implement an HTTP server in JavaScript; both groups could use internet search/Stack Overflow; treatment group additionally had Copilot access and brief onboarding.

### Key Claims

| # | Claim | Claim ID | Type | Domain | Evid | Conf | Verified? | Falsifiable By |
|---|-------|----------|------|--------|------|------|-----------|----------------|
| 1 | In a controlled experiment, Copilot users completed the task 55.8% faster than the control group (95% CI: 21–89%) | LABOR-2023-001 | [F] | LABOR | E2 | 0.90 | ✓ | Re-analysis shows statistical/measurement error; replication shows materially smaller or null effect |
| 2 | Copilot’s productivity gains were larger for less-experienced developers, older programmers, and those who program more hours/day | LABOR-2023-002 | [F] | LABOR | E2 | 0.70 | ✓ | Re-analysis shows heterogeneity claims not supported; replication fails to find these subgroup patterns |

### Notes on Interpretation

- The headline effect is on a specific task, language, and setting; generalization to broader SWE work is plausible but not established by this single experiment.
- Authors include Microsoft Research and GitHub employees, which raises conflict-of-interest risk; however, the design is described as randomized and approved by an ethics review board.

### Argument Structure

```
[Premise 1]
    +
[Premise 2]
    ↓
[Conclusion]
```

### Theoretical Lineage

- **Builds on**: [prior work/theories]
- **Departs from**: [rejected approaches]
- **Novel contribution**: [what's new here]

## Stage 2: Evaluative Analysis
### Evidence Quality

- The core result is supported by a randomized controlled experiment (E2), with reported confidence intervals.
- Limitations: single task; relatively small sample; short time horizon; uncertain representativeness of tasks and environments; potential experimenter/participant effects.

### Key Uncertainties / Risks

- Does the measured speedup persist for multi-day tasks with larger codebases, integration, and review/QA constraints?
- Does faster completion trade off against defects/security, or do quality effects net out as positive/neutral?
- How much of the effect is “novelty” or “tooling acclimation” dependent?

### Key Factual Claims Verified

| Claim | Verification Source | Status | Notes | Crux? |
|-------|---------------------|--------|-------|-------|
| [claim] | [source] | ✓/✗/? | [notes] | Y/N |


### Disconfirming Evidence Search

| Claim | Counter-Evidence Sought | Found? | Impact |
|-------|------------------------|--------|--------|
| [claim] | [what would disprove] | Y/N | [if found, how does it affect credence?] |


### Internal Tensions

| Tension | Claims Involved | Resolution Possible? |
|---------|-----------------|---------------------|
| [description] | [IDs] | [Y/N + how] |


### Persuasion Techniques

| Technique | Example | Effect on Analysis |
|-----------|---------|-------------------|
| [e.g., appeal to authority] | [quote/reference] | [how to adjust for this] |


### Unstated Assumptions

| Assumption | Required For | If False |
|------------|--------------|----------|
| [hidden premise] | [which claims depend on this] | [impact on argument] |


## Stage 3: Dialectical Analysis
### Steelmanned Argument
Even early-generation LLM-based coding assistants can deliver large, measurable productivity improvements on realistic programming tasks under controlled conditions. This supports the view that “AI for code” is not merely hype: it has near-term, economically relevant labor-productivity impact, with potential to reshape how software is produced.

### Strongest Counterarguments
- The task may be unusually suited to Copilot-style autocomplete and boilerplate generation; real-world engineering time is often dominated by problem understanding, debugging, integration, and coordination.
- An RCT on Upwork participants may not generalize to in-house teams, regulated domains, or high-reliability systems.
- The paper measures speed more than downstream outcomes (maintainability, security, long-run defect rate).

### Supporting Theories

| Theory/Source | How It Supports | Claim IDs Affected |
|---------------|-----------------|-------------------|
| [theory] | [mechanism] | [IDs] |


### Contradicting Theories

| Theory/Source | How It Contradicts | Claim IDs Affected |
|---------------|-------------------|-------------------|
| [theory] | [mechanism] | [IDs] |


### Claim Summary


| ID | Type | Domain | Evidence | Credence | Claim |
|----|------|--------|----------|----------:|-------|
| LABOR-2023-001 | [F] | LABOR | E2 | 0.90 | In a controlled experiment (May–Jun 2022) with 95 professional developers, the group with access to GitHub Copilot completed an HTTP-server implementation task in JavaScript 55.8% faster than the control group (95% CI: 21–89%). |
| LABOR-2023-002 | [F] | LABOR | E2 | 0.70 | In the same experiment, Copilot’s measured productivity gains were larger for less-experienced developers, older programmers, and those who program more hours per day. |

### Claims to Register


```yaml
claims:
  - id: "LABOR-2023-001"
    text: >-
      In a controlled experiment (May–Jun 2022) with 95 professional developers, the group
      with access to GitHub Copilot completed an HTTP-server implementation task in
      JavaScript 55.8% faster than the control group (95% CI: 21–89%).
    type: "[F]"
    domain: "LABOR"
    evidence_level: "E2"
    credence: 0.90
    source_ids: ["peng-2023-copilot-productivity"]
    operationalization: >-
      Replicate with randomized assignment across multiple programming tasks, languages,
      and environments; compare time-to-completion distributions and quality metrics.
    falsifiers:
      - Re-analysis finds measurement/statistical errors that eliminate the effect.
      - Replications across tasks show materially smaller or null time savings.

  - id: "LABOR-2023-002"
    text: >-
      In the same experiment, Copilot’s measured productivity gains were larger for
      less-experienced developers, older programmers, and those who program more hours per
      day.
    type: "[F]"
    domain: "LABOR"
    evidence_level: "E2"
    credence: 0.70
    source_ids: ["peng-2023-copilot-productivity"]
    operationalization: >-
      Estimate heterogeneous treatment effects with pre-registered subgroup analysis and
      replicate with larger samples to validate subgroup patterns.
    falsifiers:
      - Replications do not find the subgroup patterns or find opposite effects.
      - Re-analysis shows subgroup results are not robust to multiple-testing correction.
```

### Working Takeaway

Treat this as strong evidence of *task-level* productivity impact for AI coding assistants, but not decisive evidence of *economy-wide* effects or a guarantee of sustained long-run gains without complementary process changes (testing, review, QA automation, governance).

---

## Extracted Claims

- Import file: [`analysis/sources/peng-2023-copilot-productivity.yaml`](peng-2023-copilot-productivity.yaml)
---

**Analysis Date**: [YYYY-MM-DD]
**Analyst**: [human/claude/gpt/etc.]
**Credence in Analysis**: [0.0-1.0]

**Credence Reasoning**:
- [Why this credence level?]
- [What would increase/decrease credence?]
- [Key uncertainties remaining]
