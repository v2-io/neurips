# 00-test-paper — Pipeline harness

Synthetic test paper used to develop and regression-test the build pipeline at `~/src/neurips/bin/build`. Not a real paper — content is intentionally minimal and exists to exercise the pipeline's handling of theorems, multi-appendix structure, tables, figures, citations, and typographic edge cases.

Not a submodule. Lives directly in the umbrella so the pipeline can iterate against it without crossing repo boundaries.

## Structure

- `meta.md` — title, authors, abstract (YAML frontmatter + abstract body).
- `OUT.test.md` — assembly manifest. Table format, ASF-style — each row is a segment, top-to-bottom is the assembly order.
- `src/` — segment files. Markdown (`.md`) goes through pandoc; raw LaTeX (`.tex`) is included verbatim.
- `refs.bib` — small test bibliography (used in Phase B+ for natbib testing).
- `out/` — build artifacts (gitignored).

## Usage

From the umbrella root:

```bash
bin/build 00-test-paper
```

Output: `00-test-paper/out/test.pdf`.
