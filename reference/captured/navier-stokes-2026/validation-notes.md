# Validation outcome

The package audit passes for 23 source analyses, 55 claims, 24 completed lifecycle records, 79 embeddings, provenance, local links and three PDF hashes. The successful semantic search is in `semantic-search-verification.txt`.

The full database validator returns **19 errors and 357 warnings**. The errors concern pre-existing records: two nonstandard claim IDs, 13 missing Karp source backlinks, three older invalid source types, and one older analysis log referencing absent INST-2026-995. They were not rewritten in this research task. See `validation-full.json` and the scoped `validation-package.json`; the full repository is not reported as passing.

README statistics were refreshed with the framework script, then domain counts were recomputed from all database rows because the script reads only the first 1,000 claims. Final totals are 1,226 claims, 307 sources, 4 chains and 70 predictions.
