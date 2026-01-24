# Source Analysis: `shisa-ai/jp-tl-bench` repository (implementation + artifacts)

> **Claim types**: `[F]` fact, `[T]` theory, `[H]` hypothesis, `[P]` prediction, `[A]` assumption, `[C]` counterfactual, `[S]` speculation, `[X]` contradiction  
> **Evidence**: **E1** systematic review/meta-analysis; **E2** peer-reviewed/official stats; **E3** expert consensus/preprint; **E4** credible journalism/industry; **E5** opinion/anecdote; **E6** unsupported/speculative

## Metadata

| Field | Value |
|---|---|
| **Source ID** | `shisaai-2026-jp-tl-bench-repo` |
| **Title** | JP-TL-Bench (GitHub repository) |
| **Author(s)** | Shisa.AI (GitHub org: shisa-ai) |
| **Date** | 2026 |
| **Type** | KNOWLEDGE |
| **URL** | https://github.com/shisa-ai/jp-tl-bench |
| **Reliability** | 0.82 |
| **Rigor Level** | `[REVIEWED]` |
| **Bias Notes** | First-party repository for the benchmark. High reliability for “what the code does” and for published artifacts; bias risk mainly concerns interpretation/marketing claims in README and any conclusions drawn from the benchmark outputs. |

**Claims YAML**: [`analysis/sources/shisaai-2026-jp-tl-bench-repo.yaml`](shisaai-2026-jp-tl-bench-repo.yaml)

## Stage 1: Descriptive Analysis

### Core Thesis
This repository provides a reproducible, open implementation and artifact bundle for JP-TL-Bench: a versioned anchored pairwise LLM-judge workflow for Japanese↔English translation evaluation.

### Summary (Neutral)
The repo contains:
- A versioned base-set snapshot (`baseset/v1.0`) with a manifest of 20 anchor models and their translations (70 items each), plus judged pairwise comparisons and derived score reports.
- Scripts to generate translations for a candidate model, generate candidate-vs-anchor comparison pairs, judge them with a configurable LLM judge, and aggregate results using Bradley–Terry (via `choix`) into win-rate and scaled scores (EN/LT).
- Multiple prompt variants for translation (full-context vs low-context vs ultra-low-context) and a compare prompt for judging.

The README emphasizes comparability via a frozen anchor snapshot and describes outputs (analysis JSONL, scores JSON) and how to run the benchmark against a custom model endpoint.

### Key Claims

| # | Claim | Claim ID | Type | Domain | Evid | Credence | Verified? | Falsifiable By |
|---:|---|---|---|---|---|---:|---|---|
| 1 | The repo includes a frozen, versioned Base Set v1.0 snapshot with a 20-model manifest and 70-item translation files per model | TECH-2026-050 | [F] | TECH | E2 | 0.95 | ok | Base set snapshot is missing/does not include a fixed manifest + translations |
| 2 | Scoring uses Bradley–Terry aggregation (via `choix`) and reports both win-rate and a 0–10 LT score derived from fitted strengths | TECH-2026-051 | [F] | TECH | E2 | 0.90 | ok | Scoring code does not implement Bradley–Terry or does not report LT/WR as described |
| 3 | The repo includes multiple translation prompt variants (full vs low vs ultra-low context), enabling prompt/context sensitivity studies | TECH-2026-052 | [F] | TECH | E2 | 0.90 | ok | Prompts do not exist or do not materially vary in context/instructions |
| 4 | The Base Set v1.0 includes the default judge model (`gemini-2.5-flash`) as an anchor, creating a plausible self-preference bias risk | TECH-2026-053 | [H] | TECH | E4 | 0.65 | ? | Evidence that including the judge as an anchor does not create measurable self-preference effects |
| 5 | The repository defines a versioning contract for base-set snapshots: minor versions may adjust calibration; major versions imply non-comparability | TECH-2026-054 | [F] | TECH | E2 | 0.85 | ok | No versioning contract exists or it contradicts the described semantics |

### Argument Structure

```
Goal: iteration-friendly JA↔EN translation evaluation
        ↓
Need: stable reference frame across runs
        ↓
Solution: freeze base set snapshot + compare candidates to anchors
        ↓
Aggregate: Bradley–Terry → LT/WR scores + slices
```

### Theoretical Lineage
- Reproducible benchmarking via frozen datasets/snapshots.
- Preference aggregation via Bradley–Terry, with score rescaling for interpretability.

### Scope & Limitations
- The repo provides strong **mechanical reproducibility** but cannot by itself guarantee **validity** of the judge model or generalization to other domains.
- Large artifacts (JSONL judge outputs) are available but expensive to fully audit manually.

## Stage 2: Evaluative Analysis

### Internal Coherence
The repo structure aligns with the claimed workflow and supports reproducible scoring: fixed anchors + fixed translation item set + explicit aggregation code. The main uncertainty is whether the evaluation protocol is “valid enough” for the kinds of nuanced Japanese phenomena it targets—this depends on prompt design and judge model behavior.

### Key Factual Claims Verified

| Claim (paraphrased) | Crux? | Source Says | Actual | External Source | Status |
|---|---:|---|---|---|---|
| Base Set v1.0 contains 20 anchors and per-model translation files with 70 items | **Y** | Snapshot exists | `baseset/v1.0/manifest.json` lists 20 models; translation JSONL files have 70 rows and include `english`/`difficulty` fields | https://github.com/shisa-ai/jp-tl-bench | ok |
| LT scoring is sigmoid(mean-centered BT params)×10 | **Y** | LT is Bradley–Terry-derived | `choix_analyzer.py` computes LT as `1/(1+exp(-(params-mean))) * 10` | https://github.com/shisa-ai/jp-tl-bench | ok |
| Prompts include full/low/ultra-low context variants | N | Multiple prompt files exist | `prompts/translate_prompt_from_{english,japanese}*.txt` includes detailed vs minimal vs ultra-minimal instructions | https://github.com/shisa-ai/jp-tl-bench | ok |

### Disconfirming Evidence Search

| Claim | Counterevidence Found | Alternative Explanation | Search Notes |
|---|---|---|---|
| “Anchored scoring avoids most drift concerns” | Score stability still depends on judge model staying stable over time; vendor judges can silently update | Anchoring reduces *pool drift* but not *judge drift* | Considered common drift sources: model version updates, prompt changes, decoding changes; repo locks some but not all |

### Evidence Assessment
- **High** for implementation details (directly inspectable).
- **Medium** for judge validity/stability and generalization.

### Credence Assessment
- **Overall Credence**: 0.80  
- **Reasoning**: The repo provides unusually strong transparency (manifest, prompts, scoring code, reports). Remaining risk is primarily methodological (judge dependence, domain coverage).

## Stage 3: Dialectical Analysis

### Steelmanned Argument
An open repository with a frozen base set and explicit scoring code is the right way to make LLM-judge evaluation defensible. By publishing prompts, manifests, and score reports, the repo makes it possible for others to reproduce results, audit protocol details, and adapt the same structure to other language pairs or tasks.

### Strongest Counterarguments
1. **Judge dependence remains**: reproducibility is only as strong as the judge’s stability and calibration.
2. **Anchor staleness**: a fixed base set can become outdated as frontier models progress, compressing top-end scores again.

### Supporting Theories

| Theory/Framework | Source ID | How It Supports |
|---|---|---|
| Snapshot-based reproducibility | `shisaai-2026-jp-tl-bench-repo` | Fixing artifacts is a standard way to make evaluation comparable across time |

### Contradicting Theories

| Theory/Framework | Source ID | Point of Conflict |
|---|---|---|
| Continual benchmark refresh as requirement | `shisaai-2026-jp-tl-bench-repo` | A frozen snapshot risks becoming stale; continual refresh undermines comparability |

### Synthesis Notes
The repo is unusually actionable: it contains the “audit trail” needed to critique or reproduce claims. For broader trust, the next step is documenting judge-sensitivity (different judges, panel/jury judging) and mapping LT to human MQM on a subset.

### Claims to Cross-Reference
- Cross-validate LT vs COMET/MQM on overlapping item sets.
- Measure whether including the judge as an anchor changes its own relative placement (self-preference audit).

---

### Claim Summary

| ID | Type | Domain | Evidence | Credence | Claim |
|---|---|---|---|---:|---|
| TECH-2026-050 | [F] | TECH | E2 | 0.95 | The repo includes a frozen Base Set v1.0 snapshot with a 20-model manifest and 70-item translations per model |
| TECH-2026-051 | [F] | TECH | E2 | 0.90 | Scoring aggregates pairwise outcomes via Bradley–Terry (`choix`) and reports WR% plus a 0–10 LT score |
| TECH-2026-052 | [F] | TECH | E2 | 0.90 | The repo includes full/low/ultra-low translation prompt variants |
| TECH-2026-053 | [H] | TECH | E4 | 0.65 | Including the judge model as an anchor creates a plausible self-preference bias risk |
| TECH-2026-054 | [F] | TECH | E2 | 0.85 | The repo defines base-set snapshot versioning semantics (minor vs major) for comparability |

---

**Analysis Date**: 2026-01-24  
**Analyst**: gpt-5.2  
**Credence in Analysis**: 0.80

