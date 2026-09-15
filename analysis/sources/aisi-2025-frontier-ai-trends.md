# Source Analysis: Frontier AI Trends Report

[DRAFT]

> **Claim types:** `[F]` factual, `[T]` theory, `[H]` hypothesis, `[P]` prediction, `[A]` assumption, `[C]` counterfactual, `[S]` speculation, `[X]` contradiction.
> **Evidence:** E1 synthesis/replication; E2 peer-reviewed or official empirical evidence; E3 expert/working research; E4 documentary/industry/reporting; E5 opinion; E6 unsupported. Evidence tier is not a probability.
> **Verification:** `ok` verified within stated scope; `x` contradicted; `nf` searched but unresolved; `blocked` access/authentication gap; `?` not attempted. A verified statement that a source reports X does not independently establish X.

## Metadata

| Field | Value |
| --- | --- |
| Source ID | aisi-2025-frontier-ai-trends |
| Title | Frontier AI Trends Report |
| Author(s) | UK AI Security Institute |
| Date | 2025 (report covers testing through 2025; captured 2026-09-16) |
| Type | REPORT (report) |
| URL | https://www.aisi.gov.uk/frontier-ai-trends-report |
| Supplied/capture URL | https://www.aisi.gov.uk/frontier-ai-trends-report |
| Reliability | 0.85 |
| Rigor Level | DRAFT |
| Analysis date | 2026-09-16 |

## Stage 1: Descriptive Analysis

### Core Thesis

AISI reports advances on bounded scientific and cyber tasks, with explicit distinctions among knowledge tests, task assistance, safeguards and loss-of-control indicators.

### Key Claims

| # | Claim | Claim ID | Layer | Actor | Scope | Quantifier | Type | Domain | Evid | Credence | Verified? | Falsifiable By |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | AISI reports 4.7 times higher odds of non-experts producing a feasible protocol in a bounded biology task with frontier AI assistance than with internet access alone, with confidence interval 2.8–7.9. | RISK-2026-511 | ASSERTED | OTHER:UK AI Security Institute | who=UK AI Security Institute; where=referenced source or stated scenario; when=2025 (report covers testing through 2025; captured 2026-09-16) | OTHER:bounded as stated | [F] | RISK | E2 | 0.94 | ok | The reported estimate, comparison group or outcome is materially different. |
| 2 | AISI’s reported biology assistance results do not measure pandemic creation, extinction probability or reliable end-to-end autonomous biological mastery. | META-2026-502 | ASSERTED | OTHER:UK AI Security Institute | who=UK AI Security Institute; where=referenced source or stated scenario; when=2025 (report covers testing through 2025; captured 2026-09-16) | OTHER:bounded as stated | [F] | META | E2 | 0.98 | ok | The report actually measures those outcomes. |

### Argument Structure

```text
AISI reports advances on bounded scientific and cyber tasks, with explicit distinctions among knowledge tests, task assistance, safeguards and loss-of-control indicators.
  -> Measure incremental assistance against a realistic alternative rather than relying only on anecdotes or hypothetical autonomous facilities.
  -> Refutes the broad claim that AI only retrieves familiar information, without validating the strongest biological-extinction claims.
```

**Weakest link:** Task-level gains are consequential but cannot be directly mapped to a system-level risk estimate without assumptions about other stages and defenses.

**If that link fails:** the narrower observations may remain valid while the broader policy or causal conclusion loses support.

### Theoretical Lineage

Risk governance, externalities, institutional incentives and the distinction between capability evidence and policy effectiveness. These are analytic connections, not claims of direct intellectual influence.

### Scope & Limitations

Selected crux claims are extracted; this is not an inventory of every sentence. A bounded result can overstate generality if tasks are selected favorably; favorable task results do not settle net offense-defense effects.

## Stage 2: Evaluative Analysis

### Key Factual Claims Verified

The first-party report gives the odds ratio, interval and outcome. It also discusses wet-lab feasibility and assistance, and model failures on end-to-end tasks. RAND supplies an earlier, different null result. Queries: "4.7x"; "end-to-end"; "no statistically significant".

| Claim ID | Claim (paraphrased) | Crux? | Source Says | Actual / scope of check | External Source / comparison | Search Notes | Status |
| --- | --- | --- | --- | --- | --- | --- | --- |
| RISK-2026-511 | AISI reports 4.7 times higher odds of non-experts producing a feasible protocol in a bounded biology task with frontier AI assistance than with internet access alone, with confidence interval 2.8–7.9. | Y | AISI reports 4.7 times higher odds of non-experts producing a feasible protocol in a bounded biology task with frontier AI assistance than with internet access alone, with confidence interval 2.8–7.9. | Verified as an attributed source statement, not an independently replicated world-state measurement. | [rand-jina](rand-2024-ai-biological-attack-risk.md), [bio-a](derya-2026-biological-risk-defense-thread.md), [bio-b](bellamy-2026-biological-risk-bottlenecks.md) | See actual query results in verification-searches.json and capture manifests. | ok |
| META-2026-502 | AISI’s reported biology assistance results do not measure pandemic creation, extinction probability or reliable end-to-end autonomous biological mastery. | Y | AISI’s reported biology assistance results do not measure pandemic creation, extinction probability or reliable end-to-end autonomous biological mastery. | Verified as an attributed source statement, not an independently replicated world-state measurement. | [rand-jina](rand-2024-ai-biological-attack-risk.md), [bio-a](derya-2026-biological-risk-defense-thread.md), [bio-b](bellamy-2026-biological-risk-bottlenecks.md) | See actual query results in verification-searches.json and capture manifests. | ok |

### Disconfirming Evidence Search

| Claim | Counterevidence / alternative | Search Notes |
| --- | --- | --- |
| RISK-2026-511, META-2026-502 | Not all internal study detail is public, some grading uses model judges, and benchmark performance does not establish real-world catastrophic outcomes. Odds are not probability or a count of successful attacks. | Source comparisons above; captured-corpus queries recorded. General web discovery had blocked or irrelevant results, so no exhaustive-search claim is made. |

### Corrections & Updates

| Item | URL / capture | Published | Corrected/Updated | What Changed | Impacted Claim IDs | Action Taken |
| --- | --- | --- | --- | --- | --- | --- |
| Initial pass | https://www.aisi.gov.uk/frontier-ai-trends-report | 2025 (report covers testing through 2025; captured 2026-09-16) | 2026-09-16 | The first-party report gives the odds ratio, interval and outcome. It also discusses wet-lab feasibility and assistance, and model failures on end-to-end tasks. RAND supplies an earlier, different null result. Queries: "4.7x"; "end-to-end"; "no statistically significant". Current capture and its limitations preserved. | RISK-2026-511, META-2026-502 | Keep DRAFT; retain raw captures. |

### Internal Coherence and Tensions

Task-level gains are consequential but cannot be directly mapped to a system-level risk estimate without assumptions about other stages and defenses.

### Persuasion Techniques

| Technique | Example / framing | Assessment |
| --- | --- | --- |
| Selection and framing | AISI reports advances on bounded scientific and cyber tasks, with explicit distinctions among knowledge tests, task assistance, safeguards and loss-of-control indicators. | Distinguish observed premises from the conclusion; framing does not itself invalidate evidence. |
| Authority and extrapolation | UK AI Security Institute speaks from institutional, technical or personal experience. | Authority matters within its observational scope; it does not establish unobserved outcomes. |

### Unstated Assumptions

| Assumption | Claim ID | Critical? | Problematic? |
| --- | --- | --- | --- |
| The captured text is authentic and the stated scope is preserved. | RISK-2026-511 | Y | Capture/source fidelity checked; underlying attribution may remain uncertain. |
| The captured text is authentic and the stated scope is preserved. | META-2026-502 | Y | Capture/source fidelity checked; underlying attribution may remain uncertain. |

### Evidence Assessment

The first-party report gives the odds ratio, interval and outcome. It also discusses wet-lab feasibility and assistance, and model failures on end-to-end tasks. RAND supplies an earlier, different null result. Queries: "4.7x"; "end-to-end"; "no statistically significant".

### Credence Assessment

Credences in the claim tables are subjective assessments of the precise propositions, not measured frequencies. High credence in an attributed report does not imply high credence in the source’s explanation, forecast or preferred policy. Not all internal study detail is public, some grading uses model judges, and benchmark performance does not establish real-world catastrophic outcomes. Odds are not probability or a count of successful attacks.

## Stage 3: Dialectical Analysis

### Steelmanned Argument

Measure incremental assistance against a realistic alternative rather than relying only on anecdotes or hypothetical autonomous facilities.

### Strongest Counterarguments

A bounded result can overstate generality if tasks are selected favorably; favorable task results do not settle net offense-defense effects.

### Supporting Theories and Contradicting Evidence

- [Does AI Increase the Operational Risk of Biological Attacks?](rand-2024-ai-biological-attack-risk.md)
- [Biological AI risk and the opportunity cost of delaying medicine](derya-2026-biological-risk-defense-thread.md)
- [Physical bottlenecks to AI-enabled biological catastrophe](bellamy-2026-biological-risk-bottlenecks.md)

**Support:** Measure incremental assistance against a realistic alternative rather than relying only on anecdotes or hypothetical autonomous facilities.

**Challenge:** Not all internal study detail is public, some grading uses model judges, and benchmark performance does not establish real-world catastrophic outcomes. Odds are not probability or a count of successful attacks.

### Synthesis Notes

Refutes the broad claim that AI only retrieves familiar information, without validating the strongest biological-extinction claims.

### Claims to Cross-Reference

RISK-2026-511, META-2026-502; see the [cross-source synthesis](../syntheses/pacing-frontier-2026-risk-governance-china-bio.md).

## Claim Summary

| ID | Type | Domain | Layer | Actor | Scope | Quantifier | Evidence | Credence | Claim |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| RISK-2026-511 | [F] | RISK | ASSERTED | OTHER:UK AI Security Institute | who=UK AI Security Institute; where=referenced source or stated scenario; when=2025 (report covers testing through 2025; captured 2026-09-16) | OTHER:bounded as stated | E2 | 0.94 | AISI reports 4.7 times higher odds of non-experts producing a feasible protocol in a bounded biology task with frontier AI assistance than with internet access alone, with confidence interval 2.8–7.9. |
| META-2026-502 | [F] | META | ASSERTED | OTHER:UK AI Security Institute | who=UK AI Security Institute; where=referenced source or stated scenario; when=2025 (report covers testing through 2025; captured 2026-09-16) | OTHER:bounded as stated | E2 | 0.98 | AISI’s reported biology assistance results do not measure pandemic creation, extinction probability or reliable end-to-end autonomous biological mastery. |

### Claims to Register

The complete machine-readable artifact is [aisi-2025-frontier-ai-trends.yaml](aisi-2025-frontier-ai-trends.yaml).

**Credence in analysis:** 0.85. Main limitations: capture completeness, source incentives, and the absence of prospective tests of the broader hypotheses.

## Analysis Log

| Pass | Date | Tool | Model | Duration | Tokens | Cost | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | 2026-09-16 | codex | gpt-6 | unavailable | unavailable | unavailable | ANALYSIS-2026-223; shared workflow ANALYSIS-2026-201. Source reading preceded per-source log; do not interpret unavailable usage as zero. |

### Revision Notes

Pass 1: captured and compared sources, separated reported facts from forecasts, searched for counterevidence, and drafted claim/provenance artifacts. Analyst prose reviewed for attribution and unwarranted certainty.

### Search and schema notes

[Executed verification queries](../../reference/captured/pacing-frontier-2026/verification-searches.json) are captured-document searches, alongside the separately retained web-discovery attempts. Rigor fields (layer, actor, scope, quantifier) are preserved in these tables and the analysis manifest; the current LanceDB claim schema does not accept those fields.

## Registered provenance

| Claim | Evidence links | Reasoning trail |
| --- | --- | --- |
| RISK-2026-511 | EVLINK-2026-726 | REASON-2026-488 |
| META-2026-502 | EVLINK-2026-727 | REASON-2026-489 |

Registered in LanceDB. The [provenance artifact](../../reference/captured/pacing-frontier-2026/provenance.json) includes evidence direction, rationale and counterarguments.
