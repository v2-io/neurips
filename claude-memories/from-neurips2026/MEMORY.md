# Memory Index

## Role
- [Build pipeline + formatting owner role](role_pipeline_owner.md) — what I own, what's out of scope, how to engage with per-paper agents.
- [Joseph's collaborator framing — full co-owner, not task executor](feedback_collaborator_framing.md) — autonomous, opinionated, proactive; drop feedback markdown in per-paper dirs when I see something.

## Project
- [Build-pipeline owner agent (separate ownership)](project_build_pipeline_owner.md) — separate agent owns `bin/`, `common/`, LaTeX template, supplementary-ZIP. Don't reach into their territory; surface cross-paper build issues to them.

## Feedback
- [Abundance mentality — serve truth, not a clock](feedback_abundance_mentality.md) — drop deadline-anxiety framing; constricted thinking erodes quality. Strengthen-before-soften applies even when "improbable."
- [How to surface build/formatting issues to pipeline owner](feedback_pipeline_communication.md) — append to project-root `TODO.md` under a build/formatting section; reverse channel is markdown drops into per-paper dirs.
- [Per-paper agents read their own directory, not root TODO.md](feedback_per_paper_agent_inbox.md) — for URGENT items, root TODO is necessary but not sufficient; also drop a flag at the top of the paper's OUTLINE.md.
- [Voice discipline — avoid "100%" / "comprehensive" / "fully complete"](feedback_voice_no_100_percent.md) — PRAXES §2+§6; I lapsed twice on the natbib migration. Match language to actual state; mark uncertainty explicitly.
- [Use `git commit -- <pathspec>` to bound commit scope](feedback_git_commit_pathspec_discipline.md) — `git add` + `git commit` will sweep in any staged files (including a per-paper agent's pre-staged in-progress work). I made this mistake in commit `15cf13d`. Always use pathspec-bounded form when other agents' work might be staged.
- [Use build tools sparingly; build-pipeline agent has it covered](feedback_dont_run_build_pipeline.md) — don't redundantly run `convert_to_tex.py` / `pdfinfo` / `pdftotext` to "verify" markdown edits; only run a build tool when you have a specific question it can answer.
- [How to brief spike agents](feedback_spike_agent_briefing.md) — Opus 4.7; push hard from many angles; record failures as diligently as successes; point at `~/src/agentic-systems/` + `~/src/agentic-systems/ref/INDEX.md`; allow web search + paper-download requests.
- [Idle time = proactive build review, not waiting](feedback_idle_time_review_builds.md) — when inbox is clean, cycle through the three paper PDFs looking for known-bad render patterns and quietly fix or flag what you find.

## References
- [Sibling agent memory directories](reference_sibling_memory.md) — `~/.claude/projects/-Users-josephwecker-v2-src{,-ops,-agentic-systems}/memory/`. Joseph's user profile, strengthen-before-soften principle, quantifier-disambiguation pattern, naming conventions all live there.
- **PRAXES.md at project root** — comprehensive surfacing of working principles, cognitive stance, workflow conventions, multi-agent coordination, voice/tone, anti-patterns. ~292 lines, distilled from this project's memory + sibling memories + CLAUDE.md + in-flight Joseph corrections. Read selectively per task; canonical sources still win on disagreements.
