# Claude Code memory snapshot — NeurIPS 2026 sprint cycle

Point-in-time archive (2026-05-07) of Claude Code memory files relevant to the NeurIPS 2026 submission sprint that produced the three Main-Track papers in this umbrella repo. Captured the day the papers were submitted; preserved here alongside the work so future readers can see how the sprint was actually run.

## What's here

These are copies. The live memory files continue to evolve under `~/.claude/projects/<project-slug>/memory/` on Joseph's machine; this snapshot freezes their state on 2026-05-07.

```
claude-memories/
├── from-neurips2026/    13 files — sprint-workspace memory (~/src/neurips2026/)
├── from-neurips/         2 files — umbrella-repo memory (~/src/neurips/)
├── from-ops/             1 file  — sprint-summary memory from ~/src/ops/
└── from-src/             4 files — NeurIPS-context lessons captured by agents launched in ~/src/
```

## Provenance per directory

### `from-neurips2026/` — sprint workspace
The largest cluster. Captured during the active sprint (2026-05-04 → 2026-05-07) when work happened in `~/src/neurips2026/`. Includes the build-pipeline-owner role definition, the per-paper-agent inbox protocol, the collaborator-framing stance, the voice/abundance/commit-discipline lessons that emerged across the cycle, and the cold-start orientation pointer to sibling memories.

Most load-bearing: `role_pipeline_owner.md`, `feedback_collaborator_framing.md`, `feedback_voice_no_100_percent.md`, `feedback_barrier_vs_multiplier.md`, `feedback_spike_agent_briefing.md`, `feedback_git_commit_pathspec_discipline.md`.

### `from-neurips/` — umbrella repo
Slim because the umbrella was created fresh on 2026-05-05 and most cycle-context lived under `from-neurips2026/`. The single feedback file (`feedback_triage_skips_strengthening.md`) is a late-cycle lesson worth carrying forward.

### `from-ops/` — sprint summary in the broader strategic context
Just `project_neurips_2026_sprint.md` from `~/src/ops/`. This is the program-level entry the rest of the operational documents pointed to when answering "what's the NeurIPS work, and where does it live?" Updated 2026-05-07 to reflect post-submission state.

### `from-src/` — agents launched at the parent level
Three feedback memories (and the `MEMORY.md` index that ties them together) from the project memory at `~/src/`. All three share an originSessionId from the NeurIPS sprint:

- `feedback_quantifier_disambiguation.md` — disambiguate iff/forced/exact claims into named readings before softening; strong readings are usually recoverable
- `feedback_trust_persistent_files.md` — when CLAUDE.md / OUTLINE / LOG cover orientation, integration-pass agent prompts can be ~30 lines instead of ~200
- `feedback_verify_before_archive.md` — verify integration before moving content to `_archive/`; archiving before integration breaks the audit trail

The `MEMORY.md` index in this directory is the broader `~/src/`-scoped index, not NeurIPS-specific; it's preserved here so the three feedback files remain findable in their original organizational context.

## What this snapshot is *not*

- Not a live source. The originals at `~/.claude/projects/<slug>/memory/` continue to be read and updated by future Claude Code sessions; this archive will diverge from them over time.
- Not the project notes themselves. The actual sprint working notes (`HANDOFF.md`, `PRAXES.md`, `STYLE.md`, `LOG.md`, per-paper `OUTLINE.md` / `LOG.md`, the build-pipeline scripts in `bin/`) live in the umbrella repo and its submodules. This `claude-memories/` directory complements those by capturing the meta-layer: how the agent-collaboration was shaped, what corrections recurred, what role definitions emerged.
- Not a comprehensive ops archive. Memories about the broader publication strategy, funding situation, networking relationships, and ethical framings live in `-ops/` memory and were *not* copied here — only the single sprint-summary memory was, since those other memories pertain to work outside the NeurIPS scope.

## Why preserve this alongside the repo

Claude Code memory files are normally invisible to anyone who doesn't have access to Joseph's `~/.claude/` directory. Capturing them next to the artifacts they helped produce makes the agent-collaboration record reviewable: a future researcher (human or agent) reading the three NeurIPS papers can also read what working principles, voice norms, and coordination protocols were carried across the sprint cycle that produced them. That's the intended audience.

## Snapshot metadata

- **Date captured:** 2026-05-07
- **Sprint workspace at capture:** `~/src/neurips/` (umbrella, three submodules)
- **Earlier workspace:** `~/src/neurips2026/` — archived as `~/src/neurips/neurips2026.tar.gz` on the same date
- **Total files:** 20 markdown files across four source projects
