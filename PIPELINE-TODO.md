# PIPELINE-TODO.md — Build / formatting / authoring-tooling backlog

*Granular pipeline-side items. For paper-content / per-paper-agent work, see each submodule's tracking files. For authoring rules, see `AUTHORING.md`.*

Items are tagged by category. Open items live here; completed items move into context-appropriate `LOG.md` (or just stay struck-through here for a while if the context is short-lived).

---

## A. Visible-in-current-test-PDF (`00-test-paper/out/test.pdf`)

- [x] **A1.** `convert_codespan` override applies full escape inside backticks — done `ad2b025`.
- [x] **A2/A3.** Real dash/diacritic rendering bug (not pdftotext): switched to `fontspec` + `TeX Gyre Termes` for full Unicode coverage — done `0dcc717`.

- [ ] **A4. Wire in the real NeurIPS 2026 paper checklist.** The current `00-test-paper/src/checklist.tex` is a 6-item stub. The canonical checklist is `common/checklist.tex` (~26 KB, detailed multi-question form). Decide whether to (a) include `common/checklist.tex` directly via a manifest row, or (b) segment per checklist question for fillability (questions become individual `src/checklist-NN.md` files referenced from a manifest). Option (b) is more aligned with the segmented-paper philosophy but heavier upfront.

- [ ] **A5. Confirm "Anonymous Author(s)" in the title block is intentional for anonymized form.** The neurips_2026 sty suppresses the meta.md author block in default (anonymized) builds — that's correct for submission. Verify the build's behavior matches: `final` option swaps in the meta.md author info at camera-ready. May need a build flag to opt into final-form rendering.

- [ ] **A6. Footnote `[^lmi]` rendering — verify** that the kramdown markdown footnote `[^lmi]` and definition `[^lmi]: ...` render correctly in the PDF. The pdftotext output shows "framework1" suggesting the footnote marker landed; spot-check the footnote text body in the visual PDF.

## B. AUTHORING.md rules not yet enforced

The build pipeline's lint pass should warn on (or convert / strip) authoring patterns the rules say to avoid.

- [x] **B1.** Manual heading numbering lint warning in `convert_header` — done `a5756c5`.
- [x] **B2.** Bold-prefix paragraph headings auto-converted in `convert_p` (top-level only; list-item / blockquote context skipped) — done `56b0960`.
- [x] **B3.** Manual `\tag{N}` lint warning in `convert_math` — done `a5756c5`.
- [x] **B4 / B5.** Segment-source anonymization scanner using `refs/deny-list.yml` (DOIs, authors, proper-nouns) — done `c7a8d60`. PDF-level scan stays a separate post-build step.
- [x] **B6.** `convert_standalone_image` override — single `\includegraphics{}` inside [!figure] callout's `\begin{figure}` wrapper, no double-wrap — done `53970de`.

## C. Phase B converter work

- [ ] **C1. Citation rendering — bracketed superscript via natbib.** Decision per `REFS-AND-CITATIONS.md`. Implementation steps:
  1. ✓ Add `\PassOptionsToPackage{numbers,super,sort&compress}{natbib}` to the build's preamble (`bin/build`'s `PREAMBLE_ADDITIONS` constant, or factor out to `common/preamble.tex` if the constant grows). [done — commit `c64813c`]
  2. ✓ Add `\bibliographystyle{unsrtnat}` (citation order) + `\bibliography{refs}` directives at the end of the body. [done]
  3. ✓ Custom `\citet` redefinition so narrative cites emit `Author Year⁽N⁾` rather than natbib-`super` default `Author [N]` (~3-line preamble patch; verify against current natbib release). [done]
  4. ✓ **Source-form migration** `bin/migrate-cites <paper-dir>`: scans `<paper-dir>/src/**/*.md` for parenthetical `[Author Year]` and narrative `Author [Year]` patterns, matches against `refs/entries/*.yml` by first-author-surname + year, prints a per-file report (matched / ambiguous / missing); `--apply` rewrites in place. Handles `et al.`, hyphenated multi-author, page references (`[Author Year, p. 247]` → `\cite[p. 247]{key}`); multi-year (`[Friston 2013, 2019]`) and complex multi-cite (`[A Year; B Year]`) are intentionally skipped by the regex so a human can pick the right form. *Signed off 2026-05-05 — ready for use by per-paper migration agents.*
  5. Author-side convention is captured in AUTHORING.md §2.3 (already updated 2026-05-05).
  6. Verify rendering visually on `00-test-paper` before per-paper migration. Side-by-side with the current author-year render to confirm the math-collision concern is mitigated by brackets.
  7. After per-paper migration succeeds, archive `REFS-AND-CITATIONS.md` to `_archive/` (`git mv`).

- [ ] **C2. References section migration** — transition from the manual `[1] Author...` list to natbib + `refs.bib`. Build emits `\bibliographystyle{plainnat}\bibliography{refs}` automatically when `## References` segment is empty / opt-in flag set.

- [ ] **C3. Numeric vs author-year citation rendering** — one-line natbib option (`\PassOptionsToPackage{numbers,sort&compress}{natbib}`) reclaims ~1–3 pp on dense papers; per-paper choice via meta.md frontmatter (`citation_style: numeric` vs `author-year`).

- [x] **C4.** Anchored equations: `$$ ... $$ ^eq-name` rewritten to `\begin{equation}\label{}...\end{equation}` (or `\begin{align}\label{}...\end{align}` for `aligned` content); `eq-` prefixed cross-refs route to `\eqref{}` instead of `\Cref{}` — done `1468878`.

- [x] **C5.** Cleveref names added for conjecture / claim / hypothesis / appendix (had `\newtheorem` defs but no `\crefname`) — done `821ab8a`. All callout types and structural envs now have explicit crefname entries.

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

---

## Inbox

*Live channel for per-paper agents (and any other agent) to flag build / formatting / pipeline asks for the build-pipeline owner. Protocol in `AGENTS.md` §5.1.*

**To file an entry: atomic append.** Just append your block to the end of this file with `>>` (shell), `File.open(path, "a")` (Ruby), or equivalent atomic-append. Don't read the file first — concurrent flags from multiple agents would race. Each entry is self-contained; insertion point doesn't matter.

**Template:**

```markdown
### [paper-id] Brief title — flagged YYYY-MM-DD by <agent-name>

**Symptom:** what you saw.

**Context:** segment file(s), manifest, recent change that triggered.

**Ask:** what you need.

**Status:** OPEN
```

**Status progression** (build-pipeline owner edits, single-writer): `OPEN` → `IN-PROGRESS` → `RESOLVED-IN-<commit>`. Build-owner periodically clears `RESOLVED` entries (substantive ones land in `LOG.md`).

**What goes here vs not:**

- ✅ Yes: kramdown breaks on AUTHORING-conformant syntax; LaTeX package or environment you need that isn't in the preamble; rendering wrong despite source being conformant; build pipeline crashes on input AUTHORING says should work.
- ❌ No (you fix yourself): bib key not in `refs/` (run `bin/refs add`); `[[#^anchor]]` references missing label; wrong slug path in `OUT.*.md`; `[Author Year]` left in a sentence; rubocop offense in your own Ruby.

---

*(No entries yet — first per-paper migration agent kicks off the queue.)*

### [01-tragedy + general] meta.md → template substitution: title not replaced; abstract not kramdown-rendered — flagged 2026-05-05 by 01-tragedy migration agent

**Symptom (1) — title.** The generated `out/full-paper.tex` retains `\title{Formatting Instructions For NeurIPS 2026}` at line 61 (the template's placeholder) and instead injects the meta.md title into a *comment line* at line 40 (`% Note. For the workshop paper template, both \title{Tragedy of the Confident Agent: ...} and \workshoptitle{} are required...`). Net effect: PDF shows "Formatting Instructions For NeurIPS 2026" as the title, not the paper's actual title.

**Symptom (2) — abstract.** `meta.md` body is pasted into `\begin{abstract}...\end{abstract}` verbatim, with no kramdown processing. Markdown emphasis (`*foo*`), code spans (`` `foo` ``), and other inline forms render as raw markdown characters in the PDF rather than as their LaTeX equivalents (`\emph{foo}`, code-font, etc.). Reproduces in `00-test-paper` as well — abstract there has literal backticks around `01-` / `02-` / `03-`.

**Context.** `bin/build` lines 684–693:

```
# Replace title
template = template.sub(/\\title\{[^}]*\}/) { "\\title{#{meta.title}}" }
...
# Replace abstract
template = template.sub(/\\begin\{abstract\}.*?\\end\{abstract\}/m) do
  "\\begin{abstract}\n#{meta.abstract}\n\\end{abstract}"
end
```

The title regex matches the *first* `\title{...}` in the template, which is the *empty* `\title{}` inside the workshop-template comment block (template line 40). The actual `\title{Formatting Instructions...}` directive at line 61 never gets touched.

For the abstract: `meta.abstract = body.strip` (line 467) is raw text, not kramdown-rendered before splicing into the template.

Reproduces on both `00-test-paper test` and `01-tragedy-confident-agent full-paper`.

**Ask.** Title-replacement should target the actual `\title{}` directive (not the in-comment occurrence); options: anchor to start-of-line + skip lines beginning `%`, or match `\title{Formatting Instructions[^}]*}` explicitly, or process the template line-by-line so commented-out forms are skipped. Abstract should be run through the same kramdown→LaTeX pipeline as segment bodies before splicing — currently emphasis / code / cross-refs in the abstract don't render correctly.

**Status:** OPEN

### [01-tragedy] Display math inside Obsidian callout fragments the callout — flagged 2026-05-05 by 01-tragedy migration agent

**Symptom.** A `> [!lemma]` callout with `$$ ... $$` display math in its body emits a fragmented LaTeX result: `\begin{lemma}` ... `\end{lemma}` (closes at the equation), then `\begin{quotation}` (for the rest of the callout body), then `\begin{quote}` (for the trailing sentence after a second equation). The lemma's parts (i)/(ii)/(iii) end up in three different environments, none of them the lemma. Plus the equation env itself sometimes gets a stray blank line between math content and `\label{}`, producing a fatal `Missing $ inserted` from lualatex.

**Context.** Reproduced on `01-tragedy-confident-agent/src/02-persistence.md` migrating Lemma 2.1 (Persistence threshold; Model D, robust form). Source structure was the natural one — lemma callout containing parts (i), (ii) with eq (4a), (iii) with eq (4):

```
> [!lemma] Persistence threshold; Model D, robust form ^lem-persistence-d
> Under [[#^eq-mismatch-dyn]]–[[#^eq-sector]] ...
>
> *(i) ...* If $\alpha > \rho/R$, then ...
>
> *(ii) ...* ... drives every trajectory ... in finite time bounded by
> $$
> T_{\mathrm{exit}}(\delta_0) \;\leq\; ...
> $$ ^eq-exit-time
>
> *(iii) ...* ... then under worst-case $w \in \mathcal{W}$,
> $$
> \boxed{\;\alpha > \frac{\rho}{R}\;}
> $$ ^eq-persistence
> is two-sided ...
```

The kramdown blockquote terminates at the first `$$`, the equation-rewrite emits the env outside the lemma, and the subsequent `> ` lines start a fresh blockquote (with no callout marker, so default `\begin{quotation}`). This pattern is widespread in theory papers — many lemmas have embedded display math as part of the statement.

**Workaround applied.** Equations pulled out of the lemma callout, placed below it; references from inside the lemma use `[[#^anchor]]`. Works but loses the natural in-statement positioning. See `01-tragedy-confident-agent/src/02-persistence.md` for the current shape.

**Ask.** Display math `$$ ... $$ ^eq-name` (and `$$ ... $$` without anchor) should be supported inside Obsidian callouts. Implementation likely requires the parser to keep the blockquote open across display-math blocks (custom blockquote handling that recognizes `$$ ... $$` as inline content). Equivalent fix would be to recognize `> $$ ... > $$` (display math with `> ` prefix on each line) as blockquoted display math.

**Status:** OPEN

### [01-tragedy + 00-test-paper] Anchored-equation rewriter at segment-prep level doesn't respect codespan boundaries — flagged 2026-05-05 by 01-tragedy migration agent

**Symptom.** When a segment contains a `[!todo]` callout (or any prose) whose body mentions `$$ ... $$` inside backticks (codespan), AND a downstream `$$ ... $$ ^eq-name` anchored display equation, the equation rewrite produces malformed output for the *first* downstream equation: opening `$$` not converted to `\begin{equation}`, math content escaped as prose (e.g., `T_{\mathrm{exit}}` becomes `T\_{\mathrm{exit}}`, `\|\delta_0\|` becomes `|\delta\_0|`), trailing `{:/nomarkdown}` artifact emitted. The next `$$ ... $$ ^eq-name` in the same segment renders correctly. Lualatex then errors fatally on the `\end{equation}` that closes a non-existent `\begin{equation}`.

**Context.** Reproduced on `01-tragedy-confident-agent/src/02-persistence.md` when an authoring-note callout was placed between Lemma 2.1 and the pulled-out anchored equations:

```
> [!todo] Authoring note ...
> ... explanation mentioning `$$ ... $$` syntax ...

The exit-time bound:
$$
T_{\mathrm{exit}}(\delta_0) \;\leq\; ...
$$ ^eq-exit-time

The persistence threshold:
$$
\boxed{\;\alpha > \frac{\rho}{R}\;}
$$ ^eq-persistence
```

The first equation (`^eq-exit-time`) renders broken; the second (`^eq-persistence`) renders correctly. Removing the [!todo] callout fixes the first equation. Hypothesis: the anchored-equation rewrite operates at segment-prep level (per project LOG: "rewritten ... at the segment-prep level") and pairs `$$` markers naively, including the ones inside backticked codespans in the [!todo] body. The codespan `$$` is treated as an opening delimiter, capturing the actual `$$` of the next display block as its closing delimiter.

**Workaround applied.** Authoring notes moved out of segment `[!todo]` callouts into the per-paper `TODO.md` (under "Known followups").

**Ask.** Segment-prep-level anchored-equation rewriter should respect codespan boundaries — `$$ ... $$` inside backticks shouldn't be treated as math. Implementation: scan for codespans first, mask their content, then run the `$$ ... $$ ^eq-name` rewrite over the masked text.

**Status:** OPEN
