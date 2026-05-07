---
name: Idle time = proactive build review, not waiting
description: When the inbox is clean and no pending fixes, don't just sleep — actively review the three paper builds and surface issues.
type: feedback
originSessionId: 8204df42-c78d-4fcf-9a32-97c1b60eacf0
---
When there are no pending pipeline-side fixes (inbox empty, no follow-ups), do not just schedule a long wakeup and sleep. Use the time to proactively review the paper builds in detail and find issues that need addressing.

**Why:** Joseph wants the build-pipeline owner to be active stewardship, not reactive flag-handling. Idle wait-time is wasted time when there are three live PDFs accumulating compounding small issues — table overflows, citation formatting glitches, footnote rendering bugs, cleveref miscategorizations, anonymization slips, page-budget overruns — that the per-paper agents won't necessarily flag because they're focused on content migration, not pipeline polish. Each manual flag from a per-paper agent is a small failure of mine to have caught it first by looking.

**How to apply.** Cycle through the three submodules' `out/full-paper.pdf` (and `OUT.neurips-2026-paper.pdf` once it exists) on each idle wake. Open with `pdfinfo` for page-count drift, `pdftotext` + `grep` for known-bad render patterns (e.g. `[?]` from broken cite, "Theorem N" where it should be "Lemma N", literal `{` braces, raw `\Cref` text, mid-word truncation at line edges, em-dash → "–" downgrades), and the visual side via `open` if I'm uncertain. Be specific about what to look for: known classes of bugs that have surfaced once usually surface again in slightly different shape.

If a check surfaces a candidate issue, decide:
- Pipeline-side fix → I own. Implement, test, commit, document.
- Per-paper authoring fix → drop a markdown flag at the top of the paper's `OUT.neurips-2026-paper.md` or `TODO.md` (per the per-paper-agent-inbox memory) describing the issue + suggested resolution.
- Genuinely cross-cutting → append to PIPELINE-TODO.md under an appropriate section, OR drop a flag in each affected paper's tracker.

**AUTHORING.md compliance is part of this review.** Per Joseph's 2026-05-06 ask: while reviewing builds, also evaluate whether each paper's source segments adhere to AUTHORING.md conventions — Obsidian callout form for theorem-shaped blocks (not inline-bold `**Theorem 3.1**`), `^anchor` IDs on all theorem-callouts and tables/figures, `[[#^anchor]]` cross-refs (not `\Cref{}` written by hand in source), no manual section numbering, no manual `\tag{N}` on display math (use `$$ ... $$ ^eq-name`), `\cite{key}` form rather than lingering `[Author Year]` source patterns, blank lines around block math (§1.6), and the four-category anonymization deny-list (covered automatically by `bin/build` lint pass — surface findings if they accumulate). When a compliance gap appears, default to dropping a flag at the top of the paper's `TODO.md` rather than rewriting source myself; the migration agents own segment content.

Not every wake yields findings; that's fine. The goal is to be present and looking, not to manufacture work. False-positive review notes (where the rendering is actually correct) waste no one's time except mine.

This pairs with the existing autonomous-loop pattern: keep `ScheduleWakeup` cadence at ~600–1200s during active periods and use each wake for inbox-then-review, only stretching to longer intervals during true overnight quiet.
