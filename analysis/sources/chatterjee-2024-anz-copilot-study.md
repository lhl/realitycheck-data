# Source Analysis: "The Impact of AI Tool on Engineering at ANZ Bank" — Chatterjee et al. (2024)

> **Claim types**: `[F]` fact, `[T]` theory, `[H]` hypothesis, `[P]` prediction, `[A]` assumption, `[C]` counterfactual, `[S]` speculation, `[X]` contradiction
> **Evidence**: **E1** systematic review/meta-analysis; **E2** peer-reviewed/official stats; **E3** expert consensus/preprint; **E4** credible journalism/industry; **E5** opinion/anecdote; **E6** unsupported/speculative


## Metadata

- **Source ID**: chatterjee-2024-anz-copilot-study
- **Author(s)**: Sayan Chatterjee; Ching Louis Liu; Gareth Rowland; Tim Hogarth
- **Date**: 2024-02-08
- **Type**: PAPER (arXiv preprint)
- **URL**: https://arxiv.org/abs/2402.05636v2
- **Reliability**: 0.70
- **Rigor Level**: [REVIEWED]
- **Media Artifacts**: PDF (arXiv)

> **Evidence Strength (E-level)**: E1=Strong empirical (replicated) | E2=Moderate empirical | E3=Strong theoretical | E4=Weak theoretical | E5=Opinion/forecast | E6=Unsupported assertion

## Stage 1: Descriptive Analysis
### Core Thesis

The paper reports an organizational case study and experiment on adopting GitHub Copilot at ANZ Bank. It evaluates impacts on (a) productivity (time spent on programming challenges), (b) code quality (unit test success), (c) security (static analysis vulnerabilities), and (d) engineer sentiment.

### Study Design (as described)

- Six-week program: ~2 weeks of preparation + ~4 weeks of “A/B testing” style evaluation.
- Participants split into control vs Copilot groups for Python coding challenges.
- Measures: time spent; unit test results; SonarQube security findings; surveys.

### Key Claims

| # | Claim | Claim ID | Type | Domain | Evid | Conf | Verified? | Falsifiable By |
|---|-------|----------|------|--------|------|------|-----------|----------------|
| 1 | In ANZ’s experiment, Copilot users completed the coding challenges ~42.36% faster on average than the control group | LABOR-2024-001 | [F] | LABOR | E2 | 0.85 | ✓ | Re-analysis finds calculation or selection errors; replication fails to show comparable time reduction |
| 2 | Copilot-group solutions had ~12.86% higher unit test success ratio, but the difference was not statistically significant | LABOR-2024-002 | [F] | LABOR | E2 | 0.70 | ✓ | Re-analysis finds the unit-test result is incorrect or reverses; larger-sample replication shows no difference |

### Notes on Interpretation

- This is a single-org study and may not generalize across domains, team practices, or tool configurations.
- As a case study by ANZ employees, conflict-of-interest/bias is possible; nevertheless, it includes concrete measured outcomes and statistical testing claims.

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

- Measures are empirical and task-based (E2), but depend on how comparable the tasks are to real production work and whether “time spent on challenge problems” transfers to end-to-end engineering throughput.
- Quality and security results appear mixed/inconclusive in the paper (e.g., unit test improvement not statistically significant; insufficient data to conclude on vulnerabilities in at least one measure).

### Key Uncertainties / Risks

- Whether observed speedups persist with realistic codebases, integration work, and review/QA constraints.
- Whether time savings trade off against maintainability or defect rates in production contexts.
- Potential selection bias in who participated and how tasks were structured.

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
Alongside controlled trials, in-the-wild organizational evaluations can show substantial productivity gains from AI coding assistants. This supports treating AI-assisted coding as an economically meaningful productivity technology (even if the broader AI investment cycle includes bubble dynamics).

### Strongest Counterarguments
- Task benchmarks may overestimate net productivity in real codebases where verification/review and coordination dominate.
- “Percentage faster” on challenge problems may not translate linearly to delivered product value.

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
| LABOR-2024-001 | [F] | LABOR | E2 | 0.85 | In ANZ Bank’s Copilot experiment, the Copilot group completed the coding challenges about 42.36% faster on average than the control group (based on mean time spent per problem). |
| LABOR-2024-002 | [F] | LABOR | E2 | 0.70 | In ANZ Bank’s Copilot experiment, Copilot-group solutions had about a 12.86% higher unit test success ratio than control-group solutions, but the difference was not statistically significant. |

### Claims to Register


```yaml
claims:
  - id: "LABOR-2024-001"
    text: >-
      In ANZ Bank’s Copilot experiment, the Copilot group completed the coding challenges
      about 42.36% faster on average than the control group (based on mean time spent per
      problem).
    type: "[F]"
    domain: "LABOR"
    evidence_level: "E2"
    credence: 0.85
    source_ids: ["chatterjee-2024-anz-copilot-study"]
    operationalization: >-
      Replicate A/B evaluations across organizations and task suites; use pre-registered
      metrics and compare time-to-completion and downstream quality outcomes.
    falsifiers:
      - Re-analysis finds calculation/selection errors that invalidate the reported speedup.
      - Replications in comparable settings show no meaningful time reduction.

  - id: "LABOR-2024-002"
    text: >-
      In ANZ Bank’s Copilot experiment, Copilot-group solutions had about a 12.86% higher
      unit test success ratio than control-group solutions, but the difference was not
      statistically significant.
    type: "[F]"
    domain: "LABOR"
    evidence_level: "E2"
    credence: 0.70
    source_ids: ["chatterjee-2024-anz-copilot-study"]
    operationalization: >-
      Compare defect/quality metrics (unit tests, static analysis, review outcomes) under
      controlled conditions with sufficient sample sizes to detect moderate effects.
    falsifiers:
      - Re-analysis finds the unit-test result is incorrect or reverses direction.
      - Replications consistently show no difference or worse quality for Copilot-assisted code.
```

### Working Takeaway

This is supportive but not definitive evidence that AI coding assistants can raise software engineering throughput in corporate settings; strongest use is as convergent evidence alongside controlled trials (e.g., `LABOR-2023-001`).

---

## Extracted Claims

- Import file: [`analysis/sources/chatterjee-2024-anz-copilot-study.yaml`](chatterjee-2024-anz-copilot-study.yaml)
---

**Analysis Date**: [YYYY-MM-DD]
**Analyst**: [human/claude/gpt/etc.]
**Credence in Analysis**: [0.0-1.0]

**Credence Reasoning**:
- [Why this credence level?]
- [What would increase/decrease credence?]
- [Key uncertainties remaining]
