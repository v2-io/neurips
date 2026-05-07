---
name: Barrier-vs-multiplier confusion (load-bearing pattern across the project)
description: When a 1/(slack) expression appears in survival/persistence contexts, ask whether it's a barrier function or a Lagrange multiplier — they have opposite scaling behavior, and conflating them is a recurring source of overclaim
type: feedback
originSessionId: e233259c-e387-4bd3-a70c-aff74afab369
---
When a $1/(\text{slack})$-shaped or "diverges-at-the-boundary" expression appears in survival, persistence, or constraint-closure contexts, **always ask**: is this a barrier function or a Lagrange multiplier?

- **Barrier function**: a regularizer added to the optimization objective (e.g., $\log(b - g(x))$ or $1/(b-g(x))$) that diverges at the constraint boundary *by construction*, to keep iterates feasible. Numerical-optimization mechanism.
- **Lagrange multiplier (KKT shadow price)**: the slope $\partial V^*/\partial b$ of the optimal value function in the constraint parameter $b$. KKT theorem says it equals the dual variable at optimum. *Whether this diverges at the boundary depends on whether $V^*$ does.*

**The two have opposite scaling behavior at the same level set.** A barrier blows up *by construction* at the constraint level set. A Lagrange multiplier blows up *only if* the value function does — for bounded value functions, the multiplier stays finite at the constraint level set; the multiplier only diverges at *infeasibility* (where the program has no feasible point).

**This confusion has appeared three independent times on this project** as of 2026-05-05:

1. **Original ASF heuristic** (`~/src/agentic-systems/01-aad-core/src/deriv-causal-ib-exploration.md` line 53): wrote $\lambda' \propto 1/(U_o^{\max} - \mathbb{E}[U_o])$ as if it were a KKT multiplier. It's a barrier-function intuition. The Pass-2 spike (`01-tragedy/_archive/2026-05-05-spike-kkt-divergence/`) caught this and downgraded to "controller-design overshoot of a finite Lagrangian gain."

2. **Gemini Pass-5 audit on B-N4**: read "value function has a cliff at the survival boundary" → concluded "multiplier is infinite at the cliff." Wrote a chain rule $\lambda' = (\partial V^\ast/\partial S)(\partial S/\partial U_o^{\max})$ as if both factors were KKT multipliers. The chain rule is formally undefined — the two factors live in different programs and don't compose. Pass-5 reconciliation spike (`01-tragedy/AUDIT-PASS5-KKT-RECONCILIATION.md`) caught this and recommended reverting to Pass-4's finite-multiplier framing.

3. *(Future audits should not repeat this — the "$\lambda$ blows up at the cliff" intuition will keep coming back because cliff-shaped value functions are common in survival/safety problems. Always verify by writing down the program explicitly.)*

**Operational checklist for the pattern:**

1. **What program is this expression a multiplier of?** If you can't write the explicit Lagrangian whose dual variable equals the expression, it isn't a Lagrange multiplier — it's a barrier or a sensitivity (`∂x/∂y` for some other map).
2. **Is the value function bounded?** Discounted infinite-horizon problems have $V^* \leq Q^{\max}/(1-\gamma)$ — bounded. Finite-horizon problems have $V^* \leq T \cdot Q^{\max}$ — bounded. The classic divergence regime (undiscounted infinite-horizon at a feasibility boundary) is generic, not survival-specific.
3. **Where is the divergence?** A barrier diverges at a *level set* of the constraint function. A multiplier diverges at the *infeasibility boundary* of the constraint parameter. These can coincide but usually don't.
4. **Does the chain rule actually compose?** $\lambda' = (\partial V^*/\partial S)(\partial S/\partial b)$ requires both factors to be derivatives of the *same* program. If $V^*$ depends on $S$ only through a binary survival indicator, $\partial V^*/\partial S$ isn't a usable smooth derivative.

**How to apply when auditing or integrating an audit's recommendation:**

- If a soften recommendation is "the $1/(\text{slack})$ form is wrong; it's a barrier not a multiplier" — that's likely correct (1).
- If a strengthen recommendation is "the multiplier is actually divergent because of a cliff" — *verify the program* before integrating. Write down the explicit Lagrangian. Check the chain rule actually composes. The intuition is seductive and frequently wrong (2).
- If both audits disagree on whether a quantity is bounded or divergent, **launch a reconciliation spike** with explicit program-writing instructions. The two audits are often working with different implicit programs.

**Related to the quantifier-disambiguation pattern** (see `~/.claude/projects/-Users-josephwecker-v2-src/memory/feedback_quantifier_disambiguation.md`): both are about a load-bearing expression compressing several distinct claims with different truth values. Quantifier-disambiguation: "iff" / "forced" / "exact" might be hiding 4-5 different readings. Barrier-vs-multiplier: "$\lambda \to \infty$" might be hiding "barrier blows up at level set" vs. "multiplier blows up at infeasibility" vs. "value function diverges at boundary" vs. "DARE sensitivity at survival capacity"…
