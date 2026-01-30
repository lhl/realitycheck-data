# Reasoning: RESOURCE-2026-007

> **Claim**: A practical lower bound for variable inference cost per million tokens is approximately: COGS($/MTok) ≈ (cluster $/hr) / (effective tok/s × 3600) × 1e6; utilization and effective throughput therefore dominate unit cost.
> **Credence**: 0.95 (E2)
> **Domain**: RESOURCE

## Evidence Summary

| Direction | Source | Location | Strength | Summary |
|-----------|--------|----------|----------|---------|
| Supports | [lhl-2026-frontier-llm-token-unit-economics](../sources/lhl-2026-frontier-llm-token-unit-economics.md) | Analysis file: analysis/sources/lhl-2026-frontier-llm-token-unit-economics.md (claim tables / Claims to Register YAML); URL: https://github.com/lhl/frontier-llm-token-unit-economics | 0.9 | Provenance backfill: link records the primary sour... |

## Reasoning Chain

This trail documents the current credence/evidence assignment for RESOURCE-2026-007 as stored in the database. The claim is recorded with evidence level E2 and credence 0.95. Supporting evidence is linked via 1 evidence-link(s) (see list) and the source(s) listed in the claim record (e.g., lhl-2026-frontier-llm-token-unit-economics (https://github.com/lhl/frontier-llm-token-unit-economics)). Primary uncertainty is whether the underlying official/peer-reviewed data were interpreted correctly and are comparable across contexts; independent replication would strengthen. This backfill does not constitute fresh verification; it makes the provenance explicit and reviewable.

## Assumptions

- Accelerator time is the dominant variable cost component at the margin.

## Trail History

| Date | Credence | Evidence | Status | Pass |
|------|----------|----------|--------|------|
| 2026-01-31 | 0.95 | E2 | active | 2 |

## Data (portable)

```yaml
claim_id: "RESOURCE-2026-007"
reasoning_trail_id: "REASON-2026-083"
credence_at_time: 0.949999988079071
evidence_level_at_time: "E2"
supporting_evidence: ["EVLINK-2026-081"]
contradicting_evidence: []
```
