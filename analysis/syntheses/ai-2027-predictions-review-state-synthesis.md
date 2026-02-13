# Synthesis Analysis: Reviewing the state of AI 2027 predictions (as of 2026-02-13)

> **Source IDs**: `aifutures-2025-ai-2027`, `aifutures-2025-ai-2027-timelines-forecast`, `aifutures-2025-ai-futures-model-dec-2025-update`, `aifuturesmodel-2026-forecast-daniel-01-26-26`, `aifutures-2026-grading-ai-2027-2025-predictions`, `aifutures-2026-ai-2027-2025-predictions-grading-sheet`, `marcus-2025-ai-2027-scenario-how-realistic`, `metr-2026-time-horizon-1-1`, `metr-2025-ai-experienced-os-dev-productivity`, `gpt-2026-02-13-ai-2027-review`, `claude-2026-02-13-ai-2027-review`, `independent-2026-02-13-ai-2027-review`
> **Analysis Date**: 2026-02-13
> **Analyst**: codex (gpt-5.2)
> **Rigor Level**: `[DRAFT]`
> **Type**: Cross-source synthesis

---

## The Question

What is the *current reviewing state* of the AI Futures Project’s AI 2027 predictions (especially their dated, falsifiable quantitative targets), what do the authors’ own audits say so far, and how should we interpret that audit in light of methodological issues and external critique?

---

## Primary Sources (This Synthesis)

| Source ID | Type | What it provides |
|---|---|---|
| `aifutures-2025-ai-2027` | REPORT | The original scenario + research pages and extracted claims (“what was predicted”) |
| `aifutures-2025-ai-2027-timelines-forecast` | REPORT | Original-ish quantitative backbone for SC timing; disclosed edits and a code bug |
| `aifutures-2025-ai-futures-model-dec-2025-update` | BLOG | The authors’ Dec 31, 2025 model update; key reason: +3–5 years to coding automation due mainly to modeling changes |
| `aifutures-2026-grading-ai-2027-2025-predictions` | BLOG | The authors’ Feb 12, 2026 self-grading (“how did 2025 predictions fare”) |
| `aifutures-2026-ai-2027-2025-predictions-grading-sheet` | DATA | Captured grading spreadsheet (CSV) enabling reproducible audit of row values + aggregates |
| `aifuturesmodel-2026-forecast-daniel-01-26-26` | KNOWLEDGE | Snapshot of ATC percentiles for AC and a changelog of bug fixes/forecast shifts |
| `metr-2026-time-horizon-1-1` | ARTICLE | Why METR time-horizon is informative but protocol/task-suite sensitive (matters for AI‑2027-style extrapolations) |
| `metr-2025-ai-experienced-os-dev-productivity` | BLOG/ARTICLE | Causal-ish evidence that “AI allowed” can slow experienced OSS devs despite perceived speedup (impacts the “uplift” bottleneck) |
| `marcus-2025-ai-2027-scenario-how-realistic` | BLOG | External critique: narrative/probability hygiene; “fiction vs science”; possible political backfire |
| `independent-2026-02-13-ai-2027-review` | REPORT | Internal independent scorecard emphasizing “inputs vs autonomy” and a ~0.70× pace estimate |
| `gpt-2026-02-13-ai-2027-review`, `claude-2026-02-13-ai-2027-review` | CONVO | Secondary LLM memos that surface replication questions and methodological objections (non-primary evidence) |

---

## High-Signal Evidence Anchors (What the authors’ review *numerically* says)

### 1) Their “capabilities indicators only” aggregate: **0.58–0.66× pace**
From the grading post and its spreadsheet:
- Category aggregation for **capabilities indicators only** is reported as **0.58** (mean-of-means) and **0.66** (median-of-medians). (`META-2026-122`, `META-2026-124`)
- They summarize this as “~65% pace.”

Interpretation: on their chosen “capability-ish” proxies (benchmarks, coding time horizon, R&D uplift, economic value proxies), progress is *slower than the AI 2027 scenario’s 2025 trajectory*, but not dramatically “stalled.”

### 2) Their “all categories” aggregate is slightly higher: **0.63–0.66× pace**
Including compute and public salience categories, the spreadsheet reports **0.63** (mean-of-means) and **0.66** (median-of-medians). (`META-2026-124`)

Interpretation: including compute (mostly on pace) pulls the mean up a bit.

### 3) Aggregating *individual rows* gives higher results: **0.75 mean / 0.84 median**
They report that aggregating individual rows yields **0.75** mean and **0.84** median, but they argue this is misleading because compute is 7/15 rows. (`META-2026-123`, `META-2026-124`)

Interpretation: the “pace” headline is *method-dependent*; any synthesis should treat the scalar multiplier as a summary statistic with wide error bars and normative weighting choices.

---

## What’s “On Pace” vs “Behind” in their scoring (row-level texture)

From the captured grading CSV:

### Benchmarks (mid‑2025): **mixed, leaning behind**
- OSWorld‑Verified pace **0.84×** (pred 0.65 vs “actual SOTA” 0.608 by Aug 2025). (`TECH-2025-073`)
- SWE‑bench Verified pace **0.18×** (pred 0.85 vs “actual SOTA” 0.745 by Aug 2025). (`TECH-2025-072`)

### Coding time horizon (late‑2025): **roughly on pace (with a big footnote)**
- Time horizon pace **1.04×** vs a “central AI‑2027‑speed” trajectory; **0.66×** vs an erroneously plotted trajectory. (`TECH-2025-074`)

This is exactly where METR methodology sensitivity matters: TH1→TH1.1 changes suites and can shift slope estimates (`metr-2026-time-horizon-1-1`).

### R&D uplift: **behind (and epistemically fragile)**
The spreadsheet’s “AI software R&D uplift” category aggregates to ~**0.17×** (mean/median) in its aggregation section; row-level notes indicate at least one uplift row is anchored to the authors’ own later model estimates (circularity risk flagged in `META-2026-135`).

External check pressure: METR’s “AI allowed vs disallowed” study found experienced OSS developers were *slower* with AI allowed in that setting (`metr-2025-ai-experienced-os-dev-productivity`), which suggests uplift is not guaranteed and is highly context/tooling dependent.

### Economic value: **mixed**
Row-level:
- Revenue pace **1.16×** (proxy: OpenAI $20B annualized end‑2025). (`ECON-2026-916`)
- Valuation pace **0.44×** (proxy: OpenAI $500B as of Oct 2, 2025). (`ECON-2026-917`)

### Compute: **mostly on pace (but hard to observe)**
The grading post says compute growth is “mostly on pace,” with uncertainty about “largest training run.” In the spreadsheet, compute category mean/median are ~0.90/0.96.

Interpretation: the “inputs” story is strong; the decisive uncertainty is whether those inputs convert into reliable long-horizon autonomy and organization-level replacement.

---

## How the authors translate the scorecard into updated “takeoff timing”

The grading post maps ~0.65× pace into later timing:
- If progress continues at ~0.65×, AI‑2027‑style takeoff shifts to **late 2027–mid 2029**. (`TRANS-2026-028`)
- With additional slowdown adjustment using their newer model, takeoff shifts to **mid 2028–mid 2030**. (`TRANS-2026-029`)

Separately, their model update narrative says their new unified model implies **~3–5 years later** to coding automation vs the April 2025 AI‑2027‑era model, largely due to improved R&D automation modeling (not new evidence). (`META-2026-118`, `META-2026-119`)

And their Jan 26, 2026 forecast dashboard snapshot gives ATC percentiles for AC:
- Daniel AC p50 **Dec 2029**
- Eli AC p50 **Mar 2032** (`TRANS-2026-033`, `TRANS-2026-034`)

Synthesis: the “pace rescaling” story pushes the 2027 narrative later into ~2028–2030, while the explicit AC medians on the dashboard are later still (especially Eli), implying either (a) a wide distribution with heavy tail plus subjective ATC spread, or (b) that “takeoff window” talk is about a different reference point than AC p50 (e.g., a particular central trajectory or conditional path).

---

## What changed since AI 2027 (and why it matters for interpreting the review)

### 1) Their own models were materially revised (and had nontrivial bugs/edits)
The timelines-forecast note discloses a code bug that they claim moved SC median by ~9 months (`META-2026-126`) and adds a Dec 2025 disclaimer about reliance on intuitive judgment (`META-2026-127`). The forecast dashboard changelog also documents bug fixes and altered probabilities (`META-2026-129`, `META-2026-130`).

Interpretation: the review is not only “how did the world do,” but also “how did our modeling/implementation change.” This is good (honesty) but complicates naive “pace multipliers” as an objective scoreboard.

### 2) The “research taste / uplift” bottleneck is the crux and the least measurable
The Dec 2025 update explicitly shifts timelines later largely by revising beliefs about pre‑automation R&D speedups (`META-2026-118`, `META-2026-119`). The grading post also emphasizes uplift as behind pace. This points to a key synthesis claim:

If AI 2027’s fast takeoff depends on rapid conversion of coding capability into R&D automation, then evidence about real-world productivity/uplift and long-horizon autonomy is the highest-leverage place to check.

---

## External critique vs the authors’ self-audit (where they clash, where they converge)

### Marcus’s critique (methodological adversary)
Marcus’s critique is strongest on *probability hygiene* and *narrative risk*:
- vivid scenario framing can mislead likelihood judgments (`META-2026-132`)
- fear-based narratives can backfire politically (accelerate the race) (`RISK-2026-934`)

Where it converges with the self-audit: the authors’ later work (grading spreadsheet; explicit operational definitions) is partly a response to “fiction vs science” critique—i.e., they are trying to make the narrative falsifiable and scorable.

### Independent internal scorecard (another “pace” scalar)
The internal memo estimates ~**0.70×** pace and emphasizes the same structure: compute/capex inputs ahead; autonomy/productivity behind (`TRANS-2026-035`, `TRANS-2026-036`). This is broadly directionally consistent with the authors’ capabilities-only 0.58–0.66× range, with differences plausibly explained by metric choice and weighting.

---

## Methodological Red Flags (for interpreting “we are at 65% pace”)

1. **Aggregation is normative**: “capabilities only” vs “all,” and category vs row aggregation shift results materially.
2. **Cutoff dates and SOTA definitions are high-leverage**: “mid‑2025” resolved at “end of Aug 2025” is a choice, and agent/scaffold vs base-model distinctions matter.
3. **Protocol drift in key anchors**: METR TH suite updates (TH1→TH1.1) change the underlying measured quantity (`metr-2026-time-horizon-1-1`).
4. **Endogeneity risk**: “uplift” resolved by the authors’ later model estimates is not independent verification (flagged by `META-2026-135`).
5. **UI capture fragility**: interactive dashboards may not be reproducible unless key values are captured as text or exported data.

---

## What would most increase/decrease confidence in AI‑2027‑style 2027 takeoff (next checks)

1. **External-validity autonomy tests**: long-horizon SWE tasks on real repos with measured human time, spec ambiguity, and integration constraints (not just curated benchmark issues).
2. **R&D uplift measurement**: more RCT-like studies across settings, and clear separation of “tool helps” vs “autonomous agent replaces.”
3. **Higher-ceiling benchmarks**: the grading post notes that many relevant 2026 benchmarks didn’t exist in Apr 2025; these should be pre-registered with dated targets.
4. **Compute observability**: independent audit of largest training runs and leading-lab compute budgets (large uncertainty acknowledged by the authors).

---

## Bottom Line (Synthesis)

As of 2026-02-13, the “reviewing state” is:
- The AI Futures Project’s own audit grades their **2025 quantitative predictions** as **slower than AI 2027’s trajectory** (~0.58–0.66× on their “capabilities indicators”), but not an outright collapse.
- The slowdown is concentrated in **SWE-bench**, **uplift**, and **valuation proxies**, while **time-horizon** and many **compute/input** proxies are closer to on pace.
- Translating their own pace score into scenario timing shifts the AI‑2027 takeoff window to **~2028–2030** (self-reported), while their published ATC AC percentiles (Jan 2026 snapshot) imply even later medians and very wide uncertainty.

Practical implication: the 2027 “race / takeoff in 2027” narrative looks *less likely* under both the authors’ own scoring and independent “autonomy bottleneck” reasoning, but the review also leaves open a wide distribution where rapid acceleration could still occur if long-horizon autonomy and true R&D uplift improve sharply through 2026.

