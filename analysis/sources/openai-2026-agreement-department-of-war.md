# Source Analysis: Our agreement with the Department of War

> **Claim types**: `[F]` fact, `[T]` theory, `[H]` hypothesis, `[P]` prediction, `[A]` assumption/definition, `[C]` counterfactual, `[S]` speculation, `[X]` contradiction  
> **Evidence**: **E1** systematic review/meta-analysis; **E2** peer-reviewed/official stats; **E3** expert consensus/preprint; **E4** primary/credible reporting; **E5** expert opinion/analysis; **E6** unsupported/speculative

## Metadata

| Field | Value |
|---|---|
| **Source ID** | `openai-2026-agreement-department-of-war` |
| **Title** | Our agreement with the Department of War |
| **Author(s)** | OpenAI |
| **Date** | 2026-02-28 |
| **Type** | ARTICLE (contract disclosure / statement) |
| **URL** | https://openai.com/index/our-agreement-with-the-department-of-war/ |
| **Reliability** | 0.70 |
| **Rigor Level** | [DRAFT] |
| **Bias Notes** | Corporate statement designed to frame OpenAI as both national-security supportive and safety-conscious during a competitor’s dispute. High reliability for *what OpenAI publishes as its contract excerpt and narrative*, lower for comparative claims (“more guardrails than any prior agreement”) and for how DoW will interpret “all lawful purposes” operationally. |
| **Capture Notes** | OpenAI site blocked direct curl fetch in this environment; analysis based on web extraction (2026-02-28). |

**Claims YAML**: [`analysis/sources/openai-2026-agreement-department-of-war.yaml`](openai-2026-agreement-department-of-war.yaml)

## Stage 1: Descriptive Analysis

### Core Thesis
OpenAI presents its DoW agreement as a “law-and-policy grounded” implementation of “all lawful purposes” that still includes safety and oversight mechanisms (especially around autonomous weapons, surveillance, and domestic law enforcement). It implies this is the compromise Anthropic rejected.

### Summary (Neutral)
The post discloses an excerpt of contract language that:
- grants DoW permission to use OpenAI’s system for “all lawful purposes” consistent with existing law and “well-established safety and oversight protocols,”
- references DoD policy (e.g., DoD Directive 3000.09 for autonomous weapons),
- references intelligence legal authorities (FISA and EO 12333) and limits “unconstrained” monitoring/collection of U.S. persons,
- and restricts domestic law enforcement / domestic intelligence collection, with an exception for activities consistent with Posse Comitatus and law.

OpenAI also claims its agreement has more guardrails than previous government AI agreements and says it asked DoW to make the agreement available to all AI companies.

### Key Claims

| # | Claim | Claim ID | Layer | Actor | Scope | Quantifier | Type | Domain | Evid | Credence | Verified? | Falsifiable By |
|---:|---|---|---|---|---|---|---|---|---|---:|---|---|
| 1 | OpenAI’s agreement states DoW may use the AI system for “all lawful purposes…consistent with law, operational requirements, and well-established safety and oversight protocols” | GOV-2026-130 | LAWFUL | OTHER:OpenAI/DoW | who=DoW; where=US; when=2026; what=contract permission scope; phrase=all lawful purposes | N/A | [F] | GOV | E4 | 0.85 | In-post excerpt | The published excerpt does not contain this language |
| 2 | The agreement includes an autonomous-weapons constraint: the system may not be used to independently direct autonomous weapons systems where policy requires human control, referencing DoD Directive 3000.09 | GOV-2026-131 | LAWFUL | OTHER:OpenAI/DoW | who=DoW; what=autonomous weapons; constraint=no independent directing where policy requires HITL; ref=DoDD 3000.09 | N/A | [F] | GOV | E4 | 0.80 | In-post excerpt | The excerpt lacks this constraint or does not reference 3000.09 |
| 3 | The agreement includes a surveillance constraint: OpenAI’s system may not be used for “unconstrained monitoring” of U.S. persons or American citizens or unconstrained collection of their data; it references FISA and EO 12333 | GOV-2026-132 | LAWFUL | OTHER:OpenAI/DoW | who=DoW; what=monitoring/collection of US persons; constraint=not unconstrained; refs=FISA/EO12333 | N/A | [F] | GOV | E4 | 0.80 | In-post excerpt | The excerpt lacks this constraint or reference |
| 4 | The agreement includes a domestic law enforcement constraint: it may not be used for domestic law enforcement activities or domestic intelligence collection, except as consistent with Posse Comitatus and law | GOV-2026-133 | LAWFUL | OTHER:OpenAI/DoW | who=DoW; what=domestic LE/intel; constraint=not used except lawful/Posse Comitatus consistent | N/A | [F] | GOV | E4 | 0.75 | In-post excerpt | The excerpt lacks this constraint |
| 5 | OpenAI claims its agreement includes “more guardrails than any previous government AI model agreement” | GOV-2026-134 | ASSERTED | OTHER:OpenAI | who=OpenAI; what=comparative guardrails claim; when=2026-02-28 | N/A | [F] | GOV | E5 | 0.50 | ? | Comparative review shows prior agreements had equal/greater guardrails or the claim is unsubstantiated |
| 6 | OpenAI says it requested DoW make its agreement available to all AI companies that want to support national security under clear, standardized terms | INST-2026-947 | PRACTICED | OTHER:OpenAI/DoW | who=OpenAI→DoW; what=request for standard terms; when=2026-02-28 | N/A | [F] | INST | E4 | 0.70 | In-post | No such request is described in the post |
| 7 | OpenAI frames the key governance distinction as embedding constraints via existing public law/policy references rather than via private “prudential constraints” interpreted by a CEO | META-2026-154 | ASSERTED | OTHER:OpenAI | what=governance argument; why=democratic legitimacy | N/A | [T] | META | E5 | 0.60 | ? | The agreement still effectively delegates key interpretations to private parties (e.g., “unconstrained,” “well-established protocols”), undermining the claimed distinction |

## Stage 2: Evaluative Analysis

### Internal Coherence
The post is coherent as a “compromise framing” document: it adopts “all lawful purposes” while embedding explicit references to existing authorities and some constraints. The largest ambiguity is that key terms (“unconstrained,” “well-established safety and oversight protocols,” and what policy “requires” human control) can be interpreted in ways that are either strongly restrictive or permissive depending on implementing guidance.

### Key Factual Claims Verified

| Claim ID | Claim (paraphrased) | Crux? | Source Says | Actual | External Source | Search Notes | Status |
|---|---|---:|---|---|---|---|---|
| GOV-2026-130 | Agreement includes “all lawful purposes” language | **Y** | Yes | Confirmed in the post’s published excerpt | https://openai.com/index/our-agreement-with-the-department-of-war/ | in-page scan for “all lawful purposes” (2026-02-28); cross-check excerpt section | ok |
| GOV-2026-131 | Agreement references DoD Directive 3000.09 re autonomous weapons | **Y** | Yes | Confirmed in excerpt | https://openai.com/index/our-agreement-with-the-department-of-war/ | in-page scan for “3000.09” and “autonomous weapons” (2026-02-28) | ok |

### Disconfirming Evidence Search

| Claim | Counterevidence Found | Alternative Explanation | Search Notes |
|---|---|---|---|
| GOV-2026-134 (“more guardrails than any prior agreement”) | Not evaluated against a corpus of prior agreements in this check | Claim may mean “more guardrails than other currently-discussed DoW AI model agreements” rather than literally any prior government agreement | Treated as a marketing/comparative claim requiring external corpus review |
| META-2026-154 (law/policy vs CEO prudence) | Key constraints remain interpretation-dependent (“unconstrained”; “well-established protocols”) | The point may be that contested lines are adjudicated by public institutions over time, even if interpretation is uncertain now | Compared to Anthropic’s bright-line red lines and to UnderSecretary thread framing |

### Credence Assessment
- **Overall Credence**: 0.70  
- **Reasoning**: High confidence that the excerpted language appears as stated; moderate uncertainty in what it implies operationally and whether OpenAI’s comparative “guardrails” claims are accurate.

## Stage 3: Dialectical Analysis

### Steelmanned Argument
If the government is entitled to “all lawful use,” the right compromise is to anchor constraints to existing democratic law and policy (e.g., autonomy directives, intelligence oversight) rather than to vendor policies that can shift unilaterally. Publishing the agreement increases transparency and sets a reusable template that other vendors can adopt.

### Strongest Counterarguments
1. **Ambiguity laundering**: “all lawful purposes” + vague qualifiers can functionally permit the very uses vendors object to, while sounding restrained.
2. **Implementation gap**: legal references do not ensure compliance or meaningful oversight; actual practice depends on internal controls and auditability.
3. **Competitive framing**: publishing during Anthropic’s dispute may be more about market positioning than governance clarity.

---

### Claim Summary

| ID | Type | Domain | Layer | Actor | Scope | Quantifier | Evidence | Credence | Claim |
|---|---|---|---|---|---|---|---|---:|---|
| GOV-2026-130 | [F] | GOV | LAWFUL | OTHER:OpenAI/DoW | phrase=all lawful purposes | N/A | E4 | 0.85 | OpenAI’s agreement states DoW may use the AI system for “all lawful purposes…consistent with law…safety and oversight protocols” |
| GOV-2026-131 | [F] | GOV | LAWFUL | OTHER:OpenAI/DoW | ref=DoDD 3000.09 | N/A | E4 | 0.80 | Agreement includes a constraint on independently directing autonomous weapons where policy requires human control (referencing DoD Directive 3000.09) |
| GOV-2026-132 | [F] | GOV | LAWFUL | OTHER:OpenAI/DoW | refs=FISA/EO12333 | N/A | E4 | 0.80 | Agreement includes constraints on unconstrained monitoring/collection of U.S. persons’ data and references FISA/EO 12333 |
| GOV-2026-133 | [F] | GOV | LAWFUL | OTHER:OpenAI/DoW | ref=Posse Comitatus | N/A | E4 | 0.75 | Agreement restricts domestic law enforcement / domestic intelligence collection use (with a Posse Comitatus–consistent exception) |
| GOV-2026-134 | [F] | GOV | ASSERTED | OTHER:OpenAI | comparative claim | N/A | E5 | 0.50 | OpenAI claims its agreement includes more guardrails than any prior government AI model agreement |
| INST-2026-947 | [F] | INST | PRACTICED | OTHER:OpenAI/DoW | what=request standard terms | N/A | E4 | 0.70 | OpenAI says it requested DoW make the agreement available to all AI companies |
| META-2026-154 | [T] | META | ASSERTED | OTHER:OpenAI | what=governance argument | N/A | E5 | 0.60 | OpenAI argues constraints should be anchored in public law/policy rather than private CEO prudence |

### Claims to Register

```yaml
claims:
  - id: "GOV-2026-130"
    text: "OpenAI published an excerpt of its DoW agreement stating that DoW may use OpenAI’s system for all lawful purposes, consistent with law, operational requirements, and well-established safety and oversight protocols."
    type: "[F]"
    domain: "GOV"
    evidence_level: "E4"
    credence: 0.85
    operationalization: "Confirm the published excerpt and track any subsequent version changes; identify implementing guidance for the referenced safety/oversight protocols."
    assumptions: []
    falsifiers:
      - "The published excerpt is changed to remove or materially alter this clause."
    source_ids: ["openai-2026-agreement-department-of-war"]

  - id: "GOV-2026-131"
    text: "OpenAI’s published excerpt states its system may not be used to independently direct autonomous weapons systems where DoW policy requires human control, referencing DoD Directive 3000.09."
    type: "[F]"
    domain: "GOV"
    evidence_level: "E4"
    credence: 0.80
    operationalization: "Verify the excerpted clause and compare to the requirements of DoD Directive 3000.09; assess how 'independently direct' is implemented in practice."
    assumptions: []
    falsifiers:
      - "No such clause exists or it is materially different."
    source_ids: ["openai-2026-agreement-department-of-war"]

  - id: "GOV-2026-132"
    text: "OpenAI’s published excerpt states its system may not be used for unconstrained monitoring of U.S. persons/American citizens or unconstrained collection of their data, and references FISA and EO 12333."
    type: "[F]"
    domain: "GOV"
    evidence_level: "E4"
    credence: 0.80
    operationalization: "Verify excerpted clauses and examine how 'unconstrained' is defined operationally; compare to FISA/EO 12333 compliance regimes."
    assumptions: []
    falsifiers:
      - "No such clause exists or it is materially different."
    source_ids: ["openai-2026-agreement-department-of-war"]

  - id: "GOV-2026-133"
    text: "OpenAI’s published excerpt restricts use of its system for domestic law enforcement or domestic intelligence collection, except as consistent with the Posse Comitatus Act and applicable law."
    type: "[F]"
    domain: "GOV"
    evidence_level: "E4"
    credence: 0.75
    operationalization: "Verify excerpted clauses and interpret the scope of the Posse Comitatus exception; track any implementing guidance."
    assumptions: []
    falsifiers:
      - "No such clause exists or it is materially different."
    source_ids: ["openai-2026-agreement-department-of-war"]

  - id: "GOV-2026-134"
    text: "OpenAI claims its DoW agreement includes more guardrails than any previous government AI model agreement."
    type: "[F]"
    domain: "GOV"
    evidence_level: "E5"
    credence: 0.50
    operationalization: "Compile a corpus of prior government AI model agreements and compare guardrail clauses to assess the comparative claim."
    assumptions:
      - "Prior agreements are accessible or can be characterized via credible reporting."
    falsifiers:
      - "Prior agreements contain equal or stronger guardrails."
    source_ids: ["openai-2026-agreement-department-of-war"]

  - id: "INST-2026-947"
    text: "OpenAI states it asked DoW to make its agreement available to all AI companies that want to support national security under clear standardized terms."
    type: "[F]"
    domain: "INST"
    evidence_level: "E4"
    credence: 0.70
    operationalization: "Confirm the request in OpenAI’s statement and identify whether DoW later publishes a standard agreement template."
    assumptions: []
    falsifiers:
      - "No such request is described or DoW rejects standardization and keeps bespoke agreements."
    source_ids: ["openai-2026-agreement-department-of-war"]

  - id: "META-2026-154"
    text: "OpenAI frames the key governance distinction as embedding constraints via existing public law and policy references rather than via private 'prudential constraints' interpreted by a CEO."
    type: "[T]"
    domain: "META"
    evidence_level: "E5"
    credence: 0.60
    operationalization: "Assess whether the agreement’s key constraints are actually determinate under public law/policy, or remain effectively delegated to private interpretation via vague terms."
    assumptions: []
    falsifiers:
      - "Practical implementation shows decisive constraints are still privately interpreted and enforced."
    source_ids: ["openai-2026-agreement-department-of-war"]
```

---

**Analysis Date**: 2026-02-28  
**Analyst**: codex (gpt-5.2)  
**Credence in Analysis**: 0.72

## Analysis Log

| Pass | Date | Tool | Model | Duration | Tokens | Cost | Notes |
|---:|---|---|---|---:|---:|---:|---|
| 1 | 2026-02-28 | codex | gpt-5.2 | — | — | — | Initial analysis; contract language extracted from public disclosure |

