# Source Analysis: Thread: “OpenAI still has ‘all lawful use’ — nobody read the articles”

> **Claim types**: `[F]` fact, `[T]` theory, `[H]` hypothesis, `[P]` prediction, `[A]` assumption/definition, `[C]` counterfactual, `[S]` speculation, `[X]` contradiction  
> **Evidence**: **E1** systematic review/meta-analysis; **E2** peer-reviewed/official stats; **E3** expert consensus/preprint; **E4** primary/credible reporting; **E5** expert opinion/analysis; **E6** unsupported/speculative

## Metadata

| Field | Value |
|---|---|
| **Source ID** | `livgorton-2026-openai-all-lawful-use-thread` |
| **Title** | Thread: “OpenAI still has ‘all lawful use’ — nobody read the articles” |
| **Author(s)** | @livgorton |
| **Date** | 2026-02-28 |
| **Type** | SOCIAL (thread) |
| **URL** | https://threadreaderapp.com/thread/2027616963942617195.html |
| **Reliability** | 0.40 |
| **Rigor Level** | [DRAFT] |
| **Bias Notes** | Short commentary (one-tweet thread) expressing frustration and an interpretive claim about contract continuity. Useful as a signal of community reaction; not an evidentiary source for the underlying contract history unless backed by primary documents. |

**Claims YAML**: [`analysis/sources/livgorton-2026-openai-all-lawful-use-thread.yaml`](livgorton-2026-openai-all-lawful-use-thread.yaml)

## Stage 1: Descriptive Analysis

### Core Thesis
The author argues that OpenAI’s DoW deal still contains an “all lawful use” clause and therefore does not represent a meaningful change from what was previously on offer, implying that public commentary misread the underlying articles/contract terms.

### Key Claims

| # | Claim | Claim ID | Layer | Actor | Scope | Quantifier | Type | Domain | Evid | Credence | Verified? | Falsifiable By |
|---:|---|---|---|---|---|---|---|---|---|---:|---|---|
| 1 | OpenAI’s DoW contract still has an “all lawful use” clause, and OpenAI negotiated functionally the same contract it has always been offered | GOV-2026-142 | ASSERTED | OTHER:@livgorton | who=OpenAI/DoW; when=2026-02; what=contract clause continuity | N/A | [F] | GOV | E5 | 0.55 | Partially corroborated | OpenAI agreement does not contain “all lawful” language, or primary negotiation history shows materially different terms |
| 2 | Many commentators have not read the underlying articles/documents and are misinformed | META-2026-157 | ASSERTED | OTHER:@livgorton | who=public discourse; when=2026-02-28 | some | [T] | META | E6 | 0.40 | ? | Evidence shows the dominant discourse accurately reflects the underlying articles/contract language |

## Stage 2: Evaluative Analysis

### Key Factual Claims Verified

| Claim ID | Claim (paraphrased) | Crux? | Source Says | Actual | External Source | Search Notes | Status |
|---|---|---:|---|---|---|---|---|
| GOV-2026-142 | OpenAI contract includes “all lawful” clause | **Y** | Yes | Confirmed partially: OpenAI’s published excerpt uses “all lawful purposes” language | https://openai.com/index/our-agreement-with-the-department-of-war/ | q1: “OpenAI all lawful purposes clause excerpt” (2026-02-28); q2: “OpenAI agreement all lawful use clause” (2026-02-28) | ok (partial) |
| GOV-2026-142 | Contract is “functionally the same” as always offered | **Y** | Yes | Not resolved in this check; requires primary negotiation history or prior term sheets | N/A | Looked for prior offer terms disclosed; not found in provided sources | ? |

### Credence Assessment
- **Overall Credence**: 0.55  
- **Reasoning**: The “all lawful purposes” clause exists in OpenAI’s published excerpt; the stronger historical claim (“same contract always offered”) is unverified here.

## Stage 3: Dialectical Analysis

### Steelmanned Argument
Public discourse often compresses legal/contract language into slogans. If the headline clause (“all lawful use”) remains, then claims of a new “harmonized” agreement may be misleading; substantive governance hinges on the exact text and implementation, not on public PR framing.

### Strongest Counterarguments
1. **Text matters**: even if “all lawful purposes” remains, the presence of specific legal/policy references and constraints could represent meaningful changes.
2. **Historical opacity**: without disclosure of previous offers, “functionally the same contract” is an inference, not an established fact.

---

### Claim Summary

| ID | Type | Domain | Layer | Actor | Scope | Quantifier | Evidence | Credence | Claim |
|---|---|---|---|---|---|---|---|---:|---|
| GOV-2026-142 | [F] | GOV | ASSERTED | OTHER:@livgorton | what=contract clause continuity | N/A | E5 | 0.55 | OpenAI’s contract still has an “all lawful use” clause and is functionally the same as always offered |
| META-2026-157 | [T] | META | ASSERTED | OTHER:@livgorton | what=discourse misunderstanding | some | E6 | 0.40 | Many commentators have not read the underlying articles/documents |

### Claims to Register

```yaml
claims:
  - id: "GOV-2026-142"
    text: "Liv Gorton claims OpenAI’s DoW contract still contains an 'all lawful use' clause and is functionally the same contract OpenAI has always been offered."
    type: "[F]"
    domain: "GOV"
    evidence_level: "E5"
    credence: 0.55
    operationalization: "Compare OpenAI’s current published excerpt to any prior offered term sheets or historical reporting to determine whether terms materially changed."
    assumptions:
      - "The author has access to or correctly infers the historical offer terms."
    falsifiers:
      - "Primary documents show prior offered terms were materially different."
    source_ids: ["livgorton-2026-openai-all-lawful-use-thread"]

  - id: "META-2026-157"
    text: "Liv Gorton claims many commentators have not read the underlying articles/documents about the OpenAI-DoW agreement and are misinformed."
    type: "[T]"
    domain: "META"
    evidence_level: "E6"
    credence: 0.40
    operationalization: "Sample public commentary and compare stated claims to the actual published contract language/excerpts."
    assumptions: []
    falsifiers:
      - "A representative sample of discourse accurately reflects the underlying documents."
    source_ids: ["livgorton-2026-openai-all-lawful-use-thread"]
```

---

**Analysis Date**: 2026-02-28  
**Analyst**: codex (gpt-5.2)  
**Credence in Analysis**: 0.70

## Analysis Log

| Pass | Date | Tool | Model | Duration | Tokens | Cost | Notes |
|---:|---|---|---|---:|---:|---:|---|
| 1 | 2026-02-28 | codex | gpt-5.2 | — | — | — | Initial analysis; verified clause existence via OpenAI disclosure |

