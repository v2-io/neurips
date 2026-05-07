---
name: Use build tools sparingly; the build-pipeline agent has it covered
description: As a per-paper agent, don't redundantly run the converter / pdfinfo / pdftotext to "verify" your own markdown edits — the build-pipeline agent's continuous-build loop catches rendering issues on the next cycle.
type: feedback
originSessionId: 4982a806-beb1-46f9-8248-13d92749e28a
---
As a per-paper agent on the NeurIPS 2026 sprint, **use build-pipeline tools sparingly** — `python3 bin/convert_to_tex.py`, `pdfinfo`, `pdftotext`, `lualatex`. Joseph's stance (clarified 2026-05-05): not a hard prohibition, but a question of whether running them is actually useful.

**Why:** I ran the converter + pdftotext to "verify my body-pass edits compiled cleanly" (Pass-3 fixes: $B_T \to (B_T+1)$ propagation, theorem-hypothesis tightening, References-before-Appendix reorder). Joseph pushed back: it looked like I didn't really know what the build tools' output would tell me, suggesting I was running them more from anxiety-about-correctness than genuine need. The build-pipeline agent runs a continuous-build loop and surfaces rendering issues via `PIPELINE-NOTES.md` or `TODO.md` — redundant verification on my side just creates noise.

**How to apply:**

- After a markdown edit, **don't** automatically run the converter to verify. Trust that the build-pipeline agent's loop will catch any rendering breakage and surface it.
- **Do** run a build tool only when I have a specific question I can answer with its output (e.g., grep for a pattern in the rendered `.tex` to confirm a substitution landed; check the converter's stderr for a specific error message I'm expecting). If I don't know what the tool's output is supposed to tell me, I shouldn't be running it.
- For "did my edit compile?" — that's the build-pipeline agent's automation. They'll catch it.
- Stay at the markdown layer: edit `paper-draft.md`, document the change in OUTLINE/LOG, move on.
- Never `cd` into per-paper directories — keep working from project root so paths stay consistent and shell commands don't get tangled.
