# PIPELINE-TODO.md — Build / formatting / authoring-tooling backlog

*Granular pipeline-side items. For paper-content / per-paper-agent work, see each submodule's tracking files. For authoring rules, see `AUTHORING.md`.*

Items are tagged by category. Open items live here; completed items move into context-appropriate `LOG.md` (or just stay struck-through here for a while if the context is short-lived).

---

## A. Visible-in-current-test-PDF (`00-test-paper/out/test.pdf`)

- [ ] **A1. `\Cref{...}` inside backtick code-spans renders as actual LaTeX, producing `??` in PDF.** The B-supplementary segment has `` `\Cref{...}` `` as a literal example in prose; converter passes through the backslash because of our raw-TeX policy, but inside a codespan the backslash should *always* escape — codespans are the escape hatch. Override `convert_codespan` to apply full escaping (backslash + braces + dollar + the existing chars) regardless of our outer escape policy.

- [ ] **A2. Verify em-dash / en-dash / hyphen rendering visually.** `pdftotext` extraction shows "test paperits job" (em-dash gone), "247258" (en-dash gone), "19852005" (en-dash gone) — but this might be a `pdftotext` extraction quirk rather than a real rendering issue. Open the PDF visually; if the dashes ARE missing, debug font / pandoc-vs-kramdown / inputenc handling.

- [ ] **A3. Verify special-character rendering visually.** `pdftotext` output shows "ojasiewicz" / "encov" / "BretagnolleHuber" — likely also a `pdftotext` quirk (UTF-8 → Latin-1 transcoding loses combining diacritics on extraction), but worth confirming the actual PDF shows Łojasiewicz / Čencov / Bretagnolle–Huber correctly. Lualatex with UTF-8 source *should* handle these natively.

- [ ] **A4. Wire in the real NeurIPS 2026 paper checklist.** The current `00-test-paper/src/checklist.tex` is a 6-item stub. The canonical checklist is `common/checklist.tex` (~26 KB, detailed multi-question form). Decide whether to (a) include `common/checklist.tex` directly via a manifest row, or (b) segment per checklist question for fillability (questions become individual `src/checklist-NN.md` files referenced from a manifest). Option (b) is more aligned with the segmented-paper philosophy but heavier upfront.

- [ ] **A5. Confirm "Anonymous Author(s)" in the title block is intentional for anonymized form.** The neurips_2026 sty suppresses the meta.md author block in default (anonymized) builds — that's correct for submission. Verify the build's behavior matches: `final` option swaps in the meta.md author info at camera-ready. May need a build flag to opt into final-form rendering.

- [ ] **A6. Footnote `[^lmi]` rendering — verify** that the kramdown markdown footnote `[^lmi]` and definition `[^lmi]: ...` render correctly in the PDF. The pdftotext output shows "framework1" suggesting the footnote marker landed; spot-check the footnote text body in the visual PDF.

## B. AUTHORING.md rules not yet enforced

The build pipeline's lint pass should warn on (or convert / strip) authoring patterns the rules say to avoid.

- [ ] **B1. Manual heading numbering** — `## 3. The Lyapunov-Survival ...` violates AUTHORING §1.8. Lint should warn; converter could optionally strip the leading `N.` / `N.M ` prefix (or just warn).

- [ ] **B2. Bold-prefix paragraph headings** — `**Two regimes.** body` should auto-convert to `\paragraph{Two regimes} body` per AUTHORING §1.9. Detection rule: bold span at paragraph start, terminated by period, followed by space + continuation. Implement in `convert_p` (or as a preprocessor that wraps in `\paragraph{}`).

- [ ] **B3. Manual `\tag{N}` in display math** — violates AUTHORING §1.7. Lint should warn ("use `^eq-anchor` and `[[#^eq-anchor]]` instead of `\tag{}`"); existing papers will need migration.

- [ ] **B4. Anonymization vocabulary scanner** — fold the four-category check (Personal / Framework / ELI / Reviewer-priming) from old workspace's `bin/check-anonymization` into the build's lint pass. Source pass scans `src/*.md`; PDF pass remains a separate post-build step (`pdftotext | grep`).

- [ ] **B5. ASF self-citation prohibition** — lint should flag any occurrence of the Zenodo DOI `10.5281/zenodo.19986312` or `ASF` / `AAD` (as framework names) in segment source.

- [ ] **B6. `[!figure]` callout body resolution** — currently emits body verbatim. Should detect markdown image link `![alt](path)` inside the callout body and render as `\includegraphics[width=...]{path}` with caption / label from the marker. Image path resolution: relative to paper-dir.

## C. Phase B converter work

- [ ] **C1. Inline citation substitution** — `[Author Year]` → `\citep{key}`, `Author [Year]` → `\citet{key}`, multi-cite `[A Year; B Year]` → `\citep{a-key,b-key}`. Source the keys from each paper's `refs.bib` via fuzzy author-year matching (re-implement old workspace's `bin/refs-to-bib` + the substitution layer in Ruby).

- [ ] **C2. References section migration** — transition from the manual `[1] Author...` list to natbib + `refs.bib`. Build emits `\bibliographystyle{plainnat}\bibliography{refs}` automatically when `## References` segment is empty / opt-in flag set.

- [ ] **C3. Numeric vs author-year citation rendering** — one-line natbib option (`\PassOptionsToPackage{numbers,sort&compress}{natbib}`) reclaims ~1–3 pp on dense papers; per-paper choice via meta.md frontmatter (`citation_style: numeric` vs `author-year`).

- [ ] **C4. Anchored equations** — `$$ ... $$ ^eq-name` syntax → `\label{eq-name}` after the math; `[[#^eq-name]]` → `\eqref{eq-name}` instead of `\Cref{eq-name}` (since equation refs traditionally appear as "(7)" not "Equation 7"). Distinguish by anchor prefix or by the labeled element type.

- [ ] **C5. Cleveref config audit** — verify `\Cref` produces the right type label for every callout type (theorem / lemma / corollary / proposition / definition / remark / table / figure / section / equation / appendix). Some may need explicit `\crefname{}` / `\Crefname{}` setup beyond the current preamble defaults.

- [ ] **C6. `\paragraph{}` / acknowledgment behavior** — when AUTHORING §1.9 detection lands, verify the rendered paragraph headings interact correctly with `\Cref` (paragraphs aren't typically cleveref-cross-referenced, but should fail gracefully).

## D. Doc consolidation

- [ ] **D1. Consolidate the agent-facing docs.** Currently the umbrella has `AGENTS.md` (process/Ruby/rubocop), `AUTHORING.md` (paper-segment rules), `MIGRATION.md` (migration log), `restructure-plan.md` (active workstream), plus old-workspace material at `~/src/neurips2026/`: `STYLE.md`, `PRAXES.md`, `CLAUDE.md`, `HANDOFF.md`, NeurIPS-related (`common/neurips-main-track-handbook.md`, `common/neurips-guide.md`, `common/metadata-conventions.md`). Soon need to: (a) decide what's canonical here vs old-workspace-leaves; (b) port what's relevant; (c) deduplicate (some prose conventions appear in both `STYLE.md` and `AUTHORING.md`); (d) settle `CLAUDE.md` / `GEMINI.md` symlink target. **Time-box short** (Joseph's framing — "in a short time") so the consolidation doesn't sprawl.

## E. Pipeline tooling not yet ported

These existed in the old workspace as separate scripts; some may be subsumed by the build's lint pass, others remain useful as standalone tools.

- [ ] **E1. Watch-and-build daemon** (`entr`-based; old `bin/watch-and-build`). Auto-rebuilds on segment change. Useful for per-paper-agent feedback loop. Probably wants Ruby reimplementation invoking `bin/build`.

- [ ] **E2. Pre-flight check** (old `bin/preflight`). Consolidated submission-readiness bundle: anonymization + page-count + cite-coverage + compile health across all three papers in one pass.

- [ ] **E3. Page-budget tool** (old `bin/page-budget`). Main-text page count vs 9-pp limit, with per-section breakdown from `paper.aux`. Critical during trim work.

- [ ] **E4. Supplementary-ZIP builder** (old `bin/build-supplementary`). Per-paper ZIP < 100 MB for OpenReview supplementary upload (figures, code, raw-data, extended appendices not in the 9-pp main).

- [ ] **E5. Cite-audit / refs-to-bib** (old `bin/cite-audit` + `bin/refs-to-bib`). Read-only coverage audit (inline cites ↔ refs.bib) and stub-bib harvester from `## References` markdown. Useful for Phase B citation work; may also fold into the build's lint pass.

---

*Items move out of this file when complete: into the relevant LOG.md (project-level for cross-cutting items, or per-paper for paper-specific). Strikethrough items can stay here briefly for context, but should be cleared periodically so the live backlog stays readable.*
