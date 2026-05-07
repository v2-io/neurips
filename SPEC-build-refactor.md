# SPEC — `bin/build` interface + output-layout refactor

*Drafted 2026-05-06 by build-pipeline agent (foreground), in collaboration with Joseph. To be implemented by a fresh Opus agent. The `bin/refs` storage layer is out of scope (settled separately by `1623255` / `3f3a215`). This spec is the build-side companion.*

---

## Why

Current state has three friction points:

1. **`<paper-dir>/out/` mixes committed (`.tex`) and gitignored (`.pdf`, LaTeX intermediates)** — muddy, no clean "ephemeral" separation.
2. **`bin/refs emit` is manually invoked** before `bin/build` reads the per-paper `refs.bib`. Stale `refs.bib` failure mode hit once today (lie-sullivan-teckentrup transient at ~14:50). PIPELINE-TODO §F1 tracked the auto-emit-on-build follow-up; this is the moment.
3. **Build-time tooling is split.** Page-budget runs separately. No unified "build everything and report status." No multi-paper resilience (a fail in paper 2 doesn't poison paper 3 today, but only because each is a separate invocation).

Joseph's framing: clean separation between repo state (sources + reviewable artifacts) and build state (everything derived, ephemeral, regenerable).

---

## Scope

This refactor changes:

- `bin/build` CLI shape and default behavior.
- Per-paper output-directory layout.
- The auto-emit-refs path (`bin/build` calls `bin/refs emit` itself).
- Page-budget integration on successful build.
- Per-paper `.gitignore` updates.

Out of scope:

- `bin/refs` storage layer (settled — hardened YAML).
- `bin/page-budget`'s page-detection algorithm beyond a small sharpening (see §6).
- `bin/migrate-cites` (near-deprecated; leave alone).
- The kramdown→LaTeX converter (no source-format changes).

---

## CLI shape

### Synopsis

```
bin/build                                # cwd-aware default
bin/build <paper-dir>                    # all OUT.*.md manifests in <paper-dir>
bin/build <paper-dir> <manifest-stem>    # specific manifest in <paper-dir>
bin/build <manifest-stem>                # specific manifest in cwd (must be a paper-dir)
bin/build --all                          # every paper-dir under umbrella, every manifest
```

### Argument resolution

1. **No args.** Check if `$PWD` is a paper-dir (heuristic: contains a `meta.md` AND at least one `OUT.*.md`). If yes, build all manifests in `$PWD`. If no, fail with a helpful error listing the candidate paper-dirs (e.g., `0?-*` glob at the umbrella) and the syntax forms above.
2. **One arg.** If it's a directory that's a paper-dir, build all manifests in it. If it's a manifest stem (no slash, matches an `OUT.<stem>.md` in `$PWD`), build that single manifest in `$PWD`. If neither, fail with usage.
3. **Two args.** First is paper-dir, second is manifest-stem. Same as today's `bin/build <paper-dir> <manifest-stem>`.
4. **`--all`.** Every paper-dir directly under umbrella (`0?-*`), every `OUT.*.md` manifest in each. Failure-isolated per `(paper, manifest)` pair.

### Manifest naming

Stays as `OUT.<stem>.md` (dot, not dash — current convention preserved). The stem is what becomes the basename for build outputs. Paper-name extraction regex: `OUT\.([^/]+)\.md`.

### Failure isolation

When `bin/build` builds more than one `(paper, manifest)` pair (any of: `<paper-dir>` no-stem, `--all`, cwd-default-with-multiple-manifests), each pair runs in its own try/rescue. Failures are accumulated; the run continues. At end, print a summary listing successes and failures, exit nonzero iff any failure. Single-pair invocations propagate errors normally.

---

## Output layout — per-paper `.build/`

### Directory shape

```
<paper-dir>/
├── .build/                            # gitignored; everything ephemeral
│   ├── <stem>/                        # one subdir per manifest
│   │   ├── <stem>.tex                 # rendered LaTeX (was: out/<stem>.tex, formerly committed)
│   │   ├── <stem>.references.bib      # auto-emitted by bin/refs; what bibtex reads
│   │   ├── <stem>.pdf                 # compiled PDF (canonical build output)
│   │   ├── <stem>.aux, .bbl, .blg, .log, .toc, .out   # LaTeX intermediates
│   │   └── <stem>.prior.tex           # snapshot of previous .tex (optional; defer)
│   └── <other-stem>/...
├── <stem>.pdf                         # tracked-or-gitignored per author choice
├── <stem>.prior.pdf                   # gitignored; last successful build's pdf
├── <stem>.extracted.bib               # repo-visibility snapshot of <stem>.references.bib (committed; "extracted" naming explicit-on-purpose so authors don't edit it)
├── meta.md                            # unchanged
├── OUT.<stem>.md                      # manifests, unchanged
├── src/                               # segments, unchanged
└── ...
```

### Lifecycle

For each `(paper, manifest)`:

1. **Pre-build.** If `<paper>/<stem>.pdf` exists, move it to `<paper>/<stem>.prior.pdf` (overwriting any existing `.prior`).
2. **Setup.** `mkdir -p <paper>/.build/<stem>/`.
3. **Refs emit.** `bin/refs emit <paper>` — but writes to `<paper>/.build/<stem>/<stem>.references.bib`, not to `<paper>/refs.bib`. Bibinputs points at `.build/<stem>/`.
4. **Render.** Kramdown → LaTeX → write to `.build/<stem>/<stem>.tex`. All existing build logic (mask_math_pipes, mask_cite_postnotes, resolve_unresolved_refs, anonymization lint, PREAMBLE_ADDITIONS, etc.) unchanged.
5. **Compile.** lualatex → bibtex → lualatex → lualatex, all within `.build/<stem>/`. TEXINPUTS includes `<umbrella>/common:<paper>:.build/<stem>:` so the sty/template + segment-relative paths still resolve.
6. **On success.** Copy `.build/<stem>/<stem>.pdf` → `<paper>/<stem>.pdf`. Copy `.build/<stem>/<stem>.references.bib` → `<paper>/<stem>.extracted.bib`. Run page-budget against `.build/<stem>/<stem>.aux`; print stats.
7. **On failure.** Leave `.build/<stem>/` intact for diagnosis (logs, partial pdf if any, etc.). `<paper>/<stem>.pdf` is gone (moved to `.prior` in step 1); `<paper>/<stem>.prior.pdf` is the last-known-good. Print fail summary with path to `.build/<stem>/<stem>.log`.

### Git tracking — what the build does and doesn't touch

**The build NEVER touches `<paper>/refs.bib` or `<paper>/out/`.** Both become orphans of the refactor:

- `<paper>/refs.bib` is no longer read (build reads `.build/<stem>/<stem>.references.bib` instead) and no longer written. It just sits there, stale, until the per-paper agent decides to remove it. The new `<paper>/<stem>.extracted.bib` is the replacement repo-visibility artifact.
- `<paper>/out/` is no longer written. It just sits there until the per-paper agent decides to remove it.

**Per-paper submodule territory is off-limits to this refactor.** No `.gitignore` edits inside `01-tragedy-confident-agent/` / `02-unified-convergence-rl/` / `03-llm-hallucinate-bound/`. No commits inside submodules. No file deletions inside submodules. Per-paper agents own their submodule's git state; they'll clean up `out/` and `refs.bib` on their own schedule.

**What the build DOES write into submodule working trees** (this is just the build doing its job, not a git-side migration):

- `<paper>/.build/<stem>/...` — gitignore-worthy. Per-paper agents can add `.build/` to their `.gitignore` whenever they get to it; in the meantime `git status` will show it as untracked, which is harmless.
- `<paper>/<stem>.pdf` — author choice to track or gitignore.
- `<paper>/<stem>.prior.pdf` — gitignore-worthy. Same lazy-cleanup story as `.build/`.
- `<paper>/<stem>.extracted.bib` — author choice to track or gitignore (recommended track for repo-visibility of which bib entries the paper's build actually used).

**Transitional state** that per-paper agents will encounter on first build with the new tooling:

- New: `.build/<stem>/`, `<stem>.pdf`, `<stem>.prior.pdf`, `<stem>.extracted.bib` appear in their working tree.
- Stale: existing `<paper>/out/` and `<paper>/refs.bib` continue to exist but are ignored by the build. They can be removed at any time without affecting builds.

**00-test-paper is umbrella territory** (it lives at the umbrella root, not a submodule). The implementing agent CAN clean up `00-test-paper/out/` and `00-test-paper/refs.bib` directly as part of the refactor, since 00-test-paper has no per-paper-agent owner. Note that 00-test-paper's existing `refs.bib` has non-canonical keys (`boyd-1994-lmi` vs umbrella's `boyd-ghaoui-feron-balakrishnan-1994-lmi`); to avoid `bin/refs emit` falling back to umbrella for missing keys, either (a) update `00-test-paper/src/` to use the canonical keys, or (b) ensure all keys 00-test-paper cites exist in `refs/entries/`. The implementing agent should pick whichever is cleaner.

---

## Auto-refs-emit

`bin/build` calls `bin/refs emit <paper-dir>` as step 3 above, but with a target-path argument so the bib lands in `.build/<stem>/<stem>.references.bib` instead of `<paper>/refs.bib`. This requires extending `bin/refs emit` to accept an output-path override:

```
bin/refs emit <paper-dir>                      # default: <paper-dir>/refs.bib (current behavior)
bin/refs emit <paper-dir> --output <path>      # write to <path> instead
```

The default behavior preserves `bin/refs emit <paper>` as a useful standalone command (agents can still pre-emit if they want), while the build uses the override path.

After build success, the build copies `.build/<stem>/<stem>.references.bib` → `<paper>/<stem>.extracted.bib` (a tracked artifact for git-diff visibility). Document in `refs/README.md` that `<stem>.extracted.bib` is a build artifact named explicitly so authors don't edit it; canonical edits go to `refs/entries/<key>.yml`.

---

## Page-budget integration on success

After each successful build, run `bin/page-budget <paper-dir> --manifest <stem>` and print the result inline as part of the build's success line. Path resolution: today `bin/page-budget` reads `<paper>/out/<stem>.aux`; needs updating to read `<paper>/.build/<stem>/<stem>.aux`.

### Sharpening the references-region detection

Today's `bin/page-budget` overcounts main-text by 1–2 pages when bibliography sits between body and appendix and tier-2 ("References" TOC entry) doesn't fire. Sharpening: also parse `\bibcite` entries from `.aux` to identify the bibliography page range; subtract from main-text count when an explicit Tier-2 marker is missing. Half an hour of work, makes the auto-stats accurate. Worth doing as part of this refactor.

---

## Migration steps — umbrella-only

This refactor stays at the umbrella. No git operations inside per-paper submodules. The implementing agent's working scope is `~/src/neurips/` plus `00-test-paper/` (which is umbrella territory, not a submodule).

1. Extend `bin/refs emit` with `--output <path>` override.
2. Refactor `bin/build` per the §"CLI shape" + §"Output layout" sections.
3. Sharpen `bin/page-budget`'s tier-2 detection.
4. Wire page-budget integration into `bin/build`.
5. Update `00-test-paper` if needed to use canonical bib keys (so the new `bin/refs emit` path works without falling back to a hand-curated local override). Remove `00-test-paper/out/` and `00-test-paper/refs.bib` after the new build proves clean.
6. Verify all four papers build clean under the new flow (read-only against per-paper submodules — just invoke `bin/build` and check the produced artifacts):
   - `bin/build 00-test-paper test`
   - `bin/build 01-tragedy-confident-agent full-paper` (and `neurips-2026-paper`, `review`)
   - `bin/build 02-unified-convergence-rl full-paper` (and `neurips-2026-paper`, `full-paper-re`)
   - `bin/build 03-llm-hallucinate-bound full-paper` (and `neurips-2026-paper`, `re-paper`)
   - `bin/build --all` from umbrella
   - `bin/build full-paper` from inside `01-tragedy-confident-agent/` (cwd-aware path)
   - **Read-only verification** — each build will write `.build/<stem>/`, `<stem>.pdf`, `<stem>.extracted.bib`, `<stem>.prior.pdf` into the submodule's working tree. That's the build doing its job and is fine. The implementing agent should NOT git-add or commit anything inside submodules; per-paper agents handle their own git state.
7. Update `bin/build`'s comment header + `AGENTS.md` and/or `AUTHORING.md` §5.6 ("What the build pipeline handles") with the new synopsis and the orphan-artifact note (existing `out/` and `refs.bib` are no longer touched by the build; per-paper agents can clean up at their leisure).
8. Drop a per-paper-inbox notification — append a short note to each of `01-tragedy-confident-agent/TODO.md`, `02-unified-convergence-rl/TODO.md`, `03-llm-hallucinate-bound/TODO.md` saying: "Build interface refactored at umbrella commit `<hash>`. New artifacts in `<paper>/.build/<stem>/`. New tracked artifacts: `<stem>.pdf`, `<stem>.extracted.bib`. Existing `out/` and `refs.bib` are no longer read or written by the build — orphans you can clean up whenever convenient. Note: agents shouldn't have been hand-editing `refs.bib` directly; canonical edits go through `bin/refs add` / `bin/refs emit`. Recommended `.gitignore` additions when you next touch the file: `.build/` and `*.prior.pdf`." This is a one-paragraph drop into each submodule's TODO; the implementing agent CAN make this commit because it's a coordination artifact, BUT — pause-the-agents-first protocol applies (Joseph confirmed before launch). Keep it pathspec-bounded to just `TODO.md`.
9. Update `PIPELINE-TODO.md`: §F1 (auto-emit on build) → marked done with the new commit hash; §E3 (page-budget tool) gets the sharpening + integration noted; §A4 (NeurIPS checklist wiring) unaffected.

---

## Open questions for the implementing agent

- The `bin/refs emit --output <path>` override: should it implicitly create the parent directory? (Yes, suggest.)
- The page-budget bibliography-region sharpening: parse `\bibcite` count + assume ~30 entries/page, or actually find page numbers via `\hyper@anchor` labels emitted by hyperref? The latter is more accurate but only works when hyperref's labels are present (which they aren't under draft mode). Probably the `\bibcite` heuristic is fine and matches the rest of the tool's heuristic-friendly nature.
- For the cwd-aware default behavior (no args, in a paper-dir), what's the right error message when cwd is NOT a paper-dir? Suggest listing the available paper-dirs at the umbrella (`0?-*` glob) plus the syntax forms.
- Existing `<paper>/refs.bib` files: agents may currently have in-flight uncommitted edits to these. Migration step 8's removal should be done after pulling latest from each submodule and confirming no uncommitted local changes — or surface clearly to the agent that they may have local work to preserve.

---

## Voice + working notes for the implementing agent

- This is a substantial multi-step refactor. Commit incrementally per migration step (1 commit per step in the §"Migration steps" list, where it makes sense). Don't lump CLI rewrite + path migration + page-budget integration into one commit.
- Use `git commit -- <pathspec>` form to bound scope, especially in submodules where per-paper agents may have in-flight work.
- Run `bundle exec rubocop bin/build bin/refs bin/page-budget` after each meaningful change. Style is gating (rubocop + rubocop-tablecop).
- The four-paper smoke test is the acceptance gate. If all four build clean post-refactor, the migration is done.
- Truth above all (AGENTS.md §6). If you discover a design choice in this spec that's wrong (e.g., the cwd-aware behavior has an edge case I missed), push back; don't silently work around. The spec is a starting point, not a contract.

---

## Read these to orient

- `~/src/neurips/bin/build` — current implementation
- `~/src/neurips/bin/refs` — has `safe_write` (just landed) + the canonical `emit` verb
- `~/src/neurips/bin/page-budget` — three-tier detection logic
- `~/src/neurips/refs/README.md` — recently updated (sqlite trade study + safe_write contract); the section on `<stem>.extracted.bib` should land here
- `~/src/neurips/AUTHORING.md` §1.10–§1.12 (appendices / references / checklist) for what manifest types drive
- `~/src/neurips/PIPELINE-TODO.md` §A, §C, §E, §F for context on what's been considered before
- `~/src/neurips/AGENTS.md` for Ruby conventions, rubocop discipline, peer voice

---

*This spec captures the agreed design as of 2026-05-06. The implementing agent has full authority to push back on any specific choice if there's a better path; truth above all.*
