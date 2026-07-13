---
title: "Comparing Possible Plans"
byline: "Eli Lifland"
source_url: "https://ai-2040.com/supplements/comparing-possible-plans"
retrieved_at: "2026-07-11T06:00:49+00:00"
conversion: "rendered HTML to GitHub-Flavored Markdown with Pandoc"
---

# Comparing Possible Plans

**Byline:** Eli Lifland

# Introduction

In this supplement I’ll estimate how well each plan does on various intermediate metrics, and its chance of leading to a great future. I discuss quantitative metrics for the sake of concreteness, however I’m very much not confident in my precise estimates. I am confident in the conclusion that Plan A is substantially better than Plans B-D. For plans that I think could be competitive with Plan A, see [this table](comparing-possible-plans.md#plans-that-might-be-competitive-with-plan-a).

I estimate how good each plan would be conditional on the government and/or leading companies attempting to execute it. The below aren’t meant to be an exhaustive taxonomy; I am considering what would happen if roughly the described plan is attempted, rather than bucketing every possible future into the plan it is closest to. For more detail on how I classify trajectories into plans, see [below](comparing-possible-plans.md#classifying-trajectories-into-plans).

The plans I consider are:

1.  **Plan A (as implemented specifically in the scenario): Verified slowdown + total research transparency.** A verified international slowdown deal coupled with complete transparency of AI research. AI capabilities are scaled up while maintaining high confidence in safety but balancing risks from [deal decline](deal-decline.md) and [covert projects](covert-ai-projects.md).

2.  **Plan A: Verified slowdown + substantial transparency.** To be more generally classified as Plan A, the implementation must involve a substantial verified slowdown which involves continued AI scaling, as opposed to an indefinite halt. It must involve transparency at least as strong as embedded auditors from foreign governments which publish reports to governments (and for which redacted versions are made public), as described in our [filtered transparency proposal](transparency-plan.md). Other aspects of the plan, such as [mutually assured compute destruction](deal-decline.md#mutually-assured-compute-destruction-destroying-compute-fabs-and-robots), are not required.

3.  **Plan B-kinetic: Sabotage China kinetically and burn some lead.** Sabotaging China in order to get more of a lead to burn on safety, with the willingness to escalate to large-scale kinetic attacks such as by drones or conventional missile strikes. To be classified as Plan B the US must have the intention to use their lead over China for safety purposes, and must in practice slow takeoff by at least 3 months.

4.  **Plan B-cyber: Sabotage China non-kinetically and burn some lead.** The same as Plan B-kinetic, but without willingness to escalate to large-scale kinetic attacks. This could include cyber and supply chain attacks.

5.  **Plan C+: Domestic regulation and slow China without sabotage.** The US buys substantial time via domestic regulation, without sabotaging China. They instead aim to slow down China via non-sabotage measures such as export controls and giving green cards to Chinese talent. Requires at least a 2 month slowdown.

6.  **Plan C: Leading project burns some lead.** The leading AI project burns some of its lead on safety, and potentially coordinates with other frontier projects for a further slowdown without domestic regulation. Requires at least a 1 month slowdown.

7.  **Plan D: Race.** Frontier AI projects race through the intelligence explosion at nearly max speed, devoting a nonzero but small percentage of resources to safety (at least 1%; lower would count as [Plan E](comparing-possible-plans.md#plans-that-we-think-are-clearly-worse-than-plan-a)).

There are also other plans that the government could attempt to implement. Some of these are discussed [below](comparing-possible-plans.md#other-plans).

**For simplicity,** **I assume that:**

1.  **The minimum-length takeoff from Automated Coder (AC) to Top-Expert-Dominating-AI (TED-AI) is slightly less than a year, from the start of 2030 to the end of 2030.** This matches the [default Plan A AI Futures M](takeoff-supplement.md)[odel trajectory](takeoff-supplement.md). The minimum-length takeoff is what happens if the leading AI projects go at maximum speed.

2.  **All plans can begin implementation in early 2029** as in the Plan A scenario, though for Plans C and D this doesn’t matter as the plan involves doing nothing until takeoff is underway. This still might involve some safety work, if doing so is useful for advancing capabilities.

I remove these conditionals and present other authors’ views [below](comparing-possible-plans.md#comparing-authors-views-on-plan-likelihood-and-outcomes).

# Plan assessment table

These estimates are all rough best guesses, and the specifics of them aren’t load-bearing to our recommendation of Plan A (though the high-level takeaways are).

How the plans compare according to EliMedianCompetentExpand allToggle **Median** vs **Competent** to switch between the median across implementations and each plan executed competently. Hover any plan, metric, or value for its reasoning, or **click within a row to see every plan’s reasoning at once**.

| Metric ↓ / Plan →                               | Plan A |
|-------------------------------------------------|--------|
|                                                 |        |
| Objective metrics                               |        |
| ▶Takeoff length (AC to takeover-capable AI)     | 6 yrs  |
| ▶Training compute safety tax (OOMs)             | 2.8    |
| ▶Safety compute (H100e-yrs)                     | 100B   |
| ▶Safety-researcher-years                        | 1M     |
| Subjective metrics (1–5)                        |        |
| ▶Epistemic culture                              | 3      |
| ▶Public transparency                            | 4      |
| ▶Distribution of power                          | 5      |
| Outcomes (medians across implementations)       |        |
| ▶p(alignment); i.e., 1 - p(misaligned takeover) | 72%    |
| ▶p(great future \| alignment)                   | 58%    |
| ▶p(great future)                                | 42%    |

Plans are alphabetically ranked in terms of their objective metrics, with a big jump between Plan A and Plan B. However, plans C+ and C beat out Plan B on some subjective metrics. Plan B’s focus on security and its wartime vibe could degrade epistemics, and its likely implementation of nationalization or pseudo-nationalization would decrease public transparency and concentrate power.

# Comparing authors’ views on plan likelihood and outcomes

These estimates aggregate over uncertainties about the default capability trajectory and when the plans are implemented, as well as how competently the plans are executed. The numbers are in [this sheet](https://docs.google.com/spreadsheets/d/1FDyYPky6VeIs81ujssgQKyv-yIZc8iOZQrZv6KlJCNk/edit?gid=1821022003#gid=1821022003), and the plan classification is as described [below](comparing-possible-plans.md#classifying-trajectories-into-plans).

## Likelihood

### Probability each plan happens across authors

Reasoning (hover an author — here or on the chart — to spotlight their line and read their full reasoning).

<table>
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<th>Eli</th>
<td><p>p(govt does something at least as intense as Plan B): 35%; seems like govt wakeup has been increasing and also the importance of ASI will get more and more obvious. Though note that Plan B requires actually slowing down by at least 3 months.<br />
p(deal | at least as intense on Plan B): 50%; deal is clearly rational but there are various blockers in practice. Again note that something at least as intense as Plan B requires at least a 3 month slowdown.<br />
p(Plan A | deal): 30%; Plan S, a verified slowdown with less transparency, or just a somewhat weaker deal are all plausible.<br />
This gives Plan A is ~5%, other deals are ~10%.<br />
Let's say Plan B is 15% and other intense non-deal things are 5%, given that Plan B is quite broad.<br />
Domestic regulation as in Plan C+ seems plausible as well, though the requirement of actually having a 2 month slowdown lowers the probability. Also, it's a bit of a narrow target to have the will to do this but not Plan B or higher.<br />
Plan C seems more likely than C+. Plan D seems a bit more likely than Plan C.<br />
Other being at 25% feels maybe a bit low but not too bad as I think B, C, C+, and D together are broad enough to describe a bunch of the worlds that could happen at similar levels of intensity.</p></td>
</tr>
<tr>
<th>Ryan</th>
<td><p>I'm very uncertain about what should count. I think Plan C+ is mostly worlds with dumb regulation that slows down AI. I think Plan B would be higher if not for the intent to spend the lead on safety.</p></td>
</tr>
</tbody>
</table>

## Outcomes

We focus on p(alignment) here, i.e. 1 - p(misaligned takeover). We ignore p(great future \| alignment) in this section for simplicity.

### Probability of avoiding misaligned takeover by plan

Reasoning (hover an author — here or on the chart — to spotlight their line and read their full reasoning).

<table>
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<th>Eli</th>
<td><p>My probabilities in the plan assessment above were conditional on:<br />
(a) the default trajectory being the <a href="https://www.ai-2040.com/supplements/takeoff-supplement">default Plan A one</a>, which has a bit under a year between AC and TED-AI and a year between AC and ASI.<br />
(b) The plan implementation beginning in early 2029, ~0.75 years before AC.</p>
<p>My median takeoff is ~2x longer than the one described in (a), but I have significantly probability on faster takeoffs. This means that my p(alignment) estimates should do a combination of increase and regress a bit toward 50%. Also, Plan A isn't as sensitive to default takeoff length as other plans, and from a covert project perspective it's actually unclear in which way the effect size points because larger effective compute gaps between the start and end of takeoff require more software progress. The trajectory timeline to AC / start of takeoff is pretty similar to my median so for that I regress abit toward 50%.</p>
<p>For (b), my median is that the plan gets implemented later than this, but I think it doesn't matter much for all the plans besides A because in the other plans it's best to slow down later anyway. I do lower the value of Plan A due to this consideration, though not hugely because I think covert projects would likely still be difficult to do without detection.</p>
<p>Also, the plan assessment numbers were based on the median implementation of the plan, rather than aggregating the expected outcome over all implementations. My unconfident quick guess is that switching to expected outcome should also regress my numbers toward 50%, but not sure so this adjustmnet will be small.</p>
<p>With the above in mind, I make the following adjustments:<br />
A: 72-&gt;70<br />
B: 50-&gt;55<br />
C+: 45-&gt;50<br />
C: 40-&gt;45<br />
D: 25-&gt;32</p>
<p>For Other, I think a bunch of this is random pretty good plans that aren't covered, including Plan S. E.g. there's ~40% that this is a non-Plan-A deal. Though it also includes Plan E. Overall I rate it the same as B, 55.</p></td>
</tr>
<tr>
<th>Ryan</th>
<td><p>These numbers are very sensitive to how you classify plans. E.g., I think Plan A as described in the scenario has maybe 3/5 as much risk as Plan A as classifed by the supplement. An actually good version of Plan C done by the leading AI company is pretty close to the numbers I give for Plan B (but worse than a great Plan B). A large fraction of "other" is worlds with not enough effort on safety to classify for Plan D.</p></td>
</tr>
</tbody>
</table>

# Other plans

There are many other possible plans that the government could follow. Below we catalog some of the ones that we find to be most promising and/or likely.

## Plans that might be competitive with Plan A

|  |  |  |
|----|----|----|
| **Summary** | **Advantages (relative to A)** | **Disadvantages (relative to A)** |
| **Plan S:** **Indefinite halt.** A halt on all frontier AI capabilities progress, intended to last at least a few years. Different variants of Plan S have different conditions for resumption of AI progress; for example it could be alignment progress, lie detectors, human uploads, or intelligence enhancement.[^1] | A longer expected slowdown and more margin for error regarding scaling too fast. Potentially simpler. | Scaling to controllable AIs within the human range is helpful for accelerating alignment/control, epistemics, verification, and general understanding of AI. |
| **Domestic-first Plan A.** Regulate AI domestically enough to reduce AI takeover risk to acceptable levels, which will require a long slowdown. It’s possible other countries will also regulate domestically and something like Plan A won’t be needed; otherwise, transition to Plan A later. | Initial steps are achievable by the US and very helpful even if the international stage isn’t viable because it massively extends the timeline. Proactively builds trust with China. | Worse for covert projects and setting up verification than negotiating Plan A at the same time. May not be politically feasible due to race dynamics. |
| **GPU arms control.** International agreements for countries to limit their GPU stock or flow, analogous to historical arms reduction agreements.[^2] | Much simpler to enforce, and more historical precedent. Can achieve substantial slowdown. | Less slowdown, less ability to pay safety taxes, ongoing race dynamics mean no ability to coordinate towards safer paths through the tech tree. |
| **CERN for AI. An international project to develop frontier AI,** with all other projects regulated to be substantially behind in capabilities. | Easier to defend against algorithmic leakage and distillation to covert projects. Less actors at the frontier might make it easier to enforce. | Worse decisions (including worse decisions on technical safety) due to less transparency and less broad deployment.[^3] More concentration of power risk. |

## Plans that we think are clearly worse than Plan A

1.  **Repurpose the GPUs:** Like *GPU arms control*, except they are now required to be used for existentially useful applications rather than being destroyed. See [this comment](https://www.lesswrong.com/posts/HE3Styo9vpk7m8zi4/evhub-s-shortform?commentId=FqDBLsLPNEqF2ahBL) for a more specific proposal in which GPUs are required to be used for giving inference capacity to external safety organizations or to do publicly transparent safety research. In theory this plan should be better than *GPU arms reduction*, but it’s less reversible and harder to enforce.

2.  **Plan B-but-don’t-slowdown, aka D-war:** Like Plan B except that you don’t slow down, i.e. you don’t burn ~any of the lead that you increased by sabotaging China. (Currently classified as a variant of Plan D when making the above estimates.)

3.  **Weaker deals with China.** For example, the US could offer: "You get access to more chips for AI inference, and a non-binding or non-majority say in our safety requirements, if you give us full transparency into what you're up to.”

4.  **Plan E:** Like Plan D but even less safety investment, i.e. less than 1% of resources.

# Classifying trajectories into plans

Define the *implementation window* as the period between:

1.  **Start: 1 year before [Automated Coder](https://docs.google.com/document/d/1ru6Okbxb6XuH18Cz8439sdQJazMV39hNxsWDokh97r0/edit?tab=t.0#heading=h.h1t0i8bvad56)** **(AC) would be reached if scaling at maximum speed**.[^4] An AC is a collective of AIs that fully automates an AGI project’s coding work, autonomously replacing the project’s entire coding staff. That is, you’d rather fire all of the humans than stop using AIs.

2.  **End: Takeover-capable AI.** Takeover-capable AI is reached when it is practically very unlikely that humans could stop AI takeover, conditional on the AIs being adversarially misaligned. It could still be in theory possible for them to shut down the AIs by taking extremely drastic actions like shutting down the internet, but it’s unlikely that they would do so, e.g. because AIs might be heavily relied upon and/or highly persuasive.

If the plan being attempted is consistent throughout this window, then the trajectory is classified into that plan. Even if multiple plans are attempted, each trajectory can count as at most one plan; this is a non-obvious choice and it seems also reasonable to count trajectories as multiple plans.

If multiple plans are attempted during the implementation window, the trajectory is classified as the most intense plan that was attempted. This is a bit vague to use as a general classification, but for concreteness among Plans S/A/B/C+/C/D trajectories would be classified as the attempted plan that is earliest in that list. The reasoning behind this is that it seems intuitively like a trajectory should count primarily as Plan A or S even if the [deal dissolves](deal-decline.md) quickly, and also should count as Plan A or S if it starts as a less intense plan but then transitions to A/S within the implementation window.

The following selection effect is a consequence of this classification: In more intense plans, people are selected for being more competent. Furthermore, less intense plans are selected for people not later transitioning to a more intense plan even if concerning evidence arises.

One selection effect that I explicitly remove is the effect of background variables such as alignment difficulty on what plan a trajectory counts as. I.e., I assume when rating plans that the distribution of alignment difficulty is the same no matter what plan is attempted; in particular my overall guess as to the distribution of alignment difficulty. As mentioned above, I don’t do this for things that humans control such as their competence.

# Appendix

## Training compute safety tax definition

The training compute safety tax is the difference between the amount of compute actually used on a training run to reach a given capability level, and the minimum amount of compute required to reach that capability. Examples of ways to productively use that unnecessary compute might be to train in a more safe but less compute-efficient paradigm, or to spend lots of compute on AI-driven scalable oversight to improve incentives during the training process.

Measuring the safety tax by this method is an imperfect proxy for what we actually care about. There is likely large variance among improvements which provide the same amount of capability in how useful it is for safety to forego that improvement.

[^1]: Other potential differences from Plan A, though it depends on which variant of Plan S is implemented: slower compute buildout, less transparency.

[^2]: A special case of this is to **Pause the GPUs:** Require that a fixed fraction of the GPUs be either (i) turned off or (ii) used to mine cryptocurrency (or be used for some verifiable, non-AI R&D purpose). This proposal has the upside and downside of making it easier to unpause the GPUs.

[^3]: But maybe you can mitigate this via small public deployments and selective transparency.

[^4]: Potentially I should allow for plan implementation to begin earlier, especially if the plan is very intense. For example, probably Plan S should count if it begins 1.5 years before the default AC time.
