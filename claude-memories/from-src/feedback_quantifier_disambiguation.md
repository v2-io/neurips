---
name: Disambiguate quantifier scope before softening audit-flagged claims
description: When an audit flags a load-bearing iff/forced/exact/universal claim as too-strong, disambiguating the quantifier scope into named readings is consistently more productive than the default soften — strong readings are usually recoverable
type: feedback
originSessionId: 3a866d14-3550-478d-a847-976bdce77e6a
---
When an audit flags a load-bearing iff (or "forced", "exact", "universal") claim as too-strong / "worst-case sharp" / overclaim, **disambiguate the quantifier scope into named readings before deciding to soften**. The "too-strong" symbol is often compressing several distinct claims with different truth values; the strongest reading is usually the one the paper informally meant, and disambiguation recovers it under explicit hypotheses.

**Why:** Empirically validated across the NeurIPS 2026 Pass-2 strengthen sweeps (May 2026). The pattern was consistent across multiple papers and findings:

- B-N4 T3 "α > ρ/R iff persistence" was compressing three readings: universal-trajectory iff (false), robust-persistence iff (right reframe), adversarial-witness iff (recoverable in linear-correction case + finite exit-time bound as bonus).
- B-CS1 C2 "Unified convergence theorem" was compressing per-round regret coordinate / ultimate boundedness / KL coordinate estimability / cumulative dynamic regret. C2(a) cumulative dynamic regret cracked even though C2(b) pointwise convergence was structurally unavailable.
- B-CS1 C4 "every agent eventually violates" was compressing scope over update-mechanism class. Disambiguating into $\mathcal{A}_{\mathrm{accum}}$ (universal failure) and bidirectional-threshold mechanism classes recovered the strong claim within named scope.
- B-N4 T2 "either family member enforces threshold" was compressing 1D vs multi-D scope. F/A/G/P disambiguation recovered strong claim under explicit hypotheses with the 1D/multi-D split as load-bearing clarification.
- B-N8 H4 "(PI) is necessary" was conflating "(PI) is the unique commitment" (false; Hellinger/χ²/Rényi all chart-independent) with "(PI) + (R) + (K) uniquely forces Fisher-Rao + √2" (true). Disambiguating found the strong reading.

In every case Codex's audit identified the surface conflation but stopped at the standard soften; pushing one more step to disambiguate the quantifier scope revealed the readings don't collapse, and the strongest one was recoverable. The matrix lifts, sector-tightness diagnostics, structural-class characterizations, and cross-spike unifications that fell out of these disambiguations were not visible from the original surface claim.

**How to apply:** When an audit surfaces an iff/forced/exact/universal/every claim as "too-strong" or "worst-case sharp" or recommends softening:

1. *Before* writing the soften, ask: what readings is this symbol compressing? Quantifier scope (over trajectories? disturbances? agent classes? hypotheses?), conclusion conjunction, hypothesis-quantifier-scope.
2. Name each reading explicitly. Each has its own truth value.
3. Often the strong reading is recoverable under named hypotheses; the weak readings can soften.
4. The strong reading is usually what the paper informally meant — recovering it preserves the contribution while making it provable.

The "soften the whole thing" move treats the claim as monolithically too-strong and loses the recoverable content; the "disambiguate first" move surfaces the recoverable content. Audit cycles tend to under-deliver here because they're calibrated for surface-flag detection, not for downstream disambiguation work — which means the strengthen-attempt is where this work has to happen.

This pattern interacts with the strengthen-before-softening principle (`~/src/agentic-systems/CLAUDE.md`): strengthen-first is the *what*; quantifier-disambiguation is often the *how* when the audit-flagged claim is a compressed quantifier statement.
