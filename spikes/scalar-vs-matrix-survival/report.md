> **Provenance of this file.** Written by the spike agent and returned as text; persisted verbatim by the parent. The agent was interrupted by a server-side API error at the moment it began writing this report, then resumed and asked to synthesize from surviving artifacts **without re-running anything** — so this is a synthesis of work established before the cut, not a fresh pass. It carries two honesty flags of its own: it never read the Marelli material, and its recon peer's provenance marks are preserved verbatim rather than translated into marks it could not audit. §10 is explicitly recorded as *unfinished at interruption*.
>
> **Parent verification:** the parent has verified nothing in this file first-hand except that the cited repo files and numerics exist on disk. The Marelli / Theorem 14 material in §10 is second-hand *to the spike as well* — it arrived from a recon sub-agent after the spike's last read of `prior-art.md` — and the parent has not opened arXiv:1806.08098 either. Treat §10 as conditional throughout. Prior-art marks (`[VERIFIED — full text]`, `[VERIFIED-abstract]`, `[lead]`, `[RECALLED, UNVERIFIED]`) are the recon peer's.

---

# Spike: scalar-vs-matrix in the survival LMI

*Opened 2026-07-29. Umbrella-level rather than in the paper repo: the result bears on how the LMI is framed in any paper that uses it.*

**Status: substantially settled, with two named gaps (§11.1, §11.2) and one section unfinished at interruption (§10).**

**Epistemic key.** **[PROVED]** = argument written out here, elementary, checkable. **[TESTED]** = verified numerically on the exact deterministic recursion. **[HYPOTHESIS]** / **[GUESS]** as usual.

---

## 0. The answer, plainly

**The honest answer is a characterization, and it is unfavorable to the paper's framing in one place and strictly favorable in another.**

The parent's suspicion was right in its conclusion — the matrix form is **not** behaviorally necessary — but right for a cleaner reason than proposed, and the specific adversary named (`λ_max(P_{t+1}(a))`) turns out to **fail**, not succeed.

1. **A single scalar functional can encode a PSD-cone constraint exactly.** `g(X) = λ_min(I_min^{-1/2} X I_min^{-1/2})` has superlevel set `{g ≥ 1} = {X ⪰ I_min}`, exactly. The parent's dimension-counting sketch is **false as stated** — the recon sweep found the same refutation three times independently, and found `g` is a *bona fide* member of the design literature's canonical class (Pukelsheim's information functions). The real obstruction is **linearity**, not scalarity: a weighted trace has a *halfspace* level set, and a halfspace is not a shifted PSD cone once `k ≥ 2`. **[PROVED]**; class membership **[VERIFIED — Pukelsheim, Cornell BU-943-M, 1987, open access]**.

2. **The paper's own matrix bonus is a linear scalar functional.** `Tr(Λ·I_o(a))` with `Λ = c(P_t)·I_min` is, for argmax purposes, `Tr(I_min·I_o(a))` — a positive scalar cannot reorder a ranking. In the survival-dominated regime (the high-drift rows of `tab-main-results`, `drift_probe` 100% at zero exploit reward) the paper's "matrix" controller is a **state-independent scalar rule**, in the same class as the `Tr(I_o)` baseline it is compared against. **[PROVED] + [TESTED]**

3. **State-independent scalars ≡ constant-action policies** (modulo a tie-breaking hypothesis that matters — §3.1), hence survive exactly when the *per-action* LMI is feasible: precisely the strong end of the paper's own strength gradient, `^thm-per-action-lmi`. At `k = 1` no restriction; at `k ≥ 2` one 2-dimensional configuration defeats every such scalar at once. **[PROVED] + [TESTED]**

4. **State-dependent scalars are never insufficient.** The Riccati recursion doesn't depend on realized observations, so survival is a deterministic viability problem; the viability kernel admits a feedback selection; greedy on a suitable state-dependent scalar realizes any deterministic feedback law. **The matrix form is a certificate, not a behavioral requirement.** **[PROVED]** — and per the recon peer this is a two-line composition of **Athans 1972** and **Bertsekas 1972**, so *claim no novelty for it*.

5. **The real boundary is lookahead depth, and it is sharp.** All four natural myopic scalars have verified counterexamples, including configurations where **all four die simultaneously**. In a designed family with `m` drifting axes, depth-`d` worst-case lookahead survives **iff `d ≥ m`**. **[TESTED]**

6. **A strict strengthening for the paper.** The `Λ ∝ I_min^p` critical exponent diverging as drift → isotropic is an **artifact of using a linear functional to emulate a min**, not a fact about survival. The gate `g` discriminates correctly at *perfect* isotropy with no exponent. The paper's sentence *"the matrix-LMI value proposition rests on anisotropic drift"* is, on this evidence, **false as a claim about survival control**. **[PROVED]** mechanism, **[TESTED]** across anisotropies.

7. **The parent's framing hypothesis was slightly the wrong one.** "In every configuration where the LMI is satisfiable" is a bar no controller can clear: in ≈1.8% of sampled LMI-satisfiable configurations **no schedule whatsoever survives**. This *refines* the paper's existing pathwise-gap remark — the gap survives optimal deterministic scheduling, so it's a **convexity gap in the Riccati map**, not an iid-bursting artifact. **[TESTED, rigorous in the negative direction]**

**Net for the paper:** one claim narrows (the experiment is about *direction-aware vs direction-blind weighting*, not scalar-vs-matrix), one strengthens materially (isotropy limitation removable), one remark sharpens, and — if the Marelli finding holds, which the spike cannot vouch for — the contribution is better positioned as *threshold refinement + closed-loop* than as anything near necessity.

---

## 1. Setting

`n` state dim, finite action set `𝒜`, `Q_ρ ⪰ 0` with `k = rank(Q_ρ)`, `Π_ρ` its range projector, `I_o(a) = Hᵀ R_o(a)^{-1} H`, capacity `R²`.

```
P_{t+1} = F(P_t, a_t) := A ( P_t^{-1} + I_o(a_t) )^{-1} Aᵀ + Q_ρ
𝒮 := { P : λ_max(P) < R² }
```

**The fact that drives the whole report:** `F` does not depend on realized observations. The Kalman covariance recursion is an autonomous deterministic system controlled by the action sequence. The paper knows this locally (`^thm-per-action-lmi`'s proof is a deterministic induction) but doesn't draw the consequence.

**Three surrogate classes.**

| class | form | rule |
|---|---|---|
| **S₀** state-independent | `φ(I_o(a))` | `a_t ∈ argmax_a φ(I_o(a))` |
| **S₁** myopic state-dependent | `ψ(F(P_t,a))` | `a_t ∈ argmax_a ψ(F(P_t,a))` |
| **S₂** state-dependent | `φ(I_o(a), P_t)` | `a_t ∈ argmax_a φ(I_o(a),P_t)` |

The paper's scalar baseline is in `S₀`; so — the surprise — is the paper's matrix bonus (§4). The parent's proposed adversary is in `S₁`.

Diagonal specialization for all numerics, matching the paper's standing (S3): `A = I`, `Q_ρ = diag(q)`, `I_o(a) = diag(v_a)`; survival `max_i P_i < R²`. Per-axis averaged-DARE floor, exact in this convention: `ι_min,i = q_i / (R²(R² + q_i))`.

> **Minor consistency flag [PROVED], low stakes.** `A-scalar-pedagogical.md` gives `ι_min = q/(R²(R²−q))` — the **predicted**-covariance convention, requiring `q < R²`. The §5 controller gates on `R² − λ_max(P_t)` with `P_t` a posterior, i.e. the **filtered** convention, whose floor is `q/(R²(R²+q))`, finite for all `q`. The two are used within a few pages of each other without being distinguished, and the printed formula's `q → R²` blow-up is a convention artifact, not a fact about survival. One sentence in App A fixes it. Changes no conclusion.

---

## 2. Prior art, and what it does to these results

The recon peer's four-neighborhood sweep is on disk (`prior-art.md` plus four siblings, ~144KB). The five things that changed the write-up:

1. **Proposition 4 below is known.** `g` is an *information function* in Pukelsheim's sense; his one-to-one correspondence between information functions on the NND cone and closed convex subsets excluding zero covers `{M : M ⪰ I_min}` exactly. **[VERIFIED — full text read]**. Corollary from the peer: *"a design-theory reviewer would construct φ in about ten seconds"* — so the unrestricted no-scalar claim must not appear in the paper.
2. **Propositions 6–8 are a composition of two 1972 results.** **Athans (1972), Automatica 8(4) 397–412** states verbatim that optimal measurement-strategy selection *"can be transformed into a deterministic optimal control problem"* with the policy *"precomputed, i.e. specified before the measurements actually occur"* **[VERIFIED]**. **Bertsekas (1972), IEEE TAC 17(5) 604–613** gives infinite-time confinement to a region by feedback **[VERIFIED]**. Peer's explicit instruction: **do not cite Aubin** — in discrete time with finite `𝒜` the selection is bare choice.
3. **The closest well-posed version of the question is an acknowledged open problem.** Restless-bandit **Whittle indexability**: an index *is* a state-dependent scalar whose greedy argmax is the policy. Scalar Kalman: an index provably works (**Dance & Silander, JMLR 2019, 20 art. 35** — cite that, not the NeurIPS 2015 version whose Theorem 1 is conditional on an unproved assumption **[both VERIFIED]**). Multidimensional Kalman — the paper's setting — is **explicitly open**, stated three times verbatim in **Hao, Wang, Niño-Mora, Fu, Yang & Pan, arXiv:2312.07858 / Sensors 24(23):7755 [VERIFIED — full PDF]**: *"indexability is currently an open problem"* … *"at present it is unknown whether restless projects with multi-dimensional Kalman filter dynamics such as those above are indexable, even for a single dynamics model."*
4. **λ_max was *expected* to be hard to defeat.** Chamon, Pappas & Ribeiro (arXiv:1912.03799) prove worst-case error is approximately supermodular with greedy certificates approaching `(1−1/e)` **[VERIFIED-abstract]**. That makes §5.1's counterexample more interesting, not less. Complementary: **Zhang, Ayoub & Sundaram (CDC 2015) Example 1** breaks sub- and super-modularity of trace, log-det **and** λ_max simultaneously for the steady-state DARE covariance **[VERIFIED — full text]**.
5. **The peer flagged a hole in Proposition 3, and it was real.** Three results say the relevant behavior class is *periodic*, not constant (Mo/Garone/Sinopoli SCL 67:65–70 2014; Zhao et al. IEEE TAC 2014, both **[VERIFIED-abstract]**). That prompted a tie-breaking check, and tie-breaking turned out to be load-bearing — §3.1. The single most useful thing the sweep did for the mathematics, from a neighborhood neither agent had flagged as mathematical.

**Explicit negatives recorded deliberately:** no theorem "no scalar characterizes Loewner-feasibility of a mixture" (it's false, not missing); no published counterexample to myopic λ_max or log-det scheduling in the per-step setting (so these numerics aren't redundant); **nobody treats `λ_max(Σ) < R²` as a constraint rather than an objective** — the feasibility framing is genuinely under-occupied, a real novelty argument; no anisotropic-floor persistent-excitation result; no result composing Athans with viability.

One rider from the peer that cuts against the spike's own framing, accepted: viability theory obtains viable feedback *myopically* — myopic in a function derived from the viability kernel. So "myopic vs non-myopic" collapses one level into **"which scalar"**, and the honest content of §5 is not "myopia fails" but *"these four specific scalars are not the viability value function."*

---

## 3. What is proved: the `S₀` class

### 3.1 Greedy on a state-independent scalar is a constant-action policy — [PROVED], with a hypothesis that matters

**Proposition 1.** For `φ ∈ S₀`, the argmax set is independent of `t` and `P_t`; hence under any **state-independent** deterministic tie-break the rule plays one constant action forever. *Proof.* The argmax of a fixed finite list of reals is a fixed set. ∎

**The hypothesis, stated because it is load-bearing.** If tie-breaking may depend on `P_t`, the controller is really in `S₂`. **[TESTED]**: on the symmetric instance, `Tr(I_o)` scores `(1.0, 1.0, 0.04)` — `a₀` and `a₁` **tie** — and a round-robin tie-break *survives* 20 000 steps while fixed-priority dies at `t=7`. Honest statement: *an `S₀` controller is a pair `(φ, τ)` with `τ` state-independent; then it is a constant action.*

**Corollary 1 (the exact strength of `S₀`).** An `S₀` controller guarantees survival iff the constant-action trajectory survives — under (S1)–(S5), exactly the *per-action* drift-block LMI. `^thm-per-action-lmi` gives sufficiency; necessity is immediate. **So `S₀` is exactly as strong as the strong end of the paper's own LMI-strength gradient.** The paper has the theorem; what it doesn't say is that this is a *ceiling* for its controller class.

### 3.2 `k = 1`: a state-independent scalar always suffices — [PROVED]

**Proposition 2.** Under (S1)–(S5) with `k = 1`: if the averaged LMI is satisfiable by some `π`, then `φ(X) = Tr(Π_ρ X Π_ρ)` yields a surviving policy. *Proof.* Satisfiability gives `Σ_a π(a)[I_o(a)]₁₁ ≥ ι_min`; a convex combination never exceeds the max, so `max_a [I_o(a)]₁₁ ≥ ι_min`. Greedy-`φ` selects a maximizer, giving hypothesis (i) of `^thm-per-action-lmi-iid`; (S2)+(S4)+(S5) handle the orthogonal block. ∎

**This is the sharp version of the reviewer's point.** The submitted experiment has `k = 1`, so it *cannot* separate the classes. What it does show is real: `Tr(I_o)` (unprojected) fails while `Tr(I_min·I_o)` (drift-weighted) succeeds — but that is **projected-vs-unprojected weighting**, not scalar-vs-matrix. This lines up with Dance & Silander: scalar-state Kalman provably indexable, multidimensional open.

### 3.3 `k ≥ 2`: one configuration defeats every `S₀` controller — [PROVED] + [TESTED]

`n = k = 2`, `A = I`, `q = (0.5, 0.5)`, `R² = 4`, `P₀ = (0.5, 0.5)`, `ι_min = 0.0278`:

```
v(a₀) = (1.0, 0.0)     v(a₁) = (0.0, 0.9)     v(a₂) = (0.02, 0.02)
```

- averaged LMI satisfiable (50/50 of `a₀,a₁` gives `(0.5, 0.45) ⪰ (0.0278, 0.0278)`); no single action feasible;
- alternating `(a₀,a₁)` survives **[TESTED, 10⁵ steps]**;
- constant `a₀` dies, constant `a₁` dies **[TESTED]** — so *every* `S₀` controller dies.

The **asymmetric** variant (`0.9` on `a₁`) was chosen precisely because of §3.1. Note the quantifier order: **one configuration, all `φ`**.

Full class table from `exp1_state_independent.py` (symmetric variant, fixed-priority tie-break):

| rule | class | survives | note |
|---|---|---|---|
| alternating `(a₀,a₁)` | — | **yes** (10⁵ steps) | witness |
| `Tr(I_o)` | S₀ | no, `t=7` | locks to `a₀` |
| `Tr(Π_ρ I_o Π_ρ)` | S₀ | no, `t=7` | locks to `a₀` |
| `λ_min` on drift block | S₀ | no, `t=12` | locks to decoy `a₂` |
| normalized `λ_min` (`g`) | S₀ | no, `t=12` | class-optimal, class insufficient |
| `Tr(I_min^p I_o)`, `p=1,2,4,8` | S₀ | no, `t=7` | **the paper's own rule** — §4 |
| `−log det P⁺` | S₁ | yes | `a₀,a₁,a₀,a₁,…` |
| `−Tr(P⁺)` | S₁ | yes | idem |
| one-step info gain | S₁ | yes | idem |
| `−λ_max(P⁺)` | S₁ | **no**, `t=12` | decoy capture — §5.1 |

### 3.4 The obstruction is linearity, not scalarity — [PROVED]

**Proposition 4.** On `range(I_min)`, `g(X) := λ_min(I_min^{-1/2} X I_min^{-1/2})` satisfies `{X ⪰ 0 : g(X) ≥ 1} = {X : X ⪰ I_min}` **exactly**. One real functional encodes PSD-order feasibility with no loss; greedy-`g` selects a per-action-feasible action whenever one exists — `g` is **optimal within `S₀`**. *Proof.* `X ⪰ I_min ⟺ I_min^{-1/2} X I_min^{-1/2} ⪰ I ⟺ λ_min(·) ≥ 1`; congruence by an invertible matrix preserves the PSD order. ∎ *(Known — Pukelsheim.)*

**Proposition 5 (why weighted traces cannot).** `φ_Λ(X) = Tr(ΛX)` is linear, so every superlevel set is a **halfspace**. `{X ⪰ I_min}` is a shifted PSD cone, a halfspace iff `k ≤ 1`. Hence for `k ≥ 2` no weighted trace — for any `Λ`, including `Λ ∝ I_min^p` at any `p` — has the feasible set as a superlevel set. ∎

**So the parent's instinct pointed at the true structure and misattributed it.** The right axis is **linear vs nonlinear**, and the true statement is *sharper* than the dimension count: not "scalars have one degree of freedom and lose," but "**linear** functionals have halfspace level sets and lose; a suitably nonlinear scalar loses nothing at all." `det` is nonlinear too but its level sets aren't the cone.

Peer's refinement, the citable form: what *is* true is (i) no **per-action separable** scalarization works (Jensen: `E[f(I_o)] ≤ f(E[I_o])` for concave isotonic `f`, so a per-action budget is sufficient-but-never-necessary, and the gap *is* the directional-mixing effect the paper is about — peer's read is that **this is almost certainly what the paper's own argument actually establishes**); (ii) no member of the classical A/D/E/Φ_p family works, each being Loewner-isotonic but not order-*reflecting*, the lone exception being the λ_min end under an **isotropic** floor; (iii) no *fixed, floor-independent* scalar works — any exact scalar characterization must be built **from** `I_min`. (iii) is the rhetorically strongest version.

### 3.5 State-dependent scalars are never insufficient — [PROVED]

**Proposition 6.** If the `I_o(a)` are pairwise distinct, then for any `μ`, the surrogate `φ(X,P) := −‖X − I_o(μ(P))‖_F²` has unique argmax `μ(P)` everywhere. ∎

**Proposition 7.** With `K₀ := 𝒮`, `K_{j+1} := K_j ∩ {P : ∃a, F(P,a) ∈ K_j}`, `K := ⋂_j K_j`: a schedule survives from `P₀` iff `P₀ ∈ K`; and for every `P ∈ K` there is `a` with `F(P,a) ∈ K`. *Proof of the second part.* For each `j` some `a_j` has `F(P,a_j) ∈ K_j`; `𝒜` finite so some `a` recurs infinitely often; `K_j` decreasing gives `F(P,a) ∈ K_j` for all `j`. ∎ (Finiteness of `𝒜` replaces any compactness hypothesis — also why Aubin is the wrong cite.)

**Theorem 8.** If any schedule survives from `P₀`, some `φ ∈ S₂` does. ∎

**Reading.** A scalar surrogate is behaviorally sufficient in full generality; the matrix form's value is that it's a **checkable closed-form certificate** where the viability kernel is neither. But the sufficient `φ` is the viability-kernel indicator — non-myopic, not closed-form. Per Athans, the covariance trajectory is **precomputable**, worth passing to the paper for a separate reason: nothing in the covariance dynamics is stochastic, so rhetoric about the agent needing to *probe* or *learn* is doing less work than it appears to.

---

## 4. The paper's matrix bonus is itself a linear scalar surrogate — [PROVED] + [TESTED]

Rule: `a_t ∈ argmax_a [Q_O(a) + Tr(Λ·I_o(a))]` with `Λ = k·I_min/(R² − λ_max(P_t))`.

**Proposition 9.** Write `Λ = c(P_t)·Λ₀`, `c > 0` scalar, `Λ₀ = I_min` fixed. Then `argmax_a Tr(Λ·I_o(a)) = argmax_a Tr(Λ₀·I_o(a))` for every `P_t` — the state-dependence is a positive rescaling and cannot reorder. So in the survival-dominated regime the rule is a **state-independent linear scalar surrogate**, `∈ S₀`, and Propositions 1/3/5 apply verbatim. ∎

**[TESTED]** (`exp5`, part A): on the §3.3 configuration, `Tr(I_min^p I_o)` greedy dies at `t=7` for `p = 1,2,4,8`.

Three consequences, descending in comfort:

1. `Λ`'s state-dependence **is** load-bearing for the survival/reward trade-off — `c(P_t)` decides *when* the bonus outvotes `Q_O`, the whole `def-survival-margin` divergence story, untouched. It is **not** load-bearing for *which* informative action wins. The paper doesn't currently separate those two claims, and should.
2. `tab-main-results` compares two members of `S₀`. The phenomenon is genuine and `prop-blank-wall` is a correct theorem about it. But *"the matrix Lagrangian discriminates by direction, not magnitude"* does rhetorical work that "matrix" doesn't earn: the discriminating object is the **weight** `I_min`, and the bonus it produces is a number.
3. The reviewer's objection, restated, is **stronger** than the reviewer put it: not only would a posterior-dependent scalar plausibly dodge the blank wall, the paper's own controller is a scalar rule in the *weakest* of the three classes.

---

## 5. The real boundary: lookahead depth — [TESTED]

**Verification standard** (`exp3_verified.py`): a counterexample is reported only when (a) the surviving witness is an **exactly periodic** schedule simulated 10⁵ steps with `max_i P_i < R²` throughout — exact float arithmetic on the deterministic recursion, no Monte Carlo — and (b) greedy runs from the same `P₀` and exits. Searched instances additionally required **late** death (`t ≥ 8`).

### 5.1 Decoy capture defeats `λ_max(P⁺)`-greedy — the adversary the parent named

`n = k = 2`, `q = (0.5,0.5)`, `R² = 4`, `P₀ = (0.5,0.5)`, `v(a₀)=(1,0)`, `v(a₁)=(0,1)`, `v(a₂)=(0.02,0.02)`:

- `(a₀,a₁)` alternating survives 10⁵ steps (final `P = (1.118, 0.618)`);
- greedy `−λ_max(P⁺)` selects `a₂` at **every** step and exits at `t = 12`.

*Mechanism.* With `P` symmetric across axes, playing `a₀` leaves axis 1 at `P+q`, so the post-action maximum is `P+q`. The decoy shaves *both* axes slightly, so its post-action maximum is strictly lower. The myopic rule strictly prefers the decoy forever, while the decoy's rate `0.02` is below the floor `0.0278` on both axes. `λ_max` sees only the maximum and will pay any long-run price to reduce it by any amount now.

- **The decoy is not a blank wall.** `range(I_o(a₂))` is *not* orthogonal to `range(I_min)` — it informs both drifting axes. `prop-blank-wall` doesn't cover it and a `Λ ∝ I_min` bonus wouldn't zero it. This is a **second, distinct capture mode**: not "information in the wrong direction" but **"right direction, inadequate rate, myopically preferred."** More insidious than the blank wall, because no range or projection condition excludes it. Believed new relative to the paper's framing, and given Chamon et al.'s approximate-supermodularity result, a more interesting object than expected.
- It does *not* refute Theorem 8 — the viability-kernel surrogate still works here.

**So the nominated adversary fails.** That is the one place prediction and result diverge, and it flips the sign of that part of the story.

### 5.2 All four have late-death counterexamples

| surrogate | verified counterexample | dies | witness cycle |
|---|---|---|---|
| `−λ_max(P⁺)` | `q=(0.5,0.5)`, `R²=4`, decoy set | `t=12` | `(a₀,a₁)` |
| `−λ_max(P⁺)` | `q=(0.740,0.353,0)`, `R²=2.593` | `t=15` | `(a₀,a₁)` |
| `−log det P⁺` | `q=(0.585,1.927,0)`, `R²=6.611` | `t=11` | `(a₀)` constant |
| `−Tr(P⁺)` | `q=(1.895,0.085,0)`, `R²=1.996` | `t=31` | `(a₀,a₁)` |
| one-step info gain | identical to `−log det P⁺` throughout | — | — |

**Proposition 10 [PROVED].** Greedy one-step information gain and greedy `−log det P⁺` are the *same rule*: `½ log det(I + I_o(a)(P+Q)) = ½[log det(P+Q) − log det P⁺]`, first term action-independent. So D-optimal one-step design, maximum expected KL/entropy reduction, and minimum `log det` posterior are **one** surrogate, not three. Worth knowing before anyone runs "three posterior-dependent baselines."

### 5.3 Failure rates, with the soundness caveat stated

Random ensemble (`n=3`, `k=2`, 4 actions, log-uniform; `exp2`, 40 000 draws, 38 838 judged viable):

| surrogate | fails on … of viable configurations |
|---|---|
| `−λ_max(P⁺)` | 3.40 % |
| `−Tr(P⁺)` | 4.58 % |
| `−log det P⁺` ≡ info gain | 15.53 % |

**Caveat, precisely.** That sweep's viability test is a depth-bounded DFS with log-grid dedup treating a revisited rounded state as sustainable, yielding **false positives** for viability — so denominators are approximate and these percentages are indicative only. The *negative* direction is sound, which is what §7 relies on, and every individual counterexample in §5.1–5.2 was re-verified exactly.

### 5.4 All four fail simultaneously; and the depth boundary is sharp

`exp6`: **6 viable configurations where all four surrogates die**, e.g. `q=(1.965,0.145,0)`, `R²=2.428`, three actions, surviving cycle `(a₀,a₂)` verified 3000 steps. So no natural member of `S₁` suffices.

Depth-2 worst-case-`λ_max` lookahead repaired **every** one; over 1200 viable configurations the failure rate was `depth 1: 0.08%`, `depth 2–4: 0.00%`. (The depth-1 figure isn't comparable to §5.3's 3.40% — different ensemble, 3 actions not 4, different viability filter. Noticed and not reconciled.)

`exp7` asked whether depth 2 is *generally* enough. It is not. With `m` drifting axes, `q = 0.5·1`, `R² = 4`, one dedicated action per axis (`8·eᵢ`) plus a decoy at `0.9×` the per-axis floor on all axes:

| `m` | round-robin | `d=1` | `d=2` | `d=3` | `d=4` | `d=5` | `d=6` |
|---|---|---|---|---|---|---|---|
| 2 | survives | DIE | ok | ok | ok | ok | ok |
| 3 | survives | DIE | DIE | ok | ok | ok | ok |
| 4 | survives | DIE | DIE | DIE | ok | ok | ok |
| 5 | survives | DIE | DIE | DIE | DIE | ok | ok |
| 6 | survives | DIE | DIE | DIE | DIE | DIE | DIE |

**Depth-`d` lookahead survives iff `d ≥ m`** — so for every fixed finite depth, `m = d+1` gives a viable configuration defeating it. *Mechanism:* a window shorter than `m` cannot contain a full round-robin, so within it "shave everything a little" beats "fix one axis and let `m−1` grow"; only a window of length `≥ m` reveals the decoy is sub-floor and fatal. The `m=6, d=6` cell breaks the pattern; believed a tie-breaking artifact of the implementation (equal worst-case values resolved by first-sequence order) but **not verified**, and the claim only needs `m = d+1`, verified for `d = 1..5`.

Also from `exp7`: a random 5-axis instance where depths 1–4 *all* die at `t=22` while cycle `(a₁,a₂,a₂)` survives.

**Rung.** `[TESTED]` with a transparent mechanism and a clean law; **proof outstanding**. Sharp conjecture worth proving: *depth-`d` worst-case-`λ_max` lookahead fails on the round-robin family whenever `m > d`.* Completes the hierarchy `S₀ ⊊ (finite-lookahead) ⊊ S₂`.

---

## 6. A strict strengthening: the isotropy limitation is an artifact — [PROVED] + [TESTED]

`A-safety-anisotropic.md` ends on the paper's most consequential self-imposed limit:

> As `σ_x/σ_y → 1` (isotropic drift), `p_crit → ∞`: no concentration of `Λ` along `I_min`'s eigenstructure can recover directional discrimination, and the matrix-LMI value proposition rests on anisotropic drift.

The first clause is **true** and now explained: `Tr(I_min^p ·)` is *linear* in `I_o`, and the family is trying to emulate a **min** over normalized directions, with contrast supplied entirely by `I_min`'s own anisotropy. Isotropic `I_min` leaves no contrast to sharpen. That is Proposition 5 in operational form.

The second clause — *"the matrix-LMI value proposition rests on anisotropic drift"* — **does not follow, and appears to be false.** `exp5` part B, `n=k=2`, probe meeting the floor with margin 3 on both axes, near-wall action at 40× the floor on the cheap axis and 0.2× on the expensive one:

| `σ_x/σ_y` | `I_min` ratio | least `p` at which weighted trace prefers the probe | gate `g` prefers |
|---|---|---|---|
| 8.00 | 55.00 | 1 | probe |
| 4.00 | 13.86 | 1 | probe |
| 2.00 | 3.57 | 2 | probe |
| 1.50 | 2.07 | 3 | probe |
| 1.20 | 1.38 | 8 | probe |
| 1.05 | 1.09 | 30 | probe |
| **1.00** | **1.00** | **≥400 (never)** | **probe** |

The `p_crit` column reproduces the paper's divergence. The last column shows it isn't a fact about survival: a still-scalar, still-state-independent, still-drift-aware surrogate discriminates correctly at *perfect* isotropy.

**Recommendation.** State `g`, prove Proposition 4 (two lines, cite Pukelsheim), replace the sentence with: *the `Λ`-weighted-trace family's directional discrimination degrades to nothing as drift becomes isotropic, because a linear functional of `I_o` cannot express the direction-wise comparison; the min-type gate `{I_o(a) ⪰ γ I_min}` expresses it exactly and is isotropy-independent.* Strictly stronger, removes the paper's dominant caveat on this axis, costs a paragraph, and the App C `p_crit` table becomes evidence *for* the sharper claim.

**Caveat, honestly.** `g` is a *feasibility* test, not a smooth bonus — used additively against `Q_O` it saturates rather than rewarding surplus information. The clean formulation is almost certainly the **operational safety set** `𝒜_F^op(γ) = {a : I_o(a) ⪰ γ I_min}` the paper *already defines in the same appendix*: `g(I_o(a)) ≥ γ` is exactly membership in it. So the change is small and internally sourced. The KKT story for a gate-constrained rather than trace-penalized program has **not** been worked out; flagged open in §11.2.

---

## 7. The framing hypothesis: LMI-satisfiable ⊋ survivable — [TESTED, rigorous in the negative direction]

`exp4`: sample diagonal configurations; test averaged-LMI satisfiability **exactly** as an LP; then test viability by exhaustive DFS. Of **22 946** LMI-satisfiable configurations, **418 (1.82%) admit no surviving schedule at all** — no periodic schedule up to period 5 over 2·10⁵ steps, and exhaustive search rules out every sequence to depth 300. The DFS's negative answer is rigorous (tree exhausted; dedup only causes false positives), so these are genuine.

*Mechanism.* Witnessing mixtures are interior (e.g. `π = (0.733, 0, 0.267, 0)`). By nonlinearity of `P ↦ (P^{-1}+s)^{-1}` composed with the predict step, the time-average of the realized covariance under any schedule realizing that rate is not the covariance of the averaged Riccati. **Interleaving in time is strictly worse than averaging in the constraint.**

**This refines rather than contradicts the paper.** `04-main-results.md` already flags the expectation-vs-pathwise gap and attributes it to iid bursts of length `Θ(log T)`. The finding here is stronger and cleaner: the gap survives **optimal deterministic scheduling** — a convexity gap in the Riccati map, not a sampling artifact. So `thm-lmi-sufficient` is sufficient for the *averaged DARE's* steady state and is **not** a certificate of pathwise survival under any schedule; the per-action theorems aren't a convenience strengthening, they carry the pathwise claim entirely. Sharpen "iid bursts can drive `λ_max(P_t) > R²`" to "no schedule need exist at all," with this as the witness class.

**Restated question that has an answer.** *For which configurations, and which surrogate classes, does greedy scalar control achieve the viability kernel?* `S₀` achieves it iff the per-action LMI is feasible (§3.1); `S₂` achieves it always (§3.5); finite-lookahead classes sit strictly between, with a sharp depth law (§5.4).

---

## 8. Routes tried that did not work

1. **Dimension counting (`k(k+1)/2` vs 1) — abandoned, and refutable.** Proposition 4 exhibits a scalar whose superlevel set *is* the cone. The count conflates "a scalar cannot *parameterize* the cone's boundary" (true, irrelevant) with "a scalar cannot *decide* membership" (false — an indicator is a scalar). Don't resurrect it. The peer's independent finding that this refutation is constructible in ten seconds by a design-theory reviewer makes this the most important negative in the report.
2. **Defeating `λ_min`/`det` via anisotropic `I_min`.** `λ_min` of the *raw* drift block is defeatable, but the fix is trivial (normalize by `I_min^{-1/2}`), so the defeat kills a badly-chosen scalar rather than the class. What kills `S₀` is Proposition 1 + convexity of mixture feasibility, needing no construction at all.
3. **Treating "LMI satisfiable" as the hypothesis.** Cost about twenty minutes trying to prove a false statement before §7's numerics showed it unsatisfiable-by-anything on a nonzero-measure set. Check the hypothesis is achievable before trying to achieve it.
4. **Bergstrom-style projected-covariance bounds** — not attempted, deliberately. `LOG.md`'s M7 entry records `Π_ρ P Π_ρ ⪯ (Π_ρ J Π_ρ)^{-1}` is **false** (Schur complement gives the opposite direction). Everything here either assumes block-diagonality (S3) or works per-axis. For a non-block-diagonal result, that inequality is still the trap.
5. **Shipping Proposition 3 without the tie-breaking hypothesis** — caught only because the peer's periodicity results prompted the check. Any `S₀` no-go must say "state-independent tie-break" out loud.

---

## 9. Recommendations for the paper (not edits — nothing in the repo was touched)

**Narrowing that honesty requires.**
- `04-main-results.md` / `04-blank-wall-resolution.md`: "The matrix Lagrangian discriminates by direction, not magnitude" → a claim about the **weighting**. `Tr(Λ I_o(a))` is a scalar (Prop 9).
- `05-*` / `tab-main-results` scope sentence: state that the experiment has `k = 1`, that a state-independent scalar provably suffices at `k = 1` (Prop 2), and that the demonstrated contrast is *direction-aware vs direction-blind weighting*. The paper already models this honesty well elsewhere; same move, different axis.
- `prop-blank-wall`: note it covers the *orthogonal* capture mode only, and that §5.1's decoy — right direction, inadequate rate — is excluded by no range condition.
- Do **not** state any unrestricted no-scalar claim. State the restricted ones (§3.4 (i)–(iii)).

**Strengthening available now.**
- State `g` and Prop 4, cite Pukelsheim, replace the isotropy sentence (§6).
- State Corollary 1 (`S₀` ≡ per-action LMI feasibility) as a proposition — a *converse* to `thm-per-action-lmi` for the controller class the paper actually uses, three lines.
- Optionally Theorem 8 as a Discussion remark, citing Athans 1972 + Bertsekas 1972 and claiming no novelty. Conceding it *strengthens* the position, because the same argument shows the certificate is the only closed-form object available.

**The discriminating experiment, if one is wanted.** `n ≥ 3`, `k = 2`, §3.3 structure: two probes each covering one drifting axis, neither feasible alone, feasible in mixture, plus a sub-floor decoy on both axes. Then every `S₀` rule (including the paper's `Λ`-bonus) dies; `λ_max(P⁺)`-greedy dies on the decoy; `log det`/`Tr` of `P⁺` survive. One action set separates all three classes, which the current 2-D setup cannot.

---

## 10. Positioning — *unfinished at interruption*

Recorded as unfinished rather than resolved.

The spike had **not read the Marelli material**. `prior-art.md` as it read it listed **Marelli, Sui, Rohr & Fu, arXiv:1806.08098 / Automatica** — stability of Kalman filtering with a **random measurement equation** (random `H` *and* `R`), structurally the `E_π` setting, with "a necessary and a sufficient condition" — and said explicitly: *"This read is in progress as of writing."* The Appendix A / Theorem 14 finding arrived after that. **So the spike cannot vouch for it at any rung.**

How it would compose, conditionally:

- If the sharp condition for the exogenous case is `K` blockwise scalar inequalities in which `E_π[I_o]` does not appear, then the averaged LMI is sufficient-but-far-from-necessary in a *characterized* way — the same shape as §7 (LMI-satisfiable ⊋ survivable, 1.82%) reached from a completely different direction. Two independent routes to "sufficient, with the gap now named" would be strong.
- It would also line up with **Rohr, Marelli & Fu, IEEE TAC 59(10), 2014**, which give a necessary and a sufficient condition separated by an **acknowledged gap** in the *strictly easier* intermittent-observation setting **[VERIFIED-abstract]**. Peer's conclusion, endorsed: *the necessity of the matrix condition is not a gap in the author's work; it is a gap in the field.*
- So the defensible story is *threshold refinement + closed-loop*, plus sufficiency with a characterized gap, plus the §2.3 open-problem citation. That is *stronger* than any necessity claim, because "this reduces to a recognized open problem in restless-bandit indexability" is citable and checkable, whereas "we could not find a scalar that works" is neither.

What would finish this section: read Marelli directly, check whether their conditions specialize to the paper's `I_min`, and work out whether the closed-loop (action-dependent, `P_t`-dependent) case genuinely escapes their exogenous characterization or merely restates it.

---

## 11. Open

1. **[HYPOTHESIS → well-evidenced, proof outstanding]** Depth-`d` worst-case-`λ_max` lookahead fails on the round-robin family whenever `m > d` (§5.4). Check the `m=6,d=6` anomaly first — suspected tie-breaking.
2. **[open]** KKT / Lagrangian treatment of a **gate**-constrained program (`I_o(a) ⪰ γ I_min` as a hard feasible-set restriction) rather than trace-penalized, and what replaces the shadow-price story. Needed before §6's recommendation is more than a selection rule.
3. **[open]** Everything is in the block-diagonal / simultaneously-diagonalizable regime (S3). Non-commuting `{I_o(a)}` is untouched — and it's where `I_min` stops being a unique tight floor and becomes an SDP feasibility floor. Propositions 1, 4, 5, 6, 7, 8 are basis-free and survive; Prop 2's `k=1` argument and all numerics assume diagonal structure.
4. **[open]** Markov-policy generalization of the averaged LMI. §3.5 suggests the right generalization is not a policy-averaged LMI at all but a viability / controlled-invariance statement.
5. **[open]** §10 above.

---

## 12. Files on disk

- `num/diag_survival.py` — recursion, greedy harness, candidate surrogates.
- `num/exp1_state_independent.py` — §3.3 configuration; all classes tabulated.
- `num/exp2_myopic_search.py` — myopic failure rates (§5.3).
- `num/exp3_verified.py` — exactly-verified late-death counterexamples (§5.1–5.2).
- `num/exp4_lmi_vs_viable.py` — LMI-satisfiable but non-viable (§7).
- `num/exp5_weighted_trace_vs_gate.py` — `Λ`-family collapse; anisotropy vs gate (§4, §6).
- `num/exp6_lookahead.py`, `exp6.out` — all-four-fail instances; lookahead sweep (§5.4).
- `num/exp7_depth2.py`, `exp7.out` — depth-2 defeat; designed round-robin family (§5.4).
- `prior-art.md` + four sibling files — the recon peer's sweep (§2).

---

## Feedback on the brief (spike's own)

- *Surprise:* that the paper's matrix bonus is a scalar. Went in expecting to adjudicate scalar-vs-matrix and found both sides of the experiment are on the same side of the line.
- *Surprise:* the depth law being exactly `d ≥ m`. Expected mush, got a clean boundary.
- *The enumeration mistake recurred.* The brief enumerated the literatures — adaptive control, optimal experiment design, sensor scheduling — and the two most consequential hits were **off the list**: restless-bandit **Whittle indexability** (the question in its cleanest published form, 1-D proved and multi-D a *named open problem* bracketing §3.2/§5 exactly) and **Athans 1972** (which *is* the determinism reduction, so Props 6–8 claim no novelty). The brief did hedge — *"please regard anything off the list as more interesting than anything on it"* — and that hedge was passed to the peer verbatim, which is probably why the off-list hits surfaced at all. The enumeration cost less than it might have, but the pattern held.
- *Where the brief helped most:* explicitly labeling the dimension-counting sketch a guess and saying to discard it. It was discarded, and the replacement (linear vs nonlinear) is the load-bearing idea in the report. Framed as a result to confirm, the evening would likely have gone into a 3×3 counterexample to `λ_min` proving nothing.
- *One thing wanted in the brief:* whether `λ_max(Σ_δ) < R²` refers to the filtered or predicted covariance. Had to pick (filtered, matching the controller's gate) and flag the discrepancy (§1). Changes no conclusion but cost time, and it's a real ambiguity in the paper.
