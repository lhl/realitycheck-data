# Source Analysis: METR funding and conflict-of-interest disclosures

[DRAFT]

> **Claim types:** `[F]` factual, `[T]` theory, `[H]` hypothesis, `[P]` prediction, `[A]` assumption, `[C]` counterfactual, `[S]` speculation, `[X]` contradiction.
> **Evidence:** E1 synthesis/replication; E2 peer-reviewed or official empirical evidence; E3 expert/working research; E4 documentary/industry/reporting; E5 opinion; E6 unsupported. Evidence tier is not a probability.
> **Verification:** `ok` verified within stated scope; `x` contradicted; `nf` searched but unresolved; `blocked` access/authentication gap; `?` not attempted. A verified statement that a source reports X does not independently establish X.

## Metadata

| Field | Value |
| --- | --- |
| Source ID | metr-2026-independence-and-conflicts |
| Title | METR funding and conflict-of-interest disclosures |
| Author(s) | METR |
| Date | 2026-09-16 capture; policy dated 2026-08-28 |
| Type | REPORT (policy) |
| URL | https://metr.org/about/ |
| Supplied/capture URL | https://metr.org/about/ |
| Reliability | 0.85 |
| Rigor Level | DRAFT |
| Analysis date | 2026-09-16 |

## Stage 1: Descriptive Analysis

### Core Thesis

METR describes non-industry funding, in-kind lab support and a conflict-management policy; independence must be assessed at organizational and project levels.

### Key Claims

| # | Claim | Claim ID | Layer | Actor | Scope | Quantifier | Type | Domain | Evid | Credence | Verified? | Falsifiable By |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | METR states it has accepted no AI-company funding, while acknowledging significant free tokens and access from frontier labs. | INST-2026-506 | ASSERTED | OTHER:METR | who=METR; where=referenced source or stated scenario; when=2026-09-16 capture; policy dated 2026-08-28 | OTHER:bounded as stated | [F] | INST | E4 | 0.98 | ok | The captured funding disclosure says otherwise or is corrected by METR. |
| 2 | METR’s August 28 conflict policy requires handling and disclosure of material conflicts in company-identifying risk assessments. | INST-2026-507 | ASSERTED | OTHER:METR | who=METR; where=referenced source or stated scenario; when=2026-09-16 capture; policy dated 2026-08-28 | OTHER:bounded as stated | [F] | INST | E4 | 0.98 | ok | The policy lacks these requirements. |

### Argument Structure

```text
METR describes non-industry funding, in-kind lab support and a conflict-management policy; independence must be assessed at organizational and project levels.
  -> A transparent, managed-conflict arrangement can produce useful evidence even when perfect detachment is impossible.
  -> Sacks’s concern warrants scrutiny, but the retrieved evidence does not establish that METR is controlled by Anthropic or that its incident findings are false.
```

**Weakest link:** The institution both depends on voluntary access and evaluates the companies providing it. Disclosure reduces opacity but cannot remove the tension.

**If that link fails:** the narrower observations may remain valid while the broader policy or causal conclusion loses support.

### Theoretical Lineage

Risk governance, externalities, institutional incentives and the distinction between capability evidence and policy effectiveness. These are analytic connections, not claims of direct intellectual influence.

### Scope & Limitations

Selected crux claims are extracted; this is not an inventory of every sentence. The relevant tests are staffing, recusal, publication rights, external review and revealed reporting behavior, not the word independent alone.

## Stage 2: Evaluative Analysis

### Key Factual Claims Verified

The About page and downloaded policy were captured. The incident report adds September 13 relationship disclosures and describes OpenAI redaction and access conditions. Queries: "free tokens"; "unmitigated conflicts"; "spouse".

| Claim ID | Claim (paraphrased) | Crux? | Source Says | Actual / scope of check | External Source / comparison | Search Notes | Status |
| --- | --- | --- | --- | --- | --- | --- | --- |
| INST-2026-506 | METR states it has accepted no AI-company funding, while acknowledging significant free tokens and access from frontier labs. | Y | METR states it has accepted no AI-company funding, while acknowledging significant free tokens and access from frontier labs. | Verified as an attributed source statement, not an independently replicated world-state measurement. | [metr-coi](../../reference/captured/pacing-frontier-2026/metr-coi.txt), [metr](metr-2026-hugging-face-investigation.md), [4](sacks-2026-pace-frontier-response.md), [3](amodei-2026-we-must-pace-frontier.md) | See actual query results in verification-searches.json and capture manifests. | ok |
| INST-2026-507 | METR’s August 28 conflict policy requires handling and disclosure of material conflicts in company-identifying risk assessments. | Y | METR’s August 28 conflict policy requires handling and disclosure of material conflicts in company-identifying risk assessments. | Verified as an attributed source statement, not an independently replicated world-state measurement. | [metr-coi](../../reference/captured/pacing-frontier-2026/metr-coi.txt), [metr](metr-2026-hugging-face-investigation.md), [4](sacks-2026-pace-frontier-response.md), [3](amodei-2026-we-must-pace-frontier.md) | See actual query results in verification-searches.json and capture manifests. | ok |

### Disconfirming Evidence Search

| Claim | Counterevidence / alternative | Search Notes |
| --- | --- | --- |
| INST-2026-506, INST-2026-507 | Independent monetary funding is not the absence of access dependence, shared assumptions, personal relationships or incentives to preserve cooperation. A policy is not an audit of compliance. | Source comparisons above; captured-corpus queries recorded. General web discovery had blocked or irrelevant results, so no exhaustive-search claim is made. |

### Corrections & Updates

| Item | URL / capture | Published | Corrected/Updated | What Changed | Impacted Claim IDs | Action Taken |
| --- | --- | --- | --- | --- | --- | --- |
| Initial pass | https://metr.org/about/ | 2026-09-16 capture; policy dated 2026-08-28 | 2026-09-16 | The About page and downloaded policy were captured. The incident report adds September 13 relationship disclosures and describes OpenAI redaction and access conditions. Queries: "free tokens"; "unmitigated conflicts"; "spouse". Current capture and its limitations preserved. | INST-2026-506, INST-2026-507 | Keep DRAFT; retain raw captures. |

### Internal Coherence and Tensions

The institution both depends on voluntary access and evaluates the companies providing it. Disclosure reduces opacity but cannot remove the tension.

### Persuasion Techniques

| Technique | Example / framing | Assessment |
| --- | --- | --- |
| Selection and framing | METR describes non-industry funding, in-kind lab support and a conflict-management policy; independence must be assessed at organizational and project levels. | Distinguish observed premises from the conclusion; framing does not itself invalidate evidence. |
| Authority and extrapolation | METR speaks from institutional, technical or personal experience. | Authority matters within its observational scope; it does not establish unobserved outcomes. |

### Unstated Assumptions

| Assumption | Claim ID | Critical? | Problematic? |
| --- | --- | --- | --- |
| The captured text is authentic and the stated scope is preserved. | INST-2026-506 | Y | Capture/source fidelity checked; underlying attribution may remain uncertain. |
| The captured text is authentic and the stated scope is preserved. | INST-2026-507 | Y | Capture/source fidelity checked; underlying attribution may remain uncertain. |

### Evidence Assessment

The About page and downloaded policy were captured. The incident report adds September 13 relationship disclosures and describes OpenAI redaction and access conditions. Queries: "free tokens"; "unmitigated conflicts"; "spouse".

### Credence Assessment

Credences in the claim tables are subjective assessments of the precise propositions, not measured frequencies. High credence in an attributed report does not imply high credence in the source’s explanation, forecast or preferred policy. Independent monetary funding is not the absence of access dependence, shared assumptions, personal relationships or incentives to preserve cooperation. A policy is not an audit of compliance.

## Stage 3: Dialectical Analysis

### Steelmanned Argument

A transparent, managed-conflict arrangement can produce useful evidence even when perfect detachment is impossible.

### Strongest Counterarguments

The relevant tests are staffing, recusal, publication rights, external review and revealed reporting behavior, not the word independent alone.

### Supporting Theories and Contradicting Evidence

- [metr-coi](../../reference/captured/pacing-frontier-2026/metr-coi.txt)
- [Brief independent investigation of the OpenAI–Hugging Face incident](metr-2026-hugging-face-investigation.md)
- [Response to frontier pacing proposals](sacks-2026-pace-frontier-response.md)
- [We Must Pace the Frontier](amodei-2026-we-must-pace-frontier.md)

**Support:** A transparent, managed-conflict arrangement can produce useful evidence even when perfect detachment is impossible.

**Challenge:** Independent monetary funding is not the absence of access dependence, shared assumptions, personal relationships or incentives to preserve cooperation. A policy is not an audit of compliance.

### Synthesis Notes

Sacks’s concern warrants scrutiny, but the retrieved evidence does not establish that METR is controlled by Anthropic or that its incident findings are false.

### Claims to Cross-Reference

INST-2026-506, INST-2026-507; see the [cross-source synthesis](../syntheses/pacing-frontier-2026-risk-governance-china-bio.md).

## Claim Summary

| ID | Type | Domain | Layer | Actor | Scope | Quantifier | Evidence | Credence | Claim |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| INST-2026-506 | [F] | INST | ASSERTED | OTHER:METR | who=METR; where=referenced source or stated scenario; when=2026-09-16 capture; policy dated 2026-08-28 | OTHER:bounded as stated | E4 | 0.98 | METR states it has accepted no AI-company funding, while acknowledging significant free tokens and access from frontier labs. |
| INST-2026-507 | [F] | INST | ASSERTED | OTHER:METR | who=METR; where=referenced source or stated scenario; when=2026-09-16 capture; policy dated 2026-08-28 | OTHER:bounded as stated | E4 | 0.98 | METR’s August 28 conflict policy requires handling and disclosure of material conflicts in company-identifying risk assessments. |

### Claims to Register

The complete machine-readable artifact is [metr-2026-independence-and-conflicts.yaml](metr-2026-independence-and-conflicts.yaml).

**Credence in analysis:** 0.85. Main limitations: capture completeness, source incentives, and the absence of prospective tests of the broader hypotheses.

## Analysis Log

| Pass | Date | Tool | Model | Duration | Tokens | Cost | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | 2026-09-16 | codex | gpt-6 | unavailable | unavailable | unavailable | ANALYSIS-2026-222; shared workflow ANALYSIS-2026-201. Source reading preceded per-source log; do not interpret unavailable usage as zero. |

### Revision Notes

Pass 1: captured and compared sources, separated reported facts from forecasts, searched for counterevidence, and drafted claim/provenance artifacts. Analyst prose reviewed for attribution and unwarranted certainty.

### Search and schema notes

[Executed verification queries](../../reference/captured/pacing-frontier-2026/verification-searches.json) are captured-document searches, alongside the separately retained web-discovery attempts. Rigor fields (layer, actor, scope, quantifier) are preserved in these tables and the analysis manifest; the current LanceDB claim schema does not accept those fields.

## Registered provenance

| Claim | Evidence links | Reasoning trail |
| --- | --- | --- |
| INST-2026-506 | EVLINK-2026-724 | REASON-2026-486 |
| INST-2026-507 | EVLINK-2026-725 | REASON-2026-487 |

Registered in LanceDB. The [provenance artifact](../../reference/captured/pacing-frontier-2026/provenance.json) includes evidence direction, rationale and counterarguments.
