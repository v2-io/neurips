# MIGRATION — restructure log

*Notes captured as the three NeurIPS papers move from the monolithic `~/src/neurips2026/` workspace into a parent + submodule layout at `~/src/neurips/`. Goal: do the first paper stepwise with Joseph instructing; capture each decision so paper #2 and #3 become mechanical.*

Source-of-truth restructure plan: `restructure-plan.md` (alongside this file in the parent repo; moved out of `~/src/ops/` 2026-05-05).

---

## Decisions log

*One bullet per choice point, with rationale. Future agents should be able to read this and reconstruct why the layout looks the way it does.*

- **2026-05-05 — Parent path:** `~/src/neurips/` (sibling to `~/src/neurips2026/`; old workspace stays in place during migration). Initialized with `main` as the default branch.
- **2026-05-05 — Parent contents:** thin shell. Just `README.md`, `.gitignore`, `MIGRATION.md` (this file), and the per-paper submodule references. No CLAUDE.md, PRAXES.md, STYLE.md at this level yet — those decisions happen after we see how much per-paper duplication appears in practice.
- **2026-05-05 — Per-paper canonical-repo location:** GitHub. Joseph created `git@github.com:v2-io/paper-tragedy-confident-agent.git` and the bootstrap pattern is: temporary working dir at `~/src/paper-{slug}/` → init + initial commit + push to GitHub origin → submodule-add from parent via SSH URL. The temporary `~/src/paper-{slug}/` working dir is staging, not canonical; cleanup TBD per paper (Joseph's "for a moment" framing implies removal once submoduled, but waiting on confirmation).

- **2026-05-05 — Repo / submodule naming:** *hybrid numbered + multi-word slug*. GitHub repo names are `paper-{multi-word-slug}` (venue-neutral; outlives any single submission). Parent-repo submodule paths are `0N-{multi-word-slug}/` (numbered prefix matches agentic-systems convention; multi-word slug matches GitHub repo name modulo the `paper-` prefix). All three picked by Joseph:
  - **Paper #1 (B-N4):** GitHub `paper-tragedy-confident-agent`, submodule `01-tragedy-confident-agent/`.
  - **Paper #2 (B-CS1):** GitHub `paper-unified-convergence-rl`, submodule `02-unified-convergence-rl/`.
  - **Paper #3 (B-N8):** GitHub `paper-llm-hallucinate-bound`, submodule `03-llm-hallucinate-bound/`.
  - The framing-noun-first slugs (`unified-convergence-rl`, `llm-hallucinate-bound`, `tragedy-confident-agent`) sort cleanly under `v2-io/` and read as natural-language descriptors of the contribution.

- **2026-05-05 — README content in per-paper repo:** ~3 lines: paper title, one-paragraph technical summary, mention of the segmented-paper workflow + concat-manifest pattern. Venue-neutral phrasing (the repo will outlive NeurIPS 2026; will also feed camera-ready, journal versions, possibly other venues).

## Open questions

- **Content migration scope (next phase).** Structural shells exist; segmenting `paper-draft.md` into `src/{slug}.md` files + writing `OUT.*.md` concat manifests is the substantive work. Stepwise on paper #1 first, then mechanical for #2/#3 (or each paper-agent picks up their own).

## Done

- **2026-05-05 — Three temporary `~/src/paper-{slug}/` staging dirs deleted.** Each was clean, HEAD matched its `origin/main` exactly. Submodule checkouts at `~/src/neurips/0N-{slug}/` are the canonical working locations now.

## Reusable migration recipe — **structural shell** (paper #1 → #2/#3 mechanical)

*Bootstrap of an empty per-paper repo, GitHub-backed, wired as a submodule of the parent. Refines as we discover steps.*

```bash
# Variables (per paper)
SLUG=tragedy-confident-agent          # multi-word slug; matches GitHub repo (modulo "paper-" prefix)
NUM=01                                 # zero-padded ordering inside parent

# 1. Create the GitHub repo (manual, once per paper).
#    Joseph creates `v2-io/paper-${SLUG}` on GitHub with no auto-init.

# 2. Bootstrap a working repo in temporary staging location.
mkdir ~/src/paper-${SLUG}
cd    ~/src/paper-${SLUG}
# Write README.md (paper title + one-paragraph summary + workflow note); see paper #1 for the template.
git init -b main
git add README.md
git commit -m "Initial commit"
git remote add origin git@github.com:v2-io/paper-${SLUG}.git
git push -u origin main

# 3. Wire as submodule in the parent umbrella repo.
cd ~/src/neurips
git submodule add git@github.com:v2-io/paper-${SLUG}.git ${NUM}-${SLUG}
git commit -- .gitmodules ${NUM}-${SLUG} -m "Add ${NUM}-${SLUG} submodule"

# 4. Cleanup (pending confirmation): rm -rf ~/src/paper-${SLUG}
#    The submodule checkout in ~/src/neurips/${NUM}-${SLUG}/ is a working clone with .git link
#    pointing into ~/src/neurips/.git/modules/${NUM}-${SLUG}/. The staging dir is redundant.
```

**Cross-paper invariants captured:**
- GitHub repo name: `paper-{multi-word-slug}`. Venue-neutral; `paper-` prefix groups them under `v2-io/`.
- Submodule path: `{NN}-{multi-word-slug}/`. Numbered prefix matches agentic-systems pattern; slug matches GitHub repo name minus `paper-`.
- Default branch: `main`. `git init -b main` sets it from the start (no `git branch -M main` step needed).
- Initial commit message: `Initial commit`. Standard GitHub bootstrap convention.
- Submodule-add commit on parent: `git commit -- .gitmodules <path> -m "..."` form (pathspec-bound) to avoid sweeping in any other in-flight working-tree changes.

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
