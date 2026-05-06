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

`[[#^anchor]]` (Obsidian native). Renders as `\Cref{anchor}`. cleveref auto-types the noun (Theorem, Lemma, Section, Equation, Table, Figure) so the author never has to remember the type:

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

---

## 4. Raw-TeX escape policy

The build's converter passes raw TeX through unmodified by default. Backslash sequences (`\Cref{thm-main}`, `\textbf{...}`, `\nabla^2 f`), curly braces, and dollar signs are author-intentional LaTeX. Authors writing well-formed LaTeX get well-formed output.

The converter still escapes characters commonly used in prose with non-LaTeX meaning: `%`, `&`, `_`, `#`, `~`, `^`. Authors don't have to think about these — `5%` renders as "5%", `cat & dog` renders as "cat & dog."

For the rare case where authors want the literal *backslash* character in rendered text (explaining LaTeX syntax in prose, etc.), wrap in backticks: `` `\textbf` `` renders as the literal string `\textbf` in code-font.

Last-resort escape: `{::nomarkdown} ... {:/nomarkdown}` blocks pass through verbatim, no markdown parsing inside. The build flags these as a soft warning ("you stepped outside the semantic layer — sure?"). Use sparingly.

---

## 5. Open items

These are flagged in line above and consolidated here:

- **#6** — Display-math syntax. Current `$$ ... $$` with `aligned` for multi-line is good enough; may revisit if a cleaner convention emerges.
- **#10** — Footnotes. First-use convention not yet picked.
- **#12** — References section. Phase B switch from manual list to natbib + `refs.bib` (paired with the §2.3 source-form migration).

(#11 — Inline citations — resolved 2026-05-05; see §2.3 above and `REFS-AND-CITATIONS.md`.)

We'll work the rest out as the per-paper segmentation work surfaces concrete cases.

---

*This document grows as conventions firm up. When the build pipeline grows lint rules to enforce a convention, that rule should appear here with the rule itself; the build's lint findings should reference the relevant section by number.*
