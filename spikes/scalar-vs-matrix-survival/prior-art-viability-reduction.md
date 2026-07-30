# Prior art — the deterministic-reduction and viability/controlled-invariance route

*Scope: question (2) of the brief — "is the viability kernel ⇒ deterministic feedback selection move a standard cited result?" — plus the upstream reduction that makes it applicable. Sensor scheduling and experiment design are covered in sibling files.*

**Epistemic marking convention:** every item is tagged **[VERIFIED]** (I fetched the publisher/abstract page and the statement below reflects what it actually says) or **[RECALLED, UNVERIFIED]** (from memory, not checked — do not cite without checking).

---

## Headline: yes, (2) has standard citations, and the reduction upstream of it has an even older one

The move sketched in the brief — *the Riccati recursion is deterministic, so survival is a viability problem, and viability kernels admit deterministic feedback selections* — decomposes into two separately-citable steps. Both are standard. Neither needs to be proved in the paper.

### Step 1 — the reduction: measurement/sensor choice under a Kalman filter *is* a deterministic control problem on covariance space

This is the load-bearing step and it is older than I expected.

- **Athans, M. (1972). "On the determination of optimal costly measurement strategies for linear stochastic systems." *Automatica* 8(4), 397–412.** **[VERIFIED — abstract via ScienceDirect / NTRS]**
  Verbatim from the abstract: the problem of selecting the optimal measurement strategy "can be transformed into a deterministic optimal control problem," and the optimal measurement policy plus its matched Kalman filter "can be precomputed, i.e. specified before the measurements actually occur."
  **Why it bears:** this is exactly the author's own observation, published in 1972. The determinism of the Riccati recursion ⇒ open-loop-computable measurement policy is Athans' result, not a new one. Cite this rather than re-deriving. It also sharpens the framing: because the policy is *precomputable*, the "state-dependent scalar" question is not about reacting to realized data at all — the covariance trajectory is known in advance, so "state-dependent" here means "dependent on a deterministically-known clock/trajectory," which is a weaker notion of feedback than it sounds like.

- **Meier, L., Peschon, J., Dressler, R. (1967). "Optimal control of measurement subsystems." *IEEE Trans. Automatic Control* 12(5), 528–536. DOI 10.1109/TAC.1967.1098668.** **[VERIFIED — abstract via IEEE/Semantic Scholar]**
  Introduces "measurement adaptive" problems where the measurement equation contains a control variable; for linear-quadratic-Gaussian shows plant-control optimization separates from measurement-control optimization and the latter can be done *a priori*.
  **Why it bears:** the earliest statement of the separation that licenses studying the covariance recursion in isolation from the state estimate — i.e. the reason the survival question is purely about `I_o(a)` and never about the realized observations. This is the citation for the paper's implicit separation assumption if it currently has none.

### Step 2 — viability kernel / maximal controlled-invariant set admits a stationary feedback

- **Bertsekas, D. P. (1972). "Infinite-time reachability of state-space regions by using feedback control." *IEEE Trans. Automatic Control* 17(5), 604–613. DOI 10.1109/TAC.1972.1100085.** **[VERIFIED — abstract via IEEE Xplore / ASU Pure]**
  Studies when the state of an uncertain time-invariant system can be forced to stay in a specified state-space region for all time by feedback; analyses the limit of the *n*-step reachability regions, shows convergence to a steady state under a compactness assumption, and exhibits ellipsoidal regions where confinement is achievable by a *linear time-invariant* control law given stabilizability.
  **Why it bears:** this is the canonical discrete-time citation for "the infinite-horizon confinement set exists as a fixed point of a one-step recursion, and a stationary feedback confines within it." The compactness caveat is real and worth honoring in the paper's wording.

- **Blanchini, F. (1999). "Set invariance in control" (survey paper). *Automatica* 35(11), 1747–1767. DOI 10.1016/S0005-1098(99)00113-2.** **[VERIFIED — bibliographic data and survey scope via ACM DL / publisher listing; I did *not* read the body, so I am not attaching a theorem number to it]**
  Won the 2002 Automatica best-survey award. Standard entry point for positively-invariant and controlled-invariant sets in constrained control.
  **Why it bears:** the citation to use if a survey-level pointer is wanted rather than a specific theorem. **Caveat, honestly flagged:** I have not verified *which* result in it states the stationary-feedback selection, so please do not cite a numbered theorem from it on my word.

- **Aubin, J.-P. (1991). *Viability Theory.* Birkhäuser, Systems & Control: Foundations & Applications. ISBN 978-0-8176-3571-8, 543 pp.** **[VERIFIED — existence, publisher, and the publisher's own description of scope; the specific selection theorems inside are **[RECALLED, UNVERIFIED]**]**
  The publisher's description is itself the interesting part: the book emphasises "the construction of feedbacks and dynamical systems by **myopic optimization** methods," constructing systems of first-order partial differential inclusions whose solutions are feedbacks.
  **Why it bears — and this is the substantive point of this file:** viability theory's standard construction of a viable feedback *is* myopic optimization — but myopic **with respect to a function derived from the viability kernel**, not with respect to a naive one-step cost. That cuts against the brief's proposed dichotomy (see framing note below).
  **Caveat:** the continuous-time selection results rest on measurable/continuous-selection machinery (Michael's selection theorem, set-valued analysis regularity). I did **not** verify which theorem numbers, and in *discrete* time with a *finite* action set none of that machinery is needed — the selection is a bare application of choice. So Aubin is the wrong citation for a discrete-time finite-action claim; Bertsekas 1972 is the right one. Citing Aubin for a discrete-time result would invite a reviewer to ask why continuous-time selection theory is being invoked for a trivial selection.

### Negative results from this sweep

- **`~/src/arch/asf/ref/INDEX.md` has nothing relevant.** I grepped it for `sensor|schedul|submodular|kiefer|pukelsheim|design of experiment|viabil|invarian|loewner|excitation|riccati|kalman`. The single hit was an unrelated Levine 2018 RL-as-inference entry (matched on "Kalman duality" inside its annotation). This neighborhood is not in the local reference index.
- **The paper's own bib has no set-invariance, viability, or measurement-scheduling entries.** Checked `confident-agent-neurips-2026.extracted.bib`: closest neighbours are `sinopoli-2004-intermittent-kalman`, `boyd-ghaoui-feron-balakrishnan-1994-lmi`, `tanaka-kim-parrilo-mitter-2017-sdp`, `anderson-moore-1979-optimal-filtering`. Duplicate-citation risk for everything above is nil.
- **I did not find a result stating the viability-selection fact specifically for the Kalman/Riccati covariance recursion.** Athans 1972 gives the reduction and Bertsekas 1972 gives the invariance fact, but the composition — "the set of covariances from which λ_max(Σ) < R² is maintainable forever is the maximal controlled-invariant set of the Riccati recursion, hence admits a stationary policy" — I did not find stated anywhere as such. It is a two-line composition of two 1972 results, which is a good position to be in: cite both, state the composition in one sentence, claim no novelty for it.

---

## Framing feedback (offered as substantive disagreement, not bibliography)

Two places where I think the brief's framing may be doing the author a disservice. He asked for this over a tidy bibliography, so:

**1. Question (1) as posed may be unanswerable-because-false, and there is a much cleaner true statement nearby.** The brief asks for "a known theorem that no scalar function of the information matrix can characterize the Loewner-order feasibility of a mixture." As literally stated this is false, and cheaply so: the gauge functional

  φ(M) := λ_min(I_min^{-1/2} M I_min^{-1/2})

is a scalar function of the information matrix, and `E_π[I_o(a)] ⪰ I_min ⟺ φ(E_π[I_o(a)]) ≥ 1`. A scalar *of the averaged matrix* characterizes the condition exactly. (Note this φ is, up to normalization, precisely **E-optimality** in the metric induced by `I_min` — so the paper's LMI condition already *is* a scalar design criterion, just not one of the naive ones.)

So the real obstruction is not "no scalar exists" but **"scalarization does not commute with the mixture."** What fails is any scheme of the form *apply φ per-action, then average/compare*: `E_π[φ(I_o(a))] ≥ c`. And the reason it fails is the standard self-duality of the PSD cone — `{M : M ⪰ I_min}` is the intersection of the infinitely many halfspaces `{M : ⟨vvᵀ, M⟩ ≥ vᵀ I_min v}` over all directions `v`, so it takes a *family* of scalars indexed by direction, never one. Any single scalar-then-average test is one supporting hyperplane and must therefore either admit infeasible mixtures or exclude feasible ones.

If that is right, the author needs no exotic design-theory theorem at all: the statement is provable in a paragraph, and the only citation required is PSD-cone self-duality — **Boyd & Vandenberghe, which is already in his bib as `boyd-vandenberghe-2004-convex`**. That is a strictly better outcome than a citation hunt, and it also makes the claim sharper than "no scalar works," which a reviewer could refute with the φ above. I'd flag this as the highest-value item in this file after Athans.

**2. The "myopic vs non-myopic" reframing is right, but the honest version is "which scalar," and viability theory says so.** The author's step-2 argument concludes that state-dependent scalars always work in principle, so the real distinction is myopic-vs-non-myopic. Aubin's own framing (verbatim from the publisher description: feedbacks constructed "by myopic optimization methods") suggests the cleaner statement is that the distinction collapses one level further: viable feedback *is* obtained myopically, provided you are myopic in the right function — the viability kernel's own barrier/value function rather than a one-step covariance functional. So the true content of the negative result the author is hunting numerically is not "myopia fails" but **"the naive one-step covariance functionals (λ_max(P⁺), log det P⁺, tr P⁺, one-step information gain) are not the viability value function"** — which is a statement about those four specific scalars, and is exactly what a counterexample can establish. Framing the numerics as "myopic scalars fail" would overclaim relative to what a counterexample gives; framing it as "these four natural scalars are not viability-correct, and here is the configuration that shows it" is defensible and, I'd argue, more interesting.

Also worth noting because it interacts: per Athans, the covariance trajectory is *precomputable*, so this problem has no genuine information-feedback structure. "Non-myopic" here means nothing more than "solves the fixed-point recursion instead of one step of it." That makes the negative result cheaper to state but also weakens any rhetoric about the agent needing to *learn* or *probe* — there is nothing stochastic to adapt to in the covariance dynamics themselves.
