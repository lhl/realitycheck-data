# Reality Check Knowledge Base

A unified knowledge base for rigorous analysis of claims across technology, economics, labor, and governance domains. Uses the [Reality Check](https://github.com/lhl/realitycheck) framework.

## Current Status

| Metric | Count |
|--------|-------|
| **Claims** | 259 |
| **Sources** | 72 |
| **Argument Chains** | 4 |
| **Predictions Tracked** | 19 |

See [claims/README.md](claims/README.md) for full statistics.

## Navigation

- Sources index: [reference/README.md](reference/README.md)
- Predictions dashboard: [tracking/predictions.md](tracking/predictions.md)
- Claim registry (YAML export): [claims/registry.yaml](claims/registry.yaml)
- Source registry (YAML export): [reference/sources.yaml](reference/sources.yaml)
- Meta-analysis: [analysis/meta/framework-efficacy-greenland-test.md](analysis/meta/framework-efficacy-greenland-test.md)

---

## Analyses

### Syntheses

| Date | Document | Status | Summary |
|------|----------|--------|---------|
| 2026-01-24 | [JP-TL-Bench and JA↔EN Translation Evaluation](analysis/syntheses/jp-tl-bench-ja-en-translation-eval-synthesis.md) | `[DRAFT]` | Cross-source synthesis: anchored pairwise vs metrics/MQM; Japanese context challenges; directionality; novelty/tradeoffs |
| 2026-01-24 | [PageIndex vs StrataLens (Vectorless RAG)](analysis/syntheses/pageindex-vs-stratalens-vectorless-rag-synthesis.md) | `[DRAFT]` | Cross-source comparison: structure-aware retrieval vs vectorless traversal; benchmark claims flagged as protocol-dependent; maturity/licensing assessment |
| 2026-01-19 | [Vibecoding / Agent Psychosis](analysis/syntheses/vibecoding-agent-psychosis-synthesis.md) | `[DRAFT]` | Verification bottleneck as artifact generation gets cheap |
| 2026-01-19 | [Yegge Vibe Coding 2025-2026](analysis/syntheses/yegge-2025-2026-vibe-coding-synthesis.md) | `[DRAFT]` | Evolution of coding agent discourse |
| 2026-01-18 | [Neofeudalism Discourse](analysis/syntheses/neofeudalism-discourse-synthesis.md) | `[DRAFT]` | Post-labor economics, permanent underclass thesis |

### Argument Chains

| Chain | Thesis | Credence |
|-------|--------|----------|
| [Permanent Underclass](claims/chains/permanent-underclass.md) | Post-labor → permanent underclass by default | 0.30 |
| [Genocide Default](claims/chains/genocide-default.md) | Elites will choose genocide over UBI | 0.10 |
| [Open Source De-Darkener](claims/chains/open-source-de-darkener.md) | Open models shift power from cognition to infrastructure | 0.60 |

### Source Analyses

| Date | Document | Status | Summary |
|------|----------|--------|---------|
| 2026-01-25 | [Inference Cost Analysis & Projections (lhl)](analysis/sources/lhl-2026-frontier-llm-token-unit-economics.md) | `[DRAFT]` | Frontier inference unit economics: caching + routing dominate; reasoning/long-context are hidden cost multipliers; includes cache-heavy case study |
| 2026-01-24 | [Gas Town’s Agent Patterns (Appleton)](analysis/sources/appleton-2026-gastown-agent-patterns.md) | `[REVIEWED]` | Design-fiction read of Gas Town; bottleneck shifts to design/verification; orchestration patterns + “code distance” axis |
| 2026-01-24 | [JP-TL-Bench paper (Lin & Lensenmayer 2026)](analysis/sources/lin-2026-jp-tl-bench-paper.md) | `[REVIEWED]` | Anchored pairwise LLM-judge benchmark for JA↔EN translation; Bradley–Terry aggregation + LT scoring; protocol dependence noted |
| 2026-01-24 | [JP-TL-Bench (blog)](analysis/sources/lin-2025-jp-tl-bench.md) | `[REVIEWED]` | Release post motivating anchored pairwise evaluation vs metric compression for high-end JA↔EN translation |
| 2026-01-24 | [JP-TL-Bench Directional Analysis](analysis/sources/lin-2026-jp-tl-bench-directional-analysis.md) | `[REVIEWED]` | Direction and difficulty slices show large asymmetries (e.g., Llama 3.1 8B); qualitative examples |
| 2026-01-24 | [JP-TL-Bench repo](analysis/sources/shisaai-2026-jp-tl-bench-repo.md) | `[REVIEWED]` | Open artifacts: Base Set v1.0 snapshot, prompts, scoring code; reproducibility and bias considerations |
| 2026-01-24 | [Shisa V2](analysis/sources/lin-2025-shisa-v2.md) | `[REVIEWED]` | Model family release context; claims about Japanese eval gaps and new translation benchmark motivation |
| 2026-01-24 | [Shisa V2 405B](analysis/sources/lin-2025-shisa-v2-405b.md) | `[REVIEWED]` | Model release positioning; internal eval suite framing; translation evaluation rationale |
| 2026-01-24 | [Shisa V2.1](analysis/sources/shisaai-2025-shisa-v2-1.md) | `[REVIEWED]` | Dataset/recipe refresh claims; context for Japanese-specific improvements (incl. translation/politeness) |
| 2026-01-24 | [Liquid AI Hackathon Tokyo repo](analysis/sources/lhl-2025-liquid-ai-hackathon-tokyo.md) | `[REVIEWED]` | COMET-centered llm-jp-eval MT workflow; prompt asymmetry and metric clustering cautions |
| 2026-01-24 | [LiquidAI LFM2-350M-ENJP-MT model card](analysis/sources/liquidai-2025-lfm2-350m-enjp-mt.md) | `[REVIEWED]` | Vendor description of a small bidirectional EN↔JA MT checkpoint for low-latency use |
| 2026-01-24 | [TranslateGemma Technical Report](analysis/sources/google-2026-translategemma-tech-report.md) | `[REVIEWED]` | SFT+RL translation specialization of Gemma 3; WMT metrics + MQM human eval; en→ja gains reported |
| 2026-01-24 | [TranslateGemma blog](analysis/sources/google-2026-translategemma-blog.md) | `[REVIEWED]` | Announcement summary: model sizes, language coverage, and metric-based gains |
| 2026-01-24 | [FinanceBench (Islam et al. 2023)](analysis/sources/islam-2023-financebench.md) | `[REVIEWED]` | Benchmark baseline: 10,231 Qs; human-eval sample shows high failure rates for GPT-4-Turbo+retrieval; oracle ~85% |
| 2026-01-24 | [@_avichawla thread on PageIndex](analysis/sources/avichawla-2026-pageindex-thread.md) | `[REVIEWED]` | Social summary of “vectorless RAG”; highlights similarity≠relevance + structure-aware retrieval; performance claim flagged as protocol-dependent |
| 2026-01-24 | [VectifyAI PageIndex repo](analysis/sources/vectifyai-2025-pageindex.md) | `[REVIEWED]` | Repo review: hierarchical tree index + LLM traversal (no vector DB); strong adoption but limited CI/tests; “98.7% FinanceBench” is vendor-reported |
| 2026-01-24 | [VectifyAI Mafin 2.5 FinanceBench results repo](analysis/sources/vectifyai-2025-mafin25-financebench.md) | `[REVIEWED]` | Eval artifacts: claims 98.7% via permissive LLM-judge; not directly comparable to FinanceBench human-eval baselines |
| 2026-01-24 | [StrataLens AI repo](analysis/sources/kamathhrishi-2025-stratalens-ai.md) | `[REVIEWED]` | Single-maintainer hybrid RAG (pgvector+rerank+section routing); claims 85% on FinanceBench subset; repo license file missing |
| 2026-01-23 | [Anthropic "Claude's Constitution"](analysis/sources/anthropic-2026-claudes-constitution.md) | `[REVIEWED]` | Values/behavior spec: “final constitutional authority”; hard constraints (WMD uplift, critical infrastructure attacks, malware, CSAM); virtue-ethics + model-welfare framing |
| 2026-01-22 | [Stross "The pivot" (Part 1)](analysis/sources/stross-2025-the-pivot-1.md) | `[REVIEWED]` | 2025 inflection-point thesis: energy transition + climate/food risk + post-Moore’s Law tech/finance |
| 2026-01-22 | [OpenAI "Value Intelligence"](analysis/sources/openai-value-intelligence.md) | `[REVIEWED]` | Compute + ARR scaling claims; compute-scarcity flywheel; tiered monetization framing |
| 2026-01-21 | [Rogan & Musk "JRE #2404 — Elon Musk"](analysis/sources/jre-2404-elon-musk-2025-ai-woke-mind-virus.md) | `[REVIEWED]` | Transcript excerpt: truth-seeking alignment, Gemini ImageGen controversy, and objective mis-specification risks |
| 2026-01-21 | [Chatterjee et al. "ANZ Copilot Study"](analysis/sources/chatterjee-2024-anz-copilot-study.md) | `[REVIEWED]` | ANZ A/B study: Copilot group completes coding challenges ~42.36% faster |
| 2026-01-21 | [Peng et al. "GitHub Copilot Productivity"](analysis/sources/peng-2023-copilot-productivity.md) | `[REVIEWED]` | Controlled trial: Copilot users complete a coding task ~55.8% faster |
| 2026-01-21 | [Carney "Middle Powers & Rupture"](analysis/sources/carney-2026-davos-wef-speech.md) | `[REVIEWED]` | WEF Davos speech on coalition strategy vs. great power coercion |
| 2026-01-18 | [Doctorow "Reverse Centaur"](analysis/sources/doctorow-2026-reverse-centaur.md) | `[REVIEWED]` | AI bubble critique + "reverse centaur" deployment patterns |
| 2026-01-18 | [Perera "China's Trillion-Dollar Illusion"](analysis/sources/perera-2026-chinas-trillion-dollar-illusion.md) | `[REVIEWED]` | "Demand-destruction surplus" mechanism analysis |
| 2026-01-18 | [Ronacher "Agent Psychosis"](analysis/sources/ronacher-2026-agent-psychosis.md) | `[REVIEWED]` | Maintainer-centric analysis of agentic-coding addiction/slop loops |
| 2026-01-16 | [Teortaxes "Greenland Endgame"](analysis/sources/teortaxes-2026-greenland-endgame.md) | `[REVIEWED]` | GOV/RESOURCE/TRANS claims extraction with fact-checks |

---

## Claim Domains

| Domain | Description | Claims |
|--------|-------------|--------|
| TECH | Technology & AI | 104 |
| LABOR | Labor & Employment | 17 |
| ECON | Economics & Markets | 29 |
| GOV | Governance & Policy | 32 |
| SOC | Social Dynamics | 5 |
| TRANS | Transition Dynamics | 24 |
| RESOURCE | Resource Constraints | 11 |
| GEO | Geopolitics | 1 |
| META | Framework & Methodology | 23 |

---

## Repository Structure

```
realitycheck-data/
├── README.md                 # This file
├── .realitycheck.yaml        # Framework configuration
│
├── data/
│   └── realitycheck.lance/   # LanceDB database (git-lfs)
│
├── claims/
│   ├── README.md             # Claim statistics (auto-generated)
│   ├── registry.yaml         # Exported claim registry
│   └── chains/               # Argument chain analyses
│
├── reference/
│   ├── sources.yaml          # Source bibliography
│   ├── primary/              # Primary source materials
│   ├── transcripts/          # AI-assisted analysis transcripts
│   ├── articles/             # Article references
│   └── data/                 # Data source references
│
├── analysis/
│   ├── sources/              # Individual source analyses
│   ├── syntheses/            # Cross-source syntheses
│   └── meta/                 # Framework meta-analyses
│
├── tracking/
│   ├── predictions.md        # Prediction tracking
│   ├── dashboards/           # Indicator dashboards
│   └── updates/              # Prediction updates
│
├── scenarios/                # Scenario matrices
│
└── inbox/                    # Work tracking
    ├── to-catalog/
    ├── to-analyze/
    └── in-progress/
```

---

## Using This Knowledge Base

### Prerequisites

Install the [Reality Check](https://github.com/lhl/realitycheck) framework:

```bash
# Clone the framework
git clone https://github.com/lhl/realitycheck.git
cd realitycheck
uv sync  # Install dependencies
```

### Validate Data Integrity

```bash
export REALITYCHECK_DATA=/path/to/realitycheck-data/data/realitycheck.lance
uv run python scripts/validate.py --mode db
```

### Query Claims

```bash
# Search claims
uv run python scripts/db.py search "automation labor"

# List claims by domain
uv run python scripts/db.py claim list --domain LABOR

# Get specific claim
uv run python scripts/db.py claim get TECH-2026-001
```

### Export Data

```bash
# Export claims to YAML
uv run python scripts/export.py yaml claims -o claims/registry.yaml

# Export summary to Markdown
uv run python scripts/export.py md summary -o claims/README.md
```

---

## Research Questions

1. **Transition Dynamics**: How do economies transition to post-scarcity?
2. **Value Theory**: What happens to value when marginal cost → 0?
3. **Distribution**: Who owns AI/automation means of production?
4. **Labor**: What happens to human work and meaning?
5. **Governance**: What structures handle coordination in post-labor world?
6. **Timeline**: How plausible are 2035-2045 predictions?
7. **Bottlenecks**: Who controls compute, energy, chips?

---

## License

- **Framework**: [Reality Check](https://github.com/lhl/realitycheck) - Apache 2.0 License
- **Analyses**: Cite appropriately

---

*Last updated: 2026-01-25*
