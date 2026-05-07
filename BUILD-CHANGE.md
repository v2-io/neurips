# BUILD-CHANGE.md — `bin/build` interface refactor (2026-05-06)

*Heads-up for per-paper agents returning from a pause. The build pipeline got a substantial interface refactor; nothing about how you author segments has changed, but the artifacts and the CLI are different. This doc is the orientation.*

---

## What changed in one paragraph

Build artifacts moved from `<paper>/out/` to `<paper>/.build/<stem>/` (per-manifest subdirs, `.gitignored`). The build now auto-emits the per-paper `.bib` from umbrella `refs/entries/*.yml` before each `lualatex` run — your existing `<paper>/refs.bib` is no longer read or written. PDFs land at `<paper>/<stem>.pdf` (canonical, your call to track or not), with the previous successful build snapshotted to `<paper>/<stem>.prior.pdf` (gitignore-worthy) before each run. Page-budget reports inline on every successful build. CLI is cwd-aware and supports multi-manifest builds with failure isolation.

---

## New things in your working tree

After your first `bin/build` invocation post-refactor:

| Path | Purpose | Recommendation |
|:-----|:--------|:---------------|
| `<paper>/.build/<stem>/` | All ephemeral build artifacts (`.tex`, `.aux`, `.bbl`, `.log`, `.references.bib`, intermediate `.pdf`). Per-manifest subdir so multiple manifests don't conflict. | Add `.build/` to your `.gitignore`. |
| `<paper>/<stem>.pdf` | Copy of the build's PDF on success. Canonical reference output. | Track if you want repo visibility of the PDF (recommended for the manifest you treat as rc1). Otherwise gitignore. |
| `<paper>/<stem>.prior.pdf` | Snapshot of the previous successful build's PDF, taken right before the current build starts. Lets you compare against last-known-good even if the current build fails. | Add `*.prior.pdf` to your `.gitignore` — local-convenience artifact, not for the repo. |
| `<paper>/<stem>.extracted.bib` | Repo-visibility snapshot of the bib that bibtex actually used. Naming is explicit-on-purpose so it's clear by construction that it's a build artifact (canonical edits go through `bin/refs add` / `refs/entries/<key>.yml`). | Track for diff visibility — lets PR reviewers see what bib content the build used without needing the umbrella checked out. |

---

## Things that are now orphans

**`<paper>/refs.bib`** — the build no longer reads it or writes it. It just sits there, stale, until you remove it. The replacement is `<paper>/<stem>.extracted.bib` (above). When you remove `refs.bib`:

- Per-paper agents shouldn't have been hand-editing this file in the first place. Canonical edits to bibliography entries go through `bin/refs add <key>` / `refs/entries/<key>.yml`, never to per-paper `refs.bib`. The new flow makes that boundary clean.
- Safe to remove with `git rm <paper>/refs.bib` whenever convenient. No build dependency.

**`<paper>/out/`** — the build no longer writes here. Old artifacts are stale. Safe to remove with `git rm -r <paper>/out/` whenever convenient. The directory contents include the previously-tracked `<stem>.tex`; that's also derived (now in `.build/<stem>/<stem>.tex`) and doesn't need to be tracked.

**Recommended one-time cleanup** (per submodule, when you have a moment):

```bash
cd <paper>
git rm -r out/                  # gone, derived in .build/<stem>/ now
git rm refs.bib                 # gone, replaced by <stem>.extracted.bib
echo '.build/' >> .gitignore
echo '*.prior.pdf' >> .gitignore
git add .gitignore <stem>.extracted.bib   # plus <stem>.pdf if you want it tracked
git commit -m "Adopt .build/ build-pipeline refactor"
```

You don't have to do this all at once. `out/` and `refs.bib` are inert; they don't affect builds. Whenever you next touch the submodule for substantive work is fine.

---

## New CLI shape

```
bin/build                                # cwd-aware: if cwd is a paper-dir, build all OUT.*.md manifests
bin/build <paper-dir>                    # all OUT.*.md manifests in <paper-dir>
bin/build <paper-dir> <manifest-stem>    # specific manifest in <paper-dir>
bin/build <manifest-stem>                # specific manifest in cwd (cwd must be a paper-dir)
bin/build --all                          # every paper-dir under umbrella, every manifest
```

The cwd-aware default is the new ergonomic — `cd 02-unified-convergence-rl && bin/build` builds everything in 02 with one command. Multi-manifest builds use try/rescue per `(paper, manifest)` pair, so a fail in one doesn't poison the rest; a summary at end shows what passed and what failed, exit nonzero iff anything failed.

---

## Page-budget reports inline

After each successful build, `bin/page-budget` runs automatically and prints the result. The previous overcount-by-1-or-2pp issue (when bibliography sat between body and appendix and didn't emit a TOC entry) is fixed: tier 1.5 now subtracts an estimated bibliography region from the main-text count using the `\bibcite` count from `.aux` and a ~30-entries-per-page heuristic. Report shows up like:

```
01-tragedy-confident-agent/neurips-2026-paper: 10pp main-text  [OVER: +1 vs 9-pp]
  (appendix-minus-bib(2pp est. for 49 refs) starts p11)
    section progression:
      §  1  starts p  1  main  Introduction
      ...
```

If you want a budget report without rebuilding, `bin/page-budget` standalone still works, now reading from `.build/<stem>/<stem>.aux`.

---

## The bib-database boundary just got load-bearing

The auto-emit-on-build flow makes `refs/entries/*.yml` (umbrella) the actual source of truth. Pre-refactor, the build silently used your local `<paper>/refs.bib` — so if you had an entry in local `refs.bib` that wasn't in `refs/entries/`, the build worked anyway. Post-refactor, `bin/refs emit` regenerates the bib from `refs/entries/`, and any orphans (entries in your local `refs.bib` that aren't in the umbrella database) surface as `[?]` placeholders in the PDF + lint warnings at build time.

**If your build now reports unresolved cite-keys** that previously rendered fine: you almost certainly have entries in your local `refs.bib` that never made it into `refs/entries/`. Recipe per missing key:

```bash
bin/refs add <key>
# (paste the BibTeX from your local refs.bib at the prompt, or fetch fresh)
```

If you don't recognize the key and it's not in your local `refs.bib` either, it might be a typo — search source for `\cite{<key>}` and figure out what was intended.

(Paper 03 hit this on three keys when the new flow landed: `tsybakov-2009-nonparametric`, `ay-2017-information` were in 03's local `refs.bib` but not the umbrella; `lie-sullivan-teckentrup-2017` doesn't exist anywhere and was already flagged in 03's TODO as a known migration gap.)

---

## What didn't change

- Authoring conventions in `AUTHORING.md` are unchanged. Segments, manifests, callouts, cross-refs, citations — same source-side rules.
- `bin/refs` storage layer settled in a separate decision earlier today (kept hardened YAML — see `refs/README.md` "Design decisions: why per-entry YAML, not sqlite" and the `safe_write` contract section).
- Per-paper directory structure is unchanged (`src/`, `meta.md`, `OUT.*.md`, `audits/`, etc.).
- Build's lint-anonymization, kramdown→LaTeX, theorem-callout, cleveref appendix-aliasing, hyperref draft-mode-when-unresolved are all unchanged.

---

## Reference

- `AUTHORING.md` §5.6 — full new build-pipeline synopsis (what the build handles + how to ask for more)
- `AGENTS.md` §1 — cwd-aware CLI hint
- `refs/README.md` — bib database schema + safe_write atomicity contract
- `PIPELINE-TODO.md` §F1 (auto-emit on build, done) + §E3 (page-budget tool, sharpened + integrated)
- The umbrella commits that landed the refactor: `cb64428` (refs --output), `17cb12e` (bin/build refactor + 00-test-paper canonical bib keys), `9160dce` (page-budget T1.5 sharpening + path migration), `43a47da` (00-test-paper cleanup), `d24c9e8` (doc updates)

---

*Questions, surprises, or things that don't work the way you expected → atomic-append a flag to `PIPELINE-TODO.md ## Inbox` per `AGENTS.md` §5.1. The build-pipeline owner reads the inbox.*
