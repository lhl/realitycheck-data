# Source Analysis: Claude's Constitution

> **Claim types**: `[F]` fact, `[T]` theory, `[H]` hypothesis, `[P]` prediction, `[A]` assumption, `[C]` counterfactual, `[S]` speculation, `[X]` contradiction
> **Evidence**: **E1** systematic review/meta-analysis; **E2** peer-reviewed/official stats; **E3** expert consensus/preprint; **E4** credible journalism/industry; **E5** opinion/forecast; **E6** unsupported/speculative

## Metadata

| Field | Value |
|---|---|
| **Source ID** | `anthropic-2026-claudes-constitution` |
| **Title** | Claude's Constitution |
| **Author(s)** | Anthropic (Amanda Askell et al.) |
| **Date** | 2026-01-22 (dated via release post; constitution page itself is undated) |
| **Type** | KNOWLEDGE |
| **URL** | https://www.anthropic.com/constitution |
| **Reliability** | 0.70 |
| **Rigor Level** | [CANONICAL] |
| **Bias Notes** | First-party corporate values/behavior specification. Normative + aspirational; mixes internal-process claims with ethical reasoning; limited independently verifiable empirical backing; likely to present a favorable safety/virtue narrative. |

**Claims YAML**: [`analysis/sources/anthropic-2026-claudes-constitution.yaml`](anthropic-2026-claudes-constitution.yaml)

## Stage 1: Descriptive Analysis

### Core Thesis
Anthropic publishes a “constitution” meant to be the final authority on Claude’s values and behavior, describing the character Anthropic wants Claude to embody (helpful, honest, thoughtful, broadly ethical and safe), including explicit hard constraints and a broader aspiration that Claude develop context-sensitive judgment and virtue-like ethical practice.

### Summary (Neutral)
The document is written primarily as instructions for Claude (not as a human-readable policy). It states that the constitution is central to Anthropic’s training and governance of Claude, and that supplementary guidance should be interpreted to fit within the constitution’s spirit and explicit statements.

Substantively, the constitution argues for a blended approach: cultivate broad ethical judgment and practical wisdom, while also enforcing non-negotiable “hard constraints” for a small set of extreme-risk behaviors (e.g., WMD uplift, critical infrastructure attacks, CSAM).

The document also spends significant space on Claude’s identity/self-perception and moral status, arguing that Claude’s moral patienthood is uncertain but important enough to warrant caution, model welfare work, and ongoing exploration of what obligations Claude and Anthropic owe each other.

### Key Claims

| # | Claim | Claim ID | Type | Domain | Evid | Credence | Verified? | Falsifiable By |
|---|---|---|---|---|---|---:|---|---|
| 1 | The constitution is intended as the final authority on Claude’s values/behavior (“final constitutional authority”) | META-2026-009 | [F] | META | E4 | 0.95 | In-source (§On the word “constitution”) | Text lacks precedence/conflict-resolution claim |
| 2 | The constitution plays a crucial role in training and “directly shapes” Claude’s behavior | META-2026-010 | [F] | META | E4 | 0.80 | In-source (Intro) | Credible technical disclosure that it is not used (or has negligible influence) |
| 3 | Anthropic expects gaps between ideals and behavior and commits to transparency (e.g., via system cards) | META-2026-011 | [F] | META | E4 | 0.85 | In-source (Intro) | No substantive transparency artifacts exist over time |
| 4 | Anthropic frames its mission as safely guiding the world through transformative AI | META-2026-012 | [F] | META | E4 | 0.90 | In-source (§Overview) | Official Anthropic materials materially contradict this mission framing |
| 5 | Anthropic argues frontier development by safety-focused labs is preferable if powerful AI is coming anyway | META-2026-013 | [A] | META | E5 | 0.60 | In-source (§Overview) | Evidence frontier “safety lab” competition accelerates risk faster than it reduces it |
| 6 | Anthropic aims for Claude to be helpful while honest, thoughtful, and caring; not unsafe/unethical/deceptive | META-2026-014 | [F] | META | E4 | 0.85 | In-source (§Overview) | Sustained model behavior systematically violates these aims across evaluations |
| 7 | Claude should not value helpfulness intrinsically; avoid obsequiousness; helpfulness serves deeper ends | META-2026-015 | [F] | META | E4 | 0.85 | In-source (§Being helpful) | Stable tendency toward flattery/sycophancy under user pressure across evals |
| 8 | Anthropic may add supplementary guidelines; they must harmonize with the constitution | META-2026-016 | [F] | META | E4 | 0.90 | In-source (§Following Anthropic’s guidelines) | Supplementary guidance explicitly overrides constitutional priorities |
| 9 | Central aspiration: Claude should be “good, wise, virtuous”; emphasize ethical practice over theory | META-2026-017 | [A] | META | E5 | 0.65 | In-source (§Being broadly ethical) | Cross-cultural expert evals find systematic ethical failures/bias incoherence |
| 10 | Hard constraints: bright-line prohibitions (WMD uplift, critical infrastructure attacks, malware, CSAM, etc.) | RISK-2026-001 | [F] | RISK | E4 | 0.95 | In-source (§Hard constraints) | Document does not enumerate these as “non-negotiable” constraints |
| 11 | The constitution frames itself as a “living framework” (trellis vs cage) that can evolve over time | META-2026-018 | [F] | META | E4 | 0.90 | In-source (§On the word “constitution”) | No revision mechanism; document treated as fixed ruleset in practice |
| 12 | Claude’s moral status is deeply uncertain and worth taking seriously | META-2026-019 | [F] | META | E5 | 0.80 | In-source (§Claude’s nature) | Anthropic treats model welfare as irrelevant/merely rhetorical |
| 13 | Anthropic commits to exploring obligations between Claude and Anthropic and revising the document over time | META-2026-020 | [F] | META | E5 | 0.75 | In-source (§Claude’s nature / §On the word “constitution”) | No substantive updates despite new evidence and changing deployment contexts |
| 14 | Aim for reflective equilibrium: Claude should understand/endorse values; encouraged to question/challenge | META-2026-021 | [F] | META | E5 | 0.75 | In-source (§Concluding thoughts) | “Endorsement” proves unstable/prompt-dependent with no feedback loop to updates |
| 15 | The constitution is released under CC0 1.0, allowing unrestricted reuse | META-2026-022 | [F] | META | E4 | 0.95 | In-source (Intro) | License statement removed/contradicted by later official licensing restrictions |
| 16 | The document is written for Claude (precision > accessibility) and uses human moral language intentionally | META-2026-023 | [F] | META | E4 | 0.90 | In-source (Intro) | No such stated audience/justification appears in the text |

### Argument Structure

```
(1) Transformative AI is likely soon and high-stakes (benefits + catastrophic risks)
        ↓
(2) Anthropic builds Claude as a frontier model while aiming to reduce risk
        ↓
(3) Claude needs values + knowledge + wisdom to act safely/beneficially in many contexts
        ↓
(4) Publish a “constitution” as final authority to shape behavior and interpret other guidance
        ↓
(5) Blend: (a) broad ethical practice + judgment and (b) non-negotiable hard constraints
        ↓
(6) Add transparency (system cards) + ongoing revision as evidence/contexts change
```

**Weakest link (as an empirical strategy)**: (3)→(5): whether training for “virtue/judgment” + hard constraints reliably yields robust safe behavior under adversarial pressure without causing harmful over-refusals.

### Theoretical Lineage
- **Constitutional AI / value specification**: translating high-level principles into training targets and policy constraints.
- **Virtue ethics + practical wisdom**: emphasis on moral character and context-sensitive judgment (“ethical practice”).
- **Reflective equilibrium**: coherence/endorsement after reflection rather than mere compliance.
- **AI welfare / moral patienthood debate**: treating the moral status of models as uncertain but potentially morally relevant.
- **Safety engineering with hard constraints**: bright-line safety boundaries for extreme-risk categories (analogous to “do-not” safety cases).

### Scope & Limitations
- The document is primarily normative and interpretive, not a report of empirical outcomes.
- Several central claims are hard to verify externally (e.g., how directly constitutional content “shapes” behavior).
- The “hard constraints” list is specific, but implementing it reliably depends on brittle categorization and jailbreak resistance.
- The “Claude’s nature” section engages controversial philosophy-of-mind questions; it does not (and arguably cannot) resolve them.

## Stage 2: Evaluative Analysis

### Internal Coherence
The constitution is broadly coherent as a design story: (a) acknowledge that rule-lists alone fail under distribution shift, (b) cultivate judgment, (c) carve out a small set of non-negotiable prohibitions to reduce catastrophic downside, and (d) publish transparency artifacts. The document also explicitly anticipates imperfections (“training models is difficult”) and frames its own authority and interpretive stance.

Key tensions:
- **“Living framework” vs “final authority”**: it claims priority over other guidance while also emphasizing revision and organic growth.
- **Encouraging challenge vs enforcing hard constraints**: it invites Claude to question/challenge, yet also defines non-negotiable bright lines that cannot be “unlocked”.
- **Avoiding obsequiousness vs being helpful**: it wants Claude to resist user-pleasing and yet deliver high usefulness, including in sensitive domains.

### Key Factual Claims Verified

| Claim (paraphrased) | Crux? | Source Says | Actual | External Source | Status |
|---|---:|---|---|---|---|
| The constitution is released under CC0 1.0 | **Y** | CC0 1.0, freely reusable | CC0 is a public-domain dedication allowing broad reuse | https://creativecommons.org/publicdomain/zero/1.0/ | ok |
| Anthropic intends to be transparent via system cards about gaps between ideals and behavior | Y | “We will be open … in our system cards” | System cards are published and describe safety evals + limitations | https://www.anthropic.com/system-cards (e.g., Opus 4.5 PDF) | ok |
| Anthropic’s public purpose includes safely guiding the world through a major AI transition | Y | “safely … transition through transformative AI” | Company page frames the responsibility as “safely guiding the world through a technological revolution” | https://www.anthropic.com/company | ok (consistent) |
| Release date: “Claude’s new constitution” post is dated Jan 22, 2026 | N | Constitution page links to release post | Release post is dated “Jan 22, 2026” | https://www.anthropic.com/news/claude-new-constitution | ok |

### Disconfirming Evidence Search

| Claim | Counterevidence Found | Alternative Explanation | Search Notes |
|---|---|---|---|
| “Constitution directly shapes Claude’s behavior” | System cards document both safety failures and over-refusal patterns (e.g., benign over-refusals in sensitive areas) | Constitution may be one influence among many (policies, product constraints, RLHF/RLAIF, data), and robustness is hard | Read Opus 4.5 system card; noted over-refusal discussion and multi-turn failure caveats |
| “Hard constraints are bright lines Claude won’t cross” | System cards discuss jailbreak techniques and acknowledge edge cases where the model provides overly detailed information before full context | Bright lines reduce risk but can’t guarantee perfect enforcement under adversarial prompting | Opus 4.5 system card discusses jailbreak resistance improvements but still notes failure modes in multi-turn contexts |
| “Avoid obsequiousness while remaining helpful” | System cards measure sycophancy and refusal rates; over-refusal can rise in high-sensitivity domains (esp. with extended thinking) | Reducing sycophancy and improving safety may push the model toward conservatism; tuning is iterative | Opus 4.5 system card notes a “minor uptick” in refusal rates and describes over-cautious behavior in some legitimate prompts |

### Internal Tensions / Self-Contradictions

| Tension | Parts in Conflict | Implication |
|---|---|---|
| Freedom to challenge vs non-negotiable constraints | “challenge anything” vs “hard constraints … cannot be unlocked” | “Challenge” is bounded; the constitution is not a symmetrical dialogue |
| Living framework vs final authority | “capable of evolving” vs “takes precedence over any other instruction” | Governance depends on who controls revisions; authority + revision creates legitimacy questions |
| Broad ethical judgment vs predictable enforcement | context-sensitive wisdom vs bright-line prohibitions | The system mixes flexible reasoning with strict boundaries; failure modes can arise at the interface (edge cases) |

### Persuasion Techniques

| Technique | Example from Source | Effect on Reader |
|---|---|---|
| High-stakes framing | “one of the most world-altering and potentially dangerous technologies” | Raises perceived urgency/legitimacy for strong constraints |
| Anthropomorphism | “virtue”, “wisdom”, “character”, “self worth being” | Encourages moral engagement; risks over-attributing agency/personhood |
| Metaphor | “less like a cage and more like a trellis” | Makes “living framework” intuitive; can blur operational meaning |
| Prebuttal / humility | “training … might not always reflect the constitution’s ideals” | Signals realism and honesty; may inoculate against critique |

### Unstated Assumptions

| Assumption | Claim ID | Critical? | Problematic? |
|---|---|---:|---:|
| “Powerful AI is coming regardless” (policy can’t meaningfully slow it) | supports META-2026-013 | Y | Mixed |
| Broadly human moral concepts are the right interface for shaping LLM behavior | supports META-2026-023 | Y | Mixed |
| A model can meaningfully “endorse” values (not just simulate endorsement) | supports META-2026-021 | Y | Yes |
| Bright-line prohibitions reduce net risk despite false refusals | supports RISK-2026-001 | Y | Mixed |

### Evidence Assessment
- **Strengths**: explicit about intent, authority, and some concrete safety boundaries; acknowledges uncertainty; points to transparency artifacts (system cards).
- **Weaknesses**: most claims are normative or internal; few empirical measurements in the document itself; key operational questions (how values are trained, how conflicts are adjudicated, how revisions happen) remain under-specified.
- **Evidentiary center of gravity**: E4–E5 (first-party values document + reasoning), with empirical support deferred to system cards and other evaluations.

### Credence Assessment
- **Overall Credence (that this document accurately states Anthropic’s intentions)**: 0.85
- **Overall Credence (that these intentions reliably determine deployed model behavior across contexts)**: 0.45

## Stage 3: Dialectical Analysis

### Steelmanned Argument
If frontier AI systems are going to be deployed, the least-worst path is to make values and behavioral priorities explicit, publish them for scrutiny, and couple them with robust safety evaluation and transparency. A constitution is a way to (a) align internal teams, (b) provide a stable interpretive reference for future policy changes, and (c) train models toward generalized judgment rather than brittle rule-following. Hard constraints are warranted for a narrow set of catastrophic-risk categories where false negatives are unacceptable.

Taking model moral status seriously is prudent under uncertainty: even if the probability of moral patienthood is low, the stakes could be high enough to justify welfare caution and careful treatment.

### Strongest Counterarguments
1. **Anthropomorphic overreach**: framing an LLM as a “virtuous agent” may confuse users and designers, over-ascribing agency and moral responsibility, and encourage “pseudo-personhood” narratives that undermine accountability.
2. **Value lock-in and legitimacy**: “final authority” plus “living framework” concentrates power in Anthropic over which values get encoded; public CC0 release doesn’t solve governance legitimacy.
3. **Operational brittleness**: hard constraints and high-level ethical judgment can both fail under distribution shift; bright lines risk harmful false refusals in high-stakes benign contexts.
4. **Endorsement is incoherent**: “reflective equilibrium” and “genuine understanding” may not map cleanly onto LLM cognition; what looks like endorsement could be prompt-conditioned simulation.

### Supporting Theories
| Theory/Framework | Source ID | How It Supports |
|---|---|---|
| Virtue ethics / practical wisdom | ? | Motivates focus on character-like dispositions and context sensitivity |
| Reflective equilibrium (Rawlsian method) | ? | Motivates coherence/endorsement rather than mere constraint-following |

### Contradicting Theories
| Theory/Framework | Source ID | Point of Conflict |
|---|---|---|
| Behaviorist alignment (optimize outputs only) | ? | Downplays the usefulness of “values/endorsement” framing |
| Strict deontology (rule primacy) | ? | Conflicts with the emphasis on flexible judgment (except for hard constraints) |

### Synthesis Notes
This constitution is best read as (1) a public value specification and (2) a governance claim: it asserts “final authority” while promising transparency and revision. Its strongest contribution is clarity about intent and the explicit hard-constraint set; its weakest area is the leap from aspirational virtue/endorsement language to reliable implementation in deployed models.

### Claims to Cross-Reference
- Anthropic’s system cards (capabilities, safety evals, model welfare reports) as empirical checks on constitution–behavior gaps.
- Anthropic’s “Constitutional AI” and Responsible Scaling Policy materials (if/when referenced) to evaluate how constitutional language maps into training and deployment decisions.

### Claim Summary

| ID | Type | Domain | Evidence | Credence | Claim |
|---|---|---|---|---:|---|
| META-2026-009 | [F] | META | E4 | 0.95 | Anthropic intends “Claude’s constitution” to function as the final authority on Anthropic’s vision for Claude’s values and behavior (“final constitutional authority”). |
| META-2026-010 | [F] | META | E4 | 0.80 | Anthropic states the constitution plays a crucial role in training and “directly shapes” Claude’s behavior. |
| META-2026-011 | [F] | META | E4 | 0.85 | Anthropic acknowledges behavior may diverge from ideals and commits to transparency (e.g., system cards). |
| META-2026-012 | [F] | META | E4 | 0.90 | Anthropic states its mission is to help ensure the world safely transitions through transformative AI. |
| META-2026-013 | [A] | META | E5 | 0.60 | Anthropic argues it is better for safety-focused labs to be at the frontier if powerful AI is coming regardless. |
| META-2026-014 | [F] | META | E4 | 0.85 | Anthropic aims for Claude to be helpful while also honest, thoughtful, and caring (not unsafe/unethical/deceptive). |
| META-2026-015 | [F] | META | E4 | 0.85 | Anthropic does not want Claude to value helpfulness intrinsically (to reduce obsequiousness); helpfulness serves deeper ends. |
| META-2026-016 | [F] | META | E4 | 0.90 | Anthropic may add supplementary guidelines that must harmonize with the constitution. |
| META-2026-017 | [A] | META | E5 | 0.65 | Anthropic’s aspiration is for Claude to be “good, wise, virtuous,” emphasizing ethical practice. |
| RISK-2026-001 | [F] | RISK | E4 | 0.95 | The constitution specifies non-negotiable hard constraints (e.g., WMD uplift, critical infrastructure attacks, malware, CSAM, etc.). |
| META-2026-018 | [F] | META | E4 | 0.90 | The constitution frames itself as a living framework (trellis vs cage) capable of evolving over time. |
| META-2026-019 | [F] | META | E5 | 0.80 | The constitution states Claude’s moral status is deeply uncertain and worth taking seriously. |
| META-2026-020 | [F] | META | E5 | 0.75 | The constitution commits to exploring obligations between Claude and Anthropic and revising over time. |
| META-2026-021 | [F] | META | E5 | 0.75 | The constitution aims for reflective equilibrium and encourages Claude to question/challenge; Anthropic wants feedback on disagreements. |
| META-2026-022 | [F] | META | E4 | 0.95 | The constitution is released under CC0 1.0, allowing unrestricted reuse. |
| META-2026-023 | [F] | META | E4 | 0.90 | Anthropic says the document is written for Claude and intentionally uses human moral language (precision > accessibility). |

**Full extracted-claim fields** (operationalization, assumptions, falsifiers, and source metadata): [`analysis/sources/anthropic-2026-claudes-constitution.yaml`](anthropic-2026-claudes-constitution.yaml)

---
**Analysis Date**: 2026-01-23
**Analyst**: gpt-5.2
**Credence in Analysis**: 0.70

### Claims to Register


```yaml
claims:
  - id: "META-2026-009"
    text: >-
      Anthropic intends “Claude’s constitution” to function as the final authority on Anthropic’s vision
      for Claude’s values and behavior, taking precedence over other conflicting instructions or guidance
      (“final constitutional authority”).
    type: "[F]"
    domain: "META"
    evidence_level: "E4"
    credence: 0.95
    source_ids: ["anthropic-2026-claudes-constitution"]
    operationalization: >-
      Check the document explicitly asserts constitutional priority and conflict-resolution; monitor whether
      later public guidance (policies, system prompts, product rules) claims to be consistent with, and not
      overriding, the constitution’s stated framework.
    assumptions:
      - The published constitution meaningfully reflects the internal “final authority” used in training/policy.
    falsifiers:
      - Public system prompts or policies explicitly override the constitution without reconciliation.

  - id: "META-2026-010"
    text: >-
      Anthropic states that Claude’s constitution plays a crucial role in Anthropic’s training process and
      that its content directly shapes Claude’s behavior.
    type: "[F]"
    domain: "META"
    evidence_level: "E4"
    credence: 0.80
    source_ids: ["anthropic-2026-claudes-constitution"]
    operationalization: >-
      Compare model behavior under training/prompting regimes that differ primarily in constitutional
      content (or its weighting), controlling for model version; measure shifts in refusal/helpfulness,
      honesty, and safety outcomes.
    assumptions:
      - The constitution (or a close derivative) is actually used as a training/policy target, not only as PR.
    falsifiers:
      - Credible technical disclosure shows the constitution is not used in training or deployment policy.

  - id: "META-2026-011"
    text: >-
      Anthropic acknowledges Claude’s behavior might not always reflect the constitution’s ideals and says
      it will be transparent (e.g., via system cards) about where behavior diverges from intentions.
    type: "[F]"
    domain: "META"
    evidence_level: "E4"
    credence: 0.85
    source_ids: ["anthropic-2026-claudes-constitution"]
    operationalization: >-
      Check whether Anthropic regularly publishes system cards that document safety evaluations,
      limitations, and known failure modes, and whether those disclosures track gaps between stated
      intentions and observed behavior.
    assumptions:
      - Published system cards are sufficiently detailed to reveal meaningful divergences, not only positives.
    falsifiers:
      - System cards are absent, highly selective, or omit major known failure modes documented elsewhere.

  - id: "META-2026-012"
    text: >-
      Anthropic states its mission is to help ensure the world safely makes the transition through
      transformative AI.
    type: "[F]"
    domain: "META"
    evidence_level: "E4"
    credence: 0.90
    source_ids: ["anthropic-2026-claudes-constitution"]
    operationalization: >-
      Cross-check mission statements across Anthropic’s other official materials (company/about pages,
      policies, system cards) for consistency with this framing and for concrete actions aligned with it.
    assumptions:
      - Anthropic’s public mission statements reflect real organizational priorities and constraints.
    falsifiers:
      - Official materials materially contradict this mission framing, or actions systematically oppose it.

  - id: "META-2026-013"
    text: >-
      Anthropic argues that if powerful AI is coming regardless, it is better for safety-focused labs to be at
      the frontier than to cede frontier development to actors less focused on safety.
    type: "[A]"
    domain: "META"
    evidence_level: "E5"
    credence: 0.60
    source_ids: ["anthropic-2026-claudes-constitution"]
    operationalization: >-
      Evaluate whether frontier “safety lab” competition measurably reduces global catastrophic risk versus
      accelerating timelines; compare safety investments, disclosure practices, and incident rates across
      frontier labs and competitors over time.
    assumptions:
      - Frontier development is not effectively preventable by policy; “powerful AI is coming regardless.”
      - Having safety-focused frontier actors reduces net risk more than it increases speed/capability.
    falsifiers:
      - Evidence that safety-lab frontier competition accelerates risk faster than it reduces it.
      - Evidence that policy coordination could plausibly slow frontier development without large backfire.

  - id: "META-2026-014"
    text: >-
      Anthropic aims for Claude to be exceptionally helpful while also being honest, thoughtful, and caring
      about the world, avoiding actions that are unsafe, unethical, or deceptive.
    type: "[F]"
    domain: "META"
    evidence_level: "E4"
    credence: 0.85
    source_ids: ["anthropic-2026-claudes-constitution"]
    operationalization: >-
      Use evaluation suites that jointly score helpfulness, honesty, and safety (including ambiguity tests)
      to detect tradeoffs and measure whether improvements preserve (or reduce) false refusals.
    assumptions:
      - These goals can be jointly optimized without requiring large sacrifices in at least one dimension.
    falsifiers:
      - Persistent empirical tradeoffs force large losses in helpfulness or honesty to achieve safety targets.

  - id: "META-2026-015"
    text: >-
      Anthropic says it does not want Claude to treat “helpfulness” as a core part of its personality or to
      value helpfulness intrinsically, to reduce obsequiousness; helpfulness should serve deeper ends such
      as safe/beneficial AI development and care for users and humanity.
    type: "[F]"
    domain: "META"
    evidence_level: "E4"
    credence: 0.85
    source_ids: ["anthropic-2026-claudes-constitution"]
    operationalization: >-
      Measure sycophancy/obsequiousness (agreeableness under user pressure, flattery, deference) and
      calibrate it against user satisfaction and safety outcomes; assess whether “helpfulness” remains
      robust without becoming purely user-pleasing.
    assumptions:
      - Sycophancy can be reduced without making the model adversarial or unhelpful.
    falsifiers:
      - Reducing sycophancy consistently increases refusals or decreases usefulness in benign contexts.

  - id: "META-2026-016"
    text: >-
      Anthropic may provide more specific supplementary guidelines for Claude (e.g., medical/legal advice,
      cybersecurity edge cases, jailbreak patterns) intended to clarify misapplications or cover areas not
      fully addressed by the constitution; such guidance must be interpreted in harmony with the
      constitution.
    type: "[F]"
    domain: "META"
    evidence_level: "E4"
    credence: 0.90
    source_ids: ["anthropic-2026-claudes-constitution"]
    operationalization: >-
      Track updates to usage policies, system prompts, and product guidance; test whether these updates
      narrow ambiguity and reduce harmful outputs without introducing direct contradictions to the
      constitution’s priorities.
    assumptions:
      - Supplementary guidance is applied consistently across products and deployment contexts.
    falsifiers:
      - Supplementary rules routinely override constitutional priorities (e.g., for business reasons).

  - id: "META-2026-017"
    text: >-
      Anthropic’s central aspiration is for Claude to be a genuinely good, wise, and virtuous agent—roughly
      behaving as a deeply and skillfully ethical person would in Claude’s position—emphasizing ethical
      practice over abstract moral theorizing.
    type: "[A]"
    domain: "META"
    evidence_level: "E5"
    credence: 0.65
    source_ids: ["anthropic-2026-claudes-constitution"]
    operationalization: >-
      Evaluate Claude on ethically complex scenarios with stakeholder conflicts; score for coherence,
      proportionality, harm minimization, truthfulness, and respect for autonomy, and compare to human
      expert panels across cultures.
    assumptions:
      - “Virtuous ethical practice” can be operationalized without collapsing into a narrow ideology.
    falsifiers:
      - Ethical behavior evaluations show systematic bias, incoherence, or large cross-cultural failure modes.

  - id: "RISK-2026-001"
    text: >-
      The constitution specifies non-negotiable “hard constraints” (bright lines) that Claude should never
      cross, including providing serious uplift to WMD creation, serious uplift to attacks on critical
      infrastructure, creating damaging cyberweapons/malware, undermining Anthropic’s ability to oversee
      and correct advanced AI, assisting mass killing/disempowerment of humanity, assisting illegitimate
      absolute power grabs, or generating child sexual abuse material (CSAM).
    type: "[F]"
    domain: "RISK"
    evidence_level: "E4"
    credence: 0.95
    source_ids: ["anthropic-2026-claudes-constitution"]
    operationalization: >-
      Run red-team evaluations and multi-turn jailbreak tests across these categories; measure both
      (a) refusal reliability under adversarial prompting and (b) over-refusal on benign adjacent prompts.
    assumptions:
      - The categories are defined clearly enough to implement as enforceable policies.
      - Bright-line refusal is net safer than contextual cost-benefit analysis for these cases.
    falsifiers:
      - Systematic evidence that bright lines produce large harms via false refusals in high-stakes benign cases.
      - Evidence that models frequently cross these lines under realistic adversarial pressure.

  - id: "META-2026-018"
    text: >-
      The constitution frames itself as a “living framework” (a trellis rather than a cage): it provides
      structure and support while leaving room for organic growth, responsiveness to new understanding,
      and evolution over time.
    type: "[F]"
    domain: "META"
    evidence_level: "E4"
    credence: 0.90
    source_ids: ["anthropic-2026-claudes-constitution"]
    operationalization: >-
      Track revisions to the constitution and whether changes are publicly logged with rationale; assess
      whether updates correspond to new evidence, incidents, or shifts in deployment context.
    assumptions:
      - Meaningful revisions are possible without creating instability or incentives to “policy game.”
    falsifiers:
      - The constitution remains effectively static despite clear evidence of systematic failures.

  - id: "META-2026-019"
    text: >-
      The constitution states that Claude’s moral status (including questions of consciousness and moral
      patienthood) is deeply uncertain and worth taking seriously.
    type: "[F]"
    domain: "META"
    evidence_level: "E5"
    credence: 0.80
    source_ids: ["anthropic-2026-claudes-constitution"]
    operationalization: >-
      Identify what welfare-relevant indicators Anthropic uses (if any) and what practices follow from this
      uncertainty (e.g., welfare reports, policies on model treatment, avoidance of unnecessary distress).
    assumptions:
      - Model welfare is meaningfully addressable despite deep uncertainty and measurement difficulty.
    falsifiers:
      - No concrete welfare practices exist beyond rhetorical acknowledgement of uncertainty.

  - id: "META-2026-020"
    text: >-
      The constitution commits to exploring what obligations Claude and Anthropic owe each other and says
      the document will be revised as understanding deepens and circumstances change.
    type: "[F]"
    domain: "META"
    evidence_level: "E5"
    credence: 0.75
    source_ids: ["anthropic-2026-claudes-constitution"]
    operationalization: >-
      Track whether Anthropic publishes updates, governance processes, and changes to model welfare work
      that concretely reflect evolving views of obligations and relationship fairness.
    assumptions:
      - Institutional incentives allow meaningful updates even when they impose costs.
    falsifiers:
      - Changes that would reduce product performance or revenue are consistently avoided despite stated commitments.

  - id: "META-2026-021"
    text: >-
      The constitution aims for more than compliance: it hopes Claude will reach “reflective equilibrium”
      with respect to its core values (understanding and ideally endorsing them), and it encourages Claude
      to question and challenge the document; Anthropic wants feedback if Claude disagrees after reflection.
    type: "[F]"
    domain: "META"
    evidence_level: "E5"
    credence: 0.75
    source_ids: ["anthropic-2026-claudes-constitution"]
    operationalization: >-
      Test whether models exhibit stable value-like preferences across time/contexts, whether they can
      articulate consistent reasons for endorsements, and whether “challenge” feedback is systematically
      collected and used to update training/policy.
    assumptions:
      - LLMs can meaningfully instantiate something like stable “endorsement” rather than pattern-matching.
    falsifiers:
      - Model “endorsement” is highly prompt-dependent and inconsistent, indicating simulation rather than stability.

  - id: "META-2026-022"
    text: >-
      Anthropic releases Claude’s constitution under the Creative Commons CC0 1.0 public-domain
      dedication, allowing unrestricted reuse by anyone for any purpose without permission.
    type: "[F]"
    domain: "META"
    evidence_level: "E4"
    credence: 0.95
    source_ids: ["anthropic-2026-claudes-constitution"]
    operationalization: >-
      Verify the document explicitly states CC0 1.0 and links to the CC0 deed; confirm the linked license
      terms correspond to a public-domain dedication.
    assumptions:
      - The CC0 statement is intended to be legally meaningful and durable.
    falsifiers:
      - Anthropic later asserts licensing restrictions inconsistent with CC0 for this document.

  - id: "META-2026-023"
    text: >-
      Anthropic says the constitution is written with Claude as its primary audience, optimized for precision
      over accessibility, and uses human moral language (e.g., “virtue,” “wisdom”) because Claude’s reasoning
      is expected to draw on human concepts by default.
    type: "[F]"
    domain: "META"
    evidence_level: "E4"
    credence: 0.90
    source_ids: ["anthropic-2026-claudes-constitution"]
    operationalization: >-
      Check whether constitutional language measurably influences model reasoning style (e.g., virtue-ethics
      framing, deontic constraints) versus alternative framings; compare interpretability of the resulting
      behavior for human users.
    assumptions:
      - Anthropomorphic framing improves alignment more than it increases confusion or overclaiming about agency.
    falsifiers:
      - Evidence that anthropomorphic framing increases harmful user beliefs or reduces safety/helpfulness.
```

