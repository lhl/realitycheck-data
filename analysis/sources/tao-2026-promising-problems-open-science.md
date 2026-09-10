# Source Analysis: Promising problems, solution extraction and open-science incentives

> **Claim types**: `[F]` fact (including attributed statements), `[T]` theory, `[H]` hypothesis, `[P]` prediction, `[A]` assumption, `[C]` counterfactual, `[S]` speculation, `[X]` contradiction.
> **Evidence**: E1 systematic review; E2 peer-reviewed/official statistics; E3 expert/preprint; E4 reporting/industry documents; E5 firsthand statement/opinion; E6 unsupported inference. **Status**: `ok` verified at the stated scope; `x` refuted; `nf` searched but not established; `blocked` inaccessible; `?` unattempted.
> High credence in an attributed statement means confidence that it was said, not that the underlying allegation is true. Evidence category is not a mechanical probability cap. Tested implications are analyst formulations, not quotations. All files in this package remain **DRAFT** because provenance and scientific acceptance are unresolved.

## Metadata

| Field | Value |
|---|---|
| **Source ID** | tao-2026-promising-problems-open-science |
| **Title** | Promising problems, solution extraction and open-science incentives |
| **Author(s)** | Terence Tao |
| **Date** | 2026-09-08 |
| **Type** | SOCIAL |
| **URL** | https://mathstodon.xyz/@tao/117237320796901560 |
| **Reliability** | 0.80 for recoverable source content; see claim-specific scope |
| **Rigor Level** | DRAFT |
| **Capture** | [Target text](../../reference/captured/navier-stokes-2026/tao-target.txt); raw captures and hashes in the [capture directory](../../reference/captured/navier-stokes-2026/) |

## Stage 1: Descriptive Analysis

### Core Thesis

Tao argues that identifying fruitful problems depends on understanding a field’s difficulty landscape, and that rapid opaque solution extraction can undermine both that knowledge and incentives to share research directions.

### Key Claims

| # | Claim | Claim ID | Layer | Actor | Scope | Quantifier | Type | Domain | Evid | Credence | Verified? | Falsifiable By |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | Tao explicitly argues that even a rumor of promising research can trigger massive AI effort and incentivize researchers to stop sharing directions. | INST-2026-323 | ASSERTED | OTHER:Terence Tao | who=researchers and AI providers; where=public record; when=2026-09-10 review; process=research and publication | some | [F] | INST | E5 | 0.99 | ok; see verification row | Authenticated source records contradicting the attribution or chronology. |
| 2 | Rewarding rapid opaque solution extraction over explanation and problem cultivation can reduce open sharing and weaken future mathematical discovery. | RISK-2026-300 | EFFECT | OTHER:Terence Tao | who=researchers and AI providers; where=public record; when=2026-09-10 review; process=research and publication | some | [H] | RISK | E5 | 0.70 | ok; see verification row | Longitudinal evidence showing equal or greater early sharing, useful problem generation and accessible explanatory output despite comparable competitive incentives. |

### Argument Structure

```text
Fruitful problems require cultivation → powerful tools change difficulty → opaque successes and unreported failures obscure boundaries → rumors trigger competing runs → secrecy incentives and weaker future problem formation.
```

**Weakest link:** The mechanism is coherent but prospective; no longitudinal measurement of sharing or problem scarcity is presented. Tao explicitly says mathematical problems are unlimited and AI-hard problems still exist. His claim is about useful selection and understanding, not exhaustion of all mathematics.

### Theoretical Lineage

Research priority, contributor credit, information asymmetry and platform competition. The relevant existing framework is [the July value-chain essay](lhl-2026-ai-value-chain.md), with earlier database context in [the Palantir/extraction synthesis](../syntheses/palantir-sovereign-ai-frontier-lab-extraction-synthesis.md). These are analyst cross-references, not claims that this source explicitly cites that framework.

### Scope & Limitations

This pass assesses the source’s contribution to the September controversy and the customer-value question. It does not certify a fluid-dynamics theorem or reconstruct undisclosed account histories. Public testimony, press repetition, formal theorem statements and causal training evidence have different evidentiary roles.

## Stage 2: Evaluative Analysis

### Internal Coherence

The mechanism is coherent but prospective; no longitudinal measurement of sharing or problem scarcity is presented. Tao explicitly says mathematical problems are unlimited and AI-hard problems still exist. His claim is about useful selection and understanding, not exhaustion of all mathematics.

### Key Factual Claims Verified

The first factual row is a crux of this source’s contribution. For attributed statements, `ok` verifies attribution only. Rows testing implications are labeled by claim type above.

| Claim ID | Claim (paraphrased) | Crux? | Source Says | Actual | External Source | Search Notes | Status |
|---|---|---|---|---|---|---|---|
| INST-2026-323 | Tao explicitly argues that even a rumor of promising research can trigger massive AI effort and incentivize researchers to stop sharing directions. | Y | Attributed record | Part 3/4 states the mechanism; these reports repeat it rather than independently measuring the effect. | [bastian-2026-navier-stokes-trust](bastian-2026-navier-stokes-trust.md), [fernandez-perez-2026-navier-stokes-plagiarism-dispute](fernandez-perez-2026-navier-stokes-plagiarism-dispute.md); [primary](https://mathstodon.xyz/@tao/117237320796901560) | 2026-09-10: corpus q1='rumor'; q2='no longer sharing'. Web discovery and DB-first attempts: capture-method.md; exact hits: claim-verification-searches.json. | ok |
| RISK-2026-300 | Rewarding rapid opaque solution extraction over explanation and problem cultivation can reduce open sharing and weaken future mathematical discovery. | N | Analyst tests the source’s mechanism or a disputed implication; not a quotation | Plausible incentive mechanism with an illustrative case; long-run net effect is not measured. | [buckmaster-2026-navier-stokes-statement](buckmaster-2026-navier-stokes-statement.md), [openai-2026-navier-stokes-solution](openai-2026-navier-stokes-solution.md); [primary](https://mathstodon.xyz/@tao/117237320796901560) | 2026-09-10: corpus q1='difficulty landscape'; q2='negative results'. Web discovery and DB-first attempts: capture-method.md; exact hits: claim-verification-searches.json. | ok |

### Disconfirming Evidence Search

| Claim | Counterevidence / alternative | Search notes |
|---|---|---|
| INST-2026-323 | Automated results can reveal new structures and generate new worthwhile problems. Faster solution and explanation tools may improve the very landscape Tao fears losing. The outcome depends on norms, access and the quality of explanation. | Primary-source comparison plus two recorded phrase queries per claim; disputed positions retained. |
| RISK-2026-300 | The mechanism is coherent but prospective; no longitudinal measurement of sharing or problem scarcity is presented. Tao explicitly says mathematical problems are unlimited and AI-hard problems still exist. His claim is about useful selection and understanding, not exhaustion of all mathematics. | See the source-specific verification rows and the shared search log. |

### Corrections & Updates

| Item | URL | Published | Corrected/Updated | What Changed | Impacted Claim IDs | Action Taken |
|---|---|---|---|---|---|---|
| 1 | https://mathstodon.xyz/@tao/117237320796901560 | 2026-09-08 | Capture/review 2026-09-10 | All four author posts recovered through the public status/context APIs. Replies by other users, including an account named taoish, are not Tao’s words. | INST-2026-323, RISK-2026-300 | Retain raw records and distinct versions; do not overwrite prior-source wording. |

### Internal Tensions / Self-Contradictions

The mechanism is coherent but prospective; no longitudinal measurement of sharing or problem scarcity is presented. Tao explicitly says mathematical problems are unlimited and AI-hard problems still exist. His claim is about useful selection and understanding, not exhaustion of all mathematics. No additional internal contradiction is inferred merely from disagreement with another participant.

### Persuasion Techniques

The ocean-versus-drinking-water analogy explains why infinitely many possible questions need not mean an unlimited supply of fruitful ones. The food-donation analogy argues for quality standards beyond mere correctness. Neither analogy measures the net effect of AI research tools.

### Unstated Assumptions

| Assumption | Claim ID | Critical? | Problematic? |
|---|---|---|---|
| Public statements reliably establish what a participant asserts, but not every underlying private event. | INST-2026-323 | Y | N for attribution; Y if extended to conduct |
| Automated results can reveal new structures and generate new worthwhile problems. Faster solution and explanation tools may improve the very landscape Tao fears losing. The outcome depends on norms, access and the quality of explanation. | RISK-2026-300 | Y for broad conclusions | Remains an alternative to test |

### Evidence Assessment

The mechanism is coherent but prospective; no longitudinal measurement of sharing or problem scarcity is presented. Tao explicitly says mathematical problems are unlimited and AI-hard problems still exist. His claim is about useful selection and understanding, not exhaustion of all mathematics. Repetition across news outlets is not counted as independent confirmation when they rely on the same post, statement or briefing.

### Credence Assessment

**Credence in this source analysis: 0.85.** The content and attributed positions are captured; private data lineage, intent and full mathematical validation remain outside this pass. Use the claim-specific probabilities rather than averaging them into a verdict about the entire controversy.

## Stage 3: Dialectical Analysis

### Steelmanned Argument

Incentives that reward only final solutions may consume the community’s prior investment in finding good questions while under-rewarding replenishment, exposition and negative results.

### Strongest Counterarguments

Automated results can reveal new structures and generate new worthwhile problems. Faster solution and explanation tools may improve the very landscape Tao fears losing. The outcome depends on norms, access and the quality of explanation.

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

Incentives that reward only final solutions may consume the community’s prior investment in finding good questions while under-rewarding replenishment, exposition and negative results. Automated results can reveal new structures and generate new worthwhile problems. Faster solution and explanation tools may improve the very landscape Tao fears losing. The outcome depends on norms, access and the quality of explanation. See the [cross-source synthesis](../syntheses/navier-stokes-2026-research-credit-data-value-chain.md) for the dated timeline, allegation matrix, bibliography amendment and implications for customer competition.

### Claims to Cross-Reference

[buckmaster-2026-navier-stokes-statement](buckmaster-2026-navier-stokes-statement.md), [bastian-2026-navier-stokes-trust](bastian-2026-navier-stokes-trust.md), [fernandez-perez-2026-navier-stokes-plagiarism-dispute](fernandez-perez-2026-navier-stokes-plagiarism-dispute.md), [openai-2026-navier-stokes-solution](openai-2026-navier-stokes-solution.md). Existing database claims INST-2026-981 (customer-IP allegation), ECON-2026-984 (context ownership) and INST-2026-992 (portfolio posture) are related frameworks, not proof of this incident.

### Claim Summary

| ID | Type | Domain | Layer | Actor | Scope | Quantifier | Evidence | Credence | Claim |
|---|---|---|---|---|---|---|---|---|---|
| INST-2026-323 | [F] | INST | ASSERTED | OTHER:Terence Tao | who=researchers and AI providers; where=public record; when=2026-09-10 review; process=research and publication | some | E5 | 0.99 | Tao explicitly argues that even a rumor of promising research can trigger massive AI effort and incentivize researchers to stop sharing directions. |
| RISK-2026-300 | [H] | RISK | EFFECT | OTHER:Terence Tao | who=researchers and AI providers; where=public record; when=2026-09-10 review; process=research and publication | some | E5 | 0.70 | Rewarding rapid opaque solution extraction over explanation and problem cultivation can reduce open sharing and weaken future mathematical discovery. |

### Claims to Register

```yaml
claims:
- id: INST-2026-323
  text: Tao explicitly argues that even a rumor of promising research can trigger massive AI effort and incentivize
    researchers to stop sharing directions.
  type: '[F]'
  domain: INST
  evidence_level: E5
  credence: 0.99
  operationalization: Check the cited primary record, versions and counterevidence. Part 3/4 states the mechanism;
    these reports repeat it rather than independently measuring the effect.
  assumptions:
  - Attribution does not independently establish the underlying allegation.
  falsifiers:
  - Authenticated source records contradicting the attribution or chronology.
  source_ids:
  - tao-2026-promising-problems-open-science
  - bastian-2026-navier-stokes-trust
  - fernandez-perez-2026-navier-stokes-plagiarism-dispute
  first_extracted: '2026-09-10'
  last_updated: '2026-09-10'
  extracted_by: codex
  version: 1
- id: RISK-2026-300
  text: Rewarding rapid opaque solution extraction over explanation and problem cultivation can reduce open sharing
    and weaken future mathematical discovery.
  type: '[H]'
  domain: RISK
  evidence_level: E5
  credence: 0.7
  operationalization: Check the cited primary record, versions and counterevidence. Plausible incentive mechanism
    with an illustrative case; long-run net effect is not measured.
  assumptions:
  - Mechanism or inference is bounded by the stated conditions; no universal effect assumed.
  falsifiers:
  - Longitudinal evidence showing equal or greater early sharing, useful problem generation and accessible explanatory
    output despite comparable competitive incentives.
  source_ids:
  - tao-2026-promising-problems-open-science
  - buckmaster-2026-navier-stokes-statement
  - openai-2026-navier-stokes-solution
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
| 1 | 2026-09-10 | codex | gpt-6 | Shared multi-source pass; not separately measured | unavailable | unavailable | ANALYSIS-2026-186; three-stage analysis, source comparison and neutral prose pass. Session ambiguity prevents reliable per-source usage attribution. |

### Revision Notes

**Pass 1:** Captured source and replies; separated assertions, contested facts and analyst implications; retained corrections and capture limitations. Registration and provenance recorded in the shared package.
