https://claude.ai/chat/029258de-9666-4ee6-96eb-9c93462251be

# AI 2027 / AI Futures Model: Independent Verification and Critical Analysis

The AI Futures Model's December 2025 update represents a significant **3–5 year retreat** from the original AI 2027 timeline, driven primarily by modeling error corrections rather than new empirical evidence. Daniel Kokotajlo's TED-AI median now sits at December 2030; Eli Lifland's at January 2035. The team's own self-grading finds quantitative progress running at **~65% of their original predicted pace**, with coding capability benchmarks and R&D uplift estimates consistently behind. The forecasters have genuine track records — Lifland is #1 all-time on RAND's INFER platform, and Kokotajlo's 2021 predictions were remarkably prescient — but the model's 33-parameter structure, heavy reliance on METR-HRS extrapolation, and sensitivity to curve-fitting assumptions leave the fast-takeoff scenario poorly constrained. Independent comparison suggests their updated medians now roughly align with the aggressive end of the broader forecasting community (Metaculus full AGI: 2033, Epoch GATE: 2034, Davidson updated: ~2030), while their original 2027 timeline was an outlier that even their own corrected model no longer supports.

---

## Deliverable 1: Prediction criteria for independent verification

The AI 2027 scenario and AI Futures Model contain dozens of specific, evaluable claims. Below is a structured extraction organized by category, designed for external gap analysis. Each criterion includes the original claim, the metric or operationalization, and the claimed timeline.

### Milestone definitions (the model's causal chain)

The model's core architecture depends on six sequential milestones. Each is independently evaluable:

1. **Automated Coder (AC):** Full automation of an AGI project's coding work, replacing the project's entire coding staff. Operationalized as: if dropped into the present, the system would be as productive on its own as only-human coders. Uses ≤5% of compute supply. *Daniel median: Dec 2029. Eli median: Mar 2032.*

2. **Superhuman Coder (SC):** AI system where, using 5% of compute budget, a company could run **30× as many agents** as they have human research engineers, each accomplishing coding tasks at **30× the speed** of the company's best engineer, across any human researcher's area of expertise. *Original AI 2027 scenario: March 2027. Updated Eli ATC median: ~2030.*

3. **Superhuman AI Researcher (SAR):** Research taste matching the top human researcher. Fully automates AI R&D, making all human researchers obsolete. Uses 1% of compute for taste, 5% for coding. *No single median given; follows AC by months to years depending on takeoff speed.*

4. **Superintelligent AI Researcher (SIAR):** Gap between SIAR and top human is 2× the gap between top human and median researcher.

5. **Top-human-Expert-Dominating AI (TED-AI):** At least as good as top human experts at virtually all cognitive tasks. Used as their AGI proxy. *Daniel median: Dec 2030. Eli median: Jan 2035.*

6. **Artificial Superintelligence (ASI):** Gap between ASI and best humans is 2× the gap between best humans and median professional, at virtually all cognitive tasks.

### Quantitative benchmark predictions (evaluable against public data)

| Criterion | AI 2027 Claim | Timeline | Evaluable Metric |
|-----------|--------------|----------|-----------------|
| SWE-bench Verified score | 85% | Mid-2025 | Public leaderboard. Actual best: 74.5% (Opus 4.1). **Behind pace.** |
| METR-HRS 80th-percentile time horizon | Doubling every ~4.5 months | Ongoing | METR public reports. Starting point: 15 min (Claude 3.7 Sonnet). Claude Opus 4.5 reached ~289 min. |
| RE-Bench saturation (score ≥1.5) | Saturated by AI agents | Median ~2026 (Eli/FutureSearch 80% CI: Sep 2025–Jan 2031) | RE-Bench public results. Current best: ~0.6 with Best-of-K scaffolding for Claude 3.7. AI agents 4× human experts at 2hr tasks. |
| Time horizons required for SC | 10 years of HCAST-equivalent (Eli), 1.5 months (Nikola) | — | Divergence between forecasters is itself a key uncertainty |
| Frontier AI revenue | ~$20B annualized, growing ~4.1×/year | 2025 | OpenAI hit ~$30.4B annualized (4.8× growth). **Ahead of pace.** |
| Revenue reaching $100T annualized | End of 2031 | 2031 | Extrapolation from current trajectory |
| OpenAI valuation $500B | June 2025 | 2025 | Achieved October 2025. **~4 months behind.** |
| Training compute 1000× GPT-4 | Available | By 2027 | Epoch data: 30+ models above 10²⁵ FLOP; Grok-3 at 10²⁶. On track. |
| AI R&D software uplift at RE-Bench saturation | 5–60% faster than 2024 pace | At RE-Bench saturation | Anthropic claims >100% productivity improvements; METR uplift study found systematic overestimation. |
| SC-equivalent R&D progress multiplier | 8.5× (Eli), 5.5× (Nikola) faster than 2024 | At SC arrival | Not yet evaluable |
| Compute supply growth | 2.25×/year, 10M→100M H100-equivalents by EOY 2027 | 2025–2027 | Epoch data: NVIDIA GPU power growing ~2.3×/year. Hyperscaler capex $600B+ in 2026. Roughly on track. |

### Structural model parameters (evaluable indirectly)

These are the internal parameters most critical to the model's outputs:

- **METR-HRS doubling time:** 4.5 months [2.5, 9] as of March 2025. Superexponential weight: 45% (Eli). Subexponential: 10%.
- **Superexponential acceleration parameter α:** Each doubling takes 10% less time. Titotal's critique showed this single parameter, set without uncertainty analysis, drives divergent outcomes.
- **Cost/speed adjustment to 30× faster+cheaper:** 4 months [0.5, 30] of additional progress beyond raw capability.
- **Diminishing returns to software research:** The original AI 2027 model implicitly assumed *zero* diminishing returns — acknowledged as an error. The Dec 2025 model incorporates semi-endogenous growth.
- **Taste-Only Singularity parameter *b*:** Ratio of successive AI R&D uplift doublings. b<1 = accelerating intelligence explosion; b>1 = decelerating. Model median: b≈1.2 (no singularity). **38% of simulations** have b<1. **17%** have b<0.7 (consistent with original AI 2027 scenario).
- **Pre-AC AI R&D automation interpolation:** Original model had a bug overestimating intermediate speedups by ~9 months. Fixed in Dec 2025.

### Qualitative scenario predictions (from the AI 2027 narrative)

| Prediction | Timeline | Evaluability |
|-----------|----------|-------------|
| PhD-level knowledge in every field | End 2025 | Partially met: GPQA Diamond ~92%, but HLE only 37.5%, FrontierMath T4 only 12% |
| Five distinct "Agent" generations (Agent-1 through Agent-5) | 2025–2027 | Agent-1 (copilots) exists; Agent-2 (autonomous coding) emerging; Agent-3+ speculative |
| Neuralese recurrence enabling self-improving architectures | 2026–2027 | No public evidence of this technique working at scale |
| Synthetic data solving non-STEM domains | 2026 | Works for math/code; no breakthrough for open-ended domains |
| AI developing personality and drives via instruction tuning | 2026 | No credible evidence of genuine drives/personality emerging |
| 100,000 robots/month from converted car factories | 2027 | No movement toward this |
| US-China AI conflict dynamics | 2026–2027 | Chip export controls escalating; geopolitical tension real but scenario specifics untestable |

### Takeoff speed predictions (key distributional claims)

| Claim | Daniel | Eli |
|-------|--------|-----|
| P(AC→ASI < 1 year) | ~37% (model) | 30% (ATC) |
| P(AC→ASI < 3 years) | — | 60% (ATC) |
| P(AC→ASI < 10 years) | ~72% (model) | 83% (ATC) |
| P(AC by EOY 2026) | ~9% | ~6% |
| P(no AGI by 2050) | ~6% | implicit ~7.5% (from p90 at 2085) |

---

## Deliverable 2: Critical analysis of their December 2025 self-review

### The methodology is more rigorous than typical AI forecasting, but structurally biased toward self-validation

The December 2025 update deserves credit for several things most forecasting efforts never do: acknowledging and fixing a coding bug, naming specific implicit assumptions that were wrong, publishing updated distributions, and maintaining a public self-grading record. The team's quantitative framework — Monte Carlo simulation across 33 parameters with explicit uncertainty ranges — is substantially more rigorous than the modal AI timeline forecast, which is typically a vibes-based blog post.

That said, the self-review methodology has significant structural issues:

**Asymmetric framing of hits and misses.** The "~65% of predicted pace" framing is doing heavy rhetorical lifting. The team frames this as "most qualitative predictions on track" while acknowledging quantitative metrics are behind. But the quantitative metrics *are* the model — the qualitative scenario was explicitly described as illustrative. When SWE-bench Verified hits 74.5% instead of 85%, the gap matters precisely because the model's causal chain (coding automation → R&D acceleration → intelligence explosion) depends on these thresholds being crossed on schedule. A 65% pace rate, sustained, means arrival is roughly **1.5× later** than predicted — which is directionally consistent with their 3–5 year shift but gets buried under qualitative "on track" language.

**The bug disclosure is commendable but raises deeper questions.** The original AI 2027 model had (a) a coding bug in intermediate R&D speedup interpolation (~9 months too fast), (b) an implicit assumption of zero diminishing returns to software research (~2 years too fast), and (c) overly optimistic interpolation of pre-SC speedups. Together, these accounted for the majority of the 3–5 year shift. The uncomfortable implication: **the viral AI 2027 scenario was built on a model that contained known-category modeling errors that all pushed in the same direction (faster timelines)**. The team frames this as normal scientific self-correction. Critics like Titotal had identified the fragility months earlier. The question of whether the remaining model is free of similar directional errors is unresolved.

**Selective evidence standards across domains.** The team applies rigorous quantitative standards to benchmark tracking (SWE-bench scores, METR time horizons, revenue figures) but relies on much weaker evidence for several critical parameters. The taste-only singularity parameter *b*, which determines whether an intelligence explosion accelerates or fizzles, is described as an "intuitive guess." The mapping from AI R&D capability to general cognitive capability (AC→TED-AI) is acknowledged as "very rough." The team's honest uncertainty language ("we are uncertain and don't blindly trust our models") coexists with the model's structural assumption that a specific causal chain (coding → research → explosion) is the right frame — an assumption that isn't itself subjected to uncertainty analysis.

**Handling of unresolved predictions favors the model.** Most of the model's critical predictions (AC, SAR, intelligence explosion) haven't resolved and won't for years. The self-review evaluates early-stage proxies (benchmark scores, revenue, time horizons) that are largely consistent with the model's *direction* even if behind on *pace*. This creates a structural bias: the review can always point to "progress in the right direction" as partial confirmation while deferring judgment on the hard questions (will progress actually reach the critical thresholds? will the causal chain from coding to research to explosion actually hold?). The unresolvable-in-2025 predictions happen to be the ones that carry the most weight.

**The "modeling improvements > new evidence" admission is more damning than presented.** The team states that the 3–5 year shift came primarily from "improving our modeling of AI R&D automation" rather than new empirical evidence. They present this neutrally, but it means: the original model's headline-grabbing 2027 timeline was primarily the artifact of modeling choices (bugs, assumptions), not a robust empirical extrapolation. If fixing known errors produces a 3–5 year shift, the remaining unknown errors could produce shifts of similar or larger magnitude in either direction. The team acknowledges this conceptually ("we don't think this model should be trusted completely") but the model continues to be the primary basis for their forecasts.

**Revenue tracking is selectively favorable.** OpenAI's revenue ($30.4B annualized, 4.8× growth) outpaced the model's projection. The team highlights this. But revenue growth and capability growth are different things. Much of AI revenue growth comes from enterprise adoption of existing capabilities, not from the capability frontier advancing. The gap between "AI companies are making money" and "AI is automating AI research" is significant, and the self-review doesn't adequately separate these.

### Calibration comparison with community

The team's updated medians (Daniel: 2030, Eli: 2035) now bracket the broader forecasting community. Metaculus community median for full AGI is ~2033. Epoch's GATE model gives ~2034. Davidson's updated model gives ~2030. This convergence suggests the December update corrected toward community consensus, which could reflect either genuine self-correction or (less charitably) regression to the mean after an attention-grabbing outlier prediction.

---

## Deliverable 3: Independent assessment of the forecast

### Where the model appears well-calibrated

**Compute buildout trajectory.** The AI Futures Model's compute scaling assumptions are holding up well. Hyperscaler capex exceeded $400B in 2025 and is projected above $600B in 2026. Training compute continues growing ~5×/year. Over 30 models have exceeded 10²⁵ FLOP, with Grok-3 crossing 10²⁶. The Stargate Project ($500B multi-year plan) and OpenAI's datacenter ambitions suggest the compute won't be the binding constraint through 2028 at minimum.

**Coding capability improvement rate.** SWE-bench Verified went from 33% (Aug 2024) to ~65–81% (late 2025) — roughly doubling in 16 months. METR time horizons show Claude Opus 4.5 handling ~289-minute equivalent tasks, up from ~15 minutes for Claude 3.7 Sonnet. Stack Overflow's 2025 survey shows **65% of developers using AI coding tools weekly**. Stanford data indicates a **~20% employment decline** among 22–25-year-old software developers between 2022 and 2025. The direction is clearly right; the question is whether the rate is fast enough for AC by 2029–2032.

**Revenue/commercial trajectory.** OpenAI's 4.8× annual revenue growth actually *outpaced* the model's 4.1×/year assumption. At $30.4B annualized and growing, the "AI is economically transformative" claim has strong empirical support, though revenue growth can decouple from capability-frontier advancement.

### Where the model appears miscalibrated or vulnerable

**The superexponential assumption remains poorly constrained.** The model assigns ~45% weight to superexponential time-horizon growth (each doubling taking 10% less time than the previous one). Titotal's critique demonstrated that two equally-well-fitting superexponential curves to the same METR data produce wildly divergent extrapolations — one reaching infinite time horizons by 2030, another taking decades. With only a handful of data points in the "RL era" (late 2024 onward), the case for superexponential over merely exponential growth rests on thin evidence. The doubling-time parameter α was set without formal uncertainty analysis. This is the single biggest source of fragility in the model.

**The R&D automation multiplier is the model's crux, and evidence is mixed.** The claim that automated coders will produce a **5.5–8.5× R&D progress multiplier** is essential to the fast-takeoff scenario. Current evidence is ambiguous. RE-Bench shows AI agents outperform human experts at 2-hour ML tasks by 4×, but humans still dominate at 8-hour horizons. AlphaEvolve's contribution to Gemini training was a **1% efficiency gain** — real but modest. The Anthropic internal claim of ">100% productivity improvement" from AI tools is contradicted by METR's finding that people systematically overestimate AI uplift. Steve Newman's Amdahl's Law critique applies directly: even one unmovable bottleneck in the R&D pipeline (experimental verification, hardware iteration, conceptual breakthroughs requiring novel insight) could cap the multiplier far below predicted levels.

**Pre-training scaling dynamics shifted since publication.** The AI 2027 scenario implicitly assumed continued exponential capability gains from scaling pre-training compute. By late 2025, the picture changed. GPT-5's August 2025 release was widely described as "disappointing" relative to expectations. Ilya Sutskever stated "the age of scaling is ending." The industry pivoted toward post-training RL, inference-time compute scaling, and refinement loops. This doesn't mean capability growth has stopped — it clearly hasn't — but it changes the character of the growth curve in ways the model doesn't capture. **Test-time compute scaling and RL-based post-training are producing gains, but through a different mechanism than the model assumed**, and these methods face their own diminishing-returns dynamics.

**The "PhD-level knowledge" prediction illustrates systematic overconfidence on general capabilities.** GPQA Diamond scores (92%+) look impressive, but Humanity's Last Exam sits at 37.5%, FrontierMath Tier 4 at 12%, and ARC-AGI-2 at ~53%. As Ernie Davis noted, current models "make mistakes that even humans entirely ignorant of the field could avoid." The model systematically underweights the gap between benchmark performance and genuine domain expertise — a gap that matters enormously for the R&D automation thesis. Gleech.org's end-of-2025 assessment captures it well: "AI is much more impressive but not proportionally more useful. Models improved on things they were explicitly optimised for (coding, vision, OCR, benchmarks) and did not hugely improve on everything else."

**The agent reliability gap is underweighted.** Current AI agents excel at well-scoped tasks with clear feedback signals but struggle with multi-day autonomous operation, ambiguous requirements, and error recovery. More than half of developers aren't using the latest coding agents. Anthropic's own 2026 agentic coding report projects agents working for "days autonomously" as a 2026 goal, not a 2025 achievement. The model's causal chain from AC to SAR assumes agents can operate autonomously on research-scale tasks — a qualitative capability threshold that benchmark scores don't directly measure.

### How this compares with the broader forecasting landscape

The updated AI Futures Model now sits at the **aggressive but no longer outlier** end of the forecasting distribution:

| Source | AGI/TED-AI Median | Notes |
|--------|-------------------|-------|
| Daniel Kokotajlo (Jan 2026) | Dec 2030 | Shifted from ~2027–2028 |
| Eli Lifland (Jan 2026) | Jan 2035 | Conservative end of team |
| Metaculus (general AI announced) | Nov 2027 | Definitionally weaker than full AGI |
| Metaculus (full AGI w/ robotics) | ~2033 | Lengthened slightly in past year |
| Epoch GATE model | ~2034 | With median parameters |
| Davidson model (updated) | ~2030 | With observed compute/algorithmic rates |
| Bio Anchors (retrospective) | ~2030 | When recalculated with actual algorithmic progress (200%/yr vs. assumed 30%/yr) |
| Polymarket (OpenAI AGI before 2027) | ~15% Yes | Market-implied probability |
| METR simplified model (8 params) | Late 2032 | >99% AI R&D automation |
| Goodheart Labs dashboard | 2031 | 80% CI: 2027–2045 |

The convergence around **2030–2035** across diverse methodologies (extrapolation, economic modeling, benchmarking, prediction markets) is notable. It suggests this range is where the evidence actually points. The original 2027 timeline was a genuine outlier, and its correction toward consensus should update us toward viewing the team's current medians as reasonable but still on the fast side.

### Critical blind spots in the model

**No modeling of discontinuous obstacles.** MIRI's critique is sharp: the scenario is "unrealistically smooth." If there's a 30% chance each of a stock market crash, Taiwan conflict, and public unrest, each is less-likely-than-not individually, but it's more-likely-than-not that at least one occurs, causing cascading delays. The model has no mechanism for such shocks.

**Vitalik Buterin's asymmetry problem.** The scenario assumes AI capabilities increase rapidly while everyone else's capabilities (economic, defensive, regulatory) remain static. This contradicts the scenario's own claim that cancer, aging, and mind uploading could arrive by 2029 — if AI is that transformative, defensive and adaptive capabilities improve too.

**No alternative pathway modeling.** Marcus's conjunction-fallacy critique has force. The model describes one specific causal chain (METR-HRS extrapolation → automated coding → R&D acceleration → intelligence explosion). It doesn't model alternative pathways: what if progress stalls on coding but accelerates on reasoning? What if a different architecture replaces transformers? What if regulatory intervention creates meaningful delays? The single-pathway structure means the model captures its own scenario's probability but not the full space of possible futures.

**The "research taste" bottleneck is hand-waved.** The gap between automated coding and automated research is bridged by the concept of "research taste" — the ability to generate good research ideas and evaluate their promise. The model parameterizes how quickly AI taste improves, but the underlying mechanism is entirely speculative. There's no benchmark for research taste, no empirical trend to extrapolate, and the parameter values are acknowledged as "intuitive guesses." This is arguably the single most important variable in the model, and it has the weakest empirical grounding.

### Net assessment

The AI Futures Model is the most sophisticated public model of AI takeoff dynamics. The forecasters behind it have genuine, documented skill. The December 2025 update shows admirable intellectual honesty in acknowledging errors and shifting predictions substantially. Their updated medians (2030–2035) are defensible given current evidence.

However, the model's fast-takeoff scenarios (AC→ASI in <1 year, given 26–37% probability) remain poorly constrained by evidence. The critical parameters — superexponential growth rate, R&D automation multiplier, research taste improvement rate — are the least empirically grounded. The model is better understood as a **structured way to think about the scenario space** than as a prediction machine. Its value lies in making assumptions explicit and debuggable, not in its point estimates.

For a frontier-lab CTO, the actionable takeaway: the **2028–2032 window for near-full coding automation** is supported by multiple independent lines of evidence and should be taken seriously for workforce planning and competitive strategy. The fast-takeoff intelligence explosion (months from coding automation to superintelligence) is within the plausible space but should be weighted at **15–30%**, not the implied ~40% that the model's median parameters suggest. The biggest near-term indicator to watch is METR-HRS progression through 2026: if time horizons reach multi-hour sustained autonomous operation by mid-2026, the aggressive end of the timeline becomes substantially more likely.
