# AGENTS.md — Working principles for agents on this project

*Canonical agent guidance for the `neurips/` umbrella. `CLAUDE.md`, `GEMINI.md`, etc. will be symlinked to this file once it stabilizes. Sits alongside `restructure-plan.md` (active workstream) and `MIGRATION.md` (migration log from `~/src/neurips2026/`).*

Captures policies that govern HOW agents work here. WHAT is being built lives in `restructure-plan.md` and the per-paper submodules.

---

## Language policy

**Default: Ruby.** Scripts in `bin/` and supporting libraries are written in Ruby. Ruby's syntactic uniformity gives less surface for stylistic drift than Python; bash's quoting / IFS / pipe-failure traps are best avoided entirely. The empirical observation across multiple LLMs and projects has been that Ruby code stays more consistent across iterations.

**No file extensions on executables.** Scripts in `bin/` are extension-less; the consumer doesn't need to know what language they're in. The shebang at the top of each script (`#!/usr/bin/env ruby`) declares the interpreter for anyone reading the source.

**Carve-out — other languages when an upstream library makes them the right tool.** When using Python (or anything else), justify with a comment near the top:

```python
#!/usr/bin/env python3
# Reason: pylatexenc has no Ruby equivalent; we need its lualatex AST parser.
```

Explicit exception, not a loophole. The carve-out should name a specific upstream library without a Ruby equivalent. Examples that qualify: `pylatexenc`, `bibtexparser`, ML/NLP toolchains. Examples that don't: shell-out orchestration, regex, file IO, manifest parsing — Ruby handles those cleanly.

## Style enforcement

Ruby code is checked against `.rubocop.yml`, which uses [`rubocop-tablecop`](https://github.com/v2-io/rubocop-tablecop) for table-shaped layout (column-aligned assignments, methods, case branches). The LLM-discipline benefit of Ruby-by-default only materializes when style is enforced. The `.rubocop.yml` is adapted from `~/src/autopax/.rubocop.yml` (canonical reference for the tablecop philosophy); `Gemfile` pins the rubocop / rubocop-tablecop / rubocop-performance versions.

**Workflow for any Ruby edit:**

1. Edit the script.
2. Run `bundle exec rubocop <path>` (or unscoped `bundle exec rubocop` for full sweep).
3. Address every offense. Use `bundle exec rubocop -a <path>` for *safe* autocorrects; never use `-A` (unsafe autocorrect) without diff review.
4. If a cop genuinely doesn't fit a specific case, add an exception to `.rubocop.yml` with an inline comment explaining the rationale (or a per-line `# rubocop:disable` if scope is narrow). Drift in `.rubocop.yml` should be visible and justified.
5. Aim for zero offenses before committing. Style-lint is not optional polish — it's part of "done."

**Lint-as-build (forthcoming).** The kramdown-based markdown→TeX pipeline (`bin/build`) will subsume project-specific source-side lint as a side-effect of AST traversal — em-dash / section-ref / citation-form / bold-around-math / theorem-callout-integrity / anonymization-vocab checks. Rubocop covers Ruby; the build covers the markdown segments. No standalone style-lint tool — lint is the early-exit form of the build.

---

*Will grow as we discover patterns. Current scope: language + style + rubocop workflow.*
