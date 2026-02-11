# Source Analysis: Reality Check framework development velocity and codebase size (v0.3.0 snapshot)

> **Claim types**: `[F]` fact, `[T]` theory, `[H]` hypothesis, `[P]` prediction, `[A]` assumption, `[C]` counterfactual, `[S]` speculation, `[X]` contradiction  
> **Evidence**: **E1** systematic review/meta-analysis; **E2** official stats/law/code+tests; **E3** preprint/working paper w/ methods; **E4** credible journalism/industry; **E5** opinion/anecdote/expert judgment; **E6** unsupported/speculative

## Metadata

| Field | Value |
|---|---|
| **Source ID** | `lhl-2026-realitycheck-dev-velocity` |
| **Title** | Reality Check framework: development velocity and codebase size (v0.3.0 snapshot) |
| **Author(s)** | lhl |
| **Date** | 2026-02-01 (tag `v0.3.0`) |
| **Type** | REPORT |
| **URL** | https://github.com/lhl/realitycheck/tree/v0.3.0 |
| **Reliability** | 0.80 |
| **Rigor Level** | [REVIEWED] |
| **Bias Notes** | Self-analysis of a public repository’s git history and scc output to bound an upper tail of software development throughput. Strong for the raw measurements (git history, churn, scc snapshot); weak for causal attribution (how much was due to AI vs reuse/scope choices) and for generalization to typical projects and workflows. |

**Claims YAML**: [`analysis/sources/lhl-2026-realitycheck-dev-velocity.yaml`](lhl-2026-realitycheck-dev-velocity.yaml)

## Stage 1: Descriptive Analysis

### Core Thesis
The Reality Check framework repository’s public git history and `scc` snapshot at tag `v0.3.0` show a large amount of shipped artifact (code + docs + templates + tests) produced within a short calendar window. This is best treated as an **upper-tail case study**: evidence that very high delivery velocity is *possible* in some greenfield projects (especially with strong tooling/specification and (likely) AI assistance), not evidence that the median effect is large.

### What This Source Is (and isn’t)
- **Is**: reproducible measurements of repository size/churn and commit timing.
- **Isn’t**: a controlled experiment of AI vs non-AI development, and does not provide a counterfactual baseline.

### Key Claims

| # | Claim | Claim ID | Type | Domain | Evidence | Credence | Verified? | Falsifiable By |
|---:|---|---|---|---|---|---:|---|---|
| 1 | Repo history through `v0.3.0` spans 2026-01-20 → 2026-02-01 and contains 160 commits | LABOR-2026-029 | [F] | LABOR | E2 | 0.95 | In-source | Recomputing from repo history yields different dates/commit count |
| 2 | At `v0.3.0`, `scc` reports ~45,920 total lines (179 files) and estimates ~14.54 months COCOMO schedule effort | LABOR-2026-030 | [F] | LABOR | E2 | 0.90 | In-source | Running `scc` at tag yields materially different totals/estimate |
| 3 | Comparing the ~12-day window to the ~14.5-month COCOMO estimate suggests order-of-magnitude compression is plausible in some greenfield projects (non-causal; baseline uncertainty high) | LABOR-2026-031 | [H] | LABOR | E5 | 0.60 | ? | Repeated case studies show such comparisons are systematically misleading |

### Argument Structure

```
[Observed repo size + churn at v0.3.0]
    ↓
[Short calendar window from first commit → tag]
    ↓
[Conclusion: very high delivery velocity is possible (upper tail), but causality + generalization are uncertain]
```

### Scope & Limitations
- `scc` COCOMO is a heuristic baseline; it is not a validated estimate for every project type and may overestimate for small, focused systems.
- A “commit window” is not the same as labor time; it includes planning, reuse, and can include large initial commits.
- This source does **not** establish how much of the speed came from AI vs from scope selection, reuse, prior expertise, or other factors.

## Stage 2: Evaluative Analysis

### Key Factual Claims Verified

| Claim (paraphrased) | Crux? | Source Says | Actual | External Source | Status |
|---|---:|---|---|---|---|
| `v0.3.0` tag date and first commit date imply ~12-day window; total commits through tag is 160 | **Y** | `v0.3.0` tagged 2026-02-01; first commit 2026-01-20; 160 commits | Recomputed via git: first commit 2026-01-20; `v0.3.0` tag 2026-02-01; `git rev-list --count v0.3.0` = 160 | https://github.com/lhl/realitycheck/tree/v0.3.0 | ok |
| `scc` at `v0.3.0` reports ~45,920 total lines and ~14.54 months COCOMO schedule | **Y** | `scc` snapshot | Recomputed using `scc` on an archived `v0.3.0` checkout: 45,920 total lines; schedule effort 14.54 months | https://github.com/lhl/realitycheck/tree/v0.3.0 | ok |

### Disconfirming Evidence Search (Contextual)

| Claim | Counterevidence Found | Alternative Explanation | Search Notes |
|---|---|---|---|
| LABOR-2026-031 (order-of-magnitude compression plausible) | METR reports a realistic OSS study where AI access slowed experienced devs on average; NBER reports modest average time savings in a representative setting | Upper-tail velocity may be real but rare; distributions could be heavy-tailed; some workflows slow down due to verification/coordination overhead | Triangulated against `metr-2025-ai-experienced-os-dev-productivity` and `humlum-2025-llms-small-labor-market-effects` |

### Evidence Assessment
- **Strong** for raw facts (git dates, commit counts, `scc` output).
- **Weak-to-moderate** for any causal claim (“AI caused this speed”) or for generalization beyond similar greenfield/tooling/spec contexts.

### Credence Assessment
- **Overall Credence**: 0.75  
- **Reasoning**: the measured repository facts are high credence; the inference from COCOMO-to-calendar comparison is directionally informative but noisy.

## Stage 3: Dialectical Analysis

### Steelmanned Argument
Some modern software efforts can be substantially accelerated by (a) strong spec artifacts, (b) high automation in scaffolding/tests, and (c) AI coding assistance—producing “months of artifact” in a week-scale calendar window. These upper-tail successes can then shift organizational expectations and norms, contributing to intensification and burnout dynamics downstream.

### Strongest Counterarguments
1. **Baseline mismatch**: COCOMO/scc estimates may be wildly off for this kind of repo, so “order-of-magnitude” comparisons can be misleading.
2. **Selection bias**: greenfield projects, highly motivated leads, and reusable templates are not representative of typical org work.
3. **Hidden work**: “commit window” excludes earlier preparation, prior expertise, and invisible labor.

### Supporting Theories

| Theory/Framework | Source ID | How It Supports |
|---|---|---|
| Outlier narratives can set unrealistic standards and intensify expectations | `yegge-2026-ai-vampire` | Upper-tail velocity makes “unrealistic beauty standards” more salient as a mechanism |

### Contradicting Theories

| Theory/Framework | Source ID | Point of Conflict |
|---|---|---|
| AI can slow down some realistic dev work on average | `metr-2025-ai-experienced-os-dev-productivity` | Suggests that “large speedups” are not universal and may depend on context and measurement choices |

### Synthesis Notes
This source is best used to support a **distributional framing**: even if the median productivity effect is modest (or negative in some contexts), the upper tail can be large enough to move expectations, shift staffing plans, and trigger “value capture” conflicts.

---

### Claim Summary

| ID | Type | Domain | Evidence | Credence | Claim |
|---|---|---|---|---:|---|
| LABOR-2026-029 | [F] | LABOR | E2 | 0.95 | Repo history through `v0.3.0` spans 2026-01-20 → 2026-02-01 with 160 commits |
| LABOR-2026-030 | [F] | LABOR | E2 | 0.90 | `scc` at `v0.3.0`: ~45,920 total lines (179 files); ~14.54 months COCOMO schedule |
| LABOR-2026-031 | [H] | LABOR | E5 | 0.60 | Comparing window vs COCOMO suggests order-of-magnitude compression is plausible (non-causal; baseline uncertainty high) |

### Claims to Register

```yaml
claims:
  - id: "LABOR-2026-029"
    text: >-
      The Reality Check framework repository (`lhl/realitycheck`) history through tag `v0.3.0` spans from its
      first commit dated 2026-01-20 to the `v0.3.0` tag dated 2026-02-01, and contains 160 commits.
    type: "[F]"
    domain: "LABOR"
    evidence_level: "E2"
    credence: 0.95
    source_ids: ["lhl-2026-realitycheck-dev-velocity"]
    operationalization: >-
      Recompute using `git show -s --format=%ci v0.3.0`, `git show -s --format=%ci $(git rev-list --max-parents=0 v0.3.0)`,
      and `git rev-list --count v0.3.0`.
    assumptions: []
    falsifiers:
      - Recomputing from the repository history yields materially different dates or commit count.

  - id: "LABOR-2026-030"
    text: >-
      At tag `v0.3.0`, `scc` reports the Reality Check framework codebase contains about 45,920 total lines across
      179 files, and estimates (COCOMO) a schedule effort of about 14.54 months (organic mode).
    type: "[F]"
    domain: "LABOR"
    evidence_level: "E2"
    credence: 0.90
    source_ids: ["lhl-2026-realitycheck-dev-velocity"]
    operationalization: >-
      Check out the `v0.3.0` tag in a detached worktree and run `scc .`; compare totals (lines/files) and the
      reported COCOMO schedule effort.
    assumptions:
      - The `scc` version and configuration are comparable across runs.
    falsifiers:
      - Running `scc` at the `v0.3.0` tag yields materially different totals or COCOMO schedule estimates.

  - id: "LABOR-2026-031"
    text: >-
      Comparing (a) the ~12-day calendar window from first commit to `v0.3.0` tag with (b) `scc`’s ~14.5-month
      COCOMO schedule estimate suggests that, in at least some greenfield software projects, delivery pace can be
      compressed by an order of magnitude relative to conventional baselines; this comparison is non-causal and
      COCOMO may overestimate for small, well-scoped projects.
    type: "[H]"
    domain: "LABOR"
    evidence_level: "E5"
    credence: 0.60
    source_ids: ["lhl-2026-realitycheck-dev-velocity"]
    operationalization: >-
      Compute (tag_date - first_commit_date) and compare to the COCOMO schedule-effort estimate. Evaluate
      sensitivity by repeating on other repos/projects and by using alternative baseline estimation methods.
    assumptions:
      - The COCOMO schedule estimate is a useful (even if noisy) baseline for rough comparison.
    falsifiers:
      - Repeated case studies find COCOMO is systematically miscalibrated such that the comparison does not
        indicate unusual delivery speed.
```

---
**Analysis Date**: 2026-02-11  
**Analyst**: gpt-5.2  
**Credence in Analysis**: 0.75

## Analysis Log

| Pass | Date | Tool | Model | Duration | Tokens | Cost | Notes |
|---:|---|---|---|---|---:|---:|---|
| 1 | 2026-02-11 09:55 | codex | gpt-5.2 | ? | ? | ? | Initial 3-stage analysis + imported source and claims |

### Revision Notes

**Pass 1**: Initial 3-stage analysis + imported source and claims
