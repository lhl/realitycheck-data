# Source Analysis: Superlinear-Exp-v0.1 (Hugging Face model release)

> **Claim types**: `[F]` fact, `[T]` theory, `[H]` hypothesis, `[P]` prediction, `[A]` assumption, `[C]` counterfactual, `[S]` speculation, `[X]` contradiction  
> **Evidence**: **E1** systematic review/meta-analysis; **E2** peer-reviewed/official stats/law/code+tests; **E3** expert consensus/preprint; **E4** credible journalism/industry; **E5** opinion/anecdote; **E6** unsupported/speculative

## Metadata

| Field | Value |
|-------|-------|
| **Source ID** | `concavityai-2026-superlinear-exp-v0-1` |
| **Title** | Superlinear-Exp-v0.1 |
| **Author(s)** | Concavity AI (Yufeng Huang) |
| **Date** | 2026-02-06 (HF last-modified) |
| **Type** | KNOWLEDGE |
| **URL** | https://huggingface.co/concavity-ai/superlinear-exp-v0.1 |
| **Reliability** | 0.65 |
| **Rigor Level** | [REVIEWED] |
| **Bias Notes** | Self-released experimental weights + remote code; strong evidence for what is distributed (config/weights/code), weaker evidence for performance claims and downstream safety/robustness. |

**Capture note**: HF repo `sha=06ea7933166a63d3bd13b808d6f8d8aead7ed25c`, `lastModified=2026-02-06T10:38:19Z` (via HF API).  
**Claims YAML**: [`analysis/sources/concavityai-2026-superlinear-exp-v0-1.yaml`](concavityai-2026-superlinear-exp-v0-1.yaml)

## Stage 1: Descriptive Analysis

### Core Thesis
Release a derivative Nemotron-3-Nano-30B-A3B model with standard attention layers replaced by Superlinear span-search + span-attention, demonstrating feasibility of extremely long-context inference (and limited NIAH retrieval fine-tuning), with supporting remote code for Transformers loading.

### Summary (Neutral)
The Hugging Face repository contains:

- **Model weights** in 16 `safetensors` shards (plus index).
- **Transformers remote code** (`configuration_superlinear_exp.py`, `modeling_superlinear_exp.py`, `moe.py`) to load and run the model using `trust_remote_code=True`.
- A **model card** that:
  - explains the Superlinear attention mechanism (accumulation → span-search → span-attention → combination),
  - provides **hardware guidance** (B200/VRAM),
  - reports **throughput measurements** at 1M and 10M context,
  - states **limitations** (not comprehensive; NIAH + throughput focus; experimental; O(L) memory),
  - documents licensing (NVIDIA Open Model License), and includes a **patent notice**.

The repository declares the upstream base model as `nvidia/NVIDIA-Nemotron-3-Nano-30B-A3B-BF16` and includes a NOTICE stating the modifications: replacing attention layers with Superlinear attention and fine-tuning on long-context retrieval tasks.

### Key Claims

| # | Claim | Claim ID | Layer | Actor | Scope | Quantifier | Type | Domain | Evid | Credence | Verified? | Falsifiable By |
|---|-------|----------|-------|-------|-------|------------|------|--------|------|----------:|-----------|----------------|
| 1 | The HF repo distributes a derivative of NVIDIA Nemotron-3-Nano-30B-A3B with attention layers replaced by Superlinear attention and some long-context retrieval fine-tuning | TECH-2026-960 | PRACTICED | OTHER:Concavity AI | who=maintainers; where=HF repo; when=2026-02; predicate=derivative model + modifications | N/A | [F] | TECH | E2 | 0.90 | yes (NOTICE) | NOTICE/config contradicts derivative/modification description |
| 2 | Running the model requires `trust_remote_code=True` (executing repo-provided Python) | TECH-2026-961 | PRACTICED | OTHER:Transformers loader | who=users; where=HF; when=2026-02; predicate=remote code execution | N/A | [F] | TECH | E2 | 0.95 | yes | Model loads cleanly without remote code (no `auto_map` / custom classes) |
| 3 | The remote code depends on the separate `superlinear` package for custom Triton kernels (span-search/span-attention); without it, model import raises an error | TECH-2026-962 | PRACTICED | OTHER:model implementation | who=users; where=Python env; when=2026-02; predicate=external dependency | N/A | [F] | TECH | E2 | 0.85 | yes (code) | Remote code runs without installing `superlinear` / does not import its kernels |
| 4 | The released weights are ~58.9 GiB (≈63.3 GB) on disk across 16 shards (16-bit), consistent with “~60 GB VRAM” guidance | TECH-2026-965 | PRACTICED | OTHER:model weights | who=users; where=HF LFS; when=2026-02; predicate=weight size | N/A | [F] | TECH | E2 | 0.90 | yes (HF API) | HF files are materially smaller/larger than claimed |
| 5 | The config implies a hybrid architecture with 52 layers and 6 attention layers (hybrid pattern has 6 `*`), consistent with KV cache ≈6 GB per 1M tokens at 16-bit | TECH-2026-964 | ASSERTED | OTHER:model architecture | who=users; where=KV cache; when=2026; predicate=KV sizing | OTHER:order-of-magnitude | [F] | TECH | E2 | 0.85 | yes (derived) | Config implies a different number of attention layers or KV-head/head-dim that breaks the sizing |
| 6 | The model card reports B200 throughput at 1M and 10M context, and explicitly states limitations (NIAH + throughput focus; experimental; memory scales with length) | TECH-2026-966 | ASSERTED | OTHER:model card | who=authors; where=HF README; when=2026-02; predicate=reported throughput + limitations | OTHER:reported | [F] | TECH | E3 | 0.60 | partially (text exists) | Independent reproduction shows materially different throughput or limitations are contradicted by released eval artifacts |

### Argument Structure

```
[Release weights + remote code for Transformers]
    |
    v
[Model implements Superlinear span-search + span-attention in a Nemotron hybrid]
    |
    v
[Claim: feasible extremely long contexts on large GPUs; limited eval on NIAH + throughput]
    |
    v
[Warn: experimental, O(L) memory, trust_remote_code, license/patent constraints]
```

### Theoretical Lineage
- Upstream base model: NVIDIA Nemotron-3-Nano-30B-A3B (hybrid Mamba/attention/MoE).
- Superlinear attention architecture: `huang-2026-superlinear-multi-step-attention`.
- Kernel/runtime implementation: `concavityai-2026-superlinear` (separate repo/package).

### Scope & Limitations
- Strong evidence for what is shipped (weights + code + config + licensing terms).
- Weak evidence for the headline throughput numbers (self-reported; hardware-specific) and for general-task quality (explicitly not comprehensive).
- Elevated operational risk due to required `trust_remote_code=True` plus unusual inclusion of compiled `__pycache__/*.pyc` in the repo.

## Stage 2: Evaluative Analysis

### Internal Coherence
The model card’s narrative matches the paper/repo: Superlinear attention is implemented via custom kernels; long contexts are VRAM-bounded; evaluation is limited; and B200 is the reference hardware. The NOTICE file strengthens coherence by explicitly stating the derivative relationship and the nature of the modifications (replace attention layers; fine-tune retrieval).

### Key Factual Claims Verified

| Claim (paraphrased) | Crux? | Source Says | Actual | External Source | Status |
|---------------------|-------|-------------|--------|-----------------|--------|
| Derivative Nemotron with replaced attention layers + retrieval fine-tuning | **Y** | NOTICE + model card | `NOTICE` states derivative base + modifications; `config.json` uses `model_type=superlinear-exp` and hybrid pattern indicating attention layers exist but are custom | HF repo files (`NOTICE`, `config.json`) | ok |
| Requires `trust_remote_code=True` | **Y** | README warning | `config.json` uses `auto_map` to point to custom config/model classes; quickstart examples pass `trust_remote_code=True` | HF repo files (`config.json`, `README.md`) | ok |
| Remote code depends on `superlinear` package | **Y** | README suggests installing Superlinear repo | `modeling_superlinear_exp.py` imports `superlinear.kernels.superlinear.*` and raises ImportError if unavailable | HF repo file (`modeling_superlinear_exp.py`) | ok |
| Weight size and KV cache budget match “~60GB + ~6GB per 1M tokens” guidance | **Y** | README hardware section | HF tree shows ~58.9 GiB weights; config hybrid pattern has 6 attention layers and KV/cache shape parameters consistent with ~6GB per 1M tokens (16-bit) | HF API tree + `config.json` | ok (derived) |
| Throughput table at 1M/10M contexts | N | README | Table exists; not independently validated here | N/A | ? |

### Disconfirming Evidence Search

| Claim | Counterevidence Found | Alternative Explanation | Search Notes |
|-------|----------------------|-------------------------|--------------|
| “10M context throughput” is straightforwardly reproducible from HF | `max_position_embeddings` is set to 262,144 in `config.json`, which may surprise users expecting 10M out of the box | Extremely long contexts likely require server/session allocation overrides beyond default Transformers assumptions; the table may correspond to a specific runtime path in the Superlinear repo | Checked `config.json` and Superlinear adapter/server session API; did not reproduce |
| “trust_remote_code warning” is sufficient for security | HF repo includes `__pycache__/` with `.pyc` files, which is unusual and makes review harder | May be accidental packaging; still increases supply-chain risk perception | Listed HF siblings; noted pyc presence |
| License is permissive | NVIDIA Open Model License includes conditions (guardrails clause, attribution requirements, ethics terms) | “Permissive” in practice but with enforceable restrictions; users must read license | Read LICENSE header sections 2–3 |

### Corrections & Updates

| Item | URL | Published | Corrected/Updated | What Changed | Impacted Claim IDs | Action Taken |
|------|-----|-----------|-------------------|--------------|--------------------|-------------|
| N/A | N/A | N/A | N/A | No corrections observed as of analysis date. | N/A | N/A |

### Internal Tensions / Self-Contradictions

| Tension | Parts in Conflict | Implication |
|--------|-------------------|-------------|
| “Transformers model release” vs “requires external repo” | HF provides remote code, but core kernels live in the separate Superlinear package | Users may assume “pip install transformers” suffices; in practice you need the full Superlinear toolchain |
| “Extremely long context (10M)” vs `max_position_embeddings=262144` | Model card reports 10M throughput; config suggests 256K positional limit | Either the limit is not binding (NoPE / custom cache) or the benchmark used a different config/runtime; needs clarification for users |

### Persuasion Techniques

| Technique | Example from Source | Effect on Reader |
|----------|----------------------|------------------|
| Concrete throughput table | 1M/10M prefill/decode numbers | Strongly signals feasibility; can be overweighted without replication artifacts |
| Explicit limitations section | “Not comprehensive… experimental… memory scales…” | Good epistemic hygiene; reduces overclaim risk |

### Unstated Assumptions

| Assumption | Claim ID | Critical? | Problematic? |
|------------|----------|-----------|--------------|
| Users can safely execute and audit remote code before running | TECH-2026-961 | Y | Y |
| The Superlinear kernel toolchain is stable across CUDA/Triton/PyTorch versions | TECH-2026-962 | Y | ? |
| The reported throughput meaningfully reflects end-to-end serving workloads | TECH-2026-966 | N | ? |

### Evidence Assessment
- **Strong evidence (E2)**: derivative relationship (NOTICE), remote-code requirement (auto_map), external dependency (imports), weight size, and config parameters.
- **Weak evidence**: throughput and quality claims (self-reported; hardware-specific).
- **Operational/IP risk**: license conditions and patent notice may affect adoption decisions.

### Credence Assessment
- **Overall Credence**: 0.66  
- **Reasoning**: Shipped artifacts are concrete and consistent with the companion repo/paper, but running safely requires remote code + external kernels, and performance/quality claims remain largely unverified here.

## Stage 3: Dialectical Analysis

### Steelmanned Argument
Publishing weights plus runnable code lowers the barrier to reproducing long-context feasibility. The model card is candid about limitations and provides concrete configuration knobs. For the niche where you have enormous contexts and large GPUs, this release offers a credible starting point to explore the architecture and build serving workflows around explicit cache management.

### Strongest Counterarguments
1. **Security posture is tough**: `trust_remote_code=True` plus shipping `.pyc` artifacts increases risk for many environments.
2. **Repro gap**: without published benchmark scripts/logs, throughput numbers and NIAH results are hard to validate.
3. **Deployment constraints**: weight size (~60GB) and O(L) cache mean only a small set of users can realistically test 1M–10M contexts.

### Supporting Theories

| Theory/Framework | Source ID | How It Supports |
|------------------|-----------|-----------------|
| Subquadratic attention kernels as an enabler | `concavityai-2026-superlinear` | Provides the implementation needed to run the HF model |
| Structural non-exclusion definition | `huang-2026-superlinear-multi-step-attention` | Provides the conceptual justification behind the model modifications |

### Contradicting Theories

| Theory/Framework | Source ID | Point of Conflict |
|------------------|-----------|------------------|
| Retrieval-first systems render huge KV caches unnecessary | N/A | If RAG/external memory dominates, a 60GB model with 10M KV cache may be cost-ineffective |

### Synthesis Notes
Treat this as a **repro artifact**: strong for “what was shipped” and “how it’s supposed to be run”, weak for “it reliably works for general tasks at 10M tokens”.

### Claims to Cross-Reference
- Verify alignment between the HF remote code’s expected kernel APIs and the Superlinear repo’s versioned interfaces.

---

### Claim Summary

| ID | Type | Domain | Layer | Actor | Scope | Quantifier | Evidence | Credence | Claim |
|----|------|--------|-------|-------|-------|------------|----------|----------:|-------|
| TECH-2026-960 | [F] | TECH | PRACTICED | OTHER:Concavity AI | who=maintainers; where=HF repo; when=2026-02; predicate=derivative model + modifications | N/A | E2 | 0.90 | The HF repo distributes a derivative Nemotron-3-Nano-30B-A3B model with standard attention replaced by Superlinear attention and some long-context retrieval fine-tuning. |
| TECH-2026-961 | [F] | TECH | PRACTICED | OTHER:Transformers loader | who=users; where=HF; when=2026-02; predicate=remote code execution | N/A | E2 | 0.95 | Running the model requires `trust_remote_code=True` (custom config/model via `auto_map`). |
| TECH-2026-962 | [F] | TECH | PRACTICED | OTHER:model implementation | who=users; where=Python env; when=2026-02; predicate=external dependency | N/A | E2 | 0.85 | The remote code imports `superlinear` kernels and fails without the separate Superlinear package installed. |
| TECH-2026-963 | [F] | TECH | ASSERTED | OTHER:model config | who=users; where=config; when=2026; predicate=routing params | N/A | E2 | 0.85 | The config sets Superlinear routing parameters (e.g., `span_attention_*` exponents ≈0.55, `num_spans=3`, `sw_index=65`, `decode_kernel=staged-gqa`). |
| TECH-2026-964 | [F] | TECH | ASSERTED | OTHER:model architecture | who=users; where=KV cache; when=2026; predicate=KV sizing | OTHER:order-of-magnitude | E2 | 0.85 | The hybrid pattern implies 6 attention layers (out of 52), consistent with KV cache ≈6 GB per 1M tokens at 16-bit for this model shape. |
| TECH-2026-965 | [F] | TECH | PRACTICED | OTHER:model weights | who=users; where=HF LFS; when=2026-02; predicate=weight size | N/A | E2 | 0.90 | The released weights total ~58.9 GiB across 16 shards, consistent with “~60 GB VRAM” guidance for 16-bit loading. |
| TECH-2026-966 | [F] | TECH | ASSERTED | OTHER:model card | who=authors; where=HF README; when=2026-02; predicate=reported throughput + limitations | OTHER:reported | E3 | 0.60 | The model card reports B200 throughput at 1M/10M context and states limitations (NIAH+throughput focus; experimental; O(L) memory). |
| TECH-2026-968 | [F] | TECH | PRACTICED | OTHER:HF repo packaging | who=maintainers; where=HF files; when=2026-02; predicate=pyc included | N/A | E2 | 0.85 | The HF repo includes compiled `__pycache__/*.pyc` files alongside source, which is atypical for HF model repos and complicates auditing. |
| TECH-2026-969 | [F] | TECH | ASSERTED | OTHER:license/IP | who=maintainers; where=HF README; when=2026-02; predicate=patent notice | N/A | E2 | 0.80 | The model README includes a patent notice stating applications have been filed related to aspects of the methods. |

### Claims to Register

```yaml
sources:
  - id: "concavityai-2026-superlinear-exp-v0-1"
    type: "KNOWLEDGE"
    title: "Superlinear-Exp-v0.1"
    author: ["Concavity AI"]
    year: 2026
    url: "https://huggingface.co/concavity-ai/superlinear-exp-v0.1"
    accessed: "2026-02-07"
    status: "analyzed"
    analysis_file: "analysis/sources/concavityai-2026-superlinear-exp-v0-1.md"
claims:
  - id: "TECH-2026-961"
    text: "Running the model requires trust_remote_code=True (custom config/model via auto_map), executing Python code from the model repository."
    type: "[F]"
    domain: "TECH"
    evidence_level: "E2"
    credence: 0.95
    operationalization: "Inspect config.json for auto_map and attempt load with/without trust_remote_code."
    assumptions: ["Transformers respects auto_map as the mechanism for custom classes."]
    falsifiers: ["Model loads without remote code and without custom classes."]
    source_ids: ["concavityai-2026-superlinear-exp-v0-1"]
```

---

**Analysis Date**: 2026-02-07  
**Analyst**: codex (gpt-5.2)  
**Credence in Analysis**: 0.75

## Analysis Log

| Pass | Date | Tool | Model | Duration | Tokens | Cost | Notes |
|------|------|------|-------|----------|--------|------|-------|
| 1 | 2026-02-07 | codex | gpt-5.2 | ? | ? | ? | Initial 3-stage analysis + claim extraction; verified repo contents via HF API and code inspection |
