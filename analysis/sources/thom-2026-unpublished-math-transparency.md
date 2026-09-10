# Source Analysis: Unpublished mathematics, non-sofic groups and training transparency

> **Claim types**: `[F]` fact (including attributed statements), `[T]` theory, `[H]` hypothesis, `[P]` prediction, `[A]` assumption, `[C]` counterfactual, `[S]` speculation, `[X]` contradiction.
> **Evidence**: E1 systematic review; E2 peer-reviewed/official statistics; E3 expert/preprint; E4 reporting/industry documents; E5 firsthand statement/opinion; E6 unsupported inference. **Status**: `ok` verified at the stated scope; `x` refuted; `nf` searched but not established; `blocked` inaccessible; `?` unattempted.
> High credence in an attributed statement means confidence that it was said, not that the underlying allegation is true. Evidence category is not a mechanical probability cap. Tested implications are analyst formulations, not quotations. All files in this package remain **DRAFT** because provenance and scientific acceptance are unresolved.

## Metadata

| Field | Value |
|---|---|
| **Source ID** | thom-2026-unpublished-math-transparency |
| **Title** | Unpublished mathematics, non-sofic groups and training transparency |
| **Author(s)** | Andreas Thom |
| **Date** | 2026-09-09 |
| **Type** | SOCIAL |
| **URL** | https://mathstodon.xyz/@andreasthom/117240535270608201 |
| **Reliability** | 0.80 for recoverable source content; see claim-specific scope |
| **Rigor Level** | DRAFT |
| **Capture** | [Target text](../../reference/captured/navier-stokes-2026/thom-target.txt); raw captures and hashes in the [capture directory](../../reference/captured/navier-stokes-2026/) |

## Stage 1: Descriptive Analysis

### Core Thesis

Thom describes a prior exchange about unpublished group-theory discussions and argues that a categorical denial needs a documented distinction between training and inference-time access.

### Key Claims

| # | Claim | Claim ID | Layer | Actor | Scope | Quantifier | Type | Domain | Evid | Credence | Verified? | Falsifiable By |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | Thom quotes a prior two-part question about training and solving-time access and Sellke’s answer, “Regarding your conversations with ChatGPT: that did not happen.” | INST-2026-320 | ASSERTED | OTHER:Andreas Thom | who=researchers and AI providers; where=public record; when=2026-09-10 review; process=research and publication | some | [F] | INST | E5 | 0.93 | ok; see verification row | Authenticated source records contradicting the attribution or chronology. |
| 2 | Thom states he disabled model training on June 29 and argues this leaves earlier conversations and derivatives unresolved. | INST-2026-321 | ASSERTED | OTHER:Andreas Thom | who=researchers and AI providers; where=public record; when=2026-09-10 review; process=research and publication | some | [F] | INST | E5 | 0.97 | ok; see verification row | Authenticated source records contradicting the attribution or chronology. |
| 3 | De-identification of research conversations does not by itself remove their mathematical ideas or settle credit for their subsequent use. | INST-2026-322 | EFFECT | OTHER:Andreas Thom | who=researchers and AI providers; where=public record; when=2026-09-10 review; process=research and publication | some | [T] | INST | E5 | 0.95 | ok; see verification row | A demonstrated transformation removing all relevant technical content, not just identifying metadata. |

### Argument Structure

```text
Prior unpublished discussions → unexpected use of a familiar research route → two-part question → categorical answer → later OpenAI caveat → demand for auditable provenance.
```

**Weakest link:** The quoted email is firsthand testimony; its complete context, underlying account records and Sellke’s response to the new criticism were not recovered. Thom’s inference that a prior answer addressed only direct access is plausible but unverified. His June 29 opt-out is specific to his account and cannot be transferred to Buckmaster.

### Theoretical Lineage

Research priority, contributor credit, information asymmetry and platform competition. The relevant existing framework is [the July value-chain essay](lhl-2026-ai-value-chain.md), with earlier database context in [the Palantir/extraction synthesis](../syntheses/palantir-sovereign-ai-frontier-lab-extraction-synthesis.md). These are analyst cross-references, not claims that this source explicitly cites that framework.

### Scope & Limitations

This pass assesses the source’s contribution to the September controversy and the customer-value question. It does not certify a fluid-dynamics theorem or reconstruct undisclosed account histories. Public testimony, press repetition, formal theorem statements and causal training evidence have different evidentiary roles.

## Stage 2: Evaluative Analysis

### Internal Coherence

The quoted email is firsthand testimony; its complete context, underlying account records and Sellke’s response to the new criticism were not recovered. Thom’s inference that a prior answer addressed only direct access is plausible but unverified. His June 29 opt-out is specific to his account and cannot be transferred to Buckmaster.

### Key Factual Claims Verified

The first factual row is a crux of this source’s contribution. For attributed statements, `ok` verifies attribution only. Rows testing implications are labeled by claim type above.

| Claim ID | Claim (paraphrased) | Crux? | Source Says | Actual | External Source | Search Notes | Status |
|---|---|---|---|---|---|---|---|
| INST-2026-320 | Thom quotes a prior two-part question about training and solving-time access and Sellke’s answer, “Regarding your conversations with ChatGPT: that did not happen.” | Y | Attributed record | Verified as Thom’s published account; original email files were not independently authenticated. | [thom-2026-unpublished-math-transparency](thom-2026-unpublished-math-transparency.md); [primary](https://mathstodon.xyz/@andreasthom/117240535270608201) | 2026-09-10: corpus q1='did not happen'; q2='two different'. Web discovery and DB-first attempts: capture-method.md; exact hits: claim-verification-searches.json. | ok |
| INST-2026-321 | Thom states he disabled model training on June 29 and argues this leaves earlier conversations and derivatives unresolved. | N | Attributed record | Stated in part 2/3 and a separate reply; year inferred from the September 2026 discussion. | [thom-2026-unpublished-math-transparency](thom-2026-unpublished-math-transparency.md); [primary](https://mathstodon.xyz/@andreasthom/117240535270608201) | 2026-09-10: corpus q1='29 June'; q2='June 29'. Web discovery and DB-first attempts: capture-method.md; exact hits: claim-verification-searches.json. | ok |
| INST-2026-322 | De-identification of research conversations does not by itself remove their mathematical ideas or settle credit for their subsequent use. | N | Analyst tests the source’s mechanism or a disputed implication; not a quotation | Distinguishes identity protection from information content; an empirical data-lineage audit is still needed in any individual case. | [openai-2026-navier-stokes-data-response](openai-2026-navier-stokes-data-response.md), [alpoge-2026-training-authorship-response](alpoge-2026-training-authorship-response.md); [primary](https://mathstodon.xyz/@andreasthom/117240535270608201) | 2026-09-10: corpus q1='De-identification'; q2='intellectual content'. Web discovery and DB-first attempts: capture-method.md; exact hits: claim-verification-searches.json. | ok |

### Disconfirming Evidence Search

| Claim | Counterevidence / alternative | Search notes |
|---|---|---|
| INST-2026-320 | A categorical answer could have been based on account-specific exclusion that is not public. Public literature could explain the mathematical route. The Navier–Stokes caveat does not logically prove a different answer in a different case was false. | Primary-source comparison plus two recorded phrase queries per claim; disputed positions retained. |
| INST-2026-322 | The quoted email is firsthand testimony; its complete context, underlying account records and Sellke’s response to the new criticism were not recovered. Thom’s inference that a prior answer addressed only direct access is plausible but unverified. His June 29 opt-out is specific to his account and cannot be transferred to Buckmaster. | See the source-specific verification rows and the shared search log. |

### Corrections & Updates

| Item | URL | Published | Corrected/Updated | What Changed | Impacted Claim IDs | Action Taken |
|---|---|---|---|---|---|---|
| 1 | https://mathstodon.xyz/@andreasthom/117240535270608201 | 2026-09-09 | Capture/review 2026-09-10 | Initial thread-context response omitted parts 2/3 and 3/3. Both were recovered through the author’s account-status endpoint, along with the separate June 29 opt-out reply. No later rebuttal from Sellke was established by the available searches. | INST-2026-320, INST-2026-321, INST-2026-322 | Retain raw records and distinct versions; do not overwrite prior-source wording. |

### Internal Tensions / Self-Contradictions

The quoted email is firsthand testimony; its complete context, underlying account records and Sellke’s response to the new criticism were not recovered. Thom’s inference that a prior answer addressed only direct access is plausible but unverified. His June 29 opt-out is specific to his account and cannot be transferred to Buckmaster. No additional internal contradiction is inferred merely from disagreement with another participant.

### Persuasion Techniques

Quoting the short categorical answer contrasts with Thom’s explicitly two-part question. “Dishonesty” is his inference about intent. The more directly testable criticism is that no public basis for the denial is supplied.

### Unstated Assumptions

| Assumption | Claim ID | Critical? | Problematic? |
|---|---|---|---|
| Public statements reliably establish what a participant asserts, but not every underlying private event. | INST-2026-320 | Y | N for attribution; Y if extended to conduct |
| A categorical answer could have been based on account-specific exclusion that is not public. Public literature could explain the mathematical route. The Navier–Stokes caveat does not logically prove a different answer in a different case was false. | INST-2026-322 | Y for broad conclusions | Remains an alternative to test |

### Evidence Assessment

The quoted email is firsthand testimony; its complete context, underlying account records and Sellke’s response to the new criticism were not recovered. Thom’s inference that a prior answer addressed only direct access is plausible but unverified. His June 29 opt-out is specific to his account and cannot be transferred to Buckmaster. Repetition across news outlets is not counted as independent confirmation when they rely on the same post, statement or briefing.

### Credence Assessment

**Credence in this source analysis: 0.85.** The content and attributed positions are captured; private data lineage, intent and full mathematical validation remain outside this pass. Use the claim-specific probabilities rather than averaging them into a verdict about the entire controversy.

## Stage 3: Dialectical Analysis

### Steelmanned Argument

Only the provider can inspect datasets and checkpoints; requiring users to prove a hidden pipeline’s behavior reverses the practical burden of transparency. Removing a name does not remove an idea.

### Strongest Counterarguments

A categorical answer could have been based on account-specific exclusion that is not public. Public literature could explain the mathematical route. The Navier–Stokes caveat does not logically prove a different answer in a different case was false.

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

Only the provider can inspect datasets and checkpoints; requiring users to prove a hidden pipeline’s behavior reverses the practical burden of transparency. Removing a name does not remove an idea. A categorical answer could have been based on account-specific exclusion that is not public. Public literature could explain the mathematical route. The Navier–Stokes caveat does not logically prove a different answer in a different case was false. See the [cross-source synthesis](../syntheses/navier-stokes-2026-research-credit-data-value-chain.md) for the dated timeline, allegation matrix, bibliography amendment and implications for customer competition.

### Claims to Cross-Reference

[alpoge-2026-training-authorship-response](alpoge-2026-training-authorship-response.md), [openai-2026-navier-stokes-data-response](openai-2026-navier-stokes-data-response.md), [thom-2026-unpublished-math-transparency](thom-2026-unpublished-math-transparency.md). Existing database claims INST-2026-981 (customer-IP allegation), ECON-2026-984 (context ownership) and INST-2026-992 (portfolio posture) are related frameworks, not proof of this incident.

### Claim Summary

| ID | Type | Domain | Layer | Actor | Scope | Quantifier | Evidence | Credence | Claim |
|---|---|---|---|---|---|---|---|---|---|
| INST-2026-320 | [F] | INST | ASSERTED | OTHER:Andreas Thom | who=researchers and AI providers; where=public record; when=2026-09-10 review; process=research and publication | some | E5 | 0.93 | Thom quotes a prior two-part question about training and solving-time access and Sellke’s answer, “Regarding your conversations with ChatGPT: that did not happen.” |
| INST-2026-321 | [F] | INST | ASSERTED | OTHER:Andreas Thom | who=researchers and AI providers; where=public record; when=2026-09-10 review; process=research and publication | some | E5 | 0.97 | Thom states he disabled model training on June 29 and argues this leaves earlier conversations and derivatives unresolved. |
| INST-2026-322 | [T] | INST | EFFECT | OTHER:Andreas Thom | who=researchers and AI providers; where=public record; when=2026-09-10 review; process=research and publication | some | E5 | 0.95 | De-identification of research conversations does not by itself remove their mathematical ideas or settle credit for their subsequent use. |

### Claims to Register

```yaml
claims:
- id: INST-2026-320
  text: 'Thom quotes a prior two-part question about training and solving-time access and Sellke’s answer, “Regarding
    your conversations with ChatGPT: that did not happen.”'
  type: '[F]'
  domain: INST
  evidence_level: E5
  credence: 0.93
  operationalization: Check the cited primary record, versions and counterevidence. Verified as Thom’s published
    account; original email files were not independently authenticated.
  assumptions:
  - Attribution does not independently establish the underlying allegation.
  falsifiers:
  - Authenticated source records contradicting the attribution or chronology.
  source_ids:
  - thom-2026-unpublished-math-transparency
  first_extracted: '2026-09-10'
  last_updated: '2026-09-10'
  extracted_by: codex
  version: 1
- id: INST-2026-321
  text: Thom states he disabled model training on June 29 and argues this leaves earlier conversations and derivatives
    unresolved.
  type: '[F]'
  domain: INST
  evidence_level: E5
  credence: 0.97
  operationalization: Check the cited primary record, versions and counterevidence. Stated in part 2/3 and a separate
    reply; year inferred from the September 2026 discussion.
  assumptions:
  - Attribution does not independently establish the underlying allegation.
  falsifiers:
  - Authenticated source records contradicting the attribution or chronology.
  source_ids:
  - thom-2026-unpublished-math-transparency
  first_extracted: '2026-09-10'
  last_updated: '2026-09-10'
  extracted_by: codex
  version: 1
- id: INST-2026-322
  text: De-identification of research conversations does not by itself remove their mathematical ideas or settle
    credit for their subsequent use.
  type: '[T]'
  domain: INST
  evidence_level: E5
  credence: 0.95
  operationalization: Check the cited primary record, versions and counterevidence. Distinguishes identity protection
    from information content; an empirical data-lineage audit is still needed in any individual case.
  assumptions:
  - Mechanism or inference is bounded by the stated conditions; no universal effect assumed.
  falsifiers:
  - A demonstrated transformation removing all relevant technical content, not just identifying metadata.
  source_ids:
  - thom-2026-unpublished-math-transparency
  - openai-2026-navier-stokes-data-response
  - alpoge-2026-training-authorship-response
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
| 1 | 2026-09-10 | codex | gpt-6 | Shared multi-source pass; not separately measured | unavailable | unavailable | ANALYSIS-2026-185; three-stage analysis, source comparison and neutral prose pass. Session ambiguity prevents reliable per-source usage attribution. |

### Revision Notes

**Pass 1:** Captured source and replies; separated assertions, contested facts and analyst implications; retained corrections and capture limitations. Registration and provenance recorded in the shared package.
