# Source Analysis: Superlinear (GitHub repo @ `df9b2ef`)

> **Claim types**: `[F]` fact, `[T]` theory, `[H]` hypothesis, `[P]` prediction, `[A]` assumption, `[C]` counterfactual, `[S]` speculation, `[X]` contradiction  
> **Evidence**: **E1** systematic review/meta-analysis; **E2** peer-reviewed/official stats/law/code+tests; **E3** expert consensus/preprint; **E4** credible journalism/industry; **E5** opinion/anecdote; **E6** unsupported/speculative

## Metadata

| Field | Value |
|-------|-------|
| **Source ID** | `concavityai-2026-superlinear` |
| **Title** | Superlinear |
| **Author(s)** | Concavity AI (repo contributors) |
| **Date** | 2026-02-06 (HEAD commit date) |
| **Type** | KNOWLEDGE |
| **URL** | https://github.com/concavity-ai/superlinear |
| **Reliability** | 0.70 |
| **Rigor Level** | [REVIEWED] |
| **Bias Notes** | Self-authored OSS repo released alongside a paper/model. Code is strong evidence for what’s implemented; README performance claims and “preview” framing should be treated as marketing/positioning unless independently replicated. |

**Capture note**: Snapshot corresponds to GitHub default branch `main` at commit `df9b2effd2ec73a43e36b9cebdf1b2e946aff751` (commit message: “Release 0.1 - Superlinear Multi-Step Attention”, dated **2026-02-06**).  
**Claims YAML**: [`analysis/sources/concavityai-2026-superlinear.yaml`](concavityai-2026-superlinear.yaml)

## Stage 1: Descriptive Analysis

### Core Thesis
Provide a practical long-context inference stack that exposes *stateful KV-cache sessions* and implements Superlinear multi-step attention (span-search + span-attention) with Triton kernels, enabling subquadratic attention compute at very long sequence lengths.

### Summary (Neutral)
This repo packages three closely related artifacts:

1. **Kernel/library package (`superlinear/`)**: a Torch+Triton implementation of “Superlinear Multi-Step Attention”, including:
   - **Span-search** along power-law “stripes” (anchor schedules) to pick top‑k spans.
   - **Span-attention** kernels, including GQA support and a bucketed prefill path for irregular spans.
   - A staged **decode** path optimized for `L_Q=1`.
   - Reference (PyTorch) implementations for validation/fallback.

2. **Engine (`superlinear/engine/`)**: adapters and utilities for model loading and generation, including:
   - A **stateful session** API that persists model cache across calls (`create_session`, `append_to_session`, `stream_generate_session`).
   - **Snapshots**: disk-resident, immutable checkpoints containing transcript + cache tensors.

3. **Apps (`apps/`)**:
   - **FastAPI server** implementing OpenAI-style `/v1/chat/completions` plus explicit session/snapshot endpoints.
   - **CLI** (`spl`) with chat and document-ingest REPLs and session/snapshot management.

The README emphasizes that the differentiator vs standard stateless chat is explicit control over KV cache lifetime (keep a multi‑million-token context “hot” across turns, save/load snapshots, control chunked prefill) and that the released model is a **research preview** with limited evaluation.

### Key Claims

| # | Claim | Claim ID | Layer | Actor | Scope | Quantifier | Type | Domain | Evid | Credence | Verified? | Falsifiable By |
|---|-------|----------|-------|-------|-------|------------|------|--------|------|----------:|-----------|----------------|
| 1 | The repo implements Superlinear span-search kernels over power‑law stripes and returns top‑k routed spans, with Triton and reference fallbacks (incl. GQA) | TECH-2026-951 | PRACTICED | OTHER:superlinear kernels | who=repo; where=Python/Triton; when=2026-02; predicate=span-search implemented | N/A | [F] | TECH | E2 | 0.90 | yes (code) | Kernel and reference implementations absent or do not match the described API |
| 2 | The repo implements span-attention kernels for routed contiguous spans, including a bucketed prefill/training path for irregular spans and staged decode kernels (incl. GQA) | TECH-2026-952 | PRACTICED | OTHER:superlinear kernels | who=repo; where=Python/Triton; when=2026-02; predicate=span-attn implemented | N/A | [F] | TECH | E2 | 0.85 | yes (code) | Span-attention kernels/bucketing absent or only dense attention is implemented |
| 3 | The repo provides an OpenAI-compatible FastAPI server with `/v1/chat/completions` plus explicit session and snapshot management endpoints | TECH-2026-953 | PRACTICED | OTHER:Superlinear server | who=repo; where=FastAPI; when=2026-02; predicate=OpenAI-style API | N/A | [F] | TECH | E2 | 0.85 | yes (code) | Server lacks OpenAI-style endpoint(s) or does not expose sessions/snapshots |
| 4 | The repo provides stateful KV-cache sessions that persist GPU-resident cache across calls (avoiding re-prefill for follow-ups) | TECH-2026-954 | PRACTICED | OTHER:Superlinear engine | who=repo; where=engine+adapter; when=2026-02; predicate=session cache reuse | N/A | [F] | TECH | E2 | 0.90 | yes (code) | Session APIs do not persist cache across calls |
| 5 | The repo supports disk snapshots that persist transcript + cache tensors (KV + Mamba conv/ssm states) for later restore | TECH-2026-955 | PRACTICED | OTHER:Superlinear engine | who=repo; where=session snapshots; when=2026-02; predicate=serialize+restore cache | N/A | [F] | TECH | E2 | 0.90 | yes (code) | Snapshots omit cache tensors or cannot be restored into a compatible session |
| 6 | The repo’s memory budgeting guidance for `superlinear-exp-v0.1` (weights ~60GB; KV cache ~6GB per 1M tokens per session) is numerically consistent with the released model config and HF weight sizes | TECH-2026-957 | ASSERTED | OTHER:repo docs | who=users; where=GPU VRAM; when=2026-02; predicate=memory sizing | OTHER:order-of-magnitude | [F] | TECH | E2 | 0.85 | yes (derived) | HF weights/config imply substantially different VRAM use per 1M tokens |
| 7 | The repo explicitly labels the system and weights as a research preview with limited evaluation (primarily NIAH) and not production/safety-evaluated | TECH-2026-958 | ASSERTED | OTHER:repo docs | who=maintainers; where=README; when=2026-02; predicate=scope+warnings | N/A | [F] | TECH | E2 | 0.95 | yes | README/model card removes/contradicts these warnings |

### Argument Structure

```
[Need long-context inference beyond dense attention limits]
    |
    v
[Use Superlinear attention kernels to keep attention compute subquadratic]
    |
    v
[Expose sessions/snapshots so users can keep KV cache hot + control VRAM]
    |
    v
[Provide OpenAI-style server + CLI for practical usage]
```

### Theoretical Lineage
- Directly implements the accompanying preprint: `huang-2026-superlinear-multi-step-attention`.
- Kernel co-design in the spirit of FlashAttention: turn asymptotic wins into throughput.
- Session/snapshot API aligns with the broader “stateful serving” pattern: separate prompt ingestion from decode turns.

### Scope & Limitations
- This repo is strong evidence for *existence of an implementation* and API surface.
- It is weaker evidence for the reported throughput and quality claims (which require reproduction).
- It is explicitly **CUDA/GPU**-centric; many features depend on Triton and CUDA extensions (`mamba-ssm`, `causal-conv1d`, etc.).

## Stage 2: Evaluative Analysis

### Internal Coherence
The repo is internally consistent: kernels expose “search spans then attend spans”, the adapter/engine exposes session lifecycle that keeps the cache object alive across calls, and the HTTP layer wraps these into OpenAI-like semantics with explicit session/snapshot management.

### Key Factual Claims Verified

| Claim (paraphrased) | Crux? | Source Says | Actual | External Source | Status |
|---------------------|-------|-------------|--------|-----------------|--------|
| Span-search is implemented as power-law stripe anchor scoring with top‑k selection, with Triton fast path and reference fallback | **Y** | README + kernels | `superlinear/kernels/superlinear/search/api.py` dispatches Triton vs reference; reference builds a stripe mask and computes top‑k anchors; GQA variants exist | local code inspection (GitHub raw) | ok |
| Bucketed span-attention exists for irregular spans (prefill/training), plus staged decode path | **Y** | README + paper reference | `superlinear/kernels/superlinear/span/_triton_bucketed_gqa.py` implements histogram/bucketing with atomics; staged decode API exists in `superlinear/kernels/superlinear/span/api.py` | local code inspection (GitHub raw) | ok |
| Server is OpenAI-style and exposes sessions/snapshots | **Y** | README | `apps/server/app.py` defines `/v1/chat/completions` and `/v1/sessions/*`; snapshot store uses `XDG_CACHE_HOME`/`SUPERLINEAR_SNAPSHOT_DIR` | local code inspection (GitHub raw) | ok |
| Session snapshots serialize transcript + cache tensors (KV + Mamba states) | **Y** | README | `superlinear/engine/session_snapshots.py` writes `manifest.json`, `transcript.json`, `cache.pt`; export/import copy KV and conv/ssm state tensors | local code inspection (GitHub raw) | ok |
| Memory budgeting (~60GB weights; ~6GB/1M tokens KV per session) is plausible for released model | **Y** | README | HF weights total ~58.9 GiB; config implies 6 attention layers and KV-head/head-dim such that KV cache ≈ 6 GB/1M tokens at 16-bit | https://huggingface.co/concavity-ai/superlinear-exp-v0.1 (`tree/main`, `config.json`) | ok (derived) |

### Disconfirming Evidence Search

| Claim | Counterevidence Found | Alternative Explanation | Search Notes |
|-------|----------------------|-------------------------|--------------|
| “Only depends on torch + triton” | True for core package, but model running requires additional CUDA-compiled deps (mamba-ssm/causal-conv1d) and Transformers | Repo is intentionally split: lightweight kernels core + heavier optional extras | Checked `pyproject.toml` deps vs README model install notes |
| “OpenAI-compatible server” implies broad API parity | Only a subset of OpenAI API surface is implemented (chat completions + some management endpoints) | “Compatible” likely means basic client interoperability, not full feature parity | Skimmed server routes; looked for `v1/chat/completions` and session APIs |
| “Full test coverage” (commit message) | Tests exist for CLI/engine/server, but kernel-level numerical correctness coverage is not prominent at top-level | Kernel testing may exist implicitly via reference implementations or omitted for brevity | Listed `tests/` tree via API; did not find dedicated kernel correctness suites |

### Corrections & Updates

| Item | URL | Published | Corrected/Updated | What Changed | Impacted Claim IDs | Action Taken |
|------|-----|-----------|-------------------|--------------|--------------------|-------------|
| N/A | N/A | N/A | N/A | No corrections observed in this snapshot. | N/A | N/A |

### Internal Tensions / Self-Contradictions

| Tension | Parts in Conflict | Implication |
|--------|-------------------|-------------|
| “Research preview” vs “OpenAI-compatible server” polish | Production-like API wrapper + stateful features, but explicit non-production warning | Signals seriousness about usability, but also a warning that model safety/quality isn’t established |
| “Sessions avoid re-prefill” vs “multiple sessions” VRAM cost | Sessions are great for single long-lived chat; multiple concurrent sessions multiply KV cache VRAM | Deployment may need a snapshot/eviction policy and strict concurrency controls |

### Persuasion Techniques

| Technique | Example from Source | Effect on Reader |
|----------|----------------------|------------------|
| Concrete throughput + memory numbers | Tables and “6GB per 1M tokens” rules of thumb | Helps adoption but can be over-trusted without replication |
| Strong disclaimers | “Not for production use” + safety caveats | Reduces overclaim risk; appropriately sets expectations |

### Unstated Assumptions

| Assumption | Claim ID | Critical? | Problematic? |
|------------|----------|-----------|--------------|
| Users can safely run `trust_remote_code=True` in their environment | TECH-2026-954 | Y | Y |
| The bucketed kernels remain stable across Triton/CUDA/toolchain versions | TECH-2026-952 | Y | ? |
| Snapshot format and compatibility fingerprinting are sufficient to prevent unsafe cache reuse | TECH-2026-955 | N | ? |

### Evidence Assessment
- **Strong evidence (E2)**: code-level existence of kernels, server routes, session/snapshot logic.
- **Medium evidence**: performance claims (not replicated here), quality claims (depend on external eval).
- **Operational risk**: model usage requires executing remote code and building CUDA extensions.

### Credence Assessment
- **Overall Credence**: 0.73  
- **Reasoning**: The core claims about implementation and session/snapshot features are directly supported by code. Performance and quality claims remain self-reported.

## Stage 3: Dialectical Analysis

### Steelmanned Argument
The repo delivers the missing product layer for long-context models: an API that treats KV cache as a managed resource (sessions + snapshots), plus kernels that make long contexts computationally feasible. This combination can enable qualitatively new workflows (persistent agents, massive-document workspaces) without repeatedly paying the ingestion cost.

### Strongest Counterarguments
1. **Security and supply-chain risk**: running a custom attention stack requires `trust_remote_code` and CUDA builds; this is a high bar for many users.
2. **Narrow quality evidence**: without broad benchmarks, it’s unclear whether speed translates into useful general performance at huge contexts.
3. **VRAM economics**: sessions are powerful but expensive; unless snapshots are used aggressively, multi-session serving may be impractical.

### Supporting Theories

| Theory/Framework | Source ID | How It Supports |
|------------------|-----------|-----------------|
| Structural non-exclusion + subquadratic attention | `huang-2026-superlinear-multi-step-attention` | Provides the architectural rationale behind the implementation |
| Stateful serving / cache management | `concavityai-2026-superlinear` | Exposes explicit lifecycle controls absent in stateless prompting setups |

### Contradicting Theories

| Theory/Framework | Source ID | Point of Conflict |
|------------------|-----------|------------------|
| External memory as default (RAG/DB) | N/A | If most long-context needs are met by retrieval + smaller active windows, maintaining huge KV caches may be cost-ineffective |

### Synthesis Notes
As software, this is best seen as a **long-context serving prototype**: credible implementation of the attention mechanism plus a useful session/snapshot abstraction. Decision-grade adoption still hinges on (a) independent performance reproduction and (b) safety/robustness evaluation of the released model.

### Claims to Cross-Reference
- Cross-check with the HF model code/config to ensure the repo and released weights remain compatible (`concavityai-2026-superlinear-exp-v0-1`).

---

### Claim Summary

| ID | Type | Domain | Layer | Actor | Scope | Quantifier | Evidence | Credence | Claim |
|----|------|--------|-------|-------|-------|------------|----------|----------:|-------|
| TECH-2026-950 | [F] | TECH | PRACTICED | OTHER:superlinear repo | who=repo; where=Python pkg; when=2026-02; predicate=inference stack exists | N/A | E2 | 0.85 | Superlinear is a Python package/repo providing long-context inference components (kernels + engine + server + CLI) built around Superlinear multi-step attention. |
| TECH-2026-951 | [F] | TECH | PRACTICED | OTHER:superlinear kernels | who=repo; where=Python/Triton; when=2026-02; predicate=span-search implemented | N/A | E2 | 0.90 | The repo implements span-search over power-law stripes (anchors) with Triton and reference implementations, including GQA variants. |
| TECH-2026-952 | [F] | TECH | PRACTICED | OTHER:superlinear kernels | who=repo; where=Python/Triton; when=2026-02; predicate=span-attn implemented | N/A | E2 | 0.85 | The repo implements span-attention kernels including bucketed prefill/training for irregular spans and staged decode kernels, including GQA variants. |
| TECH-2026-953 | [F] | TECH | PRACTICED | OTHER:Superlinear server | who=repo; where=FastAPI; when=2026-02; predicate=OpenAI-style API | N/A | E2 | 0.85 | The repo provides a FastAPI server implementing `/v1/chat/completions` and model listing endpoints, plus explicit session/snapshot APIs. |
| TECH-2026-954 | [F] | TECH | PRACTICED | OTHER:Superlinear engine | who=repo; where=adapter; when=2026-02; predicate=stateful sessions | N/A | E2 | 0.90 | The repo implements stateful KV-cache sessions that persist cache across calls for multi-turn chat, avoiding re-prefill. |
| TECH-2026-955 | [F] | TECH | PRACTICED | OTHER:Superlinear engine | who=repo; where=snapshots; when=2026-02; predicate=disk snapshots | N/A | E2 | 0.90 | The repo implements disk snapshots (v1) that persist transcript + cache tensors (KV + Mamba conv/ssm states) for later restore. |
| TECH-2026-956 | [F] | TECH | PRACTICED | OTHER:Superlinear CLI | who=repo; where=CLI; when=2026-02; predicate=spl tool | N/A | E2 | 0.80 | The repo provides a CLI (`spl`) for chatting, document ingestion, and session/snapshot management. |
| TECH-2026-957 | [F] | TECH | ASSERTED | OTHER:repo docs | who=users; where=GPU VRAM; when=2026-02; predicate=memory sizing | OTHER:order-of-magnitude | E2 | 0.85 | The repo’s memory budgeting guidance for `superlinear-exp-v0.1` (weights ~60GB; KV cache ~6GB/1M tokens per session) matches the released model’s weight size and configuration. |
| TECH-2026-958 | [F] | TECH | ASSERTED | OTHER:repo docs | who=maintainers; where=README; when=2026-02; predicate=scope+warnings | N/A | E2 | 0.95 | The repo explicitly labels the software/model as a research preview with limited evaluation and not production/safety-evaluated. |
| TECH-2026-959 | [F] | TECH | PRACTICED | OTHER:repo tests | who=repo; where=tests/; when=2026-02; predicate=test scope | N/A | E2 | 0.70 | The repo includes tests for CLI/engine/server behavior; dedicated numerical correctness tests for the Triton kernels are not prominent in the public `tests/` tree. |

### Claims to Register

```yaml
sources:
  - id: "concavityai-2026-superlinear"
    type: "KNOWLEDGE"
    title: "Superlinear"
    author: ["Concavity AI"]
    year: 2026
    url: "https://github.com/concavity-ai/superlinear"
    accessed: "2026-02-07"
    status: "analyzed"
    analysis_file: "analysis/sources/concavityai-2026-superlinear.md"
claims:
  - id: "TECH-2026-954"
    text: "The repo implements stateful KV-cache sessions that persist cache across calls for multi-turn chat, avoiding re-prefill for follow-up turns."
    type: "[F]"
    domain: "TECH"
    evidence_level: "E2"
    credence: 0.90
    operationalization: "Inspect adapter/session state objects; verify session lifecycle methods mutate and reuse a cache object across calls; run integration test if environment permits."
    assumptions: ["Model backend exposes a cache object with stable semantics across calls."]
    falsifiers: ["Session API recreates cache per request or discards cache between calls in practice."]
    source_ids: ["concavityai-2026-superlinear"]
```

---

**Analysis Date**: 2026-02-07  
**Analyst**: codex (gpt-5.2)  
**Credence in Analysis**: 0.76

## Analysis Log

| Pass | Date | Tool | Model | Duration | Tokens | Cost | Notes |
|------|------|------|-------|----------|--------|------|-------|
| 1 | 2026-02-07 | codex | gpt-5.2 | ? | ? | ? | Initial 3-stage analysis + claim extraction; code-level verification of kernels + sessions/snapshots + server routes |
