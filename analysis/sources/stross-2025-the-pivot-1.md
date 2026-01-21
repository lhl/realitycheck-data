# Analysis: "The pivot" (Part 1) — Charlie Stross (2025-10-17)

**Source ID**: stross-2025-the-pivot-1  
**URL**: https://www.antipope.org/charlie/blog-static/2025/10/the-pivot-1.html  
**Author**: Charlie Stross  
**Published**: 2025-10-17  
**Analyzed**: 2026-01-21  
**Status**: analyzed

---

## Summary

Stross argues that 2025 is a historical inflection point (“the pivot”) driven primarily by a rapid, hard-to-reverse transition away from fossil fuels, compounded by climate-driven agricultural stress, institutional brittleness from decades of neoliberal governance, and the end of easy gains from Moore’s Law.

The post is structured as a wide-angle historical narrative: energy transitions reshape geopolitics and domestic politics; climate constraints raise the stakes for agricultural resilience; and the tech/finance status quo is portrayed as running out of growth engines (with AI data centers framed as a bubble rather than a durable new substrate).

The core “this can’t go on, so it will stop” thesis is offered as a synthesis: fossil-fuel rents, platform rent extraction, and bubble-driven capital allocation are presented as mutually reinforcing—and mutually destabilizing—features of the current era.

---

## Stage 1: Descriptive Analysis

### What the post argues (high-level)

- **Energy transition as the driver**: An “unprecedented civilizational energy transition” is presented as a primary cause of instability, radicalization, and conflict, and as effectively irreversible.
- **Solar + storage as the new baseline**: Solar PV is framed as the central technology pushing the transition via extreme cost decline and mass deployment (especially in China and the EU).
- **Fossil political economy in retreat**: Fossil fuel incumbents are portrayed as facing imminent asset stranding, with spillovers into corruption, propaganda, and resource conflict.
- **Climate and food-system fragility**: Climate volatility and heat stress are presented as major threats to agriculture; just-in-time supply chains reduce resilience.
- **Tech growth regime weakening**: The end of Moore’s Law is cited as a structural headwind; AI data centers are framed as a bubble; SMRs and quantum computing are dismissed as unlikely saviors.

### Key factual/proxy claims used in the narrative (unverified in this pass)

- Solar PV module cost declines (mid-1970s vs 2012) and continued downward trajectory.
- China’s 2025 PV deployment pace (Jan–May totals; May alone).
- EU crossing 50% renewables share for electricity in 2025.
- “Passed +1.5°C” threshold framing and implications for photosynthesis/harvest stability.

### Predictions (as stated)

- Fossil extraction rights become stranded assets by 2040.
- The hyperscale AI data center boom resembles a bubble; useful LLM deployment shifts toward local inference.
- The SMR “boom” fizzles versus cheap PV + batteries.

### Terms / references

- **Enshittification** (Doctorow): platform rent extraction after user lock-in.
- **Abilene paradox**: groups converge on outcomes nobody wants due to miscoordination.
- **Herbert Stein’s law**: “If something cannot go on forever, it will stop.”

---

## Stage 2: Evaluative Analysis

### Evidence quality (as presented)

- The post mixes **(a)** broadly accepted historical/technical background, **(b)** quantitative claims linked to external articles, and **(c)** strong causal claims (energy transition → radicalization/war; Moore’s Law end → VC/PE decay) that are asserted rather than demonstrated.
- Several key quantitative statements are **checkable** (PV costs, EU renewables share, China 2025 PV additions), but are not substantiated in the post itself beyond links and rhetorical confidence.

### Potential ambiguity / likely error sources

- The statement “net-zero … by 2030” for China appears inconsistent with widely cited public targets (China’s carbon neutrality target is commonly given as 2060); treat this as a **high-risk claim** needing direct verification.
- “Passed +1.5°C” is ambiguous: it could mean a **single-year exceedance** or the **long-term (multi-decade) threshold** used in climate governance.

### Disconfirmation / cruxes

- If PV/battery costs stall (or grid integration constraints dominate), the “distributed abundance” trajectory weakens.
- If fossil demand remains structurally high (e.g., aviation/shipping/industry), the “rapid stranding” prediction weakens.
- If AI yields durable, broad productivity gains (beyond capex burn), the “bubble” framing weakens.

---

## Stage 3: Dialectical Analysis

### Steelman

Energy systems are foundational: when the cost and logistics of energy shift, geopolitics, industrial organization, and domestic distributional conflict shift with them. A rapid transition away from fossil rents plausibly destabilizes incumbent coalitions, while climate volatility makes food security and resilience increasingly central. If compute progress slows and finance continues to chase bubbles, governance capacity may lag reality, increasing crisis frequency.

### Counterarguments

- **Substitution constraints**: Hard-to-electrify sectors (aviation, high-heat industrial processes) may keep fossil demand significant longer than implied.
- **Mineral geopolitics**: “Post-oil geopolitics” may still be resource geopolitics (lithium, nickel, copper, rare earths), just with different chokepoints.
- **Institutional adaptation**: States can adapt under pressure; “current rulers don’t remember” may be rhetorically satisfying but too coarse.
- **AI as general-purpose tech**: The bubble framing may be directionally right on hype, but still wrong on eventual economic importance. For example, controlled trial evidence suggests large near-term productivity gains from AI coding assistants (`LABOR-2023-001`), and organizational A/B studies report similarly large speedups in real engineering environments (`LABOR-2024-001`). This weakens a “no new growth engines” posture even if capex overshoots and some investment is later written down.

### Synthesis / working update

Treat the post as a **coherent hypothesis bundle** linking energy transition, climate/food resilience, and tech/finance regime changes. The strongest near-term upgrades would come from verifying the quantitative anchors (PV costs, EU/China deployment) and tightening operational definitions (what “passed 1.5°C” means; what “stranded” means).

---

## Extracted Claims

- Import file: `analysis/sources/stross-2025-the-pivot-1.yaml`

### Claim Summary

| ID | Type | Domain | Evidence | Credence | Claim |
|---|---|---|---|---:|---|
| ECON-2025-001 | [T] | ECON | E5 | 0.30 | Neoliberalism evolved into a model of state hollowing and asset-stripping via outsourcing to private-sector entities... |
| ECON-2025-002 | [T] | ECON | E4 | 0.40 | Platform capitalism increasingly sells subscription services rather than owned goods, enabling rent extraction by deg... |
| GEO-2025-001 | [T] | GEO | E5 | 0.35 | The energy transition is producing major political consequences—from bribery and corruption up to open warfare—and po... |
| RESOURCE-2025-001 | [P] | RESOURCE | E5 | 0.35 | By 2040 at the latest, coal, gas, and oil land rights will be stranded assets that cannot be monetized. |
| RISK-2025-001 | [T] | RISK | E4 | 0.35 | Humanity has passed the +1.5°C warming threshold, increasing the number of days per year when temperatures are too ho... |
| RISK-2025-002 | [T] | RISK | E4 | 0.40 | Just-in-time supply chains increased economic efficiency at the expense of resilience, leaving societies without rese... |
| SOC-2025-001 | [T] | SOC | E5 | 0.35 | A significant share of current social unrest and insecurity-driven radicalization is being caused by the ongoing civi... |
| TECH-2025-001 | [T] | TECH | E4 | 0.45 | Moore’s Law is effectively ending: compute and storage improvements have been limited for over a decade and now rely... |
| TECH-2025-002 | [P] | TECH | E5 | 0.35 | The hyperscale AI data center boom resembles a bubble; to the extent LLMs are useful, deployment will shift toward pr... |
| TRANS-2025-001 | [T] | TRANS | E4 | 0.45 | The current global energy transition away from fossil fuels is “more or less irreversible” at this point. |
| TRANS-2025-002 | [F] | TRANS | E4 | 0.40 | Solar PV module costs fell from roughly $96/W in the mid-1970s to about $0.62/W by end-2012 and continue to decline. |
| TRANS-2025-003 | [F] | TRANS | E4 | 0.35 | China installed about 198 GW of solar PV between January and May 2025, including 93 GW coming online in May 2025 alone. |
| TRANS-2025-004 | [F] | TRANS | E4 | 0.35 | By late summer 2025, renewables supplied more than 50% of the EU’s electricity. |
| TRANS-2025-005 | [T] | TRANS | E4 | 0.40 | In the post-oil era, energy production will be more widely distributed rather than concentrated in resource-extractio... |
| TRANS-2025-006 | [H] | TRANS | E4 | 0.35 | Global fossil-fuel energy use has probably already passed peak oil and peak carbon, and is now trending inexorably do... |
| TRANS-2025-007 | [P] | TRANS | E5 | 0.30 | The forecast boom in small modular nuclear reactors will fizzle as cheap distributed solar PV plus battery storage sc... |

---

## Continuation Notes: AI as possible blind spot

### What changed in this pass

This continuation focuses on the AI portion of the argument bundle. The post mentions AI primarily as a hyperscale data-center boom that resembles a bubble (with eventual migration toward local inference), but does not engage much with the possibility that LLMs are a general-purpose technology with broad productivity effects (especially in software development).

### Why it matters to the thesis

If AI delivers durable productivity gains (even if partially obscured by hype/capex overshoot), it can:

- Provide a new “growth engine” that partially offsets the “post-Moore’s Law” stagnation framing.
- Change labor-market and institutional stress dynamics (faster automation pressures, faster organizational change).
- Interact with the energy transition directly (electricity demand, datacenter siting, grid build-out).

### What to test next (sources to add)

- Controlled evidence and/or high-quality observational evidence on AI-assisted software development productivity and adoption.
- Evidence on training/inference cost curves and whether capex build-out is plausibly transient vs durable infrastructure.
- Evidence on broader “general-purpose” effects outside coding (customer support, writing, analysis workflows).

### Evidence added in this pass

- `peng-2023-copilot-productivity` reports a controlled experiment where GitHub Copilot access reduced time-to-complete a programming task by 55.8% (`LABOR-2023-001`) and reports heterogeneous effects (`LABOR-2023-002`). This is direct evidence that “AI for code” can be a real productivity technology (not merely hype), while remaining compatible with the possibility that hyperscale capex can still have bubble dynamics.
- `chatterjee-2024-anz-copilot-study` reports an organizational A/B evaluation at ANZ Bank finding Copilot users completed coding challenges ~42.36% faster on average (`LABOR-2024-001`), with mixed/inconclusive evidence on quality/security in the same study (`LABOR-2024-002`).

### Working update

Treat “bubble” vs “steam-engine-scale general-purpose tech” as competing framings that are not mutually exclusive: early bubbles can coexist with real long-run impact. The critical question is whether current AI systems generate durable, generalizable productivity gains at scale, and whether those gains are large enough to change Stross’s macro “no new growth engines” posture.
