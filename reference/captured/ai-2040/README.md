# AI 2040 audit corpus

This directory preserves the text and public-response artifacts used by the
Reality Check of **AI 2040: Plan A — The Deal**. The corpus was captured on
2026-07-11 in the standalone `ai-2040-analysis` repository and copied into the
canonical Reality Check data repository on 2026-07-14.

## Primary publication

- Canonical site: <https://ai-2040.com/>
- Published PDF: [`../../primary/aifutures-2026-ai-2040-plan-a.pdf`](../../primary/aifutures-2026-ai-2040-plan-a.pdf)
- PDF SHA-256: `1b81d083522715e48e7e8709fed7a6693a6935df2327e89e7146d83ae02471a3`
- Site-derived scenario text: [`site/main.md`](site/main.md)
- PDF-to-Markdown conversion: [`pdf-text.md`](pdf-text.md)

The retained first-party package also includes the team and release credits,
the economic model explanation and technical write-up, and every supplement
cited in the analysis: assumptions, plan comparison, verification, covert
projects, deal decline, and the alignment roadmap.

## Public responses

The `responses/` subtree preserves normalized Markdown plus the available raw
capture material for:

- Timothy B. Lee / Binary Bits: <https://threadreaderapp.com/thread/2075660927001608431.html>
- 0.005 Seconds: <https://threadreaderapp.com/thread/2075262321266704769.html>
- Anton Leicht: <https://threadreaderapp.com/thread/2075300220624085241.html>
- Hacker News discussion: <https://news.ycombinator.com/item?id=48848425>

## Integrity and scope

[`SHA256SUMS`](SHA256SUMS) records hashes for every captured artifact in this
directory. The publication PDF is stored separately under `reference/primary/`
and its hash is recorded above.

This is a curated audit corpus, not a complete website mirror. Large
presentation images, JavaScript/CSS bundles, and uncited branches were omitted;
the original 67 MB standalone capture remains reproducible from the collection
scripts in the `ai-2040-analysis` repository.
