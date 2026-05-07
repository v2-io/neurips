---
name: Use git commit -- pathspec to avoid sweeping staged files into your commit
description: `git add <files>` followed by `git commit` will commit ALL staged files, including ones a per-paper agent had staged but not yet committed. Use `git commit -- <files>` to restrict scope.
type: feedback
originSessionId: 78516948-7863-4dc6-8a9b-72612fcd9600
---
**Rule.** When a per-paper agent has files staged in the index that you don't intend to commit, *plain* `git commit` after your own `git add` will sweep them in. Use `git commit -- <pathspec>` (or stage explicitly, see below) to bound what gets committed.

**The incident.** 2026-05-05 ~15:13 — I added a one-line tweak to `bin/refs-to-bib.py`, did `git add bin/refs-to-bib.py && git commit -m "..."`. The B-CS1 agent had previously staged 6 files of their N1-N2 strengthen-spike work (paper-draft, paper.tex, OUTLINE, LOG, long-form, the new _archive spike file). Those staged files all landed in commit `15cf13d` — labeled with my refs-to-bib message. The commit reads as a misleading mix: small script tweak + 770-line paper.tex change + spike report addition + 51-line paper-draft delta. Future archaeology of that commit will be confused.

**Why.** `git status -s` first column shows the index (staged) state, second column shows the working tree state. When the first column is `M ` (staged + clean), files are queued for commit. `git commit` (no pathspec) commits **everything in the index**, regardless of what `git add` invocation queued each file.

**How to apply.**

- Before any `git commit`, run `git status -s` and check whether the first column shows anything outside your intended scope.
- If you only want to commit specific paths and the index has other staged content, use `git commit -- <path> <path> ...` — this commits only those paths from the index, leaving other staged content alone.
- Or, before staging your own files, unstage anything you didn't intend to commit: `git reset HEAD -- <other-paths>`. Then add your own and commit.
- Multi-agent operating environment makes this trap routine: per-paper agents stage things and pause; build-agent commits and inadvertently rolls them in. Prefer the pathspec-bounded form by default.
- Recoverable if caught immediately via `git reset --soft HEAD~1` + re-stage. But don't rewrite history if the commit has been pushed; just acknowledge and continue.
