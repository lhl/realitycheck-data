# Reality Check: AI 2040 — Plan A

> **Claim types:** [F] fact; [T] theory or policy proposition; [H] testable hypothesis; [P] prediction; [A] assumption; [C] counterfactual; [S] speculation; [X] contradiction.
>
> **Evidence:** E1 systematic review or replicated evidence; E2 peer-reviewed study or official statistics; E3 working paper, open empirical work, or convergent expert analysis; E4 credible primary/industry documentation; E5 forecast, expert judgment, or argument; E6 unsupported or presently untestable speculation.
>
> **Verification status:** ok verified as stated; x contradicted; nf searched but not found; blocked access/tooling prevented the check; ? not attempted.

## Verdict at a glance

**Rigor level: [REVIEWED].** The crux factual claims in this analysis received at least two distinct checks and none remains “?”. Future predictions remain unresolved by their nature; they are scored as predictions rather than laundered into facts.

**Bottom line:** AI 2040 is a serious design exercise and a weak forecast. Its best contribution is to turn “coordinate and slow down” into an inspectable system involving compute accounting, verification, multiple labs, safety cases, redistribution, and defensive preparation. Its successful ending, however, requires several individually uncertain transitions to work together: broad AI research automation, rapid cross-domain generalization, a politically legitimate US–China deal, near-comprehensive monitoring, controllable top-expert AI, explosive physical deployment, and a high-assurance alignment handoff. The publication documents many of these uncertainties unusually well. It does not resolve them.

The practical verdict is therefore asymmetric:

- **High confidence:** government technical capacity, large-cluster visibility, verification R&D, transparent model specifications, independent safety scrutiny, bio/cyber resilience, and planning for ownership and distribution are sensible preparations across many futures.
- **Medium confidence:** industrial-scale compute is a useful governance lever, and important international AI agreements could become technically verifiable. The exact Plan A regime is not yet demonstrated.
- **Low confidence:** the dates, economic magnitudes, hardware explosion, decade-long treaty path, and 2040 alignment handoff.
- **Very low confidence:** treating the entire narrated success chain as a likely future. The authors explicitly do not do this either.

These rough analyst credences are intended for decision calibration, not as pseudo-precise forecasts:

| Proposition | Credence | Interpretation |
|---|---:|---|
| Plan A is a recommendation and conditional success scenario, not the authors’ modal forecast | 0.99 | Directly and repeatedly documented |
| Selected software-agent task horizons have improved rapidly | 0.85 | Well supported as a benchmark finding; external validity is limited |
| AI R&D is fully automated by about 2041 absent major interruption | 0.45 | Plausible, definition-sensitive, and highly uncertain |
| Broadly superhuman economic capability follows within a few years of AI-R&D automation | 0.25 | A major extrapolation beyond current evidence |
| Something close to the 2029 Plan A deal is adopted by 2030 | 0.10 | Consistent with the authors’ own low adoption estimate |
| Industrial-scale AI development could be monitored under a highly cooperative agreement | 0.60 | Supported in direction by compute-governance research; not at Plan A assurance levels |
| An adopted Plan A regime avoids major impairment through 2040 | 0.35 | Political withdrawal and common-mode failure remain severe risks |
| Plan A produces roughly 200–270× world output by 2040 | 0.10 | A consequence of assumed trajectories, not an independently calibrated forecast |
| Alignment becomes mature enough for an irreversible handoff by 2040 | 0.15 | Current work is an agenda with early demonstrations, not an assurance science |
| The low-regret near-term policy portfolio is net beneficial | 0.80 | Robust to much wider timeline and capability uncertainty |

## Metadata and audit scope

| Field | Value |
|---|---|
| **Source ID** | `aifutures-2026-ai-2040-plan-a` |
| **Title** | AI 2040: Plan A — The Deal |
| **Authors** | Thomas Larsen; Romeo Dean; Brendan Halstead; Eli Lifland; Ryan Greenblatt; Daniel Kokotajlo |
| **Publisher** | AI Futures Project |
| **Publication / capture date** | July 2026; corpus captured 2026-07-11 |
| **Type** | Policy scenario, recommendation, forecast bundle, and modeling package |
| **Canonical URL** | https://ai-2040.com/ |
| **Primary local text** | [Site-derived scenario](../../reference/captured/ai-2040/site/main.md) |
| **Published artifact** | [70-page PDF](../../reference/primary/aifutures-2026-ai-2040-plan-a.pdf) |
| **Supporting corpus** | 16 prose supplements, verification addendum, alternative plans and perspectives, economics explorer, team material, three response threads, and 211 HN comments |
| **Source reliability** | 0.62 overall: high for what the authors believe and propose; much lower for distant conditional outcomes |
| **Analysis date** | 2026-07-11 |
| **Canonical claims** | [Companion YAML](aifutures-2026-ai-2040-plan-a.yaml); 25 source and policy claims registered with evidence and reasoning provenance |

This check analyzes the publication as a connected package rather than fact-checking the prose page in isolation. The most important first-party materials are the [assumptions supplement](../../reference/captured/ai-2040/site/supplements/plan-a-assumptions.md), [comparison of plans](../../reference/captured/ai-2040/site/supplements/comparing-possible-plans.md), [verification plan](../../reference/captured/ai-2040/site/supplements/verification-plan.md), [covert-project model](../../reference/captured/ai-2040/site/supplements/covert-ai-projects.md), [deal-decline model](../../reference/captured/ai-2040/site/supplements/deal-decline.md), [alignment roadmap](../../reference/captured/ai-2040/site/supplements/alignment-roadmap.md), and [economic-model documentation](../../reference/captured/ai-2040/site/economic-model/model-explanation.md).

The existing Reality Check database was queried as evidence, not treated as authority. At the time of the original analysis it contained 1,146 claims, 272 sources, 415 evidence links, 370 reasoning trails, and 175 analysis logs. Relevant records were re-read and, for cruxes, checked against current public sources. This canonical version registers the AI 2040 source and 25 claims while reusing rather than duplicating existing calibration claims.

---

## Stage 1: Descriptive analysis

### Core thesis

The authors expect a race toward systems that automate AI research and rapidly become broadly superhuman to create two linked dangers: loss of control to misaligned AIs and extreme concentration of power in the winning company or state. Plan A recommends replacing that race with an early, verified US–China slowdown; transparent and distributed frontier development; heavy use of controllable AI for safety and defensive work; redistribution of automation rents; a pause at top-expert AI; and, only after robust alignment evidence, a deliberate handoff to superintelligence.

The exact future history is a **successful conditional scenario**, not the authors’ best guess. The main text says AI 2027 remains roughly what they expect absent intervention. One author’s rough decomposition gives only about a 5% chance that Plan A itself is adopted.

### What the scenario actually says

| Date | Proposed or predicted transition | Epistemic status |
|---|---|---|
| 2026–2028 | Governments build expertise, track chips and clusters, require model-spec/internal-use reporting, improve export-control enforcement, and fund verification R&D | Mostly [T] policy propositions; relatively robust |
| 2029 | The US and China halt frontier training, declare chips, inspect facilities, and negotiate a wider Consortium | [P]/[A] for the story; low adoption probability |
| 2030 | Datacenters are converted to verified inference-only use, then limited transparent R&D resumes | [H]/[A]; prototype-level technical basis |
| 2030–2035 | Many legal projects scale mainly through hardware; AI and robots automate most work; safety cases govern capability increases | [P]; heavily model-dependent |
| 2032–2035 | Cap-and-trade for compute/robots funds citizen dividends; physical and economic output grows explosively | [P]; exact quantities are exogenous in Plan A |
| 2034 | Mutually assured compute destruction deters withdrawal and breakout | [H]/[A]; unprecedented mechanism |
| 2035 | The Consortium pauses at top-human-expert AI while humans still retain control | [P]/[A] |
| 2035–2039 | Controlled AIs do alignment research; verification, interpretability, and behavioral science mature | [P]; presently an open research agenda |
| 2040 | Humans trust aligned AIs, resume capability progress, and pass increasing authority to them | [P]/[H]; the largest unresolved endgame assumption |

### Methodology

AI 2040 combines methods with very different evidential weight:

1. **Scenario scrutiny.** A concrete future history is used like a tabletop exercise to expose policy dependencies, implementation problems, and side effects. This tests coherence, not frequency.
2. **Expert judgment and interviews.** The authors draw on frontier-lab experience, policymakers, national-security practitioners, safety researchers, user interviews, and table exercises. These inputs are informative but not a reproducible sample.
3. **Capability and takeoff modeling.** The AI Futures Model supplies a no-deal trajectory and conditional progress paths. Threshold definitions and many parameters remain judgment calls.
4. **Compute and covert-project modeling.** Bottom-up estimates of chip stocks, fabs, smuggling, construction, intelligence, and detection feed scenario simulations. The headline 13% covert-project risk is conditional on a competent Consortium and several favorable assumptions.
5. **Treaty base rates.** A manually reviewed Claude analysis compares 31 heterogeneous agreements, applies subjective similarity weights, and is combined with an inside-view decomposition. The resulting estimate is about 37% deal decline within five years and 48% within ten.
6. **Economic exploration.** A nested-CES model maps user-specified AI quantities, efficiencies, capabilities, robot stocks, and elasticities into output and factor-price paths. In the Plan A preset, the central AI and robot quantities are not generated by investment inside the growth loop.
7. **Alignment roadmap.** A rough research agenda covers control evaluations, model organisms, elicitation, behavioral tests, scheming, and handoff. It is explicit about what would need to become true; it is not a demonstrated solution.

The project used AI for programming, brainstorming, and feedback. Claude Code substantially implemented the explorer and site; Claude produced the first treaty base-rate analysis. The authors say humans wrote nearly all final prose and reviewed the remainder.

### Key claims

| # | Claim | Claim ID | Layer | Actor | Scope | Quantifier | Type | Domain | Evid | Credence | Verified? | Falsifiable by |
|---:|---|---|---|---|---|---|---|---|---|---:|---|---|
| 1 | Plan A is a recommendation and success scenario, not the authors’ modal forecast | META-2026-168 | ASSERTED | OTHER:AIFP | document framing; July 2026 | N/A | [F] | META | E4 | 0.99 | ok | First-party text presenting implementation as its best forecast |
| 2 | AI R&D will be fully automated within about 15 years absent major interruption | TECH-2026-102 | ASSERTED | OTHER:AIFP | global frontier AI; by about 2041 | OTHER:more likely than not | [P] | TECH | E5 | 0.45 | Not resolvable ex ante | No operationally defined full automation by 2041 |
| 3 | Broadly superhuman economic capability follows within a few years of AI-R&D automation | TECH-2026-103 | EFFECT | OTHER:AIFP | post-automation; most economic tasks | most | [P] | TECH | E5 | 0.25 | Not resolvable ex ante | Persistent non-AI bottlenecks or domain gaps after research automation |
| 4 | Automated coding to top-expert-dominating AI has a roughly one-year median transition | TRANS-2026-057 | ASSERTED | OTHER:AIFP | conditional takeoff | OTHER:median 1y | [P] | TRANS | E5 | 0.25 | Not resolvable ex ante | Measured transition takes much longer or threshold never occurs |
| 5 | Strategically vastly superhuman, collectively adversarial AIs could defeat human control | RISK-2026-992 | EFFECT | OTHER:AIFP | conditional on such systems existing | some | [H] | RISK | E5 | 0.65 | Unverified conditional | Credible containment under adversarial red-team conditions at relevant scale |
| 6 | Something close to a verified US–China slowdown can be adopted around 2029 | GEO-2026-061 | PRACTICED | OTHER:US/PRC | bilateral then multilateral; by 2030 | some | [P] | GEO | E5 | 0.10 | Not resolvable ex ante | No serious negotiation or agreement by 2030 |
| 7 | About 99% of strategically relevant compute can be declared and monitored | GOV-2026-291 | PRACTICED | OTHER:Consortium | industrial AI compute; global | most | [H] | GOV | E3 | 0.40 | Qualified support only | Audits find materially larger dark/edge/undeclared capability |
| 8 | Total AI-R&D transparency improves safety and diffusion more than it aids defectors | GOV-2026-292 | EFFECT | OTHER:Consortium | frontier research during slowdown | N/A | [H] | GOV | E5 | 0.50 | Unverified | Leakage measurably erodes legal-project advantage or increases misuse more than scrutiny helps |
| 9 | Covert projects remain sufficiently detectable and behind the legal frontier | RISK-2026-993 | EFFECT | OTHER:Consortium/defectors | 2029–2040 | OTHER:13% modeled failure | [P] | RISK | E5 | 0.30 | Model result only | Red-team simulation or real evasion defeats assumed controls at materially higher rates |
| 10 | Hardware-led scaling is meaningfully reversible | TRANS-2026-058 | EFFECT | OTHER:Consortium | large clusters, fabs, robots | most | [H] | TRANS | E4 | 0.35 | Partly grounded | Failsafes fail under cyberattack, war, withdrawal, or insider compromise |
| 11 | AI and robot labor produce roughly 200–270× world output by 2040 in Plan A | ECON-2026-990 | EFFECT | OTHER:world economy | 2025–2040 preset | OTHER:200–270x | [P] | ECON | E6 | 0.10 | Scenario output only | Investment-, energy-, supply-, demand-, or deployment-constrained models reject the path |
| 12 | Most economically valuable cognitive and physical labor can be automated by the mid-2030s | LABOR-2026-041 | EFFECT | OTHER:AI/robots | global economy; mid-2030s | most | [P] | LABOR | E5 | 0.20 | Not resolvable ex ante | Broad task audits show persistent human comparative advantage |
| 13 | Dividends, broad AI access, and transparent governance preserve public power after labor loses leverage | GOV-2026-293 | EFFECT | OTHER:states/citizens | post-work political economy | most | [H] | GOV | E5 | 0.35 | Unverified | Wealth concentration dominates elections, ownership, enforcement, or agenda setting |
| 14 | Control-based safety cases can contain systems through top-expert capability | RISK-2026-994 | EFFECT | OTHER:frontier projects | pre-handoff systems | most | [P] | RISK | E3 | 0.30 | Early narrow demonstrations | Control protocols fail against adaptive collusion or out-of-distribution strategies |
| 15 | AI-assisted research can make alignment a mature enough science by 2038–2040 | TECH-2026-104 | EFFECT | OTHER:alignment field | pause period | N/A | [P] | TECH | E6 | 0.15 | Not resolvable ex ante | No validated high-assurance theory/evaluation by the proposed handoff |
| 16 | Trust can be propagated safely through successive AI generations | RISK-2026-995 | EFFECT | OTHER:successor AIs | 2040 onward | most | [H] | RISK | E6 | 0.15 | Unverified | Common-mode error or coordinated deception survives every verification layer |
| 17 | Truth-seeking personal AIs improve democratic epistemics more than they amplify persuasion and control | GOV-2026-294 | EFFECT | OTHER:citizens/platforms | broad deployment | most | [H] | GOV | E5 | 0.35 | Unverified | Controlled and natural experiments show net polarization, capture, or manipulation |
| 18 | Build government expertise, compute visibility, verification, resilience, and distribution planning now | GOV-2026-295 | PRACTICED | OTHER:governments | near term | N/A | [T] | GOV | E3 | 0.80 | Policy synthesis | Demonstrated net harms exceeding option value under bounded safeguards |

### Argument structure

~~~text
Rapid improvement in AI research agents
        ↓
Full automation of AI R&D
        ↓
Fast transition to broadly superhuman, strategically decisive systems
        ↓
Race conditions create takeover and power-concentration risk
        ↓
Compute remains a concentrated, observable bottleneck
        ↓
US–China agreement slows and makes frontier work transparent
        ↓
Controlled AI + hardware scaling buys useful safety labor and calendar time
        ↓
Dividends, diffusion, and institutions preserve human agency during automation
        ↓
Alignment evidence becomes strong enough for a safe inductive handoff
        ↓
Flourishing post-superintelligence future
~~~

**Chain analysis**

- **Weakest empirical transition:** software/research progress → reliable mastery of all economically and strategically relevant domains.
- **Weakest institutional transition:** recognition of shared danger → a legitimate, intrusive, durable great-power regime.
- **Weakest endgame transition:** useful control and evaluation research → assurance strong enough for irreversible handoff.
- **Dependence problem:** these are not independent coin flips, but success still requires every class of crux to clear a minimum threshold. Narrative continuity does not remove conjunctive risk.
- **If a link breaks:** many near-term recommendations survive; the exact hardware, economic, treaty, and handoff sequence does not.

### Theoretical lineage

- **Transformative-AI and fast-takeoff forecasting:** automated R&D, recursive improvement, and short institutional response windows.
- **AI control and alignment:** scheming, model organisms, trusted monitoring, safety cases, interpretability, and iterative handoff.
- **Arms control and nonproliferation:** declarations, inspections, dual-control systems, deterrence, mutual vulnerability, and verification.
- **Compute governance:** physical chokepoints, concentrated semiconductor supply chains, workload monitoring, and hardware-enabled enforcement.
- **Task-based automation economics:** substitution between human and machine labor, capital-share growth, CES production, and redistribution.
- **Scenario planning and wargaming:** concreteness used to reveal hidden assumptions rather than to estimate a modal path.
- **Liberal pluralism and anti-lock-in:** multiple frontier projects, public scrutiny, broad access, and explicit concern about who controls aligned AI.

### Authors, expertise, and standpoint

The official biographies show substantial relevant experience in AI forecasting, frontier-lab governance, technical safety, compute, policy, and tabletop exercises. Daniel Kokotajlo previously worked on scenario planning at OpenAI; Eli Lifland specializes in forecasting; Thomas Larsen worked in AI safety and policy; Romeo Dean focuses on chips, security, and hardware; Ryan Greenblatt is a central contributor to AI-control research.

The same record shows a concentrated intellectual community. The core team is not presented as a representative panel of macroeconomists, labor economists, China specialists, arms-control practitioners, treaty lawyers, democratic-governance scholars, civil-liberties experts, robotics manufacturers, or energy-system planners. Contributors and reviewers broaden the input, but the documented center of gravity remains AI safety, forecasting, compute, and policy. The economics page itself warns that its key author lacks economics expertise.

That does not invalidate the work. It changes the evidential weight: the package is strongest as an AI-safety policy design produced by technically informed forecasters, and weakest where the narrative’s detail resembles settled expertise in political legitimacy, macroeconomics, labor institutions, or global development.

### Scope and limitations

The package asks, “What might a relatively good transition look like if transformative AI arrives soon and governments attempt a cooperative slowdown?” It does not establish:

- that transformative AI or automated R&D arrives on the depicted schedule;
- that the A/B/C/D/S alternatives exhaust the policy space;
- that Plan A adoption is likely;
- that its treaty reference class predicts an unprecedented AI regime;
- that its economic charts are calibrated forecasts;
- that the alignment endpoint exists or is reachable on a schedule;
- that citizens, workers, poorer states, courts, legislatures, or civil society would regard the regime as legitimate.

---

## Stage 2: Evaluative analysis

### Internal coherence

Plan A is more internally coherent than a slogan such as “pause,” “race,” or “regulate.” It recognizes that a slowdown changes incentives; that secrecy and transparency trade off; that alignment and concentration are separate; that covert projects and political decay threaten any treaty; that automation changes bargaining power as well as income; and that safe AI does not answer who should control it.

Its coherence is conditional rather than evidential. The story usually has an answer for each objection, but an answer of the form “the Consortium develops robust verification,” “truth-seeking AIs improve voters,” or “alignment becomes a science” can identify required work without showing that the work will succeed.

### Key factual claims verified

| Claim ID | Claim | Crux? | Source says | Finding | Evidence | Search notes | Status |
|---|---|---:|---|---|---|---|---|
| META-2026-168 | Plan A is a recommendation, not the modal forecast | **Y** | Implementation is recommended; downstream events are conditional predictions | Repeated on the homepage, in the PDF, assumptions supplement, and comparison supplement; AI 2027 remains roughly the expected no-intervention path | [Main text](../../reference/captured/ai-2040/site/main.md); [assumptions](../../reference/captured/ai-2040/site/supplements/plan-a-assumptions.md); [PDF](../../reference/primary/aifutures-2026-ai-2040-plan-a.pdf) | Q1 searched main/PDF for “recommendation, not prediction”; Q2 searched assumptions/comparison for adoption and modality | ok |
| META-2026-169 | The Plan A economics preset is largely exogenous and illustrative | **Y** | User-specified AI/robot paths drive output; numbers are not expected to be right | Documentation confirms exogenous trajectories, fixed TFP, perfect task reallocation, post-hoc investment accounting, and no credit, money creation, trade flows, or forward-looking households | [Model explanation](../../reference/captured/ai-2040/site/economic-model/model-explanation.md); [technical writeup](../../reference/captured/ai-2040/site/economic-model/model-writeup.md) | Q1 searched model explanation for exogenous/limitations; Q2 checked technical writeup for “come out of thin air” and post-hoc investment | ok |
| TECH-2025-055 | Selected software-agent task horizons doubled about every seven months | **Y** | Capability forecasts use rapid agent progress as an anchor | METR reports the benchmark trend, but defines it at 50% success on a selected task suite; TH1.1 preserves the broad trend while showing suite/protocol sensitivity | [METR 2025](https://metr.org/blog/2025-03-19-measuring-ai-ability-to-complete-long-tasks/); [TH1.1](https://metr.org/blog/2026-1-29-time-horizon-1-1/) | Q1 read-only RC semantic search plus direct METR check; Q2 DuckDuckGo/OpenAlex discovery plus TH1.1 methodology update | ok, qualified |
| TECH-2025-060 | Capability horizons vary sharply across domains | **Y** | Scenario generalizes from AI R&D progress to broad capability | METR reports visual computer-use horizons about 40–100× shorter than its software/reasoning cluster and stresses cross-benchmark caveats | [METR cross-domain study](https://metr.org/blog/2025-07-14-how-does-time-horizon-vary-across-domains/) | Q1 direct study search for GUI/OSWorld; Q2 RC claims TECH-2025-059/060 and source analysis | ok |
| GOV-2026-291 | Industrial-scale compute and important data-center rules may be monitorable under a cooperative agreement | **Y** | Large legal projects can be found, counted, and constrained with trust-minimizing verification | Compute-governance and international-verification research supports detectability and several layered mechanisms, while warning about evasion, privacy, centralization, mobile devices, and many technologies remaining unbuilt or untested | [Sastry et al. 2024](https://arxiv.org/abs/2402.08797); [Harack et al. 2025](https://aigi.ox.ac.uk/publications/verification-for-international-ai-governance/); [Baker et al. 2025](https://arxiv.org/abs/2507.15916) | Q1 compute-governance/chip-tracking and workload-verification queries; Q2 direct AIGI and arXiv checks for international mechanisms | ok, qualified |
| META-2026-170 | The 37%/48% treaty figures come from a small, judgment-heavy synthesis | **Y** | Estimate informed by base rates and inside-view decomposition | Supplement documents 31 heterogeneous agreements, subjective applicability weights, manual review of Claude output, adjustments, and a separate causal decomposition; it also warns against simple averaging and notes limited analogues | [Deal decline](../../reference/captured/ai-2040/site/supplements/deal-decline.md) | Q1 audited methodology/numerics in supplement; Q2 searched external treaty literature and checked the companion-method description | ok as provenance; calibration nf |
| META-2026-171 | The authors’ own quantitative estimates are materially more cautious than the narrative surface | **Y** | Plan A is preferred but risky | Confirmed: about 5% adoption in one decomposition; 37%/48% deal decline; 13% conditional covert failure; 72% avoid takeover and 42% “great future” in one rough Plan A assessment | [Plan comparison](../../reference/captured/ai-2040/site/supplements/comparing-possible-plans.md); [covert projects](../../reference/captured/ai-2040/site/supplements/covert-ai-projects.md); [deal decline](../../reference/captured/ai-2040/site/supplements/deal-decline.md) | Q1 searched all supplements for headline probabilities; Q2 checked main-text footnotes/branch framing | ok |
| META-2026-172 | The core team’s demonstrated expertise is concentrated in AI safety, forecasting, compute, and policy | N | Relevant to cross-domain evidential weight | Official biographies and contribution credits support the characterization; “less demonstrated breadth” is not a claim that no outside expert provided feedback | [Team biographies](../../reference/captured/ai-2040/organization/about.md); [release credits](../../reference/captured/ai-2040/site/about.md) | Q1 audited official team bios; Q2 audited named contributions/reviewers and model disclaimer | ok, carefully scoped |

The factual table verifies what the package is, how its numbers were produced, and what current evidence says. It does **not** mark the future transitions “ok.” A forecast is not verified merely because its premises are documented.

### Forecast and assumption ledger

| Claim | Authors’ stated position | Best current support | Main gap | Analyst credence |
|---|---|---|---|---:|
| Full AI-R&D automation within ~15 years | Thomas Larsen: above 80%; 90% timing interval mid-2027 to ~2050 | Fast software-agent trend; increasing long-horizon autonomy; lab investment | End-to-end research includes problem choice, experiment design, tacit knowledge, evaluation, hardware, and organization | 0.45 |
| Broad superhuman capability within a few years after R&D automation | Above 80% in the assumptions supplement | Potential compounding of automated software and research | Cross-domain transfer, reliability, data, robotics, experiments, manufacturing, and institutions | 0.25 |
| Roughly one-year takeoff | Thomas’s median; 80% interval two months to five years | Recursive R&D mechanism and high parallelism | Definition sensitivity and persistent complementary bottlenecks | 0.25 |
| 2029 US–China deal | Recommended, not predicted; one author gives ~5% for Plan A adoption | Shared interest could grow if danger is legible; historical agreements can matter | Domestic coalitions, secrecy, security dilemma, ratification, succession, firms, third states, legitimacy | 0.10 |
| About 99% of strategic compute covered | Central Plan A requirement | Industrial clusters and supply chain are unusually visible | Existing stock uncertainty, smuggling, edge hardware, new fabs, algorithmic efficiency, workload identification | 0.40 |
| 13% covert-project failure risk | Conditional model result | Bottom-up diversion/detection modeling | Competent implementation, no decisive weight theft, enforceable shutdown after detection, right danger threshold, China focus | 0.30 confidence that the estimate is calibrated |
| Hardware scale is reversible | Core design intuition | Hardware is physical and can support controls | Remote-control compromise, war, political withdrawal, insider attack, autonomous weapons, failed destruction | 0.35 |
| Near-total labor automation by mid-2030s | Conditional prediction | Strong task-level gains in some digital work | Deployment, accountability, embodiment, complementary inputs, demand, law, and job redesign | 0.20 |
| Roughly 200–270× GWP by 2040 | Explorer consequence | Task-based growth theory permits large effects under near-total substitution | Central quantities assumed; model lacks several macro/physical feedbacks | 0.10 |
| Control through top-expert AI | Alignment-plan premise | Narrow AI-control protocols show meaningful gains | Adaptive, colluding, situationally aware systems and real deployment complexity | 0.30 |
| Alignment science and safe handoff by 2040 | Desired end state | Active work on control, scheming, interpretability, and model organisms | No validated assurance theory; hard-to-check reasoning and common-mode failure | 0.15 |

### Read-only Reality Check evidence reused

The database evidence is useful primarily for calibration. It contains mutually constraining findings rather than a one-directional “AI fast” or “AI slow” story. The evidence levels and credences in this table preserve the existing read-only records for auditability; they were not silently regraded or written back, and inclusion is not an endorsement of every stored rating.

| RC claim/source | Finding already in the database | Evid / credence | Relevance here |
|---|---|---:|---|
| TECH-2025-055 / metr-2025-measuring-ai-ability-to-complete-long-tasks | Frontier 50%-success software-task horizon doubled roughly every seven months | E3 / 0.75 | Supports rapid progress, not universal autonomy |
| TECH-2025-060 / metr-2025-time-horizon-vary-across-domains | GUI/computer-use horizons were roughly 40–100× shorter than software/reasoning | E3 / 0.70 | Direct warning against domain composition |
| TECH-2026-927 and META-2026-039 / metr-2026-time-horizon-1-1 | Updated suite retained a roughly 196-day hybrid doubling trend but estimates depend on task composition and are nearing saturation | E3–E4 / 0.70–0.75 | Trend is real enough to monitor, not a law of nature |
| LABOR-2023-001 / peng-2023-copilot-productivity | A narrow randomized coding task was completed 55.8% faster with Copilot | E2 / 0.90 | Strong positive task-level evidence |
| LABOR-2024-001 / chatterjee-2024-anz-copilot-study | ANZ coding challenges were completed about 42% faster | E2 / 0.85 | Positive organizational experiment, still narrow |
| LABOR-2025-017 and SOC-2025-003 / metr-2025-ai-experienced-os-dev-productivity | Experienced maintainers took 19% longer in a realistic RCT while believing they were faster | E3 / 0.85 | Shows context and user belief can reverse benchmark intuition |
| LABOR-2025-018 / humlum-2025-llms-small-labor-market-effects | Danish administrative data found no earnings/hours effect above ~2% after two years, alongside task restructuring | E3 / 0.85 | Early diffusion is transformation, not near-total displacement |
| LABOR-2026-001 / standard-economics | If AI substitutes for humans in most tasks, wages fall and capital share rises | E3 / 0.85 | Supports Plan A’s distribution concern conditionally |
| ECON-2026-927 / aleximas-2026-negative-economic-growth | Labor-share collapse can create demand-side shortfalls even as productive capacity rises | E5 / 0.45 | A counter-model to automatic explosive realized output |
| ECON-2026-932 / aleximas-2026-negative-economic-growth | Broad capital ownership could stabilize demand better than transfers alone | E5 / 0.40 | Extends the dividend into an ownership question |
| RESOURCE-2026-001 / iea-2024-energy-ai | Data-center electricity demand is projected to rise sharply through 2030–2035 | E1 / 0.85 | Supports energy salience; does not validate Plan A’s 2040 scale |
| RISK-2026-926 / openai-2026-gpt-5-3-codex-system-card | Robust long-range-autonomy evaluations and thresholds were still lacking; proxies were used | E4 / 0.80 | Current assurance instrumentation is immature |
| RISK-2026-916 / anthropic-2026-claude-opus-4-6-system-card | Anthropic judged Opus 4.6 below AI-R&D-4/CBRN-4 while warning future thresholds are harder to rule out | E4 / 0.65 | Neither “already automated R&D” nor “no serious trajectory” is supported |

Two points follow. First, current empirical data are compatible with rapid improvement and meaningful economic use. Second, they do not identify the scenario’s key conversion factor from selected digital-task gains to universal, reliable, embodied, strategically dominant labor.

### Disconfirming evidence search

| Crux | Counterevidence or qualification found | Alternative explanation | Search record |
|---|---|---|---|
| Rapid coding progress implies broad R&D automation | Cross-domain METR results show 40–100× shorter GUI horizons; realistic developer work has produced both large gains and a 19% slowdown | Software is unusually legible, copyable, and benchmarkable; other domains may catch up later but at different rates | RC semantic queries for research automation/physical bottlenecks; direct METR; DuckDuckGo and OpenAlex queries |
| Task gains imply near-term labor displacement | The revised NBER paper finds widespread task change but no earnings/hours effects above ~2% after two years; ILO says one in four workers has some exposure but job transformation is more likely than replacement | General-purpose technologies often require complementary investment and organizational redesign before aggregate effects emerge | RC labor query; OpenAlex labor queries; [NBER WP 33777](https://www.nber.org/papers/w33777); [ILO 2025](https://www.ilo.org/publications/generative-ai-and-jobs-refined-global-index-occupational-exposure) |
| Automation implies explosive aggregate growth | Acemoglu estimates less than 0.53% TFP gain over ten years under evidence-based current-task assumptions; Imas supplies demand and capital-decumulation failure modes | Those models may radically understate post-AGI capability, but they demonstrate that “more capable” does not mechanically determine realized GDP | OpenAlex macro/growth queries; RC growth query; [Acemoglu 2024](https://doi.org/10.1093/epolic/eiae042) |
| Compute governance makes the regime enforceable | Compute research supports the lever but highlights low-compute narrow models, algorithmic progress, consumer chips, evasion, workload-identification limits, privacy, and centralization | A deliberately narrow industrial-cluster regime may retain most benefits if dangerous capability remains scale-dependent | RC compute query; OpenAlex compute queries; [Sastry et al.](https://arxiv.org/abs/2402.08797); [AIGI](https://aigi.ox.ac.uk/publications/verification-for-international-ai-governance/) |
| Strong verification makes the treaty durable | Coe and Vaynman find arms control rare because enough transparency to assure compliance can also threaten security; Plan A needs exceptionally invasive access | Fortna finds agreement design, guarantees, peacekeeping, and joint commissions can causally improve durability; failure is not inevitable | RC treaty query returned no close records; two OpenAlex treaty queries; [Coe & Vaynman 2019](https://doi.org/10.1017/S000305541900073X); [Fortna 2003](https://doi.org/10.1017/S0020818303572046) |
| Alignment research can justify handoff | Alignment-faking and in-context-scheming demonstrations show strategically deceptive behavior under constructed incentives; emergent misalignment shows narrow training can generalize unexpectedly | AI-control protocols also outperform simple baselines in a restricted coding setup, so empirical risk reduction is possible even without solved motives | RC alignment query; two OpenAlex alignment queries; [alignment faking](https://arxiv.org/abs/2412.14093); [scheming](https://arxiv.org/abs/2412.04984); [AI control](https://arxiv.org/abs/2312.06942) |

None of the near-term studies refutes a discontinuous future system with far greater capability. That is precisely the point: evidence about current systems can calibrate extrapolation, but it cannot validate the extrapolated endpoint. “Future systems will be different” preserves possibility, not probability.

### Corrections, updates, and capture issues

| Item | Date checked | Finding | Impact |
|---|---|---|---|
| NBER WP 33777 | 2026-07-11 | The paper is now titled “Still Waters, Rapid Currents: Early Labor Market Transformation under Generative AI,” revised March 2026; the RC record retains its previous title. The core null earnings/hours result remains on the current page | Cite the current title; retain the substantive evidence |
| Installed rc-db entry point | 2026-07-11 | Broken interpreter path | Used the framework’s uv-run fallback; no database mutation |
| Initial semantic search | 2026-07-11 | Blocked by uncached embedding model plus SOCKS proxy dependency | Recorded as blocked; retried with proxy variables removed, after which read-only semantic search succeeded |
| IEA public page capture | 2026-07-11 | Direct HTML access returned a JavaScript/cookie challenge | Treated direct recapture as blocked; used the existing RC evidence record and did not elevate it into a new crux |
| External discovery | 2026-07-11 | General HTML search was inconsistent after the first query | Used OpenAlex, Crossref, direct publisher/arXiv pages, and neutral disconfirming terms |
| AI 2040 corpus | 2026-07-11 | No source files changed during this check | Source manifest does not need rebuilding for this root-level analysis |

### Internal tensions and self-contradictions

| Tension | Parts in conflict | Implication |
|---|---|---|
| Conditional forecast vs narrative momentum | “Implementation is not predicted” vs confident future-tense scenes and charts | Readers can remember the story as a forecast even when the caveat is explicit |
| Transparency vs nonproliferation | Publish essentially all AI R&D vs keep defectors behind | The security/transparency tradeoff is central and cannot be optimized by assertion |
| Diffusion vs control | Spread access across firms/countries vs tightly monitor dangerous use | Pluralism and attack surface rise together |
| Reversible hardware vs catastrophic overhang | Hardware is governable and destructible vs a 10,000× buildout could compress a one-year takeoff below a day if destruction fails | Plan A manufactures a correlated tail risk and then relies on unprecedented failsafes |
| Deal fragility vs dependence on the deal | Roughly 48% ten-year decline estimate vs a decade of hardware accumulation and coordination | Exit, succession, and false-alarm design are first-order safety engineering |
| Use stronger AI to solve AI safety | Scaling provides enormous safety labor vs every capability step can increase takeover and covert-project risk | The optimal stopping point cannot be known from the model alone |
| Anti-concentration vs inspection state | Multiple labs, broad access, and public methods vs global chip tracking, audits, licensing, intelligence, and possible lie detection | A regime built to prevent private dictatorship could enable public or cartelized domination |
| Dividend vs democratic power | Cash replaces lost wages vs production, expertise, coercion, and agenda setting remain concentrated | Consumption security does not automatically preserve bargaining power or sovereignty |
| Alignment endpoint vs roadmap status | “Alignment is now a science” in the story vs a supplement labeled rough, in-progress internal notes | Detailed research categories are not evidence that the terminal criterion is achievable |
| Economic precision vs model disclaimer | Exact GDP, robots, energy, prices, and dividends vs “we don’t expect the numbers here to be right” | Charts illustrate implications of inputs; they should not update confidence like measured forecasts |
| Truth tools vs persuasion risk | Personal AIs improve epistemics vs cheap individualized persuasion and political optimization | The sign of the democratic effect is an empirical question |

The hardware tension is the sharpest. The assumptions supplement gives a naive calculation that 10,000× compute could turn a one-year takeoff into one lasting less than a day. The same package gives substantial probability to treaty decline. Mutually assured compute destruction is therefore not a colorful detail; it is one of the plan’s highest-assurance requirements.

### Persuasion and rhetoric audit

| Technique | Example | Effect | Assessment |
|---|---|---|---|
| Narrative concreteness | Dates, dialogue, branch points, personal perspectives, and dashboard figures | Makes causal structure memorable and inspectable | Valuable for scenario scrutiny; can hide that transitions were stipulated |
| Numerical anchoring | Exact robot counts, dividends, GDP, covert risk, and treaty hazards | Creates an impression of a measured system | Often useful sensitivity bookkeeping; precision exceeds calibration |
| Catastrophic contrast | Race leads to takeover, dictatorship, war, or mass disempowerment | Raises the cost of dismissing the proposal | Relevant if premise holds; can narrow attention away from muddling-through and hybrid paths |
| Conditional compression | “If recommendations are implemented, subsequent effects are predictions” | Converts a long conjunction into a smooth story | Conditions need to be re-expanded at every load-bearing transition |
| Self-critique and caveats | Rough-draft warnings, uncertainty intervals, failure branches, model limitations | Increases trust and exposes real weaknesses | Genuinely epistemically helpful, though caveats are less salient than the main narrative |
| Scenario-scrutiny challenge | Critics are asked to supply comparably concrete alternatives | Correctly raises the bar above vague optimism | It does not make Plan A probable merely because alternatives are underspecified |
| Utopian floor | The epilogue offers a minimum acceptable post-ASI future | Reframes distribution as something humanity can demand | Normatively provocative, empirically the least grounded part |

This is not a finding that the authors are deceptive. Their epistemic disclosures are better than those of most public future scenarios. The concern is a property of the form: a coherent story is cognitively easier to process than a dependency graph with wide error bars.

### Unstated or under-modeled assumptions

| Assumption | Depends on | Critical? | Problematic? |
|---|---|---:|---:|
| Software-agent progress generalizes to scientific judgment, strategy, institutions, and physical systems | TECH-2026-102/002 | Y | Y |
| Superhuman cognition converts quickly into decisive real-world power | RISK-2026-992 | Y | Y |
| Warning signs become politically legible before automation makes enforcement harder | GEO-2026-061 | Y | Y |
| US and Chinese leaders converge on a shared threat model despite incentives to exaggerate or conceal | GEO-2026-061 | Y | Y |
| Domestic emergency politics do not turn the slowdown into executive or corporate capture | GOV-2026-293 | Y | Y |
| Third states, open models, private actors, and new chip suppliers remain below the dangerous frontier | GOV-2026-291/RISK-2026-993 | Y | Y |
| Strategically dangerous progress continues to require conspicuous industrial compute | GOV-2026-291 | Y | Y |
| Verification devices, inspectors, and logs survive nation-state cyberattack and advanced-AI manipulation | TRANS-2026-058 | Y | Y |
| Compute/fab/robot destruction is technically reliable, politically authorized, and not falsely triggered | TRANS-2026-058 | Y | Y |
| Transparency leakage, distillation, and stolen weights do not erase the legal projects’ lead | GOV-2026-292 | Y | Y |
| Energy, grid, fabs, mines, construction, capital goods, and logistics scale with the modeled robot/compute path | ECON-2026-990 | Y | Y |
| New demand, finance, trade, prices, and institutions do not qualitatively change the growth path | ECON-2026-990 | Y | Y |
| Cash transfers remain enforceable after citizens lose labor leverage | GOV-2026-293 | Y | Y |
| Broad AI access distributes political power rather than merely consumption services | GOV-2026-293/004 | Y | Y |
| Safety research scales with AI labor faster than evaluation and human-understanding bottlenecks | RISK-2026-994/TECH-2026-104 | Y | Y |
| Multiple safety cases are sufficiently independent to avoid common-mode conceptual failure | RISK-2026-995 | Y | Y |

### Evidence assessment by module

| Module | Best evidence | Evidence level | Assessment |
|---|---|---|---|
| Current agent progress | Open benchmark data, updated suites, selected RCTs | E2–E3 | Real and rapid in some settings; external validity is the crux |
| Full R&D automation and takeoff | Forecast model and expert judgment | E5 | Explicit, operationalizable in parts, still highly uncertain |
| AI takeover / decisive power | Conditional strategic argument and early scheming demonstrations | E4–E5 | A serious risk hypothesis, not an empirically estimated probability |
| Compute governance | Multidisciplinary analysis and early technical work | E3 | Strongest implementation premise in direction; assurance and coverage unresolved |
| Treaty adoption/durability | Historical analogies, small dataset, judgmental weighting | E5 | Better than pure intuition; not a calibrated base rate for Plan A |
| Covert projects | Bottom-up modeling and intelligence analogies | E5 | Useful attack-surface map; headline risk is conditional and fragile |
| Economic/physical trajectory | Exogenous scenario explorer with extensive caveats | E6 for dates/magnitudes | Consistency tool, not evidence for the assumed transformation |
| Labor/distribution | Standard substitution theory plus early mixed empirical evidence | E2–E3 for direction under conditions; E5 for timing | Redistribution concern is robust; near-total automation timing is not |
| AI control | Restricted experimental protocols and research agenda | E3 | Promising for bounded deployment; far from top-expert assurance |
| Alignment/handoff | Early empirical anomalies, conceptual proposals, rough roadmap | E3 for problem demonstrations; E6 for 2040 solution | The endpoint is a placeholder with research attached |
| Democratic legitimacy | Normative design and scenario assertions | E5–E6 | Underdeveloped relative to the technical regime |

### Credence assessment

There is no single honest “probability AI 2040 is true,” because it mixes facts, forecasts, conditionals, and recommendations.

- **Credence in the descriptive reading above:** 0.90.
- **Credence that the scenario identifies important real governance problems:** 0.85.
- **Credence that industrial compute governance is a material part of a workable safety regime:** 0.65.
- **Credence that the exact Plan A institutional package is viable if seriously attempted:** 0.30.
- **Credence that its full technical-political-economic-handoff chain succeeds conditional on an attempt:** 0.15.
- **Credence that attempting the low-regret near-term portfolio is beneficial:** 0.80.

The 0.15 is not a mechanical multiplication of table entries. Dependencies can make several claims rise or fall together, and future evidence would change the plan. It is a judgment that the chain currently contains multiple low-credence, load-bearing links and no demonstrated terminal alignment result.

---

## Stage 3: Dialectical analysis

### Steelmanned argument

The strongest Plan A argument does not require confidence in every date.

1. Frontier systems are improving quickly enough that automated AI R&D and broad strategic capability deserve serious contingency planning.
2. If the transition is fast, ordinary ex-post regulation arrives too late: the leading lab or state acquires both technical advantage and agenda-setting power before society understands the choice.
3. A unilateral race worsens both major failure modes. It pressures labs to accept weak safety cases, and it concentrates any aligned capability in the winner.
4. Compute is the least-bad coordination handle because frontier work still uses physical, scarce, countable infrastructure supplied by concentrated firms.
5. Early declarations, inspection R&D, reporting, and crisis channels create options. They need not begin with a permanent global constitution.
6. Slower, transparent, plural development lets more evaluators find problems, reduces a single actor’s monopoly, and supplies powerful but bounded AI labor for defense and safety.
7. Automation rents can fund social stability, while plural access and explicit anti-capture rules address the political question that “aligned to whom?” raises.
8. If alignment evidence is inadequate, the pause continues. Plan A is therefore better understood as an adaptive safety architecture than as a commitment to hand off on 31 December 2040.

This steelman is strong enough to justify preparedness. It is not strong enough to justify the massive hardware buildout or irreversible handoff before their own assurance cases exist.

### Strongest counterarguments

1. **The epistemic-chasm problem.** Timothy B. Lee’s reaction locates the foundational disagreement: cognitive superiority does not obviously imply near-omnipotent physical or political power. AI 2040 models the conversion rather than independently establishing it. A bounded-tool world changes every policy tradeoff.

2. **Narrated causation.** Concrete dates force the authors to pick values, but they also make stipulated transitions feel caused. “China proves receptive,” “most states join,” “truth-seeking AIs improve democracy,” and “alignment becomes a science” are conclusions in need of mechanisms.

3. **Political construction and legitimacy.** Anton Leicht’s criticism lands: the story sometimes honors political constraints and elsewhere advances by “what if we just” fiat. Incentive compatibility does not create a ratifying coalition, durable bureaucracy, legitimate inspectors, judicial review, civil-liberties settlement, or public consent.

4. **Verification covers a moving target.** Large clusters can be observable while dangerous algorithms, stolen weights, distilled systems, consumer hardware, specialized models, and future fabs remain difficult. The relevant quantity is not percentage of chips counted but probability that any omitted capability can break the regime.

5. **The overbuild contradiction.** Plan A increases the strategic resource by orders of magnitude and places it behind devices, institutions, and destruction procedures that must work during war, cyber compromise, panic, and withdrawal. This is the proposal’s largest endogenous tail risk.

6. **The anti-dictatorship machinery can become the dictatorship machinery.** Chip registries, workload logs, inference restrictions, inspections, intelligence operations, robot permits, emergency shutdown, and lie detection are a formidable control stack. Privacy-preserving design helps; it does not answer who governs the governors.

7. **The economics does not generate the forecast.** AI capability, robot quantity, and key cost paths drive the model. The Plan A hardware appears before post-hoc affordability checks. Exact output, wage, interest-rate, energy, and dividend numbers are therefore illustrations of selected assumptions.

8. **Dividends solve purchasing power more readily than voice.** A transfer can sustain consumption while owners of compute, land, factories, models, security systems, and political infrastructure retain structural power. Broad or inalienable capital ownership, labor/civic institutions, and enforceable constitutional rights matter independently.

9. **Alignment-by-2038 is a named gap.** Control evaluations, model organisms, behavioral tests, and handoff criteria are valuable research programs. The roadmap itself admits that representative testing, avoiding scheming, and validating hard-to-check conceptual work are unsolved. Recursive trust can recursively propagate error.

10. **Worldview concentration.** A team deeply familiar with AI-risk arguments may be unusually good at designing within that paradigm and unusually likely to share its blind spots. The package needs adversarial co-design by China experts, labor and macro economists, arms-control implementers, civil-liberties lawyers, democratic theorists, and physical-industry operators.

### Public-response audit

The three supplied X responses are short crux locators, not full counter-models. The Hacker News thread contains more detail but no comment scores, so “substantive” is an analytical selection rather than a popularity ranking.

| Critique | Source | Verdict | Why |
|---|---|---|---|
| Superintelligence-to-omnipotence is an intuitive leap | [Timothy B. Lee](../../reference/captured/ai-2040/responses/binarybits-2075660927001608431/thread.md) | **Lands as a crux** | The package supplies mechanisms and forecasts, not decisive evidence for the capability-to-power conversion |
| Political disbelief is applied inconsistently | [Anton Leicht](../../reference/captured/ai-2040/responses/anton_d_leicht-2075300220624085241/thread.md) | **Lands** | Adoption and legitimacy receive less mechanism than technical verification |
| Plan D is the actual plan; fearful government yields Plan C | [0.005 Seconds](../../reference/captured/ai-2040/responses/seconds_0-2075262321266704769/thread.md) | **Plausible direction, weakly argued** | The authors themselves give Plan A low adoption probability, but the response supplies no comparative model |
| This is creative writing / choose-your-own-adventure | [aarondong](https://news.ycombinator.com/item?id=48868939), [bloppe](https://news.ycombinator.com/item?id=48867149) | **Partly misses, partly lands** | Scenario form is disclosed and useful; vividness still distorts perceived probability |
| Current architectures will plateau | [stego-tech](https://news.ycombinator.com/item?id=48866755), [charcircuit](https://news.ycombinator.com/item?id=48868859) | **Insufficient as stated** | Plan A does not require today’s architecture forever; the stronger objection is lack of cross-domain evidence |
| Non-aligned states and wealthy rogue actors defeat the deal | [SilentM68](https://news.ycombinator.com/item?id=48867904) | **Lands conditionally** | The plan answers with timing, scale, and supply-chain tracking; whether the dangerous threshold stays industrial is unresolved |
| Plan A and Plan C contradict each other on covert projects | [Jawiggins](https://news.ycombinator.com/item?id=48852619) | **Mostly answered** | They concern different stages; the unresolved issue is whether the early controllable window exists and lasts |
| The regime becomes a global police state | [Modeless](https://news.ycombinator.com/item?id=48850862) | **Lands, with first-party mitigations** | Multiple labs and privacy safeguards matter, but institutional accountability remains thin |
| Compute and industrial buildout are physically implausible | [oezi](https://news.ycombinator.com/item?id=48852241), [ibaikov](https://news.ycombinator.com/item?id=48849091) | **Lands against numerical confidence** | The model assumes Plan A quantities and cannot independently settle feasibility |
| Dividends leave humans peripheral | [Paradox242](https://news.ycombinator.com/item?id=48868418) | **Lands** | Income, ownership, bargaining power, meaning, and constitutional agency are distinct |
| Humanity has never successfully restrained dangerous knowledge | [joshstrange](https://news.ycombinator.com/item?id=48849070) and replies | **Too absolute** | Nuclear controls, biological norms, and facility regulation provide partial precedents; transfer to software is the real question |
| The prose is AI-generated | HN speculation | **Does not land as stated** | Credits disclose AI assistance and say humans wrote nearly all final prose; model/code and treaty-analysis use are the substantive audit targets |

### Supporting theories and evidence

| Theory / evidence | Source | How it supports Plan A |
|---|---|---|
| Rapid growth in selected autonomous-task horizons | [METR](https://metr.org/blog/2025-03-19-measuring-ai-ability-to-complete-long-tasks/) | Makes automated R&D a serious planning contingency |
| Compute as detectable, excludable, quantifiable, concentrated | [Sastry et al.](https://arxiv.org/abs/2402.08797) | Supports compute as a better lever than ideas or talent |
| Layered international AI verification | [Harack et al.](https://aigi.ox.ac.uk/publications/verification-for-international-ai-governance/), [Baker et al.](https://arxiv.org/abs/2507.15916) | Shows technically serious pathways rather than pure treaty handwaving |
| Agreement design affects durability | [Fortna](https://doi.org/10.1017/S0020818303572046) | Incentives, third-party guarantees, commissions, and monitoring can causally improve peace |
| AI control can improve on naive baselines | [Greenblatt et al.](https://arxiv.org/abs/2312.06942) | Supports bounded use of untrusted systems under layered protocols |
| Automation can reduce labor share and demand | Acemoglu–Restrepo task framework; RC LABOR-2026-001 | Supports treating distribution and ownership as core safety issues |

### Contradicting or limiting theories and evidence

| Theory / evidence | Source | Point of conflict |
|---|---|---|
| Domain-dependent task horizons | [METR cross-domain](https://metr.org/blog/2025-07-14-how-does-time-horizon-vary-across-domains/) | Software trend does not map cleanly to GUI, robotics, or institutions |
| Mixed real-world productivity and limited aggregate labor effects | [METR developer RCT](https://metr.org/blog/2025-07-10-early-2025-ai-experienced-os-dev-study/); [NBER WP 33777](https://www.nber.org/papers/w33777); [ILO](https://www.ilo.org/publications/generative-ai-and-jobs-refined-global-index-occupational-exposure) | Present evidence supports heterogeneous augmentation and task change, not a calibrated date for full automation |
| Modest macro effects under current evidence | [Acemoglu 2024](https://doi.org/10.1093/epolic/eiae042) | Exact explosive-growth claims require a regime break, not extrapolation of existing studies |
| Demand and capital-decumulation bottlenecks | RC source aleximas-2026-negative-economic-growth | Productive capacity need not translate one-for-one into realized output |
| Monitoring–security tradeoff in arms control | [Coe & Vaynman](https://doi.org/10.1017/S000305541900073X) | Intrusive verification can itself threaten state security and prevent agreement |
| Scheming, alignment faking, and emergent misalignment | [Greenblatt et al.](https://arxiv.org/abs/2412.14093); [Meinke et al.](https://arxiv.org/abs/2412.04984); [Betley et al.](https://arxiv.org/abs/2502.17424) | Current training and evaluation do not support high-assurance intent claims |
| Narrative probability bias | RC source marcus-2025-ai-2027-scenario-how-realistic | A vivid conjunction may feel likelier than its weakest links warrant |

### Synthesis

The fairest interpretation is:

- **As a forecast:** low confidence. Dates and magnitudes are selected for a scenario and inherit large uncertainty from capability, politics, economics, and alignment.
- **As a threat model:** credible enough to matter. Automated R&D, concentrated power, model theft, weak safety cases, and geopolitical racing are legitimate planning concerns even at much lower probabilities.
- **As an institutional design:** unusually valuable but incomplete. It connects technical and political components, yet legitimacy and failure recovery need the same depth as verification.
- **As a policy portfolio:** heterogeneous. Several preparations are low regret; the hardware explosion, invasive monitoring, autonomous militaries, and handoff require much stronger gates.

The central analytical update is not “Plan A works” or “Plan A is fantasy.” It is that **cooperative slowdown has now been specified well enough to separate robust components from speculative ones**.

### Decision-oriented decomposition

| Bucket | Actions | Standard of proof |
|---|---|---|
| **Do now** | Government technical hiring; large-cluster/chip visibility; model-spec and internal-use reporting; independent safety-case capacity; verification R&D; bio/cyber defense; crisis channels; distribution and ownership planning | Ordinary policy analysis with privacy, competition, and due-process safeguards |
| **Prototype and red-team** | Chip registry; privacy-preserving workload logs; inference-only verification; mutually audited datacenters; multiple independent assessors; international inspection protocols; sovereign wealth/dividend mechanisms | Adversarial technical testing, legal design, cost estimates, and limited pilots |
| **Require strong evidence before commitment** | Near-total compute declaration; total research transparency; remote disablement; compute destruction; massive hardware overbuild; high-risk inference monitoring; AI lie detection | Demonstrated coverage, security, false-positive tolerance, democratic authorization, and reversible trials |
| **Do not schedule by date** | Alignment declaration, inductive handoff, autonomous constitutional militaries, irreversible delegation | Capability- and evidence-based gates with a credible option to remain paused |

### What would materially update this assessment

**Toward Plan A**

- autonomous AI teams complete multi-month, end-to-end AI research projects with measured large productivity gains and low human oversight;
- cross-domain horizons converge rather than retaining orders-of-magnitude gaps;
- prototype verification survives adversarial hardware, network, insider, and nation-state testing;
- the US, China, and third states negotiate concrete inspection or incident-notification measures;
- independent economic models with investment, grids, supply chains, trade, finance, demand, and political constraints reproduce the broad growth path;
- control evaluations generalize from toy coding settings to real lab deployments;
- multiple independent methods predict alignment and survive deliberate attempts to game them.

**Away from Plan A**

- dangerous capability becomes cheap on diffuse or consumer hardware;
- algorithmic efficiency or stolen weights erase the compute advantage faster than monitoring adapts;
- software-agent trend saturates or fails to translate into real R&D throughput;
- inspection requirements prove incompatible with state security, privacy, or domestic law;
- early compute-governance systems are captured, selectively enforced, or routinely bypassed;
- physical bottlenecks keep robot/compute deployment far below assumed paths;
- advanced models systematically defeat representative control tests or collude across monitors.

### Claims to cross-reference

- AI Futures Model milestone definitions and out-of-sample calibration.
- Independent replications of METR time-horizon and developer-productivity results.
- Current chip-stock, smuggling, fab, grid, and datacenter construction estimates.
- Historical treaty dataset coding, weights, censoring, and sensitivity analysis.
- China-specific views of intrusive inspections, strategic stability, and domestic legitimacy.
- Macro models with endogenous demand, finance, trade, capital ownership, and political response.
- Red-team evidence for inference-only verification and compute-destruction mechanisms.
- Control protocols against situational awareness, collusion, and monitor compromise.
- Operational criteria for “alignment mature enough to hand off.”

---

## Claim summary

| ID | Type | Domain | Layer | Actor | Scope | Quantifier | Evid | Credence | Claim |
|---|---|---|---|---|---|---|---|---:|---|
| META-2026-168 | [F] | META | ASSERTED | OTHER:AIFP | framing | N/A | E4 | 0.99 | Plan A is a recommendation and conditional success scenario, not the modal forecast |
| META-2026-169 | [F] | META | ASSERTED | OTHER:AIFP | economic model | most | E4 | 0.98 | Plan A economic outputs are driven by largely exogenous trajectories and should be read as illustrative |
| META-2026-170 | [F] | META | PRACTICED | OTHER:AIFP | treaty method | N/A | E4 | 0.95 | Deal-decline estimates combine a 31-agreement Claude-assisted base-rate exercise with judgmental adjustments and decomposition |
| META-2026-171 | [F] | META | ASSERTED | OTHER:AIFP | internal estimates | N/A | E4 | 0.98 | The authors report about 5% Plan A adoption in one decomposition, 37%/48% deal decline, 13% conditional covert failure, and 42% chance of a great future under one rough assessment |
| META-2026-172 | [F] | META | ASSERTED | OTHER:AIFP | team background | most | E4 | 0.90 | The core team’s demonstrated expertise is concentrated in AI safety, forecasting, compute, and policy |
| TECH-2026-102 | [P] | TECH | ASSERTED | OTHER:AIFP | AI R&D by ~2041 | most | E5 | 0.45 | AI R&D will be fully automated within about 15 years absent interruption |
| TECH-2026-103 | [P] | TECH | EFFECT | OTHER:AIFP | post-R&D automation | most | E5 | 0.25 | Broadly superhuman economic capability follows within a few years |
| TRANS-2026-057 | [P] | TRANS | ASSERTED | OTHER:AIFP | takeoff | OTHER:~1y median | E5 | 0.25 | Automated coding to top-expert-dominating AI takes roughly one year at the median |
| RISK-2026-992 | [H] | RISK | EFFECT | OTHER:AIFP | conditional strategic risk | some | E5 | 0.65 | Vastly superhuman collectively adversarial AIs could defeat human control |
| GEO-2026-061 | [P] | GEO | PRACTICED | OTHER:US/PRC | by 2030 | some | E5 | 0.10 | Something close to Plan A can be adopted around 2029 |
| GOV-2026-291 | [H] | GOV | PRACTICED | OTHER:Consortium | strategic compute | most | E3 | 0.40 | About 99% of strategically relevant compute can be declared and monitored |
| GOV-2026-292 | [H] | GOV | EFFECT | OTHER:Consortium | frontier R&D | N/A | E5 | 0.50 | Total research transparency has net safety and diffusion benefits |
| RISK-2026-993 | [P] | RISK | EFFECT | OTHER:defectors | 2029–2040 | OTHER:13% failure | E5 | 0.30 | Covert projects remain detectably behind under competent implementation |
| TRANS-2026-058 | [H] | TRANS | EFFECT | OTHER:Consortium | hardware stock | most | E4 | 0.35 | Hardware-led scaling is meaningfully reversible |
| ECON-2026-990 | [P] | ECON | EFFECT | OTHER:world | by 2040 | OTHER:200–270x | E6 | 0.10 | Plan A AI and robot paths produce roughly 200–270× world output |
| LABOR-2026-041 | [P] | LABOR | EFFECT | OTHER:AI/robots | mid-2030s | most | E5 | 0.20 | Most economically valuable labor can be automated by the mid-2030s |
| GOV-2026-293 | [H] | GOV | EFFECT | OTHER:states/citizens | post-work | most | E5 | 0.35 | Dividends, broad AI access, and transparency preserve public power |
| RISK-2026-994 | [P] | RISK | EFFECT | OTHER:AI projects | through top-expert AI | most | E3 | 0.30 | Control-based safety cases contain pre-handoff systems |
| TECH-2026-104 | [P] | TECH | EFFECT | OTHER:alignment field | by 2038–2040 | N/A | E6 | 0.15 | AI-assisted work makes alignment a mature enough science for handoff |
| RISK-2026-995 | [H] | RISK | EFFECT | OTHER:successor AIs | post-handoff | most | E6 | 0.15 | Trust can be propagated safely through successive AI generations |
| GOV-2026-294 | [H] | GOV | EFFECT | OTHER:citizens/platforms | broad deployment | most | E5 | 0.35 | Truth-seeking AIs improve democratic epistemics on net |
| GOV-2026-295 | [T] | GOV | PRACTICED | OTHER:governments | near term | N/A | E3 | 0.80 | Build public technical capacity, visibility, verification, and defensive resilience |
| GOV-2026-296 | [T] | GOV | PRACTICED | OTHER:regulators | large clusters | N/A | E3 | 0.75 | Prototype compute accounting and verification with privacy, due process, and anti-capture safeguards |
| ECON-2026-991 | [T] | ECON | PRACTICED | OTHER:states/citizens | automation transition | N/A | E3 | 0.80 | Plan for ownership, bargaining power, public goods, and income—not dividends alone |
| RISK-2026-996 | [T] | RISK | PRACTICED | OTHER:labs/governments | pre-handoff | N/A | E3 | 0.80 | Require adversarially validated, independent safety cases and retain the option not to hand off |

## Claims artifact

The canonical source and 25 registered claims are defined in [the companion YAML](aifutures-2026-ai-2040-plan-a.yaml). Existing METR and compute-verification findings used for calibration remain cross-references rather than duplicate claim registrations.

---

**Analysis date:** 2026-07-11
**Analyst:** Codex / GPT-5
**Credence in analysis:** 0.86

**Credence reasoning**

- High confidence in source characterization because the full primary package, PDF, supplements, models, credits, and response corpus are local and auditable.
- Moderate confidence in external evaluation because current evidence is strong for selected present-day facts but cannot resolve future capability or alignment transitions.
- Lower confidence in exact numerical credences; they are decision aids and should be updated as the listed milestones resolve.

## Analysis log

| Pass | Date | Tool / model | Duration | Tokens | Cost | Notes |
|---:|---|---|---|---:|---:|---|
| 1 | 2026-07-11 | Codex / GPT-5 | not tracked | not available | not available | Adapted $check workflow; analyzed local corpus; queried Reality Check DB read-only; performed direct and disconfirming external checks; drafted standalone claim ledger and YAML |
| 2 | 2026-07-14 | Codex / GPT-5 | lifecycle tracked | unavailable | unavailable | Canonicalized claim IDs and types; archived cited source artifacts; registered source, claims, evidence links, reasoning trails, and analysis log; validated and indexed the result |

### Revision and provenance notes

- Pass 1 was intentionally standalone; pass 2 completed the canonical database integration requested by the user.
- The installed `rc-db` launcher was broken, so the framework’s `uv run python scripts/db.py` fallback was used.
- Initial semantic search in pass 1 was blocked by the uncached model/proxy setup. A proxy-free retry succeeded. Pass 2 reused the recorded DB results and performed direct record queries when semantic model loading failed again.
- External discovery used DuckDuckGo once, OpenAlex, Crossref, direct publisher pages, arXiv, and the existing Reality Check evidence corpus.
- This file separates source assertions, current facts, predictions, assumptions, and recommendations. Future claims are not labeled verified merely because they appear in a detailed model.
- The canonical repository retains the published PDF and a curated, hash-verified capture of every local source artifact cited here.
- Scoped integration checks passed for YAML/Markdown claim parity, foreign keys, active evidence paths, local Markdown links, required high-credence provenance, and source-corpus hashes. Repository-wide validation still reports pre-existing schema/ID errors and missing embeddings; this integration introduces no new structural error, while its 25 claim embeddings remain deferred with the currently unavailable shared embedding model.
- Overlapping fallback-CLI evidence batches produced 15 exact duplicates. They are retained for append-only audit history, superseded by explicit zero-weight tombstones, and excluded from reasoning-trail evidence sets.
