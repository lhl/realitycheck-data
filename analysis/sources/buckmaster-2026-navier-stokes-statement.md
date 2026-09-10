# Source Analysis: Statement on fluid blowup results and OpenAI discussions

> **Claim types**: `[F]` fact (including attributed statements), `[T]` theory, `[H]` hypothesis, `[P]` prediction, `[A]` assumption, `[C]` counterfactual, `[S]` speculation, `[X]` contradiction.
> **Evidence**: E1 systematic review; E2 peer-reviewed/official statistics; E3 expert/preprint; E4 reporting/industry documents; E5 firsthand statement/opinion; E6 unsupported inference. **Status**: `ok` verified at the stated scope; `x` refuted; `nf` searched but not established; `blocked` inaccessible; `?` unattempted.
> High credence in an attributed statement means confidence that it was said, not that the underlying allegation is true. Evidence category is not a mechanical probability cap. Tested implications are analyst formulations, not quotations. All files in this package remain **DRAFT** because provenance and scientific acceptance are unresolved.

## Metadata

| Field | Value |
|---|---|
| **Source ID** | buckmaster-2026-navier-stokes-statement |
| **Title** | Statement on fluid blowup results and OpenAI discussions |
| **Author(s)** | Tristan Buckmaster |
| **Date** | 2026-09-08 |
| **Type** | REPORT (statement) |
| **URL** | https://cims.nyu.edu/~tristanb/statement.pdf |
| **Reliability** | 0.80 for recoverable source content; see claim-specific scope |
| **Rigor Level** | DRAFT |
| **Capture** | [Target text](../../reference/captured/navier-stokes-2026/buckmaster-pdf-target.txt); raw captures and hashes in the [capture directory](../../reference/captured/navier-stokes-2026/) |

## Stage 1: Descriptive Analysis

### Core Thesis

Buckmaster credits Córdoba and Martínez-Zoroa’s program and AI assistance for joint results with Alpöge, then documents publication pressure and disputes over authorship, training provenance and the portrayal of OpenAI’s contribution.

### Key Claims

| # | Claim | Claim ID | Layer | Actor | Scope | Quantifier | Type | Domain | Evid | Credence | Verified? | Falsifiable By |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | Buckmaster reports obtaining smooth-forced Euler and Boussinesq blowup results with Alpöge on August 15 and Lean verification on August 22, building on Córdoba and Martínez-Zoroa. | INST-2026-301 | ASSERTED | OTHER:Tristan Buckmaster | who=researchers and AI providers; where=public record; when=2026-09-10 review; process=research and publication | some | [F] | INST | E5 | 0.85 | ok; see verification row | Authenticated source records contradicting the attribution or chronology. |
| 2 | Buckmaster’s statement quotes the career remark and describes offers to coordinate releases or have him write OpenAI’s Navier–Stokes result without Alpöge. | INST-2026-302 | ASSERTED | OTHER:Tristan Buckmaster | who=researchers and AI providers; where=public record; when=2026-09-10 review; process=research and publication | some | [F] | INST | E5 | 0.97 | ok; see verification row | Authenticated source records contradicting the attribution or chronology. |
| 3 | Buckmaster expressly says in his initial statement that he does not know whether his and Alpöge’s data was used by OpenAI. | INST-2026-303 | ASSERTED | OTHER:Tristan Buckmaster | who=researchers and AI providers; where=public record; when=2026-09-10 review; process=research and publication | some | [F] | INST | E5 | 0.99 | ok; see verification row | Authenticated source records contradicting the attribution or chronology. |
| 4 | The publication discussions exerted coercive pressure on Buckmaster to accept an account of authorship and credit shaped by institutional rivalry. | INST-2026-304 | EFFECT | OTHER:Tristan Buckmaster | who=researchers and AI providers; where=public record; when=2026-09-10 review; process=research and publication | some | [H] | INST | E5 | 0.75 | ok; see verification row | Complete contemporaneous correspondence and recordings showing no conditional pressure and a materially different negotiation context. |

### Argument Structure

```text
Year-long personal collaboration → August results → rumors and September emails → September 6 calls → disputed publication offers and career remark → rushed public release with an explicit uncertainty statement about data use.
```

**Weakest link:** This is detailed firsthand testimony with quoted emails, but no complete independently authenticated call recording. Bubeck confirms the rewrite proposal, affiliation concern and career remark while contesting intent. Alpöge was not on the calls and is not an independent witness to all of them. The statement’s final page expressly says Buckmaster does not know whether their data was used.

### Theoretical Lineage

Research priority, contributor credit, information asymmetry and platform competition. The relevant existing framework is [the July value-chain essay](lhl-2026-ai-value-chain.md), with earlier database context in [the Palantir/extraction synthesis](../syntheses/palantir-sovereign-ai-frontier-lab-extraction-synthesis.md). These are analyst cross-references, not claims that this source explicitly cites that framework.

### Scope & Limitations

This pass assesses the source’s contribution to the September controversy and the customer-value question. It does not certify a fluid-dynamics theorem or reconstruct undisclosed account histories. Public testimony, press repetition, formal theorem statements and causal training evidence have different evidentiary roles.

## Stage 2: Evaluative Analysis

### Internal Coherence

This is detailed firsthand testimony with quoted emails, but no complete independently authenticated call recording. Bubeck confirms the rewrite proposal, affiliation concern and career remark while contesting intent. Alpöge was not on the calls and is not an independent witness to all of them. The statement’s final page expressly says Buckmaster does not know whether their data was used.

### Key Factual Claims Verified

The first factual row is a crux of this source’s contribution. For attributed statements, `ok` verifies attribution only. Rows testing implications are labeled by claim type above.

| Claim ID | Claim (paraphrased) | Crux? | Source Says | Actual | External Source | Search Notes | Status |
|---|---|---|---|---|---|---|---|
| INST-2026-301 | Buckmaster reports obtaining smooth-forced Euler and Boussinesq blowup results with Alpöge on August 15 and Lean verification on August 22, building on Córdoba and Martínez-Zoroa. | Y | Attributed record | Participant chronology; Euler PDF confirms the forced setting and explicitly names the prior program. August timestamps were not independently audited. | [alpoge-2026-september-two-contact](alpoge-2026-september-two-contact.md), [maguire-bowler-2026-navier-stokes-controversy](maguire-bowler-2026-navier-stokes-controversy.md); [primary](https://cims.nyu.edu/~tristanb/statement.pdf) | 2026-09-10: corpus q1='August 15'; q2='August 22'. Web discovery and DB-first attempts: capture-method.md; exact hits: claim-verification-searches.json. | ok |
| INST-2026-302 | Buckmaster’s statement quotes the career remark and describes offers to coordinate releases or have him write OpenAI’s Navier–Stokes result without Alpöge. | N | Attributed record | Bubeck and Altman corroborate the broad rewrite proposal; Bubeck acknowledges the career wording while disputing intent and the removal characterization. | [bubeck-2026-navier-stokes-response](bubeck-2026-navier-stokes-response.md), [altman-2026-navier-stokes-defense](altman-2026-navier-stokes-defense.md); [primary](https://cims.nyu.edu/~tristanb/statement.pdf) | 2026-09-10: corpus q1='career'; q2='lead author'. Web discovery and DB-first attempts: capture-method.md; exact hits: claim-verification-searches.json. | ok |
| INST-2026-303 | Buckmaster expressly says in his initial statement that he does not know whether his and Alpöge’s data was used by OpenAI. | N | Attributed record | Page 4 states this directly; later suspicion is not an admission in this initial statement. | [maguire-bowler-2026-navier-stokes-controversy](maguire-bowler-2026-navier-stokes-controversy.md); [primary](https://cims.nyu.edu/~tristanb/statement.pdf) | 2026-09-10: corpus q1='do not know whether'; q2='not accusing'. Web discovery and DB-first attempts: capture-method.md; exact hits: claim-verification-searches.json. | ok |
| INST-2026-304 | The publication discussions exerted coercive pressure on Buckmaster to accept an account of authorship and credit shaped by institutional rivalry. | N | Analyst tests the source’s mechanism or a disputed implication; not a quotation | The career remark and affiliation restriction support this interpretation; coercive intent is disputed and there is no complete recording. | [bubeck-2026-navier-stokes-response](bubeck-2026-navier-stokes-response.md), [alpoge-2026-training-authorship-response](alpoge-2026-training-authorship-response.md), [altman-2026-navier-stokes-defense](altman-2026-navier-stokes-defense.md); [primary](https://cims.nyu.edu/~tristanb/statement.pdf) | 2026-09-10: corpus q1='nice'; q2='Anthropic employee'. Web discovery and DB-first attempts: capture-method.md; exact hits: claim-verification-searches.json. | ok |

### Disconfirming Evidence Search

| Claim | Counterevidence / alternative | Search notes |
|---|---|---|
| INST-2026-301 | The disputed offer may concern a new writeup of OpenAI’s work, rather than removing Alpöge from the existing joint Euler paper. A concern about sharing unreleased model IP with a competitor’s employee can be legitimate without settling how that concern was communicated. | Primary-source comparison plus two recorded phrase queries per claim; disputed positions retained. |
| INST-2026-304 | This is detailed firsthand testimony with quoted emails, but no complete independently authenticated call recording. Bubeck confirms the rewrite proposal, affiliation concern and career remark while contesting intent. Alpöge was not on the calls and is not an independent witness to all of them. The statement’s final page expressly says Buckmaster does not know whether their data was used. | See the source-specific verification rows and the shared search log. |

### Corrections & Updates

| Item | URL | Published | Corrected/Updated | What Changed | Impacted Claim IDs | Action Taken |
|---|---|---|---|---|---|---|
| 1 | https://cims.nyu.edu/~tristanb/statement.pdf | 2026-09-08 | Capture/review 2026-09-10 | The post announcing the PDF is timestamped 2026-09-08 03:58 UTC, corresponding to September 7 late evening in New York. Later social posts make stronger allegations than the cautious final paragraph of this statement; do not merge their dates or wording. | INST-2026-301, INST-2026-302, INST-2026-303, INST-2026-304 | Retain raw records and distinct versions; do not overwrite prior-source wording. |

### Internal Tensions / Self-Contradictions

This is detailed firsthand testimony with quoted emails, but no complete independently authenticated call recording. Bubeck confirms the rewrite proposal, affiliation concern and career remark while contesting intent. Alpöge was not on the calls and is not an independent witness to all of them. The statement’s final page expressly says Buckmaster does not know whether their data was used. No additional internal contradiction is inferred merely from disagreement with another participant.

### Persuasion Techniques

Full quoted emails and a dated narrative invite readers to audit a participant account. “AI slop” is Buckmaster’s description of presentation quality, not evidence that the results are false. “Closest humans” and the career quotations should remain attributed rather than becoming analyst characterizations.

### Unstated Assumptions

| Assumption | Claim ID | Critical? | Problematic? |
|---|---|---|---|
| Public statements reliably establish what a participant asserts, but not every underlying private event. | INST-2026-301 | Y | N for attribution; Y if extended to conduct |
| The disputed offer may concern a new writeup of OpenAI’s work, rather than removing Alpöge from the existing joint Euler paper. A concern about sharing unreleased model IP with a competitor’s employee can be legitimate without settling how that concern was communicated. | INST-2026-304 | Y for broad conclusions | Remains an alternative to test |

### Evidence Assessment

This is detailed firsthand testimony with quoted emails, but no complete independently authenticated call recording. Bubeck confirms the rewrite proposal, affiliation concern and career remark while contesting intent. Alpöge was not on the calls and is not an independent witness to all of them. The statement’s final page expressly says Buckmaster does not know whether their data was used. Repetition across news outlets is not counted as independent confirmation when they rely on the same post, statement or briefing.

### Credence Assessment

**Credence in this source analysis: 0.85.** The content and attributed positions are captured; private data lineage, intent and full mathematical validation remain outside this pass. Use the claim-specific probabilities rather than averaging them into a verdict about the entire controversy.

## Stage 3: Dialectical Analysis

### Steelmanned Argument

Pressure to trade away a collaborator’s participation or accept a vendor-controlled account of research would damage academic trust even if a separate proof were independently correct.

### Strongest Counterarguments

The disputed offer may concern a new writeup of OpenAI’s work, rather than removing Alpöge from the existing joint Euler paper. A concern about sharing unreleased model IP with a competitor’s employee can be legitimate without settling how that concern was communicated.

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

Pressure to trade away a collaborator’s participation or accept a vendor-controlled account of research would damage academic trust even if a separate proof were independently correct. The disputed offer may concern a new writeup of OpenAI’s work, rather than removing Alpöge from the existing joint Euler paper. A concern about sharing unreleased model IP with a competitor’s employee can be legitimate without settling how that concern was communicated. See the [cross-source synthesis](../syntheses/navier-stokes-2026-research-credit-data-value-chain.md) for the dated timeline, allegation matrix, bibliography amendment and implications for customer competition.

### Claims to Cross-Reference

[maguire-bowler-2026-navier-stokes-controversy](maguire-bowler-2026-navier-stokes-controversy.md), [alpoge-2026-september-two-contact](alpoge-2026-september-two-contact.md), [alpoge-2026-training-authorship-response](alpoge-2026-training-authorship-response.md), [altman-2026-navier-stokes-defense](altman-2026-navier-stokes-defense.md), [bubeck-2026-navier-stokes-response](bubeck-2026-navier-stokes-response.md). Existing database claims INST-2026-981 (customer-IP allegation), ECON-2026-984 (context ownership) and INST-2026-992 (portfolio posture) are related frameworks, not proof of this incident.

### Claim Summary

| ID | Type | Domain | Layer | Actor | Scope | Quantifier | Evidence | Credence | Claim |
|---|---|---|---|---|---|---|---|---|---|
| INST-2026-301 | [F] | INST | ASSERTED | OTHER:Tristan Buckmaster | who=researchers and AI providers; where=public record; when=2026-09-10 review; process=research and publication | some | E5 | 0.85 | Buckmaster reports obtaining smooth-forced Euler and Boussinesq blowup results with Alpöge on August 15 and Lean verification on August 22, building on Córdoba and Martínez-Zoroa. |
| INST-2026-302 | [F] | INST | ASSERTED | OTHER:Tristan Buckmaster | who=researchers and AI providers; where=public record; when=2026-09-10 review; process=research and publication | some | E5 | 0.97 | Buckmaster’s statement quotes the career remark and describes offers to coordinate releases or have him write OpenAI’s Navier–Stokes result without Alpöge. |
| INST-2026-303 | [F] | INST | ASSERTED | OTHER:Tristan Buckmaster | who=researchers and AI providers; where=public record; when=2026-09-10 review; process=research and publication | some | E5 | 0.99 | Buckmaster expressly says in his initial statement that he does not know whether his and Alpöge’s data was used by OpenAI. |
| INST-2026-304 | [H] | INST | EFFECT | OTHER:Tristan Buckmaster | who=researchers and AI providers; where=public record; when=2026-09-10 review; process=research and publication | some | E5 | 0.75 | The publication discussions exerted coercive pressure on Buckmaster to accept an account of authorship and credit shaped by institutional rivalry. |

### Claims to Register

```yaml
claims:
- id: INST-2026-301
  text: Buckmaster reports obtaining smooth-forced Euler and Boussinesq blowup results with Alpöge on August 15
    and Lean verification on August 22, building on Córdoba and Martínez-Zoroa.
  type: '[F]'
  domain: INST
  evidence_level: E5
  credence: 0.85
  operationalization: Check the cited primary record, versions and counterevidence. Participant chronology; Euler
    PDF confirms the forced setting and explicitly names the prior program. August timestamps were not independently
    audited.
  assumptions:
  - Attribution does not independently establish the underlying allegation.
  falsifiers:
  - Authenticated source records contradicting the attribution or chronology.
  source_ids:
  - buckmaster-2026-navier-stokes-statement
  - alpoge-2026-september-two-contact
  - maguire-bowler-2026-navier-stokes-controversy
  first_extracted: '2026-09-10'
  last_updated: '2026-09-10'
  extracted_by: codex
  version: 1
- id: INST-2026-302
  text: Buckmaster’s statement quotes the career remark and describes offers to coordinate releases or have him
    write OpenAI’s Navier–Stokes result without Alpöge.
  type: '[F]'
  domain: INST
  evidence_level: E5
  credence: 0.97
  operationalization: Check the cited primary record, versions and counterevidence. Bubeck and Altman corroborate
    the broad rewrite proposal; Bubeck acknowledges the career wording while disputing intent and the removal characterization.
  assumptions:
  - Attribution does not independently establish the underlying allegation.
  falsifiers:
  - Authenticated source records contradicting the attribution or chronology.
  source_ids:
  - buckmaster-2026-navier-stokes-statement
  - bubeck-2026-navier-stokes-response
  - altman-2026-navier-stokes-defense
  first_extracted: '2026-09-10'
  last_updated: '2026-09-10'
  extracted_by: codex
  version: 1
- id: INST-2026-303
  text: Buckmaster expressly says in his initial statement that he does not know whether his and Alpöge’s data was
    used by OpenAI.
  type: '[F]'
  domain: INST
  evidence_level: E5
  credence: 0.99
  operationalization: Check the cited primary record, versions and counterevidence. Page 4 states this directly;
    later suspicion is not an admission in this initial statement.
  assumptions:
  - Attribution does not independently establish the underlying allegation.
  falsifiers:
  - Authenticated source records contradicting the attribution or chronology.
  source_ids:
  - buckmaster-2026-navier-stokes-statement
  - maguire-bowler-2026-navier-stokes-controversy
  first_extracted: '2026-09-10'
  last_updated: '2026-09-10'
  extracted_by: codex
  version: 1
- id: INST-2026-304
  text: The publication discussions exerted coercive pressure on Buckmaster to accept an account of authorship and
    credit shaped by institutional rivalry.
  type: '[H]'
  domain: INST
  evidence_level: E5
  credence: 0.75
  operationalization: Check the cited primary record, versions and counterevidence. The career remark and affiliation
    restriction support this interpretation; coercive intent is disputed and there is no complete recording.
  assumptions:
  - Mechanism or inference is bounded by the stated conditions; no universal effect assumed.
  falsifiers:
  - Complete contemporaneous correspondence and recordings showing no conditional pressure and a materially different
    negotiation context.
  source_ids:
  - buckmaster-2026-navier-stokes-statement
  - bubeck-2026-navier-stokes-response
  - alpoge-2026-training-authorship-response
  - altman-2026-navier-stokes-defense
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
| 1 | 2026-09-10 | codex | gpt-6 | Shared multi-source pass; not separately measured | unavailable | unavailable | ANALYSIS-2026-178; three-stage analysis, source comparison and neutral prose pass. Session ambiguity prevents reliable per-source usage attribution. |

### Revision Notes

**Pass 1:** Captured source and replies; separated assertions, contested facts and analyst implications; retained corrections and capture limitations. Registration and provenance recorded in the shared package.
