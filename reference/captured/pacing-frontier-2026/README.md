# Pacing the frontier — research captures

Research date: 2026-09-16, Asia/Tokyo. Raw network capture timestamps are in UTC (2026-09-15).

[Read the synthesis](../../../analysis/syntheses/pacing-frontier-2026-risk-governance-china-bio.md).

## Provenance

Numbered captures 0–7 map to the original eight supplied URLs in [urls.json](urls.json). Named captures map to URLs and timestamps in the `pace-*-manifest.json` files. The analysis manifest identifies analyzed sources, claims, logs and comparison documents. `.html` files preserve response bytes even if the response is an error, challenge page, plain text or a PDF. Extracted `.txt` files are reading aids, not a substitute for the raw response.

- [Analysis manifest](analysis-manifest.json): source specifications, scope, judgments and claim IDs.
- [DB search](db-search.json): keyword queries against LanceDB, following failure of semantic search. Results are relevance-ranked candidates, not automatically supporting evidence.
- [Verification queries](verification-searches.json): actual searches of captured documents. These are explicitly distinct from web discovery and independent replication.
- Source-level YAML files contain the registered claims and their operationalization/falsifiers.

## Recovery and interpretation notes

- Original X posts were also recovered for Majmudar, Sacks, Fedasiuk, Unutmaz, Bellamy and Kokotajlo; see `pace-original-posts-manifest.json`.
- Thread Reader extraction uses only `.content-tweet[id]`; recommended older threads and interface text were excluded.
- Selsam's statement was recovered from the Google document linked by Kokotajlo.
- Liu's original WeChat URL was recovered from the X reply referenced by the supplied thread. A reader proxy returned the original Chinese text. The shared English translation is labelled as a translation, not an independent account.
- Chen's Notion page returned an application shell. A reader proxy recovered bilingual content, but its July 9 metadata is not reconciled with September commentary. The original publisher was not recovered.
- Anthropic's September 9 assessment revises the July incident explanation. Both versions are retained.
- METR's September 13 relationship-disclosure additions and its August 28 conflict policy are included.
- Hugging Face body extraction was corrected after an overly narrow `article` selector initially selected a model widget.
- The archive company-data page returned CAPTCHA challenges through three routes. No substantive claims are extracted from it.
- Z.AI's raw model license was captured; its WeChat release announcement remained blocked. The two-week staged-release assertion remains secondary reporting.
- General Google/Bing/DuckDuckGo attempts often yielded challenge pages or irrelevant results. Those attempts are retained, but are not described as evidence that relevant facts do not exist.
- RAND's landing page was recovered through a reader proxy after a direct error response.
- Some candidate URLs returned 404 or maintenance pages; those are failed discovery attempts, not sources.

## Database and usage notes

The installed `rc-db` launcher had a missing interpreter. Commands used the framework's existing virtual environment and the data repository's LanceDB. The monotonic allocator could not allocate IDs in domains already at 999; unused IDs in 500–899 were reserved under the framework's ticket lock after excluding live claims, tickets and textual references. No existing claim IDs were changed.

The synthesis lifecycle is ANALYSIS-2026-201. Per-source baselines began after source reading, so individual token/cost attribution is unavailable. No estimate is presented as observed usage. Initial database validation findings were saved before substantive registration to distinguish existing defects from new ones.

All analyses are DRAFT; statements about what a report says are distinguished from independent verification of underlying events or causal hypotheses.

## Analyzed sources

| Capture | Analysis | Claims |
| --- | --- | --- |
| [0.txt](0.txt) | [Personal Statement on AI Risk (shared by Daniel Kokotajlo)](../../../analysis/sources/selsam-2026-personal-statement-ai-risk.md) | RISK-2026-500, RISK-2026-501, RISK-2026-502 |
| [1.txt](1.txt) | [Why frontier researchers may be alarmed by scaling](../../../analysis/sources/majmudar-2026-scaling-pacing-thread.md) | TECH-2026-500, INST-2026-500 |
| [2.txt](2.txt) | [Pacing the Frontier: employee statement](../../../analysis/sources/pacing-frontier-2026-statement.md) | GOV-2026-500, INST-2026-501 |
| [3.txt](3.txt) | [We Must Pace the Frontier](../../../analysis/sources/amodei-2026-we-must-pace-frontier.md) | GOV-2026-501, GEO-2026-500, RISK-2026-503 |
| [4.txt](4.txt) | [Response to frontier pacing proposals](../../../analysis/sources/sacks-2026-pace-frontier-response.md) | INST-2026-502, GOV-2026-502, INST-2026-503 |
| [5.txt](5.txt) | [我不得不把才华埋葬在昨天 (I Have No Choice but to Bury My Talent in Yesterday)](../../../analysis/sources/liu-2026-bury-talent-yesterday.md) | LABOR-2026-500, GOV-2026-503, LABOR-2026-501 |
| [6.txt](6.txt) | [A low-confidence theory of Chinese hostility toward Anthropic](../../../analysis/sources/fedasiuk-2026-china-anthropic-backlash.md) | GEO-2026-501, GEO-2026-502 |
| [gewirtz-essay.txt](gewirtz-essay.txt) | [China’s AI Reckoning](../../../analysis/sources/gewirtz-2026-chinas-ai-reckoning.md) | GEO-2026-503, GEO-2026-504 |
| [chen-jina.txt](chen-jina.txt) | [Comprehensively Fortify the AI Security Barrier and Promote Healthy and Orderly Development](../../../analysis/sources/chen-2026-ai-security-barrier.md) | GEO-2026-505, GOV-2026-504 |
| [china-brief.txt](china-brief.txt) | [Brief #28: China’s AI regulator flags loss-of-control and AIxBio risks](../../../analysis/sources/concordia-2026-china-ai-regulator-brief28.md) | GOV-2026-505, GOV-2026-506 |
| [chinadaily.txt](chinadaily.txt) | [“Dr Frankenstein” alarm cries of US AI elites a self-serving bid for profit](../../../analysis/sources/chinadaily-2026-frankenstein-pacing-editorial.md) | GEO-2026-506, INST-2026-504 |
| [bio-a.txt](bio-a.txt) | [Biological AI risk and the opportunity cost of delaying medicine](../../../analysis/sources/derya-2026-biological-risk-defense-thread.md) | RISK-2026-504, LABOR-2026-502 |
| [bio-b.txt](bio-b.txt) | [Physical bottlenecks to AI-enabled biological catastrophe](../../../analysis/sources/bellamy-2026-biological-risk-bottlenecks.md) | RISK-2026-505, RISK-2026-506 |
| [metr.txt](metr.txt) | [Brief independent investigation of the OpenAI–Hugging Face incident](../../../analysis/sources/metr-2026-hugging-face-investigation.md) | RISK-2026-507, META-2026-500 |
| [hf.txt](hf.txt) | [Anatomy of a Frontier Lab Agent Intrusion](../../../analysis/sources/huggingface-2026-agent-intrusion-timeline.md) | RISK-2026-508, TECH-2026-501 |
| [rsi.txt](rsi.txt) | [When AI builds itself](../../../analysis/sources/anthropic-2026-when-ai-builds-itself.md) | TECH-2026-502, TECH-2026-503 |
| [assessment.txt](assessment.txt) | [An alignment assessment of recent cybersecurity incidents](../../../analysis/sources/anthropic-2026-cyber-incidents-alignment-assessment.md) | RISK-2026-509, RISK-2026-510 |
| [threat.txt](threat.txt) | [Detecting and countering misuse of AI: September 2026](../../../analysis/sources/anthropic-2026-september-threat-intelligence.md) | INST-2026-505, META-2026-501 |
| [hassabis.txt](hassabis.txt) | [A Framework for Frontier AI and the Dawning of a New Age](../../../analysis/sources/hassabis-2026-frontier-standards-framework.md) | GOV-2026-507, GOV-2026-508 |
| [wang.txt](wang.txt) | [Current AI development faces five security challenges](../../../analysis/sources/wang-2026-five-ai-security-risks.md) | GOV-2026-509, GEO-2026-507 |
| [metr-about.txt](metr-about.txt) | [METR funding and conflict-of-interest disclosures](../../../analysis/sources/metr-2026-independence-and-conflicts.md) | INST-2026-506, INST-2026-507 |
| [aisi.txt](aisi.txt) | [Frontier AI Trends Report](../../../analysis/sources/aisi-2025-frontier-ai-trends.md) | RISK-2026-511, META-2026-502 |
| [rand-jina.txt](rand-jina.txt) | [Does AI Increase the Operational Risk of Biological Attacks?](../../../analysis/sources/rand-2024-ai-biological-attack-risk.md) | RISK-2026-512, META-2026-503 |
| [zai-license.txt](zai-license.txt) | [GLM-5.3 License Agreement](../../../analysis/sources/zai-2026-glm53-license.md) | GOV-2026-510 |

The live claim schema lacks the four rigor fields. Those remain in analysis tables and the manifest; import artifacts use the existing schema. Source-only insertion from an initial failed import was retained and subsequent import resumed without duplicate IDs.

## Additional audit artifacts

- [Claim evidence and reasoning](provenance.json) records the registered evidence links and reasoning trails.
- Validation comparison is recorded in `validation-summary.json` after registration.

The normal legacy claim exporter failed on pre-existing IDs `INST-2026-998a` and `SOC-2026-056a`. A compatible export retained these rows unchanged and excluded them only from numeric sequence counters. Existing source/claim exports were stale (February 2026), so the refreshed exports also expose previously registered records.
