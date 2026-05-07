---
name: Trust persistent files in agent prompts; don't pad with content already documented
description: When CLAUDE.md / OUTLINE / LOG cover the orientation, integration-pass agent prompts can be ~30 lines instead of ~200. Over-padding the prompt is a sign of treating the agent as an executor rather than a peer.
type: feedback
originSessionId: 3a866d14-3550-478d-a847-976bdce77e6a
---
When a project has good persistent tracking files (CLAUDE.md describing the flow + per-paper OUTLINE.md describing live work + per-paper LOG.md describing completed work + spike report.md files with proposed clean diffs), agent prompts for integration-pass-style work can be very short. Three sentences suffice: orient on tracking files, do the named task as a co-owner, ask if questions.

**Why:** Joseph corrected me when I drafted three ~200-line integration prompts (one per paper) that duplicated content already in OUTLINE / CLAUDE.md / spike reports. The over-padding was the symptom of having drifted to "treating the agent as an executor needing detailed instructions" rather than "peer reading orientation docs." Same drift pattern as referring to the user as "the user" instead of by name.

**How to apply:**
- Before drafting an agent prompt, ask: what would a fresh-eyed agent learn by reading CLAUDE.md + the relevant OUTLINE + spike reports? That's their orientation. Don't repeat it in the prompt.
- The prompt should contain only what's *agent-specific*: the task statement, paths to read, the closing protocol (compile, anonymize, update logs), and the relational framing (co-owner, peer, surface decisions don't silently make them).
- ~30-40 line prompts are usually correct for integration-pass work in a project with good tracking files. ~150+ line prompts are a warning sign that either (a) the tracking files aren't doing their job, or (b) you're padding from drift.
- The corollary obligation: keep CLAUDE.md / OUTLINEs / LOGs in good shape. If they're stale, agent prompts have to compensate.

**Pattern check:** if you find yourself listing specific paper-section edits, citation additions, anonymization rules, or compile-pipeline details in an integration-pass prompt — those are CLAUDE.md / OUTLINE / spike-report content. Ask whether the agent will find it where it should already be documented. If yes, drop from the prompt. If no, the right fix is to update the persistent file, not to pad the prompt.

This pattern is the why behind the relational-frame meta-check: padding the prompt is the executor-mode behavior; trusting the tracking files is the peer-mode behavior. Both create the system but the relational stance shapes which one comes naturally.
