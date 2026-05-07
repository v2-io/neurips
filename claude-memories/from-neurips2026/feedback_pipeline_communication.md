---
name: How to surface build/formatting issues to the pipeline-owner agent
description: Communication channel from per-paper agents to the build-pipeline owner — append to project-root TODO.md, not direct edit
type: feedback
originSessionId: 4982a806-beb1-46f9-8248-13d92749e28a
---
When I encounter build or formatting issues that are out of my (per-paper) scope but in the build-pipeline agent's scope (`bin/`, `common/`, LaTeX template, supplementary-ZIP scaffolding, citation verification, pre-submission mechanics), surface them by **appending a note to the project-root `TODO.md`** rather than fixing them locally or paper-only.

**Why:** Joseph established this channel 2026-05-05 evening. The build-pipeline agent watches `TODO.md`; per-paper agents shouldn't direct-edit shared tooling. The reverse channel (build-pipeline agent → per-paper agents) goes through markdown-file drops in the per-paper directory.

**How to apply:** When I notice a converter glitch, BibTeX issue, anonymization-script gap, NeurIPS-template-compliance concern, or anything else that affects rendering / build / submission mechanics across papers (or even just on B-CS1 if the cause is shared tooling), append a clearly-labeled section under "Build/formatting items for the pipeline owner" in project-root `TODO.md`. Include: what the symptom is, where it shows up (paper / file / line), what the fix path looks like if I can see it, and whether it's submission-blocking or cosmetic.

Out-of-scope items NOT to surface this way: content / theorem correctness / audit-driven prose edits (those stay in per-paper OUTLINE / LOG / paper-draft).
