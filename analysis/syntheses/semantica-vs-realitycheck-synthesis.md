# Synthesis: Semantica vs Reality Check (Complementarity, Overlap, Gaps)

## Metadata

| Field | Value |
|------|-------|
| **Date** | 2026-02-07 |
| **Synthesis ID** | `semantica-vs-realitycheck-synthesis` |
| **Primary Sources** | `hawksightai-2026-semantica`, `lhl-2026-realitycheck-readme`, `lhl-2026-realitycheck-data-readme` |
| **Related Analyses** | `analysis/sources/hawksightai-2026-semantica.md`, `analysis/sources/lhl-2026-realitycheck-readme.md`, `analysis/sources/lhl-2026-realitycheck-data-readme.md` |

## Executive Summary
Semantica and Reality Check are aligned in *intent* (auditability/traceability), but operate at different layers:

- **Semantica** is a **semantic data/knowledge-engineering framework**: ingestion → parsing/normalization/splitting → entity/relation extraction → knowledge graph/ontology → reasoning → storage backends (graph/triplet/vector) with provenance/change-management overlays.
- **Reality Check** is an **epistemic bookkeeping + analysis framework**: sources → structured 3-stage analyses → claims with stable IDs → evidence links → reasoning trails → predictions/chains, all backed by a DB and validated by integrity checks.

They can be **useful together** when you want *both* (a) scalable semantic structuring of content (Semantica) and (b) explicit, human-auditable claim/evidence/credence tracking (Reality Check). Neither substitutes for the other’s core competency.

## What Each Project Optimizes For

### Reality Check: “Claim Ledger + Provenance”
**Primary artifact**: discrete claims with stable IDs, evidence levels, credence, and explicit backing/contradiction links.

**Strengths**
- Strong support for **auditable epistemic state**: what is claimed, why believed, how falsified, and where it came from.
- Database-native primitives (**claims / sources / evidence links / reasoning trails / predictions / chains**) with validation tooling.
- Works well as a **knowledge base for decision-making** and long-running research programs.

**Weaknesses / gaps**
- Not designed as a full ingestion/knowledge-graph framework: it doesn’t aim to provide multi-format parsing, KG stores, or graph reasoning engines.
- Requires discipline: a lot of value comes from **human verification work**, not just tooling.

### Semantica: “Semantic Layer + Knowledge Graph Stack”
**Primary artifact**: entities/relations/graphs/ontologies + provenance records across pipeline steps; plus modules for storage and reasoning.

**Strengths**
- Broad coverage for **semantic engineering workflows**: ingestion/parsing → extraction → graph/ontology → reasoning → storage and retrieval.
- Strong evidence of implementation for headline modules (notably **provenance + change management**) and meaningful unit coverage for many areas.
- Offers building blocks for **GraphRAG** and agent memory (vector + graph retrieval and traversal).

**Weaknesses / risks**
- Scope is wide; maturity is **uneven**. In this checkout, some suites fail (notably embeddings + visualization, plus smaller issues in several modules). See `analysis/sources/hawksightai-2026-semantica.md`.
- “Compliance / trustworthy” framing is best interpreted as **infrastructure** (lineage, checksums, audit logs), not an end-to-end guarantee of correctness.
- Core dependency footprint is large, increasing operational friction.

## Overlap: Where They Mean Similar Things

### Provenance / Traceability
- **Semantica provenance**: tracks lineage of pipeline artifacts (document → chunk → entity → relation → graph) with a PROV-O-inspired schema and checksums.
- **Reality Check provenance**: tracks epistemic justification via **evidence links** (claim ↔ source with strength + location) and **reasoning trails** (why a credence was assigned).

**Key difference**: Semantica provenance is oriented toward *pipeline artifact lineage*; Reality Check provenance is oriented toward *belief justification and revision*.

### Conflict/Contradiction
- **Semantica**: conflict resolution tends to be about **entity/property/relationship conflicts** in integrated data and KGs.
- **Reality Check**: contradictions (when used) are about **claims** that conflict and must be adjudicated with evidence/credence updates.

## Complementarity: How to Use Them Together

### Pattern 1: Semantica as “Extraction + KG”, Reality Check as “Epistemic Ledger”
1. Use Semantica to ingest/parse sources and extract candidate entities/relations/triplets.
2. Convert high-salience triplets into Reality Check **claims** (with stable IDs).
3. Use Reality Check to attach **evidence links** (source locations/quotes) and **reasoning trails** (credence, falsifiers).

**Why this works**: Semantica increases throughput for structuring information; Reality Check ensures the “truth maintenance system” stays explicit and auditable.

### Pattern 2: Reality Check as “Audit DB” for Semantica GraphRAG
1. Treat Reality Check’s claim registry as the authoritative set of “assertions you’re willing to stand behind”.
2. Mirror claims into Semantica as nodes/edges (or as a graph overlay) for GraphRAG retrieval.
3. Require Semantica’s downstream responses to include Reality Check claim IDs + evidence links as citations.

**Why this works**: It prevents “graph-shaped hallucinations” by anchoring the KG to a curated claim ledger.

### Pattern 3: PROV-O bridging (optional, advanced)
If you care about standards interoperability, you can map:
- Semantica `ProvenanceEntry` → Reality Check evidence links / reasoning trails (and vice versa),
but this is non-trivial and should be treated as an integration project rather than “out of the box”.

## Decision Guidance

### Use Reality Check alone if…
- Your core problem is **epistemic tracking** (what do we believe, why, and what would change it).
- You want stable claim IDs, credence accounting, and evidence trails more than KG infrastructure.

### Use Semantica alone if…
- Your core problem is **semantic structuring** (multi-format ingest + extraction + KG/ontology + reasoning) and you don’t need explicit credence/evidence accounting.
- You’re building an application where *audit trails of pipeline steps* matter more than belief revision.

### Use both if…
- You want **high-throughput semantic extraction** *and* **explicit, revisable belief tracking**.
- You’re in a domain where you need to answer both:
  - “What does the system think?” (Semantica/KG)
  - “Why should we believe it?” (Reality Check evidence + credence)

## Open Questions / Next Checks
- Define a minimal “glue schema”: how Semantica entities/relations map into Reality Check claim types (and how provenance locations map into evidence link locations).
- Decide the source of truth for “facts”: Semantica KG vs Reality Check claim ledger (recommended: Reality Check for committed claims; Semantica for candidate extraction + retrieval substrate).

