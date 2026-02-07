# Synthesis Analysis: METR time horizon (long-task capability) 2025–2026

> **Source IDs**: `metr-2025-measuring-ai-ability-to-complete-long-tasks`, `metr-2025-time-horizon-vary-across-domains`, `metr-2026-time-horizon-1-1`
> **Analysis Date**: 2026-02-06
> **Analyst**: codex (gpt-5.2)
> **Rigor Level**: `[DRAFT]`
> **Type**: Cross-source synthesis

---

## The Question

What does METR’s “time horizon” work actually establish about AI ability to complete long tasks, how uncertain is the trend (error bars + protocol sensitivity), and how should this update AI-2027-style forecasts about near-term autonomy (especially in software work)?

---

## Primary Sources (This Synthesis)

| Source ID | Type | What it provides |
|---|---|---|
| `metr-2025-measuring-ai-ability-to-complete-long-tasks` | ARTICLE | Definition + headline trend claim (~7-month doubling) + forecasting interpretation; links to paper/code/data |
| `metr-2025-time-horizon-vary-across-domains` | ARTICLE | Cross-domain comparison: horizons and growth rates vary widely; OSWorld (GUI agents) much shorter than coding/math; Tesla proxy slower |
| `metr-2026-time-horizon-1-1` | ARTICLE | TH1.1 measurement update: task-suite expansion + Inspect migration; shows task-composition sensitivity; updates post-2023/post-2024 doubling estimates; ceiling/saturation concerns |

---

## High-Signal Evidence Anchors (Cross-Source)

1. **There is a strong exponential trend in the *released artifacts*, not just rhetoric.**  
   A quick independent re-fit from METR’s released TH1.0 raw runs supports ~7-month doubling for the frontier p50 time horizon (`TECH-2025-055`), consistent with METR’s linked preprint abstract. TH1.1’s post-2023 slope is faster (≈4–5 months doubling) and also roughly reproducible (`TECH-2026-928`).
2. **The error bars are real and not a minor footnote, and part of the uncertainty is “choice of task distribution.”**  
   TH1.1 explicitly shows that updating the suite can shift older models down and newer models up, changing trendline shape (`TECH-2026-929`, `META-2026-039`).
3. **“Autonomy” is not a single axis across domains (and GUI/computer-use is much shorter-horizon than coding/math).**  
   METR’s cross-domain artifacts support that OSWorld horizons are ~1–2 minutes for strong models, while coding/math horizons are ~100–300+ minutes (`TECH-2025-060`), implying that some real-world “do work on a computer” tasks may lag even if coding horizons rise.

---

## What METR Is Measuring (and what it is not)

### The metric
METR defines (for a given benchmark/task distribution) a model’s “p50 time horizon” as the task duration (measured in human minutes/hours) where the model’s success probability is 50%, typically estimated by fitting a logistic curve to success vs log(human time) (`META-2025-001`, `META-2025-002`).

### What it captures well
- Reliability under compounding steps: as tasks get longer, small error rates compound.
- A capability quantity with an interpretable unit (minutes/hours of human work), unlike many accuracy-based benchmarks.

### What it does not automatically capture
- Real-world project complexity: unclear specs, shifting requirements, coordination, security constraints, “codebase familiarization,” etc.
- Scaffold vs model effects: tool policies, retries, memory/compaction, and agent design can move horizons without changing core model weights.
- Vendor “LRA” framing: OpenAI’s GPT‑5.3‑Codex system card explicitly flags long-range autonomy (LRA) as under-thresholded and proxy-measured (e.g., TerminalBench + compaction harnesses), reinforcing that “time horizon” is definition- and scaffold-dependent (`openai-2026-gpt-5-3-codex-system-card`).

---

## The “Verticalish” Trendline vs Error Bars

The “verticalish” appearance is mostly a plotting intuition: exponential growth looks steep/near-vertical on linear scales and roughly linear on log scales. The more important question is whether the exponential continues and how sensitive it is to:
- **Task suite composition** (TH1→TH1.1 shifts; `META-2026-039`),
- **Ceiling/saturation** (few tasks remain unsolved by strongest models; `TECH-2026-930`),
- **Human-time estimation quality**, especially for long tasks (only 5/31 long tasks had measured human times in TH1.1; `TECH-2026-926`).

Bottom line: there is a genuine trend signal, but the *slope* and *mapping to real autonomy* remain high-leverage uncertainties.

---

## What This Suggests for AI 2027 (Update, not “proof”)

### Supports the empirical anchor behind AI-2027-style claims
The core “fast doubling of coding autonomy” premise used in `aifutures-2025-ai-2027` (notably `TECH-2025-051`) is directionally supported by METR’s work and is partially reproducible from released run data (`TECH-2025-055`, `TECH-2026-928`).

### But also adds two major caveats that weaken “straight-line” extrapolation
1. **Protocol/task-distribution sensitivity**: TH1.1 shows suite updates can change point estimates and slope comparisons (`TECH-2026-929`, `META-2026-039`). Extrapolating requires defining *which distribution of tasks* we care about.
2. **Cross-domain bottlenecks**: GUI/computer-use horizons are far shorter than coding/math (`TECH-2025-060`). Many economically and operationally important tasks (including “remote executive assistant”-style work) are GUI-heavy and may not track coding horizons.

### Practical interpretation for AI 2027
Treat METR’s time horizon as:
- **Strong evidence** that within-domain agentic capability (on these suites) is accelerating quickly, and
- **Weak-to-moderate evidence** for exact calendar predictions of “multi-day/week/month” autonomy in the real world, unless the benchmark distribution and scaffolds are demonstrated to generalize.

---

## What Would Most Increase/Decrease Confidence (Next Checks)

1. **Stability under suite changes**: pre-register a task distribution and show doubling-time estimates are robust under suite refreshes.
2. **External-validity tests**: run the same horizon methodology on real-world SWE tasks with documented human time distributions (including codebase familiarization) and compare slopes.
3. **Cost-adjusted horizons**: report horizons under fixed cost budgets (tokens/latency/human oversight), not just raw success.
4. **Domain expansion**: add “short-horizon bottleneck” domains (GUI office work, security workflows, etc.) to see if their horizons begin catching up or remain stuck.
