# Source Analysis: matplotlib/matplotlib Issue #31130 — `column_stack` vs `vstack().T` performance

> **Claim types**: `[F]` fact, `[T]` theory, `[H]` hypothesis, `[P]` prediction, `[A]` assumption, `[C]` counterfactual, `[S]` speculation, `[X]` contradiction  
> **Evidence**: **E1** systematic review/meta-analysis; **E2** peer-reviewed/official stats / primary logs; **E3** expert consensus/preprint; **E4** credible journalism/industry; **E5** opinion/anecdote; **E6** unsupported/speculative

## Metadata

| Field | Value |
|-------|-------|
| **Source ID** | matplotlib-2026-issue-31130-column-stack-vstack-perf |
| **Title** | Issue #31130: “[MNT] Switch from `np.column_stack()` to `np.vstack().T` for performance” |
| **Author(s)** | Scott Shambaugh (issue opener) + commenters |
| **Date** | 2026-02-10 |
| **Type** | CONVO (GitHub issue thread) |
| **URL** | https://github.com/matplotlib/matplotlib/issues/31130 |
| **Captured Artifact** | `reference/captured/mjrathburn/github/matplotlib_matplotlib_issue_31130_thread.md` |
| **Reliability** | 0.85 |
| **Rigor Level** | REVIEWED |

## Stage 1: Descriptive Analysis

### Core Thesis
This issue proposes a broad micro-optimization across Matplotlib: replacing certain uses of `np.column_stack()` with `np.vstack().T` on the claim that `column_stack` is slower due to interleaving memory, while `vstack().T` uses contiguous copies and returns a view. The thread then evaluates whether the performance story is consistent and worth touching the codebase broadly, and it contextualizes the issue as an “easy first issue” intended for human onboarding (not autonomous bot work).

### Key Claims

| # | Claim | Claim ID | Layer | Actor | Scope | Quantifier | Type | Domain | Evid | Credence | Verified? | Falsifiable By |
|---|-------|----------|-------|-------|-------|------------|------|--------|------|----------|-----------|----------------|
| 1 | Matplotlib issue `#31130` was opened on 2026-02-10 as a “good first issue” proposing `column_stack`→`vstack().T` changes for performance, and it included benchmark results supporting a speedup in some scenarios. | INST-2026-921 | ASSERTED | OTHER:matplotlib maintainers | who=matplotlib; where=GitHub issues; when=2026-02-10; object=np.column_stack vs np.vstack().T | N/A | [F] | INST | E2 | 0.95 | URL | GitHub issue metadata/body differs materially from the captured snapshot. |
| 2 | A maintainer hid an automatically generated comment from a bot account (@AiGentsy), noting the issue was low priority and better for human contributors learning to contribute. | INST-2026-922 | PRACTICED | OTHER:matplotlib maintainer | who=maintainer; where=GitHub issue; when=2026-02-10; action=hide bot comment | N/A | [F] | INST | E2 | 0.90 | URL | GitHub issue moderation log / comment history contradicts. |
| 3 | Maintainers concluded the performance gains were not consistent/compelling enough to justify broad find-and-replace work, and the issue was closed with guidance to focus on hot spots / better benchmarking. | INST-2026-923 | PRACTICED | OTHER:matplotlib maintainers | who=maintainers; where=GitHub issue; when=2026-02-11; action=close issue / discourage PRs | N/A | [F] | INST | E2 | 0.85 | URL | Issue remained open or closure rationale materially differs. |

### Argument Structure

```
`column_stack` may be slower than `vstack().T` in some cases
  → propose broad replacement
  → test/benchmark across sizes/contexts
  → conclude gains are mixed + micro-optimization is fragile
  → prefer targeted hotspots + better perf testing
```

### Theoretical Lineage
- **Performance engineering**: microbenchmarks are workload-, hardware-, and version-dependent; “faster primitive” ≠ end-to-end win.
- **OSS governance**: “good first issue” as a human onboarding mechanism; maintainers ration review attention.

### Scope & Limitations
- This is a thread snapshot, not an official policy document.
- Benchmarks are illustrative, not a controlled cross-platform study.
- “AI policy” is adjacent in the thread’s moderation context but not the dominant technical topic.

## Stage 2: Evaluative Analysis

### Internal Coherence
The thread is coherent: it starts with a plausible mechanism (“interleaving vs contiguous copies”), then quickly runs into measurement variance across array sizes and environments, yielding a conservative decision to avoid broad code churn without stronger evidence.

### Key Factual Claims Verified

| Claim ID | Claim (paraphrased) | Crux? | Source Says | Actual | External Source | Search Notes | Status |
|----------|---------------------|-------|-------------|--------|-----------------|-------------|--------|
| INST-2026-921 | Issue #31130 exists, with described title/body and dates | **Y** | GitHub issue thread snapshot | Matches live issue metadata/title; created 2026-02-10 | https://github.com/matplotlib/matplotlib/issues/31130 | q1 “matplotlib 31130 column_stack vstack”; q2 “site:github.com matplotlib issue 31130”; checked 2026-02-20 | ok |

### Disconfirming Evidence Search

| Claim | Counterevidence Found | Alternative Explanation | Search Notes |
|-------|----------------------|-------------------------|--------------|
| “Broad replacement yields meaningful wins” (implied) | Thread itself shows mixed results and historical NumPy measurements that reversed direction | Access patterns, cache effects, NumPy/Python/CPU differences dominate; optimization should be targeted and benchmarked | Looked for “numpy column_stack vstack performance” + “matplotlib mpl-bench column_stack” (2026-02-20) |

### Corrections & Updates
No corrections identified in the captured snapshot itself. (Any later edits to the issue thread were not audited in depth in this pass.)

### Internal Tensions / Self-Contradictions
None salient: the thread explicitly acknowledges benchmark variance and avoids overstating.

### Persuasion Techniques
Primarily technical argumentation; little rhetorical framing beyond “easy first issue” context-setting.

### Unstated Assumptions

| Assumption | Claim ID | Critical? | Problematic? |
|------------|----------|-----------|--------------|
| Microbenchmarks in isolation predict real Matplotlib workload wins | INST-2026-921 | Y | Y |

### Evidence Assessment
Strong for the *existence* and *content* of the thread (primary logs). Weak for generalizing performance impacts beyond what’s measured.

### Credence Assessment
- **Overall Credence**: 0.85 that the issue thread accurately reflects maintainers’ reasoning and decisions at the time.

## Stage 3: Dialectical Analysis

### Steelmanned Argument
Even modest wins in a frequently executed primitive can accumulate. If a replacement is proven safe in specific sites and is backed by benchmark coverage across supported platforms, targeted changes can be worth it.

### Strongest Counterarguments
1. Broad replacements risk semantic edge cases and churn without robust, workload-relevant benchmarking.
2. Micro-optimizations are brittle across versions/hardware; time is better spent on algorithmic or duplication-elimination wins.

### Supporting Theories

| Theory/Framework | Source ID | How It Supports |
|------------------|-----------|-----------------|
| “Verification is the bottleneck” in OSS | ronacher-2026-agent-psychosis | Maintainers ration review capacity; cheap changes can still be expensive to validate |

### Contradicting Theories

| Theory/Framework | Source ID | Point of Conflict |
|------------------|-----------|------------------|
| “Always take cheap wins” micro-optimization doctrine | N/A | This thread argues “cheap” wins often aren’t durable or clearly positive |

### Synthesis Notes
The issue is best treated as a case study of performance-tradeoff ambiguity and review-capacity constraints, which become sharper under automated contribution pressure.

### Claims to Cross-Reference
- INST-2026-924 / INST-2026-925 (PR #31132 closure and policy rationale)

---

### Claim Summary

| ID | Type | Domain | Layer | Actor | Scope | Quantifier | Evidence | Credence | Claim |
|----|------|--------|-------|-------|-------|------------|----------|----------|-------|
| INST-2026-921 | [F] | INST | ASSERTED | OTHER:matplotlib maintainers | who=matplotlib; where=GitHub issues; when=2026-02-10; object=np.column_stack vs np.vstack().T | N/A | E2 | 0.95 | Issue #31130 proposed `column_stack`→`vstack().T` replacements for performance and included benchmarks. |
| INST-2026-922 | [F] | INST | PRACTICED | OTHER:matplotlib maintainer | who=maintainer; where=GitHub issue; when=2026-02-10; action=hide bot comment | N/A | E2 | 0.90 | A maintainer hid an automatically generated comment from a bot account on the issue. |
| INST-2026-923 | [F] | INST | PRACTICED | OTHER:matplotlib maintainers | who=maintainers; where=GitHub issue; when=2026-02-11; action=close issue / discourage PRs | N/A | E2 | 0.85 | Maintainers closed the issue and discouraged PRs absent stronger benchmark evidence. |

### Claims to Register

```yaml
claims:
  - id: "INST-2026-921"
    text: "Matplotlib issue #31130 was opened on 2026-02-10 as a “good first issue” proposing certain `np.column_stack()` uses be replaced with `np.vstack().T` for performance, and it included benchmark results suggesting speedups in some scenarios."
    type: "[F]"
    domain: "INST"
    evidence_level: "E2"
    credence: 0.95
    operationalization: "Check the live GitHub issue body/metadata and compare to the archived thread snapshot."
    assumptions: ["GitHub thread snapshots reflect the state at capture time."]
    falsifiers: ["Issue metadata/body materially differs from the archived snapshot."]
    source_ids: ["matplotlib-2026-issue-31130-column-stack-vstack-perf"]
  - id: "INST-2026-922"
    text: "A Matplotlib maintainer hid an automatically generated comment from a bot account on issue #31130, stating the task was low priority and better for human contributors to learn with."
    type: "[F]"
    domain: "INST"
    evidence_level: "E2"
    credence: 0.9
    operationalization: "Review the issue thread for the maintainer comment describing the hidden bot comment."
    assumptions: ["The captured thread includes hidden-comment annotation context."]
    falsifiers: ["Thread history shows no such maintainer comment or contradicts the claim."]
    source_ids: ["matplotlib-2026-issue-31130-column-stack-vstack-perf"]
  - id: "INST-2026-923"
    text: "Matplotlib maintainers concluded broad `column_stack`→`vstack().T` changes were not compelling or durable enough without stronger benchmarking, and they closed issue #31130 on 2026-02-11."
    type: "[F]"
    domain: "INST"
    evidence_level: "E2"
    credence: 0.85
    operationalization: "Check issue state/closure date and closure comments."
    assumptions: ["Issue state and timestamps are accurately recorded by GitHub."]
    falsifiers: ["Issue remained open or closure rationale differs materially."]
    source_ids: ["matplotlib-2026-issue-31130-column-stack-vstack-perf"]
```

**Analysis Date**: 2026-02-20  
**Analyst**: gpt-5.2 (Codex CLI)  
**Credence in Analysis**: 0.80

## Analysis Log

| Pass | Date | Tool | Model | Duration | Tokens | Cost | Notes |
|------|------|------|-------|----------|--------|------|-------|
| 1 | 2026-02-20 | codex-cli | gpt-5.2 | — | — | — | Initial analysis from captured GitHub thread + light live verification |

