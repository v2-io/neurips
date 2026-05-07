---
name: How to brief spike agents (Joseph's standing guidance)
description: When launching exploratory / investigative subagents for math spikes, prior-art surveys, restructure attempts, etc. — model, framing, resource pointers, failure-recording
type: feedback
originSessionId: 4982a806-beb1-46f9-8248-13d92749e28a
---
When launching exploratory or investigative subagents (math spikes, restructure attempts, prior-art surveys, de novo audits, anything that requires the agent to push on a hard problem and find structure rather than execute a known plan), apply Joseph's standing guidance (2026-05-05 evening):

**1. Model: Opus, ideally 4.7.** Spike work demands the largest cognitive capacity available. The Agent tool's `model` parameter accepts `opus` (which uses the latest Opus version available to the harness). Set it explicitly. Do NOT default to general-purpose's default model for spike work.

**2. Push hard from many angles.** Tell the spike: don't take the first viable approach. Try multiple. If approach 1 looks promising, also try approaches 2, 3, 4 — different framings, different lemmas, different decompositions. The space of approaches is itself the territory being mapped, not just the one that succeeds.

**3. Record failures as diligently as successes — and read failures for structure, not just to avoid repeats.** Joseph's deeper framing (2026-05-05 evening): *"a thoughtful attempt that fails reveals something fundamental that almost always leads to a strengthening or deeper understanding."* The failure-narrative isn't a documented-dead-end (so future agents don't retread); it's *information about the structure of the problem*. The obstruction itself is the discovery.

Concrete examples from this project:
- B-N4 Pass-2 T1: the KKT-shadow-price-divergence strengthen *failed* (closed-form $\rho^2/(2R^2 + \rho^2)$ via DARE shows shadow prices stay BOUNDED). But the failure unlocked a sharper framing: *the tragedy is environment-side (worst-case exit time diverges) not controller-side (shadow price bounded)*. The failure was the discovery.
- B-CS1 Pass-2 strategic-tempo: Codex's literal sum-form recommendation *failed* under adversarial disturbance. The failure revealed the bottleneck-form is the right Lyapunov object — a strictly stronger result than what the audit asked for. The failure-of-the-softening produced the C3 strengthen.

How to read a "failed" spike result: not "give up and narrow" but *"what does this obstruction tell us about the structure?"* Possibilities for any failed-strengthen:
- The strengthen requires an additional condition we hadn't surfaced → sharpens scope statement
- The strengthen requires a constant we can't bound → reveals a fundamental obstruction worth naming
- The strengthen reveals two distinct theorems where we thought there was one → sharper structure
- The strengthen reveals a coupling we hadn't captured → new concept

The spike report should include "approaches tried that didn't work, and exactly why" — not as embarrassed footnotes but as primary content. The "why" is the result.

**4. Tell them about local resources** they may need:
- `~/src/agentic-systems/` — ASF working-paper source materials. The B-CS1 OUTLINE.md lists the load-bearing dependencies (`01-aad-core/src/def-satisfaction-gap.md`, `def-control-regret.md`, `deriv-strategy-cost-regret-bound.md`, `def-strategic-tempo.md`, `schema-strategy-persistence.md`, `scope-agent-identity.md`, `der-loop-interventional-access.md`, `der-causal-hierarchy-requirement.md`, `def-value-object.md`, `result-persistence-condition.md`). These are the original derivations the paper is built from.
- `~/src/agentic-systems/ref/` — has an `INDEX.md` cataloguing reference papers and external resources. Good place to look for adjacent literature.

**5. Web access.** They can:
- Use WebSearch + WebFetch to look at any existing literature.
- Search for adjacent prior work that might confirm/contradict their working hypothesis.
- **Pass on a request** for any paper they want downloaded but can't access — they can flag this in their report and someone (Joseph or a sibling agent) can retrieve.

**6. Length / format of report.** Spike reports are *cognitive-work* artifacts, not just summaries. The report should:
- Lead with the bottom-line finding (what was learned, what's still open).
- Document each approach attempted, with as much detail on the failures as the successes.
- Include any concrete proposed edits to the paper (clean diffs the per-paper integration agent can mechanically apply) when applicable.
- Flag anything that warrants Joseph's strategic call separately at the end.

**Counter-example (don't apply this guidance):** pure-execution agents that apply pre-specified mechanical edits, citation lookups against a defined list, or other bounded-deterministic tasks. For those, ordinary general-purpose with default model is fine; the "push hard from many angles" framing would just confuse them.
