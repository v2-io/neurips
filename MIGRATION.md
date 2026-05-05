# MIGRATION — restructure log

*Notes captured as the three NeurIPS papers move from the monolithic `~/src/neurips2026/` workspace into a parent + submodule layout at `~/src/neurips/`. Goal: do the first paper stepwise with Joseph instructing; capture each decision so paper #2 and #3 become mechanical.*

Source-of-truth restructure plan: `~/src/ops/neurips-restructure.md`.

---

## Decisions log

*One bullet per choice point, with rationale. Future agents should be able to read this and reconstruct why the layout looks the way it does.*

- **2026-05-05 — Parent path:** `~/src/neurips/` (sibling to `~/src/neurips2026/`; old workspace stays in place during migration). Initialized with `main` as the default branch.
- **2026-05-05 — Parent contents:** thin shell. Just `README.md`, `.gitignore`, `MIGRATION.md` (this file), and the per-paper submodule references. No CLAUDE.md, PRAXES.md, STYLE.md at this level yet — those decisions happen after we see how much per-paper duplication appears in practice.
- **2026-05-05 — Per-paper submodule layout:** TBD (waiting on Joseph; see "Open questions" below).

## Open questions

- **Per-paper canonical-repo location.** The parent will reference each paper as a submodule. Where does the canonical per-paper repo physically live, given we don't have GitHub remotes yet?
  - **Option A — Sibling working repo:** `~/src/paper-tragedy/` (or `~/src/neurips-tragedy/`), parent submodules it via relative path `../paper-tragedy`. Two on-disk checkouts of the same repo (the canonical + the parent's submodule clone). Standard pattern; trivial to migrate to GitHub URL later via `git submodule set-url`.
  - **Option B — Local bare canonical:** `~/src/_neurips-bare/tragedy.git`, parent submodules it. One working checkout (in parent); bare repo is the canonical. Slightly less discoverable; cleaner single-checkout workflow.
  - **Option C — Init nested, formalize later:** `git init` directly inside `~/src/neurips/01-tragedy/`, parent `.gitignore`s it for now. Convert to formal submodule once a GitHub URL exists. One checkout; not technically a submodule until later.
  - *Default if no input:* Option A with `~/src/paper-tragedy/` naming. Standard, forward-compatible with GitHub.

- **First paper:** assumed to be `01-tragedy/` (B-N4 — *Tragedy of the Confident Agent*). Confirm.

- **Submodule path-name inside parent:** `01-tragedy/` (matching the existing `~/src/neurips2026/01-tragedy/` slug). Numbered prefix follows the agentic-systems convention.

## Reusable migration recipe

*(Will be filled in once paper #1 is done. The intent is that paper #2 and #3 reduce to running the recipe.)*

## Open content-migration scope

*(Captured here as we go so we don't lose track. The structural shell is one job; pulling content from `~/src/neurips2026/01-tragedy/` into the new segmented layout is the next.)*

- Source content lives at `~/src/neurips2026/01-tragedy/` and is currently a monolithic `paper-draft.md`.
- The segmented `src/<slug>.md` + `OUT.*.md` manifest layout needs both:
  1. A segmentation of `paper-draft.md` (where do natural boundaries fall? typically at sub-section level, sometimes finer).
  2. Two assembly manifests — `OUT.full-paper.md` (no page constraint, includes everything) and `OUT.neurips-2026-paper.md` (9-page-budget-aware, omits some segments, possibly reorders).
- Auxiliary content to migrate: `prior-art/`, `sim/` (B-N4 has empirical anchor; B-N8 doesn't), `_archive/` (audit relics), `OUTLINE.md`, `LOG.md`, `PIPELINE-NOTES.md`, `paper.tex` (compiled artifact — gitignored), assets in `common/` shared across all three.
- The `bin/` build pipeline needs to be reworked to consume `OUT.*.md` manifests instead of monolithic `paper-draft.md`. Build-script lives in the parent or per-paper? — TBD.
- `common/` (refs.bib, neurips_2026 LaTeX template, checklist.tex) — likely stays at parent level, exposed to submodules via path. — TBD.

---

*Append entries chronologically. Reverse-chronological convention used in the old workspace's LOG.md is fine here too if it gets long.*
