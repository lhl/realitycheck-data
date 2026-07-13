---
title: "Verification Plan"
byline: "Romeo Dean"
source_url: "https://ai-2040.com/supplements/verification-plan"
retrieved_at: "2026-07-11T06:00:49+00:00"
conversion: "rendered HTML to GitHub-Flavored Markdown with Pandoc"
---

# Verification Plan

**Byline:** Romeo Dean

Plan A is predicated on the ability to enforce an international deal to slow down AI progress without relying on trust. We are confident that verification measures can make this possible,[^1] by providing sufficient assurance to both the US and China that defection by the other would either be caught or small enough to be inconsequential.[^2]

There is a spectrum of how costly and how trustworthy our best verification solutions are, which we can think of as a verification frontier. Today, the verification frontier is not mature. Currently the only way of verifying an AI development pause with extremely high assurance between the US and China would probably require datacenters to be powered down,[^3] and anything less costly than this might have significant risk of being violated.[^4] That being said, we believe the verification problem is inherently defense dominant,[^5] and AI verification is also an extremely young and so far [tiny field](https://nacicankaya.substack.com/p/all-hands-on-deck-to-build-the-datacenter), so it should be highly tractable to make significant progress in the next few years.

This supplement provides a summary of the verification plan that we think should be followed to make Plan A viable, and then is followed by a more detailed walkthrough of how the verification story unfolds in our specific Plan A scenario.

**Want to help build this?** See the [Get Involved](verification-plan/get-involved.md) tab: what needs to be done, who the field needs, an [expression of interest form](https://tally.so/r/LZyyDy), and open opportunities across the verification field.

1.  **[Summary of the Plan](verification-plan.md#summary-of-the-plan)**

    1.  [Prepare deal optionality](verification-plan.md#phase-1-prepare-deal-optionality)

    2.  [Implement the deal](verification-plan.md#phase-2-implement-the-deal)

    3.  [Improve robustness](verification-plan.md#phase-3-improve-robustness)

2.  **[Verifying the deal in our Plan A scenario](verification-plan.md#verifying-the-deal-in-our-plan-a-scenario)**

<!-- -->

1.  **[Appendix:](verification-plan.md#appendix-packet-based-verification) [Packet-Based Verification](verification-plan.md#appendix-packet-based-verification)**

# Summary of the Plan

We recommend an international deal to avoid a catastrophic race to superintelligence, spearheaded by the US and China. This deal needs to be enforceable without relying on trust, because the US and China will be unlikely to make an agreement that cannot be verified; and they are much less likely to defect on the agreement if any defection is likely to be caught.

We can break up the verification problem into two key components:

1.  **Problem 1. Verifying that known compute is compliant.**

    1.  We are confident that it is possible to have verification measures that enable a trustless deal. That being said, if a deal needed to happen tomorrow, we would not be ready to enforce it trustlessly in a low-cost way.[^6] Given the increasingly large economic incentive to keep AI services online, a ready-to-go verification solution (that doesn’t require much time to activate) may be incredibly important for making a deal happen.

2.  **Problem 2. Verifying that unknown compute is inconsequential.**

    1.  Our [covert project supplement](covert-ai-projects.md) estimates that even a competently-executed covert diversion effort would net a median of about 0.5% of the world’s AI-relevant compute (80% CI: 0.1% to 1.4%) as ‘dark compute’ at the start of the deal,[^7] which given the likelihood of compute-dependence of frontier progress, should buy the deal a lot of time and stability.[^8] This bound should also tighten as the deal goes on, as detection efforts accumulate and more compute is brought under verification.

Our recommended solutions come in three phases.

**Phase 1. Prepare Deal Optionality.** The US and China take actions to make a deal more likely to be enforceable and durable, by preparing the ability to do inference-only verification, and keeping close tabs on how much AI compute exists and who owns it.

**Phase 2. Implement a Deal.** The US and China perform a mutual compute declaration (spreading to third countries and ideally reaching \>99% of world compute); inference-only verification retrofit to ~99% of world AI datacenter compute, and then sprint towards setting up secure R&D verification that will use new post-deal compute production.

This is what we think implementing the deal would look like in 2029 in our scenario, with an inference-only retrofit of all the medium and large AI datacenters (\>10K H100e, or approx. \>\$100M), and this being enough to cover ~99% of world AI-relevant compute. Then keeping tabs on the rest of the smaller clusters and taking measures to avoid them being possibly used in a covert project. We are not confident in the modelling of this [concentration in datacenter sizes](compute-supplement.md#14-datacenter-sizes), so the exact cutoffs and interventions may need to be different.

Compute locations by datacenter size (Jan 1 2029) - ai-2040.com

**Phase 3. Improve robustness.** Over time the US and China improve the stability and durability of the verification regime, especially through hardware security, verification robustness, and more.

## Phase 1. Prepare Deal Optionality

We recommend focusing pre-deal effort on sprinting towards a minimal verification package that can be used to securely retrofit 99% of the world's AI compute to be verified as inference-only, and for at least 99% of the world's AI compute to be known-to-exist (at least to intelligence agencies) with low uncertainty, so that it can’t be hidden from a future compute declaration (and therefore verification regime) with plausible deniability.[^9]

Why do we recommend this?

If the year is 2029, and there is no verification progress relative to today, our best guess is that frontier AI services would need to mostly (e.g., 90%) stay offline for 6-12 months in the wake of a deal if both sides wanted to be highly confident there wasn’t fast frontier AI development continuing. If there were a minimum-viable inference-only retrofitting solution prepared, the equivalent period would be more like 2-5 months. The difference between these in terms of economic impact might be in the trillions of dollars by 2029. Of course, it would be even better if there was a more general verification solution ready, that could e.g., also allow approved training and experiments to continue, but we think this is likely to be harder, and only provide a marginal gain on top of an inference-only solution, because most of the economic upside can be retained by only keeping inference online (since training and experiments will be intentionally limited under a slowdown deal anyway, especially at first while negotiations on how to proceed with AI development are negotiated).

Even with such a verification solution ready, the maximum verification coverage of a deal is still bounded by the percentage of the world's compute that can be brought under the deal. If the US, China, or any other actor has plausible deniability on how much compute they have, they can use that plausible deniability to hide compute from the deal, and use it as unverified compute in a covert project. But if the total unknown compute is under 1% of world compute, we think any such covert effort is likely to be inconsequential: our [covert project supplement](covert-ai-projects.md#section-6-overall-risk-estimate) models this directly, and estimates roughly a 13% chance that a competently-pursued covert project reaches deal-undermining AI before detection or handoff, under our recommended scaling strategy. These estimates apply to the start of the deal: as the deal goes on, the uncertainty should narrow and the plausible covert stock should shrink, as tracing and audits converge, detection efforts accumulate (see the [detection estimates](covert-ai-projects.md#section-3-detecting-covert-ai-infrastructure) in the covert project supplement), and more compute is brought under verification. Of course, the lower the unknown compute is, the better but we think around 1% of world compute is likely to be an achievable target and sufficient for a stable deal.

**Top priority recommendations:**

1.  **Invest in verification R&D with a specific focus on developing a secure inference-only retrofitting plan with around 80% of total verification R&D effort.**

    1.  Also, support supplementary R&D efforts with around 20% of verification R&D effort pursuing promising additional measures, such as software-only solutions, privacy-preserving verification measures, and more general verification solutions (e.g., that verify the compliance of training and experiments as well).

2.  **Invest in compute accounting and tracking (e.g., carried out by intelligence agencies) to know how much AI relevant compute exists in the world, and which entities are in possession of it.**

    1.  Notably, our recommendation for this early chip tracking doesn’t prioritize knowing where this compute is, or what it is being used for. We believe that the majority of the upside in terms of making a deal viable is simply in knowing how much exists and keeping track of which actors own it at any given time, because the lack of plausible deniability should be sufficient to force this compute to be declared at the time of deal negotiation (given that there will be large incentives in favour of joining a deal). That being said, also knowing its location is helpful in avoiding cases of plausible deniability (e.g., faked records of on-selling or chip deaths) and cases where (for some reason) the US and Chinese governments have little leverage over the owning entity (and therefore can’t pressure them to declare the location of the compute they are known to have, e.g., Russian compute).

## Phase 2. Implement the deal

To set up a stable deal, we recommend immediately carrying out a mutual compute declaration and supply chain records audit to maximize the amount of compute that is brought under the deal. Then implementing the best available inference-only verification solution to this compute to enforce a brief pause on training and experiments. In parallel, we recommend a sprint to set up a verification regime for resumed training and experiments.

Why do we recommend this?

Given that unknown compute can’t be brought under the verification of a deal, the first priority should be to minimize the amount of compute that is unknown. The urgent action needed for this is to immediately carry out a declaration of existing compute and compute currently in transit or production. Both the US and China should then be able to carry out an audit and inspection of each other’s declaration, and compare it against their private intelligence efforts (to the extent they properly prepared this) to resolve their uncertainties over how much compute each other have.

Around 85% of global compute should be owned by US or Chinese entities, so aiming for 99% of compute being under the deal will require rolling out such a declaration agreement to the other 5-10 nations that will likely make up the rest of this gap. The level of urgency of extending this to other nations will depend on the uncertainty intelligence agencies have over how much compute these other nations have, how likely it seems that these other nations would successfully be able to hide significant quantities of it without detection.

Following this declaration, we recommend a brief AI R&D pause (i.e., new training runs and experiments), with existing compute being converted to inference-only. As explained above, we think this achieves the goal of a deal (slowdown in AI progress) while keeping most of the economic upside (AI services and products keep running), while also being relatively easier to verify. Whatever the best inference-only verification solution that is ready should be used. We currently recommend aiming for a network-tap and recomputation based approach, but more R&D is needed to figure out if another approach will be better. It’s also possible that only an inferior solution will be ready, but still sufficient to be used in the initial setup of a deal until something better is ready.

Finally, we recommend setting up the verification regime for resuming training and experiments as a separate effort that happens after the deal begins because we think there are important properties of R&D verification to decide on once the deal is setup, and also extremely high security requirements needed for the R&D verification to enable a stable deal going forward. In particular, there is a decision to make about what level of transparency to aim for (we recommend a ‘Total Research Transparency’ regime, but more on the possibilities to decide between in our [transparency supplement](transparency-plan.md)), and in any case there are high security requirements, so we believe that the verified datacenters will need to be built from scratch. If new construction is deemed to take unacceptably long, or there is a sufficiently secure retrofitting solution for R&D verification, then there could be an interim period where pre-existing datacenters are used for R&D. That being said, we think after around 2 years, when verification and security requirements are elevated, and something like 90% of the world’s compute will be new post-deal compute anyway, we recommend more strongly having new, post-deal, highly secure datacenters.

**Top priority recommendations:**

1.  **Carry out a bilateral compute declaration and supply chain audit, for both existing compute and new compute production, and extend to third nations with significant compute ownership or production.**

    1.  Every major datacenter owner and companies with a major role in the supply chain publicly declare their records about purchases and sales, and allow auditors and inspectors into each other’s countries and companies to verify the records and count of final chips. This needs to also including compute in transit and active compute production. From this point forward, existing compute and new compute production is closely tracked and guarded so that it can’t be redirected to a covert project without detection. Extend this declaration to other countries with significant compute ownership or production capacity. Do so urgently unless there is confident intelligence in place that would detect this compute being moved.

2.  **Implement inference-only verification on existing compute and any new compute coming online.**

    1.  Roll out inference-only verification to existing compute to enforce the brief AI R&D pause while allowing AI services to remain online. Ideally there would be a highly secure solution ready to go. If not, implement the best solution available. If there is no solution at all ready then either shut down the compute, or rely only on non-technical measures (e.g., embedded auditors in each other’s companies checking that no one is implementing experiments or training runs) in the meantime while sprinting to transition to a better solution.

3.  **Sprint to set up R&D verification in accordance with the chosen transparency regime.**

    1.  We recommend a specific regime we call Total Research Transparency in the Plan A scenario, but as explained in our [transparency supplement](transparency-plan.md), there are conditions under which a different approach may be better. Regardless of the regime, there should be some combination of highly secure R&D clusters and highly secure post-deal inference clusters built, because across most transparency regimes we imagine at least AI model weights and verification correctness requiring [SL5](https://www.rand.org/pubs/research_reports/RRA2849-1.html) (robust to nation state actors) level security. Because of this we think these clusters should be built from scratch.

What AI R&D agreements should actually be verified?

The primary purpose of the deal is to create the conditions that can allow for slowing down AI development in order to increase safety, by paying safety taxes in safety resource allocation (e.g., doing alignment research instead of capabilities research) or development directions (e.g., agreeing to not pursue a certain research direction or use a certain efficient algorithm that might be less safe). Overall, we refer to this safety focused slow down on AI research as ‘AI research titration’. The method of AI research titration may be crude at first (e.g., harsh experiment compute caps) and become more sophisticated over time (e.g., case by case decisions informed by scientific understanding of capabilities externalities).

We additionally think that a deal may have to deal with potentially destabilizing levels of hardware research, and hardware production levels. In the Plan A scenario we recommend hardware research titration and a cap & trade policy on robots and compute production to deal with the risks from these sources. All of this is explored in more detail in the [Plan A verification story](verification-plan.md#verifying-the-deal-in-our-plan-a-scenario).

## Phase 3. Improve Robustness

Once a deal has been set up, we expect many improvements to its robustness will be possible. We recommend investing heavily in hardware security; improving the verification regime; pursuing favorable trade-offs in hardware design that favor deal robustness (e.g., by making verification easier, improving various security properties, differentially favoring the actors in the deal over covert projects, etc.); and reducing incentives to pull out of the deal (e.g., through mutually assured compute destruction, and balancing deal dissolution outcomes between actors).

Why do we recommend this?

We expect there to be many achievable improvements to the robustness of the deal. Given that the deal breaking down is one of the biggest threats to Plan A succeeding, as explored in our [deal decline supplement](deal-decline.md), reducing the incentive to pull out of the deal is a core part of improving the deal’s stability. Covertly defecting from the deal is another core threat to the deal (as explored in our [covert project supplement](covert-ai-projects.md)), so another core part of improving the deal’s robustness is making the verification regime better, both on the level of assurance of known compute and reducing the amount of unknown compute; improving various other security properties, like model weights security; and more generally making it harder for potential defecting actors to make or steal progress.

Concrete ideas for deal robustness

**Deal dissolution contingencies and incentive shaping.Mutually assured compute destruction.**One of our main proposals for how to disincentivize actors from pulling out of the deal, and make AI development safer if actors do pull out of the deal, is to set up mutual ability to destroy the post-deal compute.If this is strongly in place, then no actor will sanely attempt to pull out of the deal and gain a lasting advantage by defending some of the compute, and returning to racing. If the deal does break down despite this, then compute destruction can let any actor destroy the post-deal compute, which makes things potentially vastly safer because it destroys the large compute overhang, which back in a default world with actors racing might be extremely dangerous because it would make AI progress extremely fast.**Cold storage compute banks.**Another possibility would be to decrease the incentive for actors to pull out of the deal is to have a small compute bank that is verified to not be in use during the deal, but which each side can reliably defend and bring back online if the deal does break down.If this is reliably bigger than any potential covert project, then it removes the incentive to pull out of the deal for any actor that may have the largest covert project, also reducing the incentive to attempt one in the first place.[^10] In our scenario, the US maintains a 5M H100e bank and China a 500K H100e bank (see our [deal decline supplement](deal-decline.md#preparing-stockpiles-to-align-incentives), the source of truth for these stockpiles); the US bank sits comfortably above the ~4M H100e top of the 80% CI for plausible diversion in our [covert project supplement](covert-ai-projects.md#section-2-preventing-covert-compute-procurement). The ratio between the size of the US and China’s compute banks (and whichever third parties might negotiate their own) could be frozen at the pre-deal status quo compute ratio.**Cold storage model weights and data bank.**Another idea we have to improve the situation if the deal breaks down is to allow the US and China to agree to submit models to a hardened cold storage model weights bank.Both sides would need to verify that the other side’s weights are not going anywhere else, but not have the ability to destroy them if the deal broke down. The reason they may want to do this is if they have made a lot of alignment progress in the form of a final trained model or large datasets, and they mutually agree it would be safer for the world in the event of deal break down if they were allowed to have these model weights and/or datasets.**Improving the verification assurance on the compute in the deal.Hardware security.**There may be several hardware security properties that can be drastically improved under the deal, especially by applying AI research automation help differentially in these areas, and paying hardware ‘security taxes’ in the design choices. These could include software level security improvements, such as expanded formal verification, and hardware security improvements, making tampering extremely difficult. One step towards achieving this could be to increase the monitoring and security at fabs and other parts of the supply chain. Another nice property that could also help with mutually assured compute destruction (purely through cryptography) could be [offline licensing](https://www.rand.org/content/dam/rand/pubs/working_papers/WRA3000/WRA3056-1/RAND_WRA3056-1.pdf). Also, it might be possible to build computing clusters that keep model weights encrypted inside secure parts of the AI clusters using hardware-derived keys that are unobservable from the outside. If this could be made robust enough, then it might drastically help with the security of model weights and allow other SL5 model weights measures (bandwidth limiting) to be relaxed.**Verification granularity.**Another more specific area for hardware improvements is to help with verification robustness, such as extremely high fidelity reproducibility, support for increasingly granular logging, and other more specific solutions like [fixed set](https://www.rand.org/content/dam/rand/pubs/working_papers/WRA3000/WRA3056-1/RAND_WRA3056-1.pdf) hardware designs (e.g., [hardcoded weights](https://taalas.com/the-path-to-ubiquitous-ai/) might be a nice way to upgrade the inference-only verification).**Reducing compute that could be used for a covert project.Track down potential covert projects.**Over time we think it may be plausible to rule out covert projects above smaller and smaller sizes, using intelligence efforts, agreements to bring more known compute (e.g., military-exempt compute or tiny private clusters) under privacy-preserving verification measures, or agreements to do power usage accounting (e.g., mutual declaration and random inspection). Our [covert project supplement](covert-ai-projects.md#section-3-detecting-covert-ai-infrastructure) covers the detection methods (waste heat tracking, other IMINT/MASINT, SIGINT, HUMINT) and estimates detection probabilities by covert datacenter size, along with the [stronger verification concessions](covert-ai-projects.md#section-71-options-for-responding-to-covert-projects) that could be negotiated over time.**Make sure no new compute goes to covert projects.**One extremely important property of the deal is that none of the post-deal compute production can go to covert projects. Our [covert project supplement](covert-ai-projects.md#section-2-preventing-covert-compute-procurement) estimates that because production runs through a small number of highly controlled fabs, diversion of new chips can be kept to approximately zero, with very high confidence that the total is under 100K H100e. To make this even more robust, it might be favourable to concentrate AI chip production in fewer locations and/or colocate production with the final destinations (datacenters), which is doable because with total production increasing 3x/yr, every 2 years 90% of the fabs are new fabs. This means they can pretty easily be somewhere else. Consumer compute could be produced elsewhere but the risk of covert project usage of consumer compute should be separately mitigated.**Limit consumer compute that could be used in covert projects.**Consumer compute will likely include some AI-relevant compute by 2029 (e.g., hobbyists with powerful gaming GPUs, self-driving car chips), and mostly non-AI relevant chips with low effectiveness in AI workloads but which are nonetheless very numerous.[^11] This should be tested more precisely at the time for its usefulness in frontier AI workloads. If its usefulness is found to be high, then it needs to be avoided that large quantities of consumer compute could be rounded up and used in a covert project. Surveillance (i.e., reporting requirements and spot checks) should be an extreme last resort, instead there could be a voluntary buy back program, and a cap & trade on the total production of new unverified consumer compute. Ideally, this would lead to innovation about doing ‘edge verification’ (e.g., robust fixed set hardware mechanisms), to avoid the permit costs.[^12] The cap can be set such that trivially noticeable shares of the consumer compute would need to be diverted to noticeably accelerate a covert project.**Favorable directions that differentially help the deal over potential covert projects.AI scaling tradeoffs.**One of the core recommendations we make in Plan A is that to the extent capabilities progress is made intentionally, it should be done by scaling hardware (i.e., model size, training compute, data, etc.) rather than software (algorithmic efficiency) where possible, because the latter is harder (and less desirable) to govern (i.e., keep secure from potential covert projects). There are probably ways to push this idea very far as the deal goes on, by pushing to extremely large AI models that would be very difficult to steal, and even if they did would be extremely difficult for a covert project to even run at all on pre-deal compute. Our [covert project supplement](covert-ai-projects.md#section-4-limiting-consortium-uplift-to-covert-projects) estimates that a median of around two thirds of Consortium software progress leaks to covert projects, and quantifies how hardware-leaning scaling strategies reduce [covert project risk](covert-ai-projects.md#section-6-overall-risk-estimate).**Hardware-software co-design.**If it proves technically possible, transition to new AI algorithms that run poorly on pre-deal compute but well on newly designed and manufactured post-deal compute. For instance, introduce new model architectures and number formats different from those for which pre-deal compute was optimized. This way, covert projects cannot easily steal algorithms from the Consortium and run them on mostly pre-deal dark compute.

# Verifying the deal in our Plan A scenario

In our Plan A scenario, we follow the high level verification plan sketched out in the previous section. This part of the verification supplement will walk through the implementation and verification story with more concrete detail. Because it is a scenario about the future, in a very young field with ongoing R&D, we are not confident in the specific details. That being said, we hope to establish a useful concrete baseline for how the verification plan we sketched out above could actually be implemented.

## 2026-2028: Preparing deal optionality

### 2026: Chip tracking begins

The intelligence agencies in the US begin internally keeping tabs on AI compute smuggling into China, and their domestic production levels, reaching a 10% uncertainty over how much AI compute Chinese entities own in total by the end of the year. They don’t do anything with this information yet (i.e., they don’t share smuggling information with the BIS). China learns that the US intelligence community is doing this, and begins doing it as well by leveraging existing assets mostly out of TSMC in Taiwan to get accurate counts and records of total production. They reach 10% uncertainty on US total AI compute, mostly due to uncertainty over pre-existing compute and production outside of Taiwan (e.g., South Korea and the US). Uncertainty over new compute production is much lower (on the order of 1%).

### 2027: Verification R&D gets funding

The US executive branch starts expressing interest in deal optionality and verification measures that could enable this. After a series of [RFIs](https://en.wikipedia.org/wiki/Request_for_information) they choose to focus efforts on a network-tap and recomputation centered approach for an inference-only retrofitting solution. The prospect of installing devices in each other’s datacenters raises initial alarm bells but it's a tractable security problem to work on. Ultimately due to the sheer simplicity of some of the possible network tap designs (essentially a piece of glass splitting optical signals), and parallel investment into various physical security agendas, it becomes a palpable possibility that these taps might actually be worth producing en-masse in case they were to be needed. Unilaterally trusted recomputation servers (that the network taps redirect traffic to and are responsible for actually performing the verification) are more complicated and thus harder to trust by default, but there are large investments made here. The R&D programs are purposely transparent and open sourced to build trust. China also sees the incentive to develop and build their own symmetrical solution in a similarly transparent way. In the latter half of the year, they agree to mutual information sharing about important verification-relevant information which is otherwise not sensitive, especially about each other’s networking and computing paradigms, which is necessary in order to build compatible network taps and recomputation servers.[^13] Several pilots from different sources of funding and different places around the world are carried out over the course of the year, improvements to the designs are iterated on, and preparations are made to increase production scales. Ultimately the US and China end up opting for network tap solutions with extremely simple optical splitting designs that have minimal room for any vulnerabilities, rather than some of the more ambitious designs that we propose in the box below, or different [cryptographic based-approaches](https://pearlresearch.ai/), which are more uncertain, but if they work (at sufficiently low cost) they might be even better and easier to trust.

Concrete inference-only retrofitting proposal.

Our current best guess is that the US and China should aim for an inference-only solution that uses network taps and a recomputation server. It appears to us to capture the vast majority of the upside in enabling an initial slowdown deal to be highly verified and low economic cost, while being achievable and easy to build. We are less confident in the second part of this, which is why we more confidently recommend RFIs and iteration starting as soon as possible on piloting and iterating on approaches.

![](../assets/verification-plan/image6.png)

Summary of the proposal:

1.  **Convert datacenters into groups of isolated inference-units by removing (a significant amount of) backend networking (also known as east-west networking).**

    1.  Currently AI servers in a datacenter have a lot of high bandwidth communication between them, but this is (mostly) only necessary for training, and with some relatively small overhead (e.g., reorganizing user memory storage), large scale inference should be able to use drastically less scale-out interconnect. Removing it is a significant defense in depth measure for making it harder to use the cluster for large training runs.

2.  **Add in simple, [passive network taps](https://amodo.substack.com/p/tech-note-network-taps-for-ai-verification?triedRedirect=true) on the frontend network (also known as north-south networking) that redirect copies of all input/output traffic to a recomputation server.**

    1.  These network taps on frontend networks have multiple possible implementations. We currently think they should probably be completely passive and split optical signals into two because this is probably easiest to trust. Separately there should be a path from the storage bank back to the inference units.

3.  **Force all AI workloads (inference, agentic tool use, etc.) to be organized in discrete and reproducible packets, which are transparent to the recomputation server (because they pass through the network taps).**

    1.  Reproducibility is required to enable correctness proofs on the packets. By default, inference workloads are not necessarily [reproducible](https://thinkingmachines.ai/blog/defeating-nondeterminism-in-llm-inference/). Achieving reproducibility may involve some cost overhead in order to maintain reproducibility but we think it is a solvable problem (see [here](https://arxiv.org/pdf/2511.20621) for example of work in this direction).

4.  **Perform partial recomputation (random samples of the packets) on the recomputation server to check the correctness of the packets.**

    1.  The integrity of the recomputation server is an extremely important aspect of this step, but assuming its computations and outputs can be trusted, then partial recomputation through random sampling should scale extremely favourably to verify the correctness of all the outputs with extremely high probability while only using a small fraction of the original compute. See calculations in the [appendix](verification-plan.md#appendix-packet-based-verification).

5.  **Have strong physical security properties to help ensure integrity of the verification measures from e.g., tampering attacks**

    1.  The integrity of the verification process requires there to be sufficient physical security measures to avoid tampering, and other attacks that could subvert the verification process.

6.  **Verify completeness by [bounding the maximum side channel communication](https://techgov.intelligence.org/blog/suppressing-side-channels-in-an-untrusted-data-center-via-retrofitted-defenses), and using periodic memory wipes (probably through forced memorization).**

    1.  The completeness of this verification proposal, i.e., that the only outputs from the cluster are verified inference tokens, requires side channel mitigations and memory wiping as described. We do not verify that spare compute isn’t used for unapproved workloads (because this seems very challenging) but try to ensure that the only persisting results in the form of outputs are verified inference outputs. This requires strong side channel mitigations and periodic memory wiping on the inference units (which we think can be done through forced memorization).

One potential upgrade to this proposal would be to build more complex ‘secure network gateways’ that have more functionality than the network taps, and do random sampling and organize and randomly sample the logs of reproduction packets to send to the recomputation server in a robust way.

![](../assets/verification-plan/image3.png)

A rough sketch for what these secure network gateways might look like. There are data path directions (input and output) with network splitters on each path that log data flow to be organized into packets that are randomly sampled and then sent to a secure recomputing server. In a boot phase, these gateways can additionally check that exclusively whitelisted model weights are being uploaded to the inference unit. Some of the hardware security properties you might want for these gateways are precedented, for example, see [iPhone secure enclaves](https://support.apple.com/guide/security/the-secure-enclave-sec59b0b31ff/web) and [PUFs](https://en.wikipedia.org/wiki/Types_of_physical_unclonable_function).

These could be used in place of the network taps in a similar setup as before.

![](../assets/verification-plan/image1.png)

On top of this key effort to build the network-tap and recomputation centered approach, there is also significant funding (order of \$100M) mobilized into R&D for other approaches, including software-only and cryptography-centric (e.g., [ZKPs](https://en.wikipedia.org/wiki/Zero-knowledge_proof)) approaches, and a similar pool for physical security R&D (order of \$100M) that supplements the inference-only retrofitting solution.

Other promising verification directions.

Instead of the partial recomputation approach we sketched out, it might be possible to verify inference-only in other ways, e.g.:

1.  Purely cryptographic protocols, e.g., Zero Knowledge Proofs (ZKPs) for AI workloads

    1.  This has the promise of being privacy-preserving and potentially requiring less of a hardware retrofit, but is currently somewhat speculative due to the lack of computationally efficient enough algorithms for doing so being discoverable.

2.  Memory-challenge based verification

    1.  This has the promise of potentially also not requiring a hardware retrofit, but seems likely to face some difficulties with verifying completeness. Nonetheless it might be viable for an initial deal implementation.

3.  Crude hardware modifications.

    1.  Removing major scale out interconnect and e.g., installing some simple sensors and other physical security mechanisms might also suffice for verifying inference-only for an initial phase of a deal (e.g., 1 year) until higher assurance measures are ready for larger amounts of compute and higher stakes workloads.

### 2028: Chip tracking is mature

The intelligence agencies have been keeping close track of new compute production, and have been partially successful in narrowing down their uncertainty over how much AI compute pre-dated their tracking efforts. By the end of the year, China has around 2% uncertainty over the US’ total compute, and the US has around 4% uncertainty over China’s. This means from China’s perspective, they are 80% confident that the US owns somewhere between 222M and 226M H100-equivalents. From the US’ perspective, they are 80% confident that China has somewhere between 25M and 27M H100-equivalents.

## 2029-2030: Deal Implementation

Deal Implementation Timeline (detailed) - ai-2040.com

### Jan 2029: Mutual Chip Declaration and Inspection

Within a week of starting Plan A negotiations, the US and China have carried out a compute declaration and supply chain record audit, allowing each other to send a few hundred people into each other’s countries to inspect and audit records. This lets them reduce their already relatively small uncertainties over each other’s compute. Each side’s best guess is now that the other could have hidden at most around 1.5M H100e from the declaration (with the 80% CI reaching about 4M), which is about 4% of the leading AI company’s R&D compute and about 0.5% of total world compute. For our estimates and reasoning on how much compute a covert project could probably hide see the [covert projects supplement](covert-ai-projects.md#section-2-preventing-covert-compute-procurement).

Chip declaration result - ai-2040.com

More detail on the suggested interventions by cluster size bucket below:

Cluster size

Medium and Large datacenters (\>10K H100e, ~\$100M)

Immediate intervention

Inference-only retrofit

Estimated compute in this category in Jan 2029 as % of global AI datacenter compute

99%

Cluster size

Small datacenters and diffused AI compute

Immediate intervention

Reporting requirements for anything above an A100 in AI performance. Random spot checks.

Estimated compute in this category in Jan 2029 as % of global AI datacenter compute

1%

Cluster size

Non-AI compute (e.g., iPhones) with unclear AI usefulness

Immediate intervention

Intelligence to look for efforts to gather up massive quantities of consumer compute.

Estimated compute in this category in Jan 2029 as % of global AI datacenter compute

0.1-10%? Depends on uncertain AI-usefulness adjustments.

|  |  |  |
|----|----|----|
| Cluster size | Immediate intervention | Estimated compute in this category in Jan 2029 as % of global AI datacenter compute |
| Medium and Large datacenters (\>10K H100e, ~\$100M) | Inference-only retrofit | 99% |
| Small datacenters and diffused AI compute | Reporting requirements for anything above an A100 in AI performance. Random spot checks. | 1% |
| Non-AI compute (e.g., iPhones) with unclear AI usefulness | Intelligence to look for efforts to gather up massive quantities of consumer compute. | 0.1-10%? Depends on uncertain AI-usefulness adjustments. |

The chip declaration also involves keeping extremely close tabs on all new compute production, and any chips above certain performance metrics of AI-relevance need to either be directed to known locations to be included under the verification measures. While lower powered consumer compute production can likely remain unrestricted.

Chip flow restrictions.

The US and China need to minimize the plausible flow of future compute production to illegal projects. This means they need to monitor its manufacturing and guard its transportation. Luckily AI compute manufacturing is highly centralized in few facilities around the world, and this should continue to be the case through 2029. We think it is highly tractable for them to successfully account for 100% of the new AI compute production (along with critical components like high performance AI memory and networking); our [covert project supplement](covert-ai-projects.md#section-2-preventing-covert-compute-procurement) estimates diversion from post-deal production can be kept to approximately zero, with very high confidence that the total is under 100K H100e. We recommend having companies be allowed to direct new compute they purchase to one of two places.

1.  Existing datacenters / ongoing datacenter builds: compute directed here will only be allowed to do inference once the inference-only retrofit is complete.

2.  Temporary, mutual cold storage holding facilities: compute directed here will be guarded until it is able to be set up for R&D (training and experiments) once new secure, mutually verified R&D clusters are set up.

Chip Flow Restrictions, 2029 - ai-2040.com

At first, we propose that any chip with low enough interconnect, compute, memory and bandwidth can be produced unrestricted. Then by 2032, we tentatively propose a cap, with a slight alleviation of the compute threshold (to give room for more consumer applications that might require higher edge compute) and a tightening of the interconnect threshold (to hopefully lower their potential usefulness in a covert project if diverted). More on this in the [2032 section](verification-plan.md#2032-cap-and-trade-for-robots-and-compute).

### Feb 2029: Inference-only retrofit begins

After the US and China have carried out the compute declaration and inspection, and are relatively confident that they know about the vast majority of each other’s compute, they handshake on a brief AI R&D moratorium and announce it to the world. AI companies are supposed to stop doing R&D immediately for now, including pausing in-process training runs. While they roll out the inference-only verification solution to each other’s largest datacenters, they agree to a 100% power-off of small clusters (anything under 10K H100e, because it will take a while to get to retrofitting these) and a 80% power-off of all larger datacenters because only around 20% of the compute should be sufficient to keep all AI products and services running properly, simply at slightly reduced rates. This limits the extent to which anyone can defect and make differential gains while the deal is being set up and then just going back to racing from a better position than they were in before.

The US has about 95% of its compute in around 200,000 total AI server racks (with just over 1K H100e per server rack on average), and China has about 95% of its compute in 100,000 AI server racks (with about 250 H100e per server rack on average).

Luckily the US has a stock of around 10,000 network taps and 100 (unilaterally) trusted recomputation servers. China has a stock of around 20,000 taps and 200 servers, and they can each purchase another 10,000 per month from various third parties. As a result of China having less compute, the US can retrofit China’s compute faster, but they agree to a proportional retrofitting schedule determined by China’s achievable pace, which is retrofitting 40% of the US compute into inference units of 4 server racks (or 4K H100e) with their existing stock of network taps in 1 month. So they will both follow this pace, and then ramp up to 80% by the 3 month mark and then to \>95% and/or smaller inference-units beyond that.

![](../assets/verification-plan/image6.png)

### March 2029: R&D cluster construction begins

While the inference-only retrofit is being carried out, the US and China then agree on the high level regulatory plan and transparency regime they will be aiming for (some of the options are highlighted in our [transparency supplement](transparency-plan.md)). Given the relatively small perceived risk from illegal projects and various other considerations, they decide to aim for the Total Research Transparency approach. This involves setting up R&D datacenters with SL5 model weights security and SL5 verification integrity. They want these to not be defendable so that it's difficult to try to pull out of the deal and start racing again using these new R&D clusters, so they aim for mutual deterrence by locating the US R&D clusters in Mongolia and the Chinese ones in Canada. The US has guards at their Mongolia cluster that have robust ‘scorched earth’ mechanisms to destroy the compute if China or someone else tries to seize it, and symmetrical measures are in place for the Chinese compute in Canada. They get started on these infrastructure projects immediately in March with high urgency, aiming to have a small amount of capacity online within 6 months so that a verified R&D pilot can start. The verification approach they plan to follow is similar to the inference verification approach, with network taps being used as evidence collection, and partial recomputation being used to verify correctness of the packets that make up the workload.

### April - May 2029: Third party countries begin joining the deal

Starting in April and through the rest of 2029, most of the richest 20 countries in the world, and important semiconductor supply chain countries join the deal by doing a compute declaration and allowing the inference-only retrofitting to their datacenters, including: Germany, Japan, UK, India, France, Brazil, Canada, Mexico, Italy, Australia, South Korea, Spain, UAE, Saudi Arabia, Taiwan, Netherlands, Switzerland.

Chip declaration result - ai-2040.com

### June - July 2029: Construction of new highly secure (SL5) inference-only clusters begins

As part of the transparency regime, the plan is to do broad public deployment of approved frontier models, but under SL5 model weights security achieved through SL5 output verification and distillation mitigations. The plan is to offer a mixture of [Zero Data Retention](https://code.claude.com/docs/en/zero-data-retention) (ZDR) inference for consumers, and transparent inference for higher-risk deployments. More on this in our [transparency supplement](transparency-plan.md). We think these clusters probably need to be built from scratch to reach SL5 model weights security and verification integrity.

Zero Data Retention (ZDR) inference

In order to balance the benefits of ZDR (AI users having strong privacy guarantees) with the risks (AI being used for existentially dangerous applications), we propose 3 tiers of privacy offerings for inference during the deal:

**Total ZDR**

Probability of data deletion

100%

Mitigations

There are very aggressive classifiers, refusals, anti-jailbreaking and models that are not capable in high-risk domains (e.g., AI R&D).

Finetuning API?

No

Inference-fleet cap (global)

100K H100e

**Probabilistic ZDR**

Probability of data deletion

99.9%

(Random sampling, goes to transparent public database if flagged as high-risk by classifiers)

Mitigations

Random sampling that goes to classifiers and to transparent public database if flagged as high-risk

Finetuning API?

Yes

Inference-fleet cap (global)

100M H100e

**No ZDR**

Probability of data deletion

Variable based on classifiers (Random sampling, goes to transparent public database if flagged as high-risk by classifiers)

Mitigations

Normal classifier, refusals, unlearning etc. mitigations, and compression / distillation mitigations.

Finetuning API?

Yes

Inference-fleet cap (global)

100B H100e

<table>
<colgroup>
<col style="width: 20%" />
<col style="width: 20%" />
<col style="width: 20%" />
<col style="width: 20%" />
<col style="width: 20%" />
</colgroup>
<tbody>
<tr>
<td></td>
<td><p>Probability of data deletion</p></td>
<td><p>Mitigations</p></td>
<td><p>Finetuning API?</p></td>
<td><p>Inference-fleet cap (global)</p></td>
</tr>
<tr>
<td><p><strong>Total ZDR</strong></p></td>
<td><p>100%</p></td>
<td><p>There are very aggressive classifiers, refusals, anti-jailbreaking and models that are not capable in high-risk domains (e.g., AI R&amp;D).</p></td>
<td><p>No</p></td>
<td><p>100K H100e</p></td>
</tr>
<tr>
<td><p><strong>Probabilistic ZDR</strong></p></td>
<td><p>99.9%</p>
<p>(Random sampling, goes to transparent public database if flagged as high-risk by classifiers)</p></td>
<td><p>Random sampling that goes to classifiers and to transparent public database if flagged as high-risk</p></td>
<td><p>Yes</p></td>
<td><p>100M H100e</p></td>
</tr>
<tr>
<td><p><strong>No ZDR</strong></p></td>
<td><p>Variable based on classifiers (Random sampling, goes to transparent public database if flagged as high-risk by classifiers)</p></td>
<td><p>Normal classifier, refusals, unlearning etc. mitigations, and compression / distillation mitigations.</p></td>
<td><p>Yes</p></td>
<td><p>100B H100e</p></td>
</tr>
</tbody>
</table>

### August - September 2029: Inference-only ready on 95% of world compute

With several of the largest compute owners joining the deal over the summer, 95% of the compute in the world is now under inference-only verification, and it has now scaled to higher granularity (smaller inference units) and improved physical security (side channel reductions and high effort physical guarding and monitoring).

### Late 2029: Pilot R&D verification begins coming online

In both Canada and Mongolia, mutually constructed datacenters come online at around 1GW in Canada and 2GW scale in Mongolia by September (around 2% of world compute) scaling to around 15% of global compute by the end of the year. Companies are allowed to start hosting compute in these clusters and bid over space as it comes online. Initially, only very small experiments get approved and there is red teaming and iteration on the verification and security measures to test and improve their efficacy.

An overview of possible verification approaches.

Existing work on AI verification ([Baker et. al.](https://arxiv.org/abs/2507.15916), [Scher et. al.](https://arxiv.org/abs/2506.15867), [Harack et. al.](https://aigi.ox.ac.uk/publications/verification-for-international-ai-governance/), [Cankaya et. al.](https://aigi.ox.ac.uk/wp-content/uploads/2026/04/Fingerprinting_All_AI_Cluster_IO.pdf)) introduces many concepts and proposals that could be leveraged or developed to perform R&D verification.

One way we propose to think about the verification problem is to divide it in two parts: (1) collecting evidence, and (2) proving something based on the evidence. This can range from being very simple (e.g., the power in all known compute facilities is off, therefore there is no AI R&D happening) to sophisticated (e.g., based on cryptographic evidence, with extremely high probability the training run correctly used the approved training data and methods).

Here’s a non-exhaustive illustration of some of the evidence collection and verification methods that could be used as we currently see them:

![](../assets/verification-plan/image11.png)

Five key verification metrics we care about include:

- **Assurance curve.** The assurance curve captures information about the level of **coverage** (the % of the AI compute that the verification solution makes claims about) and **confidence** (with what probability is the verification solution correct about the claims it makes on the covered resources). We define an assurance curve as a set of relevant (coverage, confidence) values. We care about the entire 2D curve, because it's important to know where handoff and covert project risks cross over.[^14]

Assurance curves - ai-2040.com

- **Execution difficulty.** How difficult would it be to implement the verification solution correctly? For example, if there are load-bearing parts of the verification solution that require a large amount of expert human labor for e.g., setting up the verification software, manufacturing and installing devices, physical security enforcement and monitoring, etc.

- **Preparation required.** How much research time is required to implement the verification solution. For a solution that could be implemented with existing intelligence capacity, the preparation would be extremely low, conversely, for a solution that requires sophisticated on-chip mechanisms the preparation requirement would be extremely high.

- **Privacy level.** This describes to what extent the verification proposal requires private information to be disclosed between the prover and verifier. We aren’t overly worried about this because we are independently recommending increased transparency anyway, and we also think there can be security mitigations (especially in the case of information we don’t want to diffuse, like model weights).[^15] Nonetheless, it would still be ideal for verification to not require low level access (e.g. tokens, model weights, algos).

- **Economic cost.** Finally, this is a metric for how much overall economic value is lost by implementing the verification solution, ignoring the fact that due to the intervention there may have been risks averted with enormous economic downside (e.g., AI catastrophes, human extinction, etc.) So we are conditioning on a ‘good world’ with continued AI development, and seeing how much economic value is lost compared to that counterfactual. The cost of actually developing, manufacturing, and/or implementing the verification solution is very likely to be dominated by the consideration of how much AI inference is allowed to continue and resulting downstream economic benefits which are harder to quantify.[^16]

- **Scope.** For example, does the verification solution just check for inference-only, or arbitrary AI workloads including large training runs and experiments.

What verification solution to choose will likely have complex tradeoffs between these metrics. Our current best guess is to primarily rely on on-path information collection (i.e., network taps) and then partial recomputation as the verification algorithm, since it seems most likely to be robustly scalable to extremely high coverage and confidence.

Key ingredients to any verification approach that we will assume are pursued.

Drawing on previous AI verification work ([Baker et. al.](https://arxiv.org/abs/2507.15916), [Scher et. al.](https://arxiv.org/abs/2506.15867), [Harack et. al.](https://aigi.ox.ac.uk/publications/verification-for-international-ai-governance/), [Cankaya et. al.](https://aigi.ox.ac.uk/wp-content/uploads/2026/04/Fingerprinting_All_AI_Cluster_IO.pdf)) we think there should be many layers of defense in any verification approach. In other parts of this supplement we typically focus on the verification approach that we think can do the heaviest lifting, but we think many other measures will also be necessary or at the very least helpful, including:

- **Physical security.** Any verification approach is likely going to rely on some set of invariants about the physical state of the AI computing infrastructure. Several promising future directions and existing methods include tamper-evident enclosures, security cameras, perimeter controls, and airgapping. Inference-only enforcement will very likely need confidence that hardware hasn't been significantly tampered with, especially if the verification involves a physical retrofit (which we currently think is the most promising path, though a software-only approach isn't ruled out). The good news is that the physical security requirements for verification overlap heavily with the security posture we'd independently want datacenters to have.

- **Human-based methods.** Whistleblower programs, interviews of personnel, and embedded auditors could go a long way in uncovering large-scale violations, especially early on. We don't rely on these as load-bearing in any of our proposals, but we see them being very useful supplements, particularly during the early stages before more robust technical mechanisms are ready to come online.

- **Mutually trusted manufacturing and supply chain security measures.** Many verification mechanisms will depend on hardware, e.g., network taps, recomputation servers, tamper-evident enclosures, etc., actually being what they claim to be. This creates a desire for mutual verification of the manufacturing and supply chain for verification hardware itself. Harack et al. note that off-chip mechanisms in particular might be mutually verified through non-invasive downstream tests or cooperative production at trailing-node fabs. There's also the promising idea of sidestepping the mutual trust problem in some areas with synchronized unilateral checks: [Cankaya](https://nacicankaya.substack.com/p/catching-misreporting-about-ml-hardware-bd2) proposes using passive optical fiber splitters (no digital logic, just fused glass) so both parties can independently observe network traffic without needing to trust the other's hardware, combined with unilaterally trusted devices to independently implement their own verification.

### Early 2030: Full R&D verification underway

There are now around 100M H100-equivalents in the verified R&D clusters in either Canada or Mongolia (which is about 20% of world compute at the time and equal to 35% of the compute that existed at the start of the deal). These clusters have the [transparency measures](transparency-plan.md) in place and now companies are approved to do the first major post-deal training runs using combined algorithms. In a few months these training runs complete and several of the models are around the automated coder milestone (AC). The models get broadly tested and red-teamed, including by many third party groups and auditors that rent small amounts of compute in the R&D clusters for this purpose.

**There is now a big regulatory question of how to control the speed of R&D progress to balance the risks (of going too quickly) and benefits (of improving capabilities).** This will arguably be the hardest part of the deal to execute on competently. There is a complex set of dependencies, where going too fast incurs AI takeover risk and/or causes progress to [diffuse to potential covert projects](covert-ai-projects.md#section-4-limiting-consortium-uplift-to-covert-projects) (reducing the slack the legal project has), while going too slow incurs risk of making less progress on alignment before the deal possibly breaks down, or indeed actually losing to an illegal project operating outside of the deal.

The high level capability schedule we recommend is to scale to the maximum capability you can reliably make control-based safety-cases for, ideally mostly with hardware scaling, and then pause until your marginal progress on alignment-based safety-cases (handoff risk) is lower than the risk being incurred by the deal.[^17]

But even with a desired high level capability schedule in mind it may be hard to actually enforce this level of capabilities progress, especially to the extent that capabilities progress is unpredictable from inputs (e.g., compute), hard to measure, or fast paced by default. Our best guess is that harsh compute caps, and then a mixture of quality ad-hoc rules will be sufficient, as explained in more detail in the below box.

Research Titration: How to control the speed of R&D progress?

This part of the plan ultimately relies on regulatory competence on what is likely to be a thorny, complex, unpredictable problem of deciding what speed is the correct speed to titrate research to. This is therefore a weaker part of the plan that we are worried about, and hope that future work could improve on the ideas of how to navigate it well. Ultimately, this is one of the core reasons that we recommend Total Research Transparency, because we think it can help there be more accurate and effective regulatory decisions. We do think there are some promising approaches that tradeoff between requiring less regulatory competence, and being a more accurate proxy for the research titration goal being attempted. These two concepts we’ll refer to as:

1.  **Ease of implementation.** How easy it is to implement correctly and easy it is to enforce.

2.  **Regulatory accuracy.** How likely it is that the regulation actually achieves the goal, i.e., under correct implementation and enforcement, software research goes at a safe speed with high probability.

We highlight a few approaches below, and roughly where we think they fall on this tradeoff.

1.  **Safety case burden of proof.** all R&D requires strong safety case arguments before approval. This approach is almost definitionally what we want from a regulatory accuracy perspective, but the difficulty of distinguishing a good from bad safety case might be extremely hard. It also might be very difficult to make good safety cases in the first place, especially without any AI assistance, which is one reason why this approach may only become more viable as the deal goes on. The importance of the regulatory accuracy will also become more important though as the deal progresses, and AIs are reaching higher capabilities, so we suggest this be the regime used for mid-late stages of the deal where highly capable (e.g., TED-AIs) have been developed, or are close to being developed.

2.  **Quality ad-hoc rules.** case by case decisions on permitted research directions and speed. This approach seems like it could be slightly easier to execute on than having to correctly diagnose safety cases, which may be extremely complex (or just too hard to even generate), and instead being able to make high-level calls about paradigms to pursue or abandon and levers to pull in terms of resource allocation. On the other hand, this approach likely loses out on some accuracy, as it might be that high level ad-hoc rules have wiggle room or loopholes that allow unsafe development.

3.  **Human-interpretable requirement.** all approved techniques need to be understood end to end by some group of humans. Forcing human comprehension to be a bottleneck to research progress might be quite a good proxy for safety, and quite easy to implement (have humans look at random samples). That being said, it seems very likely possible for something to be both unsafe, and interpretable by a human, so it may be unstable to rely on this method for very long. It’s also plausible though that this actually slows things down too much, and there should either be a relaxed version or another method used. This method seems potentially very suitable for hardware research titration, more on this below.

4.  **Compute and resource caps.** simple caps on R&D compute. This is extremely easy to implement and verify, but it might just be very inaccurate. Knowing how much progress will result from certain compute and other resource (e.g., human researcher) thresholds will be an uncertain modelling question, that likely will have wide error bars. In the early stages of a deal though, setting these very low seems like a good, easy to implement starter, which can then be escalated to more accurate approaches given time to ramp capacity.

Research Titration Approaches - ai-2040.com

With a particular set of rules on research in place, there is a separate problem of enforcing these rules are actually followed. We can divide the problem of enforcing the R&D rules into two parts:

1.  **Workload Approval.** Workloads that companies declare actually meet the regulatory rules, whatever their implementation may be.

2.  **Workload Verification.** Workloads that the companies declare match what they actually run.

Our view is that workload verification is solvable in a similar way to what we discussed previously (evidence collection via network taps, and then partial recomputation of randomly selected reproducible packets), whereas workload approval will be closely tied to the form of AI R&D rules that are in place (e.g., are they just experiment compute caps? Are there specific banned techniques? Are there specific required techniques?) and our overall baseline proposal for approval is for this to just be manually carried out by teams of auditors in the R&D clusters.

Workload Approval.

The core difficulty here is that it might be unclear whether the workload follows the rules, especially as the rules are more ad-hoc. Also, it might be possible for AI companies to do adversarial attacks, like trying to encode a non-compliant workload inside a workload that looks compliant on the surface. As the regime progresses and they have more and more compute under mutual verification, attacks like this that exploit tiny percentages of the total compute for a non-compliant purpose might become significant.

Possible mitigations we can think of are:

1.  Anti-steganography measures on the declared workloads and data

2.  Auditor compilation into gpu instructions, ideally with increasingly robust and secure programming languages.

3.  AI assisted data filtering and checks

A potential overall regime to use is to maintain ‘white’ lists of code and data that has been vetted and approved to be used, and/or ‘black’ lists of code/data that is banned, and/or ‘gold’ lists of techniques that are required on every workload of a certain type. Then the workload approval problem can be reduced to simply checking against these lists in order to approve or deny a workload. It might be drastically harder to implement a covertly rogue workload using only whitelisted code, but it also might just punt the problem to whatever the process is for populating these lists. At least this might help with making workload approval a more transparent process that companies and even the broader public can contribute to (at least on everything that is publicly available, which later into the deal might exclude some internally discovered algorithms that there is an attempt to keep secure through the embargo mechanism we describe in our transparency proposal).

![](../assets/verification-plan/image9.png)

Workload Verification.

We also mentioned multiple different types of evidence collection or verification that might be used. Our guess is that in order to reach extremely high levels of assurance, which will be increasingly necessary in Plan A (more on this later), a reproducibility mandate, combined with complete (and increasingly granular) on-path evidence collection, paired with a partial recomputation based verification algorithm, will be a viable approach. That being said, we are not confident that another approach (e.g., using low latency challenges and validity checks) might not be able to reach the same levels of assurance at lower costs or higher levels of assurance at equal costs. For the purposes of making the case that the verification problem will be viable, we will talk about the complete (and increasingly granular) on-path evidence collection with partial recomputation based verification algorithm.

Another useful concept for thinking about the verification problem is to think of AI workloads as discrete series of steps.

Example Packet Sizes - ai-2040.com

By default, these computational steps execute with randomness, but if they can be forced to be reproducible (e.g., seeded randomness is fine), then we can have a predictable relationship between the granularity of the evidence collection and the assurance level of the verification algorithm. This is because partial recomputation with random sampling with some small percentage of the workload being recomputed has favourable scaling of detection probability as you decrease the size of the individual workload packets that you check the correctness of. More detail on this in the [appendix](verification-plan.md#appendix-packet-based-verification).

**Pool:** ~33B H100e (2034 buildout)**Recomputation budget:** 1%**Year:** 20342030203220342040**Packet size:** 100 H100e-hours1101001K10KCatching a rogue internal deployment - ai-2040.com

The concrete regime we imagine for the first few years of the deal is to still use network taps for evidence collection, and partial recomputation of randomly selected reproducible packets to verify correctness. The same high level approach as inference-only, with smaller and smaller packet sizes over time by moving the network taps to lower levels of the backend network.

![](../assets/verification-plan/image8.png)

1.  **Declaration:** AI companies declare the workload they want to run with full transparency on the code, algorithms, etc.

2.  **Approval:** Auditors run checks per the **Workload Approval** implementation and if it passes they send back approval and provide necessary random seeds (removes a potential attack vector from AI companies gaming fake randomness).

3.  **Evidence collection:** Auditors collect evidence from the workload (e.g., complete logging flow through network taps). In the diagram the evidence collection is depicted as low granularity, but in reality it could be happening at the level of individual servers, or GPUs or at even lower levels later on.

4.  **Verification:** Auditors sample randomly and do partial recomputation and other checks to catch violations of workload correctness.

5.  **Evaluations and release:** For workloads that consist of final training runs there can be an extra step that involves running evaluations that also get verified for correctness, and then final model approval for release leads to the model weights being downloaded from the opaque internal database and transported to the inference-only clusters. This process is extremely high stakes from a model weights theft perspective, so would need to be carefully designed and executed.

### Late 2030: Secure inference-only clusters for post-deal model deployment come online

First SL5 inference-only clusters are online and start serving the first post-deal models that have been approved from the R&D clusters for broad public deployment. These clusters have the same basic verification approach as the retrofitted ones (network taps and partial recomputation) but with improved security properties. By the end of the year, around 40% of world compute (~370M of the global ~930M H100e) is in these new post-deal SL5 inference-only clusters.

Also by the end of 2030, the US and China have set up hardened cold storage facilities where they allow inspectors to verify each other’s stash of AI chips, sized to be bigger than any plausible covert projects (a 5M H100e US bank and a 500K H100e China bank, per our [deal decline supplement](deal-decline.md#preparing-stockpiles-to-align-incentives)), and of relative size to each other similar to pre-deal status quo. These are in places that either side can easily defend. These locations will also be home to verified model weights stashes, so that models that the US and China agree would be positive sum to approve for use in the case of deal dissolution (e.g., models that would be very helpful for safety research and have strong safety cases). Around 2033 there is a model around the automated coder capability milestone that gets approved for the weights stash, and then in 2037 there is a near-frontier (top expert AI) model approved for the cold weights storage.

## 2031-2036+ Improving the deal

### 2031: Restrictions for hardware R&D and other high-risk domains

The core problem the US-China deal sets out to address is the intelligence explosion.[^18] But the intelligence explosion isn’t the only threat to deal with. Another core concern is that AI could enable an industrial explosion, too much AI hardware progress, or other dangerous scientific progress.

The case for being worried about AI software progress was illustrated in AI 2027: superhuman AI researchers could bootstrap to a superintelligence that we might not be able to control and whose goals we haven’t figured out how to align. The case for being worried about too much hardware progress is superseded by this under a fast takeoff, but under the Plan A deal if we only slow down software progress a hardware driven takeover might actually be the majority of the takeover risk absent separate mitigations.

Three major reasons to be worried about unconstrained hardware progress:

**Production explosion effects**We should be worried about an explosion in the industrial capacity (e.g., number of robots) on earth, even absent design improvements.With existing robot designs, it might become easy to rapidly build an absurd number of robots, by having new robots work on making more robots, naively the doubling times might be as low as months, which is very fast. The likelihood of an industrial explosion is argued in more detail in our [economics supplement](economics-of-plan-a.md#core-arguments-for-explosive-growth).An absurd number of robots might be able to do destabilizing things like:(1) Create massive military advantages for first movers (either directly in the form of a robot army, or through pure industrial capacity, e.g., missile/weapons production capacity),(2) Build AI hardware covertly (by building all the equipment & facility needed to do so from the ground up in a secret location)**Destabilizing robot designs**We should also be worried about new advanced designs, e.g., self-replicating microbot/nanobot/biotech.Biological anchors (and precedents of humans beating biology with intelligent designs) should have us worried that scary robot designs are possible. Specifically, we should be worried about self-replicating nanotech / biotech that have very fast doubling times.The core concern here is that these designs, unlike macroscale robots, might be too hard to govern, and break any regulations once they are invented.**Destabilizing AI compute designs**We should also be worried about AI hardware design improvements that make it easier to manufacture.AI hardware design improvements and/or paradigm shifts might make it easy to defect from the deal. If there is a paradigm shift in hardware design making it no longer require an extremely specialized, complex, and centralized manufacturing supply chain to make AI compute, it might be tractable for covert projects to manufacture more AI compute in an undetected way threatening the stability of the deal.

Similarly we want other high risk scientific domains such as biology research to have R&D restricted. Our default proposal for this is to rely on inference refusals and monitoring on the majority of public deployment, and then potentially set up dedicated locations that allow high-stakes hardware and other scientific research to be carried out in mutually verified research labs, where we make some (not necessarily identical) security-transparency tradeoff choices, and mutually verify that the companies follow the titration rules on hardware R&D, which can also be some combination of safety cases, ad-hoc rules, human interpretability requirements and resource caps (similar to software research).

Inference restrictions, monitoring and refusals for high-risk domains.

One downside of publicly deploying highly capable models is that they could enable dangerous research, or illegal projects could use those models to help them with AI research, or directly distill the outputs of these models to help train their models. In order for broad inference deployment to not lead to distillation, illegal project uplift, or other dangerous research, there needs to not only be correct output verification, but also some sufficient combination of refusals, monitoring, and compression.

1.  **Refusals or capabilities shaping.**

    1.  AIs that are released publicly by the Consortium should be bad at AI research. They could be designed to be worse at ML engineering than other tasks, to make it harder for rogue projects to use them. This has the downside of being worse for speeding up diffused safety research. Robust refusals, instead of a lack of capability, may be another way to achieve this goal.

2.  **Monitoring.**

    1.  On top of inference correctness verification, there should be monitors (probably passive rather than active is fine) running on the models, checking to see if they seem to be involved in doing AI research, large scale training, or other dangerous research. It may be tractable to detect these cases quite reliably, for example, if they are operating in a codebase that involves code for training over a large number of GPUs, it is pretty obvious that this is an illegal usage.

3.  **Compression.**

    1.  Never show any reasoning intermediates to users by default, and maximally compress outputs to summaries up to some small quota.

    2.  Vertically integrate whenever possible at multiple levels and just produce outputs:

We currently think these are tractable mitigations that will allow a lot of broad deployment, but are uncertain. There should be ongoing testing for distillation and detecting dangerous research.

Hardware research restrictions.

1.  **Setting rules on hardware research**

    1.  One specific subset of the rules might be to only allow research into traditional-like robot designs, traditional-like chip designs, since much of the risks from hardware research are in destabilizing paradigm shifting scientific breakthroughs that might lead to things like nanotechnology or far easier-to-manufacture AI compute. And traditional-like designs might still be improvable enough to realize the benefits of hardware and robot buildups under the deal. That being said, if they are not improvable enough, then it might be more advisable to make more relaxed hardware research restrictions.

    2.  In hardware we might have an unclear idea of the relationship between inputs and progress, just like we are also very uncertain about the relationship between compute and software progress. Nevertheless, we can use the same hope that by operating over harsh order of magnitude reductions in inputs (e.g., energy caps, materials caps, research labor caps, etc.) we might be able to iteratively slow the pace of hardware progress to levels perceived to be safe in a lossy but easy to implement way.

2.  **Enforcing rules on hardware research.**

    1.  Once the hardware research titration rules are set, we need a way to verify they are being followed. One possibility would be to use the same high level approach as for software enforcement, i.e., approve hardware research jobs case by case (or via some automated whitelist/blacklist process), divide up jobs into substeps and collect evidence about them, and then check random samples for compliance. One problem with this approach in the hardware case is that it seems far harder to get high reproducibility in e.g., a chemistry experiment, because two labs in the real world are not as homogenous as AI chips. This opens the door for plausible deniability and violations. Therefore, we probably need to not go with a reproducing based approach on everything. That being said, there might be many slices of the hardware research that are reproducible.

    2.  Another possibility is that since many things might be macroscale, you can monitor everything directly with a monitoring scheme that you trust. Maybe the trusted monitor will be hard to build though, so instead, you might be able to instead have humans inspect random samples of all the recordings, and benefit from the favorable detection probability scaling from random sampling.

Overall, we are very uncertain about how to verify hardware research rules, and have the current sense that it might be harder than software (but also think it's plausibly easier). That being said the default speed and risk level, and therefore the overall slowdown required we think is likely to be lower.

### 2032: Cap & Trade for Robots and Compute

As mentioned earlier, we want to stop an explosion in the number of robots and AI chips on earth from threatening the stability of the deal. By default, our [current naive modelling](economics-of-plan-a.md#the-full-economic-model) predicts that even with current hardware designs, the AI and robot capabilities that we forecast to be reached during the Plan A scenario would lead to a huge discrepancy between the raw cost of producing more AI chips and Robots and their economic value. By default, we think this leads to a reinvestment spiral and very fast doubling times.

In Plan A we propose a cap starting in 2032 that limits the number of robots and AI chips on earth to doubling times around 6 months, through cap & trade regulation, where private companies need to bid on the finite robot and AI chip production permits in any given time period. This cap should be set in units of usefulness of the robots for industrial production and AI compute in AI workloads, measuring both of these, especially across tasks and form factors in the case of robots, might be difficult and muddied (e.g., fuzzy lines between robots and more traditional machines). We nonetheless think it should be feasible to measure these things reasonably well for different robot and hardware designs, and allocate the cap & trade limits accordingly.

Actually enforcing the cap & trade permit rules might be very difficult if robot and/or AI compute production happens all over the world, so we propose centralizing new built up industrial capacity and robots in special economic zones (SEZs) to make for easier enforcement of the cap & trade rules.

How to enforce the cap & trade rules.

Our proposal for this is to centralize all the built up industrial capacity and robots in special economic zones (SEZs), to centralize the enforcement and associated surveillance in these restricted zones, and allow the rest of the economy to not be subjected to any hardware verification checks.

The SEZs can then have a similar high level verification approach to either hardware research and/or the inference-only and software R&D approach, where production gets broken up into discrete steps, and these get randomly, manually audited by humans (and/or with trusted AI monitoring assistance).

The rest of the economy can then be left unverified, but should probably have upper bounds on the robots, power and other potential inputs to hardware production. If these bounds are low, then there can be minimal surveillance outside of the SEZs. That being said, we guess the bounds might be too costly to keep sufficiently low because people really want diffused robots. So it might be good to have reliable geolocation on the diffused robots and maybe random inspections. In order to avoid too much diffused compute as well, we also propose that robots have very little unverified edge compute, and instead largely be served via the cloud on the monitored (ideally automated by AIs to be privacy preserving) and verified inference-only clusters, until there is robust edge compute verification.

The same cap and trade principle is extended to other products and services that are destabilizing in unrestricted quantities, but can be safe in lower quantities. Two major examples are products with edge compute and unmonitored inference. Things that might particularly rely on edge compute include self-driving cars and consumer compute, while unmonitored inference might be particularly valuable to governments for military operations. Under cap and trade the regime can accommodate these activities being legal, under safe societal-scale caps that maintain the stability of the deal. Then there can be markets for the permits the people, firms and the government can bid between each other to have the rights for.

Unverified edge compute cap.

**We propose a cap of 30M effective-H100e of unverified edge compute being allowed to exist in the world, with estimates of 25M [effective](compute-supplement.md#appendix-the-effective-h100e-model) H100e predating the deal, there are only 5M credits available for new unverified production.** **With sufficient edge verification measures, the compute can be exempt.**

Unrestricted, edge compute in consumer devices, self-driving cars and robots might introduce a significant stock of compute that could be used by illegal projects. Before the deal consumer and edge compute likely will include some AI-relevant compute,[^19] (e.g., hobbyists with single GPUs, self-driving car chips), and mostly non-AI relevant compute (chips with low effectiveness on AI workloads), but which is nonetheless very numerous (i.e., there are tens of billions of phones, each around 0.1 - 1% as useful as an H100 for AI workloads, which still means tens of millions of H100-equivalents, i.e., ~10% of the total AI-relevant compute in the world). In our [compute supplement](compute-supplement.md#12-all-compute), we estimate that this will be around 25M **[effective](compute-supplement.md#appendix-the-effective-h100e-model)** H100e.

This should be estimated more precisely at the time with a better model of usefulness in frontier AI workloads. If consumer compute usefulness is found to be higher than we estimate, then it becomes more important to avoid that large quantities of consumer compute could be rounded up and used in a covert project, and therefore e.g., a high-priority compute buy-back effort might be warranted.

We expect the cap we propose to lead to rapid innovation in ‘edge verification’ (i.e., essentially robust hardware mechanisms), to avoid the permit costs. We predict that there will be plenty of cheap phones that have low local-AI capabilities, whereas phones or other consumer devices that have a lot of local, or ‘edge’ AI compute will be very expensive at first, but don’t need to be banned. Then after a few years there will be robust edge verification that can allow powerful edge compute to also become cheap (not require a permit), for example, with hardcoded code and weights. The cap is set such that trivially noticeable shares of the consumer compute would need to be diverted to noticeably accelerate a covert project (or to give bad actors too much of a weapon). It’s a sad but potentially necessary reality for at least at the beginning of Plan A that if you want to have a fancy gaming GPU that could also be used for AI instead, you need to pay a premium (because we can’t let everyone have one or else it would become too easy to round up a significant number of these to contribute to a rogue compute cluster). Or in economist terms, unverified edge compute carries a large negative externality (risk of being used by a covert project).

On top of the unverified consumer compute cap, it might be desirable to have a certain effective-H100e cutoff (e.g., with specific compute, bandwidth, memory capacity and networking speed thresholds) for consumer compute that is allowed to be sold in single units (to the extent that the difficulty of gathering chips into a covert project or detection therefore scales more closely with the absolute number of chips than with the compute). There might also be a tier of compute that we require to have location tracking measures (to make use by a covert project easier to detect).

Chip Flow Restrictions, 2032 - ai-2040.com

Putting together research titration and production capping, we have the following overview:

![](../assets/verification-plan/image13.png)

### 2033: Security improvements

By 2033 we expect significant hardware security, and more general security properties of the datacenters, verification regime and capabilities to have improved significantly. By the end of 2033, around 99.9% of the worlds’ compute is post-deal compute, meaning that it's trivial to just power down all pre-deal clusters and compute, and have the vast majority of compute be in new more secure locations built from scratch. Furthermore, by the end of 2034, around 90% of the compute that exists will have been produced during 2033 or 2034. This means that security improvements made by then can already be widely in place within just 1-2 years. Similar dynamics apply to the fabrication facilities.

Our uncertainty on what will be possible is high here, but some of the main ideas we have include:

- Datacenters built from scratch with extremely good side channel and airgapping properties.

- Huge progress in standardizing (for reproducibility) and improving security of software stacks for inference and R&D workloads more generally.

- New compute production facilities (fabs) built from scratch with mutual monitoring measures and being colocated with supply chain and potentially even with final centralized datacenters they will fill to minimize attack surface.

- The beginning of some hardware-software co-dependencies especially with architecture changes or number formats, so that optimization and progress in these paradigms is less applicable on pre-deal compute

- Increases to the logging / evidence collection granularity of the verification regime, especially of the R&D datacenters, with logging technology being compatible with extremely high bandwidth data paths on backend networking to reduce overhead.

- Generally improved hardware security properties with more robust trusted execution, secure boot, encryption, reproducibility, etc., which are especially important for recomputation servers. Some degree of standardization in hardware may also be helpful for reproducibility.

- Special hardware designs for automatic on-device verification of certain workloads, in particular, hardcoded weights on some chips to verify they're inference-only. This might be particularly useful for ‘edge verification’ allowing for more AI compute in consumer products without risk of use in covert projects.

### 2034: Verification improvements

Through the 2030s the total amount of AI compute in the world grows explosively. One important dynamic to note is that the verification burden (the need to have higher coverage) grows as the total compute under verification grows. In Plan A, we both forecast and recommend a significant hardware buildup (capped by the cap & trade regime to stay verifiable) for other reasons related to tradeoffs with deal stability (hardware is less likely to leak to illegal projects so differentially increases the legal projects affordances).

World Compute - ai-2040.com

The verification assurance curve needs to improve such that any potential nonnegligible rogue internal deployment would have a high chance of detection. By 2034, with one packet collected per hour from each frontier GPU (~100 H100e each, so ~100 H100e-hour packets) and a 1% recomputation budget, the appendix math shows the verifier catches any rogue internal deployment at 99% confidence after it accumulates ~46,000 H100e-hours of unapproved work, so a sustained 10K H100e deployment is detected within ~4.6 hours, a 1K within ~46 hours, and so on.

Workload: ~GPT-3 sized training run (100K H100e-hours)Verification logging granularity - ai-2040.com

This is an ambitious verification scale, and it also relies on extremely good integrity security on the verification regime. We think it will be possible to scale it this far, especially with AI assistance, but are not confident, and find it plausible that the compute cap should be set lower in order to not increase the verification burden this much.

**Pool:** ~33B H100e (2034 buildout)**Recomputation budget:** 1%**Year:** 20342030203220342040**Packet size:** 100 H100e-hours1101001K10KCatching a rogue internal deployment - ai-2040.com

### 2035: Moving the datacenters to the ocean

One of the biggest ongoing risks is that the deal breaks down and actors return to racing. Because of the vast increase in compute scale that has not been turned into capabilities progress (due to the safety regulations) the return to racing could be even more dangerous than the initial status quo, despite the alignment progress made up until this point, because things would now go faster. This motivates having measures in place to return to pre-deal compute levels, or even smaller compute scales if the deal breaks down.

We think the relative engineering and logistical costs involved in building new datacenter capacity on the ocean in international waters will be low enough due to robot and AI labor to make this worth it around 2035, because it would become much harder for any particular actor to defend and much less escalatory to destroy in the event of the deal breaking down. This is an intentional measure for mutually assured compute destruction to increase the deal’s stability.

### 2036+ Advanced robustness improvements

Later into Plan A we are increasingly uncertain about what robustness improvements will be possible in terms of security, verification and deal stability. Potentially extremely ambitious things will be possible, a brainstorm here included:

- Completely rewritten software stacks to be significantly or entirely formally verified.

- Huge red teaming efforts on the verification scheme or security measures using resources that dominate any potential covert actors.

- Using AI and robot labor to track down potential covert projects in mutually agreed, symmetrical ways, e.g., the ‘AI silver bullets’ explored in our [covert project supplement](covert-ai-projects.md#section-31-plan-a-strategies-for-detection): reliable lie detectors, privacy-preserving AI verification, and extreme industrial verification.

## Appendix: Packet-Based Verification

This appendix works through the math on random sampling for use in partial recomputation to show why it scales so favourably for detecting incorrect workloads. A key simplifying assumption we make in this analysis is that the workload packets are perfectly reproducible.

### A.1 Setup

In this analysis we treat verification as a sampling problem on a stream of packets. A packet is a reproducible unit of computation that the verifier can recompute: its inputs, instructions, and outputs are all collected at the evidence-collection point (e.g., a network tap). What the computation actually is (one forward pass, one training batch) doesn’t affect the math below. Further simplifying assumptions we make are:

1.  **Uniform size.** Every packet represents the same amount of underlying compute. Non-uniform packets work too, with a weighted-sampling argument that doesn't change the qualitative results.

2.  **Independent random sampling.** The verifier audits each packet independently with the same probability. In reality you would sample without replacement.

Let the verifier's pool be some collection of packets; it could be a single training run, every packet from every workload running under the deal in a given month, or one cluster's traffic. Let \$N\_{\text{packets}}\$ be the total number of packets in that pool, \$s = 1 / N\_{\text{packets}}\$ the packet size (the fraction of the pool each packet represents), \$C\$ the recomputation budget (the fraction of the pool the verifier can afford to recompute), and \$N\_{\text{verified}} = C \cdot N\_{\text{packets}} = C / s\$ the number of packets actually audited.[^20]

### A.2 Detection by Random Sampling

The detection math in this section was independently derived but matches the analysis in [Rinberg et al. (2025)](https://arxiv.org/abs/2511.02620). Suppose an attacker substitutes \$N\_{\text{fake}}\$ packets, replacing the declared computation in each with their own unauthorized one. Let

\$\$ F\_{\text{fake}} = \frac{N\_{\text{fake}}}{N\_{\text{packets}}} \$\$

be the fraction of packets that are fake. If the verifier audits each packet independently with probability \$C\$, the exact probability that none of the \$N\_{\text{fake}}\$ fakes is audited is

\$\$ P(\text{undetected}) \\=\\ (1 - C)^{N\_{\text{fake}}}. \$\$

For small \$C\$ and modestly large \$N\_{\text{fake}}\$, this is well approximated by a Poisson distribution on the number of caught fakes, with mean \$\lambda = N\_{\text{verified}} \cdot F\_{\text{fake}} = C \cdot N\_{\text{fake}}\$:

\$\$ P(\text{undetected}) \\\approx\\ e^{-N\_{\text{verified}} \cdot F\_{\text{fake}}}, \$\$

so the probability of catching the attack (the **detection confidence** at attack size \$F\_{\text{fake}}\$) is

\$\$ P(\text{detected}) \\=\\ 1 - P(\text{undetected}) \\\approx\\ 1 - e^{-N\_{\text{verified}} \cdot F\_{\text{fake}}}. \$\$

We'll use the Poisson form throughout, since it's the cleanest expression of the scaling. It breaks down only when \$C\$ approaches 1 or \$N\_{\text{fake}}\$ is single-digit, which is also when random sampling stops buying you anything (see the discussion at the end of [§A.3](verification-plan.md#a3-the-assurance-curve)).

### A.3 The Assurance Curve

The assurance curve is determined by **coverage** and **confidence** which can be expressed in terms of \$F^{\*}\_{\text{fake}}\$, the largest fraction of fake packets we're willing to tolerate without detection:

- **Coverage** \$\\=\\ 1 - F^{\*}\_{\text{fake}}\$, the fraction of the workload we're claiming is legitimate.

- **Confidence** \$\\=\\ 1 - e^{-N\_{\text{verified}} \cdot F^{\*}\_{\text{fake}}}\$, the probability we'd catch any actual violation at or above that threshold.

The confidence formula comes from [§A.2](verification-plan.md#a2-detection-by-random-sampling): \$P(\text{detected}) = 1 - e^{-N\_{\text{verified}} \cdot F\_{\text{fake}}}\$, evaluated at the threshold \$F^{\*}\_{\text{fake}}\$. The recomputation budget shows up through \$N\_{\text{verified}} = C \cdot N\_{\text{packets}}\$, so more audited packets push the curve outward.

Plotting confidence against coverage for several verification budgets (i.e., different values of \$N\_{\text{verified}}\$):

Assurance curves - ai-2040.com

These curves show the confidence-coverage relationship at different values of \$N\_{\text{verified}}\$. Higher \$N\_{\text{verified}}\$ gives you higher assurance (shifts the curve right). Since \$N\_{\text{verified}} = C / s\$, **the curve can be shifted higher either by (1) increasing the recomputation budget \$C\$ or (2) shrinking the packet size \$s\$.**

When the Poisson approximation breaks down.

The product \$C \cdot N\_{\text{fake}}\$ (recomputation budget times number of fake packets) is the single quantity that determines 99% catch probability: it just needs to exceed about 4.6.

This makes the limiting case revealing. Imagine you sample one packet per server-hour, so \$p = 1\$ server-hour, and the attack is also just a single fake packet (one rogue server-hour buried in a much longer, say year-long, workload). With \$N\_{\text{fake}} = 1\$, the Poisson approximation would say you need \$C \geq 4.6\$, which doesn't make sense: \$C\$ is a fraction, capped at 1 (you can't recompute more than 100% of packets).

This is the regime where the Poisson approximation breaks down, and the right formula is the exact one for sampling without replacement:

\$\$ P(\text{catch}) \\=\\ 1 - (1 - C)^{N\_{\text{fake}}}. \$\$

For \$N\_{\text{fake}} = 1\$ this gives \$P(\text{catch}) = C\$. To catch a single fake packet with 99% confidence, you'd need to recompute 99% of all packets, i.e. you've essentially given up on sampling and are doing full verification. The size of the surrounding workload doesn't matter: you're flipping a single coin biased by \$C\$.

The Poisson formula is accurate whenever \$N\_{\text{fake}}\$ is at least a few dozen and \$C\$ is small (say under 10%). For \$N\_{\text{fake}} = 100\$, the exact required budget for 99% catch is 4.5%, vs Poisson's 4.6%, which is very close. For \$N\_{\text{fake}} = 1000\$ the exact answer is 0.459%, vs Poisson's 0.46%. The two agree better as \$N\_{\text{fake}}\$ grows. Things only diverge in the small-\$N\_{\text{fake}}\$ corner, which is also exactly the corner where random sampling stops being useful and you have to recompute everything.

So the practical takeaway: random sampling buys you a lot once you're catching attacks that span at least dozens of packets. To catch attacks below that, shrink packets (decrease \$p\$) so the same fake compute-work spans more packets.

### A.4 Worked Examples

#### A.4.1 100K-token Backdoor in a 100T-token Training Run

Consider a training run of \$N\_{\text{tokens}} = 10^{14}\$ tokens (100T) using distributed data parallelism. Network taps between server racks log every gradient step (its input batch, the gradient update, and the resulting checkpoint update), so each gradient step is one packet. An attacker wants to insert a backdoor by silently training on \$N\_{\text{fake tokens}} = 10^{5}\$ off-spec tokens (100K).

| Quantity | Symbol | Value |
|----|----|----|
| Training tokens | \$N\_{\text{tokens}}\$ | \$10^{14}\$ |
| Attack size (backdoor) | \$N\_{\text{fake tokens}}\$ | \$10^{5}\$ |
| Batch size | \$B\$ | design choice |
| Number of packets | \$N\_{\text{packets}}\$ | \$N\_{\text{tokens}} / B\$ |
| Packet size | \$s\$ | \$B / N\_{\text{tokens}}\$ |
| Fake fraction | \$F\_{\text{fake}}\$ | \$N\_{\text{fake tokens}} / N\_{\text{tokens}} = 10^{-9}\$ |

For 99.9% detection confidence we need \$N\_{\text{verified}} \cdot F\_{\text{fake}} \geq \ln(1000) \approx 7\$, i.e. \$N\_{\text{verified}} \geq 7 \times 10^{9}\$. The recomputation cost as a fraction of the training run is then

\$\$ C \\=\\ \frac{N\_{\text{verified}}}{N\_{\text{packets}}} \\=\\ N\_{\text{verified}} \cdot s \\=\\ \frac{7 \cdot B}{N\_{\text{fake tokens}}} \\=\\ \frac{7 B}{10^{5}}. \$\$

| Batch size \$B\$ | \$N\_{\text{packets}}\$ | Recomputation cost \$C\$ |
|------------------|-------------------------|--------------------------|
| 10,000           | \$10^{10}\$             | 70%                      |
| 1,000            | \$10^{11}\$             | 7%                       |
| 100              | \$10^{12}\$             | 0.7%                     |
| 10               | \$10^{13}\$             | 0.07%                    |

Making batches \$10\times\$ smaller cuts the required recomputation cost \$10\times\$ for the same confidence (ignoring the fact that we do better than this at values of C close to 1 by sampling without replacement). The two practical levers on packet size are (1) smaller batches (more gradient steps per training run), and (2) sub-batch logging, tracking intermediate computations within a batch (e.g., individual forward/backward passes), which might require evidence-collection devices inside server racks or even inside GPUs themselves.

#### A.4.2 Bounding Rogue Compute Use in 100B H100e of Verified R&D

The [2034: Verification improvements](verification-plan.md#2034-verification-improvements) section explores what **rogue internal deployments** have low detection probability if the verifier has a 1% recomputation budget across 100B H100e of verified R&D compute. Rogue internal deployments are potentially scarier than external illegal projects due to internal access to frontier models and the rest of the R&D cluster. Detection relies on the verification system catching their fake packets. The math below translates the assurance curve from [§A.3](verification-plan.md#a3-the-assurance-curve) to concrete values.

Starting from \$P(\text{detected}) = 1 - e^{-N\_{\text{verified}} \cdot F\_{\text{fake}}}\$ and substituting \$N\_{\text{verified}} = C \cdot N\_{\text{packets}}\$ and \$F\_{\text{fake}} = N\_{\text{fake}} / N\_{\text{packets}}\$, the \$N\_{\text{packets}}\$ cancels and the detection probability becomes:

\$\$ P(\text{detected}) \\=\\ 1 - e^{-C \cdot N\_{\text{fake}}}. \$\$

In this form the detection probability is a function of the recomputation budget \$C\$ and the absolute number of fake packets \$N\_{\text{fake}}\$ the attacker generates.

For 99% confidence we need \$C \cdot N\_{\text{fake}} \geq \ln(100) \approx 4.6\$, so the attacker is caught with 99% confidence the moment they have accumulated

\$\$ N\_{\text{fake}}^{99\\} \\=\\ \frac{4.6}{C} \$\$

fake packets. With \$C = 1\\\$ that is 461 packets, independent of pool size and of how the work is spread across workloads. Multiplying by the packet size \$p\$ converts this to a bound on cumulative rogue compute work:

\$\$ W\_{\text{rogue}}^{99\\} \\=\\ \frac{4.6 \cdot p}{C}. \$\$

Consider the operational setup of the 2034 section, in which the verifier collects one packet per hour from each frontier GPU (about 100 H100e each by 2034). Then \$p = 100\$ H100e-hours, and with \$C = 1\\\$,

\$\$ W\_{\text{rogue}}^{99\\} \\=\\ \frac{4.6 \cdot 100}{0.01} \\=\\ 46{,}000 \text{ H100e-hours}. \$\$

The verifier catches with 99% confidence any rogue internal deployment that accumulates more than about 46K H100e-hours of unapproved compute work inside the verified pool, regardless of pace or distribution. The bound on cumulative rogue work scales linearly in \$p / C\$; a few representative operating points:

| Packet size \$p\$ | Budget \$C\$ | Max undetected rogue work |
|-------------------|--------------|---------------------------|
| 100 H100e-hours   | 1%           | 46,000 H100e-hours        |
| 100 H100e-hours   | 0.1%         | 460,000 H100e-hours       |
| 10 H100e-hours    | 1%           | 4,600 H100e-hours         |
| 1 H100e-hour      | 1%           | 460 H100e-hours           |

[^1]: With variable economic costliness and other tradeoffs which we discuss. As a baseline we are \>90% confident that a highly costly verification solution is possible for both inference and training (e.g., multi-year verified compute shutdown with verification R&D sprint and secure rebuild).

[^2]: Our [covert project supplement](covert-ai-projects.md) discusses how likely it is for a covert project to be able to pose a threat to the deal or win the AI race.

[^3]: Even this might be difficult to execute on to the extent that at least one side has high uncertainty over the other having a large secret datacenter that they don’t declare and allow the other side to verify is powered off.

[^4]: Another live option that could currently be executed quickly would be to unplug (most) backend networking from datacenters. This might allow a lot of inference to continue (less costly), but also might not slow down AI development robustly (inference is used as rollouts for data to be used in federated learning training run elsewhere).

[^5]: A key reason we believe this is that the verifier only needs to catch one violation, while a prover needs to successfully hide all of their covert computations. This is the reason behind e.g., the favourable scaling of partial recomputation due to random sampling which we explore in our [appendix](verification-plan.md#appendix-packet-based-verification).

[^6]: I.e., doesn’t require compute to be shut down for long.

[^7]: Conditional on the Plan A scenario (the mutual chip declaration and inspection in 2029 carried out, and our chip tracking recommendation executed competently), our [covert project supplement](covert-ai-projects.md#section-2-preventing-covert-compute-procurement) estimates that a competently-executed PRC diversion effort would net a median of 0.51% of world compute (80% CI: 0.11% to 1.4%), implying roughly an 80% chance that total ‘dark compute’ stays under 1% of the world’s AI-relevant compute.

[^8]: We are uncertain about the compute-sensitivity of progress in the takeoff period (automated coder to superintelligence milestones). If we operationalize this (for simplicity) in terms of how much slower you go if you have 10x less compute, we think it's most likely to be somewhere between 2x to 6x slower (see [How much slower does takeoff go with 10x less compute?](https://www.lesswrong.com/posts/7jcPg79p3kD5ir3CL/how-much-slower-does-takeoff-go-with-10-less-compute) and the matching [model](covert-ai-projects.md#how-much-does-takeoff-slow-down-if-you-reduce-compute-by-10x-n) in the covert project supplement). The specific trajectories we expect hypothetical covert projects to follow in the Plan A scenario (including the effects of algorithmic progress leaking from legal projects) are modelled and explained much more carefully in our [covert project supplement](covert-ai-projects.md#how-we-model-the-ai-capabilities-progress-of-covert-projects).

[^9]: By known-to-exist, we are recommending that intelligence agencies know with high confidence at least that the compute exists, and who has it, not necessarily exactly where it is (though that is also helpful), because the first two conditions should be sufficient to make it impossible to exclude from a future mutual chip declaration with plausible deniability.

[^10]: In other words, without this measure in place, one strategy that an actor might pursue is to build the largest covert project they can get away with, and then wait until they make enough alignment progress such that they are confident they could win with their covert project. At this point they could pull out the deal, destroy the post-deal compute, and now their covert project would be the leading world project, with a high chance of success. This strategy is no longer likely to be viable if your adversary has a cold storage compute bank that dominates your covert project.

[^11]: There are tens of billions of phones, each around 0.1 - 1% as useful as an H100 for AI workloads, which still means tens of millions of H100-equivalents, i.e., ~10% of the total AI-relevant compute in the world.

[^12]: This means there will be plenty of cheap phones that have low local-AI capabilities, whereas phones or other consumer devices that have a lot of local, or ‘edge’ AI compute will be very expensive at first until there is robust edge verification.

[^13]: For example, technical details about the networking, e.g., optical speeds, bandwidths, frequencies.

[^14]: For example, maybe we think handoff risk has gone under 10%, and so we want to exit the deal via handoff if there is a greater than 10% risk that a violation using 1% of the verified compute in a given period would be catastrophic (i.e., our curve is under the 90% confidence, 99% coverage point).

[^15]: For example, the disclosure happening within an airgap, which should make it tolerable in most of the relevant cases.

[^16]: The outlook for resumed AI R&D is also important for driving continued AI investment.

[^17]: This is explored more in our [capabilities scaling strategy supplement](capability-scaling-strategy.md). There are also a few deeper layers of nuance here that complicate the picture, including what transparency regime is in place as discussed in our transparency supplement.

[^18]: An R&D efficiency spiral in AI research, where the feedback loop of smarter AIs → better research → smarter AI, holds through to AIs that we cannot control or align, and slowing down to invest in control/alignment is uncompetitive, locking companies and countries into a multipolar trap. Coordination, that is verified, is the path out.

[^19]: We define AI-relevant compute as any computational unit capable of achieving Total Processing Performance (TPP) of at least 4,000 and Performance Density (PD = TPP / die size) of at least 4. This definition is set just below the [A100 SXM GPU](https://www.nvidia.com/en-us/data-center/a100/), NVIDIA's state of the art chip in 2021.

[^20]: Note none of these quantities depend on how the work is divided into individual workloads. What matters is the pool the verifier samples from. If there are 100 different training runs going on simultaneously and the verifier samples uniformly at random across all their packets, then ‘the workload’ in the math below is the union of all 100. The per-workload framing in the worked example ([§A.4.1](verification-plan.md#a41-100k-token-backdoor-in-a-100t-token-training-run)) is a convenience for talking about one concrete attack.
