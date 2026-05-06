# MIGRATE-TODO.md — Restructure / migration backlog

*Active items for the umbrella restructure + per-paper content migration + cross-cutting doc consolidation. Companion to `PIPELINE-TODO.md` (build / formatting / authoring tooling) and `AGENTS.md` (process / language / rubocop). Replaces and consolidates the previous `restructure-plan.md` (sprint plan) and `MIGRATION.md` (migration log) — both archived to `_archive/` with full historical context preserved.*

---

## Structural decisions in place

(Reference only; the active work below assumes these are settled.)

- **Umbrella** at `~/src/neurips/` with three per-paper submodules, each backed by its own GitHub repo (`v2-io/paper-tragedy-confident-agent`, `v2-io/paper-unified-convergence-rl`, `v2-io/paper-llm-hallucinate-bound`).
- **Hybrid numbered + multi-word-slug naming**: GitHub `paper-{slug}`; parent submodule path `0N-{slug}/`.
- **Segmented-paper layout** modeled on `~/src/agentic-systems/`: `src/<slug>.md` segments + `OUT.*.md` concatenation manifests (one per output form — `OUT.full-paper.md`, `OUT.neurips-2026-paper.md`, future-venue manifests).
- **Authoring rules** captured in `AUTHORING.md` (Style Guide section of the prior restructure-plan superseded).
- **Citation system** decided in `REFS-AND-CITATIONS.md` (bracketed superscript; `\cite{key}` source).
- **Pipeline harness** at `00-test-paper/`; build at `bin/build`.

---

## A. Per-paper content migration

The substantive work. Segment each `paper-draft.md` from the old workspace into `src/<slug>.md` segments, write `OUT.*.md` manifests, port auxiliary content. Stepwise on paper #1 (with Joseph guiding); paper #2 and #3 follow the recipe.

- [ ] **A1. Paper #1 (B-N4 / 01-tragedy-confident-agent).** Segment `~/src/neurips2026/01-tragedy/paper-draft.md` (~674 lines) into `src/{slug}.md`. Decide segment boundaries (subsection-level vs finer; ASF-style adhoc per restructure-plan §2). Write `OUT.full-paper.md` (everything) and `OUT.neurips-2026-paper.md` (9-page subset). Theorem authoring: B-N4 uses inline-bold pattern (`**Lemma 2.1 (...)**`); migrate to Obsidian `> [!lemma] Title ^anchor` callouts per AUTHORING.md.
- [ ] **A2. Paper #2 (B-CS1 / 02-unified-convergence-rl).** Same recipe; B-CS1 also uses the inline-bold theorem pattern.
- [ ] **A3. Paper #3 (B-N8 / 03-llm-hallucinate-bound).** Same recipe; B-N8 uses 14 theorem-marked blockquotes (`> **Theorem 3.1 (...)** *...*`) — port to Obsidian callouts.
- [ ] **A4. Citation-source migration.** After PIPELINE-TODO §C1 (citation system) lands: run `bin/migrate-cites` on each paper to convert `[Author Year]` source to `\cite{key}` form. Per-author disambiguation pass on ambiguous matches (`[Hintikka 1991]` and similar).
- [ ] **A5. Heading-prefix sweep.** Strip manual `## 3. ` / `### 3.1 ` numbering from segment headings; LaTeX numbers per AUTHORING.md §1.8.
- [ ] **A6. Equation-tag migration.** Replace manual `\tag{N}` in display math with anchored `^eq-name` form per AUTHORING.md §1.7. ~140–200 equations per paper to convert; flag ambiguous cross-references in prose ("see (9a)") for human resolution.
- [ ] **A7. Anonymization sweep.** Per AUTHORING §3.5, four-category check on every segment. Lint scanner from PIPELINE-TODO §B4 should be running by then; this pass verifies and fixes any flagged hits.

## B. Per-paper directory scaffolding

Each submodule needs the standard subdirs (per the original restructure-plan §3).

- [ ] **B1. Per-paper subdirs.** `audits/` (audit landing), `out/` (build artifact landing, gitignored), `spikes/` (temporary investigations), `simulations/` (sim code — B-N4 only paper with this), `results/` (raw empirical results — B-N4 only). Add to each submodule's `.gitignore`.
- [ ] **B2. Per-paper trackers.** `OUTLINE.md` (paper plan + section budget + audit findings), `LOG.md` (append-only history). Port from old workspace where useful; freshen for the new structure.
- [ ] **B3. Per-paper `meta.md`** with title / anonymized author block / abstract.
- [ ] **B4. Per-paper `refs.bib`** vs shared `common/refs.bib` — TBD. Old workspace's `common/refs.bib` (164 entries) is shared. Per-paper bibs are cleaner for submodule independence; shared bib is easier to maintain. Decide before A4 (citation migration).

## C. Auxiliary content

- [ ] **C1. Port prior-art research** from each old `<paper>/prior-art/` directory (Undermind queries + reports + positioning syntheses).
- [ ] **C2. Port simulation code** for B-N4 — `~/src/neurips2026/01-tragedy/sim/` → `01-tragedy-confident-agent/simulations/`.
- [ ] **C3. Port audit relics** from each old `<paper>/_archive/` to the new submodule's `_archive/`. Use `git mv` to preserve provenance where possible (will need history-rewrite incantation since the archive is moving across repos — alternatively, just commit fresh in the new repo with a note pointing to the old SHA).

## D. Doc consolidation (was PIPELINE-TODO §D1)

Multiple agent-facing docs at the umbrella; old workspace has more. Time-box short (Joseph's framing — "in a short time") so consolidation doesn't sprawl.

- [ ] **D1. Inventory current docs** at the umbrella (`AGENTS`, `AUTHORING`, `MIGRATE-TODO`, `PIPELINE-TODO`, `REFS-AND-CITATIONS`, `README`, `_archive/README`) plus old workspace (`STYLE`, `PRAXES`, `CLAUDE`, `HANDOFF`, `common/neurips-main-track-handbook.md`, `common/neurips-guide.md`, `common/metadata-conventions.md`).
- [ ] **D2. Decide canonical structure** — which docs live here, which stay in old workspace as historical, what gets symlinked. Rough proposal:
  - `AGENTS.md` — process / language / rubocop / agent-coordination patterns. Canonical here.
  - `AUTHORING.md` — paper-segment authoring rules. Canonical here.
  - `MIGRATE-TODO.md` — this file. Canonical here.
  - `PIPELINE-TODO.md` — build/tooling backlog. Canonical here.
  - `LOG.md` — append-only history. Create here, port relevant entries from old `~/src/neurips2026/LOG.md`.
  - `PRAXES.md` — working principles. **Decide:** port (one canonical), reference (link from AGENTS), or re-derive subset for AGENTS.md.
  - `STYLE.md` — prose-style conventions. **Decide:** content already largely folded into AUTHORING.md §2/§3; either delete or keep as a reference for things not in AUTHORING (em-dash unicode discipline, etc.).
  - `CLAUDE.md` / `GEMINI.md` — symlinks to `AGENTS.md`.
  - NeurIPS reference docs (`common/neurips-*.md`, `common/metadata-conventions.md`) — port to umbrella's `common/` or leave in old workspace as reference.
- [ ] **D3. Symlink CLAUDE.md / GEMINI.md → AGENTS.md** (Joseph's earlier framing: "we'll symlink in a little bit").
- [ ] **D4. Add LOG.md** at umbrella root for append-only project-level history.
- [ ] **D5. Trim AGENTS.md** if appropriate after the consolidation pass — should be the minimum a fresh agent needs on cold start.

## E. Old-workspace retirement (eventually)

- [ ] **E1. Decide retirement timing.** When all three submodules are content-complete and the new umbrella is the canonical source of truth, retire `~/src/neurips2026/`. Move to `~/src/_neurips2026-archive/` or equivalent. Keep available for reference; stop modifying.

---

## Reference: completed structural-shell items

The structural shell of the umbrella is in place; these items don't need redoing. Listed here so the work that DID happen is visible without having to dig into archived files.

- ✓ Umbrella git-init at `~/src/neurips/` with `main` branch.
- ✓ Three GitHub repos created and initial-committed.
- ✓ Three submodules wired into the umbrella at `0N-{slug}/`.
- ✓ Three temporary `~/src/paper-{slug}/` staging dirs deleted (submodule checkouts are canonical).
- ✓ NeurIPS LaTeX template + sty + checklist copied to `common/`.
- ✓ AGENTS.md + .rubocop.yml + Gemfile/Gemfile.lock with rubocop-tablecop pinned.
- ✓ AUTHORING.md (paper-segment rules).
- ✓ REFS-AND-CITATIONS.md (citation rendering decision).
- ✓ `00-test-paper/` pipeline harness with idiomatic exemplar segments.
- ✓ `bin/build` Phase A — kramdown parser extension, `00-test-paper/out/test.pdf` builds clean.
- ✓ `_archive/` scaffold with move-via-git-mv policy README.

Detailed history in `_archive/MIGRATION.md` (commit-by-commit migration log) and `_archive/restructure-plan.md` (original sprint plan).
