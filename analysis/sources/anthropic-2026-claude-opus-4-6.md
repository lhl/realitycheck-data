# Source Analysis: Claude Opus 4.6

> **Claim types**: `[F]` fact, `[T]` theory, `[H]` hypothesis, `[P]` prediction, `[A]` assumption, `[C]` counterfactual, `[S]` speculation, `[X]` contradiction
> **Evidence**: **E1** systematic review/meta-analysis; **E2** peer-reviewed/official stats; **E3** expert consensus/preprint; **E4** credible journalism/industry; **E5** opinion/forecast; **E6** unsupported/speculative

## Metadata

| Field | Value |
|---|---|
| **Source ID** | `anthropic-2026-claude-opus-4-6` |
| **Title** | Claude Opus 4.6 |
| **Author(s)** | Anthropic |
| **Date** | 2026-02-05 |
| **Type** | ARTICLE (Product release) |
| **URL** | https://www.anthropic.com/news/claude-opus-4-6 |
| **Reliability** | 0.60 |
| **Rigor Level** | [REVIEWED] |
| **Bias Notes** | First-party release post with competitive incentives. Capability claims depend on evaluation harness configuration (tools, agent scaffold, sampling, resources). Safety claims rely on Anthropic’s disclosed internal evaluations and may not be independently reproducible. |

**Claims YAML**: [`analysis/sources/anthropic-2026-claude-opus-4-6.yaml`](anthropic-2026-claude-opus-4-6.yaml)

## Stage 1: Descriptive Analysis

### Core Thesis
Anthropic claims Claude Opus 4.6 is a significant upgrade to its flagship model—especially for agentic coding and long-horizon tasks—pairing improved coding/planning with a new 1M-token context window (beta) and product/API features (agent teams, compaction, adaptive thinking, effort controls), while maintaining or improving safety outcomes.

### Summary (Neutral)
The post announces Opus 4.6 and positions it as stronger than Opus 4.5 on coding, agentic workflows, and long-context tasks. It highlights a 1M token context window in beta for Opus-class models, and reports “state-of-the-art” performance on multiple evaluations (Terminal‑Bench 2.0, Humanity’s Last Exam, GDPval‑AA, BrowseComp), with footnotes describing evaluation details and tooling.

Anthropic also emphasizes safety evaluation results, asserting low rates of misaligned behaviors (deception, sycophancy, cooperation with misuse, etc.) and low “over-refusals.” Product updates include Claude Code “agent teams,” and API features including context compaction, adaptive thinking, effort controls, large output limits (up to 128k tokens), and special pricing for very long prompts.

### Key Claims

| # | Claim | Claim ID | Layer | Actor | Scope | Quantifier | Type | Domain | Evid | Credence | Verified? | Falsifiable By |
|---|---|---|---|---|---|---|---|---|---|---:|---|---|
| 1 | Anthropic announced Claude Opus 4.6 on 2026-02-05 | TECH-2026-910 | ASSERTED | OTHER:Anthropic | who=Anthropic; what=model release; when=2026-02-05 | N/A | [F] | TECH | E4 | 0.95 | In-source (header/date) | Official correction/removal of date + announcement |
| 2 | Opus 4.6 is the first Opus-class model to offer 1M token context (beta) | TECH-2026-911 | ASSERTED | OTHER:Anthropic | who=model; what=context limit; when=2026-02; limit=1M | N/A | [F] | TECH | E4 | 0.85 | In-source (intro/API updates) | API docs contradict or limit not available |
| 3 | Opus 4.6 achieves the highest score on Terminal‑Bench 2.0 and leads on Humanity’s Last Exam and BrowseComp | TECH-2026-912 | ASSERTED | OTHER:Anthropic | who=model; what=leaderboard/benchmark dominance; when=2026-02 | N/A | [H] | TECH | E5 | 0.55 | In-source (intro) | Public leaderboards show not top-ranked |
| 4 | On GDPval-AA, Opus 4.6 beats OpenAI GPT‑5.2 by ~144 Elo and Opus 4.5 by 190 | TECH-2026-913 | ASSERTED | OTHER:Anthropic | who=model; what=Elo advantage; when=2026-02; eval=GDPval-AA | N/A | [F] | TECH | E4 | 0.75 | In-source (intro/footnotes) | Independent GDPval-AA reproductions contradict |
| 5 | Opus 4.6 supports outputs up to 128k tokens | TECH-2026-914 | ASSERTED | OTHER:Anthropic | who=model; what=max output; when=2026-02; limit=128k | N/A | [F] | TECH | E4 | 0.80 | In-source (API updates) | API docs/behavior show lower limit |
| 6 | Product/API updates: agent teams, context compaction, adaptive thinking, effort controls | INST-2026-910 | PRACTICED | OTHER:Anthropic | who=Claude users/devs; what=features; when=2026-02 | N/A | [F] | INST | E4 | 0.80 | In-source (Product and API updates) | Docs contradict or features absent |
| 7 | Availability: claude.ai, Anthropic API, major clouds; model name `claude-opus-4-6` | INST-2026-911 | PRACTICED | OTHER:Anthropic | who=users/devs; where=claude.ai/API/cloud; when=2026-02 | N/A | [F] | INST | E4 | 0.85 | In-source (Availability) | API model list contradicts |
| 8 | Base pricing remains $5/$25 per million input/output tokens | ECON-2026-910 | ASSERTED | OTHER:Anthropic | who=devs; what=pricing; when=2026-02; tier=base | N/A | [F] | ECON | E4 | 0.75 | In-source (Availability) | Official pricing docs differ |
| 9 | Premium pricing applies for prompts >200k tokens ($10/$37.50 per million input/output); US-only inference at 1.1× | ECON-2026-911 | ASSERTED | OTHER:Anthropic | who=devs; what=pricing tiers; when=2026-02; threshold=200k | N/A | [F] | ECON | E4 | 0.80 | In-source (API updates) | Official pricing docs contradict |
| 10 | Safety: Opus 4.6 has low misaligned behaviors and lowest over-refusals among recent Claude models (per system card) | RISK-2026-910 | ASSERTED | OTHER:Anthropic | who=model; what=safety audit outcomes; when=2026-02 | N/A | [F] | RISK | E4 | 0.70 | In-source (Safety section) | Third-party evals find higher misalignment/over-refusal |

### Argument Structure

```
(1) Users want long-horizon, agentic work (coding + research + docs) with less supervision burden
        ↓
(2) Opus 4.6 improves planning/coding + adds 1M context (beta) + better long-context retrieval/reasoning
        ↓
(3) Benchmarks (Terminal‑Bench, HLE, BrowseComp, GDPval‑AA) show state-of-the-art performance
        ↓
(4) Product/API features (agent teams, compaction, adaptive thinking, effort controls) enable deployment
        ↓
(5) Safety evaluations indicate gains do not come at the cost of safety
```

**Weakest links**:
- (3): benchmark results depend on harness/tooling; “highest score” claims can become false as leaderboards update.
- (5): safety claims are difficult to independently validate without comparable audits.

### Theoretical Lineage
- **Long-context as capability multiplier**: retrieval/“context rot” mitigation; needle-in-haystack benchmarks.
- **Agentic coding benchmarks**: terminal harnesses; patch/issue resolution task families.
- **Tool-using model governance**: compaction, effort controls, and adaptive thinking as knobs for cost/latency vs quality.
- **Safety-by-evaluation**: reliance on system cards and behavioral audits to ground safety claims.

### Scope & Limitations
- First-party release framing; likely selective in what is emphasized.
- Several claims (especially benchmark superiority and safety profile comparisons) are only as strong as the disclosed methodology.
- Pricing is nuanced: base rates may be unchanged while very-long-context tiers introduce surcharges.

## Stage 2: Evaluative Analysis

### Internal Coherence
The capability and product narrative is internally consistent. The major internal tension is the pricing framing: the post first says pricing “remains the same” at $5/$25 per million tokens, but later specifies premium pricing for prompts exceeding 200k tokens. This is reconcilable (base pricing unchanged; long-context tier priced differently) but is easy to misread.

### Key Factual Claims Verified

| Claim (paraphrased) | Crux? | Source Says | Actual | External Source | Status |
|---|---:|---|---|---|---|
| Opus 4.6 is top-ranked on Terminal‑Bench 2.0 | **Y** | “highest score” | Terminal‑Bench 2.0 leaderboard shows Opus 4.6 rank #2 at 69.9% (±2.5) on 2026-02-05; GPT‑5.3‑Codex is rank #1 (75.1% ±2.4) on 2026-02-06 (agents differ) | https://www.tbench.ai/leaderboard/terminal-bench/2.0 | x (leaderboard top) |
| Opus 4.6 leads GPT‑5.2 by ~144–150 Elo on GDPval‑AA | **Y** | “~144 Elo” | Artificial Analysis reports Opus 4.6 Elo 1606, ~150 points ahead of GPT‑5.2 (xhigh), implying ~70% win rate | https://artificialanalysis.ai/articles/opus-4.6-takes-lead-in-agentic-real-world-knowledge-tasks | ok |
| GDPval tasks span 44 occupations | N | “44 occupations” | OpenAI GDPval page states GDPval spans 44 occupations | https://openai.com/index/gdpval | ok |
| “Pricing remains $5/$25 per million” needs tier nuance | **Y** | $5/$25 per million | Release post also states premium pricing for >200k prompts ($10/$37.50) | https://www.anthropic.com/news/claude-opus-4-6 | ok (but conditional) |

### Disconfirming Evidence Search

| Claim | Counterevidence Found | Alternative Explanation | Search Notes |
|---|---|---|---|
| “Highest score on Terminal‑Bench 2.0” | Terminal‑Bench 2.0 public leaderboard shows Opus 4.6 is not #1 as of 2026-02-06 | “Highest score” may refer to Anthropic’s reproduced runs on their infrastructure/harness, a different agent, or an earlier snapshot | Checked Terminal‑Bench leaderboard entries for Opus 4.6 and GPT‑5.3‑Codex |
| “~144 Elo lead on GDPval‑AA” | No clear refutation found; third-party report exists | Elo gaps may depend on harness (Stirrup), tool policies, and token budgets; may not translate to other agent products | Reviewed Artificial Analysis article summarizing GDPval‑AA methodology and results |
| “Safety profile as good or better than other frontier models” | No external audit found during this pass that reproduces the same behavioral audit | Differences in threat models and test suites could explain the claim even if other labs disagree | Searched for independent reproductions; none located in quick pass |

### Corrections & Updates

| Item | URL | Published | Corrected/Updated | What Changed | Impacted Claim IDs | Action Taken |
|---|---|---:|---:|---|---|---|
| N/A | N/A | N/A | N/A | No corrections observed during capture | N/A | None |

### Internal Tensions / Self-Contradictions

| Tension | Parts in Conflict | Implication |
|---|---|---|
| Pricing framing | “Pricing remains the same” vs premium rates for prompts >200k | Readers may underestimate costs for long-context workloads |
| “Highest score” wording | “Highest score on Terminal‑Bench 2.0” vs public leaderboard not showing #1 | Suggests harness mismatch or stale snapshot; undermines categorical superiority claim |

### Persuasion Techniques

| Technique | Example from Source | Effect on Reader |
|---|---|---|
| Social proof | Many partner quotes praising capability leaps | Encourages inference that improvements are large and widely validated |
| Benchmark authority | Multiple benchmark names + large Elo deltas | Anchors perceived objective superiority despite harness sensitivity |
| Safety reassurance | “Gains do not come at the cost of safety” | Reduces concern without third-party validation in the post |

### Unstated Assumptions

| Assumption | Claim ID | Critical? | Problematic? |
|---|---|---:|---:|
| “Highest score” implies public leaderboard dominance | TECH-2026-912 | Y | Y |
| Elo gains on GDPval‑AA translate to typical enterprise workflows | TECH-2026-913 | N | ? |
| Long context is usable without “context rot” at production load | TECH-2026-911 | Y | ? |

### Evidence Assessment
The best-supported performance claim in this pass is GDPval‑AA Elo (corroborated by an external benchmarking write-up). The least-supported is categorical leaderboard dominance claims (“highest score”) when public leaderboards can diverge based on agents and update cadence.

### Credence Assessment
- **Overall Credence**: 0.62
- **Reasoning**: High confidence on release existence and on feature/pricing statements contained in the post; moderate confidence on external benchmark superiority (depends on harness); lower confidence on broad safety comparisons across “any other frontier model” without matched audits.

## Stage 3: Dialectical Analysis

### Steelmanned Argument
Long-horizon autonomy is the product frontier: models that can hold and reason over massive context, plan agentically, and manage tool use will unlock real workflow automation. Opus 4.6 plausibly improves core ingredients (planning, long-context stability, coding and review) and adds practical controls (effort, compaction, adaptive thinking). If the system card’s safety story holds, this is progress toward more powerful agents without proportionally greater misalignment risk.

### Strongest Counterarguments
1. **Leaderboard claims are brittle**: “highest score” can be false under public leaderboards, different agents, or even small evaluation differences.
2. **Cost and incentives**: long-context premium pricing and higher token use can make “best” models uneconomical for many use cases.
3. **Safety claims remain lab-relative**: without shared audits and threat models, “as good as any frontier model” is hard to interpret.

### Supporting Theories

| Theory/Framework | Source ID | How It Supports |
|---|---|---|
| Long context + tool use enables autonomy | N/A | 1M context and compaction can extend task horizon |
| Effort controls as compute allocation | N/A | User-selectable “effort” can trade latency/cost for performance |

### Contradicting Theories

| Theory/Framework | Source ID | Point of Conflict |
|---|---|---|
| Public evals often fail to predict deployment | N/A | Benchmark wins may not translate to messy real-world workflows |
| Verification bottleneck dominates | ronacher-2026-agent-psychosis | Stronger agents amplify review burden and failure impact |

### Synthesis Notes
Anthropic’s release emphasizes long context, agent teams, and fine-grained effort/cost controls. The strongest externally supported “headline” is GDPval‑AA Elo advantage (via a third-party benchmarking write-up). By contrast, categorical “highest score” claims on public benchmarks can quickly diverge from public leaderboards.

### Claims to Cross-Reference
- Terminal‑Bench 2.0 leaderboard (agent differences; reproducibility constraints).
- GDPval‑AA leaderboard details and Stirrup harness configuration.
- Opus 4.6 system card for definitions of “misaligned behaviors” and audit methodology.

---

### Claim Summary

| ID | Type | Domain | Layer | Actor | Scope | Quantifier | Evidence | Credence | Claim |
|---|---|---|---|---|---|---|---|---:|---|
| TECH-2026-910 | [F] | TECH | ASSERTED | OTHER:Anthropic | who=Anthropic; what=release; when=2026-02-05 | N/A | E4 | 0.95 | Anthropic announced Claude Opus 4.6 on February 5, 2026 |
| TECH-2026-911 | [F] | TECH | ASSERTED | OTHER:Anthropic | who=model; what=1M context; when=2026-02 | N/A | E4 | 0.85 | Opus 4.6 is the first Opus-class model with a 1M token context window (beta) |
| TECH-2026-912 | [H] | TECH | ASSERTED | OTHER:Anthropic | who=model; what=benchmark dominance; when=2026-02 | N/A | E5 | 0.55 | Anthropic claims Opus 4.6 achieves the highest score on Terminal‑Bench 2.0 and leads on HLE and BrowseComp |
| TECH-2026-913 | [F] | TECH | ASSERTED | OTHER:Anthropic | who=model; what=Elo delta; when=2026-02; eval=GDPval-AA | N/A | E4 | 0.75 | Anthropic claims Opus 4.6 beats GPT‑5.2 by ~144 Elo on GDPval‑AA and Opus 4.5 by 190 |
| TECH-2026-914 | [F] | TECH | ASSERTED | OTHER:Anthropic | who=model; what=128k output; when=2026-02 | N/A | E4 | 0.80 | Anthropic claims Opus 4.6 supports outputs up to 128k tokens |
| INST-2026-910 | [F] | INST | PRACTICED | OTHER:Anthropic | who=users/devs; what=features; when=2026-02 | N/A | E4 | 0.80 | Anthropic announced agent teams, compaction, adaptive thinking, and effort controls |
| INST-2026-911 | [F] | INST | PRACTICED | OTHER:Anthropic | who=users/devs; where=claude.ai/API/cloud; when=2026-02 | N/A | E4 | 0.85 | Anthropic states Opus 4.6 is available on claude.ai, API, and major clouds; model name `claude-opus-4-6` |
| ECON-2026-910 | [F] | ECON | ASSERTED | OTHER:Anthropic | who=devs; what=base pricing; when=2026-02 | N/A | E4 | 0.75 | Anthropic states base pricing remains $5/$25 per million input/output tokens |
| ECON-2026-911 | [F] | ECON | ASSERTED | OTHER:Anthropic | who=devs; what=premium tiers; when=2026-02; threshold=200k | N/A | E4 | 0.80 | Anthropic states premium pricing applies for prompts >200k tokens and US-only inference costs 1.1× |
| RISK-2026-910 | [F] | RISK | ASSERTED | OTHER:Anthropic | who=model; what=safety outcomes; when=2026-02 | N/A | E4 | 0.70 | Anthropic claims Opus 4.6 has low misaligned behaviors and low over-refusals (per system card) |

### Claims to Register

```yaml
claims:
  - id: "TECH-2026-910"
    text: "Anthropic announced Claude Opus 4.6 on February 5, 2026."
    type: "[F]"
    domain: "TECH"
    evidence_level: "E4"
    credence: 0.95
    operationalization: "Verify the announcement date and the existence of the official release page and model naming."
    assumptions: []
    falsifiers: ["Anthropic removes or materially revises the announcement and date without replacement."]
    source_ids: ["anthropic-2026-claude-opus-4-6"]

  - id: "TECH-2026-911"
    text: "Anthropic claims Claude Opus 4.6 is the first Opus-class model to offer a 1M token context window (beta)."
    type: "[F]"
    domain: "TECH"
    evidence_level: "E4"
    credence: 0.85
    operationalization: "Confirm context limits in Anthropic API documentation and product settings; test prompts near 1M tokens under stated conditions."
    assumptions: ["The “1M token context” is generally available to users/developers (not only a restricted preview)."]
    falsifiers: ["Official docs contradict the 1M context claim or the limit is not actually available in practice."]
    source_ids: ["anthropic-2026-claude-opus-4-6"]

  - id: "TECH-2026-912"
    text: "Anthropic claims Claude Opus 4.6 achieves the highest score on Terminal-Bench 2.0 and leads other frontier models on Humanity’s Last Exam and BrowseComp."
    type: "[H]"
    domain: "TECH"
    evidence_level: "E5"
    credence: 0.55
    operationalization: "Compare Opus 4.6 against peer models on the same public benchmark versions and leaderboards using matched agent scaffolds and constraints."
    assumptions: ["Benchmark names refer to standard public benchmarks and “highest score” is meant in a public-leaderboard sense."]
    falsifiers: ["Public benchmark leaderboards show Opus 4.6 is not top-ranked under comparable conditions."]
    source_ids: ["anthropic-2026-claude-opus-4-6"]

  - id: "TECH-2026-913"
    text: "Anthropic claims that on GDPval-AA, Opus 4.6 outperforms the next-best model (OpenAI GPT-5.2) by around 144 Elo points and outperforms Claude Opus 4.5 by 190 points."
    type: "[F]"
    domain: "TECH"
    evidence_level: "E4"
    credence: 0.75
    operationalization: "Check the GDPval-AA leaderboard methodology and Elo computation; verify reported Elo and confidence intervals and reproduce with an open harness if possible."
    assumptions: ["Elo conversion and sampling assumptions are valid and comparable across models."]
    falsifiers: ["Independent GDPval-AA reproductions show materially different Elo gaps."]
    source_ids: ["anthropic-2026-claude-opus-4-6"]

  - id: "TECH-2026-914"
    text: "Anthropic claims Claude Opus 4.6 supports outputs of up to 128k tokens."
    type: "[F]"
    domain: "TECH"
    evidence_level: "E4"
    credence: 0.80
    operationalization: "Verify maximum output-token settings in Anthropic API docs and test generation near the limit."
    assumptions: []
    falsifiers: ["API docs or observed behavior show a substantially lower maximum output limit."]
    source_ids: ["anthropic-2026-claude-opus-4-6"]

  - id: "INST-2026-910"
    text: "Anthropic announced product/API updates tied to Opus 4.6 including: Claude Code “agent teams” (preview), context compaction (beta), adaptive thinking, and effort controls."
    type: "[F]"
    domain: "INST"
    evidence_level: "E4"
    credence: 0.80
    operationalization: "Verify feature availability and configuration in Claude Code and Anthropic API documentation."
    assumptions: []
    falsifiers: ["Official product docs contradict feature availability or omit these features for Opus 4.6."]
    source_ids: ["anthropic-2026-claude-opus-4-6"]

  - id: "INST-2026-911"
    text: "Anthropic states Opus 4.6 is available on claude.ai, the Anthropic API, and major cloud platforms, and that developers can use the model name claude-opus-4-6 via the Claude API."
    type: "[F]"
    domain: "INST"
    evidence_level: "E4"
    credence: 0.85
    operationalization: "Confirm model availability and naming in official API model lists and cloud marketplace listings."
    assumptions: []
    falsifiers: ["The model name is not listed in API docs or is unavailable on the stated platforms."]
    source_ids: ["anthropic-2026-claude-opus-4-6"]

  - id: "ECON-2026-910"
    text: "Anthropic states Opus 4.6 pricing remains $5/$25 per million input/output tokens (base pricing)."
    type: "[F]"
    domain: "ECON"
    evidence_level: "E4"
    credence: 0.75
    operationalization: "Check Anthropic’s official pricing documentation for Opus 4.6 base input/output token rates."
    assumptions: ["“Pricing remains the same” refers to standard context lengths and does not exclude surcharges."]
    falsifiers: ["Official pricing docs show different base rates for Opus 4.6."]
    source_ids: ["anthropic-2026-claude-opus-4-6"]

  - id: "ECON-2026-911"
    text: "Anthropic states Opus 4.6 has premium pricing for prompts exceeding 200k tokens ($10/$37.50 per million input/output tokens) and offers US-only inference at 1.1× token pricing."
    type: "[F]"
    domain: "ECON"
    evidence_level: "E4"
    credence: 0.80
    operationalization: "Verify pricing tiers and US-only inference multiplier in official Anthropic API documentation and billing."
    assumptions: []
    falsifiers: ["Official docs contradict the premium pricing thresholds/rates or the US-only inference multiplier."]
    source_ids: ["anthropic-2026-claude-opus-4-6"]

  - id: "RISK-2026-910"
    text: "Anthropic claims Opus 4.6 has an overall safety profile as good as or better than other frontier models, with low rates of misaligned behaviors on its automated behavioral audit and low over-refusal rates, as described in its system card."
    type: "[F]"
    domain: "RISK"
    evidence_level: "E4"
    credence: 0.70
    operationalization: "Review the Opus 4.6 system card for audit definitions and results; compare to other labs’ disclosed safety evaluations and run third-party red-team style tests."
    assumptions: ["The automated audit is meaningful and comparable across versions and model families."]
    falsifiers: ["Independent evaluations find materially higher misaligned behavior or over-refusal than claimed."]
    source_ids: ["anthropic-2026-claude-opus-4-6"]
```

---

**Analysis Date**: 2026-02-06
**Analyst**: codex (gpt-5.2)
**Credence in Analysis**: 0.70

**Credence Reasoning**:
- High confidence on the existence of the release and the feature/pricing statements in the post.
- Benchmark superiority claims are plausible but highly sensitive to harness and leaderboard update cadence.
- Key uncertainty: how Anthropic’s “highest score” statement maps to public leaderboards given agent differences.

## Analysis Log

| Pass | Date | Tool | Model | Duration | Tokens | Cost | Notes |
|---:|---|---|---|---:|---:|---:|---|
| 1 | 2026-02-06 | codex-cli | gpt-5.2 | ? | ? | ? | Initial 3-stage analysis, claim extraction, and cross-check against public leaderboards and third-party benchmark write-up |
