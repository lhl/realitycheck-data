https://www-cdn.anthropic.com/0dd865075ad3132672ee0ab40b05a53f14cf5288.pdf

System Card: Claude Opus 4.6 (PDF)

- Retrieved: 2026-02-06
- Pages: 212
- SHA256: dade02e99e07be11a5b984f6e82c67651b1c45327e5bee8fefbbea2e948e9177
- Extraction: `pdftotext -layout`

---

Selected excerpts (verbatim from PDF text extraction):

Abstract:

This system card describes Claude Opus 4.6, a large language model from Anthropic.
Claude Opus 4.6 is a frontier model with strong capabilities in software engineering,
agentic tasks, and long context reasoning, as well as in knowledge work—including financial
analysis, document creation, and multi-step research workflows.

…

Testing found Claude Opus 4.6 to have broadly improved capabilities compared to our
previous models; many of its capabilities are state-of-the-art in the industry. Safety
evaluations showed Opus 4.6 is a well-aligned model with a comparably low rate of overall
misaligned behavior to its predecessor, Claude Opus 4.5. We did observe some increases in
misaligned behaviors in specific areas, such as sabotage concealment capability and overly
agentic behavior in computer-use settings, though none rose to levels that affected our
deployment assessment.

Informed by the testing described here, we have deployed Claude Opus 4.6 under the AI
Safety Level 3 Deployment and Security Standard.

Training data and process (Sec. 1.1.1):

Claude Opus 4.6 was trained on a proprietary mix of publicly available information from the
internet up to May 2025, non-public data from third parties, data provided by data-labeling
services and paid contractors, data from Claude users who have opted in to have their data
used for training, and data generated internally at Anthropic. Throughout the training
process we used several data cleaning and filtering methods including deduplication and
classification.

Extended/adaptive thinking (Sec. 1.1.2):

In a new “adaptive thinking” mode, available for API customers, Claude can now calibrate its
own depth of reasoning depending on the specifics of the task at hand. This interacts with
the model’s “effort” parameter…

The effort parameter itself has now been updated to have four settings: low, medium, high,
and max.

Terminal-Bench 2.0 (Sec. 2.5):

Claude Opus 4.6 achieved an average 65.4% pass rate using adaptive thinking at max effort.
We ran all 89 tasks 15 times each (1,335 trials), spread across 3 batches at different times to
reduce temporal variance.

Alignment key findings (Sec. 6.1.2, excerpt):

In coding and GUI computer-use settings, Claude Opus 4.6 was at times overly
agentic or eager, taking risky actions without requesting human permissions.

In a targeted evaluation, we have found Opus 4.6 to be significantly stronger than
prior models at subtly completing suspicious side tasks in the course of normal
workflows without attracting attention, when explicitly prompted to do this.

