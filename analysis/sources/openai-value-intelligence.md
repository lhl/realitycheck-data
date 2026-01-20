# Source Analysis: A business that scales with the value of intelligence

## Metadata
- **Source ID**: openai-value-intelligence
- **Author(s)**: OpenAI
- **Date**: Unknown (not captured in no-network environment)
- **Type**: ARTICLE
- **URL**: https://openai.com/index/a-business-that-scales-with-the-value-of-intelligence/
- **Reliability**: 0.55
- **Rigor Level**: [DRAFT]
- **Media Artifacts**: ? — not reviewed

> **Evidence Strength (E-level)**: E1=Strong empirical (replicated) | E2=Moderate empirical | E3=Strong theoretical (grounded) | E4=Weak theoretical (speculative) | E5=Opinion/forecast | E6=Unsupported assertion

## Stage 1: Descriptive Summary

### Core Thesis
The post’s framing (based on the title and the unit-economics question it prompts) appears to argue that an AI business can scale because the *value of intelligence* can rise faster than the marginal cost of producing “intelligence” (compute/energy), especially as hardware and inference efficiency improve.

**Limitation**: I could not retrieve/capture the full text in this environment (no external network). This analysis focuses on the concrete economic question raised: whether ~$1.20 revenue per kWh is plausibly compatible with break-even/profit for H100/H200-class inference.

### Key Claims
| # | Claim | Claim ID | Type | Domain | Evid | Conf | Verified? | Falsifiable By |
|---|-------|----------|------|--------|------|------|-----------|----------------|
| 1 | For H100/H200-class GPUs, accelerator capex amortization is commonly on the order of ~$1–$3 per kWh of IT energy under plausible price/utilization/depreciation assumptions, often exceeding the direct electricity cost | RESOURCE-2026-004 | [T] | RESOURCE | E3 | 0.70 | ✓ | Credible evidence that typical effective GPU cost-per-kWh is materially lower under real cloud purchasing/financing/utilization assumptions |
| 2 | If OpenAI’s effective revenue is ~**$1.20 per kWh** of IT energy used for inference, breakeven on H100/H200 hardware likely requires either unusually low GPU prices, very high utilization, long depreciation, or higher effective revenue per kWh than the estimate | TECH-2026-013 | [H] | TECH | E4 | 0.60 | ? | Updated revenue-per-kWh estimate substantially above $1.20, or observed (price, util, depreciation) combination yielding clear positive margins at ~$1.20/kWh |

### Argument Structure

```
Higher intelligence → higher willingness-to-pay
    ↓ while
Hardware + inference efficiency improve → lower marginal cost per “unit” of intelligence
    ↓ therefore
Unit economics can remain attractive (and scale with demand)
```

### Theoretical Lineage
- **Industrial organization / scale economics**: unit costs, utilization, capex amortization.
- **Compute-as-input political economy**: compute/energy as bottlenecks affecting margins and power.

### Scope & Limitations
- This analysis does **not** attempt to estimate OpenAI’s realized blended margins across all products; it targets *inference* unit economics on H100/H200-class accelerators.
- Key unknowns (not measurable here): actual GPU purchase/lease cost, depreciation policy, utilization (batching/latency constraints), PUE, and effective realized revenue per unit compute.

## Stage 2: Evaluation

### Internal Coherence
The “scales with value of intelligence” thesis is directionally coherent: if the product’s marginal value grows faster than marginal cost, scale economics improve. The crux is empirical: are costs dominated by electricity (cheap) or by scarce/expensive accelerators (often expensive), and can utilization stay high enough to amortize capex?

### Key Factual Claims Verified

> **Crux requirement**: verify ≥1 central claim. Here the crux is whether ~$1.20/kWh can cover H100/H200-style capex + power.

Assumptions for the back-of-envelope:
- **GPU power (IT)**: 0.7 kW (H100/H200-class TDP scale)
- **PUE**: 1.2
- **Electricity price**: $0.06/kWh (order-of-magnitude hyperscaler contract rate; varies widely)
- **Costs included**: GPU capex + electricity only (excludes staff, networking, facilities capex, financing, support hardware)

Break-even revenue per **IT kWh** (GPU capex + electricity):

| GPU price | Depreciation | Utilization | Break-even $/kWh (IT) |
|---:|---:|---:|---:|
| $20k | 3y | 70% | 1.63 |
| $20k | 3y | 90% | 1.28 |
| $30k | 3y | 70% | 2.40 |
| $30k | 3y | 90% | 1.88 |
| $40k | 3y | 70% | 3.18 |
| $40k | 3y | 90% | 2.49 |
| $20k | 5y | 70% | 1.00 |
| $20k | 5y | 90% | 0.80 |
| $30k | 5y | 70% | 1.47 |
| $30k | 5y | 90% | 1.16 |
| $40k | 5y | 70% | 1.94 |
| $40k | 5y | 90% | 1.52 |

Equivalent “per-GPU-hour” intuition (assuming 0.7kW IT power):
- ~$1.20 per IT kWh ⇒ **~$0.84 revenue per GPU-hour**
- A $30k GPU depreciated over 3y implies **~$1.14/GPU-hour** capex at 100% utilization (and ~$1.63/GPU-hour at 70% utilization), before electricity and other overheads
 - If ~$1.20 is actually per **facility** kWh (i.e., includes PUE in the denominator), then revenue per IT kWh would be ~$1.20×PUE (≈$1.44 at PUE 1.2)

Implication: if the effective revenue really is ~$1.20 per IT kWh, it is:
- compatible with **high utilization + long depreciation** (e.g., ~$30k GPU, 5y, 90% util → ~$1.16/kWh before other overheads)
- hard to reconcile with **3-year depreciation** unless effective GPU cost is closer to ~$15–$20k *and* utilization is very high

“What GPU price would make ~$1.20/kWh break even?” (same assumptions; excluding other overheads):
- 3y depreciation, 70% util: **~$14.5k** max GPU price
- 3y depreciation, 90% util: **~$18.7k**
- 5y depreciation, 70% util: **~$24.2k**
- 5y depreciation, 90% util: **~$31.1k**

### Disconfirming Evidence Search
No external web access in this environment; unable to verify the source’s publication date, the exact “$1.20/kWh” derivation, or current H100/H200 transfer prices/lease rates. This should be revisited with:
- documented H100/H200 OEM pricing or cloud internal transfer prices
- observed average utilization for latency-constrained interactive inference (likely <70% without heavy batching)
- PUE and electricity price ranges for the specific datacenters

### Evidence Assessment
- The arithmetic is straightforward (E3) but the result is **highly sensitive** to utilization, depreciation horizon, and the actual effective price paid for GPUs (purchase vs lease; volume discounts; financing).
- Even if electricity is cheap, **accelerator capex can dominate** inference COGS unless hardware is cheap or heavily utilized for long enough.

### Unstated Assumptions
| Assumption | Claim ID | Critical? | Problematic? |
|------------|----------|-----------|--------------|
| The “$1.20/kWh” estimate corresponds to **IT kWh** (not facility kWh) and reflects revenue tightly coupled to GPU runtime | supports TECH-2026-013 | High | Yes (measurement ambiguity) |
| Utilization can be kept high (batching, demand smoothing) in the relevant product mix | supports TECH-2026-013 | High | Yes (latency SLA and peak provisioning can lower effective utilization) |
| Depreciation can be long enough (≥5y) without performance obsolescence undermining competitiveness | supports TECH-2026-013 | Medium | Mixed |

### Weak Links
- The biggest weak link is the **measurement** of “revenue per kWh”: different denominators (IT vs facility kWh; GPU-only vs full stack; average vs peak) can move the estimate substantially.
- The second weak link is **utilization**: interactive products often require headroom, reducing average GPU occupancy.

### Confidence Assessment
- **Overall Confidence**: 0.60 on the qualitative conclusion (“$1.20/kWh is not obviously a sure-profit number once GPU capex is included”).
- **Reasoning**: the directionality is robust, but parameter uncertainty is large; accurate assessment needs real pricing + utilization data.

## Stage 3: Dialectical Analysis

### Steelmanned Argument
- Even if electricity is cheap, the true lever is that AI systems can deliver **high value per marginal compute**; therefore a business can price against customer value, not against energy cost.
- Over time, inference efficiency and hardware improve, pushing down COGS per unit output; if willingness-to-pay rises with capability, margins can expand.
- Scale + product mix (batch API, long-running enterprise workloads) can keep utilization high enough to amortize accelerators.

### Strongest Counterarguments
1. **Capex dominates**: for frontier inference, GPU acquisition and depreciation are the binding constraint; electricity is secondary, so “$ per kWh” revenue metrics may obscure that hardware costs can be >$1/kWh by themselves.
2. **Utilization ceiling**: latency-constrained interactive inference may structurally limit batching and therefore utilization; overprovisioning for peaks can make average economics worse.
3. **Competitive pressure**: even if value rises, competition can force prices toward cost; margins depend on defensibility (models, distribution, productization).

### Supporting Theories
- `DIST-2026-001`: compute + energy + chips as chokepoints for economic power (aligns with “capex dominates” framing).

### Contradicting Theories
- None directly; this analysis is mostly about parameterization of chokepoint claims rather than a different direction.

### Synthesis Notes
If the “$1.20/kWh” estimate is accurate and refers to IT kWh, it is *not* automatically “great margins”: on plausible H100/H200 assumptions, **GPU capex alone can be ~$1–$3/kWh** unless depreciation is long and utilization is high. The core empirical question is thus: what is OpenAI’s effective all-in accelerator cost (purchase/lease) and how high is realized utilization in their product mix?

### Claims to Cross-Reference
- GPU pricing and lease economics (H100/H200 street price vs hyperscaler transfer pricing).
- Inference utilization in practice for chat-style workloads (batching constraints).
- Facility-level energy costs and PUE ranges for AI datacenters.

---
**Analysis Date**: 2026-01-19
**Analyst**: gpt-5.2
**Confidence in Analysis**: 0.65
