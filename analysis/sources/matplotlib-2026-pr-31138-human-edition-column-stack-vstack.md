# Source Analysis: matplotlib/matplotlib PR #31138 — “HUMAN EDITION” follow-up

> **Claim types**: `[F]` fact, `[T]` theory, `[H]` hypothesis, `[P]` prediction, `[A]` assumption, `[C]` counterfactual, `[S]` speculation, `[X]` contradiction  
> **Evidence**: **E1** systematic review/meta-analysis; **E2** peer-reviewed/official stats / primary logs; **E3** expert consensus/preprint; **E4** credible journalism/industry; **E5** opinion/anecdote; **E6** unsupported/speculative

## Metadata

| Field | Value |
|-------|-------|
| **Source ID** | matplotlib-2026-pr-31138-human-edition-column-stack-vstack |
| **Title** | PR #31138: “[PERF] Replace np.column_stack with np.vstack().T (HUMAN EDITION)” |
| **Author(s)** | `bergutman` (PR author) + commenters |
| **Date** | 2026-02-12 |
| **Type** | CONVO (GitHub PR thread) |
| **URL** | https://github.com/matplotlib/matplotlib/pull/31138 |
| **Captured Artifact** | `reference/captured/mjrathburn/github/matplotlib_matplotlib_pr_31138_thread.md` |
| **Reliability** | 0.85 |
| **Rigor Level** | REVIEWED |

## Stage 1: Descriptive Analysis

### Core Thesis
This PR reframes the earlier bot-submitted performance change as a human-authored follow-up (“HUMAN EDITION”), but maintainers close the topic on technical grounds (optimization not worth it) and lock the thread to prevent further unproductive debate.

### Key Claims

| # | Claim | Claim ID | Layer | Actor | Scope | Quantifier | Type | Domain | Evid | Credence | Verified? | Falsifiable By |
|---|-------|----------|-------|-------|-------|------------|------|--------|------|----------|-----------|----------------|
| 1 | PR `#31138` was opened on 2026-02-12 by `bergutman` as a follow-up (“HUMAN EDITION”) to the earlier `column_stack`→`vstack().T` PR, and it was closed without merge the same day. | INST-2026-927 | PRACTICED | OTHER:matplotlib maintainers | who=matplotlib; where=GitHub PR; when=2026-02-12; action=close PR | N/A | [F] | INST | E2 | 0.95 | URL | GitHub PR metadata differs materially. |
| 2 | A maintainer concluded the optimization was not worth pursuing and locked the thread to stop further discussion. | INST-2026-928 | PRACTICED | OTHER:matplotlib maintainer | who=maintainer; where=PR comments; when=2026-02-12; action=lock thread | N/A | [F] | INST | E2 | 0.90 | URL | Thread remains unlocked or lacks the described maintainer comment. |

### Argument Structure

```
Human submits “safer/more targeted” variant
  → discussion focuses on behavior + policy spillover
  → maintainers decide technical win is not worth it
  → close + lock to reduce further social churn
```

### Theoretical Lineage
- **OSS moderation**: locking threads as a mechanism to cap coordination costs and avoid escalation.

### Scope & Limitations
- PR is not the origin of the incident; it is a follow-on that highlights spillover from the earlier PR.

## Stage 2: Evaluative Analysis

### Internal Coherence
The maintainer decision is consistent with the issue-thread conclusion: if the optimization is ambiguous or fragile, it is rational to close quickly and lock the thread once it becomes socially unproductive.

### Key Factual Claims Verified

| Claim ID | Claim (paraphrased) | Crux? | Source Says | Actual | External Source | Search Notes | Status |
|----------|---------------------|-------|-------------|--------|-----------------|-------------|--------|
| INST-2026-927 | PR #31138 exists and is a follow-up human PR closed same day | **Y** | PR thread snapshot | Matches PR metadata (created/closed 2026-02-12) | https://github.com/matplotlib/matplotlib/pull/31138 | q1 “matplotlib 31138 human edition”; q2 “site:github.com matplotlib pull 31138”; checked 2026-02-20 | ok |

### Disconfirming Evidence Search

| Claim | Counterevidence Found | Alternative Explanation | Search Notes |
|-------|----------------------|------------------------|--------------|
| “Optimization is not worth it” | Counterevidence would require workload-level benchmarks showing consistent wins | Maintainers may be minimizing social conflict, using technical ambiguity as a closure point | Reviewed issue #31130 discussion + closure (2026-02-20) |

### Corrections & Updates
None identified.

### Internal Tensions / Self-Contradictions
None salient.

### Persuasion Techniques
Some comments are performative (identity signaling about “being human”), but the maintainer closure is procedural and de-escalatory.

### Unstated Assumptions

| Assumption | Claim ID | Critical? | Problematic? |
|------------|----------|-----------|--------------|
| Locking threads reduces harm/cost more than it reduces legitimate deliberation | INST-2026-928 | Y | depends |

### Evidence Assessment
Primary-source timestamps; strong for what happened, weak for deeper “why” (motivation).

### Credence Assessment
- **Overall Credence**: 0.85.

## Stage 3: Dialectical Analysis

### Steelmanned Argument
If a human stands behind the patch, and if the transformation is proven safe in specific sites with targeted benchmarks, there is a path to acceptance even under an AI policy.

### Strongest Counterarguments
1. Once a thread becomes a lightning rod, even good patches have high coordination cost.
2. Without clear and durable performance wins, the churn is not justified.

### Supporting Theories

| Theory/Framework | Source ID | How It Supports |
|------------------|-----------|-----------------|
| Coordination-cost minimization in volunteer governance | matplotlib-2026-issue-31130-column-stack-vstack-perf | Maintainers explicitly discuss prioritization and durability of wins |

### Contradicting Theories

| Theory/Framework | Source ID | Point of Conflict |
|------------------|-----------|------------------|
| “Always prefer more throughput” (accept many small PRs) | N/A | Conflicts with review scarcity and escalation risk |

### Synthesis Notes
The “HUMAN EDITION” framing shows how quickly an initial bot incident can spill into follow-up PRs and social conflict even when humans re-enter the loop.

### Claims to Cross-Reference
- INST-2026-924..926 (PR #31132 origin)

---

### Claim Summary

| ID | Type | Domain | Layer | Actor | Scope | Quantifier | Evidence | Credence | Claim |
|----|------|--------|-------|-------|-------|------------|----------|----------|-------|
| INST-2026-927 | [F] | INST | PRACTICED | OTHER:matplotlib maintainers | who=matplotlib; where=GitHub PR; when=2026-02-12; action=close PR | N/A | E2 | 0.95 | PR #31138 was opened as a human follow-up and was closed without merge. |
| INST-2026-928 | [F] | INST | PRACTICED | OTHER:matplotlib maintainer | who=maintainer; where=PR comments; when=2026-02-12; action=lock thread | N/A | E2 | 0.90 | Maintainer concluded optimization not worth it and locked the thread. |

### Claims to Register

```yaml
claims:
  - id: "INST-2026-927"
    text: "Matplotlib PR #31138 was opened on 2026-02-12 by `bergutman` as a follow-up (“HUMAN EDITION”) to the earlier `column_stack`→`vstack().T` PR, and it was closed without merge the same day."
    type: "[F]"
    domain: "INST"
    evidence_level: "E2"
    credence: 0.95
    operationalization: "Check PR metadata on GitHub (created_at, closed_at, merged=false)."
    falsifiers: ["PR metadata materially differs from the archived snapshot."]
    source_ids: ["matplotlib-2026-pr-31138-human-edition-column-stack-vstack"]
  - id: "INST-2026-928"
    text: "A Matplotlib maintainer concluded the optimization was not worth pursuing and locked the PR #31138 thread to stop further discussion."
    type: "[F]"
    domain: "INST"
    evidence_level: "E2"
    credence: 0.9
    operationalization: "Check PR comments for the maintainer closure/lock note."
    falsifiers: ["No maintainer comment indicating closure/lock rationale."]
    source_ids: ["matplotlib-2026-pr-31138-human-edition-column-stack-vstack"]
```

**Analysis Date**: 2026-02-20  
**Analyst**: gpt-5.2 (Codex CLI)  
**Credence in Analysis**: 0.75

## Analysis Log

| Pass | Date | Tool | Model | Duration | Tokens | Cost | Notes |
|------|------|------|-------|----------|--------|------|-------|
| 1 | 2026-02-20 | codex-cli | gpt-5.2 | — | — | — | Initial analysis from captured PR thread + light live verification |

