# Source Analysis: Project 2025 Tracker (Project2025.observer)

> **Claim types**: `[F]` fact, `[T]` theory, `[H]` hypothesis, `[P]` prediction, `[A]` assumption/definition, `[C]` counterfactual, `[S]` speculation, `[X]` contradiction  
> **Evidence**: **E1** systematic review/meta-analysis; **E2** peer-reviewed/official stats; **E3** expert consensus/preprint; **E4** primary/credible reporting; **E5** expert opinion/analysis; **E6** unsupported/speculative

## Metadata

| Field | Value |
|---|---|
| **Source ID** | `project2025observer-2026-tracker` |
| **Title** | Project 2025 Tracker |
| **Author(s)** | Project 2025 Observer (community project; individual authors not specified) |
| **Date** | Accessed 2026-03-03 (rolling tracker) |
| **Type** | REPORT (living tracker/website) |
| **URL** | https://www.project2025.observer/en |
| **Reliability** | 0.55 |
| **Rigor Level** | [DRAFT] |
| **Bias Notes** | Community-driven tracker; valuable for organizing claims/objectives and linking to sources per objective. Classification (“completed / in progress”) and aggregation methodology can embed subjective judgments; claims should be re-verified against the underlying cited sources. |

**Claims YAML**: [`analysis/sources/project2025observer-2026-tracker.yaml`](project2025observer-2026-tracker.yaml)

## Stage 1: Descriptive Analysis

### Core Thesis
The site presents itself as an objective monitoring dashboard that tracks which Project 2025 proposals are being implemented, including counts by agency and a timeline of completed objectives.

### Summary (Neutral)
The Project 2025 Tracker is a website that enumerates “objectives” attributed to Project 2025 proposals and tags each objective with a status (e.g., completed, in progress). It reports totals (objectives tracked, agencies involved) and provides filtering, agency-level progress breakdowns, and a timeline of completed objectives. The “About” page describes the project’s origins as a spreadsheet started by Reddit users and frames the tracker as non-advocacy, encouraging readers to consult multiple sources.

### Key Claims

| # | Claim | Claim ID | Layer | Actor | Scope | Quantifier | Type | Domain | Evid | Credence | Verified? | Falsifiable By |
|---:|---|---|---|---|---|---|---|---|---|---:|---|---|
| 1 | The tracker states it is a comprehensive, community-driven initiative to track implementation of Project 2025 proposals without advocating for or against them | GOV-2026-185 | ASSERTED | OTHER:Project2025Observer | who=site operators; where=project2025.observer; when=2026 | N/A | [F] | GOV | E5 | 0.70 | Verified (self-description) | Site governance/docs contradict neutrality claim |
| 2 | The tracker reports it is tracking 320 total objectives across 34 agencies | GOV-2026-186 | ASSERTED | OTHER:Project2025Observer | who=tracker; what=counts; when=2026-03-03 | N/A | [F] | GOV | E4 | 0.70 | Verified (as displayed) | Site shows different totals or later revisions materially change counts |
| 3 | The tracker reports aggregate status counts including 131 “Done” and 69 “In Progress” (implying 120 not started if totals are consistent) | GOV-2026-187 | ASSERTED | OTHER:Project2025Observer | when=2026-03-03; what=aggregate status counts | N/A | [F] | GOV | E4 | 0.60 | Verified (as displayed) | Site changes the counts or status definitions contradict |
| 4 | The tracker’s agency breakdown shows USAID at 100% (6 objectives), White House at 92% (13 objectives), and Dept. of State at 77% (11 objectives) | GOV-2026-188 | ASSERTED | OTHER:Project2025Observer | when=2026-03-03; what=agency progress stats | N/A | [F] | GOV | E4 | 0.60 | Verified (as displayed) | Site changes the agency counts or status assignments |
| 5 | The tracker provides per-objective “Sources” and “Discuss” links, implying each objective is intended to be auditable via cited references | GOV-2026-189 | ASSERTED | OTHER:Project2025Observer | what=feature set; when=2026 | N/A | [F] | GOV | E5 | 0.65 | Verified (UI feature) | Objectives lack sources or cited links are nonfunctional/irrelevant |

### Argument Structure

```
Project 2025 has many proposals (“objectives”)
        ↓
Tracker maps objectives → status + agency + sources
        ↓
Dashboard aggregates progress and timelines
```

### Scope & Limitations
- The tracker is a **secondary aggregation layer**; its core value depends on the quality and completeness of cited sources per objective.
- The site does not (in the captured pages) fully specify the **quantitative method** for converting objective statuses into a single “percent complete” metric.

## Stage 2: Evaluative Analysis

### Internal Coherence
The site’s UI and “About” narrative are coherent: it claims to list discrete objectives and mark status based on evidence. The principal epistemic risk is category drift (what counts as “completed”) and inconsistent mapping from the Project 2025 document to objective definitions.

### Key Factual Claims Verified

| Claim ID | Claim (paraphrased) | Crux? | Source Says | Actual | External Source | Search Notes | Status |
|---|---|---:|---|---|---|---|---|
| GOV-2026-186 | Tracker totals: 320 objectives; 34 agencies | **Y** | Yes | Confirmed those totals are displayed on the site’s home dashboard (as of access) | https://www.project2025.observer/en | q1: “project2025 observer 320 objectives 34 agencies” (2026-03-03); q2: “Project 2025 Tracker 320 total objectives” (2026-03-03) | ok (self-referential) |
| GOV-2026-185 | Project 2025 includes a ~900-page “Mandate for Leadership 2025” policy guide (context the site provides) | N | Yes | Heritage/Project 2025 materials describe “Mandate for Leadership” as the main policy volume; page count varies by edition/format | https://static.project2025.org/2025_MandateForLeadership_FULL.pdf | Timeboxed: verified existence of the PDF and its scale; did not reconcile exact page-count claims | ok (existence); ? (exact pages) |

### Disconfirming Evidence Search

| Claim | Counterevidence Found | Alternative Explanation | Search Notes |
|---|---|---|---|
| GOV-2026-187 (aggregate counts and implied “% complete”) | The site’s rendered “overall progress” percentage did not appear reliably in text extraction | Percent may be computed client-side; or weighted by “in progress” status | Looked at home + charts pages; did not find explicit formula |

### Credence Assessment
- **Overall Credence**: 0.55  
- **Reasoning**: Strong as an index/tracker; weaker as an authority on “completion percentage” without explicit methodology and without re-checking each objective’s cited sources.

## Stage 3: Dialectical Analysis

### Steelmanned Argument
A community tracker can increase accountability and reduce information asymmetry by translating a long policy blueprint into auditable, discrete objectives with linked evidence. Even if imperfect, it can be a high-signal starting point for systematic verification.

### Strongest Counterarguments
1. **Subjectivity**: “completed” is often contestable; a tracker can encode political interpretations as status labels.
2. **Selection bias**: tracked objectives might overrepresent sensational or easily-citable items.
3. **Method opacity**: a single “percent complete” number can mislead without a transparent formula and update discipline.

---

### Claim Summary

| ID | Type | Domain | Layer | Actor | Scope | Quantifier | Evidence | Credence | Claim |
|---|---|---|---|---|---|---|---|---:|---|
| GOV-2026-185 | [F] | GOV | ASSERTED | OTHER:Project2025Observer | when=2026 | N/A | E5 | 0.70 | The tracker describes itself as a community-driven, non-advocacy monitoring initiative |
| GOV-2026-186 | [F] | GOV | ASSERTED | OTHER:Project2025Observer | when=2026-03-03 | N/A | E4 | 0.70 | The tracker reports 320 total objectives across 34 agencies |
| GOV-2026-187 | [F] | GOV | ASSERTED | OTHER:Project2025Observer | when=2026-03-03 | N/A | E4 | 0.60 | The tracker reports 131 “Done” and 69 “In Progress” objectives |
| GOV-2026-188 | [F] | GOV | ASSERTED | OTHER:Project2025Observer | when=2026-03-03 | N/A | E4 | 0.60 | The tracker shows USAID 100% (6), White House 92% (13), State 77% (11) |
| GOV-2026-189 | [F] | GOV | ASSERTED | OTHER:Project2025Observer | when=2026 | N/A | E5 | 0.65 | The tracker provides per-objective sources/discussion links intended for auditability |

### Claims to Register

```yaml
claims:
  - id: "GOV-2026-186"
    text: "The Project 2025 Observer tracker reports that it is tracking 320 total objectives across 34 agencies (as of 2026-03-03)."
    type: "[F]"
    domain: "GOV"
    evidence_level: "E4"
    credence: 0.70
    operationalization: "Re-check the site dashboard at later dates and confirm the displayed totals and any changes."
    assumptions: ["The site’s displayed counts reflect its underlying objective database."]
    falsifiers: ["Later snapshots show materially different totals without clear explanation."]
    source_ids: ["project2025observer-2026-tracker"]
```

---

**Analysis Date**: 2026-03-03  
**Analyst**: codex (gpt-5.2)  
**Credence in Analysis**: 0.64

## Analysis Log

| Pass | Date | Tool | Model | Duration | Tokens | Cost | Notes |
|---:|---|---|---|---:|---:|---:|---|
| 1 | 2026-03-03 | codex | gpt-5.2 | — | — | — | Initial 3-stage analysis; captured dashboard totals and limitations; flagged missing transparency on “percent complete” formula |

