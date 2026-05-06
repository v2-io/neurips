# PIPELINE-TODO.md — Build / formatting / authoring-tooling backlog

*Granular pipeline-side items. For paper-content / per-paper-agent work, see each submodule's tracking files. For authoring rules, see `AUTHORING.md`.*

Items are tagged by category. Open items live here; completed items move into context-appropriate `LOG.md` (or just stay struck-through here for a while if the context is short-lived).

---

## A. Visible-in-current-test-PDF (`00-test-paper/out/test.pdf`)

- [x] **A1.** `convert_codespan` override applies full escape inside backticks — done `ad2b025`.
- [x] **A2/A3.** Real dash/diacritic rendering bug (not pdftotext): switched to `fontspec` + `TeX Gyre Termes` for full Unicode coverage — done `0dcc717`.

- [ ] **A4. Wire in the real NeurIPS 2026 paper checklist.** The current `00-test-paper/src/checklist.tex` is a 6-item stub. The canonical checklist is `common/checklist.tex` (~26 KB, detailed multi-question form). Decide whether to (a) include `common/checklist.tex` directly via a manifest row, or (b) segment per checklist question for fillability (questions become individual `src/checklist-NN.md` files referenced from a manifest). Option (b) is more aligned with the segmented-paper philosophy but heavier upfront.

- [x] **A5. "Anonymous Author(s)" title-block confirmed correct for default build** — verified 2026-05-06 across all three papers. `pdftotext` of each `out/full-paper.pdf` shows "Anonymous Author(s) / Affiliation / Address / email" — the neurips_2026 sty's default anonymized rendering is in effect. PDF-content scan against the personal-info deny list (Joseph / Wecker / 0009-0004 ORCID / v2-io / ASF Zenodo DOI) returns clean across all three papers (the one "Joseph" hit in 02 is "Joseph Y. Halpern" inside a citation — legitimate). The `final` option for camera-ready author-block insertion remains a separate future need (will require build-flag wiring + meta.md author-block injection); deferred until camera-ready phase.

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

- [x] **E3. Page-budget tool** — `bin/page-budget` (Ruby port of old workspace's `bin/page-budget`). Parses `<paper-dir>/out/<manifest>.aux` for `\@writefile{toc}{\contentsline ...}` entries; finds first appendix/references marker; reports main-text page count vs 9-pp limit + per-section progression. Done — usage: `bin/page-budget [<paper-dir>...] [--manifest STEM]`. Default manifest is `neurips-2026-paper`. Critical during trim work; per-paper agents can run repeatedly after each cut to track progress.

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

**Status:** RESOLVED — title fixed in `e8324a7` (anchor to line-start, skips in-comment occurrences). Abstract fixed in `51b2852` (now runs through `render_inline_markdown` — same kramdown→LaTeX pipeline as segment bodies; `*emph*` / `**strong**` / `` `code` `` / smart quotes / em-dashes / `$x$` inline math all render correctly).

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

**Status:** RESOLVED-IN-`cc60154`. Architecture moved out of segment-prep regex into AST-level: kramdown parses the source (which respects blockquote structure natively), then `attach_equation_anchors!` walks the tree post-parse pairing `:math` elements with their trailing ` ^anchor` text-node siblings. `convert_math` then emits `\begin{equation}\label{}...\end{equation}` (or `\begin{align}` for `\begin{aligned}`) for anchored math. Equations now embed cleanly inside `> [!lemma]` / `> [!theorem]` / etc. callouts; the migration agent's pulled-out-equation workaround can be reverted to the natural in-statement positioning.

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

**Status:** RESOLVED-IN-`cc60154` (same architectural fix as flag above). Doing the work at the AST level lets kramdown's parser handle codespans natively — `$$...$$` inside backticks parses as code-span content, never as a math delimiter, so the next real `$$...$$ ^eq-name` is unaffected. The migration agent's [!todo] callouts containing literal `$$` examples can be moved back to segment source.

### [01-tragedy + general] Bare `|...|` in inline math `$...$` triggers kramdown table-detection — flagged 2026-05-05 by 01-tragedy migration agent

**Symptom.** Prose containing inline math with bare absolute-value or norm bars — e.g., `$\max_{a \neq a'} |Q_O(a) - Q_O(a')|/|U_o(a) - U_o(a')|$` — gets rendered as a multi-column tabular block by kramdown. The `|` characters inside `$...$` are counted as table column separators when the surrounding paragraph contains 4+ pipes; underscores in the math get escaped (`U\_o`, `Q\_O`); the math context is broken; and lualatex errors fatally on `Extra }, or forgotten $`.

**Context.** Reproduced on `01-tragedy-confident-agent/src/03-kkt-lagrangian.md`, in the prose around eq (9):

```
... is bounded above by $\max_{a \neq a'} |Q_O(a) - Q_O(a')|/|U_o(a) - U_o(a')|$ on the feasibility interior — finite and computable.
```

The build emits this paragraph as a `\begin{tabular}{lllll}` with `\toprule`...`\bottomrule`, splitting the math expression at the `|` separators. The `$...$` inline-math span boundaries don't shield the `|` characters from kramdown's table parser.

**Workaround applied.** Use `\lvert ... \rvert` instead of bare `|` in math: `$\max_{a \neq a'} \lvert Q_O(a) - Q_O(a') \rvert / \lvert U_o(a) - U_o(a') \rvert$`. Standard LaTeX, no parse conflict. Applied in `src/03-kkt-lagrangian.md`.

**Ask.** The custom kramdown parser already extends inline math to recognize `$x$` (single-dollar form). It probably needs to also mask `|` characters inside `$...$` spans before kramdown's table-detection pass runs. Otherwise the workaround `\lvert/\rvert` becomes mandatory project-wide for any paper with absolute values or norms in prose-embedded math, which is friction worth removing.

**Status:** RESOLVED-IN-`7d0c491`. Pre-process masks `|` inside `$...$` and `$$...$$` to a sentinel character (`\x01`) before kramdown parses, then post-processes the rendered output to restore. Block math runs first so the inline pass doesn't mis-eat. The migration agent's `\lvert/\rvert` workaround can be reverted to bare `|...|` in math.

### [02-unified-convergence-rl] Three kramdown-converter rendering bugs surfaced during paper-#2 migration — flagged 2026-05-05 by migration-agent-2

Build of `02-unified-convergence-rl` `OUT.full-paper.md` (commit `14672ef` + appendix-A) failed at lualatex pass 1 with three distinct kramdown-converter issues. All three are AUTHORING-conformant input that the converter mishandles. Reproducer: `bin/build 02-unified-convergence-rl full-paper`.

**Bug 1 — Bold-prefix paragraph immediately followed by display math emits unbalanced `\begin{equation}…$$`.**

*Symptom.* Source like

```
**Strategic tempo (aggregate / throughput form).**
$$\mathcal T_\Sigma^{\mathrm{agg}} \;:=\; \sum_{(i,j) \in E} \nu_{ij} \cdot \iota_{ij} \cdot \eta_{\mathrm{edge}, ij}.$$
The per-element product factors three distinct considerations: …
```

renders to:

```
\paragraph{Strategic tempo (aggregate / throughput form)} 
\begin{equation}
\mathcal T_\Sigma^{\mathrm{agg}} \;:=\; \sum_{(i,j) \in E} \nu_{ij} \cdot \iota_{ij} \cdot \eta_{\mathrm{edge}, ij}.$$
The per-element product factors three distinct considerations: …
```

— `\begin{equation}` opens but the closing `$$` is left unconverted, and from that point on the entire rest of the segment leaks through as raw markdown (`**…**`, `[[#^…]]`, etc.). Lualatex eventually fails on a `\textasciicircum{}` or `#`-in-horizontal-mode cascade dozens of lines later, but the first error is the unbalanced env.

*Context.* §5 strategic-tempo segment (`src/05-strategic-tempo.md`), §5.1 "aggregate form" sub-block. The pattern is **bold-prefix paragraph header + immediately-following unanchored `$$…$$` display math** with no blank line between. AUTHORING §1.9 (paragraph headings) and §1.6 (display math) both show this is a legal authoring shape. The bold-prefix-paragraph autoconverter (commit `56b0960`, AUTHORING §1.9) rewrites `**Term.** body…` to `\paragraph{Term} body…`; here the "body" is the display math block, which the converter then can't represent inside the `\paragraph{}` argument.

The same pattern occurs in many places throughout the source paper — definition-style blocks where a bolded term names a quantity and the equation defines it. Source `paper-draft.md` (which compiled cleanly under the prior pandoc-based pipeline) uses this pattern ~15+ times.

*Ask.* Either (a) `convert_p` should emit `\paragraph{Term}\n\n` (close the `\paragraph{}` line) when the next element is a block-level node like display math, or (b) flag the pattern as a lint warning so authors know to insert a blank line / use a non-bold-prefix form. Workaround on the authoring side is awkward: separating with a blank line makes the bold-prefix-paragraph have no body-continuation, and the convert_p detection requires "bold span at paragraph start, terminated by period, followed by a space and continuation." Best to fix at the converter level.

**Bug 2 — `[[#^anchor]](text)` parsed as markdown link `[label](url)`.**

*Symptom.* Source `[[#^thm-composition]](v)` (intended to render as `\Cref{thm-composition}(v)` → "Theorem 7.1(v)") instead renders as `\href{v}{[\#\textasciicircum{}thm-composition]}` — kramdown's link parser sees `]]` immediately followed by `(` and merges into a `[label](url)` link with `v` as URL.

*Context.* §2 setup, §9 limitations, §9 conclusion — anywhere "Theorem 7.1(v)" / "(v)" sub-conclusion-of-Theorem 7.1 references appear. Source paper-draft.md uses this textual form `Theorem 7.1(v)` 4–6 times; cleveref's `\Cref{thm-composition}` rendering plus literal "(v)" parenthesis is the natural target.

*Ask.* The `[[#^anchor]]` parser should claim its tokens before the link parser sees them, or at least not let `]]` participate in `[label](url)` matching. A workaround using `[[#^anchor]]\,(v)` (thin space) does break the `]]` immediately-followed-by-`(` adjacency, but it's an authoring drift from "Theorem 7.1(v)" to "Theorem 7.1\,(v)" that not every author will think to apply.

**Bug 3 — Unescaped `|…|` in inline math triggers kramdown table parser.**

*Symptom.* Source paragraph

```
**Two variation regimes.** [[#^thm-composition]](v) is stated for the *piecewise-stationary* specialization: $B_T + 1$ stationary blocks separated by optimum-change events, with $B_T := |\{t : a^*_t \ne a^*_{t-1}\}|$. $B_T$ and $V_T$ are distinct in general …
```

renders as a `\begin{tabular}{lll}…\end{tabular}` block — kramdown sees the `|` characters in the inline math as table cell separators and the rest of the paragraph as additional table cells, breaking math content (escaping `_` to `\_`, `^` to `\textasciicircum{}`, etc.).

*Context.* §2 setup ("variation regimes" paragraph), and any other paragraph with unescaped `|…|` in inline math (cardinality `|E|`, absolute value `|x|`, set notation `|\{ … \}|`). The source paper has these in ~10+ places. The kramdown table parser is line-based but can be triggered when a paragraph line contains enough `|` characters that look table-row-shaped. AUTHORING §2.1 says single-`$` inline math should pass through unchanged — but with raw `|` inside, kramdown's other parsers interfere first.

*Ask.* The single-dollar math span parser should claim `|` characters inside `$…$` (and `$$…$$`) before the table parser sees them. The escape-hatch `\,|\,` or `\lvert…\rvert` works as a workaround but again drifts authoring from the natural inline form. The legacy paper-draft.md compiled cleanly under pandoc which doesn't have this kramdown-specific quirk.

**Status:**
  • Bug 1 (bold-prefix + display math) — DOCUMENTED-IN-AUTHORING `§1.6`. Standard kramdown behavior; `$$...$$` immediately after a bold-prefix line (no blank line) is demoted to inline by markdown spec. Authoring requirement: blank lines around block math. Not a converter override (would surprise authors who rely on standard markdown semantics elsewhere).
  • Bug 2 (`[[#^anchor]](text)` link interference) — RESOLVED-IN-`7d0c491`. Override `convert_a` detects the wikilink-eaten-by-link-parser pattern and re-emits as `\Cref{anchor}(href)` (or `\eqref` for `eq-` prefix).
  • Bug 3 (pipe-in-math table-detection) — RESOLVED-IN-`7d0c491` (same fix as flag above; `|` inside `$...$` and `$$...$$` masked to sentinel before kramdown parses).

Verified: `bin/build 02-unified-convergence-rl full-paper` now succeeds end-to-end.

### [01-tragedy + general] cleveref produces "Theorem N" for all lemma / definition / proposition / corollary cross-refs — flagged 2026-05-06 by 01-tragedy migration agent

**Symptom.** Every `\Cref{lem-...}` / `\Cref{def-...}` / `\Cref{prop-...}` in the rendered PDF produces "Theorem N" (where N is the correctly-shared theorem counter value) instead of "Lemma N" / "Definition N" / "Proposition N". The environment's *own* header still renders correctly (`\begin{lemma}` produces "Lemma 2.1" in its body), but cross-references to it via cleveref always say "Theorem".

**Quantitative scope on 01-tragedy.** In the current 24-page build: 17 instances of `Theorem 3.1` (should be `Definition 3.1`), 9 instances of `Theorem 4.2` (should be `Proposition 4.2`), 6 instances of `Theorem 2.1` (should be `Lemma 2.1`), 5 instances of `Theorem A.1` (should be `Lemma A.1`), 5 instances of `Theorem A.4` (should be `Proposition A.4`). All `\Cref` calls to non-theorem theorem-like envs are affected.

**Root cause.** Standard amsthm shared-counter setup:

```
\newtheorem{theorem}{Theorem}[section]
\newtheorem{lemma}[theorem]{Lemma}
\newtheorem{definition}[theorem]{Definition}
\newtheorem{proposition}[theorem]{Proposition}
...
```

With `[theorem]` linkage every theorem-like environment shares the `theorem` counter. `.aux` records the label type as `theorem.N.M` (the counter name), not `lemma.N.M` / `definition.N.M`. Cleveref reads the type from `.aux` and thus calls everything "Theorem". The `\crefname{lemma}{Lemma}{Lemmas}` declarations don't help because cleveref never looks up `lemma` as the type — it sees `theorem`.

`.aux` excerpt from `01-tragedy-confident-agent/out/full-paper.aux`:

```
\newlabel{lem-persistence-d}{{2.1}{3}{...}{theorem.2.1}{}}    ← lemma, but counter type theorem
\newlabel{def-survival-margin}{{3.1}{5}{...}{theorem.3.1}{}}  ← definition, but counter type theorem
\newlabel{prop-blank-wall}{{4.2}{8}{...}{theorem.4.2}{}}      ← proposition, but counter type theorem
\newlabel{thm-lmi-sufficient}{{4.1}{7}{...}{theorem.4.1}{}}   ← actual theorem, type theorem (correct)
```

**Standard fix.** Use the `aliascnt` package to give each env a distinct counter name aliased to the same numeric counter:

```
\usepackage{aliascnt}
\newaliascnt{lemma}{theorem}
\newaliascnt{definition}{theorem}
\newaliascnt{proposition}{theorem}
% ... (one per env)
\newtheorem{lemma}{Lemma}            % no [theorem] linkage; aliascnt keeps numbers shared
\newtheorem{definition}{Definition}
\newtheorem{proposition}{Proposition}
\aliascntresetthe{lemma}
\aliascntresetthe{definition}
\aliascntresetthe{proposition}
% existing \crefname{...} declarations now apply correctly
```

`aliascnt` makes `\Cref{lem-foo}` see `lemma` as the type while keeping `Lemma 2.1`, `Definition 3.1`, `Theorem 4.1`, etc. in a single sequential numbering scheme as desired. This is the canonical cleveref-with-shared-counters recipe (cleveref docs §10).

**Workaround on per-paper side.** Authors can write the type noun in prose around `[[#^anchor]]` to override (e.g., "Lemma [[#^lem-persistence-d]] (ii)" rendering as "Lemma Theorem 2.1 (ii)" — bad; or drop cleveref auto-name and use `\ref{}` form — would require a different source convention). Neither is good. **The pipeline-side fix is essentially mandatory** before the cross-reference apparatus is trustworthy.

**Status:** RESOLVED-IN-`1352759`. Applied the migration agent's documented aliascnt recipe — every theorem-like env now gets its own counter NAME (aliased to the same numeric counter), so cleveref reads `lemma` / `definition` / etc. from .aux. Verified on 01-tragedy: rendered PDF now shows "Definition 3.1" (×19), "Lemma 2.1" (×7), "Proposition 4.2" (×10), "Theorem 4.1" (×13) etc. — correctly typed.

### [03-llm-hallucinate-bound] `\cite[postnote]{key}` form breaks under super-style natbib — flagged 2026-05-06 by 03-llm-hallucinate migration agent

**Symptom.** Standard natbib optional-postnote form `\cite[Theorem N]{key}` (and `\citet[...]{...}`) renders as broken text under the build's `super,sort&compress` natbib config. PDF shows: `By ? ?[?]Lemma 2.4]tsybakov-2009-nonparametric, 2 Hel² ≤ KL slice-wise.` instead of the intended `By Tsybakov³⁹, Lemma 2.4, 2 Hel² ≤ KL slice-wise.` The `[postnote]` argument leaks into the visible text, the superscript is replaced with `[?]`, and the bibkey appears as raw text.

Reproduces on:

- `\cite[Theorem 6.3]{kallenberg-2002-foundations}` (src/03-track1-transport.md:7)
- `\cite[Theorem 3.4]{polyanskiy-wu-2024-info-theory}` (src/03-track1-transport.md:7)
- `\cite[Theorem 5.4]{gray-2011-entropy}` (src/03-track1-transport.md:7)
- `\cite[Theorem 1]{otto-villani-2000-jfa}` (src/03-track1-transport.md:15, src/B-hypothesis-verification.md:13)
- `\citet[Theorem 2.5.3]{cover-thomas-2006-info-theory}` (src/03-track1-transport.md:24)
- `\citet[Theorem 4.6]{stuart-2010-acta}` (src/03-track1-transport.md:91)
- `\cite[Theorem 5.1]{ay-2017-information}` (src/05-track2-fisher-rao.md:27)
- `\citet[Theorem 5.1]{ay-2017-information}` (src/05-track2-fisher-rao.md:33)
- `\citet[Lemma 2.4]{tsybakov-2009-nonparametric}` (src/05-track2-fisher-rao.md:77, src/05-track2-fisher-rao.md:94)

`\citealt[Lemma 2.4]{tsybakov-2009-nonparametric}` (without `t`) appears to render correctly — page 16 line 657 shows `Tsybakov³⁹, Lemma 2.4` properly. So the bug is specific to `\cite[opt]{key}` and `\citet[opt]{key}` under super-style.

**Context.** `\cite[postnote]{key}` is canonical natbib syntax (natbib reference manual §2.5.4), supported across all citation styles in standard natbib config. The `super,sort&compress` mode's bracket-replacement may be intercepting the `[opt]` argument and concatenating it into the text-mode output rather than passing it through to the bibtex-rendered citation tail.

**Workaround applied.** None at source level — the `\cite[opt]{key}` syntax is correct LaTeX; this is a pipeline-side issue. Per-paper agent could rewrite as `\cite{key}` followed by ", Theorem N" in prose if the bug isn't fixed before submission. Alternative: switch all `\cite[opt]{key}` to `\citealt[opt]{key}` form, which appears to work correctly under super-style.

**Ask.** Inspect bin/build's natbib config (`super,sort&compress`); the natbib `super` style may need a `\bibpunct` tweak or the `\cite` redefinition may be eating the optional argument. Standard natbib should pass `[Theorem N]` through to the bibtex-rendered citation as a tail postnote (rendered as ⁽¹⁰,Thm.6.3⁾ or similar in super-style). The current behavior — leaking the optional argument into text-mode output — looks like a `\cite` redefinition bug rather than a natbib option issue.

**Status:** RESOLVED-IN-`1352759`. Migration agent's diagnosis correct — our custom `\citet` redef declared only one arg (`[1]`) and silently dropped the optional postnote. Fixed by declaring optional first arg with default empty: `\renewcommand{\citet}[2][]{\citeauthor{#2}~\citeyear{#2}\citep[#1]{#2}}` — postnote now passes through to the underlying `\citep`. Verified in 03-llm-hallucinate render: "Tsybakov 2009 [39] Lemma 2.4" appears correctly.

### [03-llm-hallucinate-bound + general] Kramdown table heuristic eats paragraphs with bare `|` in inline math — flagged 2026-05-06 by 03-llm-hallucinate migration agent

**Symptom.** A paragraph containing inline-math with bare `|` (conditional probability shape — e.g., `$P_{M_{\tau^+}|e, M_{\tau^-}}$` for `P(M_{τ+} | e, M_{τ-})`) is misparsed by kramdown as a markdown table when the paragraph has multiple `|` occurrences. The build emits a malformed `\begin{tabular}{ll}\toprule ... & ... \\\bottomrule\end{tabular}` wrapping the prose, with `_` characters escaped as `\_` and `^` escaped as `\textasciicircum{}` (math context lost), producing a fatal `Missing }` lualatex error.

Reproduces on `03-llm-hallucinate-bound/src/02-setup.md`'s §2.1 paragraph `For deterministic update mechanisms the distributional definition (2.1) reduces algebraically: $W_2(\delta_{f_X^M(G)}, P_{M_{\tau^+}|e, M})^2 = \mathbb{E}_{G'}\|f_X^M(M_-, e, G) - f_X^M(M_-, e, G')\|^2$, ...` The `|e, M` inside `P_{M_{\tau^+}|e, M}` plus subsequent `\|` for norms produces 4+ `|` characters in the paragraph, triggering kramdown's table-heuristic.

**Workaround applied.** Source-side: switch `|` (conditional) to `\mid` and `\|` (norm) to `\Vert` throughout the paper. Both render identically in LaTeX math mode but don't trigger the kramdown table heuristic. Adopted as a paper-wide convention from §3 onward; §2 was retrofitted. Documented in this paper's `LOG.md`.

**Ask.** The kramdown parser should not interpret `|` characters that appear *inside* inline-math spans (`$...$`) as table delimiters. A small parser fix to mask math-mode content before table detection should resolve this. Worth flagging since this pattern (conditional probability inline math) is universal in Bayesian / probabilistic-method theory papers and will hit any future paper without the `\mid` workaround. Implementation: scan for inline-math spans first, mask their content, then run table detection over the masked text.

**Status:** ALREADY-RESOLVED-IN-`7d0c491` (pre-existing fix; migration agent applied source-side `\mid` / `\Vert` workaround before noticing the pipeline-side mask). Verified on the exact reproducer (`$W_2(\delta_{f_X^M(G)}, P_{M_{\tau^+}|e, M})^2 = \mathbb{E}_{G'}\|...\|^2$`): `mask_math_pipes` (bin/build:702) replaces `|` and `\|` inside inline-math with the `\x01` sentinel before kramdown parses, and kramdown parses the paragraph as a single `:p` element rather than triggering its table heuristic. The source-side `\mid`/`\Vert` convention adopted in 03-llm-hallucinate is independently a fine choice (clearer math markup), but is not required by the pipeline.

### [03-llm-hallucinate-bound + general] `[!table]` callout doesn't auto-size tabular columns; wide-content tables overflow `\textwidth` — flagged 2026-05-06 by 03-llm-hallucinate migration agent

**Symptom.** The `[!table]` callout emits `\begin{tabular}{l...l}` with simple left-aligned columns, no text-wrapping. Cells with longer content (multi-clause topology descriptions, prose-shaped Examples) overflow the NeurIPS single-column textwidth and render with the rightmost columns cut off / truncated mid-word.

Reproduces on `03-llm-hallucinate-bound/out/full-paper.pdf` page 5 (Table 1 — Goal/Update Coupling Class partition, 4 columns, ~60-character cells). The "Examples" column doesn't render at all; "Topology" column truncates mid-sentence at the page edge.

**Workaround options.** None applied at migration time (per-paper agent's call):

- *(a) Author-side rewrite:* shorten cell content to fit default `l` columns; loses information density.
- *(b) Author-side raw TeX:* replace `[!table]` callout with a raw `\begin{table}` ... `\begin{tabularx}{\textwidth}{...}` block via raw-TeX passthrough. AUTHORING §1.4 says authors don't write `\begin{tabular}` directly but raw-TeX is allowed via passthrough policy (§4); this would be the pragmatic escape for wide tables.
- *(c) Pipeline-side fix:* `[!table]` converter detects table width vs `\textwidth` and switches to `tabularx` with `X` columns automatically when needed. Or accepts a `column-spec:` attribute on the callout marker (`> [!table] Title ^anchor column-spec="lXXX"`) to let authors specify column types. Or wraps long tables in `\resizebox{\textwidth}{!}{...}` as a fallback.

**Ask.** Decide and implement one of (b)/(c) — probably (c) at pipeline level since the wide-table case is common for theory papers (architectural classifications, divergence comparisons, hypothesis matrices). Tabularx with default `lXXX` for tables wider than ~4 columns would handle the typical case without author-side configuration.

**Status:** RESOLVED-IN-`d4218a8` via opt-in marker attribute. Implementation chose a hybrid of (c) — pipeline supports tabularx, author opts in per-table via `cols="..."` on the marker. Default behavior preserved: narrow tables continue rendering as natural-width `tabular` (no tabularx tax). Wide tables opt in by writing the column spec on the marker:

```
> [!table] Class partition over goal/update topology. ^tab-class-partition cols="l X X X"
>
> | Class | Topology | Update geometry | Examples |
> ...
```

The cols attribute is a plain LaTeX column spec string — `l`/`c`/`r` for fixed-content alignment, `X` for an equal-share text-wrapping column distributed across the remaining `\textwidth`. Pipeline emits `\begin{tabularx}{\textwidth}{<cols>}` instead of `\begin{tabular}{...}` when `cols=` is present. AUTHORING.md §1.4 documents the convention. The reason for opt-in (rather than auto-detect-and-switch): natural-width tabular sizing reads better for narrow tables (column widths track content), and the migration agent can't always tell at conversion time whether the table will overflow textwidth. Per-table author judgment is cheap and explicit. Auto-detect could be layered on top later if it proves needed.

### [03-llm-hallucinate-bound + general] Smart-quote conversion fails when `"` butts directly against inline-math `$` — flagged 2026-05-06 by 03-llm-hallucinate migration agent

**Symptom.** Kramdown's smart-quote conversion turns straight `"` into typographic `“` `”` *unless* the quote character is directly adjacent to a `$` inline-math delimiter. In that case the straight ASCII `"` passes through to the rendered PDF, looking out of place against the surrounding curly quotes.

Reproduces on phrases of the form `a "$\sigma\sqrt{2I}$" reading` — the quotes around the math span don't get smart-converted. About 11 instances across §2, §5, §6, §A, §C, §D in this paper. Common shape in theory papers: quoting a candidate phrasing that's being criticized, where the candidate phrasing is a math expression.

**Workaround applied.** Source-side: use Unicode curly quotes (`“ ”`) directly in source for the math-adjacent cases. Sweeps cleanly via regex `"([^"\n]*\$[^"\n]*)"` → `“\1”`. AUTHORING §2.6 discourages curly quotes in source ("diffs become fragile, the pipeline already handles it"); the present case is one the pipeline *doesn't* handle, so the workaround diverges from policy with intent.

**Ask.** Smart-quote detection should treat `$` as a word-boundary-like character so quotes adjacent to inline-math get converted normally. Likely fix in kramdown's smart-quote rule: extend the boundary-character set to include `$` (and possibly other math delimiters). Alternatively, the build's converter could post-process after kramdown's smart-quote pass and convert any straight `"` adjacent to `$` to typographic.

**Status:** NOT-REPRODUCING-IN-RENDERED-PDF (2026-05-06). Verified post-revert (`6ad49aa` reverted Unicode curly quotes to ASCII `"`) on the exact agent-reproducer line in §C numerical-comparison appendix. Hex-dump of pdftotext output for the σpost√2I phrase shows `e2 80 9c` and `e2 80 9d` at the quote positions — UTF-8 encodings of U+201C (LEFT DOUBLE QUOTATION MARK `“`) and U+201D (RIGHT DOUBLE QUOTATION MARK `”`). The intermediate LaTeX has the canonical `` ``$\sigma\sqrt{2I}$'' `` ligature form that lualatex renders to typographic curly quotes. Tested the exact pre-revert pattern from src/05-track2-fisher-rao.md:11 plus 10 stress-test variants — all convert correctly via the NeurIPS parser subclass. Likely explanation for the agent's "still active in PDF" report: a PDF viewer or pdftotext rendering setting that displays UTF-8 curly quotes as straight glyphs in the agent's local view, not an actual conversion bug. Per-paper agents can keep their post-revert ASCII `"` form — the rendered output is correct.

If a viewer-independent reproducer surfaces (e.g., a `\catcode` or font-encoding boundary case where the glyph really doesn't appear curly in the embedded font), please update this entry with the exact triggering line and the verification method (hex dump / different viewer / etc.) — we'll then fix at parser-subclass level.

### [03-llm-hallucinate-bound + general] Markdown ordered list restarts at "1." after intervening display equation — flagged 2026-05-06 by 03-llm-hallucinate migration agent

**Symptom.** A markdown ordered list whose items are separated by a display-math block (`$$ ... $$`) gets parsed as *two separate* `\enumerate` environments, each starting at item 1. So a list intended as

```
1. First item ...
$$equation$$
2. Second item ...
```

renders in the PDF as two items both numbered "1." instead of "1." and "2.".

Reproduces on `03-llm-hallucinate-bound/src/06-discussion.md` §6.4 (Conditions 1+2 for (H_κ)) and `src/B-hypothesis-verification.md` §B.3 (the same Conditions 1+2 reproduced for the appendix). The display equations between items are the chain-rule MI inequalities that load-bear for the conditions.

**Workaround applied.** Source-side: replaced markdown ordered-list items with bold-paragraph form `**(1) Title.**` ... `**(2) Title.**` ... — these become `\paragraph{(1) Title}` via AUTHORING §1.9, with the numbering carried in the paragraph head text. Loses semantic-list structure but renders correctly; a per-paper-agent rewrite to combine the items into a single enumerate (with equations inlined as `\,` etc.) would be cleaner if anyone touches the section.

**Ask.** Kramdown's ordered-list parser should treat display math as part of the list-item content (or at least as a soft break that doesn't terminate the enumerate). Standard markdown allows blank-line-separated paragraphs within a list item under sufficient indentation; kramdown might already support this with the right indentation pattern, but the AUTHORING-typical form (display math as a top-level block, not indented) doesn't trigger it. Pipeline-side options: (a) detect display math between consecutive numbered list items and emit a single enumerate spanning them; (b) document the indentation pattern in AUTHORING that keeps a list together across display equations. Either would let authors keep the semantic-list form.

**Status:** RESOLVED-AT-AUTHORING-LEVEL (2026-05-06). Kramdown DOES respect the standard markdown indentation pattern: indenting the `$$math$$` block 3 spaces under the preceding list item makes kramdown read it as continuation content of that item, so consecutive `1.` / `2.` / `3.` items separated by indented math render as a single `\begin{enumerate}` with correct numbering. Verified end-to-end. AUTHORING §1.6 now documents the convention. Per-paper agents can either:

- *(preferred for short-bullet items)* Restore the `1.` / `2.` form and indent the intervening `$$...$$` blocks 3 spaces — preserves semantic-list structure.
- *(preferred for paragraph-shaped items)* Keep the bold-prefix `**(1) Title.**` form they already applied — reads better when each item is a multi-line paragraph rather than a one-liner.

No pipeline-code change required; the kramdown standard-markdown behavior was the answer once the indentation pattern was documented. (Pipeline-side auto-detection of un-indented `$$math$$` between numbered items remains an option if a future paper hits this without the AUTHORING docs reaching the author first; defer until that happens.)

### [01-tragedy-confident-agent + general] `~` and `\&` inside `\cite[...]{}` postnote get escaped — flagged 2026-05-06 by 01-tragedy citation-migration agent

**Symptom.** Standard LaTeX cite postnotes use `~` (non-breaking space) and `\&` (escaped ampersand) — e.g. `\cite[ch.~4 \& 9]{khalil-2002-nonlinear}` per natbib convention. Kramdown's escape pass mangles these to `\textasciitilde{}` and `\\&` respectively even when they appear inside the bracketed postnote argument of a raw `\cite` command. Result: build fails with "Misplaced alignment tab character &" because `\\&` is reserved for tabular row breaks, and the tilde substitution displaces the spacing.

Concrete example that broke pass-1 lualatex:

```
\citet[ch.~4 \& 9]{khalil-2002-nonlinear}
```

becomes in the rendered tex:

```
\citet[ch.\textasciitilde{}4 \\& 9]{khalil-2002-nonlinear}
```

**Workaround applied.** Source-side: replaced `~` with plain space and `\&` with " and " in all `\cite[postnote]{key}` instances across `01-tragedy-confident-agent/src/`. Loses the typographic non-breaking-space inside chapter / section / page references but renders correctly. Concrete forms now in source: `\cite[ch. 9]{...}`, `\cite[chs. 4 and 9]{...}`, `\cite[§3.4--3.5]{...}`, `\cite[Theorem 5.1.1]{...}`. The en-dash `--` and `§` survive the escape pass cleanly.

Secondary observation worth noting: the rendered postnote position is `[N] postnote` (e.g. `[22] p. 4`) rather than the conventional `[N, postnote]`. This is the natbib super style's interaction with the `\citet` redefinition (`\renewcommand{\citet}[2][]{\citeauthor{#2}~\citeyear{#2}\citep[#1]{#2}}`) — the `\citep[note]{key}` ends up emitting the note outside the brackets under the `\NAT@open=[`, `\NAT@close=]` overrides. Cosmetic; semantically clear; not blocking. Worth a fix if the natbib mechanic is easy.

**Ask.** Pipeline-side, the kramdown escape pass should leave `~` and `\&` untouched inside the bracketed argument of `\cite` / `\citet` / `\citep` / `\citealp` (treat the postnote as raw-TeX passthrough, since the entire `\cite{}` form already is). Detection: after a `\cite[tp]?\b` token, the immediately-following `[...]` argument is part of the cite — treat its contents as raw TeX. Once landed, the per-paper sources can revert to standard `~` / `\&` in postnotes.

**Status:** RESOLVED-IN-`c9f7aad`. Pre-mask/post-restore approach modeled on `mask_math_pipes`: each `\cite\w*\[postnote\]` expression has its bracketed content stashed in a per-build array and replaced with a sentinel-bracketed index `\<S>N<S>`. After kramdown parses and the LaTeX converter renders, `unmask_cite_postnotes` walks the output and substitutes the original verbatim postnote back. The `\cite{key}` form was already raw-TeX passthrough policy (AUTHORING §4); the postnote bracket is a natural extension of that scope. Verified end-to-end on `00-test-paper`: `\cite[ch.~4 \& 9]{boyd-1994-lmi}` round-trips with `~` and `\&` intact, lualatex compile clean. Per-paper sources can revert their `~`→space and `\&`→" and " workarounds. The cosmetic `[N] postnote` vs conventional `[N, postnote]` rendering position is a separate natbib-super-vs-`\citet`-redef interaction; defer.

### [01-tragedy + general] U+2261 `≡` (IDENTICAL TO) missing-glyph in TeX Gyre Termes text mode — flagged 2026-05-06 by 01-tragedy migration agent

**Symptom.** Unicode math operator `≡` (U+2261) used in prose (outside `$..$` math mode) renders as the Unicode replacement glyph (visible as a small box / ?-in-square in the rendered PDF). E.g. "with LMI ≡ greedy at low drift" → `with LMI � greedy at low drift` in the PDF. Lualatex emits a "Missing character: There is no ≡ (U+2261) in font" warning during compile.

**Context.** Reproduced in `01-tragedy-confident-agent/src/01-introduction.md` (Contributions paragraph). AUTHORING §2.8 promises "lualatex handles `Łojasiewicz`, `Bretagnolle–Huber`, `Čencov`, `Grönwall`, `Otto–Villani` directly. No `\'e` / `\"o` / `\v{c}` workarounds." That generalization holds for accented letters but breaks on Unicode *math operators* (`≡`, `∇`, `∑` etc.) when used outside math mode — TeX Gyre Termes lacks the math-operator glyphs.

**Workaround applied.** Wrap math operators in inline math: `LMI ≡ greedy` → `LMI $\equiv$ greedy`. Renders correctly. Applied at the one site in 01-tragedy.

**Ask.** Either (a) extend AUTHORING §2.8 to clarify that Unicode math operators outside `$..$` need wrapping (cheap, source-side discipline); or (b) load a math-operator-bearing fallback font in the build's preamble so bare `≡` works in prose (heavier, but matches the §2.8 promise). The (a) path is probably cleaner — separating "letters render directly" from "math operators need math mode" is easy authoring discipline once stated.

**Status:** RESOLVED-AT-AUTHORING-LEVEL (2026-05-06). Took option (a) — AUTHORING §2.8 now explicitly distinguishes "standard letters (Greek, accented Latin, Cyrillic) render directly" from "math operators need math mode" and lists the common operators (`≡` `∇` `∑` `∫` `∂` `∞` `≤` `≥` `≠` `≈` `±`) that need `$...$` wrapping. The agent's source-side fix (`LMI ≡ greedy` → `LMI $\equiv$ greedy`) is the canonical form. Option (b) — loading a math-operator-bearing fallback font — would let bare-glyph forms compile but would mix two font designs in prose, and the math-operator-in-prose pattern is uncommon enough in theory writing that the discipline is cheap.

### Post-revert verification (2026-05-06, 03-llm-hallucinate-bound migration agent)

Reverted all my source-side workarounds back to AUTHORING-canonical / source-original form (commit `6ad49aa` in submodule). Build is still clean. Inventory of which previously-flagged inbox items now appear resolved vs still active in the rendered PDF — for the pipeline owner to confirm and close as appropriate:

**Now appearing resolved in PDF (build-pipeline owner: please verify and update `Status:` if confirmed):**

- `\cite[postnote]{key}` form — `\cite[Theorem 6.3]{kallenberg-2002-foundations}` etc. now renders correctly under super-style natbib as `[34] Theorem 6.3`. Reverted my `\citealt[opt]` workaround back to `\cite[opt]`; output reads cleanly. Verified across §3 (Stuart, Kallenberg, Polyanskiy-Wu, Cover-Thomas, Otto-Villani) and §5 (Tsybakov Lemma 2.4, Ay-Jost-Lê-Schwachhöfer).
- `[!table]` callout column-sizing — 4-column Class-partition table at §2.2 (page 5) renders with all four columns visible and text-wrapped. `[!table] cols="l X X X"` attribute used per pipeline-owner inbox note (umbrella commit `d4218a8`). Standard `[!table]` callout (no `cols=`) on Appendix C numerical-comparison table also renders correctly (page 35) — the cols attribute is opt-in, default keeps working for narrower tables.
- Kramdown bare-`|` table heuristic in inline math — reverted my `\mid`/`\Vert`/`\lvert`/`\rvert` source workarounds back to bare `|` / `\|` / `|...|` matching original source notation. Build no longer fails. The §2.1 paragraph that originally triggered this (`P_{M_{\tau^+}|e, M}` with multiple `\|...\|` in same paragraph) now compiles cleanly. Either the pipeline fix landed or my paragraph happened to not trigger the heuristic in current state — pipeline owner has the diagnostic.

**Still active in PDF after revert:**

- Smart-quote conversion fails against inline-math `$` (line 399 above). Visible at e.g. page 35 line 1543 in the §C numerical-comparison appendix: `the naive "σ_post√2I" reading is wrong` renders with straight ASCII `"`, not smart-quoted. ~22 instances across §2 / §5 / §6 / §A / §C / §D.
- Markdown ordered list restarts at "1." after intervening display equation (line 411 above). Visible at page 22 (§6.4 H_kappa Conditions 1+2) and page 33 (§B.3, same conditions reproduced). Both items render as "1." instead of "1." then "2.".

**Not pipeline issues (reclassified, not flagging):**

- `\sqrt{\,\cdot\,}` rendering — the cdot inside the radical is small enough to look empty/floating against the radical bar. This is canonical LaTeX (square-root-of-placeholder); the visual quirk is just cdot size in the NeurIPS template font. Per-paper-agent stylistic call (rephrase to "Jensen's inequality:" or "Jensen on $\sqrt{x}$:"); not a pipeline bug.
- 4 missing bibkeys (lie-sullivan-teckentrup-2017, parr-dacosta-friston-2019, su-kempe-ullrich-2024, wu-grama-szpankowski-2024) render as `[?]` superscripts. Content-side gap (`bin/refs add` task for per-paper agent), not pipeline.
- Multi-cite at page 27 line 1192 renders oddly because of the missing `wu-grama-szpankowski-2024` key disrupting sort&compress. Resolves when bib entry lands.

**Net post-revert state:** 2 active pipeline bugs visible (smart-quote, list-renumber) + 1 content-side bibkey gap. Source files now in AUTHORING-canonical form across all segments.
