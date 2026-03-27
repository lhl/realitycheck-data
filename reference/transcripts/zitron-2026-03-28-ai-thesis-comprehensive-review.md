# Ed Zitron's AI Thesis: A Comprehensive Review

## Who Is Ed Zitron?

Ed Zitron is a PR professional turned tech critic who runs the newsletter "[Where's Your Ed At](https://www.wheresyoured.at)" and hosts the "Better Offline" podcast. Since mid-2024, he has become one of the most prominent AI skeptics, producing detailed financial forensics of AI companies and arguing that the AI industry is heading for a "Subprime AI Crisis" — a structural economic collapse analogous to the 2008 housing crisis, where products are being sold at artificially low prices sustained by unsustainable debt and venture funding.

This document synthesizes his arguments, evaluates them against available evidence, and identifies where he is strongest, where he is weakest, and what he misses entirely.

## Sources Reviewed

**Zitron's work:**
- [YouTube: "Nobody Will Pay For Unsubsidised AI" — The Tech Report interview](https://www.youtube.com/watch?v=oAbpVCn-Ox0) (~March 2026) [[Podscan transcript](https://podscan.fm/podcasts/the-tech-report/episodes/ai-bubble-nobody-will-pay-for-unsubsidised-ai-ed-zitron)]
- [The Hater's Guide To The SaaSpocalypse](https://www.wheresyoured.at/hatersguide-saas/) (March 13, 2026)
- [Why Are We Still Doing This?](https://www.wheresyoured.at/why-are-we-still-doing-this/) (March 17, 2026)
- [The AI Industry Is Lying To You](https://www.wheresyoured.at/the-ai-industry-is-lying-to-you/) (March 24, 2026)
- [The Beginning of History](https://www.wheresyoured.at/the-beginning-of-history/) (March 10, 2026)
- [Subprime AI](https://www.wheresyoured.at/subprimeai/) (Sep 2024, originating thesis)
- Various earlier newsletter posts on Anthropic/OpenAI economics

**Counter-evidence and independent analysis:**
- [Frontier LLM Token Unit Economics](https://github.com/lhl/frontier-llm-token-unit-economics) — hardware-level inference cost modeling, token pricing analysis, and real-world usage data
- [AI Coding Measurement](https://github.com/lhl/ai-coding-measurement) — analysis of how AI-assisted coding is measured, its visibility in git metadata, and productivity evidence
- [JP-TL-Bench](https://github.com/shisa-ai/jp-tl-bench) — translation benchmark showing task-specific SLM competitiveness vs frontier models
- [Anthropic pricing documentation](https://www.anthropic.com/pricing)
- [Anthropic Series G announcement](https://www.anthropic.com/news/anthropic-raises-30-billion-series-g-funding-380-billion-post-money-valuation) (Feb 2026)
- [Anthropic research: Impact on Software Development](https://www.anthropic.com/research/impact-software-development)
- [Reuters Breakingviews: Anthropic Gives Lesson in AI Revenue Hallucination](https://www.reuters.com/commentary/breakingviews/anthropic-gives-lesson-ai-revenue-hallucination-2026-03-10/)
- [Reuters: Anthropic revenue targets](https://www.tradingview.com/news/reuters.com%2C2025%3Anewsml_L6N3VW07F%3A0-anthropic-aims-to-nearly-triple-annualized-revenue-in-2026-sources-say/) (enterprise share, customer count)
- [Reuters via Business Standard: Anthropic run rate](https://www.business-standard.com/companies/news/us-tech-startup-anthropic-unveils-cheaper-model-to-widen-ai-s-appeal-125101501588_1.html)
- [METR: Experienced OS Developers RCT](https://metr.org/Early_2025_AI_Experienced_OS_Devs_Study-paper.pdf) (2025)
- [METR: AI Task Time Horizons](https://metr.org/blog/2025-03-19-measuring-ai-ability-to-complete-long-tasks/)
- [METR: Algorithmic vs Holistic Evaluation](https://metr.org/blog/2025-08-12-research-update-towards-reconciling-slowdown-with-time-horizons/)
- [Microsoft Research: Copilot Productivity Study](https://www.microsoft.com/en-us/research/publication/the-impact-of-ai-on-developer-productivity-evidence-from-github-copilot/)
- [GitHub: Copilot Adoption Figures](https://github.blog/ai-and-ml/github-copilot/gartner-positions-github-as-a-leader-in-the-2025-magic-quadrant-for-ai-code-assistants-for-the-second-year-in-a-row/)
- [OpenRouter: State of AI 2025](https://openrouter.ai/state-of-ai/) (100T+ tokens served, agentic inference trends)
- [SWE-bench](https://arxiv.org/abs/2310.06770), [SWE-agent](https://arxiv.org/abs/2405.15793), [SWE-bench Verified](https://www.swebench.com/verified.html) — coding agent benchmarks

---

## His Core Argument

**"AI has no profit lever."** Unlike traditional SaaS companies that can grow fast, burn money, then turn profitable at scale, AI companies face a structural economic problem: inference costs are too high and wildly unpredictable per-user. The standard tech startup playbook doesn't apply.

His specific subscription-vs-API claim from the Tech Report interview:

> "If these services were actually worthwhile, they wouldn't have subscriptions. They would only charge for the API because it would be so valuable that you would have to pay them. And that's not the case right now."

This thesis has five pillars:

### 1. Every AI User Loses Money

A $20/month Claude subscriber can burn up to $163 in compute. Even $200/month Claude Max subscribers can cost Anthropic thousands — Zitron documented users on the "viberank" leaderboard burning $51,291 of compute in a single month. Coding use cases are the worst for margins because code generation is token-heavy and mistakes guarantee further token burn. [[Why Are We Still Doing This?](https://www.wheresyoured.at/why-are-we-still-doing-this/)]

### 2. The Subscription Model Is Structurally Broken

Users have been conditioned to all-you-can-eat pricing. They've never built the mental model of what individual tasks cost. His Uber analogy: if you'd always paid a flat monthly rate for unlimited rides, switching to per-ride pricing would be a massive shock even if the service is identical. He argues there's no clean migration path from subscriptions to usage-based pricing. [[Why Are We Still Doing This?](https://www.wheresyoured.at/why-are-we-still-doing-this/)]

His math for an engineering team:
- 100 engineers x $200/month Claude Max = $240,000/year
- Same engineers on API at $10/day = $365,000/year
- At $25/day = $912,500/year
- At $40/day = over 10% of salary costs

### 3. Annualized Revenue Figures Are Misleading

He did forensic analysis of Anthropic's leaked ARR numbers vs. the $5B lifetime revenue figure from CFO Krishna Rao's March 2026 legal affidavit. Adding up all publicly reported annualized revenue milestones gives ~$6.66B — exceeding the stated lifetime figure. His conclusion: Anthropic is measuring "annualized revenue" in a non-standard way that makes numbers look bigger. He similarly argues OpenAI made roughly $3.6B in actual 2024 revenue, not what the ARR leaks implied. [[The Beginning of History](https://www.wheresyoured.at/the-beginning-of-history/)]

He also showed Anthropic spent $2.66B on AWS through September 2025 against ~$2.55B in revenue — 104% of revenue on just one cloud provider. [[The AI Industry Is Lying To You](https://www.wheresyoured.at/the-ai-industry-is-lying-to-you/)]

### 4. Enterprise AI Revenue Is Negligible

His enterprise revenue roundup across major software companies [[Hater's Guide to the SaaSpocalypse](https://www.wheresyoured.at/hatersguide-saas/)]:

| Company | AI Revenue Claim | Zitron's Interpretation |
|---|---|---|
| IBM | $12.5B "generative AI book of business" | 80% is consultancy reselling others' models |
| Adobe | ~$375M ARR "AI-first" | ~1.5% of quarterly revenue |
| Salesforce | $2.9B Agentforce headline | $800M actual ARR; headline included $1.1B non-AI acquisition |
| ServiceNow | $600M ACV from AI | Net income flat since 2023 |
| Workday | $400M ARR from AI | $33M/month on $2.5B quarterly revenue |
| Intuit | $90M in "AI efficiencies" | Paid $100M+ for ChatGPT access |
| Microsoft | $13B run rate (Jan 2025) | Never reported this metric again |
| Google, Amazon | N/A | Don't break out AI revenue at all |

### 5. The Infrastructure Is Built on Debt and Fiction

- Only ~3GW of data center capacity came online in the US in 2025, vs. 241GW "planned"
- NVIDIA sells GPUs 2-4 years ahead of installation capacity
- $178.5B in US data center debt deals in 2025, much of it junk-rated
- CoreWeave rated B+ (junk), 77% of revenue from Microsoft and NVIDIA, lost $1.2B
- Data center debt funded by pension funds and insurance companies
- SoftBank trying to raise $40B loan while carrying $41.5B in debt maturing within 9 months
- $948B in total US data center capex, but growth decelerated for first time since 2023

[[The AI Industry Is Lying To You](https://www.wheresyoured.at/the-ai-industry-is-lying-to-you/), [The Beginning of History](https://www.wheresyoured.at/the-beginning-of-history/)]

---

## His Take on Developer Tools

Zitron doesn't deny that developer tools exist or that people use them. He addresses them directly:

**Claude Code:** Acknowledges it became "the most-popular coding environment in the world" but argues it only generates $33M/month (as of July 2025), "all of it unprofitable." His framing: "is that it? Is that all that's happening here?" [[Why Are We Still Doing This?](https://www.wheresyoured.at/why-are-we-still-doing-this/)]

**Cursor:** $2B annualized revenue but raised $3B in 2025 alone. AWS bills doubled after Anthropic raised enterprise API prices. [[Hater's Guide](https://www.wheresyoured.at/hatersguide-saas/)]

**GitHub Copilot:** 1.8M subscribers but Microsoft loses >$20/month per user, some costing $80/month. [[Why Are We Still Doing This?](https://www.wheresyoured.at/why-are-we-still-doing-this/)]

**Replit:** Agent 3 launch was a disaster — costs spiraled from $100-250/month to $1,000/week per user.

**Vibe Coding:** Dismissed entirely: "Show me a vibe coded company... You won't be able to find this as it isn't possible. Vibe Coding is a marketing term based on lies."

**AI-caused incidents:** Cites Amazon outages caused by AI coding tools (120K lost orders and 6.3M lost orders in separate incidents) and Meta's security breach from an internal AI agent. [[The AI Industry Is Lying To You](https://www.wheresyoured.at/the-ai-industry-is-lying-to-you/)]

**His software engineer sources:** Interviews three known AI skeptics — Carl Brown ("The Internet of Bugs"), Nik Suresh ("I Will Fucking Piledrive You If You Mention AI Again"), and Colt Voege ("No, AI is not Making Engineers 10x As Productive"). All describe AI coding tools as marginally useful at best. He explicitly identifies Simon Willison and Max Woolf as credible people who "actually work with LLMs on a daily basis" — but doesn't interview them.

---

## Assessment: Where He's Right

### Financial forensics are genuinely good

His Anthropic revenue analysis — cross-referencing leaked ARR numbers against the CFO affidavit, AWS billing data, and actual revenue figures — is more rigorous than what most financial journalists have done. The discrepancies he found between reported ARR milestones and lifetime revenue are real and deserve explanation. Reuters Breakingviews independently noted that 80% of Anthropic's revenue comes from consumption-based enterprise billing, making run-rate numbers "sensitive to temporary usage spikes, credits, pricing changes, and customer optimization." [[Reuters Breakingviews](https://www.reuters.com/commentary/breakingviews/anthropic-gives-lesson-ai-revenue-hallucination-2026-03-10/)]

### Enterprise AI revenue claims are mostly smoke

His company-by-company breakdown showing that virtually no major software company can point to material, clearly-defined AI revenue is compelling and under-reported. When IBM's $12.5B "AI book of business" is 80% consultancy, when Salesforce bundles a $1.1B acquisition into its "AI revenue" headline, and when Microsoft stops reporting its AI run rate after one disclosure — the aggregate picture supports deep skepticism about enterprise AI monetization outside of the foundation model providers themselves.

### Subscription economics are unsustainable as-is

The math on Claude Max subscribers burning orders of magnitude more than their subscription fee is real. Anthropic and OpenAI are subsidizing heavy usage. Anthropic's own docs confirm average Claude Code cost is ~$6/developer/day with 90% of users below $12/day, but power users vastly exceed this. [[Anthropic pricing](https://www.anthropic.com/pricing)]

### The data center buildout is behind schedule

The gap between "announced" and "under construction" and "actually operational" is enormous — 241GW planned vs. ~3GW delivered in 2025. NVIDIA is selling GPUs years ahead of the infrastructure to house them.

### The debt exposure is real and concerning

The amount of junk-rated debt going into AI infrastructure, funded by pension and insurance money, is a genuine systemic risk. CoreWeave lost $1.2B on $5.13B in revenue. Neocloud financials across the board show large losses. The geopolitical risk argument — that interest rate spikes from events like the Strait of Hormuz closure would devastate debt-funded AI buildout — is directionally sound. [[The Beginning of History](https://www.wheresyoured.at/the-beginning-of-history/)]

---

## Assessment: Where He's Wrong

### 1. The subscription/API argument is backwards

His central claim — "if AI were valuable, they'd only charge API, not subscriptions" — is incoherent. The existence of subsidized subscriptions doesn't prove the product lacks value; it proves companies are competing for market share, which is standard tech strategy. The fact that users are burning $5,000-$12,000/month of compute on $200 subscriptions is actually evidence the product is *extremely* valuable to those users — they're getting massive consumer surplus.

Anthropic already sells API access and enterprises already pay for it. The pricing stack is hybrid: Team is seat-based, Enterprise is seat + usage at API rates, and raw API is pure consumption. Enterprise buyers want predictable budgets, central billing, admin controls, and SSO — that's why seat-based pricing exists, not because the product is worthless. [[Anthropic pricing](https://www.anthropic.com/pricing)]

### 2. He conflates profitability with utility

This is his deepest analytical error. "Claude Code only makes $33M/month, all unprofitable" is an argument about Anthropic's business model. It says nothing about whether the tool is transforming how software gets built.

Amazon Web Services lost money for years. Google Search was free. Netflix burned cash for a decade. The question is whether the value being created will eventually be captured through sustainable pricing — not whether the current pricing is sustainable.

### 3. Enterprise API economics contradict his thesis

His "no profit lever" argument applies primarily to consumer all-you-can-eat subscriptions. Enterprise API customers paying per-token have a completely different cost structure.

Reuters reports Anthropic's annualized revenue run rate approaching $7B (Oct 2025), with enterprise customers accounting for about 80% of revenue and more than 300,000 business/enterprise customers. Internal targets were ~$9B by end-2025 and $20-26B for 2026. [[Reuters](https://www.tradingview.com/news/reuters.com%2C2025%3Anewsml_L6N3VW07F%3A0-anthropic-aims-to-nearly-triple-annualized-revenue-in-2026-sources-say/)] By February 2026, Anthropic reported Claude Code's run-rate revenue over $2.5B with business subscriptions quadrupled since January 1. [[Anthropic](https://www.anthropic.com/news/anthropic-raises-30-billion-series-g-funding-380-billion-post-money-valuation)]

This does not prove margins are healthy, but it directly conflicts with the claim that enterprise AI revenue is "tiny" or that there is "no profit lever" beyond unsustainable subscriptions.

### 4. He has no apparent firsthand experience with agentic coding

His framing is consistently "AI coding tools generate verbose code that doesn't follow conventions" — which described Copilot autocomplete circa 2023. It doesn't describe what Claude Code with Opus, or Cursor in agent mode, actually does in March 2026.

The jump from "autocomplete that suggests the next line" to "agent that reads your entire codebase, plans multi-file changes, runs tests, and iterates until they pass" happened over roughly the last 6-9 months. His software engineer sources are all known skeptics, and he explicitly identifies credible daily LLM users (Willison, Woolf) but doesn't interview them.

### 5. He ignores cost deflation trajectories

He argues that while per-token costs have dropped, models now burn more tokens per useful output (reasoning, chain-of-thought), so total cost per task has gone up. This is partially true for frontier reasoning models but misses the bigger picture:

- GPT-4 output: $60/MTok (2023) -> GPT-4o-mini: $0.60/MTok (2024) = **99% cheaper**
- Training cost: GPT-4 ~$100M -> DeepSeek V3 ~$5.6M (**20x cheaper**)
- Hardware: A100 -> H200 = 2.4x memory bandwidth improvement
- Software: FlashAttention 1->3 = 4-18x speedup; PagedAttention/vLLM = 2-4x throughput
- Architecture: Dense models -> MoE (e.g., Kimi K2: 1T params, 32B active = ~3% activation)
- Combined realistic efficiency gain since 2022: **100-500x**

He doesn't address smaller/cheaper models (Haiku, GPT-4o-mini), open-source models, or local inference as cost escape valves. Chinese providers are publishing list prices dramatically below Western frontier models. [[DeepSeek pricing](https://api-docs.deepseek.com/quick_start/pricing/), [OpenRouter](https://openrouter.ai/pricing)]

More importantly, task-specific routing to smaller models is already viable. For example, on English-Japanese translation benchmarks, a 14B parameter model scores within 3-6% of Gemini 2.5 Pro (EN->JA: 9.63 vs 9.97; JA->EN: 9.36 vs 9.94), and automated quality metrics like COMET saturate at the top — meaning the gap between a $0.07/MTok model and a $10/MTok model is negligible for that task. [[JP-TL-Bench](https://github.com/shisa-ai/jp-tl-bench)] Zitron's implicit assumption that only frontier-scale models matter ignores that intelligent routing to cheaper models can handle a large share of real workloads.

### 6. Selection bias in sourcing

His engineer sources are people literally named "The Internet of Bugs," "I Will Fucking Piledrive You If You Mention AI Again," and "No, AI is not Making Engineers 10x As Productive." This is like interviewing three people named "Cars Are Bad" and concluding nobody drives. He acknowledges but doesn't engage with the large population of developers who use these tools daily and report substantial productivity gains.

---

## The Tokenomics Gap: What He Doesn't Model

Zitron's economic analysis operates at a **financial journalist** level — revenue figures, AWS bills, subscription math — but never descends into the actual mechanics of inference economics. This matters because the token-level economics are where his thesis most clearly breaks down.

### What he does

His cost analysis is essentially:
- Anthropic lifetime revenue: $5B (from CFO affidavit)
- Anthropic lifetime compute costs: >$10B (from same affidavit)
- Therefore: unprofitable, QED

He also does useful work cross-referencing leaked ARR figures against the affidavit to show inconsistencies, and obtained AWS billing data showing Anthropic spent $2.66B on AWS through September 2025. This is real investigative journalism and it's valuable.

### What he treats as a black box

When it comes to **how inference actually works and what it costs**, his model is: "tokens go in, money comes out, the money is less than the cost." He never engages with:

- The difference between prefill (input, parallelizable, compute-bound) and decode (output, sequential, memory-bandwidth-bound)
- Why output tokens cost 3-5x more than input tokens (memory bandwidth bottleneck)
- How prompt caching fundamentally changes the cost structure
- MoE architectures and activation sparsity (modern models activate 3-10% of parameters)
- The 100-500x efficiency gains from hardware + software improvements since 2022
- Model routing (using cheaper models for easier tasks)

### The cache revolution he ignores

For agentic coding workloads (like Claude Code), the majority of tokens are cache reads. Real-world usage data from production coding workflows [[frontier-llm-token-unit-economics](https://github.com/lhl/frontier-llm-token-unit-economics)]:

| Metric | Claude | OpenAI |
|---|---|---|
| Cache hit rate | ~91% | ~96% |
| Cache reuse factor | ~10.6x | ~23.3x |
| Cost with caching vs without | ~80% savings | Similar magnitude |

This is the single biggest factor in inference economics for coding use cases, and Zitron never mentions it. His "$25,000 of compute on a $200 subscription" figures are calculated at retail API output token rates, dramatically overstating actual provider cost-to-serve.

### Actual cost-to-serve ranges (estimated)

A proper analysis of frontier LLM token unit economics models [[frontier-llm-token-unit-economics](https://github.com/lhl/frontier-llm-token-unit-economics)]:

**Hardware-level cost:**
```
$/MTok ~ (cluster $/hr) / (effective tok/s x 3600) x 1,000,000
```

With variables including GPU cost/hour, memory bandwidth as the binding constraint, KV cache footprint, utilization rates, and batch efficiency.

**Estimated ranges:**
- Claude Opus output: $1-12/MTok cost vs $75/MTok retail pricing
- Cache reads: $0.02-0.20/MTok cost vs $0.30-0.75/MTok retail pricing
- GPT-class output: $0.5-6/MTok cost vs $14/MTok pricing

These are wide ranges (true internal COGS are proprietary), but even the high end shows substantial margins on API pricing. The margins on cached input — which dominates agentic coding workloads — are enormous.

### His "costs are going up" claim

Zitron's response to "costs are coming down" is that reasoning models burn more tokens, so total cost per task has gone up. This is partially true for frontier reasoning but it is false for the models and use cases that dominate actual coding workloads (Sonnet-class, heavily cached, non-reasoning).

### What his analysis lacks structurally

Without throughput, utilization, cache mechanics, and workload mix modeling, his economic claims are not falsifiable. He jumps between variable COGS (per-token cost) and macro capex (training, infrastructure) in ways that lead to overconfident conclusions. A real economic analysis of AI inference would need to model GPU cluster costs, memory bandwidth constraints, cache hit rates, MoE activation ratios, utilization, batch efficiency, and the hardware/software improvement trajectory. [[frontier-llm-token-unit-economics](https://github.com/lhl/frontier-llm-token-unit-economics)]

---

## The Coding Productivity Evidence: Mixed, Not Binary

Zitron presents AI coding as a binary: either it works or it doesn't. The evidence is more nuanced than either boosters or skeptics acknowledge.

### Benchmarks show rapid capability gains

- SWE-bench: Claude 2 solved 1.96% of real GitHub issues -> SWE-agent improved to 12.5% -> SWE-bench Verified reports 65% for recent agents on curated tasks [[SWE-bench](https://arxiv.org/abs/2310.06770), [SWE-agent](https://arxiv.org/abs/2405.15793), [SWE-bench Verified](https://www.swebench.com/verified.html)]
- METR's time-horizon analysis: the length of tasks models can complete with 50% reliability has been doubling roughly every 7 months [[METR](https://metr.org/blog/2025-03-19-measuring-ai-ability-to-complete-long-tasks/)]

### Real-world productivity studies are more cautious

- **Microsoft Research/Copilot study:** 55.8% faster completion on a controlled task (implementing an HTTP server) [[Microsoft Research](https://www.microsoft.com/en-us/research/publication/the-impact-of-ai-on-developer-productivity-evidence-from-github-copilot/)]
- **METR RCT (early 2025):** Experienced open-source developers were **19% slower** with AI tools on real tasks, despite expecting speedups [[METR](https://metr.org/Early_2025_AI_Experienced_OS_Devs_Study-paper.pdf)]
- **METR follow-on:** Agent-written PRs that passed tests were still not mergeable without additional human work — benchmark passing overestimates real-world mergeability [[METR](https://metr.org/blog/2025-08-12-research-update-towards-reconciling-slowdown-with-time-horizons/)]
- **Google:** Reported 25-30% of new code is AI-generated but only ~10% engineering velocity gain

### The measurement problem nobody discusses

Most AI-assisted coding is invisible in git metadata [[ai-coding-measurement](https://github.com/lhl/ai-coding-measurement)]:

- Copilot has 20M+ users and generates ~46% of code in enabled files but leaves zero git traces
- The visible ~5% (attributed agent commits) underestimates actual AI assistance by roughly 8x
- Revenue measures willingness-to-pay, not code output; developer surveys measure perceived productivity, not actual throughput
- Agent code shows higher churn (7.33% vs 4.10%) and shorter symbol survival (3 days vs 34 days), but this may reflect iterative development patterns rather than quality problems
- DORA 2024 found AI adoption accompanied slight throughput decrease and stability reduction, but teams with good architecture benefited while poorly-structured teams didn't — "AI doesn't fix a team; it amplifies what's already there"

### What Zitron gets right about coding

His skepticism about immediate, universal productivity gains is supported by the METR RCT and the Google data. The honest answer is that measured effects are smaller and more uneven than the hype suggests. Benchmarks improve faster than real-world outcomes.

### What Zitron gets wrong about coding

His broader dismissal of agentic coding capability ignores clear benchmark improvements, massive adoption (20M+ Copilot users, 77,000 enterprises), and the evidence that scaffolding and workflow integration materially improve real-task performance. He relies on anecdotal incidents (Amazon outages, Meta breach) and interviews with known skeptics, without a balanced technical evidence base. He does not engage with capability benchmarks (SWE-bench, SWE-agent), agent scaffolding research, or the test/mergeability gap literature.

---

## A Concrete Counterpoint: What Agentic Coding Actually Looks Like

Zitron's analysis is entirely financial — he never talks to (or apparently talks with) anyone who is actually wielding these tools at scale in production. Here's what the reality looks like from an experienced practitioner — someone with 25+ years of professional software development who calls this the biggest change since the late '80s/'90s:

**The numbers:**
- Hundreds of thousands of SLoC of production software generated since late 2025, with barely a line written by hand
- Billions of cached tokens/month in usage
- At retail API token pricing, this costs roughly $4-5K/month
- The agentic coding agents (manually orchestrated) do the work of at least 4-5 FTEs
- At US market rates, that's potentially $1-2M+ of developer value per year

**Why this breaks Zitron's thesis:**

1. **This is API pricing, not subsidized subscriptions.** The ~$4-5K/month figure is based on retail token rates. Nobody is losing money on this transaction. Zitron's entire argument is built around the premise that subsidized $200/month subscriptions can't survive repricing — but API customers are *already* paying real rates and finding it absurdly cheap relative to the value produced.

2. **The value multiplier is enormous.** $4-5K/month for 4-5 FTEs of output is a 10-40x return depending on labor market. Even if token costs doubled or tripled, the ROI would still be overwhelming. Zitron's scenario where enterprises balk at API pricing assumes they're getting marginal value from AI.

3. **This isn't vibe coding.** Zitron dismisses AI coding by conflating it with "vibe coding" — non-developers prompting chatbots to spit out apps. What's actually happening for power users is experienced engineers using agentic tools as force multipliers. The decades of architectural knowledge, system design intuition, and debugging skill don't go away — they get amplified. The AI handles the mechanical code generation; the human handles judgment, direction, and quality control.

4. **The cost curve is going the right direction.** Cached token pricing dominates agentic coding workloads (since agents repeatedly re-read the same codebase context), and caching costs are already dramatically cheaper than base rates. The economics that are already favorable will only improve.

5. **He compares to zero, not to the alternative.** Zitron never makes the comparison that matters: AI costs vs. human developer costs. At $4-5K/month, agentic coding is cheaper than a single junior developer *anywhere in the world* while producing more output than most junior developers would.

This isn't an anomaly — it's the experience of a growing population of senior developers who have integrated agentic coding into their workflows.

---

## The Deeper Issue: Two Arguments Wearing the Same Clothes

Zitron runs two arguments simultaneously:

**Argument A (Strong):** The AI industry's financial structure is unsustainable. Companies are losing money on every subscription user, revenue figures are inflated by misleading ARR reporting, the infrastructure buildout is funded by junk debt, and there is no clear path from current subscription pricing to profitability. This is a serious, well-documented argument backed by real financial forensics.

**Argument B (Weak):** AI products, including coding tools, don't actually work or provide meaningful value. Vibe coding is fake, AI makes engineers slower, the whole thing is a mirage. This is asserted more than proven, relies on cherry-picked sources, and conflicts with the lived experience of a large and growing developer population.

He constantly conflates these two arguments. When challenged on Argument B (people clearly find Claude Code valuable), he retreats to Argument A (but the economics don't work). When Argument A is challenged (Anthropic's enterprise revenue is growing fast), he pivots to Argument B (but the product doesn't really work).

**The strong version of his thesis** — that current subscription pricing is unsustainable and a repricing event will be painful — can be true simultaneously with AI coding tools being genuinely transformative. These are not contradictory claims. Early AWS was also unprofitable. The question is whether the value creation is real enough to support sustainable pricing, and on that question, the enterprise API customer base suggests yes.

---

## Has He Updated His Priors?

**No.** His March 2026 articles are more of the same thesis with better data. He's gotten *more* committed to the position, not less. He has updated his *evidence* (incorporating the $5B lifetime revenue affidavit, Amazon outage incidents, geopolitical risk factors) but not his *conclusions*. The "Subprime AI Crisis" frame from September 2024 is unchanged. [[Subprime AI](https://www.wheresyoured.at/subprimeai/)]

This is notable because the period from mid-2025 to March 2026 saw:
- Claude Code going from niche to mainstream developer tool (>$2.5B run rate by Feb 2026)
- Anthropic's revenue growing from ~$600M/year to multi-billion pace
- Enterprise API adoption accelerating (300,000+ business customers, 80% of revenue)
- Cursor hitting $2B ARR
- Multiple companies building businesses on AI APIs
- GitHub Copilot reaching 20M+ users across 77,000 enterprises

None of this has dented his thesis because he interprets all of it through the same lens: revenue growth on unprofitable pricing proves his point rather than challenging it.

That said, he is not failing to engage — he has explicitly acknowledged Claude Code's popularity, Cursor's revenue, and enterprise adoption. He just interprets it all negatively. As the ChatGPT Pro research noted: "not clueless, not unaware, not failing to update. He has updated — and still thinks Claude Code popularity is being misread."

---

## Claim-by-Claim Summary Table

| Claim | Assessment | What Holds | What Breaks |
|---|---|---|---|
| Subscription economics are structurally broken | **Partially true, overstated** | Worst-case workloads are genuinely loss-making; power users vastly exceed subscription revenue | Ignores cache mix (91%+ hit rates make most usage cheap); treats worst-case as universal |
| Inference costs are too high and won't fall | **Incomplete** | Frontier reasoning models remain expensive | Ignores serving optimizations, prompt caching, model routing, and 100-500x efficiency gains since 2022 |
| Enterprise AI revenue is tiny | **Conflicts with best data** | Individual enterprise software companies show modest AI revenue | Anthropic enterprise revenue is ~80% of a multi-billion run rate; 300K+ business customers |
| AI coding tools don't improve productivity | **Mixed; dismissal too strong** | METR RCT shows slowdowns; mergeability gaps are real | Benchmarks show rapid progress; 20M+ Copilot users; broad enterprise adoption |
| ARR figures are misleading | **Largely correct** | Cross-referencing leaked milestones vs. affidavit shows inconsistencies | Reuters Breakingviews independently confirmed consumption-based billing makes run rates unreliable |
| Infrastructure buildout is fragile | **Largely correct** | 3GW delivered vs 241GW planned; junk-rated debt; pension fund exposure | Long-term demand trajectory is uncertain in both directions |
| Token pricing has no sustainable floor | **Too strong** | Some providers may subsidize; pricing pressure is real | Chinese providers publish very low list prices; task-specific SLMs match frontier quality at 100x lower cost; API margins at retail are substantial |
| "No profit lever" exists | **Too strong as stated** | Consumer subscriptions have no clean profit path | Enterprise API is usage-based, can be margin-positive; cache reuse and model routing create viable economics |
| Vibe coding is fake | **Straw man** | Non-developer "vibe coding" has obvious limits | Conflates vibe coding with agentic coding by experienced developers, which is a different thing entirely |

---

## Bottom Line

**Ed Zitron is a better financial analyst than AI product evaluator.** His forensic work on revenue discrepancies, AWS costs, enterprise AI revenue claims, and data center infrastructure debt is genuinely valuable and under-replicated by mainstream financial journalism. When he sticks to following the money, he produces work that deserves serious engagement.

But his product analysis is shallow, his sourcing on utility is one-sided, and his central rhetorical move — treating unprofitability as proof of uselessness — doesn't hold up. He operates without any model of how inference actually works, what it costs at the hardware level, how caching changes the equation, or how rapidly the cost curve is moving. His subscription loss calculations use retail output token pricing applied to total consumption, which dramatically overstates provider losses.

**The strongest counterargument to his thesis** isn't "Anthropic's revenue is growing" (he has a response to that). It's that **enterprises and power users are already on API pricing, they know exactly what it costs, they find it extraordinarily cheap relative to the value, and they keep buying more**. That's the thing he doesn't address.

His thesis would be much stronger if he separated the financial sustainability argument (strong) from the utility argument (weak) and acknowledged that both can be independently true or false. The AI industry can be built on unsustainable financial structures *and* the products can be genuinely transformative. History is full of real technologies funded by bubbles — railroads, fiber optics, the early internet. The question isn't whether AI works. It's whether the current financial structure survives long enough for the economics to mature. On that narrower question, Zitron's concerns deserve serious attention.
