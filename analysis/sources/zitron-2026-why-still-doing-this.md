# Source Analysis: Why Are We Still Doing This?

> **Claim types**: `[F]` fact, `[T]` theory, `[H]` hypothesis, `[P]` prediction, `[A]` assumption, `[C]` counterfactual, `[S]` speculation, `[X]` contradiction  
> **Evidence**: **E1** systematic review/meta-analysis; **E2** peer-reviewed/official stats; **E3** expert consensus/preprint; **E4** credible journalism/industry; **E5** opinion/anecdote; **E6** unsupported/speculative

## Metadata

| Field | Value |
|-------|-------|
| **Source ID** | zitron-2026-why-still-doing-this |
| **Title** | Why Are We Still Doing This? |
| **Author(s)** | Ed Zitron |
| **Date** | 2026-03-17 |
| **Type** | BLOG |
| **URL** | https://www.wheresyoured.at/why-are-we-still-doing-this/ |
| **Reliability** | 0.55 |
| **Rigor Level** | `[DRAFT]` |

## Stage 1: Descriptive Analysis

### Core Thesis
Zitron argues that frontier AI companies are **structurally unprofitable under consumer subscription pricing** because token usage is highly variable and unpredictable, making (1) budgeting hard for users under usage-based pricing and (2) sustainable price increases politically/economically difficult. He claims there is **no clean migration path** from “all-you-can-eat” subscriptions to API-style metering without severe churn.

### Key Claims

| # | Claim | Claim ID | Layer | Actor | Scope | Quantifier | Type | Domain | Evid | Credence | Verified? | Falsifiable By |
|---|-------|----------|-------|-------|-------|------------|------|--------|------|----------|-----------|----------------|
| 1 | A $20/month Claude subscriber can (per Zitron’s estimate) consume up to ~$163 worth of compute | ECON-2026-952 | EFFECT | OTHER:Anthropic | who=Claude subscribers; where=Claude subscription; when=2026; process=token usage converted to API-equivalent cost | some | [F] | ECON | E5 | 0.40 | nf | Anthropic disclosures show materially different max token value / usage caps |
| 2 | If subscriptions were repriced to reflect compute, prices might need to rise to ~$80–$800/month, which would cause major churn | ECON-2026-953 | EFFECT | OTHER:frontier AI providers | who=subscription users; where=AI subscriptions; when=2026; process=repricing; outcome=churn | some | [H] | ECON | E6 | 0.35 | ? | Providers raise prices substantially without major churn or margin stress |
| 3 | For a 100-engineer company paying $200/month per seat, subscription spend is $240k/year (toy example baseline) | ECON-2026-954 | ASSERTED | OTHER:enterprise AI buyers | who=100 engineers; where=enterprise; when=2026; metric=subscription spend arithmetic | N/A | [F] | ECON | E2 | 0.95 | ok | Arithmetic error in the baseline computation |
| 4 | Anthropic’s Claude Code docs say average cost is ~$6 per developer per day, with daily costs below $12 for 90% of users | ECON-2026-955 | ASSERTED | OTHER:Anthropic | who=Claude Code users; where=Anthropic docs; when=2026; metric=$/dev/day distribution | N/A | [F] | ECON | E2 | 0.90 | ok | Anthropic docs do not contain this statement or materially differ |
| 5 | Metered API pricing is difficult for users to budget because token burn is unpredictable and retries/loops are common | ECON-2026-956 | EFFECT | OTHER:AI users | who=API users; where=LLM tools; when=2025-2026; process=budgeting under stochastic token burn | often | [T] | ECON | E5 | 0.60 | ? | Users can reliably budget metered usage with low cognitive burden in practice |
| 6 | Subscription-to-API conversion is unlikely because subscriptions build habits that are incompatible with thinking in metered tokens | INST-2026-958 | PRACTICED | OTHER:AI providers | who=subscription users; where=consumer AI; when=2025-2026; process=habit formation; outcome=low conversion under metering | often | [H] | INST | E5 | 0.55 | ? | Providers migrate users to metered pricing with high retention and stable usage |
| 7 | Coding workflows are a worst-case for cost predictability because iterative prompting and debugging loops drive repeated token spend | LABOR-2026-033 | EFFECT | OTHER:AI coding users | who=developers; where=AI coding tools; when=2025-2026; process=iteration/loops; outcome=high and variable token spend | often | [H] | LABOR | E5 | 0.55 | ? | Measured coding workflows show low variance and predictable token spend under typical use |

### Argument Structure

```
[Token burn is variable & hard to predict]
            |
            v
[Subscriptions hide true costs; heavy users are loss-making]
            |
            v
[Raising prices or switching to metered API requires user mental-model shift]
            |
            v
[Most users churn / usage collapses]
            |
            v
[No clean profit lever for subscription AI]
```

### Theoretical Lineage
- Behavioral pricing / habit formation: flat fees create “unlimited” mental models that resist metering.
- Unit economics skepticism for AI subscriptions; emphasis on tail users and stochastic costs.

### Scope & Limitations
- Strongest on consumer subscription dynamics; weaker on enterprise usage-based economics and price discrimination.
- Mixes numeric examples (some auditable, some illustrative) with claims about user behavior.

## Stage 2: Evaluative Analysis

### Internal Coherence
The “no clean migration path” story is plausible as a behavioral economics claim. Key uncertainties are empirical:
- How many users are “tail” loss-makers?
- Can providers design hybrid pricing (caps, bundles, result-based pricing) that preserves retention?
- How quickly do costs fall (hardware/serving) relative to demand growth?

### Key Factual Claims Verified

| Claim ID | Claim (paraphrased) | Crux? | Source Says | Actual | External Source | Search Notes | Status |
|----------|---------------------|-------|-------------|--------|-----------------|-------------|--------|
| ECON-2026-955 | Anthropic docs: avg Claude Code cost $6/dev/day; 90% below $12/day | **Y** | As stated | Found matching statement in Anthropic Claude Code costs documentation | Anthropic docs: Claude Code costs page | q1: "\"average cost is $6 per developer per day\" Claude Code"; q2: "below $12 for 90% of users Claude Code costs"; 2026-03-28 | ok |
| ECON-2026-952 | $20 Claude sub can burn ~$163 compute | N | $163 compute value | Could not locate a primary Anthropic statement of “$163” in this pass; appears to be Zitron’s derived estimate | N/A | q1: "\"$163\" Claude subscription compute"; q2: "Anthropic subscription $163 compute cost"; 2026-03-28 | nf |

### Disconfirming Evidence Search

| Claim | Counterevidence Found | Alternative Explanation | Search Notes |
|-------|----------------------|-------------------------|--------------|
| “No clean migration path” | Providers can tighten “fair use” and implement bundles/tiers gradually | Migration may be gradual and mostly invisible via caps and agent efficiency improvements | Searched for examples of successful usage-based migration in SaaS/cloud; mixed but common in infra; 2026-03-28 |
| “Subscriptions are necessarily loss-making” | Losses may be concentrated in a small tail; providers can clamp down on abuse | Profitability might be achieved via segmentation rather than uniform repricing | Checked provider policies; many already tightening; 2026-03-28 |

### Corrections & Updates

| Item | URL | Published | Corrected/Updated | What Changed | Impacted Claim IDs | Action Taken |
|------|-----|-----------|-------------------|--------------|--------------------|-------------|
| N/A | | | | | | |

### Internal Tensions / Self-Contradictions

| Tension | Parts in Conflict | Implication |
|---------|-------------------|-------------|
| “Budgeting is impossible” vs Anthropic cost guidance | Claims unpredictability; docs provide cost-management tips and typical ranges | Suggests budgeting may be hard but not impossible; the magnitude is an empirical question |

### Persuasion Techniques

| Technique | Example from Source | Effect on Reader |
|-----------|---------------------|------------------|
| Future-tense prohibition | Declares rules for discourse (“AI boosters no longer allowed…”) | Rhetorically effective, but not evidence |
| Extreme hypotheticals | $250/gallon gas analogy; $800/mo subscriptions | Emphasizes shock; risks anchoring on tail scenarios |

### Unstated Assumptions

| Assumption | Claim ID | Critical? | Problematic? |
|------------|----------|-----------|--------------|
| Most marginal users are price sensitive and will churn under metering | INST-2026-958 | Y | ? |
| Tail users dominate losses and cannot be constrained without destroying product value | ECON-2026-956 | Y | ? |
| “Useful output” requires long loops/iterations that scale tokens faster than value | LABOR-2026-033 | N | ? |

### Evidence Assessment
- Strongest: explicit Anthropic cost guidance (auditable).
- Weaker: derived “$163 compute” conversion and the size of churn under repricing (needs internal retention data).

### Credence Assessment
- **Overall Credence**: 0.60
- **Reasoning**: The behavioral/economic critique is plausible and partially anchored by provider cost docs, but many large-dollar examples are illustrative and not fully audited.

## Stage 3: Dialectical Analysis

### Steelmanned Argument
Subscription pricing creates a miscalibrated user mental model (“unlimited AI”), while the provider’s marginal costs are stochastic and can be dominated by tail users and long-context sessions. Even if AI is valuable, this pricing structure is unstable and likely to tighten or break, reducing adoption and/or exploding enterprise budgets.

### Strongest Counterarguments
1. **Hybrid pricing works**: caps, bundles, and differentiated tiers can approximate metering without a hard switch.
2. **Efficiency gains**: model and serving improvements reduce cost per useful output, shrinking the subsidy gap.
3. **Enterprise differs**: usage-based APIs and negotiated contracts already align revenue with cost better than consumer subscriptions.

### Supporting Theories

| Theory/Framework | Source ID | How It Supports |
|------------------|-----------|-----------------|
| Subprime fragility framing | zitron-2024-subprime-ai-crisis | Similar “dependency on subsidized pricing” mechanism |

### Contradicting Theories

| Theory/Framework | Source ID | Point of Conflict |
|------------------|-----------|-------------------|
| Unit-economics modeling and pricing levers | lhl-2026-frontier-llm-token-unit-economics | Suggests multiple levers (utilization, caching, tiering) and that “true cost” depends heavily on workload mix |

### Synthesis Notes
This post is strongest as a **pricing mental-model critique**. The “$163 compute” style examples should be treated as derived and validated against official token/cap disclosures when possible.

### Claims to Cross-Reference
- Anthropic cost distribution and guidance: ECON-2026-955
- Subscription break-even math and “true cost” modeling: lhl-2026-frontier-llm-token-unit-economics

---

### Claim Summary

| ID | Type | Domain | Layer | Actor | Scope | Quantifier | Evidence | Credence | Claim |
|----|------|--------|-------|-------|-------|------------|----------|----------|-------|
| ECON-2026-952 | [F] | ECON | EFFECT | OTHER:Anthropic | who=Claude subscribers; where=subscriptions; when=2026 | some | E5 | 0.40 | A $20 Claude subscriber can consume up to ~$163 worth of compute (derived estimate) |
| ECON-2026-953 | [H] | ECON | EFFECT | OTHER:frontier AI providers | who=subscription users; where=AI subscriptions; when=2026 | some | E6 | 0.35 | Repricing subscriptions to cost could require ~$80–$800/month and would cause major churn |
| ECON-2026-954 | [F] | ECON | ASSERTED | OTHER:enterprise AI buyers | who=100 engineers; where=enterprise; when=2026 | N/A | E2 | 0.95 | 100 seats at $200/month equals $240k/year subscription spend |
| ECON-2026-955 | [F] | ECON | ASSERTED | OTHER:Anthropic | who=Claude Code users; where=docs; when=2026 | N/A | E2 | 0.90 | Anthropic docs: avg $6/dev/day; 90% below $12/day |
| ECON-2026-956 | [T] | ECON | EFFECT | OTHER:AI users | who=API users; where=LLM tools; when=2025-2026 | often | E5 | 0.60 | Token-burn unpredictability and retries make budgeting metered usage difficult |
| INST-2026-958 | [H] | INST | PRACTICED | OTHER:AI providers | who=subscription users; where=consumer AI; when=2025-2026 | often | E5 | 0.55 | Subscription habit formation makes migration to metered pricing difficult |
| LABOR-2026-033 | [H] | LABOR | EFFECT | OTHER:AI coding users | who=developers; where=coding tools; when=2025-2026 | often | E5 | 0.55 | Iterative prompting/debug loops drive high and variable token spend for coding workflows |

### Claims to Register

```yaml
claims:
  # Canonical claims artifact:
  # analysis/sources/zitron-2026-why-still-doing-this.yaml
  - id: "INST-2026-958"
  - id: "ECON-2026-952"
  - id: "ECON-2026-953"
  - id: "ECON-2026-954"
  - id: "ECON-2026-955"
  - id: "ECON-2026-956"
  - id: "LABOR-2026-033"
```

---

**Analysis Date**: 2026-03-28  
**Analyst**: gpt-5  
**Credence in Analysis**: 0.70

## Analysis Log

| Pass | Date | Tool | Model | Duration | Tokens | Cost | Notes |
|------|------|------|-------|----------|--------|------|-------|
| 1 | 2026-03-28 | codex | gpt-5 | ? | ? | ? | Initial 3-stage analysis + extracted claims; verified Anthropic Claude Code cost guidance; could not verify “$163” derived estimate. |

