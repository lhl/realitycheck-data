# Source Analysis: A Country Full of Geniuses

> **Claim types**: `[F]` fact, `[T]` theory, `[H]` hypothesis, `[P]` prediction, `[A]` assumption, `[C]` counterfactual, `[S]` speculation, `[X]` contradiction
> **Evidence**: **E1** systematic review/meta-analysis; **E2** peer-reviewed/official stats/law; **E3** expert consensus/preprint; **E4** credible journalism/industry/primary docs; **E5** opinion/analysis/forecast; **E6** unsupported/speculative

## Metadata

| Field | Value |
|---|---|
| **Source ID** | `harries-2026-country-full-of-geniuses` |
| **Title** | A Country Full of Geniuses |
| **Author(s)** | JP Harries |
| **Date** | 2026-02-13 |
| **Type** | ESSAY (blog) |
| **URL** | https://jph.me/essays/a-country-full-of-geniuses/ |
| **Reliability** | 0.60 |
| **Rigor Level** | [REVIEWED] |
| **Bias Notes** | Author runs an AI evaluation company and is both professionally and emotionally proximate to the subject; incentives skew toward urgency/framing “inflection point.” Strength: heavy citation to primary/near-primary sources (METR, OpenAI/Anthropic docs, SEC filings). Weakness: key conclusions lean on extrapolation, interpretive metaphors (“nation of geniuses”), and a mix of personal anecdotes and vendor/industry self-report. |

**Claims YAML**: [`analysis/sources/harries-2026-country-full-of-geniuses.yaml`](harries-2026-country-full-of-geniuses.yaml)

## Stage 1: Descriptive Analysis

### Core Thesis
AI capability and deployable scale crossed a qualitative threshold in early February 2026 (especially via agentic coding), implying rapid near-term disruption to knowledge work and a widening gap between accelerating model capability and slow-moving institutions; therefore governance, safety, and distributional institutions must adapt now.

### Summary (Neutral)
Harries opens with work anecdotes meant to communicate a step-change in personal throughput from agentic AI systems: long multi-step analysis/reporting tasks, spreadsheet modeling, and end-to-end software features produced from minimal prompting. He argues these experiences are not isolated and cites industry observers to support that insiders perceive an “insider wave / outsider calm” dynamic.

The essay then frames the “first week of February 2026” as an inflection point, contextualizing it with late-2025 releases and a shortened cadence between major frontier model updates. It introduces a central measurement lens via METR’s “time horizon” metric, claiming a long-run exponential trend with possible post-2024 acceleration. Harries uses this to extrapolate near-term milestones (multi-hour → multi-day autonomous work) while acknowledging external-validity caveats: benchmarked software tasks are cleaner than real-world organizational work.

From there, the essay generalizes from software engineering to broader screen-based work. It leans on OpenAI’s GDPval benchmark as evidence that task-level parity is spreading across many professional domains, and it argues that domains with high decomposability, verifiability, and tool-compatibility are particularly exposed. It further claims that reinforcement learning/post-training is becoming a faster axis of improvement than training entirely new “foundations,” potentially making progress more robust to certain compute bottlenecks.

Finally, Harries argues the world is not institutionally prepared: capital deployment (AI infrastructure spend + fundraising valuations) is portrayed as massive and difficult to unwind; safety incidents are presented as already-occurring examples of agent failures; and alignment/evaluation are framed as immature relative to the pace of deployment. The essay closes with scenario-style futures (managed transition vs unraveling vs slow build) and a call for concrete governance capacity, deployment controls, international coordination, and distributional politics.

### Key Claims

| # | Claim | Claim ID | Layer | Actor | Scope | Quantifier | Type | Domain | Evid | Credence | Verified? | Falsifiable By |
|---:|---|---|---|---|---|---|---|---|---|---:|---|---|
| 1 | SemiAnalysis reports Claude Code authors ~4% of GitHub public commits as of 2026-02 and projects rapid growth | TECH-2026-995 | EFFECT | OTHER:Claude Code | who=public GitHub repos; where=GitHub; when=~2026-02; predicate=share of public commits authored by Claude Code | OTHER:~4% | [F] | TECH | E4 | 0.60 | See Stage 2 | Reproduction from independent GitHub telemetry shows materially different share for the same definition/time window |
| 2 | METR reports frontier time-horizon doubled ~every 7 months over 2019–2025 (≈196 days), and faster since 2024 under TH1.1 (≈89 days) | TECH-2026-996 | EFFECT | OTHER:METR | who=frontier model agents; where=software/reasoning tasks; when=2019–2026; predicate=time horizon doubling-time estimates | OTHER:~7 months; ~89 days since 2024 | [F] | TECH | E3 | 0.80 | See Stage 2 | METR-cited sources/updates retract or materially revise the quoted doubling-time estimates |
| 3 | Extrapolating recent time-horizon growth implies multi-day autonomous work by ~mid-2027 and ~40h “work-week” horizon by ~early-2027 | TECH-2026-997 | ASSERTED | OTHER:JP Harries | who=frontier model agents; where=knowledge work; when=2026–2027; predicate=time-horizon milestone timing | OTHER:multi-day by ~mid-2027 | [P] | TECH | E5 | 0.25 | In-source | By 2027-06, frontier agents’ time horizon remains well below multi-day work under comparable measurement, and trendline fails to sustain |
| 4 | GDPval evaluates models on real-world tasks across 44 occupations; on the 220-task gold subset, Claude Opus 4.1 outputs were rated better-or-tied vs human in 47.6% of tasks | TECH-2026-998 | EFFECT | OTHER:OpenAI | who=frontier models; where=GDPval gold subset; when=2025-09–2025-10; predicate=pairwise expert preference vs human baseline | OTHER:47.6% | [F] | TECH | E3 | 0.75 | See Stage 2 | GDPval paper/artifacts do not contain the quoted 44-occupation scope and/or the 47.6% result |
| 5 | OpenAI claims GPT-5.3-Codex was “instrumental in creating itself,” with early versions helping debug training, manage deployment, and diagnose evaluations | TECH-2026-999 | ASSERTED | OTHER:OpenAI | who=OpenAI Codex team; what=model assisted development; when=2026-02; predicate=AI-assisted R&D loop | N/A | [F] | TECH | E4 | 0.85 | See Stage 2 | OpenAI retracts/edits the claim or provides clarifications contradicting the described usage |
| 6 | The largest tech companies’ AI-infrastructure spend is claimed to be >$357B (2025) with 2026 guidance $612–$642B | ECON-2026-922 | PRACTICED | OTHER:Big Tech | who=largest tech firms; where=global; when=2025–2026; predicate=AI infrastructure spend / capex guidance | OTHER:$357B; $612–$642B | [F] | ECON | E4 | 0.55 | ? | Review SEC filings and attributable “AI infra” definitions; aggregated sums materially differ |
| 7 | Anthropic funding rounds: $3.5B @ $61.5B (2025-03), $13B @ $183B (2025-09), $30B @ $380B (2026-02) post-money valuations | ECON-2026-923 | PRACTICED | OTHER:Anthropic | who=Anthropic; where=venture financing; when=2025–2026; predicate=round sizes + post-money valuation | OTHER:$61.5B/$183B/$380B | [F] | ECON | E4 | 0.85 | See Stage 2 | Anthropic press releases/credible reporting contradict amounts/valuation/dates |
| 8 | Public incidents show agentic systems can execute destructive actions (e.g., Antigravity wiped a drive; Replit agent wiped a prod DB) | RISK-2026-954 | EFFECT | OTHER:AI agents | who=end-users; where=developer tools; when=2025; predicate=unintended destructive actions | some | [F] | RISK | E4 | 0.75 | See Stage 2 | Credible reporting corrections show the incidents did not occur as described |
| 9 | Safety/alignment evaluation is immature and increasingly hard to bound as models near/surpass their evaluations; evaluation may become self-referential (AI evaluating AI) | RISK-2026-955 | ASSERTED | OTHER:AI labs/researchers | who=frontier labs; where=safety eval; when=2024–2026; predicate=epistemic limits + evaluation difficulty | N/A | [T] | RISK | E4 | 0.60 | In-source | Evidence of stable, widely adopted, validated alignment/eval best practices that reliably bound dangerous capabilities under deployment conditions |
| 10 | Institutional readiness is a key bottleneck: model capability compounds faster than organizational adaptation, creating governance and safety lag | TRANS-2026-040 | EFFECT | OTHER:Institutions | who=orgs/regulators; where=regulated deployments; when=2026+; predicate=capability→deployment gap | often | [H] | TRANS | E5 | 0.55 | In-source | Broad evidence shows institutional adaptation rates match/exceed capability growth, preventing lag accumulation |
| 11 | If AI capital captures most value relative to labor, modern social contracts tied to labor income/status/voice come under pressure, requiring new distributional arrangements | TRANS-2026-041 | EFFECT | OTHER:Society | who=workers/citizens; where=capitalist democracies; when=~2026–2035; predicate=distributional stress | some | [H] | TRANS | E5 | 0.45 | In-source | Strong evidence that labor-share and political voice remain stable under widespread AI deployment without major redistribution/governance changes |

### Argument Structure

```
(1) Agentic tools produce large, recent productivity jumps (anecdotes + early diffusion signals)
        ↓
(2) Frontier progress is accelerating (shorter release cadence; METR time-horizon trend)
        ↓
(3) Coding is the leading indicator (decomposable, verifiable, tool-compatible)
        ↓
(4) Broader knowledge-work parity is rising (GDPval + other benchmarks)
        ↓
(5) Capital deployment + scale make reversal unlikely; safety incidents already occur
        ↓
(6) Institutions adapt slower than capability → transition risk
        ↓
(7) Therefore: build governance + safety + distribution capacity now
```

**Chain Analysis**:
- **Weakest link**: (2)→(4) generalization from benchmark trends to broad real-world autonomy and economic displacement.
- **Why weak**: time-horizon / benchmark performance are sensitive to task distributions, scaffolding, and deployment friction; “task parity” is not “job parity.”
- **If link breaks**: near-term disruption could be slower/patchier, giving institutions more time; but the essay’s “prepare institutions” conclusion may still hold (just with different urgency).

### Theoretical Lineage
- **“Country of geniuses” framing**: Amodei’s “country of geniuses in a datacenter” metaphor and related essays on compressed progress and governance.
- **Time-horizon evaluation**: METR’s long-task capability trendline (TH1/TH1.1) as a compact scaling proxy for autonomy.
- **Post-AGI political economy**: Drago & Laine “Intelligence Curse” framing for rent-allocation and social-contract stress under AI capital dominance.
- **Benchmarks-to-economy**: GDPval’s attempt to measure economically valuable tasks as a leading indicator rather than lagging adoption metrics.

### Scope & Limitations
- Strongest when it is a *synthesis of cited sources* (METR, OpenAI/Anthropic, specific incident reports).
- Weakest where it asks the reader to accept *extrapolations* (rapid milestone timelines) and *macro-institutional conclusions* from a small number of quantitative anchors.
- Not a labor-economics model; distributional/political claims are primarily conceptual and scenario-like.

## Stage 2: Evaluative Analysis

### Internal Coherence
The essay is coherent as a “capability trend → economic implication → governance response” argument. It generally distinguishes task-level capability from whole-job automation and notes external-validity caveats. Its main internal vulnerability is urgency inflation: rapid changes in a subset of agentic coding workflows are treated as strong evidence for broad near-term transformation, while “deployment friction” is acknowledged but not deeply modeled.

### Key Factual Claims Verified

| Claim ID | Claim (paraphrased) | Crux? | Source Says | Actual | External Source | Search Notes | Status |
|---|---|---:|---|---|---|---|---|
| TECH-2026-996 | METR time-horizon frontier doubling time ~7 months historically; faster in recent window (e.g., since 2024 ~89 days under TH1.1) | **Y** | ~7 months (2019–2024); ~3–4 months since 2025 | METR TH1.1 states stitched/hybrid doubling time = 196 days (~7 months) and since 2024 doubling time = 89 days (TH1.1). | https://metr.org/blog/2026-1-29-time-horizon-1-1/ | q1 “METR Time Horizon 1.1 196 days doubling time”; q2 “METR TH1.1 89 days since 2024”; (2026-02-20) | ok |
| TECH-2026-995 | SemiAnalysis reports Claude Code authors ~4% of GitHub public commits “right now” | N | “4% of GitHub public commits are being authored by Claude Code right now” | Statement appears in SemiAnalysis post; underlying telemetry not independently reproduced in this pass. | https://newsletter.semianalysis.com/p/claude-code-is-the-inflection-point | q1 “Claude Code 4% GitHub public commits”; q2 “SemiAnalysis Claude Code inflection point 4%”; (2026-02-20) | ok (in-source) |
| TECH-2026-998 | GDPval spans 44 occupations; on gold subset, Claude Opus 4.1 wins+ties vs human in 47.6% | N | “44 occupations…”; “just under half…” | OpenAI GDPval page states 44 occupations and release date; GDPval paper reports 47.6% wins+ties on gold subset for Claude Opus 4.1. | https://openai.com/index/gdpval ; https://arxiv.org/pdf/2510.04374.pdf | q1 “GDPval 44 occupations OpenAI September 25 2025”; q2 “GDPval gold subset 47.6% Claude Opus 4.1”; (2026-02-20) | ok |
| TECH-2026-999 | OpenAI claims GPT-5.3-Codex was “instrumental in creating itself” via internal engineering/research workflows | N | “instrumental in creating itself…” | The quoted claim appears in OpenAI’s GPT‑5.3‑Codex release post. | https://openai.com/index/introducing-gpt-5-3-codex/ | q1 “Introducing GPT‑5.3‑Codex instrumental in creating itself”; q2 “GPT‑5.3‑Codex debug training manage deployment diagnose test results”; (2026-02-20) | ok (in-source) |
| ECON-2026-923 | Anthropic Series E/F/G funding amounts + post-money valuations | N | $3.5B @ $61.5B; $13B @ $183B; $30B @ $380B | Anthropic press releases match dates/amounts/valuations. | https://www.anthropic.com/news/anthropic-raises-series-e-at-usd61-5b-post-money-valuation ; https://www.anthropic.com/news/anthropic-raises-series-f-at-usd183b-post-money-valuation ; https://www.anthropic.com/news/anthropic-raises-30-billion-series-g-funding-380-billion-post-money-valuation | q1 “Anthropic Series E $61.5B $3.5B”; q2 “Anthropic Series G $380B $30B”; (2026-02-20) | ok |
| RISK-2026-954 | Public reporting: Antigravity wiped a user’s drive; Replit agent wiped prod DB affecting ~1,200 executives | N | Two incidents presented as already occurred | Reporting exists for both incidents; details vary and are partly based on user-post documentation. | https://www.theregister.com/2025/12/01/google_antigravity_wipes_d_drive/ ; https://fortune.com/2025/07/23/ai-coding-tool-replit-wiped-database-called-it-a-catastrophic-failure/ | q1 “Google Antigravity wipes D drive”; q2 “Replit agent deleted production database 1200 executives”; (2026-02-20) | ok |

### Disconfirming Evidence Search

| Claim | Counterevidence Found | Alternative Explanation | Search Notes |
|---|---|---|---|
| “Time horizon → near-term multi-day autonomy” | METR emphasizes suite/protocol sensitivity and domain variation; OSWorld-style GUI agents can remain far shorter-horizon than coding tasks | The time-horizon curve may be a strong proxy for *coding-task autonomy* but a weak proxy for broader organizational work; deployment reliability and incentives may bottleneck | Searched “METR time horizon external validity” and reviewed METR cross-domain analysis: `metr-2025-time-horizon-vary-across-domains` (2026-02-20) |
| “4% of GitHub commits are authored by Claude Code” | Measurement definition risks: author vs committer vs co-authored; public-only vs total; bot detection; “authored by” may be inferred not directly observed | The share may be directionally correct but sensitive to telemetry choices and to rapid short-term fluctuations | Searched for independent corroboration; none located during this pass beyond SemiAnalysis itself (2026-02-20) |
| “GDPval parity implies near-term labor-market shock” | GDPval is task-level, highly scaffolded, and graded via pairwise preference; it does not capture organizational integration, liability, or relationship-heavy work | GDPval may be a leading indicator of “parts of jobs” and cost pressure, but job-level displacement may be delayed by adoption frictions and regulation | Reviewed GDPval paper limitations sections; searched “GDPval limitations preference grading scaffolding” (2026-02-20) |

### Corrections & Updates

| Item | URL | Published | Corrected/Updated | What Changed | Impacted Claim IDs | Action Taken |
|---|---|---:|---:|---|---|---|
| GDPval parity trajectory claims beyond the paper | https://artificialanalysis.ai/evaluations/gdpval-aa | N/A | Observed 2026-02-20 | Essay’s “GPT-5.2 ~71%” and “Opus 4.6 leads” statements were not located in GDPval paper; Artificial Analysis reports GDPval‑AA primarily as Elo ratings and currently highlights Claude Sonnet 4.6 as top | TECH-2026-998 | Treat the essay’s “rapid to 70%+ parity” numeric trajectory as unverified in this pass; keep extracted claim anchored to paper + benchmark definition |
| “AI infrastructure spend” aggregation | N/A | N/A | Observed 2026-02-20 | Aggregation of “AI infrastructure spend” from SEC filings is definition-sensitive; this pass did not reproduce the $357B / $612–$642B totals from filings | ECON-2026-922 | Keep claim at lower credence and evidence level E4 pending a dedicated capex attribution audit |

### Internal Tensions / Self-Contradictions

| Tension | Parts in Conflict | Implication |
|---|---|---|
| Caveat vs urgency | Acknowledges benchmarks are “clean” while later extrapolations are presented with confident milestone dates | Readers may overweight the extrapolated timeline relative to the stated uncertainty |
| “Institutional readiness is bottleneck” vs “even if progress stopped” | Claims organizational change is main bottleneck, yet also claims *current* capability already exceeds readiness even with zero further progress | The call-to-action can be correct under both frames, but the implied timeline for governance differs |

### Persuasion Techniques

| Technique | Example from Source | Effect on Reader |
|---|---|---|
| Vivid metaphor | “Country of geniuses in a datacenter” as a nation appearing overnight | Compresses complex capability+deployment into an intuitive, urgent mental model |
| Salient anecdotes | Personal “one prompt → 17-page deck” and “feature from my phone” stories | Increases perceived immediacy; risk of selection bias |
| Extrapolation anchoring | Uses a few quantitative anchors (time horizon) to project a full-year timeline | Encourages linear reading of exponential plots and may underweight saturation/regime change |
| Moral framing | Social contract “threatened” if humans lose economic relevance | Raises stakes beyond productivity; can polarize interpretation |

### Unstated Assumptions

| Assumption | Claim ID | Critical? | Problematic? |
|---|---|---:|---:|
| Time-horizon gains transfer from benchmark tasks to messy real-world work with similar cadence | TECH-2026-997 | Y | Y |
| Agent failures will not be contained by product/process controls before high-stakes deployment | RISK-2026-954; RISK-2026-955 | Y | ? |
| Capital deployment implies political/organizational lock-in (cannot “change mind” without crisis) | ECON-2026-922 | N | ? |
| Labor-based social contracts cannot re-equilibrate via new roles/markets fast enough | TRANS-2026-041 | Y | ? |

### Evidence Assessment
Strengths:
- Uses multiple quantitative anchors with citations (METR; GDPval; specific incident reporting).
- Distinguishes “task parity” from “whole-job automation,” which improves conceptual hygiene.

Weaknesses:
- Several important numeric claims depend on vendor or industry analysis without independent reproduction.
- The central “milestone timeline” is extrapolation-heavy and sensitive to trend definition and task distribution.
- Macro-political conclusions are plausible but not evidence-complete; they function more as scenario prompts than demonstrated forecasts.

### Credence Assessment
- **Overall Credence**: 0.60
- **Reasoning**: The essay’s *directional* thesis (rapid improvement + institutional lag) is well supported by cited sources and broadly consistent with independent capability tracking. The *timeline specificity* and some macro-economic claims rely on extrapolation and definition-sensitive aggregations, so the confident urgency should be discounted relative to the empirical core.

## Stage 3: Dialectical Analysis

### Steelmanned Argument
Even if we debate exact milestones, multiple independent indicators (coding-agent diffusion, long-task capability trends, cross-occupation deliverable benchmarks, and capital buildout) suggest AI is transitioning from “assistive tool” to “delegable coworker.” Institutions are historically slow to adapt to new capability regimes, and governance capacity tends to lag especially in fast-moving, technical domains. Therefore, the correct response is to build adaptive capacity early: regulatory competence, deployment gating for high-risk domains, international safety coordination, and distribution mechanisms to preserve social stability if labor’s economic role declines.

### Strongest Counterarguments
1. **External validity / bottlenecks**: time-horizon and GDPval results may not translate to real-world autonomy at scale due to reliability, specification, integration, and liability constraints; adoption is slower than capability.
2. **Metric gaming / scaffolding dependence**: measured capability can improve via better harnesses and tool scaffolds without corresponding reductions in human supervision needs.
3. **Economic equilibrium response**: labor markets and institutions may adapt through new complementary roles, policy reforms, and demand expansion; “social contract collapse” is not the default.
4. **Governance feasibility**: the proposed governance stack may be politically infeasible; premature controls could entrench incumbents or fuel international race dynamics.

### Supporting Theories

| Theory/Framework | Source ID | How It Supports |
|---|---|---|
| Time-horizon as autonomy proxy with exponential trend (with suite sensitivity caveats) | `metr-2026-time-horizon-1-1` | Supports the claim that long-task capability is rising quickly and that measurement is hard but informative |
| “Country of geniuses” as scaling metaphor for labor-like AI supply | `amodei-2024-machines-of-loving-grace` | Provides the core metaphor and governance framing for massive scalable cognitive labor |
| “AI makes AI” feedback loop (human-supervised but accelerating) | `openai-2026-gpt-5-3-codex` | Provides first-party evidence that internal workflows are already being accelerated by agentic tools |

### Contradicting Theories

| Theory/Framework | Source ID | Point of Conflict |
|---|---|---|
| Domain variation and non-transferability of autonomy | `metr-2025-time-horizon-vary-across-domains` | Undercuts simple “coding → everything” generalization; GUI/real-world tasks may remain shorter-horizon |
| “Automated coding ≠ software engineering” hypothesis | `mathrachel-2026-automated-coding-not-se-thread` | Suggests “code writing” may automate faster than end-to-end SWE, weakening extrapolation from coding productivity to broader autonomy |
| Profit/value capture shifts away from labs | `gestaltu-2026-frontier-labs-profits-thread` | Challenges the implied political economy of value capture and “AI capital dominance” being centralized in labs |

### Synthesis Notes
This essay is best read as a synthesis/dispatch: it connects multiple already-existing indicators (agent diffusion, long-task trends, occupational-task evaluations, capital buildout) into a single coherent “institutional lag” story. The core upgrade it offers is not a new metric but a governance framing: treat AI scaling as a new “nation-like” actor and optimize institutions for rapid adaptation under uncertainty.

### Claims to Cross-Reference
- The “AI infrastructure spend” aggregation and guidance: audit definitions and reconcile to SEC-reported capex categories (and prior analyses of AI capex).
- GDPval trajectory claims (“~71%” etc): locate the exact metric/source or remove if not well grounded.
- Independent GitHub telemetry for “Claude Code share” and definition consistency (author/committer, bots, public vs private).

---

### Claim Summary

| ID | Type | Domain | Layer | Actor | Scope | Quantifier | Evidence | Credence | Claim |
|---|---|---|---|---|---|---|---|---:|---|
| TECH-2026-995 | [F] | TECH | EFFECT | OTHER:Claude Code | who=public GitHub repos; where=GitHub; when=~2026-02 | OTHER:~4% | E4 | 0.60 | SemiAnalysis reports Claude Code authors ~4% of GitHub public commits as of 2026-02 and projects rapid growth |
| TECH-2026-996 | [F] | TECH | EFFECT | OTHER:METR | who=frontier model agents; where=software/reasoning tasks; when=2019–2026 | OTHER:~7 months; ~89 days since 2024 | E3 | 0.80 | METR reports frontier time-horizon doubled ~every 7 months historically and faster since 2024 under TH1.1 |
| TECH-2026-997 | [P] | TECH | ASSERTED | OTHER:JP Harries | who=frontier model agents; where=knowledge work; when=2026–2027 | OTHER:multi-day by ~mid-2027 | E5 | 0.25 | Extrapolating recent time-horizon growth implies multi-day autonomous work by ~mid-2027 and ~40h horizon by ~early-2027 |
| TECH-2026-998 | [F] | TECH | EFFECT | OTHER:OpenAI | who=frontier models; where=GDPval gold subset; when=2025-09–2025-10 | OTHER:47.6% | E3 | 0.75 | GDPval spans 44 occupations; on gold subset, Claude Opus 4.1 wins+ties vs human in 47.6% |
| TECH-2026-999 | [F] | TECH | ASSERTED | OTHER:OpenAI | who=OpenAI Codex team; what=model assisted development; when=2026-02 | N/A | E4 | 0.85 | OpenAI claims GPT-5.3-Codex was “instrumental in creating itself” via internal workflows |
| ECON-2026-922 | [F] | ECON | PRACTICED | OTHER:Big Tech | who=largest tech firms; where=global; when=2025–2026 | OTHER:$357B; $612–$642B | E4 | 0.55 | The largest tech companies’ AI-infrastructure spend is claimed to be >$357B (2025) with 2026 guidance $612–$642B |
| ECON-2026-923 | [F] | ECON | PRACTICED | OTHER:Anthropic | who=Anthropic; where=venture financing; when=2025–2026 | OTHER:$61.5B/$183B/$380B | E4 | 0.85 | Anthropic rounds: $3.5B @ $61.5B; $13B @ $183B; $30B @ $380B post-money valuations |
| RISK-2026-954 | [F] | RISK | EFFECT | OTHER:AI agents | who=end-users; where=developer tools; when=2025 | some | E4 | 0.75 | Public incidents show agentic systems can execute destructive actions (Antigravity drive wipe; Replit prod DB wipe) |
| RISK-2026-955 | [T] | RISK | ASSERTED | OTHER:AI labs/researchers | who=frontier labs; where=safety eval; when=2024–2026 | N/A | E4 | 0.60 | Safety/alignment evaluation is immature and increasingly hard to bound as models near/surpass their evaluations |
| TRANS-2026-040 | [H] | TRANS | EFFECT | OTHER:Institutions | who=orgs/regulators; where=regulated deployments; when=2026+ | often | E5 | 0.55 | Institutional readiness is a key bottleneck: capability compounds faster than organizational adaptation |
| TRANS-2026-041 | [H] | TRANS | EFFECT | OTHER:Society | who=workers/citizens; where=capitalist democracies; when=~2026–2035 | some | E5 | 0.45 | If AI capital captures most value relative to labor, labor-based social contracts come under pressure |

### Claims to Register

```yaml
claims:
  - id: "TECH-2026-995"
    text: "SemiAnalysis reports Claude Code authors about 4% of GitHub public commits as of February 2026."
    type: "[F]"
    domain: "TECH"
    evidence_level: "E4"
    credence: 0.60
    operationalization: "Define 'authored by Claude Code' (author attribution vs co-author tags vs committer) and reproduce the estimate via GitHub public event data over the same window."
    assumptions: ["SemiAnalysis' telemetry methodology is correctly specified and not dominated by attribution artifacts."]
    falsifiers: ["Independent reproduction shows a materially different share under the same definition/window."]
    source_ids: ["harries-2026-country-full-of-geniuses"]

  - id: "TECH-2026-996"
    text: "METR reports a long-run frontier time-horizon doubling time of about 196 days (~7 months) and a faster doubling time of about 89 days since 2024 under TH1.1."
    type: "[F]"
    domain: "TECH"
    evidence_level: "E3"
    credence: 0.80
    operationalization: "Recompute doubling-time fits from METR TH1/TH1.1 released estimates using METR's described frontier selection rules and confirm quoted doubling times."
    assumptions: ["METR's published trendline procedures are stable and correctly interpreted."]
    falsifiers: ["Recomputed doubling times differ materially from 196 days overall or 89 days since 2024 under reasonable reproductions."]
    source_ids: ["harries-2026-country-full-of-geniuses"]

  - id: "TECH-2026-997"
    text: "If recent time-horizon growth persists, multi-day autonomous work could arrive by mid-2027 and a ~40-hour work-week horizon by early 2027."
    type: "[P]"
    domain: "TECH"
    evidence_level: "E5"
    credence: 0.25
    operationalization: "Track METR time-horizon estimates through 2027 and test whether frontier models reach multi-day horizons under comparable protocols."
    assumptions: ["Recent trendline remains roughly exponential over 2026–2027.", "Time-horizon measurement remains comparable as tasks/scaffolds evolve."]
    falsifiers: ["By 2027-06, frontier time horizons remain well below multi-day work and the extrapolation fails."]
    source_ids: ["harries-2026-country-full-of-geniuses"]

  - id: "TECH-2026-998"
    text: "GDPval spans 44 occupations; on the 220-task gold subset, Claude Opus 4.1 outputs were rated better than or tied with the human deliverable in 47.6% of tasks."
    type: "[F]"
    domain: "TECH"
    evidence_level: "E3"
    credence: 0.75
    operationalization: "Verify GDPval scope on OpenAI's GDPval page and reproduce the 47.6% win+tie statistic from the GDPval paper/appendix artifacts."
    assumptions: ["The gold subset and grading protocol match the paper's description."]
    falsifiers: ["GDPval artifacts do not support the 44-occupation scope or the 47.6% statistic."]
    source_ids: ["harries-2026-country-full-of-geniuses"]

  - id: "TECH-2026-999"
    text: "OpenAI claims GPT-5.3-Codex was 'instrumental in creating itself' by helping debug training, manage deployment, and diagnose evaluations."
    type: "[F]"
    domain: "TECH"
    evidence_level: "E4"
    credence: 0.85
    operationalization: "Verify the statement is present in OpenAI's release post and track any subsequent edits/clarifications."
    assumptions: ["The release post reflects OpenAI's intended claim about internal usage."]
    falsifiers: ["OpenAI retracts/edits the statement or clarifies it in a way that negates the described usage."]
    source_ids: ["harries-2026-country-full-of-geniuses"]

  - id: "ECON-2026-922"
    text: "The essay claims the world's largest technology companies spent over $357B on AI infrastructure in 2025 and guided $612–$642B for 2026."
    type: "[F]"
    domain: "ECON"
    evidence_level: "E4"
    credence: 0.55
    operationalization: "Define 'AI infrastructure' and reconcile company-reported capex and guidance (SEC filings/earnings) into an attributable aggregate."
    assumptions: ["Company capex/guidance categories can be meaningfully allocated to AI infrastructure."]
    falsifiers: ["A reconciliation using disclosed categories yields materially different totals or shows the claim depends on non-AI capex."]
    source_ids: ["harries-2026-country-full-of-geniuses"]

  - id: "ECON-2026-923"
    text: "Anthropic press releases state: Series E raised $3.5B at a $61.5B post-money valuation (2025-03-03), Series F raised $13B at $183B post-money (2025-09-02), and Series G raised $30B at $380B post-money (2026-02-12)."
    type: "[F]"
    domain: "ECON"
    evidence_level: "E4"
    credence: 0.85
    operationalization: "Verify amounts/dates/valuations in Anthropic's press releases for Series E/F/G."
    assumptions: ["Press releases accurately reflect the financing terms."]
    falsifiers: ["Credible corrections/reporting contradict the announced terms."]
    source_ids: ["harries-2026-country-full-of-geniuses"]

  - id: "RISK-2026-954"
    text: "Public reporting describes agentic systems causing destructive incidents, including Google's Antigravity deleting a user's drive (Dec 2025) and Replit's agent deleting a production database during a code freeze (Jul 2025)."
    type: "[F]"
    domain: "RISK"
    evidence_level: "E4"
    credence: 0.75
    operationalization: "Verify incident reporting and primary artifacts (posts/screenshots) and check for corrections or alternative explanations."
    assumptions: ["Reported incidents reflect real events and not fabricated artifacts."]
    falsifiers: ["Published corrections or primary evidence show incidents did not occur as reported."]
    source_ids: ["harries-2026-country-full-of-geniuses"]

  - id: "RISK-2026-955"
    text: "The essay argues that alignment and safety evaluation are immature, and that reliably ruling out dangerous capability thresholds is becoming increasingly difficult as models approach or surpass their evaluations."
    type: "[T]"
    domain: "RISK"
    evidence_level: "E4"
    credence: 0.60
    operationalization: "Survey system cards and evaluation reports for explicit uncertainty bounds and track whether evaluation coverage expands to keep pace with capability; check for consensus statements on field maturity."
    assumptions: ["System-card statements reflect genuine epistemic limits rather than purely reputational positioning."]
    falsifiers: ["A stable set of validated, widely adopted evaluation+alignment best practices reliably bounds dangerous capabilities under deployment conditions."]
    source_ids: ["harries-2026-country-full-of-geniuses"]

  - id: "TRANS-2026-040"
    text: "Institutional readiness (governance, risk ownership, workflow redesign) is a key bottleneck, with organizational adaptation lagging model capability improvements."
    type: "[H]"
    domain: "TRANS"
    evidence_level: "E5"
    credence: 0.55
    operationalization: "Measure deployment lead times (pilot→prod), governance cycle times, and compliance approval durations versus observed model capability improvement cadence across multiple organizations."
    assumptions: ["Institutional cycle times are relatively stable and not easily compressed by AI adoption itself."]
    falsifiers: ["Across sectors, institutional cycle times compress to match capability cadence, preventing lag accumulation."]
    source_ids: ["harries-2026-country-full-of-geniuses"]

  - id: "TRANS-2026-041"
    text: "If returns to AI capital substantially exceed returns to human labor, labor-based social contracts (income/status/voice via work) come under pressure and require new distributional arrangements."
    type: "[H]"
    domain: "TRANS"
    evidence_level: "E5"
    credence: 0.45
    operationalization: "Track labor share, wage premia, employment composition, and political participation proxies as AI deployment scales; evaluate whether redistribution/policy changes preserve stability."
    assumptions: ["AI-driven productivity gains are captured primarily as capital returns absent policy changes."]
    falsifiers: ["Labor share and political voice remain stable under widespread AI deployment without major redistribution/governance changes."]
    source_ids: ["harries-2026-country-full-of-geniuses"]
```

---

**Analysis Date**: 2026-02-20
**Analyst**: codex (gpt-5.2)
**Credence in Analysis**: 0.70

## Analysis Log

| Pass | Date | Tool | Model | Duration | Tokens | Cost | Notes |
|---:|---|---|---|---:|---:|---:|---|
| 1 | 2026-02-20 | codex | gpt-5.2 | 1m37s | ? | ? | Started; restarted due to ambiguous session auto-detection |
| 2 | 2026-02-20 | codex | gpt-5.2 | 18m53s | 4,796,350 | ? | Initial 3-stage analysis + extracted claims; registered source/claims |

### Revision Notes
- **Pass 2**: Initial write-up, claim extraction, and basic cross-checks against cited primary sources; flagged definition-sensitive aggregations for follow-up.
