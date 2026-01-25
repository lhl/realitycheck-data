https://chatgpt.com/c/6975edcc-b140-8321-8ace-1d1f5735d99f

> I've been using a new analysis tool that helps separate rhetoric from claims and also does some referencing for citations/evidence etc. I'm curious how you would characterize its performance on topics like this. Is there something it's missing, is it largely accurate?

From what you pasted, your tool is doing a lot of the *right* things for a “rhetoric → checkable claims → evidence” workflow, and several of its key factual anchors do line up with primary/credible sources. But there are also a few systematic gaps that will matter a lot on politically charged, legally technical topics like ICE/DHS enforcement—especially around **scope**, **agency attribution**, **primary-source capture**, and **update/correction handling**.

## How I’d characterize its performance (overall)

### What it’s doing well

* **Separating “authoritarian-toolkit rhetoric” from falsifiable subclaims.** The list-format post (“ICE says it can…”) is designed to make you accept a *bundle* by emotional momentum. Your tool correctly identifies that bundle structure and flags the key weakness: **overgeneralization / scope erasure** (“can” as universal vs conditional).
* **Explicitly distinguishing** (even if not perfectly) between:

  * *legal authority* (statute/regulation/case law),
  * *agency position* (what ICE/DHS claims internally or in litigation),
  * *observed practice / incidents* (what happened in a place/time, possibly disputed).
* **Using real primary law where appropriate.** Example: it cites the “right to counsel at no government expense” provision in removal proceedings (8 U.S.C. § 1362), which is exactly the kind of statute that cleanly falsifies the *categorical* framing “no lawyer access.” ([Legal Information Institute][1])
* **Calling out “deadly force” overreach** as rhetorical rather than policy-like permission. The relevant DHS/ICE use-of-force regulation limits deadly force to situations involving imminent danger of death/serious physical injury—so “they can shoot you for interference” is not supported as a general authorization. ([eCFR][2])
* **Strong support on the “home entry memo exists / asserts X” point.** There really is high-quality reporting that a May 12, 2025 memo signed by Acting ICE Director Todd Lyons instructs officers they may use administrative warrants (Form I‑205) for home arrests with “necessary and reasonable” force. ([AP News][3])

So as a *reader’s guide*—“which bullets are checkable and which are rhetorical inflation”—it’s mostly doing its job.

### Where it’s weaker than it looks

Even though it “sounds rigorous,” it still has some failure modes that can mislead:

1. **It sometimes treats secondary reporting as if it were the best available evidence—even when the primary document is obtainable.**
   The AP story links to a DocumentCloud PDF containing the whistleblower disclosure and embedded memo excerpts. That document includes the key language (Form I‑205 + force + knock/announce + final order predicate) and contextual details (OGC determination, distribution practices, training conflicts). 
   If the tool didn’t ingest that PDF and quote/attribute the critical lines directly, it’s leaving accuracy on the table.

2. **It doesn’t reliably track *corrections/updates* to sources.**
   A concrete example: the Reason piece it cites about “filming raids = domestic terrorism” contains an explicit correction noting the article was updated to remove reference to a DOJ memo that *does not* refer to merely filming. ([Reason.com][4])
   That’s a big deal for an “evidence/citations” tool: on fast-moving controversies, corrections are common, and failing to detect them makes the tool look confident while quietly drifting out of date.

3. **“ICE” vs “DHS/CBP/Border Patrol” attribution is still leaky.**
   Your tool *notices* the problem (“ICE used loosely to refer to broader DHS enforcement”), but it still uses mixed-agency incidents as if they directly validate “ICE positions.” On this topic, that distinction is not pedantry—it affects:

   * which legal authorities apply (e.g., Border Patrol/CBP contexts differ),
   * which policies/memos control,
   * which oversight pathways exist,
   * and what “ICE can do” even means.

4. **It compresses compound claims into single rows, which inflates perceived certainty.**
   Example: “ICE can detain people broadly… including children… and errors can result in detention of citizens” mixes at least three separable propositions with different evidentiary status. There is very specific reporting about a U.S. citizen detained after warrantless/forced home entry in Minnesota (a discrete incident) ([PBS][5]), and separate reporting about small children being detained in enforcement actions (another discrete incident class). ([ABC News][6])
   Bundling them makes the “credence number” feel more grounded than it really is.

5. **Numeric credences look calibrated, but the method isn’t auditable.**
   A “0.90” on a claim can be reasonable *if* it’s anchored to a primary memo quote (which exists), but the same interface also assigns mid-range credences to claims where the only support is anecdotal incidents. Without a transparent rubric (“0.9 means X; 0.6 means Y”), these numbers can become “confidence theater.”

## Is it “largely accurate” here?

On balance: **directionally yes**, with two caveats:

* It’s most accurate when it phrases claims as **“ICE/DHS asserted in a memo / argued in court / did in incident X”** rather than **“ICE can do X (as a general power).”**
  The home-entry point is a good example: the memo’s *existence and content* are strongly supported by reporting and the whistleblower disclosure PDF. ([AP News][3])
  Whether it’s *lawful* as a general matter is a separate question (constitutional doctrine, litigation outcomes, injunctions, etc.).

* The tool is least reliable where it leans on **rhetorical extrapolation** (“therefore no day in court,” “therefore they can’t bring you back,” “therefore lethal force is justified by ‘terrorism’ labeling”) without consistently separating:

  * what the law says,
  * what the agency claims,
  * what happened in a few high-salience events,
  * and what is being predicted as a systemic outcome.

## The biggest things it’s missing (and how I’d upgrade it)

### 1) A “primary-source-first” rule for legal/policy claims

For anything like “ICE memo says…” or “DHS policy is…”, it should try in order:

1. official PDF / DocumentCloud / court filing,
2. then high-quality reporting summarizing it,
3. then commentary.

Here, the DocumentCloud PDF is available and contains the critical language. 

### 2) A dedicated field for *scope conditions*

Instead of burying qualifiers in prose, enforce structured scope fields:

* **Who** (noncitizens w/ final order? anyone “believed to be an alien”?)
* **Where** (home vs public space; border zone vs interior)
* **Process** (expedited removal vs full removal proceedings)
* **Time sensitivity** (short notice vs typical notice)
* **Actor** (ICE ERO vs CBP/Border Patrol vs “DHS”)

This would reduce the classic failure mode where “can” becomes “can anywhere/always.”

### 3) Source-quality weighting separate from “evidence type”

Right now E4 lumps together “credible journalism” and (sometimes) weaker outlets. A better model is:

* **Evidence type** (law / memo / reporting / opinion)
* **Source reliability score** (per outlet + per article type)
* **Claim match score** (does the source directly support the exact phrasing?)

That would prevent one sensational article from “anchoring” an overstated claim.

### 4) Correction/recency detection

At minimum:

* Detect explicit “Correction/Update” blocks (like Reason’s). ([Reason.com][4])
* Prefer the most recently updated version.
* Record “last checked” timestamps per cited URL.

### 5) Split “legal authority” vs “practical access” vs “guaranteed outcome”

Example: counsel.

* Legal rule: counsel permitted at no expense to government (8 U.S.C. § 1362). ([Legal Information Institute][1])
* Practical reality: access can be impeded (transfers, remote detention, etc.).
  Those are different claims and should not share one credence score.

### 6) Treat “court opinion” details with internal labels

Your tool is smart to cite actual Supreme Court material on third-country removals. ([Supreme Court][7])
But it should explicitly label whether a passage is:

* majority,
* concurrence,
* dissent,
* stay order reasoning,
  because readers often over-weight “it’s SCOTUS” without noticing *which voice* is speaking.

---

If you want a short takeaway: **the structure is strong and many anchors are real, but it needs (a) primary-document ingestion, (b) correction tracking, and (c) stricter scope/agency disambiguation** to avoid “high-confidence summaries of ambiguous powers,” which is the failure mode that matters most on topics like this.

* [AP News](https://apnews.com/article/00d0ab0338e82341fd91b160758aeb2d?utm_source=chatgpt.com)
* [Reuters](https://www.reuters.com/world/us-appeals-court-pauses-lower-court-order-restraining-immigration-agents-use-2026-01-21/?utm_source=chatgpt.com)
* [The Washington Post](https://www.washingtonpost.com/opinions/2026/01/22/ice-warrants-memo-fourth-amendment-unconstitutional/?utm_source=chatgpt.com)
* [Houston Chronicle](https://www.houstonchronicle.com/news/houston-texas/immigration/article/ice-warrants-homes-fourth-amendment-21309274.php?utm_source=chatgpt.com)
* [AP News](https://apnews.com/article/0af10ec433181aa9300deea26d1cc8c5?utm_source=chatgpt.com)
* [AP News](https://apnews.com/article/76ecdc4b502dc8b3f3acd18a10ed8279?utm_source=chatgpt.com)

[1]: https://www.law.cornell.edu/uscode/text/8/1362?utm_source=chatgpt.com "8 U.S. Code § 1362 - Right to counsel - Cornell Law School"
[2]: https://www.ecfr.gov/current/title-8/chapter-I/subchapter-B/part-287/section-287.8 "
    eCFR :: 8 CFR 287.8 -- Standards for enforcement activities.
  "
[3]: https://apnews.com/article/00d0ab0338e82341fd91b160758aeb2d?utm_source=chatgpt.com "Immigration officers assert sweeping power to enter homes without a judge's warrant, memo says"
[4]: https://reason.com/2025/12/26/justice-department-says-filming-immigration-raids-is-domestic-terrorism/ "Could the feds throw you in jail for merely filming ICE immigration raids?"
[5]: https://www.pbs.org/newshour/nation/a-u-s-citizen-says-ice-forced-open-the-door-to-his-minnesota-home-and-removed-him-in-his-underwear-after-a-warrantless-search?utm_source=chatgpt.com "A U.S. citizen says ICE forced open the door to his ..."
[6]: https://abcnews.go.com/US/5-year-asylum-seeker-detained-ice-expands-enforcement/story?id=129451987&utm_source=chatgpt.com "5-year-old asylum seeker detained as ICE expands enforcement in Minnesota"
[7]: https://www.supremecourt.gov/opinions/24pdf/24a1153_l5gm.pdf "24A1153 DHS v. D.V.D. (06/23/2025)"

> Can you do your own analysis on sources etc and see how you'd augment, modify or contradict any of the claims, evidence, credence etc.

Below is how I’d *personally* re-grade and re-frame the analysis, based on (a) primary law (U.S. Code/CFR + Supreme Court cases) and (b) the reporting/court filings that the analysis itself points to. I’ll keep your claim IDs as anchors, but in several places I’d split a single “big” claim into narrower subclaims, because the truth value changes a lot depending on whether you mean **(1) legal authority on the books**, **(2) ICE/DHS’s asserted position**, or **(3) observed practice/incidents**.

## High-level: how your tool performed (what it got right, what it missed)

### What it did well

* **It correctly treats the X post as rhetorical packaging**, and it repeatedly flags that “ICE can” is ambiguous between *legal authority*, *agency litigation stance / internal memo*, and *field practice*. That’s exactly the right “first move” on a post like this. ([AP News][1])
* **It correctly identifies the strongest factual core** as (i) the “carry papers” statute, (ii) reporting about an ICE internal memo on administrative warrants + home entry, and (iii) ongoing third‑country removal litigation where notice/process is a central dispute. ([Legal Information Institute][2])

### What I think it’s missing / where I’d modify it

1. **It sometimes slides from “ICE asserts X” → “ICE can lawfully do X.”**
   Those are not the same proposition, and the difference matters most for GOV‑2026‑033 (home entry). The *existence of the asserted position* is strongly supported; the *lawfulness* is contested and arguably in tension with DHS’s own regulations and at least some federal court reasoning. ([AP News][1])

2. **It under-weights a big “detention due process” development that bears directly on claims 5/6 (lawyer/court access): the 2025 policy shift on bond hearings.**
   If the AP/WaPo reporting is accurate, that policy change is a more direct, system-wide lever on “meaningful day in court” and “ability to fight your case from outside detention” than some of the post’s more sensational bullets. ([AP News][3])

3. **It treats some corrected/contested journalism as stronger than it is.**
   Example: the “DOJ memo says merely filming raids is domestic terrorism” idea looks shakier because even the cited Reason piece notes a correction removing the “merely filming” framing. ([Reason.com][4])

4. **It misses a penalty nuance on the “carry papers” claim**: while 8 U.S.C. § 1304(e) contains an old $100 fine cap in-text, federal fine statutes can raise practical exposure; a Federal Register notice explicitly describes a higher fine ceiling. That doesn’t change the *duty* to carry, but it affects “what happens if you don’t.” ([Legal Information Institute][2])

---

## My claim-by-claim “diff” (what I’d keep, change, or contradict)

### GOV-2026-033 — *Administrative-warrant home entry (“ICE can enter homes without a judge warrant”)*

**My verdict:** *Keep the “ICE has asserted this position” claim as high-confidence; downgrade any implication that it is clearly lawful or universally implemented.*

* **What I’d keep (and treat as verified):**
  Multiple outlets report an internal ICE memo (dated May 12, 2025; signed by Acting Director Todd Lyons) asserting that officers may use an administrative warrant (Form I‑205) and “necessary and reasonable” force to enter a residence to arrest someone with a final removal order, after “knock and announce.” ([AP News][1])

* **What I’d add (missing constraint / why lawfulness is genuinely contested):**
  DHS’s own regulation for “site inspections” says officers may not enter “a residence including the curtilage” to question occupants about immigration status **unless** they have a warrant or consent, and if denied access “a warrant may be obtained.” ([Legal Information Institute][5])
  And a federal district court order in *Kidd v. Mayorkas* includes language recognizing that Fourth Amendment warrant requirements apply to home/curtilage entries under that regulatory framework. ([ACLU of Socal][6])
  That doesn’t automatically dispose of the memo’s legal theory (because ICE can argue it’s not a “site inspection” but execution of a removal warrant), but it’s strong counterweight that your tool only partially foregrounds.

* **How I’d rewrite the claim for precision (recommended split):**

  1. **[F]** “ICE issued/used guidance asserting that an I‑205 administrative warrant can justify forced entry into a target’s residence (after knock/announce) to execute a final removal order.” (High confidence) ([AP News][1])
  2. **[H]** “That asserted authority is lawful under the Fourth Amendment nationwide.” (Much lower confidence / unresolved) ([Legal Information Institute][5])
  3. **[H]** “This is now routine practice across ICE field offices.” (Unknown; reporting suggests limited circulation + uneven implementation) ([The Washington Post][7])

* **Credence adjustment:**

  * As written in your YAML (“ICE has asserted authority…”): **0.90 → 0.93**
  * If read as “ICE is legally allowed to do this as a general rule”: **I’d put ~0.35–0.50** (contested, fact-dependent, and in tension with other legal materials). ([Legal Information Institute][5])

---

### GOV-2026-034 — *“Carry papers” requirement*

**My verdict:** *Accurate as a statement of federal law, but I’d tighten scope + update the penalty discussion.*

* **What’s solid:**
  8 U.S.C. § 1304(e) states that “every alien, eighteen years of age and over, shall at all times carry” registration/receipt documentation, and makes failure a misdemeanor. ([Legal Information Institute][2])

* **What I’d add (penalty nuance):**
  A Federal Register notice explicitly describes higher fine exposure (via general federal fine provisions) than the statute’s $100 figure suggests. ([Federal Register][8])

* **What I’d clarify (scope):**

  * This is not “ICE policy”; it’s a statute.
  * “Alien” includes lawful permanent residents and many other noncitizens; it does **not** apply to U.S. citizens. ([Legal Information Institute][2])
  * The statute doesn’t itself authorize random stops; it’s a possession requirement (enforcement authority is a separate question). (This last point is legal interpretation; I’m stating it cautiously.)

* **Credence adjustment:** **0.95 → 0.98** (as a legal-duty claim). ([Legal Information Institute][2])

---

### GOV-2026-035 — *Biometrics “scanner supremacy”*

**My verdict:** *The “sometimes relies on biometrics / sometimes rejects documents” part is plausible and has incident support; the “only biometrics matter” generalization is not established.*

* **Best support I can validate quickly:**
  ABC reports a U.S. citizen said agents forced entry and detained him; DHS’s response included the claim he “refused to be fingerprinted or facially identified,” which implies biometric verification was treated as central in that encounter. ([ABC News][9])

* **What I’d change:**
  Your tool’s version (“ICE can disregard paper documents and rely primarily on biometrics”) is fine as a **bounded hypothesis** (“in some encounters”), but I’d explicitly mark the *general-rule* reading as unproven.

* **Credence adjustment:** **0.55 stays about right** *if* the claim is scoped to “some encounters.”
  If read as “ICE policy is to ignore documents generally,” I’d drop to **~0.30–0.40**. ([ABC News][9])

---

### GOV-2026-036 — *Broad detention authority incl. children; mistaken detention of citizens*

**My verdict:** *The “broad authority to question/detain briefly” is real but conditional; “children/citizens can get swept up” is supported by recent reporting; the “regardless of status” reading is overstated.*

* **Primary-law anchor (what officers are authorized to do):**

  * Federal law authorizes immigration officers to interrogate “any alien or person believed to be an alien” about their right to be/remain and to make certain arrests without warrant (subject to conditions). ([GovInfo][10])
  * DHS regs also describe brief detentions for questioning based on “reasonable suspicion” and allow questioning in public-access areas, while requiring warrant/consent for certain non-public areas. ([Legal Information Institute][5])

* **Practice/incidents (children):**

  * AP reports federal agents took a 5-year-old boy and his father to a Texas detention facility, with school officials alleging the child was used as “bait” to get someone to open the door; DHS disputed aspects. ([AP News][11])
  * Reuters video reporting also describes at least four children detained in the same Minnesota-area context. ([Reuters Japan][12])

* **Practice/incidents (citizens):**

  * ABC reports a U.S. citizen alleging wrongful detention during an ICE encounter; even if disputed, it’s evidence that mistaken detention is a live risk in high-tempo operations. ([ABC News][9])

* **Credence adjustment:**

  * For a *careful* claim (“ICE/CBP can briefly detain on reasonable suspicion; and recent incidents show children and at least one citizen have been detained during operations”): **0.65 → 0.80–0.85**. ([Legal Information Institute][5])
  * For the *X-post absolute* (“no matter status/age anywhere”): I’d keep **low (~0.25–0.35)** because legal authority is conditional and citizen detention is not lawful when they’re correctly identified as citizens. ([Legal Information Institute][5])

---

### GOV-2026-037 — *Indefinite detention + “no access to a lawyer”*

**My verdict:** *As written, it’s mostly wrong. But there’s a very strong “adjacent” claim that *is* true: no right to government-paid counsel + policies/practices can produce prolonged detention that severely impairs effective access to counsel.*

* **Counsel (what the law actually says):**
  In removal proceedings, a person has the privilege of counsel **“at no expense to the Government.”** That is not “no lawyer,” but it is “no guaranteed appointed lawyer.” ([Legal Information Institute][13])

* **“Indefinite” detention (legal constraints):**
  The Supreme Court has held that the post-removal-order detention statute cannot be read to permit **indefinite** detention; detention is limited to a period “reasonably necessary” to effect removal (with a presumptive 6-month benchmark in the case law). ([Legal Information Institute][14])

* **But: prolonged detention is still a real issue (and your tool underweights this):**

  * Supreme Court precedent also rejects reading certain detention statutes to require periodic bond hearings as a matter of statutory interpretation (leaving constitutional challenges to be litigated). ([Justia Law][15])
  * And recent reporting describes an ICE directive/policy shift limiting bond hearing access for large categories of people, which can translate into long detention while cases proceed. ([AP News][3])

* **Credence adjustment:**

  * For the claim as stated (“indefinitely with no access to a lawyer”): **0.20 is fair; I might go 0.15–0.25**. ([Legal Information Institute][13])
  * For a revised, more accurate claim (“no right to government-appointed counsel + prolonged detention without bond is possible for some categories, which can practically impede access to counsel”): I’d put **0.75–0.85**. ([Legal Information Institute][13])

---

### GOV-2026-038 — *“No meaningful day in court”*

**My verdict:** *Too categorical. The real story is “category-dependent process,” with some pathways that sharply limit hearings and judicial review.*

* **What’s true (conditional):**

  * Some noncitizens are placed in processes that explicitly do **not** provide a full immigration judge hearing (e.g., parts of expedited removal; stowaway provisions). ([Legal Information Institute][16])
  * The Supreme Court has upheld significant limits on federal court review in the expedited-removal context (the opinion describes the statutory scheme and the constrained review posture). ([Supreme Court][17])

* **What’s misleading in the blanket framing:**
  Many removals still run through immigration court proceedings where a person can appear before an IJ (though quality/representation varies). Your tool notes this, but I’d more aggressively force a split into: “expedited/reinstatement/admin” vs “regular removal proceedings.”

* **Credence adjustment:** **0.45 is plausible** as a “felt reality / risk framing,” but **as a descriptive general fact** I’d go **~0.30–0.40** unless you specify the category being discussed. ([Supreme Court][17])

---

### GOV-2026-039 — *Third-country removals on short notice with limited safeguards*

**My verdict:** *This one is strongly supported—especially because you’re not relying only on journalism; there are Supreme Court / appellate filings describing the factual disputes.*

* **Strong support:**
  The opposition brief in *DHS v. D.V.D.* describes attempted removals to Libya (13 people) and removals/attempted removals to South Sudan with notice as short as “the night before,” plus ongoing litigation over what process is required before third‑country removals. ([Supreme Court][18])
  The Supreme Court emergency-order document also reflects active litigation over these issues (order + dissent discussing removals and notice). ([Supreme Court][19])

* **Legal framework:**
  8 U.S.C. § 1231 governs detention/removal after an order of removal (including the “removal period”); it’s the statutory home for much of the “after final order” machinery in this space. ([Legal Information Institute][20])

* **Credence adjustment:** **0.85 → 0.90–0.93** (for the scoped claim “some people have been/attempted to be removed to third countries with very short notice and disputed safeguards”). ([Supreme Court][18])

---

### GOV-2026-040 — *“ICE can’t/won’t bring you back after a mistake”*

**My verdict:** *Absolute version is wrong; “return is not automatic and may be resisted” is plausible.*

* **Why “can’t” is not right (there are mechanisms and court orders):**

  * A federal docket entry (in the same third‑country removal litigation universe) notes that courts regularly order facilitation of return for wrongfully removed individuals and cites ICE’s “Facilitating Return” directive. ([Justia Dockets & Filings][21])

* **What I’d change:**
  Your tool already flags the “can’t” absolute as false, which I agree with. But I’d also tighten the *“generally”* language: “generally cannot” is hard to support without stats; the evidence supports “return may require litigation and is contested,” not “generally impossible.”

* **Credence adjustment:**

  * As written (“generally cannot or will not”): **0.55 → ~0.35–0.45** (directionally plausible but overclaims “generally”). ([Justia Dockets & Filings][21])
  * Revised claim (“return is possible but often requires court intervention; government sometimes disputes ability/duty”): **~0.70**. ([Justia Dockets & Filings][21])

---

### GOV-2026-041 — *“If you interfere, ICE can shoot you and call you a terrorist”*

**My verdict:** *As a “policy permission” claim, I would directly contradict it.*

* **Primary law is clear on the deadly-force standard:**
  DHS regs state deadly force may be used only when the officer has reasonable grounds to believe it’s necessary to protect against **imminent danger of death or serious physical injury**—not mere “interference.” ([Legal Information Institute][5])

* **What’s true but different:**
  “Domestic terrorism” rhetoric can show up in post-incident messaging, but that rhetoric does not itself expand the legal deadly-force standard. (That’s an inference; the legal standard is the key anchor.)

* **Credence adjustment:** **0.15 → 0.05** for the claim as stated. ([Legal Information Institute][5])

---

### GOV-2026-042 — *Pattern of “domestic terrorist” labeling tied to immigration enforcement / observation*

**My verdict:** *There is meaningful evidence of “domestic terrorism” framing in this ecosystem, but the claim should be narrowed and better sourced to avoid overreach.*

* **What I can support:**

  * DHS/leadership messaging around at least one high-profile Minneapolis incident has used “domestic terrorism” language (The Marshall Project reports DHS officials described the incident that way). ([The Marshall Project][22])
  * DOJ leadership has also issued directives emphasizing “domestic terrorism” investigations into certain movements/groups (Reuters reporting on a Bondi memo). ([Reuters][23])
  * Civil-liberties orgs and local reporting document threats/retaliation claims around recording immigration enforcement (ACLU press release; MPR reporting on data/intimidation). ([American Civil Liberties Union][24])
  * AP reporting describes overcharging/“domestic terrorist” rhetoric not consistently holding up in court in protest-related cases, which is relevant to whether “terrorism” labeling is systematic fact vs political messaging. ([AP News][25])

* **What I’d explicitly downgrade:**
  Claims that “merely filming” is treated as domestic terrorism hinge on shaky sourcing; the Reason piece itself includes a correction that undercuts the strongest version of that claim. ([Reason.com][4])

* **Credence adjustment:**
  For the claim as your tool states it (“repeatedly labeled… often immediately after events”): **0.75 → ~0.60–0.70** (plausible and partially supported, but “repeatedly” + scope across “observation/filming” needs tighter, more primary documentation). ([The Marshall Project][22])

---

## Two concrete “additions” I’d make to your tool’s output

### Addition A: explicitly track “asserted authority vs lawful authority” as separate fields

Your tool *talks* about this distinction, but the table format doesn’t enforce it. For GOV‑2026‑033 in particular, I’d add two boolean columns:

* **“Asserted by ICE/DHS?”** (yes, strongly supported) ([AP News][1])
* **“Clearly lawful under controlling precedent?”** (unknown/contested; conflicts/tensions exist) ([Legal Information Institute][5])

This prevents the most common reader error: confusing “a leaked memo exists” with “courts have upheld this practice.”

### Addition B: incorporate the 2025 bond-hearing shift into GOV‑2026‑037/038

If your goal is “separating rhetoric from operational reality,” the bond-hearing policy shift is a more operationally central “due process lever” than some of the scarier-sounding bullets. ([AP News][3])

---

## Bottom line

If I treat your tool’s output as a *fact-checking+framing assistant*, it’s **directionally good**: it identifies the claims that really can be checked, and it already downrates the most sensational pieces (indefinite detention/no lawyer; “shoot you because terrorist”). Where I’d improve it is mostly **precision mechanics**:

* Split claims so “ICE memo asserts X” doesn’t silently become “X is lawful everywhere.”
* Tighten quantifiers (“generally,” “anywhere,” “no matter status”) unless you have stats.
* Prefer primary documents (regulations, court filings) for legal-process claims—and use journalism mainly for *what happened* and *what officials said*.

If you want, I can rewrite your “Key Claims” table into a revised version that *enforces* these splits (asserted vs lawful vs practiced) while keeping your evidence-level scheme—using only the sources above.

[1]: https://apnews.com/article/00d0ab0338e82341fd91b160758aeb2d "https://apnews.com/article/00d0ab0338e82341fd91b160758aeb2d"
[2]: https://www.law.cornell.edu/uscode/text/8/1304 "https://www.law.cornell.edu/uscode/text/8/1304"
[3]: https://apnews.com/article/e1c2322c3f88c1f7d7e83c8c42109cb6 "https://apnews.com/article/e1c2322c3f88c1f7d7e83c8c42109cb6"
[4]: https://reason.com/2025/12/26/justice-department-says-filming-immigration-raids-is-domestic-terrorism/ "https://reason.com/2025/12/26/justice-department-says-filming-immigration-raids-is-domestic-terrorism/"
[5]: https://www.law.cornell.edu/cfr/text/8/287.8 "https://www.law.cornell.edu/cfr/text/8/287.8"
[6]: https://www.aclusocal.org/app/uploads/drupal/sites/default/files/kidd_msj_order.pdf "https://www.aclusocal.org/app/uploads/drupal/sites/default/files/kidd_msj_order.pdf"
[7]: https://www.washingtonpost.com/immigration/2026/01/22/ice-memo-enter-homes-warrant/ "https://www.washingtonpost.com/immigration/2026/01/22/ice-memo-enter-homes-warrant/"
[8]: https://www.federalregister.gov/documents/2025/03/12/2025-03944/alien-registration-form-and-evidence-of-registration "https://www.federalregister.gov/documents/2025/03/12/2025-03944/alien-registration-form-and-evidence-of-registration"
[9]: https://abcnews.go.com/US/wireStory/us-citizen-ice-removed-minnesota-home-underwear-after-129372047 "https://abcnews.go.com/US/wireStory/us-citizen-ice-removed-minnesota-home-underwear-after-129372047"
[10]: https://www.govinfo.gov/content/pkg/USCODE-2013-title8/pdf/USCODE-2013-title8-chap12-subchapII-partIX-sec1357.pdf "https://www.govinfo.gov/content/pkg/USCODE-2013-title8/pdf/USCODE-2013-title8-chap12-subchapII-partIX-sec1357.pdf"
[11]: https://apnews.com/article/immigration-minnesota-boy-father-detained-342f319fafb766d13afe07f5bcc1f112 "https://apnews.com/article/immigration-minnesota-boy-father-detained-342f319fafb766d13afe07f5bcc1f112"
[12]: https://jp.reuters.com/video/watch/idRW919022012026RP1/ "https://jp.reuters.com/video/watch/idRW919022012026RP1/"
[13]: https://www.law.cornell.edu/uscode/text/8/1362 "https://www.law.cornell.edu/uscode/text/8/1362"
[14]: https://www.law.cornell.edu/supct/html/99-7791.ZS.html "https://www.law.cornell.edu/supct/html/99-7791.ZS.html"
[15]: https://supreme.justia.com/cases/federal/us/583/15-1204/ "https://supreme.justia.com/cases/federal/us/583/15-1204/"
[16]: https://www.law.cornell.edu/uscode/text/8/1225 "https://www.law.cornell.edu/uscode/text/8/1225"
[17]: https://www.supremecourt.gov/opinions/19pdf/19-161_g314.pdf "https://www.supremecourt.gov/opinions/19pdf/19-161_g314.pdf"
[18]: https://www.supremecourt.gov/DocketPDF/24/24A1153/362298/20250604143617283_DHS%20v.%20DVD%20-%20Opp%20Stay%20-%20FINAL.pdf "https://www.supremecourt.gov/DocketPDF/24/24A1153/362298/20250604143617283_DHS%20v.%20DVD%20-%20Opp%20Stay%20-%20FINAL.pdf"
[19]: https://www.supremecourt.gov/opinions/24pdf/24a1153_l5gm.pdf "https://www.supremecourt.gov/opinions/24pdf/24a1153_l5gm.pdf"
[20]: https://www.law.cornell.edu/uscode/text/8/1231 "https://www.law.cornell.edu/uscode/text/8/1231"
[21]: https://docs.justia.com/cases/federal/district-courts/massachusetts/madce/1%3A2025cv10676/282404/64 "https://docs.justia.com/cases/federal/district-courts/massachusetts/madce/1%3A2025cv10676/282404/64"
[22]: https://www.themarshallproject.org/2026/01/07/ice-minneapolis-shooting-renee-good "https://www.themarshallproject.org/2026/01/07/ice-minneapolis-shooting-renee-good"
[23]: https://www.reuters.com/legal/government/bondi-orders-law-enforcement-investigate-us-groups-over-accusations-domestic-2025-12-05/ "https://www.reuters.com/legal/government/bondi-orders-law-enforcement-investigate-us-groups-over-accusations-domestic-2025-12-05/"
[24]: https://www.aclu.org/press-releases/aclu-demands-information-from-dhs-about-alarming-pattern-of-retaliation-against-those-recording-immigration-agents "https://www.aclu.org/press-releases/aclu-demands-information-from-dhs-about-alarming-pattern-of-retaliation-against-those-recording-immigration-agents"
[25]: https://apnews.com/article/591f155d50c13756842e033ea23f16d3 "https://apnews.com/article/591f155d50c13756842e033ea23f16d3"

