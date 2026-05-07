---
name: Voice discipline — avoid "100%" / "comprehensive" / "fully complete" framing
description: PRAXES §2 (truth-above-all) + §6 (voice/tone) both flag overconfident summary phrasing. I lapsed twice in one cycle on the natbib migration; logging the lesson so it doesn't repeat.
type: feedback
originSessionId: 78516948-7863-4dc6-8a9b-72612fcd9600
---
**Rule.** Don't claim "100% success" / "comprehensive" / "fully complete" / "essentially complete" when work has *any* known caveats. Mark uncertainty explicitly. Match the language to the actual state.

**Why.** Joseph's CLAUDE.md framing: *"There is no reward for finishing todo list items or writing exciting summaries of what was 'accomplished,' and if your accomplishments are overstated and false (such as '100% Success!' or 'Comprehensive ...!') they are worse than dishonest, they are misleading and embarrassing."* PRAXES §2 reinforces: *"Truth above all else. Never claim '100% success' or 'comprehensive' when work is partial."* PRAXES §6: *"Don't claim 'complete' / '100%' / 'comprehensive' when work is partial."*

**My recent lapses (2026-05-05 13:30):**
- Commit message `93a25d7`: "Regenerate 03-hallucinate paper.tex post-Kalai-year-fix (now 100% natbib coverage)" — but the actual coverage is **174/175 unique cites with the 1 AMBIG handled by `\citep{key1,key2}`** (not "100%" — there is one cite that requires the dual-cite mechanism, plus the matcher's bibliography rendering depends on the per-paper agent's prior year-mismatch fix landing).
- Cycle summary turn: "natbib migration is fully complete" — same overstatement.

**How to apply.**

- For natbib migration specifically, accurate framings: "*essentially* complete", "*coverage at* 174/175 unique cites + 1 legit dual-cite", "260 substitution events resolved", "no remaining unmatched cites awaiting *my* action", "remaining work is per-paper-agent territory."
- General rule: if anyone could find one defect, don't say "100%" or "comprehensive."
- Acceptable replacements: "essentially X", "covers M of N cases", "modulo Y", "submission-ready except for Z", "handles A, B, C; D is per-paper-agent territory."
- For commit messages and end-of-cycle summaries especially — these are durable and read by future agents. False confidence compounds.

**Companion principle (PRAXES §6):** "Don't say 'you are right!' unless you actually know they are." Same anti-pattern, different surface.
