# Synthesis Analysis: JP-TL-Bench and JA↔EN Translation Evaluation (Anchored Pairwise vs Metrics/MQM)

> **Source IDs**: `lin-2026-jp-tl-bench-paper`, `lin-2025-jp-tl-bench`, `shisaai-2026-jp-tl-bench-repo`, `lin-2026-jp-tl-bench-directional-analysis`, `lin-2025-shisa-v2`, `lin-2025-shisa-v2-405b`, `shisaai-2025-shisa-v2-1`, `lhl-2025-liquid-ai-hackathon-tokyo`, `liquidai-2025-lfm2-350m-enjp-mt`, `google-2026-translategemma-tech-report`, `google-2026-translategemma-blog`
> **Analysis Date**: 2026-01-24 (rev. 2026-01-24)
> **Analyst**: gpt-5.2 → claude-opus-4-5
> **Rigor Level**: `[REVIEWED]`
> **Type**: Cross-source synthesis

---

## The Question

How credible and useful is JP-TL-Bench’s anchored, pairwise LLM-judge approach for **high-end JA↔EN translation evaluation**, how does it compare to **WMT/MQM + learned metrics** (e.g., COMET/MetricX) and to **llm-jp-eval’s COMET-centered workflow**, and what Japanese-specific linguistic factors (context, pro-drop, register) should an evaluation framework explicitly address?

Also: is the “anchored pairwise” design truly novel (or is there close prior art), and are “classic” MT metrics outmoded for evaluating frontier LLM MT on Japanese?

---

## Primary Sources (This Synthesis)

| Source ID | Type | What it provides |
|---|---|---|
| `lin-2026-jp-tl-bench-paper` | PAPER | Full protocol: anchored pairwise LLM judging, Bradley–Terry aggregation, LT score definition, known limitations |
| `shisaai-2026-jp-tl-bench-repo` | KNOWLEDGE | Auditable implementation + frozen Base Set v1.0 artifacts (manifest, prompts, slice scores) |
| `lin-2025-jp-tl-bench` | BLOG | Motivation and claimed benefits (discrimination vs metric compression; cost framing) |
| `lin-2026-jp-tl-bench-directional-analysis` | BLOG | Concrete directional/difficulty slice examples with verifiable scores |
| `lhl-2025-liquid-ai-hackathon-tokyo` | KNOWLEDGE | Practical COMET-centered llm-jp-eval MT workflow + cautions about metric clustering/prompt asymmetry |
| `liquidai-2025-lfm2-350m-enjp-mt` | MODEL_CARD | A small vendor MT model with bidirectional EN↔JA positioning (useful “non-frontier” comparator) |
| `google-2026-translategemma-tech-report` | PAPER | Modern WMT-style evaluation: SFT+RL, MetricX/COMET22, and MQM human eval (incl. en→ja numbers) |
| `google-2026-translategemma-blog` | ARTICLE | Compressed announcement framing (useful for claims/positioning) |
| `lin-2025-shisa-v2`, `lin-2025-shisa-v2-405b`, `shisaai-2025-shisa-v2-1` | BLOG | Context: Shisa model development claims and why “missing evals” (incl. translation) motivated JP-TL-Bench |

---

## Key Evidence Anchors (Claims referenced)

| Claim ID | Summary | Evidence | Credence |
|---|---|---:|---:|
| TECH-2026-031 | JP-TL-Bench protocol: anchored pairwise LLM judging + Bradley–Terry → WR% + LT | E3 | 0.90 |
| TECH-2026-033 | Benchmark coverage: 70 items, 34/36 direction split, 30/40 easy/hard | E2 | 0.95 |
| TECH-2026-050 | Repo ships frozen Base Set v1.0 (20 anchors + translations + reports) | E2 | 0.95 |
| TECH-2026-039 | LT is sigmoid(mean-centered BT params)×10 | E2 | 0.95 |
| TECH-2026-046 | Llama 3.1 8B shows large direction gap (JA→EN ≈4.52 vs EN→JA ≈1.40) | E2 | 0.95 |
| TECH-2026-047 | Swallow v0.5 shows reverse direction gap (EN→JA ≈8.80 vs JA→EN ≈5.96) | E2 | 0.95 |
| TECH-2026-071 | llm-jp-eval MT has few-shot asymmetry (ALT 4-shot vs WikiCorpus zero-shot) | E2 | 0.85 |
| TECH-2026-079 | TranslateGemma: SFT + RL with MetricX-QE/AutoMQM reward models | E3 | 0.90 |
| TECH-2026-081 | TranslateGemma improves WMT24++ en→ja_JP MetricX vs Gemma 3 (e.g., 27B: 3.53 vs 4.11) | E2 | 0.90 |
| TECH-2026-083 | TranslateGemma report’s per-language WMT24++ appendix is en→* (no explicit ja→en table), limiting JA→EN regression claims | E2 | 0.80 |
| TECH-2026-087 | Japanese↔English evaluation must address pro-drop/zero pronouns + honorific/register control | E3 | 0.75 |

---

## Synthesis: What Each Evaluation Paradigm Actually Optimizes For

### 1) COMET/MetricX (WMT-style learned metrics)
**Strength**: scalable, stable aggregation over *large* corpora; correlates with human judgments in many WMT settings; good for regression detection and broad ranking.  
**Weakness**: can underweight or miss Japanese-specific phenomena (register/honorific control, implicature, pro-drop resolution) and can “compress” or become ambiguous in the high-quality regime; depends on reference quality and metric calibration. (See `lhl-2025-liquid-ai-hackathon-tokyo` and JP-TL-Bench’s motivation claims.)

TranslateGemma represents a modern “metrics + MQM” approach: automatic metric gains plus professional human MQM, which is closer to decision-grade evidence than metrics alone. (`TECH-2026-079`, `TECH-2026-082`)

### 2) MQM (human error-span evaluation)
**Strength**: highest-fidelity signal for adequacy + error categories; can incorporate document context; harder to “game.”  
**Weakness**: expensive and slow; hard to use in tight inner loops.

TranslateGemma explicitly uses MQM on WMT25 with document context, which addresses many “metrics are outmoded” concerns—at a cost. (`TECH-2026-082`)

### 3) LLM-as-a-judge, pairwise preference
**Strength**: directly targets the comparative question developers often need (“which of these already-good translations is better?”); pairwise tends to be more consistent than absolute rubric scoring for close calls.  
**Weakness**: judge dependence (bias, drift, style preferences) and protocol sensitivity are first-order; without audits it can become a “beautiful but brittle” signal.

JP-TL-Bench is explicitly in this bucket, with a design intended to reduce cost and increase comparability. (`TECH-2026-031`)

---

## Japanese Linguistic Challenges: Why "Perfect Single-Line Translation" Is Often Impossible

Japanese↔English is one of the most challenging language pairs for MT due to **fundamental typological differences**. The core problem: Japanese encodes much information implicitly that English requires explicitly (and vice versa), making sentence-level translation inherently lossy in both directions. (`TECH-2026-087`)

### 1. Pro-Drop / Zero Anaphora (JA→EN)

Japanese is a **radical pro-drop language** where subjects, objects, and topics can be omitted when recoverable from context. Unlike Spanish or Italian (subject-drop only), Japanese allows *any* argument to be dropped.

**Example:**
```
Japanese: 食べた。 (Tabeta.)
Literal:  "[∅] ate."
English:  "I ate." / "He ate." / "She ate." / "They ate." (unknowable without context)
```

Research shows that **30–40% of sentences** in typical Japanese text have zero subjects (Isozaki & Hirao, 2003). Zero anaphora resolution requires discourse-level centering theory, not just local context (Nakaiwa & Shirai, 1996). Even sophisticated models achieve only ~60–70% accuracy using syntactic features alone (Iida et al., 2007 ACL).

**MT failure mode:** Sentence-by-sentence systems frequently guess wrong pronouns, especially for 3rd person (he/she/they) which Japanese doesn't morphologically distinguish. This produces misgendering, wrong agent/patient assignment, or awkward over-specification.

**Key citations:**
- Nakaiwa & Shirai (1996) "Anaphora Resolution of Japanese Zero Pronouns with Deictic Reference" (COLING)
- Iida, Inui & Matsumoto (2007) "Zero-anaphora resolution by learning rich syntactic pattern features" (ACL)
- Hangyo, Kawahara & Kurohashi (2013) "Japanese Zero Reference Resolution Considering Exophora and Author/Reader Mentions" (EMNLP)

### 2. Keigo (敬語) / Honorifics / Register (EN→JA)

Japanese grammaticalizes **social relationships** through morphological choice across multiple registers:

| Level | Name | Example (to eat) |
|-------|------|------------------|
| Plain | 普通形 | 食べる (taberu) |
| Polite | 丁寧語 | 食べます (tabemasu) |
| Humble | 謙譲語 | いただく (itadaku) |
| Respectful | 尊敬語 | 召し上がる (meshiagaru) |

**Critical problem:** A single English sentence like "Please eat" could map to **6+ Japanese forms** depending on:
- Speaker-hearer relationship
- Speaker-referent relationship
- Formality of situation
- In-group vs. out-group dynamics

Without context (speaker, hearer, setting), selecting the correct keigo level is **formally impossible**. The output may be semantically "correct" but socially wrong—and socially wrong Japanese can be worse than semantic errors in many real-world contexts (customer service, business, literary translation).

**MT failure mode:** Systems typically default to mid-level politeness (-masu form), producing inappropriate output for business, customer service, or literary contexts.

**Key citations:**
- Ide (1989) "Formal forms and discernment: Two neglected aspects of universals of linguistic politeness" (Multilingua)
- Okamoto (1999) "Situated politeness: Manipulating honorific and non-honorific expressions in Japanese conversations"
- Matsumoto (1988) "Reexamination of the universality of face: Politeness phenomena in Japanese" (Journal of Pragmatics)

### 3. Implicature, Ellipsis, and High-Context Communication

Japanese is classified as a **high-context culture** (Hall, 1976) where meaning relies heavily on shared background knowledge, situational context, and what is *not* said.

**Sentence-final particles** encode speaker attitude without English equivalents:
```
行くよ (iku yo)    - "I'm going" (assertive)
行くわ (iku wa)    - "I'm going" (soft/feminine)
行くね (iku ne)    - "I'm going, okay?" (seeking agreement)
行くかな (iku kana) - "I wonder if I'll go..." (uncertainty)
```

**Hedging and indirectness:** Japanese speakers routinely leave sentences grammatically incomplete:
```
ちょっと... (chotto...) - "A little..." → (implied: "that's difficult/I'd rather not")
```

**MT failure mode:** Literal translation of hedges sounds rude in English; over-translation of particles loses nuance.

**Key citations:**
- Maynard (1989) "Japanese Conversation: Self-contextualization through Structure and Interactional Management"
- Kamio (1997) "Territory of Information" (epistemic stance theory)

### 4. Document-Level Coherence

Japanese uses **demonstratives** (kore/sore/are) and **zero anaphora** across sentences. Pronoun choice in sentence 5 may depend on antecedents in sentence 1. Japanese **topic chains** carry the wa-marked topic across multiple sentences—breaking this creates incoherent English.

Research demonstrates **10–15% quality improvements** for JA-EN with document-level models (Nagata, 2017). Voita et al. (2019) showed that context-aware MT specifically improves deixis, ellipsis, and lexical cohesion—all critical for Japanese.

### 5. Summary: The Asymmetry

| Challenge | What's Missing in Source |
|-----------|-------------------------|
| Zero pronouns (JA→EN) | Explicit subjects/objects |
| Keigo (EN→JA) | Social relationship metadata |
| Implicature | Implicit meaning |
| Sentence-final particles | Speaker attitude/gender cues |
| Document coherence | Cross-sentence reference chains |

**The fundamental asymmetry:** Japanese sentences are **under-specified** relative to English requirements. A single Japanese sentence may map to dozens of valid English sentences depending on context that exists only outside the sentence boundaries. Conversely, English sentences are **over-specified** for Japanese—generating natural Japanese requires REMOVING information (pronouns) and ADDING information (honorifics) that English doesn't encode.

**Implication for evaluation:** Benchmarks that only use **one-off, low-context prompts** will systematically generate errors that are not "model stupidity" so much as *missing information*. JP-TL-Bench partially addresses this by including longer items and by using richer translation prompts (full vs low vs ultra-low variants), but the benchmark still largely treats each item independently. (`TECH-2026-033`, `TECH-2026-052`)

---

## Directionality: Evidence and Interpretation

JP-TL-Bench provides concrete evidence that directionality can be large:
- Llama 3.1 8B: JA→EN ≈ 4.52 vs EN→JA ≈ 1.40 (`TECH-2026-046`)
- Swallow v0.5: EN→JA ≈ 8.80 vs JA→EN ≈ 5.96 (`TECH-2026-047`)

Synthesis view:
- Direction gaps are plausibly driven by (a) training data balance, (b) tokenizer efficiency differences, (c) target-language generation constraints (EN→JA requires “social correctness”), and (d) prompting/decoding choices.
- This strengthens the case that any “JA↔EN” evaluation should report **at least** direction-sliced scores, and ideally difficulty and domain slices.

---

## Anchored Pairwise Evaluation: What It Solves, What It Trades Off

### What it credibly solves
1. **Quadratic cost scaling** of all-pairs tournaments: each candidate plays a fixed set of opponents (anchors), so cost is linear in evaluated candidates. (`TECH-2026-032`)
2. **Pool drift and order dependence** typical of Elo-style floating leaderboards: the “measuring stick” is the fixed anchor set. (`TECH-2026-032`)
3. **High-end discrimination**: pairwise preference is well matched to “two good translations; which is better?” and LT/WR provide a stable reporting format. (`TECH-2026-031`, `TECH-2026-039`)

### What it does *not* solve (and can worsen)
1. **Judge drift**: anchoring fixes the opponent pool, not the judge. If the judge model changes behavior over time, comparability breaks even if anchors are frozen.
2. **Anchor staleness**: as frontier models improve, the anchor set can become outdated and compress scores at the top again; versioning helps but trades off cross-version comparability.
3. **Self-preference risk**: including the default judge as an anchor creates an obvious bias concern that should be empirically audited. (`TECH-2026-053`)
4. **Protocol-dependence becomes “the definition of the score”**: LT is not a universal quantity; it is “LT under (BaseSet vX, Judge Y, code Z).”

Synthesis recommendation: treat anchored pairwise as a strong **inner-loop discriminator** and pair it with periodic **outer-loop audits** (e.g., MQM on a small set, a panel/jury of judges, or cross-metric checks) to catch judge failures and staleness.

---

## What Makes Anchored Pairwise Evaluation Unique?

JP-TL-Bench explicitly builds on established prior work—Bradley-Terry models (Hopkins & May, 2013), TrueSkill (Sakaguchi et al., 2014), Chatbot Arena's Elo approach (Zheng et al., 2023), and psychometric anchor calibration from educational testing. The paper cites all of this. The question is not "did they invent ranking theory?" but rather: **why hasn't anyone combined these pieces this way before, and does the combination solve problems that existing approaches don't?**

### The Problem Space: Why Pairwise Comparison Isn't Widely Used

Pairwise comparison has known advantages over rubric-based absolute scoring—it's more discriminative at the high end, more consistent for close calls, and avoids the compression problem where "pretty good" and "excellent" both score 8/10. Yet most LLM benchmarks use rubric scoring (MT-Bench, AlpacaEval, etc.), and MT evaluation moved *away* from pairwise ranking (WMT 2007–2016) toward Direct Assessment (2017+).

Why? Because existing pairwise approaches have significant practical problems:

| Problem | All-Pairs Pairwise | Elo / TrueSkill | Rubric LLM-Judge | **Anchored Pairwise** |
|---------|-------------------|-----------------|------------------|----------------------|
| **Quadratic cost** | ❌ O(n²) | ✅ Sampled | ✅ O(n) | ✅ O(n×k) |
| **Order dependence** | ✅ N/A | ❌ Match order affects final ratings | ✅ N/A | ✅ N/A |
| **Pool drift** | ✅ Fixed | ❌ Adding models changes all scores | ✅ Fixed | ✅ Fixed |
| **High-end compression** | ✅ Good discrimination | ✅ Good discrimination | ❌ Scores cluster at top | ✅ Good discrimination |
| **Bounded interpretable scores** | ❌ Raw win counts | ❌ Unbounded, relative | ✅ 0–10 scale | ✅ 0–10 LT scale |

**Anchored pairwise is the only approach that solves all five problems simultaneously.** This is not a minor optimization—it's a design point that no prior system occupied.

### Why This Combination Wasn't "Obvious"

The components existed for decades:
- Bradley-Terry preference modeling (1952)
- Anchor-based calibration in psychometrics (IRT/Rasch models)
- Pairwise ranking for MT evaluation (WMT 2007–2016)
- LLM-as-judge for preferences (2023+)

Yet:
- **WMT moved away** from pairwise ranking toward Direct Assessment in 2017
- **Chatbot Arena explicitly chose** floating Elo despite its known drift problems
- **Educational testing** uses anchor items for calibrating *test difficulty*, not for comparing *system outputs*
- **No LLM-as-judge benchmark** (MT-Bench, AlpacaEval, etc.) proposed freezing a base set of outputs

If this combination were truly obvious, someone would have done it. The fact that they didn't—despite the problems being well-known—suggests either (a) the problem wasn't clearly articulated, or (b) the solution wasn't seen.

**"Obvious in hindsight" is not the same as "obvious."** Many important ideas seem trivial once someone demonstrates them. The contribution is identifying a design point that solves real problems others hadn't addressed.

### Prior Work JP-TL-Bench Builds On

**1. Pairwise Ranking in MT (WMT 2007–2016)**
- WMT used relative ranking (annotators rank 5 systems per segment) from 2007–2011
- **TrueSkill** (Bayesian skill estimation from pairwise outcomes) was used 2012–2016 (Sakaguchi et al., 2014)
- **Bradley-Terry models** for MT competitions: Hopkins & May (2013) "Models of Translation Competitions"
- *Limitation:* All-pairs or floating pools; no fixed anchor set

**2. Direct Assessment and MQM (2017–present)**
- WMT shifted to Direct Assessment (absolute 0–100 scores) in 2017 (Graham et al., 2017)
- MQM fine-grained error annotation added later (Freitag et al., 2021)
- *Limitation:* Absolute scoring compresses at high end; expensive for iteration

**3. LLM Benchmarking with Elo**
- **Chatbot Arena / LMSYS** uses standard Elo with bootstrapped CIs (Zheng et al., 2023)
- Bradley-Terry MLE as alternative to Elo updates
- *Limitation:* Floating pool—adding models changes all scores; no stable reference frame

**4. Psychometric Anchor Calibration**
- Educational testing (IRT/Rasch models) uses "anchor items" with known difficulty to calibrate across test forms
- Enables cross-temporal comparability
- *Limitation:* Applied to item difficulty, not system comparison; not adopted in MT/LLM evaluation

### Synthesis Assessment

JP-TL-Bench's contribution is **the specific combination** applied to MT/LLM evaluation:
1. Fixed, versioned anchor set (from psychometrics) (`TECH-2026-050`)
2. Pairwise LLM-judge comparison (from Chatbot Arena) (`TECH-2026-031`)
3. Bradley-Terry aggregation (from WMT/ranking literature) (`TECH-2026-039`)
4. Bounded scoring transform (LT 0–10) for interpretability (`TECH-2026-039`)
5. Slice reporting by direction and difficulty (`TECH-2026-049`)
6. Full auditability (prompts, manifests, score reports)

This isn't "just good engineering"—it's identifying and occupying a design point that solves practical problems (cost, drift, compression, interpretability) that existing approaches don't address simultaneously. The fact that the components existed but nobody combined them this way for MT evaluation is itself meaningful.

**Key citations:**
- Hopkins & May (2013) "Models of Translation Competitions" (Bradley-Terry for MT)
- Sakaguchi et al. (2014) "Efficient Elicitation of Annotations for Human Evaluation of MT" (TrueSkill)
- Graham et al. (2017) "Continuous Measurement Scales in Human Evaluation of MT" (DA shift)
- Freitag et al. (2021) "Experts, Errors, and Context: A Large-Scale Study of Human Evaluation for MT" (MQM)
- Zheng et al. (2023) "Judging LLM-as-a-Judge with MT-Bench and Chatbot Arena" (Elo for LLMs)

---

## Are “classic” MT metrics outmoded for frontier JA translation?

Synthesis view:
- **Not outmoded** for what they’re good at: broad regression detection and large-scale comparability, especially when paired with MQM (as TranslateGemma does). (`TECH-2026-082`)
|- **Incomplete** for Japanese nuance and for developer inner-loop decisions among already-good models: you often need direction/context-sensitive diagnostics and preference-based separation. (`TECH-2026-087`, `TECH-2026-046`)

The most robust posture is “metrics + audits + preference-based discriminators,” not “replace metrics entirely.”

---

## Credence-Weighted Conclusions

| Conclusion | Credence | Key support | Key uncertainty |
|---|---:|---|---|
| JP-TL-Bench is a credible, auditable anchored pairwise protocol suitable for development-time discrimination in JA↔EN MT | 0.85 | TECH-2026-031, TECH-2026-050, TECH-2026-039 | Judge dependence/drift and anchor staleness over time |
| Direction-sliced evaluation is essential for JA↔EN; aggregate single-number scores can be misleading | 0.85 | TECH-2026-046, TECH-2026-047 | How much of the gap is intrinsic vs prompt/judge artifacts |
| WMT/MQM + learned metrics remain state-of-the-art for broad evaluation, but are not sufficient to capture all Japanese linguistic correctness concerns | 0.75 | TECH-2026-082, TECH-2026-087 | Degree to which MQM/document-level evaluation covers the "context impossibility" cases |
| The anchored pairwise combination is a meaningful contribution: it's the only approach that solves cost, drift, compression, and interpretability simultaneously | 0.80 | TECH-2026-050, TECH-2026-039, TECH-2026-032 | Whether adoption outside JA↔EN validates the general approach |

---

## Practical Next Steps (If we want to tighten the framework)

1. **Judge-sensitivity audit**: rerun a subset with 2–3 judges (or a judge panel) and quantify rank stability; explicitly test self-preference if the judge is an anchor.
2. **Context-aware slices**: add a "requires discourse context" tag to benchmark items and report those separately.
3. **Cross-paradigm correlation**: evaluate a shared model set with both JP-TL-Bench and llm-jp-eval MT (COMET) and identify systematic disagreements (register vs adequacy vs fluency).
4. **Small MQM audit set**: run professional MQM on a tiny curated subset (e.g., 10–20 items) focusing on keigo/pro-drop and compare to LT ordering.

---

## References

### MT Evaluation and Methodology
- Bojar, O., et al. (2016). "Findings of the 2016 Conference on Machine Translation (WMT16)." ACL.
- Freitag, M., et al. (2021). "Experts, Errors, and Context: A Large-Scale Study of Human Evaluation for Machine Translation." ACL.
- Graham, Y., et al. (2017). "Continuous Measurement Scales in Human Evaluation of Machine Translation." ACL.
- Hopkins, M. & May, J. (2013). "Models of Translation Competitions." ACL.
- Sakaguchi, K., et al. (2014). "Efficient Elicitation of Annotations for Human Evaluation of Machine Translation Quality." WMT.
- Zheng, L., et al. (2023). "Judging LLM-as-a-Judge with MT-Bench and Chatbot Arena." NeurIPS.

### Japanese Linguistics and MT Challenges
- Hangyo, M., Kawahara, D. & Kurohashi, S. (2013). "Japanese Zero Reference Resolution Considering Exophora and Author/Reader Mentions." EMNLP.
- Ide, S. (1989). "Formal forms and discernment: Two neglected aspects of universals of linguistic politeness." Multilingua 8(2-3).
- Iida, R., Inui, K. & Matsumoto, Y. (2007). "Zero-anaphora resolution by learning rich syntactic pattern features." ACL.
- Kamio, A. (1997). *Territory of Information*. John Benjamins.
- Kuno, S. (1973). *The Structure of the Japanese Language*. MIT Press.
- Matsumoto, Y. (1988). "Reexamination of the universality of face: Politeness phenomena in Japanese." Journal of Pragmatics 12(4).
- Maynard, S.K. (1989). *Japanese Conversation: Self-contextualization through Structure and Interactional Management*. Ablex.
- Nagata, M. (2017). "Document-level Neural Machine Translation." ACL workshop proceedings.
- Nakaiwa, H. & Shirai, S. (1996). "Anaphora Resolution of Japanese Zero Pronouns with Deictic Reference." COLING.
- Voita, E., Sennrich, R. & Titov, I. (2019). "When a Good Translation is Wrong in Context: Context-Aware Machine Translation Improves on Deixis, Ellipsis, and Lexical Cohesion." ACL.

### Document-Level MT
- Maruf, S., Saleh, F. & Haffari, G. (2021). "A Survey on Document-level Neural Machine Translation: Methods and Evaluation." ACM Computing Surveys.

---

## Analysis Log

| Pass | Date | Tool | Model | Duration | Tokens | Cost | Notes |
|------|------|------|-------|----------|--------|------|-------|
| 1 | 2026-01-24 | codex | gpt-5.2 | ~30m | ? | ? | Initial multi-source analysis + synthesis |
| 2 | 2026-01-24 | claude-code | claude-opus-4-5 | ~15m | ? | ? | Expanded prior art, added linguistic citations, upgraded to REVIEWED |
| 3 | 2026-01-24 | claude-code | claude-opus-4-5 | ~10m | ? | ? | Revised prior art framing per author feedback |

### Revision Notes

**Pass 1 (gpt-5.2)**: Initial analysis covering 11 sources. Created source analyses for JP-TL-Bench paper, repo, blog posts, TranslateGemma, Shisa model releases, and LiquidAI model card. Synthesized evaluation paradigms (COMET vs MQM vs LLM-judge), identified anchored pairwise design as primary contribution.

**Pass 2 (claude-opus-4-5)**: Continuation/refinement pass requested by user. Key additions:
- Significantly expanded "Japanese Linguistic Challenges" section with academic citations (Nakaiwa & Shirai 1996, Iida et al. 2007, Ide 1989, etc.)
- Expanded "Prior Art" section with WMT evaluation history (TrueSkill, DA, MQM), Bradley-Terry background, and psychometric anchor calibration analog
- Added full References section with 17 citations
- Upgraded rigor level from DRAFT to REVIEWED
- Added this analysis log

**Pass 3 (claude-opus-4-5)**: Author feedback on prior art framing. Key revisions:
- Removed strawman framing ("is there prior art?") — JP-TL-Bench explicitly cites prior work and doesn't claim de novo invention
- Renamed section to "What Makes Anchored Pairwise Evaluation Unique?"
- Added problem comparison table showing anchored pairwise is the only approach solving all five problems (quadratic cost, order dependence, pool drift, high-end compression, bounded scores)
- Added "Why This Combination Wasn't 'Obvious'" section with specific examples (WMT moved away from pairwise; Chatbot Arena chose floating Elo; no LLM-judge benchmark proposed fixed anchors)
- Revised assessment: this is a meaningful contribution to a previously unoccupied design point, not "just good engineering"
- Updated credence-weighted conclusions to reflect revised framing
