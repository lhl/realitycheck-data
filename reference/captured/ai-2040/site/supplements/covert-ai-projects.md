---
title: "Covert AI Projects"
byline: "Brendan Halstead, Thomas Larsen"
source_url: "https://ai-2040.com/supplements/covert-ai-projects"
retrieved_at: "2026-07-11T06:00:49+00:00"
conversion: "rendered HTML to GitHub-Flavored Markdown with Pandoc"
---

# Covert AI Projects

**Byline:** Brendan Halstead, Thomas Larsen

In the Plan A scenario, we propose international coordination to develop AI safely. Keeping risk at an acceptable level requires substantial slowdowns in the pace of AI development. A central blocker for this type of coordination is the risk that one party develops AI in secret, thus gaining an advantage.

Fortunately, it seems very hard to build and operate covert AI datacenters in a way that would be catastrophic. In the rest of this supplement, we’ll analyze how difficult it would be for China to defect from Plan A in secret, and the mitigations that can be put in place to prevent defection.[^1]

What successful defection would require

In summary, optimally subverting a competent implementation of our recommended Plan A policies would require China to:

1.  Decide to begin diverting chips before the chip transparency agreements are made (in the Plan A scenario, this would need to occur in 2028).

2.  Acquire on the order of 1.5M H100e (around 7% of counterfactual EOY 2028 Chinese stock) without being detected. The most promising options for acquiring this compute are: (i) diverting smuggled chips over the course of 2028, (ii) diverting older chips by claiming to have decommissioned and recycled them, and (iii) coordinating falsified production records across the semiconductor supply chain to hide some pre-deal production.

3.  Build illegal datacenters without being detected. The most promising strategy we’re aware of for doing this is to locate the datacenters underground to avoid satellite detection.

4.  Power and cool the underground datacenters. One strategy involves using small nuclear reactors to generate electricity onsite and rejecting heat by circulating water into a [large river](https://en.wikipedia.org/wiki/Water_cooling#:~:text=%5B11%5D-,Once%2Dthrough%20cooling,-(OTC)%2520systems%2520may&sa=D&source=editors&ust=1783739800541296&usg=AOvVaw0nKjefhDjpDU1mX3GeQHT_) or [deep water source](https://en.wikipedia.org/wiki/Deep_water_source_cooling) in a way that avoids an IR-visible thermal plume.

5.  Operate the sites without being detected for long enough to build extreme enough AI capabilities to significantly shift the geopolitical balance of power. This involves avoiding spies within the government, cyber operations, smarter AIs helping with covert project detection, satellite monitoring, and any agreed upon US/China government transparency (e.g. privacy preserving AIs reading classified info). If the US became suspicious (e.g. due to evidence from any of the items above), China would need to avoid giving concessions that would reveal their covert projects (e.g. physical US inspectors at potential covert project locations), while avoiding the possibility of the deal breaking down.

6.  Avoid the development or usage of lie detectors (or other AI tech that improves verification massively).

China could also do a smaller covert project, which would have a proportionally smaller footprint and detection likelihood, but would also make slower progress towards strategically relevant AI capabilities.[^2]

It will be impossible, in practice, for the US to confidently rule out a sufficiently small Chinese covert project. Therefore, the main questions of interest are:

1.  What is the largest size of covert project that can evade detection?

2.  On our current trajectory,[^3] at what time do covert projects pose a threat to the integrity of the deal and global security?

The answers to these questions will depend substantially on the overall scenario. However, in any scenario, the members of the Consortium will have the affordance to adjust their strategy to increase their lead over covert projects, primarily by reducing their rate of software progress at the cost of additional risk that the deal declines before sufficient alignment progress has been made, or by insisting on more robust detection technology before proceeding.

# Section 1: Overview of our strategy for covert project mitigation

This supplement outlines our plan for preventing this type of catastrophic defection from Plan A.

This diagram gives an overview of our strategy for handling covert projects. Elements of the strategy are covered across four supplements, as pictured above. In this section, we’ll give an overview of the entire strategy.

Covert project mitigation strategy overview - ai-2040.com

Defection from Plan A can happen on legal datacenters or covert datacenters. The legal datacenters are approved for AI development or usage, but are subject to verification to ensure that they are following those rules. Verification of the legal servers is the primary focus of the [Verification Plan](verification-plan.md).

This supplement will focus on the risk from covert projects, i.e. projects primarily using secret datacenters.

The main way that we can limit covert projects is by limiting their amount of compute: the covert project datacenters must be very small in order to go unnoticed. We can limit covert project compute through a combination of **preventing** covert projects from acquiring compute and **detecting** covert datacenters once they are constructed.

Compute for covert datacenters can either come from “stock” (compute produced before 2029) or “flow” (compute produced during or after 2029). We are optimistic about very strong control of the flow of new chips because under Plan A compute production is extremely carefully monitored using highly controlled fabs. (Concretely, we should be able to keep diversion to approximately zero and have very high confidence that total diversion is less than 100k H100e.) Verifying the flow of new chips becomes somewhat more difficult during the industrial explosion because the abundance of robots may make it much more viable to construct a secret chip supply chain. The Consortium can prevent this through verification methods applied to the robot workforce.

The stock of compute is already distributed and thus much harder to find, so we predict that a potential covert project would acquire their compute from existing stock. This means that a key priority in Plan A is estimating pre-deal stock and accounting for a high fraction of it.

Our median estimate for the amount of compute a competently-executed PRC covert project could divert is roughly 1.5M H100e (.5% of world compute at EOY 2028, costing around \$15B).

Software is much harder to limit than hardware. However, if enough software leaks, even very small covert projects will be able to develop extremely capable AI. Software progress in covert projects can be broken down into two categories: progress acquired from legal projects and software progress from research done by the covert project itself.

**Progress acquired from legal projects**. For most AI algorithms, security will be nearly impossible.[^4] Therefore, our primary line of defense here is to limit algorithmic progress made by the legal projects. Still, this will be the primary way that covert projects acquire AI algorithms for the majority of Plan A.

**Software progress made by the covert project.** This will be slow by default because of the extreme limitations on compute under which covert projects are operating. Additionally, Plan A aims to prevent covert projects from being able to use the most capable available AI systems for AI R&D. But, they may be able to gain access to highly capable AIs through several routes which could dramatically accelerate the covert project rate of software progress:

- **Distillation from the legal AIs.** We’re optimistic about [mitigating distillation via standard techniques like hiding intermediate computation](verification-plan.md#2031-restrictions-for-hardware-randd-and-other-high-risk-domains), but still expect the covert project to have access to somewhat more capable AI systems due to distillation.

- **Usage of the legal inference AIs to do AI research.** This can be mitigated by refusals by default.

- **Theft of the legal AIs and then training away refusals.** This can be mitigated by model weight security. We are much more optimistic about securing model weights than algorithms because of their size.

# Section 2: Preventing covert compute procurement

We estimate that, under competent US execution of our policies in Plan A, a competently-executed PRC diversion effort beginning one year in advance of the deal would be able to acquire **between** **0.1% and 1.4% (80% CI)** of the world’s AI-relevant compute at the start of the deal, without the US getting unambiguous evidence of violation. We show this in various units in the table below.[^5]

<table>
<colgroup>
<col style="width: 33%" />
<col style="width: 33%" />
<col style="width: 33%" />
</colgroup>
<tbody>
<tr>
<td></td>
<td><p><strong>Median estimate</strong></p></td>
<td><p><strong>80% CI</strong></p></td>
</tr>
<tr>
<td><p><strong>Fraction of world</strong></p></td>
<td><p>0.51%</p></td>
<td><p>[0.11%, 1.4%]</p></td>
</tr>
<tr>
<td><p><strong>H100e</strong> (Using our median estimate of world compute in Jan 2029)</p></td>
<td><p>1.5M H100e</p></td>
<td><p>[310k, 4.13M]</p></td>
</tr>
<tr>
<td><p><strong>IT equipment cost</strong></p>
<p>(Using our median estimate of $/H100e China would pay)</p></td>
<td><p>$15B</p></td>
<td><p>[$3.6B, $65B]</p></td>
</tr>
<tr>
<td><p><strong>Compared to our median estimate of the leading AI lab’s R&amp;D compute in Jan 2029</strong> (36M H100e)</p></td>
<td><p>24x less</p></td>
<td><p>[115x less, 9x less]</p></td>
</tr>
</tbody>
</table>

The rest of Section 2 justifies these numbers.

In Section 2.1, we explain our verification approach, which centrally involves accurately determining the amount of compute in the world, then tracing sales to their end user to verify the physical location of as much pre-deal compute as possible.

In Section 2.2, we describe the strategies covert projects could use to subvert our verification approach. All of these routes require taking action before the deal is implemented; here we assume China begins diversion one year prior to the deal:

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
<td><p><strong></strong></p></td>
<td><p><strong>Source</strong></p></td>
<td><p><strong>Chip origin</strong></p></td>
<td><p><strong>P(feasible)</strong></p></td>
<td><p><strong>Median [80% CI]</strong></p></td>
</tr>
<tr>
<td><p><strong>Smuggled Western chips</strong></p></td>
<td><p>2028 flow</p></td>
<td><p>US-designed</p></td>
<td><p>100%</p></td>
<td><p>0.23%</p>
<p>[0.02%, 1.17%]</p></td>
</tr>
<tr>
<td><p><strong>False decommissioning</strong></p></td>
<td><p>pre-2028 stock</p></td>
<td><p>US-designed</p></td>
<td><p>60%</p></td>
<td><p>0.31%</p>
<p>[0.21%, 0.42%]</p></td>
</tr>
<tr>
<td><p><strong>Concealed domestic production</strong></p></td>
<td><p>stock + flow</p></td>
<td><p>China-designed</p></td>
<td><p>25%</p></td>
<td><p>0.14%</p>
<p>[0.05%, 0.30%]</p></td>
</tr>
<tr>
<td><p><strong>Exempt military compute</strong></p></td>
<td><p>Verification-</p>
<p>exempt</p></td>
<td><p>either</p></td>
<td><p>Not estimated</p></td>
<td><p>not estimated</p></td>
</tr>
</tbody>
</table>

Finally, in Section 2.3, we forecast how much compute each route would yield and make an aggregate estimate for how much compute a covert project could acquire.

## Section 2.1: Policies for limiting covert project compute acquisition

AI-relevant compute produced after Plan A is implemented is carefully tracked and monitored.[^6] Therefore, the most feasible path for covert projects to acquire compute during Plan A is from compute that was produced before the deal’s implementation date.

The existing compute will eventually end up in one of the terminal states below:

Where pre-deal AI chips end up - ai-2040.com

In short, we recommend

1.  [Tracing the records of the](covert-ai-projects.md#recommendation-1-audit-the-semiconductor-supply-chain-to-get-an-accurate-record-of-all-pre-deal-compute-production) *[inputs](covert-ai-projects.md#recommendation-1-audit-the-semiconductor-supply-chain-to-get-an-accurate-record-of-all-pre-deal-compute-production)* [to AI compute production to get an accurate idea of how much compute was actually produced before the deal,](covert-ai-projects.md#recommendation-1-audit-the-semiconductor-supply-chain-to-get-an-accurate-record-of-all-pre-deal-compute-production)

2.  [Tracing the records of the](covert-ai-projects.md#recommendation-2-trace-declared-compute-sales-to-their-physical-end-use-location) *[sales and resales](covert-ai-projects.md#recommendation-2-trace-declared-compute-sales-to-their-physical-end-use-location)* [of finished AI compute to ultimately trace it to its current physical location](covert-ai-projects.md#recommendation-2-trace-declared-compute-sales-to-their-physical-end-use-location)

3.  [Using incentive programs and aerial imagery to locate any compute whose sale was not recorded or is otherwise untraceable.](covert-ai-projects.md#recommendation-3-locating-remaining-unaccounted-for-compute-via-incentives-and-aerial-imagery)

Respectively, these are focused on the leftmost node of the flowchart, the blue tree within the flowchart, and the Unrecorded Sales section of the flowchart.

### Recommendation \#1: Audit the semiconductor supply chain to get an accurate record of all pre-deal compute production

To exhaustively account for all pre-deal compute, we need to start from accurate declarations of pre-deal production. In other words, we need to ensure AI accelerator vendors (like Nvidia and Huawei) declare *all* of their pre-deal sales. To make underreporting of production as difficult as possible, we recommend that the US demand records from the various upstream suppliers involved in producing AI accelerators.

Concretely, you would start with sales declarations from Nvidia and AMD for merchant GPUs; Broadcom and Marvell for custom AI accelerators; and Huawei and Cambricon in China. Then these companies would declare their inventories, suppliers, and purchase history, for example:

- logic fabrication from TSMC, Samsung Foundry, Intel Foundry, and SMIC;

- high-bandwidth memory from SK Hynix, Samsung, and Micron;

- advanced packaging from ASE/SPIL, Amkor, and JCET.

Then these upstream suppliers would declare *their* suppliers, purchases, inventory, and cumulative production. At each layer, the flows can be cross-checked, such that underreporting production without introducing inconsistencies would require some combination of

- Underreporting purchases of upstream inputs, which means that the upstream supplier would also need to underreport production,

- Overreporting inventories of an upstream input, which would be caught during physical inspection of the declared inventories

- Overreporting losses in the production step, which would require all subsequent nodes to underreport their input flows to match.

Notably, many of the suppliers involved in producing Chinese chips are not headquartered in China. It is conceivable that the PRC could coordinate this falsification regardless. To further deter the PRC from attempting to underreport production, the US can

1.  Interview employees at Chinese wafer foundries, accelerator vendors, etc. as part of a [w](#id.6qel4dtdj9p)[histleblower program](#id.6qel4dtdj9p).

2.  Use national intelligence (such as cyber operations, human sources, etc) in the years leading up to the deal to search for evidence of falsification in the Chinese supply chain[^7].

We consider it likely but not certain that Chinese companies would make accurate disclosures under these conditions. Though we don’t include this as a core recommendation or rely on it in our estimates, the supply chain can and should take action before the deal to make the verification process easier ([example](https://nacicankaya.substack.com/p/tsmc-most-definitely-has-a-golden)).

### Recommendation \#2: Trace declared compute sales to their physical end-use location

Tracing chip sales to end-use location - ai-2040.com

We recommend that the Consortium verify the location of all pre-deal compute in two layers: exhaustively audit[^8] every compute owner above a size threshold by tracing vendors' sales records downward, and randomly sample the remaining tail of small owners, tracing each sampled unit of compute to its current physical location. The result is a certificate, at a chosen confidence level, upper-bounding how much compute could have been diverted to a covert project.

Our auditing proposal in detail

1.  Starting from Recommendation \#1's verified record of vendors' sales to direct customers, audit every direct customer above a size threshold T, then every above-threshold customer of an audited firm, recursively, until all unaudited recipients are below T.

    1.  For example, you might set this threshold at 0.01% of pre-deal world compute (30k H100e, costing ~\$200M at the time). T should be at or below the treaty's target bound on covert project size, so that any firm large enough to constitute a covert project by itself is audited deterministically.

    2.  By "audit", we mean "obtain all records of compute purchased, resold/transferred, or retained as inventory", as well as "physically inspect any compute the firm presently owns".

2.  Some recorded outflows cannot be traced onward. These are added in full to an untraced pool L, and counted as potentially diverted. The two main cases:

    1.  Sales to unauditable counterparties. If a firm's records show a sale to a buyer that cannot be produced for audit (e.g. a shell company, or a smuggler who kept no onward records), the entire sale is added to L. Since T is at or below the target bound, a single such sale above T is enough to block certification, so the Consortium should also investigate the seller's remaining records and refer the case to the tools of Recommendation \#3.

    2.  Unverifiable decommissioning claims. If a firm claims to have scrapped or recycled compute, the Consortium cross-checks the claim against recycler-side records (recyclers are themselves auditable counterparties), serial numbers where available, and actuarial fleet-attrition rates. Amounts that pass these checks are accepted; the rest is added to L. As above, an unverifiable claim above T blocks certification and warrants investigation.

3.  When this completes, every unit of pre-deal compute is either physically verified, added to L, or recorded as delivered to a below-threshold recipient. The verified record of these small deliveries (firm 1 received a_1 H100e, firm 2 received a_2, and so on) is the list Layer 2 samples from.

4.  Randomly sample H100e-units from that delivery record, and trace each sampled unit through any chain of resales until it either reaches a physically inspected chip or fails to.

5.  Draw one unit uniformly at random from all compute recorded as delivered into the tail. This selects a recipient firm with probability proportional to how much it received. Audit that firm: the compute it verifiably received must equal current holdings plus recorded onward sales plus documented attrition, with holdings physically inspected.

6.  Sales records don't distinguish individual chips, so the sampled unit is resolved proportionally within the account. If the firm holds 200 of the 500 units it received, the trace ends here with probability 200/500, and a chip must be produced for inspection. Otherwise it follows a recorded onward sale to the buyer, where the audit repeats.

7.  Each trace ends as a pass (a physically inspected chip) or a fail (an inspection shortfall, an unbalanced account, a buyer that cannot be produced, or an unverifiable decommissioning claim). An adversary who splits a large diversion across many sub-T shell buyers gains nothing: those sales appear in the delivery record, so sampled traces land on them in proportion to their size, and every such trace fails. Layer 2 then detects and measures the missing compute statistically.

8.  Sampled audits occur with minimal advance notice, and inspectors record chip serial numbers at every inspection. The same serial appearing in two inspections at inconsistent times is itself a violation. Without both measures, a covert project could pass audits with temporarily borrowed chips.

9.  Going forward, the Consortium prevents L from growing: post-deal transfers above a de minimis size are permitted only to registered auditable counterparties, and post-deal decommissioning requires witnessed destruction or serial-verified recycling.

The resulting certificate: with confidence 1 - delta, no covert project exceeds D + L. D shrinks with the number of clean sampled traces (roughly, n traces certify D of about (tail size / n) \* ln(1/delta)). L is a directly measured quantity that further auditing cannot reduce; reducing it requires the external-evidence tools of Recommendation \#3.

### Recommendation \#3: Locating remaining unaccounted-for compute via incentives and aerial imagery

**Direct observation of AI datacenters.** We are relatively confident that intelligence services could, in advance of the deal, *identify and locate every (non-specifically-concealed) AI datacenter in China*, using similar methods to Epoch, SemiAnalysis, and other commercial efforts. When they do eventually get inspected, the inspectors might find some of the untraceable compute. (This method does not help with compute that has been produced but not deployed in datacenters at the time of the deal, which might be around 50M H100e.)

**Buyback programs and amnesty for smuggling.** We want to incentivize whoever owns the untraceable compute, or anyone who may have information on it, to come forward and reveal its location to the Consortium. The most obvious reason not to reveal missing compute is if you’re using it as part of a covert AGI project. Besides that, two reasons why private actors might be reluctant to come forward is

1.  If the compute was obtained illegally in the first place, (e.g. smuggling, or fraud or theft for the purpose of smuggling), and the person fears punishment if they come forward, or

2.  if the person believes they can receive a better reward selling the compute to some other actor (e.g. a state attempting a covert AGI project)

We recommend combating both of these incentives if the amount of missing compute remains unacceptably high after the previous steps are taken. For 1), states should provide complete amnesty to anyone who can deliver missing compute to the inspectors. For 2), states should offer to pay above-market prices for missing compute. Note that committing to this creates a perverse incentive in favor of smuggling, so should only occur if needed to account for additional missing compute.

## Section 2.2. Covert project strategies for acquiring compute

**Source \#1: Diverting from smuggled flow**

*Applies to: Western-made 2028 flow*

Even in Plan A, we forecast that significant compute will still be smuggled to China before the deal is implemented. Since the smugglers will have already broken/falsified some links in the chain, and may not keep similarly detailed records to legitimate suppliers, it may be possible to purchase compute under false identities without arousing much suspicion when supply chain tracing eventually arrives at a supplier.

Speculatively, Chinese intelligence services could set up a fake company ostensibly from a different US adversary country (e.g. Russia), and purchase chips under that identity. Since such a country might also have incentive to hide chips, the eventual compute sales tracing might not be able to conclude whether the chips are in (e.g.) Russia or elsewhere.[^9]

**Source \#2: Concealing some pre-deal domestic production**

*Applies to: China-designed pre-2028 stock AND pre-2028 flow.*

To hide compute from the resale tracing and physical inspection process, Chinese intelligence services could arrange for domestic accelerator vendors to underreport their pre-deal sales. The [compute production tracing](covert-ai-projects.md) efforts aim to prevent this by accounting for all the accelerators which were physically produced. Chinese intelligence services would need to arrange for accelerator vendors like Huawei to understate their orders from the various supplier companies, and for those suppliers to understate their production. Those suppliers have their own suppliers, who would also need to align their statements. (For example, to fabricate the logic dies for Huawei’s chips, SMIC depends on silicon wafers from a different firm.)

Some elements of the supply chain will be in foreign countries, making them harder for Chinese intelligence services to manipulate. On the other hand, some critical bottlenecks like high-bandwidth memory are likely being smuggled, which could complicate supply chain tracing.

To avoid having to falsify records from dozens of different upstream suppliers, missing production could be explained by varying production yields. (e.g. in lithography, some fraction of the dies on each wafer will have defects, rendering those dies useless. Foundries aim to optimize this yield, but it requires ongoing R&D and can vary over time, especially at Chinese foundries as they race to catch up to TSMC.) However, any intermediate input flow whose existence is denied by understating yields still needs to be secretly made into the finished product. (continuing the example above, understating yields to acquire untracked logic dies would still require untracked HBM (from a different supplier) and untracked packaging (also done elsewhere) to make into a finished accelerator package). So yield falsification only *reduces* the number of firms whose coordination would be needed.

The ideal case would be manipulating yield at the final assembly stage. As far as we know, yields here are much higher and more predictable than at earlier stages, so this seems infeasible to significantly falsify.[^10]

Overall, this strategy seems quite risky, as each additional firm added increases the number of opportunities for mistakes and for leaks. However, it’s possible the whistleblower/interview/HUMINT program are less effective than we expect, or that this sort of multi-firm falsification under scrutiny is more routine for Chinese intelligence services than we expect.

**Source \#3: Diverting from stock via false decommissioning**

*Applies to: Western-made pre-2028 stock*

By default, some compute will be decommissioned between its purchase and the start of the deal. This poses an issue for compute sales tracing, since (as done today) decommissioning does not involve retroactively-verifiable destruction of the chips.

How much compute will be decommissioned by default?

For normal chip lifetimes, this is a small amount. (e.g. a common depreciation schedule is 5 years, so with an annual compute growth rate of 2-4x per year over the 5 years preceding the deal, compute whose fifth birthday happens before the deal will be less than 2^-5 – 4^-5, or 3.1% to 0.1% of global compute at the beginning of the deal.)

We understand US hyperscalers to have detailed records of the entire decommissioning process. For example, AI servers decommissioned by Microsoft are sent to Microsoft Circular Centers, where high value components (AI accelerators would certainly qualify) are removed and assessed for internal reuse, resale, donation (for educational purposes), or recycling. If we assume that US hyperscalers (who currently own 71% of global compute) can provide an accurate count of their decommissioned chips, the decommissioned fraction is reduced to between 0.9% and 0.03% of cumulative global compute production at the start of the deal.

We are less sure about the situation with smaller compute operators and for Chinese compute operators.

As a potential diversion strategy, Chinese intelligence services might arrange to have large Chinese clouds decommission their US-designed compute[^11] in advance of the deal (perhaps justified as a political demonstration of Chinese semiconductor self-sufficiency, or to hide evidence of previous smuggling[^12]), with fake recyclers set up to accept the hardware and stockpile it rather than recycling it. Decommissioning a large fraction of compute in advance of the deal would create ambiguity about whether to treat it as possibly used for a covert project, since even if China were acting honestly, it might have no way to prove that the chips had truly been recycled.

To the extent feasible, we recommend the US intelligence community surveil the Chinese IT equipment recycling industry to guard against this strategy.

As a speculative potential strategy for making decommissioning look less suspicious, Chinese intelligence services might use cyberattacks to induce what appear to be hardware failures in installed devices, inducing unknowing datacenter operators to return some fraction of their installed hardware to server or GPU manufacturers (e.g. Huawei) for RMA, or otherwise to recycle them. Chinese intelligence services would then divert these shipments and have them documented as recycled.

**Source \#4: Using declared military compute to aid a covert AGI project**

If the US and China aren’t able to negotiate away their unverified military compute, it could be used for AI development. The amount of military compute that could be diverted to a covert project is entirely a function of how the negotiations proceed. There are a few different ways the US could negotiate to minimize the amount of unverified military compute. To *minimize the maximum* amount of compute that could possibly be used for military AI development, the US should push to bring *all* military compute under inference-only verification. This has the drawback of incentivizing covert projects where previously they might have been judged not worthwhile, but it does improve the worst-case scenario (covert project AND declared military compute working together).

Alternatively, the US could accept a greater quantity of unverified military compute, perhaps tying the amount to the amount of missing pre-deal compute to incentivize bringing any covert stockpiles into the open. Under some assumptions these strategies might reduce the *expected* total amount of compute used for military R&D, at the cost of increasing the total amount usable by an aggressive adversary.

Overall, we recommend that the US should push to bring all military compute under inference-only verification.

## Section 2.3 Quantitative Estimates

We consider two estimation methods for the amount of compute a high-competence covert project could acquire. We trust the first more than the second, and treat the second method mainly as a sanity-check. Currently, none of these include using declared military compute to aid a covert AGI project.

<table>
<colgroup>
<col style="width: 25%" />
<col style="width: 25%" />
<col style="width: 25%" />
<col style="width: 25%" />
</colgroup>
<tbody>
<tr>
<td><p><strong>Estimate</strong></p></td>
<td><p><strong>Fraction of global total</strong></p></td>
<td><p><strong>H100e, assuming 289M at 2029.0</strong></p></td>
<td><p><strong>Description</strong></p></td>
</tr>
<tr>
<td><p>1</p></td>
<td><p>Median 0.51%</p>
<p>80% CI [0.11%, 1.4%]</p></td>
<td><p>Median 1.5M</p>
<p>[310k, 4.13M]</p></td>
<td><p>Bottom-up estimate combining the plausible diversion strategies discussed above.</p></td>
</tr>
<tr>
<td><p>2</p></td>
<td><p>Median 0.23%80% CI [0.022%, 2.34%]</p></td>
<td><p>Median 660k</p>
<p>[63k, 6.8M]</p></td>
<td><p>Based on a rough estimate of how much money the PRC could spend secretly purchasing AI servers in 2028, as well as our forecasts of $/H100e in 2028</p></td>
</tr>
</tbody>
</table>

### Method \#1: Bottom-up

In this method, we assume China simultaneously pursues all the acquisition strategies we identified above. We give distributions over the compute that could be acquired by each strategy, as well as the probability that each strategy is feasible. We then aggregate these together to get a distribution over the total amount of compute diverted.

|  |  |  |  |
|----|----|----|----|
| **Diversion route** | **P(feasible)** | **Median** | **80% CI** |
| Decommissioning pre-2028 stock | 60% | 0.31% | \[0.21%, 0.42%\] |
| Underreporting 2028 domestic production | 25% | 0.14% | \[0.05%, 0.30%\] |
| Buying smuggled western chips in 2028 | 100% | 0.23% | \[0.02%, 1.17%\] |

**Source \#1: False decommissioning**

If supply chain tracing and datacenter tracking are effective, installed compute cannot be removed from datacenters without explanation. So either there will need to be an explanation, or supply chain tracing and datacenter tracking will need to be subverted. We think the latter is likely infeasible and would contribute a relatively small amount of compute if feasible, so we have excluded it for simplicity.[^13] Therefore, the only way to divert pre-2028 stock is to falsely decommission chips that still work.

Parameter estimates and rationales

<table>
<colgroup>
<col style="width: 33%" />
<col style="width: 33%" />
<col style="width: 33%" />
</colgroup>
<tbody>
<tr>
<td><p><strong>Parameter</strong></p></td>
<td><p><strong>Estimate</strong></p></td>
<td><p><strong>Rationale</strong></p></td>
</tr>
<tr>
<td><p>Probability that decommissioning is feasible at all to do deniably</p></td>
<td><p>60%</p></td>
<td><p>Intuitive guess.</p></td>
</tr>
<tr>
<td><p>US-designed fraction of pre-2028 stock in China</p></td>
<td><p>45%</p></td>
<td><p>If domestic production is 3.7% of world, and (as <a href="https://docs.google.com/spreadsheets/d/1fIPU1OkgnKgsCiQqcj18RXRNlqqfL1YDGCjeWAeXC7s/edit?gid=2003669200#gid=2003669200&amp;range=O57">Plan A side panel data</a> says) 6.7% of world stock at 2028.0 is located on Chinese soil, then the US-designed share must be 45%. (or 3% of the world stock at 2028.0)</p></td>
</tr>
<tr>
<td><p>Fraction of pre-2028 US-designed compute located in China that can be falsely decommissioned before 2029.0, conditional on this being feasible to do at all deniably</p></td>
<td><p>22%</p>
<p>80% CI: [15%, 30%]</p>
<p>Beta</p></td>
<td><p>Intuitive guess. If the top few clouds (Alibaba, Tencent, ByteDance, etc) own 60% of US-designed compute in China, and they decommission the oldest p25–p50 of their US-designed compute as part of this scheme, then this is 15–30% of the US-designed stock. (or 6.75% – 13.5% of the 2028.0 total PRC stock, using 45% as the parameter above).</p></td>
</tr>
</tbody>
</table>

We estimate that conditional on false decommissioning being feasible, it yields 6.7% – 13.4% of the 2028.0 total PRC stock, and 0.45% – 0.9% of the 2028.0 world stock, and **0.21% – 0.42% of world pre-deal compute, conditional on the false decommissioning scheme being feasible at all (60%).**

**Source \#2: Diverting pre-deal flow**

This would entail [concealing some pre-deal domestic production](covert-ai-projects.md) and routing it directly into storage for a covert project.

Parameter estimates and rationales

<table>
<colgroup>
<col style="width: 33%" />
<col style="width: 33%" />
<col style="width: 33%" />
</colgroup>
<tbody>
<tr>
<td><p><strong>Parameter</strong></p></td>
<td><p><strong>Estimate</strong></p></td>
<td><p><strong>Rationale</strong></p></td>
</tr>
<tr>
<td><p>Probability that concealment of domestic production is feasible</p></td>
<td><p>25%</p></td>
<td><p>Intuitive guess, see the discussion of the difficulties <a href="#id.8f05c939oyy6">here</a>. I could update based on learning more about the Chinese semiconductor ecosystem or the historical effectiveness of whistleblower programs like ours.</p>
<p>My initial guess was 15%, Romeo thinks 35% for this, so we take the average and use 25%.</p></td>
</tr>
<tr>
<td><p>Fraction of 2028 domestic production which can be concealed, conditional on feasibility above</p></td>
<td><p>7%</p>
<p>Beta distribution with p90 = 15%.</p></td>
<td><p>Intuitive guess, p90 based on the idea that removing “one Chinese hyperscaler” (e.g. 10-20%) would probably be too obvious. Though note that this is different from removing one hyperscaler from the total compute in China; some of that will be legally imported or smuggled US-designed chips.</p></td>
</tr>
</tbody>
</table>

Assuming that the fraction of global compute produced by China stays roughly constant, and accounting for the [2028 flow](#kix.n9c95482a1ct), we estimate that this route yields a **median of 0.13% (80% CI: \[0.05%, 0.31%\]) conditional on being feasible at all (25%).**

**Source \#3: Diverting smuggled chips**

Parameter estimates and rationales

<table>
<colgroup>
<col style="width: 33%" />
<col style="width: 33%" />
<col style="width: 33%" />
</colgroup>
<tbody>
<tr>
<td><p><strong>Parameter</strong></p></td>
<td><p><strong>Estimate</strong></p></td>
<td><p><strong>Rationale</strong></p></td>
</tr>
<tr>
<td><p>Fraction of 2028 compute sales smuggled to China</p></td>
<td><p>2%</p>
<p>[0.66%, 6.0%]</p>
<p>LogNormal</p></td>
<td><p>Currently, Epoch’s median <a href="https://epoch.ai/publications/chip-smuggling">estimate</a> is that 3.2% of compute sold through 2025 Q4 was smuggled to China. This might go up in the future due to increased demand for compute in China as frontier AI becomes a bigger business there (or as AI compute’s importance for national security becomes more obvious to the CCP). It might go down in the future due to improved US enforcement.<br />
<br />
<a href="#h.daipbfer72sz">Epoch’s 80% CI for cumulative smuggling</a> through Q4 2025 is p10=1.7%, p90=6.4%. This is factor 1.8 to 2 uncertainty for p50 to p10 and p90. We will go with factor 3 uncertainty due to this being farther into the future.</p>
<p>I am shifting the median down to 2% as in the Compute Forecast, deferring to Romeo, who gives this as a point estimate based on improved enforcement. I think this makes sense conditional on Plan A.</p></td>
</tr>
<tr>
<td><p>Smuggled compute for which the end customer cannot be identified</p></td>
<td><p>25%</p>
<p>[2.5%, 70%]</p>
<p>Beta</p></td>
<td><p>Intuitive guess. I think it is probably less than half. I think my uncertainty could be reduced by learning more, but not super easily.<br />
<br />
An example of an accurately-recorded chain of custody:</p>
<ul>
<li>Nvidia has a record of selling some number of units to the direct customer (e.g. a server OEM like Dell)</li>
<li>Dell assembles the accelerators into servers and has a record of how many servers it sold to Nebius</li>
<li>Nebius has a record of how many servers it purchased and which datacenters they're located in.</li>
</ul>
<p>I think smuggled chips can have an accurately-recorded chain of custody if all the entities involved have some record of who they sold to, even if that record isn't what they'd show to auditors. However, if at some point they were sold to an entity who used a false identity, or sold "cash-only", such that the reseller isn't sure where the chips went to, that doesn't count. But if the CIA knows where the chips ended up and the information can be used in the supply chain tracing process without compromising sources and methods or whatever, that does count.</p></td>
</tr>
<tr>
<td><span></span>
<p>2028 flow as a fraction of cumulative compute sales to date at time 2029.0</p></td>
<td><p>53%</p></td>
<td><p><a href="https://docs.google.com/spreadsheets/d/1fIPU1OkgnKgsCiQqcj18RXRNlqqfL1YDGCjeWAeXC7s/edit?gid=2003669200#gid=2003669200&amp;range=R36">Plan A side panel data</a> has 154M H100e added in 2028 and 289M H100e total as of 2029.0. 154 M / 289 M = 53%.</p></td>
</tr>
</tbody>
</table>

Assuming independence of these parameters and simulating, this yields 0.44% of the 2028 flow \[0.04%, 2.19%\], or **0.23% of world compute at time 2029.0, 80% CI \[0.02%, 1.2%\]**.

![](../assets/supplements/covert-ai-projects/image8.png)

The distribution of total compute diverted, aggregating across all the methods discussed above.

### Method \#2: Military-spending-based estimate

The numbers below are estimated less precisely than the numbers in Method 1, as this is mainly used as a sanity check.

Parameter estimates and rationales

<table>
<colgroup>
<col style="width: 33%" />
<col style="width: 33%" />
<col style="width: 33%" />
</colgroup>
<tbody>
<tr>
<td><p><strong>Parameter</strong></p></td>
<td><p><strong>Estimate</strong></p></td>
<td><p><strong>Rationale</strong></p></td>
</tr>
<tr>
<td><p>China’s military spending in 2028</p></td>
<td><p>$400B</p>
<p>80%: [350B, 457B]</p>
<p>LogNormal</p></td>
<td><p>China’s <a href="https://www.macrotrends.net/datasets/global-metrics/countries/chn/china/military-spending-defense-budget">official military budget</a> for 2023 was $296.44B. It grew roughly linearly over the preceding decade, adding an average of $13.2B per year. Extrapolating this to 2029, would predict official military spending to reach $362.4B.</p>
<p>We use something closer to an extrapolation of <a href="https://www.sipri.org/databases/milex">SIPRI’s estimates of military spending</a> (which are broader than the official budget).There are subtleties around PPP vs fixed-year exchange rate vs nominal which we’re currently ignoring.</p></td>
</tr>
<tr>
<td><p>Fraction of annual budget China can spend secretly buying AI servers</p></td>
<td><p>2%80%: [0.2%, 20%]LogNormal</p></td>
<td><p>Intuitive unanchored guess. When asked, Claude suggested a number more like 15% – 20%.</p></td>
</tr>
<tr>
<td><p>$/H100e for newest US AI servers in 2028</p></td>
<td><p>$8k</p></td>
<td><p>Geometric mean of the 2028.0 and 2029.0 values in <a href="https://docs.google.com/spreadsheets/d/1fIPU1OkgnKgsCiQqcj18RXRNlqqfL1YDGCjeWAeXC7s/edit?gid=2003669200#gid=2003669200&amp;range=R36">Plan A side panel data</a>.</p></td>
</tr>
<tr>
<td><p>Smuggling markup %</p></td>
<td><p>+100%</p>
<p>[+50%, +200%]</p></td>
<td></td>
</tr>
<tr>
<td><p>Decommissioned server markdown</p></td>
<td><p>-50%</p></td>
<td><p>Cheaper than the US-market $/per H100e surely, otherwise you could arbitrage by buying compute in the US and selling it directly to recyclers. But Chinese intelligence services might need to pay a bit more than is standard for recyclers since they need to capture the market, maybe 1.2x, or the cloud execs might just be told which specific recyclers to use, or the real recyclers could be put out of business.I will just go with half off.</p></td>
</tr>
<tr>
<td><p>Decommissioned to smuggled ratio</p></td>
<td><p>3:5.5</p></td>
<td><p>Based on the numbers in Method 1.</p></td>
</tr>
<tr>
<td><p>H100e in the world at 2029.0</p></td>
<td><p>289M H100e</p></td>
<td><p>From the <a href="https://ai-2040.com/supplements/compute-supplement">compute supplement</a>.</p></td>
</tr>
</tbody>
</table>

Simulating the distributions in the table above yields a **median of 0.23% of global compute, with an 80% CI of \[0.022%, 2.34%\].**

# Section 3: Detecting covert AI infrastructure

*This section is more speculative than the previous section. We are not experts in any of the relevant fields and may be overlooking important considerations.*

In this section we go over:

- Methods for detecting covert projects (Section 3.1)

- Strategies that covert projects might pursue to avoid these detection methods (Section 3.2)

- Quantitative estimates for how well detection will work, on what timescales, and how this depends on covert project scale (Section 3.3).

## Section 3.1 Plan A strategies for detection

**Method \#1: Tracking waste heat**

By conservation of energy, each megawatt of electricity going into a datacenter must be matched with a megawatt going out in some form (mostly as heat). The standard means of rejecting heat from datacenters produce distinctive signatures visible from space, and hiding or disguising these signatures seems to be the primary constraint on covert datacenter concealment.

Modern AI servers are designed to use liquid cooling, where coolant is pumped through IT equipment to absorb heat. The coolant dumps its heat to water, which is normally pumped out of the data halls and cooled by outdoor chillers. These chillers are either air-cooled or water-cooled.

*Air-cooled* chillers run cool air through finned condenser coils, heating the air by ~10-15 degrees C. It is possible to hide the chillers from direct view, but the warmed air eventually has to escape to the atmosphere, and whatever aperture it leaves through will equilibrate to a warmer temperature than the surrounding surfaces. These warmed surfaces emit in the IR spectrum, which can be seen from space. Technology exists for minimizing the IR signature from hot exhaust ports (for example, on low-observable aircraft like the F-117).[^14] We are somewhat skeptical that this could be applied successfully against persistent satellite monitoring, but it could be possible. Of course, making these exhaust ports [invisible](covert-ai-projects.md#method-2-invisible-datacenters) isn’t strictly necessary, they could instead be disguised as part of a legitimate industrial facility.

*Water-cooled* chillers transfer heat from the datacenter cooling loop to another flow of water which is evaporated in a cooling tower. Under certain weather conditions, the water vapor condenses to form visible clouds. We are unsure how hard these would be to hide consistently.

![](../assets/supplements/covert-ai-projects/image1.png)

Condensation visible above cooling towers at the [Google Council Bluffs (East)](https://epoch.ai/data/data-centers/satellite-explorer/GoogleCouncilBluffsEast) datacenter, rejecting ~190 MW of heat.

Another method for rejecting heat is simply dumping the hot water into a river or sea, a method commonly used to cool nuclear power plants.[^15] Doing this without creating an IR-visible thermal plume is hard, especially since time-averaging over a yearslong operating period allows for resolution of very minute heat differences. It may be possible to hide the thermal signature amid existing sources, or use multiport diffusers at depth to disperse the plume over a wide enough area to avoid detection.

![](../assets/supplements/covert-ai-projects/image5.png)

[Landsat images of the thermal plume from the Haiyang Nuclear Power Plant](https://www.mdpi.com/2076-3417/15/2/738), cooling two 1.1 GWe reactors on China’s eastern coast.

**Method \#2: Other sources of IMINT/MASINT**

[Interferometric synthetic-aperture radar](https://en.wikipedia.org/wiki/Interferometric_synthetic-aperture_radar) (InSAR) seems potentially useful for detecting the construction phase of a covert datacenter project. Based on measuring minute displacements of the earth’s crust over time caused by tunneling, an [LLNL technical report](https://www.osti.gov/servlets/purl/1036847) investigated using this for characterizing underground construction in a known location, but it seems less well suited to noticing an unknown facility.[^16] It might be useful to gain additional evidence that a suspicious site is in fact a covert datacenter (e.g. by observing the shape of the excavated volume).

Any underground excavation needs to move the dirt and rock (termed “spoil”) to the surface. This may be hard to hide: options include hiding the excavation in another industrial project, putting tunnel entrances inside buildings and shipping out the spoil in trucks, or dumping the spoil into rivers.

Finally, the space-based ground-moving target indicator (GMTI) system currently under development by the US Space Force and NRO could be used to track individual logistics vehicles involved in constructing or operating a covert datacenter, depending on the program timeline.[^17] We are unsure how much this would aid detection, but to the extent it can be modeled as “a video map showing every unobstructed vehicle in China,” it seems extremely useful in conjunction with the massive amounts of AI labor that Plan A would bring. If the system needs to be tasked to a narrow area to track vehicles, it becomes less useful for discovering remote sites, but still useful for gathering evidence about an area already flagged as suspicious.

**Method \#3: SIGINT**

Building covert datacenters would require specialized contractors. For example, following the strategy we discuss below in [Building invisible datacenters](covert-ai-projects.md), you would need

1.  Excavation

2.  Hydraulic engineering, to design and build the hidden cooling intake structure and outfalls

3.  Nuclear engineering

4.  All the contractors and disciplines involved in a normal datacenter project

5.  Possibly TEMPEST or equivalent

It seems plausible that the US could identify a relatively small number of contractors among whom one would almost certainly be involved in a covert project. Cyber operations against all of those firms might be sufficient to rule out the existence of a covert project. We are uncertain about the tractability and potential consequences of doing this. Relevant public information includes the [NSA’s breach of Huawei in 2010](https://www.nytimes.com/2014/03/23/world/asia/nsa-breached-chinese-servers-seen-as-spy-peril.html), in which they reportedly “obtained information about the workings of \[Huawei-produced networking products\] and monitored communications of the company’s top executives”.

**Method \#4: HUMINT**

Though counterintelligence would likely carefully vet the individuals with full, incriminating knowledge of a covert AI project, it seems possible that foreign intelligence assets would be read into the program. Obviously very little public information is available to estimate how likely this is. Our vague sense is that China is considered one of the more difficult countries for Western HUMINT collection.[^18]

As part of the deal, we recommend that the US negotiate for a whistleblower program under which anyone with evidence of compute diversion, covert AI datacenter construction, or other deal-undermining activities can be interviewed and guaranteed protection against retaliation. We are uncertain about how much diplomatic allowance here is realistic, considering that a program like this would also aid normal non-AI-related HUMINT efforts in China. It’s possible that having a neutral third party operate the whistleblower program in China would be more acceptable than if the US were operating it.

**Method \#5: AI silver bullets**

*Note: Everything in this section is significantly more speculative than the rest of this document because it assumes extreme AI capabilities.*

During plan A, we scale to extremely capable AI; reaching AI as capable as top human experts at everything. This accelerates economic and scientific progress, which could substantially improve detection capabilities:

1.  **Reliable Lie Detectors.** AIs could accelerate the development of reliable lie detectors. Existing lie detectors (e.g. polygraphs) can relatively easily be fooled. Reliable lie detectors might be developed in the near future over the course of normal human technological development, but extreme level of AI capabilities could accelerate the timeline. It’s also unclear to what extent the development of lie detectors would be politically accepted. If it’s possible for a regime with a covert project to decline being subject to a lie detector on principle, lie detectors won’t be helpful. On the other hand, the US could leave the deal unless China and/or other counterparties agreed to submit senior leaders to lie detection.

2.  **Privacy preserving AI verification technology.** AIs could enable intrusive verification to be done in a privacy preserving fashion, i.e., without leaking unacceptable information. This could be implemented as follows. First, place a huge number of sensors (e.g. cameras, thermometers), and mobile robots across China, such that if the US were able to observe each of them, they would be confident there is no Chinese covert project. Then, give all of that information to an AI trained by the US on a secure server on Chinese soil, and have the AI analyze that information for worrying signs. Finally, allow the AI to communicate a very high level summary of its findings, (for example, “Is China running a covert project?”), and delete the rest of the information. In principle, this approach could enable verification intrusive enough to usefully rule out covert projects without divulging any sensitive state secrets.

3.  **Extreme industrial verification.** By 2035, real US GDP in Plan A has grown by a factor of 25 relative to today. This enables extreme feats of industrial capacity. In an extreme case, all relevant manufacturing and industrial processes (e.g. aluminum plants that could be used to hide the waste heat of a covert project) could be disassembled and replaced/reassembled in a verified location (i.e., a robot SEZ). Again, there may not be political willingness to pay this cost, however, if there is substantial pressure (e.g. because both sides strongly want to continue the cooperative Plan A regime, but there is some evidence of a covert project, so one side wants higher assurance), it is plausible that this could happen, especially if combined with privacy preserving AI verification.[^19]

AIs will be making vast amounts of scientific progress over the course of Plan A (probably something like the equivalent of 100s of years of human equivalent progress over the course of the 2030s). Historical technological progress has resulted in all sorts of technologies that are helpful for detecting covert projects that would have been very hard to predict far in advance (e.g. satellite monitoring). We should expect all of this progress to result in improved detection methodologies in hard to predict ways. We should similarly expect that the technological progress would help concealment of covert projects as well; however, our general guess is that we expect technological progress to favor verification over concealment.

## Section 3.2 Covert project strategies for avoiding detection

In this section, we cover strategies that covert projects could take to avoid detection (classified as “invisible” or “disguised”.

**How distributed would covert datacenters be?**

Why one big datacenter instead of many small ones? Covert projects would aim to minimize project detection hazard per unit compute. At sufficiently small scales (e.g. a single 8xH100 server), detection hazard per site seems to scale sublinearly with site size (the detection risk to a group of four different 8xH100 servers in four different cities is higher than if all four servers were placed in a single rack). To minimize detection hazard per unit compute, you should therefore increase site size up to the point where detection hazard per site starts to scale superlinearly with site size, or until some other constraint prevents you from scaling up further.

### Method \#1: Disguised Datacenters

Compared to “invisible datacenters”, “disguised datacenters” have the disadvantage that any specific, visible facility could be subject to focused scrutiny and potentially challenge inspection.[^20] For example, the US could assemble a ranked list of China’s largest industrial loads and task satellites to frequently revisit them, collect SIGINT on the companies that ostensibly operate them, and attempt to recruit human sources who work there or live nearby. For a plant that produces a visible material output, it seems plausible to directly track shipments out of the facility and compare that with the heat rejection. (e.g. a datacenter disguised as an aluminum smelter would produce far less aluminum than is typical for a smelter of similar power draw.) You could try to get around this by making the datacenter a small fraction of the total power draw (e.g. 1% – 10%), but this would restrict the datacenter to on the order of 10 MW – 100 MW (we are not aware of any industrial loads on the order of 10 GW or higher.)

However, “invisible datacenters” require more complicated engineering and may not be feasible, especially against potential new AI-produced remote sensing capabilities developed during Plan A.

Some specific industrial facility types that might be useful cover stories:

1.  Aluminum smelters. China produces 43 MT of aluminum per year, aluminum smelters require ~1.6 gigawatts per Mt/yr, which naively implies ~70 GW of aluminum smelting capacity in China.

2.  Nuclear power plants.

3.  Combustion power plants

**Example: hiding a datacenter under an aluminum smelter**

In this example, the IT equipment would be located underground, with any excavation happening indoors to avoid visible spoil piles or excavation equipment. The power would be diverted from an onsite coal plant or grid connection (ostensibly to support the smelter). This would require the facility to produce less aluminum than its power draw or thermal signature would imply. But based on our research, it doesn’t seem possible to accurately measure the actual aluminum shipped from an aluminum smelter using national technical means.[^21] Though the heat signature of a datacenter is different than that of an aluminum smelter, it doesn’t seem obviously thermodynamically prohibited to design a cooling system which dissipates heat from the IT equipment in a way that resembles the heat dissipation from aluminum smelters.

### Method \#2: Invisible Datacenters

Trying to make a datacenter look like *nothing* seems more complex than making it look like something else. The biggest difficulty we’ve identified is hiding the heat rejected by the IT equipment (and any onsite power generation). In theory, all the equipment can be built underground and shielded from the view of satellites, but the heat needs to leave the facility somewhere. See the [Remote sensing, IMINT, and MASINT](covert-ai-projects.md) section. Besides the ongoing signatures, the initial construction period will also show activity, though avoiding detection has some precedent.

**Example: once-through cooling + nuclear power**

One potential strategy might be to build or extend an existing underground facility, install sufficiently many small nuclear reactors there to power the IT equipment, build an intake structure deep underwater on the coast, and use some sort of deep-water multiport-diffuser type design for the outfall to try to ensure that the hot cooling water dilutes to a temperature below the IR noise floor before reaching the surface. We aren’t sure whether a diffuser could be designed to those requirements, but it seems plausible. If so, a facility of this type seems quite difficult to detect via remote sensing once operational. The infrequent or nonexistent refueling requirements of the nuclear reactors would make even full knowledge of China’s electrical grid, natural gas distribution, etc. insufficient to locate the facility. We do not think [existing technologies](https://www.ctbto.org/resources/for-the-media/press-releases/chinese-monitoring-stations-now-sending-data) for detecting hidden nuclear reactors would be effective in this case, but again, we are not experts and could be wrong here.

### Hybrid strategies

China could also target “invisibility” for some aspects of the facility while disguising others. For example, it might be possible to site the IT equipment and power generation inside a logistics warehouse (e.g. receiving shipments of diesel fuel by truck). This has the advantage that there are many logistics warehouses, so the close-scrutiny consideration mentioned above might not apply. However, since a logistics warehouse doesn’t reject much heat normally, the cooling would need to be rendered “invisible” via one of the techniques discussed above.

## Section 3.3 Quantitative estimates

**How much datacenter capacity does the diverted compute require?**

Parameter estimates and rationales

<table>
<colgroup>
<col style="width: 33%" />
<col style="width: 33%" />
<col style="width: 33%" />
</colgroup>
<tbody>
<tr>
<td><p><strong>Parameter</strong></p></td>
<td><p><strong>Estimate</strong></p></td>
<td><p><strong>Rationale</strong></p></td>
</tr>
<tr>
<td><p>2026.0 US IT power per H100e (at max utilization)</p></td>
<td><p>833 W/H100e</p></td>
<td><p><a href="https://docs.nvidia.com/dgx-superpod/reference-architecture-scalable-infrastructure-gb200/latest/_downloads/238ab33ee345a7241fc2f15eedc2ff6c/RA11338001-DSPGB200-ReferenceArch.pdf">DGX GB200 SuperPOD reference architecture</a> p.6. One Scalable Unit of 8 NVL72 servers has a TDP of 1.2 MW, so 150 kW per server, including InfiniBand and Ethernet networking, management nodes, and storage.</p>
<p>We then divide by 2.5 * 72 H100e per server to get 833 W/H100e.</p></td>
</tr>
<tr>
<td><p>Average US power efficiency progress per year, 2026.0–2028.0</p></td>
<td><p>1.37x/year</p></td>
<td><p>Averaging the three relevant cells in <a href="https://docs.google.com/spreadsheets/d/1fIPU1OkgnKgsCiQqcj18RXRNlqqfL1YDGCjeWAeXC7s/edit?gid=2003669200#gid=2003669200&amp;range=L95">Plan A side panel data</a>, (1.3*1.4*1.4)^(1/3) = 1.37.</p></td>
</tr>
<tr>
<td><p>Smuggled chip proxy year</p></td>
<td><p>2028.6</p></td>
<td><p>Roughly when the smuggling happens, adjusted forward slightly to account for the value of an exponential at the midpoint underestimating its average.</p></td>
</tr>
<tr>
<td><p>Chinese domestic power efficiency gap during diversion period</p></td>
<td><p>3.7x</p></td>
<td><p>Taking a value between the two relevant cells in <a href="https://docs.google.com/spreadsheets/d/1fIPU1OkgnKgsCiQqcj18RXRNlqqfL1YDGCjeWAeXC7s/edit?gid=2003669200#gid=2003669200&amp;range=O100">Plan A side panel data</a>.</p></td>
</tr>
<tr>
<td><p>Decommissioned chip proxy year</p></td>
<td><p>2026.5</p></td>
<td><p>Seems vaguely right, the decommissioned chips will generally be older than this, but more of the compute will be from the newer chips since the quantity is growing 2–4x per year or so.</p></td>
</tr>
<tr>
<td><p>Covert datacenter peak PUE</p></td>
<td><p>1.4</p></td>
<td><p>This refers to the facility power usage at maximum utilization divided by the IT power usage at maximum utilization. We use the value from <a href="https://epoch.ai/data-insights/gpus-power-usage-in-ai-data-centers">here</a>. It should maybe be adjusted upward because it’s a covert datacenter, but pretty unclear, also unclear whether theoretical maximum power is what we want to track for a project that could be flexible if needed. Leaving it at 1.4 for now.</p></td>
</tr>
</tbody>
</table>

With the parameter values above, a covert datacenter with 1 GW total facility power could support 1.9M H100e of 2028-era smuggled US chips, or around 1M H100e of decommissioned US chips, or 525k H100e of 2028-era domestically produced chips.

**How much time would construction take?**

Today, Epoch finds that [gigawatt-scale datacenters can likely be built in two years or less](https://epoch.ai/data-insights/data-centers-buildout-speeds).

![](../assets/supplements/covert-ai-projects/image6.png)

Considerations pointing towards construction being faster than this:

1.  By 2029, constructing datacenters of this scale will be more routine and likely faster than today.

2.  Additionally, being a top national priority for the Chinese government might enable a faster timeline than usual.

3.  In Plan A, we forecast that construction labor will be largely automated by robots. We are uncertain about the timing here, and this might not be a significant factor at the beginning of the deal.

Considerations pointing towards construction being slower than this:

1.  Clandestine underground facilities would require bespoke engineering that normal datacenters do not.

2.  Construction speed may be constrained by factors other than labor or spending (for example, if excavating a large underground cavern in a remote area, there may be a maximum rate at which spoil (dirt, rocks from excavation) can be carried away for distribution across a wide area to avoid creating satellite-visible piles).

3.  If significant human labor is required, the requirement to avoid spies might make it difficult to find workers. Separately, compartmentalizing parts of the project could constrain parallelizability (e.g. you might want to finish excavation before installing any IT equipment to reduce the number of people who know IT equipment is being installed there.)

We use **two years** as a point estimate.

**What detection risk do covert projects of various sizes incur?**

We use the following methodology to estimate the probability of detection.

1.  We are uncertain about how detection hazard scales with site size. Lacking any reason to expect detection hazard to scale superlinearly in site size, we suspect that the [optimal strategy](covert-ai-projects.md) resembles “make sites as large as possible subject to feasibility constraints”. Informed by the strategies above, we [estimate a distribution](#id.tjcejqx40fwx) over the optimal site size (where optimal is basically an operationalization of “maximum feasible site size”.)

2.  For a few possible “optimal site size” conditionals, we [estimate the probability](#id.wf3mq4kt2zgb) of detection over the 10 year period in plan A conditional on 1 such site, and 10 such sites.

3.  We interpolate these intuitions with a shared-frailty model. This lets us produce 10-year detection probabilities for sites operating arbitrary amounts of compute (conditional on specific optimal site size outcomes, but we can also marginalize over that.)

4.  We also estimate 3-year detection probabilities and interpolate the times with a weibull-type hazard rate (hazard rate varies with a power of time). This lets us produce survival curves over time for covert projects operating arbitrary amounts of compute.

Our current operationalization of “detection” is focused on the physical infrastructure. We require that

1.  Among locations that the US assesses as suspicious, the one they assess as the most likely covert datacenter candidate is in fact a covert datacenter

2.  The assessment of the US IC is \>50% confident that this candidate is a covert datacenter. (it’s possible this threshold should be higher).

The goal of this operationalization is to match the point where the US would feel diplomatically comfortable requesting an inspection of that site, and disclosing it to the international community if needed to generate additional pressure.

Unfortunately, due to time constraints, the numbers used in the above process are based entirely on intuition and qualitative reasoning about the [detection methods](covert-ai-projects.md#section-31-plan-a-strategies-for-detection) and [hiding strategies](covert-ai-projects.md#section-32-covert-project-strategies-for-avoiding-detection) we considered. It seems possible to apply a historical reference-class approach, and we’ve informally looked at various historical examples of covert projects. But due to the number of asymmetries between this case and the historical examples we could find, and the lack of an obvious conclusion from our informal research, we did not judge a quantitative reference-class estimate to be worth devoting time to.

Therefore our estimates of detection probability over time should be treated as highly speculative. We choose to include them anyway for the sake of reasoning transparency, since the ability of states to detect covert projects is an important input to our views.

Distribution over the optimal site size

<table>
<colgroup>
<col style="width: 33%" />
<col style="width: 33%" />
<col style="width: 33%" />
</colgroup>
<tbody>
<tr>
<td><p><strong>Parameter</strong></p></td>
<td><p><strong>Estimate</strong></p></td>
<td><p><strong>Rationale</strong></p></td>
</tr>
<tr>
<td><p>Probability that &gt;1MW is infeasible/suboptimal</p></td>
<td><p>0%</p></td>
<td><p>This is an approximation for modeling purposes.</p></td>
</tr>
<tr>
<td><p>Probability &gt;10MW is infeasible/suboptimal</p></td>
<td><p>10%</p>
<p> </p></td>
<td><p>Intuitive guess. There are many different kinds of industrial sites that draw 10MW from the grid and dissipate 10MW of heat. Of each kind of site, China might have hundreds or thousands. It seems highly likely that at least one of them works as a disguise for a covert datacenter.</p></td>
</tr>
<tr>
<td><p>Probability that &gt;100MW is infeasible/suboptimal</p></td>
<td><p>35%</p></td>
<td><p>Intuitive guess. There are fewer 100MW industrial sites in China, but probably still 1000+. But at this scale, you might need to rely on concealing the facility entirely rather than disguising it as something else.</p></td>
</tr>
<tr>
<td><p>Probability that &gt;1 GW is infeasible/suboptimal</p></td>
<td><p><em>80%</em></p></td>
<td><p>Our assessment is that once-through cooling at 1 GW+ requires a deep-water diffuser in an ocean (not a river) to avoid a thermal plume. Rendering other cooling methods (air-cooled or water-vapor cooled chillers) invisible at this scale seems implausible.</p>
<p>There are some industrial sites at this scale, but seemingly not very many, and they would be highly visible targets for challenge inspection.</p>
<p>From <a href="https://epoch.ai/data-insights/ai-datacenter-cost-breakdown">this Data Insight</a>, “a MW-weighted average across major US markets” finds that the facility capex per IT GW is $11B.</p></td>
</tr>
<tr>
<td><p>Probability that &gt;10GW is infeasible/suboptimal</p></td>
<td><p>100%</p></td>
<td><p>This is an approximation for modeling purposes.</p></td>
</tr>
</tbody>
</table>

![](../assets/supplements/covert-ai-projects/image7.png)

Intuition-based detection probabilities, by site size and number of sites

These estimates assume only the unilateral detection methods discussed above, and condition on no “AI silver bullets” being discovered (we add those on top in the final model). By “3y”, this means “three years into the deal”.

|  |  |  |  |
|----|----|----|----|
| **Per-site facility power (MW)** | **n sites** | **P(detected by 3y)** | **P(detected by 10y)** |
| 10 | 1 | 0.20 | 0.26 |
| 10 | 3 | 0.25 | 0.30 |
| 10 | 10 | 0.32 | 0.37 |
| 10 | 100 | 0.55 | 0.75 |
| 100 | 1 | 0.25 | 0.35 |
| 100 | 3 | 0.35 | 0.40 |
| 100 | 10 | 0.45 | 0.67 |
| 100 | 100 | 0.65 | 0.80 |
| 1000 | 1 | 0.40 | 0.50 |
| 1000 | 3 | 0.45 | 0.70 |
| 1000 | 10 | 0.70 | 0.85 |
| 1000 | 100 | 0.85 | 0.90 |

![](../assets/supplements/covert-ai-projects/image3.png)

Forecast of “AI silver bullet” discovery by year

Thomas’s overall view about the likelihood that anything in the category allows us to detect covert projects by the following years (assuming the events of Plan A) is:

|  |  |  |  |
|----|----|----|----|
|  | High will | Low will | Reasoning |
| 2033 | 65% | 20% | I think the development of lie detectors is about 50/50 by 2033 conditional on the capability trajectory. In high will, this enables the US to threaten to leave the deal unless China submits to lie detection, which would reveal a covert project. Then there’s some probability that other paths help substantially, especially unknown unknowns. |
| 2037 | 95% | 55% | By 2037, we are likely to have developed good lie detectors (maybe 80%). If a high will regime, lie detectors seems sufficient, and it’s very likely that other verification methods pan out, especially given that we'll have the industrial capacity to install whatever monitoring devices are necessary. In a low will regime I’m less confident about what will happen. |

All of these numbers set aside all the other detection methodologies, i.e., they assume that there’s no ability to detect.

![](../assets/supplements/covert-ai-projects/image2.png)

# Section 4: Limiting Consortium uplift to covert projects

In Plan A, legal projects worldwide develop highly capable AI and robotics over the course of the 2030s. Some of this progress will spill over to covert projects, making it easier to build AGI in secret than it would have been under a [global moratorium on AI development (as in Plan S)](../main.md). Our best guess is that this increased risk is worthwhile, due to the alignment, power concentration, and war-avoidance benefits of building more capable AI under the auspices of a deal; see discussion in our [Comparing Possible Plans supplement](comparing-possible-plans.md#eli-lifland) for more on why.

In this section, we summarize the various Plan A policies affecting the degree to which Consortium AI progress benefits covert project R&D. We also estimate

## Section 4.1: Relevant Plan A policies

**Recommendation \#1: Total research transparency**

In Plan A, nearly all AI research is fully transparent to the public, including AI algorithms, code, and documentation, for all frontier AI projects. AI model weights, significant fractions of the training data, and a small amount of other sensitive information is prevented from leaving the datacenters.

**Recommendation \#2: Inference monitoring to prevent covert project uplift**

See our inference monitoring and restrictions [here](verification-plan.md#hardware-research-restrictions).

We do not plan to offer zero-data-retention (ZDR) inference on models whose capabilities we would not want proliferated to covert projects. See our ZDR policy [here](verification-plan.md#zero-data-retention-zdr-inference).

**Recommendation \#3: Model weight security**

We think achieving high-confidence model weight security is extremely important for Plan A, and the Consortium probably should not proceed very far above pre-deal capability level until they are ~95% confident that the best-equipped actors in the world cannot steal the model weights. Forecasting the likelihood of this happening is outside the scope of this supplement.

## Section 4.2: Covert project strategies

**Path \#1: Distillation from Consortium models**

Currently, Chinese labs like Minimax and Zhipu are spending around 20–30x less[^22] on R&D compute than US frontier labs like OpenAI. From our forecasts, it seems plausible that a covert AI project would start off with ~20-30x less compute compared to the leading AI company at the start of the deal.[^23] So while the requirement of secrecy would no doubt be a burden, researchers running a PRC covert project might not feel much more compute constrained initially than when they were operating legally. Despite their compute advantage, US labs have not obviously managed to lengthen their lead in model capabilities.[^24]

![](../assets/supplements/covert-ai-projects/image4.png)

We believe this is primarily due to “distillation”, [used in a loose sense](https://www.anthropic.com/news/detecting-and-preventing-distillation-attacks) to refer to using state-of-the-art closed source models to generate synthetic data and grade RL trajectories. These techniques can allow for highly compute-efficient training, in some cases offering more than an OOM of compute equivalent gain.[^25]

Will covert projects be able to stay 3–9 months behind the frontier then, like today’s Chinese labs? On one hand, covert projects will get an additional boost at the start of the deal compared to today’s trailing labs: unlike today, all training recipes will become [transparent](transparency-plan.md). This initial sharing of non-overlapping insights will bring forward the Consortium and covert frontiers together at the start of the deal. On the other hand, Plan A tries to [mitigate distillation](verification-plan.md#2031-restrictions-for-hardware-randd-and-other-high-risk-domains) by e.g. restricting companies from revealing intermediate model outputs in their APIs.

We are uncertain how effective these measures will be against a determined adversary. The large number of different AI companies, applications, and deployments will provide a correspondingly large attack surface. A government could also pressure one of their country’s AI projects to intentionally leave a loophole open for distillation.

It is essential that distillation not enable the proliferation of [destabilizing dual-use R&D capabilities](covert-ai-projects.md#section-51-paths-to-a-covert-project-catastrophe), which might come fairly early into the deal (e.g. between our SAR and TED-AI milestones). For this reason, we recommend that the Consortium conduct ongoing red-team experiments where a group of researchers attempt to distill the current frontier models under similar circumstances a covert project would face. Depending on the results, it might be necessary to halt external deployment of more capable models until more assurance can be achieved.

**Path \#2: Extracting R&D labor from Consortium models**

Consortium models running in inference datacenters will have classifiers that flag attempts at anything that looks like AI R&D. (In Plan A, models that would provide AI R&D uplift above the pre-deal SOTA are not offered under ZDR.) It seems risky to iterate against these things; we do not view this as a promising strategy.

Overall, this path seems fairly unlikely to work at all if the Consortium is competent. If it did, covert projects could potentially make use of models with superhuman experiment selection skill (or “research taste”) in AI R&D, biology R&D, and other dual use domains, significantly accelerating their progress.

## Section 4.3 Quantitative estimates

<table>
<colgroup>
<col style="width: 33%" />
<col style="width: 33%" />
<col style="width: 33%" />
</colgroup>
<tbody>
<tr>
<td><p><strong>Parameter</strong></p></td>
<td><p><strong>Estimate</strong></p></td>
<td><p><strong>Rationale</strong></p></td>
</tr>
<tr>
<td><p>Fraction of Consortium software progress that leaks to covert project</p></td>
<td><p>Median: 67%</p>
<p>80% CI: [36%, 90%]</p>
<p>Beta distribution</p></td>
<td><p>See our estimate <a href="https://docs.google.com/spreadsheets/d/1zKOxldIPXrz6RypC8Zr50rTpF10yGz4w0UZhNxk78XE/edit?gid=0#gid=0">here</a> for the median. The 80% CI is an intuitive guess (specifically, the p90 was chosen at 90%, and a beta distribution was assumed, which forces the p10 to be 36%).</p></td>
</tr>
</tbody>
</table>

# Section 5: When is a covert project catastrophic?

To become catastrophic, a covert project must achieve one of three things:

1.  **Insurmountable capabilities lead.** This occurs if a covert project is able to get enough of a lead over the Consortium that even if the Consortium were to pivot back to racing quickly, it would not be able to stop the covert project (or its sponsor nation) from reaching AI capabilities sufficient to prevent any of the following outcomes.

2.  **Balance-of-power warping capabilities.** This occurs if the covert project significantly changes the geopolitical balance of power, e.g. by granting a large economic, military, or political lead. The extreme version of this involves a decisive strategic advantage—i.e. granting the country with a covert project a position of complete strategic superiority over their rivals.

3.  **BATNA warping capabilities.** This occurs if the covert project AIs empower their host countries to such an extent that the counterparty prefers remaining in the deal (despite knowing about the cheating) over pulling out of the deal and trying to go at it alone.

If none of these are true, then: (i) the covert project does not have an insurmountable capabilities lead: legal projects can catch up if they want, (ii) all sides roughly preserve their within-deal balance of power, and (iii) all sides can credibly threaten to leave the deal to coerce a known defector into shutting down their covert project. As long as each of these are true, then, the defection from the deal isn’t catastrophic.

We define the capability level that a covert project would need to reach to satisfy any of these conditions as *deal-undermining-AI.* Deal-undermining-AI is not a fixed capability threshold, that threshold will vary over time depending on the level of capability available to other nations.

We’ll now discuss how difficult it is for a covert project to build a deal-undermining AI.

## Section 5.1: Paths to a covert project catastrophe

**Insurmountable capabilities lead**

Achieving an insurmountable capabilities lead is extremely hard because of the massive compute deficit faced by the covert project.[^26]

Before the legal projects pause capability development at TED-AI, most of the covert project’s capabilities progress will come from implementing the new training recipes developed by the legal projects (assuming no distillation is occuring). Therefore, the “effective training system performance” gap will be equal to the hardware gap, which, at the beginning of Plan A in the scenario, is around 24x (80% CI: \[115x, 9x\]) from a covert project to the largest legal project (assuming the covert project has ~1.5M H100e, and the biggest legal project uses ~36M H100e for R&D).

There are two advantages for covert projects:

First, they may not slow down for safety. At points within Plan A, capability progress will slow down dramatically or pause because of safety concerns. In this situation, the covert project will make some software progress itself, but very slowly.[^27]

Second, due to the transparency and difficulty of algorithmic security, algorithms flow from the legal projects to the covert projects, but not the other way around.

Even if the covert project were to get a capability lead, the Consortium could just pivot back to spending all of its compute on AI progress. At the beginning of the deal, there is a ~20x compute gap (1.3 OOMs); and by 2035 it’ll have expanded to 4.3 OOMs. If all of the newly founded algorithms are immediately shipped to the covert projects, this doesn’t help at all, but:

- Some algorithms are scale dependent and therefore more helpful for the legal projects than the covert projects.

- Some algorithms may be able to be kept secure (e.g., [our estimate](https://docs.google.com/spreadsheets/d/1zKOxldIPXrz6RypC8Zr50rTpF10yGz4w0UZhNxk78XE/edit?gid=0#gid=0) during Plan A is only ~67% of algorithms leak).

- There may be some latency in the theft for the algorithms that are not radically transparent (e.g. by a few months).

**Balance of power warping capabilities**

The most promising capabilities that a covert project could pursue to change the geopolitical balance of power that we’re aware of are:

- **Persuasion / AIs for political uplift**. If covert projects are able to get AIs with similar levels of capabilities to, for example, the early 2028 AIs of the race ending of [AI 2027](https://ai-2027.com/), this could make their host country substantially more politically effective than anyone else, enabling them to get substantially more power. The main limiting factor on persuasion AIs is that it is probably a high capability threshold.

- **Secret robot buildout**. The covert project could enable a massive industrial buildout. e.g. in underground tunnels, giving much greater industrial capacity than the rest of the world. This is particularly relevant because of the cap and trade regime over robot production in the Plan A scenario.[^28]

- **Military R&D.** If covert projects have substantially more capable AIs than the legal AIs, or the legal AIs are all subject to aggressive refusals, covert projects could help design cheaper and better weapons (e.g. drones, missiles, ships, planes, bombs, etc).

- **Exotic novel technology.** This includes nanotechnology, mind uploading, certain kinds of bioengineering, and unknown unknowns. Any of these would be extremely destabilizing; the main uncertainty is how difficult they are, i.e. what level of AIs over what time period are necessary for achieving them.

For military R&D and the robot buildout, the main limitation will be succeeding sufficiently in a manner that other countries cannot detect. If other countries notice, they can respond by requiring improved verification, requiring further arms control deals, or ramping up production themselves to restore the relative balance of military power.

**BATNA-warping capabilities**

The main paths for a covert project to greatly improve China’s BATNA are:

- **Splendid First Strike on the Compute**. China could pull out of the deal, destroying US datacenters, plus gain an asymmetric advantage over the US by either (i) destroying the US hardened weight or chip stockpile, or (ii) Protecting some compute that was meant to be destroyed in the case of a deal dissolution. Having a sufficient cyber lead to overcome the inference compute disadvantage of the legal projects could enable covert projects to hack into the US model weight vault and destroy the copies. Protecting the compute probably requires significant physical capabilities, i.e. a secret robot buildout.

- **Speed up the robot production ramp after the deal breaks down.** For example, you could covertly get a robot research lead on the rest of the world so that when the deal breaks down, you are starting off with better robot designs. Alternatively, you could build a hardened robot stockpile, which would create a higher starting population of robots from which to bootstrap.

For this, as well as the above, there are also unknown unknowns (e.g. new military tech we don’t know about yet). The unknown unknowns are probably scarier than any of the concrete paths we’ve identified.

## Section 5.2: Operationalizing Deal Undermining AI

In the quantitative analysis for this supplement, we simplified the modeling by assuming that deal undermining AI is a specific capability threshold that doesn’t change over time.

What specific threshold do we choose? We are currently operationalizing this as “Top Expert Dominating AIs (TED-AI)”, or AIs that are better than the top expert at every domain. Since AI capability profiles are currently fairly spiky, TED-AIs will be substantially superhuman at the skills they are strongest at, while merely being top expert level at the skills they are weakest at.

- **Why not a higher threshold?** Once AIs are beyond the human range, it’s hard to limit the possibility of novel exotic technology which we don’t know how to defend against. Moreover, it probably won’t make a huge difference, because the intelligence explosion beyond TED-AI is probably going to be quite fast.

- **Why not a lower threshold?** AIs that are within the human range seem much less likely to develop the sorts of novel technology that could be geopolitically destabilizing. Even very large advances (e.g. much cheaper interceptors) seem pretty far from undermining MAD.

We hope that future analysis improves on this baseline. For example, another reasonable operationalization of “deal undermining AI” is “any AI that’s more capable than the legal projects”, becuase…

- Covert projects can’t have an insurmountable capability lead if they don’t have a lead at all.

- AIs of similar capability levels probably can’t change the geopolitical balance of power, if the defenders are deploying AIs of greater capabilities research to red team. especially given Consortium defenders will have vastly more compute (e.g. for finding and patching vulnerabilities). This will depend on the strategy taken by the legal projects, i.e., assuming that legal projects are allowed to apply AI to military R&D. In Plan A we currently recommend some arms control limitations on the use of AI to build new superweapons. The main downside of that policy is that it increases the chance that covert projects could be used to gain large military advantages.

However, this strategy likely requires more aggressive capability scaling than is needed.

- It’s probably fine for covert projects to get a lead at lowish levels of capability (e.g. automated coder) because at that point, they aren’t strong enough that small gaps in capability seriously alter military / economic balance of power. In the scenario, for a very brief period of time during 2029 (before automated coder), legal training is paused while verification is set up, and so in the scenario, covert projects in principle might be able to get a lead during this window, though in practice it is unlikely because of the hardware gap (also, covert projects [likely will need even more time](#id.xtksf8btwltx) to set up their infrastructure, unless they are using existing exempt military datacenters).

- Closer to the top of the human range (e.g. at or beyond top expert level AI) it’s easy to imagine a small AI capability quickly snowballing into huge capability / political power. Things like superhuman political strategy and persuasion become more important and are almost impossible to defend against.

# Section 6: Overall risk estimate

*The estimates in this section are based on simulating covert project capabilities progress as described in our [Takeoff Supplement](takeoff-supplement.md).*

In this section we quantify how the Consortium’s [scaling strategy](capability-scaling-strategy.md) affects the risk that covert projects develop deal-undermining AI.[^29] We only evaluate fixed strategies here, of the form “aim to reach TED-AI some number of years into the deal, then pause there to do alignment research until the risks of delaying handoff outweigh the benefits.” This is somewhat unrealistic, because in reality the decision-makers implementing Plan A will be able to flexibly respond and adopt their strategy based on evidence received.

For example, if the US received evidence that reaching TED-AI within 6 years would require a massive amount of software progress, they could push the rest of the Consortium to follow a more gentle scaling trajectory that leaned more on hardware buildout, thereby leaking less software to the covert projects. This would reduce the risk due to covert projects, though it would also increase the risk that the deal breaks down before TED-AI has been reached safely. They could also adopt filtered transparency instead of Total Research Transparency, which would leak a smaller fraction of software progress to covert projects, enabling faster scaling for equal covert project risk, at the cost of safety and risk of deal impairment.

The actual covert project risk incurred will depend on how decisionmakers balance these factors to select a scaling strategy. Below, we show how varying the **scaling duration** and **handoff delay** affect the risk incurred.

All the assumptions we are making

We assume that

- The US and other non-defecting Consortium members competently implement all of our policy recommendations

- The PRC executed a competent diversion program one year before the deal was implemented (i.e. in 2028)

- Covert projects which are detected before reaching deal-undermining AI stop their progress immediately.

- Deal-undermining AI is operationalized as TED-AI

- No weight theft occurs during the deal

- The deal does not break down during the time period in question.

|  |  |  |  |
|----|----|----|----|
|  | **Aim for TED-AI in 2 years** | **Aim for TED-AI in 5 years** | **Aim for TED-AI in 8 years** |
| **Covert project risk at TED-AI** | 7% | 8% | 8% |
| **Covert project risk waiting 5 years after TED-AI** | 18% | 13% | 11% |
| **Covert project risk waiting 10 years after TED-AI** | 20% | 16% | 15% |

Concretely, with the evidence available to us today, we estimate that

- Halting AI R&D and initiating Plan A roughly one year before the Automated Coder milestone (in our scenario, this means implementing it in early 2029),

- then making whatever software progress is needed to safely scale to Top Expert Dominating AI over the following 6 years, (early 2035, in our scenario),

- then working towards a high-confidence alignment solution for 5 more years (until 2040, in our scenario)

would incur a 13% chance of covert projects developing deal-undermining AI before detection or handoff, if China competently pursued a covert project and remained committed to keeping it hidden.

The probabilities above are obtained by drawing from our full range of uncertainty about the [dynamics underlying AI R&D](https://www.aifuturesmodel.com/), in addition to our uncertainty about the feasibility of various covert project strategies and mitigation strategies. We explain the details of our quantitative model in our [Takeoff Supplement](takeoff-supplement.md). Again, the decisionmakers implementing Plan A will have access to more information than we do, which might reveal that the risk incurred by the above strategies differs much more sharply than they do in our estimation.

To illustrate this, if we could be certain that AI R&D and takeoff dynamics worked exactly how it does in our scenario, but still had uncertainty about covert project affordances, the table above would look like this:

**Covert project risk incurred by several strategies, assuming the AI 2040 takeoff parameters:**

|  |  |  |  |
|----|----|----|----|
|  | **Aim for TED-AI in 2 years** | **Aim for TED-AI in 5 years** | **Aim for TED-AI in 8 years** |
| **Covert project risk at TED-AI** | 2.0% | 1.6% | 1.8% |
| **Covert project risk waiting 5 years after TED-AI** | 18.8% | 8.8% | 5.2% |
| **Covert project risk waiting 10 years after TED-AI** | 22.8% | 12.4% | 10.8% |

# Section 7: Covert project response plan

The main goals of a policy response to covert projects are:

1.  **Prevent a covert project from building deal-undermining AI.** We generally want it to be the case that legal AI projects have stronger AIs than covert projects. This is less important early in the intelligence explosion but becomes crucial later on, as having better AI capabilities could quickly lead to an insurmountable geopolitical lead. Specifically, by *deal-undermining AI*, we mean an AI that either (i) directly confers a [decisive strategic advantage](https://aisafety.info/questions/8AEZ/What-is-a-decisive-strategic-advantage) to the covert project or (ii) is able to ongoingly outpace the legal AI projects, even if they switch to maximally fast AI capabilities progress.

2.  **Deter the creation of covert projects.** We want it to be the case that at the beginning of Plan A, both the US and China are confident that if they were to do a covert project, it would either be detected before it is relevant, or outpaced on AI progress, and that these outcomes are worse than not having any covert project.[^30]

3.  **Maintain international cooperation.** In particular, if there isn’t a covert project, we want to avoid Plan A breaking down due to lack of trust, i.e. one side being worried that the other has a covert project and thus wanting to exit the agreement.

4.  **Prolong the time with human-level but not superintelligent AI.** Time with human level AI is very valuable because it is when we’ll make the most progress on alignment.

Goals 1 & 2 are in tension with Goals 3 & 4 because a central tool for preventing / deterring covert projects is accelerating capabilities progress within Plan A.

The rest of this section is structured as follows:

- First, we discuss the set of possible responses to covert projects.

- Second, we discuss an example high level overall strategy

- Third, we go through concrete scenarios and how we would recommend responding to each.

## Section 7.1: Options for responding to covert projects

In this section, we’ll go over policy options for situations where covert project risk seems unacceptably high. These options can be pursued in parallel. Note that many of these options (especially options 1-4) require negotiation with China.

**Option \#1: Switch to Plan S**

*Multilateral*

The US and China could agree to a full moratorium on ongoing AI development. This would slow down covert projects in the regime where they are mostly benefitting from Consortium-driven algorithmic progress. The covert project could still make progress on its own, but it would be much slower because of the compute and labor bottlenecks. Overall, this maximizes the serial time in the agreement before a fixed size covert project overtakes, putting aside detection.

This option, of course, has the standard downsides of switching to Plan S. With respect to covert projects in particular, it may also delay the creation of any of the “AI silver bullets”, discussed above, which are helpful for mitigating covert projects.

The exit paths for Plan S are (1) we successfully developed improved verification technology, (2) both sides decided to grant the other improved verification access, (3) sufficient progress on alignment was made to continue scaling quickly, in a manner that outpaces covert projects or (4) covert projects pose a large, imminent risk, and misalignment risk is smaller than covert project risk (while still being substantial, or else we’d be in option (3).

The most preferable option among these is (1). In that case the plan is: issue a complete moratorium on AI R&D until we’ve got good enough verification to be confident covert projects are not a binding constraint, then revert back to Plan A.

**Option \#2: Adopt a scaling strategy that minimizes software share of capabilities progress**

*Multilateral*

In Plan A, we currently allow for ~.5 OOMs/year of software scaling, and ~0.5 OOM/year of hardware scaling over 2035. The reason we recommend making algorithmic progress is in large part because of deal dissolution risk; if covert projects are a binding constraint, we could minimize algorithmic progress and scale purely with hardware, which doesn’t diffuse. It’s probably impossible to get algorithmic progress to zero (for example, there are inevitable capabilities externalities from safety research), but we might be able to decrease it to ~.1-.2 OOMs/year.

**Option \#3: Attempt to improve algorithmic progress security**

*Multilateral*

Another approach is to try to prevent algorithmic progress from diffusing (or, increasing the latency with which it diffuses). Again, this would slow covert projects substantially insofar as they were primarily relying on Consortium algorithmic progress. The main difficulty is that there is a major tension between our desire for openness/transparency with a desire for algorithms to be secure: an important component of Plan A is the Total Research Transparency that deliberately publishes most algorithms onto the internet. We discuss options for increased algorithmic security in our [transparency supplement](transparency-plan.md#thomas-larsen).

Depending on how successful algorithms security is, it may be viable to switch to faster capability scaling. This will obviously pose additional misalignment risk, and in this regime it is hard to slow down because a covert project is close behind, so this is not a desirable position to be in.

**Option \#4**: **Negotiate with China to submit to stronger verification**

*Bilateral*

For example, China could agree to:

- Ongoing intrusive physical monitoring (e.g. thermometers in large water sources, cameras in relevant sites, electrical grid monitoring)

- Provide access to classified materials that indicate there is no covert project.

- Physical inspections of plausible covert project locations (e.g. industrial plants that produce substantial waste heat, tunnels near large water sources, etc).

- Access to classified data, e.g. AIs can see the black budget and report back if there are any AI looking things on there

- Lower the exempt military compute cap

If we have viable privacy preserving verification such that an AI could get access to these information sources and only report back high level bits of information, this could make this option much more viable. Alternatively, the US might credibly warn China that we are pulling out of the deal unless they provide us with stronger verification affordances.[^31] China would then be incentivized to agree to these concessions because the deal breaking down is very bad for them, because it would amount to something similar to a return to the status quo (e.g. a return to a race with the US having vastly more AI compute).

**Option \#5: Race to improved verification**

*Bilateral*

If we have enough time, it may be worthwhile diverting massive resources into a sprint to develop improved verification technology, for example, privacy preserving verification that could enable the option above. Having access to more advanced AI is helpful for this option. We recommend pursuing this in almost any scenario because having the affordance to implement stronger verification is generally useful, but in scenarios where covert projects are posing substantial risk, this is especially promising.

**Option \#6: Improve takeoff speed modeling**

*Unilateral*

Concern for covert projects may be substantially driven by the tail risk, i.e., that takeoff is faster than we think with a tiny amount of compute. It may be worthwhile to invest substantial resources to gain better information about how fast the intelligence explosion goes with a small amount of compute. An obvious baseline is to invest more into generic takeoff speed modeling (e.g. things like the AI Futures Model).

A more intense option is to create a “covert dominating miniproject (CDMP)”—a sanctioned project that would simulate the progress of a covert project; it would be given somewhat more compute than we think would be able to evade detection, and would try to conduct an intelligence explosion as fast as it could, theoretically outpacing any covert project. The main downside of this proposal is that it would lead to faster algorithmic progress (which may then diffuse to the covert project itself, further accelerating it). However, this might net out to an improvement in a regime where we are very uncertain about takeoff speed because the empirical observations from the CDMP could give us a much better estimate of takeoff speeds in a highly compute constrained regime.

**Option \#7: Pull out of the deal and switch to Plan B**

*Unilateral*

This would involve leaving the deal. Immediately, both sides would destroy the vast majority of each other’s compute, and then both sides would go back to racing. This is really bad for both sides, because it would be immediately economically catastrophic and it would significantly increase misalignment risk, World War 3 risk, and concentration of power.

The main upside of this option is that it is useful as a BATNA during negotiation, and preserving a credible threat of leaving the deal can help deter the creation of a covert project in the first place. If China builds a covert project knowing it runs a substantial chance of detection, and the US commits to pulling out of the deal if they detect it, it is probably irrational for China to create a covert project in the first place.

The main downside of pulling out of the deal is if this happens when China was in reality honest, but for some reason the US had an overly hawkish estimate of a Chinese covert project. (For example, maybe compute estimates were off, or smugglers were harder to track down than expected). In these worlds, there was the option of continuing on in Plan A and incurring much lower risk across the board.

**Option \#8: Other geopolitical concessions**

*Bilateral*

In general, if the US is suspicious that China is defecting, they can use the standard set of geopolitical tools to incentivize them against this. Particularly notable tools in the Plan A scenario include the robot and compute cap subject to both countries.

## Section 7.2: Response plan for ambiguous evidence of covert project

Example concrete ways the US could get weak evidence of a covert project:

- The chip supply chain tracing reveals a missing 1M H100e: records exist of these chips being manufactured (e.g. from Nvidia/TSMC/Huawei), but we aren’t able to find them. This could be smugglers, or it could be a nation-state backed covert project.

- China refuses additional verification. For example, maybe the US is suspicious of a particular set of sites, where there might be a covert project, but China isn’t willing to allow the US access. This is an update towards a covert project because they are much more likely to give the US access to these sites if they are legitimate.

- The US might get ambiguous intelligence from IMINT / OSINT / SIGINT, for example, satellite images might suggest large scale underground construction, but the US might not be able to ascertain whether it's an AI related covert project.

- The US notices model weight exfiltration attempts that seem like they could be coming from China but with unclear attribution. (This doesn’t necessarily imply China is operating covert compute, but is evidence.)

Baseline response:

1.  Adopt a more covert project sensitive scaling strategy, for example, minimizing algorithmic progress (Option \#2).

2.  Improve verification: both by improving the technology (Option \#5) and negotiating for increased implementation (Option \#4).

3.  If China refuses to allow improved verification, consider leaving the deal (Option \#7). This is the only part of the response that the US can do unilaterally, but the fact that this is a bad BATNA for both parties creates pressure for China to agree to the above.

Essentially, this proposal involves marginally tweaking parts of Plan A to be more conservative with respect to covert project risk, because there is direct evidence that covert projects are a significant concern, but allows the core properties of Plan A to continue—there is still total research transparency, broad deployment of AI, ongoing reversible scaling, etc.

## Section 7.3: The US gets unambiguous evidence of a PRC covert project

Example concrete ways the US could get unambiguous evidence of a covert project:

- Cyber espionage (e.g. GPU backdoors, finding classified documents, etc)

- Satellite footage (e.g. finding the construction, heat signature from the project, etc)

- A literal spy in the project

- Egregious refusals from China during negotiation (e.g., there is really solid privacy preserving verification technology, but China refuses to use it and doesn’t give a reasonable explanation for why).

Baseline response:

1.  Require that China make large geopolitical and verification based concessions (Option \#8 and \#4).

2.  If China isn’t willing to make those concessions, exit the agreement. (Option \#7).

3.  If China is willing to make sufficient concessions, evaluate how good the verification situation looks and choose a [capability scaling strategy](capability-scaling-strategy.md) that corresponds with the overall level of ongoing covert project risk.

This strategy is reasonable because it (i) punishes China and puts them in a bad strategic state, thus deterring them from doing a covert project in the first place, (ii) allows the Plan A deal to continue, as is rational for both sides to want, and (iii) prevents the covert project from developing deal-undermining AI.

# Appendix

## Covert project strategies we think are ineffective

### Acquiring compute

##### Diverting pre-2028 stock by retroactively understating domestic production

This category refers to pre-2028 sales by Chinese chip vendors. These sales could conceivably be understated, but it seems even more difficult than the (already seemingly quite difficult) task of understating new production.

<table>
<colgroup>
<col style="width: 33%" />
<col style="width: 33%" />
<col style="width: 33%" />
</colgroup>
<tbody>
<tr>
<td><p><strong>Parameter</strong></p></td>
<td><p><strong>Estimate</strong></p></td>
<td><p><strong>Rationale</strong></p></td>
</tr>
<tr>
<td><p>Probability that retroactive concealment of domestic production is feasible</p></td>
<td><p>7%</p></td>
<td><p>I think that doing it non-retroactively is about 15% likely to be feasible, and I am dividing this number by two. Seems about right, but I could update based on learning more about the Chinese semiconductor ecosystem or the historical effectiveness of whistleblower programs like ours.</p></td>
</tr>
<tr>
<td><p>Fraction of pre-2028 cumulative domestic production which can be concealed and removed from datacenters, conditional on feasibility above</p></td>
<td><p>5%</p>
<p>Beta distribution with p90 = 7%.</p></td>
<td><p>Intuitive guess, p90 based on the idea that removing “one Chinese hyperscaler” (e.g. 10-20%) would be super obvious. Though note that this is different from removing one hyperscaler from the total compute in China; some of that will be legally imported or smuggled US-designed chips.</p></td>
</tr>
</tbody>
</table>

Assuming that the fraction of global compute produced by China stays roughly constant, and accounting for the [2028 flow](#kix.n9c95482a1ct), we get a Beta distribution supported on \[0, 1.6%\] with **median 0.08% of pre-deal compute from this route, conditional on it being feasible at all.**

## Non-Chinese covert projects

This supplement is focused on the possibility of a Chinese covert project. However, there is also a chance that other countries besides China attempt a covert project. We have not looked into this possibility in detail, so are not confident in our conclusions here, but we tentatively believe that China is the country where doing a covert project is most viable, because:

1.  The US is the only country in the world with more compute than China, and acquiring compute is a central bottleneck for covert projects (see Section 2).

2.  The US seems less likely to agree to Plan A while simultaneously choosing to divert compute, since the US BATNA is more favorable than the Chinese BATNA.

3.  The US has less ability to do a covert project relative to China. The main reasons for this:

    1.  It will be much harder for the US to acquire chips because there is no major chip smuggling inside the US, and the US doesn’t seem to have a reasonable excuse to force companies to decommission large numbers of chips, cutting off the major avenues for covert compute procurement..

    2.  The US has more checks and balances on executive power, so a covert project is probably politically more difficult to set up. It also seems harder to for the US to compel the relevant companies to comply with the efforts of a covert project (e.g., getting semiconductor companies to falsify sales records), as very few companies below the chip-design level are US-headquartered

[^1]: We focus on China in particular because we think China is the best positioned party to defect. This is discussed further in [the appendix](covert-ai-projects.md#non-chinese-covert-projects).

[^2]: Based on our modeling, deliberately holding back on the amount of compute deployed does not improve a covert project’s chance of [success](covert-ai-projects.md#section-5-when-is-a-covert-project-catastrophic).

[^3]: Based on our modeling, the rate of capabilities progress of covert projects is largely determined by the rate of progress of the Consortium. Specifically, under our [transparency recommendations](transparency-plan.md#thomas-larsen) the main lever for speeding up (software progress) also accelerates the covert projects. Hence “going faster to outpace covert projects” usually has the opposite effect—instead, the lead-maximizing strategy involves making as little software progress as possible while maintaining the hardware-buildout-constrained rate of training compute scaling.

[^4]: Moreover, due to Total Research Transparency, for virtually all AI algorithms, we are deliberately publishing them.

[^5]: If the PRC acted with less foresight, and only began diverting chips three months in advance rather than a year in advance, their diversion yield might be ~3x less. If the US was less competent, and failed to reduce the smuggling rate relative to today in the year leading up to the deal, the diversion yield might be ~1.5x more.

[^6]: The mechanics of this are discussed more in our verification supplement [here](verification-plan.md#2032-cap-and-trade-for-robots-and-compute).

[^7]: As above, we are very uncertain about the tractability and potential consequences of doing this. Relevant public information includes the [NSA’s breach of Huawei in 2010](https://www.nytimes.com/2014/03/23/world/asia/nsa-breached-chinese-servers-seen-as-spy-peril.html), which seems to meet or exceed the level of access that would be required to gain accurate accounting records (for example, they “obtained information about the workings of \[Huawei-produced networking products\] and monitored communications of the company’s top executives”).

[^8]: By "audit," we mean: obtain a firm's complete records of compute purchased, resold or transferred, and retained as inventory, and physically inspect any compute the firm presently owns.

[^9]: It might also be possible to purchase chips directly from Chinese domestic producers in a similar manner, though I’m unsure whether China has export restrictions that would make this more difficult or unusual. In practice it probably does look rather unusual to export any significant fraction of your 2028 production, just because of the strategic importance of AI compute.

[^10]: You could also stockpile the inputs (e.g. logic dies and HBM) and finish the assembly during the deal in a secret facility. For the case we looked at (a covert packaging line) this seemed not worthwhile, namely because of the comparatively low throughput and ongoing inflow of inputs that would be required to operate it.

[^11]: Or their Chinese-designed compute, though doing this for US-made compute has a number of advantages, including (1) power efficiency to minimize required covert datacenter footprint, (2) complementarity with other diversion strategies more applicable to Chinese-designed compute, such as falsifying production records, and (3) increased plausible deniability, though this is speculative.

[^12]: This would be against their interests, but could be a plausible rationale.

[^13]: See our analysis here: Diverting pre-2028 stock by retroactively understating domestic production.

[^14]: On the one hand, the exhaust from a jet engine is much hotter than the exhaust from a chiller, but on the other hand, these aircraft only need to hide from things like IR-guided missiles rather than from repeated satellite observation and analysis.

[^15]: 1 cubic meter per second of water flow carries 4.2MW per degree C of temperature rise. The [largest water treatment plant](https://mwrd.org/locations/stickney-water-reclamation-plant) in the world handles ~30 m^3/s (covering around half of Chicago). The [largest](https://www.mee.gov.cn/gkml/sthjbgw/spwj1/201608/t20160815_362297.htm) [Chinese](https://www.nsbdjhsw.com.cn/list-yjbh.html) [underground](https://www.mee.gov.cn/xxgk2018/xxgk/xxgk11/202205/t20220505_976927.html) [water](https://www.ndrc.gov.cn/fzggw/jgsj/njs/sjdt/201808/t20180821_1194903.html) transfer projects carry ~100 m^3/s. The [largest nuclear plants](https://en.wikipedia.org/wiki/Kashiwazaki-Kariwa_Nuclear_Power_Plant) discharge a few hundred m^3/s (they heat water by more than 1 degree C in order to discharge ~10GW at this rate). The [largest desalination plants](https://en.wikipedia.org/wiki/Jebel_Ali_Power_and_Desalination_Plant) withdraw 1000+ m^3/s of seawater. The [largest](https://en.wikipedia.org/wiki/Amazon_River) [rivers](https://en.wikipedia.org/wiki/Yangtze) [in](https://en.wikipedia.org/wiki/Mississippi_River) the world have average discharge in the range 30,000–300,000 m^3/s.

    The best-suited thermal satellite we could find [has](https://www.mdpi.com/2072-4292/15/2/517?utm_source=researchgate.net&utm_medium=article) a total noise equivalent differential temperature of ~0.2 K at a resolution of 57m, better than the 100m resolution of the Landsat 8 and 9, which were used in [this paper](https://www.mdpi.com/2076-3417/15/2/738) to image nuclear plant thermal plumes. So the temperature increase *at the surface* would perhaps need to be \<0.1 degree C. This could be accomplished by drawing 10 m^3/s of water for every 4.2 MW (putting the flow rate for a 100MW facility on par with the world’s largest nuclear plants), or by dumping more megawatts into each m^3/s of water but releasing it at a greater depth (or in some sort of underground waterway) so the plume dilutes more before eventually reaching the surface. I am currently unsure whether this analysis properly accounts for time averaging or other signal processing methods.

[^16]: The technique seems to require stacking multiple images taken at different times from near-identical orbital geometry, which seems poorly suited to broad-area detection. It’s possible this could be solved via brute force with enough satellites.

[^17]: A Space Force spokesperson [said](https://breakingdefense.com/2025/08/space-force-to-launch-actual-gmti-sats-in-the-next-year-general/) to Breaking Defense that dedicated satellites for this purpose are expected to launch in 2028. The program’s FY2026 RDT&E budget schedule separately lists the GMTI “Develop and field GMTI” activity as running through Q4 FY2030, indicating a planned fielding window extending to the end of fiscal 2030, though the document does not identify an IOC or FOC date.

[^18]: Between 2010 and 2012, many CIA sources (seemingly almost all?) in China were [killed and imprisoned](https://en.wikipedia.org/wiki/2010%E2%80%932012_killing_of_CIA_sources_in_China). The New York Times in 2017 [wrote](https://archive.is/QQ8lJ#selection-2867.0-2867.181) that “the C.I.A. has tried to rebuild its network of spies in China… an expensive and time-consuming effort.” \[refer to 2023 Burns comments about progress\]

[^19]: The most extreme case of this proposal is something like: (1) move all humans to other planets with spaceships, (2) verify that no covert GPUs were transported to other planets, (3) make sure that no compute is diverted from the newly manufactured compute on other planets, and (4) disassemble the earth. This is obviously an extreme case meant to be illustrative, in practice we expect that with all of this capacity, something more efficient and far less costly could be done.

[^20]: Even if challenge inspection provisions are not included in the initial agreement, China might later come under international pressure to permit them if fear of covert projects becomes a binding constraint for Consortium scaling decisions.

[^21]: It might be possible to measure [perfluorocarbon emissions](https://www.epa.gov/sites/default/files/2016-02/documents/pfc_generation.pdf) from the Hall-Heroult process, which could distinguish how much energy is being used on actual aluminum production. We’re not aware of any way to measure this from space at a per-facility level though.

[^22]: In 2024, OpenAI [spent](https://epoch.ai/data-insights/openai-compute-spend) \$5B on R&D compute, Zhipu AI spent \$308M ([page 10](https://www1.hkexnews.hk/listedco/listconews/sehk/2025/1230/2025123000017.pdf)) on total R&D (which included 657 technical staff; assuming \$100k/yr each yields \$242.3M on compute), and Minimax spent \$189M ([page 11](https://www1.hkexnews.hk/listedco/listconews/sehk/2025/1231/2025123100025.pdf)) total.

[^23]: The compute advantage will widen in some sense with time; in our scenario the Consortium increases their compute at ~3x per year. However, this will only translate straightforwardly to capabilities through training compute scaling (research compute scaling on the other hand will be restricted to target limited amounts of software progress.)

[^24]: Depending on how you measure this; the US Center for AI Standards and Innovation found an apparently growing US lead; here we use the Epoch Capabilities Index. See “[The US-China AI gap is very uncertain](https://mcnair.center/china/)”.

[^25]: As a (somewhat dated) example, [Phi-4](https://epoch.ai/models/phi-4) used GPT-4 to generate specialized synthetic data, exceeding GPT-4’s ECI while requiring around 20x less training compute.

[^26]: We’re assuming here that covert projects are only able to acquire untracked pre-deal compute, i.e. that it’s not feasible for them to smuggle post-deal compute or to create a secret chip supply chain. After extreme capabilities, it would be possible for covert projects to set up a secret compute supply chain, but we don’t anticipate this being the binding constraint, i.e. this would happen after other capabilities we consider to be catastrophic.

[^27]: See further analysis [here](https://www.lesswrong.com/posts/7jcPg79p3kD5ir3CL/how-much-slower-does-takeoff-go-with-10-less-compute).

[^28]: An extreme version of this could undermine Nuclear MAD, but this would be very difficult. It would need to happen in secret or else other countries would respond by building up nuclear stockpiles or intervening on buildup.

[^29]: Importantly, we do not include the risk due to [weight theft](#id.xyhkdtwz44yf) during the deal in these estimates.

[^30]: One reason is that even if a covert project turns out to be non-viable, worlds where China diverts significant compute might force the Consortium to adopt a less favorable scaling strategy due to their uncertainty about how quickly the missing quantity of compute would enable deal-undermining AI to be reached by a hypothetical covert project. Another reason is that the tensions associated with detecting and shutting down a covert project would incur additional risk of deal decline, even if the covert project itself is small enough to be harmless.

[^31]: This may not be possible. See “[BATNA-warping capabilities](#id.1s6lnd83su1z)”.
