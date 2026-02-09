# Source Analysis: Thread: “Windows is awful” + caste-discrimination claims at Microsoft (Thread Reader)

> **Claim types**: `[F]` fact, `[T]` theory, `[H]` hypothesis, `[P]` prediction, `[A]` assumption, `[C]` counterfactual, `[S]` speculation, `[X]` contradiction  
> **Evidence**: **E1** systematic review/meta-analysis; **E2** peer-reviewed/official stats/law; **E3** expert consensus/preprint; **E4** credible journalism/official report; **E5** opinion/anecdote; **E6** unsupported/speculative

## Metadata

| Field | Value |
|---|---|
| **Source ID** | `miyaspokeofthis-2026-windows-caste-thread` |
| **Title** | Thread: “If you ever wondered why Windows is so awful…” (caste-discrimination allegations) |
| **Author(s)** | @miyaspokeofthis (miya.eth ┊ nsa.eth ┊ FKA krys.eth) |
| **Date** | 2026-02-08 |
| **Type** | SOCIAL |
| **URL** | https://threadreaderapp.com/thread/2020302908919804019.html |
| **Reliability** | 0.25 |
| **Rigor Level** | [REVIEWED] |
| **Bias Notes** | Heavy stereotyping and scapegoating (“Windows is awful because… Indians”); rhetorical sarcasm; no primary citations; points to embedded X links (inaccessible here) and screenshots rather than verifiable documents. |

**Claims YAML**: [`analysis/sources/miyaspokeofthis-2026-windows-caste-thread.yaml`](miyaspokeofthis-2026-windows-caste-thread.yaml)

## Stage 1: Descriptive Analysis

### Core Thesis
The thread mocks Windows/Microsoft by attributing Windows’ perceived poor quality to Microsoft employing “so many Indians” that caste discrimination allegedly shapes work assignment (e.g., “Python for higher castes, C++ for lower castes”). It then claims the author received threatening DMs denying caste discrimination and urges readers to search “caste in IT” for supporting reports.

### Summary (Neutral)
The thread is short (five posts). The first post asserts a causal explanation for “Windows is awful,” referencing alleged caste discrimination at Microsoft and an alleged caste-based sorting of programming-language assignments (Python vs C++). The second and later posts mostly gesture to other (embedded) X posts for supporting examples. The third post claims the author received many DMs threatening them and denying caste discrimination, and it claims that searching “caste in IT” will reveal many reports and first-person accounts.

### Extract (What the thread says)

> 1) “If you ever wondered why Windows is so awful… ‘Microsoft faces allegations of caste-based discrimination’ … ‘Higher castes are assigned Python’ … ‘Lower castes are relegated to C++’”
>
> 2) “It’s how you get things like this:” (embedded X link)
>
> 3) “I got half of India in my DMs sending threats… Just look up ‘caste in IT’ and check the various reports…”
>
> 4–5) “Unrelated to Microsoft, but check this out:” (embedded X links)

### Key Claims

| # | Claim | Claim ID | Type | Domain | Evidence | Credence | Verified? | Falsifiable By |
|---|-------|----------|------|--------|----------|----------:|-----------|----------------|
| 1 | Windows is “awful” because Microsoft has “so many Indians” (implicit: Indian workforce → poor software outcomes) | SOC-2026-010 | [S] | SOC | E6 | 0.05 | ? | Evidence that Windows’ quality problems are causally attributable to nationality/ethnicity composition, controlling for org/process/architecture (highly implausible) |
| 2 | Caste discrimination in the tech/IT industry has been credibly alleged and has been the subject of major legal actions (e.g., the Cisco case) | LABOR-2026-016 | [F] | LABOR | E2 | 0.85 | CRD/DFEH | Authoritative sources show the cited cases did not occur or were materially mischaracterized |
| 3 | Major outlets have reported caste-discrimination allegations/complaints involving Microsoft in the U.S. tech sector (often via advocacy-group complaint/survey reporting and policy-coverage discussions) | LABOR-2026-017 | [F] | LABOR | E4 | 0.75 | VICE; NPR; Ars | Corrections/retractions showing Microsoft was not included in the reported complaint/survey lists; or a finding that the reported complaint data was fabricated |
| 4 | Caste status determines assignment to “Python” vs “C++/Java/janitorial duties” at Microsoft (as described in the thread) | LABOR-2026-018 | [F] | LABOR | E6 | 0.10 | ? | Any reliable documentary record showing the language-division claim is false; or, conversely, corroborated complaint/court record confirming it |
| 5 | The author received many threatening DMs from Indians denying caste discrimination | SOC-2026-011 | [F] | SOC | E5 | 0.40 | ? | Account data/screenshots showing no such messages (not generally falsifiable without access to the account) |
| 6 | Searching “caste in IT” yields many reports and first-person accounts from Indians alleging caste discrimination in tech workplaces | LABOR-2026-019 | [F] | LABOR | E4 | 0.75 | WIRED; NPR; VICE; Ars; NBC; AP; New Yorker | A systematic review finds such reporting is vanishingly rare or based on fabricated accounts |

### Argument Structure

```
Claim: Microsoft has many Indian employees
        ↓
Claim: Caste dynamics in Indian society carry into tech workplaces
        ↓
Claim: Caste discrimination affects work assignment (Python vs C++/etc.)
        ↓
Conclusion: This “explains” why Windows is bad (mocking/scapegoating frame)
```

### Theoretical Lineage
- **Workplace discrimination**: informal hierarchies and in-group favoritism reproduced inside organizations.
- **Diaspora transmission**: social stratification and bias persisting across geographies and institutions.
- **Scapegoating/national stereotyping**: attributing complex system failures to an out-group.

### Scope & Limitations
- The thread provides no primary documentation (no complaint filing, docket, or independent reporting) for its specific Microsoft “Python vs C++/janitorial duties” allegation.
- However, multiple major outlets document caste-discrimination allegations in U.S. tech and include Microsoft in complaint/survey and policy discussions; this supports the *existence of public allegations/complaints*, not adjudicated findings.
- Embedded X posts linked by the thread are not accessible in this environment (HTTP 403), limiting verification of referenced examples.
- Some asserted “evidence” appears to be screenshots; images were not OCRed in this pass, so only the text explicitly written in the thread was analyzed.

## Stage 2: Evaluative Analysis

### Internal Coherence
The thread’s core move is rhetorical rather than evidential: it jumps from a claimed instance of caste discrimination to a broad ethnic scapegoat explanation for Windows quality. Even if caste discrimination exists in some workplaces (plausible), it does not logically support the additional inference that “Windows is awful because Indians,” nor does it establish that caste-based language assignment is real or common.

### Key Factual Claims Verified

| Claim (paraphrased) | Crux? | Source Says | Actual | External Source | Status |
|---|---:|---|---|---|---|
| Caste discrimination in tech has been alleged and has reached major legal action (Cisco) | **Y** | “look up ‘caste in IT’ and check reports” (implies real cases) | CRD/DFEH publicly announced a lawsuit alleging caste-based discrimination at Cisco (June 2020), and later mainstream reporting covered its continued litigation and policy spillovers | https://calcivilrights.ca.gov/2020/06/30/dfeh-sues-cisco-systems-inc-and-former-managers-for-caste-based-discrimination/ ; https://apnews.com/article/cisco-caste-discrimination-lawsuit-california-a82cf1b775217bd3cabca24be89c3bf8 ; https://www.npr.org/2020/10/12/922936053/california-workplace-discrimination-system-sheds-light-on-caste-system | ok (major documented case exists) |
| Major outlets report caste-discrimination allegations/complaints that explicitly include Microsoft (U.S. tech sector) | **Y** | “Microsoft faces allegations…” | Multiple major outlets report advocacy-group complaint/survey claims and related reporting that includes Microsoft; this verifies *reported allegations/complaints exist*, not that any specific allegation is adjudicated true | https://www.vice.com/en/article/silicon-valley-has-a-caste-discrimination-problem/ ; https://www.npr.org/2020/10/12/922936053/california-workplace-discrimination-system-sheds-light-on-caste-system ; https://arstechnica.com/tech-policy/2022/08/indian-workers-allege-casteism-in-big-tech-question-discrimination-policies/ | ok/? (reported allegations exist; not adjudicated) |
| Microsoft has a substantiated, widely reported caste-discrimination case with Python-vs-C++ assignment claims | Y | “Higher castes… Python / Lower… C++” | Still only found a single low-rigor outlet (GreatAndhra) describing an alleged Hyderabad complaint with Python/C++/janitorial-duty claims; no corroborating mainstream reporting or docket found in this pass | https://www.greatandhra.com/articles/special-articles/dalit-engineer-alleges-caste-bias-at-microsoft-152676 | ? (unverified beyond single outlet) |
| There are many reports/first-person accounts of caste discrimination in Silicon Valley / tech | Y | “A LOT of reports…” | Multiple major outlets have published reporting and first-person accounts around caste discrimination allegations in tech; prevalence and representativeness remain uncertain, but the “there is lots of reporting” claim is supported | https://www.wired.com/story/trapped-in-silicon-valleys-hidden-caste-system/ ; https://www.nbcnews.com/news/asian-america/big-techs-big-problem-also-best-kept-secret-caste-discrimination-rcna33692 ; https://www.newyorker.com/news/q-and-a/googles-caste-bias-problem ; https://arstechnica.com/tech-policy/2022/08/indian-workers-allege-casteism-in-big-tech-question-discrimination-policies/ | ok/? (many sources exist; magnitude unclear) |

### Disconfirming Evidence Search

| Claim | Counterevidence Found | Alternative Explanation | Search Notes |
|---|---|---|---|
| LABOR-2026-017 (Microsoft included in reported allegations/complaints) | The most concrete “Microsoft” evidence in accessible reporting often takes the form of advocacy-group complaint/survey claims rather than adjudicated findings; companies may also claim they received no official complaints | Selection bias and reporting incentives: workers may prefer advocacy groups or journalists over HR (visa fear, retaliation concerns), and complaint counts don’t measure prevalence | Reviewed multiple major outlets (VICE, NPR, Ars/Reuters-summary, Quartz, etc.) for explicit Microsoft mentions and disclaimers |
| LABOR-2026-018 (Python vs C++ by caste) | No evidence of an actual organizational practice; claim appears as a punchline-like simplification of a single alleged complaint | The “Python vs C++” framing may be a meme-like distortion of “some assignments denied” rather than a systematic policy | Searched for the phrase “Higher castes are assigned Python” and found only one outlet repeating the idea |
| SOC-2026-010 (Windows bad because Indians) | Windows quality is more plausibly explained by architecture legacy, incentives, product-management choices, and organizational complexity | Scapegoating: using an out-group stereotype to explain a complex system failure | Treated as rhetoric; no serious empirical support located |

### Supplementary Source Review (Pass 2; user-provided list)

| Source | Notes (supports/disclaims) | Claim impact |
|---|---|---|
| Ars Technica (2022-08-15) | Summarizes Reuters interviews/policy-doc review; explicitly names Microsoft among firms discussed for caste policy coverage | Supports LABOR-2026-017; LABOR-2026-019 |
| WIRED (2022-03-01) | Longform reporting; discusses Cisco case, alleged harms, and post-case complaint volume to Equality Labs | Supports LABOR-2026-019; context for LABOR-2026-016 |
| The New Yorker (2022-08-11) | Q&A about Google controversy; references Cisco case and reported Equality Labs complaint volume | Supports LABOR-2026-019 |
| AP News (2023-04-10) | Litigation-status reporting; documents policy debate and downstream actions (Seattle ordinance context) | Supports LABOR-2026-016; LABOR-2026-019 |
| Quartz (2022-08-16) | Summarizes Reuters policy coverage; includes Microsoft among firms not explicitly prohibiting caste; notes “ancestry/national origin” framing | Supports LABOR-2026-017; context for LABOR-2026-019 |
| VICE (2020-08-05) | Reports Equality Labs complaint counts including Microsoft and other firms; includes first-person accounts | Supports LABOR-2026-017; LABOR-2026-019 |
| NBC News (2022-06-23) | Reporting/interviews; frames post-Cisco tech-sector discussion and includes additional accounts | Supports LABOR-2026-019; context for LABOR-2026-016 |
| NPR (2020-10-12) | Morning Edition segment + transcript; quotes Equality Labs listing Microsoft among companies in reported complaints; discusses policy gaps | Supports LABOR-2026-017; LABOR-2026-019; context for LABOR-2026-016 |
| TechEquity (2023-06-02) | Capture failed in this environment (“Just a moment…” / anti-bot) | Not used |
| WomenWhoCode blog | Capture failed in this environment (HTTP 403) | Not used |
| OpenTools.ai item | Capture yielded a generic daily feed; specific linked article content not accessible/confirmable in this pass | Not used |

### Corrections & Updates

| Item | URL | Published | Corrected/Updated | What Changed | Impacted Claim IDs | Action Taken |
|---|---|---:|---:|---|---|---|
| Thread date extraction error | https://threadreaderapp.com/thread/2020302908919804019.html | 2026-02-08 | 2026-02-09 | A generic HTML extractor misread the date (picked up an unrelated “More from…” block). Correct date derived from the thread’s `data-time` UNIX timestamp | N/A | Recorded the correct date in Metadata; flagged as capture pitfall |
| Embedded X links inaccessible | https://x.com/ethannestor/status/2008032739552051359 (and others) | 2026-02-08 | 2026-02-09 | X returned HTTP 403 in this environment; embedded evidence could not be reviewed | LABOR-2026-018 | Treated linked examples as “not reviewed”; downgraded confidence |
| Added corroborating mainstream reporting (Pass 2) | (see Supplementary Source Review) | 2020–2023 | 2026-02-09 | Reviewed additional major-outlet reporting provided by the user; updated the Microsoft allegation claim to the better-supported “reported complaints/allegations include Microsoft” framing | LABOR-2026-017; LABOR-2026-019 | Updated claim framing and verification notes; added provenance links in DB |
| Additional capture failures (Pass 2) | https://techequity.us/2023/06/02/employers-already-know-caste-discrimination-exists-but-only-a-law-can-stop-them-from-ignoring-it/ ; https://womenwhocode.com/blog/making-hidden-inequality-visible-caste-discrimination-in-tech/ | 2023-06-02 ; ? | 2026-02-09 | Cloudflare/anti-bot and 403 prevented extraction in this environment | N/A | Not used as evidence in this pass |

### Internal Tensions / Self-Contradictions

| Tension | Parts in Conflict | Implication |
|---|---|---|
| Broad documentation vs specific “Python vs C++” claim | Major-outlet reporting supports that caste-discrimination allegations exist in tech (and include Microsoft), but the thread’s specific programming-language assignment allegation remains uncorroborated beyond a low-rigor outlet | Don’t let true general context validate an unverified specific claim; treat the “Python vs C++/janitorial” detail as unconfirmed |

### Persuasion Techniques

| Technique | Example (paraphrased) | Effect on Reader |
|---|---|---|
| Scapegoating / stereotyping | “Windows is awful… because… Indians” | Reframes a complex technical topic into an ethnic blame narrative |
| Sarcasm / ridicule | Skull emojis; punchline-style “Python vs C++” | Signals the conclusion as socially “obvious” without evidence |
| Citation laundering | “Just look up…” without citing sources | Outsources verification to the reader while retaining rhetorical force |

### Unstated Assumptions

| Assumption | Claim ID | Critical? | Problematic? |
|---|---|---:|---:|
| Workforce nationality/ethnicity is a meaningful causal driver of Windows quality | SOC-2026-010 | Y | Y |
| Reported complaints/allegations involving Microsoft imply a broad Microsoft-wide pattern (not isolated or unverified reports) | LABOR-2026-017 | Y | Y |
| “Python vs C++” is a stable caste-linked status hierarchy in workplaces | LABOR-2026-018 | Y | Y |

### Evidence Assessment
- **Best supported**: that caste-discrimination allegations have reached major legal action in US tech (Cisco), and that credible journalism documents allegations/complaints and first-person accounts across big tech (including Microsoft) (E2/E4).
- **Weakly supported**: the thread’s specific “Python vs C++/janitorial duties” allegation (single low-rigor outlet; no docket or mainstream corroboration found in this pass).
- **Unsupported**: the thread’s ethnic scapegoat explanation for Windows quality (rhetorical).

### Credence Assessment
- **Overall Credence**: 0.25  
- **Reasoning**: The thread’s rhetorical framing is high-bias and low-citation. The broader “caste discrimination allegations exist in tech (including Microsoft being named in reported complaints)” is well documented, but the specific programming-language assignment claim remains uncorroborated in this pass.

## Stage 3: Dialectical Analysis

### Steelmanned Argument
Caste discrimination is a well-documented social stratification system in South Asia, and it can persist within diaspora communities. In workplaces with substantial South Asian representation, caste identity may inform informal networks, mentorship, and bias. Even a small number of credible allegations should motivate companies to investigate, establish clear anti-discrimination policies (including caste where relevant), and create safe reporting channels.

### Strongest Counterarguments
1. **Racist frame invalidates inference**: even if caste discrimination exists, it does not justify attributing Windows quality to “Indians.” The causal link is unsupported and prejudicial.
2. **Unverified specifics**: the “Python for higher castes / C++ for lower castes” framing appears to rest on an uncorroborated story; without primary documentation it should be treated as rumor/meme, not a fact claim.
3. **Category error**: workplace discrimination (a social/HR problem) and software quality (a technical/organizational product problem) require different evidence and causal analysis; the thread conflates them for rhetorical impact.

### Supporting Theories

| Theory/Framework | Source ID | How It Supports |
|---|---|---|
| Discrimination as networked advantage | miyaspokeofthis-2026-windows-caste-thread | Informal in-group favoritism can shape hiring, promotions, and work assignment even without formal policy |

### Contradicting Theories

| Theory/Framework | Source ID | Point of Conflict |
|---|---|---|
| Complex-systems product quality | miyaspokeofthis-2026-windows-caste-thread | Software quality is typically better explained by architecture, incentives, and process than by workforce nationality stereotypes |

### Synthesis Notes
Treat this thread as a low-rigor, high-bias artifact that mixes (1) a well-documented broader phenomenon (caste discrimination allegations in tech; Cisco case; and reporting that includes Microsoft in complaint/policy discussions) with (2) an unverified specific “Python vs C++/janitorial duties” claim and (3) an explicitly scapegoating ethnic explanation for product quality. For decision-making, separate these layers and insist on primary documentation for the specific Microsoft assignment allegation.

### Claims to Cross-Reference
- LABOR-2026-016 with other jurisdictions’ caste-discrimination cases/policies (Seattle ordinance; other corporate policies).
- LABOR-2026-017 with policy-language comparisons (explicit “caste” vs “ancestry/national origin” coverage) and independently documented complaint channels.
- LABOR-2026-018 with primary documents if any complaint/docket becomes discoverable.

### Claim Summary

| ID | Type | Domain | Evidence | Credence | Claim |
|---|---|---|---|---:|---|
| SOC-2026-010 | [S] | SOC | E6 | 0.05 | Windows is “awful” because Microsoft has “so many Indians” (ethnic scapegoat causal claim) |
| LABOR-2026-016 | [F] | LABOR | E2 | 0.85 | Caste discrimination in tech/IT has been credibly alleged and has been the subject of major legal actions (e.g., Cisco) |
| LABOR-2026-017 | [F] | LABOR | E4 | 0.75 | Major outlets have reported caste-discrimination allegations/complaints involving Microsoft in the U.S. tech sector (often via advocacy-group complaint/survey reporting and policy-coverage discussions) |
| LABOR-2026-018 | [F] | LABOR | E6 | 0.10 | Caste status determines assignment to “Python” vs “C++/Java/janitorial duties” at Microsoft (as described in the thread) |
| SOC-2026-011 | [F] | SOC | E5 | 0.40 | The author received many threatening DMs from Indians denying caste discrimination |
| LABOR-2026-019 | [F] | LABOR | E4 | 0.75 | Searching “caste in IT” yields many reports and first-person accounts from Indians alleging caste discrimination in tech workplaces |

### Claims to Register

```yaml
claims:
  - id: "SOC-2026-010"
    text: >-
      Microsoft’s Windows operating system is “awful” because Microsoft employs “so many Indians”
      (i.e., workforce nationality/ethnicity causally explains product quality).
    type: "[S]"
    domain: "SOC"
    evidence_level: "E6"
    credence: 0.05
    source_ids: ["miyaspokeofthis-2026-windows-caste-thread"]
    operationalization: >-
      Define measurable “Windows quality” outcomes and test whether workforce ethnicity/nationality composition
      predicts them after controlling for architecture, process, incentives, and organizational complexity.
    assumptions:
      - Workforce ethnicity/nationality is a meaningful causal driver of software quality.
    falsifiers:
      - Empirical evidence shows no relationship after controlling for confounders; or shows opposite direction.

  - id: "LABOR-2026-016"
    text: >-
      Caste discrimination in tech/IT workplaces has been credibly alleged and has been the subject of major
      legal actions in the United States (e.g., California DFEH/CRD’s lawsuit against Cisco alleging caste-based
      discrimination).
    type: "[F]"
    domain: "LABOR"
    evidence_level: "E2"
    credence: 0.85
    source_ids: ["miyaspokeofthis-2026-windows-caste-thread"]
    operationalization: >-
      Verify via official filings/press releases and court dockets that caste-discrimination allegations were
      formally brought in a major tech workplace case.
    assumptions:
      - Official public records accurately describe the existence of the case and its caste-discrimination theory.
    falsifiers:
      - Authoritative legal records show no such case was filed or that caste was not at issue.

  - id: "LABOR-2026-017"
    text: >-
      Major outlets have reported caste-discrimination allegations/complaints involving Microsoft in the U.S. tech
      sector (often via advocacy-group complaint/survey reporting and policy-coverage discussions).
    type: "[F]"
    domain: "LABOR"
    evidence_level: "E4"
    credence: 0.75
    source_ids: ["miyaspokeofthis-2026-windows-caste-thread"]
    operationalization: >-
      Verify via multiple major-outlet reports that Microsoft is explicitly named in reported caste-discrimination
      complaint/survey claims and/or in coverage of how large tech firms address caste in workplace policy.
    assumptions:
      - Major outlets accurately quote or summarize the complaint/survey/policy reporting they rely on.
    falsifiers:
      - Reputable corrections/retractions indicate Microsoft was not included in the reported complaint/survey lists.

  - id: "LABOR-2026-018"
    text: >-
      At Microsoft (as described in the thread), caste status determines assignment to “Python” projects versus
      being relegated to “C++/Java” work or even janitorial duties.
    type: "[F]"
    domain: "LABOR"
    evidence_level: "E6"
    credence: 0.10
    source_ids: ["miyaspokeofthis-2026-windows-caste-thread"]
    operationalization: >-
      Confirm via a verified complaint/court record, HR investigation, or independent reporting with named sources
      that such caste-linked language assignment occurred.
    assumptions:
      - Programming-language assignment is used as a caste-status marker in the alleged environment.
    falsifiers:
      - Verified records show no such claims were made in any complaint; or show the assignment claims were false.

  - id: "SOC-2026-011"
    text: >-
      The author of the thread received many threatening direct messages from Indians denying the existence of
      caste-based discrimination.
    type: "[F]"
    domain: "SOC"
    evidence_level: "E5"
    credence: 0.40
    source_ids: ["miyaspokeofthis-2026-windows-caste-thread"]
    operationalization: >-
      Audit the author’s DM inbox (or screenshots with verifiable metadata) for a high volume of threatening
      messages plausibly connected to the post.
    assumptions:
      - The author’s self-report is broadly accurate.
    falsifiers:
      - Verified account data shows no such influx occurred.

  - id: "LABOR-2026-019"
    text: >-
      In recent years, there have been many reports and first-person accounts from Indians alleging caste
      discrimination in tech/IT workplaces.
    type: "[F]"
    domain: "LABOR"
    evidence_level: "E4"
    credence: 0.75
    source_ids: ["miyaspokeofthis-2026-windows-caste-thread"]
    operationalization: >-
      Compile a bibliography of credible journalism, policy reports, and documented cases featuring first-person
      accounts; assess volume, independence, and representativeness.
    assumptions:
      - Available reporting reflects at least some genuine experiences rather than systematic fabrication.
    falsifiers:
      - A systematic review finds reports are rare, non-independent, or largely debunked.
```

---

**Analysis Date**: 2026-02-09  
**Analyst**: gpt-5.2  
**Credence in Analysis**: 0.70

**Credence Reasoning**:
- Thread content and thread date are directly captured from Thread Reader HTML.
- External verification is strong for the Cisco case and for the existence of broader reporting, but weak for Microsoft-specific allegations due to lack of corroboration and inaccessible embedded X links.

## Analysis Log

| Pass | Date | Tool | Model | Duration | Tokens | Cost | Notes |
|---|---|---|---|---:|---:|---:|---|
| 1 | 2026-02-09 08:13 | codex | gpt-5.2 | 19m06s | 6,679,128 | ? | Initial 3-stage analysis + extracted claims; registered source/claims; added minimal provenance for high-credence claims. |
| 2 | 2026-02-09 13:46 | codex | gpt-5.2 | 15m04s | 7,727,271 | ? | Pass 2: incorporated user-provided sources; updated LABOR-2026-017 framing; added provenance links. |

### Revision Notes

**Pass 2**:
- Reviewed additional major-outlet reporting provided by the user (Ars, VICE, NPR, NBC, AP, The New Yorker, Quartz, WIRED).
- Reframed `LABOR-2026-017` from a specific “Hyderabad case” claim to the better-supported “reported allegations/complaints include Microsoft” claim; added DB evidence links + reasoning trail.
- Added a supplementary source review table; kept the specific “Python vs C++/janitorial duties” allegation as uncorroborated beyond a low-rigor outlet.
