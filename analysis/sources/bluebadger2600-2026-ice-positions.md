# Source Analysis: “Positions ICE has taken” (BlueBadger2600 on X)

> **Claim types**: `[F]` fact, `[T]` theory, `[H]` hypothesis, `[P]` prediction, `[A]` assumption, `[C]` counterfactual, `[S]` speculation, `[X]` contradiction  
> **Evidence**: **E1** systematic review/meta-analysis; **E2** peer-reviewed/official stats/law; **E3** expert consensus/preprint; **E4** credible journalism/official memo; **E5** opinion/anecdote; **E6** unsupported/speculative

## Metadata

| Field | Value |
|---|---|
| **Source ID** | `bluebadger2600-2026-ice-positions` |
| **Title** | X post: “Positions ICE has taken” |
| **Author(s)** | @BlueBadger2600 |
| **Date** | 2026-01-24 |
| **Type** | SOCIAL |
| **URL** | https://x.com/BlueBadger2600/status/2015086695566451161 |
| **Reliability** | 0.40 |
| **Rigor Level** | [REVIEWED] |
| **Bias Notes** | Highly compressed, adversarial framing; mixes legal-technical assertions with worst-case rhetorical extrapolation. Some items are checkable against statutes/regulations and reported internal DHS/ICE memos; others are broad generalizations. |

**Primary capture**: `reference/primary/social/bluebadger2600-2026-ice-positions.md`  
**Claims YAML**: [`analysis/sources/bluebadger2600-2026-ice-positions.yaml`](bluebadger2600-2026-ice-positions.yaml)

## Stage 1: Descriptive Analysis

### Core Thesis
The post argues that ICE is asserting or exercising powers that effectively bypass warrants, due process, and meaningful legal remedies, creating conditions conducive to authoritarian governance (“totalitarianism”).

### Summary (Neutral)
The post presents a list of asserted “positions” attributed to ICE. These positions are framed as a package of expansive state powers: entry into homes without judicial warrants, compulsory document-carrying with biometric “scanner” supremacy, broad detention powers (including children and allegedly regardless of legal status), indefinite detention without counsel, limited access to courts, deportation to dangerous “third countries,” inability to correct mistakes, and lethal force justified by labeling interference “terrorism.”

The concluding question (“How is this not a recipe for totalitarianism?”) treats the list as collectively constituting an authoritarian toolkit, rather than as isolated legal claims.

### Key Claims

| # | Claim | Claim ID | Type | Domain | Evidence | Credence | Verified? | Falsifiable By |
|---|-------|----------|------|--------|----------|----------:|-----------|----------------|
| 1 | ICE can forcibly enter a residence to make an immigration arrest without a judge-signed warrant (e.g., relying only on an administrative warrant) | GOV-2026-033 | [F] | GOV | E4 | 0.90 | ? | Publication of the referenced ICE guidance showing it does not authorize forced entry without judicial warrant; or credible reporting that the memo was forged/mischaracterized |
| 2 | Federal law requires noncitizens (18+) to carry their registration documents (“papers”) at all times | GOV-2026-034 | [F] | GOV | E2 | 0.98 | 8 U.S.C. § 1304(e) | Statutory change or authoritative legal interpretation that this does not impose an “at all times” possession requirement |
| 3 | In encounters, ICE can disregard paper documents and rely primarily on biometrics (“scanner”) to determine identity/status | GOV-2026-035 | [H] | GOV | E4 | 0.75 | ? | Policy/oversight evidence that ICE reliably accepts documentary proof in the field and does not use biometrics as the primary determinant |
| 4 | ICE can detain people broadly across contexts, including children, and errors can result in detention of citizens | GOV-2026-036 | [H] | GOV | E4 | 0.80 | ? | Evidence that federal immigration enforcement does not detain minors in practice and that citizen misidentification/detention is vanishingly rare in comparable operations |
| 5 | ICE can detain people indefinitely with no access to a lawyer | GOV-2026-037 | [H] | GOV | E6 | 0.20 | ? | Evidence that immigration detainees have guaranteed government-appointed counsel and that indefinite detention is legally permitted without meaningful review |
| 6 | People targeted by ICE generally have no meaningful “day in court” / due-process hearing | GOV-2026-038 | [H] | GOV | E4 | 0.55 | ? | Evidence that expedited processes are rare and that most removals involve meaningful adversarial hearings with robust judicial review |
| 7 | ICE can deport people to “third countries” on short notice, potentially exposing them to persecution or harsh detention conditions | GOV-2026-039 | [F] | GOV | E2 | 0.85 | ? | Evidence that third-country removals are tightly constrained in practice with robust notice/process requirements and are not occurring as described in recent litigation/reporting |
| 8 | If ICE makes a serious mistake (wrongful detention/deportation), it generally cannot or will not bring the person back | GOV-2026-040 | [H] | GOV | E4 | 0.55 | ? | Evidence that ICE routinely and promptly facilitates return after wrongful removals across categories (including third-country/offshored-detention contexts), beyond narrow policy/court-ordered cases |
| 9 | If you interfere with ICE actions, ICE can shoot you and justify it by labeling you a “terrorist” | GOV-2026-041 | [H] | GOV | E6 | 0.15 | ? | Evidence of an ICE policy authorizing lethal force for mere “interference,” absent imminent threat, and/or reliable cases where “terrorist” labeling is used to justify otherwise unlawful shootings |
| 10 | DHS/ICE leadership and allied messaging have repeatedly labeled people involved in immigration-enforcement incidents and interference/observation (e.g., filming) as “domestic terrorists”/“terrorists,” often immediately after events | GOV-2026-042 | [F] | GOV | E4 | 0.75 | ? | Evidence that “domestic terrorist” labeling is rare and not used in connection with immigration-enforcement incidents or documented interference/observation |

### Argument Structure

```
(1) Warrantless home entry + (2) compulsory papers + (3) biometric supremacy
        ↓ enables
(4) broad detention power (incl. mistaken/collateral detentions)
        ↓ reinforced by
(5) weak access to counsel + (6) weak access to courts
        ↓ amplified by
(7) third-country removals + (8) poor correction of mistakes
        ↓ enforced by
(9) lethal force framed as “counter-terror” against interference
        ↓
Conclusion: a practical “authoritarian toolkit” → “recipe for totalitarianism”
```

### Theoretical Lineage
- **Constitutional criminal-procedure norms**: Fourth Amendment warrant requirement, home as protected space; due process.
- **Carceral state / administrative state critique**: low-visibility processes, limited adversarial checks.
- **Authoritarianism risk framing**: concentration of coercive power + weak accountability increases abuse risk.

### Scope & Limitations
- The post does not cite sources; several bullets are ambiguous about whether they mean *legal authority*, *agency position in memos/litigation*, or *observed practice*.
- “ICE” is sometimes used loosely in public discourse to refer to broader DHS immigration enforcement (ICE + CBP); the requested Minnesota examples involve both.

## Stage 2: Evaluative Analysis

### Internal Coherence
As a rhetorical package, the list is internally coherent: if each bullet were literally true as a general rule, it would describe a coercive apparatus with weak judicial constraint.

The largest weakness is **overgeneralization**: some bullets collapse (a) narrow statutory authorities; (b) contested internal memos; and (c) on-the-ground incidents (including alleged misconduct) into sweeping claims (“anywhere,” “indefinitely,” “no right”).

### Key Factual Claims Verified

| Claim (paraphrased) | Crux? | Source Says | Actual | External Source | Status |
|---------------------|-------|-------------|--------|-----------------|--------|
| ICE can enter homes without a judge’s warrant | **Y** | “enter your home without a warrant” | Credible reporting describes an internal ICE memo claiming authority to forcibly enter homes using an administrative (non-judicial) warrant to arrest people with final removal orders; separate reporting describes a federal judge’s ruling that a warrantless home entry violated the Fourth Amendment (without adjudicating the memo itself). Overall: asserted “position” is well-supported; lawfulness is contested | https://www.pbs.org/newshour/nation/immigration-officers-claim-sweeping-power-to-enter-homes-without-a-judges-warrant-memo-says ; https://www.pbs.org/newshour/nation/not-opening-the-door-to-ice-may-no-longer-stop-officers ; https://www.wired.com/story/us-judge-rules-ice-raids-require-judicial-warrants-contradicting-secret-ice-memo/ ; https://abcnews.go.com/US/ice-memo-allows-agents-enter-homes-judicial-warrant/story?id=129436766 ; contrast: 8 CFR 287.8(f)(2) https://www.law.cornell.edu/cfr/text/8/287.8 | ok (position claimed), ? (lawfulness) |
| Noncitizens must carry “papers” at all times | N | “must carry your papers at all times” | Federal law requires “every alien, eighteen years of age and over” to “at all times carry” registration/receipt card. A DHS Federal Register notice summarizes noncompliance as a misdemeanor punishable by up to 30 days and a fine up to $5,000 (via general federal fine provisions). This duty does not apply to U.S. citizens and does not itself create a general “street check” authority absent other legal grounds | https://www.law.cornell.edu/uscode/text/8/1304 ; https://www.govinfo.gov/content/pkg/FR-2025-03-12/pdf/2025-03944.pdf | ok (scope-limited) |
| ICE can ignore documents and only biometrics matter | N | “ignore them… only our scanner matters” | A DHS privacy threshold analysis for the Mobile Fortify field app states ICE does not provide an opportunity to decline/consent to biometric/photo collection and that new photographs/fingerprints are retained in ATS for 15 years (including U.S. citizens/LPRs). This supports “biometrics matter” as a real system in some encounters. Reporting also describes specific incidents where agents allegedly refused to review ID, but a universal “only biometrics matter” rule remains unverified (practice appears variable) | https://s3.documentcloud.org/documents/26209262/mobile-fortify-pta.pdf ; https://www.pbs.org/newshour/nation/a-u-s-citizen-says-ice-forced-open-the-door-to-his-minnesota-home-and-removed-him-in-his-underwear-after-a-warrantless-search ; https://www.usatoday.com/story/news/nation/2026/01/20/immigration-agents-minnesota-police-officer/88268058007/ | ok (biometrics program), ? (universal rule) |
| ICE can detain people broadly, regardless of age/status | **Y** | “detain you anywhere… no matter… age… status” | INA grants immigration officers authority to interrogate people believed to be aliens and to arrest certain noncitizens without a warrant (with conditions), and DHS regulations allow questioning in public-access areas without a warrant; but the claim is overstated as a universal rule (citizens cannot lawfully be detained *as aliens*, though errors and alleged misconduct occur). GAO reports ICE arrested/detained/removed some “potential U.S. citizens” (FY2015–Q2 FY2020) and issued detainers for “potential U.S. citizens,” indicating misidentification/enforcement errors occur. Minnesota reporting also describes detention of very young children during operations | 8 U.S.C. § 1357 https://www.law.cornell.edu/uscode/text/8/1357 ; 8 CFR 287.8(f)(4) https://www.law.cornell.edu/cfr/text/8/287.8 ; GAO-21-487 https://www.gao.gov/assets/gao-21-487.pdf ; https://www.theguardian.com/us-news/2026/jan/23/us-immigration-two-year-old-minnesota-girl ; incidents discussed below | ? |
| ICE can detain people indefinitely with no lawyer access | **Y** | “indefinitely… no access to a lawyer” | People in removal proceedings have a statutory privilege to counsel (at no government expense). Indefinite post-removal-order detention is limited by Supreme Court interpretation (Zadvydas), though prolonged detention without periodic bond hearings can occur under statutes (Jennings) and access to counsel can be impeded in practice | 8 U.S.C. § 1362 https://www.law.cornell.edu/uscode/text/8/1362 ; Zadvydas v. Davis (2001) https://tile.loc.gov/storage-services/service/ll/usrep/usrep533/usrep533678/usrep533678.pdf ; Jennings v. Rodriguez (2018) https://www.law.cornell.edu/supremecourt/text/15-1204 | x (as stated), ok (access barriers exist) |
| People have basically no right to a “day in court” | N | “basically no right… day in court” | Many people in removal proceedings receive immigration court hearings, but expedited removal is designed to bypass full hearings for certain categories; Supreme Court upheld limits on habeas review for expedited removal (Thuraissigiam). Separately, AP reports ICE leadership directed broader use of a detention authority that makes many people in removal proceedings ineligible for immigration-judge bond hearings, which can reduce practical ability to pursue claims while free (without eliminating all hearings) | 8 U.S.C. § 1225 (expedited removal) https://www.law.cornell.edu/uscode/text/8/1225 ; DHS v. Thuraissigiam (2020) https://www.law.cornell.edu/supremecourt/text/19-161 ; https://apnews.com/article/immigration-detention-ice-trump-e1c2322c3f88c1f7d7e83c8c42109cb6 | ? (depends on category) |
| ICE can “send you to a third world prison” | N | “send you to a third world prison” | Reporting and litigation describe “third-country” removals (removal to countries other than a person’s origin), sometimes with very short notice; while not a criminal “prison sentence,” removals can expose people to severe conditions (including foreign custody) | https://www.nbcnews.com/news/us-news/ice-may-deport-migrants-third-countries-assurances-wont-tortured-memo-rcna218990 ; https://www.supremecourt.gov/opinions/24pdf/24a1153_l5gm.pdf ; https://apnews.com/article/trump-migrants-el-salvador-prison-3c46db296c219c7b3a701474eaea5184 | ok (third-country removals reported), ? (“prison” framing is rhetorical) |
| ICE can’t bring you back if it made a mistake | N | “can’t bring you back” | ICE has a written policy (2012) to facilitate return in some narrow categories, so “can’t” is not categorically true. However, recent reporting and litigation around third-country removals/offshored detention describe the administration arguing it is powerless to return people once moved abroad and resisting return even in acknowledged-error cases—though at least one such case (Abrego Garcia) ultimately resulted in return to the U.S. | ICE Directive 11061.1 (2012) https://www.ice.gov/doclib/foia/dro_policy_memos/11061.1_current_policy_facilitating_return.pdf ; https://apnews.com/article/trump-migrants-el-salvador-prison-3c46db296c219c7b3a701474eaea5184 ; https://www.supremecourt.gov/opinions/24pdf/24a1153_l5gm.pdf | x (as absolute), ? (return not guaranteed; often contested) |
| ICE can shoot you for “interference” because you are a “terrorist” | N | “shoot… because… terrorist” | DHS/ICE deadly-force authority is limited to situations of “imminent danger of death or serious physical injury,” not mere interference. However, there is substantial reporting that senior officials and DHS/ICE messaging have used “domestic terrorism”/“terrorist” labels quickly after shootings and in response to protest/observation activity. That rhetoric may shape public justification, but it does not itself expand legal authority for lethal force | 8 CFR 287.8(a)(2) https://www.law.cornell.edu/cfr/text/8/287.8 ; https://www.cbsnews.com/minnesota/news/what-is-domestic-terrorism-renee-good-ice/ ; https://www.foxnews.com/politics/noem-says-minneapolis-suspect-committed-domestic-terrorism-accuses-walz-frey-inciting-violence ; https://www.wired.com/story/the-instant-smear-campaign-against-border-patrol-shooting-victim-alex-pretti/ ; https://reason.com/2026/01/23/ice-tells-legal-observer-we-have-a-nice-little-database-and-now-youre-considered-a-domestic-terrorist/ ; https://reason.com/2025/12/26/justice-department-says-filming-immigration-raids-is-domestic-terrorism/ | x (lethal-force claim), ok (labeling pattern) |
| DHS/ICE messaging uses “domestic terrorism”/“terrorist” labels in connection with immigration enforcement incidents and interference/observation | N | implied by “you are a terrorist” framing | Multiple outlets report top DHS officials describing the Renee Good and Alex Pretti incidents in “domestic terrorism” terms and/or labeling the victim/suspect a “terrorist,” and a separate incident where an ICE officer told a legal observer they were considered a “domestic terrorist” | https://www.cbsnews.com/minnesota/news/what-is-domestic-terrorism-renee-good-ice/ ; https://www.foxnews.com/politics/noem-says-minneapolis-suspect-committed-domestic-terrorism-accuses-walz-frey-inciting-violence ; https://www.wired.com/story/the-instant-smear-campaign-against-border-patrol-shooting-victim-alex-pretti/ ; https://reason.com/2026/01/23/ice-tells-legal-observer-we-have-a-nice-little-database-and-now-youre-considered-a-domestic-terrorist/ | ok |

### Additional Context Checks (Requested)

| Topic | What Was Claimed / Requested | What We Found | Source(s) | Status |
|---|---|---|---|---|
| Renee (Renée) Good shooting (MN) | “recent ICE shooting of Rene Good” | Multiple outlets report Renee Nicole Good (37) was fatally shot by an ICE officer in Minneapolis during enforcement operations; DHS/ICE claimed she attempted to run over officers; state/local officials disputed aspects; Noem publicly described it as “domestic terrorism,” and later coverage notes the label is contested/premature | https://abcnews.go.com/US/ice-related-shooting-occurred-minnesota-governor/story?id=128984401 ; https://www.cbsnews.com/news/renee-good-gunshot-wounds-ice-agent-minneapolis-fire-department-report/ ; https://www.cbsnews.com/minnesota/news/what-is-domestic-terrorism-renee-good-ice/ ; https://www.newsweek.com/noem-ice-shooting-domestic-terrorism-minneapolis-11324489 | ok (event), ? (justification) |
| Alex Pretti shooting (MN) | “recent ICE shooting of Alex Pretti” | Multiple outlets report Alex Jeffrey Pretti (37) was shot and killed by a U.S. Border Patrol officer in Minneapolis; Border Patrol is CBP (DHS) not ICE. DHS officials claimed Pretti approached with a handgun; multiple video analyses/reporting describe agents pepper-spraying and restraining him and suggest a gun was removed by an agent shortly before the shooting, disputing the “approached with gun” framing | https://apnews.com/article/immigration-enforcement-minnesota-protester-alex-pretti-15ade7de6e19cb0291734e85dac763dc ; https://abcnews.go.com/US/alex-pretti-icu-nurse-killed-federal-agent-minneapolis/story?id=129525591 ; https://time.com/7357547/minneapolis-shooting-ice-agent/ ; https://edition.cnn.com/2026/01/24/us/invs-videos-show-federal-officer-recovered-gun ; https://www.wired.com/story/the-instant-smear-campaign-against-border-patrol-shooting-victim-alex-pretti/ | ok (event), ? (official narrative) |
| National Guard deployments (MN) | “deployments of national guard” | Multiple outlets report Minnesota officials activated/mobilized the National Guard to support local law enforcement amid protests and unrest following federal immigration enforcement actions and shootings | https://www.fox9.com/news/minneapolis-shooting-national-guard-called-assist-after-latest-incident-federal-agents ; https://nypost.com/2026/01/24/us-news/minnesota-gov-tim-walz-activates-state-national-guard-blasts-federal-government-after-shooting/ ; https://www.minnpost.com/metro/2026/01/federal-officers-shoot-and-kill-man-in-minneapolis/ | ok |
| Citizen street stops / paperwork demands | “people being taken off the street” (and “carry papers”) | USA Today reports local police chiefs alleging U.S. citizens (including off-duty officers) were stopped, had “paperwork” demanded, and were prevented from recording; DHS said it could find no record absent names | https://www.usatoday.com/story/news/nation/2026/01/20/immigration-agents-minnesota-police-officer/88268058007/ | ? |
| Detention of 5-year-old | “detentions of 5yo etc” | ABC reports a 5-year-old (Liam Conejo Ramos) was taken into custody with his father by ICE agents in Minnesota; school officials alleged ICE used the child to prompt door opening; DHS disputed details | https://abcnews.go.com/US/5-year-asylum-seeker-detained-ice-expands-enforcement/story?id=129451987 | ok (custody), ? (specific allegations) |
| Detention of 2-year-old (MN) | “detentions of 5yo etc” | The Guardian reports federal agents detained a 2-year-old and her father in Minneapolis and transported them to Texas despite a federal judge ordering the child’s release the same day; the child was later returned to Minnesota and released to her mother, while the father remained detained | https://www.theguardian.com/us-news/2026/jan/23/us-immigration-two-year-old-minnesota-girl | ok (reported), ? (details pending official records) |
| Warrantless home entry disputes / rulings | “enter your home without a warrant” | PBS/AP reporting describes an internal ICE memo claiming authority to forcibly enter homes without judge-signed warrants; Wired reports a federal judge in Minnesota ruled a warrantless forced entry violated the Fourth Amendment in a specific case (without adjudicating the memo’s legality) | https://www.pbs.org/newshour/nation/not-opening-the-door-to-ice-may-no-longer-stop-officers ; https://www.wired.com/story/us-judge-rules-ice-raids-require-judicial-warrants-contradicting-secret-ice-memo/ | ok (position + ruling reported), ? (ultimate legal status) |
| “Taken off the street” (protest detentions) | “people being taken off the street” | CNN reporting describes protesters detained by federal law enforcement near a federal building during Minneapolis protests; contemporaneous local reporting also describes clashes and arrests/detentions amid protests | https://www.cnn.com/2026/01/17/us/ice-shooting-minneapolis-protests-renee-good-hnk/index.html ; https://www.minnpost.com/metro/2026/01/federal-officers-shoot-and-kill-man-in-minneapolis/ | ok (detentions occurred), ? (basis) |
| Vance “unlimited immunity” statements | “statements by Vance on unlimited immunity for ICE agents” | CNN reports Vice President JD Vance claimed an ICE officer who shot Renee Good was “protected by absolute immunity,” drawing legal pushback; “absolute immunity” ≈ “unlimited immunity” in common phrasing, but the claim is disputed by experts | https://www.cnn.com/2026/01/08/politics/ice-immunity-jd-vance-minneapolis/index.html | ok (said), x/? (legal accuracy) |

### Supplementary Source Review (Provided List; Pass 2)

| Source | Notes (supports/disclaims) | Claim impact |
|---|---|---|
| USA Today: “ICE agents drew guns on off-duty officer…”[^S01] | Reports local police chiefs alleging U.S. citizens (incl. off-duty police) were stopped and had “paperwork” demanded; DHS said it could find no record without names | Supports GOV-2026-036; complicates GOV-2026-035 |
| Democracy Docket: Bondi letter / voter rolls[^S02] | Reports AG Bondi tying federal demands (incl. voter-roll access) to unrest after the Minneapolis shooting | Context for GOV-2026-036 (expanded enforcement posture) |
| NY Post: Walz activates National Guard[^S03] | Reports Guard activation; repeats federal characterization of Pretti as “armed” and “intervening” | Context for deployments; not treated as high-rigor fact source |
| CNN Politics: “Another killing… political nightmare”[^S04] | Notes administration has claimed power to enter homes without judge’s warrant; discusses DHS/Noem messaging after shootings | Supports GOV-2026-033 and GOV-2026-042 |
| Reuters (provided)[^S05] | Not accessible in this environment (Reuters blocks non-JS access); not reviewed | Not used |
| WIRED: smear campaign vs Alex Pretti[^S06] | Reports rapid “terrorist” labeling/smear campaign and challenges official narrative vs video evidence | Supports GOV-2026-042; informs GOV-2026-041 rhetoric component |
| The Guardian: Jacob Frey full statement[^S07] | Primary statement text from the Minneapolis mayor after Pretti shooting | Context (political response) |
| FOX 9: Bondi urges Walz support ICE[^S08] | Reports Bondi letter and “path for ICE to leave”; repeats claim Pretti was armed | Context; informs disputes around event narrative |
| PBS/AP: “Not opening the door… may no longer stop officers”[^S09] | Reports internal ICE memo claiming administrative-warrant home entry; situates change against Fourth Amendment doctrine | Supports GOV-2026-033 |
| FOX 32: Johnson/Pritzker call to abolish ICE[^S10] | Political reaction; also notes the Minneapolis shooting involved Border Patrol (CBP) not ICE | Context; clarifies agency |
| In These Times: protests + Pretti[^S11] | Advocacy framing; repeats DHS claim Pretti armed and notes video + O’Hara’s permit statement | Context; informs narrative dispute |
| TIME: “Federal Agents Kill Another Person…”[^S12] | Describes bystander videos, pepper spray, and gun removal narrative; includes O’Hara gun-permit note | Supports dispute of “approached with gun” framing |
| Fox News: Noem calls Pretti incident “domestic terrorism”[^S13] | Quotes Noem labeling the Pretti incident domestic terrorism and asserting weapon/ammo details | Supports GOV-2026-042 |
| Newsweek: impeach Noem after new shooting[^S14] | Reports DHS statement and political backlash; includes video description | Context; confirms event salience |
| The Hill (ACLU tactics)[^S15] | Not accessible in this environment (blocked) | Not used |
| FOX 9: National Guard activated after Pretti[^S16] | Reports Guard activation and related local actions (TRO request, etc.) | Context for deployments |
| Axios: Walz vows state investigation into DHS “lies”[^S17] | Summarizes Walz disputing DHS account based on video; notes videos don’t appear to show brandishing | Supports dispute of official narrative |
| CNN: video analysis re gun recovery[^S18] | Video analysis suggests an agent retrieved a gun from Pretti shortly before shooting; notes Pretti not seen wielding weapon | Supports dispute of “approached with gun” framing |
| Washington Post (provided)[^S19] | Not accessible in this environment (network/HTTP errors); not reviewed | Not used |
| Beaumont Enterprise (provided)[^S20] | Not accessible in this environment (CAPTCHA) | Not used |
| Al Jazeera: federal agents shoot US citizen[^S21] | Summarizes events; includes DHS claim about handgun/resisting disarmment and Walz quote | Context; confirms competing narratives |
| The Hill (Trump defends agents)[^S22] | Not accessible in this environment (blocked) | Not used |
| The Guardian: protests after Pretti[^S23] | Describes protests across cities after Pretti killing | Context |
| AP News: Pretti killed by Border Patrol[^S24] | Reports family background; DHS statement; notes videos show phone in hand and weapon not visible | Supports competing narratives |
| ABC News (provided URL returned 404)[^S25] | The provided ABC URL appears unavailable; used ABC’s story with `id=129525591` for substantially similar reporting | Supports event details and DHS vs local dispute |
| The Times (UK)[^S26] | Partial access only (headline/lede) | Not used for substantive claims |
| MinnPost/AP: shooting + Guard[^S27] | Reports DHS statement; notes videos show phone; notes Noem remarks | Supports competing narratives |
| WIRED: judge ruling on judicial warrants[^S28] | Reports federal judge ruling a warrantless forced entry violated the Fourth Amendment in Minnesota; links to whistleblower complaint | Supports contestation of GOV-2026-033 lawfulness |
| Vox: “unchecked abuses” explainer[^S29] | Interpretive synthesis; asserts Good was called a domestic terrorist and frames crackdown as abuses | Context; some claims overlap with CBS/Newsweek reporting |
| The Guardian: two-year-old detained[^S30] | Reports court records/lawyers on toddler detention and transport despite release order | Supports GOV-2026-036 (child detention) |
| Vox podcast: Ellison interview[^S31] | Interpretive/political context; alleges federal stonewalling and victim-blaming rhetoric | Context |
| Reason: legal observer “domestic terrorist”[^S32] | Reports video where ICE officer tells a legal observer they’re considered a “domestic terrorist”; includes DHS denial of such a database | Supports GOV-2026-042 |
| The New Republic: “We’re all domestic terrorists now”[^S33] | Opinion using Noem quote and broader framing | Context; supports “labeling” pattern narrative |
| Reason: DOJ says filming raids is “domestic terrorism”[^S34] | Reports DOJ/DHS framing and ramifications for filming/recording raids; article includes a correction removing reference to a DOJ memo that did not describe “merely filming” as domestic terrorism | Weaker support for “filming alone” framing; still relevant to GOV-2026-042 (labeling/retaliation rhetoric) |
| Newsweek: Noem called Good “domestic terrorism”[^S35] | Reports Noem describing Good shooting as domestic terrorism; includes video description | Supports GOV-2026-042 (Good) |
| CBS Minnesota: “label is premature”[^S36] | Quotes Noem domestic-terrorism label; provides definitions and expert caution | Supports GOV-2026-042 (labeling occurred) while cautioning against premature application |

### Supplementary Source Review (Return / Third-Country Removals; Pass 3)

| Source | Notes (supports/disclaims) | Claim impact |
|---|---|---|
| AP: CECOT custody + “powerless to return” argument[^S37] | Reports Salvadoran officials told U.N. investigators the U.S. retains control of deported men at CECOT; notes the administration argued it is powerless to return them; describes Abrego Garcia case where the administration initially resisted but later returned him | Supports GOV-2026-039 and GOV-2026-040; informs GOV-2026-038 |
| SCOTUS emergency order/opinion (third-country removals)[^S38] | Describes (incl. in dissent) class-member removals to Libya/El Salvador/South Sudan with minimal notice; notes district court sometimes ordered “return,” and in at least one instance the government eventually facilitated it; also shows courts sometimes allowed process overseas rather than ordering return | Strong support for GOV-2026-039; informs GOV-2026-040 and GOV-2026-038 |
| AP: South Sudan flight + judge-ordered interviews[^S39] | Reports dispute over third-country removal procedures and a judge ordering new interviews either back in the U.S. or abroad | Supports GOV-2026-039; informs GOV-2026-040 (return vs overseas process) |
| Fox News: Djibouti “shipping container” custody (court filing)[^S40] | Summarizes ICE filing describing conditions and judge’s position that the government is not compelled to create the “stranded” situation | Context for GOV-2026-039 and GOV-2026-040 (government choices affect “can’t bring you back” claims) |
| American Immigration Council (advocacy synthesis)[^S41] | Claims widespread due-process failures in March 15 El Salvador removals; highlights acknowledged “administrative error” in Abrego Garcia case (with many citations) | Context; supports concern behind GOV-2026-039/040 while treated as advocacy |
| Refugee Rights / IRAP (advocacy synthesis)[^S42] | Synthesizes third-country removals and cites court opinions and reported internal guidance; useful pointer to primary sources but treated as advocacy | Context; points to evidence relevant to GOV-2026-039 |
| Brennan Center (analysis/opinion)[^S43] | Addresses legality of incarcerating U.S. citizens abroad; not directly probative of “return after wrongful removal” | Context only |
| Factually.co (fact-check)[^S44] | Not accessible in this environment (Vercel checkpoint / 429) | Not used |
| OHCHR press release (provided)[^S45] | Not accessible in this environment (Cloudflare/JS challenge) | Not used (AP quote about U.N. investigators used instead) |

### Supplementary Source Review (Transcript Reviews + Primary Docs; Pass 4)

| Source | Notes (supports/disclaims) | Claim impact |
|---|---|---|
| GAO-21-487 (citizenship investigations)[^S46] | GAO reports ICE/CBP took enforcement actions against “potential U.S. citizens” (FY2015–Q2 FY2020) and that ICE issued (and often canceled) detainers for “potential U.S. citizens,” supporting that mistaken enforcement against citizens/noncitizens can occur at non-trivial scale | Supports GOV-2026-036; informs GOV-2026-034 nuance (citizens can still be affected in practice) |
| *Kidd v. Mayorkas* order (C.D. Cal. 2024)[^S47] | Federal district court order states administrative warrants (I-200/I-205) do not authorize entry into a residence/curtilage without consent/judicial warrant, reinforcing that GOV-2026-033 is a contested *asserted authority* rather than settled lawful power | Supports contestation of GOV-2026-033 lawfulness (position vs legality distinction) |
| Federal Register: alien registration evidence (90 FR 11793; 2025-03944)[^S48] | DHS Federal Register notice explicitly summarizes 8 U.S.C. § 1304(e) as requiring registered noncitizens (18+) to carry registration documents “at all times” and describes penalties as including fines up to $5,000 (via 18 U.S.C. § 3571) and/or up to 30 days | Supports GOV-2026-034 (penalty nuance) |
| Mobile Fortify PTA (Version: Feb 2025)[^S49] | DHS privacy document says ICE does not provide opt-out/consent for biometric/photo collection; retains all new photographs/fingerprints for 15 years in ATS (including U.S. citizens/LPRs); and notes agents do not know citizenship at initial encounter | Strengthens GOV-2026-035; supports GOV-2026-036 (citizen exposure via misidentification/unknown status) |
| AP: expand detention without bond hearing (July 2025 Lyons directive)[^S50] | AP reports ICE leadership directed broader use of mandatory detention without immigration-judge bond hearings for many people in removal proceedings, tightening the practical due-process environment even where formal hearings remain | Informs GOV-2026-037/038 (practical ability to contest cases from detention) |
| ACLU press release: retaliation against recording[^S51] | ACLU alleges pattern of retaliation/harassment against people recording immigration agents; advocacy source but useful as a pointer and for documenting claims being made publicly | Supports GOV-2026-042 (observation/recording conflict) |
| The Marshall Project: Renee Good shooting coverage[^S52] | Credible reporting on the Good incident and post-incident messaging dynamics | Context for Minnesota incidents; supports GOV-2026-042 pattern framing |

### Disconfirming Evidence Search

| Claim | Counterevidence Found | Alternative Explanation | Search Notes |
|---|---|---|---|
| GOV-2026-033 (home entry) | DHS/ICE regulations and longstanding Fourth Amendment doctrine are commonly understood to require judicial warrant or consent for home entry; 8 CFR 287.8(f)(2) states warrant/consent requirement for residence site inspections | The reported memo may be a narrow theory tied to final removal orders and administrative warrants; courts may ultimately reject or constrain it, or it may apply only in limited conditions | Checked reported memo descriptions (AP/PBS; ABC) and compared with 8 CFR 287.8(f)(2) text |
| GOV-2026-037 (indefinite/no lawyer) | Statute provides privilege of counsel at no government expense; Supreme Court constrains indefinite post-removal-order detention (Zadvydas) | “No access” may reflect practical barriers (remote detention, communication limits, rapid transfers), not legal absence of counsel privilege | Consulted 8 U.S.C. § 1362 and Zadvydas; noted Jennings complexity for prolonged pre-removal detention |
| GOV-2026-038 (no day in court) | Many removals proceed via immigration judge hearings and appeals; not “basically none” for everyone | The claim may be focusing on expedited removal and limited judicial review pathways for certain categories | Reviewed expedited removal framework (8 U.S.C. § 1225) and Thuraissigiam holding |

### Persuasion Techniques
- **Compression / list framing**: presents a worst-case list as a unified “platform,” encouraging a “package” inference.
- **Ambiguity in quantifiers**: “we can” can mean legal authority, claimed authority, or isolated incidents; the post generally elides scope conditions.
- **Rhetorical escalation**: “third world prison,” “terrorist,” “totalitarianism” are affective terms that may outrun the sourced factual core.

### Unstated Assumptions

| Assumption | Claim ID | Critical? | Problematic? |
|---|---|---|---|
| Reported internal memos translate into widespread, routine practice | GOV-2026-033 | Y | ? |
| Errors/misconduct (e.g., citizen detention) are not rare outliers but a predictable outcome of policy | GOV-2026-036 | Y | ? |
| Expedited/limited-review pathways dominate rather than being bounded to certain categories | GOV-2026-038 | Y | ? |
| “Totalitarianism” is the correct frame for a mix of contested memos, statutory authorities, and incidents | (overall) | N | ? |

### Evidence Assessment
- **Stronger support**: statutory “carry papers” requirement for noncitizens (8 U.S.C. § 1304(e)) and DHS’s own Federal Register summary of penalties; credible reporting on the internal memo asserting administrative-warrant home entry (with contemporaneous judicial pushback in at least one case); DHS privacy documentation showing field biometric/photo collection without opt-out and long retention (Mobile Fortify PTA); GAO documentation that enforcement actions and detainers have affected “potential U.S. citizens”; documented detention of very young children during operations; repeated use of “domestic terrorism”/“terrorist” labels by senior officials and DHS messaging after incidents.
- **Weaker support / overstatement**: “indefinite detention with no lawyer” as a general rule; “no day in court” as a general rule; and “shoot you because you are a terrorist” as a policy-like permission (deadly force remains legally constrained to imminent threat).

### Credence Assessment
- **Overall Credence**: 0.45
- **Reasoning**: Several bullets map to real statutory requirements or to contemporaneous reporting about contested DHS/ICE memos and Minnesota incidents; however, the post’s framing tends to erase scope conditions and legal nuance, and it mixes “ICE” with broader DHS immigration enforcement. As a result, it is directionally informative but not reliable as a standalone statement of what the law uniformly permits.

## Stage 3: Dialectical Analysis

### Steelmanned Argument
Even if some legal constraints exist on paper, immigration enforcement can operate through fast-moving administrative processes and contested internal legal theories that functionally evade ordinary checks (judicial warrants, meaningful hearings, timely counsel). When combined with aggressive tactics, third-country removal policies, and expansive immunity claims by top officials, the system’s “error tolerance” and accountability may be low enough that it resembles an authoritarian mechanism for a subset of residents—especially noncitizens and mixed-status communities.

### Strongest Counterarguments
1. Many of the post’s claims are **categorical where reality is conditional**: statutory and constitutional constraints exist, courts can intervene, and many people do get hearings and access to counsel (though not government-appointed).
2. Some cited “positions” are **contested or episodic** (reported memos; high-salience incidents) and may be narrowed, enjoined, or reversed; the post risks treating peak-controversy moments as stable governance.
3. “Totalitarianism” is a strong descriptor; liberal democracies can have severe rights violations in specific domains without meeting the historical/analytical criteria for totalitarian systems.

### Synthesis Notes
The post is best read as a **risk framing** rather than a literal legal cheat-sheet. The most actionable takeaways for factual assessment are: (a) distinguish *legal authority* vs *claimed authority* vs *practice*; (b) treat “ICE” vs “DHS immigration enforcement” precisely; and (c) evaluate contested memos and accountability mechanisms (courts, inspectors general, congressional oversight) as the key hinge points.

### Claims to Cross-Reference
- GOV-2026-033 with primary memo text (if/when publicly released) and any court injunctions or DHS OGC follow-up.
- GOV-2026-039 with the underlying memo/court filings and State Department “assurances” procedures.
- Minnesota incidents (Good/Pretti/citizen detention/child detention) with official investigations and any criminal/civil case outcomes.
- GOV-2026-035 with Mobile Fortify PIA/SORN materials (as referenced in the PTA) and any congressional oversight correspondence.

### Claim Summary

| ID | Type | Domain | Evidence | Credence | Claim |
|----|------|--------|----------|----------:|-------|
| GOV-2026-033 | [F] | GOV | E4 | 0.90 | ICE has asserted authority to forcibly enter homes without a judge-signed warrant (administrative-warrant theory) |
| GOV-2026-034 | [F] | GOV | E2 | 0.98 | Federal law requires noncitizens (18+) to carry registration documents at all times |
| GOV-2026-035 | [H] | GOV | E4 | 0.75 | ICE may disregard paper documents and rely primarily on biometrics (“scanner”) during encounters |
| GOV-2026-036 | [H] | GOV | E4 | 0.80 | ICE can detain people broadly across contexts, including children, and errors can result in detention of citizens |
| GOV-2026-037 | [H] | GOV | E6 | 0.20 | ICE can detain people indefinitely with no access to a lawyer |
| GOV-2026-038 | [H] | GOV | E4 | 0.55 | People targeted by ICE generally have no meaningful “day in court” |
| GOV-2026-039 | [F] | GOV | E2 | 0.85 | ICE can deport some people to third countries on short notice, potentially exposing them to persecution or harsh detention conditions |
| GOV-2026-040 | [H] | GOV | E4 | 0.55 | If ICE makes a serious mistake, it generally cannot or will not bring the person back |
| GOV-2026-041 | [H] | GOV | E6 | 0.15 | ICE can shoot people for “interference,” justified by labeling them “terrorists” |
| GOV-2026-042 | [F] | GOV | E4 | 0.75 | DHS/ICE leadership and allied messaging have repeatedly labeled people involved in immigration-enforcement incidents and interference/observation as “domestic terrorists”/“terrorists,” often immediately after events |

### Claims to Register

```yaml
claims:
  - id: "GOV-2026-033"
    text: "ICE has asserted authority to forcibly enter homes to make immigration arrests without a judge-signed warrant (e.g., relying on an administrative warrant)."
    type: "[F]"
    domain: "GOV"
    evidence_level: "E4"
    credence: 0.90
    source_ids: ["bluebadger2600-2026-ice-positions"]
  - id: "GOV-2026-034"
    text: "Federal law requires noncitizens (18+) to carry their registration documents (e.g., alien registration/receipt card) at all times."
    type: "[F]"
    domain: "GOV"
    evidence_level: "E2"
    credence: 0.98
    source_ids: ["bluebadger2600-2026-ice-positions"]
  - id: "GOV-2026-035"
    text: "In some encounters, ICE agents may disregard paper documents and instead rely primarily on biometric identity checks (fingerprint/face ID) to determine identity/status."
    type: "[H]"
    domain: "GOV"
    evidence_level: "E4"
    credence: 0.75
    source_ids: ["bluebadger2600-2026-ice-positions"]
  - id: "GOV-2026-036"
    text: "ICE can detain people broadly across contexts, including children, and errors can result in detention of U.S. citizens."
    type: "[H]"
    domain: "GOV"
    evidence_level: "E4"
    credence: 0.80
    source_ids: ["bluebadger2600-2026-ice-positions"]
  - id: "GOV-2026-037"
    text: "ICE can detain people indefinitely with no access to a lawyer."
    type: "[H]"
    domain: "GOV"
    evidence_level: "E6"
    credence: 0.20
    source_ids: ["bluebadger2600-2026-ice-positions"]
  - id: "GOV-2026-038"
    text: "People targeted by ICE generally have no meaningful right to a day in court."
    type: "[H]"
    domain: "GOV"
    evidence_level: "E4"
    credence: 0.55
    source_ids: ["bluebadger2600-2026-ice-positions"]
  - id: "GOV-2026-039"
    text: "ICE can deport some people to third countries (not their country of origin), potentially on short notice and with limited procedural safeguards."
    type: "[F]"
    domain: "GOV"
    evidence_level: "E2"
    credence: 0.85
    source_ids: ["bluebadger2600-2026-ice-positions"]
  - id: "GOV-2026-040"
    text: "If ICE makes a serious mistake (e.g., wrongful removal), it generally cannot or will not bring the person back."
    type: "[H]"
    domain: "GOV"
    evidence_level: "E4"
    credence: 0.55
    source_ids: ["bluebadger2600-2026-ice-positions"]
  - id: "GOV-2026-041"
    text: "If someone interferes with ICE activity, ICE can use lethal force and justify it by labeling the person a terrorist."
    type: "[H]"
    domain: "GOV"
    evidence_level: "E6"
    credence: 0.15
    source_ids: ["bluebadger2600-2026-ice-positions"]
  - id: "GOV-2026-042"
    text: "DHS/ICE leadership and allied messaging have repeatedly labeled people involved in immigration-enforcement incidents and interference/observation as “domestic terrorists”/“terrorists,” often immediately after events."
    type: "[F]"
    domain: "GOV"
    evidence_level: "E4"
    credence: 0.75
    source_ids: ["bluebadger2600-2026-ice-positions"]
```

---

**Analysis Date**: 2026-01-25  
**Analyst**: codex (gpt-5.2)  
**Credence in Analysis**: 0.70

## Analysis Log

| Pass | Date | Tool | Model | Duration | Tokens | Cost | Notes |
|------|------|------|-------|----------|--------|------|-------|
| 1 | 2026-01-25 06:01 | codex | gpt-5.2 | 20m9s | 4,937,455 | ? | Initial 3-stage analysis + sourced verification (law, memos, Minnesota incident… |
| 2 | 2026-01-25 08:10 | codex | gpt-5.2 | 24m2s | 13,083,563 | ? | Pass 2: incorporated user-provided reporting list; updated credences; added GOV… |
| 3 | 2026-01-25 09:03 | codex | gpt-5.2 | 10m39s | 7,837,591 | ? | Pass 3: added AP/SCOTUS reporting on third-country removals and contested retur… |
| 4 | 2026-01-25 12:52 | codex | gpt-5.2 | 26m36s | 16,104,319 | ? | Pass 4: integrated transcript review; added primary docs (GAO, Mobile Fortify P… |

### Revision Notes

**Pass 4**: Pass 4: integrated transcript review; added primary docs (GAO, Mobile Fortify PTA, Kidd order, Federal Register); updated GOV-2026-034/035/036/038 credences; n…
**Pass 3**: Pass 3: added AP/SCOTUS reporting on third-country removals and contested return after error; updated GOV-2026-039/040 evidence+credence.
**Pass 2**: Pass 2: incorporated user-provided reporting list; updated credences; added GOV-2026-042 (domestic-terrorism/terrorist labeling pattern).
**Pass 1**: Initial 3-stage analysis + sourced verification (law, memos, Minnesota incidents).

[^S01]: https://www.usatoday.com/story/news/nation/2026/01/20/immigration-agents-minnesota-police-officer/88268058007/
[^S02]: https://www.democracydocket.com/news-alerts/attorney-general-bondi-minnesota-voter-rolls-border-patrol-fatal-shooting/
[^S03]: https://nypost.com/2026/01/24/us-news/minnesota-gov-tim-walz-activates-state-national-guard-blasts-federal-government-after-shooting/
[^S04]: https://edition.cnn.com/2026/01/24/politics/shooting-minneapolis-trump-politics
[^S05]: https://www.reuters.com/world/us/minnesota-governor-says-federal-agents-involved-shooting-minneapolis-2026-01-24/ (not accessible in this environment; JS/anti-bot)
[^S06]: https://www.wired.com/story/the-instant-smear-campaign-against-border-patrol-shooting-victim-alex-pretti/
[^S07]: https://www.theguardian.com/us-news/2026/jan/24/jacob-frey-full-statement
[^S08]: https://www.fox9.com/news/minneapolis-shooting-ag-pam-bondi-urges-gov-walz-support-ice
[^S09]: https://www.pbs.org/newshour/nation/not-opening-the-door-to-ice-may-no-longer-stop-officers
[^S10]: https://www.fox32chicago.com/news/johnson-pritzker-abolish-ice-shooting
[^S11]: https://inthesetimes.com/article/minneapolis-ice-shooting-protests
[^S12]: https://time.com/7357547/minneapolis-shooting-ice-agent/
[^S13]: https://www.foxnews.com/politics/noem-says-minneapolis-suspect-committed-domestic-terrorism-accuses-walz-frey-inciting-violence
[^S14]: https://www.newsweek.com/democrats-demand-impeach-kristi-noem-new-dhs-fatal-shooting-11412444
[^S15]: https://thehill.com/regulation/court-battles/5705035-aclu-minnesota-federal-agent-tactics/ (not accessible in this environment; blocked)
[^S16]: https://www.fox9.com/news/minneapolis-shooting-national-guard-called-assist-after-latest-incident-federal-agents
[^S17]: https://www.axios.com/local/twin-cities/2026/01/24/tim-walz-investigation-border-patrol-shooting-minneapolis (accessed via text extraction proxy due to Cloudflare)
[^S18]: https://edition.cnn.com/2026/01/24/us/invs-videos-show-federal-officer-recovered-gun (accessed via text extraction proxy due to JS)
[^S19]: https://www.washingtonpost.com/nation/2026/01/24/federal-agents-minneapolis-shooting-investigation/ (not accessible in this environment; network/anti-bot)
[^S20]: https://www.beaumontenterprise.com/news/article/governor-a-person-has-been-shot-killed-by-21313055.php (not accessible in this environment; CAPTCHA)
[^S21]: https://www.aljazeera.com/news/2026/1/24/us-federal-agents-shoot-another-person-in-minneapolis-governor
[^S22]: https://thehill.com/homenews/administration/5704739-trump-defends-federal-agents-minnesota/ (not accessible in this environment; blocked)
[^S23]: https://www.theguardian.com/us-news/2026/jan/24/protests-alex-pretti-killing-federal-agents-ice
[^S24]: https://apnews.com/article/immigration-enforcement-minnesota-protester-alex-pretti-15ade7de6e19cb0291734e85dac763dc
[^S25]: https://abcnews.go.com/US/alex-pretti-icu-nurse-killed-federal-agent-minneapolis/story (URL provided; returned 404 when accessed). Used: https://abcnews.go.com/US/alex-pretti-icu-nurse-killed-federal-agent-minneapolis/story?id=129525591
[^S26]: https://www.thetimes.com/us/news-today/article/ice-detains-2-year-old-chloe-renata-tipan-villacis-6nx77vfv7 (partial access)
[^S27]: https://www.minnpost.com/metro/2026/01/federal-officers-shoot-and-kill-man-in-minneapolis/
[^S28]: https://www.wired.com/story/us-judge-rules-ice-raids-require-judicial-warrants-contradicting-secret-ice-memo/
[^S29]: https://www.vox.com/politics/476398/minneapolis-fatal-shooting-border-patrol-ice-alex-pretti
[^S30]: https://www.theguardian.com/us-news/2026/jan/23/us-immigration-two-year-old-minnesota-girl
[^S31]: https://www.vox.com/podcasts/476276/keith-ellison-astead-herndon-minneapolis-today-explained
[^S32]: https://reason.com/2026/01/23/ice-tells-legal-observer-we-have-a-nice-little-database-and-now-youre-considered-a-domestic-terrorist/
[^S33]: https://newrepublic.com/article/205061/renee-good-kristi-noem-domestic-terrorists-minneapolis
[^S34]: https://reason.com/2025/12/26/justice-department-says-filming-immigration-raids-is-domestic-terrorism/
[^S35]: https://www.newsweek.com/noem-ice-shooting-domestic-terrorism-minneapolis-11324489
[^S36]: https://www.cbsnews.com/minnesota/news/what-is-domestic-terrorism-renee-good-ice/
[^S37]: https://apnews.com/article/trump-migrants-el-salvador-prison-3c46db296c219c7b3a701474eaea5184
[^S38]: https://www.supremecourt.gov/opinions/24pdf/24a1153_l5gm.pdf
[^S39]: https://apnews.com/article/deportees-south-sudan-ice-immigration-identities-eddd2d1a172775ec7d9403984ffb41e2
[^S40]: https://www.foxnews.com/politics/south-sudan-deportations-have-placed-migrants-ice-officials-danger-new-court-filing
[^S41]: https://www.americanimmigrationcouncil.org/blog/men-deported-el-salvador-stories-investigation/ (accessed via text extraction proxy due to bot protection)
[^S42]: https://refugeerights.org/news-resources/trump-administrations-third-country-removals-put-migrants-in-harms-way (accessed via text extraction proxy due to 403)
[^S43]: https://www.brennancenter.org/our-work/analysis-opinion/el-salvadors-offer-house-us-prisoners-illegal
[^S44]: https://factually.co/fact-checks/justice/has-ice-deported-us-citizens-874fd2 (not accessible in this environment; Vercel checkpoint / 429)
[^S45]: https://www.ohchr.org/en/press-releases/2025/04/un-experts-alarmed-illegal-deportations-united-states-el-salvador (not accessible in this environment; Cloudflare/JS challenge)
[^S46]: https://www.gao.gov/assets/gao-21-487.pdf (GAO)
[^S47]: https://www.aclusocal.org/app/uploads/drupal/sites/default/files/kidd_msj_order.pdf
[^S48]: https://www.govinfo.gov/content/pkg/FR-2025-03-12/pdf/2025-03944.pdf
[^S49]: https://s3.documentcloud.org/documents/26209262/mobile-fortify-pta.pdf
[^S50]: https://apnews.com/article/immigration-detention-ice-trump-e1c2322c3f88c1f7d7e83c8c42109cb6
[^S51]: https://www.aclu.org/press-releases/aclu-demands-information-from-dhs-about-alarming-pattern-of-retaliation-against-those-recording-immigration-agents
[^S52]: https://www.themarshallproject.org/2026/01/07/ice-minneapolis-shooting-renee-good
