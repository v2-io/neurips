---
name: Sibling agent memory directories
description: Where to find load-bearing context from agents that worked on this project from parent dirs
type: reference
originSessionId: 78516948-7863-4dc6-8a9b-72612fcd9600
---
Several agents worked on this sprint launched from `~/src/` and `~/src/ops/` rather than `~/src/neurips2026/`. Their memories live under different project keys.

**Likely-relevant sibling memory dirs:**
- `~/.claude/projects/-Users-josephwecker-v2-src/memory/` — agents launched from `~/src/`. CLAUDE.md cites `feedback_quantifier_disambiguation.md` here as a load-bearing pattern from this sprint (the "disambiguate quantifier scope before softening" sub-pattern).
- `~/.claude/projects/-Users-josephwecker-v2-src-ops/memory/` — agents launched from `~/src/ops/`. May contain program-level strategy memory.
- `~/.claude/projects/-Users-josephwecker-v2-src-agentic-systems/memory/` — upstream ASF working culture; the "strengthen before softening" principle came from there per CLAUDE.md.

**How to apply:** When I need context that isn't in my own memory or the project files, check these directories. Especially for:
- "Strengthen before softening" working principle
- Quantifier-disambiguation sub-pattern
- Program-level strategy / publication ladder framing

If a memory there is referenced in CLAUDE.md or TODO.md but I can't recall it, read it directly.
