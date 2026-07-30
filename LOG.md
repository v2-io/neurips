# LOG.md — Project history

*Append-only. Reverse-chronological (newest first). Never edit prior entries — LOG is the permanent record. Future agents reading this should be able to reconstruct what was tried, what worked, what failed, and why.*

For active backlog see `MIGRATE-TODO.md` (restructure / per-paper / docs) and `PIPELINE-TODO.md` (build / formatting / authoring tooling). Per-paper history lives in each submodule's `LOG.md`.

---

## 2026-07-29 (later) — Post-review sync across all three papers; as-submitted state pinned

Follow-on to the artifact refresh earlier today, after reading the returned reviews. **No paper content touched** — NeurIPS forbids revisions during the response period, and the original submission is the basis for the decision. Everything here is bookkeeping so the author response can cite the submitted PDFs accurately, plus the code rot that two idle months plus a last-minute submission sprint left behind.

**The as-submitted state is now pinned, in each submodule.** Tag `submitted/neurips-2026` (01 `091a8cd`, 02 `38463e2`, 03 `dd50f7f` — each the last content commit before submission), plus a frozen `submitted-neurips-2026.pdf` blind build in each paper dir under a stem **no manifest owns**, so `bin/build` cannot overwrite it.

This closes a real gap rather than a tidiness one. The tracked `<stem>.pdf` in each repo is regenerated on every build — each was overwritten *twice today alone* — so it was never a record of what reviewers read. And "just rebuild from the tag" is not a substitute: verified today that `bin/build` output is **not byte-reproducible** (rebuilding 02 and 03 from identical source produced different bytes with byte-identical extracted text — PDF creation timestamp / file ID). The frozen copy is the artifact; the tag is how you know what it came from.

*Basis for treating current source as as-submitted:* no source commits between 2026-05-07 and today except the 2026-05-22 `meta.md` author-info edits, which only affect `--preprint` / `--final` renders. Cross-checked per paper by word-frequency comparison of fresh blind builds against the stamped non-anon copies in `~/Documents/submitted-papers/`: every content phrase matches; vocabulary differences confined to author block, stamp banner, preprint footer. Page counts identical (38 / 31 / 37). Residual caveat kept rather than buried: OpenReview records all three as *modified 27 May 2026*, and whether that was metadata-only or a PDF re-upload is not determinable from here — no source commit exists in that window, so a re-upload came from this same source, but the authoritative artifact is the PDF downloadable from OpenReview, and dropping those in alongside the frozen copies would remove the last inference.

**Rot found and fixed** (details in each submodule's LOG):

- **03 — title rot, three titles deep.** Last-second 2026-05-07 edits took the title from *"An Upper Bound via Coupling and Ambiguity"* → *"An Information-Geometric Upper Bound on Goal-Coupling Displacement"* (`ab759d6`) → *"An Upper Bound on Goal-Coupling Displacement"* (`280762f`, submitted). The final one reached `meta.md` and the PDF but never the README, which still advertised the original. Fixed, with a title-history note so no future agent corrects it backwards. **Still open and outside every repo: the OpenReview submission form field itself still shows the original title.** Author-side fix; flagged, not resolved.
- **03 — manifest header stale.** Called itself `OUT.re-paper.md`, described the `src/re/` reshape as pending. The reshape completed; the `src/re/` → `src/` rename it anticipated never happened, and `src/re/` is simply the live segment dir. Now says so.
- **03 — Bibliography row pointed at a file that never existed** (`src/references.md`). Harmless: `bin/build`'s bibliography branch short-circuits before `render_segment`, emitting `\bibliography{<stem>.references}` without reading the path — references always rendered fine. But a row pointing at nothing invites someone to author a manual list there. Stub created, matching 01's existing convention and comment.
- **02 — a 76-line manual bibliography had been dead since before submission.** `src/re/10-references.md` still said *"until then, manual list"* long after the natbib switch landed (the PDF renders numbered natbib references — verified against the built PDF). Never rendered, so it cost nothing in the paper; the risk was someone trusting or maintaining it. Archived to `_archive/references-manual-list-2026-05-07.md` and replaced with the stub, kept because several entries carry journal / publisher / edition detail better than the matching `refs/entries/` YAML — a third data point for §F7 alongside today's stray relata emission.
- **02 — README advertised two manifests that do not exist** (`OUT.full-paper.md`, `OUT.neurips-2026-paper.md`, both migration-era and archived) and said "currently bootstrapping." One live manifest.
- **01 needed the least** — title never drifted, README accurate, and the Bibliography-stub convention originated there. It got the tag, the frozen PDF, and an URGENT author-response section in `TODO.md`.

**Reviews are on disk and deliberately untracked.** `reviews/neurips-2026/` holds the OCR'd review pages (`marker_single --force_ocr`), the saved OpenReview page PDFs, the notification email, and a README index with ratings, phase deadlines, response rules, and the two open technical questions. It is **gitignored**: this umbrella and all three paper submodules are **public** on GitHub, and venue reviews are confidential through the discussion period. Tracked files carry paraphrased technical substance only — no reviewer pseudonyms, no verbatim review text. That rule was written *after* first violating it: reviewer pseudonyms and a verbatim clause went into 01's `LOG.md` and `TODO.md` and were pushed before being caught and paraphrased (`f7a9a32`). They remain in that repo's history; a history rewrite across three public repos was judged disproportionate given the pseudonyms are venue-assigned and identify no one. Noted here because the next person to add review material needs the rule *and* the reason it exists.

**Where the papers stand.** 01: **4 / 3 / 3**, balanced meta-review — genuinely in play, and most reviewer objections are answered by appendix content the reviewers did not find. 03: 3 / 1 / 2, negative meta-review that nonetheless closes on what would strengthen the work. 02: 3 / 3 / 2, with the AC judging that the clarity and precision problems require rewriting beyond what the response period allows — effectively a reject announced in advance. Batch-level: **8 of 9 reviewers scored clarity "not good" or "poor,"** and every meta-review leads with presentation. That is one systematic finding, not three — the dense named-hypothesis register that carries the epistemic discipline honestly reads to outside reviewers as jargon-padding, and in one case as machine-generated. Worth sitting with before the next submission, because the discipline is right and only its surface is costing us.

Author-visible discussion closes **2026-08-03**; per-paper response work is queued in each paper's `TODO.md`.

---

## 2026-07-29 — Artifact refresh after two idle months; peer reviews arrive; tracked-PDF convention written down

First session in this workspace since 2026-05-22. All three papers went to NeurIPS 2026 in early May and the main peer-review feedback came back today (OpenReview PDFs downloaded to the umbrella root, plus the NeurIPS guidelines email saved). Reviews are **not yet triaged** — that's the next substantive cycle, and none of the work below touches paper content.

**What the working tree was holding.** Every submodule had a dirty tree that turned out to be a single cause: the last build run in each was the 2026-05-22 `--preprint` / `--final` render, so the tracked `<stem>.pdf` (and 01's `<stem>.extracted.bib` pair) had flipped to *non-anonymous*. Rebuilt all four manifests (01 main + 01 review + 02 + 03) with the default flags and committed those instead.

**Convention now stated explicitly, because it wasn't:** *the PDF/`extracted.bib` artifacts tracked in each paper repo are the **blind** build.* The 2026-05-22 entry documents what the flags do but never says which build the repo keeps, and the failure is silent and repeatable — you run `--preprint` for an external copy, the flag isn't sticky, the dirty tree looks like nothing important, and a later `git add -A` publishes de-anonymized PDFs to what are four **public** GitHub repos. Non-anon renders belong in an external distribution dir (`~/Documents/submitted-papers/` is the established one), not here. If you want a non-anon copy committed somewhere, give it a distinct manifest stem rather than overwriting the blind artifact.

**The one substantive delta** in the rebuilds: reference titles now render with their source capitalization ("Dual Adaptive Model Predictive Control", "LMIs" rather than "lmis"), from the brace-protection pass on `refs/entries/`. Page counts and section progressions unchanged; page-budget check still OK at 9pp main text for all three.

**Also:** a stray `bin/relata`-emitted `refs.bib` at `02-unified-convergence-rl/` root is now gitignored (generated artifact; `bin/build` already emits the tracked `.extracted.bib`). Comparing it against the tracked bib produced a small but directional finding for `PIPELINE-TODO §F7` — relata's metadata is *better* where the two disagree — recorded in that item.

Also pushed: the three `meta.md` real-author commits from 2026-05-22 that had been sitting unpushed. No new exposure — real identity is already throughout the pushed public history of all three repos (`LOG.md`, `TODO.md`, 03's `meta.md`), and the repos live under the `v2-io` org by name.

---

## 2026-05-22 — Non-anonymous render flags (`--preprint`, `--final`) + author info hygiene

Added two flags to `bin/build` so the umbrella pipeline can produce non-anonymous renders without hand-editing `common/neurips_2026.tex`:

- `bin/build --preprint` — splices `[preprint]` into the package load (`\usepackage[preprint]{neurips_2026}`). Renders real authors from `meta.md`; adds NeurIPS's "Preprint. Work in progress." footer. Right choice for arXiv-style distribution or for review-but-not-yet-accepted PDFs that should not visually claim accepted status.
- `bin/build --final` — splices `[final]`. Real authors, no preprint footer. NeurIPS reserves `[final]` for accepted camera-ready; only use it when that is true (or layer a clarifying notice on top — that's how the 2026-05-22 `~/Documents/submitted-papers/` non-anon rebuilds added a "SUBMITTED FOR REVIEW — DO NOT REDISTRIBUTE" overlay).
- Both flags share the same splice point as the citation/hyperref `pre_sty_options` (line ~1130 of `bin/build`). Mutually exclusive; if both are set, `--final` wins, matching the sty's own precedence order at `neurips_2026.sty:61`.

`\if@anonymous` in `neurips_2026.sty` handles author suppression at `\@maketitle` time, so real author info in `meta.md` is **safe** for default (blind) builds — the sty replaces `\@author` with "Anonymous Author(s) / Affiliation / Address / email" placeholder text regardless. This is why `meta.md` carrying real author info isn't a double-blind violation in default mode; it only renders when `--preprint` or `--final` is set.

**Hygiene fix landed this cycle:** `01-tragedy-confident-agent/meta.md` carried placeholder anon-author info (`name: Anonymous Author / affiliation: Affiliation pending / email: anonymous@example.org`) — inconsistent with 02/03 which had real info, and unnecessary given the sty's anon-mode handling. Updated all three to Joseph's canonical v2.io form (`Independent Researcher, Vis Veritatis (v2.io), Lehi, USA / joseph.wecker@v2.io`).

**When to use which flag** (decision rule for future agents):

- Submitting to NeurIPS (or any double-blind venue): no flag. Default builds anonymously regardless of `meta.md`.
- Distributing the work pre-decision (arXiv preprint, sharing with collaborators, audit copies): `--preprint`. Author info appears, preprint footer reminds readers it isn't accepted.
- Camera-ready for an accepted paper: `--final`.
- Building "submitted-but-not-yet-accepted" non-anon copies for trusted-distribution archives: `--final` plus an external review/redistribute notice (PDF overlay or banner stamp). The 2026-05-22 `~/Documents/submitted-papers/.tmp/stamp.tex` is one such overlay implementation.



While migration agent #1 spins up, knocked through the most-blocking PIPELINE-TODO items so they land in cleaner working conditions:

- **`bin/migrate-cites`** (`3f98329`) — sweeps `[Author Year]` / `Author [Year]` patterns in segment source against `refs/entries/`, proposes `\cite{}` / `\citet{}` replacements, flags ambiguous and missing for human disambiguation. Dry-run by default; `--apply` rewrites in place. Closes `PIPELINE-TODO §C1.4`, the most-blocking piece for per-paper content migration.
- **Bold-prefix paragraph headings** (`56b0960`) — `convert_p` auto-converts `**Term.** body...` at paragraph start to `\paragraph{Term} body...` per AUTHORING §1.9. Limited to top-level paragraphs (children of `:root`); list-item / blockquote / table-cell paragraphs skipped (would emit `\item{} \paragraph{...}` and break LaTeX structure — caught by build failure on the test paper's numbered lists).
- **Manual heading numbering + `\tag{N}` lint** (`a5756c5`) — `convert_header` warns when title starts with `N.` / `N.M`; `convert_math` warns on `\tag{}` / `\tag*{}`. Migration agents see warnings during their build cycle and strip during their pass.
- **Anchored equations + `eq-` cross-ref routing** (`1468878`) — `$$ ... $$ ^eq-name` source rewrites to `\begin{equation}\label{eq-name}...\end{equation}` (numbered) at the segment-prep level; multi-line `aligned` content becomes `\begin{align}` (also numbered). `[[#^eq-name]]` cross-refs route to `\eqref{}` (parenthesized number) instead of `\Cref{}` (typed noun) when the anchor starts with `eq-`. Closes AUTHORING §1.7 + §2.2 conventions.
- **Segment-side anonymization scanner** (`c7a8d60`) — loads `refs/deny-list.yml` (DOIs, authors, proper-nouns), scans every segment's source before kramdown, surfaces violations through `@lint_findings`. Build-side complement to `bin/refs lint`.

Net `PIPELINE-TODO` state after this stretch: §A1–A3 done; §B1–B5 done; §C1.4 + §C4 done; remaining open: A4 (real NeurIPS checklist wiring), A5/A6 (visual verifications), B6 (`[!figure]` image-link resolution), C2/C3/C5/C6 (refs/citation-form-switch / cleveref audit / paragraph interaction), E1–E5 (old-workspace tooling ports), F1–F5 (bib database deferred follow-ups).

Migration agent arriving now has all the convention-enforcement infrastructure they need.

---

## 2026-05-05 — Umbrella created; pipeline + bib system in place; docs consolidated

**Umbrella structure landed.** New repository at `~/src/neurips/` with three per-paper submodules backed by independent GitHub repos (`v2-io/paper-tragedy-confident-agent`, `v2-io/paper-unified-convergence-rl`, `v2-io/paper-llm-hallucinate-bound`). Hybrid numbered + multi-word slug naming (`0N-{slug}/` inside the umbrella, `paper-{slug}` on GitHub). Migration recipe captured in `_archive/MIGRATION.md` (preserved for provenance) and condensed in `AUTHORING.md` §8 for future migration agents. *Commits 6819b90 → ba23e42 → 0bfeb85 → bfa5bee.*

**Build pipeline (Phase A).** `bin/build` is a Ruby kramdown→LaTeX pipeline. Custom `Kramdown::Parser::NeurIPS` extracts Obsidian callouts (`> [!theorem] Title ^anchor`) at parse time as element attributes (no fragile post-hoc text-node digging) and adds single-dollar inline-math span parsing. Custom `Kramdown::Converter::NeurIPS` routes callouts to amsthm environments (theorem/lemma/corollary/proposition/definition/remark/proof, `[!table]` to booktabs `\begin{table}`, `[!figure]` to `\begin{figure}`, working-note callouts `[!note]`/`[!todo]`/`[!info]`/`[!warning]`/`[!tip]` stripped). `[[#^anchor]]` cross-refs render as `\Cref{anchor}`. Raw-TeX passthrough escape policy — only `%`, `&`, `_`, `#`, `~`, `^` are escaped; `\`, `{`, `}`, `$` pass through untouched (codespans get full escape via separate `convert_codespan`). Test paper `00-test-paper/` is the regression harness. *Commits 2e5b64b → feb29ca → ad2b025.*

**Phase B citation system.** Bracketed-superscript rendering via natbib `numbers,super,sort&compress`; `\citet` redefined to emit `Author Year [N]` form (default natbib-super drops the year); `\NAT@open`/`\NAT@close`/`\NAT@super@kern` patched to restore brackets without internal spacing. Source convention is `\cite{key}` / `\citet{key}` (raw TeX, passes through unchanged); replaces the prior `[Author Year]` source which had same-year-disambiguation and multi-author-truncation problems. Implementation in `bin/build`; per-paper `refs.bib` is generated by `bin/refs emit`. *Commits c64813c → 91839fd.*

**Bibliography database.** `bin/refs` (Ruby, ~600 lines, stdlib-only, rubocop-clean) and `refs/` tree solve the multi-agent-concurrent-edit problem. Per-entry YAML files (`refs/entries/<bibkey>.yml`) — distinct entries → distinct files → no merge conflicts; same-entry edits → single-file conflict that git resolves cleanly. Append-only verification event log (`refs/verifications/<bibkey>/<ts>-<verifier>-<criterion>.md`) — six criteria (`bib-fields`, `doi-resolves`, `claim-supported`, `page-ref`, `anonymization`, `no-self-cite`); concurrent verifies never collide on filename. `refs/deny-list.yml` for anonymization vocab including ASF Zenodo DOI. Pipeline integration zero-touch via `bin/refs emit <paper-dir>` writing the per-paper `refs.bib`. 164 entries imported from old workspace's shared `refs.bib` (all unverified pending re-verification). Sqlite was the original sketch; per-entry YAML proved cleaner. *Spike Opus subagent. Commit de5e00c.*

**Typography.** `fontspec` + `TeX Gyre Termes` (Times-equivalent with full Unicode coverage). Resolved silent dropping of em-dash / en-dash / Polish Ł / Czech Č under the previous Nimbus Roman + T1 setup — those glyphs are now rendered correctly (Grönwall, Bretagnolle–Huber, Otto–Villani, Łojasiewicz, Čencov all fine). Hyperref boxes off (`hidelinks`) for visually quieter prose. *Commits 0dcc717 → ef618d6.*

**Doc consolidation.** Single canonical doc per concern at the umbrella level. `AGENTS.md` (process / Ruby / rubocop / agent-coordination) + `AUTHORING.md` (paper-segment authoring rules + NeurIPS-rules-for-authors slice + per-paper layout + migration recipe) + `PRAXES.md` (working principles) + `MIGRATE-TODO.md` (restructure / migration backlog) + `PIPELINE-TODO.md` (build / tooling backlog) + this `LOG.md`. `CLAUDE.md` and `GEMINI.md` are symlinks to `AGENTS.md`. The earlier working docs `restructure-plan.md`, `MIGRATION.md`, `REFS-AND-CITATIONS.md` are archived to `_archive/` once their decisions landed in canonical docs. *Commits 6a2dd3f → 52b9c65 → dddd6a7 → bbde6f2 → 90d0955.*

**Convention decisions.** Lock in:

- *Citation source* `\cite{key}` / `\citet{key}` (decided 2026-05-05; replaces `[Author Year]` source).
- *Citation render* bracketed superscript `[N]` / `[1–3]` (decided 2026-05-05; mitigates math-collision concern in equation-heavy papers).
- *Per-paper trackers* `TODO.md` (with branching freedom: `TODO-citations.md`, `TODO-trim.md`, etc.) + `LOG.md` (decided 2026-05-05; replaces prior `OUTLINE.md` triple-duty role).
- *Math notation* single-dollar `$x$` for inline (compatibility with abstract-submission MathTeX rendering); `$$ ... $$` for display with `aligned` for multi-line.
- *Theorem authoring* Obsidian callouts `> [!theorem] Title ^anchor`; never raw `\begin{theorem}`.

**Open questions** (deferred):

- Footnote convention (markdown `[^id]` vs raw `\footnote{}`) — first-use decides.
- Eventual `bin/migrate-cites` for the `[Author Year]` → `\cite{key}` source migration (`PIPELINE-TODO.md` §C1.4).
- Re-verification of the 164 imported bib entries (`PIPELINE-TODO.md` §F5).

What's next is per-paper content migration (`MIGRATE-TODO.md` §A1–§A3) — segmenting each `paper-draft.md` into `src/<slug>.md` files, writing assembly manifests, applying citation / heading / equation-anchor migrations, anonymization sweep, build verification.
