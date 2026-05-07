---
name: NeurIPS 2026 sprint — submissions complete, awaiting decisions
description: Three NeurIPS 2026 Main-Track submissions (B-N4, B-CS1, B-N8) complete 2026-05-07; sprint workspace at ~/src/neurips/ (umbrella with three submodules); decision window typically Sept; reciprocal reviewer registration done
type: project
originSessionId: 316c5020-93a0-46b2-8f5c-6c4c3f9a34f3
---
Sprint launched 2026-05-04 evening after Joseph's OpenReview profile activated; submissions completed 2026-05-07 with ~1.75 hours of runway before the noon-UTC paper deadline.

**Active workspace:** [`~/src/neurips/`](../../../neurips/) — umbrella repo with three submodules (`01-tragedy-confident-agent`, `02-unified-convergence-rl`, `03-llm-hallucinate-bound`). Cleaned up and pushed 2026-05-07.

**Earlier workspace:** `~/src/neurips2026/` (the sprint started here 2026-05-04; the umbrella migration happened 2026-05-05). Archived as `~/src/neurips/neurips2026.tar.gz` on 2026-05-07; original directory retained on disk for now.

**Three papers, all Main-Track-shaped (formal results + empirical/derivational anchor):**
- **B-N4** Tragedy of the Confident Agent — Lyapunov-survival exploration drive at low uncertainty + LMI directional FIM constraint. **Empirically validated** (variant_causal_ib: greedy 0% / Lyapunov-bounded 100% / mean reward 92.08).
- **B-CS1** Unified RL Convergence Theory Under Non-Stationarity — composes Two-Gap + BH identity + strategic tempo + Loop-as-Causal-Engine. Hardest assembly (cross-segment composition).
- **B-N8** Logogenic Bias Bound (κ × 𝒜) — conditional theorem with Track 1 (transport-inequality) + Track 2 (Fisher-Rao) + Attempt E no-go. Most mathematical.

**Track policy (confirmed by Program Chairs 2026-05-04, ~22:31):** Distinct papers from the same author may go to different tracks ("substantially different" required). No upper limit on per-author submissions across tracks. Email response from neuripsprogramchairs@gmail.com (Deisenroth, Doshi-Velez, Haghtalab, Rolnick).

**Track placement decision (2026-05-04):** All three → Main Track. PP was originally held as a hedge against a hypothetical "one-Main-one-PP" cap that didn't materialize. None of B-N4 / B-CS1 / B-N8 fit PP shape (all are theorem + empirical/derivational, not discursive position arguments). Joseph noted he has several PP candidates in the broader inventory but no time to assemble one for this cycle.

**Three Undermind prior-art queries** in `~/src/neurips2026/prior-art/` — B-N4 query already submitted with calibration follow-ups answered (broad mathematical lineage map; Tier 1 = direct anticipation, Tier 2 = compositional anticipation; lean hard into pre-2000 control/estimation literature). The other two queries (B-CS1, B-N8) ready to submit; expect calibration follow-ups.

**Key NeurIPS 2026 format constraints:** 9 content pages (figures count); 50MB PDF; 100MB supplementary ZIP; references/appendices/checklist don't count; double-blind anonymized; LaTeX template required.

**Critical verification task:** manually verify every citation in each paper given the documented 2025 NeurIPS hallucinated-citations problem. Reviewers actively flag this.

**Submission status (2026-05-07):** All 3 papers fully submitted with ~1.75 hours of runway before deadline. Joseph noted this as personal improvement on his deadline cadence. Reciprocal reviewer registration completed same day. Umbrella repo cleaned up + pushed 2026-05-07.

**Next decision window:** NeurIPS 2026 author notifications typically September. Until then the sprint is in wait-mode; the 3 papers can be revised in OpenReview during the rebuttal window only (no edits to the submitted PDFs themselves, but supplementary materials are amendable per handbook).

**Memory archive (2026-05-07):** Sprint-cycle memory files from `-neurips/`, `-neurips2026/`, this `-ops/` entry, and three NeurIPS-context feedback memories from `-src/` were copied into `~/src/neurips/claude-memories/` and committed alongside the umbrella repo. Provenance noted in that directory's README.

**Cross-references:**
- Inventory entries (canonical descriptions): [`~/src/ops/papers/02-asf-tier1-findings.md`](../../../src/ops/papers/02-asf-tier1-findings.md) for B-N4 / B-N8; [`papers/03-asf-tier2-and-cross-segment.md`](../../../src/ops/papers/03-asf-tier2-and-cross-segment.md) for B-CS1
- Strategic priority: [`papers/12-strategic-priority.md`](../../../src/ops/papers/12-strategic-priority.md) — context for why these three over other candidates
- AI disclosure approach: NeurIPS 2026 Main Track allows substantive AI assistance with author verification + acknowledgments + AI-use attestation; PP track may be stricter (verify before settling disclosure language). Joseph wants strict honesty about collaborative human-AI development.
