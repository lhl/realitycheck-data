# Reality Check v0.3.0 Reanalysis Backlog (rigor-v1)

- **Generated**: 2026-02-01 07:11Z

- **Project Root**: `/home/lhl/github/lhl/realitycheck-data`

- **DB**: `/home/lhl/github/lhl/realitycheck-data/data/realitycheck.lance`


## Completed (automatic)

- [x] Backfilled `analysis_logs.framework_version` + `analysis_logs.methodology_version` (from framework git tags via `rc-db analysis backfill-versions`).
- [x] New `analysis_logs` rows now auto-fill `framework_version` + `methodology_version`.

## How to Work This List

1. Pick the next source under **Source Analyses (Prioritized)**.
2. Update/rewrite the analysis to meet the v0.3.0 output contract + rigor-v1 (Layer/Actor/Scope/Quantifier + Corrections & Updates).
3. Update/verify extracted claims (credence/evidence), evidence links, and reasoning trails as needed.
4. Run validators:

   - `uv run python scripts/analysis_validator.py --rigor analysis/sources/<source-id>.md`
   - `rc-validate --strict` (or `uv run python scripts/validate.py --strict`)
5. After a batch of source upgrades, revisit syntheses in **Syntheses (After Sources)**.

## Source Analyses (Prioritized)

Total: **56** source analyses (`analysis/sources/*.md`).

Priority heuristic: chains → synthesis refs → high-credence claims → claim volume.


### ronacher-2026-agent-psychosis — Agent Psychosis: Are We Going Insane?

- **Analysis**: [analysis/sources/ronacher-2026-agent-psychosis.md](analysis/sources/ronacher-2026-agent-psychosis.md)
- **Claims**: 7 (high-credence/E1-E2: 0) | **In chain**: Y | **Referenced by syntheses**: 1
- **Latest analysis log**: `ANALYSIS-2026-032` (2026-02-01T08:46:26.526946Z) | fw=0.3.0 | meth=reanalysis-core@v0.3.0
- **TODOs**:
  - [x] Add `### Corrections & Updates` section (rigor-v1)
  - [x] Upgrade Key Claims table to include Layer/Actor/Scope/Quantifier (rigor-v1)
  - [x] Upgrade Claim Summary table to include Layer/Actor/Scope/Quantifier (rigor-v1)

### lhl-2026-frontier-llm-token-unit-economics — Inference Cost Analysis & Projections (Jan 2026)

- **Analysis**: [analysis/sources/lhl-2026-frontier-llm-token-unit-economics.md](analysis/sources/lhl-2026-frontier-llm-token-unit-economics.md)
- **Claims**: 24 (high-credence/E1-E2: 12) | **In chain**: N | **Referenced by syntheses**: 0
- **Latest analysis log**: `ANALYSIS-2026-033` (2026-02-01T08:56:06.936287Z) | fw=0.3.0 | meth=reanalysis-core@v0.3.0
- **TODOs**:
  - [x] Add missing sections: ### Internal Tensions, ### Persuasion Techniques, ### Unstated Assumptions, ### Claims to Register
  - [x] Add `Claims to Register` YAML block (`claims:`)
  - [x] Add `### Corrections & Updates` section (rigor-v1)
  - [x] Upgrade Key Claims table to include Layer/Actor/Scope/Quantifier (rigor-v1)
  - [x] Upgrade Claim Summary table to include Layer/Actor/Scope/Quantifier (rigor-v1)

### lhl-2026-realitycheck-readme — Reality Check

- **Analysis**: [analysis/sources/lhl-2026-realitycheck-readme.md](analysis/sources/lhl-2026-realitycheck-readme.md)
- **Claims**: 9 (high-credence/E1-E2: 9) | **In chain**: N | **Referenced by syntheses**: 1
- **Latest analysis log**: `ANALYSIS-2026-030` (2026-02-01T05:33:37.612327Z) | fw=0.3.0 | meth=check-core@v0.3.0
- **TODOs**:
  - [ ] No validator issues detected (still review for substantive reanalysis under v0.3.0).

### anthropic-2026-claudes-constitution — Claude's Constitution

- **Analysis**: [analysis/sources/anthropic-2026-claudes-constitution.md](analysis/sources/anthropic-2026-claudes-constitution.md)
- **Claims**: 16 (high-credence/E1-E2: 14) | **In chain**: N | **Referenced by syntheses**: 0
- **Latest analysis log**: _none_ (create a new pass when reanalyzing)
- **TODOs**:
  - [ ] Add `### Corrections & Updates` section (rigor-v1)
  - [ ] Upgrade Key Claims table to include Layer/Actor/Scope/Quantifier (rigor-v1)
  - [ ] Upgrade Claim Summary table to include Layer/Actor/Scope/Quantifier (rigor-v1)

### lhl-2026-realitycheck-data-readme — Reality Check Knowledge Base

- **Analysis**: [analysis/sources/lhl-2026-realitycheck-data-readme.md](analysis/sources/lhl-2026-realitycheck-data-readme.md)
- **Claims**: 6 (high-credence/E1-E2: 6) | **In chain**: N | **Referenced by syntheses**: 1
- **Latest analysis log**: `ANALYSIS-2026-031` (2026-02-01T05:33:59.448657Z) | fw=0.3.0 | meth=check-core@v0.3.0
- **TODOs**:
  - [ ] No validator issues detected (still review for substantive reanalysis under v0.3.0).

### lin-2026-jp-tl-bench-paper — JP-TL-Bench: Anchored Pairwise LLM Evaluation for Bidirectional Japanese-English Translation

- **Analysis**: [analysis/sources/lin-2026-jp-tl-bench-paper.md](analysis/sources/lin-2026-jp-tl-bench-paper.md)
- **Claims**: 7 (high-credence/E1-E2: 6) | **In chain**: N | **Referenced by syntheses**: 1
- **Latest analysis log**: _none_ (create a new pass when reanalyzing)
- **TODOs**:
  - [ ] Add missing sections: ### Internal Tensions, ### Persuasion Techniques, ### Unstated Assumptions, ### Claims to Register
  - [ ] Add `Claims to Register` YAML block (`claims:`)
  - [ ] Add `### Corrections & Updates` section (rigor-v1)
  - [ ] Upgrade Key Claims table to include Layer/Actor/Scope/Quantifier (rigor-v1)
  - [ ] Upgrade Claim Summary table to include Layer/Actor/Scope/Quantifier (rigor-v1)

### lee-2026-minnesota-trump-immigration-conflict — Minnesota standoff with Trump administration stokes fears of civil war

- **Analysis**: [analysis/sources/lee-2026-minnesota-trump-immigration-conflict.md](analysis/sources/lee-2026-minnesota-trump-immigration-conflict.md)
- **Claims**: 8 (high-credence/E1-E2: 4) | **In chain**: N | **Referenced by syntheses**: 1
- **Latest analysis log**: `ANALYSIS-2026-029` (2026-02-01T03:56:15.313725Z) | fw=0.2.0 | meth=analysis-core@v0.2.0
- **TODOs**:
  - [ ] No validator issues detected (still review for substantive reanalysis under v0.3.0).

### claude-2026-deepresearch-pla-purge-taiwan-calculus — China's January 2026 military purge reshapes Taiwan calculus

- **Analysis**: [analysis/sources/claude-2026-deepresearch-pla-purge-taiwan-calculus.md](analysis/sources/claude-2026-deepresearch-pla-purge-taiwan-calculus.md)
- **Claims**: 7 (high-credence/E1-E2: 4) | **In chain**: N | **Referenced by syntheses**: 1
- **Latest analysis log**: `ANALYSIS-2026-022` (2026-01-26T14:22:06.508000Z) | fw=0.1.8 | meth=check-core@v0.1.8
- **TODOs**:
  - [ ] Add missing sections: ### Internal Tensions, ### Persuasion Techniques, ### Unstated Assumptions
  - [ ] Add `### Corrections & Updates` section (rigor-v1)
  - [ ] Upgrade Key Claims table to include Layer/Actor/Scope/Quantifier (rigor-v1)
  - [ ] Upgrade Claim Summary table to include Layer/Actor/Scope/Quantifier (rigor-v1)

### google-2026-translategemma-tech-report — TranslateGemma Technical Report

- **Analysis**: [analysis/sources/google-2026-translategemma-tech-report.md](analysis/sources/google-2026-translategemma-tech-report.md)
- **Claims**: 5 (high-credence/E1-E2: 5) | **In chain**: N | **Referenced by syntheses**: 1
- **Latest analysis log**: _none_ (create a new pass when reanalyzing)
- **TODOs**:
  - [ ] Add missing sections: ### Internal Tensions, ### Persuasion Techniques, ### Unstated Assumptions, ### Claims to Register
  - [ ] Add `Claims to Register` YAML block (`claims:`)
  - [ ] Add `### Corrections & Updates` section (rigor-v1)
  - [ ] Upgrade Key Claims table to include Layer/Actor/Scope/Quantifier (rigor-v1)
  - [ ] Upgrade Claim Summary table to include Layer/Actor/Scope/Quantifier (rigor-v1)

### lin-2026-jp-tl-bench-directional-analysis — JP-TL-Bench: Why Translation Direction Matters (JA↔︎EN)

- **Analysis**: [analysis/sources/lin-2026-jp-tl-bench-directional-analysis.md](analysis/sources/lin-2026-jp-tl-bench-directional-analysis.md)
- **Claims**: 5 (high-credence/E1-E2: 5) | **In chain**: N | **Referenced by syntheses**: 1
- **Latest analysis log**: _none_ (create a new pass when reanalyzing)
- **TODOs**:
  - [ ] Add missing sections: ### Internal Tensions, ### Persuasion Techniques, ### Unstated Assumptions, ### Claims to Register
  - [ ] Add `Claims to Register` YAML block (`claims:`)
  - [ ] Add `### Corrections & Updates` section (rigor-v1)
  - [ ] Upgrade Key Claims table to include Layer/Actor/Scope/Quantifier (rigor-v1)
  - [ ] Upgrade Claim Summary table to include Layer/Actor/Scope/Quantifier (rigor-v1)

### shisaai-2026-jp-tl-bench-repo — JP-TL-Bench (GitHub repository)

- **Analysis**: [analysis/sources/shisaai-2026-jp-tl-bench-repo.md](analysis/sources/shisaai-2026-jp-tl-bench-repo.md)
- **Claims**: 5 (high-credence/E1-E2: 4) | **In chain**: N | **Referenced by syntheses**: 1
- **Latest analysis log**: _none_ (create a new pass when reanalyzing)
- **TODOs**:
  - [ ] Add missing sections: ### Internal Tensions, ### Persuasion Techniques, ### Unstated Assumptions, ### Claims to Register
  - [ ] Add `Claims to Register` YAML block (`claims:`)
  - [ ] Add `### Corrections & Updates` section (rigor-v1)
  - [ ] Upgrade Key Claims table to include Layer/Actor/Scope/Quantifier (rigor-v1)
  - [ ] Upgrade Claim Summary table to include Layer/Actor/Scope/Quantifier (rigor-v1)

### vectifyai-2025-pageindex — PageIndex: Document Index for Vectorless, Reasoning-based RAG

- **Analysis**: [analysis/sources/vectifyai-2025-pageindex.md](analysis/sources/vectifyai-2025-pageindex.md)
- **Claims**: 5 (high-credence/E1-E2: 4) | **In chain**: N | **Referenced by syntheses**: 1
- **Latest analysis log**: _none_ (create a new pass when reanalyzing)
- **TODOs**:
  - [ ] Add missing sections: ### Internal Tensions, ### Persuasion Techniques, ### Unstated Assumptions, ### Supporting Theories, ### Contradicting Theories
  - [ ] Add `### Corrections & Updates` section (rigor-v1)
  - [ ] Upgrade Key Claims table to include Layer/Actor/Scope/Quantifier (rigor-v1)
  - [ ] Upgrade Claim Summary table to include Layer/Actor/Scope/Quantifier (rigor-v1)

### commondreams-2026-minneapolis-shooting-family — 'Please Get the Truth Out,' Alex Pretti's Parents Plead as Trump Officials Baselessly Smear Shooting Victim

- **Analysis**: [analysis/sources/commondreams-2026-minneapolis-shooting-family.md](analysis/sources/commondreams-2026-minneapolis-shooting-family.md)
- **Claims**: 9 (high-credence/E1-E2: 8) | **In chain**: N | **Referenced by syntheses**: 0
- **Latest analysis log**: `ANALYSIS-2026-008` (2026-01-26T05:27:20.421369Z) | fw=0.1.7 | meth=analysis-core@v0.1.7
- **TODOs**:
  - [ ] Add missing sections: ### Claim Summary, ### Claims to Register
  - [ ] Upgrade Key Claims table to include Layer/Actor/Scope/Quantifier (rigor-v1)
  - [ ] Upgrade Claim Summary table to include Layer/Actor/Scope/Quantifier (rigor-v1)

### economist-2026-xi-purge-senior-general — What Xi Jinping’s purge of China’s most senior general reveals

- **Analysis**: [analysis/sources/economist-2026-xi-purge-senior-general.md](analysis/sources/economist-2026-xi-purge-senior-general.md)
- **Claims**: 9 (high-credence/E1-E2: 2) | **In chain**: N | **Referenced by syntheses**: 1
- **Latest analysis log**: `ANALYSIS-2026-011` (2026-01-26T09:56:58.277000Z) | fw=0.1.8 | meth=check-core@v0.1.8
- **TODOs**:
  - [ ] Add missing sections: ### Internal Tensions, ### Persuasion Techniques, ### Unstated Assumptions, ### Supporting Theories, ### Contradicting Theories
  - [ ] Add `### Corrections & Updates` section (rigor-v1)
  - [ ] Upgrade Key Claims table to include Layer/Actor/Scope/Quantifier (rigor-v1)
  - [ ] Upgrade Claim Summary table to include Layer/Actor/Scope/Quantifier (rigor-v1)

### reuters-2026-taiwan-monitoring-pla-leadership — Taiwan monitoring 'abnormal' China military leadership changes after top general put under investigation

- **Analysis**: [analysis/sources/reuters-2026-taiwan-monitoring-pla-leadership.md](analysis/sources/reuters-2026-taiwan-monitoring-pla-leadership.md)
- **Claims**: 4 (high-credence/E1-E2: 3) | **In chain**: N | **Referenced by syntheses**: 1
- **Latest analysis log**: `ANALYSIS-2026-010` (2026-01-26T09:54:39.809000Z) | fw=0.1.8 | meth=check-core@v0.1.8
- **TODOs**:
  - [ ] Add missing sections: ### Internal Tensions, ### Persuasion Techniques, ### Unstated Assumptions, ### Supporting Theories, ### Contradicting Theories
  - [ ] Add `### Corrections & Updates` section (rigor-v1)
  - [ ] Upgrade Key Claims table to include Layer/Actor/Scope/Quantifier (rigor-v1)
  - [ ] Upgrade Claim Summary table to include Layer/Actor/Scope/Quantifier (rigor-v1)

### ap-2026-pla-purge-taiwan — How a purge of China’s military leadership could impact the army and the future of Taiwan

- **Analysis**: [analysis/sources/ap-2026-pla-purge-taiwan.md](analysis/sources/ap-2026-pla-purge-taiwan.md)
- **Claims**: 6 (high-credence/E1-E2: 2) | **In chain**: N | **Referenced by syntheses**: 1
- **Latest analysis log**: `ANALYSIS-2026-009` (2026-01-26T09:53:09.943000Z) | fw=0.1.8 | meth=check-core@v0.1.8
- **TODOs**:
  - [ ] Add missing sections: ### Internal Tensions, ### Persuasion Techniques, ### Unstated Assumptions
  - [ ] Add `### Corrections & Updates` section (rigor-v1)
  - [ ] Upgrade Key Claims table to include Layer/Actor/Scope/Quantifier (rigor-v1)
  - [ ] Upgrade Claim Summary table to include Layer/Actor/Scope/Quantifier (rigor-v1)

### lhl-2025-liquid-ai-hackathon-tokyo — Liquid AI Hackathon Tokyo (repo)

- **Analysis**: [analysis/sources/lhl-2025-liquid-ai-hackathon-tokyo.md](analysis/sources/lhl-2025-liquid-ai-hackathon-tokyo.md)
- **Claims**: 5 (high-credence/E1-E2: 3) | **In chain**: N | **Referenced by syntheses**: 1
- **Latest analysis log**: _none_ (create a new pass when reanalyzing)
- **TODOs**:
  - [ ] Add missing sections: ### Internal Tensions, ### Persuasion Techniques, ### Unstated Assumptions, ### Claims to Register
  - [ ] Add `Claims to Register` YAML block (`claims:`)
  - [ ] Add `### Corrections & Updates` section (rigor-v1)
  - [ ] Upgrade Key Claims table to include Layer/Actor/Scope/Quantifier (rigor-v1)
  - [ ] Upgrade Claim Summary table to include Layer/Actor/Scope/Quantifier (rigor-v1)

### lin-2025-shisa-v2 — Shisa V2

- **Analysis**: [analysis/sources/lin-2025-shisa-v2.md](analysis/sources/lin-2025-shisa-v2.md)
- **Claims**: 5 (high-credence/E1-E2: 3) | **In chain**: N | **Referenced by syntheses**: 1
- **Latest analysis log**: _none_ (create a new pass when reanalyzing)
- **TODOs**:
  - [ ] Add missing sections: ### Internal Tensions, ### Persuasion Techniques, ### Unstated Assumptions, ### Claims to Register
  - [ ] Add `Claims to Register` YAML block (`claims:`)
  - [ ] Add `### Corrections & Updates` section (rigor-v1)
  - [ ] Upgrade Key Claims table to include Layer/Actor/Scope/Quantifier (rigor-v1)
  - [ ] Upgrade Claim Summary table to include Layer/Actor/Scope/Quantifier (rigor-v1)

### carney-2026-davos-wef-speech — Mark Carney WEF Davos 2026 Speech: Middle Powers and the Rupture in Global Order

- **Analysis**: [analysis/sources/carney-2026-davos-wef-speech.md](analysis/sources/carney-2026-davos-wef-speech.md)
- **Claims**: 14 (high-credence/E1-E2: 7) | **In chain**: N | **Referenced by syntheses**: 0
- **Latest analysis log**: _none_ (create a new pass when reanalyzing)
- **TODOs**:
  - [ ] Add `### Corrections & Updates` section (rigor-v1)
  - [ ] Upgrade Key Claims table to include Layer/Actor/Scope/Quantifier (rigor-v1)
  - [ ] Upgrade Claim Summary table to include Layer/Actor/Scope/Quantifier (rigor-v1)

### liquidai-2025-lfm2-350m-enjp-mt — LFM2-350M-ENJP-MT (LiquidAI)

- **Analysis**: [analysis/sources/liquidai-2025-lfm2-350m-enjp-mt.md](analysis/sources/liquidai-2025-lfm2-350m-enjp-mt.md)
- **Claims**: 4 (high-credence/E1-E2: 3) | **In chain**: N | **Referenced by syntheses**: 1
- **Latest analysis log**: _none_ (create a new pass when reanalyzing)
- **TODOs**:
  - [ ] Add missing sections: ### Internal Tensions, ### Persuasion Techniques, ### Unstated Assumptions, ### Claims to Register
  - [ ] Add `Claims to Register` YAML block (`claims:`)
  - [ ] Add `### Corrections & Updates` section (rigor-v1)
  - [ ] Upgrade Key Claims table to include Layer/Actor/Scope/Quantifier (rigor-v1)
  - [ ] Upgrade Claim Summary table to include Layer/Actor/Scope/Quantifier (rigor-v1)

### nyt-2026-world-sees-america-tooze — How the World Sees America, With Adam Tooze

- **Analysis**: [analysis/sources/nyt-2026-world-sees-america-tooze.md](analysis/sources/nyt-2026-world-sees-america-tooze.md)
- **Claims**: 12 (high-credence/E1-E2: 6) | **In chain**: N | **Referenced by syntheses**: 0
- **Latest analysis log**: `ANALYSIS-2026-028` (2026-01-31T21:39:54.544626Z) | fw=0.2.0 | meth=check-core@v0.2.0
- **TODOs**:
  - [ ] Upgrade Claim Summary table to include Layer/Actor/Scope/Quantifier (rigor-v1)

### wikipedia-2026-us-intervention-venezuela — 2026 United States intervention in Venezuela - Wikipedia

- **Analysis**: [analysis/sources/wikipedia-2026-us-intervention-venezuela.md](analysis/sources/wikipedia-2026-us-intervention-venezuela.md)
- **Claims**: 2 (high-credence/E1-E2: 2) | **In chain**: N | **Referenced by syntheses**: 1
- **Latest analysis log**: `ANALYSIS-2026-023` (2026-01-26T14:23:15.067000Z) | fw=0.1.8 | meth=check-core@v0.1.8
- **TODOs**:
  - [ ] Add missing sections: ### Argument Structure, ### Theoretical Lineage, ### Key Factual Claims Verified, ### Disconfirming Evidence Search, ### Internal Tensions, ### Persuasion Techniques, ### Unstated Assumptions, ### Steelmanned Argument, ### Strongest Counterarguments, ### Supporting Theories, ### Contradicting Theories
  - [ ] Add `### Corrections & Updates` section (rigor-v1)
  - [ ] Upgrade Key Claims table to include Layer/Actor/Scope/Quantifier (rigor-v1)
  - [ ] Upgrade Claim Summary table to include Layer/Actor/Scope/Quantifier (rigor-v1)

### stross-2025-the-pivot-1 — The pivot (Part 1)

- **Analysis**: [analysis/sources/stross-2025-the-pivot-1.md](analysis/sources/stross-2025-the-pivot-1.md)
- **Claims**: 16 (high-credence/E1-E2: 0) | **In chain**: N | **Referenced by syntheses**: 1
- **Latest analysis log**: _none_ (create a new pass when reanalyzing)
- **TODOs**:
  - [ ] Add `### Corrections & Updates` section (rigor-v1)
  - [ ] Upgrade Key Claims table to include Layer/Actor/Scope/Quantifier (rigor-v1)
  - [ ] Upgrade Claim Summary table to include Layer/Actor/Scope/Quantifier (rigor-v1)

### bluebadger2600-2026-ice-positions — X post: “Positions ICE has taken”

- **Analysis**: [analysis/sources/bluebadger2600-2026-ice-positions.md](analysis/sources/bluebadger2600-2026-ice-positions.md)
- **Claims**: 10 (high-credence/E1-E2: 6) | **In chain**: N | **Referenced by syntheses**: 0
- **Latest analysis log**: `ANALYSIS-2026-007` (2026-01-25T13:19:32.935000Z) | fw=0.1.4 | meth=check-core@v0.1.4
- **TODOs**:
  - [ ] Add missing sections: ### Internal Tensions, ### Supporting Theories, ### Contradicting Theories
  - [ ] Add `### Corrections & Updates` section (rigor-v1)
  - [ ] Upgrade Key Claims table to include Layer/Actor/Scope/Quantifier (rigor-v1)
  - [ ] Upgrade Claim Summary table to include Layer/Actor/Scope/Quantifier (rigor-v1)

### lin-2025-jp-tl-bench — JP-TL-Bench: Anchored Pairwise LLM Evaluation for Bidirectional Japanese-English Translation

- **Analysis**: [analysis/sources/lin-2025-jp-tl-bench.md](analysis/sources/lin-2025-jp-tl-bench.md)
- **Claims**: 5 (high-credence/E1-E2: 2) | **In chain**: N | **Referenced by syntheses**: 1
- **Latest analysis log**: _none_ (create a new pass when reanalyzing)
- **TODOs**:
  - [ ] Add missing sections: ### Internal Tensions, ### Persuasion Techniques, ### Unstated Assumptions, ### Claims to Register
  - [ ] Add `Claims to Register` YAML block (`claims:`)
  - [ ] Add `### Corrections & Updates` section (rigor-v1)
  - [ ] Upgrade Key Claims table to include Layer/Actor/Scope/Quantifier (rigor-v1)
  - [ ] Upgrade Claim Summary table to include Layer/Actor/Scope/Quantifier (rigor-v1)

### lin-2025-shisa-v2-405b — Shisa V2 405B: Japan’s Highest Performing LLM

- **Analysis**: [analysis/sources/lin-2025-shisa-v2-405b.md](analysis/sources/lin-2025-shisa-v2-405b.md)
- **Claims**: 5 (high-credence/E1-E2: 2) | **In chain**: N | **Referenced by syntheses**: 1
- **Latest analysis log**: _none_ (create a new pass when reanalyzing)
- **TODOs**:
  - [ ] Add missing sections: ### Internal Tensions, ### Persuasion Techniques, ### Unstated Assumptions, ### Claims to Register
  - [ ] Add `Claims to Register` YAML block (`claims:`)
  - [ ] Add `### Corrections & Updates` section (rigor-v1)
  - [ ] Upgrade Key Claims table to include Layer/Actor/Scope/Quantifier (rigor-v1)
  - [ ] Upgrade Claim Summary table to include Layer/Actor/Scope/Quantifier (rigor-v1)

### nyt-2026-xi-purge-top-general-down — Xi’s Purge of China’s Military Brings Its Top General Down

- **Analysis**: [analysis/sources/nyt-2026-xi-purge-top-general-down.md](analysis/sources/nyt-2026-xi-purge-top-general-down.md)
- **Claims**: 5 (high-credence/E1-E2: 1) | **In chain**: N | **Referenced by syntheses**: 1
- **Latest analysis log**: `ANALYSIS-2026-014` (2026-01-26T10:01:15.839000Z) | fw=0.1.8 | meth=check-core@v0.1.8
- **TODOs**:
  - [ ] Add missing sections: ### Internal Tensions, ### Persuasion Techniques, ### Unstated Assumptions, ### Supporting Theories, ### Contradicting Theories
  - [ ] Add `### Corrections & Updates` section (rigor-v1)
  - [ ] Upgrade Key Claims table to include Layer/Actor/Scope/Quantifier (rigor-v1)
  - [ ] Upgrade Claim Summary table to include Layer/Actor/Scope/Quantifier (rigor-v1)

### perera-2026-chinas-trillion-dollar-illusion — China’s Trillion-Dollar Illusion

- **Analysis**: [analysis/sources/perera-2026-chinas-trillion-dollar-illusion.md](analysis/sources/perera-2026-chinas-trillion-dollar-illusion.md)
- **Claims**: 10 (high-credence/E1-E2: 7) | **In chain**: N | **Referenced by syntheses**: 0
- **Latest analysis log**: _none_ (create a new pass when reanalyzing)
- **TODOs**:
  - [ ] Add `### Corrections & Updates` section (rigor-v1)
  - [ ] Upgrade Key Claims table to include Layer/Actor/Scope/Quantifier (rigor-v1)
  - [ ] Upgrade Claim Summary table to include Layer/Actor/Scope/Quantifier (rigor-v1)

### wsj-2026-chinese-spy-machine-taiwan-military — The Chinese Spy Machine Infiltrating Taiwan’s Military

- **Analysis**: [analysis/sources/wsj-2026-chinese-spy-machine-taiwan-military.md](analysis/sources/wsj-2026-chinese-spy-machine-taiwan-military.md)
- **Claims**: 5 (high-credence/E1-E2: 1) | **In chain**: N | **Referenced by syntheses**: 1
- **Latest analysis log**: `ANALYSIS-2026-018` (2026-01-26T10:07:41.015000Z) | fw=0.1.8 | meth=check-core@v0.1.8
- **TODOs**:
  - [ ] Add missing sections: ### Internal Tensions, ### Persuasion Techniques, ### Unstated Assumptions, ### Supporting Theories, ### Contradicting Theories
  - [ ] Add `### Corrections & Updates` section (rigor-v1)
  - [ ] Upgrade Key Claims table to include Layer/Actor/Scope/Quantifier (rigor-v1)
  - [ ] Upgrade Claim Summary table to include Layer/Actor/Scope/Quantifier (rigor-v1)

### sinocism-2026-pla-purges-intensify-zhang-liu — PLA purges intensify: Zhang Youxia and Liu Zhenli under investigation

- **Analysis**: [analysis/sources/sinocism-2026-pla-purges-intensify-zhang-liu.md](analysis/sources/sinocism-2026-pla-purges-intensify-zhang-liu.md)
- **Claims**: 4 (high-credence/E1-E2: 1) | **In chain**: N | **Referenced by syntheses**: 1
- **Latest analysis log**: `ANALYSIS-2026-019` (2026-01-26T10:08:58.744000Z) | fw=0.1.8 | meth=check-core@v0.1.8
- **TODOs**:
  - [ ] Add missing sections: ### Internal Tensions, ### Persuasion Techniques, ### Unstated Assumptions, ### Supporting Theories, ### Contradicting Theories
  - [ ] Add `### Corrections & Updates` section (rigor-v1)
  - [ ] Upgrade Key Claims table to include Layer/Actor/Scope/Quantifier (rigor-v1)
  - [ ] Upgrade Claim Summary table to include Layer/Actor/Scope/Quantifier (rigor-v1)

### google-2026-translategemma-blog — TranslateGemma: A new suite of open translation models

- **Analysis**: [analysis/sources/google-2026-translategemma-blog.md](analysis/sources/google-2026-translategemma-blog.md)
- **Claims**: 3 (high-credence/E1-E2: 2) | **In chain**: N | **Referenced by syntheses**: 1
- **Latest analysis log**: _none_ (create a new pass when reanalyzing)
- **TODOs**:
  - [ ] Add missing sections: ### Internal Tensions, ### Persuasion Techniques, ### Unstated Assumptions, ### Claims to Register
  - [ ] Add `Claims to Register` YAML block (`claims:`)
  - [ ] Add `### Corrections & Updates` section (rigor-v1)
  - [ ] Upgrade Key Claims table to include Layer/Actor/Scope/Quantifier (rigor-v1)
  - [ ] Upgrade Claim Summary table to include Layer/Actor/Scope/Quantifier (rigor-v1)

### kamathhrishi-2025-stratalens-ai — StrataLens AI (open source equity research platform)

- **Analysis**: [analysis/sources/kamathhrishi-2025-stratalens-ai.md](analysis/sources/kamathhrishi-2025-stratalens-ai.md)
- **Claims**: 3 (high-credence/E1-E2: 2) | **In chain**: N | **Referenced by syntheses**: 1
- **Latest analysis log**: _none_ (create a new pass when reanalyzing)
- **TODOs**:
  - [ ] Add missing sections: ### Internal Tensions, ### Persuasion Techniques, ### Unstated Assumptions, ### Supporting Theories, ### Contradicting Theories
  - [ ] Add `### Corrections & Updates` section (rigor-v1)
  - [ ] Upgrade Key Claims table to include Layer/Actor/Scope/Quantifier (rigor-v1)
  - [ ] Upgrade Claim Summary table to include Layer/Actor/Scope/Quantifier (rigor-v1)

### skynews-2026-xi-purge-power-control — Xi's purge of top general paints a fascinating picture of power and control within a ruthless and unforgiving system

- **Analysis**: [analysis/sources/skynews-2026-xi-purge-power-control.md](analysis/sources/skynews-2026-xi-purge-power-control.md)
- **Claims**: 3 (high-credence/E1-E2: 1) | **In chain**: N | **Referenced by syntheses**: 1
- **Latest analysis log**: `ANALYSIS-2026-015` (2026-01-26T10:02:23.447000Z) | fw=0.1.8 | meth=check-core@v0.1.8
- **TODOs**:
  - [ ] Add missing sections: ### Internal Tensions, ### Persuasion Techniques, ### Unstated Assumptions, ### Supporting Theories, ### Contradicting Theories
  - [ ] Add `### Corrections & Updates` section (rigor-v1)
  - [ ] Upgrade Key Claims table to include Layer/Actor/Scope/Quantifier (rigor-v1)
  - [ ] Upgrade Claim Summary table to include Layer/Actor/Scope/Quantifier (rigor-v1)

### vectifyai-2025-mafin25-financebench — Mafin2.5-FinanceBench (published evaluation results)

- **Analysis**: [analysis/sources/vectifyai-2025-mafin25-financebench.md](analysis/sources/vectifyai-2025-mafin25-financebench.md)
- **Claims**: 3 (high-credence/E1-E2: 2) | **In chain**: N | **Referenced by syntheses**: 1
- **Latest analysis log**: _none_ (create a new pass when reanalyzing)
- **TODOs**:
  - [ ] Add missing sections: ### Theoretical Lineage, ### Internal Tensions, ### Persuasion Techniques, ### Unstated Assumptions, ### Supporting Theories, ### Contradicting Theories
  - [ ] Add `### Corrections & Updates` section (rigor-v1)
  - [ ] Upgrade Key Claims table to include Layer/Actor/Scope/Quantifier (rigor-v1)
  - [ ] Upgrade Claim Summary table to include Layer/Actor/Scope/Quantifier (rigor-v1)

### islam-2023-financebench — FinanceBench: A New Benchmark for Financial Question Answering

- **Analysis**: [analysis/sources/islam-2023-financebench.md](analysis/sources/islam-2023-financebench.md)
- **Claims**: 2 (high-credence/E1-E2: 2) | **In chain**: N | **Referenced by syntheses**: 1
- **Latest analysis log**: _none_ (create a new pass when reanalyzing)
- **TODOs**:
  - [ ] Add missing sections: ### Internal Tensions, ### Persuasion Techniques, ### Unstated Assumptions, ### Supporting Theories, ### Contradicting Theories
  - [ ] Add `Claims to Register` YAML block (`claims:`)
  - [ ] Add `### Corrections & Updates` section (rigor-v1)
  - [ ] Upgrade Key Claims table to include Layer/Actor/Scope/Quantifier (rigor-v1)
  - [ ] Upgrade Claim Summary table to include Layer/Actor/Scope/Quantifier (rigor-v1)

### x-2026-zhang-purge-hot-takes — Hot takes/threads on Zhang Youxia purge, “treason” narratives, and Taiwan timing (X/Twitter compilation)

- **Analysis**: [analysis/sources/x-2026-zhang-purge-hot-takes.md](analysis/sources/x-2026-zhang-purge-hot-takes.md)
- **Claims**: 7 (high-credence/E1-E2: 0) | **In chain**: N | **Referenced by syntheses**: 1
- **Latest analysis log**: `ANALYSIS-2026-020` (2026-01-26T10:10:46.975000Z) | fw=0.1.8 | meth=check-core@v0.1.8
- **TODOs**:
  - [ ] Add missing sections: ### Internal Tensions, ### Persuasion Techniques, ### Unstated Assumptions, ### Supporting Theories, ### Contradicting Theories
  - [ ] Add `### Corrections & Updates` section (rigor-v1)
  - [ ] Upgrade Key Claims table to include Layer/Actor/Scope/Quantifier (rigor-v1)
  - [ ] Upgrade Claim Summary table to include Layer/Actor/Scope/Quantifier (rigor-v1)

### janes-2025-air-sea-operations-around-taiwan — Special Report: China sets new records in air-sea operations around Taiwan

- **Analysis**: [analysis/sources/janes-2025-air-sea-operations-around-taiwan.md](analysis/sources/janes-2025-air-sea-operations-around-taiwan.md)
- **Claims**: 1 (high-credence/E1-E2: 1) | **In chain**: N | **Referenced by syntheses**: 1
- **Latest analysis log**: `ANALYSIS-2026-026` (2026-01-30T19:31:19.953823Z) | fw=0.2.0 | meth=check-core@v0.2.0
- **TODOs**:
  - [ ] Add missing sections: ### Internal Tensions, ### Persuasion Techniques, ### Unstated Assumptions, ### Supporting Theories, ### Contradicting Theories
  - [ ] Add `### Corrections & Updates` section (rigor-v1)
  - [ ] Upgrade Key Claims table to include Layer/Actor/Scope/Quantifier (rigor-v1)
  - [ ] Upgrade Claim Summary table to include Layer/Actor/Scope/Quantifier (rigor-v1)

### wsj-2026-top-general-nuclear-secrets — China’s Top General Accused of Giving Nuclear Secrets to U.S.

- **Analysis**: [analysis/sources/wsj-2026-top-general-nuclear-secrets.md](analysis/sources/wsj-2026-top-general-nuclear-secrets.md)
- **Claims**: 6 (high-credence/E1-E2: 0) | **In chain**: N | **Referenced by syntheses**: 1
- **Latest analysis log**: `ANALYSIS-2026-017` (2026-01-26T10:05:19.725000Z) | fw=0.1.8 | meth=check-core@v0.1.8
- **TODOs**:
  - [ ] Add missing sections: ### Internal Tensions, ### Persuasion Techniques, ### Unstated Assumptions, ### Supporting Theories, ### Contradicting Theories
  - [ ] Add `### Corrections & Updates` section (rigor-v1)
  - [ ] Upgrade Key Claims table to include Layer/Actor/Scope/Quantifier (rigor-v1)
  - [ ] Upgrade Claim Summary table to include Layer/Actor/Scope/Quantifier (rigor-v1)

### bloomberg-2026-purge-top-general-taiwan-succession — Xi’s Purge of Top General Spurs Questions on Taiwan, Succession

- **Analysis**: [analysis/sources/bloomberg-2026-purge-top-general-taiwan-succession.md](analysis/sources/bloomberg-2026-purge-top-general-taiwan-succession.md)
- **Claims**: 5 (high-credence/E1-E2: 0) | **In chain**: N | **Referenced by syntheses**: 1
- **Latest analysis log**: `ANALYSIS-2026-012` (2026-01-26T09:58:30.460000Z) | fw=0.1.8 | meth=check-core@v0.1.8
- **TODOs**:
  - [ ] Add missing sections: ### Internal Tensions, ### Persuasion Techniques, ### Unstated Assumptions, ### Supporting Theories, ### Contradicting Theories
  - [ ] Add `### Corrections & Updates` section (rigor-v1)
  - [ ] Upgrade Key Claims table to include Layer/Actor/Scope/Quantifier (rigor-v1)
  - [ ] Upgrade Claim Summary table to include Layer/Actor/Scope/Quantifier (rigor-v1)

### shisaai-2025-shisa-v2-1 — Shisa V2.1: Smaller, Smarter, More Accessible

- **Analysis**: [analysis/sources/shisaai-2025-shisa-v2-1.md](analysis/sources/shisaai-2025-shisa-v2-1.md)
- **Claims**: 5 (high-credence/E1-E2: 1) | **In chain**: N | **Referenced by syntheses**: 1
- **Latest analysis log**: _none_ (create a new pass when reanalyzing)
- **TODOs**:
  - [ ] Add missing sections: ### Internal Tensions, ### Persuasion Techniques, ### Unstated Assumptions, ### Claims to Register
  - [ ] Add `Claims to Register` YAML block (`claims:`)
  - [ ] Add `### Corrections & Updates` section (rigor-v1)
  - [ ] Upgrade Key Claims table to include Layer/Actor/Scope/Quantifier (rigor-v1)
  - [ ] Upgrade Claim Summary table to include Layer/Actor/Scope/Quantifier (rigor-v1)

### ft-2026-xi-sole-operational-control-pla — Xi takes sole operational control of army as China probes military leaders

- **Analysis**: [analysis/sources/ft-2026-xi-sole-operational-control-pla.md](analysis/sources/ft-2026-xi-sole-operational-control-pla.md)
- **Claims**: 4 (high-credence/E1-E2: 0) | **In chain**: N | **Referenced by syntheses**: 1
- **Latest analysis log**: `ANALYSIS-2026-013` (2026-01-26T09:59:46.393000Z) | fw=0.1.8 | meth=check-core@v0.1.8
- **TODOs**:
  - [ ] Add missing sections: ### Internal Tensions, ### Persuasion Techniques, ### Unstated Assumptions, ### Supporting Theories, ### Contradicting Theories
  - [ ] Add `### Corrections & Updates` section (rigor-v1)
  - [ ] Upgrade Key Claims table to include Layer/Actor/Scope/Quantifier (rigor-v1)
  - [ ] Upgrade Claim Summary table to include Layer/Actor/Scope/Quantifier (rigor-v1)

### telegraph-2026-xi-purge-total-control-pla — Military purge gives Xi total control of Chinese army

- **Analysis**: [analysis/sources/telegraph-2026-xi-purge-total-control-pla.md](analysis/sources/telegraph-2026-xi-purge-total-control-pla.md)
- **Claims**: 4 (high-credence/E1-E2: 0) | **In chain**: N | **Referenced by syntheses**: 1
- **Latest analysis log**: `ANALYSIS-2026-016` (2026-01-26T10:03:39.332000Z) | fw=0.1.8 | meth=check-core@v0.1.8
- **TODOs**:
  - [ ] Add missing sections: ### Internal Tensions, ### Persuasion Techniques, ### Unstated Assumptions, ### Supporting Theories, ### Contradicting Theories
  - [ ] Add `### Corrections & Updates` section (rigor-v1)
  - [ ] Upgrade Key Claims table to include Layer/Actor/Scope/Quantifier (rigor-v1)
  - [ ] Upgrade Claim Summary table to include Layer/Actor/Scope/Quantifier (rigor-v1)

### jamestown-2025-pla-aircraft-incursions-taiwan-airspace-2024 — Military Implications of PLA Aircraft Incursions in Taiwan’s Airspace 2024

- **Analysis**: [analysis/sources/jamestown-2025-pla-aircraft-incursions-taiwan-airspace-2024.md](analysis/sources/jamestown-2025-pla-aircraft-incursions-taiwan-airspace-2024.md)
- **Claims**: 1 (high-credence/E1-E2: 1) | **In chain**: N | **Referenced by syntheses**: 1
- **Latest analysis log**: _none_ (create a new pass when reanalyzing)
- **TODOs**:
  - [ ] Add missing sections: ### Internal Tensions, ### Persuasion Techniques, ### Unstated Assumptions, ### Supporting Theories, ### Contradicting Theories
  - [ ] Add `### Corrections & Updates` section (rigor-v1)
  - [ ] Upgrade Key Claims table to include Layer/Actor/Scope/Quantifier (rigor-v1)
  - [ ] Upgrade Claim Summary table to include Layer/Actor/Scope/Quantifier (rigor-v1)

### moeaea-2024-stable-supply-natural-gas — Stable Supply of Natural Gas

- **Analysis**: [analysis/sources/moeaea-2024-stable-supply-natural-gas.md](analysis/sources/moeaea-2024-stable-supply-natural-gas.md)
- **Claims**: 1 (high-credence/E1-E2: 1) | **In chain**: N | **Referenced by syntheses**: 1
- **Latest analysis log**: _none_ (create a new pass when reanalyzing)
- **TODOs**:
  - [ ] Add missing sections: ### Internal Tensions, ### Persuasion Techniques, ### Unstated Assumptions, ### Supporting Theories, ### Contradicting Theories
  - [ ] Add `### Corrections & Updates` section (rigor-v1)
  - [ ] Upgrade Key Claims table to include Layer/Actor/Scope/Quantifier (rigor-v1)
  - [ ] Upgrade Claim Summary table to include Layer/Actor/Scope/Quantifier (rigor-v1)

### taipeitimes-2022-energy-supplies-sufficient-ministry — Energy supplies sufficient, ministry says

- **Analysis**: [analysis/sources/taipeitimes-2022-energy-supplies-sufficient-ministry.md](analysis/sources/taipeitimes-2022-energy-supplies-sufficient-ministry.md)
- **Claims**: 1 (high-credence/E1-E2: 1) | **In chain**: N | **Referenced by syntheses**: 1
- **Latest analysis log**: _none_ (create a new pass when reanalyzing)
- **TODOs**:
  - [ ] Add missing sections: ### Internal Tensions, ### Persuasion Techniques, ### Unstated Assumptions, ### Supporting Theories, ### Contradicting Theories
  - [ ] Add `### Corrections & Updates` section (rigor-v1)
  - [ ] Upgrade Key Claims table to include Layer/Actor/Scope/Quantifier (rigor-v1)
  - [ ] Upgrade Claim Summary table to include Layer/Actor/Scope/Quantifier (rigor-v1)

### avichawla-2026-pageindex-thread — Thread: PageIndex (vectorless, reasoning-based RAG)

- **Analysis**: [analysis/sources/avichawla-2026-pageindex-thread.md](analysis/sources/avichawla-2026-pageindex-thread.md)
- **Claims**: 3 (high-credence/E1-E2: 0) | **In chain**: N | **Referenced by syntheses**: 1
- **Latest analysis log**: _none_ (create a new pass when reanalyzing)
- **TODOs**:
  - [ ] Add missing sections: ### Internal Tensions, ### Persuasion Techniques, ### Unstated Assumptions, ### Supporting Theories, ### Contradicting Theories
  - [ ] Add `### Corrections & Updates` section (rigor-v1)
  - [ ] Upgrade Key Claims table to include Layer/Actor/Scope/Quantifier (rigor-v1)
  - [ ] Upgrade Claim Summary table to include Layer/Actor/Scope/Quantifier (rigor-v1)

### rawstory-2026-trump-voters-suicide-pact — These Trump voters 'formed a suicide pact' and Republicans are panicking: ex-GOP operative

- **Analysis**: [analysis/sources/rawstory-2026-trump-voters-suicide-pact.md](analysis/sources/rawstory-2026-trump-voters-suicide-pact.md)
- **Claims**: 9 (high-credence/E1-E2: 3) | **In chain**: N | **Referenced by syntheses**: 0
- **Latest analysis log**: `ANALYSIS-2026-025` (2026-01-30T19:08:48.864000Z) | fw=0.1.9 | meth=check-core@v0.1.9
- **TODOs**:
  - [ ] Add `### Corrections & Updates` section (rigor-v1)
  - [ ] Upgrade Key Claims table to include Layer/Actor/Scope/Quantifier (rigor-v1)
  - [ ] Upgrade Claim Summary table to include Layer/Actor/Scope/Quantifier (rigor-v1)

### doctorow-2026-reverse-centaur — AI companies will fail. We can salvage something from the wreckage

- **Analysis**: [analysis/sources/doctorow-2026-reverse-centaur.md](analysis/sources/doctorow-2026-reverse-centaur.md)
- **Claims**: 9 (high-credence/E1-E2: 3) | **In chain**: N | **Referenced by syntheses**: 0
- **Latest analysis log**: _none_ (create a new pass when reanalyzing)
- **TODOs**:
  - [ ] Add `### Corrections & Updates` section (rigor-v1)
  - [ ] Upgrade Key Claims table to include Layer/Actor/Scope/Quantifier (rigor-v1)
  - [ ] Upgrade Claim Summary table to include Layer/Actor/Scope/Quantifier (rigor-v1)

### reason-2026-dhs-retreats-violent-riot-pretti — DHS retreats from the claim that the agents who killed Alex Pretti faced a 'violent riot'

- **Analysis**: [analysis/sources/reason-2026-dhs-retreats-violent-riot-pretti.md](analysis/sources/reason-2026-dhs-retreats-violent-riot-pretti.md)
- **Claims**: 4 (high-credence/E1-E2: 3) | **In chain**: N | **Referenced by syntheses**: 0
- **Latest analysis log**: `ANALYSIS-2026-027` (2026-01-31T00:10:09.834317Z) | fw=0.2.0 | meth=check-core@v0.2.0
- **TODOs**:
  - [ ] Add `### Corrections & Updates` section (rigor-v1)
  - [ ] Upgrade Key Claims table to include Layer/Actor/Scope/Quantifier (rigor-v1)
  - [ ] Upgrade Claim Summary table to include Layer/Actor/Scope/Quantifier (rigor-v1)

### jre-2404-elon-musk-2025-ai-woke-mind-virus — Joe Rogan Experience #2404 — Elon Musk (AI alignment, Gemini “ImageGen”, “woke mind virus”)

- **Analysis**: [analysis/sources/jre-2404-elon-musk-2025-ai-woke-mind-virus.md](analysis/sources/jre-2404-elon-musk-2025-ai-woke-mind-virus.md)
- **Claims**: 12 (high-credence/E1-E2: 2) | **In chain**: N | **Referenced by syntheses**: 0
- **Latest analysis log**: _none_ (create a new pass when reanalyzing)
- **TODOs**:
  - [ ] Add `### Corrections & Updates` section (rigor-v1)
  - [ ] Upgrade Key Claims table to include Layer/Actor/Scope/Quantifier (rigor-v1)
  - [ ] Upgrade Claim Summary table to include Layer/Actor/Scope/Quantifier (rigor-v1)

### openai-value-intelligence — A business that scales with the value of intelligence

- **Analysis**: [analysis/sources/openai-value-intelligence.md](analysis/sources/openai-value-intelligence.md)
- **Claims**: 11 (high-credence/E1-E2: 2) | **In chain**: N | **Referenced by syntheses**: 0
- **Latest analysis log**: _none_ (create a new pass when reanalyzing)
- **TODOs**:
  - [ ] Add `### Corrections & Updates` section (rigor-v1)
  - [ ] Upgrade Key Claims table to include Layer/Actor/Scope/Quantifier (rigor-v1)
  - [ ] Upgrade Claim Summary table to include Layer/Actor/Scope/Quantifier (rigor-v1)

### appleton-2026-gastown-agent-patterns — Gas Town’s Agent Patterns, Design Bottlenecks, and Vibecoding at Scale

- **Analysis**: [analysis/sources/appleton-2026-gastown-agent-patterns.md](analysis/sources/appleton-2026-gastown-agent-patterns.md)
- **Claims**: 7 (high-credence/E1-E2: 0) | **In chain**: N | **Referenced by syntheses**: 0
- **Latest analysis log**: `ANALYSIS-2026-002` (2026-01-24T07:42:07.276000Z) | fw=0.1.3 | meth=check-core@v0.1.3
- **TODOs**:
  - [ ] Add `### Corrections & Updates` section (rigor-v1)
  - [ ] Upgrade Key Claims table to include Layer/Actor/Scope/Quantifier (rigor-v1)
  - [ ] Upgrade Claim Summary table to include Layer/Actor/Scope/Quantifier (rigor-v1)

### chatterjee-2024-anz-copilot-study — The Impact of AI Tool on Engineering at ANZ Bank: An Empirical Study on GitHub Copilot within Corporate Environment

- **Analysis**: [analysis/sources/chatterjee-2024-anz-copilot-study.md](analysis/sources/chatterjee-2024-anz-copilot-study.md)
- **Claims**: 2 (high-credence/E1-E2: 2) | **In chain**: N | **Referenced by syntheses**: 0
- **Latest analysis log**: _none_ (create a new pass when reanalyzing)
- **TODOs**:
  - [ ] Add `### Corrections & Updates` section (rigor-v1)
  - [ ] Upgrade Key Claims table to include Layer/Actor/Scope/Quantifier (rigor-v1)
  - [ ] Upgrade Claim Summary table to include Layer/Actor/Scope/Quantifier (rigor-v1)

### peng-2023-copilot-productivity — The Impact of AI on Developer Productivity: Evidence from GitHub Copilot

- **Analysis**: [analysis/sources/peng-2023-copilot-productivity.md](analysis/sources/peng-2023-copilot-productivity.md)
- **Claims**: 2 (high-credence/E1-E2: 2) | **In chain**: N | **Referenced by syntheses**: 0
- **Latest analysis log**: _none_ (create a new pass when reanalyzing)
- **TODOs**:
  - [ ] Add `### Corrections & Updates` section (rigor-v1)
  - [ ] Upgrade Key Claims table to include Layer/Actor/Scope/Quantifier (rigor-v1)
  - [ ] Upgrade Claim Summary table to include Layer/Actor/Scope/Quantifier (rigor-v1)

### uscourts-mnd-2025-04669-doc109-doctor-declaration — Declaration of an unnamed physician (Doc. 109, D. Minn. 0:25-cv-04669-KMM-DTS)

- **Analysis**: [analysis/sources/uscourts-mnd-2025-04669-doc109-doctor-declaration.md](analysis/sources/uscourts-mnd-2025-04669-doc109-doctor-declaration.md)
- **Claims**: 2 (high-credence/E1-E2: 2) | **In chain**: N | **Referenced by syntheses**: 0
- **Latest analysis log**: _none_ (create a new pass when reanalyzing)
- **TODOs**:
  - [ ] Add missing sections: ### Argument Structure, ### Theoretical Lineage, ### Key Factual Claims Verified, ### Internal Tensions, ### Persuasion Techniques, ### Unstated Assumptions, ### Supporting Theories, ### Contradicting Theories, ### Claims to Register
  - [ ] Add `Claims to Register` YAML block (`claims:`)
  - [ ] Add `### Corrections & Updates` section (rigor-v1)
  - [ ] Upgrade Key Claims table to include Layer/Actor/Scope/Quantifier (rigor-v1)
  - [ ] Upgrade Claim Summary table to include Layer/Actor/Scope/Quantifier (rigor-v1)

### teortaxes-2026-greenland-endgame — Greenland/resource extraction + 'light cone' endgame post

- **Analysis**: [analysis/sources/teortaxes-2026-greenland-endgame.md](analysis/sources/teortaxes-2026-greenland-endgame.md)
- **Claims**: 8 (high-credence/E1-E2: 0) | **In chain**: N | **Referenced by syntheses**: 0
- **Latest analysis log**: _none_ (create a new pass when reanalyzing)
- **TODOs**:
  - [ ] Add `### Corrections & Updates` section (rigor-v1)
  - [ ] Upgrade Key Claims table to include Layer/Actor/Scope/Quantifier (rigor-v1)
  - [ ] Upgrade Claim Summary table to include Layer/Actor/Scope/Quantifier (rigor-v1)

## Syntheses (After Sources)

Total: **7** syntheses (`analysis/syntheses/*.md`).

General rule: update syntheses after the underlying source analyses they depend on have been upgraded.


### china-pla-purge-zhang-youxia-taiwan-synthesis

- **Synthesis**: [analysis/syntheses/china-pla-purge-zhang-youxia-taiwan-synthesis.md](analysis/syntheses/china-pla-purge-zhang-youxia-taiwan-synthesis.md)
- **Inputs (declared)**: `ap-2026-pla-purge-taiwan`, `bloomberg-2026-purge-top-general-taiwan-succession`, `claude-2026-deepresearch-pla-purge-taiwan-calculus`, `economist-2026-xi-purge-senior-general`, `ft-2026-xi-sole-operational-control-pla`, `jamestown-2025-pla-aircraft-incursions-taiwan-airspace-2024`, `janes-2025-air-sea-operations-around-taiwan`, `moeaea-2024-stable-supply-natural-gas`, `nyt-2026-xi-purge-top-general-down`, `reuters-2026-taiwan-monitoring-pla-leadership`, `sinocism-2026-pla-purges-intensify-zhang-liu`, `skynews-2026-xi-purge-power-control`, `taipeitimes-2022-energy-supplies-sufficient-ministry`, `telegraph-2026-xi-purge-total-control-pla`, `wikipedia-2026-us-intervention-venezuela`, `wsj-2026-chinese-spy-machine-taiwan-military`, `wsj-2026-top-general-nuclear-secrets`, `x-2026-zhang-purge-hot-takes`
- **TODOs**:
  - [ ] Revisit synthesis once input sources are upgraded to rigor-v1
  - [ ] Ensure synthesis cites updated claim IDs and reflects any credence/evidence changes

### jp-tl-bench-ja-en-translation-eval-synthesis

- **Synthesis**: [analysis/syntheses/jp-tl-bench-ja-en-translation-eval-synthesis.md](analysis/syntheses/jp-tl-bench-ja-en-translation-eval-synthesis.md)
- **Inputs (declared)**: `google-2026-translategemma-blog`, `google-2026-translategemma-tech-report`, `lhl-2025-liquid-ai-hackathon-tokyo`, `lin-2025-jp-tl-bench`, `lin-2025-shisa-v2`, `lin-2025-shisa-v2-405b`, `lin-2026-jp-tl-bench-directional-analysis`, `lin-2026-jp-tl-bench-paper`, `liquidai-2025-lfm2-350m-enjp-mt`, `shisaai-2025-shisa-v2-1`, `shisaai-2026-jp-tl-bench-repo`
- **TODOs**:
  - [ ] Revisit synthesis once input sources are upgraded to rigor-v1
  - [ ] Ensure synthesis cites updated claim IDs and reflects any credence/evidence changes

### neofeudalism-discourse-synthesis

- **Synthesis**: [analysis/syntheses/neofeudalism-discourse-synthesis.md](analysis/syntheses/neofeudalism-discourse-synthesis.md)
- **Inputs (declared)**: `gpt-2026-01-18-fiction-hottakes`, `gpt-2026-01-18-hottakes`
- **TODOs**:
  - [ ] Revisit synthesis once input sources are upgraded to rigor-v1
  - [ ] Ensure synthesis cites updated claim IDs and reflects any credence/evidence changes

### pageindex-vs-stratalens-vectorless-rag-synthesis

- **Synthesis**: [analysis/syntheses/pageindex-vs-stratalens-vectorless-rag-synthesis.md](analysis/syntheses/pageindex-vs-stratalens-vectorless-rag-synthesis.md)
- **Inputs (declared)**: `avichawla-2026-pageindex-thread`, `islam-2023-financebench`, `kamathhrishi-2025-stratalens-ai`, `vectifyai-2025-mafin25-financebench`, `vectifyai-2025-pageindex`
- **TODOs**:
  - [ ] Revisit synthesis once input sources are upgraded to rigor-v1
  - [ ] Ensure synthesis cites updated claim IDs and reflects any credence/evidence changes

### realitycheck-2026-v0-3-0-framework-data-synthesis

- **Synthesis**: [analysis/syntheses/realitycheck-2026-v0-3-0-framework-data-synthesis.md](analysis/syntheses/realitycheck-2026-v0-3-0-framework-data-synthesis.md)
- **Inputs (declared)**: `lee-2026-minnesota-trump-immigration-conflict`, `lhl-2026-realitycheck-data-readme`, `lhl-2026-realitycheck-readme`, `stross-2025-the-pivot-1`
- **TODOs**:
  - [ ] Revisit synthesis once input sources are upgraded to rigor-v1
  - [ ] Ensure synthesis cites updated claim IDs and reflects any credence/evidence changes

### vibecoding-agent-psychosis-synthesis

- **Synthesis**: [analysis/syntheses/vibecoding-agent-psychosis-synthesis.md](analysis/syntheses/vibecoding-agent-psychosis-synthesis.md)
- **Inputs (declared)**: `ronacher-2026-agent-psychosis`, `yegge-2025-beads`, `yegge-2025-gastown`, `yegge-2026-bags-creator-economy`, `yegge-2026-future-coding-agents`, `yegge-2026-gas-town-emergency-user-manual`, `yegge-2026-welcome-gas-town`
- **TODOs**:
  - [ ] Revisit synthesis once input sources are upgraded to rigor-v1
  - [ ] Ensure synthesis cites updated claim IDs and reflects any credence/evidence changes

### yegge-2025-2026-vibe-coding-synthesis

- **Synthesis**: [analysis/syntheses/yegge-2025-2026-vibe-coding-synthesis.md](analysis/syntheses/yegge-2025-2026-vibe-coding-synthesis.md)
- **Inputs (declared)**: `yegge-2025-beads`, `yegge-2025-beads-best-practices`, `yegge-2025-beads-blows-up`, `yegge-2025-cheese-wars-rise-vibe-coder`, `yegge-2025-gastown`, `yegge-2025-six-new-tips-coding-agents`, `yegge-2025-zero-framework-cognition`, `yegge-2026-bags-creator-economy`, `yegge-2026-future-coding-agents`, `yegge-2026-gas-town-emergency-user-manual`, `yegge-2026-steveys-birthday-blog`, `yegge-2026-welcome-gas-town`
- **TODOs**:
  - [ ] Revisit synthesis once input sources are upgraded to rigor-v1
  - [ ] Ensure synthesis cites updated claim IDs and reflects any credence/evidence changes
