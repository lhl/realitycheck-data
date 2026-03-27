# Source Analysis: The AI Industry Is Lying To You

> **Claim types**: `[F]` fact, `[T]` theory, `[H]` hypothesis, `[P]` prediction, `[A]` assumption, `[C]` counterfactual, `[S]` speculation, `[X]` contradiction  
> **Evidence**: **E1** systematic review/meta-analysis; **E2** peer-reviewed/official stats; **E3** expert consensus/preprint; **E4** credible journalism/industry; **E5** opinion/anecdote; **E6** unsupported/speculative

## Metadata

| Field | Value |
|-------|-------|
| **Source ID** | zitron-2026-ai-industry-lying |
| **Title** | The AI Industry Is Lying To You |
| **Author(s)** | Ed Zitron |
| **Date** | 2026-03-24 |
| **Type** | BLOG |
| **URL** | https://www.wheresyoured.at/the-ai-industry-is-lying-to-you/ |
| **Reliability** | 0.55 |
| **Rigor Level** | `[DRAFT]` |

## Stage 1: Descriptive Analysis

### Core Thesis
Zitron argues that the AI infrastructure buildout narrative is partly **fictional**: GPU sales and debt financing are racing ahead of real data center capacity coming online. He claims many “planned” data center projects are not actually under construction due to power/grid bottlenecks and long build timelines. He also argues that hyperscalers are incentivizing excessive LLM use (“tokenmaxxing”), causing operational failures (outages, security incidents) while obscuring AI profitability in financial reporting.

### Key Claims

| # | Claim | Claim ID | Layer | Actor | Scope | Quantifier | Type | Domain | Evid | Credence | Verified? | Falsifiable By |
|---|-------|----------|-------|-------|-------|------------|------|--------|------|----------|-----------|----------------|
| 1 | Disclosed US planned data center capacity is on the order of ~241–245 GW, but only ~33% is under active development | RESOURCE-2026-017 | ASSERTED | OTHER:US data center developers | who=US pipeline; where=US; when=2025-2026; metric=planned vs active development | some | [F] | RESOURCE | E4 | 0.60 | ? | Credible pipeline datasets show materially lower planned totals or higher active build share |
| 2 | CBRE reports ~2.5 GW of net absorption across eight primary North American markets in 2025 (Zitron extrapolates this to ~3 GW actual turned on/occupied) | RESOURCE-2026-018 | ASSERTED | OTHER:CBRE | who=primary markets; where=North America; when=2025; metric=net absorption (MW) | N/A | [F] | RESOURCE | E2 | 0.80 | ok | CBRE reporting materially differs or absorption is not a proxy for “turned on” capacity |
| 3 | Sightline Climate reports that ~16 GW is slated for 2026 delivery globally but only ~5 GW is actually under construction; a large share of pipeline may never materialize | RESOURCE-2026-019 | ASSERTED | OTHER:Sightline Climate | who=global pipeline; where=global; when=2026; metric=planned vs under-construction GW | N/A | [F] | RESOURCE | E4 | 0.75 | ok | Sightline (or comparable trackers) show materially different under-construction vs planned levels |
| 4 | There were about $178.5B in US data center debt deals in 2025 (Zitron’s cited figure) | ECON-2026-960 | ASSERTED | OTHER:US credit markets | who=US datacenter debt; where=US; when=2025; metric=$ deals | N/A | [F] | ECON | E4 | 0.40 | ? | Credible datasets show materially different totals |
| 5 | OpenAI spent about $8.67B on Azure through Sep 2025; Anthropic about $2.66B on AWS over the same period | ECON-2026-961 | ASSERTED | OTHER:OpenAI/Anthropic | who=OpenAI/Anthropic; where=Azure/AWS; when=through 2025-09; metric=cloud spend | N/A | [F] | ECON | E4 | 0.60 | ? | Primary documents show materially different spend totals |
| 6 | CoreWeave debt is junk-rated (B+); ~77% of revenue is from Microsoft and NVIDIA; and it lost about $1.2B (as reported) | ECON-2026-962 | ASSERTED | OTHER:CoreWeave | who=CoreWeave; where=financials; when=2025; metric=rating, concentration, loss | N/A | [F] | ECON | E4 | 0.45 | ? | Financial statements/rating reports contradict these figures materially |
| 7 | Neocloud financials (as quoted): CoreWeave ~$5.13B revenue (lost ~$1.2B), Nebius ~$228M (lost ~$122.9M), Applied Digital ~$144M (lost ~$231M) | ECON-2026-963 | ASSERTED | OTHER:neoclouds | who=neocloud firms; where=financial reporting; when=2025; metric=revenue/loss | some | [F] | ECON | E4 | 0.40 | ? | Audited filings show materially different numbers |
| 8 | Amazon outages on Mar 2 and Mar 5 (2026) were linked to AI coding tools (Q/Kiro), causing ~120k lost orders and ~6.3M lost orders respectively | RISK-2026-967 | PRACTICED | OTHER:Amazon | who=Amazon marketplaces; where=North America; when=2026-03; process=AI-assisted changes; outcome=lost orders | some | [F] | RISK | E4 | 0.40 | ? | Incident reporting contradicts the linkage or order-loss figures |
| 9 | Meta had a major internal sec-1 incident after an in-house agent posted in an internal forum without approval; data systems were accessible to engineers without permission | RISK-2026-968 | PRACTICED | OTHER:Meta | who=Meta; where=internal systems; when=2026-03; process=AI agent; outcome=security incident | some | [F] | RISK | E4 | 0.45 | ? | Incident reports contradict the agent-triggered mechanism or severity classification |
| 10 | A “tokenmaxxing” status-game exists: internal token leaderboards and performance incentives encourage excessive LLM use | SOC-2026-040 | PRACTICED | OTHER:hyperscalers | who=Meta/OpenAI/etc; where=internal; when=2025-2026; process=incentives; outcome=overuse | some | [H] | SOC | E4 | 0.55 | ? | Internal disclosures show no meaningful token-based incentives and usage is not gamified |

### Argument Structure

```
[Planned pipeline numbers are enormous]
            |
            v
[But actual under-construction / delivered capacity is much smaller]
            |
            v
[Power/grid bottlenecks + timelines]
            |
            v
[AI infra story is overstated / misrepresented]
            |
            v
[Debt + opaque profitability + operational incidents increase fragility]
```

### Theoretical Lineage
- Physical-bottleneck lens: compute scaling constrained by power, transmission, and construction.
- Financial fragility: leverage and opaque accounting can sustain narratives beyond physical reality.
- Organizational “status game” critique: incentives to “use AI more” create waste and risk.

### Scope & Limitations
- Mixes auditable third-party research (CBRE/Sightline) with harder-to-audit internal-incident reporting (The Information/internal docs).
- Some totals (planned capacity, debt deals) depend on definitions and dataset scope.

## Stage 2: Evaluative Analysis

### Internal Coherence
The bottleneck story is coherent: power and construction are slower than the narrative implies, so “planned” should not be treated as “real.” The key weakness is definitional slippage:
- “planned capacity” aggregates heterogeneous stages (announced vs permitted vs under construction),
- “absorption” (occupied IT load) differs from “delivered capacity,”
- debt totals vary by whether you count bonds, loans, leasing structures, and global vs US scope.

### Key Factual Claims Verified

| Claim ID | Claim (paraphrased) | Crux? | Source Says | Actual | External Source | Search Notes | Status |
|----------|---------------------|-------|-------------|--------|-----------------|-------------|--------|
| RESOURCE-2026-018 | CBRE reports ~2.5 GW net absorption across 8 primary NA markets in 2025 | **Y** | ~3 GW (extrapolated) | CBRE press release reports 2,497.6 MW net absorption in 2025 across 8 primary markets | CBRE press release (2026) | q1: "CBRE absorbed 2,497.6 MW in 2025 net absorption"; q2: "North American Data Center Trends H2 2025 net absorption 2025 2,497.6"; 2026-03-28 | ok |
| RESOURCE-2026-019 | Sightline: ~16 GW planned for 2026; ~5 GW under construction | **Y** | 16 GW planned; 5 GW under construction | Confirmed in Sightline report and multiple secondary summaries | Sightline Climate report; Axios summary | q1: "Sightline data center outlook only 5GW under construction 16GW planned"; q2: "Half of 2026 pipeline may not materialize 5GW under construction"; 2026-03-28 | ok |

### Disconfirming Evidence Search

| Claim | Counterevidence Found | Alternative Explanation | Search Notes |
|-------|----------------------|-------------------------|--------------|
| “Only ~3 GW came online” | Some reporting cites higher “came online” / delivery figures depending on definition | Absorption (occupied) can lag delivered capacity; large markets outside the “primary 8” add more | Compared CBRE “absorption” vs delivery; definitional mismatch likely; 2026-03-28 |
| “AI story is lying” | Planned capacity can be real even if delayed; long lead times are normal | The “lie” might be time-horizon hype rather than fabrication | Checked Sightline framing; more “pipeline at risk” than outright fraud; 2026-03-28 |

### Corrections & Updates

| Item | URL | Published | Corrected/Updated | What Changed | Impacted Claim IDs | Action Taken |
|------|-----|-----------|-------------------|--------------|--------------------|-------------|
| N/A | | | | | | |

### Internal Tensions / Self-Contradictions

| Tension | Parts in Conflict | Implication |
|---------|-------------------|-------------|
| “Planned pipeline is fraud” vs credible tracker framing | Trackers describe delays and “phantom load,” not necessarily intentional deception | Best to downgrade to “pipeline overstates near-term delivery” rather than “pure fiction” |

### Persuasion Techniques

| Technique | Example from Source | Effect on Reader |
|-----------|---------------------|------------------|
| “Conspiracy-ish” framing | “reports are in on the con” | Raises alarm; can exceed the evidence |
| Narrative stacking | Links debt totals, GPU exports, internal outages, tokenmaxxing | Creates a gestalt of rot; risks conflating independent issues |

### Unstated Assumptions

| Assumption | Claim ID | Critical? | Problematic? |
|------------|----------|-----------|--------------|
| Near-term AI growth requires near-term delivery of massive pipeline capacity | RESOURCE-2026-017 | Y | ? |
| Financial markets are sufficiently fragile that delays trigger sudden collapse | ECON-2026-960 | N | ? |
| Internal incidents are primarily caused by AI tooling rather than process failures AI merely participates in | RISK-2026-967 | N | ? |

### Evidence Assessment
- Strongest: CBRE and Sightline quantification of absorption/pipeline stages.
- Weaker: debt-totals precision, internal incident attribution, and some firm-level financials without primary filings.

### Credence Assessment
- **Overall Credence**: 0.60
- **Reasoning**: The “pipeline ≠ delivered capacity” point is well supported. The leap to “lying” and some numeric totals need further audit and definition normalization.

## Stage 3: Dialectical Analysis

### Steelmanned Argument
AI infrastructure narratives may be built on *booked plans* rather than *delivered reality*. When power and construction are the binding constraints, “planned GW” numbers can function as hype, enabling financing and GPU orders that are disconnected from near-term feasibility. This creates systemic risk: if delivery lags, debt and equity narratives can unwind rapidly.

### Strongest Counterarguments
1. **Delays are normal**: large infrastructure pipelines routinely include “announced” projects that later slip; this is not necessarily deception.
2. **Absorption vs delivery**: actual physical capacity can be built faster than “occupied absorption” suggests.
3. **Strategic buildout**: hyperscalers may pursue projects for strategic positioning even under low near-term profitability.

### Supporting Theories

| Theory/Framework | Source ID | How It Supports |
|------------------|-----------|-----------------|
| Capital-cost sensitivity and debt fragility | zitron-2026-beginning-of-history | Macro shocks amplify buildout risk |

### Contradicting Theories

| Theory/Framework | Source ID | Point of Conflict |
|------------------|-----------|-------------------|
| “Rents shift, not necessarily collapse” | gestaltu-2026-frontier-labs-profits-thread | Suggests low profits and bottleneck rents without a discrete crash |

### Synthesis Notes
The durable contribution here is: **treat pipeline numbers as a staged funnel**, not a forecast. The “lying” claim should be reformulated as “systematically overstating near-term delivery.”

### Claims to Cross-Reference
- CBRE absorption definitions and totals: RESOURCE-2026-018
- Sightline pipeline-at-risk quantification: RESOURCE-2026-019
- Debt issuance and financing totals: ECON-2026-960

---

### Claim Summary

| ID | Type | Domain | Layer | Actor | Scope | Quantifier | Evidence | Credence | Claim |
|----|------|--------|-------|-------|-------|------------|----------|----------|-------|
| RESOURCE-2026-017 | [F] | RESOURCE | ASSERTED | OTHER:US data center developers | who=US pipeline; where=US; when=2025-2026 | some | E4 | 0.60 | Planned US data center capacity is ~241-245 GW with ~33% under active development |
| RESOURCE-2026-018 | [F] | RESOURCE | ASSERTED | OTHER:CBRE | who=primary markets; where=North America; when=2025 | N/A | E2 | 0.80 | CBRE reports ~2.5 GW net absorption in 2025 across 8 primary markets |
| RESOURCE-2026-019 | [F] | RESOURCE | ASSERTED | OTHER:Sightline Climate | who=global pipeline; where=global; when=2026 | N/A | E4 | 0.75 | Sightline: ~16 GW planned for 2026 but only ~5 GW under construction |
| ECON-2026-960 | [F] | ECON | ASSERTED | OTHER:US credit markets | who=datacenter debt; where=US; when=2025 | N/A | E4 | 0.40 | US data center debt deals totaled ~$178.5B in 2025 (as cited) |
| ECON-2026-961 | [F] | ECON | ASSERTED | OTHER:OpenAI/Anthropic | who=OpenAI/Anthropic; where=Azure/AWS; when=to 2025-09 | N/A | E4 | 0.60 | OpenAI spent ~$8.67B on Azure and Anthropic ~$2.66B on AWS through Sep 2025 |
| ECON-2026-962 | [F] | ECON | ASSERTED | OTHER:CoreWeave | who=CoreWeave; where=financials; when=2025 | N/A | E4 | 0.45 | CoreWeave is junk-rated and highly concentrated; lost ~$1.2B (as reported) |
| ECON-2026-963 | [F] | ECON | ASSERTED | OTHER:neoclouds | who=CoreWeave/Nebius/Applied Digital; where=financials; when=2025 | some | E4 | 0.40 | Neocloud revenue/loss figures as quoted in the post |
| RISK-2026-967 | [F] | RISK | PRACTICED | OTHER:Amazon | who=Amazon; where=marketplaces; when=2026-03 | some | E4 | 0.40 | Amazon outages were linked to AI tools; caused ~120k and ~6.3M lost orders |
| RISK-2026-968 | [F] | RISK | PRACTICED | OTHER:Meta | who=Meta; where=internal systems; when=2026-03 | some | E4 | 0.45 | Meta had a sec-1 incident linked to an in-house AI agent posting without approval |
| SOC-2026-040 | [H] | SOC | PRACTICED | OTHER:hyperscalers | who=Meta/OpenAI/etc; where=internal; when=2025-2026 | some | E4 | 0.55 | “Tokenmaxxing” incentives gamify LLM usage inside hyperscalers |

### Claims to Register

```yaml
claims:
  # Canonical claims artifact:
  # analysis/sources/zitron-2026-ai-industry-lying.yaml
  - id: "RESOURCE-2026-017"
  - id: "RESOURCE-2026-018"
  - id: "RESOURCE-2026-019"
  - id: "ECON-2026-960"
  - id: "ECON-2026-961"
  - id: "ECON-2026-962"
  - id: "ECON-2026-963"
  - id: "RISK-2026-967"
  - id: "RISK-2026-968"
  - id: "SOC-2026-040"
```

---

**Analysis Date**: 2026-03-28  
**Analyst**: gpt-5  
**Credence in Analysis**: 0.70

## Analysis Log

| Pass | Date | Tool | Model | Duration | Tokens | Cost | Notes |
|------|------|------|-------|----------|--------|------|-------|
| 1 | 2026-03-28 | codex | gpt-5 | ? | ? | ? | Initial 3-stage analysis + extracted claims; verified CBRE absorption and Sightline under-construction vs planned metrics. |

