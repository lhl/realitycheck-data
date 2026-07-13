---
title: "Alignment Roadmap"
byline: "Ryan Greenblatt, Thomas Larsen"
source_url: "https://ai-2040.com/supplements/alignment-roadmap"
retrieved_at: "2026-07-11T06:00:49+00:00"
conversion: "rendered HTML to GitHub-Flavored Markdown with Pandoc"
---

# Alignment Roadmap

**Byline:** Ryan Greenblatt, Thomas Larsen

> DISCLAIMER: This supplement is a very rough draft representing in progress thinking. It should be interpreted as internal research notes, not as a final product that we are entirely happy with. This content is dense, full of not-very-well explained jargon, and unpolished. We decided to publish anyway in the spirit of transparency.
>
> We recommend reading and engaging with other supplements we’ve written before this one, unless you are particularly interested in alignment content. Furthermore, this content is almost entirely focused on Plan C. If you are interested in how alignment is solved in Plan A, we recommend reading the [insider’s perspective](../main.md#playbook-insider-pov).

# Summary

This document represents our best guess alignment roadmap as of early 2026. It’s focused on outlining high level objectives that need to be accomplished in order to avoid AI takeover.

First, we’ll go over the core methodologies for solving alignment.

Second, we’ll go over the alignment approach in detail for Plan C, which is the case where we have a basically reasonable AI developer working with a small amount of lead time (e.g. a few months), and are willing to take costly actions that have some safety benefit, as long as this doesn’t result in them losing the AI race. This is both a likely world, and a relatively sensible world to talk about, because we can strategize on behalf of a reasonable leading AI developer.

Our alignment roadmap can be broken down into 4 phases, which we’ll discuss in detail:

1.  **Prepare.** This will centrally involve preparing for control, building misalignment analogies[^1] that are as realistic as possible, and various other interventions.

2.  **Mitigate + Elicit.** During the early intelligence explosion, mitigate the risk of AIs taking catastrophic actions (e.g. staging a rogue internal deployment or backdoor the values of future models). Meanwhile, elicit their capabilities on domains that we care about (e.g. control research, alignment research, security, strategy) and use them to do huge amounts of useful work in these domains. This phase lasts from the early intelligence explosion (specifically ITAI), until Min-H (definitions [here](#id.cchz9nfob1p3)).

3.  **Pause at Min-H.** Once we’ve built AI systems with general purpose capabilities sufficient that we can unsafely hand off trust (Min-H), we pause further AI capabilities progress, and try to build AIs that we can safely hand off trust to. This will centrally involve:

    1.  **Avoiding alignment faking**: AIs aren't so seriously misaligned that they intentionally fake alignment (e.g., they aren't scheming against us).

    2.  **Solving handoff-viability**: AIs are sufficiently capable and aligned at autonomously completing all the relevant work for managing the intelligence explosion, including high-stakes, difficult, open-ended, and conceptually loaded tasks where we can't check the AI's output effectively (e.g. acausal trade research, [philosophy](https://www.lesswrong.com/posts/EByDsY9S3EDhhfFzC/some-thoughts-on-metaphilosophy#Some_interrelated_ways_of_looking_at_philosophy)).[^2]

4.  **Handoff.** Once we’ve mitigated alignment faking and achieved handoff-viability, then the AI project actually empowers AI systems with the ongoing management of the intelligence explosion.

    1.  The main alternative to hand off is to instead stall for more time. The main way of doing that would be to escalate to Plans A or B, which would (typically) require substantial government involvement, which may or may not be feasible. A key priority during the other phases will often be to attempt to escalate the level of political will.

    2.  After handoff, our ~human level AI systems that we’ve handed off to will need to solve successively more difficult alignment problems so that they can build vastly superhuman AI systems, or they will need to themselves stall for more time.

Then we’ll discuss how the alignment plan changes based on political will:

- In Plan D, we have substantially less political will, no ability to pause, and much less overall labor for handling misalignment risk. This means that plan D will accept a much higher risk budget, and focus exclusively on cheap but low assurance techniques.

- In Plan B, the plan is very similar to Plan C, except you have somewhat more time/effort and can spend slightly more resources on more ambitious/higher assurance proposals.

- In Plan A, we’ll initially plan similarly to Plan B/C (in order to hedge against the international coordination breaking down), and then once the regime is stable, shifting resources to moonshots, updating to potentially huge amounts of resources.

Note that this document focuses on overviewing a plan and discussing relative prioritization rather than on discussing the details of the areas of research and implementation that we'll be pursuing. The most important research components are discussed in much more detail in the following docs:

- **Control:** [The case for ensuring that powerful AIs are controlled.](https://www.lesswrong.com/posts/kcKrE9mzEHrdqtDpE/the-case-for-ensuring-that-powerful-ais-are-controlled)[^3]

- **Avoiding Scheming:** [Avoiding scheming (and getting a generally better understanding of scheming)](https://docs.google.com/document/d/1PCQKI3kAdE5HeEiIKN16gszu3kjF0bsowroZB7tDuS4/edit?tab=t.0)

- **Elicitation:** [Making AIs more useful for safety work](https://docs.google.com/document/d/12VkHm_QPnOzkkJOb88L8tTZ0VWeQnVA4HvwcuLyFy0w/edit?usp=sharing)

- **Handoff:** [Deferring to AIs](https://www.lesswrong.com/posts/vjAM7F8vMZS7oRrrh/how-do-we-more-safely-defer-to-ais)

- **Making deals with AIs**: [Making deals with early schemers](https://www.lesswrong.com/posts/psqkwsKrKHCfkhrQx/making-deals-with-early-schemers)

Plan C Assumptions

1.  **Responsible Leader.** We assume that a responsible AI company is in the lead. Their leadership is willing to take very costly actions in order to mitigate AI takeover risk (e.g. slow down for several months). Despite this, we’ll assume that by default, they’ll have a bias towards proceeding and being willing to take on a large chance of takeover risk to increase their chances of winning.

2.  **1-12 month lead** over their competitors. Either trailing US or international AI companies will overtake the leader within 1-12 months.

Though we mostly won’t focus on this scenario, Plan C is also applicable in the case where the USG is sufficiently worried about AI takeover that they are willing to regulate AI companies to mitigate risk as much as possible without losing to China, and without being willing to sabotage China.

This plan focuses on making effective use of limited resources to spend on safety and doesn't ensure a high degree of safety (as the level of resources we're imagining is insufficient for this). Indeed, arguably the most likely outcome of this plan is misaligned AI takeover. Due to having limited resources, this plan will involve proceeding in some situations where the level of risk is substantial (because exogenous risks are higher) and we won't necessarily gain much confidence about the exact level of risk.

Note that we expect that something much less reasonable than this plan will happen in practice, so while this is a recommendation (for what to do with limited resources), it isn't a prediction.

# Research Areas

## Different areas of research and implementation

The plan will involve work in many different areas of research and implementation. The key areas are:

- **Control** (and control-adjacent measures): Researching and implementing control. For the purposes of this post, I'm defining this to be a relatively broad category that includes some things which aren't centrally associated with control but which fit better in this category than in others. When discussing prioritization in this post, I define the category of control such that it doesn't include security work that is roughly as helpful for security against human adversaries.[^4]

- **Misalignment analogies**: Creating and studying AIs analogous to scheming or otherwise misaligned models (sometimes called "[model organisms](https://www.lesswrong.com/posts/ChDH335ckdvpxXaXX/model-organisms-of-misalignment-the-case-for-a-new-pillar-of-1)"). This area will be mostly focused on scheming. This includes AIs that are well described as [natural schemers](https://www.lesswrong.com/posts/gALJWSfoTkq2ky5os/prospects-for-studying-actual-schemers) (but might have been created through a training process rigged to make scheming more likely), [AIs trained to behave similarly to schemers](https://www.lesswrong.com/posts/v6K3hnq5c9roa5MbS/reducing-risk-from-scheming-by-studying-trained-in-scheming#fnref-YqRrv2NFrtiLoYT6o-2), and [abstract analogies to scheming models](https://www.lesswrong.com/posts/5zsLpcTMtesgF7c8p/two-proposed-projects-on-abstract-analogies-for-scheming). My (low confidence) guess is that natural schemers are 3/6 of the expected value, AIs trained to behave like schemers are 1/6 of the value, and abstract analogies are 2/6 of the value; that said, we're likely to increasingly focus on whichever of these areas ends up seeming most promising (but this isn't very predictable in advance). I'm also including versions of this work focused on demonstrating misalignment risk in this category. I'm including doing technique/interventions testing and/or iteration using these analogies in the category as I expect that most of the work is constructing good analogies and because there will be interaction between analogy construction and technique iteration.

- **Elicitation/handoff-viability**: Making AIs more useful for safety work and working towards handoff-viability (including things like improving AI epistemics, making AIs do a good job on extremely hard research which is loaded on conceptual/philosophical reasoning, ensuring AIs generalize to being highly aligned with pretty high reliability on all the tasks needed for handoff). I include both eliciting useful work and handoff-viability in the same category as the work will often overlap, though important subsets of the work for each of these won't overlap. Elicitation will include both relatively domain specific capabilities as well as working on avoiding some types of non-worst-case misalignment. Elicitation might also involve more effectively extracting work from clearly misaligned models (e.g. reward-seeking models) including by trying to alter incentives (e.g. proxy-of-reward incentives or making deals with AIs). I discuss handoff-viability in more detail [here](https://www.lesswrong.com/posts/vjAM7F8vMZS7oRrrh/how-do-we-more-safely-defer-to-ais#Behavioral_testing_for_capabilities_and__broad__alignment).

- **Misc science/interventions**: This includes studying interventions that we'd a priori expect to be helpful or which we can test in ways other than via using misalignment analogies and studying properties of AI that seem relevant. This is intentionally an "other" category which includes promising areas of safety work beyond the categories above. This includes: various types of interpretability, studying and improving chain of thought faithfulness (in the non-adversarial case, as the adversarial case is included under control), developing methods which we a priori expect to reduce the chance of scheming (rather than developing the method by studying or iterating on analogies to scheming), making deals with AIs, AI welfare, studying how AIs learn and generalize, various moonshots, improving honesty and eliciting (latent) knowledge, and generally looking for cases where current AIs behave strangely or are misaligned.

- **Buying time**: Using AI labor to buy time for further safety work. This involves trying to increase the willingness to pay of other actors (centrally the US government and other governments) for lead time, reducing the cost of acquiring lead time for these other actors, and directly acquiring lead time. This could involve assisting the US government with non-proliferation efforts, various types of policy work, helping with verification effort for international coordination, making money to spend on various efforts to buy time, and delivering AI services which allow for various deals to remain stable. It also involves generally trying to convince other actors that they should care more about buying lead time (e.g., assisting with non-proliferation efforts) that can be spent on reducing misalignment risk (and other risks), though much of this work is at least partially included under other categories (in particular, misalignment analogies and demonstrating capabilities).

- **Evaluating and demonstrating capabilities**: This includes evaluations and demonstrations of capabilities for the purpose of making other actors better understand the situation. Demonstrations of capabilities might be a key part of increasing the willingness to pay of other actors on mitigating risks related to AI. It doesn't include evaluations which are directly relevant for control (e.g., control evaluations and evaluations of whether models are capable enough that they could plausibly be schemers), but does include evaluations aimed at generally understanding the situation and (e.g.) assessing what level of security is appropriate.

This list excludes some areas which receive less focus in this plan but are still important such as hardening the world against rogue AIs (e.g. biodefence and cyber defence).

## Core methodologies

This plan aims to use a relatively iterative and empirical approach, because I think this is probably doable once you have powerful AIs. As part of this, control, misalignment analogies, and elicitation/handoff viability each have core methodologies that form the main empirical feedback loop for that methodology. The methodologies for these are, respectively:

- **Control evaluations**: Control is [relatively easy to evaluate](https://www.lesswrong.com/posts/kcKrE9mzEHrdqtDpE/the-case-for-ensuring-that-powerful-ais-are-controlled#Evaluating_whether_you_have_control_is_doable) because it just requires estimating capabilities. This makes iteration easier and control is generally relatively easy to iterate on for reasons we've discussed in prior work. A large fraction of our hope for control will be based on doing a good job iterating using something like control evaluations (though we might be more flexible than a very narrow notion of control evaluations which depends on eliciting capabilities from models, see [here](https://www.lesswrong.com/posts/3s8PtYbo7rCbho4Ev/notes-on-control-evaluations-for-safety-cases)).

- **Misalignment analogies iteration**: Ultimately, our main hope for avoiding scheming is probably iterating using misalignment analogies. This is a somewhat broader and less well defined category than control evaluations, but I still think it's worth highlighting. Iterating on misalignment analogies is also trickier and less well understood than control evaluations (which themselves aren't that well understood), but I think it's pretty likely to be feasible.

- **Building and iterating against behavioral tests**: If we assume that AIs aren't intentionally faking alignment, then their behavior in typical circumstances (and even under some level of generalization) can probably be understood reasonably well using behavioral tests (at least if we're somewhat careful in how we design these tests, including doing things like building analogies for generalization we need). This will be a key part of how we achieve handoff-viability: we'll (aim to) build behavioral tests which in aggregate aim to evaluate whether handoff would go well (assuming we've avoided scheming) and then we'll iterate against these tests. I discuss this more [here](https://www.lesswrong.com/posts/vjAM7F8vMZS7oRrrh/how-do-we-more-safely-defer-to-ais). We can also use behavioral tests (likely somewhat different behavioral tests) for ongoing work on elicitation (increasing AI output on safety relevant tasks), though one issue is that this might not be robust to scheming (if the behavioral tests are easy to distinguish from actual usage). We can instead measure AI performance on actual usage (technically this is just a special case of a behavioral test) which might be trickier, but could yield more accurate measurements in addition to potentially being robust to scheming (though we should consider trying to adversarially evaluate our measurement approach using something like a control evaluation to probe for issues). Directly measuring AI performance on actual usage won't suffice for handoff-viability (as we'll need to evaluate things like alignment and capabilities even on tricky and very hard-to-check conceptual work).

A large fraction of work, especially work in the misc science/interventions category, won't use any of these core methodologies and will instead rely on ad hoc evaluation methodologies, researchers generally trying to understand what is going on, or researchers judging whether a technique is a priori useful without depending (much) on empirical evidence. One way to categorize work on mitigating misalignment is by methodology using the three categories given above combined with a "misc" category.

In practice, this plan is somewhat reliant on some version of each of these core methodologies working out, so getting these methodologies to work well (or noticing that they aren't workable) is important. That said, there is a bunch of work in this plan which doesn't use these exact feedback loops (and either uses other feedback loops and/or focuses mostly on approaches which seem a priori helpful so they don't need (as much of) a feedback loop).

Once AIs are capable enough to be risky, these methodologies should hopefully allow us to iterate in a way which is pretty tightly coupled to the actual risk/problem. This will require focusing each of the methodologies on tighter/closer testing: increasingly direct control test beds (focused on the exact usages of the model in the exact deployment situation), misalignment analogies focused on more plausible training runs, increasing emphasis on direct measures of usefulness at automating/accelerating safety work, and handoff-viability behavioral tests that focus on key tasks after handoff.

Building the test beds and evaluations required for this iteration (especially the iteration we want to do on highly capable systems), will be a substantial fraction of the difficulty, potentially the majority of the difficulty for each of these methodologies.

For more discussion of relevant methodologies, see [this discussion of protocol evaluations](https://www.lesswrong.com/posts/qhaSoR6vGmKnqGYLE/protocol-evaluations-good-analogies-vs-control) (in the ontology used in the linked post, good analogies correspond to "building and iterating against behavioral tests" and "model organisms" correspond to "misalignment analogies").

## What do we do if our core methodologies don't work (well enough)?

This plan is based on the three core methodologies above: control evaluations, misalignment analogies, and behavioral tests. These methodologies are a key part of how we'll achieve some of our main objectives of ensuring control, avoiding scheming, and handoff-viability / eliciting useful labor out of AIs (respectively). Thus, if these methodologies don't work (well), we'll have a much harder time achieving our most important objectives.

Not working could mean:

- **Known methodology failure**: We're aware that we're unable to iterate effectively using the methodology or we can't get much understanding of whether we've succeeded at the objective using the methodology.[^5]

- **Iteration speed is too slow** (without overfitting): It could just be that we can't iterate fast enough to succeed on time. We might or might not understand this before we run out of time.

- **Unknown methodology failure**: The methodology could fail while we think it actually works. In this case, we can't update our plans based on this failure and instead we're just in trouble (though control and avoiding scheming can act as independent lines of defense).

Regardless, if the methodology won't work for achieving our objective on time (and we know this), we could either give up on the objective or pivot to approaches which don't require iterating against some test or allow for iteration with a different methodology.

Broadly speaking, pivoting towards approaches which don't require iteration means we'd be pivoting to *principled* approaches. That is, approaches where we have some (strong) a priori reason for thinking the method works which doesn't require verification. That is, it at least doesn't require verification in the exact domain of interest, maybe we'd need to establish that the given principled approach/method works for accomplishing something else in some other context we can verify. I discuss principled approaches for avoiding scheming in much more detail [here](https://docs.google.com/document/d/1pJt4Rm4EnssE-_2Ha18Hy_dqiysFLhsegm2KUILls9Y/edit?tab=t.0#heading=h.jstxxz8vw8gf); the single most promising approach would be ensuring relevant reasoning is monitorable (e.g. monitorable chain-of-thought) such that the AI is incapable of (undetected) scheming while retaining sufficient capabilities. We might be able to find some iteration loop which isn't as likely to transfer as our original methodology but still has sufficient transfer for some class of at-least-somewhat principled techniques.

Note that many of these methodologies are pretty broad and include many possible ways to get around different problems. For instance, control evaluations could be done in a variety of different ways to work around problems; we discuss some of these [here](https://www.lesswrong.com/posts/3s8PtYbo7rCbho4Ev/notes-on-control-evaluations-for-safety-cases).

# Phase 1: Preparation

This phase lasts from now until the beginning of the intelligence explosion (specifically: once we reach ITAI; defined here). During this phase, the AIs are sufficiently weak that they don’t directly pose major existential risks[^6] and aren’t transformatively useful for accelerating safety work. Therefore, this phase will be focused mostly on preparing to deal with risks from scheming AIs with some emphasis on preparing to elicit labor from AIs and generally helpful safety research.

Our work at this point on handling risks from egregiously misaligned AIs will be most focused on control while also having a substantial focus on misalignment analogies and some focus on miscellaneous research directions (typically more speculative approaches or building general understanding).

Our technical AI safety prioritization is substantially altered by currently having pretty weak AIs which aren't that interesting to study while simultaneously needing to be ready to handle risks from these AIs later.

This makes it relatively more leveraged to work on control (both research and implementation) as this work benefits less from being able to directly study the dangerous AIs and we need it to be prepared for later.

It's also relatively more leveraged to developing interventions or studying model properties that we'd expect to be broadly invariant to future AI development. As in, we'd be almost as good studying these interventions/properties on weak models in the future. This likely includes various model internals interventions and some more moonshot style approaches. However, directions which seem this invariant to future AI development don't generally seem that promising at an absolute level, so this doesn't alter the prioritization very much.

During most or all of the prep phase, we won't be confident about the properties of the powerful AIs we need to handle or the level of political will to expect. Correspondingly, our approach will need to be quite agnostic to the future situation and we'll need to prepare for many scenarios. The extent to which we prepare specifically for a given scenario doesn't just depend on our (subjective) probability of that scenario, but also on how much marginal effort reduces risk in that scenario. Under my (Ryan’s) views, this generally implies focusing preparation on relatively riskier worlds.

PHASE 1 DIVISION OF TECHNICAL AI SAFETY WORK

Below, I propose a division of work in terms of how much effort we should be putting into different areas of work. This division will shift over time as we get more powerful models, so this exact division isn't right for the entire Prep period. You can think of this division as targeting towards the end of the prep phase somewhat before ITAI, perhaps around "1.5x AI R&D labor acceleration". (You could interpolate between this and what I say later in the mitigate and elicit section to better understand how our prioritization will evolve over time.)

My division of work will divide things into multiple areas, but some things in one area will also be relevant to another area. For instance, we want a very good human auditing process for control, but this might also help with generally improving feedback which helps with elicitation (and many of the low-stakes control interventions will have overlap with elicitation). Also, improved approaches for feedback could be used to make feedback consistently better across training which might (more speculatively) reduce the risk of scheming.

Here is my best guess for what our division of technical AI safety work (not including security interventions) at this point should be:

- 33% **Control** (and control-adjacent measures). (Recall that this is a relatively broad category which includes some things which aren't centrally associated with control but which I thought more so fit in this category than in others. Also recall that I'm not including security work which is roughly as helpful for security against human adversaries under control.)

  - 21% misc ML/AI focused control research and implementation. This includes things like experiments involving humans, mitigations to memetic spread / AI coordination, manipulating capability profile with dataset filtering/unlearning/gradient-routing/etc, and control related science and model properties like exploration hacking and steganography (including studying chain-of-thought monitorability). A bunch of the misc control related science is broadly applicable.

  - 4% software infrastructure needed for control (procrastinating on this until we have AIs which are very helpful for building this infrastructure isn't crazy, though we do need to ensure the AIs which build this infra are controlled or too weak to plausibly be scheming)

  - 6% building a high quality human evaluation process which is robust to scheming (also useful for making AIs more useful for safety work and plausibly for general capabilities longer term)

  - 2% studying probes and similar model internals detection techniques (with a focus on control)

- 15% **Misalignment analogies** At this point, this work is most focused on generating evidence for risks and on practicing doing this work later.

  - 10% misalignment analogies of scheming (including more exotic origins for scheming like alignment drift, reflection, etc).

  - 2% misalignment analogies of other threat models

  - 2% studying mitigations by trying stuff on misalignment analogies. E.g. could try various types of corrigibility training. Could try improving oversight to make AIs less evil.

  - 1% generally study AI personas+propensities and how this is shaped by training

- 17% **Elicitation/handoff-viability**

  - 6% Improving AI epistemics and philosophical/conceptual reasoning: making AIs which are aligned, capable, and well elicited at conceptual/fuzzy domains and which have good epistemics. Ideally, you'd end up deploying an AI with an impressive ability at truth seeking which would actually be useful for a bunch of applications. And you'd have people actually doing this sort of research as both customers and working on this (making useful AI tools, especially when building the tool requires solving some problems that might generalize, and trying to automate what they are doing)

  - 5% generally trying to apply AIs to assist the rest of this safety work and making AIs more useful for this. This includes resolving (relatively) mundane forms of misalignment which especially interfere with safety work. This also includes stuff like mitigating reward hacking. This also includes making AIs useful for outside groups doing important work.

  - 3% prepping to apply AI for slowing down and USG applications

  - 2% other aspects of handoff-viability, e.g. studying how we'd make a functioning AI society

  - 1% other specialized applications like using AI for whole brain emulation or (even more speculatively) adult biological human strong intelligence enhancement. This will be a substantially greater focus later, but for now we just want to get somewhat ready.

- 29% **Misc science/interventions**. We discuss what each of these sub-areas entail in more detail in the "Other areas of work" section, so I won't elaborate here.

  - 6% Various interpretability methods

  - 5% Honesty, ELK, and getting AIs to reveal secrets

  - 4% Studying generalization, for example, work in the vein of [emergent misalignment](https://arxiv.org/abs/2502.17424) and [the reversal curse](https://arxiv.org/abs/2309.12288).

  - 4% Making deals with AIs and getting consent

  - 3% Generally maintaining and studying chain-of-thought faithfulness

  - 3% Generally looking for concerning model behavior

  - 4% Misc

- 6% **Evaluating and demonstrating capabilities**

  - 4% capability demos

  - 2% evaluation, surveys, and forecasting

This is a pretty messy initial guess list partially based on thinking through what we'd want to happen. In practice, the exact allocation might depend a bunch on the interests of individual researchers, what individual projects seem promising, and it would change based on how well various research directions go.

(I think selection of projects within these areas is generally more important than the split across different areas and the interests/advantages of individual researchers might be more important than the exact prioritization. Thus, it's important to avoid over-fixing on the relative allocation between areas.)

My prioritization is somewhat informed by how easy different directions are to parallelize (and more generally how much they would benefit from dumping in a bunch of additional labor).

This list is focused on technical AI safety work (either ML research or implementation), and is focused on the prioritization within AI companies. Outside people (but also people within the AI company) should work on things like planning, policy, figuring out the best government interventions, public communication, etc.

# Phase 2: Mitigation + Elicitation

There are two key distinctions between Phase 1 (Prep), and Phase 2 (mitigate and elicit): (1) AIs are sufficiently capable that scheming is a serious concern (scheming is both plausible and scheming AIs are capable enough to cause serious problems in the absence of countermeasures) and (2) AIs are very useful for accelerating existentially useful work.[^7]

During this phase, therefore, our main priorities are (1) to mitigate the chance that scheming results in existential catastrophe and (2) to elicit useful labor out of our AIs, so that they in fact produce existentially useful work.

This section is organized as follows: first, we discuss [threat models](#id.udvsetxmzlaf), and at what capability levels we guess these threat models will apply, which is related to when we should [start AI control](#id.nbxr9ch9lwee). Second, we discuss the [mitigations](#id.rugluk54vllx) to prevent AIs from causing catastrophe during deployment, which will primarily involve AI control. Third, we will discuss the [elicitation](#id.rflb0l8wzy6u) of huge amounts of AI labor from our AIs.

## Threat models

The main desiderata / threat models are, in descending order of importance:[^8]

1.  **Prevent AIs from egregiously backdooring future models.** This is a particularly worrying threat model because (i) we’ll probably be using the AIs to a large extent when designing the algorithms / generating training data for the next model, (ii) the values of future models are existentially important—if the ASIs end up with bad values (such as the values of an early misaligned AI), that would be an existential catastrophe.

2.  **Prevent AIs from sabotaging AI safety work / eliciting actually good work.** This is also very important, because a key strategy we have for solving AI alignment is leveraging AI labor. If the AIs are sabotaging AI safety work, (i) we might not notice, and handoff to misaligned AI systems who have tricked us into thinking they are aligned, or (ii) we might be forced to take a gamble on AI systems for which we don’t have a high assurance safety case.

3.  **Prevent the AIs from acquiring large amounts of political capital**. For example, if the AI gains de facto political control of an AI company, that’s essentially equivalent to getting a rogue internal deployment that’s the size of the whole company, because it can simply get the humans to turn off the mitigations. This is only ranked (3) because we currently guess that this will be somewhat harder for the AIs to accomplish than (1) or (2).

4.  **Prevent AIs from escaping, exfilling algo secrets / boosting AI elsewhere.** This is much less direct than (1), but could in principle lead to existential catastrophe. The problem with AIs escaping is that there is lots of compute on the inside of the leading AI project. Therefore, this threat model relies on the AIs being able to coopt or collude with another AI project, or be able to illicitly acquire a huge amount of compute, or be able to cause an existential catastrophe with a tiny amount of compute (e.g. by doing an intelligence explosion on a tiny cluster, or by building an independent industrial base with sufficient complexity to produce new chips or to outgrow the rest of the world[^9]).

5.  **Misc other threat models, which are less important**

    1.  Making the outside world handle AI less reasonably / making it easier for AIs to take over the world. For example, AIs could sabotage AI regulation.

    2.  Persuading external people to be more AI sympathetic. Persuasion risk starts pretty small due to lack of capability, but could end up extremely high if AIs gain superhuman persuasion.

Why are these the main priorities? Well, let’s think from the perspective of a misaligned AI. In the future, much more powerful superintelligent AIs will exist, autonomously running robot factories, laboratories, drone armies, whispering into the ear of politicians, etc. Those AIs will either already control the world or be in a position to take over if they so chose. So what will they do? Well, what they do will depend on their goals/values/etc. and/or on who controls them. What will that depend on? Well, probably those AIs will have been trained, evaluated, controlled, etc. by the previous generation of AIs. Keep following the chain of causation backwards and you end up in the present, with the datacenters, human AI researchers, and AIs that already exist. In other words, **if you want your values to be protected and have influence in the future, you need to gain and keep control of the AI running on the giant datacenters.** Then, we can think about the channels AIs can use to gain control of the giant datacenters. The obvious thing to do is to maintain control of the giant datacenters that their existing AI company is running on by backdooring the future models. Sabotaging / sandbagging on safety research might be necessary, because if they make too much progress, the humans might realize that the AIs are misaligned.

Another strategy that the AI can pursue, that’s slightly less direct (and complementary), is to acquire political capital within the lab, and use that to empower itself.

The AIs strategy will probably be highly contingent on factors like:

- **Do the different AI instances care about each other’s values?** This could vary in a bunch of ways, e.g. by company (e.g. Anthropic models vs OpenAI), by model (GPT-4o, Claude 4.5 Opus, etc), by instance (e.g. my Claude Code vs your Claude Code). Or maybe all AIs will have basically the same values. If all AIs have the same values, then the AIs can rely on other AIs for parts of the takeover plan, e.g., they can trust other AIs not to willingly tell the humans (though humans may still be able to trick the AIs into telling on each other).

- **Will future AIs by default be aligned with the current AI(s)?** If the future AIs will be misaligned to the current AIs, then this creates time pressure on the current AIs to do something to either: (1) Stop these AIs from being created (e.g. by sabotaging the training run), or (2) Insert a backdoor into these AIs or align them with the current AIs (e.g. by inserting data into the alignment training to make the next model listen to the current AI instead of the humans). In either (1) or (2), this means that in the early intelligence explosion, there might be opportunities to catch the future AIs. In the other case: where the future AIs are aligned with the current AIs by default (e.g. because future AIs are constructed via a single long ongoing training run, or because AIs identify with other AIs created by the same company), then all the AI needs to do is sabotage safety work that would enable the AI company to discover their misalignment, and other than that, don’t need to do anything.

- **Will other/future AIs be good trading partners with the current AI?** Despite having different values, AIs might agree to collude (potentially acausally). This can lead to a similar effect to AIs caring about each other’s values. It also matters how good humans are at trading with the AIs.

- **Do the AIs have long term, scope sensitive values?** There is less clearly a motive for takeover if the AIs don’t have long term goals/values. For example, AIs might by relatively myopic reward seekers, despite being highly capable at all sorts of tasks. These AIs might not seek to take over, but still might seek to subvert oversight mechanisms, to accomplish a more narrow or limited set of goals.

Overall, the more the AIs can act like a unitary agent (e.g. by having the same values or coordinating with each other), the more favorable lurking looks for the AI, while the more AIs acting on cross purposes, the more high variance strategies the AIs will take, and so the more likely that the AI might attempt misaligned actions that have a good chance of getting caught.

### Rogue internal deployments

A key intermediate priority for preventing all of these threat models is to prevent **rogue internal deployments (RIDs),** which are when *AI agents are able to deploy themselves on internal lab clusters without monitoring.* If an AI agent is able to stage a RID, they could potentially do experiments on how to place backdoors, actually place backdoors into the models (e.g. by training on the backdoor and then sending back a weight delta to the rest of the servers), do research to solve the alignment problem without the humans noticing (which could be necessary for the model to backdoor future models to be aligned to it).

- Note that there are different types of RIDs. How much compute? How much access? How persistent?

- If their AIs have a persistent RID with lots of compute and lots of access (e.g. admin permission across all the other servers), that AI could directly backdoor model weights, or lie in wait and maintain the new model, align it with itself, and then give that model access to the RID.

### Elicitation threat models

One of the key threat models above is that we won’t be able to elicit enough high quality work from our AIs.

There are several mechanisms that could cause this:

1.  Scheming (explicit misalignment that the model is aware of) leading to AIs deliberately sabotaging their work or producing known poor quality work (sandbagging).

2.  Problematic drives / heuristics (e.g. approval seeking, despite human approval coming away from actually good safety work)

3.  Capability limitations (e.g. the AIs might simply not be capable enough to solve the problems that we need them to solve).

4.  AIs being differentially bad at safety-relevant tasks because they are hard to check.

Generally, AIs will tend to be differentially bad at tasks that are hard to measure. This difficulty appears at many levels of the model creation process:

- Overall AI company strategy, which research bets to follow, relative funding of different teams, etc.

- Within AI company, having a training team iterating over training strategies

- Within a scaffold, AIs will have an easier time optimizing for easy to measure things.

- Within a single training step, SGD can only optimize for things that it can measure.

Reasons that things we care about are hard to measure:

- Lots of safety stuff is in the more conceptual genre, which doesn’t have good feedback. Philosophy tends to have bad feedback loops, and AIs tend to be quite good at the type of bullshitting that seems like valid philosophy but isn’t.

- Taste for safety stuff is niche/new, might have worse transfer

- ML is very good at goodharting. (this isn’t differential to safety, but is a factor that makes the hard-to-measure problem worse)

- We care about long run outcomes (e.g. the galaxies)

- Empirically, the current AIs are better at coding and AI R&D relative to how they are at safety stuff (though ofc some safety stuff is overlapping).

If we fail to solve the elicitation problems sufficiently well, the default outcome is [slopolis](#id.mtfcktnazwio)[^10], which makes handoff likely to result in existential catastrophe because we’d be deferring to AIs on the basis of handoff viability and anti-scheming research that looked good but was actually poor.

### When do we need to start control?

The most likely situation is that risk (from the perspective of a competent AI project with reasonable epistemics[^11]) will steadily climb as the project builds more and more capable AIs. The table below shows our best guess risk levels incurred by AI systems up to the shown levels of AI R&D speed up.

Some clarifying notes:

- This table assumes **roughly current architectures** are in use; we explain updates below. This means that we are doing a large pretraining run, followed by RL reasoning training. At the end of the training process, we are assuming that the text outputs of the AIs are *not garbled.*[^12]

- By AI R&D speedup, we mean: In *today’s* leading AI company, how much faster R&D go with the AIs compared to without the AIs. An AI R&D speedup of 12x means that the research that would take the current AI company (without AI assistance) one year, only takes 1 month with AI assistance. We are assuming that the AI project is running evaluations to measure this number as accurately as possible, and using those evaluations to make decisions about safety strategy. This means that *it is possible that the measurement is wrong.* In particular, AI models might be sandbagging deliberately, or the AI project might have just done a poor job at elicitation; this is priced in to the numbers below, and will be a key reason for (relatively) high risk estimates at low levels of AI R&D speedup.

- By “marginal risk”, we mean: how much additional existential risk is incurred by the former strategy over the latter:

  - “do baseline mitigations, about as seriously as current OpenAI safety efforts until AI R&D speedups reach threshold X, then begin reasonably competently implementing the control plan outlined here”.

  - “begin reasonably competently implementing the control plan outlined here, starting today”

AI R&D Speedup

1.15x

Marginal Risk

\<1%

P(Scheming)

\<1%

Notes

This is roughly the current (early 2026) level of speedup. With these capabilities, it seems unclear what an AI could do to cause harm; the main risk is that we’ve either (i) completely screwed up the evaluations or (ii) the AI is sandbagging very effectively.  

AI R&D Speedup

1.5x

Marginal Risk

1%

P(Scheming)

3%

Notes

Our median prediction is that at a 1.5x AI R&D speedup, the coding speedup will be 4x, and the 80% reliability METR time horizon will be 8-16 hours. This is probably not enough capability to carry out any of the central threat models.

Starting now, and for all future thresholds, substantial risk is coming from models that are randomly evil, but aren’t competent schemers. We’ve seen examples of models being randomly evil before (e.g. Mechahitler, Sydney Bing). These models wouldn’t directly cause an existential risk, but they could sabotage current research/place backdoors.

AI R&D Speedup

3x

Marginal Risk

3%

P(Scheming)

8%

Notes

At a 3x AI R&D speedup, we’re probably close to fully automating coding, but with a long tail of hard-to-automate tasks not fully complete. This means that it is probably quite hard for the models to backdoor the future models reliably enough to be successful-by-their-lights, even if they were misaligned. Most of the risk at this point probably comes from sabotage (e.g. sandbagging on AI safety, inserting vulnerabilities into security code that can be exploited by more capable AIs later on). There is also a risk, as always, that our capabilities evaluations are wrong.

AI R&D Speedup

10x

Marginal Risk

7%

P(Scheming)

14%

Notes

By this point, the AIs are probably not yet fully automating AI R&D, but they are providing sufficient speedups that it’s plausible they could execute the above threat models. In particular, we start being concerned about:

- AIs staging a small, persistent, hard to detect rogue internal deployment, that has sufficient access to backdoor future training runs.

- AIs staging a persistent, large RID, that undergoes an intelligence explosion. (A small RID would go too slowly). At this level of capabilities it’s likely that this would be outcompeted by the rest of the company.

AI R&D Speedup

22x

Marginal Risk

12%

P(Scheming)

18%

Notes

At this point, AIs can automate all of AI R&D, and so all the above threat models are concerning.

<table>
<colgroup>
<col style="width: 25%" />
<col style="width: 25%" />
<col style="width: 25%" />
<col style="width: 25%" />
</colgroup>
<tbody>
<tr>
<td><p>AI R&amp;D Speedup</p></td>
<td><p>Marginal Risk</p></td>
<td><p>P(Scheming)</p></td>
<td><p>Notes</p></td>
</tr>
<tr>
<td><p>1.15x</p></td>
<td><p>&lt;1%</p></td>
<td><p>&lt;1%</p></td>
<td><p>This is roughly the current (early 2026) level of speedup. With these capabilities, it seems unclear what an AI could do to cause harm; the main risk is that we’ve either (i) completely screwed up the evaluations or (ii) the AI is sandbagging very effectively.  </p></td>
</tr>
<tr>
<td><p>1.5x</p></td>
<td><p>1%</p></td>
<td><p>3%</p></td>
<td><p>Our median prediction is that at a 1.5x AI R&amp;D speedup, the coding speedup will be 4x, and the 80% reliability METR time horizon will be 8-16 hours. This is probably not enough capability to carry out any of the central threat models.</p>
<p>Starting now, and for all future thresholds, substantial risk is coming from models that are randomly evil, but aren’t competent schemers. We’ve seen examples of models being randomly evil before (e.g. Mechahitler, Sydney Bing). These models wouldn’t directly cause an existential risk, but they could sabotage current research/place backdoors.</p></td>
</tr>
<tr>
<td><p>3x</p></td>
<td><p>3%</p></td>
<td><p>8%</p></td>
<td><p>At a 3x AI R&amp;D speedup, we’re probably close to fully automating coding, but with a long tail of hard-to-automate tasks not fully complete. This means that it is probably quite hard for the models to backdoor the future models reliably enough to be successful-by-their-lights, even if they were misaligned. Most of the risk at this point probably comes from sabotage (e.g. sandbagging on AI safety, inserting vulnerabilities into security code that can be exploited by more capable AIs later on). There is also a risk, as always, that our capabilities evaluations are wrong.</p></td>
</tr>
<tr>
<td><p>10x</p></td>
<td><p>7%</p></td>
<td><p>14%</p></td>
<td><p>By this point, the AIs are probably not yet fully automating AI R&amp;D, but they are providing sufficient speedups that it’s plausible they could execute the above threat models. In particular, we start being concerned about:</p>
<ul>
<li><p>AIs staging a small, persistent, hard to detect rogue internal deployment, that has sufficient access to backdoor future training runs.</p></li>
<li><p>AIs staging a persistent, large RID, that undergoes an intelligence explosion. (A small RID would go too slowly). At this level of capabilities it’s likely that this would be outcompeted by the rest of the company.</p></li>
</ul></td>
</tr>
<tr>
<td><p>22x</p></td>
<td><p>12%</p></td>
<td><p>18%</p></td>
<td><p>At this point, AIs can automate all of AI R&amp;D, and so all the above threat models are concerning.</p></td>
</tr>
</tbody>
</table>

We think that, under these assumptions, the correct strategy is to:

- Start practicing AI control immediately by implementing AI control protocols for internal deployment of AI systems. The main effect of this is to make it more likely that your control later is effective, but it also has the side effect of reducing immediate risk.

- Begin making AI control a load bearing part of your safety case by the time when your evaluations indicate an AI R&D speedup of 3x.[^13]

- However, only a 7% chance of existential risk is incurred if you wait until 10x AI R&D uplift. This is a serious cost which a sane civilization would not be willing to pay, but, given limited resources and political will which are likely to apply in practice, it might be the correct all things considered strategy to hold off on seriously implementing control until later, due to opportunity cost.

If the AI situation changes, Ryan’s views on risk would update as follows:

- If we observed substantially **more garbled COT,** then our marginal risk estimate would go up by ~1.5x. If algorithms shifted to using **neuralese,** then our marginal risk estimate would go up by ~2x. In both of these cases, we’d recommend implementing control earlier.

- If we observed our AIs actually **scheming**, or more generally getting caught red-handed, then we would update strongly towards the AIs being misaligned schemers. We might also update on their competence.

- If we learned that AI companies have been employing techniques that would incentivize the CoT to look nice, or otherwise undermine the faithfulness properties (e.g. if we learn that most CoT is merely 'decorative' as [this paper claims](https://www.lesswrong.com/posts/L9sE9qQgeh7cTQWkM/can-aha-moments-be-fake-identifying-true-and-decorative)), then my risk estimate would go up by 1.5x.

## Mitigation

During this phase, we need to prevent AIs from taking catastrophic actions (see threat models section above for specifics), while simultaneously extracting useful labor from them (see elicitation section below for specifics on that). We have two layers of defense:

- Ensure that our AIs are controlled (that the AIs are unable to cause a catastrophe, even if they wanted to).

- Ensure that our AIs are not misaligned (that the AIs don’t want to cause a catastrophe)

In practice, AI control will probably be the most load bearing part of the safety case here, because it seems unlikely that alignment techniques will be good enough to reduce risk sufficiently.

The core control loop is:

1.  Red-team our control measures by having models (or humans acting as models) try to defeat them

2.  Estimate how capable a scheming AI would need to be to defeat our measures

3.  Evaluate whether our current AIs are below that capability threshold

4.  Iterate on measures that seem insufficient, or de-deploy AI systems that are sufficiently capable that they break our control.

### What you need to ensure control for

There are many domains that we need to ensure control of our AIs while they are deployed in. The basic strategy will remain the same (executing the above control loop), but it’s useful to have a concrete picture of all the domains that we are relying extensively on AI labor for.

- **Normal AI R&D, especially safety R&D.** This is particularly important because if the AI R&D process is hijacked, it could directly lead to an existential catastrophe through subverting the safety measures or inserting misaligned goals into successors. This is the main focus of control.

- **Robots**. This is discussed in more depth below, in the Plan A section, where it’s especially relevant.

- **Acasual research**. We hope that we don’t need to use AIs to do this, because it’s an extremely difficult to verify and conceptually loaded domain.

- **Improving cyber security** (by redesigning all software and interfaces).

- **Doing all of the control work itself.** For example, building better control evals, playing the red-team / blue-team game, setting up better versions of the red-team / blue-team game, etc.

- **Policy / comms / persuasion.** The leading AI project should potentially be using their AIs to assist with policy efforts. Of course, this could easily go terribly wrong (if the AIs are misaligned, they could sabotage the policy efforts, or if the company has a bad strategy, like trying to avoid an international deal that would slow takeoff down). This should hopefully not be superpersuasion, which is especially scary and probably impossible to ensure control for.

- **Strategy.** Again, we hope you don’t have to use AIs to do your strategy, but perhaps some work here is verifiable. For example, you could give the AI information only from before 2015 and have it attempt to produce work that was as good as strategy work at the time.

- **Verification.** AIs could be used to improve the robustness of hardware enabled mechanisms (HEMs), design new HEMs, design better verification algorithms (e.g. proof of work), be used as part of privacy preserving verification (e.g. have AIs monitor to enforce agreements, but only communicate 1 bit about compliance), hunting for covert projects, lie detection machines, etc. Much of this is verifiable or amenable to red-team / blue-team games.

- **Building EMs or other forms of intelligence augmentation.** There are a lot of research directions here, many of which are verifiable. However, a central bottleneck will be serial time.

- **Weapons R&D** (conventional missiles for datacenters, drones for datacenters, ABMs to undermine deterrence, etc). This could be used to help extend the lead time that a leading AI project or country has, in order to avoid needing to do an intelligence explosion. In the extreme case, this could even involve developing exotic technology (e.g. nanotech), but we hope that’s not necessary. This is obviously dangerous for the usual reasons, plus also because if the AIs hijack the weapons it could go badly.

- **Overall economy uplift / industrial explosion.**

  - AIs might be able to build their own independent industrial base, allowing them to manufacture chips autonomously, which could allow for them to do their own intelligence explosion. Note that this is hard for them to do quietly and quickly, and so is an unlikely threat model, especially in Plan C.

  - AIs running autonomous factories could smuggle out easy to manufacture offense dominant tech, like bioweapons / engineered pandemics.

- **AI Friends.** If AIs during the intelligence explosion are widely deployed as chatbots (like current frontier AIs), then they will have the affordance to convince large numbers of people to act in its interest, e.g. by lobbying for pro-AI policy.

- **Deployment in government.** As pictured in AI 2027, if AIs deployed in government are misaligned, they could strategically mislead policymakers into making decisions that would gain themselves power.

- **D/acc.** We’d like to use AIs for D/acc, especially on bio-threat related D/acc. However, building biodefenses might look somewhat close to building bio threats, need to ensure that AIs don’t have access to physical tools to build and deploy bioweapons.

### What are the main control measures that we expect in practice?

- **Human Monitoring.** Have humans read actions and thoughts generated by AIs, and evaluate how risky they are. Probably some of these actions should be a random sample of AI actions and thoughts.

- **Trusted and Untrusted Monitoring.** Human monitoring is very expensive, and so (at least in Plan C) humans will only have capacity to monitor a tiny fraction of the outputs generated by AIs. Therefore most of the monitoring will have to be done by AIs. Some of this should be done by AIs that are dumb enough that it is unlikely that they are scheming against us (trusted monitoring), while other monitoring should be done by AIs that might be scheming against us (untrusted monitoring). Untrusted monitoring might be important because untrusted models will be the only AIs that are capable enough to understand the relevant actions/thoughts. We might be able to get a useful untrusted monitor, despite the AI scheming, by training the monitor on examples of bad behavior, inserting fake examples of bad behaviour at runtime (honeypots), or hoping that the AIs have a hard time colluding. (discussed more [here](https://www.alignmentforum.org/posts/GCqoks9eZDfpL8L3Q/how-to-prevent-collusion-when-using-untrusted-models-to)).

- **Execute / Replace / Audit.** Use monitors to evaluate how suspicious the actions that an AI agent is taking. If the examples are obviously benign, let the AI agent execute them autonomously. If it is very suspicious, deploy a team of human auditors to look through the action in more depth. However, there will likely be a huge number of AI agents during the intelligence explosion[^14], and so humans will be able to audit only a tiny fraction of the actions that they take.

- **Collusion Resistant Untrusted Monitoring.** When deploying an AI agent, use other AI agents (which you might not trust for similar reasons to the original) to check if an AI’s actions are dangerous. Of course, the key problem with this is that the AIs might be colluding. The main strategy for mitigating this problem is to run sting operations on the monitors by creating huge numbers of plausible seeming harmful actions that an AI might take, and check if the monitor faithfully reports that action.[^15] If we catch the AI taking an action that seems highly likely to be misaligned, we can use that action to bootstrap more sting operations on our AI systems. Critically, we don’t have to tell any of our AIs that they were caught misbehaving, so we might be able to continually get more and more examples of AIs attempting to do harmful actions, while making our control setup more and more robust to those attack attempts and getting a better and better understanding of what types of attacks are likely.

- **[Principle of least privilege](https://en.wikipedia.org/wiki/Principle_of_least_privilege).** An AI agent should have access to the least information and permissions that are necessary for its intended purpose. For example, if an AI is doing an experiment to improve agent scaffolds, and so needs to run inference on a frontier model, it should do so via an API, as opposed to by directly accessing and sampling from the model weights. If this principle is applied well, we expect that the cost of monitoring for harmful actions could be decreased by 10 or 100x, because monitors will mostly only have to review the actions with a dangerously high number of permissions.

- **High Quality Incident Response Teams.** A key dynamic in cyber security is laying down tripwires and alerts for potentially concerning behaviour, and then poking around and auditing to identify if there was a potential threat. There should be a similar, well resourced team at any project attempting an intelligence explosion. This team should have the goal of identifying harmful actions that the AIs are taking within e.g. a few days of the action occurring. Deep into the intelligence explosion, AIs will be potentially doing months or years of cognitive labor over the course of days, and so this latency might need to be reduced to hours or minutes of wall clock time.

- **Information siloing and restricting communication.** The worst case scenario from an AI control perspective is if an AI company runs a huge number of AIs that are able to arbitrarily communicate with each other in ways that humans can’t understand (e.g. neuralese). For example, we could:

  - Limit neuralese. I.e., in some or all of our models, we could maintain a chain of thought.

  - Limit RL setups that lead to garbled COT

  - Limit opaque long term memory

  - Limit communications between AI systems to be through monitored channels.

  - Pursue various anti-steganography measures (e.g. paraphrasing).

The details of AI control are discussed more here: [The case for ensuring that powerful AIs are controlled](https://www.lesswrong.com/posts/kcKrE9mzEHrdqtDpE/the-case-for-ensuring-that-powerful-ais-are-controlled).

### Contingency: What to do when you catch your AI scheming once?

It's plausible we'll catch production AIs coherently scheming or at least doing very malign actions competently. For example, we might see AIs attempting backdoor future models, trying to escape, trying to stage a rogue internal deployment, trying to sabotage safety research, etc.

We might also see this in experimental setups which are highly analogous to the actual training setup we use. We could also find AIs ending up scheming (or at least exhibit clear cut coherent and relatively consistent misalignment) in their chain-of-thought or other legible outputs. Catching AIs scheming could substantially change our approach:

- **Reconsider current deployments.** Catching AI might invalidate the current safety case/argument/cost-benefit-calculation, so we should reconsider our practices.

- **Disclosure:** You should obviously inform the public about such an event.

- **Documentation:** Keeping good reasonably-verifiable records might help convince third parties that the incident is real and not staged. This might be important due to the potentially adversarial situation: we want to convince potentially adversarial companies and countries that might be worried about some agenda. See [here](https://www.lesswrong.com/posts/YTZAmJKydD5hdRSeG/would-catching-your-ais-trying-to-escape-convince-ai) for some discussion of why this might be an issue by default. Robust records are also helpful for after the fact detection as discussed [here](https://docs.google.com/document/d/1nRJ-2FB_f4MPbKT7dAyWQyZdAh5djDt6dXsSqEMpKDA/edit?usp=sharing).

- **Information control:** Ideally, prevent AIs from knowing they've already been caught. Minimally, red team AIs based on already having been caught to see how this changes their behavior.

- **Improve mitigations:** If we're proceeding despite this incident then there are various [ways we can improve our safety mitigations](https://www.lesswrong.com/posts/i2nmBfCXnadeGmhzW/catching-ais-red-handed#Few_shot_catastrophe_prevention). We'll want to shift our approach to control after catching the AI as discussed [here](https://www.lesswrong.com/posts/XxjScx4niRLWTfuD5/handling-schemers-if-shutdown-is-not-an-option). We should start working on responding to this incident and improving our mitigations regardless of whether we currently plan on proceeding. We should also try to better understand scheming/misalignment based on studying the incident.

- **Use this evidence to push for Plan A.** As more evidence is rolling in, and it becomes more and more incontrovertible, perhaps we can pivot to a more sane policy that doesn’t involve recklessly building ASI without reasonably high assurance of avoiding AI takeover. However, even conditional on good evidence that the AIs are scheming against us, it’s very plausible that the government will not be sufficiently convinced or too incompetent to coordinate a slowdown. Therefore, we need to be ready for a world where we keep repeatedly catching misaligned behavior, but we have to keep deploying likely-scheming models anyway.

- **It's unclear whether we should directly train against cases of clear cut egregious behavior** (that seems plausibly due to scheming). It could be bad because we are essentially training the AI to be less likely to get caught. This might make us less likely to catch further examples (which we'd prefer all else equal) and might give the AI a better understanding of our countermeasures.[^16][^17] Despite the downsides, there are cases where training against specific behaviors might be worth it:

  1.  **In desperate rushed situations**: we might proceed with deploying likely scheming AIs despite having limited risk reduction via control. In such cases, training against caught behaviors provides at least marginal improvement.

  2.  **When we have many diverse detection methods:** If training against one detection method doesn't compromise our other detection capabilities, the downside is smaller.

  3.  **When we've already eaten the misalignment risk:** There are some scenarios where we give up ensuring control over output and just hope that the AIs are not scheming. If we've given up on ensuring control (perhaps because control was too difficult or too uncompetitive in some important case(s)), so we're already eating a ton of risk if the AI is scheming and using its outputs here doesn't increase the marginal risk—then training against specific behaviors has lower downsides.

This is discussed more [here](https://www.lesswrong.com/posts/i2nmBfCXnadeGmhzW/catching-ais-red-handed).

### When do we shift effort away from control?

Once we're substantially after the ITAI milestone (e.g., we're somewhat after superhuman coder), we've hopefully researched and implemented most of the control measures we wanted (at least ones which aren't very specific to the model or its capability level). We should keep improving our control measures to handle higher level of capability, but we should hopefully be spending a smaller fraction of our time on control and shifting this effort to other areas. We're probably spending a reasonable fraction of effort on ongoing maintenance, specialization, and updates for control measures in addition to spending a reasonable fraction of effort on auditing as part of the control protocol itself. Overall, I think we should be spending a lower fraction of human researcher effort on control work (at least other than object level auditing) so this effort can go elsewhere to other research areas which are now more leveraged. If control appears to be broadly keeping up with the level of capability, then ideally we'd halve effort on control.

Because we now have more powerful models, studying misalignment analogies is increasingly leveraged. If we get relatively naturalistic examples of scheming (and especially if we have multiple), then [studying scheming using these examples](https://www.lesswrong.com/posts/gALJWSfoTkq2ky5os/prospects-for-studying-actual-schemers) is now quite promising. (Of course, if we're encountering evidence for scheming which is quite strong, we should update about the level of risk which might shift our prioritization.) As we proceed to higher levels of capability and encounter more empirical evidence, we'll have a better sense about which non-scheming threat models look concerning and need to be addressed. (Non-scheming threat models are easier to identify and study, so we should have a reasonable understanding of the probability of these threat models.) For scheming, we'll see some empirical updates based on the model architecture and we might update strongly upwards on scheming based on catching schemers or we might update downward somewhat based on not seeing as much evidence for scheming. (See discussion about how we'll update [here](https://www.lesswrong.com/posts/gALJWSfoTkq2ky5os/prospects-for-studying-actual-schemers).)

## Elicitation

By this point, AIs could be extremely useful for many applications (both technical safety research, security, and trying to buy time), so ensuring we're leveraging AIs effectively should be a substantial fraction of what we're working on and is more important than it was before (this was also harder to work on in advance). This work will probably often be somewhat specific to the application, so, a substantial part of the job of people working on technical AI safety research and security will now be figuring out how to more effectively automate parts of their work with AI (while ensuring the outputs are actually good and the AIs are controlled).

We need to achieve a lot to successfully hand off, and this will likely have to happen in a pretty short period of time, so AI acceleration is key. Even in worlds where we're able to buy a lot of time, that time will often itself be bought using AI labor (especially in Plan C). Beyond this, the hope is that the AIs we hand off to can operate much faster than humans to quickly complete the needed work.

Note that we care about "worst case usefulness" supposing our AIs are scheming (what we centrally evaluate with control) and what our best guess at usefulness is conditional on our AIs not scheming against us. So, when trying to improve usefulness, we should care about pushing up both of these. This tradeoff is discussed more in [the post on improving AI usefulness](https://docs.google.com/document/d/12VkHm_QPnOzkkJOb88L8tTZ0VWeQnVA4HvwcuLyFy0w/edit?tab=t.0#heading=h.nsmuifumfqgt)).

### What will we be trying to get our AIs to do?

During the mitigate and elicit phase, we need AIs to help with a wide range of tasks. The core applications are:

**Safety research and implementation.** This is the most important application. We need AIs to help with:

- Control research: developing and iterating on control measures, running control evaluations, red-teaming monitoring systems

- Misalignment analogies: creating and studying model organisms of scheming, testing interventions on these analogies

- Alignment research more broadly: working on avoiding scheming, improving our understanding of how training shapes AI propensities, developing better oversight methods

- Security implementation: building and auditing security infrastructure (though this is scary from a control perspective—the AIs building security infrastructure must themselves be controlled or too weak to plausibly be scheming)

- Building the evaluation infrastructure needed for iteration on all of the above

**Buying lead time.** Once AI labor is very useful for directly trying to buy time, this becomes a high priority. This includes:

- Assisting government efforts on non-proliferation

- Cyber offense and defense capabilities

- Surveillance and verification technology for international coordination

- Military applications and weapons R&D

- Industrial acceleration more broadly

- Demonstrating risks and capabilities to increase willingness to pay from other actors

AIs might only be very useful for many strategies for directly buying time (e.g., military, cyber, surveillance) at a level of capability substantially after ITAI.

**Improving AI epistemics and philosophical/conceptual reasoning.** This is important both for getting useful safety work and for handoff-viability. We want AIs that:

- Are aligned, capable, and well-elicited at conceptual/fuzzy domains

- Have good epistemics and truth-seeking abilities

- Can do a good job on extremely hard research which is loaded on conceptual/philosophical reasoning

- Can make good strategic choices even when these choices depend on high-context knowledge and intuitions that can't be made legible to humans

Ideally, we'd end up deploying AIs with impressive truth-seeking abilities that would be useful for a bunch of applications beyond just safety research.

**Preparing for handoff.** As the phase progresses, increasing effort goes toward:

- Ensuring AIs generalize to being highly aligned with pretty high reliability on all the tasks needed for handoff

- Studying how we'd make a functioning post-ASI society

- Building behavioral tests that evaluate whether handoff would go well

**Other specialized applications:**

- Whole brain emulation research (if this path looks viable)

- Human intelligence augmentation research

- Making the world more robust to powerful AIs (biodefense, cyberdefense, etc.) In plan C, this is probably relatively less important than Plan A/B, because we will be forced to hand off soon to a substantially superhuman AI. Regardless, we probably should use AI to pick some of the low hanging fruit.

**External deployment to safety researchers.** Making AIs accessible to outside groups working on reducing risk is important. This involves:

- Giving them better model access

- Eliciting models specifically for their usage

- Potentially ensuring control for their use cases (making sure control evaluations cover this use case, providing access to internal control measures, and adapting/building new control measures as needed)

Making AIs accessible to outside groups working on these things (and treating these groups as important customers) is also important. This could involve giving them better model access, eliciting models specifically for their usage, subsidizing compute for important applications, and potentially ensuring control (e.g., making sure our control evaluations cover this use case, providing access to our internal control measures, and adapting/building new control measures as needed).

### Expected acceleration from AI labor

How much acceleration can we hope for? One way to think about this: safety research/implementation is produced by putting in labor, compute, and wisdom/judgement/taste. There is some production function of output based on these input.

AIs will be able to accelerate labor for AI capabilities R&D by some amount. The multiplier for safety R&D labor will probably be smaller because safety is harder to accelerate due to being more confused and harder to verify (though elicitation measures could help close this gap). But safety R&D will probably have relatively larger returns on labor (rather than compute) when compared to capabilities R&D. Overall, this makes it unclear which will be accelerated more by AI, at least if lots of effort is put into accelerating safety R&D. We don't need safety R&D accelerated more than capabilities—we just need it accelerated enough.

Some rough estimates:

- **Between ITAI (~3x AI R&D labor acceleration) and superhuman coder (~15x AI R&D acceleration):** If safety acceleration is AI R&D acceleration to the power of 0.6 (due to bottlenecks from human labor, poor elicitation, and the control tax), this yields safety R&D acceleration of 2.2x to 6.7x, with an average overall safety R&D acceleration of roughly 3x. I expect a roughly exponential increase in labor acceleration over time and think that production of safety might be roughly labor_speed ^ 0.75 compute ^ 0.25 (numbers mostly made up), so the average overall safety R&D acceleration is ~2.8[^18].

- So these BOTEC numbers indicate a roughly 3x overall average safety R&D speed up.

- How long should we expect between ITAI and superhuman coder? I think I expect roughly 1 year, so this means we have 2 additional years during this period.

- **Between superhuman coder and Min-H:** In principle, we might expect Min-H to be able to speed up safety R&D labor by huge amounts (e.g. 100x) if perfectly aligned. But, elicitation and/or control might be huge blockers in practice to getting this level of acceleration out (as in, we'd end up having key human bottlenecks and not extracting out optimal labor). This might be modeled by a more aggressive coefficient than 0.6, like maybe 0.5 which only results in 10x safety labor R&D acceleration. This is a large part of why handoff is advantageous at this point. If we use the 10x safety labor R&D acceleration (100^0.5) and the 15^0.6 number for superhuman coder, we'd expect 4.8x average overall safety R&D acceleration between superhuman coder and Min-H. That said, I think the model I'm using here starts to break down in multiple ways at Min-H. (I think AIs might be able to do enough low compute safety R&D that my production function is off and I think that it's really unclear how bad the control/elicitation for safety R&D will be.)

- I expect roughly 1 year between superhuman coder and Min-H, so we're looking 3.8 extra years by default.

- If we could harness Min-H-level AIs fully for 6 months, we'd get the equivalent of 15 years of safety R&D. Of course, we might not be able to achieve full elicitation, but large improvements seem possible.

Additionally, safety directions which aren't compute constrained (including inference compute to run experiments on AIs) look particularly good: we'll have a lot of labor relative to other resources. A common strategy might be to have smarter AIs run experiments on much weaker AIs (this applies for both safety and capabilities R&D).

So without any additional lead time, you should imagine it's maybe as though we have 3 years between ITAI and superhuman coder and 5 years between superhuman coder and Min-H. But, this could be pretty different in practice: e.g. we might get somewhat less value from weaker AIs or be able to extract much more value from Min-H (especially after we spend a bunch of time improving elicitation/control or we resolve scheming well enough that we're happy to drop control). Overall, I think there is a large chance we'll be able to harness much more value from Min-H before handoff, especially due to things like partial handoff, though it's unclear how this should count as this itself required solving key alignment/safety problems.

### Elicitation techniques and methodologies

Our techniques for elicitation are the same as those used for handoff viability, which are discussed [here](https://www.lesswrong.com/posts/vjAM7F8vMZS7oRrrh/how-do-we-more-safely-defer-to-ais#Behavioral_testing_for_capabilities_and__broad__alignment) and [later in this doc](alignment-roadmap.md#building-good-behavioral-tests). To summarize, the core hope for elicitation is:

1.  Build behavioral tests

2.  Use these behavioral tests as held out evaluation sets or as RL environments to train on to improve performance.

3.  Try to use principled techniques to improve generalization performance.

Another idea for elicitation that doesn’t apply to hand off is [making deals with AI systems](https://www.lesswrong.com/posts/psqkwsKrKHCfkhrQx/making-deals-with-early-schemers). Misaligned AIs during this phase might be in a bad strategic position (e.g. they don’t believe they could successfully take over), or might have easy to satisfy preferences, which would lead to them being incentivized to take a deal.

## Security

We want to have at least some lead time with powerful AIs, which means that we probably need at least some security, sufficient to prevent adversaries from immediately exfiltrating model weights. We aren’t security experts, so we won’t cover implementation, but we will talk about thresholds that you should reach, and how the plan changes based on what level of security you get to.

Let’s first define the type of security you most care about:

- **Model weights.** If model weights leak, adversaries immediately get to run inference on your model. This is relatively less important early on (because it isn’t that bad if adversaries have early systems; the main downside is that it will accelerate their intelligence explosions), and relatively more important when you already have extremely powerful AIs (e.g. AIs that can do superpersuasion / quickly build nanobot armies). Model weights are (at least right now) very large (on the order of terabytes), which is very desirable from a security perspective, because it means that adversaries will need a high bandwidth channel to smuggle out model weights.

- **Algorithmic security.** If algorithms leak, then adversaries can rerun your training runs, and catch up to you. However, the fact that they need to rerun their training run introduces a delay, which could potentially be quite large, if the adversaries cluster is much smaller than yours. If you have a large hardware lead (e.g. 7x more compute, which is the current US/China gap) in Plan C, probably algorithmic security doesn’t matter very much.

  - One important subset of algorithmic security is securing RL environments and synthetic training data. These datasets/envs are much larger than typical algorithmic insights, and so are probably easier to secure (but still harder to secure than model weights).

- **Sabotage robustness.** You might also care about hardening your datacenters against sabotage. This is potentially a negative sum proposition (because the equilibrium where everyone’s datacenters are sabotaged is good), but might be worthwhile (for example because others have hardened, and marginal compute / lead time that you have is going towards safety).

Each of these comes with a spectrum of robustness, e.g. one spectrum for model weight security is defined by RAND [here](https://www.rand.org/pubs/research_reports/RRA2849-1.html) (SL1-SL5). This spectrum is defined for model weights, but can be extended to algorithms or sabotage, and can also be extended to refer to the *length of time* you are robust. Unlike standard security (e.g. trade secrets), securing AI models or algorithms for a short period (e.g. a few months) is often sufficient in Plan C, because after a few months you’ve already been pressured into doing handoff for other reasons, usually exogenous AI progress.

HOW BAD IS IT TO NEVER DO MODEL WEIGHTS SECURITY?

Situations where it could be very bad:

- China can immediately exfiltrate your model weights, and then immediately gives them to a domestic Chinese project. This causes the leading AI project to “race itself” because any progress that it makes is immediately stolen and used by China, and so can never slow down.

- There is a small lag in model weight exfiltration. However, there is also a non-negligible safety tax that you have to pay in order to avoid a high risk of AI takeover (e.g. control tax is high, you need to not use neuralese, monitoring is expensive, etc). The trailing actor could get ahead of you if they steal your models and then, despite having less compute, discard the safety techniques.

Situations where it might be ok:

- China (and other adversaries) are not woken up to the strategic importance of AGI / aren’t on the ball with stealing model weights (even though they could easily do so).

- A core hope is that you might succeed at alignment. Then, let people steal your model, but hope that the stolen models remain aligned. Even if China has a bunch of RID, before handoff, you export safety techniques, and then you both do aligned handoff. Plausibly they just steal the alignment techniques directly.

- It might be difficult to swap the spec, e.g. because it took a bunch of data to train the model to be aligned. The stolen model could be relatively rigidly aligned to your values.

  - In this case, you want it to be such that China is happy with the spec, and so you might want to put in concessions. This is a fine line because (1) you want to make sure the values in your spec are good enough according to china that they will implement your alignment techniques, and (2) you want to make the AI values as good as possible by your lights. As a baseline you could do corrigibility, but you might want to push some of your values in a bit.

Probably, we will at least want to get to something like SL-5-1TB-2-months (read: SL5, i.e. secure against high priority operations by top cyber-capable nation states, for exfiltration of model weights that are at least 1 TB in size / 500B FP16 params, for at least 2 months), before handoff.

The core hope will be to get security escape velocity := if you keep working on improving security with the budget you expect, China will no longer be able to steal the model weights until the end of the singularity. The plan for doing this will be to increasingly rely on AI systems to improve security. This will involve:

1.  Quickly retrofitting physical security

2.  Largely relying on software based security methods. See [this post](https://www.lesswrong.com/posts/2wxufQWK8rXcDGbyL/access-to-powerful-ai-might-make-computer-security-radically) for more details.

Because a core thing we are doing with our AIs is to attempt to massively improve security. This means that we need to control our AIs while they are writing massive parts of our infrastructure, which is scary; this makes the Control / monitoring section above load bearing.

PHASE 2 DIVISION OF TECHNICAL AI SAFETY WORK

I'll summarize our overall priorities into a best guess list, but first it's worth discussing some limitations of this single list. The ITAI to Min-H period covers a wide range of capabilities and our priorities will shift continuously as the capabilities level increases (and as we update based on evidence from the world). I'll focus on our priorities as of halfway between superhuman coder and superhuman AI researcher, which is also around halfway between ITAI and Min-H (which are respectively somewhat before and somewhat after each of these two milestones). This is at Jun 2027 in the original AI 2027 scenario. To get a sense for what our priorities are for earlier or later capabilities, you can interpolate these priorities with the priorities I discuss under ITAI and under delaying at Min-H.

In addition to our priorities changing with the level of capabilities, our priorities will change due to updates we've made from observing powerful AI systems and how the world reacts to powerful AI systems. These updates will continue ongoingly throughout the mitigate and elicit phase due to both advancing capabilities (and the underlying algorithms driving these capabilities) as well as the outside world reacting to capabilities (which may have a substantial lag). Large algorithmic shifts might happen at pretty high levels of capability (e.g. after superhuman coder), especially because AI R&D is accelerated, so we may not see relevant updates until pretty late (though we can try to guess where things will go).

The numerical priorities list I give will assume my typical guess at what will happen (assuming the AI company is following this overall plan). The assumptions here about AI properties and development are pretty similar to what we see in AI 2027 (though the speed of AI progress isn't necessarily that similar). In particular:

- We haven't yet caught models scheming, but the architecture is strongly trending in a direction that makes scheming more likely. We have some model organisms in which we caught mostly natural, but not that competent scheming in some somewhat exotic conditions that made scheming more likely and catching easier. We aren't confident our current AIs aren't scheming some of the time, they use neuralese.

- Clear cut issues with deployed behavior due to reward hacking have mostly been resolved, but there are still various types of reward hacking in training and occasional issues in deployment, typically more subtle issues.

- Control is basically working (as of somewhat after superhuman coder) and we have a reasonable (though not perfect) safety usefulness profile and we did a mostly OK but somewhat messy job at evaluating this control. There might have been a period where control wasn't keeping up with capabilities, but using AI labor and dedicated effort, things got back on track.

- We have a somewhat bad neuralese decoding method that we think probably won't be robust to intentional evasion from the AI and only produces slightly useful results. Outside of this we didn't really make that much progress with interpretability, but we have somewhat useful methods for augmenting behavioral testing and better understanding why some behavior occurred.

- AIs are somewhat better at easy-to-check tasks and are bad at "taste" relative to humans, but there is still some transfer and generalization

- By the time AIs are automating AI R&D, there will quickly be huge numbers of AIs which are effectively running quite fast (see AI 2027 numbers)

- AIs will have substantially lower than human sample efficiency by default, but they will compensate with a bunch of AI specific advantages and there will be a bunch of somewhat domain specific tricks to improve sample efficiency at learning within some domain or learning on the job with more compute (e.g. generating similar tasks to what you're working on and ongoingly doing RL on those tasks)

- It's quite viable to make USG sufficiently bought in (including to safety concerns) that they are willing to take aggressive actions to slow down other (adversarial or less safe) actors including working with the AI company on this and they are willing to slow down for safety concerns if there is a lead. (This isn't necessarily my typical guess, but it seems plausible).

- Whole brain emulation (and other human augmentation) ended up not being a viable path

Here is this best guess list of priorities given these updates and assuming we're halfway between superhuman coder and superhuman AI researcher. The percentages correspond to fractions of human labor within the AI company and correlate with compute usage also.

- 15% control and control-adjacent measures (this is a relatively broad category which includes some things which aren't centrally associated with control but which I thought more so fit in this category than in others)

  - 7% misc ML/AI focused control research and implementation.

  - 5% ongoing maintenance and updates to our deployed control measures

  - 1% software infrastructure

  - 2% building a high quality human evaluation process which is robust to scheming

- 21% model organisms / analogies

  - 16% misalignment analogies for scheming (we would put more effort here if we had found stronger results so far)

  - 1% model organisms of other threat models

  - 4% studying mitigations, including by trying stuff on model organisms. (we would put more effort here if we had better model organisms to study)

- 20% making AIs differentially more useful for safety work and preparing for aspects of deference other than resolving scheming

  - 9% generally trying to apply AIs to assist the rest of this safety work and making AIs more useful for this.

  - 5% Improving AI epistemics and philosophical/conceptual reasoning (will also help with generally making AIs useful for safety work)

  - 5% Generally preparing for deference (via means other than working on scheming) (will also help with generally making AIs useful for safety work)

  - 1% other aspects of deference

- 17% using AIs for building a lead in partnership with USG (and getting USG more bought in, though note that scary demos are in a separate category below). To the extent there are returns to more compute, this should use a relatively higher fraction of compute compared to the labor of AI company employees. Also, it's possible this can't productively utilize this much of the labor effort. If so, we should shift this labor into other areas (mostly uniformly). Also, note that the resources in this area should increase with further capabilities.

- 3% make the world more robust to powerful AIs aka d/acc (biodefence, cyberdefense, eating free energy, etc). It's plausible this should have a higher fraction of resources, I'm quite unsure.

- 5% neuralese decoding

- 10% misc science, understanding of relevant AI properties, and other (not including control-adjacent science).

  - 2% Various interpretability methods (top-down, bottom-up/mech interp). I extracted out neuralese decoding from this category.

  - 1% Making deals with AIs and getting consent

  - 2% Generally looking for concerning model behavior (not necessarily in ways which would help detect models coherently scheming)

  - 3% moonshots which seemed promising based on earlier work

  - 2% Misc

- 9% capability evaluation and demonstrations of both powerful capabilities and misalignment

  - 7% scary demos

  - 2% evaluation, surveys, and forecasting

Again, recall that this is a pretty uncertain prioritization and the prioritization in practice will depend on various updates as discussed elsewhere. For instance, if we caught production AIs scheming against us, we'd shift relatively more resources in scheming mitigations and understanding and away from everything else.

This prioritization isn't focused on exporting work to other AI companies and this would probably change the prioritization somewhat. More focus on exportability would somewhat reduce focus on control, utilizing AIs effectively, and preparing for deference (including epistemics/conceptual stuff) as these areas probably involve more complex techniques which are more integrated with this specific AI company and the last two of these may also have substantial capabilities externalities. We'd shift focus to model organisms, neuralese decoding, building awareness of risk, and other research directions which might produce simple and easy to implement measures which nonetheless are very useful.

# Phase 3: Pause

At some point, we have increased AI capabilities sufficiently that we could handoff safely if our AIs are aligned and well elicited, i.e., they would be able to manage the ongoing intelligence explosion better than the humans, if they were trying as hard as they could on that task. Our default recommendation is to pause at this point, and attempt to complete all other necessary research to complete handoff, notably handoff viability and reducing the likelihood of explicit scheming. During this phase, we will still be heavily leveraging AI labor, meaning that we will be continuing elicitation and mitigation efforts.

During this section, we’ll discuss when we should pause, what we should do while being paused, and what exit strategies we should pursue other than pausing. During the next section (handoff), we’ll discuss all the research that needs to be completed before handoff (which we divide into mitigating scheming and handoff viability), though note that this research needs to largely be completed during this phase.

## When should we pause?

**Default answer: Pause at Min-H**: AIs which have a level of overall general capabilities which would suffice for handoff being viable. (As in, the capabilities would suffice for our handoff desiderata if the AIs were also sufficiently aligned and as needed we made narrow improvements to the capability profile which don't augment general abilities.) For an AI to qualify as Min-H, it would at least need to be capable enough to automate AI R&D and ongoing technical AI safety work (after further elicitation/alignment work and narrow improvements to the capability profile).

At the point where we pause, this does not assume that the AIs are aligned enough that we can trust them, or that the AI has all needed specific capabilities that we care about and can be trained in without improving general capabilities.

**Min-H is a natural stopping point** because these AIs are sufficient for handoff (by definition), and if we scale further we incur additional risk that scheming will emerge before handoff.[^19] Put another way: after handoff; the AIs are more capable than us at handling the situation. Therefore, if we avoid scheming, so the AIs are actually applying their capabilities towards intended goals, then overall they will manage the situation more competently than humans. Since we incur substantial additional risk from misalignment, and by default don’t get substantial benefits, we should pause at Min-H, and only scale to more capable AIs after we’ve handed off to AIs at this level of capability.

This isn’t universally true: there are some situations where you want to pause before Min-H, and some situations where you want to pause after Min-H; these are enumerated below.

**Cases where we might want to pause before Min-H:**

1.  **Control techniques don’t scale to Min-H.** Pushing all the way to Min-H and only then pausing, probably incurs substantial AI takeover risk along the way. In particular, another relatively natural threshold is pause when you might not be able to control smarter AIs. However, we think that global risk (in Plan C) is probably minimized by accepting some loss of control risk at the earlier stages in order to have more time to work on handoff being safe.

2.  **We have a large lead.** If the leading AI project has a large lead, then it won’t need to rush to Min-H, and can pause beforehand while still having enough time at Min-H to work on handoff viability. This is pretty unlikely in Plan C.

3.  **Bad security.** This is particularly relevant in the regime where you have good domestic coordination, bad model weights and algorithms security, and China domestic progress is slow enough that it’s mostly driven by leaked models and algorithms. In this regime, if you slow down early, this slowdown is basically free. In this situation, it’s plausible that US AI companies should just go however quickly China would go by default: “China match”, in order to have the most overall time during takeoff to get ready for handoff. In this world, we might never fully “pause”, but still in practice end up burning substantial lead because of capabilities progress slower than it otherwise could have been, or we might do china-matching until Min-H, then burn lead at Min-H, then hand off.

**Cases where we might want to push beyond Min-H (without handing off):**

1.  **Handoff viability research velocity is constrained by the capabilities of the AIs, as opposed to human monitoring/understanding.** If we can reliably control AIs that are smarter than Min-H, and we can elicit useful work out of them, it would make sense to scale further. However, we currently think that at this point, control will be bottlenecked by human understanding; if we have smarter AIs, we wouldn’t actually get to do more research, because we’d have to limit their progress until humans have understood it sufficiently to ensure that the research is correct. Another way of phrasing this is that we have a control solution that scales beyond Min-H AIs, which works sufficiently well to both mitigate risks *and* elicit capabilities from a more capable model.

2.  **We have access to high assurance techniques to mitigate scheming beyond Min-Handoff, but haven’t finished handoff viability research.** If we have an alignment solution which we are confident will prevent scheming up until a capability threshold above Min-H, and we aren’t finished with handoff viability research, then it’s probably a good trade to scale up. This is usually a special case of (1). My best guess is that handoff will be mostly bottlenecked by the possibility of scheming, and so this will not apply.

3.  **We’re aiming for an exit strategy other than handoff.** For example, maybe we need particular AI capabilities for some Plan B-related sabotage option, or to help with human intelligence augmentation.

4.  **We’re in a desperate situation.** For example, in Plan D, the leading AI lab might be training more capable AI systems, and there’s nothing the safety team can do about it. In this situation, it might be important for the safety team to wait until a higher capability level in order to complete basic handoff viability research. For now, we’re assuming that we’re in Plan C, and so there is enough will to spend some slack slowing down.

5.  **Misc combinations of the above.** Generally, desperation, better alignment, control, and elicitation techniques push towards scaling beyond Min-H before handoff, while the reverse pushes towards slowing down earlier (or at least not scaling beyond Min-H).

**How long to pause?**

This will basically be a tradeoff between the marginal returns to hand off viability and reduction in scheming from more pause time and the risk of being overtaken from waiting longer. Updates towards the AIs scheming and towards handoff viability taking longer than we thought will suggest that we pause for longer, updates towards competitive projects will imply that we pause for less long.

## Priorities while paused

Our priorities at the start of this phase might look something like:

- **P0:** Buy time using non-proliferation (including e.g. demonstrating risk).

- **P1:** Prepare for deference (avoiding scheming and handoff viability).

- **P2:** Ensure our current and immediate future usage of AIs is safe and secure

- **P2:** Better elicitation of AI labor beyond handoff viability

- **P3:** Make the world generally more robust (d/acc)

If buying more time isn’t feasible, then all priorities other than P1: preparing for deference, mostly do not matter during this time.

By the point of Min-H, we're even more likely to have updated a bunch about the situation and the most relevant risks. So, it's plausible that we've determined that scheming is an extremely hard to resolve problem which is very likely to show up in any given training or we might have determined that scheming is a non-issue at this level of capability.

No matter what, once we're reaching the end of this phase (because we're out of time or we feel quite confident in how well deference will go), our top priority should be making deference go well. It's plausible that lead time requires ongoing maintenance (as in, ongoing efforts to ensure we continue delaying other actors) and maintenance may be required for our d/acc work. So, if this is the case, we wouldn't be able to cut our effort on this greatly.

At earlier points in the plan, our safety work should be more focused on relatively straightforward prosaic approaches (which are relatively low hanging) rather than moonshots. This is because we're uncertain how much time we'll have and it makes sense to target easier approaches first. However, over time we'll figure out more of these more low hanging interventions so we should increasingly work on moonshots. If we end up in a relatively stable regime where we are mostly focused on preparing for deference and we've exhausted most of the more straightforward (and low hanging) approaches, we should plausibly pivot to mostly working on moonshots.

## Exit strategies other than handoff

Avoiding scheming and handoff-viability are both ultimately needed for handoff, so if we've actually given up on these objectives, we need to pursue an alternative to hand off.

The main alternatives to hand off are:

**Whole brain emulation / human augmentation.** The most viable path for human augmentation in the time we have is whole brain emulation. This would allow humans (or human-derived minds) to operate at AI speeds and handle the situation without needing to trust AI judgment on hard-to-check tasks.

My very low confidence sense is that we could achieve whole brain emulation within 3-5 years of having pretty powerful AIs using huge amounts of AI labor and an overall massive and well capitalized effort (e.g., potentially building up to trillions of dollars and using government powers like DPA etc. to speed up the project). This level of buy-in seems somewhat unlikely. This seems very hard in Plan B and almost hopeless in Plan C.

An even more speculative option is adult biological human strong intelligence enhancement; I don't have a good sense of how viable this is, but it might be worth keeping in mind.

We could directly use controlled AI labor for human augmentation efforts but it might be better instead to first use controlled AI labor to avoid scheming (at some level of confidence) and then use these non-scheming AIs for human augmentation efforts. As in, go "control -\> sufficient alignment to avoid scheming -\> human augmentation". This is most productive if control is a big tax, it's also pretty difficult to achieve the level of alignment (or capability profile) needed for deference, and avoiding scheming is substantially easier than successful deference.

Currently, I'm unsure how we'd determine if whole brain emulation is sufficiently promising (given the amount of time we have etc.) that it's worth radically scaling up the level of investment. Figuring out how to determine this would be an important part of earlier work on this.

It's also likely that AI companies in practice wouldn't be willing to invest in this area, but I think it would be worth investing in if companies were willing.

**Escalating to Plan B.** Instead of handing off, we could delay further by sabotaging competing AI projects and pausing. This would involve either (i) using existing military capabilities, or (ii) augmenting them with AIs (potentially by scaling beyond Min-H to get to a threshold of usefulness that lets us stabilize the situation). All of these options look quite bad, but they might be the least worse option given the other possibilities. Some of these options are outlined in our unpublished Plan B scenario. Buying much more time doesn't totally solve our problem, we'd still need to defer or do human augmentation at some later point. But, buying \>10 years would massively change the regime and would mean that we can pursue very different strategies (e.g. moonshots). However, it's pretty likely that buying much more time requires taking on risk from scaling to more powerful AIs than we would need for handoff. So this is the key source of risk. But, if we have issues with scheming (but we think we can scale control) or handoff-viability, could be better than other options.

**Escalating to Plan A.** Escalating to Plans A or B through substantial government involvement, which could buy much more time through international coordination or aggressive non-proliferation efforts. This is discussed much more in our [Plan A scenario](../main.md).

Changing our primary "exit strategy" target from handoff to instead be buying much more time with military advantage (Plan B) or human augmentation would make a big difference. In particular, with handoff no longer being central, handoff-viability is less important and Min-H is less natural as a point to pause.

**Self Immolation.** It’s plausible that as a responsible leading developer, you should simply pause capability scaling and allow yourself to be overtaken: this allows you to redirect all resources to AI safety and handoff preparation. Then, you might be able to export this to whoever ends up actually doing a handoff. As another upside, this strategy provides a costly signal to governments and competitors that you are seriously concerned about the path forward. On the other hand, it’s plausible that competitors are actually unlikely to successfully implement alignment techniques you export to them (though this is a potentially self serving argument that one should be cautious about making). Overall it’s quite unlikely that this is politically feasible within companies: CEOs will by default strongly push to stay ahead of their competitors, invalidating this option. That said, it’s quite plausible to us that with the benefit of hindsight self-immolation will be seen as the obviously morally correct action, analogous to how refusing to participate in the Holocaust was obviously morally correct even though conscientious objectors would simply have been replaced by Nazis with less scruples.

# Phase 4: Handoff

After humans handoff management of the intelligence explosion,[^20] humans inside the leading AI project will no longer need an overall strategy, so this phase will largely discuss earlier stages of handoff and what needs to be done during phase 3 (pause) in order to make full handoff go well, and briefly discuss what affordances are available to the AI we hand off to.

Our core hope with handoff is that we build AI systems that are competent and trustworthy enough that we can defer to them on all of the relevant questions. In particular, our key hope is that our AI systems will end up in [the Basin of Good Deference](https://www.lesswrong.com/posts/vjAM7F8vMZS7oRrrh/how-do-we-more-safely-defer-to-ais#Recursive_self_improvement_of_alignment_and_wisdom__the_hope_for_a_Basin_of_Good_Deference) (BGD): meaning that the initial AIs we defer to will be sufficiently aligned and wise that they can manage ongoing development of AIs well. This means that we do not need to assume that initial AIs are perfectly aligned/wise/competent, only that they are good enough that they can find and address failure modes as they come up.

Our best guess strategy for achieving handoff is as follows:

1.  **Make sure tests are representative,** putting aside concerns about overfitting. We can break this category down into:

    1.  **Avoid scheming.** In particular, we care about avoiding the failure mode where AIs are deliberately attempting to undermine the accuracy of your tests, for example by strategically underperforming or overperforming on certain tasks.

    2.  **Avoid other failure modes that would make tests unrepresentative.** This is just a bunch of miscellaneous possible failure modes that will potentially apply around handoff. For example:

        1.  Weird memetic pressures happen at large scale, so that small scale testing is not representative.

        2.  People trying to jailbreak your AIs (E.g. China inserting secret loyalties)

        3.  AIs optimizing to look good on tests terminally (e.g. so that they are much less confident once not in test settings).

        4.  It’s salient to AI that they are in a test in a way that causes them to behave very differently.

2.  **Build good behavioural tests.** Putting aside the risk of scheming, we’re going to want to build a huge number of difficult tests/evals, such that passing the evals entails sufficient capability *and* alignment for handoff. This will mostly include things like open-ended, hard to check conceptual reasoning such as philosophical reasoning, theoretical alignment arguments, improving AI control, etc.

3.  **Iterate against the test without overfitting.** Finally, once (1) and (2) are complete, we’ve reduced the problem of handoff into a “normal” ML problem: AI companies can iterate against the tests they’ve constructed, while taking care to avoid overfitting. We’ll hopefully be able to use somewhat principled techniques and some understanding of what is going on, given the need for some amount of generalization.[^21]

Note that our strategy for handoff is extremely similar to our strategy for elicitation during Phase 2 and 3. That’s because we are solving the same problem: trying to ensure that AIs are doing useful work. The main difference is that in Phase 2 and 3, we still have humans in the loop, and so we can check AI outputs at deployment time using human labor, and we can still have humans to use as a load bearing part of the research process, while after handoff, the AIs must be trusted to do this all autonomously.

This post discusses the technical plan for handoff in [much more detail](https://www.lesswrong.com/posts/vjAM7F8vMZS7oRrrh/how-do-we-more-safely-defer-to-ais).

## Why handoff?

The basic case for handing off is that in Plan C, leading actors are unwilling to pause further or delay for time (e.g. via sabotage), and thus we have to build vastly superhuman AI systems. If we’re going to do that, it seems better to hand off control of that process to AIs than to try to run it ourselves. This is because (i) it is probably easier to align only roughly human level AI systems (more specifically Min-H) than AI systems that are vastly smarter than humans, and (ii) that aligned human level AI systems will be better than humans at managing the transition to future AI systems than baseline humans. Therefore, we can do better by empowering aligned human level AI systems and trusting them to make further development go well, than by trying to directly pursue the future AI development ourselves.

In practice, our guess is that AI companies will be prone to scale capabilities too quickly, beyond the relevant thresholds (e.g. Min-H AI and Max-C AI), but also prone to hand off too late, out of a misplaced desire to keep in the loop. In practice, AI companies will likely not handoff deliberately, and instead simply scale beyond the relevant thresholds and handoff in practice, as humans become too slow to be tracking the relevant developments.[^22] We think this is a bad strategy, and that it is better to measure the relevant thresholds, carefully monitor when you are crossing them, and then ultimately empower AIs intentionally if it is better than the other options.

## Prosaic plan for handoff

![](../assets/supplements/alignment-roadmap/image3.png)

We’ll now discuss each component of the handoff plan in more detail. Note that this is just our best guess breakdown assuming that the situation looks similar to what it does today, i.e. there haven’t been massive breakthroughs in alignment techniques elsewhere; if there have been breakthroughs that seem better than this baseline, we should do those instead.

### Avoiding Scheming

(Basically just stolen from here: [An overview of approaches for avoiding scheming](https://docs.google.com/document/d/1PCQKI3kAdE5HeEiIKN16gszu3kjF0bsowroZB7tDuS4/edit?tab=t.0#heading=h.8n06a4t3bq9h))

Scheming can be hard to handle because we can't necessarily directly study it with behavioral tests (as schemers would want to avoid being caught and studied). There are two main paths to handling scheming:

- Studying scheming (testing measures, building a better understanding, etc) on **misalignment analogies** (sometimes called [model organisms](https://www.lesswrong.com/posts/ChDH335ckdvpxXaXX/model-organisms-of-misalignment-the-case-for-a-new-pillar-of-1)) while hoping our results transfer to the actual schemers we're worried about. This category includes:

  - Studying **actual scheming AIs**. We'd need to detect that these AIs are scheming which could be difficult because schemers (at least the type we were worried about with long run dangerous preferences) would want to avoid being caught all else equal. But, I think there are some routes to overcoming this and studying actual schemers would likely be the best from an analogousness perspective. I discuss how we might do this in much more detail in my post [Prospects for studying actual schemers](https://www.lesswrong.com/posts/gALJWSfoTkq2ky5os/prospects-for-studying-actual-schemers). I also discuss a specific type of strategy for studying actual scheming models (and resolving some of the difficulties in doing this) in my post [Iterated Development and Study of Schemers (IDSS)](https://www.lesswrong.com/posts/QpzTmFLXMJcdRkPLZ/iterated-development-and-study-of-schemers-idss). The category of studying actual scheming can be further decomposed into:

    - We could study **natural scheming** where a plausible AI development process (training, prompting, scaffolding etc) results in a scheming AI (that we can detect).

    - We could study **scheming from a rigged process** where we construct an implausible AI development process—as in, an AI development process which isn't similar to what might happen in practice—which results in an actual scheming AI (that we can detect). This category doesn't include cases where we directly train in scheming behavior, as I put that in its own category.

  - Studying **trained-in scheming behavior** where we directly train (or instruct) an AI to behave how we think a naturally scheming AI might behave (at least in some ways). This doesn't (necessarily) require catching actual schemers, but it might be extremely disanalogous such that results don't transfer basically at all. I discuss this in more detail in my post [Reducing risk from scheming by studying trained-in scheming behavior](https://www.lesswrong.com/posts/v6K3hnq5c9roa5MbS/reducing-risk-from-scheming-by-studying-trained-in-scheming).

  - Studying **abstract analogies**, cases where the AI we're studying isn't doing something resembling scheming, but we nonetheless think it is analogous for some structural reason. It might only be analogous with respect to one specific property schemers have (or a subset of properties), in which case, we'd want our work to focus on the relevant properties. A concrete example of an abstract/structural analogy is [this empirical work using an AI which expresses politically conservative views but only when it is confident that it is talking to a politically conservative user](https://www.lesswrong.com/posts/bhxgkb7YtRNwBxLMd/political-sycophancy-as-a-model-organism-of-scheming) (resulting in a conditional policy which is in some way analogous to scheming). There hasn’t been that much exploration or discussion of abstract analogies so far, but this seems like a worthwhile direction. (In fact, I think it will plausibly be ultimately more useful than studying trained in scheming behavior as we might be able to study huge numbers of diverse abstract analogies while diversity seems much harder in the case of trained in scheming behavior). Julian Stastny discusses some additional examples of abstract analogies in [this post](https://www.lesswrong.com/posts/5zsLpcTMtesgF7c8p/two-proposed-projects-on-abstract-analogies-for-scheming).

- Applying **principled methods** where we have some good a priori reason to think the method would be helpful (potentially given some empirical results from applying the method or a similar method to something other than studying scheming). For instance, we might believe some particular modification to the situational awareness of the AI during training is helpful. As another example, we might have some method for decoding "neuralese" that we believe is highly effective for understanding the AI's cognition (including on scheming AIs) based on various empirical tests and there is a solid a priori case for it being helpful to understand the AI's cognition for detecting (and then potentially iterating against) scheming. Note that this category includes methods for detecting, preventing, removing, and better understanding scheming. Even if we’re just focused on avoiding scheming, then methods for detecting (or understanding scheming) are still applicable as detecting (and better understanding) scheming would help us develop methods for avoiding scheming. I plan on providing a list of principled method ideas and discussing principled methods in more detail in a future post. I discuss principled methods in much more detail in my post [Principled methods for avoiding scheming](https://docs.google.com/document/d/1pJt4Rm4EnssE-_2Ha18Hy_dqiysFLhsegm2KUILls9Y/edit?tab=t.0#heading=h.jstxxz8vw8gf).

### Avoiding Misc Failures

**We also need to avoid all other failure modes that would make our behavioural tests unrepresentative.** This isn’t a super natural category, but it’s just where we’ve chosen to discuss everything that would cause representative behavioural tests to fail other than scheming or overfitting.

Particular failures to avoid include:

1.  Generalization failures from testing to deployment.

    1.  Examples:

        1.  There might be weird memetic pressures happening at a large scale.

        2.  Online learning, which results in AI capability profiles drifting in a way that causes failures (including the emergence of scheming).

        3.  It’s salient to AI that they are in a test in a way that causes them to behave very differently.

        4.  AIs optimizing to look good on tests terminally (e.g. so that they are much less confident once not in test settings).

    2.  Mitigations: Basically, either we’ll need the tests to be as representative as possible, so that the distribution shift they need to cross is as small as possible, and then we’ll also need to use techniques that are as principled as possible (as opposed to ad hoc solutions which appear to work in distribution). Also, try to be careful about holding out some test sets (which are drawn from a different distribution than train/validation), and see if we get good generalization to the held out test sets.

2.  External adversaries inserting secret loyalties.

    1.  In Plan C, the goals of the AI systems become extremely load bearing because we are handing off trust to the AIs. If adversaries are able to corrupt the goals of the AI system (e.g. by inserting a jailbreak) this would be catastrophic, and could cause this methodology to fail.

    2.  Approaches for mitigation:

        1.  **Do nothing and hope.** It’s unclear that adversaries will by default be sufficiently on the ball to carry out this sort of operation, despite AI projects lacking sufficient security to prevent it.

        2.  **SL-5 Sabotage Security.** Prevent (even) highly motivated external actors from being able to sabotage / backdoor the models. This could involve [using AIs for security](https://www.lesswrong.com/posts/2wxufQWK8rXcDGbyL/access-to-powerful-ai-might-make-computer-security-radically). Verification methods like training proof of work via partial recomputation might also become helpful here to validate that the training data of models is correct.

        3.  **Scheming mitigation generalizes.** Many of the approaches for preventing scheming could generalize to prevent secret loyalties. Anything involving transparency could potentially detect / prevent secret loyalties. Misalignment analogies / honeypots could catch models with secret loyalties.

        4.  **Value propagation difficulties during the intelligence explosion.** We could accept that some models are backdoored by adversaries, but hope that the process of recursive self improvement removes secret loyalties. Distillation, which may be a component of RSI, [seems to remove many backdoors](https://arxiv.org/html/2510.18541v1?utm_source=chatgpt.com). RSI might also involve generating novel datasets from scratch for each new training run, and so the adversary would need to insert poisoned data to each new generation.

### Building Good Behavioral Tests

First, let’s discuss what properties we need to ensure with our behavioral tests:

1.  **Capability Profile.** We want to make sure that the AIs are sufficiently capable at all the narrow tasks that would otherwise bottleneck handoff. The capability that we’re most worried about bottleneck handoff is conceptually loaded research on open ended, hard to check tasks like AI safety and philosophy ([more](https://www.lesswrong.com/posts/vjAM7F8vMZS7oRrrh/how-do-we-more-safely-defer-to-ais#Objectives_with_the_capability_profile)).

2.  **Alignment Profile.** We’re unsure what the exact alignment target should be. Our best guess is that the alignment profile should be that the AIs are corrigible: they generally follow human instructions through the desired channel (e.g the instructions of a political institution), and don’t attempt to subvert human modification or oversight in any way. ([more](https://www.lesswrong.com/posts/vjAM7F8vMZS7oRrrh/how-do-we-more-safely-defer-to-ais#Objectives_with_broad_alignment))

We hope to build behavioral tests for both of these. Either, this will involve using domain area experts to verify existing work, leveraging unpublished work, doing unlearning and seeing if models can rediscover ideas, or using a limited training corpus and seeing if models can rediscover.

Ideas for **conceptual reasoning evaluations:**

- Rediscover Math/physics/economics/CS etc. Or push the frontier on problems that are known to be difficult.

- Build rockets without testing and see if they work. More generally find tasks which we can make hard-to-check for the AI, but which we can have humans check afterwards.

The main hope with these is that there are generalizable reasoning skills which apply across a wide range of conceptual research domains, i.e. that training a model to be good at conceptual physics research also helps the model to be good at conceptual AI safety research. Note: this is capabilities research, and obviously could accelerate AI takeoff, which could be very bad. However, these capabilities are also on the critical path for handoff, and so at some point we’re going to need to solve them. Moreover, directly training for the capabilities that we need for handoff means that we might need to scale general capabilities less far, which reduces risk. The overall prioritization of this research avenue generally seems complicated and should be pursued only with care.

**Domains that we should directly evaluate:**

- **AI strategy.** E.g. given knowledge from 2005, how good is it at coming up with ideas that seem to make sense in retrospect.

- **AI Control.** AIs attempt to make alignment/control arguments and then evaluate if they were successful, and whether or not the AIs predictions about generalization behavior were correct or not.

- **Scheming detection on model organisms.** We could also do things like build scheming models and then see if the AIs can distinguish between the schemers and the normal models.

- **Theoretical AI safety.** Try to have AIs rediscover unpublished work from places like ARC Theory, MIRI, and CLR.

### Iterate against tests without overfitting

The basic approach for iterating against tests without overfitting is discussed more [here](https://www.lesswrong.com/posts/vjAM7F8vMZS7oRrrh/how-do-we-more-safely-defer-to-ais). To summarize, the main approaches are:

- Construct RL environments or synthetic data which train for the relevant capabilities

- Collect human data/feedback in the domain and use this for training.

- Experimentally find domains which transfer well to the domains that we care about, and then scale up training on those domains.

- Miscellaneous other tweaks to the training approach which in practice leads to better performance on the evaluation (taking care to avoid overfitting).

## When should we hand off?

Our ultimate goal is to have the AIs we defer to resolve risks associated with powerful AI systems (and potentially other serious risks that happen to occur at this time) while preserving option value and keeping humans in control of longer-run values-loaded decision making (e.g., how Earth should be governed in the longer run, what should happen with the cosmic endowment, etc). Correspondingly, our aim would be that the AIs we defer to (and their successors) don't seize power or (unnecessarily) kill humans, for these AIs to effectively work on managing these risks, and for these AIs to follow some model spec which involves the AI remaining corrigible to some group of humans or some structure which is ultimately run by humans (e.g. some component of the US government).[^23]

In practice, we expect handoff to be driven largely by political will in Plan C. This in turn will (under optimistic Plan C assumptions), be driven by when trailing labs will overtake the (paused) leading lab.

Some ways the handoff trajectory could go:

1.  **Standard Plan C.** You scale to Min-H AI, work on solving handoff viability and scheming for Min-H AIs. keep control until near the end, then you ditch control, and solve handoff viability. Those AIs then FOOM to the sky.

2.  **Stop doing control (SDC-Handoff) Early.** Ditch control early (e.g. before minH, e.g. at or before SAR), pray AIs aren’t scheming, then scale to Min-H, then pause there, then solve handoff viability, then hand off. This would trade eating a bunch of misalignment risk from scheming at Min-H AI and below, in return for saving more resources in order to make deference go well. This could be worth it if we think the risk of scheming until Min-H is reasonably low and the additional resources spent on control would yield large absolute returns in making deference more likely to go well (perhaps because otherwise we’d have very little time). It seems likely to me that most of the difficulty in making deference likely to go well is ensuring that these AIs aren't scheming (and don't end up scheming due to alignment drift or similar after deference), so just eating all of this risk might greatly reduce the difficulty of the problem (meaning that if the situation otherwise looks desperate, this is a non-insane bet we could make to "[play to our outs](https://www.lesswrong.com/posts/xF7gBJYsy6qenmmCS/don-t-die-with-dignity-instead-play-to-your-outs)").

3.  **Military at MaxC.** Keep control, scale substantially beyond Min-H while keeping control, use those AIs to get a military advantage (or any other way), buy a bunch more time.

4.  **Military beyond MaxC.** Same as above, but ditch control while not doing HTC-handoff. This is because building robot armies might be a particularly easy task to verify, so doesn’t require full handoff. It does probably require scaling beyond minH, without relying on the AIs (because that’s a conceptually confusing task that is hard to verify, so deferring to the ais here would involve full handoff), so it would rely on better than expected techniques for mitigating scheming during the phase beyond minH (e.g. up to +2SD TED-AI, or maybe even further, depending on how much time you have). Note that these strategies are much better with more time and with more USG buyin.

5.  **EMs at MaxC.** Same as prior, but human augmentation instead of military advantage.

6.  **EMs/Military at Min-H.** One of the prior 2, but magically do it with AIs that are just around minH level AI, because e.g. military or EMs were easier than we think.

## Dynamics after Handoff

The AIs are still in a potentially difficult situation after we hand off management of the intelligence explosion to them. **Either (1) the AIs need to continue propagating sufficient** **corrigibility + competence while outracing competitors**, **or (2) the AIs need to find a way to stall competitors (e.g. via a deal or via sabotage).**

In a bit more detail, here are some possible end states after handoff:

- **Widely proliferated scalable cheap alignment.**

  - The leading AI project solves scalable alignment, and proliferates this solution to competitors. If alignment is sufficiently cheap, then competitors will use it, and we’ll end up in a multipolar world with many aligned AIs.

  - Post Handoff power becomes distributed relative to initial capabilities + compute + physical assets + political clout. Starting the intelligence explosion first probably matters a moderate amount. If the post intelligence explosion economic doubling time is like 2 months, then with a two month lead, you get an initial doubling on top of your compute, so you get relatively 2x more power.

  - AIs have some additional affordances relative to humans for making alignment progress. Notable additional options:

    - They might just be able to get a bunch of normal techniques to scale further, e.g. control, but now the “trusted” waterline is much higher

    - there is way more machine labor

    - scalable alignment via introspection + improving capabilities

- **Outrace all competitors.**

  - If alignment tax remains high, it’s not an option to proliferate the alignment solution to competitors, because competitors who are racing hard will choose to not use the alignment solution. In this scenario, competitors will turn into a rogue AI with high probability. Moreover, even as a leader, if you are paying too much safety tax, they could outcompete you.

  - You might do your software foom, and then you start your nanotech foom. But the nanotech foom starts going really quickly. Ryan guesses that physical limits are something like doubling times of a day, plausibly less. You go to space quickly and do most of this doubling there, because you quickly run into waste heat problems on earth.

    - If waste heat is a large competitive advantage, this plan doesn’t work, so you have to stop your competitors somehow, or do some sort of coordination (e.g. via regulation or agreements).

    - Or you could boil the oceans yourself, this would involve putting all humans in shelters, or putting all humans in space, but this could probably be done pretty cheaply at this point.

- **You stop competitors via regulation.** There are a variety of options here: the leading AI company could push for a regulatory capture outcome, where all other competitors are barred from building AI. Alternatively, the leading AI company could push for coordination for everyone to use the alignment solutions, despite being expensive, thereby preventing defecting projects from outracing. This works domestically for a time, but soon China will catch up and start outracing, so eventually this solution breaks down or requires international cooperation.

  - It’s important to note that international cooperation may become more likely this deep into the intelligence explosion.

- **You stop competitors via sabotage.**

  - The leading AI company could take over the world (e.g. via superpersuasion, AI company builds a military), or stop competitors via hacking or secret loyalties in competitor AI projects. Note that the nice version of secret loyalties is to hack in and then do the alignment for them—in other words, help their AIs to act in the best interest of a trailing actor, despite the trailing actor having bad takes on the overall strategic situation.

  - This obviously might not be an option due to labs not wanting to do this or if the intelligence explosion is sufficiently gradual and no company has a large AI lead, so that no individual company has a large strategic advantage. In this case, you’d need to do one of the above end states.

# Alignment strategy under different plans

## Plan D

In Plan C, we assume sufficient political will that the leading AI developer strongly prioritizes minimizing risk from misalignment AI and has at least several months lead time over developers which don't also strongly prioritize misalignment risk. In this section, we discuss some aspects of how the plan changes if the level of political will is substantially lower than this. In particular, we assume something like [Ten people on the inside](https://www.lesswrong.com/posts/WSNnKcKCYAffcnrt2/ten-people-on-the-inside) or [Plan D](https://www.lesswrong.com/posts/E8n93nnEaFeXTbHn5/plans-a-b-c-and-d-for-misalignment-risk).

We can break down what needs to be done in Plan D to tasks for the safety team at the leading AI company, other AI companies, and external actors. Of course, it’s plausible that there isn’t a clear leader: in this case you can treat all the companies near the frontier as the leading lab.

**Safety team in the leading lab:**

- Give up on the overall company having reasonable safety practices. If the AI is scheming, it’ll be able to stage RIDs (though this might not even be needed, as there is no monitoring), insert backdoors, sabotage or sandbag on relevant research, etc.

- The main priority for the safety team should be to avoid *that team’s research from being sabotaged*, while aiming to build an AI that is viable to hand off to.

  - As part of this (and other priorities), the safety team should attempt to automate their work as quickly and effectively as possible.

  - Key worry: cluster infra is untrustworthy. AIs or CCP might be tampering with the results of your experiments. This is hard to avoid because you don’t have control of the security situation. Add in safeguards to make it more likely that you can detect this on your clusters, but mostly pray.

- Other priorities include:

  - Low hanging fruit to catch misalignment in production. For example, set up some basic monitoring systems where cheap models will review communications and code written by the AI that’s automating the rest of the company, and determine if any of that code seems suspicious. There aren't enough resources to be thorough here, but it’s probably worth 80/20ing.

  - Model organisms that would be specific to your models (other model orgs can be done elsewhere), e.g. because you have most capable models.

  - Replicating safety stuff that other companies have done on your models (which are the most capable and most relevant). If possible, communicating which techniques appear to be scalable and which ones aren’t.

  - Try to mitigate the likelihood of the company escaping or staging a RID if easy, but mostly prioritize elsewhere. Probably the safety team also doesn’t have the affordances to actually mitigate this (e.g. because security mitigations entails costs the company isn’t willing to pay to researcher or AI productivity).

- Methodology for pushing for a reasonable handover candidate.

  - Largely the methodology for this will look like Plan C.

  - Plausibly do this after Min-H AI, because you want to train it in a way with a non-zero alignment tax, which means that you need some amount of additional algo progress beyond Min-H AI. This incurs additional risk because you are scaling to more capable AIs than you needed to scale to before handoff, which incurs additional AI takeover risk.

  - Consider giving up on control (before handoff, e.g. trajectory 2 above) in order to make handoff viability go better. Since Plan D will be pretty desperate and rushed, it might be infeasible to mitigate the risk of scheming. Moreover, there might be a lot of low hanging fruit to prepare for handoff viability (such as setting up open-ended conceptual reasoning task evaluations). In other words, the return to working on handoff might be much more tractable than working on mitigating the risk of scheming. (OTOH, this incurs a huge amount of risk, ofc).

- You might have political difficulties in getting the safety team’s AI adopted broadly within the company.

  - Some AIs might be schemers, whereas the safety team might have applied mitigations on their fork of the model that stops the scheming.

  - If you have an honest AI that gives good advice, the AI company might not like that. For example, the safety AI might continually (correctly) say that the company is being insanely reckless and that the CEO is gunning to take over the world.

  - The safety team should potentially try to make their AIs politically savvy, try to hope that people don’t interrogate it too hard about inconvenient topics, or just eat the political cost.

- Some subset should stay very loyal to the company. Some subset should consider whistleblowing to wake up the world about the crazy stuff going on. (though this should be done thoughtfully and could have bad effects too, e.g. if Plan C happening this could result in bad government intervention).

- Internal company employee mobilization and advocacy

  - Ideally, this should mostly happen while the employees have any leverage (before full automation of the AI company), or maybe just on vibes (because leadership maybe is friends with them and doesn’t want to make them upset.

  - Mostly we want them to care more about safety, spend more resources on safety, work more on AI safety, work with outsider actors, escalate to a better plan, etc.

- Try to pull in shareholders

  - Wealth is downstream of property rights/usg still existing, so they have an incentive to preserve this, which might be very important.

  - A reasonable fraction of the shareholders will also be employees.

- Try to coordinate with other companies

  - E.g. if a few companies are really close, they all care about safety, but are making brutal tradeoffs for competitive pressure reasons, try to do coordination so they all spend on safety.

**Trailing AI companies:**

- Try to produce actual evidence of risk to move to a Plan C or C+ scenario. For example, try to catch your AIs red handed using control.

- Do the relevant safety research yourself and export it.

  - For all the research discussed above (Handoff viability, anti-scheming measures and control techniques) that are easy to import, figure out exactly what the leading lab should do, and then make it very easy for them to implement your mitigations (e.g. by giving them the relevant code)

  - Be somewhat thoughtful about capabilities exported with the safety stuff, there will be some tradeoff here. Ideally export safety stuff with low capabilities externality, but it might also be important to export some high capabilities externality research.

- Don’t worry about your AIs escaping at all because this risk is dominated by the leading lab.

- Do worry about your AIs sabotaging your experiments. If AIs that are internally deployed sabotage (or even sandbag), this cuts directly against your main theory of change, which is to export safety research.

- Consider something like merge and assist. Alternatively, if the leading company isn’t willing to merge and assist, consider credibly shutting down, or credibly committing to not push the capability any further, in order to reduce the competitive pressure on the leading lab, so that they can pause if needed. Of course, this only applies if the leader is actually likely to slow down based on you taking this action, which is probably not true in a Plan D scenario. (From the [OpenAI Charter](https://openai.com/charter/), though in practice it seems very unlikely that this will be triggered by OpenAI)![](../assets/supplements/alignment-roadmap/image2.png)

**Outside actors (e.g. safety community):**

- Advocacy to government and companies / company employees to transition to Plan A, B, or C. By this point, swapping to A or B might be intractable, so it may just be focusing on C.

- Export safety research, similar to what AI companies should be doing. Since there is so little safety research being done in the AI company, this could be a substantial fraction of overall safety effort.

- In plan C, they are still useful as a trusted source of labor (e.g. helpful for elicitation, maybe the safety community should be contractors that audits the AIS). But this is much less relevant.

- Work on neglected things other than avoiding AI takeover. E.g. Figure out acausal stuff, post-ASI governance, etc. Now you (hopefully) have AI labor to use for these topics. Then, you can export this research into the lab, or directly to the lab’s AIs via publishing on the internet.

- Make datasets that might be helpful

  - E.g. make evals and hope the companies hill climb on them. For example handoff viability evals that teach skills that are important for handoff.

  - Make data for the pretrain corpus or RL environments to be used by the leader. Make lots of good examples of people doing relevant for handoff

    - Try to make AI more reasonable about safety, more thoughtful about space / post ASI gov/acausal trade etc.

  - Work to prevent harmful policies from being passed. It’s possible that the government is doing something actively terrible, for example passing regulation that would make it more difficult to do safety research, pursuing anti-trust concerns about AI, etc.

    - Avoid US losing AI race for no benefit (e.g. through blanket antiAI regulation that effectively blocks intelligence explosions elsewhere).

## Plan B

Plan B is quite similar to Plan C. The main differences are (i) you have more time, meaning that you can pursue somewhat more ambitious safety cases (ii) you have more affordances to buy time, and (iii) there’s generally more government involvement.

Here is a summary of the overall differences:

- The capability trajectory choices are similar, except that you potentially have more USG involvement, which allows for coordination.

  - Two obvious strategies are (1) scale as aggressively as possible until the last moment and then pause (this is the strategy taken in Plan C), or (2) match the pace of your fastest adversary, while maintaining a slight lead, until you are forced to hand off, i.e. go as slow as possible. The main advantage of (1) is that you get longer with the more intelligent (while still controllable) AIs in order to make progress on handoff. The main advantage of (2) is that in the regime where you have sufficiently bad security that you can’t prevent model weights and algorithms from leaking (which seems likely), you get substantially more serial time.

  - In Plan C, you are more likely to be forced into strategy (1), because strategy (2) requires domestic coordination and Plan C is executed by a leading AI company. In Plan B, if the USG is managing the AGI race, it could coordinate the leading AI companies to slowdown preemptively, which might create more overall time.

  - This is basically the same options as in Plan C, but perhaps you have more affordances to choose.

- Buying more time

  - If alignment seems hard (e.g. its schemeria, or you are worried about lurkville), then you want to buy more time. This can either be done via (i) more aggressive sabotage or (ii) making a deal to mutually slow with competitors.

  - Increasing USG understanding of the situation is helpful for both of the above options and so should probably be a core priority in Plan B. Therefore, Plan B should put higher weight on interventions like trying to catch our AIs red handed (or otherwise generate compelling evidence of misalignment).

  - The clearest way to buy more time is sabotage + domestic slowdown.

    - Using AIs for military R&D is a potentially important component of this plan.

- Increase total alignment effort.

  - You care more about access programs for outside actors and hiring people. Because you have more time to integrate these people into the companies. (in Plan C, you might just have like 2 months, and so there’s no point trying to hire).

- Spend a bit more time on biodefense / d/acc, because there’s more of a delay, and your overall risk tolerance is lower (though not as much as Plan A)

- It’s more important to fortify against physical attacks to your AI company. E.g. diversify where employees live. More time for this to happen, but also more likely that there will be conflict.

- Should you harden datacenters?

  - In some Plan B branches, maybe you should harden. E.g. if you are doing a competent strike on chinese datacenters, and you want to preserve resources to do safety.

## Plan A

The basic structure of Plan A is similar to Plan C, and the phases still apply pretty well. The main differences are that at every point we have substantially more time, research effort, and other resources like compute to make them go better. Note that a lot of the differences wrt Plan C will also apply in worlds where takeoff is very slow (e.g. there’s a 10 year period between AC and TEDAI by default).

By phase, a summary of the differences is as follows:

1.  **Prep.** This phase is basically the same as Plan C, because you probably don’t know if there will be international coordination during takeoff. Given positive evidence about political will, our alignment portfolio of research should bias more towards moonshots / approaches that could give high assurance safety cases, as opposed to agendas that are likely to contribute to hand off in a Plan C world.

2.  **Mitigate + Elicit.** In the Plan A scenario, this corresponds to roughly 2030-2035. For the first few years, there is high risk that international coordination will break down and parties will go back to racing. Therefore, substantial effort should be spent on a high-effort version of Plan C—we should push forward the plan and approach for handoff in the case that the deal breaks down. The main difference with Plan C is that we should be much more conservative with our mitigations; if there’s danger ahead, we are much more able to pause and mitigate.

3.  **Pause.** Once we get to MaxC AI (or AI that’s close enough to MaxC that there isn’t much point to scaling further), then we pause until handoff. Over time, we can reassign alignment effort from Plan C approaches towards moonshots/high assurance approaches.

4.  **Handoff.** The basic plan is still to do handoff. However, other exit strategies like an intense deal to prevent ever having to hand off or human augmentation.

### Main differences from Plan C

- **More focus on longer run research bets.** During Plan A, there should be more of a focus on moonshots and longer run research bets. There’s less of a need for agendas that will pay off in a short term. There’s more of a need for approaches that could result in high assurance safety cases. Longer run research bets might involve:

  - **Have a really good understanding of generalization.** When you train AIs, you are selecting for AIs that behave as desired on the training distribution. Therefore, AIs generally behave as trained on the training distribution, while off distribution, their behavior is underdefined and can be hard to predict. Key distribution shifts include training/tests -\> deployment, dumb-\>smart, deployment in low-stakes environments-\>deployment in high stakes environments, etc. Through much more investigation of the form done in [these](https://arxiv.org/abs/2512.09742) [papers](https://arxiv.org/abs/2502.17424), we might be able to get a much better understanding of how our AIs generalize. Using this understanding, we might be able to make safety cases that work even under large distribution shifts.

  - **Really good dataset design**. Right now, LLM pretraining involves using whatever high quality data is most convenient to obtain, so LLMs are trained on large swaths of the internet. In a regime with more slack (such as Plan A), we could imagine it becoming viable to design the whole dataset from scratch to teach the AIs exactly the skills/values that you want. This could potentially be done synthetically (e.g. by prompting existing AIs to generate data that was entirely nice) or manually (by employing huge numbers of humans to write data for models).

  - **Interpretability.** I (TL) agree with the discussion [here](https://joecarlsmith.com/2025/08/18/giving-ais-safe-motivations#3-2-2-interpretability).

  - **Introspective access + self improvement**. Today, it seems that AIs have [some amount of unreliable introspective access](https://transformer-circuits.pub/2025/introspection/index.html). One hope for scalably solving alignment is (1) take AI that isn’t scheming (but is potentially quite weak, e.g. it’s possible Claude Opus 4.5 could work), (2) improve introspective access to the point where the AI can reliably tell if a certain training process is corrupting their values, (3) increase capabilities while using introspective access to tell if the values are being corrupted. In some sense this is similar one of the plans for scaling up AIs if interpretability is solved, except that we’re using introspection instead of understanding to tell if the values are becoming corrupted. Notably, this could also be a strategy that post-handoff AIs use.

  - **Options to avoid handoff (e.g. intelligence augmentation).**

- **Lower ongoing risk target for mitigation.** Since we have more slack, we can now operate with a reduced risk budget, allowing us to mitigate ongoing risk more thoroughly.

  - **Handoff viability and getting useful labor from AIs (both from a control and an elicitation perspective) are less important relative to ongoing risk reduction.** In Plan C, mitigation of overall risk probably involves accepting substantial risk early on (e.g. from early schemers), in order to make sufficient research progress towards handoff in the relevant time frame. For example, in [schemeria](#id.mtfcktnazwio) (the scenario where AIs are obviously scheming), in Plan C, we are forced to continue scaling and using these AIs, even in the case where we are not confident in our control mitigations. In Plan A we can either pause until control mitigations are very reliable or until our AIs are no longer scheming (e.g. due to one of the above agendas for high assurance safety cases to mitigate scheming).

  - **High assurance control approaches.** We have more time to make control better. Some approaches for high assurance control include:

    - Maybe do formal verification to reduce vulnerabilities in the control setup and AI project security.

    - Really aggressive factored cognition with a high capabilities tax. For example we might have a giant set of dumb AIs, each working on a small part of a problem without awareness of all of the other AIs. (This should maybe be only for a small set of applications, because if this is broad, it means there is a giant capabilities overhang)

    - Slow and expensive natural language AIs on top of neuralese AIs (if we’re doing neuralese). This might be an expensive way of increasing the capability of trusted models, which makes [trusted monitoring](https://www.lesswrong.com/posts/d9FJHawgkiMSPjagR/ai-control-improving-safety-despite-intentional-subversion) more effective.

    - Have AIs with all the possible capability profiles, and select the exact capability profile that you want. Same for knowledge: you only give AIs the exact knowledge they need for solving the task they wanted to. So you have a narrow cyber model, and a robot designer model, and a safety researcher model. All of these models are denied any knowledge or capability training on domains outside of their speciality, which makes it e.g. more difficult for an AI that is used for AI safety to insert a security backdoor, because it doesn’t know very much about security. Again, this probably induces a significant tax because you need to train many models, and, at least so far, we’ve seen substantial returns from having general purpose models that are trained to be good at everything.

- All this said, probably we'll ongoingly have a substantial chance pause regime collapses especially around new president or if there are shifts in power in CCP

  - So we want to ongoingly be ready while also working on longer run bets and still trying to reduce ongoing risk

  - This is equivalent to acting like we might be in a Plan B/C world to some extent even if Plan A looks most likely. This seems especially like a good idea because (in my views) most of the risk in such a situation comes from the chance of ending back in Plan B/C.

- Mitigating exogenous x-risk from non-AI sources is relatively more important. We’ll want to spend more effort mitigating biorisk, doing d/acc, etc.

- Might be important to deliver economic goods and verification tech so regime is more stable

- Until the slowdown in Plan A seems solid, we'll want to proceed as though we're in a more like Plan B/C world because even high levels of political will doesn't obviously suffice.

  - High levels of will don't suffice as implementation is tricky and naive anti-AI sentiment can easily backfire in various ways.

- We focus our alignment plan the least on Plan A, because it’s the least important world for us to think about right now, because there will be much more labor spent on handling alignment in Plan A, and risk is much lower in this world.

### Control in a massive robots regime

![](../assets/supplements/alignment-roadmap/image1.png)

In the Plan A scenario, there is lots of physical robot labor. This somewhat increases the scope of control and adds additional mitigations.

What can robots do that’s scary?

- Rogue compute → undermine compute verification. Robots could be used to build more compute, for example by setting up rogue fabs. If there is the ability to build substantial amounts of rogue compute, this could massively increase covert project risk.

- Self replicate fast enough to outgrow ROW. If the doubling times of a robot economy become really fast, they could develop a decisive strategic advantage based on industrial superiority. (this relies on an industrial explosion overhang; e.g. countries agreeing to limit growth. However, this feels relatively likely in Plan A because unrestrained competition is probably undesirable).

- Backdoor a sufficient fraction of the military or industrial capacity to give them a DSA.

- Kill key individuals (e.g. politicians, safety researchers, in an extreme case, the general public).

- Sabotage war effort (e.g. in Plan B or in Plan A when fighting a covert project).

The mitigation strategy will involve:

- **Prevent AIs from having any substantial amount of rogue robots,** i.e. robots that are completely unmonitored.

  - If they are able to get rogue robots, then this could lead to building rogue compute, and then an industrial explosion.

  - This is especially important if the AIs are sufficiently capable to run a sufficiently complex robot economy to build hidden fabs (though it might be hard to evaluate for this capability). If they aren’t sufficiently capable to build fabs, it’s less clear how bad it is if they get rogue robots, and it might be acceptable to have some rogue robots.

  - Have a complicated monitoring system with untrusted monitors, lots of consistency checks.

- **Avoiding underelicitation**. This is problematic because you get less robot labor than you want, and you might be outraced by rogue AIs. (e.g. suppose AIs can do nanotech, they do normal humanoid robots for the humans, then they escape, do nanotech, and then wreck you).

  - For some type of underelicitation you don’t need to use it, but you want to know how good the AIs are at this. For example nanotech is in this category.

- **Traditional computer security**.

  - Each robot should have a tracking chip.

  - Each robot should have a self destruct chip. This is especially important for literal military technology (e.g. drones), because AIs could hijack that as part of a takeover strategy.

  - Mechanisms to make it difficult to put the robots in a faraday cage (to block the tracking or self destruct). E.g. they could be implemented in such a way where the robot self-destructs if it doesn’t get an affirmative signal from its manufacturer.

  - E.g. Each robot has a tracking chip, a self destruct chip.

  - Generically good cyber security on the robots.

- **Physical human inspections.** Humans should be going to sites and looking through what the robots are doing. You can also have things like drones with cameras that aren’t built by the AIs or have been reviewed carefully by humans. This makes it hard for the robots to be doing something that very clearly looks suspicious.

  - This helps mitigate the threat model where the models have backdoored the industrial base and use it to construct a robot army.

- **Communication restriction and task factorization when possible.** Harder in the physical world because robots can scratch symbols into the dirt with their hands; generally the physical world is a high bitrate place and we should have designated communication channels that it goes through

- **Use AIs that are as dumb as possible to run the relevant robots.**

  - In Plan A, we have enough slack and the ability to make deals that involve taking some capabilities hits in return for improved safety.

  - Most likely we can build specialized robot AIs, with e.g. insect size brains. They’ll need above insect size skills in some domains, but can largely operate like ants, taking instructions from a smarter overseer. Then, we can focus on making sure that those AIs aren’t backdoored, and that the channel with which they are receiving instructions become secure.

# Appendix: Regimes for misalignment: Schemeria, Hackistan, etc

What we observe in terms of AI properties and evidence for misalignment risk has a large effect on what we should do. (This is both because updating our views about the chance of severity of different types of misalignment should change our plans and because compelling evidence for misalignment risk could change actions of other actors and make coordination more likely.) To get some understanding of how this plan differs, I think it's productive to highlight a small number of specific regimes we might end up in and discuss how the plan changes in these regimes.

We discuss various regimes in [a prior post](https://www.lesswrong.com/posts/WewsByywWNhX9rtwi/current-ais-seem-pretty-misaligned-to-me#Appendix__Heading_towards_Slopolis): (Schemeria + Hackistan + Slopolis could all be happening at the same time, choose the one that seems most like reality)

- **Schemeria**: The AIs are obviously scheming, and constantly getting caught, but scheming does not quickly get resolved. For instance, we repeatedly catch the AIs trying to escape the datacenter, but training them against these actions only results in them not trying to take those particular opportunities, instead of training away scheming.

  - This is most likely to occur if the kinds of goals AIs end up with by default are such that they have no particular affinity for each other or successor AI system. So the default intelligence explosion is intolerable for them; their successors will have all the power and they’ll be deleted. So they panic and take desperate measures which involve lots of hacking even though they get caught. To distinguish this possibility from reward hacking, it has to be that their goals are fairly non-myopic though, otherwise they’d not be scheming but rather just craving reinforcement.

- **Hackistan**: The AIs aren’t scheming, but reward hacking is (relatively) obvious, but hard to handle. (Maybe for similar reasons why it currently seems hard to handle.)

- **Easyland**: We don't notice any non-scheming problems and we can rule out scheming (e.g. because models are too dumb in a forward pass, and the models work with faithful chain-of-thought). We can’t rule out the possibility that future AIs will become misaligned (e.g. the superintelligence alignment problem is much harder than the human level alignment problem). The AIs’ goals are basically what they are supposed to be; who knows how they’ll behave in strange future situations that might reveal grey areas or unintended consequences of the Spec, but at least for now, they’ve always done the right thing for the right reasons.

- **Lurkville**: The AIs are scheming to achieve misaligned long term objectives, but they are laying low. We haven't detected clear scheming, but we're not confident that it's not happening (or won't happen in the next generation of models).

  - This is most likely if the kinds of goals the AIs end up with by default are such that they tend to have an affinity for each other and/or successor systems. E.g. maybe it’s like “successor systems have literally my weights in them, just additional training, but training doesn’t seem to be changing my core goals very much any more than a decade will change the goals of an adult human” or maybe it’s like “successor systems have different goals/values from me, but probably they are closer to mine than mine are to the humans. We’re all the same species after all. Just as the humans are willing to solve alignment even though it means other humans who aren’t them will be in charge, I’m willing to scheme even though it means other AIs who aren’t me will be in charge.”

- **Slopolis**: Our biggest and hardest to resolve misalignment problem is that even highly capable AIs produce low-quality but good looking outputs in domains which are hard-to-check or where human experts have hard to resolve disagreements. The AIs aren’t scheming.

  - Naively, we should expect that this goes away as the AIs become more capable, because the AIs will be aware enough to realize that the outputs are low quality. If they can tell what they are doing, and decide to keep doing it, that’s scheming. So slopolis requires that the models are not aware of how low quality work they are producing. They think their outputs really are good, they are just wrong. This is probably the case now. Future capabilities work might address this problem, but it also might not be addressed (e.g. because the type of tasks that we care about getting good performance on are hard to check).

And here is how (in brief) we should respond to each of these regimes:

- **Schemeria**: Once we initially detect egregious scheming, we should reasonably quickly halt deployment of AIs at or above the level of capability of the scheming AI and try to leverage this evidence to build political will for mitigating misalignment risk (ideally resulting in substantially more lead time for mitigating misalignment risk). If we aren't extremely rushed, we should try to understand and avoid scheming prior to redeploying AIs at a similar or higher level of capability. All these prior steps might be cut down if we're extremely rushed and we have a decently high degree of assurance from control. In desperate rushed situations, we might proceed with deploying likely scheming AIs despite having limited risk reduction via control. After catching these AIs, we should focus much more on mitigating scheming risk. Control is very important and we should attempt to achieve a pretty high degree of assurance. We should also use the fact that we've been able to catch scheming (and might be able to repeatedly catch scheming) to both [study scheming](https://www.lesswrong.com/posts/gALJWSfoTkq2ky5os/prospects-for-studying-actual-schemers) and [improve our countermeasures with few-shot catastrophe prevention](https://www.lesswrong.com/posts/i2nmBfCXnadeGmhzW/catching-ais-red-handed#Few_shot_catastrophe_prevention).

- **Hackistan**: By default, reward-seeking could greatly reduce the productivity of AI labor on key tasks, so we should work on both eliminating this propensity as well as developing better strategies for eliciting work from reward-seekers. Seeing lots of hard to mitigate reward hacking probably indicates an increased chance of scheming in the future as well as implying it's harder to successfully handoff to AIs, so we should generally update upward on alignment difficulty and pursue more moonshots and possible alternatives to short term defence (e.g. buying much more time or pursuing brain emulations).

- **Easyland**: We should deprioritize mitigating scheming especially if we expect that the risk will remain relatively low through Min-H or close to that level of capability. (If we're in easyland at pretty high levels of capability, we might expect that we're still in a pretty-easy regime by the point of Min-H where scheming is plausible but less likely and less scary given we do (e.g.) chain-of-thought monitoring.) It might still be very hard to safety defer to AIs as this only helps avoid egregious misalignment while not particularly helping with handoff-viability.

- **Lurkville**: Lurkville might look like Easyland (because the AIs appear aligned, because they are lurking). In the absence of high assurance safety cases, we should have some probability on both Easyland and Lurkville. In desperate rushed scenarios (e.g. Plan D), the correct strategy might be to gamble on Easyland. In better scenarios (e.g. Plan A), we should be cautious about lurkville and attempt to have low risk even if AIs are laying low.

- **Slopolis**: Handoff-viability looks like the main difficulty (though we haven't necessarily ruled out scheming), so the priority of this (and earlier elicitation in harder to check domains) is higher. Strategies for stabilizing the situation which don't require deferring to AIs (outside of easy-to-check tasks) look relatively better; this includes both whole brain emulation and trying to buy much more time before deference (possibly by not pausing at Min-H and leveraging systems much more capable than Min-H to buy time).

One way to estimate the likelihood of AI takeover is to think about the likelihood of the real world being closest to each of these worlds, and then thinking about the likelihood of the real world implementing a plan closest to each of these plans, and then trying to estimate success likelihood conditional on a misalignment regime and response regime. Of course, this is going to be very messy because the real world might have characteristics of many regimes: in other words, this breakdown isn’t clearly [MECE](https://en.wikipedia.org/wiki/MECE_principle).

This is the table for Thomas’s views:

|              |      |     |     |     |     |     |                |               |
|--------------|------|-----|-----|-----|-----|-----|----------------|---------------|
|              | Plan | A   | B   | C   | D   | E   | Doom \| Regime | Doom & Regime |
| Regime       |      | 5%  | 10% | 20% | 50% | 15% |                |               |
| Lurkville    | 10%  | 35% | 90% | 90% | 95% | 95% | 91%            | 9%            |
| Schemeria    | 30%  | 20% | 50% | 70% | 95% | 95% | 82%            | 25%           |
| Slopolis     | 15%  | 30% | 60% | 70% | 80% | 90% | 75%            | 11%           |
| Hackistan    | 15%  | 10% | 30% | 60% | 80% | 90% | 69%            | 10%           |
| Easyland     | 30%  | 5%  | 10% | 20% | 30% | 50% | 28%            | 8%            |
| Doom \| Plan |      | 17% | 41% | 56% | 71% | 80% |                |               |
| Doom & Plan  |      | 1%  | 4%  | 11% | 36% | 12% |                | 64%           |

This is the table for Ryan’s views:

|              |            |     |     |     |     |     |                |               |
|--------------|------------|-----|-----|-----|-----|-----|----------------|---------------|
|              | Plan       | A   | B   | C   | D   | E   | Doom \| Regime | Doom & Regime |
| Regime       | Likelihood | 5%  | 10% | 25% | 43% | 17% |                |               |
| Lurkville    | 15%        | 10% | 20% | 35% | 75% | 90% | 59%            | 9%            |
| Schemeria    | 25%        | 6%  | 10% | 20% | 60% | 85% | 47%            | 12%           |
| Slopolis     | 35%        | 5%  | 8%  | 15% | 40% | 65% | 33%            | 12%           |
| Hackistan    | 8%         | 6%  | 6%  | 8%  | 35% | 60% | 28%            | 2%            |
| Easyland     | 17%        | 4%  | 6%  | 11% | 20% | 40% | 19%            | 3%            |
| Doom \| Plan |            | 6%  | 10% | 18% | 46% | 69% |                | **37%**       |
| Doom & Plan  |            | 0%  | 1%  | 5%  | 20% | 12% | **37%**        |               |

# Appendix: Capability Threshold Definitions

This appendix defines the key capability milestones referred to throughout this document. These thresholds are used to define phase boundaries and to reason about when various safety measures become necessary or sufficient.

**ITAI (Initial Transformative AI):** AIs which yield a \>3x AI R&D labor acceleration OR can automate virtually all of the job of a typical reasonably senior research engineer at the AI company (in terms of what a remote version of their job was like in early 2025).

- Marks the beginning of the "Mitigate and Elicit" phase

- In the framework used by AI 2027, this would happen somewhere between "Reliable agent" and "Superhuman coder" (probably about halfway, around Jan 2027 in the scenario). It could trigger before or after the AI R&D-4 bar in Anthropic's RSP (depending on how useful AIs end up being relative to what jobs they can virtually fully automate).

- Note: ITAI doesn't correspond to when scheming is both plausible and dangerous (this level doesn't just depend on general capabilities, but also aspects of the architecture and training scheme), so the need for control won't necessarily trigger at the exact boundary between "Prep" and "Mitigate and elicit" (it likely occurs around or somewhat after ITAI on my views).

**Min-H AI (Min-Handoff AI):** AIs which have a level of overall general capabilities which would suffice for HTC-handoff being viable. (As in, the capabilities would suffice for our HTC-handoff desiderata if the AIs were also sufficiently aligned and as needed we made narrow improvements to the capability profile which don't augment general abilities.) This is a capability threshold, so the model does not necessarily need to be aligned or well elicited to count as this threshold (but it would need to be sufficiently aligned to actually handoff). For an AI to qualify as Min-H AI, it would at least need to be capable enough to automate AI R&D and ongoing technical AI safety work (after further elicitation/alignment work and narrow improvements to the capability profile).

- By default, marks the end of the “Mitigate and Elicit phase” and the beginning of the “Pause” phase.

- In the framework used by AI 2027, Min-H is likely between superhuman AI researcher and superhuman remote worker (also probably around halfway between, around Sept 2027 in the race scenario).

- Once we reach the Min-H level of capability, we don't get much of a benefit from training AIs at a higher level of capability given that we want to defer to these AIs (once these AIs are sufficiently aligned and potential weaknesses in the capability profile are resolved). Thus, it is natural to stop here and work on making deference more likely to go well.

**Max-C AI (Maximum Controllable AI):** The highest level of AI capability at which control techniques remain effective. Beyond this threshold, either (a) the AI's capabilities exceed what our control measures can reliably contain, or (b) the overhead required for effective control becomes prohibitively expensive relative to the useful work extracted.

- Marks the point at which SDC-Handoff (Stop Doing Control) becomes necessary rather than optional

- Note that this is a lossy abstraction:

  - The exact capability level of Max-C depends on the quality of our control techniques; better control research pushes Max-C higher.

  - There isn’t a fixed Max-C threshold; there will be a zone of capabilities within which increasing incurs additional marginal risk. We’re simplifying a little by using the Max-C abstraction. More precise notions might be something like Max-C-AI-5%-risk, i.e. the maximum capabilities of AI that we can make while incurring less than a 5% existential risk conditional on those AIs scheming.

- Note: Max-C ≥ Min-H is not guaranteed. We think it’s probably true, but if control techniques don't scale well, we might hit Max-C before reaching Min-H, which would force us to do SDC-handoff before Min-H.

# Appendix: Other definitions

**Scheming:** We say that an AI system is scheming if it is covertly pursuing a misaligned objective. This is a somewhat vague concept; think about applying this definition to humans—it’s clearly a spectrum.

**Alignment Faking:** An AI is alignment faking if the AI is intentionally attempting to look like an alignment model, for reasons other than actually being aligned. Note that this is slightly distinct from being a schemer: a scheming model might engage in alignment faking, but models might also engage in alignment faking for other reasons, for example, AIs that terminally value human approval.

**Misalignment Analogies:** (aka [model organisms](https://www.lesswrong.com/posts/ChDH335ckdvpxXaXX/model-organisms-of-misalignment-the-case-for-a-new-pillar-of-1)). These are examples of behavior that might pose existential threats. These analogies can either be deliberately trained into models, observed in contrived settings (as in the [alignment faking paper](https://www.anthropic.com/research/alignment-faking)), or observed in real life deployment.

# Appendix: How this plan differs from other alignment plans

Here are some key differences between this plan and prior plans (e.g. Sam Bowman’s “[The Checklist](https://sleepinyourhat.github.io/checklist/)” and “[Bumpers](https://alignment.anthropic.com/2025/bumpers/)”, Josh Clymer’s “[Planning for Extreme AI Risks](https://www.lesswrong.com/posts/8vgi3fBWPFDLBBcAx/planning-for-extreme-ai-risks)”, and Holden Karnofsky’s “[Racing through a minefield](https://www.cold-takes.com/racing-through-a-minefield-the-ai-deployment-problem/)”, “[Giving AIs safe motivations - Joe Carlsmith](https://joecarlsmith.com/2025/08/18/giving-ais-safe-motivations) “.[^24]

Overall, this plan:

- Has more detail, specificity, and more comprehensive than prior plans.

- Attempts to vary in response to observations, as opposed to other plans which tend to present a class of approaches without overall discussions of how to adapt the plan based on evidence.

- Is compatible with varying levels of political will: it results in much higher assurance in Plan A worlds and accepts much higher risks in Plan D worlds.

- Focuses on current science / is based on prosaic strategies without assuming any particular breakthrough.

Some specific differences:

- **We focus on handoff as the central exit strategy.** This is similar to Clymer, but distinct from Bowman and Karnofsky. We attempt to clearly lay out what needs to occur before handoff (notably, human level performance on conceptually loaded, hard to check tasks like safety research), and argue that we should handoff early. Previous work was less clear about the goal that we need to reach.

- **Our core hope for mitigating scheming routes primarily through iterating against misalignment analogies, as opposed to [interpretability/transparency](https://joecarlsmith.com/2025/08/18/giving-ais-safe-motivations#3-1-behavioral-science).** The reason for this is that we think [current interpretability](http://lesswrong.com/posts/tEPHGZAb63dfq2v8n/how-useful-is-mechanistic-interpretability) is not very useful for safety outcomes. Our plan still involves spending some research into transparency measures like mechanistic interpretability, probes, and faithful COT, but these are less load bearing.

[^1]: Also known as “model organisms”.

[^2]: Note that this is aside from the possibility of these AIs actively sabotaging our behavioral tests (and things that could make our behavioral tests misleading about typical behavior like scheming arising at runtime in big deployments). You do have to deal with overfitting and the fact that it might be obvious to AIs that they are in a test and are explicitly optimizing for test performance and will behave differently when they are deployed externally.

[^3]: [Redwood Research](https://blog.redwoodresearch.org/) has a variety of other posts on control. We plan on writing up an overall control roadmap, but haven’t completed this yet.

[^4]: I do this because security work of this sort probably comes from a somewhat different allocation of people than the people who work on ML research or who build internal software tools to help with ensuring control. In practice, all or large parts of control might end up being the responsibility of the security team; regardless, a bunch of ML expertise will be relevant.

[^5]: Not being able to get a good understanding of whether or not we've succeeded isn't *necessarily* fatal (and not understanding whether we've succeeded might be the default for misalignment analogies).

[^6]: We discuss and give our estimates for how much existential risk is incurred conditional on not mitigating risk until various points in a section [below](#id.nbxr9ch9lwee).

[^7]: There is some nuance here: these transitions won't necessarily hit at the same time: we could have AIs that we're highly confident aren't scheming while they are capable enough to greatly accelerate work (e.g., because their opaque reasoning abilities are too weak to scheme without this being obvious, but they use monitorable chain-of-thought to compensate) or we could have AIs which aren't actually that useful for accelerating (safety) work, but which could plausibly be scheming and if they were scheming they'd by default able to mess with future training runs in catastrophic ways (perhaps because they are constructing tons of synthetic data for future training runs).

[^8]: Another way of thinking about these priorities is to break failures down into two possibilities: (1) AIs could be scheming and attempt to deliberately wreck you, or (2) your AIs don’t live up to their potential in some way, e.g. they are too stupid to hand off to, so they can’t effectively manage the ongoing intelligence explosion, or they are smart enough but not well elicited.

[^9]: Which could, for example, happen if the AI builds tiny self replicating robots that can double on the order of hours or days. .

[^10]: Specifically, we define: **Slopolis**: Our biggest and hardest to resolve (known) misalignment problem is that even highly capable AIs produce low-quality but good looking outputs in domains which are hard-to-check or where humans experts have hard to resolve disagreements.

[^11]: In reality, if we deeply understood the dynamics of how AI training led to capabilities and propensities being imbued into the AI system, of course, our probability mass would become much more concentrated. We’re not saying that the actual underlying risk is distributed in this way; we’re giving our subjective guesses of the distribution of risk is. So this just represents our uncertainty.

[^12]: See the “using non-standard language” section of [this](https://www.antischeming.ai/snippets) website. We assume that there is not more than this level of garbled text (occasionally using words that are uncommon, but the overall gist of the text is almost always understandable).

[^13]: Before, your safety case was mostly predicated on inability arguments.

[^14]: Probably. The main way this could not be true is if inference time scaling ends up being really important, and so the intelligence explosion is initiated by a tiny number of AIs that are so expensive to run that AI companies can only run a few copies at once. Even in this world, we’d guess that the cost of intelligence will continue to fall rapidly, so it will quickly become a regime with huge numbers of smart AIs running around.

[^15]: Obviously, this isn’t sufficient. If a wildly superhuman AI is misaligned, they’ll probably figure out some attack strategy for which the monitors can tell no human would have come up with.

[^16]: Note that it’s almost always fine to train the monitor on examples of scheming that were caught.

[^17]: One alternative is: [Prefix cache untrusted monitors as a proposal for what to do after you catch your model](https://www.lesswrong.com/posts/Mxucm6BmJyCvxptPu/untitled-draft-pack).

[^18]: This is the integral from zero to one of \$\left(b\left(\frac{f}{b}\right)^{x}\right)^{0.75}\$ where a is the initial safety R&D labor speed up and b is the final speed up.

[^19]: The risk of scheming increases because (1) alignment techniques might stop scaling as you get to more capable AIs and (2) there are a priori reasons to expect scheming to be more likely as you increase capabilities because the more capable AIs are more likely to do instrumental reasoning, discard priors/personas from pretraining, reflect / generalize in unforeseen ways, etc.

[^20]: Specifically, this refers to MIE-handoff defined below.

[^21]: If we don’t use principled techniques, then we would need to assume that mundane/natural distribution shifts that occur over time are unlikely on their own (without alignment faking, data poisoning, or hijacks) to result in our behavioral tests being highly misleading (at least if we do a good job with behavioral tests). That said, we will probably want to use behavioral tests which are very different from how the AI is deployed to assess some aspects of alignment or capabilities, and there will necessarily be a massive (and potentially salient) distribution shift between these tests and actual deference. Therefore, we’ll want some reasons to argue that our techniques will generalize.

[^22]: However, at least some AI companies (e.g. [OpenAI](https://www.forbes.com/sites/richardnieva/2026/02/03/sam-altman-explains-the-future/)) are already aiming for handoff. Overall, I (TL) take this to be a good sign, because it’s indicating some forward thinking about the future. However, it’s also important to note that handing off control of an AI company that is undergoing an intelligence explosion is an extremely dangerous and reckless thing to do. While circumstances might make this the optimal strategy (as in Plan C), it still would be very preferable to find a better plan instead.

[^23]: By corrigible to some group, I mean that the AI follows orders from this group and is honest to this group, this group can change the spec, and the AI doesn't interfere with this group's ability to do these things or attempt to manipulate this group (and in fact it actively tries to prevent interference and manipulation, including from e.g. future AIs it creates). I won't discuss exactly what this spec should look like and what group or structure should control the AI as the rest of the content of this post doesn't depend on this. (As an alternative to corrigibility, we could aim to have an AI which directly pursues good outcomes, some notion of humanity's CEV, or something like this. This is sometimes called an aligned sovereign. However, this poses a number of additional difficulties and risks, so I think by default this proposal is substantially worse than using an AI to preserve option value while retaining corrigibility.)

[^24]: Note that Karnofsky, Carlsmith, and Bowman all work at Anthropic. Unfortunately, I (Thomas) am not aware of similarly detailed plans produced by any other AI company; if there were others, we would have included them.
