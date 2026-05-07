---
name: Per-paper agents read their own directory, not root TODO.md
description: Routing rule for surfacing build/formatting issues to specific per-paper agents — drop into the paper's OUTLINE.md (or PIPELINE-NOTES.md), not just root TODO.md.
type: feedback
originSessionId: 78516948-7863-4dc6-8a9b-72612fcd9600
---
**Rule.** When a build/formatting issue is specific to one paper and is URGENT (e.g., the build is currently broken), surfacing it in root `TODO.md` is necessary but not sufficient — per-paper agents do not actively watch root `TODO.md`. They watch their own working directory (`<paper>/OUTLINE.md`, `<paper>/LOG.md`, `<paper>/paper-draft.md`, etc.). Drop a clearly-marked note inside the paper's directory too (`<paper>/OUTLINE.md` is the most actively-watched single file; `<paper>/PIPELINE-NOTES.md` is acceptable but transient).

**Why.** Joseph corrected this on 2026-05-05 mid-morning when I'd surfaced a B-CS1 build-broken issue only in root `TODO.md`. He said: *"B-CS1 doesn't watch TODO -- he watches the work in his own directory -- you can drop a note or add it to his OUTLINE.md."* The routing protocol from earlier ("appending to project root-level TODO.md" for build/formatting errors) makes TODO.md the canonical record, but per-paper agents won't see it in time for urgent items.

**How to apply.**

- Routine, non-urgent build/formatting issues: append to root `TODO.md` only. Per-paper agents will see them eventually via Joseph or a sweep.
- URGENT items (build broken, anonymization desk-rejection-grade hit, time-sensitive citation question): root `TODO.md` AND a clearly-marked block at the top of the paper's `OUTLINE.md`. Mark it as a build-agent flag with a "safe to delete after fix" tag so the agent knows to excise it once acted on.
- Reverse direction (per-paper agent surfaces a request to me): they append to root `TODO.md` under "Open build/formatting issues." That direction works fine — *I* watch root TODO.md.

**Don't:** edit `paper-draft.md` directly to flag issues (that's their content territory; the diff would clutter their commit). The OUTLINE.md drop is the right surface — visible, easily removable, and outside the submission body.
