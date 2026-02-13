# AI 2027 Predictions and Primary Resources

This file intentionally contains only:
- prediction statements and scoring targets
- original AI 2027 / AI Futures primary resources

## Executive Summary (Independent, as of February 13, 2026)

- **Overall pace vs original AI 2027 schedule:** **0.70x** (sensitivity: **0.62x-0.78x**) -> **behind schedule overall**.
- **Relative to Dec 31, 2025 updated medians:** **roughly on track to slightly behind**.
- **What is ahead:** compute/capex and datacenter buildout.
- **What is behind:** robust long-horizon autonomous R&D performance and real-world productivity evidence.
- **Core synthesis:** inputs are ahead, benchmark outputs are mixed, full-stack autonomy is behind.
- **Independence rule:** the authors' self-grading post (`https://blog.ai-futures.org/p/grading-ai-2027s-2025-predictions`) is excluded and not used as independent evidence.

## Prediction Set

### 1) Milestone Predictions

| Milestone | Prediction |
|---|---|
| Automated Coder (AC) | Full automation of an AGI project's coding work; Daniel median: Dec 2029; Eli median: Mar 2032 |
| Superhuman Coder (SC) | 30x as many AI research-engineer agents, each 30x faster than the company's best engineer; original scenario timing: Mar 2027; updated Eli ATC median: ~2030 |
| Superhuman AI Researcher (SAR) | Research taste at top-human level; AI fully automates AI R&D |
| Superintelligent AI Researcher (SIAR) | SIAR-to-top-human gap is 2x the top-human-to-median-researcher gap |
| TED-AI (AGI proxy) | At least as good as top human experts at virtually all cognitive tasks; Daniel median: Dec 2030; Eli median: Jan 2035 |
| ASI | ASI-to-best-human gap is 2x the best-human-to-median-professional gap |

### 2) Takeoff-Speed Distribution Predictions

| Claim | Daniel | Eli |
|---|---|---|
| P(AC -> ASI < 1 year) | ~37% | 30% |
| P(AC -> ASI < 3 years) | - | 60% |
| P(AC -> ASI < 10 years) | ~72% | 83% |
| P(AC by end of 2026) | ~9% | ~6% |
| P(no AGI by 2050) | ~6% | ~7.5% (implied) |

### 3) Quantitative Predictions and Scoring Targets

#### Benchmark and capability targets

- SWE-bench Verified: 85% by mid-2025.
- OSWorld-Verified: 0.65 by mid-2025.
- METR coding time horizon (80%): central trajectory tracked as a key pace indicator (including corrected-vs-erroneous trajectory comparison in grading).
- METR-HRS doubling-time assumption: about every 4.5 months.
- RE-Bench saturation threshold: score >= 1.5; median around 2026 (Eli/FutureSearch 80% CI: Sep 2025 to Jan 2031).

#### AI R&D uplift and automation targets

- AI software R&D uplift (internal/OpenBrain track): scored at end-2025.
- AI software R&D uplift (public track): scored at end-2025.
- AI R&D software uplift at RE-Bench saturation: 5% to 60% faster than 2024 pace.
- SC-equivalent R&D multiplier: 5.5x (Nikola) to 8.5x (Eli) faster than 2024 pace.

#### Economic targets

- Frontier AI company annualized revenue: about $20B in 2025; growth around 4.1x/year.
- OpenAI valuation target: $500B in 2025 (noted as June 2025 in one framing).
- Revenue reaching $100T annualized by end of 2031.

#### Compute and infrastructure targets

- Training compute: 1000x GPT-4 scale available by 2027.
- Compute supply growth: about 2.25x/year; from 10M to 100M H100-equivalents by end of 2027.
- Largest training run FLOPs by end-2025 (grading metric).
- China leading-company compute budget by end-2025 (grading metric).
- Global AI datacenter spend by end-2025 (grading metric).
- Global H100-equivalents available by end-2025 (grading metric).
- Leading AI company compute budget (FLOPs/month) by end-2025 (grading metric).
- Leading AI company datacenter capacity (GW) by end-2025 (grading metric).
- Leading AI company datacenter capex by end-2025 (grading metric).

#### Public salience target

- Percent of Americans citing AI as the most important problem: 1% target by late-2025.

### 4) Qualitative Scenario Predictions

- PhD-level knowledge in every field by end-2025.
- Five distinct "Agent" generations (Agent-1 through Agent-5) during 2025 to 2027.
- Neuralese recurrence enabling self-improving architectures in 2026 to 2027.
- Synthetic data solving non-STEM domains in 2026.
- AI developing personality and drives via instruction tuning in 2026.
- 100,000 robots/month from converted car factories in 2027.
- US-China AI conflict dynamics escalating in 2026 to 2027.
- Computer-using agents marketed as personal assistants.
- Broad adoption dynamics (including possible struggle for widespread usage).
- Specialized coding/research agents transforming workflows.
- Reliability and cost profile of agent systems as a tracked prediction theme.
- Top-lab race intensity and relative closeness as a tracked prediction theme.
- "Finishes training" becoming less meaningful due to frequent updates.
- Hacking-assistance and bio-risk assistance capability trends.

## Original AI 2027 Primary Resources

- AI Futures Model: Dec 2025 Update  
  `https://blog.ai-futures.org/p/ai-futures-model-dec-2025-update`
- Grading Spreadsheet  
  `https://docs.google.com/spreadsheets/d/1Ncol1SYIeLhGKdOUHKSYPxCTjkUwQVxkIbp393hveyA/edit?gid=145629229`
- AI 2027 Timelines Forecast  
  `https://ai-2027.com/research/timelines-forecast`
- AI Futures Model forecast snapshot (Daniel, Jan 26, 2026)  
  `https://www.aifuturesmodel.com/forecast/daniel-01-26-26`

## 2026 Independent Reality Check (as of February 13, 2026)

This section uses the prediction set above as baseline, then checks confirming/disconfirming evidence from public benchmark data, earnings reports, and surveys.

### Stage 1: Descriptive (what we observe on the ground)

| Area | Prediction Baseline | Observed Reality (dated) | Status vs Schedule | Evidence |
|---|---|---|---|---|
| SWE-bench Verified | 85% by mid-2025 | Official leaderboard top: 78.8% (TRAE + Doubao-Seed-Code, Sep 28, 2025) | **Behind** | E2 |
| OSWorld-Verified | 0.65 by mid-2025 | OSWorld/aggregated benchmark data reaches 66.3% (Nov 25, 2025), 63.3% in latest listed Feb 3, 2026 run | **Slightly behind at target date; near/on target by late-2025** | E2 |
| METR coding horizon pace | Doubling ~every 4.5 months | METR v1.1 reports 128-day doubling (~4.2 months from 2023 onward); p80 horizon rose from 9.79 min (Claude 3.7, Feb 24, 2025) to 55.13 min (GPT-5.2, Dec 11, 2025) | **On track / slightly ahead** | E2 |
| RE-Bench-style R&D automation expectations | Saturation around 2026 with major uplift | RE-Bench reports AI agents above humans at 2-hour budgets, but humans overtake at 8-hour budgets and are ~2x top-agent performance at 32 hours; Jan 2025 update places Claude 3.5/o1 at ~37th/~30th percentile of 8-hour human experts; Apr 2025 Claude 3.7 reaches about median 8-hour human performance only with a 32-hour budget on a 5-task subset | **Behind for near-term saturation; improving but unresolved** | E2 |
| “PhD-level in every field” by end-2025 | Broad frontier competence | FrontierMath core best 40.7%; FrontierMath Tier 4 best 31.3%; GPQA best 92.6% (strong but uneven) | **Behind on “every field”** | E2 |
| AI software R&D productivity uplift | Strong near-term uplift | Randomized controlled trial with experienced OSS developers found AI tools *reduced* completion speed by ~19% in that setting | **Disconfirming for broad near-term uplift claims** | E2 |
| Frontier AI company revenue | ~$20B annualized in 2025 | Reuters reported OpenAI at ~$10B annualized (Jun 2025) and ~$12B annualized (Jul 2025); later $20B+ claims exist but are less directly auditable | **Mixed (trajectory up, target timing uncertain)** | E4 |
| OpenAI valuation | $500B by June 2025 framing | OpenAI reached ~$500B valuation in Oct 2025 fundraising reports | **Slightly behind timing (~4 months)** | E4 |
| Compute/datacenter growth | 2.25x/year style growth, heavy capex | Alphabet capex: $52.5B (2025), expects ~$75B (2026); Meta capex: $39.2B (2025), guides $60B-$65B (2026); Microsoft additions to property/equipment: $64.6B (FY2025); Amazon purchases of property/equipment: $83B (2025), with 2026 run-rate expected around the higher Q4 annualized pace | **Ahead / strongly on track** | E2-E3 |
| Public salience (% naming AI as most important problem) | 1% by late-2025 | Gallup MIP table shows “Advancement of computers/technology” at 1% in Dec 2025; Gallup does not publish a separate AI-only row in this table | **Proxy meets threshold; AI-specific resolution remains uncertain** | E2-E3 |
| Agent adoption dynamics | Personal assistants emerge; broad adoption uncertain | Stack Overflow 2025: 84% use/plan AI tools and 51% of professional developers use AI tools daily; but 52% do not use agents or only use simpler tools, and 38% have no plans to adopt agents | **Tools ahead; autonomous-agent adoption behind** | E2-E3 |

### Stage 2: Evaluative (does this confirm or disconfirm the schedule?)

#### Net verdict

- Relative to the **original fast AI 2027 narrative**, current evidence says we are **behind schedule overall**.
- Relative to the **updated Dec 2025 “slower” AI Futures medians**, we look **closer to on-track**, with continued uncertainty concentrated in R&D automation and agent reliability.

#### Why the “behind” conclusion holds for the original schedule

- Milestone-level capability thresholds (SWE-bench 85 by mid-2025, broad “PhD-level in every field”) were not met on time.
- Real-world autonomous-agent penetration in professional workflows remains partial, with high usage of AI tools but lower trust and lower agent autonomy.
- Independent causal evidence for strong AI R&D uplift is mixed-to-negative in rigorous settings (METR RCT evidence plus RE-Bench long-horizon human advantage), which weakens the “coding -> rapid full AI R&D automation” link on original timing.

#### Why this is not a simple “everything is behind”

- Input-side drivers (compute buildout, capex, model horizon growth) are very strong and in some cases faster than baseline assumptions.
- Some narrow benchmarks are accelerating quickly (e.g., GPQA, ARC-AGI, METR horizons), leaving room for future catch-up if reliability and organizational integration improve.

### Stage 3: Dialectical (best steelman vs strongest counterargument)

#### Steelman for “ahead”

- Infrastructure and spending are scaling at extreme levels, reducing risk of compute bottlenecks.
- Measured capability trends on selected benchmarks remain steep.
- Economic pull is real and sustained, which can accelerate deployment and iteration cycles.

#### Steelman for “behind”

- The difficult part is not raw benchmark score; it is robust long-horizon autonomy, error recovery, and research taste.
- Cross-domain generalization remains uneven (strong on some tests, still weak on hardest open-ended tasks).
- Observed productivity gains in realistic software settings are not consistently matching optimistic narrative claims.

#### Synthesis

- **Inputs are ahead. Outputs are mixed. Full-stack autonomy is behind.**
- Best estimate: the world in early 2026 looks roughly like a **60%-75% pace realization** of the original AI 2027 timeline, based on independently checked benchmarks, adoption, productivity, and infrastructure indicators in this section.

## Conclusion: Pace and Schedule (Independent)

### Pace Scorecard (as of February 13, 2026)

Scoring rule: `1.0x = on the original AI 2027 pace`, `>1.0x = ahead`, `<1.0x = behind`.

| Dimension | Weight | Pace Score | Rationale |
|---|---:|---:|---|
| Capability benchmarks (SWE-bench, OSWorld, METR, FrontierMath) | 30% | 0.80x | Mixed: METR/OSWorld trend strength vs missed SWE-bench and broad “PhD-level in every field” overreach |
| R&D automation and real productivity (RE-Bench + METR RCT) | 35% | 0.50x | Core bottleneck: long-horizon human advantage on RE-Bench and negative RCT signal for realistic expert coding tasks |
| Adoption and deployment quality (agent usage in workflows) | 15% | 0.70x | AI tool usage is broad, but high-autonomy agent usage remains partial |
| Compute and infrastructure | 10% | 1.15x | Capex and datacenter expansion are clearly strong and generally ahead of bottleneck-risk expectations |
| Economics and public salience | 10% | 0.70x | Revenue trajectory positive, valuation timing slipped vs aggressive framing, and AI-specific salience measure remains only partially resolved |
| **Weighted total** | **100%** | **0.70x** | **Behind original schedule overall** |

Sensitivity band (based on unresolved salience definition, private-company revenue uncertainty, and RE-Bench setup comparability): **~0.62x to 0.78x**.

### Schedule Verdict

- **Relative to the original fast AI 2027 narrative:** **Behind schedule** (central estimate: **0.70x pace**).
- **Relative to the Dec 31, 2025 updated AI Futures medians (later timeline):** **Roughly on track to slightly behind**, with the decisive uncertainty concentrated in whether R&D automation closes the long-horizon reliability/taste gap.

### Bottom Line

- The world in early 2026 is best described as: **compute-and-capital ahead, benchmark progress mixed, autonomy/productivity behind**.
- Practical implication: the strongest independent evidence still points to **slower-than-original takeoff pacing**, unless 2026 brings a step-change in reliable long-horizon agentic R&D performance.

## Extracted Claims (Rigor Contract v1)

| ID | Claim | Type | Layer | Actor | Scope | Quantifier | Evidence Level | Credence | Assessment |
|---|---|---|---|---|---|---|---|---|---|
| rc-2026-01 | Top SWE-bench Verified result is below the 85% mid-2025 target. | [F] | Capability | Frontier agent systems | Verified software issue resolution | 78.8% vs 85% target | E2 | 0.90 | Disconfirming |
| rc-2026-02 | OSWorld-Verified reached target-level performance by late 2025, but not clearly by mid-2025. | [F] | Capability | Frontier UI/computer-use agents | Desktop task completion | 66.3% (Nov 2025), target 65% mid-2025 | E2 | 0.75 | Mixed |
| rc-2026-03 | METR task-horizon growth is near or faster than assumed trend pace. | [F] | Capability trend | Frontier LLMs | Longer coding tasks | 128-day doubling; p80 9.79 -> 55.13 min (Feb-Dec 2025) | E2 | 0.85 | Confirming |
| rc-2026-04 | “PhD-level in every field by end-2025” is not supported by hardest public math benchmarks. | [F] | General capability | Frontier models | Cross-domain expert reasoning | FrontierMath core 40.7%, Tier-4 31.3% | E2 | 0.85 | Disconfirming |
| rc-2026-05 | Strong near-term AI coding productivity uplift is not robustly established in realistic expert settings. | [F] | Productivity | Professional developers using AI tools | OSS task execution | ~19% slower in METR RCT setting | E2 | 0.80 | Disconfirming |
| rc-2026-06 | AI tool usage is broad, but autonomous-agent usage is not yet mainstream. | [F] | Adoption | Developers | Workflows with/without agents | 84% use/plan AI tools; 52% non-agent/light-agent usage | E2-E3 | 0.85 | Mixed |
| rc-2026-07 | Compute infrastructure investment is scaling aggressively enough to support continued frontier growth. | [F] | Infrastructure | Big tech hyperscalers | Datacenter/capex capacity | Alphabet 52.5B capex (2025), Meta 39.2B capex (2025), Microsoft 64.6B P&E additions (FY2025), Amazon 83B P&E purchases (2025); higher 2026 guides | E2-E3 | 0.85 | Confirming |
| rc-2026-08 | OpenAI valuation hit the ~$500B level later than the most aggressive timing framing. | [F] | Economics | OpenAI + investors | Private-market valuation | ~$500B in Oct 2025 vs June framing | E4 | 0.80 | Slightly disconfirming |
| rc-2026-09 | RE-Bench evidence does not support near-term saturation-level AI R&D automation. | [F] | R&D capability | Frontier model agents vs human experts | AI research-engineering tasks under fixed budgets | AI > humans at 2h, humans > AI at 8h, humans ~2x AI at 32h; updates place top agents around 30th-37th percentile vs 8h human experts | E2 | 0.87 | Disconfirming |
| rc-2026-10 | Public-salience target is only partially resolvable with independent evidence: Gallup’s technology category reached 1% in Dec 2025, but AI-specific share is not separately published. | [F] | Public salience | U.S. adults (Gallup respondents) | “Most important problem” mentions | 1% for “Advancement of computers/technology” (Dec 2025) | E2-E3 | 0.70 | Mixed / unresolved |
| rc-2026-11 | A weighted synthesis of independently checked dimensions implies overall pace below the original AI 2027 schedule. | [T] | Synthesis | AI timeline forecast vs observed indicators | Cross-domain pace realization | Central 0.70x pace, sensitivity band 0.62x-0.78x | E3 | 0.72 | Disconfirming |

## Corrections & Updates (Audit Log)

- **Recency check:** all external datapoints above were re-checked on **February 13, 2026**.
- **Independence rule:** the author self-grading post ("Grading AI 2027's 2025 Predictions") is explicitly excluded from the independent check and cannot be used as independent evidence.
- **Metric mismatch noted:** SWE-bench values differ by evaluation setup. Official leaderboard top (78.8%) is higher than stricter model-run slices in some aggregate datasets (e.g., Epoch’s 64.8% series). The official benchmark leaderboard is used for target comparison.
- **OSWorld caution:** OSWorld-Verified includes variants by step budget and run setup; exact comparability across rows is imperfect.
- **RE-Bench caution:** 2025-2026 RE-Bench updates are not perfectly apples-to-apples (e.g., Claude 3.7 result is on a 5-task subset with score-feedback structure); directionally they still show a persistent long-horizon human advantage.
- **Public-salience caveat:** Gallup publishes a technology-category row ("Advancement of computers/technology"), not an AI-only row, so direct resolution of the AI-specific 1% target remains partially unresolved.
- **Compute data update:** capex figures were corrected to primary company releases/filings where possible; earlier transcript-derived values were replaced.
- **Pace-score caveat:** the weighted pace score is an explicit judgment model for synthesis, not a directly observed metric.
- **Economic data caution:** OpenAI is private; revenue and valuation values rely on credible reporting rather than SEC filings.

## External Evidence Sources

- AI Futures model update (Dec 31, 2025):  
  `https://blog.ai-futures.org/p/ai-futures-model-dec-2025-update`
- SWE-bench official leaderboard:  
  `https://www.swebench.com/`
- METR time-horizon public results (v1.1 YAML):  
  `https://metr.org/assets/benchmark_results_1_1.yaml`
- METR time-horizons project page:  
  `https://metr.org/time-horizons/`
- METR RE-Bench release + paper + follow-up evaluations:  
  `https://metr.org/blog/2024-11-22-evaluating-r-d-capabilities-of-llms/`  
  `https://metr.org/AI_R_D_Evaluation_Report.pdf`  
  `https://metr.org/blog/2025-01-31-update-sonnet-o1-evals/`  
  `https://evaluations.metr.org/claude-3-7-report/`
- METR randomized trial paper (arXiv:2507.09089):  
  `https://arxiv.org/abs/2507.09089`
- Epoch benchmark hub (FrontierMath, GPQA, SWE-bench series, etc.):  
  `https://epoch.ai/benchmarks/frontiermath`
- Epoch benchmark dataset files:  
  `https://epoch.ai/data/benchmarks.csv`  
  `https://epoch.ai/data/generated/external_benchmarks/os_world.csv`
- Alphabet Q4 2025 earnings release (capex + 2026 expectation):  
  `https://abc.xyz/assets/investor/static/pdf/2025Q4_alphabet_earnings_release.pdf`
- Meta Q4/FY 2025 earnings release (capex and guidance):  
  `https://investor.atmeta.com/investor-news/press-release-details/2026/Meta-Reports-Fourth-Quarter-and-Full-Year-2025-Results/default.aspx`
- Amazon Q4/FY 2025 release (P&E purchases and 2026 capex run-rate commentary):  
  `https://ir.aboutamazon.com/news-release/news-release-details/2026/Amazon-com-Announces-Fourth-Quarter-Results/default.aspx`
- Microsoft FY2025 annual report (P&E additions, datacenter lease commitments):  
  `https://www.microsoft.com/investor/reports/ar25/index.html`
- Reuters coverage of OpenAI revenue milestones:  
  `https://www.reuters.com/world/china/openai-surpasses-10-billion-annualized-revenue-run-rate-information-reports-2025-06-09/`  
  `https://www.reuters.com/business/openai-reaches-12-billion-annual-revenue-run-rate-information-reports-2025-07-30/`
- OpenAI valuation reporting (~$500B):  
  `https://www.reuters.com/world/china/openai-seeks-fundraising-valuation-up-500-billion-information-reports-2025-10-11/`
- Gallup U.S. "Most Important Problem" trend + embedded data table:  
  `https://news.gallup.com/poll/1675/most-important-problem.aspx`  
  `https://datawrapper.dwcdn.net/vEKjO/86/dataset.csv`
- Stack Overflow Developer Survey 2025 AI chapter:  
  `https://survey.stackoverflow.co/2025/ai`
