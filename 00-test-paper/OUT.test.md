# OUT.test.md — Test paper assembly manifest

*Concatenation order for the test paper. Each row is a segment in `src/`; assembly is top-to-bottom. The manifest IS the assembly order. `\appendix` is auto-injected before the first row whose Type is `Appendix`; `\newpage` is auto-injected before any `Checklist` row.*

| § | Type       | Slug                                | Title                       | Stage |
|---|------------|-------------------------------------|-----------------------------|-------|
| 1 | Section    | [intro](src/01-introduction.md)     | Introduction                | draft |
| 2 | Section    | [theory](src/02-theory.md)          | Theory                      | draft |
| 3 | Section    | [results](src/03-results.md)        | Results                     | draft |
| – | References | [refs](src/04-references.md)        | References                  | draft |
| A | Appendix   | [proofs](src/A-proofs.md)           | Proofs                      | draft |
| B | Appendix   | [supp](src/B-supplementary.md)      | Supplementary               | draft |
| – | Checklist  | [checklist](src/checklist.tex)      | NeurIPS paper checklist     | ready |
