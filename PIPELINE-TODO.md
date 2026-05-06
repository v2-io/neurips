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

- [ ] **C1. Citation rendering — bracketed superscript via natbib.** Decision per `REFS-AND-CITATIONS.md`. Implementation steps:
  1. ✓ Add `\PassOptionsToPackage{numbers,super,sort&compress}{natbib}` to the build's preamble (`bin/build`'s `PREAMBLE_ADDITIONS` constant, or factor out to `common/preamble.tex` if the constant grows). [done — commit `c64813c`]
  2. ✓ Add `\bibliographystyle{unsrtnat}` (citation order) + `\bibliography{refs}` directives at the end of the body. [done]
  3. ✓ Custom `\citet` redefinition so narrative cites emit `Author Year⁽N⁾` rather than natbib-`super` default `Author [N]` (~3-line preamble patch; verify against current natbib release). [done]
  4. **Source-form migration** `bin/migrate-cites <paper>`: scan segment source for `[Author Year]` patterns, fuzzy-match against `refs/entries/<bibkey>.yml` (via `bin/refs search` or direct), replace with `\cite{key}` (parenthetical) or `\citet{key}` (narrative — detected by sentence-position context). Flag ambiguous matches (`[Hintikka 1991]` → multiple entries) for human disambiguation. Emit a diff for review before applying. **Backend ready:** `bin/refs` provides the entry index + per-paper bib emission; `bin/migrate-cites` is the paper-segment rewriter on top.
  5. Author-side convention is captured in AUTHORING.md §2.3 (already updated 2026-05-05).
  6. Verify rendering visually on `00-test-paper` before per-paper migration. Side-by-side with the current author-year render to confirm the math-collision concern is mitigated by brackets.
  7. After per-paper migration succeeds, archive `REFS-AND-CITATIONS.md` to `_archive/` (`git mv`).

- [ ] **C2. References section migration** — transition from the manual `[1] Author...` list to natbib + `refs.bib`. Build emits `\bibliographystyle{plainnat}\bibliography{refs}` automatically when `## References` segment is empty / opt-in flag set.

- [ ] **C3. Numeric vs author-year citation rendering** — one-line natbib option (`\PassOptionsToPackage{numbers,sort&compress}{natbib}`) reclaims ~1–3 pp on dense papers; per-paper choice via meta.md frontmatter (`citation_style: numeric` vs `author-year`).

- [ ] **C4. Anchored equations** — `$$ ... $$ ^eq-name` syntax → `\label{eq-name}` after the math; `[[#^eq-name]]` → `\eqref{eq-name}` instead of `\Cref{eq-name}` (since equation refs traditionally appear as "(7)" not "Equation 7"). Distinguish by anchor prefix or by the labeled element type.

- [ ] **C5. Cleveref config audit** — verify `\Cref` produces the right type label for every callout type (theorem / lemma / corollary / proposition / definition / remark / table / figure / section / equation / appendix). Some may need explicit `\crefname{}` / `\Crefname{}` setup beyond the current preamble defaults.

- [ ] **C6. `\paragraph{}` / acknowledgment behavior** — when AUTHORING §1.9 detection lands, verify the rendered paragraph headings interact correctly with `\Cref` (paragraphs aren't typically cleveref-cross-referenced, but should fail gracefully).

## E. Pipeline tooling not yet ported

These existed in the old workspace as separate scripts; some may be subsumed by the build's lint pass, others remain useful as standalone tools.

- [ ] **E1. Watch-and-build daemon** (`entr`-based; old `bin/watch-and-build`). Auto-rebuilds on segment change. Useful for per-paper-agent feedback loop. Probably wants Ruby reimplementation invoking `bin/build`.

- [ ] **E2. Pre-flight check** (old `bin/preflight`). Consolidated submission-readiness bundle: anonymization + page-count + cite-coverage + compile health across all three papers in one pass.

- [ ] **E3. Page-budget tool** (old `bin/page-budget`). Main-text page count vs 9-pp limit, with per-section breakdown from `paper.aux`. Critical during trim work.

- [ ] **E4. Supplementary-ZIP builder** (old `bin/build-supplementary`). Per-paper ZIP < 100 MB for OpenReview supplementary upload (figures, code, raw-data, extended appendices not in the 9-pp main).

- [ ] **E5. Cite-audit / refs-to-bib** (old `bin/cite-audit` + `bin/refs-to-bib`). Read-only coverage audit (inline cites ↔ refs.bib) and stub-bib harvester from `## References` markdown. Useful for Phase B citation work; may also fold into the build's lint pass. **Largely subsumed by `bin/refs`** — `bin/refs cited` does the coverage audit, `bin/refs lint` does the missing-key check, `bin/refs emit` does the bib generation. Stub-bib harvester from `## References` markdown remains useful for one-shot legacy migrations.

## F. Citation backend — `bin/refs` (landed)

The multi-agent-safe citation system at `~/src/neurips/refs/` + `bin/refs`. Source of truth is per-entry YAML (`refs/entries/<bibkey>.yml`); BibTeX is a generated artifact. Verification is append-only events at `refs/verifications/<bibkey>/*.md`. Anonymization deny-list at `refs/deny-list.yml`. See `refs/README.md` for schema + workflow.

- ✓ `bin/refs` CLI with verbs: `add` / `import` / `show` / `list` / `search` / `verify` / `unverify` / `cited` / `emit` / `lint` / `pdf` / `validate`.
- ✓ 164 entries imported from legacy `~/src/neurips2026/common/refs.bib` (`bin/refs validate` clean).
- ✓ Anonymization deny-list at `refs/deny-list.yml` (DOIs, authors, framework / ELI proper-nouns from AUTHORING.md §3.5).
- ✓ Concurrency story: per-entry files mean two agents adding distinct entries never collide; verification events are filename-unique (timestamp + verifier + criterion).

Open follow-ups (deferred — backend is sufficient for the per-paper agents to start using it):

- [ ] **F1. Build-pipeline integration.** `bin/build` could optionally call `bin/refs emit <paper-dir>` before the lualatex pass so the per-paper `refs.bib` is always derived from the current entries. Today the build reads a hand-maintained `<paper-dir>/refs.bib`; once the paper-side migration (C1.4) lands, switching to emit-on-build is one config line.
- [ ] **F2. DOI auto-fetch** (`bin/refs fetch <doi>`). Phase 0 is paste-BibTeX-on-stdin / scaffold-and-fill. CrossRef / DataCite would let an agent verify-by-fetching.
- [ ] **F3. Duplicate-DOI detection.** Two entries with different keys but the same DOI should surface in `bin/refs lint`. Today each is treated independently.
- [ ] **F4. PDF-claim anchoring.** `bin/refs pdf <key> <path>` registers a PDF; nothing yet inspects content. A future `bin/refs grep <key> <claim>` would let the `claim-supported` criterion be backed by literal text-match anchors rather than free-form notes.
- [ ] **F5. Re-verification of imported 164 entries.** The legacy bib's verification status (from `~/src/neurips2026/common/citation-verification-report.md`) is currently *unverified* in the new system. Per-paper agents will surface verification events as they encounter each entry; a one-shot import from the verification report is also possible (would attribute events to "joseph + bib-verification subagent, 2026-05-04").

---

*Items move out of this file when complete: into the relevant LOG.md (project-level for cross-cutting items, or per-paper for paper-specific). Strikethrough items can stay here briefly for context, but should be cleared periodically so the live backlog stays readable.*
