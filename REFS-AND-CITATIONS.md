# REFS-AND-CITATIONS.md — working doc

*Temporary. Surveys options and prior discourse on citation rendering + bibliography format. Once a decision lands, the operative parts move into AUTHORING.md / `bin/build` config and this file gets archived.*

---

## DECISION (2026-05-05)

**Render** — bracketed superscript (§3.4 below).

- `\cite{key}` / `\citep{key}` (parenthetical attribution) → `⁽¹⁰⁾`.
- `\citet{key}` (narrative — author as sentence subject) → `Anderson 1985⁽¹⁰⁾`.
- Multi-cite via `sort&compress`: `\cite{a,b,c}` → `⁽¹⁻³⁾`.

**Source convention** — `\cite{key}` / `\citet{key}` directly in markdown (raw TeX passes through; no converter parser changes). Replaces the prior `[Author Year]` source convention.

*Why the source change:* `[Author Year]` is structurally ambiguous when an author has multiple same-year publications (Hintikka 1991 has six relevant ones) and forces an author-list-truncation choice (`[Bachman et al. 2031]` vs `[Bachman, Smith, Yang, Lin, Park 2031]`). Bib keys are canonical and editor-completable; both problems vanish.

**Bibstyle** — `unsrtnat` (citation order; `[1]` is first-cited).

**LaTeX preamble** —
```latex
\PassOptionsToPackage{numbers,super,sort&compress}{natbib}
\usepackage{neurips_2026}
% Custom \citet so narrative cites emit "Author Year⁽N⁾" rather than the
% default natbib-super "Author [N]" without the year (~3-line patch; tested
% against natbib release pinned in build).
\bibliographystyle{unsrtnat}
\bibliography{refs}
```

**Implementation** — PIPELINE-TODO §C1. Includes the one-shot `bin/migrate-cites` for converting existing `[Author Year]` segment source to `\cite{key}` form.

**This doc archives to `_archive/`** once the implementation lands and AUTHORING.md is the live source of truth.

---

**Tier markers** (borrowed from `~/src/neurips2026/common/metadata-conventions.md`):
- **[POLICY]** — explicitly stated in NeurIPS 2026 official documents.
- **[PATTERN]** — observed convention in published / accepted theory-CS papers.
- **[INFERENCE]** — analytical inference; weight accordingly.

---

## 1. Joseph's stated preference

Superscripted numeric — `text¹⁰⁻¹¹` inline — with a numbered bibliography `[10] Author... \n[11] Author...`. Rationale: tremendous space savings + noise reduction in already visually-dense, math-heavy papers (HANDOFF prior session: *"numeric footnotes ideal,"* estimated **1–3 pp reclaim on B-N8**).

This is a *rendering* choice. Authors keep writing `[Anderson 1985]` in markdown source regardless; the build's compile-time substitution determines rendered form. Rendering can be re-decided without re-authoring.

## 2. NeurIPS 2026 official policy

[POLICY] From the NeurIPS 2026 LaTeX template (`common/neurips_2026.tex`, §"Citations within the text"):

> *"The natbib package will be loaded for you by default. Citations may be author/year or numeric, as long as you maintain internal consistency. As to the format of the references themselves, any style is acceptable as long as it is used consistently."*

[POLICY] Hallucinated citations violate the NeurIPS Code of Conduct (handbook §"Author Use of Agents and LLMs") — desk-rejection risk. Existing `common/citation-verification-report.md` from 2026-05-04 covers verification of every flagged citation. Verification is independent of rendering choice.

[POLICY] References don't count toward the 9-page main-content limit (handbook §1.2): *"Additional pages containing acknowledgments, references, checklist, and optional technical appendices do not count as content pages."*

[POLICY] Self-citation must be third-person; ASF working paper (Zenodo 10.5281/zenodo.19986312) cannot be cited at all (double-blind violation).

**Net:** NeurIPS allows author-year, bracketed-numeric, **and** superscript-numeric forms. Constraint is internal consistency.

## 3. Format options

Each format is just a different `natbib` configuration. Authoring source stays the same (`[Anderson 1985]`); compile-time substitution chooses the form.

### 3.1 Author-year, parenthetical — `\citep{}` (CURRENT)

Sample inline:
> ...the bursting result of (Anderson, 1985), refined by (Boyd et al., 1994; Hasselmo et al., 1995)...

natbib config: `\PassOptionsToPackage{authoryear}{natbib}` (default). Bibstyle: `plainnat` (alphabetical, full names).

**Pros:** instant author/year context for the reader; standard NeurIPS / ICML / ICLR convention. **Cons:** **verbose** — each cite consumes ~15–35 characters; `(Bareinboim-Correa-Ibeling-Icard, 2022)` is ~45 characters.

### 3.2 Bracketed numeric — `[10, 12-14]`

Sample inline:
> ...the bursting result of [1], refined by [2, 3]...

natbib config: `\PassOptionsToPackage{numbers,sort&compress}{natbib}`. Bibstyle: `unsrtnat` (citation-order so bib `[1]` is first-cited, `[2]` second-cited, etc.).

**Pros:** ~4–7 characters per citation; `sort&compress` collapses runs (`[1, 3-5, 8]`); standard in TCS / theory. **Cons:** reader must flip to bib for context.

### 3.3 Superscript numeric — `text¹⁰⁻¹²` (Joseph's preference)

Sample inline (rendered):
> ...the bursting result of¹, refined by²,³...

natbib config: `\PassOptionsToPackage{numbers,super,sort&compress}{natbib}`. Bibstyle: `unsrtnat`.

**Pros:** most compact (~1–4 characters); fades into background. **Cons:** *math collision risk* — see §4.

### 3.4 Bracketed superscript — `text^[10]`

Sample inline (rendered):
> ...the bursting result of⁽¹⁾, refined by⁽²⁾,⁽³⁾...

Not native to natbib — requires a `\renewcommand{\@cite}{...}` patch wrapping the supers in brackets. Mitigates the math-collision risk because brackets visually distinguish citations from mathematical superscripts. Slightly longer than bare superscript (3–5 chars) but still much shorter than author-year.

**Pros:** compact + visually unambiguous in math-heavy papers. **Cons:** non-standard; needs a small hand-rolled patch.

### 3.5 Alphabetic key — `[And85, Boy94]`

Sample inline (rendered):
> ...the bursting result of [And85], refined by [Boy94, HSB95]...

natbib doesn't natively produce these labels; requires `alpha`-style or `alphanum` bibstyle.

**Pros:** compact AND informative — reader recognizes "And85" without flipping. **Cons:** uncommon outside pure-math journals (Annals, Inventiones, etc.); may read as old-fashioned to ML audience.

### 3.6 Author-year, narrative — `Anderson (1985)` (USED MID-SENTENCE)

natbib `\citet{}`. Used when the cited author is the sentence subject ("Anderson (1985) showed..."). Independent of the parenthetical/numeric/superscript choice — `\citet{}` adapts to whatever rendering you've chosen.

**Verdict:** keep as-is regardless of which §3.1–3.5 we pick — `\citet{}` always renders as "Anderson (1985)" or "[1] Anderson" depending on style.

## 4. Specific concern: superscript citations in math-heavy papers

Our papers are dense with raised quantities: `\pi^*`, `Q^*`, `V^*`, `\mathcal{C}^2`, `f^t`, `0.85^t`, `\|x\|^2`, etc. Bare superscript citations could create visual ambiguity:

```
   ...rate is 0.85^t per step¹⁵...
```

vs.

```
   ...rate is 0.85^t per step^15...
```

The reader scanning the second form for two seconds may briefly parse `step^15` as a math operation. The bracketed form

```
   ...rate is 0.85^t per step⁽¹⁵⁾...
```

is harder to misread.

[INFERENCE] Whether this is a real problem in practice depends on font, baseline shift, and bracketing. In Springer/Nature-style typesetting (where superscript citations are standard) it works because everything else is also visually distinct. In LaTeX with the NeurIPS sty, my prior is the bracketed superscript (§3.4) is the safer compact choice. Worth a single visual side-by-side render before committing.

## 5. Bibliography list

Bibstyle determines how the bib renders. Independent of in-text format.

| Bibstyle      | Sample entry                                                                | Order                      |
| ------------- | --------------------------------------------------------------------------- | -------------------------- |
| `plainnat`    | `Anderson, B. D. O. (1985). Adaptive systems, lack of persistency of...`    | alphabetical, full names   |
| `unsrtnat`    | `[1] B. D. O. Anderson. Adaptive systems, lack of persistency of...`        | citation-order             |
| `abbrvnat`    | `B.D.O. Anderson. Adaptive systems, lack of persistency of...`              | alphabetical, abbreviated  |
| `alpha`       | `[And85] B. D. O. Anderson. Adaptive systems, lack of persistency of...`    | alphabetical, alpha-key    |

For numeric in-text (§3.2 / §3.3 / §3.4), the natural pairing is **`unsrtnat`** so `[1]` in the bib equals the first-cited reference. Cleaner than alphabetical.

For author-year in-text (§3.1), **`plainnat`** is the standard.

## 6. What's typical at NeurIPS and in theory-CS / math

[PATTERN] Recent NeurIPS / ICML / ICLR — author-year is the dominant default. Numeric is allowed and sees occasional use, especially in theory-flavored papers under page pressure. Superscript is uncommon in CS / ML; I have no strong prior on whether it's been seen at NeurIPS.

[PATTERN] STOC / FOCS / SODA / ITCS (theoretical CS conferences) — bracketed numeric is the norm. Author-year is rare. Superscript is uncommon.

[PATTERN] Mathematical journals (Annals of Mathematics, Inventiones, Compositio) — alphabetic key (`[And85]`) is dominant.

[PATTERN] Nature, Science, biology / physics journals — superscript numeric is dominant. So readers from those backgrounds will recognize the form; readers from the CS / math background will find it slightly unusual.

[INFERENCE] The most "neutral" choice for an ML-audience theory paper is bracketed numeric (§3.2). The most "Joseph-preferred-and-still-acceptable" choice is bracketed superscript (§3.4). Pure superscript (§3.3) is technically allowed but unusual enough to warrant a quick visual check that math doesn't get confused.

## 7. LaTeX implementation

### 7.1 The one-line switch

For bracketed numeric:
```latex
\PassOptionsToPackage{numbers,sort&compress}{natbib}
\usepackage{neurips_2026}
\bibliographystyle{unsrtnat}
\bibliography{refs}
```

For superscript numeric:
```latex
\PassOptionsToPackage{numbers,super,sort&compress}{natbib}
\usepackage{neurips_2026}
\bibliographystyle{unsrtnat}
\bibliography{refs}
```

For bracketed superscript (custom):
```latex
\PassOptionsToPackage{numbers,super,sort&compress}{natbib}
\usepackage{neurips_2026}
\renewcommand\@biblabel[1]{[#1]}     % bracket the bib labels
\renewcommand\NAT@open{[}             % wrap super in brackets
\renewcommand\NAT@close{]}
\bibliographystyle{unsrtnat}
\bibliography{refs}
```

(The `\NAT@*` redefinitions need a quick test — natbib internals shift between releases.)

### 7.2 Multi-cite compression

`sort&compress` collapses `\citep{a,b,c,d,e}` (where the keys hash to numbers 1, 3, 4, 5, 8) into `[1, 3-5, 8]` automatically. Worth it if the paper has any 3+ cites in the same parenthetical (common in related-work paragraphs).

### 7.3 Bibliography auto-rendering

Once the build pipeline switches to `\bibliography{refs}` (Phase B work, see PIPELINE-TODO §C2), the manual `## References` markdown list in each paper goes away — natbib generates the list at compile time from `refs.bib`. Less work for authors, can't drift.

### 7.4 Mid-step compatibility

If we switch rendering format mid-stream (e.g., `[1, 2]` to `^{1,2}`), the bib stays the same; only the `\PassOptionsToPackage` line changes. Easy to A/B test on a single paper.

## 8. Authoring layer (decoupled from rendering)

Authors keep writing `[Anderson 1985]` / `Anderson [1985]` / `[A 1985; B 1990]` in segment markdown — this is a *semantic* marker. The build's substitution layer converts to natbib `\citep{}` / `\citet{}` and natbib does the rest.

So the open decision is **purely a `\PassOptionsToPackage` line** + bibstyle choice. No author-side change.

[POLICY] Implication for AUTHORING.md §2.3: keep the `[Author Year]` source convention; rendering is a separate decision that can flip without authoring impact.

## 9. Hallucination risk & verification (orthogonal but load-bearing)

Per `~/src/neurips2026/TODO.md` § Citation verification protocol — every cited paper must be verified against full text:
- DOI resolves
- Authors / year / venue / pages match the bib entry
- The claim attributed to the paper actually appears in its text
- Page reference (when given) is correct

The 2025 NeurIPS hallucination problem is real — even one fabricated citation can sink a submission per Code of Conduct. Existing `common/citation-verification-report.md` covers the May-4 verification pass; per-paper LOG entries note which entries were verified vs flagged.

Rendering choice (§3.x) does not change verification work at all. A wrong year / DOI / claim in the bib produces a wrong citation in any rendering.

## 10. Recommendations + open questions

**My pre-decision read:**

- **§3.4 (bracketed superscript)** matches Joseph's compactness preference while mitigating the math-collision concern. Slightly non-standard but allowed.
- **§3.2 (bracketed numeric)** is the safer, more conventional choice and almost as compact (4–7 chars vs 3–5 for superscript). Saves ~80% of the space vs author-year.
- **§3.3 (bare superscript)** is the most compact but I'd want a visual A/B side-by-side first to confirm the math collisions aren't a real reading-experience issue in our specific papers.
- **§3.1 (author-year, current)** is what every paper currently uses; moving away from it costs zero authoring effort but reclaims meaningful page space.

**Open questions for you:**

1. Visual A/B preference: render the same passage from B-N4 §3 (math-heavy) under §3.2 / §3.3 / §3.4 and pick by eye? Quick to do once `bin/build` has citation substitution working (Phase B).
2. `unsrtnat` (citation-order) vs `plainnat` (alphabetical) for the bib? Numeric in-text → unsrtnat is natural; if bib also serves as a "look up by author" reference, alphabetical may serve readers better even if `[1]` no longer maps to the first-cited paper.
3. If we go with bracketed-superscript (§3.4), is the extra `\renewcommand` patch worth the marginal compactness loss vs plain bracketed (§3.2)? My prior: marginal at best.
4. Per-paper choice or program-wide? All three papers are on the same template; consistency across all three reads better but isn't required by NeurIPS.

**My recommendation if forced:** §3.2 (bracketed numeric `[1, 3-5]`) + `unsrtnat`. Reclaims ~80% of the space-vs-author-year, doesn't risk math confusion, standard for theory papers at non-ML-track venues, allowed everywhere. If after a single visual A/B test the bare superscript (§3.3) doesn't visibly collide with math, switch to that for the extra ~30% character savings.

**Verification commitment:** rendering choice settled or not, every cite in `refs.bib` continues to need DOI/year/claim verification before submission. PIPELINE-TODO §C1 covers porting `refs-to-bib` + cite-substitution; §B4 covers anonymization of self-citation patterns.

---

*To be archived to `_archive/` once the rendering decision lands and the configuration is captured in `bin/build` + AUTHORING.md.*
