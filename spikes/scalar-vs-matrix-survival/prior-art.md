# Prior art — scalar vs matrix survival conditions

*Compiled 2026-07-29 for the `01-tragedy-confident-agent` spike. Merged synthesis over four neighborhood sweeps. Read this file first; the sibling files carry the full per-item detail, verbatim quotes, and BibTeX-ready metadata.*

| Sibling file | Neighborhood |
|---|---|
| `prior-art-sensor-scheduling.md` | Kalman sensor scheduling / selection: hardness, submodularity, stability-under-random-measurement, periodicity |
| `prior-art-design-excitation.md` | Optimal experiment design (Loewner order, Kiefer Φ_p, admissibility) + adaptive-control persistent excitation |
| `prior-art-index-policies.md` | Restless bandits / Whittle indexability — the closest match to the actual question |
| `prior-art-viability-reduction.md` | The deterministic reduction (Athans) + viability / controlled-invariance (question 2) |

**Epistemic rungs.** Each sibling file states its own marking convention; all four distinguish *read the actual text* from *read the abstract only* from *verified via a citing paper's reference list* from *recalled, unverified*. **No theorem number appears anywhere in this bundle that was not read off extracted source text.** Where a lead could not be verified, it is marked as a lead and not as a citation.

---

## The five things that matter

### 1. Question (1) is answered — and the answer is that the hoped-for theorem is false, not missing

**Three independent sweeps converged on the same construction.** The brief asked for "a known theorem that no scalar function of the information matrix can characterize the Loewner-order feasibility of a mixture." No such theorem exists, and none can, because the statement is false as posed. The counterexample is two lines:

  φ(M) := λ_min(I_min^{-1/2} M I_min^{-1/2}),  and  E_π[I_o(a)] ⪰ I_min ⟺ φ(E_π[I_o(a)]) ≥ 1.

This was derived independently three times tonight (once per sweep, no cross-talk). More importantly, it is not an ad-hoc gadget — it is a *bona fide* member of the design literature's canonical class:

- **Pukelsheim's information-function ↔ convex-set correspondence** establishes a **one-to-one correspondence** between information functions on the NND cone (isotonic w.r.t. Loewner, concave, positively homogeneous, nonconstant, upper semicontinuous) and closed convex subsets of NND that exclude zero and recede in all NND directions. `{M : M ⪰ I_min}` satisfies those hypotheses exactly, so φ above *is* an information function, and mixture-feasibility *is* a single scalar test. **[VERIFIED — read from Pukelsheim, Cornell Biometrics Unit tech report BU-943-M, 1987, open access]**
- Independently, **Druilhet's** universal-optimality material shows *distance to a convex cone* is itself a legitimate Kiefer criterion — a second constructive route to the same refutation. **[VERIFIED — full text read]**

**A design-theory reviewer would construct φ in about ten seconds.** So the unrestricted claim cannot appear in the paper.

**What is true, and is where the paper's real content lives** — three restricted claims, in increasing strength:

1. **No *per-action separable* scalarization works.** A constraint `E_π[f(I_o(a))] ≥ c` cannot characterize `E_π[I_o(a)] ⪰ I_min`. For concave isotonic `f`, Jensen gives `E[f(I_o(a))] ≤ f(E_π[I_o])`, so a per-action budget is sufficient-but-never-necessary — and the gap *is* the directional-mixing effect the paper is about. **This is almost certainly what the author's own argument actually establishes.**
2. **No member of the classical A/D/E/Φ_p family works.** Each Φ_p is Loewner-isotonic but not order-*reflecting*, so `Φ_p(Ī) ≥ Φ_p(I_min)` is necessary and never sufficient (for dimension ≥ 2, eigen-rotate to get equal Φ_p value with Loewner-incomparability). The lone exception is the λ_min end, and only under an **isotropic** floor.
3. **No *fixed, floor-independent* scalar works.** Any exact scalar characterization must be built *from* `I_min`. Rhetorically the strongest version: the matrix condition is not replaceable by a criterion chosen in advance of the survival floor — the floor's **anisotropy** is irreducible information no off-the-shelf design criterion carries.

**Two consequences for tonight.** (a) The author does not need a citation hunt for this; claim (1) is a paragraph, and the only citation needed is PSD-cone self-duality, i.e. **`boyd-vandenberghe-2004-convex`, already in his bib**. (b) The right positive citation is **Pukelsheim's equivalence theorem** — verbatim, Loewner optimality ⟺ *"optimal for c'θ for all vectors c ≠ 0 in the range of K"* — the field's canonical statement that the matrix condition is exactly the conjunction of a *continuum* of scalar conditions, one per direction, and no single one of them. That is the citable form of "directional, not magnitude."

**Also flagged: an optimality/feasibility category error to avoid.** Nearly all of the design literature's pessimism about the Loewner order ("partial order," "Loewner optimal designs mostly fail to exist except when K has rank one") is about *maximizing* over a set with no maximum. The paper's condition is *membership in a shifted PSD cone* — a convex feasibility question, where the Loewner order is perfectly well behaved and admits an exact concave gauge. Importing the pessimism wholesale would be caught by a design-theory reviewer. The correct imports are the equivalence theorem and the concavity-under-mixture reasoning (Pukelsheim's own justification for concavity, verbatim: *"information cannot be increased by interpolation"* — the design literature has already reasoned about mixtures of designs and concluded any legitimate criterion must be superadditive over them).

### 2. Question (2) is answered cleanly — two 1972 papers, and Aubin is the wrong citation

Yes, the viability move is standard, and it decomposes into two separately-citable steps. Neither needs proving.

- **The reduction — and this is the pleasant surprise:** **Athans (1972), *Automatica* 8(4), 397–412** states, verbatim in the abstract, that optimal measurement-strategy selection *"can be transformed into a deterministic optimal control problem"* with the policy and matched Kalman filter *"precomputed, i.e. specified before the measurements actually occur."* **[VERIFIED]** The author's own observation that the Riccati recursion's determinism makes survival a viability problem *is Athans' 1972 result.* Predecessor for the separation that licenses it: **Meier, Peschon & Dressler (1967), IEEE TAC 12(5), 528–536** **[VERIFIED]**.
- **The invariance/selection step:** **Bertsekas (1972), IEEE TAC 17(5), 604–613** — infinite-time confinement to a state-space region by feedback, the *n*-step reachability regions' limit, and confinement by a *linear time-invariant* law under stabilizability. **[VERIFIED]** Survey-level alternative: **Blanchini, *Automatica* 35(11):1747–1767, 1999** **[VERIFIED bibliographically; body unread — do not cite a numbered theorem from it on this sweep's authority]**.
- **Do not cite Aubin (1991) for this.** In discrete time with a finite action set, the selection is a bare application of choice; Aubin's continuous-time measurable/continuous-selection machinery (Michael's selection theorem et al.) is not needed and invoking it invites a reviewer to ask why. **[Aubin's existence/scope VERIFIED; the specific selection theorems inside are RECALLED, UNVERIFIED]**

**One substantive rider, which cuts against the brief's own dichotomy.** Aubin's publisher description emphasises constructing feedbacks *"by myopic optimization methods."* Viability theory obtains viable feedback **myopically** — but myopic in a function derived from the *viability kernel*, not in a one-step cost. So "myopic vs non-myopic" collapses one level further into **"which scalar."** The honest content of the negative result being hunted numerically is therefore not "myopia fails" but *"λ_max(P⁺), log det P⁺, tr P⁺ and one-step information gain are not the viability value function"* — a claim about those four specific scalars, which is exactly what a counterexample can establish and no more.

Also note, per Athans: the covariance trajectory is **precomputable**, so this problem has no genuine information-feedback structure. "Non-myopic" here means only "solves the fixed-point recursion rather than one step of it." That makes the negative result cheaper to state, but it also weakens any rhetoric about the agent needing to *probe* or *learn* — nothing in the covariance dynamics is stochastic.

### 3. The real prior-art center was off everyone's list: the question is a *recognized open problem*

Two sweeps converged independently on restless-bandit **Whittle indexability**, which is the author's question in its cleanest published form: an index *is* a state-dependent scalar functional of the belief state whose greedy argmax is the policy.

The literature's verdict:

- **Scalar (1-D) Kalman filter: a scalar index provably works.** Dance & Silander — cite the **JMLR 2019** version (*JMLR* 20, art. 35, pp. 1–93), which **proves** threshold optimality, not the NeurIPS 2015 version, whose Theorem 1 is *conditional* on an unproved assumption (A1). **[both VERIFIED — full text of the 2015 paper, verbatim abstract of the 2019]** The 2019 abstract also establishes that **LQG control with costly observations has threshold-structured optimal policies** — the closest thing in the literature to a positive answer to the author's step-2 intuition, and it holds only in dimension one.
- **Multidimensional Kalman filter — the paper's setting — is explicitly OPEN.** Stated verbatim, three times, in **Hao, Wang, Niño-Mora, Fu, Yang & Pan, arXiv:2312.07858 / *Sensors* 24(23):7755** — with Niño-Mora, who built the main tool for attacking it, as coauthor **[VERIFIED — full PDF read]**:
  > *"In the more practically relevant case of multi-target tracking RMABP models with multi-dimensional state Kalman filter dynamics, indexability is currently an open problem."*
  > *"In models with multi-dimensional tracking error covariance (TEC) state, the application of the Whittle index policy is at present elusive."*
  > *"at present it is unknown whether restless projects with multi-dimensional Kalman filter dynamics such as those above are indexable, even for a single dynamics model."*
- Corroborating hardness: **restless bandits are PSPACE-complete** (Papadimitriou & Tsitsiklis, *Math. of OR* 24(2):293–305, 1999) **[VERIFIED]**. Niño-Mora's Jan-2026 review (arXiv:2601.13045) corroborates the open status **by omission** — its Kalman coverage is entirely scalar-state **[VERIFIED — full text grepped]**.

**This is the answer to "tell me if the whole question is answered somewhere."** It is the opposite, and better: the closest well-posed version of the question is an acknowledged open problem in operations research. That means (a) nothing is being reinvented, (b) there is a citable justification for offering a *sufficient matrix certificate* rather than a scalar index, and (c) a counterexample defeating the natural myopic scalars in the matrix case would contribute to a *named* open problem, not merely support a lemma.

**Suggested reframing.** Adopting this vocabulary, the contribution reads: *the multidimensional survival problem is not known to be indexable, so we give a tractable sufficient matrix certificate instead* — far stronger than *we could not find a scalar that works*. And the state-independent-scalar collapse result is best described as ruling out **static (non-index) scalar rules**, which is sharper than "scalars fail."

### 4. A flag on the author's own proof: the comparison class may be periodic, not constant

Offered as a flag, not a refutation — nobody on this sweep read the proof. Three independent results say the relevant behavior class in this problem family is **periodic**:

- **Mo, Garone & Sinopoli**, *SCL* 67:65–70, 2014 — any finite-cost infinite-horizon sensor plan is approximable arbitrarily closely by a **periodic** one. **[VERIFIED-abstract]**
- **Zhao, Zhang, Hu, Abate & Tomlin**, IEEE TAC 2014 / arXiv:1312.0157 — optimal infinite-horizon average cost *and* optimal schedules are **independent of the initial covariance**; approximable arbitrarily closely by a finite-period schedule. **[VERIFIED-abstract]**
- **Orihuela, Barreiro, Gómez-Estern & Rubio**, *Automatica* 50:2672–2676, 2014 — the **greedy Kalman-based scheduler itself** converges to a periodic selection / unique limit cycle. **[lead — search snippets only]**

If the internal proof's "constant-action" conclusion means *open-loop constant*, the comparison class is too small, and the honest statement is collapse to **periodic** policies — a weaker collapse and a harder thing to defeat, because a periodic schedule can alternate to control two eigendirections in turn, which is precisely the mechanism a λ_max constraint exercises. If "constant" already means constant *distribution* π sampled i.i.d., these results are instead a strengthening opportunity and independent confirmation the reduced class is rich enough. **Either reading changes what a defeating configuration has to defeat, so it is worth checking against the actual proof before interpreting tonight's numerics.**

### 5. Retarget the numerics: feasibility separation, not cost suboptimality — and expect λ_max to be hard

**The requested artifact does not exist, and would not have settled the question anyway.** No published counterexample to greedy-on-λ_max or greedy-on-log-det exists in the per-step *scheduling* setting (explicit negative; see sibling file §6). But more consequentially: *"greedy is not optimal"* is **strictly weaker** than *"greedy fails to survive."* A policy can be badly suboptimal in cost and still hold λ_max(Σ) under threshold; a cost-optimal policy carries no survival guarantee. Importing a suboptimality citation would be a subtle overclaim.

**What the question needs is a feasibility separation:** an instance where survival is achievable by *some* policy and the greedy-scalar policy fails it. That is also probably an *easier* search — R² can be chosen adversarially after seeing both trajectories, so no large cost gap is needed, only one that straddles the threshold.

Three practical facts for the search:

- **λ_max will be hard to defeat.** Chamon, Pappas & Ribeiro (arXiv:1912.03799, IEEE TAC) prove worst-case error is *approximately* supermodular with greedy certificates approaching (1−1/e). **[VERIFIED-abstract]** A λ_max failure likely has to live where their bound degrades — and their bound is the map to that regime.
- **Formulation, not functional, decides submodularity.** Zhang, Ayoub & Sundaram (CDC 2015) **Example 1** is an explicit 2-state/4-sensor instance (data transcribed in the sibling file) breaking sub- *and* super-modularity of trace, log-det, **and** λ_max **simultaneously**, for the steady-state DARE covariance. **[VERIFIED — full text]** Jawaid & Smith's log-det submodularity is a **single-step** result and is log-det of the *information*, not the covariance. Tzoumas et al. get log-det supermodularity in the *placement* formulation. So the brief's hunch checks out but is sharper than stated: the split closes once the Riccati map is involved.
- **Use an exact oracle rather than hand-rolling a DP.** Dutta, Wilde & Smith (arXiv:2304.02692) give MIQP exact optima for 30–50-state systems in seconds. **[VERIFIED-abstract]** Also: Ye, Roy & Sundaram (arXiv:1711.01920) **Thm 1** NP-hard even for stable A with equal costs, **Thm 2** no poly-time constant-factor approximation, **Thm 3** greedy-on-trace ratio → 2/3 + 1/(3(1−λ₁²)), unbounded as λ₁→1 — note this is design-time *selection* and *trace*, but the blow-up parameter is degree of stability, i.e. exactly the drifting regime. **[VERIFIED — full text]**

---

## On "necessary": the field cannot carry that claim either

**Rohr, Marelli & Fu**, IEEE TAC 59(10), 2014 give a necessary condition and a sufficient condition for boundedness of E[error covariance] **separated by an acknowledged gap** — in the *strictly easier* intermittent-observation setting (single sensor, random dropouts, no action-dependent R_o). **[VERIFIED-abstract]** So the necessity of the matrix condition is **not a gap in the author's work; it is a gap in the field.** The defensible position is sufficiency + a characterized gap + the §3 open-problem citation. That is a *stronger* paper-level stance than a necessity claim, because "this reduces to a recognized open problem in restless-bandit indexability" is citable and checkable.

**Closest published structural match, full read outstanding:** **Marelli, Sui, Rohr & Fu, arXiv:1806.08098 / *Automatica*** — stability of Kalman filtering with a **random measurement equation** (random H *and* R), i.e. structurally the E_π setting, with "a necessary and a sufficient condition." Whether those reduce to something like `E_π[I_o] ⪰ I_min` is exactly what the text would settle. *This read is in progress as of writing; see the sensor-scheduling sibling file for the outcome.*

---

## Persistent excitation: a supporting analogy, with a caveat that matters

**Shimkin & Feuer**, *Systems & Control Letters* 9 (1987) 225–233 **[VERIFIED — full text]** is the cleanest citable instance of the paper's thesis in control: PE is *definitionally* a Loewner lower bound on an averaged information-like matrix (Def. 1: `∫_τ^{τ+T} x x* dt > ε₁ I`), and the **necessary-and-sufficient** characterization is a *uniform linear independence / projection* condition — directional, not energy. Their Theorem 1: an input is PE for the class iff it is "rich of order n."

**The caveat, and it is important:** their floor is `ε₁ I` — **isotropic** — and for an isotropic floor λ_min *is* an exact scalar characterization. **No anisotropic-floor PE result was found in this sweep** (explicit negative). So the control literature furnishes an analogy, not a substitute theorem; and if the paper's `I_min` is anisotropic — which is where all its novelty lives — that anisotropy is a genuine departure from the PE literature and should be sold as such rather than assimilated to it.

Modern subspace framing, and it is 2025 so the question is live: **Cao, Wang, Guay, Wang, Duan & Polycarpou, "Deficient Excitation in Parameter Learning," arXiv:2503.02235** — learning error converges exponentially *within the identifiable subspace* without PE; the distributed version uses **complementary DE conditions** across estimators, a structural cousin of the paper's mixture (individually deficient excitations combining to cover the space). **[VERIFIED-abstract only — do not cite a numbered result without opening it]**

---

## Explicit negatives (recorded deliberately)

1. **No theorem "no scalar function of the information matrix characterizes Loewner-feasibility of a mixture."** It does not exist and cannot — constructively refuted twice (Pukelsheim's correspondence; Druilhet's distance-to-cone criterion). Any no-go must state its class restriction as a hypothesis.
2. **No theorem "every admissible (Loewner-maximal) design is optimal for some scalar criterion."** The verified implication runs the other way (scalar-optimal ⟹ admissible, per Pukelsheim Ch. 10 via Dette–Liu–Yue). The general-position substitute is **Arrow–Barankin–Blackwell** (properly-efficient points are *dense* in the efficient set), which is where impossibility-of-scalarization results actually live — vector-optimization theory, not design theory. The brief's "supporting hyperplanes vs the PSD cone" intuition is right in mechanism but needs *proper* efficiency and density, not surjectivity.
3. **No published counterexample to myopic λ_max or log-det scheduling** in the per-step setting. Tonight's numerics are not redundant.
4. **Nobody treats λ_max(Σ) < R² as a *constraint* rather than an objective** in the sensor-scheduling literature — the field minimizes cost subject to *resource* constraints, not covariance constraints. The feasibility framing is genuinely under-occupied. This is a novelty argument, and it is why the stability/boundedness sub-literature is better matched than the optimality one.
5. **No λ_max submodularity boundary stated as an iff** — every verified statement is "not submodular in general" plus a counterexample, or "approximately supermodular with a certificate." Unclaimed territory.
6. **No anisotropic-floor persistent-excitation result.**
7. **No result composing Athans' reduction with viability** — i.e. "the set of covariances from which λ_max(Σ) < R² is maintainable forever is the maximal controlled-invariant set of the Riccati recursion, hence admits a stationary policy" is not stated anywhere as such. It is a two-line composition of two 1972 results: cite both, state the composition, claim no novelty.
8. **`~/src/arch/asf/ref/INDEX.md` has nothing in any of these neighborhoods** (one irrelevant Kalman-duality mention in a Levine 2018 annotation). Checked independently by three sweeps.
9. **The paper's bib has zero overlap** with sensor scheduling, restless bandits, set invariance, or design theory. Duplicate-citation risk is nil across the whole bundle. Notably absent despite being foundational: Meier/Peschon/Dressler 1967.

## Unfinished, in priority order

1. **Marelli/Sui/Rohr/Fu arXiv:1806.08098 full text** — the closest structural match; in progress.
2. **Pukelsheim 1980, "On linear regression designs which maximize information," JSPI 4(4):339–364** — E-optimality duality. E-optimality's non-differentiability is exactly the eigenvalue-crossing that makes a scalar λ_min budget behave badly under mixing, and the dual is a mixture over the minimal eigenvalue's eigenspace. Likely reusable as a **strengthening route**, not merely prior art. Highest-value unread item on the design side.
3. **Pang & Shan 2019, IEEE Sensors J. 19(18):8224–8232** — cited by the radar paper for "in general, myopic scheduling policies exhibit inevitable performance degradation in the long run." Unknown whether theorem or empirical remark.
4. **Forward-citation sweep of Dance & Silander 2019** for any post-2023 multidimensional indexability progress.
5. **Jawaid & Smith's own theorem numbers** — paywalled, no arXiv version found.
6. ~~The Automatica 1996 performance-limitation paper — authors/volume unresolved.~~ **RESOLVED, see below.**
7. **Blanchini 1999 body** — to attach a specific theorem to the stationary-feedback claim, if a numbered citation is wanted.

---

## Resolved during the sweep: the closest necessity-flavored result on the control side

**Tsakalis, Kostas (1996). "Performance limitations of adaptive parameter estimation and system identification algorithms in the absence of excitation." *Automatica* 32(4), 549–560. DOI 10.1016/0005-1098(95)00163-8.** **[bibliographic data VERIFIED — authoritative DBLP record `journals/automatica/Tsakalis96` retrieved directly, cross-checked against the Semantic Scholar API; body NOT read — ScienceDirect 403s]**

Sole author (initially reported as unresolved; the ScienceDirect paywall was the obstacle). Earlier conference version: **Proc. 1994 American Control Conference**, vol. 2, pp. 1260–1264, DOI 10.1109/ACC.1994.752260 **[VERIFIED via Semantic Scholar API]**.

Per its abstract as reported in search results **[NOT verified against the article itself — treat the content claims as a lead]**: constructs a **bursting scenario** to derive an **analytical lower bound on the worst-case peak steady-state error** for a wide class of parameter-estimation and identification algorithms, showing that absent input constraints, arbitrarily small perturbations impose a serious performance limitation, with worst-case performance deteriorating proportionally to the size of the parametric uncertainty set.

**Why it bears.** This is the nearest thing found in *any* neighborhood to a genuine **impossibility/necessity** theorem: absent adequate excitation, *no algorithm in a broad class* escapes a quantified error floor. If the paper wants a converse ("without the matrix condition, failure"), this is the analogue to cite — and to distinguish from, since Tsakalis' floor is about estimation error under perturbation rather than covariance survival. It also connects directly to `anderson-1985-bursting`, already in the bib: same bursting phenomenon, but with a lower bound attached. **The body is worth a real read** if the paper makes any necessity-flavored claim; the bibliographic data above is now solid enough to cite.

## A note on how much to trust §1

The gauge-function refutation is the one result in this bundle with **triple independent derivation** (three sweeps, no cross-talk) plus **two independent constructive confirmations from published sources**. If any single item here should change tonight's plan, it is that one — the unrestricted no-go cannot go in the paper, and the restricted version is both true and more interesting.
