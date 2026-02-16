# Source Analysis: How Generative and Agentic AI Shift Concern from Technical Debt to Cognitive Debt

> **Claim types**: `[F]` fact, `[T]` theory, `[H]` hypothesis, `[P]` prediction, `[A]` assumption, `[C]` counterfactual, `[S]` speculation, `[X]` contradiction  
> **Evidence**: **E1** systematic review/meta-analysis; **E2** peer-reviewed/official stats; **E3** preprint/working paper w/ methods; **E4** credible journalism/industry; **E5** opinion/anecdote; **E6** unsupported/speculative

## Metadata

| Field | Value |
|---|---|
| **Source ID** | `storey-2026-cognitive-debt` |
| **Title** | How Generative and Agentic AI Shift Concern from Technical Debt to Cognitive Debt |
| **Author(s)** | Margaret-Anne Storey |
| **Date** | 2026-02-09 |
| **Type** | BLOG |
| **URL** | https://margaretstorey.com/blog/2026/02/09/cognitive-debt/ |
| **Reliability** | 0.60 |
| **Rigor Level** | [REVIEWED] |
| **Bias Notes** | Short conceptual blog post by a software-engineering researcher arguing for a reframing (“technical debt” → “cognitive debt”) under generative/agentic AI. Strong on mechanism plausibility + grounded SE lineage (Naur/Brooks) + concrete mitigations; weak on empirical measurement and on disambiguating “cognitive debt” (software shared-theory vs general LLM “cognitive offloading” usage). |

**Claims YAML**: [`analysis/sources/storey-2026-cognitive-debt.yaml`](storey-2026-cognitive-debt.yaml)

## Stage 1: Descriptive Analysis

### Core Thesis
As generative and agentic AI increase development speed, the dominant long-run risk shifts from “technical debt in code” to “cognitive debt in people”: the loss of shared understanding (“theory”) of what the system is, why it is that way, and how to change it safely.

### Summary (Neutral)
Storey contrasts *technical debt* (design/implementation shortcuts that later make software harder to change) with a newer term, *cognitive debt*, meant to emphasize that the limiting factor is often not the code itself but developers’ shared understanding. She argues that even if AI agents can generate locally readable code, teams can still “lose the plot”: no one can explain why decisions were made, how parts fit together, or what the system is supposed to do.

She grounds the idea in classic software-engineering lineage: Peter Naur’s view that “a program is a theory” built and held in developers’ minds (and distributed across a team), and Fred Brooks’ observation that adding people increases coordination overhead. She gives an anecdote from teaching: a student team hit a wall not because code was messy per se, but because their shared understanding had fragmented.

Storey concludes with mitigations and research questions: slow down, use practices that rebuild shared understanding (pair programming, refactoring, TDD), require human comprehension of AI-generated changes before shipping, document “why” not just “what,” and develop ways to detect cognitive debt early (fear of changes, over-reliance on tribal knowledge, black-box feelings). She flags cognitive-debt measurement and scaling (distributed/open-source) as open research problems.

### Key Claims

| # | Claim | Claim ID | Type | Domain | Evidence | Credence | Verified? | Falsifiable By |
|---:|---|---|---|---|---|---:|---|---|
| 1 | Storey defines “cognitive debt” (in AI-augmented software work) as the loss/fragmentation of developers’ shared understanding of what the system does, why decisions were made, and how to change it safely | META-2026-137 | [F] | META | E5 | 0.90 | source | The article does not define cognitive debt in terms of shared understanding/theory loss |
| 2 | As generative/agentic AI adoption rises, cognitive debt will become a bigger threat to long-term software health than technical debt | META-2026-138 | [P] | META | E5 | 0.55 | ? | Empirical studies of AI-augmented teams find maintainability failures are dominated by code-level debt and not by erosion of shared understanding |
| 3 | Peter Naur’s “Programming as Theory Building” argues that software development is fundamentally about building a theory in programmers’ minds; a program is more than its source text | META-2026-139 | [F] | META | E4 | 0.90 | ok | Naur’s paper does not argue for “theory building” as the primary aim of programming |
| 4 | Even if AI-generated code is locally understandable, teams can still “lose the plot”: humans may not understand intentions, rationale, or interactions well enough to change the system without regressions | META-2026-140 | [H] | META | E5 | 0.60 | ? | Controlled studies show AI-generated change explanations and artifacts reliably preserve or improve system-level understanding over time |
| 5 | Brooks’ Law / *The Mythical Man-Month* implies adding more people/agents increases coordination overhead and cognitive load, which can reduce overall velocity | META-2026-141 | [F] | META | E4 | 0.90 | ok | Brooks does not claim added manpower increases coordination overhead / makes late projects later |
| 6 | Practices like pair programming, refactoring, and test-driven development can mitigate cognitive debt by rebuilding and distributing shared understanding | META-2026-142 | [H] | META | E5 | 0.60 | ? | Comparisons of teams with/without these practices show no differences in shared understanding retention or change-safety under AI-assisted development |
| 7 | A practical mitigation is to require at least one human to fully understand each AI-generated change before shipping, and to document “why” not just “what” | META-2026-143 | [H] | META | E5 | 0.55 | ? | Adding “human-understands” gates does not reduce regressions/maintenance time and does not improve comprehension measures |
| 8 | Cognitive-debt warning signs include hesitation to change due to fear, over-reliance on tribal knowledge held by a few, and a growing sense the system is a black box | META-2026-144 | [H] | META | E5 | 0.65 | ? | These signals do not predict maintainability or shared-understanding collapse in AI-augmented teams |

### Argument Structure

```
AI/agents increase speed and volume of change
        ↓
Velocity can exceed human/shared understanding capacity
        ↓
Shared theory of the system erodes (“cognitive debt” accumulates)
        ↓
Teams lose ability to change safely (paralysis, regressions, black-boxing)
        ↓
Conclusion: mitigate + detect cognitive debt; research measurement and scaling
```

### Theoretical Lineage
- **Programming as theory building** (Naur): emphasizes internalized, distributed understanding as the “real” program.
- **Coordination overhead** (Brooks): added contributors amplify communication/decision complexity.
- **Extreme Programming / continuous design** (Beck): practices intended to keep change safe by making system evolution comprehensible.
- **Cognitive load / distributed cognition** (implicit): shared mental models as a bottleneck under accelerating iteration.

### Scope & Limitations
- Primarily conceptual + anecdotal; does not provide an operational definition or measurement recipe for cognitive debt.
- “Cognitive debt” is potentially overloaded: other communities use it to mean *cognitive offloading harms* (e.g., LLM-assisted writing), which is related but not identical.
- Treats “AI-generated code could be easy to understand” as a plausible premise, but does not analyze tool design features (e.g., change rationales, tests, specs) that might reduce cognitive debt.

## Stage 2: Evaluative Analysis

### Internal Coherence
The core mechanism is coherent: if the marginal cost of producing and merging code drops while the cost of reconstructing “why” stays high, teams can accumulate a backlog of unintegrated rationale and mismatched mental models. The article’s “cognitive debt” framing usefully distinguishes (a) *code quality* from (b) *shared theory quality*.

The main weakness is empirical: the post asserts *relative magnitude* (“bigger threat than technical debt”) without measurement, and it does not cleanly separate “understanding debt” from other failure modes (testing gaps, unclear requirements, accountability incentives).

### Key Factual Claims Verified

| Claim ID | Claim (paraphrased) | Crux? | Source Says | Actual | External Source | Search Notes | Status |
|---|---|---:|---|---|---|---|---|
| META-2026-139 | Naur’s “Programming as Theory Building” frames programming as building a “theory” in developers’ minds (program > source text) | **Y** | Cites “a program is a theory” | Naur’s abstract describes the primary aim of programming as having programmers build theories about the problem and solution (beyond the program text) | https://naur.com/papers/ProgAsTheoryBuilding.pdf | q1: “Naur programming as theory building abstract”; q2: “program is a theory Naur quote” (found multiple summaries aligning on the theory-building framing) | ok |
| META-2026-141 | Brooks’ Law states “adding manpower to a late software project makes it later” (coordination overhead) | N | Invokes Brooks’ Mythical Man-Month coordination lesson | Wikipedia entry attributes the quote and describes the coordination/communication overhead rationale | https://en.wikipedia.org/wiki/Brooks%27s_law | q1: “Brooks’s law quote adding manpower late project”; q2: “Mythical Man-Month coordination overhead adding people” | ok |
| META-2026-145 | Thoughtworks hosted an invite-only “future of software development retreat” (Feb 1–3, 2026) hosted by Martin Fowler and Thoughtworks | N | References retreat arranged by Fowler + Thoughtworks | Thoughtworks event page lists “February 1–3, 2026” and “hosted by Martin Fowler and Thoughtworks” | https://www.thoughtworks.com/en-ca/about-us/events/the-future-of-software-development | q1: “future of software development retreat hosted by Martin Fowler Thoughtworks”; q2: “Deer Valley Grand Hyatt February 1–3 2026 Martin Fowler retreat” | ok |
| META-2026-146 | Storey is listed as a TechDebt 2026 keynote speaker; keynote abstract defines cognitive debt as accumulated future mental effort to understand/collaborate around a system in AI-assisted development | N | Mentions exploring in a TechDebt keynote | TechDebt 2026 keynotes page includes Storey and a cognitive-debt abstract consistent with the blog framing | https://conf.researchr.org/attending/TechDebt-2026/keynotes#dr-margaret-anne-storey | q1: “TechDebt 2026 keynote Storey cognitive debt”; q2: “ICSE 2026 TechDebt Storey keynote” | ok |

### Disconfirming Evidence Search

| Claim | Counterevidence Found | Alternative Explanation | Search Notes |
|---|---|---|---|
| META-2026-138 (“cognitive debt” dominates) | Some research suggests LLMs can *improve* comprehension via explanations/comments (e.g., LLM comment generation improving code comprehension) | “Cognitive debt” risk may be conditional on *how* AI is used (prompting vs spec-first) and on review/testing discipline; “local comprehension gains” may still coexist with “system-level theory erosion” | Looked for “LLM comment generation code comprehension study” and “AI-assisted development maintainability cognitive debt”; found academic/working-paper evidence for local comprehension gains but not decisive long-run system-level evidence |
| META-2026-140 (humans lose the plot) | Tooling could plausibly reduce “plot loss” by generating rationale summaries, architecture maps, and traceability from issue→spec→change | The issue may be incentive/governance (shipping pressure) rather than AI per se; AI increases the slope of change volume and therefore stresses existing processes | Searched for “AI-assisted development maintainability study” and “LLM code comprehension summaries explanation”; evidence is sparse on multi-month longitudinal cognition outcomes |

### Internal Tensions / Self-Contradictions
No direct contradictions, but there is a tension between:
- **“AI can make code easier to understand”** and **“humans will lose understanding anyway”**: if the dominant issue is *rationale + shared theory*, the key artifacts may be specs, decision records, tests, and traceability—not code readability alone.

### Persuasion Techniques
| Technique | Example from Source | Effect on Reader |
|---|---|---|
| Anecdote as mechanism exemplar | Student team “hit a wall” due to lost rationale/shared understanding | Makes the concept vivid; risks overgeneralizing from one case |
| Appeal to canonical authorities | Naur + Brooks | Increases plausibility via lineage; still not empirical validation for AI-era dynamics |
| Framing shift | “Debt lives in brains, not code” | Encourages readers to attend to shared cognition rather than just refactoring metrics |

### Unstated Assumptions

| Assumption | Claim ID | Critical? | Problematic? |
|---|---|---:|---:|
| AI adoption increases code/change throughput faster than teams increase practices that preserve shared understanding | META-2026-138 | High | Mixed |
| “Shared theory” is the limiting factor for most long-run maintainability failures (vs tests, specs, incentives) | META-2026-138 | Medium | Yes |
| “At least one human understands each change” is feasible at high velocity without becoming a bottleneck | META-2026-143 | Medium | Mixed |

### Evidence Assessment
- **Strongest**: clear conceptual distinction (artifact debt vs cognition debt) and plausible failure modes under speed pressure; good linkage to established SE thinking about shared understanding.
- **Weakest**: no operational measure, no longitudinal evidence, and ambiguous scope for “cognitive debt” relative to existing constructs (knowledge loss, bus factor, documentation debt, test debt).

### Credence Assessment
- **Overall Credence**: 0.55  
- **Reasoning**: plausible and directionally consistent with known coordination/knowledge-loss dynamics, but magnitude (“bigger threat than technical debt”) is uncertain and needs measurement.

## Stage 3: Dialectical Analysis

### Steelmanned Argument
AI lowers the cost of producing code and encourages faster iteration and parallel change streams. Humans and organizations have bounded capacity to maintain a coherent shared model of a system’s intent, constraints, and invariants. If teams optimize for shipping speed without investing in practices that preserve and refresh shared understanding, they will accumulate “cognitive debt,” leading to risk-averse paralysis, brittle changes, and unbounded reliance on a shrinking set of “keepers of the theory.”

### Strongest Counterarguments
1. **AI can reduce cognitive debt**: agents can summarize changes, generate rationale docs, map dependencies, and tutor new contributors—raising shared understanding rather than lowering it.
2. **This is not new**: “cognitive debt” may mostly rename long-known issues (knowledge loss, bus factor, documentation decay, Conway/coordination effects).
3. **The binding constraint is verification/governance**: in many real systems, tests, specs, and accountability (not mental models) dominate change safety; AI changes the tooling but not the core bottleneck.

### Supporting Theories

| Theory/Framework | Source ID | How It Supports |
|---|---|---|
| Programming as theory building | `storey-2026-cognitive-debt` (via Naur) | Frames “the real program” as shared theory, making “debt in minds” a coherent concept |
| Coordination overhead | `storey-2026-cognitive-debt` (via Brooks) | Predicts that more “agents” (human or AI) increases communication/decision complexity unless structured |

### Contradicting Theories

| Theory/Framework | Source ID | Point of Conflict |
|---|---|---|
| AI improves local comprehension | (external) LLM-assisted comprehension/comment-generation studies | Suggests AI can reduce immediate cognitive burden; may counter “AI inevitably increases cognitive debt” framing |

### Synthesis Notes
“Cognitive debt” is a useful lens if treated as an *organization-level latent variable* (shared-theory integrity) distinct from code-level metrics. The productive next step is to propose measurable proxies (rationale completeness, change explainability, newcomer reconstruction cost) and to test whether AI tools increase or decrease these under different process regimes.

### Claims to Cross-Reference
- Longitudinal studies on AI-assisted maintenance outcomes (multi-month) rather than short tasks.
- Empirical work on knowledge retention / bus factor dynamics under high-churn development.

### Claim Summary

| ID | Type | Domain | Evidence | Credence | Claim |
|---|---|---|---|---:|---|
| META-2026-137 | [F] | META | E5 | 0.90 | Storey defines “cognitive debt” here as the erosion/fragmentation of developers’ shared understanding (“theory”) of a system |
| META-2026-138 | [P] | META | E5 | 0.55 | As generative/agentic AI adoption rises, cognitive debt becomes a larger threat to software health than technical debt |
| META-2026-139 | [F] | META | E4 | 0.90 | Naur’s “Programming as Theory Building” frames programming as building a theory in developers’ minds (program > source text) |
| META-2026-140 | [H] | META | E5 | 0.60 | AI-generated code can be locally clear while system-level understanding erodes (“lose the plot”), impairing safe change |
| META-2026-141 | [F] | META | E4 | 0.90 | Brooks’ Law implies added contributors increase coordination overhead (classic “late project gets later” formulation) |
| META-2026-142 | [H] | META | E5 | 0.60 | Pair programming/refactoring/TDD reduce cognitive debt by rebuilding and distributing shared understanding |
| META-2026-143 | [H] | META | E5 | 0.55 | Requiring at least one human to fully understand each AI-generated change before shipping reduces cognitive-debt accumulation risk |
| META-2026-144 | [H] | META | E5 | 0.65 | Cognitive debt can be detected early via fear-driven change avoidance, tribal-knowledge concentration, and black-box feelings |
| META-2026-145 | [F] | META | E4 | 0.85 | Thoughtworks hosted a Feb 1–3, 2026 “future of software development retreat” hosted by Martin Fowler and Thoughtworks |
| META-2026-146 | [F] | META | E4 | 0.80 | TechDebt 2026 lists Storey as a keynote speaker and defines cognitive debt as accumulated future mental effort to understand/collaborate around software in AI-assisted development |

### Claims to Register

```yaml
claims:
  - id: "META-2026-137"
    text: >-
      Storey defines “cognitive debt” (in this article’s AI-augmented software-engineering context) as the
      erosion/fragmentation of developers’ shared understanding (“theory”) of what a system does, why it is
      built that way, and how to change it safely.
    type: "[F]"
    domain: "META"
    evidence_level: "E5"
    credence: 0.90
    operationalization: "Check the article text for its explicit definition and examples of cognitive debt vs technical debt."
    assumptions: []
    falsifiers:
      - "The article does not define cognitive debt in terms of shared understanding/theory loss."
    source_ids: ["storey-2026-cognitive-debt"]

  - id: "META-2026-138"
    text: >-
      As generative and agentic AI become more widely used in software development, cognitive debt will become
      a bigger threat to long-term software health than technical debt.
    type: "[P]"
    domain: "META"
    evidence_level: "E5"
    credence: 0.55
    operationalization: >-
      Compare AI-augmented teams over multi-month horizons on (a) cognitive-debt proxies (rationale loss,
      explainability of changes, newcomer reconstruction cost) vs (b) code-level technical-debt metrics and
      assess which better predicts incidents, change lead time, and rework.
    assumptions:
      - AI increases code-change throughput faster than teams can maintain shared understanding.
      - Cognitive-debt proxies can be measured consistently across teams.
    falsifiers:
      - Longitudinal studies show technical-debt metrics remain the dominant predictor of maintainability failures under AI adoption.
      - Cognitive-debt proxies do not increase (or improve) with AI adoption when controlling for process discipline.
    source_ids: ["storey-2026-cognitive-debt"]

  - id: "META-2026-139"
    text: >-
      Peter Naur’s “Programming as Theory Building” argues that the primary aim of programming is for
      programmers to build theories about the problem and solution; the “program” is more than its source text
      and lives as theory in developers’ minds.
    type: "[F]"
    domain: "META"
    evidence_level: "E4"
    credence: 0.90
    operationalization: "Read Naur (1985) and confirm the “theory building” framing (e.g., abstract and discussion)."
    assumptions: []
    falsifiers:
      - "Naur’s paper does not assert that theory building is the primary aim of programming."
    source_ids: ["storey-2026-cognitive-debt"]

  - id: "META-2026-140"
    text: >-
      Even if AI-generated code is locally understandable, teams can still accumulate cognitive debt as humans
      lose system-level understanding (intent, rationale, and interactions), making safe change difficult.
    type: "[H]"
    domain: "META"
    evidence_level: "E5"
    credence: 0.60
    operationalization: >-
      In AI-augmented teams, track system-level comprehension (ability to explain “why” and “how” across
      modules) and correlate with regressions, lead time, and frequency of “surprise breakage” after changes.
    assumptions:
      - System-level understanding can be measured via structured “why/how” interviews or tests.
    falsifiers:
      - Controlled studies show AI use improves system-level understanding and reduces surprise breakage over time.
    source_ids: ["storey-2026-cognitive-debt"]

  - id: "META-2026-141"
    text: >-
      Brooks’ Law (from *The Mythical Man-Month*) is commonly summarized as: “Adding manpower to a late
      software project makes it later,” due in part to increased coordination and communication overhead.
    type: "[F]"
    domain: "META"
    evidence_level: "E4"
    credence: 0.90
    operationalization: "Consult Brooks (1975) and supporting references for the quote and explanation."
    assumptions: []
    falsifiers:
      - "Primary sources do not contain the quote or do not attribute it to Brooks / The Mythical Man-Month."
    source_ids: ["storey-2026-cognitive-debt"]

  - id: "META-2026-142"
    text: >-
      Practices such as pair programming, refactoring, and test-driven development can mitigate cognitive debt
      by rebuilding and distributing shared understanding of a system.
    type: "[H]"
    domain: "META"
    evidence_level: "E5"
    credence: 0.60
    operationalization: >-
      Compare teams using these practices vs matched controls on cognitive-debt proxies (rationale capture,
      bus-factor resilience, comprehension tests) under similar AI tooling and delivery pressure.
    assumptions:
      - These practices increase shared understanding rather than only improving code structure/tests.
    falsifiers:
      - No measurable differences in cognitive-debt proxies between practice-adopting teams and controls in AI-augmented settings.
    source_ids: ["storey-2026-cognitive-debt"]

  - id: "META-2026-143"
    text: >-
      Requiring at least one human to fully understand each AI-generated change before shipping, and recording
      “why” (not just “what”), reduces the risk of cognitive-debt accumulation.
    type: "[H]"
    domain: "META"
    evidence_level: "E5"
    credence: 0.55
    operationalization: >-
      Run an intervention study: enforce a “human-understands” gate + rationale documentation on some teams
      and compare change failure rate, rework, and comprehension outcomes to teams without the gate.
    assumptions:
      - The gate is enforced rigorously and does not devolve into box-checking.
      - The added time cost is not so high that it is abandoned under pressure.
    falsifiers:
      - No differences in change failure rate or comprehension outcomes after adoption of the gate/rationale practice.
    source_ids: ["storey-2026-cognitive-debt"]

  - id: "META-2026-144"
    text: >-
      Cognitive debt can be detected early via warning signs such as fear-driven hesitance to make changes,
      increasing reliance on “tribal knowledge” held by a small subset of team members, and a growing sense the
      system is becoming a black box.
    type: "[H]"
    domain: "META"
    evidence_level: "E5"
    credence: 0.65
    operationalization: >-
      Use survey + behavioral proxies (PR hesitation, reviewer concentration, “who can change X?” queries) and
      test whether they predict later maintainability incidents and reduced onboarding success.
    assumptions:
      - These signals are not fully explained by other factors (e.g., organizational blame culture).
    falsifiers:
      - These warning signs do not predict later maintainability incidents or comprehension failures after controlling for confounders.
    source_ids: ["storey-2026-cognitive-debt"]

  - id: "META-2026-145"
    text: >-
      Thoughtworks hosted an invite-only “future of software development retreat” at Deer Valley Grand Hyatt,
      Utah on February 1–3, 2026, hosted by Martin Fowler and Thoughtworks.
    type: "[F]"
    domain: "META"
    evidence_level: "E4"
    credence: 0.85
    operationalization: "Verify event date and hosts on Thoughtworks’ event page."
    assumptions: []
    falsifiers:
      - "Thoughtworks’ event page does not list the retreat dates/hosts as stated."
    source_ids: ["storey-2026-cognitive-debt"]

  - id: "META-2026-146"
    text: >-
      TechDebt 2026 (ICSE 2026) lists Margaret-Anne Storey as a keynote speaker; the keynote abstract frames
      “cognitive debt” as accumulated future mental effort required to understand, reason about, and
      collaborate around software systems in AI-assisted development.
    type: "[F]"
    domain: "META"
    evidence_level: "E4"
    credence: 0.80
    operationalization: "Verify Storey’s keynote listing and abstract text on the TechDebt 2026 conference site."
    assumptions: []
    falsifiers:
      - "TechDebt 2026 does not list Storey as a keynote speaker or does not describe cognitive debt as stated."
    source_ids: ["storey-2026-cognitive-debt"]
```

---
**Analysis Date**: 2026-02-16  
**Analyst**: codex (gpt-5.2)  
**Credence in Analysis**: 0.70

## Analysis Log

| Pass | Date | Tool | Model | Duration | Tokens | Cost | Notes |
|---:|---|---|---|---|---:|---:|---|
| 1 | 2026-02-16 | codex-cli | gpt-5.2 | ? | ? | ? | Initial 3-stage analysis + extracted claims (planned import). |

