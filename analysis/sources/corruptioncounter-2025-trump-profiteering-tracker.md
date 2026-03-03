# Source Analysis: CorruptionCounter — Trump’s Presidential Profiteering (real-time tracker)

> **Claim types**: `[F]` fact, `[T]` theory, `[H]` hypothesis, `[P]` prediction, `[A]` assumption/definition, `[C]` counterfactual, `[S]` speculation, `[X]` contradiction  
> **Evidence**: **E1** systematic review/meta-analysis; **E2** peer-reviewed/official stats; **E3** expert consensus/preprint; **E4** primary/credible reporting; **E5** expert opinion/analysis; **E6** unsupported/speculative

## Metadata

| Field | Value |
|---|---|
| **Source ID** | `corruptioncounter-2025-trump-profiteering-tracker` |
| **Title** | CorruptionCounter — Trump’s Presidential Profiteering: A Real-Time Corruption Tracker |
| **Author(s)** | CorruptionCounter.com (site operators not clearly identified on landing page) |
| **Date** | Site indicates 2025-01-15 (page metadata); accessed 2026-03-03 |
| **Type** | REPORT (living tracker/website) |
| **URL** | https://corruptioncounter.com/ |
| **Reliability** | 0.40 |
| **Rigor Level** | [DRAFT] |
| **Bias Notes** | Advocacy-style tracker with strong rhetoric; it links each case to external journalism but does not clearly publish a transparent methodology for valuation/aggregation on the landing page. Useful as a case index and for extracting “what the tracker asserts,” but requires careful auditing. |

**Claims YAML**: [`analysis/sources/corruptioncounter-2025-trump-profiteering-tracker.yaml`](corruptioncounter-2025-trump-profiteering-tracker.yaml)

## Stage 1: Descriptive Analysis

### Core Thesis
CorruptionCounter claims to provide “comprehensive, real-time tracking” of alleged Trump presidential corruption/profiteering, categorizing cases and reporting a topline total dollar amount, with sources linked to major news outlets.

### Summary (Neutral)
The landing page states that CorruptionCounter tracks alleged corruption categories (foreign bribes, pardons for sale, quid pro quo, pocket lining, extortion, graft) and that each case includes “verified sources” from outlets like NYT/WSJ/Reuters. The site offers a CSV export feature. Page metadata and structured data describe “$2.9B+” tracked, but the amount implied by the embedded case dataset (as captured in a quick parse) does not obviously match that topline, suggesting either (a) the topline includes additional items not in the embedded list, (b) the list is incomplete in captured HTML, or (c) the topline is stale.

### Key Claims

| # | Claim | Claim ID | Layer | Actor | Scope | Quantifier | Type | Domain | Evid | Credence | Verified? | Falsifiable By |
|---:|---|---|---|---|---|---|---|---|---|---:|---|---|
| 1 | CorruptionCounter claims to provide comprehensive, real-time tracking of alleged Trump corruption cases and says each case includes “verified sources” from major outlets (NYT/WSJ/Reuters, etc.) | GOV-2026-196 | ASSERTED | OTHER:CorruptionCounter | who=site; when=2025..2026 | N/A | [F] | GOV | E5 | 0.55 | Verified (self-description) | Case links are missing/unverifiable or sources are systematically low quality |
| 2 | Site metadata/structured text claims “$2.9B+” in Trump corruption documented (including a line “As of June 2025… over $2.9 billion”) | GOV-2026-197 | ASSERTED | OTHER:CorruptionCounter | when=2025-06 claimed | N/A | [F] | GOV | E5 | 0.45 | Verified (as stated) | Embedded/available dataset cannot support the number under any consistent aggregation method |
| 3 | A parse of the embedded `corruptionCases` dataset in the landing-page HTML yields 25 cases dated 2024-12-20..2025-10-30 with a summed `amount` total of $2,165,900,000 | GOV-2026-198 | ASSERTED | OTHER:CorruptionCounter | when=captured 2026-03-03 | N/A | [F] | GOV | E2/E5 | 0.70 | Verified (code-level capture) | Re-parse shows materially different case count/total |
| 4 | The tracker’s categories include: Foreign Bribes, Pardons for Sale, Quid Pro Quo, Pocket Lining, Extortion, and Graft | GOV-2026-199 | ASSERTED | OTHER:CorruptionCounter | when=2025..2026 | N/A | [F] | GOV | E5 | 0.75 | Verified (page text) | Categories differ materially |
| 5 | The site offers a client-side “Export Data as CSV” feature that exports total amount + case rows (date/title/description/amount/category/source) | GOV-2026-200 | ASSERTED | OTHER:CorruptionCounter | when=2025..2026 | N/A | [F] | GOV | E5 | 0.70 | Verified (HTML/JS) | Export function is absent or materially different |
| 6 | The embedded dataset includes a case labeled “$Trump Memecoin Sales Fees” with `amount` $320,000,000 categorized as “Pocket Lining,” citing a NYT source | GOV-2026-201 | ASSERTED | OTHER:CorruptionCounter | when=2025-05-22 | N/A | [F] | GOV | E5 | 0.55 | Verified (dataset entry) | Dataset entry absent or materially different |
| 7 | The embedded dataset includes a case labeled “The 747 from Qatar” with `amount` $200,000,000 categorized as “Foreign Bribe,” citing a NYT source | GOV-2026-202 | ASSERTED | OTHER:CorruptionCounter | when=2025-05-26 | N/A | [F] | GOV | E5 | 0.55 | Verified (dataset entry) | Dataset entry absent or materially different |

## Stage 2: Evaluative Analysis

### Internal Coherence
The site coherently presents itself as a corruption tracker with categories and sourced entries. The main coherence issue is the mismatch between the prominent “$2.9B+” framing and the apparent total of the embedded case list captured in a quick parse.

### Key Factual Claims Verified

| Claim ID | Claim (paraphrased) | Crux? | Source Says | Actual | External Source | Search Notes | Status |
|---|---|---:|---|---|---|---|---|
| GOV-2026-197 | “$2.9B+” documented (as of June 2025) | **Y** | Yes | Confirmed the page metadata and structured text assert “$2.9B+,” but the embedded case array captured in HTML sums to ~$2.166B across 25 cases; unclear whether topline includes additional items/valuations | https://corruptioncounter.com/ | Verified by inspecting HTML meta + parsing embedded `corruptionCases` array; timeboxed | ? (internal mismatch) |
| GOV-2026-198 | Embedded dataset sums to $2.1659B across 25 cases | N | Yes | Recomputed by parsing the landing-page HTML case array and summing numeric `amount` fields | https://corruptioncounter.com/ | q1: “parse corruptionCases array sum amounts” (local capture, 2026-03-03); q2: “recompute total from embedded JS array” (local capture, 2026-03-03) | ok |

### Corrections & Updates

| Item | URL | Published | Corrected/Updated | What Changed | Impacted Claim IDs | Action Taken |
|---:|---|---|---|---|---|---|
| 1 | https://corruptioncounter.com/ | 2025-01-15 (metadata) | 2026-03-03 (capture) | Found internal inconsistency between “$2.9B+” framing and embedded dataset sum | GOV-2026-197, GOV-2026-198 | Flagged as unresolved; requires full audit or exporter output comparison |

### Evidence Assessment
- The tracker is best treated as an **index** into linked journalism, not a primary financial ledger.
- Embedded dataset is machine-readable and auditable, but interpretation depends on definitions (what counts; realized vs unrealized; missing entries).

### Credence Assessment
- **Overall Credence**: 0.40  
- **Reasoning**: Strong rhetoric and unclear provenance; internal mismatch suggests either missing context or poor update discipline. Still useful for enumerating alleged cases and source links.

## Stage 3: Dialectical Analysis

### Steelmanned Argument
A centralized tracker can lower the cost of public scrutiny by collecting disparate corruption allegations into a single list with links, enabling journalists and researchers to verify and extend. A client-side export tool supports transparency.

### Strongest Counterarguments
1. **Aggregation games**: topline numbers can be inflated by including illiquid valuations or double-counting.
2. **Selection bias**: case inclusion may be driven by narrative/political salience rather than consistent criteria.
3. **Update mismatch**: if the headline number isn’t mechanically tied to the dataset, it’s easy to drift into misinformation.

---

### Claim Summary

| ID | Type | Domain | Layer | Actor | Scope | Quantifier | Evidence | Credence | Claim |
|---|---|---|---|---|---|---|---|---:|---|
| GOV-2026-196 | [F] | GOV | ASSERTED | OTHER:CorruptionCounter | when=2025..2026 | N/A | E5 | 0.55 | CorruptionCounter claims comprehensive real-time tracking with verified sources from major outlets |
| GOV-2026-197 | [F] | GOV | ASSERTED | OTHER:CorruptionCounter | when=2025-06 claimed | N/A | E5 | 0.45 | Site metadata/structured text claims “$2.9B+” documented |
| GOV-2026-198 | [F] | GOV | ASSERTED | OTHER:CorruptionCounter | when=2026-03-03 capture | N/A | E2/E5 | 0.70 | Embedded dataset parses to 25 cases totaling $2,165,900,000 (amount fields) |
| GOV-2026-199 | [F] | GOV | ASSERTED | OTHER:CorruptionCounter | when=2025..2026 | N/A | E5 | 0.75 | Tracker categories include Foreign Bribes, Pardons for Sale, Quid Pro Quo, Pocket Lining, Extortion, Graft |
| GOV-2026-200 | [F] | GOV | ASSERTED | OTHER:CorruptionCounter | when=2025..2026 | N/A | E5 | 0.70 | Site offers client-side CSV export of total amount + case rows |
| GOV-2026-201 | [F] | GOV | ASSERTED | OTHER:CorruptionCounter | when=2025-05-22 | N/A | E5 | 0.55 | Dataset includes a $320M “memecoin sales fees” pocket-lining entry |
| GOV-2026-202 | [F] | GOV | ASSERTED | OTHER:CorruptionCounter | when=2025-05-26 | N/A | E5 | 0.55 | Dataset includes a $200M “747 from Qatar” foreign-bribe entry |

### Claims to Register

```yaml
claims:
  - id: "GOV-2026-198"
    text: "A parse of CorruptionCounter’s embedded landing-page dataset (`corruptionCases`) on 2026-03-03 yields 25 cases dated 2024-12-20..2025-10-30 whose numeric `amount` fields sum to $2,165,900,000."
    type: "[F]"
    domain: "GOV"
    evidence_level: "E5"
    credence: 0.70
    operationalization: "Re-run the parse on later dates; compare to CSV export output; reconcile differences with the site’s headline totals."
    assumptions: ["The embedded dataset represents the tracker’s canonical case list."]
    falsifiers: ["Later captures show a different canonical dataset or export totals contradict this parse consistently."]
    source_ids: ["corruptioncounter-2025-trump-profiteering-tracker"]
```

---

**Analysis Date**: 2026-03-03  
**Analyst**: codex (gpt-5.2)  
**Credence in Analysis**: 0.60

## Analysis Log

| Pass | Date | Tool | Model | Duration | Tokens | Cost | Notes |
|---:|---|---|---|---:|---:|---:|---|
| 1 | 2026-03-03 | codex | gpt-5.2 | — | — | — | Initial 3-stage analysis; parsed embedded JS dataset and found mismatch with headline “$2.9B+” framing |

