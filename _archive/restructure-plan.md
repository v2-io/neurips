## Toplevel & Overall Organization

- [ ] Git submodules for each of the three papers
- [ ] Better praxes & workflow documented, affirmatively agreed to, and monitored
- [ ] Better primary agent and subagent onboarding


## Per Paper Submodule / Repository

- Each `OUT.*` file is plain markdown and a *table* (for tracking) that is the order in which any subset of `src/` fragments are concatenated, **ala ~/src/agentic-systems/ (nested) OUTLINE.md and src and build scripts**.  e.g.,:

```
OUT.full-paper.md
OUT.neurips-2026-paper.md
src/01-title
    02-abstract
    ...
    04-discussion/part-1.md
                  part-2.md
                  extended.md
```


- **Segment the papers**
    - [ ] Break up paper parts into segments (more adhoc than ASF)
    - [ ] Outline for full-works
    - [ ] Outline for neurips paper
    - [ ] Better bibliography and citation checklist
    - [ ] Paper checklist (for paper so that we can start filling out the sections) -- these will be TeX input segments instead of markdown (I think)
    - [ ] (Correct ordering for references and appendices and checklist)

* This way segments can be reused between "full" and trimmed "paper"
* Segments can be orphaned as needed

## Additional Per Paper Directories

- [ ] audits/ *Audit landing directory*
- [ ] out/ *Build artifact landing (for **checking flow of assembled markdown**, and output LaTeX along w/ any errors etc.)*
- [ ] spikes/ *For temporary spikes*
- [ ] simulations/
- [ ] results/ *raw empirical results etc.*


## Style Guide / Normalization

*Carry forward from the prior workspace's `STYLE.md` + `PRAXES.md`. Becomes more important under segmentation: any per-segment drift surfaces at concat time, and segments may be reused across `OUT.full-paper.md` / `OUT.neurips-2026-paper.md` / future-venue manifests, so the conventions need to apply uniformly regardless of which manifest a segment ends up in.*

- [ ] **Em-dash / en-dash / hyphen** — em-dash `—` no spaces (`text—text`); en-dash `–` numerical ranges only; hyphen `-` for compounds. Pipeline-side em-dash space normalization (deferred from prior session — never landed).
- [ ] **Section references** — `§N` / `§N.M` mid-sentence; `Appendix A` (full word) for appendix references.
- [ ] **Citations** — markdown inline `[Author Year]` / `Author [Year]`; pipeline substitutes to natbib `\citep{key}` / `\citet{key}` at compile. Single shared `refs.bib` (currently 162 entries; lives at parent or per-paper — TBD). Numeric vs author-year switch is a one-line config worth revisiting (≈1–3 pp reclaim on B-N8).
- [ ] **Theorem / lemma numbering** — section-based `Theorem N.M`; avoid 3-level (`Lemma 4.1.1`) and avoid paper-level integer counters. Currently inconsistent across the three drafts; segmentation is a natural moment to normalize.
- [ ] **Pandoc edge cases** — bold around digit-adjacent `$math$` (`**2$\times$2**`) breaks math-mode pairing; documented workarounds. `bin/style-lint` flags.
- [ ] **Quotes** — straight `"` / `'` in source; pandoc with `markdown+smart` converts to curly automatically. Don't paste curly quotes into source.
- [ ] **`et al.`, `i.e.`, `e.g.`** — period after `et al.` always; comma after `i.e.,` / `e.g.,` always.
- [ ] **Formal voice** — active in proofs and prose; no chronicle voice in theorem text ("Landed 2026-05-05", "the Pass-2 strengthening lifted ..."); no "100%" / "comprehensive" / "fully complete"; canonical `future AI` (avoid superintelligence/AGI vocabulary). Diff-voice belongs in Working Notes only.
- [ ] **Math notation** — LaTeX form in markdown source (`$\delta_{\mathrm{sat}}$`); Unicode in agent chat.
- [ ] **Anonymization vocabulary** — four categories carried forward: Personal identifiers (Joseph / Wecker / email / ORCID / GitHub handle); Framework proper-nouns (ASF / AAD / PROPRIUM / AXIOMATA / CHRONICA / VERA / MEMORATA); ELI names (Zi-am-tur / Anamnos / Lumin / Architectus / Resonance / Soren / Tartur / Calyx / Katan / Synesis / Proto-Architectus / Temporal); Reviewer-priming vocabulary ("directed separation" → "architectural separation"; etc.). Self-citation policy: ASF Zenodo DOI must NOT appear (double-blind violation).
- [ ] **Tooling carry-forward** — `bin/style-lint` (audit, `--fix` for safe fixes); `bin/check-anonymization` (four-category scanner). Need adaptation to segmented layout: each `src/{slug}.md` becomes a lint target, plus the assembled `OUT.*` outputs.
