# `_archive/` — frozen artifacts

Move-via-`git mv` destination for content whose findings have been integrated and which no longer feeds active work. Examples: completed audit relics (post-integration), spike directories whose proposed diffs have been applied, generation reports that informed a finished decision.

**Move policy:** `git mv <source> _archive/<source>` — preserves git history. Never copy-and-delete; the audit trail matters.

**Verify before archiving:** read the relevant `LOG.md` entry to confirm "integrated" before any `git mv`. The check costs almost nothing; the recovery from a premature archive is expensive. (See sibling-project memory `feedback_verify_before_archive.md` if unfamiliar with the rationale.)

Per-paper submodules each have their own `_archive/` for paper-specific frozen artifacts; this top-level one is for project-wide / cross-cutting artifacts only.
