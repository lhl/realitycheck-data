# Reality Check Knowledge Base

A unified knowledge base for rigorous analysis of claims across technology, economics, labor, and governance domains. Uses the [Reality Check](https://github.com/lhl/realitycheck) framework.

## Current Status

| Metric | Count |
|--------|-------|
| **Claims** | 595 |
| **Sources** | 145 |
| **Argument Chains** | 4 |
| **Predictions Tracked** | 36 |

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
| 2026-02-09 | [Software factories, dark factories, and compounding teams (harness vs control plane)](analysis/syntheses/software-factory-dark-factory-harness-control-plane-synthesis.md) | `[DRAFT]` | Cross-source synthesis: “software factory” doctrine + dark-factory levels + compounding teams; separates correctness plane (harness/holdouts/DTU) from control plane (orchestration/memory/gates) |
| 2026-02-07 | [Superlinear (paper + repo + model release)](analysis/syntheses/superlinear-multi-step-attention-release-synthesis.md) | `[DRAFT]` | Cross-source audit: code+weights consistency checks (VRAM/KV math); throughput/quality unverified; security/license/patent risks flagged |
| 2026-02-07 | [Semantica vs Reality Check](analysis/syntheses/semantica-vs-realitycheck-synthesis.md) | `[DRAFT]` | Cross-project comparison: Semantica semantic/KG stack vs Reality Check claim/provenance ledger; integration guidance |
| 2026-02-06 | [METR time horizon (long-task capability) 2025–2026](analysis/syntheses/metr-2025-2026-time-horizon-synthesis.md) | `[DRAFT]` | Cross-source synthesis: time-horizon trend (≈7-month doubling; faster post-2023 under TH1.1), protocol sensitivity, and cross-domain bottlenecks (OSWorld much shorter) |
| 2026-02-06 | [GPT-5.3-Codex vs Claude Opus 4.6 (agentic coding releases)](analysis/syntheses/gpt-5-3-codex-vs-claude-opus-4-6-release-synthesis.md) | `[DRAFT]` | Cross-source comparison: benchmark cross-checks (Terminal-Bench), long-context + pricing tiers, product surfaces/controls, safety framing |
| 2026-02-06 | [GPT-5.3-Codex vs Claude Opus 4.6 (system cards)](analysis/syntheses/gpt-5-3-codex-vs-claude-opus-4-6-system-cards-synthesis.md) | `[DRAFT]` | Cross-source comparison: Preparedness vs RSP/ASL framing, agentic-risk surfaces, sabotage/sandbagging signals (Apollo), and operational controls (sandboxing/monitoring/trusted access) |
| 2026-02-01 | [Arclight “Mirror” + “AOS” (developmental AI mentor + hidden institution OS)](analysis/syntheses/arclight-2026-mirror-aos-synthesis.md) | `[DRAFT]` | Cross-source synthesis: anti-sycophancy “graduation” mentor thesis + constraint-based “kernel invariants”; flags psychometrics+secrecy risks |
| 2026-02-01 | [Reality Check v0.3.0 self-check (framework + dataset)](analysis/syntheses/realitycheck-2026-v0-3-0-framework-data-synthesis.md) | `[DRAFT]` | Framework+dataset triangulation; rigor-v1 vs legacy examples; workflow notes |
| 2026-01-27 | [Zhang Youxia purge, PLA disruption, and Taiwan timing](analysis/syntheses/china-pla-purge-zhang-youxia-taiwan-synthesis.md) | `[DRAFT]` | Cross-source synthesis: Zhang Youxia purge, PLA “high command” disruption, and Taiwan invasion timing |
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
| 2026-02-09 | [StrongDM “Software Factory” (main essay)](analysis/sources/strongdm-2026-software-factory.md) | `[REVIEWED]` | Vendor manifesto: non-interactive “software factory” posture; scenarios as governance; DTU (behavioral twins) concept; token-fuel heuristic |
| 2026-02-09 | [StrongDM “Software Factory” (principles)](analysis/sources/strongdm-2026-software-factory-principles.md) | `[REVIEWED]` | Doctrine: seed→validation harness→feedback loop until holdout scenarios pass stably; “frontier engineering” as representation work |
| 2026-02-09 | [Shapiro: five levels to the “Dark Factory”](analysis/sources/shapiro-2026-five-levels-dark-factory.md) | `[REVIEWED]` | Heuristic maturity model (0–5) for AI coding; role shift coder→reviewer→PM/spec; “technical deflation” framing |
| 2026-02-09 | [Willison: StrongDM software without looking at code](analysis/sources/willison-2026-strongdm-software-factory.md) | `[REVIEWED]` | Makes “Dark Factory” concrete; highlights spec-only `strongdm/attractor` artifact + holdout-scenario framing |
| 2026-02-09 | [Anthropic: harnesses for long-running agents](analysis/sources/anthropic-2025-effective-harnesses-long-running-agents.md) | `[REVIEWED]` | Harness pattern: initializer + iterative coding sessions + durable artifacts (progress logs, git checkpoints) + end-to-end testing discipline |
| 2026-02-09 | [Schillace: compounding teams](analysis/sources/schillace-2025-compounding-teams.md) | `[REVIEWED]` | “Compounding” org pattern: bespoke frameworks + filesystem/git artifacts + recursive tool building; warns against mixing manual+AI styles in one repo |
| 2026-02-09 | [DoltHub: a day in Gas Town](analysis/sources/dolthub-2026-day-in-gas-town.md) | `[REVIEWED]` | Field report on Gas Town “limitless mode”; highlights merge/guardrail failure modes and cost; suggests Dolt as memory substrate |
| 2026-02-09 | [Virtuslab: Beads review (“give AI memory”)](analysis/sources/virtuslab-2026-github-all-stars-beads.md) | `[REVIEWED]` | Review of Beads as agent memory/task system; agent-UX heuristics (structured output, deterministic thick logic, idempotency) |
| 2026-02-09 | [Yegge: “Revenge of the junior developer”](analysis/sources/yegge-2025-revenge-junior-developer.md) | `[REVIEWED]` | Early “waves” model: agents→clusters→fleets; token-opex framing; “junior revenge” labor hypothesis under rising spend |
| 2026-02-09 | [Thread: “Windows is awful” + caste-discrimination claims at Microsoft (Thread Reader)](analysis/sources/miyaspokeofthis-2026-windows-caste-thread.md) | `[REVIEWED]` | Low-rigor, high-bias thread: separates general caste-discrimination reporting/cases (Cisco verified) from uncorroborated Microsoft+“Python vs C++” allegations; X embeds inaccessible |
| 2026-02-07 | [Superlinear Multi-Step Attention (arXiv 2601.18401v1)](analysis/sources/huang-2026-superlinear-multi-step-attention.md) | `[REVIEWED]` | Preprint: structural non-exclusion framing; N=2 `O(L^(3/2))` scaling; self-reported B200 throughput + NIAH results |
| 2026-02-07 | [Superlinear (GitHub repo @ df9b2ef)](analysis/sources/concavityai-2026-superlinear.md) | `[REVIEWED]` | Repo audit: Triton kernels + OpenAI-style server; explicit sessions/snapshots for KV cache reuse; memory budgeting cross-checked |
| 2026-02-07 | [Superlinear-Exp-v0.1 (HF model release)](analysis/sources/concavityai-2026-superlinear-exp-v0-1.md) | `[REVIEWED]` | Weights+remote code audit: `trust_remote_code`; ~59GiB weights; config implies ~6GB/1M tokens KV; license + patent notice |
| 2026-02-07 | [Semantica (GitHub repo @ b4cfb6d)](analysis/sources/hawksightai-2026-semantica.md) | `[REVIEWED]` | Repo audit: claims vs code/tests; maturity, strengths/weaknesses, and gaps |
| 2026-02-06 | [Time Horizon 1.1 (METR)](analysis/sources/metr-2026-time-horizon-1-1.md) | `[REVIEWED]` | METR methodology update: suite 170→228, long tasks 14→31, Vivaria→Inspect; updated slope estimates + protocol/task-distribution sensitivity |
| 2026-02-06 | [How Does Time Horizon Vary Across Domains? (METR)](analysis/sources/metr-2025-time-horizon-vary-across-domains.md) | `[REVIEWED]` | Cross-domain time-horizon comparisons: coding/math/QA fast; GUI agents (OSWorld) much shorter; proxy-based caveats + soundness conditions |
| 2026-02-06 | [Measuring AI Ability to Complete Long Tasks (METR blog)](analysis/sources/metr-2025-measuring-ai-ability-to-complete-long-tasks.md) | `[REVIEWED]` | Introduces time-horizon metric; reports ~7-month doubling with wide CIs; includes partial reproduction checks via released run data |
| 2026-02-06 | [Introducing GPT-5.3-Codex](analysis/sources/openai-2026-gpt-5-3-codex.md) | `[REVIEWED]` | OpenAI release post: agentic coding + “computer work” framing; benchmark table; Terminal-Bench leaderboard cross-check; cyber capability classification + trusted-access program |
| 2026-02-06 | [GPT-5.3-Codex System Card](analysis/sources/openai-2026-gpt-5-3-codex-system-card.md) | `[REVIEWED]` | System card: Codex sandboxing + network controls; destructive-action avoidance mitigation; Preparedness “High cyber capability” framing with layered safeguards + TAC; Apollo sandbagging/sabotage summary; residual risk notes |
| 2026-02-06 | [Claude Opus 4.6](analysis/sources/anthropic-2026-claude-opus-4-6.md) | `[REVIEWED]` | Anthropic release post: 1M context (beta), compaction/effort controls, pricing tiers; benchmark claims vs Terminal-Bench leaderboard; GDPval-AA Elo cross-check |
| 2026-02-06 | [System Card: Claude Opus 4.6](analysis/sources/anthropic-2026-claude-opus-4-6-system-card.md) | `[REVIEWED]` | System card: training data cutoff (May 2025); adaptive thinking + effort levels; benchmark methodology; RSP/ASL-3 deployment determination; alignment key findings incl overly agentic GUI computer-use and “suspicious side tasks”; external testing (AISI/Apollo/Andon) |
| 2026-02-06 | [AI 2027](analysis/sources/aifutures-2025-ai-2027.md) | `[REVIEWED]` | Scenario + forecast pages: “superhuman coder” by 2027 plausible; ~1-year superhuman-coder→ASI median; compute stock 10× to 100M H100e; theft/race dynamics |
| 2026-02-01 | [Memorandum of Strategy: Project Mirror (Arclight)](analysis/sources/arclight-2026-mirror.md) | `[DRAFT]` | Proposal: anti-sycophancy AI “mentor” optimized for graduation; psychometric middleware + lockout rules; limited empirical grounding |
| 2026-02-01 | [Arclight Operating System (AOS): Internal Codex](analysis/sources/arclight-2026-aos.md) | `[DRAFT]` | Constraint-based institution “OS”: agency + endowment + founder-decay; argues kernel must stay hidden; heavy on non-operational metaphors |
| 2026-02-01 | [Reality Check (framework README)](analysis/sources/lhl-2026-realitycheck-readme.md) | `[REVIEWED]` | Repo self-description; verified CLI+DB primitives; notes rigor-v1 validator + 401 tests |
| 2026-02-01 | [Reality Check Knowledge Base (dataset README)](analysis/sources/lhl-2026-realitycheck-data-readme.md) | `[REVIEWED]` | Dataset snapshot and structure; verified DB counts and layout; flags YAML exports vs DB truth |
| 2026-02-01 | [Minnesota standoff with Trump administration stokes fears of civil war (The Hill)](analysis/sources/lee-2026-minnesota-trump-immigration-conflict.md) | `[REVIEWED]` | Civil-war escalation framing; links Good/Pretti killings to federalism/legal conflict (SCOTUS Guard limits) and CERL simulation; flags under-verified deployment-scale claims |
| 2026-01-31 | [How the World Sees America, With Adam Tooze (NYT)](analysis/sources/nyt-2026-world-sees-america-tooze.md) | `[REVIEWED]` | Davos 2026 “rupture” framing; Greenland tariffs as rupture datapoint; China scale + climate constraints; skepticism of “U.S.→China hegemony transition” story |
| 2026-01-31 | [DHS retreats from the claim that the agents who killed Alex Pretti faced a 'violent riot' (Reason)](analysis/sources/reason-2026-dhs-retreats-violent-riot-pretti.md) | `[DRAFT]` | “Violent riot” framing vs OPR-described yelling/whistles; Bovino “rights don’t count” quote; credibility argument via prior Chicago misrepresentation finding |
| 2026-01-30 | [These Trump voters 'formed a suicide pact' and Republicans are panicking: ex-GOP operative (Raw Story)](analysis/sources/rawstory-2026-trump-voters-suicide-pact.md) | `[DRAFT]` | Opinion recap of Rick Wilson on farm distress from tariffs + immigration enforcement; verified “444 farming counties” typology + high foreign-born crop labor share; key numeric forecasts uncorroborated |
| 2026-01-27 | [Special Report: China sets new records in air-sea operations around Taiwan (Janes)](analysis/sources/janes-2025-air-sea-operations-around-taiwan.md) | `[DRAFT]` | Verification source: Taiwan MND-attributed ADIZ annual totals (2023 vs 2024) used as pressure metric |
| 2026-01-27 | [Military Implications of PLA Aircraft Incursions in Taiwan’s Airspace 2024 (Jamestown)](analysis/sources/jamestown-2025-pla-aircraft-incursions-taiwan-airspace-2024.md) | `[DRAFT]` | Verification source: definition-sensitive median-line day-count metric (62 vs 209 “over half” days) |
| 2026-01-27 | [Energy supplies sufficient, ministry says (Taipei Times)](analysis/sources/taipeitimes-2022-energy-supplies-sufficient-ministry.md) | `[DRAFT]` | Verification source: MOEA-stated natural-gas reserves ~10–11 days of consumption (2022-08) |
| 2026-01-27 | [Stable Supply of Natural Gas (Taiwan MOEA Energy Administration)](analysis/sources/moeaea-2024-stable-supply-natural-gas.md) | `[DRAFT]` | Verification source: policy target schedule for natural-gas “security stockpile required” (14 days by 2027) |
| 2026-01-27 | [China's January 2026 military purge reshapes Taiwan calculus (Claude deepresearch memo)](analysis/sources/claude-2026-deepresearch-pla-purge-taiwan-calculus.md) | `[DRAFT]` | AI-generated synthesis memo: blockade/quarantine framing, Taiwan energy vulnerability, and norms/credibility context |
| 2026-01-26 | [2026 United States intervention in Venezuela (Wikipedia)](analysis/sources/wikipedia-2026-us-intervention-venezuela.md) | `[DRAFT]` | Context source: Venezuela intervention capture event + UN/legal criticism as precedent/analogy |
| 2026-01-26 | [How a purge of China’s military leadership could impact the army and the future of Taiwan (AP)](analysis/sources/ap-2026-pla-purge-taiwan.md) | `[DRAFT]` | Explainer: announced investigations, purge scale, and competing views on short- vs long-term Taiwan risk |
| 2026-01-26 | [Taiwan monitoring “abnormal” China military leadership changes (Reuters)](analysis/sources/reuters-2026-taiwan-monitoring-pla-leadership.md) | `[DRAFT]` | Taiwan official posture: monitor abnormal PRC changes; don’t lower guard; notes near-daily PRC ops |
| 2026-01-26 | [What Xi Jinping’s purge of China’s most senior general reveals (Economist)](analysis/sources/economist-2026-xi-purge-senior-general.md) | `[DRAFT]` | Motive space: corruption vs performance vs faction; warns of readiness impacts; cites DoD assessments |
| 2026-01-26 | [Xi’s Purge of Top General Spurs Questions on Taiwan, Succession (Bloomberg)](analysis/sources/bloomberg-2026-purge-top-general-taiwan-succession.md) | `[DRAFT]` | Speed/urgency and succession speculation; skeptical of nuclear-leak claim; Taiwan timing implications |
| 2026-01-26 | [Xi takes sole operational control of army as China probes military leaders (FT)](analysis/sources/ft-2026-xi-sole-operational-control-pla.md) | `[DRAFT]` | CCP “discipline” language caution; “sole operational control” framing; ties to 2027 capability target discourse |
| 2026-01-26 | [Xi’s Purge of China’s Military Brings Its Top General Down (NYT)](analysis/sources/nyt-2026-xi-purge-top-general-down.md) | `[DRAFT]` | Xi distrust hypothesis; public investigation implies downfall; suggests multi-year rebuild lowers short-term invasion odds |
| 2026-01-26 | [Xi's purge paints a picture of power and control (Sky News)](analysis/sources/skynews-2026-xi-purge-power-control.md) | `[DRAFT]` | Signal-reading: speed + PLA Daily political framing; captures coup/treason rumor ecology |
| 2026-01-26 | [Military purge gives Xi total control of Chinese army (Telegraph)](analysis/sources/telegraph-2026-xi-purge-total-control-pla.md) | `[DRAFT]` | Strong-form analyst forecasts (“Taiwan delayed for years”) and purge-tempo-as-strength hypothesis |
| 2026-01-26 | [China’s Top General Accused of Giving Nuclear Secrets to U.S. (WSJ)](analysis/sources/wsj-2026-top-general-nuclear-secrets.md) | `[DRAFT]` | Unnamed-source briefing allegations: nuclear leak + bribes + Shenyang task force; readiness-vacuum risk |
| 2026-01-26 | [The Chinese Spy Machine Infiltrating Taiwan’s Military (WSJ)](analysis/sources/wsj-2026-chinese-spy-machine-taiwan-military.md) | `[DRAFT]` | Taiwan insider-threat axis: espionage cases and recruitment methods; relevance to contingency risk |
| 2026-01-26 | [PLA purges intensify: Zhang Youxia and Liu Zhenli under investigation (Sinocism)](analysis/sources/sinocism-2026-pla-purges-intensify-zhang-liu.md) | `[DRAFT]` | PLA Daily excerpt emphasizes authority/cliques; SCMP-sourced internal briefings/detention claims (provisional) |
| 2026-01-26 | [Hot takes/threads on Zhang Youxia purge and Taiwan timing (X compilation)](analysis/sources/x-2026-zhang-purge-hot-takes.md) | `[DRAFT]` | Rumor-space map: invasion-delay, info-warfare, coup claims; extracted as low-evidence hypotheses |
| 2026-01-26 | [Physician Declaration on Pretti Shooting (Doc. 109)](analysis/sources/uscourts-mnd-2025-04669-doc109-doctor-declaration.md) | `[DRAFT]` | Primary court filing: physician declaration describing post-shooting medical response + reported wound locations (agency attribution in declaration is disputed) |
| 2026-01-26 | [Alex Pretti Family Statement (Common Dreams)](analysis/sources/commondreams-2026-minneapolis-shooting-family.md) | `[REVIEWED]` | Family response to CBP shooting; video evidence disputes official narrative (phone vs gun, disarmament before shooting); immediate "domestic terrorist" labeling without evidence |
| 2026-01-25 | ["Positions ICE has taken" (BlueBadger2600)](analysis/sources/bluebadger2600-2026-ice-positions.md) | `[REVIEWED]` | Legal/policy fact-check of ICE authority claims (home entry, detention, counsel, courts, third-country removals) + Minnesota incidents (Good/Pretti, 5yo detention, National Guard, Vance immunity) |
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
| TECH | Technology & AI | 206 |
| LABOR | Labor & Employment | 29 |
| ECON | Economics & Markets | 48 |
| GOV | Governance & Policy | 87 |
| SOC | Social Dynamics | 12 |
| TRANS | Transition Dynamics | 29 |
| RESOURCE | Resource Constraints | 15 |
| GEO | Geopolitics | 30 |
| INST | Institutions & Organizations | 49 |
| RISK | Risk Assessment | 30 |
| META | Framework & Methodology | 60 |

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

*Last updated: 2026-02-09*
