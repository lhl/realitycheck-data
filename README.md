# Reality Check Knowledge Base

A unified knowledge base for rigorous analysis of claims across technology, economics, labor, and governance domains. Uses the [Reality Check](https://github.com/lhl/realitycheck) framework.

## Current Status

| Metric | Count |
|--------|-------|
| **Claims** | 99 |
| **Sources** | 44 |
| **Argument Chains** | 3 |
| **Predictions Tracked** | 9 |

See [claims/README.md](claims/README.md) for full statistics.

---

## Analyses

### Source Analyses

| Date | Document | Status | Summary |
|------|----------|--------|---------|
| 2026-01-21 | [Carney "Middle Powers & Rupture"](analysis/sources/carney-2026-davos-wef-speech.md) | `[REVIEWED]` | WEF Davos speech on coalition strategy vs. great power coercion |
| 2026-01-18 | [Doctorow "Reverse Centaur"](analysis/sources/doctorow-2026-reverse-centaur.md) | `[REVIEWED]` | AI bubble critique + "reverse centaur" deployment patterns |
| 2026-01-18 | [Perera "China's Trillion-Dollar Illusion"](analysis/sources/perera-2026-chinas-trillion-dollar-illusion.md) | `[REVIEWED]` | "Demand-destruction surplus" mechanism analysis |
| 2026-01-18 | [Ronacher "Agent Psychosis"](analysis/sources/ronacher-2026-agent-psychosis.md) | `[REVIEWED]` | Maintainer-centric analysis of agentic-coding addiction/slop loops |
| 2026-01-16 | [Teortaxes "Greenland Endgame"](analysis/sources/teortaxes-2026-greenland-endgame.md) | `[REVIEWED]` | GOV/RESOURCE/TRANS claims extraction with fact-checks |
| 2026-01-15 | [OpenAI "Value Intelligence"](analysis/sources/openai-value-intelligence.md) | `[REVIEWED]` | Value capture dynamics in AI systems |

### Syntheses

| Document | Status | Summary |
|----------|--------|---------|
| [Neofeudalism Discourse](analysis/syntheses/neofeudalism-discourse-synthesis.md) | `[DRAFT]` | Post-labor economics, permanent underclass thesis |
| [Vibecoding / Agent Psychosis](analysis/syntheses/vibecoding-agent-psychosis-synthesis.md) | `[DRAFT]` | Verification bottleneck as artifact generation gets cheap |
| [Yegge Vibe Coding 2025-2026](analysis/syntheses/yegge-2025-2026-vibe-coding-synthesis.md) | `[DRAFT]` | Evolution of coding agent discourse |

### Argument Chains

| Chain | Thesis | Credence |
|-------|--------|----------|
| [Permanent Underclass](claims/chains/permanent-underclass.md) | Post-labor → permanent underclass by default | 0.30 |
| [Genocide Default](claims/chains/genocide-default.md) | Elites will choose genocide over UBI | 0.10 |
| [Open Source De-Darkener](claims/chains/open-source-de-darkener.md) | Open models shift power from cognition to infrastructure | 0.60 |

---

## Claim Domains

| Domain | Description | Claims |
|--------|-------------|--------|
| TECH | Technology & AI | 13 |
| LABOR | Labor & Employment | 12 |
| ECON | Economics & Markets | 14 |
| GOV | Governance & Policy | 32 |
| SOC | Social Dynamics | 3 |
| TRANS | Transition Dynamics | 13 |
| RESOURCE | Resource Constraints | 4 |
| GEO | Geopolitics | 0 |
| META | Framework & Methodology | 8 |

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

*Last updated: 2026-01-21*
