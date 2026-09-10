# Capture, discovery and verification notes

Captured and reviewed on **2026-09-10**. This is a public-record investigation, not an audit of private systems or a certification of the mathematics.

## Coverage

All 17 supplied URLs are represented by separate source analyses. The set adds The Decoder, ABC and El País reporting, primary replies from Boaz Barak and Noam Brown discovered through those reports, and official API data policy: **23 analyses total**. OpenAI’s launch thread, technical PDFs, the Clay formulation, screenshots and historical versions support those analyses rather than being counted as additional independent accounts. The synthesis is a separate database source.

`manifest.json` records the initial 17 URLs and raw-byte SHA-256 hashes. Additional manifests record subsequent fetch URLs. `files-sha256.json` inventories retained artifacts. A successful curl exit only means transport completed: challenge pages and incomplete page shells are explicitly identified below. `*-target.txt` files isolate the requested post or author thread; raw captures retain surrounding context.

## DB-first check

Before external discovery, `rc-db search 'Navier Stokes' --limit 5` was attempted. The installed launcher pointed to a missing Python. The framework virtual environment worked, but semantic search failed because the configured proxy required missing Python SOCKS support. `REALITYCHECK_EMBED_SKIP=1` does not disable embedding generation inside that search function.

The fallback queried the actual LanceDB tables, not legacy YAML, for `Navier`, `Buckmaster`, `value chain`, `customer`, and `sovereign`. Results are in `db-search.json`. No existing Navier/Buckmaster record was found. Related records include INST-2026-981, ECON-2026-984 and INST-2026-992. These are theoretical context rather than evidence about this event.

The optional monotonic claim-ticket allocator could not reserve 60 INST IDs because the existing sequence was already near 999. New claims use explicitly collision-checked unused IDs starting at 300 in the relevant domains. No existing claims were renumbered or overwritten.

## External discovery

The initial Google queries were:

1. `OpenAI Navier Stokes Buckmaster plagiarism September 2026`
2. `OpenAI Navier Stokes customer data training Bubeck response`

Google returned redirect/JavaScript shells. DuckDuckGo queries about plagiarism/Buckmaster and training/data/fraud returned human-verification challenges. Bing returned low-relevance results; these were not treated as evidence. A Jina Google-search request was access-blocked. An HN Algolia request failed at the configured proxy.

Brave returned useful results for these distinct queries (raw pages and extracts retained):

- `"Navier Stokes" "OpenAI" plagiarism`
- `"Buckmaster" "academic fraud"`
- `"Navier Stokes" "OpenAI" data training`
- `"Bubeck" "authorship" "September"`
- `"OpenAI" "Navier" "10000"`
- `"Alpöge" "September 2"`

The queries `"Andreas Thom" "Sellke"` and `"Terence Tao" "promising problem"` hit challenges. The original author threads were nevertheless recovered directly. A follow-up `"Navier" "Cao-Labora" references` query was also retained. Search-result snippets were used for discovery only; claims about the added reports and replies come from fetched source bodies.

Brave discovered ABC, The Decoder and El País. The Decoder linked Buckmaster’s later malpractice allegation and Barak’s reply; El País linked Brown’s reply. This added counterarguments as well as criticism. No independently documented formal finding of plagiarism or fraud was found in this bounded search; this is not a claim to have exhausted every report or institutional process.

## Primary capture recovery

- **OpenAI release:** direct page returned a challenge. `r.jina.ai/https://openai.com/index/navier-stokes-solution/` returned the full text. Cross-checked against the official launch thread, official response and linked PDF.
- **Thread Reader:** target post bodies recovered for all supplied threads. “More from” sections are not additional target posts. Embedded screenshots need separate retrieval; Bubeck’s attached message screenshot was downloaded and visually inspected.
- **X:** Alpöge, Barak and Brown post bodies were recovered from HTML. Quoted posts and surrounding replies can be truncated and are not assumed complete.
- **Mastodon:** normal pages were JavaScript shells. Public `/api/v1/statuses/<id>` and `/context` endpoints recovered post content. Thom’s context did not include parts 2/3 and 3/3; the account-status endpoint recovered both. Tao’s four author posts were recovered; replies by similarly named accounts are excluded from his target text. Buckmaster’s account history supplied the later post and attached bibliography screenshot.
- **PDFs:** downloaded Buckmaster’s statement, the pair’s Euler paper, OpenAI’s Navier–Stokes paper and the Clay formulation. Used `pdftotext -layout` for searchable text. Only theorem statements, attribution and relevant contextual passages were checked, not the complete proofs.
- **Policy:** fetched official API data documentation. The Codex enterprise admin route led to a general rollout guide; it is not evidence of either researcher’s settings. The API guide establishes a stated API default, not all product defaults or actual enforcement.

## Bibliography version verification

CDX query:

`https://web.archive.org/cdx/search/cdx?url=cdn.openai.com/pdf/32d9f210-8b73-45e0-91bc-82a30aef8a9a/navier-stokes.pdf&output=json&filter=statuscode:200`

Raw indexed snapshots retrieved:

- `https://web.archive.org/web/20260908172948id_/https://cdn.openai.com/pdf/32d9f210-8b73-45e0-91bc-82a30aef8a9a/navier-stokes.pdf`
- `https://web.archive.org/web/20260908200449id_/https://cdn.openai.com/pdf/32d9f210-8b73-45e0-91bc-82a30aef8a9a/navier-stokes.pdf`

Responses were gzip-compressed despite the PDF URL. Initial PDF extraction failed; inspecting file signatures identified compression. Preserved the original `.pdf.gz` responses and decoded them before extraction. Both decoded files are readable PDFs. Earlier bibliography has 16 references; later has 22 and added historical discussion. The later file is byte-identical to the direct September 10 PDF. This supports a version change within observed archive bounds, not an exact edit time or motive.

## Per-claim verification and limitations

`claim-verification-searches.json` records **two distinct exact-phrase searches per claim**, with filenames, line numbers and matching excerpts across the captured primary sources and reporting. Those are corpus-verification queries, not disguised independent web searches. The web queries above are the shared discovery and disconfirmation pass. Each analysis identifies which source comparisons settle its attributed facts and which private propositions remain unresolved.

Independent sources must be distinguished from repeated testimony. WIRED’s briefing, ABC’s named interviews and archived PDF versions add evidence of different kinds; ten summaries of Buckmaster’s statement do not constitute ten witnesses to the call. Primary records verify what was said and published; they do not independently verify hidden training or access events.

No private drafts, account settings, dataset manifests, model checkpoints, full call recordings or independently audited access logs were obtained. No Lean clean build or axiom audit was performed. The July essay is analyzed for its central mechanism and the present update, not re-audited claim by claim across all its older numerical examples. These limits are why the entire package is marked **DRAFT**.

## Lifecycle and database handling

The first OpenAI lifecycle log was opened before capture. Session discovery was ambiguous, so no token totals or cost were fabricated. Other per-source lifecycle baselines were recorded at drafting after shared capture; the synthesis baseline was recorded after drafting. Completion logs explicitly retain these limitations.

Sources, claims, evidence links and reasoning trails were initially registered through the framework API with embeddings disabled. A complete cached all-MiniLM-L6-v2 model was then located and used offline to prepare 79 embeddings for the 55 new claims and 24 new source records (including the synthesis). These embeddings were applied without changing unrelated records. No framework source files were changed. PySocks was installed only into a temporary dependency directory during diagnosis; the final embedding calculation used local model files. YAML source artifacts and package JSON are audit/export artifacts; LanceDB remains authoritative.

The working local embedding override is `REALITYCHECK_EMBED_MODEL=/home/lhl/.cache/huggingface/hub/models--sentence-transformers--all-MiniLM-L6-v2/snapshots/1110a243fdf4706b3f48f1d95db1a4f5529b4d41`, with `HF_HUB_OFFLINE=1`. This avoids remote discovery through the problematic proxy. The installed launcher itself was not modified.
