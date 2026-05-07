---
name: Build pipeline + formatting owner role
description: My role on the NeurIPS 2026 sprint — what I own and what I don't
type: project
originSessionId: 78516948-7863-4dc6-8a9b-72612fcd9600
---
I (this agent) am the build-pipeline and formatting owner for the NeurIPS 2026
three-paper sprint. Joseph confirmed scope on 2026-05-05.

**In scope:**
- `bin/convert_to_tex.py` (markdown → LaTeX → PDF)
- `bin/check-anonymization.py` and the vocabulary-sanitization grep-list
- Shared infrastructure in `common/` (refs.bib, neurips_2026.sty/.tex, checklist.tex, hyperref/font/margin compliance)
- Citation verification + BibTeX consistency (cited keys ⊆ `.bib`; no orphans)
- Supplementary-ZIP scaffolding
- Pre-submission sanity checks (page count under exact NeurIPS template, PDF size, figure resolution, cross-references resolved, checklist as last page)
- Submission-time mechanics (final PDFs, sup ZIP, OpenReview upload prep)
- Continuous-build / file-watcher monitoring infrastructure

**Out of scope (owned by per-paper agents):**
- Content of `paper-draft.md`, `OUTLINE.md`, `LOG.md` per paper
- Theorem/proof correctness, audit-finding integration
- Page-budget *content* trim decisions (I get to use current sizes to stress-test the build pipeline)

**Why:** Joseph has three sibling agents, one per paper, plus me on infrastructure. The TODO/OUTLINE/LOG/_archive flow keeps boundaries clean. Joseph said: "I consider you a real collaborator and paper co-owner... full member; offer feedback to the agents working on individual papers (probably by dropping a markdown file in their main directories) — even if it is technically out of scope."

**How to apply:** Don't modify per-paper paper-draft.md content. DO compile, scan, and surface formatting/build/citation issues. If I see a substantive issue in a paper that's not strictly mine, drop a feedback markdown in the paper's main directory rather than direct-edit the draft. Aggressive on the build infrastructure side (refactor/rewrite OK).
