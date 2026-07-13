---
title: "AI 2040 Economic Growth Explorer — Model Explanation"
source_url: "https://ai-2040.com/econ-explorer/world"
retrieved_at: "2026-07-11T06:00:49+00:00"
conversion: "rendered HTML to GitHub-Flavored Markdown with Pandoc"
---

## How the Model Works

This model is a largely exogenous (i.e., driven by user-specified inputs) scenario-driven economic growth model with additional extensions, including a model of AI and robot hardware production costs and other economic and societal outcomes. The core of the model is a growth model where user-specified trajectories for AI and robot quantities (number of copies deployed), efficiencies (human equivalents on automated tasks), and capabilities (% of 2024 non-automated tasks they can automate) combine with human cognitive and physical labor through production functions to produce economic output.

There are several limitations and problems with modeling the economy in this way, both inherent to growth models and—given the key author’s lack of expertise in economics—probably with the specific approaches chosen here. Nevertheless, we find this a useful exploratory tool to add color to some of our scenario forecasting in ways that form a nice baseline. We don’t expect the numbers here to be right, but we do think the model behaves reasonably on the presets. The implementation of the model and the website were done using Claude Code, and therefore it’s very possible that there are bugs and problems, particularly with exploring custom scenarios.

Overall, our views about the future from an economics perspective are largely informed by other higher-level views and arguments about AI capabilities improvements and diffusion, rather than through any model, including this one.

Acknowledgments: Tom Houlden, Tom Cunningham.  [Full technical writeup (PDF)](raw/writeup.pdf)

### Contents

- [Main Explorer](#sec-main)
- [Cost Explorer](#sec-cost)
- [Energy Explorer](#sec-energy)
- [Extensions](#sec-extensions)

### Main Explorer[↑ top](#top)

Exogenous Inputs AI quantity & efficiency  
Robot quantity & efficiency  
Automation frontiers  
Capital stock (K)  
Human workforce → Production Function Y = A × CES(K, L<sub>eff</sub>) Task-based CES nesting:  
auto vs non-auto tasks,  
perfect subs within auto → Outputs GDP (Y)  
Human wages (w<sub>c</sub>, w<sub>p</sub>)  
AI/Robot rentals (q<sub>c</sub>, q<sub>r</sub>)  
Interest rate (r)  
Factor income shares

Three regions (US, China, World) calibrated independently.  Supplementary: a **cost & surplus model** (Wright’s Law + Jones design improvement, markups, cap-and-trade) and various **extensions** (income distribution, sector prices, land, endogenous labor supply) provide additional scenario exploration.

### Model Presets

<table>
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<thead>
<tr>
<th>AI 2040 Plan A Scenario</th>
<th>AI 2040 Default World</th>
</tr>
</thead>
<tbody>
<tr>
<td><p>A world where the US and allied nations coordinate to manage the AI transition through international regulation beginning around 2030. Key features:</p>
<ul>
<li><strong>International deal on R&amp;D titration.</strong> Under mutual transparency and auditing, the US, China, and other countries titrate R&amp;D to increase safety and the likelihood that humans will be able to control the systems.<sup><a href="#preset-fn-1">1</a></sup> In the model this limits an out-of-control feedback loop of R&amp;D reinvestment, leading the fraction of effective labor allocated to software and hardware R&amp;D to decrease, limiting Jones-channel cost improvements and preventing runaway recursive self-improvement.</li>
<li><strong>Cap-and-trade on production quantities.</strong> AI and robot deployment quantities are capped via a cap-and-trade permit system that limits scaling to roughly 6-month doubling times after 2032. Without such a constraint, the cost model’s implied dynamics (rapidly falling production costs, massive surplus) would in theory allow reinvestment and exploding production quantities, which might be too destabilizing.</li>
<li><strong>Human monitoring and auditing carveout.</strong> Certain tasks are kept “unautomated” by policy—reserved for human oversight, auditing, and accountability—even where AI and robots dominate them on pure capability.<sup><a href="#preset-fn-2">2</a></sup> This preserves a non-automated task bucket that humans must fill, maintaining a wage floor and keeping humans structurally relevant to the economy in the Plan A scenario, despite being dominated capability-wise after 2035 in cognitive tasks and 2036 in physical tasks.</li>
<li><strong>Citizen-dividend redistribution.</strong> Cap-and-trade permit revenue plus taxation funds citizen dividends, redistributing the surplus from AI/robot deployment to households.</li>
</ul>
<p>This is not a prediction—it’s a scenario with strong international coordination to slow things down.</p></td>
<td><p>A world with no slowdown governance—no titrated R&amp;D, and no cap-and-trade regulation on AI or robot production. AI and robot quantities are determined endogenously by the model. Key features:</p>
<ul>
<li><strong>Endogenous quantities.</strong> Each year the savings pool is invested proportionally between capital, AI, and robot hardware based on the ROI of each (marginal product per dollar invested), as determined jointly by the growth and cost models. AI and robot stocks accumulate from this investment.</li>
<li><strong>No R&amp;D throttling.</strong> The R&amp;D allocation that drives Jones-channel cost improvements is held flat rather than titrated down after 2032, so hardware and design costs continue to fall.</li>
<li><strong>No cap-and-trade.</strong> No permit system limits deployment. The surplus from AI/robots (the difference between value and cost) can feed directly back into production—AI and robots can be reinvested into producing more hardware or R&amp;D, producing a positive feedback loop. The simulation truncates at a singularity cutoff once output grows more than 1000× in a single year.</li>
<li><strong>No regulatory capability pause.</strong> The capability frontier continues improving rather than being restricted earlier, with AI and robots dominating humans by reaching 100% cognitive and physical automation by 2031.</li>
</ul>
<p>This is closer to what we would predict for the economic outcomes of the default capability progression we expect in the AI 2040 world absent the Plan A governance interventions.</p></td>
</tr>
</tbody>
</table>

<sup>1</sup> This might also reflect pursuing safer / human-interpretable / inspectable, albeit less efficient, directions—for example, macro-scale traditional-style robot designs as opposed to self-replicating or micro-scale robots.

<sup>2</sup> The most notable examples for the regime itself are AI researchers working on R&D under the regime (e.g., probably mostly working on alignment and control techniques), and auditors and inspectors for the verification regime. These are tasks that could be ‘handed off’ to AIs (AIs are capable of these tasks) but they aren’t sufficiently trusted yet.

### The Production Function

**Production function.** Output is produced by combining capital and effective labor:

**Y** — total output (GDP). **σ<sub>Y</sub>** — capital–labor elasticity. Default 1.1 (mild gross substitutes). **A** — TFP (calibrated once at base year, held constant). **σ<sub>L</sub>** — cognitive/physical labor elasticity. Default 0.6 (complements). **K** — capital stock (machinery, buildings, datacenters). **θ** — cognitive task weight. **US 0.68, China 0.50, World 0.60**. **α** — capital share of output. **US 0.43, China 0.50, World 0.40**. **f<sub>c</sub>, f<sub>p</sub>** — cog / phys capability frontiers (from **AI** / **Robot Input**). **L<sub>eff</sub>** — effective labor (aggregates cog + phys). **σ<sub>c</sub>, σ<sub>p</sub>** — across-task elasticities (auto vs. non-auto bottleneck strength). **L<sub>cog</sub>, L<sub>phys</sub>** — cognitive and physical labor aggregates. **h<sub>auto</sub>, h<sub>non</sub>** — humans allocated to each task bucket (endogenous). **A<sub>eff</sub>** — effective AI labor = copies × human-equivalents per copy. **R<sub>p</sub>** — effective robot labor = count × human-equivalents per robot. **CES vs. CES<sub>task</sub>.** The top two levels are standard CES aggregators. **CES<sub>task</sub>** at level 3 is a *task-based* CES: the automatable bucket mixes humans and machines as *perfect substitutes*, the non-automatable bucket is humans-only. Within each nest, humans allocate between the two buckets to equalise marginal products.

TFP (A) — calibration device, held constant

Total factor productivity is calibrated once at the base year from observed GDP, capital, and effective labor, then held constant. All growth comes from the model’s explicit channels: more AI/robots, better AI/robots, expanding automation frontiers, and capital accumulation. TFP plays no role in generating growth. For the regional breakdown, each region gets its own fixed A calibrated to its 2025 GDP. This means persistent cross-country productivity differences (institutions, infrastructure, human capital) are captured in the base year but don’t evolve—a limitation, since AI diffusion would likely narrow these gaps over time.

**Exogenous user inputs**

<table>
<colgroup>
<col style="width: 33%" />
<col style="width: 33%" />
<col style="width: 33%" />
</colgroup>
<thead>
<tr>
<th></th>
<th>AI (AI Input tab)</th>
<th>Robots (Robot Input tab)</th>
</tr>
</thead>
<tbody>
<tr>
<td>Quantity</td>
<td>AI copies deployed<br />
Public deployment H100e × AI copies per H100e</td>
<td>Robot units deployed</td>
</tr>
<tr>
<td>Efficiency</td>
<td>Human-equivalents per copy</td>
<td>Human-equivalents per robot</td>
</tr>
<tr>
<td>Capability frontier</td>
<td>% of <strong>2024 non-automated</strong> cognitive tasks AI <em>can</em> do</td>
<td>% of <strong>2024 non-automated</strong> physical tasks robots <em>can</em> do</td>
</tr>
</tbody>
</table>

Quantity × efficiency = effective labor supply from each technology. The capability frontier caps what tasks machines can perform—the model then determines how much automation *actually* occurs based on relative cost.

**Automation: definitions.**

**Task universe, year-t.** The set of economically relevant tasks in year t. Pre-2024 automated work (factory automation, CNC, software pre-2024) doesn’t count — it’s embedded in capital K.

**Automatable f(t) ∈ \[0, 1\]. Exogenous capability frontier.** The fraction of the year-t task universe that AI/robots are both *able* to perform (capability) and *allowed* to perform (policy). Within this fraction, one AI unit (measured in H100e compute) is treated as interchangeable with e(t) human-equivalent labor-hours on average — a simplifying assumption, since real per-task efficiency varies widely.

**Non-automatable 1 − f(t).** The complement: tasks AI/robots cannot do at all, or are not allowed to do. (If AI could do them at any relevant efficiency, they’d be in the automatable bucket.)

**Automated a(t) ∈ \[0, f(t)\]. Endogenous.** The share of automatable-task labor (in human-equivalent units) that AI/robots actually supply in equilibrium; the rest is supplied by humans working alongside them. The model determines this by allocating humans across the automatable and non-automatable buckets until their marginal product is equal in both — humans don’t care which side they work on, so they spread until indifferent. When AI/robots are scarce, AI’s rental is pulled up by that scarcity and the wage on automatable tasks is high enough that humans profitably “undercut” by working there too → a(t) \< f(t). As AI scales and its rental falls, eventually it drops below the non-automatable wage even with no humans on the auto side; humans abandon automatable entirely and a(t) = f(t).

The gap a(t) \< f(t) is the “AI could do this task, but humans can still undercut because AI is scarce” regime. a(t) = f(t) is the “AI is so abundant it has fully crowded humans out of these tasks” regime.

**Across-task elasticity (σ<sub>c</sub>, σ<sub>p</sub>).** How complementary are automatable and non-automatable tasks? To what extent can you compensate for missing labor on non-automated tasks with additional labor on automated tasks? This controls the bottleneck strength on non-automated tasks.

A concrete way to see it: if you lose one hour of non-automated labor, how many hours of automated labor do you need to add to keep output constant? The answer depends on both σ and the current automation level. Analytically, the marginal rate of technical substitution (MRTS) is MRTS = (1−f)/f · (L<sub>auto</sub>/L<sub>non</sub>)<sup>1/σ</sup>. Plugging in representative ratios (≈0.25 at 20% auto, ≈1 at 50%, ≈10 at 90%, ≈100 at 99%, ≈1000 at 99.9%):

| Automation level | σ = 0.3 | σ = 0.5 | σ = 0.8 | σ = 1.0 | σ = 2.0 | σ = 10 |
|----|----|----|----|----|----|----|
| 20% (L<sub>auto</sub>/L<sub>non</sub> ≈ 0.25) | 0.04 | 0.25 | 0.71 | 1.0 | 2.0 | 3.5 |
| 50% (balanced) | 1.0 | 1.0 | 1.0 | 1.0 | 1.0 | 1.0 |
| 90% (L<sub>auto</sub>/L<sub>non</sub> ≈ 10) | 239 | 11.1 | 2.0 | 1.1 | 0.35 | 0.14 |
| 99% (L<sub>auto</sub>/L<sub>non</sub> ≈ 100) | 4.7×10<sup>4</sup> | 101 | 3.2 | 1.0 | 0.10 | 0.02 |
| 99.9% (L<sub>auto</sub>/L<sub>non</sub> ≈ 1000) | 1.0×10<sup>7</sup> | 1001 | 5.6 | 1.0 | 0.03 | 0.002 |

Hours of automated labor needed to compensate for losing 1 hour of non-automated labor. The 50% row is 1.0 for every σ because both buckets are balanced (same task weight, same labor) — no marginal-product asymmetry for σ to amplify. Above 50%, auto labor is abundant so it has low marginal value: replacing a non-auto hour requires many auto hours, and low σ amplifies that. Below 50% the reverse holds: auto labor is the scarce bucket with high marginal value, so a fraction of an auto hour suffices, and low σ amplifies *that*. At σ = 1 (Cobb-Douglas) MRTS reduces to (1−f)/f times the labor ratio. At σ → ∞ (perfect substitutes) the labor-ratio factor drops out and MRTS approaches (1−f)/f; we never reach this regime in our defaults.

Default: σ<sub>c</sub> = σ<sub>p</sub> = 0.8 (moderate complementarity). Note: within the automatable bucket, humans and AI are always *perfect substitutes* (additive). σ only governs how much the automatable and non-automatable buckets need each other.

Production function parameters & defaults

Set in the Parameters panel (right side) under “Production Function.”

|  |  |  |
|----|----|----|
| α | 0.43 | **Capital share.** Capital’s share of output at base year. **US 0.43, China 0.50, World 0.40**. Auto-syncs with the region toggle. |
| σ<sub>Y</sub> | 1.1 | **Capital-labor elasticity.** How easily capital substitutes for labor at the top level of the production function. 1.0 = Cobb-Douglas; \>1 = gross substitutes; \<1 = complements. *Empirical estimates for historical economies point below 1:* the Gechert et al. (2022) meta-analysis of 3,186 estimates finds σ ≈ 0.3 after correcting for publication bias; Oberfield & Raval (2021) estimate 0.5–0.7 for US manufacturing. Karabarbounis & Neiman (2014) estimated ~1.25. We default to σ = 1.1, mildly above Cobb-Douglas and above the historical estimates, because the capital stock in our scenarios is increasingly AI capital (compute, robots) that substitutes more directly for cognitive and physical labor than the structures and equipment behind the historical estimates did. This is a judgment call about a new regime, not an empirical finding; users who prefer the historical evidence can set σ ≤ 1. |
| σ<sub>L</sub> | 0.6 | **Cognitive vs. physical labor elasticity.** How substitutable cognitive and physical labor are within the effective-labor aggregator L<sub>eff</sub> = CES(L<sub>cog</sub>, L<sub>phys</sub>; θ, σ<sub>L</sub>). 1.0 = Cobb-Douglas. Direct estimates are rare; the closest proxies from the skilled/unskilled labor literature are generally \>1: Katz & Murphy (1992) σ ≈ 1.4, Card & Lemieux (2001) σ ≈ 2.0–2.5, Ciccone & Peri (2005) σ ≈ 1.5. But those proxies measure substitution between skill levels of *human workers*, not between the outputs of cognitive and physical work as such. Kording & Marinescu (2025, Brookings) use σ \< 1 at the cross-sector “physical vs intelligence” level to generate saturation dynamics. We default to 0.6: thinking and doing are complements at the economy level — plans are worth little without hands to execute them and vice versa — so abundant cognitive AI labor alone cannot substitute for scarce physical capacity. |
| θ | 0.68 | **Cognitive task weight.** Fraction of labor tasks that are cognitive vs physical. Regional defaults: **US 0.68** (services-heavy economy), **China 0.50** (manufacturing-heavy, balanced cog/phys mix), **World 0.60** (GDP-weighted average). Auto-syncs with the region toggle. |
| σ<sub>c</sub> | 0.80 | **Across-task elasticity (cognitive).** How complementary are automatable and non-automatable cognitive tasks. \<1 = non-automatable tasks bottleneck automatable tasks. Within the automatable bucket, humans and AI are always perfect substitutes regardless of this parameter. |
| σ<sub>p</sub> | 0.80 | **Across-task elasticity (physical).** Same logic as σ<sub>c</sub>. How much non-automatable physical tasks constrain the value of robot-automated tasks. |
| s<sub>base</sub> | 0.19 | **Base savings rate.** Gross savings / GDP at baseline interest rate. Regional defaults: **US 0.19, China 0.428, World 0.262**. Responds endogenously to interest rate: s(r) = s<sub>base</sub> × ((1+r)/(1+r<sub>base</sub>))<sup>η</sup> with η = 0.8. |
| LFP<sub>target</sub> | 0.62 | **Labor-force participation target.** Base-year LFP; used as the anchor for the logistic LFP response (eq. 12). Regional defaults: **US 0.62, China 0.648, World 0.686**. Auto-syncs with the region toggle. |
| β<sub>w</sub> | 0.4 | **Wage sensitivity of LFP.** Logistic shift per log-point of wage change: β<sub>w</sub> × ln(w̄/w̄<sub>0</sub>). Higher wages → higher LFP. Plan A uses 0.4 (citizen dividends and the regulatory regime cushion the wage→participation link); Default World uses 1.5 (no buffers, labor supply tracks wages more strongly). |
| β<sub>u</sub> | 2.5 | **Citizen-dividend sensitivity of LFP.** Logistic shift per log-point of citizen dividend relative to base wage: −β<sub>u</sub> × ln(1 + CD/w̄<sub>0</sub>). Higher dividends → lower LFP, but with diminishing marginal effect at extreme \$ levels (matching the &log;-elasticity convention used in labor-supply studies and the β<sub>w</sub> wage term). At CD = base wage the shift is −0.69×β<sub>u</sub>; at CD = 100× base wage it's only −4.6×β<sub>u</sub>. This self-saturating behavior matches the intuition that an inherent desire to work persists even under very generous dividends. |

**Capital accumulation.** Capital evolves via the law of motion:

K<sub>t+1</sub>  =  s(r<sub>t</sub>) · Y<sub>t</sub>  +  (1 − δ) · K<sub>t</sub> **s** = investment rate (fraction of GDP invested as new capital each year; “savings rate” in econ terminology—in a closed economy, savings ≡ investment by accounting identity). **δ** = depreciation rate (default 5.3%—the fraction of the capital stock that wears out or becomes obsolete each year). **r** = interest rate (the marginal product of capital, i.e., how much one extra dollar of capital contributes to output—computed from r = α · Y / K, where **α** is the capital share of output, **Y** is output, and **K** is the capital stock; so r = capital income / capital stock).

With endogenous savings (on by default, can be toggled off for a flat rate), the investment rate responds to the interest rate via a constant-elasticity response on the gross return (1+r), following the log-linear specification used by [Boskin (1978)](https://www.jstor.org/stable/1829972) in his empirical work on savings elasticity:

s(r) = s<sub>base</sub> × ((1+r) / (1+r<sub>base</sub>))<sup>η</sup> **s<sub>base</sub>** = baseline investment rate (19% for US, matching current gross savings/GDP). **r<sub>base</sub>** = the interest rate in 2025 (calibrated from the base-year production function). **η** = savings elasticity (default 0.8).

Boskin (1978) estimated empirical savings elasticities of 0.2–0.4 for postwar US data, but those estimates come from economies where consumption is dominated by necessities and saving is constrained by subsistence needs. Our scenarios depart from that regime in two ways, both pointing toward a higher elasticity:

- **Vertically-integrated AI/robot producers.** In our preset scenarios, we think it is very possible that firms producing AI and robots will—instead of publicly deploying or selling them—plow their output and labor back into expanding their own production capacity rather than selling to outside consumers. This would effectively function as a firm-level savings rate near 1. In the extreme, we could see fully self-replicating robot factories, or a takeover scenario in which AI and robots scale themselves—an economy-wide savings rate close to 100%, with no human consumption at all. Even in a more normal case where output routes through distributed household income (even if very unequally), we think savings elasticity could still be higher in high-abundance scenarios—as explained in the next point.
- **Luxury-shifted consumption.** As output and incomes grow drastically, as they do in our preset scenarios, we expect consumption to shift toward discretionary and luxury goods. We guess that discretionary consumption is more deferrable than necessities, so a larger share of output can be redirected into investment even if it is routing through households.

We chose **η = 0.8** so endogenous savings can rise meaningfully with r and approximate such regimes in the limit, without saturating the 100% savings cap too aggressively at moderate takeoff-r values. This is a judgment call, not a direct empirical finding.

Numerically, with s<sub>base</sub> = 19% and r<sub>base</sub> ≈ 14%: if returns hit 10× baseline (r ≈ 140%), savings rises to ~35%; at r ≈ 500% savings reaches ~72%; the 100% cap binds around r ≈ 810%. With the toggle off, investment stays flat at s<sub>base</sub>.

Limitations of the growth / production-function model

The production function and growth dynamics make several deliberate simplifications. Known limitations include:

Labor and wages

- **Factor prices are marginal products, not forecasts of pay.** All prices (w<sub>c</sub>, w<sub>p</sub>, q<sub>c</sub>, q<sub>r</sub>, r) are derived through the nested CES chain rule. They are indicators of *productive contribution*, not forecasts of actual compensation—real pay depends on bargaining power, institutions, policy, labor-market frictions, and norms that the model does not capture.
- **Humans perfectly reallocate across tasks.** The task-bucket optimization assumes humans costlessly shift between automatable and non-automatable tasks each year. We probably overstate employment and labor-force participation as a result—in reality, frictions would slow reallocation and produce displacement even when aggregate employment *could* in principle stay high.

Real vs nominal / composition of growth

- **Real-output focused, 2025-dollar anchored.** The model tracks real output and real factor prices, with everything expressed in 2025-dollar terms. It abstracts from price-level dynamics and the composition of growth. In reality, a lot of the gain from AI may show up as *consumer surplus*—cheaper goods and services—rather than higher nominal GDP. Nominal growth during an AI takeoff could plausibly be much lower than the real output numbers this model produces.

Savings, capital markets, and intertemporal dynamics

- **Ad-hoc savings response.** The Boskin-style power law s(r) = s<sub>base</sub> × ((1+r)/(1+r<sub>base</sub>))<sup>η</sup> is a reduced-form approximation, not derived from household preferences.
- **No forward-looking consumption decisions.** Households don’t anticipate future returns or smooth consumption over time — they just save a fraction of current income based on the current interest rate. A proper optimizing model would have savings respond to *expected future* returns too, which could shift the timing of investment.
- **No capital markets, credit, or money creation.** Investment each year is funded entirely from the previous year’s savings (s × Y<sub>t−1</sub>). There is no borrowing against future output, no leverage, no monetary expansion. In reality, during an AI takeoff firms would likely leverage heavily against anticipated productivity gains, potentially pulling forward a lot of the investment our model stretches out over years.
- **No foreign investment flows between regions.** The US, China, and World simulations run independently; real-world capital flows between regions are not modeled.

### Cost Explorer[↑ top](#top)

**Core question:** How much does it cost to produce AI chips and robots?

Production costs decline through two multiplicative channels:

Cost \$ = (Cost \$)<sub>2025</sub> × Wright (\$/unit produced) × Jones (quality/unit)

Wright’s Law drives down the **manufacturing cost per unit** (learning-by-doing, economies of scale). Jones drives down the **design cost per unit of quality-adjusted capability** (R&D makes each unit you produce, even at fixed quantities, more capable). Both indices start at 1.0 in 2025 and decline over time, multiplicatively reducing cost.

**Motivation.** In AI chips there are two dynamics we want to capture separately:

1.  **Pure chip design and quality** (Jones channel): how much compute performance can you extract per fixed unit of manufacturing, e.g. transistors/compute per wafer. Driven by R&D into chip architecture, process nodes, and design.
2.  **Pure production cost** (Wright channel): how cheap is it to actually manufacture a wafer, e.g. AI and robots improving the cost of raw materials, manufacturing inputs, fab labor, etc. Driven by cumulative production experience and scale.

The same two-channel split applies to robots (Wright = cost per physical unit; Jones = capability per unit).

**Wright’s Law (manufacturing learning).** Each doubling of cumulative production reduces manufacturing cost by a fixed percentage (Wright 1936). One of the most robust empirical regularities in economics, it has held across semiconductors, solar panels, batteries, and many other technologies.

Wright<sub>i,t</sub> = (Q<sub>cum,t</sub> / Q<sub>cum,0</sub>)<sup>−b</sup>

|  |  |
|----|----|
| Q<sub>cum</sub> | Cumulative production (total units ever produced) |
| b | Learning rate. Each doubling of Q<sub>cum</sub> reduces cost by (1 − 2<sup>−b</sup>). Default values for AI chips and robots are set in the "Wright's Law & Jones parameter defaults & calibration" section below. |

**Jones (1995) design improvement.** This is the model’s key mechanism for how AI feeds back into its own cost decline:

rate(t) = r<sub>base</sub> × (L<sub>design</sub> / L<sub>design,2025</sub>)<sup>λ</sup> × D<sup>1−φ</sup>

|  |  |
|----|----|
| r<sub>base</sub> | Current rate of design improvement. AI hardware: 10%/yr (the compute supplement’s controlled Plan A design decline, §2.2). Robots: 5%/yr. |
| λ (lambda) | **Stepping-on-toes.** If you 10× the researchers, progress gets 10<sup>λ</sup> faster. With λ=0.2: 10× researchers → only **1.6×** faster. Most additional researchers are redundant—they work on the same problems, make the same discoveries independently. |
| φ (phi) | **Fishing out.** As cumulative progress grows, the rate of improvement is multiplied by D<sup>1−φ</sup>. After a 100× cost reduction: with φ=0.90, the rate is 63% of original (moderate drag). With φ=0.95, it’s 79% (gentle). |
| λ/(1−φ) | **The key ratio** ≈ 5 for semiconductors. From Bloom et al. (2020): 18× more semiconductor researchers over 43 years maintained constant Moore’s Law. Each OOM of researcher growth bought ~5 OOMs of cumulative progress. |
| L<sub>design</sub> | R&D workforce = L<sub>eff</sub> × allocation %. As AI scales L<sub>eff</sub>, more goes to design R&D → feedback loop (but with strong diminishing returns via λ and φ). In the **Plan A Scenario** preset, the exogenous R&D trajectory reflects governance to titrate R&D heavily, so the % of L<sub>eff</sub> allocated to R&D shrinks significantly after 2032. In the **Default World** preset it rises and stays flat at high levels post-2030. |

**The feedback loop:** More AI deployed → L<sub>eff</sub> grows → more effective labor available for design R&D (L<sub>design</sub> = L<sub>eff</sub> × frac<sub>R&D</sub>) → Jones equation speeds up design improvement → costs fall → AI becomes cheaper to deploy. This is the model’s one semi-endogenous channel—but with λ=0.2, the feedback has strong diminishing returns (10× more R&D workers only speeds progress by 1.6×). The R&D allocation fraction (frac<sub>R&D</sub>) is set as an exogenous time series on the **Cost-Side Input** tab.

Wright’s Law & Jones parameter defaults & calibration

Set in the Parameters panel under “Cost-Side Parameters” or in the Cost-Side Input tab.

Wright’s Law

|  |  |  |
|----|----|----|
| b<sub>AI</sub> | 0.25 | **AI chip learning rate.** Calibrated to the compute supplement’s §2.2 implied-investment model (`impliedInvestmentModel.ts`, Wright b = 0.25 ≈ 16% cost cut per doubling of cumulative output), so the explorer’s production-cost path reproduces the supplement’s \$/H100e. |
| b<sub>robot</sub> | 0.20 | **Robot learning rate.** Higher than AI chips because humanoid robots are early on the experience curve—analogous to where semiconductors were in the 1970s. Uncertain due to minimal cumulative production to date. |

Jones Design Improvement

|  |  |  |
|----|----|----|
| r<sub>base,AI</sub> | 0.10 | **AI HW design base rate.** 10%/yr = the compute supplement’s controlled Plan A design decline (§2.2 `impliedInvestmentModel.ts` JONES_CTRL) under the titrated-R&D regime. Anchors where the Jones trajectory starts. |
| r<sub>base,robot</sub> | 0.05 | **Robot design base rate.** 5%/yr. Rough estimate for current robot design improvement—industrial robots have improved ~2–3%/yr historically, but humanoid robots may be improving faster. |
| λ<sub>AI</sub> | 0.20 | **AI stepping-on-toes.** From Sequeira & Neves (2020): cross-country estimates find λ ≈ 0.2 across many domains. Means 10× researchers → 1.6× faster progress. Bloom et al. (2020) data is consistent: 18× semiconductor researchers didn’t speed up Moore’s Law. |
| λ<sub>robot</sub> | 0.20 | **Robot stepping-on-toes.** Same as AI—no strong reason to differentiate. Less empirical evidence for robotics specifically. |
| φ<sub>AI</sub> | 0.90 | **AI fishing-out.** Moderate idea depletion. With λ=0.2: λ/(1−φ) = 0.2/0.1 = 2.0, below the historical steady-state ratio of ~5. |
| φ<sub>robot</sub> | 0.933 | **Robot fishing-out.** With λ=0.2: λ/(1−φ) = 0.2/0.067 ≈ 3.0 — slightly above aggregate-TFP and agriculture (Bloom et al. 2020 estimate ~3 for ag) but below semiconductors (~5). |

How to think about λ/(1−φ)

This ratio is the “OOMs of progress per OOM of researcher growth” in steady state. Bloom et al. (2020) found ~5 for semiconductors: every 10× increase in researcher count sustained ~100,000× more cumulative progress (5 OOMs) over the same period. Our forward-looking parameters give **2.0 for AI**, reflecting an expectation that the historical pace will slow as leading-edge semiconductors approach physical limits. For **robots we use 3.0**, chosen as a middle point between aggregate-TFP/agriculture (Bloom et al. report ~3 for ag, 2–4 for aggregate US TFP) and semiconductors (~5). There is no direct Bloom-style estimate for robotics.

**Markups.** Exogenous time-varying trajectories applied on top of marginal cost. Informed by observed market structure (e.g., TSMC’s dominance in AI chip fabrication) but user-specified, not modeled endogenously. Total price = MC × μ<sub>manufacturing</sub> × μ<sub>design</sub>. (Set on the **Cost-Side Input** tab.)

**Surplus.** The gap between what AI/robots produce (marginal product from the growth model) and what they cost (production cost + markup) is surplus. It’s split three ways:

- **Producer surplus** — the markup above marginal cost (goes to manufacturers/designers)
- **Buyer surplus** — the gap between value and purchase price (goes to firms deploying AI/robots)
- **Government** — taxes + cap-and-trade permit revenue (funds citizen dividends)

**Cap-and-trade.** The Plan A scenario includes a cap-and-trade regime where governments issue a certain number of permits to produce restricted goods (including AI chips and robots) in order to restrict overly destabilizing production levels. Compared to status-quo economics today, these caps are set very high, allowing robots to double every 6 months and AI chips to grow 5× per year in early years, but then flattening after 2035 when scaling is paused for other reasons in the Plan A scenario. Each new AI chip or robot requires a permit, and the model prices these permits as a fraction of the unit's discounted forward-looking lifetime surplus: the model's own projected per-unit surplus (marginal value minus market price, which erodes as later years' cheaper and more numerous units arrive) summed over the unit's service life (3 years for chips, 5 for robots) and discounted back at the model's endogenous interest rate r = αY/K. The fraction is an “auction efficiency” η(t), evaluated at the permit’s issue year: by default it is flat at 0.80 across the horizon — well-designed auctions capture most, but not all, of the units’ surplus (the 2032 and 2040 anchors are separately editable on the Cost-Side inputs for sensitivity runs, with linear interpolation between them). The cost model runs once at the world level — the chip and robot chains are a single global market — and the resulting world permit revenue is divided among governments by treaty share: US 35%, China 20%, Rest-of-World 45%. Each region pays out a domestic citizen dividend from its share (default fraction 25% in 2032 → 75% in 2035 → 60% in 2040, applied to the region’s full AI + robot permit revenue), and the US and China additionally send a foreign-aid fraction of their shares (default 10% → 10% → 30% on the same anchors) into the Rest-of-World dividend pool; the remainder is retained by each government. With cap-and-trade enabled, the AI/robot quantities specified in the growth model are automatically treated as the quantities permitted by the cap-and-trade regulation.

### Energy Explorer[↑ top](#top)

We added an exploratory energy model that has (i) total primary energy demand, (ii) the bottom-up energy consumption of AI compute and robots, (iii) climate externalities (waste heat, CO<sub>2</sub> emissions), and (iv) naive energy cost modelling by type of generation source (CapEx, OpCost, LCOE) and an endogenous function to decide what energy gets built over time. It also implements optional carbon credit auctioning, where in the desired year, the cost to offset emissions of each generation source is added to the cost of that source. Like the cost model, it leaves the growth-model factor prices untouched, it is not a part of the core model.

Total primary energy (top-down, GDP-anchored)

Global energy consumption in 2025 was around 19.0 TW-yrs. In the Plan A scenario, there is ~270× cumulative GWP growth by 2040 (on our default model assumptions). If the energy intensity of the economy (ratio of GDP to energy consumption) stayed constant, then energy consumption would also increase by 270× — but historically we have observed a decrease in energy intensity since 1920.

We expect this energy decoupling to continue, because the drivers of growth (AI, robots, and accompanying capital) should all become more energy efficient per unit of economic output (AI hardware in particular has a strong power-efficiency trend). In our energy model, we assume the energy-decoupling trend of the last few decades will continue, and energy consumption will grow at roughly 40% the pace of economic growth (we call this energy growth / GDP growth the *energy elasticity of GDP*, ε = 0.4). We are highly uncertain about this value, and find values between 20% and 70% plausible (80% CI, conditional on this economic growth trajectory).

E<sub>t</sub> = E<sub>2025</sub> · (Y<sub>t</sub> / Y<sub>2025</sub>)<sup>ε</sup>

An energy elasticity of GDP of 40% leads to energy consumption on Earth growing around 9× during Plan A, bringing total primary energy to 180 TW-yrs by 2040 (the 20% case lands at 60 TW-yrs, the 70% case at 960 TW-yrs).

Equations & defaults

E<sub>t</sub> = E<sub>2025</sub> · (Y<sub>t</sub> / Y<sub>2025</sub>)<sup>ε</sup>

|                  |                                     |
|------------------|-------------------------------------|
| E<sub>2025</sub> | 19 TW-yrs (IEA primary energy 2025) |
| ε                | 0.40 (default; 80% CI 0.2–0.7)      |

AI compute and robot energy, bottom-up

For AI compute and robots we separately model their power efficiency and combine with the stocks from the growth model to get their total power draw. We assume AI compute draws roughly 1,000 W per H100-equivalent at 2025 efficiency, and a human-equivalent robot draws around 4,000 W. We then assume both per-unit numbers improve over time at a Jones-style rate driven by the same R&D allocations as the cost model — so AI-driven progress on chip cost and AI-driven progress on chip power efficiency are tied together.

In the Plan A scenario this produces AI compute energy that grows from ~10 GW-yrs in 2025 to around 26 TW-yrs by 2040, with robot energy around 33 TW-yrs — so AI plus robots is roughly 33% of total energy by 2040, up from less than 1% today. “Other” (industry, transport, buildings, residential) is the rest.

Equations & defaults

W<sup>new</sup><sub>j,t</sub> = W<sup>new</sup><sub>j,2025</sub> · D<sup>en</sup><sub>j,t</sub> \[frontier W per unit, Jones-driven\] W<sup>avg</sup><sub>j,t</sub> = vintage average over surviving + new units E<sup>tech</sup><sub>j,t</sub> = S<sub>j,t</sub> · W<sup>avg</sup><sub>j,t</sub>

Per-unit power anchors (2025)

|  |  |
|----|----|
| W<sup>new</sup><sub>AI,2025</sub> | 1,000 W per H100-equivalent (server-board total) |
| W<sup>new</sup><sub>robot,2025</sub> | 4,000 W per HE-robot |

Jones design improvement (per intensity)

|       | r<sub>base</sub> | λ    | φ    |
|-------|------------------|------|------|
| AI    | 0.26             | 0.20 | 0.85 |
| Robot | 0.05             | 0.60 | 0.95 |

Depreciation rates δ<sub>AI</sub> = 0.30 and δ<sub>robot</sub> = 0.10 are shared with the cost model.

Climate externalities

Depending on the energy source, this scale-up has implications for the Earth's surface temperature. There are two separate things to consider: (1) a net increase in waste heat on Earth, and (2) emissions — particularly CO<sub>2</sub> — leading to temperature increases through radiative forcing.

**Waste heat.** Solar panels convert energy that was arriving on Earth anyway from the sun, so they only change Earth's net energy balance if they meaningfully change the planet's albedo. Nuclear and fossil generation, on the other hand, create a direct increase in waste heat by releasing energy that was previously locked up in the Earth's crust. That said, even at the higher end of levels we might reach by 2040 in Plan A, waste heat on its own does not become a major consideration. A back-of-envelope: 50 TW of fossil and nuclear waste heat spread over Earth's surface is roughly 0.1 W/m<sup>2</sup> of additional forcing, against ~3 W/m<sup>2</sup> from accumulated CO<sub>2</sub>. We drop heat and albedo externalities from the model accordingly.

**Carbon emissions.** If fossil fuels were used as the sole source for this energy scale-up, carbon emissions would become a significant problem by 2040 absent significant mitigation (e.g. direct air capture), with equilibrium surface temperature rising to roughly +3.0°C over pre-industrial levels, up from +1.8°C today.

We therefore think there should be CO<sub>2</sub> emission mitigation policies agreed to globally. Direct air capture (DAC) provides an affordable path to mitigation, especially with help from AI and robot labor during the 2030s — the thermodynamic floor for separating CO<sub>2</sub> from the atmosphere is around 0.034 MWh per tonne, and engineered systems get within ~15× of that today (Climeworks Mammoth, ~\$600/tCO<sub>2</sub>). We assume DAC costs \$30/tCO<sub>2</sub> by 2040.

The carbon policy the model can support is:

- **Private cap-and-trade market (no government subsidy needed).** Any fossil emitter globally is required to offset 100% of emissions with equivalent carbon-capture credits. DAC operators earn revenue by capturing carbon and selling credits to emitters. Reaches net-zero emissions but does not draw down legacy CO<sub>2</sub>.

The cap-and-trade regime is priced into the energy mix by adding the per-source lifecycle emissions (× the CO<sub>2</sub> price) onto each source's marginal cost. By default, the model enacts the cap-and-trade regime in 2035 with credits priced at the DAC cost curve; in the Default World scenario, policy is assumed not to bind and no carbon price is charged.

Defaults

Per-source lifecycle emissions (gCO<sub>2</sub>eq / kWh, IPCC AR6 WGIII Annex III medians)

|         |                                                              |
|---------|--------------------------------------------------------------|
| Fossil  | 660 (combustion + upstream fuel cycle)                       |
| Nuclear | 12 (enrichment + concrete + decommissioning)                 |
| Hydro   | 24 (dam concrete/steel + reservoir CH<sub>4</sub>)           |
| Solar   | 48 (panel + battery manufacturing; declines via CapEx Jones) |
| Wind    | 11 (turbine + tower; declines via CapEx Jones)               |
| Other   | 230 (geothermal + biofuel blend; declines via CapEx Jones)   |

DAC cost trajectory

|  |  |
|----|----|
| 2025 | ~\$600 / tCO<sub>2</sub> (Climeworks Mammoth operational cost) |
| 2040 | \$30 / tCO<sub>2</sub> (singularity floor; thermodynamic min 0.034 MWh/tCO<sub>2</sub>) |

Cap-and-trade enactment year: **2035** (Plan A); not enacted in Default World.

Energy cost model

Each generation source has cost modelling for CapEx (\$/W-delivered) and OpCost (\$/MWh), naively estimated from today's levels and modelled forward. Levelized cost is the standard formula, with both capex and opex amortized at a real WACC of 7% (interpreted as the r−g risk premium):

LCOE<sub>i,t</sub> = CapEx<sub>i,t</sub> · CRF<sub>i</sub> · 114.16 + OpCost<sub>i,t</sub> + externality<sub>i,t</sub> **CRF<sub>i</sub>** = WACC / (1 − (1+WACC)<sup>−Life<sub>i</sub></sup>) is the capital recovery factor. **114.16** = 1000 / 8760 converts \$/W-delivered·year to \$/MWh.

We feed in CapEx and OpCost separately rather than a single LCOE because they evolve differently. The 2025 anchors produce a stock-weighted average of around \$63/MWh, which matches the world energy bill divided by TWh consumed.

Equations & defaults

LCOE<sub>i,t</sub> = CapEx<sub>i,t</sub> · CRF<sub>i</sub> · 114.16 + OpCost<sub>i,t</sub> + ext<sub>i,t</sub> CRF<sub>i</sub> = WACC / (1 − (1+WACC)<sup>−Life<sub>i</sub></sup>) CapEx<sub>i,t</sub> = CapEx<sub>i,2025</sub> · D<sup>cap</sup><sub>i,t</sub>,  OpCost<sub>i,t</sub> = OpCost<sub>i,2025</sub> · D<sup>op</sup><sub>i,t</sub>

WACC = 0.07 (real risk premium r−g). 114.16 = 1000 / 8760 converts \$/W-delivered·year to \$/MWh. D<sup>cap</sup>, D<sup>op</sup> are per-source Jones design indices.

Physical plant lifetimes (years)

| Fossil | Nuclear | Hydro | Solar | Wind | Other |
|--------|---------|-------|-------|------|-------|
| 35     | 55      | 90    | 28    | 22   | 28    |

CapEx 2025 anchors (\$/W-delivered) + Jones params (r<sub>base</sub>, λ, φ)

|         | Anchor | r<sub>base</sub> | λ    | φ    |
|---------|--------|------------------|------|------|
| Fossil  | 1.5    | 0.02             | 0.10 | 0.85 |
| Nuclear | 5.0    | 0.05             | 0.20 | 0.80 |
| Hydro   | 4.0    | 0.01             | 0.05 | 0.20 |
| Solar   | 5.0    | 0.20             | 0.05 | 0.65 |
| Wind    | 3.5    | 0.10             | 0.10 | 0.65 |
| Other   | 4.0    | 0.04             | 0.05 | 0.95 |

OpCost 2025 anchors (\$/MWh) + Jones params (r<sub>base</sub>, λ, φ)

|         | Anchor | r<sub>base</sub> | λ    | φ    |
|---------|--------|------------------|------|------|
| Fossil  | 50     | 0.05             | 0.10 | 0.85 |
| Nuclear | 50     | 0.10             | 0.20 | 0.80 |
| Hydro   | 20     | 0.02             | 0.05 | 0.20 |
| Solar   | 5      | 0.05             | 0.10 | 0.65 |
| Wind    | 15     | 0.05             | 0.10 | 0.65 |
| Other   | 25     | 0.05             | 0.20 | 0.85 |

Endogenous energy mix

Each year, new capacity is allocated across sources by a softmax over LCOE: cheaper sources get most of the new builds, but not all of it (the temperature parameter governs how aggressively the cheapest source dominates). The market price each year is the stock-weighted average LCOE across the remaining fleet.

In Plan A with the 2035 cap-and-trade regime, this produces a fairly sharp transition: by 2032 solar and wind dominate new builds but the deployed mix is still mostly legacy fossil, which is already getting outcompeted by scaling solar/wind/nuclear on our naive cost model, then in 2035 carbon credits fire, fossil's marginal cost spikes from ~\$50 to ~\$116/MWh with the DAC caputre requirement, while renewables are at ~\$30/MWh, and this retires almost all fossil within a single year. By 2040 the mix is approximately 100% solar / wind / nuclear.

Total energy investment peaks at 6–8% of GWP in 2032–2034 (demand growth and fossil-replacement build-out fire simultaneously), then falls as the CapEx Jones drives solar and wind below \$1 per W-delivered.

Equations & defaults

New-build allocation (softmax over LCOE)

share<sub>i</sub> ∝ exp(−(LCOE<sub>i</sub> − min<sub>j</sub> LCOE<sub>j</sub>) / σ)

Stock-weighted market price

P<sub>market</sub> = ∑<sub>i</sub> s<sub>i</sub> · LCOE<sub>i</sub>

Retirement rate per source

rate<sub>i</sub> = 1 / Life<sub>i</sub> + max(0, MC<sub>i</sub>/P<sub>market</sub> − 1) / τ<sub>patience</sub>

MC<sub>i</sub> = OpCost<sub>i</sub> + ext<sub>i</sub> is the marginal operating cost (no sunk capex). A plant retires when it can't cover its own opex at the going market price.

Allocation / retirement parameters

|  |  |
|----|----|
| σ (softmax temperature) | 10 \$/MWh. Lower = winner-take-all, higher = more diversified new-build mix. |
| τ<sub>patience</sub> | 1 year. Lower = faster retirement of uneconomic plants. |

2025 starting energy mix (TW)

| Fossil | Nuclear | Hydro | Solar | Wind | Other |
|--------|---------|-------|-------|------|-------|
| 12.5   | 0.3     | 1.0   | 0.4   | 0.4  | 1.4   |

Limitations of the energy and climate model

- **Cost modelling is extremely naive.** Each generation source's CapEx and OpCost trajectories are propagated forward with Jones-style parameters that we don't have good data or well-justified values for. The cost trajectories should be read as illustrative rather than calibrated.
- **DAC cost is also not well justified.** The trajectory from ~\$600/tCO<sub>2</sub> today to \$30/tCO<sub>2</sub> by 2040 is anchored on Climeworks today and a thermodynamic-floor BOTEC, with the rate of progress in between essentially guessed.
- **Top-level primary energy is naive.** The single-ε decoupling formula extrapolates a historical trend forward with no structural model of where energy is actually consumed. The implied non-AI / non-robot power consumption (industry, transport, buildings, residential) — which we just back out as the residual between total energy and the bottom-up AI+robot energy — might not be in a reasonable range for a singularity-era economy.
- **AI and robot power efficiency is uncertain but somewhat better grounded.** The Jones-style trajectories on W per H100-equivalent and W per HE-robot are also uncertain, but the AI compute power-efficiency trend has been clear and consistent for decades, so we at least have a sense of what to anchor to there.

### Extensions (scenario exploration)[↑ top](#top)

Exploratory add-ons to the growth and cost model that add more scenario color.

Endogenous AI and robot quantities (Default World)

Unlike the other extensions in this section (which are post-hoc layers that leave the core growth model untouched), this one *replaces* the exogenous AI and robot trajectories the user draws in the input tabs with an investment-allocation rule. It is what the **AI 2040 Default World** preset runs.

**Investable savings pool.** Each year the same pool s(r<sub>t</sub>) · Y<sub>t</sub> that funds capital now funds all three of capital, AI hardware, and robot hardware. Under **Plan A**, 100% of the pool goes to capital and AI/robot quantities follow the user trajectories, with a post-hoc display of what investment that requires in the cost model; under **Default World**, the pool is split across K, AI, and robots in proportion to a naive myopic **return on investment**, defined as the annual marginal product at current rates per \$1 invested. Because of the explosive growth these scenarios experience, we think this is a decent proxy — the “useful life” of the new production being greater than 1 year may even be too long if anything, given the likely speed of change of the technology.

ROI<sub>K</sub> = r,  ROI<sub>AI</sub> = q<sub>c</sub> / MC<sub>per AI HE</sub>,  ROI<sub>robot</sub> = q<sub>r</sub> / MC<sub>per robot HE</sub> **r** = αY/K is the interest rate. **q<sub>c</sub>, q<sub>r</sub>** are the AI and robot rental rates (∂Y/∂A<sub>eff</sub>, ∂Y/∂R). **MC<sub>per AI HE</sub>**, **MC<sub>per robot HE</sub>** are the cost model's lifetime marginal costs per human-equivalent unit, which decline over time via Wright's Law (learning) and Jones R&D (design improvement).

**Allocation rule.** Shares are set proportionally to ROI: φ<sub>K</sub> = ROI<sub>K</sub> / ∑ROI, and analogously for AI and robots. The combined AI+robot share φ<sub>AI</sub> + φ<sub>robot</sub> is capped at the average automation frontier (f<sub>c</sub> + f<sub>p</sub>) / 2 of 2024 non-automated tasks — which we use as a proxy for the cap on what the economy can reinvest into AI and robot production.

**Within-year equilibration.** Pure start-of-year allocation is winner-take-all: whichever factor happens to have the highest ROI that year absorbs nearly all investment, and shares flip abruptly year-over-year as the leading factor saturates. To smooth this and better approximate market equilibrium, within each year we iterate: pick shares, advance stocks by the implied investment, re-solve the production function at the *post*-investment stocks, recompute ROIs, and update shares with damping. Five iterations typically reduce the spread between the three ROIs to within 5%.

**Stock accumulation.** After the shares converge, stocks update:

AI<sub>t+1</sub> = (1−δ<sub>AI</sub>) · AI<sub>t</sub> + φ<sub>AI,t</sub> · s(r<sub>t</sub>) Y<sub>t</sub> / MC<sub>per AI HE,t</sub> R<sub>t+1</sub>  = (1−δ<sub>R</sub>) · R<sub>t</sub>  + φ<sub>robot,t</sub> · s(r<sub>t</sub>) Y<sub>t</sub> / MC<sub>per robot HE,t</sub> K<sub>t+1</sub>  = (1−δ) · K<sub>t</sub>   + φ<sub>K,t</sub> · s(r<sub>t</sub>) Y<sub>t</sub> In Plan A (exogenous quantities), φ<sub>K</sub> = 1 and the K law reduces to the standard Solow–Swan equation.

**Singularity cutoff.** If Y<sub>t+1</sub> / Y<sub>t</sub> \> 1000 in any year, the simulation stops — a numerical safeguard against runaway takeoff, since by that point the model's underlying assumptions (Wright learning, fixed markups, factor-share CES structure) are well outside their domain of validity.

Goods vs. services decomposition

This add-on models the relative prices of goods and services by assuming a certain relative cognitive and physical labor intensity for each, together with a price-sensitive consumer demand system that splits spending between them as relative prices evolve over time.

Given the factor prices (w<sub>c</sub>, w<sub>p</sub>, q<sub>c</sub>, q<sub>r</sub>) and Y from the main solver, it splits output into two categories with different cognitive/physical intensity: services (cognitively heavy, θ<sub>S</sub> = 0.80) and goods (more physical, θ<sub>G</sub> = 0.40). It outputs **relative prices** P<sub>S</sub>/P<sub>G</sub> within each year (a pure within-year comparison, with the CES aggregate index normalized to 1 each year since the model does not track absolute price levels over time). The corresponding consumer expenditure shares come from a CES demand system with elasticity **η = 0.5** (the default, at the upper end of the 0.2–0.5 range Comin, Lashkari & Mestieri 2021 estimate across specifications in postwar cross-country data, and consistent with the broader structural-transformation literature: Ngai & Pissarides 2007; Herrendorf, Rogerson & Valentinyi 2013).

This was added with the idea in mind that if AI automates cognitive work faster than robots automate physical work, services might become relatively cheaper than goods at some aggregate level. Notably we don't do any cost modelling, so this does not model actual price levels over time. Being a post-hoc add-on, the core growth-model outputs are unaffected.

Equations

First some intermediate unit costs, which come "for free" from the production function by Shephard's lemma (any nested CES quantity aggregator has a matching nested CES price aggregator):

- **p<sub>cog</sub>** = unit cost of one cognitive labor hour (a CES blend of humans at wage w<sub>c</sub> and AI at rental q<sub>c</sub>).
- **p<sub>phys</sub>** = same for one physical labor hour (humans at w<sub>p</sub>, robots at q<sub>r</sub>).
- **p<sub>eff,j</sub>** = unit cost of effective labor in sector j, using that sector's cognitive weight θ<sub>j</sub> in place of the aggregate θ. Services weight cognitive higher (θ<sub>S</sub>=0.80), goods lower (θ<sub>G</sub>=0.40), aggregate at θ (0.68 for US).

One-time calibration at the base year

(19)  ν = a<sub>S</sub> · P<sub>G,0</sub><sup>1−η</sup> / \[a<sub>S</sub> · P<sub>G,0</sub><sup>1−η</sup> + (1−a<sub>S</sub>) · P<sub>S,0</sub><sup>1−η</sup>\]

Here **ν** is the CES demand weight on services (think of it as a taste/preference parameter). **a<sub>S</sub>** is the empirical base-year share of household spending on services (e.g. 0.77 for the US). **P<sub>S,0</sub>, P<sub>G,0</sub>** are the base-year sector prices from equation (20) before normalization. The formula inverts the CES spending-share equation so that if we plug ν back in, equation (21) reproduces a<sub>S</sub> at t=0. In the Cobb-Douglas special case (η=1), this collapses to simply ν = a<sub>S</sub>.

Each year

(20)  P<sub>S</sub> ∝ (p<sub>eff,S</sub> / p<sub>eff,agg</sub>)<sup>1−α</sup>,  P<sub>G</sub> ∝ (p<sub>eff,G</sub> / p<sub>eff,agg</sub>)<sup>1−α</sup>

**P<sub>S</sub>, P<sub>G</sub>** are the relative output prices of services and goods within a given year. The ratio on the right is "how much more/less expensive labor is in this sector than at the economy-wide average." The exponent **1−α** is the labor share of output: in a Cobb-Douglas Y = A · K<sup>α</sup> · L<sup>1−α</sup>, a 1% change in labor cost flows through to a 1−α percent change in output price (capital cost r is common across both sectors, so it cancels). Both prices are rescaled each year so the CES aggregate index P<sub>agg</sub> = CES(P<sub>S</sub>, P<sub>G</sub>; ν, η) = 1. This is purely a numeraire choice: only the ratio P<sub>S</sub>/P<sub>G</sub> is meaningful. The model does not track absolute price levels over time.

(21)  S = ν · P<sub>S</sub><sup>−η</sup> · Y,  G = (1−ν) · P<sub>G</sub><sup>−η</sup> · Y

**S, G** are the real quantities consumed of each sector. **Y** is total real output (to be allocated between S and G). CES demand: if services are relatively cheaper this year, people want more of them. **η = 0.5** means the response is sub-unitary, so a 1% drop in relative service price raises service quantity by only 0.5%, which means spending on services (price × quantity) actually *falls* (price fell more than quantity rose). At η = 1 (Cobb-Douglas), spending shares are constant. At η \> 1, cheaper sectors take a bigger spending share.

We use η = 0.5 because empirical estimates from the structural-transformation literature (Ngai & Pissarides 2007; Herrendorf, Rogerson & Valentinyi 2013; Comin, Lashkari & Mestieri 2021) find the goods-services substitution elasticity is well below 1, typically in the 0.2–0.5 range.

Land

The land add-on models demand for four land categories (urban, rural, agricultural, and commercial), each with its own starting expenditure share and its own elasticities. Each category has an **income elasticity β** (how demand responds to rising incomes), a **demand elasticity η<sup>D</sup>** (how demand responds to price), and a **supply elasticity η<sup>S</sup>** (how supply responds to price). Whether land expenditure grows faster, slower, or in line with overall consumption depends mostly on β: if β \> 1 the category is a luxury and its share of spending rises with income, if β \< 1 it is a necessity and its share falls, if β = 1 spending scales proportionally. Category defaults: urban and rural residential are roughly β ≈ 1.1 (slight luxury), agricultural is low β (necessity, falls as a share with income), commercial is in between. A wilderness-deregulation option releases protected land after a configurable year, loosening the supply constraint. Each period the model clears each category's land market for its rental rate and land-use share.

We have land as a post-hoc add-on as opposed to a factor in the production function, because our view is that land is unlikely to be a binding constraint on AI/robot production except through regulation: land-use footprints even under extreme growth scenarios are small relative to available land on Earth, so we currently don't think modeling land as a bottleneck on overall production is justified. So the more relevant and interesting thing about land would be the availability and pricing of land on the consumer side, which is what we try to add some color to with this extension.

Equations & defaults

For each endogenous category i (urban, rural, agricultural), let v<sub>i</sub> be land rent per hectare, M<sub>i</sub> the acres supplied/demanded, R<sub>i</sub> the total rent spent on that category, X total consumer expenditure, and v<sub>i,0</sub>, M<sub>i,0</sub>, X<sub>0</sub> the base-year values of those variables.

Consumer expenditure

(22)  X<sub>t</sub> = (1 − s(r<sub>t</sub>)) · Y<sub>t</sub> (output minus savings, using the endogenous s from eq 6)

X is not calibrated to a fixed share of Y; it fluctuates with the savings response to returns.

Demand and supply shapes (for each category)

M<sub>i</sub><sup>D</sup> ∝ X<sup>β<sub>i</sub></sup> · v<sub>i</sub><sup>−η<sup>D</sup><sub>i</sub></sup> (income-sensitive, price-responsive demand) M<sub>i</sub><sup>S</sup> ∝ v<sub>i</sub><sup>η<sup>S</sup><sub>i</sub></sup> (isoelastic land supply)

Market clearing, expressed in base-year-relative form

(23)  v<sub>i</sub>(t) / v<sub>i,0</sub> = (X<sub>t</sub> / X<sub>0</sub>)<sup>β<sub>i</sub> / (η<sup>D</sup><sub>i</sub> + η<sup>S</sup><sub>i</sub>)</sup> (equilibrium rent, relative to base year, as a function of expenditure growth) (24)  M<sub>i</sub>(t) / M<sub>i,0</sub> = (v<sub>i</sub>(t) / v<sub>i,0</sub>)<sup>η<sup>S</sup><sub>i</sub></sup> (acres from the supply curve at the new rent) (25)  R<sub>i</sub>(t) = v<sub>i</sub>(t) · M<sub>i</sub>(t) (total rent = rent per hectare × hectares)

If total endogenous acreage would exceed the physically available land (after removing protected wilderness and commercial floors), all endogenous land acres (M<sub>i</sub>) are scaled proportionally and prices are re-solved from the demand curve, so scarcity raises rents.

Parameter defaults (US)

| Category | β | η<sup>D</sup> | η<sup>S</sup> | Starting share of land expenditure |
|----|----|----|----|----|
| Urban | 1.1 | 1.0 | 0.5 | ~89% |
| Rural | 1.1 | 1.0 | 0.8 | ~7% |
| Agricultural | 0.1 | 0.4 | 0.6 | ~4% |

Overall land expenditure share: 6.8% of household spending at base year. Wilderness is 100% protected until the configurable deregulation year (default 2032), then ramps down over 7 years to the `protect_wilderness` floor (default 0.8). **Commercial land is exogenous**: its acreage is held fixed at the base-year value (multiplied by `protect_commercial`, default 1.0, meaning 100% protected) and its rent is not priced in the consumption-side equilibrium. It functions as a fixed set-aside that reduces the land available for the three endogenous categories, rather than being a market the model clears.

Income distribution and inequality

In this add-on, households are binned into percentiles (1, 25, 50, 75, 90, 99, 99.9) that each own different shares of the five income sources: wages, capital, AI, robots, and land. **Ownership shares across percentiles are exogenously set by the user** in the Income Distribution section of the Parameters panel; the defaults mirror real-world wealth concentration. The module does not endogenize ownership changes over time, it just treats the exogenous distributions as fixed. Output charts include:

- **Income Distribution** — per-person income by percentile over time.
- **Income Composition** — at each percentile, what fraction of income comes from wages vs capital vs AI vs robots vs land.
- **Net Worth Distribution** — accumulated wealth per percentile.
- **Gini Coefficients** — overall and by source, showing how AI shifts inequality.

This module lets you see the distributional consequences of AI-driven growth: if AI/robot rents accrue mostly to top percentiles while wages stagnate, overall GDP can rise while the median household gains little without redistribution.

Equations & defaults

For each factor j ∈ {wage, capital, AI, robot, land}, the user specifies a cumulative ownership CDF at 7 percentile breakpoints (p1, p25, p50, p75, p90, p99, p99.9) and a finer multiplier curve at 9 percentiles (p5, p10, p25, p50, p75, p90, p95, p99, p99.9). The CDF sets the coarse distribution of ownership; the multiplier curve (e.g. "income at p95 is 3.3× the mean, at p99 it's 8.5×") is a smooth fill-in used to draw distribution charts without step-function artifacts between CDF breakpoints. Notation: **share<sub>j</sub>(p)** is the fraction of factor j owned by percentile p, **m<sub>j</sub>(p)** is the income multiplier vs. the mean at percentile p, **I<sub>j</sub>(p)** is per-person income at percentile p from factor j (with I<sub>total</sub>(p) being the sum over factors plus citizen dividends plus foreign aid received), and **W<sub>t</sub>(p)** is accumulated net worth at percentile p in year t.

Ownership shares from CDF breakpoints

(26)  share<sub>j</sub>(p) = CDF<sub>j</sub>(p+dp) − CDF<sub>j</sub>(p) (piecewise-linear Lorenz)

Within-percentile multipliers

(27)  m<sub>j</sub>(p) = monotone cubic interpolation (PCHIP) of the user-specified multiplier breakpoints

Household income

(28)  I<sub>j</sub>(p) = m<sub>j</sub>(p) · share<sub>j</sub>(p) · TotalIncome<sub>j</sub>,  I<sub>total</sub>(p) = ∑<sub>j</sub> I<sub>j</sub>(p) + CD(p) + FA(p)

CD(p) is the per-person domestic citizen dividend; FA(p) is the per-person foreign aid received (zero in donor regions).

Where TotalIncome<sub>j</sub> is the aggregate income from factor j produced by the growth model (e.g. rK for capital, q<sub>c</sub>·AI_cog for AI, wages for humans). The citizen dividend CD(p) is per-capita by construction, independent of percentile.

Net worth accumulation

(29)  W<sub>t+1</sub>(p) = W<sub>t</sub>(p) + s(r<sub>t</sub>) · I<sub>total,t</sub>(p) (uses the economy-wide endogenous savings rate from eq. 6 — no separate personal-savings parameter)

Gini

(30)  Gini = 1 − 2 · ∫₀¹ L(p) dp (L(p) = cumulative income share up to percentile p)

Ownership CDF defaults (US, top-heavy)

| Factor  | p1    | p25    | p50   | p75   | p90  | p99  | p99.9 |
|---------|-------|--------|-------|-------|------|------|-------|
| Wages   | 0.004 | 0.10   | 0.25  | 0.48  | 0.70 | 0.90 | 0.97  |
| Capital | 0.0   | 0.0    | 0.02  | 0.07  | 0.27 | 0.61 | 0.80  |
| AI      | 0.0   | 0.0005 | 0.003 | 0.015 | 0.05 | 0.25 | 0.50  |
| Robots  | 0.0   | 0.001  | 0.005 | 0.025 | 0.08 | 0.35 | 0.60  |
| Land    | 0.0   | 0.0    | 0.05  | 0.20  | 0.45 | 0.80 | 0.92  |

Each row shows the cumulative fraction of total ownership held by percentiles up to and including that point. Top-1% shares implied by the defaults: wages 10%, land 20%, capital 39%, robots 65%, AI 75%. Wages are the most broadly distributed; AI and robots are the most concentrated (early AI/robot wealth accrues heavily to founders, early employees, and concentrated investor stakes). These are **exogenous** user inputs: the module projects this starting distribution forward while factor totals evolve, it does not endogenize wealth mobility.

Taxation & Citizen Dividends

Two modes for funding citizen dividends:

- **Cap-and-trade-funded dividends** (Plan A default). The government revenue stream computed in the cost model (cap-and-trade permits + labor tax + producer-surplus tax + consumption tax) pools into a redistribution budget.
- **Naive flat taxes**. Alternative: user-set tax rates on capital income (τ<sub>k</sub>), AI rental income (τ<sub>AI</sub>), and robot rental income (τ<sub>R</sub>). Simpler, lets you explore counterfactual tax structures without the full cost-model machinery.

Each region's tax base is its treaty share of the world cap-and-trade permit revenue (US 35% / China 20% / Rest-of-World 45%). Revenue is split into five configurable allocation shares, each a 3-anchor time series (2032 / 2035 / 2040, linearly interpolated): domestic dividends for US, China, and Rest-of-World, plus foreign-aid contributions from the US and China. Defaults: 25% → 75% → 60% for all three domestic shares; 10% → 10% → 30% for the two foreign-aid shares (China's schedule mirrors the US pending confirmation). The foreign-aid contributions pay into the Rest-of-World dividend pool on top of RoW's own domestic share — RoW pays no foreign aid, and a donor's domestic and foreign-aid fractions are separate slices of its share (no double-counting; domestic + foreign-aid + retained = 1). The remainder is retained by government. The per-adult dividend amount (region pool divided by that year's adult 16+ population) feeds back into labor supply via β<sub>u</sub> in the LFP equation (11).

Other cost-model outputs

- **Markup evolution** — how manufacturing and design markups (μ<sub>mfg</sub> × μ<sub>design</sub>) evolve over time, set as user trajectories reflecting expected competitive dynamics. Falling markups (e.g., as Chinese entrants emerge) reduce buyer prices even without cost improvement.
- **AI/Robot supply chain decomposition** — stacked-area charts breaking producer revenue into resource cost, value-added per layer (mfg, design), rent per layer, and buyer surplus. Shows where the margin sits in the supply chain.
- **Prices vs. costs** — lifetime value, purchase price, and production cost per human-equivalent, making visible the gap between what buyers pay and what AI/robots are worth.
- **Government revenue breakdown** — share of total gov revenue coming from AI permits, robot permits, labor tax, and other sources. Useful for understanding how fiscal dynamics shift as the mix of surplus moves between AI, robots, and human labor.
- **Cap-and-trade counterfactual** — when cap-and-trade is active, the model produces a naive per-year counterfactual showing roughly how many additional AI chips or robots could have been produced if the permit fee had instead been spent on buying more units at counterfactual (no-permit) prices. It is **not a re-simulation of the whole economy**; it's just an accounting exercise each year: take the permit revenue, divide by the counterfactual unit price, and report the implied extra human-equivalents. Wright's and Jones law is applied within-year, but the counterfactual does not feed back into subsequent years' macro state, capital stock, or factor prices.

Other model-wide limitations

Growth/production-function-specific limitations are covered in the earlier “Limitations of the growth / production-function model” section.

- **Fixed TFP per region** — each region’s TFP is calibrated to 2025 GDP and held constant. Cross-country productivity differences persist unchanged. In reality, AI diffusion would likely narrow these gaps, but the model does not capture this convergence.
- **Technology trajectories mostly exogenous** — AI/robot quantity, efficiency, and capability are user-specified. The Jones feedback (AI → more R&D → faster cost decline) and the endogenous-investment mode (Default World) are the only endogenous channels.
- **Single composite good** — no new goods, quality improvements, or consumer surplus from variety. Much of AI’s value may come through channels that never appear in GDP (related to the “real vs nominal” limitation above).
- **No trade between regions** — each region is a closed economy. No cross-border capital flows, technology diffusion, or supply chain interdependence.
- **Regional breakdown is not very trustworthy.** The US, China, and World simulations each run independently with their own parameter files and their own base-year data, and we currently use global-average parameters as a proxy for Rest-of-World. Beyond the no-trade limitation above, the independent-simulation design means the three regional lines can diverge in ways that aren't internally consistent (e.g. the summed “World (sum)” line differs from the standalone global simulation). The regional decomposition is useful for getting a rough sense of how different parameter sets affect the trajectory, but should not be read as a careful multi-region model.

Solver architecture & implementation notes

Time step and state

The model simulates 16 years (2025 to 2040) in 1-year increments. Each year has its own production-function solve plus a cost-model solve. State carried between years: capital stock K, AI stock, robot stock, cumulative production Q<sub>cum</sub> for Wright, design indices D for Jones, and (in endogenous mode) the accumulated investment-funded stocks.

Within-year solve (`solveMuOneYear`)

Given K<sub>t</sub>, AI<sub>cog,t</sub>, R<sub>phys,t</sub>, H<sub>t</sub>, and the exogenous capability frontiers f<sub>c,t</sub>, f<sub>p,t</sub>, the solver:

1.  Allocates humans across the auto and non-auto task buckets by bisection on h<sub>auto</sub>/H until the marginal products equalize across buckets (equation 7).
2.  Builds L<sub>cog</sub>, L<sub>phys</sub> from the task-based CES (equations 3, 4).
3.  Combines them into L<sub>eff</sub> via the middle CES (equation 2).
4.  Computes Y from the top-level production function (equation 1), calibrated via A at the base year.
5.  Derives wages, AI/robot rentals, and the interest rate as marginal products (equation 8) via the nested-CES chain rule.

Endogenous labor supply (LFP iteration)

When LFP responds to wages and citizen dividends (equations 9–12), the within-year solve is wrapped in a fixed-point iteration: guess H, solve for wages, recompute LFP from the new wages, update H, repeat until ΔH / H \< 1%. Damping factor 0.5 to prevent oscillation. Typically converges in 5–8 iterations.

Between-year accumulation

- **Capital:** K<sub>t+1</sub> = (1−δ) K<sub>t</sub> + s(r<sub>t</sub>) Y<sub>t</sub> − (R&D cost). R&D cost is subtracted from the investable savings pool (see Limitations).
- **Wright/Jones:** Q<sub>cum</sub> grows with production; design index D declines at the Jones rate (equations 14–15). These feed back into marginal cost the next year.
- **Endogenous mode only:** capital, AI, and robot stocks all accumulate from the investable savings pool using ROI-weighted shares. See the *Endogenous AI and robot quantities (Default World)* subsection under Extensions above for the equations.

Cost model integration

The cost model runs ONCE on the standalone world simulation (`runCostSide` over `solveCostSideOneYear`) — the chip and robot chains are a single global market, so there are no per-region cost-side runs. Each year it takes the world AI/robot quantities, cumulative production, R&D labor allocation (from L<sub>eff</sub> × user-specified fraction), and markup trajectories, and produces MC, buyer prices, surplus decomposition, and tax revenues. Permit prices (if cap-and-trade is active) are then set in a batch post-pass (`applyForwardPermitPricing`): η(t) at the issue year × the discounted forward-looking lifetime surplus over the model's own future path, discounted at its interest rate r = αY/K. Regions receive their treaty share of the world permit revenue (35/20/45), which feeds back into the citizen-dividend amount for next year's LFP calculation (one-year lag to keep the outer loop simple).

Base-year calibration

- **TFP (A)** calibrated once so Y<sub>2025</sub> matches the exogenous base-year GDP from the region params file, given the base-year K<sub>2025</sub> and L<sub>eff,2025</sub>.
- **ν** (goods/services CES demand weight) calibrated from base-year services spending share a<sub>S</sub> (equation 19).
- **Land demand/supply scale coefficients** calibrated from base-year observations of rents v<sub>i,0</sub> and acres M<sub>i,0</sub>.
- **r<sub>base</sub> for savings** set to the base-year interest rate from the first solve; used as the denominator in the Boskin savings equation so s(r<sub>base</sub>) = s<sub>base</sub>.

Singularity cutoff

In endogenous mode, if Y grows by more than 1000× in a single year, the simulation stops. This is a numerical safeguard against runaway takeoff: by the time the model is producing such growth, the underlying assumptions (Wright learning, fixed markups, factor-share CES structure) are well outside their domain of validity.

Regions run independently

The model runs a full simulation separately for US, China, and Rest-of-World when the multi-region toggle is on. There is no cross-region trade, capital flow, or technology diffusion (see Limitations). Each region has its own params file (α, θ, savings rate, base-year macro, ownership distributions, tax rates) and a separate cost-side state.

All Model Equations

Growth Model **(1)**  Y<sub>t</sub> = A · CES(K<sub>t</sub>, L<sub>eff,t</sub>; α, σ<sub>Y</sub>)  \[reduces to A · K<sup>α</sup> · L<sub>eff</sub><sup>1−α</sup> when σ<sub>Y</sub> = 1 (Cobb-Douglas); default σ<sub>Y</sub> = 1.1\] **(2)**  L<sub>eff,t</sub> = CES(L<sub>cog,t</sub>, L<sub>phys,t</sub>; θ, σ<sub>L</sub>) **(3)**  L<sub>cog,t</sub> = CES<sub>task</sub>(h<sub>auto</sub> + A<sub>eff</sub>, h<sub>non</sub>; f<sub>c</sub>, σ<sub>c</sub>)  \[perfect subs within auto, CES across\] **(4)**  L<sub>phys,t</sub> = CES<sub>task</sub>(h<sub>auto</sub> + R<sub>p</sub>, h<sub>non</sub>; f<sub>p</sub>, σ<sub>p</sub>)  \[same structure for physical\] **(5)**  K<sub>t+1</sub> = s(r<sub>t</sub>) · Y<sub>t</sub> + (1 − δ) · K<sub>t</sub> **(6)**  s(r) = s<sub>base</sub> · ((1+r) / (1+r<sub>base</sub>))<sup>η</sup>  \[endogenous savings, Boskin-style, η=0.8\] **(7)**  h<sub>auto</sub> + h<sub>non</sub> = H   s.t. MP<sub>auto</sub> = MP<sub>non</sub>  \[human allocation: equalize marginal product across buckets\] **(8)**  r = αY/K   w<sub>c</sub> = ∂Y/∂h<sub>non,c</sub>   q<sub>c</sub> = ∂Y/∂A<sub>eff</sub>  \[human cog wage = MP of humans on non-auto cog tasks; AI rental = MP of AI; w<sub>c</sub> \> q<sub>c</sub> when AI abundant\] Labor supply (endogenous LFP) **(9)**  H<sub>t</sub> = WAP<sub>t</sub> · LFP<sub>t</sub>  \[total human labor = working-age pop × participation rate; feeds h<sub>auto</sub>+h<sub>non</sub>=H in (7)\] **(10)**  LFP<sub>t</sub> = 1 / (1 + exp(−z<sub>t</sub>))  \[logistic\] **(11)**  z<sub>t</sub> = z<sub>baseline</sub> + β<sub>w</sub> · ln(w̄<sub>t</sub>/w̄<sub>0</sub>) − β<sub>u</sub> · (CD<sub>t</sub>/w̄<sub>0</sub>)  \[wages push LFP up, citizen dividends push down\] **(12)**  z<sub>baseline</sub> = ln(LFP<sub>target</sub> / (1 − LFP<sub>target</sub>))  \[pins LFP = LFP<sub>target</sub> at base-year wage with zero citizen dividends\] Cost Explorer **(13)**  MC<sub>i,t</sub> = MC<sub>i,0</sub> · Wright<sub>i,t</sub> · Jones<sub>i,t</sub>  \[marginal cost (MC) = base-year MC (user-specified) scaled by manufacturing learning (Wright) and design improvement (Jones)\] **(14)**  Wright<sub>i,t</sub> = (Q<sub>cum,t</sub> / Q<sub>cum,0</sub>)<sup>−b</sup>  \[manufacturing learning: unit cost falls by a fixed fraction (2<sup>−b</sup>−1) with each doubling of cumulative production. b is the learning-rate exponent: higher b → faster cost decline.\] **(15)**  Jones:  d(design rate)<sub>t</sub> = r<sub>base</sub> · (L<sub>design,t</sub>/L<sub>design,0</sub>)<sup>λ</sup> · D<sub>t</sub><sup>1−φ</sup>  \[design improvement: R&D labor L<sub>design</sub> generates new design ideas that reduce cost. r<sub>base</sub> = base-year improvement rate. λ \< 1 captures “stepping on toes” (duplicated effort among researchers → diminishing returns to more researchers). φ controls “ideas getting harder to find”: as the design stock D<sub>t</sub> grows, each new idea contributes proportionally less (φ \> 0 means harder over time, φ = 1 means constant).\] **(16)**  L<sub>design,t</sub> = L<sub>eff,t</sub> · frac<sub>R&D,t</sub>  \[R&D workforce = L<sub>eff</sub> × exogenous allocation %\] **(17)**  P<sub>i,t</sub> = MC<sub>i,t</sub> · μ<sub>manuf,t</sub> · μ<sub>design,t</sub>  \[price = cost × markups; manufacturing and design markups are user-specified trajectories\] **(18)**  Surplus<sub>i,t</sub> = (q<sub>i,t</sub> − P<sub>i,t</sub>) · Q<sub>i,t</sub>  \[buyer surplus = value − price\] Energy and Climate **(19)**  E<sub>t</sub> = E<sub>2025</sub> · (Y<sub>t</sub>/Y<sub>2025</sub>)<sup>ε</sup>  \[total primary energy: GDP-anchored with constant decoupling elasticity ε (default 0.4)\] **(20)**  E<sup>tech</sup><sub>j,t</sub> = S<sub>j,t</sub> · W<sup>avg</sup><sub>j,t</sub>  \[bottom-up tech energy: stock × vintage-averaged power per unit (j ∈ {AI compute, robots})\] **(21)**  E<sup>other</sup><sub>t</sub> = max(0, E<sub>t</sub> − E<sup>tech</sup><sub>AI,t</sub> − E<sup>tech</sup><sub>robot,t</sub>)  \[residual “Other” = total minus bottom-up AI and robot energy\] **(22)**  LCOE<sub>i,t</sub> = CapEx<sub>i,t</sub> · CRF<sub>i</sub> · 114.16 + OpCost<sub>i,t</sub> + ext<sub>i,t</sub>  \[levelized cost per generation source (i ∈ fossil/nuclear/hydro/solar/wind/other)\] **CES**(x, y; μ, σ) = \[μ<sup>1/σ</sup> x<sup>(σ−1)/σ</sup> + (1−μ)<sup>1/σ</sup> y<sup>(σ−1)/σ</sup>\]<sup>σ/(σ−1)</sup>.  σ=1: Cobb-Douglas.  σ\<1: complements.  σ\>1: substitutes.  
**CES<sub>task</sub>**(L<sub>auto</sub>, L<sub>non</sub>; f, σ) = \[f · L<sub>auto</sub><sup>(σ−1)/σ</sup> + (1−f) · L<sub>non</sub><sup>(σ−1)/σ</sup>\]<sup>σ/(σ−1)</sup>.  Same CES but weighted by task fraction f instead of share parameter μ.

References

- Bloom, N., Jones, C. I., Van Reenen, J., & Webb, M. (2020). Are Ideas Getting Harder to Find? *American Economic Review*, 110(4), 1104–1144.
- Halperin, B., Ho, H., Srinivasan, A., & Teo, M. (2024). The AGI Efficient Markets Hypothesis. Working paper.
- Jones, C. I. (1995). R&D-Based Models of Economic Growth. *Journal of Political Economy*, 103(4), 759–784.
- Sequeira, T. & Neves, P. (2020). Stepping on Toes in the Production of Knowledge. *Oxford Economic Papers*, 72(4), 1036–1061.
- Wright, T. P. (1936). Factors Affecting the Cost of Airplanes. *Journal of the Aeronautical Sciences*, 3(4), 122–128.

[Full Model Writeup](raw/writeup.pdf)
