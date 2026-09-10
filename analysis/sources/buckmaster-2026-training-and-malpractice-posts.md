# Source Analysis: Training chronology and academic-malpractice criticism

> **Claim types**: `[F]` fact (including attributed statements), `[T]` theory, `[H]` hypothesis, `[P]` prediction, `[A]` assumption, `[C]` counterfactual, `[S]` speculation, `[X]` contradiction.
> **Evidence**: E1 systematic review; E2 peer-reviewed/official statistics; E3 expert/preprint; E4 reporting/industry documents; E5 firsthand statement/opinion; E6 unsupported inference. **Status**: `ok` verified at the stated scope; `x` refuted; `nf` searched but not established; `blocked` inaccessible; `?` unattempted.
> High credence in an attributed statement means confidence that it was said, not that the underlying allegation is true. Evidence category is not a mechanical probability cap. Tested implications are analyst formulations, not quotations. All files in this package remain **DRAFT** because provenance and scientific acceptance are unresolved.

## Metadata

| Field | Value |
|---|---|
| **Source ID** | buckmaster-2026-training-and-malpractice-posts |
| **Title** | Training chronology and academic-malpractice criticism |
| **Author(s)** | Tristan Buckmaster |
| **Date** | 2026-09-08 |
| **Type** | SOCIAL |
| **URL** | https://mastodon.social/@tristanbuckmaster/117236471352470303 |
| **Reliability** | 0.80 for recoverable source content; see claim-specific scope |
| **Rigor Level** | DRAFT |
| **Capture** | [Target text](../../reference/captured/navier-stokes-2026/buckmaster-target.txt); raw captures and hashes in the [capture directory](../../reference/captured/navier-stokes-2026/) |

## Stage 1: Descriptive Analysis

### Core Thesis

Buckmaster’s later posts move from uncertainty to suspicion that unpublished research may have influenced training, and amplify a criticism of the proof’s bibliography.

### Key Claims

| # | Claim | Claim ID | Layer | Actor | Scope | Quantifier | Type | Domain | Evid | Credence | Verified? | Falsifiable By |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | Buckmaster’s September 8 follow-up calls the situation “absolute academic malpractice” and says, as he understands it, their unpublished hypodissipative result was part of OpenAI’s training data. | INST-2026-305 | ASSERTED | OTHER:Tristan Buckmaster | who=researchers and AI providers; where=public record; when=2026-09-10 review; process=research and publication | some | [F] | INST | E5 | 0.98 | ok; see verification row | Authenticated source records contradicting the attribution or chronology. |
| 2 | OpenAI trained on Buckmaster and Alpöge’s unpublished mathematical work and that training materially helped its Navier–Stokes result. | INST-2026-306 | EFFECT | OTHER:Tristan Buckmaster | who=researchers and AI providers; where=public record; when=2026-09-10 review; process=research and publication | some | [H] | INST | E6 | 0.35 | nf; see verification row | Audited exclusion of all relevant original and derived data from relevant checkpoints, or a controlled ablation establishing no material influence. |
| 3 | The bibliography screenshot amplified by Buckmaster omits Córdoba and Martínez-Zoroa, whereas the PDF retrieved on September 10 cites their forced-blowup work and discusses its relation to the construction. | INST-2026-307 | ASSERTED | OTHER:Tristan Buckmaster | who=researchers and AI providers; where=public record; when=2026-09-10 review; process=research and publication | some | [F] | INST | E4 | 0.99 | ok; see verification row | Authenticated source records contradicting the attribution or chronology. |

### Argument Structure

```text
August research predates an ongoing training run → possible exposure of unpublished ideas → questions about scooping customers; screenshot of omitted citations → academic-malpractice criticism.
```

**Weakest link:** Training after a discovery does not establish that the discovery entered the training set. A stronger downstream theorem also cannot disprove upstream influence. The attached bibliography screenshot and the current PDF differ; the citation allegation must be version-specific.

### Theoretical Lineage

Research priority, contributor credit, information asymmetry and platform competition. The relevant existing framework is [the July value-chain essay](lhl-2026-ai-value-chain.md), with earlier database context in [the Palantir/extraction synthesis](../syntheses/palantir-sovereign-ai-frontier-lab-extraction-synthesis.md). These are analyst cross-references, not claims that this source explicitly cites that framework.

### Scope & Limitations

This pass assesses the source’s contribution to the September controversy and the customer-value question. It does not certify a fluid-dynamics theorem or reconstruct undisclosed account histories. Public testimony, press repetition, formal theorem statements and causal training evidence have different evidentiary roles.

## Stage 2: Evaluative Analysis

### Internal Coherence

Training after a discovery does not establish that the discovery entered the training set. A stronger downstream theorem also cannot disprove upstream influence. The attached bibliography screenshot and the current PDF differ; the citation allegation must be version-specific.

### Key Factual Claims Verified

The first factual row is a crux of this source’s contribution. For attributed statements, `ok` verifies attribution only. Rows testing implications are labeled by claim type above.

| Claim ID | Claim (paraphrased) | Crux? | Source Says | Actual | External Source | Search Notes | Status |
|---|---|---|---|---|---|---|---|
| INST-2026-305 | Buckmaster’s September 8 follow-up calls the situation “absolute academic malpractice” and says, as he understands it, their unpublished hypodissipative result was part of OpenAI’s training data. | Y | Attributed record | Verified as his later allegation, not as a verified account of training ingestion. | [bastian-2026-navier-stokes-trust](bastian-2026-navier-stokes-trust.md); [primary](https://mastodon.social/@tristanbuckmaster/117236471352470303) | 2026-09-10: corpus q1='academic malpractice'; q2='hypodissipative'. Web discovery and DB-first attempts: capture-method.md; exact hits: claim-verification-searches.json. | ok |
| INST-2026-306 | OpenAI trained on Buckmaster and Alpöge’s unpublished mathematical work and that training materially helped its Navier–Stokes result. | N | Analyst tests the source’s mechanism or a disputed implication; not a quotation | Not established. OpenAI leaves training influence open; no dataset manifest, account-specific lineage or causal ablation was supplied. | [openai-2026-navier-stokes-data-response](openai-2026-navier-stokes-data-response.md), [alpoge-2026-training-authorship-response](alpoge-2026-training-authorship-response.md), [thom-2026-unpublished-math-transparency](thom-2026-unpublished-math-transparency.md); [primary](https://mastodon.social/@tristanbuckmaster/117236471352470303) | 2026-09-10: corpus q1='de-identified'; q2='training data'. Web discovery and DB-first attempts: capture-method.md; exact hits: claim-verification-searches.json. | nf |
| INST-2026-307 | The bibliography screenshot amplified by Buckmaster omits Córdoba and Martínez-Zoroa, whereas the PDF retrieved on September 10 cites their forced-blowup work and discusses its relation to the construction. | N | Attributed record | Confirmed against independently archived September 8 PDFs: 16 references at 17:29:48 UTC, 22 at 20:04:49 UTC. The later copy includes the previously missing Córdoba/Martínez-Zoroa literature. This verifies the omission and amendment, not plagiarism or motivation. | [openai-2026-navier-stokes-solution](openai-2026-navier-stokes-solution.md); [primary](https://mastodon.social/@tristanbuckmaster/117236471352470303) | 2026-09-10: corpus q1='Córdoba'; q2='References'. Web discovery and DB-first attempts: capture-method.md; exact hits: claim-verification-searches.json. | ok |

### Disconfirming Evidence Search

| Claim | Counterevidence / alternative | Search notes |
|---|---|---|
| INST-2026-305 | Timing and thematic similarity are circumstantial. Public prior literature and independent agent exploration remain plausible. Buckmaster’s nonpublic hypodissipative manuscript was not available for comparison. | Primary-source comparison plus two recorded phrase queries per claim; disputed positions retained. |
| INST-2026-307 | Training after a discovery does not establish that the discovery entered the training set. A stronger downstream theorem also cannot disprove upstream influence. The attached bibliography screenshot and the current PDF differ; the citation allegation must be version-specific. | See the source-specific verification rows and the shared search log. |

### Corrections & Updates

| Item | URL | Published | Corrected/Updated | What Changed | Impacted Claim IDs | Action Taken |
|---|---|---|---|---|---|---|
| 1 | https://mastodon.social/@tristanbuckmaster/117236471352470303 | 2026-09-08 | Capture/review 2026-09-10 | Recovered original post, a later post (117237555794407063), account history and screenshot through Mastodon APIs. Screenshot identifies Gonzalo Cao-Labora as the bibliography critic. Current PDF includes Córdoba and Martínez-Zoroa; never describe all versions as omitting them. Independent Wayback captures at 17:29:48 and 20:04:49 UTC on September 8 confirm an earlier 16-entry bibliography and a later 22-entry bibliography with Córdoba/Martínez-Zoroa citations and a new historical discussion. This brackets an observed change, not its precise publication time. See proof-version-diff.txt. | INST-2026-305, INST-2026-306, INST-2026-307 | Retain raw records and distinct versions; do not overwrite prior-source wording. |

### Internal Tensions / Self-Contradictions

Training after a discovery does not establish that the discovery entered the training set. A stronger downstream theorem also cannot disprove upstream influence. The attached bibliography screenshot and the current PDF differ; the citation allegation must be version-specific. No additional internal contradiction is inferred merely from disagreement with another participant.

### Persuasion Techniques

The rhetorical question about scooping shifts from a known training chronology to an unproved data-use inference. “Absolute academic malpractice” expresses condemnation; the attached bibliography criticism has a separately verifiable factual core.

### Unstated Assumptions

| Assumption | Claim ID | Critical? | Problematic? |
|---|---|---|---|
| Public statements reliably establish what a participant asserts, but not every underlying private event. | INST-2026-305 | Y | N for attribution; Y if extended to conduct |
| Timing and thematic similarity are circumstantial. Public prior literature and independent agent exploration remain plausible. Buckmaster’s nonpublic hypodissipative manuscript was not available for comparison. | INST-2026-307 | Y for broad conclusions | Remains an alternative to test |

### Evidence Assessment

Training after a discovery does not establish that the discovery entered the training set. A stronger downstream theorem also cannot disprove upstream influence. The attached bibliography screenshot and the current PDF differ; the citation allegation must be version-specific. Repetition across news outlets is not counted as independent confirmation when they rely on the same post, statement or briefing.

### Credence Assessment

**Credence in this source analysis: 0.85.** The content and attributed positions are captured; private data lineage, intent and full mathematical validation remain outside this pass. Use the claim-specific probabilities rather than averaging them into a verdict about the entire controversy.

## Stage 3: Dialectical Analysis

### Steelmanned Argument

A provider that retains drafts and performs ongoing training bears an evidentiary burden to explain provenance when it subsequently competes with users in the same research area.

### Strongest Counterarguments

Timing and thematic similarity are circumstantial. Public prior literature and independent agent exploration remain plausible. Buckmaster’s nonpublic hypodissipative manuscript was not available for comparison.

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

A provider that retains drafts and performs ongoing training bears an evidentiary burden to explain provenance when it subsequently competes with users in the same research area. Timing and thematic similarity are circumstantial. Public prior literature and independent agent exploration remain plausible. Buckmaster’s nonpublic hypodissipative manuscript was not available for comparison. See the [cross-source synthesis](../syntheses/navier-stokes-2026-research-credit-data-value-chain.md) for the dated timeline, allegation matrix, bibliography amendment and implications for customer competition.

### Claims to Cross-Reference

[alpoge-2026-training-authorship-response](alpoge-2026-training-authorship-response.md), [bastian-2026-navier-stokes-trust](bastian-2026-navier-stokes-trust.md), [openai-2026-navier-stokes-data-response](openai-2026-navier-stokes-data-response.md), [openai-2026-navier-stokes-solution](openai-2026-navier-stokes-solution.md), [thom-2026-unpublished-math-transparency](thom-2026-unpublished-math-transparency.md). Existing database claims INST-2026-981 (customer-IP allegation), ECON-2026-984 (context ownership) and INST-2026-992 (portfolio posture) are related frameworks, not proof of this incident.

### Claim Summary

| ID | Type | Domain | Layer | Actor | Scope | Quantifier | Evidence | Credence | Claim |
|---|---|---|---|---|---|---|---|---|---|
| INST-2026-305 | [F] | INST | ASSERTED | OTHER:Tristan Buckmaster | who=researchers and AI providers; where=public record; when=2026-09-10 review; process=research and publication | some | E5 | 0.98 | Buckmaster’s September 8 follow-up calls the situation “absolute academic malpractice” and says, as he understands it, their unpublished hypodissipative result was part of OpenAI’s training data. |
| INST-2026-306 | [H] | INST | EFFECT | OTHER:Tristan Buckmaster | who=researchers and AI providers; where=public record; when=2026-09-10 review; process=research and publication | some | E6 | 0.35 | OpenAI trained on Buckmaster and Alpöge’s unpublished mathematical work and that training materially helped its Navier–Stokes result. |
| INST-2026-307 | [F] | INST | ASSERTED | OTHER:Tristan Buckmaster | who=researchers and AI providers; where=public record; when=2026-09-10 review; process=research and publication | some | E4 | 0.99 | The bibliography screenshot amplified by Buckmaster omits Córdoba and Martínez-Zoroa, whereas the PDF retrieved on September 10 cites their forced-blowup work and discusses its relation to the construction. |

### Claims to Register

```yaml
claims:
- id: INST-2026-305
  text: Buckmaster’s September 8 follow-up calls the situation “absolute academic malpractice” and says, as he understands
    it, their unpublished hypodissipative result was part of OpenAI’s training data.
  type: '[F]'
  domain: INST
  evidence_level: E5
  credence: 0.98
  operationalization: Check the cited primary record, versions and counterevidence. Verified as his later allegation,
    not as a verified account of training ingestion.
  assumptions:
  - Attribution does not independently establish the underlying allegation.
  falsifiers:
  - Authenticated source records contradicting the attribution or chronology.
  source_ids:
  - buckmaster-2026-training-and-malpractice-posts
  - bastian-2026-navier-stokes-trust
  first_extracted: '2026-09-10'
  last_updated: '2026-09-10'
  extracted_by: codex
  version: 1
- id: INST-2026-306
  text: OpenAI trained on Buckmaster and Alpöge’s unpublished mathematical work and that training materially helped
    its Navier–Stokes result.
  type: '[H]'
  domain: INST
  evidence_level: E6
  credence: 0.35
  operationalization: Check the cited primary record, versions and counterevidence. Not established. OpenAI leaves
    training influence open; no dataset manifest, account-specific lineage or causal ablation was supplied.
  assumptions:
  - Mechanism or inference is bounded by the stated conditions; no universal effect assumed.
  falsifiers:
  - Audited exclusion of all relevant original and derived data from relevant checkpoints, or a controlled ablation
    establishing no material influence.
  source_ids:
  - buckmaster-2026-training-and-malpractice-posts
  - openai-2026-navier-stokes-data-response
  - alpoge-2026-training-authorship-response
  - thom-2026-unpublished-math-transparency
  first_extracted: '2026-09-10'
  last_updated: '2026-09-10'
  extracted_by: codex
  version: 1
- id: INST-2026-307
  text: The bibliography screenshot amplified by Buckmaster omits Córdoba and Martínez-Zoroa, whereas the PDF retrieved
    on September 10 cites their forced-blowup work and discusses its relation to the construction.
  type: '[F]'
  domain: INST
  evidence_level: E4
  credence: 0.99
  operationalization: 'Check the cited primary record, versions and counterevidence. Confirmed against independently
    archived September 8 PDFs: 16 references at 17:29:48 UTC, 22 at 20:04:49 UTC. The later copy includes the previously
    missing Córdoba/Martínez-Zoroa literature. This verifies the omission and amendment, not plagiarism or motivation.'
  assumptions:
  - Attribution does not independently establish the underlying allegation.
  falsifiers:
  - Authenticated source records contradicting the attribution or chronology.
  source_ids:
  - buckmaster-2026-training-and-malpractice-posts
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
| 1 | 2026-09-10 | codex | gpt-6 | Shared multi-source pass; not separately measured | unavailable | unavailable | ANALYSIS-2026-179; three-stage analysis, source comparison and neutral prose pass. Session ambiguity prevents reliable per-source usage attribution. |

### Revision Notes

**Pass 1:** Captured source and replies; separated assertions, contested facts and analyst implications; retained corrections and capture limitations. Registration and provenance recorded in the shared package.
