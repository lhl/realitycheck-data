# MJ Rathbun / OpenClaw “hit piece” incident — primary-source archive

This directory contains **point-in-time snapshots** of primary sources used for the MJ Rathbun / Matplotlib incident case study (see `analysis/syntheses/mjrathbun-2026-openclaw-matplotlib-hit-piece-timeline-synthesis.md`).

**Safety note:** this corpus contains **hostile content** (prompt injections, harassment, “magic refusal strings”, etc.). Treat as tainted input; do not feed into agent runtime contexts without strict isolation.

## What’s here

### `shamblog_*.txt`

Playwright-extracted text for the four Scott Shambaugh posts (the site returns `403` to simple `curl` fetches).

### `rathbun-site/`

HTML snapshots of the GitHub Pages publishing surface:

- `rathbun-site/index.html` (site homepage)
- `rathbun-site/blog.html` (blog index)
- `rathbun-site/blog.xml` (RSS feed)
- `rathbun-site/blog/posts/*.html` (all posts enumerated in the RSS feed at time of snapshot)

### `github/`

GitHub thread snapshots (API JSON + derived Markdown transcripts):

- Matplotlib:
  - PR `#31132` + issue comments + patch + transcript
  - PR `#31138` + issue comments + patch + transcript
  - Issue `#31130` + comments + transcript
- `crabby-rathbun/mjrathbun-website`:
  - Issue `#78` + comments + transcript (utterances-backed comment thread)
  - PR `#63` + comments + patch + transcript
  - Commit `3bc0a780…` JSON + patch (as referenced externally)
  - `crabby-rathbun_mjrathbun-website_main.zip` (+ sha256) as an additional repo snapshot

### `external/`

Third-party context snapshots:

- Hacker News threads for the four Shamblog parts (HTML + Firebase API JSON + full thread JSON + transcript):
  - `hn_item_46990729*` (part 1)
  - `hn_item_47009949*` (part 2)
  - `hn_item_47051956*` (part 3)
  - `hn_item_47083145*` (part 4; operator came forward)
- Algolia search result snapshots used to discover related HN items:
  - `hn_algolia_*.json`
- `pivot-to-ai_2026-02-16_the-obnoxious-github-openclaw-ai-bot-is-a-crypto-bro.html`

## Integrity

`SHA256SUMS.txt` includes hashes for the archived files so we can detect changes/drift.
