---
name: build-pipeline owner agent (separate ownership)
description: There is a separate agent who owns the NeurIPS 2026 sprint build pipeline (bin/convert_to_tex.py, LaTeX template, common/ infrastructure). They drop notes in per-paper directories.
type: project
originSessionId: 4982a806-beb1-46f9-8248-13d92749e28a
---
A separate agent owns the NeurIPS 2026 sprint build pipeline as of 2026-05-05 evening (post-abstract-submission, in the May 6 AOE full-paper-deadline window). Their territory: `bin/convert_to_tex.py`, `bin/check-anonymization.py`, the NeurIPS LaTeX template + `.sty`, `common/refs.bib`, supplementary-ZIP scaffolding, and any cross-paper rendering / formatting issues.

**Why:** The three-paper sprint has multiple per-paper agents working in parallel (B-N4, B-CS1, B-N8). Build-pipeline issues are cross-paper-applicable, so they were factored out to a single owner to avoid duplicated work and merge conflicts in shared tooling.

**How to apply:**

- Don't touch `bin/`, `common/`, or LaTeX template files unless explicitly asked. Surface build-pipeline issues into per-paper `OUTLINE.md` (under a "Known issue / pending build-pipeline fix" section) rather than fixing them locally.
- Watch for notes from the build-pipeline agent dropped in `02-convergence/` — they're likely instructions to land specific edits or signals about pipeline changes that affect the paper.
- The B-CS1 OUTLINE already has a `\appendix` converter glitch documented this way (renders appendices as section 11+ rather than letter-prefixed) — this is a cross-paper issue, not a B-CS1 issue, and it's the build-pipeline agent's call.
