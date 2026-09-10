# Source Analysis: OpenAI API data controls: training and retention

> **Claim types**: `[F]` fact (including attributed statements), `[T]` theory, `[H]` hypothesis, `[P]` prediction, `[A]` assumption, `[C]` counterfactual, `[S]` speculation, `[X]` contradiction.
> **Evidence**: E1 systematic review; E2 peer-reviewed/official statistics; E3 expert/preprint; E4 reporting/industry documents; E5 firsthand statement/opinion; E6 unsupported inference. **Status**: `ok` verified at the stated scope; `x` refuted; `nf` searched but not established; `blocked` inaccessible; `?` unattempted.
> High credence in an attributed statement means confidence that it was said, not that the underlying allegation is true. Evidence category is not a mechanical probability cap. Tested implications are analyst formulations, not quotations. All files in this package remain **DRAFT** because provenance and scientific acceptance are unresolved.

## Metadata

| Field | Value |
|---|---|
| **Source ID** | openai-2026-api-data-controls |
| **Title** | OpenAI API data controls: training and retention |
| **Author(s)** | OpenAI |
| **Date** | 2026-09-10 capture |
| **Type** | KNOWLEDGE (official documentation) |
| **URL** | https://platform.openai.com/docs/guides/your-data |
| **Reliability** | 0.80 for recoverable source content; see claim-specific scope |
| **Rigor Level** | DRAFT |
| **Capture** | [Target text](../../reference/captured/navier-stokes-2026/api-policy-target.txt); raw captures and hashes in the [capture directory](../../reference/captured/navier-stokes-2026/) |

## Stage 1: Descriptive Analysis

### Core Thesis

OpenAI’s API documentation distinguishes a no-training default from abuse-monitoring retention and application-state storage.

### Key Claims

| # | Claim | Claim ID | Layer | Actor | Scope | Quantifier | Type | Domain | Evid | Credence | Verified? | Falsifiable By |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | OpenAI’s API documentation states that since March 1, 2023 API data is not used to train or improve models unless the customer explicitly opts in. | INST-2026-339 | ASSERTED | OTHER:OpenAI | who=researchers and AI providers; where=public record; when=2026-09-10 review; process=research and publication | some | [F] | INST | E4 | 0.99 | ok; see verification row | Authenticated source records contradicting the attribution or chronology. |
| 2 | OpenAI’s API documentation allows retention of abuse-monitoring logs containing prompts, responses and derived metadata, distinct from model training. | INST-2026-340 | ASSERTED | OTHER:OpenAI | who=researchers and AI providers; where=public record; when=2026-09-10 review; process=research and publication | some | [F] | INST | E4 | 0.99 | ok; see verification row | Authenticated source records contradicting the attribution or chronology. |

### Argument Structure

```text
API use → no model training absent explicit opt-in; separate operational storage → retention controls with eligibility and exceptions.
```

**Weakest link:** This is authoritative for the published API policy, not evidence of implementation in a particular account. It does not establish which products the researchers used, whether they opted in, or whether individual subscription settings differed.

### Theoretical Lineage

Research priority, contributor credit, information asymmetry and platform competition. The relevant existing framework is [the July value-chain essay](lhl-2026-ai-value-chain.md), with earlier database context in [the Palantir/extraction synthesis](../syntheses/palantir-sovereign-ai-frontier-lab-extraction-synthesis.md). These are analyst cross-references, not claims that this source explicitly cites that framework.

### Scope & Limitations

This pass assesses the source’s contribution to the September controversy and the customer-value question. It does not certify a fluid-dynamics theorem or reconstruct undisclosed account histories. Public testimony, press repetition, formal theorem statements and causal training evidence have different evidentiary roles.

## Stage 2: Evaluative Analysis

### Internal Coherence

This is authoritative for the published API policy, not evidence of implementation in a particular account. It does not establish which products the researchers used, whether they opted in, or whether individual subscription settings differed.

### Key Factual Claims Verified

The first factual row is a crux of this source’s contribution. For attributed statements, `ok` verifies attribution only. Rows testing implications are labeled by claim type above.

| Claim ID | Claim (paraphrased) | Crux? | Source Says | Actual | External Source | Search Notes | Status |
|---|---|---|---|---|---|---|---|
| INST-2026-339 | OpenAI’s API documentation states that since March 1, 2023 API data is not used to train or improve models unless the customer explicitly opts in. | Y | Attributed record | Explicit in the official data guide. Applies to API policy, not all products by assumption. | [lhl-2026-ai-value-chain](lhl-2026-ai-value-chain.md); [primary](https://platform.openai.com/docs/guides/your-data) | 2026-09-10: corpus q1='March 1, 2023'; q2='explicitly opt in'. Web discovery and DB-first attempts: capture-method.md; exact hits: claim-verification-searches.json. | ok |
| INST-2026-340 | OpenAI’s API documentation allows retention of abuse-monitoring logs containing prompts, responses and derived metadata, distinct from model training. | N | Attributed record | The guide describes default retention up to 30 days and specified exceptions and controls. | [openai-2026-api-data-controls](openai-2026-api-data-controls.md); [primary](https://platform.openai.com/docs/guides/your-data) | 2026-09-10: corpus q1='Abuse monitoring logs'; q2='30 days'. Web discovery and DB-first attempts: capture-method.md; exact hits: claim-verification-searches.json. | ok |

### Disconfirming Evidence Search

| Claim | Counterevidence / alternative | Search notes |
|---|---|---|
| INST-2026-339 | Policies need auditable enforcement and coverage of derivatives. No-training alone does not prevent the provider competing on a publicly learned opportunity. | Primary-source comparison plus two recorded phrase queries per claim; disputed positions retained. |
| INST-2026-340 | This is authoritative for the published API policy, not evidence of implementation in a particular account. It does not establish which products the researchers used, whether they opted in, or whether individual subscription settings differed. | See the source-specific verification rows and the shared search log. |

### Corrections & Updates

| Item | URL | Published | Corrected/Updated | What Changed | Impacted Claim IDs | Action Taken |
|---|---|---|---|---|---|---|
| 1 | https://platform.openai.com/docs/guides/your-data | 2026-09-10 capture | Capture/review 2026-09-10 | Official API page fetched in full. Current policy snapshot is not a historical contract reconstruction. The separate Codex enterprise route redirected to a general admin rollout guide and was not used to infer the researchers’ settings. | INST-2026-339, INST-2026-340 | Retain raw records and distinct versions; do not overwrite prior-source wording. |

### Internal Tensions / Self-Contradictions

This is authoritative for the published API policy, not evidence of implementation in a particular account. It does not establish which products the researchers used, whether they opted in, or whether individual subscription settings differed. No additional internal contradiction is inferred merely from disagreement with another participant.

### Persuasion Techniques

“Your data is your data” is reassuring language. The operative details are the product scope, opt-in condition, operational retention and exceptions; these should carry the evidentiary weight.

### Unstated Assumptions

| Assumption | Claim ID | Critical? | Problematic? |
|---|---|---|---|
| Public statements reliably establish what a participant asserts, but not every underlying private event. | INST-2026-339 | Y | N for attribution; Y if extended to conduct |
| Policies need auditable enforcement and coverage of derivatives. No-training alone does not prevent the provider competing on a publicly learned opportunity. | INST-2026-340 | Y for broad conclusions | Remains an alternative to test |

### Evidence Assessment

This is authoritative for the published API policy, not evidence of implementation in a particular account. It does not establish which products the researchers used, whether they opted in, or whether individual subscription settings differed. Repetition across news outlets is not counted as independent confirmation when they rely on the same post, statement or briefing.

### Credence Assessment

**Credence in this source analysis: 0.85.** The content and attributed positions are captured; private data lineage, intent and full mathematical validation remain outside this pass. Use the claim-specific probabilities rather than averaging them into a verdict about the entire controversy.

## Stage 3: Dialectical Analysis

### Steelmanned Argument

Product-specific contractual defaults and retention controls allow customers to choose exposure appropriate to their research.

### Strongest Counterarguments

Policies need auditable enforcement and coverage of derivatives. No-training alone does not prevent the provider competing on a publicly learned opportunity.

### Supporting Theories

| Theory/framework | Source ID | Relation |
|---|---|---|
| Separate training, byproducts and competition | lhl-2026-ai-value-chain | Prevents evidence about one mechanism from being used as proof of another. |
| Problem selection and sharing incentives | tao-2026-promising-problems-open-science | Explains why a research direction can be valuable before a final proof exists. |

### Contradicting Theories

| Theory/framework | Source ID | Point to test |
|---|---|---|
| Independent discovery from a stronger model | openai-2026-navier-stokes-solution | A rapid or stronger result can be independently produced; capability does not settle provenance. |
| Customer control and exit options | lhl-2026-ai-value-chain | Exposure can be reduced, but control does not guarantee capability parity. |

### Synthesis Notes

Product-specific contractual defaults and retention controls allow customers to choose exposure appropriate to their research. Policies need auditable enforcement and coverage of derivatives. No-training alone does not prevent the provider competing on a publicly learned opportunity. See the [cross-source synthesis](../syntheses/navier-stokes-2026-research-credit-data-value-chain.md) for the dated timeline, allegation matrix, bibliography amendment and implications for customer competition.

### Claims to Cross-Reference

[openai-2026-api-data-controls](openai-2026-api-data-controls.md), [lhl-2026-ai-value-chain](lhl-2026-ai-value-chain.md). Existing database claims INST-2026-981 (customer-IP allegation), ECON-2026-984 (context ownership) and INST-2026-992 (portfolio posture) are related frameworks, not proof of this incident.

### Claim Summary

| ID | Type | Domain | Layer | Actor | Scope | Quantifier | Evidence | Credence | Claim |
|---|---|---|---|---|---|---|---|---|---|
| INST-2026-339 | [F] | INST | ASSERTED | OTHER:OpenAI | who=researchers and AI providers; where=public record; when=2026-09-10 review; process=research and publication | some | E4 | 0.99 | OpenAI’s API documentation states that since March 1, 2023 API data is not used to train or improve models unless the customer explicitly opts in. |
| INST-2026-340 | [F] | INST | ASSERTED | OTHER:OpenAI | who=researchers and AI providers; where=public record; when=2026-09-10 review; process=research and publication | some | E4 | 0.99 | OpenAI’s API documentation allows retention of abuse-monitoring logs containing prompts, responses and derived metadata, distinct from model training. |

### Claims to Register

```yaml
claims:
- id: INST-2026-339
  text: OpenAI’s API documentation states that since March 1, 2023 API data is not used to train or improve models
    unless the customer explicitly opts in.
  type: '[F]'
  domain: INST
  evidence_level: E4
  credence: 0.99
  operationalization: Check the cited primary record, versions and counterevidence. Explicit in the official data
    guide. Applies to API policy, not all products by assumption.
  assumptions:
  - Attribution does not independently establish the underlying allegation.
  falsifiers:
  - Authenticated source records contradicting the attribution or chronology.
  source_ids:
  - openai-2026-api-data-controls
  - lhl-2026-ai-value-chain
  first_extracted: '2026-09-10'
  last_updated: '2026-09-10'
  extracted_by: codex
  version: 1
- id: INST-2026-340
  text: OpenAI’s API documentation allows retention of abuse-monitoring logs containing prompts, responses and derived
    metadata, distinct from model training.
  type: '[F]'
  domain: INST
  evidence_level: E4
  credence: 0.99
  operationalization: Check the cited primary record, versions and counterevidence. The guide describes default
    retention up to 30 days and specified exceptions and controls.
  assumptions:
  - Attribution does not independently establish the underlying allegation.
  falsifiers:
  - Authenticated source records contradicting the attribution or chronology.
  source_ids:
  - openai-2026-api-data-controls
  first_extracted: '2026-09-10'
  last_updated: '2026-09-10'
  extracted_by: codex
  version: 1
```

**Analysis Date:** 2026-09-10

**Analyst:** Codex / GPT-6

**Credence in Analysis:** 0.85

## Analysis Log

| Pass | Date | Tool | Model | Duration | Tokens | Cost | Notes |
|---|---|---|---|---|---|---|---|
| 1 | 2026-09-10 | codex | gpt-6 | Shared multi-source pass; not separately measured | unavailable | unavailable | ANALYSIS-2026-199; three-stage analysis, source comparison and neutral prose pass. Session ambiguity prevents reliable per-source usage attribution. |

### Revision Notes

**Pass 1:** Captured source and replies; separated assertions, contested facts and analyst implications; retained corrections and capture limitations. Registration and provenance recorded in the shared package.
