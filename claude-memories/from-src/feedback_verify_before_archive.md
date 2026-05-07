---
name: Verify integration before moving content to _archive/
description: Before moving spike directories or audit relics to _archive/, verify that the findings are documented in TODO/OUTLINE/LOG. Archiving content whose findings haven't been integrated breaks the audit trail.
type: feedback
originSessionId: 3a866d14-3550-478d-a847-976bdce77e6a
---
`_archive/` directories (project root + per-paper) are for *frozen artifacts whose findings have been integrated into the live tracking files*. Archiving content before the integration is documented breaks the audit trail — the finding then exists only in the archived artifact, not in the navigable working files.

**Why:** Joseph caught me archiving B-CS1 Pass-3 audits before verifying their body-pass items had been integrated. The B-CS1 LOG explicitly said "body-pass items pending (load over the next ~48h)" — meaning the audit content was still active source material. Restored the audits to paper-root.

**How to apply:** Before any `git mv X _archive/Y` or `mv X _archive/Y`:

1. Read the LOG for the paper (or project root) that should reference X. If X is a spike report, look for an integration entry that maps the spike's findings to specific paper sections. If X is an audit relic, look for a resolution table covering each finding.
2. If the LOG doesn't explicitly document the integration, do not archive. The integration may be partial (some findings folded, others pending) — read the LOG entry carefully for "pending" or "still load" language.
3. The naming convention for archived spikes/audits: `_archive/YYYY-MM-DD-spike-<name>/` or `_archive/YYYY-MM-DD-AUDIT-{codex,gemini}.md`. Match the existing convention in the destination directory.
4. After archival, update path references in OUTLINE.md and LOG.md so links still work (LOG.md is "append-only" but updating broken paths is keeping the record functional, not rewriting history).
5. If multiple agents ran (per-paper integration agents), each agent has authority over their paper's archival. Cross-paper consolidation passes (like a stabilization sweep) should still verify each paper's archival pre-conditions independently.

**Sub-pattern:** spike directories typically archive *after* the proposed clean-diff edits land in `paper-draft.md` AND a follow-up audit pass confirms the integration is sound. Audit relics typically archive *after* the audit's findings are each addressed (resolved or explicitly deferred) per a resolution table in LOG.

This pattern interacts with the "trust persistent files in agent prompts" memory: archiving content prematurely puts pressure on agent prompts to compensate by re-introducing context that *should* live in the working files.
