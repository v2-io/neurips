# AUTHORING.md — Paper-segment rules

*Canonical authoring rules for per-paper agents writing segment files (`<paper>/src/*.md`). Companion to `AGENTS.md` (process / language / rubocop) and the build pipeline at `bin/build` (which enforces these rules at compile time and emits lint findings).*

The rules below are deliberately specific. They exist because cross-paper drift was load-bearing in the prior workspace — manual section numbering broke under reorganization, manual equation tags broke under trim, multiple theorem-authoring styles required pipeline-side workarounds. We're authoring in a uniform shape so the pipeline owns layout/styling and segment authors own content.

When in doubt, write less LaTeX, not more. Raw TeX passes through unmodified — but the pipeline-shaped conventions render better, lint cleanly, and survive renumbering.

---

## 1. Block-level structure

### 1.1 Theorem-shaped semantic blocks

Obsidian callouts. The marker `[!type]`, optional title, and `^anchor` are all on the first line:

```
> [!theorem] Main convergence result ^thm-main
> For any $\mathcal{C}^2$-smooth $f$ with $\nabla^2 f \succeq \mu I$ and $\mu > 0$,
> the gradient flow $\dot{x} = -\nabla f(x)$ converges at exponential rate.
```

Recognized types (each maps to a numbered amsthm environment, sharing one counter so cross-document numbering is coherent): `theorem`, `lemma`, `corollary`, `proposition`, `conjecture`, `claim`, `hypothesis`, `definition`, `remark`. The optional title goes in `\begin{type}[Title]`; the anchor becomes `\label{anchor}`.

`> [!proof]` renders as `\begin{proof}...\end{proof}` (unnumbered). `> [!quote]` renders as `\begin{quote}`.

The author **never** writes `\begin{theorem}` directly. The author **never** numbers theorems by hand.

### 1.2 Working-note callouts

Callouts whose type is `note` / `todo` / `info` / `warning` / `tip` are **stripped at build**. They're authoring sidebars: in-source TODOs, agent notes, drafting reminders. Free of consequence — use them.

```
> [!todo] Authoring note
> Need to revisit Pass-3 alignment with the §5 numerical bound.
```

### 1.3 Acknowledgments

```
> [!ack]
> We thank ...
```

Renders as `\begin{ack}...\end{ack}` (NeurIPS sty-defined; auto-suppressed in anonymized submission). Camera-ready only — the build strips these from anonymized PDF builds per double-blind policy.

### 1.4 Tables

```
> [!table] Empirical convergence rates ($\mu = 1$). ^tab-rates
>
> | Method           |   Rate   | Iterations |
> |:-----------------|:--------:|:----------:|
> | Gradient descent | $0.85^t$ |    120     |
> | Heavy ball       | $0.62^t$ |     45     |
> | Nesterov         | $0.38^t$ |     22     |
```

Title becomes `\caption{...}`, anchor becomes `\label{...}`, body becomes `\begin{tabular}` with booktabs (`\toprule` / `\midrule` / `\bottomrule`). Column alignment from the markdown separator row. Captions can contain inline math; they pass through.

The author **never** writes `\begin{table}` or `\begin{tabular}` directly.

### 1.5 Figures

```
> [!figure] Loss curves across three methods. ^fig-curves
>
> ![Loss curves](sim/loss-curves.pdf)
```

Title becomes `\caption{...}`, anchor becomes `\label{...}`, body's image link becomes `\includegraphics{...}`. The author **never** writes `\begin{figure}` directly.

### 1.6 Display math

`$$...$$` for any block-level math. For multi-line, `\begin{aligned}...\end{aligned}` *inside* the `$$...$$`:

```
$$
\begin{aligned}
V(x) &= f(x) - f(x^*) \\
     &\geq \tfrac{\mu}{2} \|x - x^*\|^2.
\end{aligned}
$$
```

Single uniform shape. **No** `\begin{align}`, `\begin{align*}`, `\begin{equation}`, `\begin{multline}`, `\begin{gather}` at paragraph level — `aligned` covers the multi-line cases inside `$$...$$`. Why: one syntactic shape means the converter never has to detect "am I in math-mode already" or fight with `\\` at row boundaries.

*Open (#6 in the rule discussion):* current convention is good enough; we'll revisit if a cleaner block-math syntax emerges.

### 1.7 Equation numbering and reference

**Authors do not type equation numbers.** Each equation gets an anchor; references use Obsidian wikilink form:

```
$$
V(x) = f(x) - f(x^*) \geq \tfrac{\mu}{2} \|x - x^*\|^2.
$$ ^eq-lyap

Substituting [[#^eq-lyap]] into Theorem [[#^thm-main]] gives the rate.
```

Renders the equation with `\label{eq-lyap}` and the reference as `\eqref{eq-lyap}` (parenthesized number). Cross-references resolve automatically; renumbering can't break the document. **No `\tag{N}`, no manual "(7)", no "see equation 9a" in prose.**

### 1.8 Section headings

`## Section Title` — **no manual numbering in the heading text.** LaTeX numbers (1, 2, 3, ...). Cross-reference via section anchor:

```
## Theory ^sec-theory
```

Reference: `[[#^sec-theory]]` → `\Cref{sec-theory}` ("Section 2"). Same rule for subsection (`### ...`) and deeper. Why: trim work and reorganization are constant; manual numbering drifts silently and breaks references.

`## References` is special-cased — it's recognized as the unnumbered references heading and renders `\section*{References}`. Pandoc's `## References {-}` form is also accepted (explicit unnumbered marker).

### 1.9 Bold-prefix "paragraph" headings

Paragraph-leading bold + period at the start of a paragraph is detected and rendered as `\paragraph{...}`:

```
**Two variation regimes.** Theorem 7.1 is stated for the piecewise-stationary case ...
```

→ `\paragraph{Two variation regimes} Theorem 7.1 is stated ...`

This matches the NeurIPS academic convention without changing how authors write. The detection is "bold span at paragraph start, terminated by period, followed by a space and continuation."

### 1.10 Appendices

The OUT.*.md manifest's `Type` column drives the `\appendix` directive — the build injects `\appendix` before the first row whose Type is `Appendix`. Section headings in appendix segments use the same un-numbered authoring (`## Setup`); LaTeX renders them as A.1, A.2, B, B.1, etc. **No manual `## A.1 Setup` prefix.**

### 1.11 References section

`## References` (or `## References {-}`) at the end of the body, before the appendices. For now, manual entry list:

```
## References

[1] Anderson, B. D. O. (1985). Adaptive systems, lack of persistency of excitation, and bursting phenomena. *Automatica*, 21(3), 247–258.
```

*Open (#12 in the rule discussion):* Phase B will switch to natbib + `refs.bib`. Authors will inline-cite via `[Author Year]` (see §2.3) and the reference list will auto-render. Until then, the manual list is fine.

### 1.12 Checklist

`> [!checklist]` callout (Phase B), or include `src/checklist.tex` as a raw-TeX segment via the manifest. The build injects `\newpage` before any segment whose Type is `Checklist`.

---

## 2. Inline conventions

### 2.1 Inline math

`$x$` — single-dollar form. **This is a hard requirement**, not a preference: the same segment text feeds both the LaTeX build and the OpenReview abstract submission (which uses standard MathTeX rendering and only recognizes `$..$`). Authoring discipline that breaks abstract submission breaks the workflow. The build's parser recognizes single-`$` math directly (no preprocessor; no escape hatch needed).

`$$x$$` form is also valid for inline; either is parsed correctly.

### 2.2 Cross-references

`[[#^anchor]]` (Obsidian native). Renders as `\Cref{anchor}` for typed references (cleveref auto-types the noun: "Theorem N", "Lemma N", "Section N", "Table N", "Figure N"). Anchors prefixed `eq-` route to `\eqref{anchor}` instead, producing the conventional parenthesized form `(N)` that math-paper readers expect for equation references. Reserve the `eq-` prefix for equation anchors only.

```
We've now referenced [[#^thm-main]], [[#^lem-lyapunov]], [[#^tab-rates]], and [[#^sec-theory]].
```

Renders as: "We've now referenced Theorem 1.1, Lemma 1.2, Table 1, and Section 2."

For a specific phrasing (e.g., "see Theorem 1.1's proof in Appendix A"), write the prose around `[[#^anchor]]` and the cleveref-rendered noun fits the sentence.

### 2.3 Inline citations

`\cite{key}` for default attribution; `\citet{key}` when the cited author is the sentence subject. Multi-cite via comma in the key list:

```
the bursting result of \cite{anderson-1985-bursting}
\citet{anderson-1985-bursting} established bursting
multi-cite: \cite{anderson-1985-bursting,bar-shalom-1981,mesbah-2017}
```

Rendered (bracketed-superscript per `REFS-AND-CITATIONS.md`):

- `\cite{...}` / `\citep{...}` → `⁽¹⁰⁾` — compact attribution at end of clause.
- `\citet{...}` → `Anderson 1985⁽¹⁰⁾` — narrative, when the author is the sentence subject.
- Multi-cite via `sort&compress` collapses runs: `\cite{a,b,c}` where keys hash to 1, 2, 3 → `⁽¹⁻³⁾`.

`key` is the BibTeX entry key in the paper's `refs.bib`. Bib keys are canonical — no same-year ambiguity (the Hintikka-1991 problem disappears), no multi-author truncation question. Editor / IDE completion makes lookup ergonomic; the cognitive shape matches our other key-form anchors (`[[#^thm-main]]`).

Raw `\cite{}` passes through the converter unchanged (raw-TeX passthrough policy); the build's natbib config drives the rendering. Switching from numeric to author-year or back is a one-line config change with no author-side impact.

The legacy `[Author Year]` source convention from the prior workspace is deprecated. Existing segments will be migrated via `bin/migrate-cites` (see `PIPELINE-TODO.md` §C1).

### 2.4 Footnotes

*Open (#10 in the rule discussion):* first-use convention; may go with markdown form `[^id]` (kramdown handles natively) or raw `\footnote{}`. Existing papers use neither; will firm up when first author needs one.

### 2.5 Em-dash / en-dash / hyphen

- Em-dash `—` (U+2014): no spaces around it. `text—text`, not `text — text`.
- En-dash `–` (U+2013): numerical ranges only. `pages 5–10`, `the 1985–2005 cycle`.
- Hyphen `-`: compound words and compound names. `context-free`, `Bareinboim-Correa`.

LaTeX-source forms `--` and `---` are not used in markdown; pandoc/kramdown convert anyway, but explicit Unicode reads more clearly in source.

### 2.6 Quotes

Straight `"` / `'` in source. Pandoc/kramdown smart-conversion converts to curly in the LaTeX output. Don't paste curly into source — diffs become fragile and the pipeline already handles it.

### 2.7 `et al.`, `i.e.`, `e.g.`

Period after `et al.` always. Comma after `i.e.,` and `e.g.,` always.

```
Boyd et al. [1994] provide ...
bounded variation, i.e., $\sum_t |\delta_t| \le V_T$
intrinsic-motivation methods (e.g., ICM, RND, VIME)
```

### 2.8 Special characters

UTF-8 in source. Lualatex handles `Łojasiewicz`, `Bretagnolle–Huber`, `Čencov`, `Grönwall`, `Otto–Villani` directly. No `\'e` / `\"o` / `\v{c}` workarounds.

### 2.9 Code spans

Backticks. Inline `` `code` `` and fenced ```code blocks``` work as kramdown standard. Inline code escapes the body content (so `` `\textbf` `` renders as literal `\textbf`, not as the LaTeX command).

This is also the **escape hatch for literal backslash** — if the author needs to render a literal `\` in prose, wrap in backticks.

---

## 3. Voice & vocabulary

### 3.1 Active voice

Active in proofs and prose. "We derive" not "It is derived." "Theorem 1 implies" not "Implication of Theorem 1."

### 3.2 No chronicle voice in formal text

Theorem and proof bodies don't reference change history. **Don't write** "Landed 2026-05-05," "the Pass-2 strengthening lifted ...," "this version replaces the prior bound." Diff-voice belongs in working notes (`> [!todo]`) only.

### 3.3 No "100%" / "comprehensive" / "fully complete"

Match language to actual state. Don't claim universality where the result is restricted.

### 3.4 Canonical "future AI"

Avoid superintelligence / AGI vocabulary — AI-safety-discourse priming. The canonical phrasing for self-actuated future systems is "future AI" — measured, no capability-comparative claims.

### 3.5 Anonymization

Four categories that must NOT appear in submitted PDFs:

- **Personal identifiers:** Joseph, Wecker, joseph.wecker@gmail.com, ORCID 0009-0004-2599-4766, github.com/v2-io.
- **Framework proper-nouns:** ASF, AAD (as a framework name; generic "adaptation" / "actuation" OK), PROPRIUM, AXIOMATA, CHRONICA, VERA, MEMORATA.
- **ELI names:** Zi-am-tur, Anamnos, Lumin, Architectus, Resonance, Soren, Tartur, Calyx, Katan, Synesis, Proto-Architectus, Temporal.
- **Reviewer-priming vocabulary:** "directed separation" → "architectural separation"; etc.

**Self-citation policy:** the ASF working paper (Zenodo DOI 10.5281/zenodo.19986312) **must not be cited** in any submission. Citing it is a double-blind violation per handbook §"Double-blind Reviewing" — a reviewer following the DOI would find the same results under the author's name.

### 3.6 Math notation in markdown vs chat

LaTeX form in markdown source: `$\delta_{\mathrm{sat}}$`, `$\sum_{t=1}^T$`. Unicode in agent chat: `δ_sat`, `Σ`.

### 3.7 Disambiguate quantifier scope before softening

When an audit flags a load-bearing iff / forced / exact / universal / every claim as too-strong, **disambiguate the quantifier scope into named readings before deciding to soften**. The "too-strong" symbol is often compressing several distinct claims with different truth values. The strongest reading is usually the one the paper informally meant; disambiguation recovers it under explicit hypotheses.

A sub-pattern of strengthen-before-softening (`AGENTS.md` §3.1) that fell out of this sprint. Validated repeatedly across B-N4 / B-CS1 / B-N8 audits — every Pass-2 / 3 / 4 audit produced at least one finding where this move converted a recommended softening into a recovered strong reading.

### 3.8 Barrier-vs-multiplier

When a $1/(\text{slack})$-shaped expression appears in survival or constraint contexts, **always ask**: is this a barrier function or a Lagrange multiplier? They scale oppositely at the same level set. A barrier blows up at the constraint level set *by construction*; a multiplier blows up at *infeasibility* (not at the level set, unless the value function diverges there). Conflating them has caused three independent overclaim incidents on this project.

Operational checklist: (1) what program is this a multiplier of — write the explicit Lagrangian; (2) is the value function bounded; (3) where is the divergence — level set or infeasibility; (4) does the chain rule actually compose — both factors must derive from the same program.

### 3.9 Content-side anti-patterns

- ❌ **Chronicle voice in formal text** — theorem and proof bodies don't reference change history. Don't write "Landed 2026-05-05," "the Pass-2 strengthening lifted ...," "this version replaces the prior bound." Diff-voice belongs in working notes (`> [!todo]`) only; formal expression speaks as the current theory.
- ❌ **Hallucinated citations** — every entry must be verified before submission (Code-of-Conduct grade). `bin/refs verify <key> ...` is the channel.
- ❌ **LLM citation context that decays fast** — Nature DOIs that change, arXiv versions that move, web URLs without retrieval dates. Pin versions explicitly or don't cite them.
- ❌ **Trusting agent summaries for downstream decisions** — verify against primary sources (`AGENTS.md` §3.5).
- ❌ **Manual numbering** in headings (`## 3. Title`) or equations (`\tag{N}`) — both drift silently under reorganization. LaTeX numbers; you anchor with `^slug`.

---

## 4. Raw-TeX escape policy

The build's converter passes raw TeX through unmodified by default. Backslash sequences (`\Cref{thm-main}`, `\textbf{...}`, `\nabla^2 f`), curly braces, and dollar signs are author-intentional LaTeX. Authors writing well-formed LaTeX get well-formed output.

The converter still escapes characters commonly used in prose with non-LaTeX meaning: `%`, `&`, `_`, `#`, `~`, `^`. Authors don't have to think about these — `5%` renders as "5%", `cat & dog` renders as "cat & dog."

For the rare case where authors want the literal *backslash* character in rendered text (explaining LaTeX syntax in prose, etc.), wrap in backticks: `` `\textbf` `` renders as the literal string `\textbf` in code-font.

Last-resort escape: `{::nomarkdown} ... {:/nomarkdown}` blocks pass through verbatim, no markdown parsing inside. The build flags these as a soft warning ("you stepped outside the semantic layer — sure?"). Use sparingly.

---

## 5. NeurIPS rules per-paper agents act on

*The full handbook is at `~/src/neurips2026/common/neurips-main-track-handbook.md` (~76 KB; authoritative). What's here is the slice that drives per-paper-agent decisions. Owner-level concerns (track-option choice, AI-use disclosure, camera-ready additions, PDF size envelopes, etc.) live with the build-pipeline owner — surface anything via the umbrella `MIGRATE-TODO.md` if it lands in your lap and you're not sure.*

### 5.1 Page limit

**9 pages** of main content. Figures and tables count toward the limit; references, acknowledgments, optional technical appendices, and the paper checklist do **not** count. Exceeding = desk rejection. This is what drives the `OUT.neurips-2026-paper.md` trim manifest's existence; segments that don't fit get omitted from that manifest (still present in `OUT.full-paper.md`).

### 5.2 Single-PDF order — drives manifest structure

In the assembled PDF, the order is: paper body → references → optional appendices → NeurIPS paper checklist (last). Manifest tables follow this order: numbered Section rows first, then a `Bibliography` row, then `Appendix` rows, then a `Checklist` row last. Build pipeline injects `\appendix` and `\newpage` directives at the right boundaries.

### 5.3 Anonymization

- **Third-person self-citation.** "In the previous work of Jones et al. [4]," not "In our previous work [4]." Cite your own prior work like anyone else's.
- **Self-citation prohibition** for the ASF working paper (Zenodo DOI `10.5281/zenodo.19986312`). Citing it is a double-blind violation. `bin/refs lint` enforces.
- **Anonymization vocabulary** (§3.5 above): Personal / Framework / ELI / Reviewer-priming categories. `bin/refs lint` scans both segment source and bib entries against `refs/deny-list.yml`.
- **No `\begin{ack}` content** at submission. The `ack` callout (§1.3) is auto-suppressed in anonymized builds; just leave the content there for camera-ready.

### 5.4 Contemporaneous-work cutoff

**March 1, 2026.** Papers appearing online before this date are **prior work** — cite and distinguish (full cite-and-distinguish treatment in related-work). Papers after are **contemporaneous** — cite them, but the submission isn't required to empirically beat them. This drives related-work writing.

### 5.5 Paper checklist — fill in what you know

The NeurIPS Paper Checklist is required (its absence = desk rejection). Per-paper agents should fill in answers for everything they know about their paper:

- **Claims** — do main claims in the abstract / intro accurately reflect contributions and scope? (Theory papers: yes if claims match what theorems prove.)
- **Limitations** — discussed honestly in the paper? (Yes for theory papers with named scope conditions.)
- **Theory** — if the paper presents theoretical results, are full proofs available? (Yes; main proofs in body or appendix, sketches link to appendix.)
- **Reproducibility, Code, Data** — for theory-only papers, often **N/A** with a one-line justification.
- **Resources, Ethics, Societal Impact** — answer based on what the paper actually does. "N/A" with justification is fine; just don't skip.

Answer **every** question (yes / no / N/A) with a brief justification. The checklist itself lives at `common/checklist.tex` (canonical, ~26 KB); how it gets wired into the build is `PIPELINE-TODO.md` §A4 — the build-pipeline owner handles that wiring.

### 5.6 What the build pipeline handles — and how to ask for more

The build (`bin/build`) takes care of:

- The right sty file (`common/neurips_2026.sty`, canonical, do not modify) and track options.
- Preamble setup: `amsmath`, `amssymb`, `amsthm` with theorem / lemma / corollary / proposition / definition / remark environments under a shared counter; `cleveref` with `\Cref` / `\crefname` for the type-aware references; `fontspec` + TeX Gyre Termes for Unicode; `hyperref{hidelinks}` to suppress link boxes; natbib `super,sort&compress` with `\citet` redefined for the `Author Year [N]` form.
- `\appendix` / `\newpage` injection from manifest types.
- bibtex / lualatex compile passes.
- Anonymization for default builds (author block suppressed automatically).

If you need something the preamble doesn't have — a missing package, a new theorem-style environment (`\newtheorem{conjecture}[theorem]{Conjecture}` for example), a `\crefname` entry for some custom env, a font weight, a math symbol from an exotic package, anything — **ask Joseph and the build-pipeline owner will add it to the preamble.** Don't try to inject preamble bits from segment source; the segment-author / build-owner separation matters for cross-paper consistency.

Same channel for build issues — if something compiles wrong or renders weirdly, `MIGRATE-TODO.md` flag at the umbrella level (or a per-paper `TODO.md` flag for paper-specific weirdness).

---

## 6. Title / TL;DR / abstract patterns

*Distilled from `~/src/neurips2026/common/metadata-conventions.md`, which synthesized title / TL;DR / abstract patterns from accepted NeurIPS theory papers. Tier markers in that doc: [POLICY] (verifiable against NeurIPS docs), [PATTERN] (observed across recent acceptances), [INFERENCE] (analytical inference). Read the full doc for examples and rationale.*

### 6.1 Title

- **Dominant style:** "Concept Phrase: Descriptive Subtitle." Punchy main clause naming the contribution + clarifying mechanism/result clause.
  *Examples (NeurIPS 2024–2025 best-paper recipients): "Visual Autoregressive Modeling: Scalable Image Generation via Next-Scale Prediction"; "Stochastic Taylor Derivative Estimator: Efficient Amortization for Arbitrary Differential Operators".*
- **Colon-free form** for one crisp claim: "Not All Tokens Are What You Need for Pretraining"; "Optimal Mistake Bounds for Transductive Online Learning."
- **Length:** 6–14 words. Pure-theory papers tend toward shorter, more descriptive forms.
- **Avoid acronyms** in the title unless naming a system that will be reused.

### 6.2 OpenReview TL;DR

- **250-character cap.** Optional but worth filling.
- One declarative sentence: name the object, name what's shown about it. No setup, no motivation, no caveats.
- Under-using the budget is fine.

### 6.3 Abstract

- **One paragraph** (NeurIPS template constraint). 10-point type, 11-point leading, 1/2-inch indent both sides.
- **Roadmap shape:** what we do → how we do it → what we find. ~150–250 words for theory papers.
- Avoid forward references to section numbers (paper hasn't started yet); name the result instead.
- Don't claim "100%" / "comprehensive" / "fully complete" — match language to actual state (PRAXES.md voice discipline).

---

## 7. Per-paper directory layout

### 7.1 Directory shape

Each submodule (`01-tragedy-confident-agent/`, `02-unified-convergence-rl/`, `03-llm-hallucinate-bound/`) has the same shape:

```
0N-{slug}/
├── meta.md              # YAML frontmatter (title / authors / abstract); pipeline reads as preamble metadata
├── refs.bib             # GENERATED by `bin/refs emit 0N-{slug}` — do not hand-edit
├── TODO.md              # live work; agents free to branch to TODO-citations.md, TODO-trim.md, etc.
├── LOG.md               # append-only history (reverse-chronological, never edit prior entries)
├── OUT.full-paper.md    # assembly manifest, full version (no page constraint)
├── OUT.neurips-2026-paper.md  # assembly manifest, 9-page-budget version
├── src/                 # segment files (.md or .tex), each one a piece the manifests reference
├── audits/              # external/internal audit reports land here; findings get triaged into TODO.md
├── spikes/              # temporary investigations; spike report.md → archive when integrated
├── simulations/         # simulation code (B-N4 only — has empirical anchor)
├── results/             # raw empirical results (B-N4 only)
├── out/                 # build artifacts: out/<manifest-stem>.{tex,pdf,aux,log,bbl}; gitignored
└── _archive/            # frozen artifacts (integrated audits, completed spike directories)
```

The umbrella owns: `bin/build` (pipeline), `bin/refs` (bibliography), `common/` (LaTeX template + sty), `refs/` (bib database). Per-paper repos own only their own content; pipeline behavior is shared.

### 7.2 Assembly manifests (`OUT.*.md`)

The manifest is a markdown file. Each row in its tables references a `src/` segment; top-to-bottom is the assembly order (see §1 for column convention `§ | Type | Slug | Title | Stage`). `bin/build <paper> <manifest-stem>` builds the manifest at `OUT.<stem>.md`.

**Multiple manifests, same segments.** A paper has more than one manifest. The base case is `OUT.full-paper.md` (everything, unconstrained) + `OUT.neurips-2026-paper.md` (subset trimmed to the 9-page main-content budget, possibly reordered). Other forms can follow — `OUT.workshop-talk.md`, `OUT.journal-version.md`, `OUT.short-form.md` — all pointing at the same `src/` segments, just different selections / orderings.

**Reuse over re-edit.** When trimming, prefer to write a new manifest that selects a subset of existing segments rather than edit segments to fit a smaller form. Less drift between versions; math changes propagate to all manifests automatically; fewer segments to apply downstream conventions to. *This is especially valuable while the math is still in flux* — a segment that proves Theorem 3.1 lives in one place; if the proof tightens, every manifest gets the update for free. If a segment doesn't fit a particular manifest, **omit it** (don't fork-and-edit). Trimming becomes a curation problem, not a content-rewriting problem.

**Manifest narrative.** A manifest file can carry markdown / LaTeX prose between tables — context, structural rationale, drafting notes, "this section bridges to §4 via..." commentary, anything. The build only assembles rows that look like table rows (lines starting with `|` with the standard column shape); everything else is ignored at build time but renders normally if the manifest is read as a doc. ASF-style; see `~/src/agentic-systems/01-aad-core/OUTLINE.md` for the canonical example with extensive between-table prose.

**Multiple tables per manifest.** A manifest commonly has one table per paper section ("## 1. Introduction" with its segments table, then "## 2. Theory" with its segments table, etc.) with prose between. The parser handles multi-table fine; just leave a blank line between table and prose, between prose and next table.

**Commenting out a row** — wrap the row in `<!-- | ... | -->` on its own line:

```
| 3 | Section | [results](src/03-results.md) | Results | draft |
<!-- | 4 | Section | [discussion](src/04-discussion.md) | Discussion | tentative -->
| A | Appendix | [proofs](src/A-proofs.md) | Proofs | draft |
```

The parser sees the leading `<` and skips; the row stays in the file as a placeholder for later restoration. Kramdown also won't render the comment in the displayed manifest. Use this when experimenting with trim variants before committing to a decision.

**Trim freedom.** Authors are encouraged to try completely different outlines / orderings as part of trim work — different `OUT.*.md` manifests with different selections express different stories without touching the segments themselves. See what reads best and pick.

---

## 8. Migration recipe

Concrete workflow when migrating a paper from the old workspace at `~/src/neurips2026/<paper>/` into a target submodule at `~/src/neurips/0N-{slug}/`. Stepwise on paper #1 with Joseph guiding; mechanical on #2 / #3.

### 8.0 Answers from paper #1 migration (Joseph, 2026-05-05)

Joseph's responses to first-migration-agent questions, captured so paper #2 / #3 agents have the same context. These are his answers — not principles validated through migration work. Paper #1 is the first to try this; downstream agents will refine the pattern.

- **Substrate.** `long-form.md` is the content superset, but `paper-draft.md` is most correct: critical late-cycle spike-integration and audit-finding fixes typically landed only in paper-draft and were never back-ported. Joseph's recommendation: start from paper-draft (most correct) and add segments / alt-segments from long-form. The old workspace's `git log` (full messages, not `--oneline`) carries the integration narrative; `OUTLINE.md`'s todo lists help locate which fixes landed where. Long-form's outline will likely improve significantly as a side-effect.

- **Iterations.** Many expected, not one-pass — Joseph's framing is "don't try to ingest everything and spit out the pieces in one go." Even the substrate merge alone (paper-draft baseline + long-form supersets), separate from formatting conversion, will probably take multiple passes per segment.

- **Drive-by fixes.** Welcome where obvious, with a note in the submodule's `LOG.md` so they're traceable. The focus is parity with the paper outline; opportunistic improvement is fine, sweep-rewriting drifts off-scope.

- **Trim.** Not a migration concern. If natural opportunities surface during segmentation — finer-than-per-section breaks, or two forms of a segment ("with-prose" wrapping the formal content vs. formal-content-only) — those can pay off in later trim passes. Joseph's realistic note: formatting conversion will likely fill the available attention regardless.

- **Segmentation granularity.** Open question. Paper #1 is the first to try it; paper #2 / #3 inherit whatever pattern lands and refine.

- **`bin/migrate-cites`.** Joseph's read as of 2026-05-05: looks like it's working. For the bulk `[Author Year]` → `\cite{key}` step.

- **Old `_archive/`.** No port — fresh `_archive/` in the new submodule. Old workspace's `_archive/` stays as the historical record at `~/src/neurips2026/<paper>/_archive/`. (Supersedes MIGRATE-TODO §C3.)

### 8.1 Numbered recipe

1. **Read the source.** `paper-draft.md` is the main content (most correct, post-spike-integration). `long-form.md` is the content-superset (more material, possibly missing late fixes — see §8.0 substrate strategy). `OUTLINE.md` carries the section budget + audit findings. `LOG.md` carries history. `prior-art/` carries Undermind + positioning. `sim/` (B-N4 only) carries simulation code. `_archive/` carries frozen audit relics (do not port — see §8.0).
2. **Decide segmentation boundaries.** Default: one segment per top-level section (`## 1. Introduction` → `src/01-introduction.md`). Finer where natural (long appendix subsections may want their own segment). Slugs are stable — once a segment exists at `src/intro.md`, don't rename.
3. **Write segments** using AUTHORING conventions:
   - Theorem-shaped blocks → Obsidian callouts (§1.1).
   - Cross-refs → `[[#^anchor]]` (§2.2).
   - Equations with anchors, not `\tag{N}` (§1.7).
   - Headings without manual numbering (§1.8).
   - `\cite{key}` source form (§2.3).
   - $..$ inline math (§2.1).
4. **Write the manifests.** `OUT.full-paper.md` lists segments in assembly order; `OUT.neurips-2026-paper.md` is the 9-page subset (typically: trim some appendix segments, possibly compress some main-content segments; same `src/` files referenced in different orders/subsets).
5. **Citation migration.** `bin/migrate-cites <paper>` (when implemented per `PIPELINE-TODO.md` §C1.4) sweeps `[Author Year]` → `\cite{key}` against the `refs/entries/` index. Ambiguous matches (e.g., `[Hintikka 1991]` → multiple bib entries) flag for human disambiguation. Until that lands, hand-convert as you go OR leave `[Author Year]` markers for later sweep.
6. **Equation-tag migration.** Replace manual `\tag{N}` in display math with anchored `^eq-name` form. ~140–200 equations per paper. Cross-references in prose ("see (9a)") → `[[#^eq-9a]]`. Some prose references (e.g., "(7) above") will need re-anchoring; flag those for human resolution.
7. **Heading-prefix sweep.** Strip `## 3. ` / `### 3.1 ` manual prefixes from segment headings; LaTeX numbers automatically.
8. **Anonymization sweep.** `bin/refs lint <paper>` checks the bib side. For segment text, scan against the four-category vocab (`refs/deny-list.yml`); fix any hits. Self-citation policy enforced for ASF Zenodo DOI.
9. **Auxiliary content.** Port `prior-art/` → into the new submodule's `audits/` or a new `prior-art/` subdir (decide by kind). Port `sim/` (B-N4) → `simulations/`. Port `_archive/` audit relics → `_archive/` (verify integration before archiving — see PRAXES §3.6).
10. **Build as you go.** `bin/build 0N-{slug}` after every meaningful chunk — not just at the end. Tight feedback loop catches issues when they're cheap to debug. Open `out/<manifest>.pdf` visually; confirm rendering, citation form, anonymization. The boundary between "I fix it" and "pause + flag":

    - **Content-side (fix yourself):** bib key missing from `refs/` (run `bin/refs add` or `bin/refs search`); `[[#^anchor]]` references a label that doesn't exist (add the anchor or fix the link); wrong slug path in `OUT.*.md` (correct it); missing cite migration (`[Author Year]` left in a sentence — convert it); etc. If `lualatex` says "undefined reference" or `bibtex` says "I don't know entry X" or the build's lint pass flags something — usually fixable from your seat.
    - **Pipeline-side (pause + flag):** kramdown parse errors on AUTHORING-conformant syntax; a LaTeX package or environment you need that isn't in the preamble (e.g., `\begin{algorithm}` if you have algorithm pseudocode; a `\crefname` entry for a callout type the converter doesn't yet know about); rendering wrong despite source being conformant; build pipeline crashes on input that AUTHORING says should work. Flag in the umbrella's `MIGRATE-TODO.md` (or your paper's `TODO.md` for paper-specific weirdness), continue with non-blocked work, the build-pipeline owner picks it up.

    The rule of thumb: *"is the pipeline supposed to handle this per AUTHORING.md?"* — if yes and it doesn't, that's a pipeline bug; if no, that's content. When in doubt, flag — false positives are cheap, silent compromises are expensive.
11. **Per-paper trackers.** Initialize `TODO.md` (capture remaining work) and `LOG.md` (capture the migration milestone) at the submodule root.
12. **Commit per milestone.** Don't lump segmentation + manifests + cite migration + heading sweep into one commit; separate concerns make the diff reviewable. Use `git commit -- <pathspec>` form to bound scope. Push to your paper's remote regularly.

If something blocks (bib-key mismatch, ambiguous cite, math segment that won't compile, anonymization edge case), drop a flag in the umbrella's `MIGRATE-TODO.md` or the per-paper `TODO.md` and continue with non-blocked work; come back when the blocker resolves.

---

## 9. Open items

These are flagged in line above and consolidated here:

- **#6** — Display-math syntax. Current `$$ ... $$` with `aligned` for multi-line is good enough; may revisit if a cleaner convention emerges.
- **#10** — Footnotes. First-use convention not yet picked.
- **#12** — References section. Phase B switch from manual list to natbib + `refs.bib` (paired with the §2.3 source-form migration).

(#11 — Inline citations — resolved 2026-05-05; see §2.3 above and `REFS-AND-CITATIONS.md`.)

We'll work the rest out as the per-paper segmentation work surfaces concrete cases.

---

*This document grows as conventions firm up. When the build pipeline grows lint rules to enforce a convention, that rule should appear here with the rule itself; the build's lint findings should reference the relevant section by number.*
