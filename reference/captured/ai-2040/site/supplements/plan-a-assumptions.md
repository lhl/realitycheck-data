---
title: "Plan A Assumptions"
byline: "Thomas Larsen"
source_url: "https://ai-2040.com/supplements/plan-a-assumptions"
retrieved_at: "2026-07-11T06:00:49+00:00"
conversion: "rendered HTML to GitHub-Flavored Markdown with Pandoc"
---

# Plan A Assumptions

**Byline:** Thomas Larsen

# Summary

Plan A is a scenario: it combines forecasts with policy recommendations. Some of the forecasts and recommendations we are confident in; others are just guesses we made because we had to, in order to achieve the desired level of concreteness.

|  |  |  |
|----|----|----|
|  | **Confident** | **Unconfident** |
| **Prediction** | E.g.: “AGI is coming soon and will be a bigger deal than the industrial revolution” | E.g.: “AGI will arrive in 2030” |
| **Recommendation** | E.g. “There should be an international deal to limit the speed of AI takeoff” | E.g. “Many new datacenters should be constructed in Mongolia and Canada.” |

This supplement goes through the major predictions and recommendations of the scenario and explains which are which. The supplement tries to capture all our main recommendations, so if something isn’t mentioned here, it is probably a prediction, and insofar as it’s a recommendation, it is not an important one.

Since this is a document about specific beliefs, it’s written from the perspective of one of the scenario authors (Thomas). Other authors by and large agree with the central claims but have somewhat different opinions on the specifics.

## Forecasts Summary

For each of the following, I am \>80% confident:

- **AI R&D will be fully automated within the next ~15 years**, absent substantial regulation, war, or societal collapse. (See the [AI Futures Model](https://www.aifuturesmodel.com/) for more detail; AIFP employees have somewhat different views, but all agree that 2027 and 2030 are plausible and reasonably central years.)

- **Within a few years of AI R&D automation we will build AIs that are better than humans at all economically relevant tasks** (absent substantial policy intervention). These AIs would quickly become vastly cheaper than humans, and so soon humans will become economically irrelevant.

- **If we build vastly superhuman AIs, the AIs could take over, if they collectively wanted to**. Therefore, it is critically important that most of them do not want to.

I’m not confident about:

- **The exact timeline.** In AI 2027, the automation of coding happened in 2027; in Plan A, this would have happened in 2030 in the absence of governance, but is slowed by a few years. My 90% confidence interval is mid-2027 to ~2050. We chose 2030 because it's near enough that our specific planning is useful, but far enough that the government has time for the preparation phase we recommend. If timelines are shorter, there isn't time to prepare and so Plan A becomes more rushed; if longer, more of the details are wrong but the high-level plan stays the same. ([more](plan-a-assumptions.md#timelines))

- **Takeoff speeds.** How long between automating coding and AIs that dominate the top human at everything? We assume a default of ~1 year (my median), but my 80% CI ranges from 2 months to 5 years. Under my views about takeoff, the plan is basically similar under different takeoff speeds, though there are some small prioritization updates depending on the direction. ([more](plan-a-assumptions.md#takeoff-speeds))

- **Alignment difficulty**. We don’t know how hard it will be to solve the AI alignment problem. I think it’s possible that even without a major slowdown, we are able to solve the alignment problem. Similarly, I think it’s possible that even 10+ years of dedicated effort, with lots of AI assistance, won’t be enough. Plan A is designed to buy time and attempt to gain evidence about how difficult the problem is. If evidence accumulates that AI takeover risk is small, then we can proceed faster, otherwise, the pause extends. ([more](plan-a-assumptions.md#alignment-difficulty))

- **How difficult it will be to verify compliance with a slowdown deal.** It could be that it’s basically intractable to do major AI development without access to giant datacenters which are easily monitored. On the other hand, it could be that algorithmic progress is doable even with a very small amount of compute, which means that very quickly even a very small cluster could do an intelligence explosion. In even the most pessimistic case, we think it’s very likely that a deal could be robustly enforced for a year or two. ([more](plan-a-assumptions.md#verification-difficulty))

- **Many other strategic variables.** ([more](plan-a-assumptions.md#less-central-updates))

For each of these key strategic variables, the Plan A scenario chooses a reasonably central value with respect to my views. For many of these my views are very uncertain, and many policy decisions should be made with more information about these variables than we currently have.

## Policies Summary

In the next section, I discuss which of our policy recommendations in the scenario are robust across a wide range of empirical updates.

These are robustly good policy recommendations:

- **Improve AI Preparedness in government** *(importance: medium).* Transparency, improving technical expertise within government, and measures to accelerate verification research. These policies are good because they are low-regret, and in some scenarios (like Plan A), they are very important.

- **Model spec transparency and verification against power grabs** *(importance: medium).* Model specifications (of both internal and external models) should explicitly prohibit assisting with power consolidation (by CEOs, presidents, or anyone else), and AI projects should be required to implement verification measures to prevent backdoors.

- **US/China deal to slow the capabilities explosion, based on compute governance** *(importance: high).* This is the core of Plan A. I’m confident that a cooperative international approach (Plan A) is better than the alternatives because the alternatives involve being in a race during the intelligence explosion, which incurs huge risks. I’m not confident about the exact variant of Plan A, or whether Plan A as we’re imagining it (a many year mutual slowdown) is better than Plan S (a full shutdown). Conditional on attempting to “slow down”[^1] AI progress, doing this via compute governance looks like by far the most effective way of accomplishing this goal (even though I’m not sure exactly how well it will work).

- **Redistribution of AI-generated wealth** *(importance: medium).* As AIs automate the entire economy, the wages that humans will be able to earn will plummet to near-zero. By default (and assuming we avoid AI takeover), AI will cause historically unprecedented wealth inequality. I feel confident that there needs to be some measures for wealth redistribution.

- **Defensive Acceleration** *(importance: medium).* Governments, AI companies, and the public should invest in technologies that make society more robust. Particularly important domains include AI for epistemics, bio defense, and cyber security. In the absence of a concerted effort to pursue defensive acceleration, increased offensive capabilities coming from high AI capabilities will lead to significant risk. Defensive acceleration also has positive externalities because it makes it harder for misaligned AIs to take over the world, and thus gives us more time to do alignment research

- **Thoughtful post-ASI governance** *(importance: high).* We feel good about some general principles for post ASI governance: (1) have lots of smart people use (aligned) AI assistance to think carefully about effective governance, (2) be careful making irreversible commitments, (3) make it hard for any individual actor to consolidate power.

These recommendations depend on particular assumptions that we’re not confident in, or have alternatives that might be better:

- **How fast to scale AI capabilities after a deal** *(importance: high).* Scaling faster incurs more immediate safety risk, while scaling slower means that you delay safety progress that’s downstream of having smarter AIs and incurs risk of deal dissolution and covert projects. These decisions will and should be made largely based on the evidence at the time about how risky particular AI systems and deployments seem to be, and how good our mitigations seem to be. ([more](plan-a-assumptions.md#how-fast-to-scale-ai-progress-after-a-slowdown-deal))

- **Massive datacenter buildout** *(importance: medium).* In our Plan A scenario, we recommend that governments encourage a massive datacenter buildout. This recommendation is contingent on having implemented an effective international deal to slow down AI, and even conditional on that, it’s not clearly good. The case in favor is that hardware scaleups are more governable than software scale ups because we can prevent the hardware from proliferating. But there are major costs: (i) it increases the required accuracy of verification within the legal projects, and (ii) if the deal breaks down (and failsafe mechanisms fail), it could result in the intelligence explosion afterwards being much faster. ([more](plan-a-assumptions.md#massive-datacenter-buildout))

- **Our verification plan** *(importance: high).* The verification plan described in Plan A is important for making sure that both the US and China are following the agreement. But I’m quite unconfident about the exact best way to implement it. We have a specific proposal which involves first implementing inference-only (and stopping the construction of new AI models) while sprinting to figure out how to verify training and experiments. Many alternative approaches to verification exist. ([more](plan-a-assumptions.md#our-specific-verification-plan))

- **What transparency/security tradeoffs to make** *(importance: high).* Security and transparency both have obvious upsides, but are in tension. We’d like as much transparency as possible to get as many eyes as possible on the safety cases being presented, but we’d also like to secure model weights, algorithms, and inference tokens. Overall, we think that we should be willing to pay substantial security costs in return for improved transparency, because we are more worried about major AI projects abusing their power and/or making mistakes, than we are about defecting projects with a tiny amount of compute (who are the main beneficiaries of poor security). The tiny projects just aren’t going to be as powerful, and bad or reckless behavior by them correspondingly doesn’t matter as much. ([more](plan-a-assumptions.md#transparency-and-security-tradeoffs))

- **Our post-ASI governance plan** *(importance: high).* [Our space governance plan](../main.md#playbook-epilogue) is, in my opinion, a reasonable first pass about what should be aimed for, and is generally applicable to any scenario where humanity retains control. However, I am not at all confident in the details, and in these scenarios, we will have aligned, superhuman AIs to help us puzzle this out, so my main recommendation is to use the huge amounts of AI labor to come up with a better plan. ([more](plan-a-assumptions.md#our-post-asi-governance-plan))

- **Broad deployment of AI** *(importance: medium).* Broad deployment spreads power and could improve societal epistemics. Some central ways it could be bad are (i) the net effect on societal epistemics might be bad, (ii) broad deployment could make a persuasion/political power takeover easier for the AIs (or for a human attempting an AI takeover) or (iii) they could lead to the proliferation of offense dominant capabilities. On net, I think broad deployment is probably good, but I feel uncertain, and it depends on how good mitigations are in place for each of the above failure modes. ([more](plan-a-assumptions.md#broad-deployment-of-ai-during-the-takeoff-period))

- **Various other details of Plan A implemented in our particular scenario.** This includes things like datacenters on the oceans, incentive shaping with respect to alignment, incentive shaping with respect to covert projects (e.g. hardened compute stockpiles), how to trade off deal dissolution risk, covert project takeover risk, and risk of incompetent governance.

The above were largely details about Plan A that might change. There are also structurally different plans that may be competitive with Plan A, which we discuss [here](../main.md#other-plans-that-are-competitive-with-plan-a).

Still, I think we should be aiming for something like Plan A across a wide range of scenarios. The rest of this document has two sections, which both discuss how our plan would change in response to empirical changes.

1.  **Empirical Updates** answers the question “if an empirical fact changed (e.g., suppose timelines were shorter or longer), how would our policy change”.

2.  **Policy Updates** answers the question: “for each of our major policy recommendations, what would make us change that recommendation”.

# Empirical Updates

In this section, I’ll go over how Plan A would change in response to some important empirical assumptions that we make in the scenario, which might turn out to be different in practice.

## Timelines

We don’t know when AGI will be built; it’s possible that it could be built this year or next year, it’s also possible that it will take decades.[^2]

In the Plan A scenario, the full automation of AI R&D was on track to happen in 2030 by default, but then was pushed back by government involvement. We’ve written much more on AI timelines; you can find our most updated work [here](https://www.aifuturesmodel.com/). AIFP employees continue to have (slightly) different views about AI timelines, but we all think that 2030 is a plausible and reasonably central year for AGI to arrive.

**Why did we choose to write this scenario assuming 2030 timelines?**

It’s good to showcase a variety of different plausible scenarios. We already wrote a very short timeline scenario (AI 2027), so we figured it would be good to choose a different timeline for our next one. 2030 is my (Thomas’) median currently, i.e. I think there is a 50% chance things will proceed slower, and 50% chance things will proceed faster. In the future, if time remains, we’d like to do scenarios for other authors like Eli.[^3]

**Overall, Plan A remains my central plan ~regardless of timeline**, because the underlying problems (AI takeover, AI enabled concentration of power, and rapid AGI induced societal upheaval) are the same regardless of timelines, and Plan A is our best guess for how to deal with these problems.

Regardless of the timeline, Plan A is most effective the earlier an international deal that involves mutual compute declarations and transparency begins. When we get to the beginning of the intelligence explosion (e.g. the automated coder milestone), verification becomes substantially more difficult, because defecting projects can involve many fewer humans, and therefore be much harder to detect.

If the timeline is much longer (e.g. 2035+), we begin to have much more uncertainty about the situation. The world will also be more transformed pre-AGI relative to our scenario, there will be larger economic effects of AI, AI company revenues (and share of the overall market) will (probably) be higher, there will be more robots around, and there will be more wakeup to the importance of AI. Particular effects include:

- We become somewhat less worried about covert projects because compute stockpiles are inherently insanely large, and so the relative amount of compute that covert projects have compared to the verified projects will be smaller. (The absolute amount of compute, on the other hand, is larger). However, there are also reasons to be more concerned about covert projects—a counteracting effect is that there will be more compute distributed throughout the world which will be harder for intelligence agencies to locate.

- It becomes more important to do the economic parts of the Plan A policy package (e.g. the Citizen’s Dividend) earlier, because more people are affected earlier.

- It becomes more important to do D/acc earlier because there is a longer period of time with reasonably intelligent AIs around, and current AIs already provide substantial biouplift.

- Since the overall amount of compute in the world is higher, we become more worried about a new paradigm being discovered that’s much more compute efficient, which could lead to a fast intelligence explosion.

If timelines are much shorter (e.g. 2026 or 2027), there isn’t time to do the preparation phase, and so we have to do a version of Plan A with no preparation.

- It’s more likely that we should pivot to one of the contingency plans that involves less government capacity. Unfortunately, these contingency plans have other downsides. For example, shutting down large fractions of AI relevant compute would also turn off inference of existing models, which would be economically costly.

- It’s more urgent that an agreement to slow down AI takeoff happens early, because we’ll soon be so deep into the intelligence explosion that it’s impossible to slow down.

## Takeoff speeds

In this scenario, similar to AI 2027, we chose to assume that the default length of time between AC (Automated coder) and TED-AI (Top-Expert-Dominating AI) was 1 year. This is roughly my median, but we again have large uncertainty; my 80% CI at time of writing for the takeoff duration is something like \[2 months; 5 years\].[^4]

**Why did we choose 1 year takeoff speeds by default?** This is my median at the time of writing Plan A, and seemed like a representative scenario to plan for.

**How does the plan change under different takeoff speeds?**

**If takeoff is faster than 1 year**, things become generally more difficult, and not just for Plan A. The main specific changes are:

- Doing an international deal to slow down takeoff becomes more important, because the status quo is more risky, because AI driven change without deal happens much faster and there is less time to react to each change and prepare for the next changes.

- Enforcement of an international deal becomes more difficult. Faster takeoff typically involves much less hardware increase, because if the takeoff occurs over months, there isn’t time for a massive compute scale up. The possibility of an intelligence explosion without a massive compute scaleup is the key assumption behind being worried about covert projects; if such an intelligence explosion wasn’t possible, then covert projects with relatively small amounts of compute would be much less concerning. Since the intelligence explosion happens faster, it also makes covert projects faster, reducing the amount of slack that the international Consortium has to work with.[^5]

- The slowdown agreement needs to be started earlier, which would make the enforcement easier (and therefore the whole plan more viable).

- Since enforcement of the deal is more difficult, this is an update towards making tradeoffs that help with enforcement but with various other costs, such as (i) leaning more towards security on the security/transparency tradeoff, (ii) making less algorithmic progress, and therefore scaling more slowly, even if scaling further would still be safe, and (iii) doing more early hardware scaling, which makes verification and self-destruct plans more load bearing, but helps reduce misalignment risk.[^6]

**If takeoff is slower than 1 year,** e.g. even without regulation it takes several years to go from the full automation of coding to the first artificial superintelligence, then we basically update in the opposite direction on all of the above tradeoffs.

- Overall risk becomes lower, because there is more time by default to deal with risks as they arise. Therefore, the overall plan will attempt to incur a smaller amount of risk, and will be willing to make more aggressive tradeoffs to reduce risk.

- Covert project takeover in particular becomes less likely, because it is extremely unlikely that they could bootstrap into existentially dangerous AI systems with only a tiny amount of compute. This updates us even further in favor of doing Total Research Transparency (because we are relatively more worried about the large projects than the small projects), and away from doing the large hardware scaleup. The plan can involve just doing a slowed down version of the intelligence explosion on the existing compute stockpile, leaking algorithms to the trailing project, but relying on the fact that they are so compute limited that they cannot make significant further AI progress.[^7]

- AI takeover is less likely, and so we can devote relatively more effort on mitigating other risks. It’s still very important to slow down AI progress, because there’s still a significant chance that AI alignment won’t be solved during the default takeoff, and because slowing down helps to mitigate other risks like concentration of power. However, it’s more likely that we wouldn’t actually slow down much in this world. Therefore, doing the slowdown part of the treaty is less load bearing.

Overall, we recommend pursuing Plan A regardless of takeoff speeds. However, changes to our takeoff speeds[^8] do substantially change the specific implementation of Plan A, in the ways noted above.

## Alignment difficulty

In the Plan A scenario, humanity rallies and creates a high assurance safety case for handing off to ASI. However, **we are much more confident in the general picture that more time and effort lead to a greater chance of solving the alignment problem than the specific story told here.** We don’t know how hard it’ll be to align ASI. Opinions vary substantially within our team (and even more outside of our team). Given the uncertainty, our view is that we should take a portfolio approach, and invest substantially in both prosaic AI safety agendas (e.g. variants of RLHF) and moonshots (e.g. uploading human brains).

The plan we are advocating for is one in which the world coordinates to give the scientific community breathing room and resources to figure out how difficult the alignment problem is. If Yudkowsky is right that AI alignment is difficult, our view is that evidence would increase during this time period and then the pause would be extended. Likewise, if the optimists are right and alignment is easy, we would get evidence of this during that period, and we could proceed at a faster pace (though it’s not clear that we should, given the other risks of doing so, most notably concentration of power).

I think that alignment is probably difficult enough that without a well managed multi-year slowdown, we will incur substantial AI takeover risk. Even with a ten year slowdown, as depicted in the scenario, there is a significant chance that alignment was too hard, or that it’s feasible but human error causes us to fail anyway. You can see more about the team’s views about alignment success likelihood conditional on following different plans [here](comparing-possible-plans.md#outcomes).

**What do we do if alignment is much harder?**

Gather as much evidence about alignment difficulty as possible by:

- Deploying and observing AI systems to get empirical feedback about how aligned they seem to be.[^9]

- Building model organisms—AIs trained to deliberately be misaligned—and see if alignment techniques are good enough to catch and train away the misalignment. Do this for deceptive alignment, sycophancy, reward hacking, etc.

- Giving a large, heterogenous set of people access to the models (ideally including model internals) to avoid groupthink.

- Have explicit safety cases that lay out the evidence and arguments for why the models can and should be trusted, and publish them so they can be critiqued and debated by the scientific community.

During Plan A, maintain the optionality of extending the pause by:

- Monitoring for covert projects and shutting them down if detected

- Ensuring that the flow of new chips is highly secure and not going to any rogue projects

- Improve coordination and verification technology, both with large investment and using AIs to improve this technology. In particular, using AIs to build privacy preserving auditing and reliable lie detection seems very promising.

- Minimizing software progress that leaks to covert projects. If alignment is harder, we should update towards making tradeoffs that enable us to stay slowed for longer.

- Making sure decisionmakers have access to the best information on alignment difficulty, including by making sure that people who are more pessimistic about alignment have access to the models and the current safety cases, so that they can find problems in them before it becomes catastrophic.

If alignment is extremely hard, e.g., humanity isn’t making substantial progress on alignment whatsoever, then the correct call may be to pivot to Plan S, and instead of attempting a managed takeoff, shut it all down. Then, we could pursue alternate strategies to build superhuman AI that are inherently safer than ML, such as uploads. Unfortunately, these approaches have substantial downsides as well, notably the risk that the moratorium breaks down and we go back to racing before enough progress is made on uploads or other strategies in that vein.

**What if alignment is much easier?**

Slowing down AI takeoff is still probably good for many other reasons, including avoiding AI-driven concentration of power, figuring out appropriate post-ASI governance, transitioning to a regime where human labor is no longer economically relevant in a healthy manner, hardening the world to AI enabled superweapons, etc—basically, we still need to solve all of the problems that we dealt with in Plan A other than misaligned AI takeover.

The main difference is that there is a higher chance of humanity being able to successfully muddle through these other risks without permanent lock in. This means that the necessity of a slowdown does go down substantially if alignment is much easier than I expect.

## Verification difficulty

*Related reading: [Covert Project Branch](../main.md#branchpoint-china-attempts-a-covert-agi-project), [Covert AI Projects Supplement](covert-ai-projects.md), [Verification Plan](verification-plan.md).*

I’m not sure how difficult verification will be. Our main strategy for verifying compliance with an AI agreement is (1) limit the amount of compute that covert projects have access to, and (2) ensure that legal projects are doing what they claim. Both of these will be somewhat lossy, and we’re unsure about what the mapping is between “amount of unmonitored compute” and “how fast could an illicit intelligence explosion reach an existentially dangerous capability threshold”.

Now we’ll go through each of these in a bit more detail:

- **Covert project verification difficulty.** In the Plan A scenario, we assume that the maximum plausible covert project size without detection is about 1% of pre-deal compute. Our assumption here in the scenario is close to the worst case scenario. My best guess is that neither side would build a covert project in a Plan A scenario because (i) there’s no incentive to because it’ll be out paced by the legal projects, and (ii) both sides are scared of AI takeover risk; and building a covert project would undermine the deal. Sub-questions I’m most uncertain about:

  - **What fraction of pre-deal compute can be tracked down?** Our uncertainty over pre-deal compute is very relevant, because it will determine the extent to which China’s initial compute declaration can be falsified. Existing experts we’ve talked to maintain huge amounts of uncertainty about how large China’s existing compute buildout is. As a percentage, this might become easier to track as AI datacenters get larger, but as an absolute number more and more compute will be harder to track down over time. However, the intelligence community may have access to private information that’s much more accurate today, and they might begin to gather this information in the near future. Overall, it’s possible that denying covert projects access to huge numbers of GPUs will be one of the most load bearing components in the non-proliferation plan; but it’s also possible that other factors such as HUMINT will be far more important.[^10]

  - **How effective will HUMINT be for detecting covert projects?** It seems likely to me that a covert project of the size we assume in the [covert project branch](../main.md#branchpoint-china-attempts-a-covert-agi-project) of Plan A (500k H100e, \$7.9B) would be quickly detected by intelligence gathering. Historical mega projects that were attempted in secret (e.g. the Manhattan Project) seem to have been riddled with spies; our baseline assumption should be that anything on the order of this size will be quickly detected and shut down. However, later into the intelligence explosion, the number of people involved in a covert project could be much smaller, as AIs could automate the AI research and robots could automate the construction and maintenance of the datacenter, dramatically reducing the probability of leaks.

  - **What is the necessary reduction in access to compute resources?** In the Plan A scenario, we assume that an AI project with 10x less compute can do an intelligence explosion 5.5x slower; this is discussed more in [the appendix of our Covert Projects Supplement](covert-ai-projects.md).

- **Legal project verification difficulty.** In the Plan A scenario, we assume that we can verify inference-only very quickly, and that we can verify training runs after a six month sprint to develop that technology. It could be easier (e.g. it’s possible to do at the software level), or it could be harder (particularly because governments are slow and ineffective at this). Our assumption here is on the optimistic end because we assume high competence in execution.

  - If legal project verification is more difficult, then increasing hardware buildout is more scary. Quantitatively, with no hardware buildout, then we’d need something like 99% assurance on legal project compute; with a +4 OOM increase in stock, we’d need 99.9999% assurance on legal project compute.

There are various other particular verification dynamics which could affect the rest of the policy strategy:

- **Favorability of SW scaling?** A key dynamic for covert projects is stealing algorithms from legal projects. Therefore, legal projects should consider pursuing algorithms that are less favorable for covert projects. In particular: (1) HW/SW co-design, i.e. research algorithms that are only effective on specifically designed chips that covert projects don’t have access to, and (2) heavily scale-dependent algorithms. We’re unsure how favorable both of these paths will be; the more favorable they are, the more capabilities progress can be done without speeding up covert projects.

- **How much edge-hardware is required?** Some applications strongly prefer edge hardware (hardware that operates on the device as opposed to the cloud): notably military applications (because of jamming) and self-driving cars (because you don’t want your car to crash if there’s a network issue). This poses a challenge for verification because edge compute could be removed from the device and funneled to a covert project, or potentially backdoored and used as part of a large distributed training run. We’re uncertain to what extent large quantities of this will be required, if there are other solutions, and how good the mitigations look for preventing usage of edge compute in training runs.

- **How difficult will security be?** Nation-state proof security[^11] is basically required to make the legal project verification work. Nation state proof algorithmic security is helpful for preventing covert projects. Our baseline assumption on security is that it’s possible to make verification mechanisms sufficiently secure, most algorithms will not be possible to secure (because they are so small), and that model weights will be possible to secure (because they are so large). I’ll now go through the updates if our current assumption is wrong for each of the desired security properties:

  - **If verification security isn’t viable** then our ideal strategy would either involve (1) doing a moratorium on further AI development (and potentially inference) until security is viable or (2) relying heavily on trust.

  - **If algorithm security is viable** then we’d have more buffer against covert projects than we are currently modeling in Plan A. We’d also have less of a need to do a compute buildout, because one of the core motivations for building compute was to mitigate algorithms leaking to covert projects.

  - **If model weights security isn’t viable** then we’d either need to (1) not scale AI capabilities until security becomes viable or (2) need to invest more heavily in defending against exfiltrated AIs. At very high levels of capability, this might involve extremely drastic measures, because we’ll need to defend against extremely capable AIs.[^12]

## AI Paradigm Shifts

Plan A currently assumes gradient descent on giant neural networks remains the dominant AI paradigm until the late 2030s. We assume significant advances are made within that paradigm, including (i) the addition of neuralese (both as long term memory, and replacing chain-of-thought) and (ii) dramatic scaling in reinforcement learning (many more diverse environments that are much larger than existing environments).

Substantial algorithmic changes, even within the broad “gradient descent on giant neural networks” paradigm, might change the implementation details of parts of Plan A. For example:

1.  We assume that online learning via live weight updates (instead of in context learning or delayed weight updates) is not necessary for generally top expert level AI systems of the type developed in Plan A. If live weight updates were necessary, then we would need to have some training infrastructure happening on the inference datacenters, which would complicate the inference verification because we’d need to live update the reference models in the verification infrastructure, which would increase the security risk surface area. It would also prevent us from using chips that are hardcoded to do inference on a given model (e.g. [Etched](https://www.etched.com/careers)), which could be part of the inference-only verification scheme.

2.  We assume that restricting access to compute is an effective measure to prevent covert projects. If there are, for example, new architectural discoveries with dramatically (e.g. 1000x) more favorable compute scaling than current architectures, this would make covert projects much more dangerous. That said, if such architectural discoveries are in the pipeline so to speak, all the other plans are much less likely to work too—a discovery which allows a covert project to overtake the legal projects in Plan A, despite a huge compute disadvantage, would in Plan D cause an extremely fast, discontinuous “FOOM” to ASI within whichever frontier AI project first found it. These worlds are extremely scary and probably the best way to handle them is something like Plan S.

There are also obviously many “unknown unknowns” in AI paradigm shifts which could change Plan A in unforeseen ways, in practice we expect that many updates to the Plan A baseline will need to be made in response to further paradigm shifts.

## Less central updates

- **State capacity.** Plan A relies on high state capacity on AI, in particular, the capacity to distinguish existentially unsafe training runs and deployments.[^13] However, in worlds where the state capacity is low enough that they are not able to distinguish safe and unsafe AI, we recommend pivoting to another plan. Two salient alternatives are: (1) having an extremely conservative bar for safety, (e.g. shut it all down), or (2) limit the speed of the intelligence explosion through more blunt techniques (e.g. mutual GPU destruction).

- **Capability level of the initial deal.** The later the deal begins, the more difficult enforcement becomes. In particular, once we get substantial automation of AI research, it becomes easier to run a covert project on AI with only a small number of people involved, which reduces the surface area for leaks. This means that the overall regime has less time, and so risk will be higher.

- **Distillation mitigation.** We discuss [our strategy for mitigating distillation in the verification supplement](https://docs.google.com/document/d/1K4vxl_IMf58OgNXbWntQl6BQ06yAWZ62WmW5Ypp4KYA/edit?tab=t.86wiss1dhlds#bookmark=id.9ax99eo6ehyb). It’s unclear how well this will work. If it doesn’t work well, it’s an update towards being more concerned with covert projects. It is also an update towards slower capability scaling being optimal. Finally, it’s also an update towards strongly limiting broad deployment, although I still think that even if mitigating distillation is very difficult, it would still be worthwhile to do broad deployment.

# Policy Updates

## How fast to scale AI progress after a slowdown deal?

It’s unclear, and will be dependent on observations at the time. Here are some key considerations:

1.  **Is the deal likely to break down soon?** If the deal is more likely to break down soon (for example, due to political reasons, or due to covert project takeover), then you should be willing to take on more risk, and so you should be more willing to scale faster.

2.  **How good do current safety cases look (and how misaligned do the models seem)?** The more AI takeover risk there is from marginal scaling, the slower we should scale capabilities.

3.  **How large are the returns to better AIs?** If better AIs won’t contribute useful labor (for example because we can’t trust their outputs, and control isn’t very scaleable), then we shouldn’t scale. On the other hand, if scaling AI capabilities would dramatically increase the amount of high-quality alignment research we can do, it may be worth scaling, even if doing so is risky.

4.  **Will the weights and algorithms leak to covert projects, and how bad are the leaks?** If the model weights and/or algorithms of a scaled up AI model were to leak this would accelerate defecting projects by some amount, decreasing the amount of slack the regime has. If it’s possible to secure the model weights and algorithms, or to scale capabilities without doing substantial algorithmic progress, then we should update towards scaling more. In the Plan A scenario, we mostly scale with hardware buildouts, to avoid the need to make substantial algorithmic progress, because we are not optimistic about securing the algorithmic secrets.

5.  **How much risk comes from current AIs vs future AIs?** The earlier in the intelligence explosion we are, the more we should be sympathetic to scaling earlier, because the marginal risk of current scaling is much lower, whereas if we’re in the capabilities regime where we are incurring most of the risk, we should be much more careful and tend to slow down more. (This is why, in the scenario, the Consortium scales up AI capabilities reasonably but not entirely cautiously in the early 2030s, and then pauses at top expert level in 2035.)

6.  **Is it possible to scale up capabilities without substantial algorithmic improvements?** In plan A, we try to scale up AI capabilities via hardware scaling, while heavily limiting algorithmic progress. However, it may be the case that scaling up AI capabilities inherently leads to lots of algorithmic progress (e.g. via distillation). Moreover, the main alternative to scaling up algorithms is scaling hardware. However, it may be the case that most algorithmic progress is downstream of hardware progress. In this case, the most effective way of governing algorithmic progress might be to limit hardware itself.

Ultimately, trading off these considerations will require quantitatively modeling each of these sources of risk: covert project risk, risk of AI takeover from current AIs and future AIs, etc, understanding how the speed of deployment impacts each of these risks, and then making complicated tradeoffs about the overall best path forward.

Plan A’s trajectory is essentially based on the viewpoint that deal dissolution risk will probably be high, that risks from early AGIs (e.g. ACs and SARs) can be mitigated via control (i.e. that control-based safety cases can be made good enough very quickly, for AIs at that level), and that we can elicit a huge amount of useful labor from these early AGIs. It also assumes that we can do most of our capabilities scaling via a rapid hardware buildout, and strongly limit the total amount of algorithmic progress that occurs, including successfully mitigating distillation (largely by hiding the intermediate reasoning traces). Under these assumptions, the best trajectory seems to involve scaling quite rapidly at the beginning of the slowdown agreement, and then slowing down dramatically at the maximum controllable capability level.

Plan A’s specific trajectory is our best guess for the best way to handle these tradeoffs. However, we aren’t confident whatsoever that this is the correct path, and we hope that decisionmakers at the time will have a better understanding of these empirical factors at the time, whereas we have to make rough guesses.

Another very plausible trajectory, Plan S, is essentially the opposite choice about how fast to scale: immediately issue a moratorium on further AI capability scaling. This policy looks better if there is a small risk of deal dissolution, and/or the returns to better AIs for safety research are low, and/or the risks of any capability scaling are high.

## Massive datacenter buildout

It is desirable to do a massive datacenter buildout in Plan A if (and only if!) the upside of scaling quickly, reducing covert project takeover risk, and having additional capacity to pay alignment taxes is bigger than the risk of verification failing or the additional risk incurred by the deal failing with a gigantic compute stockpile.

In a bit more detail, the main upsides of a massive datacenter buildout are that it allows AI developers to:

- **Scale quickly without leaking algorithms to covert projects.** In the previous section, we discussed the conditions under which it is good to increase AI capabilities, and the tradeoffs associated with going faster and slower. Simplistically, to increase AI capabilities, you can either improve algorithms or scale compute. By leaning heavily on compute, we can avoid making algorithmic progress in the first place, which is the best way to ensure that said progress doesn’t leak.

- **Pay alignment taxes.** Large compute-based alignment taxes might be very helpful for safety. For example, it might be that neuralese is much more performant than current architectures, but also has dramatically worse safety properties. If we have enough compute that we can just accept the performance penalty and continue with current architectures anyways, this might dramatically reduce risk. Without a massive compute buildup, we will by definition not be able to pursue architectures that are much less compute efficient.

The main downsides are:

- **Verification and regulation becomes more load bearing.** Since the verified projects have even more compute, it is more important that this compute is used safely, and, in particular, not used to do an intelligence explosion as fast as possible. So it becomes even more important that the regulations that AI projects are subject to are sufficiently conservative that they preclude an intelligence explosion, and that the verification is sufficiently robust that companies or rogue AIs can’t undermine it, and illegally gain control of a huge amount of compute within the verified clusters.

- **If the deal breaks down with a gigantic compute cluster, and the clusters are not destroyed, the intelligence explosion might be extremely rapid.** One naive estimate is that a 10x of compute leads to a 5.5x increase in the speed of the intelligence explosion, so a 10,000x increase in compute might increase the speed of the intelligence explosion by 900x. So if it would take a year by default, it might take less than a day with the Plan A hardware explosion. This is obviously extremely dangerous, hence why we put so much emphasis on mutually assured compute destruction.

Putting all of this together, my view on how to decide to what extent we should pursue a massive hardware buildout under Plan A is as follows:

1.  If covert projects aren’t a concern (because, for example, it’s impossible to do a reasonably fast intelligence explosion on a 100,000 GPU cluster), then **don’t scale hardware at all, or only go slowly.**[^14]

2.  If there are reliable mechanisms for destroying compute after the deal dissolution, and reliable verification mechanisms so that we can have high confidence that there will not be major rogue internal deployments (either by countries or AIs), and there is reliable verification for within-deal compute, then the downsides of a compute buildout are small. Therefore, it is beneficial to **scale hardware ~as aggressively as possible.**

3.  Otherwise, it is going to be a complicated tradeoff, which needs to be decided by weighing the magnitudes of the various costs and benefits listed above.

## Our specific verification plan

The verification plan used in the Plan A scenario can be summarized as follows:

1.  Mutually declare the locations of all large datacenters. Check the declared counts against intelligence estimates.

2.  Agree to pause training and experiments. Install inference-only verification devices on the declared clusters to verify this pause.

3.  Race to set up verifiable (e.g. radically transparent) training and experiment clusters; when complete, resume capability scaling within the constraints of safety and transparency.

We discuss this in more depth [here](https://docs.google.com/document/d/1K4vxl_IMf58OgNXbWntQl6BQ06yAWZ62WmW5Ypp4KYA/edit?tab=t.86wiss1dhlds#heading=h.g5eefrev1iir).

This version of the verification plan assumes that at the beginning of the deal (1) we can verify inference, and (2) AI development verification is feasible within a relatively short research sprint (but is not immediately feasible). It is most likely that one or both of these assumptions will be wrong; these assumptions are my central guess of what could be done under Plan A assumptions of political will and competence, but reality will most likely involve less good preparations.

What if we don’t have verification measures ready in time?

Three high level buckets of verification approaches are:

1.  **Technical verification methods**. These methods would allow ongoing AI usage or development, with both sides of a deal being confident that the other isn’t doing anything dangerous. An example of this is what we do in Plan A where we initially rely on inference-only, while sprinting to technical methods to verify training and experiments.

2.  **Rely on trust,** i.e. accept that either side could defect, and hope that neither side is foolish enough to try, or that they’d be caught by HUMINT and so forth if they did.

3.  **Blunt verification techniques** (e.g. compute destruction or mutual power down).

Three buckets of verification approaches - ai-2040.com

It is highly desirable that we have technical verification methods ready before the beginning of the intelligence explosion. If inference verification devices are ready, then access to AIs gets to continue at the beginning of the deal. If development verification is ready, then we don’t need to stop AI capabilities scaling or AI safety research that involves frontier models at the beginning of the deal, and can instead scale until it is sufficiently unsafe not to (following the considerations above).

2 and 3 will likely only be temporary regimes, and be paired with a sprint to get technical measures online. Therefore, we hope that eventually we’ll get to sufficiently good technical methods.

The main downside of 2 is that it runs a risk of defection. Therefore, it may also run into increased political difficulties, as both parties will be worried that the other will defect, and so will be less likely to sign in the first place. However, it’s not correct to entirely write off trust, because it may be that the risk of AI takeover becomes so high that neither side is incentivized to defect, because doing so would so likely result in existential catastrophe. If high AI takeover risk becomes common knowledge (for example, after we’ve caught early misaligned AIs in the act of sabotage), relying on trust may be the best option.

The main downside of 3 is that it involves a temporary period where large scale inference goes offline. However, this would be less bad than one might naively think; even an agreement to power off (or destroy) 90% of the compute, would only force a reversion to 10x cheaper models. Since cost of a given level of capability has historically decreased very rapidly ([averaging ~40x/yr](https://epoch.ai/data-insights/llm-inference-price-trends)), having 10x less compute would roughly correspond with having to use SOTA models from 7.5 months ago.[^15] A downside of 3 is obvious; if defection is viable, it becomes more likely that both sides would choose to defect in the first place.

Note that this is one upside of Plan S over Plan A; Plan A requires (1), while Plan S only requires (3).

## Transparency and Security tradeoffs

There is an inherent tradeoff between security and transparency—to secure something, you inherently need to prevent some group from being able to see it.

Security vs. transparency - ai-2040.com

Plan A biases towards transparency, in large part because I am more worried about the risk of poor governance within the legal projects than the risk of covert projects defecting and successfully undermining the deal. Increasing transparency will on average improve the quality of the governance decisions made by the Consortium, whereas increasing security makes it harder for covert projects to succeed. Furthermore, even if the governance decisions are perfect, the legal projects may not be able to solve alignment in time themselves, and may need help from the wider world to e.g. notice some subtle flawed assumption in a safety case. Also, transparency is very helpful for verification.

That being said, we are currently nowhere near the pareto frontier between these two dimensions. Plan A proposes dramatically increasing both security and transparency into frontier AI projects. We discuss transparency-related tradeoffs in much more detail in our [Transparency Supplement](transparency-plan.md#thomas-larsen).

## Our Post-ASI governance plan

*Related reading:* [Space governance supplement](space-governance-plan.md)*, [AI 2040 epilogue](../main.md#playbook-epilogue).*

We make a concrete guess as to what a positive post-ASI governance plan might look like. However, we expect that there exist better proposals, which we haven’t thought of yet, that will be discoverable at the time. Therefore, we want readers to orient to our plan as a baseline with which to compare other plans to on dimensions that they care about. Then, we hope that humanity will spend vastly more effort—both human and AI cognitive labor—on designing a system that performs better.

## Broad Deployment of AI during the takeoff period

The Plan A scenario involves broadly deploying AI into the economy during takeoff. This has massive effects on the world during takeoff: almost everyone loses their jobs and starts relying on Citizen's Dividend. Overall, I think that it is better for massive AI impacts to happen gradually, e.g., over the course of a 10 year takeoff, than to have all of the impacts happen really quickly, right at the end, once AIs are vastly smarter than humans.

US factor income shares (Plan A) - ai-2040.com

(See more about how AI impacts the broader economy in [our economics model](../economic-model/model-explanation.md), and discussion in our [economics supplement](economics-of-plan-a.md))

However, this relies on a few key questions:

1.  Is the net effect on societal epistemics positive or negative? I currently feel highly unsure. On one hand, broad deployment of human level AI will increase access to information, like the internet. On the other hand, while the internet is definitely helpful for some people, it’s unclear if the average effect on societal epistemics is good or bad. More research is needed on this; what plan we actually recommend at the time would depend a lot on our best guess about the epistemic effects of broad AI deployment. With our current state of knowledge, I currently don’t feel like this is a major consideration in either direction.

2.  Does broad deployment meaningfully increase the difficulty of AI control? I think probably not, because the main risks of AI takeover route through rogue internal deployments and recursive self improvement. The case for broad deployment increasing risks is that it may lead to AIs having affordances that might be helpful for takeover, especially (i) a large robot workforce and manufacturing base, (ii) control over robot armies, (iii) access to biology labs, and (iv) regular contact with a broad range of humans. I think that these risks are likely mitigatable through a combination of monitoring AI behaviour, limiting access to the most dangerous physical infrastructure (e.g. biolabs), preventing any one AI system from having control of a large fraction of the physical resources, and preventing collusion between different AI systems. However, I do think that it’s plausible that broad deployment makes control much harder. Hopefully this can be handled via limiting AI deployment in a particular domain of concern, but it may in practice limit deployment across many domains.

3.  How high are misuse risks from broadly deployed closed-source models? My inclination is that these risks are reasonably low, because (1) I’m optimistic about adversarial robustness in a regime like Plan A, where you are slowing down substantially in order to improve safety, and you have the capacity to run lots of monitoring, and (2) even if it’s possible to jailbreak widely deployed AI models, I think that the defensive measures put into place will be sufficient for preventing existential catastrophes from misuse risk. However, it is plausible that both of these assumptions fail (either because of intrinsically high difficulty or incompetent execution), in which case, we would be incurring serious misuse risk from broadly deployed models.

If we’re not broadly deploying AI through society, the main alternative is to be developing AI inside closed projects. This incurs additional risks. Whatever closed off group of people that are managing the intelligence explosion without contact with the rest of the world will have a huge amount of power over the future. For an extreme case, the closed project might literally be developing AI in secret, without notifying the rest of the world, as described in [Training AGI in Secret would be Unsafe and Unethical](https://www.lesswrong.com/posts/FGqfdJmB8MSH5LKGc/training-agi-in-secret-would-be-unsafe-and-unethical-1). A secret intelligence explosion would be bad for misalignment risk, because far fewer people would know and understand what’s going on, and be able to give input on the alignment techniques, and would be bad for the distribution of power, because powerseeking individuals might be able to seize control of the AGI project, and build ASI aligned with their values (as opposed to humanity more broadly)

A better proposal for avoiding broad deployment is to do local deployment, but maximize transparency: publish evaluation results, publish demos of AIs doing very impressive things, publish the AI-generated research (on non-AI domains), publish the model spec, etc. This is far better than a secret intelligence explosion. However, it seems likely that if this is happening, humanity will be still largely in the dark about what’s going on, because to normal people, without AI impacting their day to day life, it’ll seem like some far-away science project that people like to talk about—it’ll be in far mode, not near mode. Therefore, it seems likely that broad deployment of AI will improve epistemics around AI in particular, which seems positive.

## Appendix: How plausible and how desirable are our key policies?[^16]

Plan A is neither a pure recommendation nor a pure prediction. A pure recommendation in which every actor makes maximally responsible moves starting tomorrow would have been too implausible. And we already wrote a pure prediction scenario—that's AI 2027. So we chose to make Plan A a compromise between plausibility and desirability.

The interactive graph below shows roughly where each of the scenario's policies sits on these two dimensions. Plausibility is judged at the point in the scenario when the policy is adopted, conditional on everything that has happened up to then. It does not represent how likely the policy is to happen starting from today's world. For instance, "Pause at top human level" is rated highly plausible not because we think a pause is highly likely from where we stand in 2026, but because in a world where the deal has held for years and control-based safety cases are visibly reaching their limits, we expect decisionmakers to choose something like it. Desirability measures how much better we currently expect a policy to be than the most plausible alternative at that same point in the scenario. It is not a ranking of which policies we're most keen to see adopted today. A low score can mean that our recommendation is subject to lots of unpredictable empirical updates or that alternative policies look about as good to us as our recommendation.

Click on a policy to read more.

Click a point to read the policy’s explanation.Policy plausibility vs. desirability - ai-2040.com

[^1]: This is in scare quotes because, as our scenario illustrates, even if we do a well-enforced international deal to limit the pace of AI progress, the overall pace of AI progress will be extremely fast compared to what most people are expecting and used to. For more on why we think this, you can view our models of AI progress (the [AI Futures Model](https://www.aifuturesmodel.com)) and of AI economic impacts ([Economics of Plan A supplement](economics-of-plan-a.md)), as well as numerous blog posts and of course [AI 2027](https://ai-2027.com).

[^2]: AGI = Artificial General Intelligence, or, AIs that have a similar amount of general intelligence to humans. Our actual thinking uses more precise concepts which you can read about in the [AI Futures Model](https://ai-rates-calculator.vercel.app/). Concepts like AC, SAR, TED-AI. However, we find "AGI" to be a handy shorthand for some vague combo of the above milestones, because we expect those milestones to arrive within a few years of each other or less. So when we say 'AGI', understand that we are gesturing at milestones such as the above, and being deliberately nonspecific because the context doesn't require precision

[^3]: Eli’s timelines are similar to mine, but his takeoff would be about two times slower.

[^4]: Note: some people use takeoff speeds to refer to the period after TEDAI, it’s an ambiguous term, but for the purposes of this document, I’ll use the definition given here: the length of time between AC and TED AI.

[^5]: To illustrate, suppose that the length of time between AC and TEDAI is one month. Even if we can (optimistically) use compute governance to slow down rogue projects with ACs by 20x, you still only have 2 years until the rogue projects have TEDAI, which is a smaller window than Plan A assumes.

[^6]: This reasoning is given in the [datacenter buildout](plan-a-assumptions.md#massive-datacenter-buildout) section below.

[^7]: Note that covert projects doing an intelligence explosion is only one of the reasons to be worried about them, there’s also the risk of them directly obtaining a decisive strategic advantage; so it would still be risky if they were, e.g., able to train a top expert level AI.

[^8]: As well as various aspects of takeoff besides speed, notably the possibility of fast progress on a small, fixed, amount of hardware.

[^9]: There’s a good chance that empirical feedback will be highly ambiguous, but overall I’m optimistic that if there’s a long period with broad access to experiment on roughly human level AIs, then we will surface a huge amount of evidence related to the difficulty of alignment. Given the current (poor) epistemic environment, I don’t think this evidence will be sufficient for broad scientific consensus (until we have a good fundamental understanding of AI), but I personally expect to learn a lot and change my mind in substantive ways.

[^10]: Note that pre-deal compute matters a lot because it seems probable that post-deal compute will be effectively monitored, because (1) there are very few extremely expensive fabs which can build the relevant chips, all of which can be directly monitored with auditors, and (2) it is intractable to build illicit fabs.

[^11]: Specifically, security to China, because China is probably the best placed actor to run a covert project.

[^12]: For example, we might need to do things like move all humans into bunkers that are robust to nanotechnology (friendly nanotech is defending), mirror life (no air is allowed to enter), and superpersuasion (all information coming in is mediated by friendly AIs, who screen out superpersuasive content).

[^13]: Thanks to the transparency of AI development to other companies, many governments, and the public, there are some failsafes in place for governments making poor decisions about safety techniques.

[^14]: Probably covert projects are somewhat of a concern, but it’s very unclear, and depends centrally on when international coordination to slowdown starts—the later a deal happens, the higher the risk of defection because (1) we’re closer to superintelligence, and (2) the smaller the personnel footprint is because the AIs can do a larger fraction of the tasks involved in running a covert project.

[^15]: If algorithmic efficiency improves at ~40x per year, then the number of years of progress *t* lost by a 10x compute reduction is log_40(10) = .624 years = ~7.5 months.

[^16]: This appendix was written by Miles Kodama.
