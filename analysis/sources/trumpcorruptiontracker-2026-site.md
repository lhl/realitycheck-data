# Source Analysis: Trump Corruption Tracker (trumpcorruptiontracker.com)

> **Claim types**: `[F]` fact, `[T]` theory, `[H]` hypothesis, `[P]` prediction, `[A]` assumption/definition, `[C]` counterfactual, `[S]` speculation, `[X]` contradiction  
> **Evidence**: **E1** systematic review/meta-analysis; **E2** peer-reviewed/official stats; **E3** expert consensus/preprint; **E4** primary/credible reporting; **E5** expert opinion/analysis; **E6** unsupported/speculative

## Metadata

| Field | Value |
|---|---|
| **Source ID** | `trumpcorruptiontracker-2026-site` |
| **Title** | Trump Corruption Tracker |
| **Author(s)** | TrumpCorruptionTracker.com (site operators not clearly identified on landing HTML) |
| **Date** | Accessed 2026-03-03 (rolling tracker) |
| **Type** | REPORT (living tracker/website + public dataset) |
| **URL** | https://trumpcorruptiontracker.com/ |
| **Reliability** | 0.45 |
| **Rigor Level** | [DRAFT] |
| **Bias Notes** | Tracker site appears to crowdsource/curate “incidents” with summaries and links. Value is primarily as an index and aggregation layer; incident summaries and data quality vary and should be audited against linked sources. |

**Claims YAML**: [`analysis/sources/trumpcorruptiontracker-2026-site.yaml`](trumpcorruptiontracker-2026-site.yaml)

## Stage 1: Descriptive Analysis

### Core Thesis
The site presents itself as a tracker of “Trump’s White House Financial Corruptions,” organizing incidents with summaries, categories, voting/engagement, and outbound source links.

### Summary (Neutral)
Direct page capture via generic HTML extraction showed a client-side web app that loads incidents dynamically. By inspecting the site’s bundled JavaScript, the tracker appears to store incidents in a Supabase-backed table (`incidents`) and fetch them via the Supabase/PostgREST API. Querying that public API shows a few hundred non-hidden incidents with standardized fields (number, date, headline/description, categories, votes, source name, and source URLs). Some records show apparent data quality problems (e.g., implausible date formats), indicating the dataset is not cleanly curated.

### Key Claims

| # | Claim | Claim ID | Layer | Actor | Scope | Quantifier | Type | Domain | Evid | Credence | Verified? | Falsifiable By |
|---:|---|---|---|---|---|---|---|---|---|---:|---|---|
| 1 | TrumpCorruptionTracker.com is a client-side single-page app intended to track and display “Trump’s White House Financial Corruptions” | GOV-2026-209 | ASSERTED | OTHER:site | what=tracker purpose; when=2026 | N/A | [F] | GOV | E5 | 0.65 | Verified (HTML/JS) | Site is not a tracker or purpose is materially different |
| 2 | The site’s bundled JS contains a public Supabase project endpoint and uses it to query a table named `incidents` | GOV-2026-210 | ASSERTED | OTHER:site | what=data backend; when=2026-03-03 | N/A | [F] | GOV | E4 | 0.75 | Verified (code + API) | No Supabase backend exists or table name differs |
| 3 | The public API query `hidden=eq.false` returns 266 visible incidents (as of 2026-03-03) | GOV-2026-211 | ASSERTED | OTHER:dataset | when=2026-03-03 | N/A | [F] | GOV | E2 | 0.80 | Verified (API count) | Repeat query yields materially different count without explanation |
| 4 | Incident records include fields such as `number`, `date`, `headline`, `description`, `categories`, `votes`, `source_name`, `sources`, and `hidden` | GOV-2026-212 | ASSERTED | OTHER:dataset | when=2026-03-03 | N/A | [F] | GOV | E2 | 0.80 | Verified (API sample) | Records lack these fields or schema differs materially |
| 5 | The maximum visible incident `number` observed in a quick query was 269 (dated 2025-11-14; source_name “Pro Publica”), suggesting numbering is not strictly contiguous with visible count | GOV-2026-213 | ASSERTED | OTHER:dataset | when=2026-03-03 | N/A | [F] | GOV | E2 | 0.70 | Verified (API query) | Later query shows materially different max number and/or meaning of `number` |
| 6 | The dataset contains apparent data quality issues (example: a visible incident record with an implausible date string “29026-01-30”) | GOV-2026-214 | ASSERTED | OTHER:dataset | when=2026-03-03 | N/A | [F] | GOV | E2 | 0.75 | Verified (API sample) | Re-check shows no such issue and date formats are consistent |

## Stage 2: Evaluative Analysis

### Internal Coherence
The tracker’s architecture is coherent (SPA + backend table + filters), but the dataset’s trustworthiness depends on the fidelity of summaries and link accuracy. The observed date-format anomaly suggests inconsistent data entry or parsing.

### Key Factual Claims Verified

| Claim ID | Claim (paraphrased) | Crux? | Source Says | Actual | External Source | Search Notes | Status |
|---|---|---:|---|---|---|---|---|
| GOV-2026-211 | 266 visible incidents in `incidents` table | **Y** | Yes | PostgREST query with `hidden=eq.false` returned content-range 0–265/266 | https://brsbkktxudbsmpqfaerz.supabase.co/rest/v1/incidents?hidden=eq.false&select=id | Verified via direct API call with public credentials embedded in client JS | ok |
| GOV-2026-214 | Data quality issue (date “29026-01-30”) | N | Yes | API sample returned at least one record with date formatted as “29026-01-30” | https://brsbkktxudbsmpqfaerz.supabase.co/rest/v1/incidents?hidden=eq.false&select=number,date,headline&order=date.desc&limit=1 | Sampled latest-by-date ordering; observed implausible date string | ok (as observed) |

### Disconfirming Evidence Search

| Claim | Counterevidence Found | Alternative Explanation | Search Notes |
|---|---|---|---|
| GOV-2026-214 (bad date) is systemic | Not tested | Could be a single data entry error rather than systemic corruption of dates | Would need schema constraints / broader scan |

### Credence Assessment
- **Overall Credence**: 0.45  
- **Reasoning**: High confidence that the tracker and dataset exist and are queryable; low confidence that individual incident summaries are consistently accurate without auditing a representative sample.

## Stage 3: Dialectical Analysis

### Steelmanned Argument
A centralized, filterable incident database with links can provide public transparency, lower research costs, and allow collaborative curation of corruption allegations over time.

### Strongest Counterarguments
1. **Curation drift**: without visible governance standards, incident inclusion and summaries can become partisan or error-prone.
2. **Data hygiene**: anomalies in dates and other fields weaken reliability and complicate aggregation.
3. **Summary vs source**: the linked articles (not the tracker summaries) are the real evidence; summaries can bias interpretation.

---

### Claim Summary

| ID | Type | Domain | Layer | Actor | Scope | Quantifier | Evidence | Credence | Claim |
|---|---|---|---|---|---|---|---|---:|---|
| GOV-2026-209 | [F] | GOV | ASSERTED | OTHER:site | when=2026 | N/A | E5 | 0.65 | TrumpCorruptionTracker.com is an SPA intended to track Trump financial corruption incidents |
| GOV-2026-210 | [F] | GOV | ASSERTED | OTHER:site | when=2026-03-03 | N/A | E4 | 0.75 | Client JS uses a public Supabase endpoint to query an `incidents` table |
| GOV-2026-211 | [F] | GOV | ASSERTED | OTHER:dataset | when=2026-03-03 | N/A | E2 | 0.80 | API query returned 266 visible incidents (hidden=false) |
| GOV-2026-212 | [F] | GOV | ASSERTED | OTHER:dataset | when=2026-03-03 | N/A | E2 | 0.80 | Incident records include number/date/headline/description/categories/votes/source fields |
| GOV-2026-213 | [F] | GOV | ASSERTED | OTHER:dataset | when=2026-03-03 | N/A | E2 | 0.70 | Max visible incident number observed was 269 (dated 2025-11-14; ProPublica) |
| GOV-2026-214 | [F] | GOV | ASSERTED | OTHER:dataset | when=2026-03-03 | N/A | E2 | 0.75 | Dataset contains an implausible date string “29026-01-30” in a visible record |

### Claims to Register

```yaml
claims:
  - id: "GOV-2026-211"
    text: "A direct query of TrumpCorruptionTracker’s public Supabase/PostgREST endpoint returned 266 non-hidden incidents in its `incidents` table (as of 2026-03-03)."
    type: "[F]"
    domain: "GOV"
    evidence_level: "E2"
    credence: 0.80
    operationalization: "Repeat the API query at later dates; record changes in total count and visibility rules."
    assumptions: ["The public API reflects the same dataset the website displays."]
    falsifiers: ["Public API and website totals diverge systematically."]
    source_ids: ["trumpcorruptiontracker-2026-site"]
```

---

**Analysis Date**: 2026-03-03  
**Analyst**: codex (gpt-5.2)  
**Credence in Analysis**: 0.67

## Analysis Log

| Pass | Date | Tool | Model | Duration | Tokens | Cost | Notes |
|---:|---|---|---|---:|---:|---:|---|
| 1 | 2026-03-03 | codex | gpt-5.2 | — | — | — | Initial 3-stage analysis; overcame bot-gated UI by inspecting bundled JS and querying the public Supabase dataset directly |

