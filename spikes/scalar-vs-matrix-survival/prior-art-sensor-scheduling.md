# Prior art — Kalman sensor scheduling / sensor selection

*Neighborhood sweep for the scalar-vs-matrix survival question. Compiled 2026-07-29. Other neighborhoods (optimal experiment design, viability theory) covered separately.*

**Epistemic marking convention used throughout:**

- **[V-full]** — I fetched and read the paper text (PDF extracted to plain text); theorem numbers and statements below were read off that text.
- **[V-abs]** — I fetched the arXiv/journal abstract page and read it; claims are at abstract granularity. Theorem numbers are *not* asserted.
- **[V-2nd]** — bibliographic details verified from a *citing* paper's reference list that I read directly, not from the paper itself.
- **[U]** — recalled or search-snippet only, **not verified**. Treat as a lead, not a citation.

Nothing below is offered as a theorem number I did not read. Where a number appears, it came from **[V-full]** text.

---

## 0. The headline for tonight

**The single most useful thing I found is not a counterexample to greedy — it is that the exact question being asked is a recognized open problem in the closest adjacent literature.**

Dance & Silander (NeurIPS 2015) study precisely "can a *scalar index* of the Kalman belief state substitute for the full matrix in scheduling," and their closing sentence is that the multidimensional case **remains open** (§4 below). Their positive result is confined to a *scalar* (1-D) Kalman filter, and even there it is *conditional* on an unproven assumption (A1), for which they report finding counterexamples to the submodularity condition one would use to prove it.

**Second most useful, and it may change the plan:** two independent results (Mo/Garone/Sinopoli 2014; Zhao/Zhang/Hu/Abate/Tomlin 2014) prove that any infinite-horizon schedule with finite average cost can be **approximated arbitrarily closely by a periodic schedule**, and a third (Orihuela et al. 2014) shows that the *greedy Kalman-based* scheduler itself typically converges to a **periodic** selection / limit cycle. This suggests the natural comparison class for the state-independent-scalar argument is **periodic**, not **constant** — see §7 (feedback) for why I think this is worth checking against the existing "state-independent scalars collapse to constant-action policies" proof before it is relied on.

**Third:** there *is* a hard, verified, published negative result for greedy — Ye/Roy/Sundaram, Theorem 3 — but it is for **design-time sensor selection** (a fixed subset for all time), not per-step scheduling, and it is about **trace**, not λ_max. It is an unbounded-ratio result, so it is stronger than "suboptimal"; it is just in the adjacent problem. See §2 and the caveat in §7.

---

## 1. Verified non-submodularity / non-supermodularity results

### 1.1 Zhang, Ayoub & Sundaram — the explicit counterexample for all three scalars **[V-full]**

Haotian Zhang, Raid Ayoub, Shreyas Sundaram, "Sensor Selection for Optimal Filtering of Linear Dynamical Systems: Complexity and Approximation," Proc. 54th IEEE Conference on Decision and Control (CDC), 2015. (Journal version: *Automatica* 78:202–210, 2017, "Sensor selection for Kalman filtering of linear dynamical systems: Complexity, limitations and greedy algorithms" — journal version **[U]**, CDC version **[V-full]** from <https://engineering.purdue.edu/~sundara2/papers/cdc15_sensor_selection.pdf>.)

Read directly from the text:

- They define three metrics over the DARE solution Σ(z): **F₁(z) = −trace(Σ(z))**, **F₂(z) = log det(Σ⁻¹(z))**, **F₃(z) = −max_i λ_i(Σ(z))** — explicitly noting "F₂ captures the volume of the confidence ellipsoid and F₃ captures the worst-case error covariance." *These are exactly three of the four myopic scalars in the numerics.*
- **Theorem 1:** "The KFSS problem is NP-hard."
- **Theorem 2:** "The KFSS problem is NP-hard even under the [assumption that A is stable]."
- **Example 1** (verbatim data): A = [[0.3, 0.2], [0.4, 0.6]], Cᵀ = [[1, 0.5, 0.7, 0], [0, 0.5, 0.3, 0.7]], W = I₂, V = I₄; eig(A) = {0.1298, 0.7702}. "One can check that ΔF_i({1}|{2,3}) < ΔF_i({1}|{2,3,4}) and ΔF_i({1}|{2}) > ΔF_i({1}|{2,3}), i ∈ {1,2,3}, which contradict the submodularity and supermodularity of the corresponding metrics, respectively."
  → **A single 2-state, 4-sensor instance in which trace, log-det, *and* λ_max all simultaneously fail both submodularity and supermodularity, for the steady-state (DARE) covariance.**
- They attribute to Jawaid & Smith: "In [3], the authors showed that the metric F₂ is submodular for the **single-step** sensor scheduling problem while F₁ and F₃ are neither submodular nor supermodular."
  → **This confirms the coordinator's unverified hunch, and sharpens it: log-det's submodularity is a *single-step* result, and it is log-det of the *information* (Σ⁻¹), not of the covariance.** λ_max and trace are neither, already at one step.
- They also show (Theorem 5, read but not transcribed) that a *Lyapunov-equation relaxation* of the cost **is** modular, giving a greedy variant with guarantees — i.e. the tractable scalar surrogate is obtained by giving up the Riccati recursion.

**Bears on the question:** this is the cleanest verified statement that the covariance-derived scalars split — log-det-of-information behaves, λ_max and trace do not — and that the split closes (all three fail) as soon as the steady-state Riccati map is involved rather than one step.

BibTeX-ready: `zhang-ayoub-sundaram-2015-sensor-selection-complexity`, CDC 2015, pp. 5251–5256 (page range **[U]**). Journal: *Automatica*, vol. 78, pp. 202–210, 2017, DOI `10.1016/j.automatica.2016.12.025` **[U — DOI recalled, unverified]**.

### 1.2 Jawaid & Smith — the source of the log-det submodularity result **[V-2nd]**

S. T. Jawaid and S. L. Smith, "On the submodularity of sensor scheduling for estimation of linear dynamical systems," Proc. American Control Conference (ACC), 2014, pp. 4139–4144. Journal version: "Submodularity and greedy algorithms in sensor scheduling for linear dynamical systems," *Automatica*, vol. 61, pp. 282–288, 2015.

Bibliographic details **[V-2nd]** (read from Zhang et al.'s reference list [3] for the ACC version; the Automatica version's volume/pages from search snippets, **[U]**). **I did not read either paper's text** — the ScienceDirect page is paywalled and no arXiv version surfaced under several queries. So: the "F₂ submodular, F₁ and F₃ neither" attribution above is Zhang et al.'s characterization of Jawaid & Smith, which is **[V-full] as a claim in Zhang et al.** and **[U] as a claim about Jawaid & Smith's own theorem numbering**. If a specific theorem number from Jawaid & Smith is going to be cited, someone needs the actual PDF.

### 1.3 Tzoumas, Jadbabaie & Pappas — log-det supermodularity + a linear-decay fundamental limit **[V-abs]**

Vasileios Tzoumas, Ali Jadbabaie, George J. Pappas, "Sensor Placement for Optimal Kalman Filtering: Fundamental Limits, Submodularity, and Algorithms," arXiv:1509.08146 (ACC 2016 **[U]**).

From the abstract page: the **log-det of the Kalman error covariance is a supermodular, non-increasing set function** in the choice of sensor set (hence diminishing returns and a greedy guarantee), whereas the **minimum mean-square error does not** exhibit that structure. They also state a fundamental limit — MMSE decreases only *linearly* in the number of sensors, so sensor count must grow linearly with system size to hold error fixed.

**Bears on the question:** the linear-decay limit is a quantitative statement about how much information-purchasing power extra observation channels buy, which is the same currency as I_min. Also: note the tension with §1.1 — Tzoumas gets supermodularity for log-det over a *finite-horizon/placement* formulation while Zhang et al.'s Example 1 breaks it for the *steady-state DARE* formulation. **The formulation, not the functional, is what decides it.** That distinction is worth carrying into the paper if any submodularity claim is made.

### 1.4 Chamon, Pappas & Ribeiro — λ_max is *approximately* supermodular **[V-abs]**

Luiz F. O. Chamon, George J. Pappas, Alejandro Ribeiro, "Approximate Supermodularity of Kalman Filter Sensor Selection," arXiv:1912.03799; IEEE Transactions on Automatic Control (year **[U]**).

From the abstract: MSE and **worst-case error** (i.e. λ_max) are **not** supermodular — but they prove *approximate* supermodularity and derive greedy near-optimality certificates that "approach the (1−1/e) guarantee" in typical scenarios, on the original metrics rather than on a log-det surrogate.

**Bears on the question — and it cuts against the hoped-for counterexample.** This is the strongest published reason to expect the numerics hunting for a myopic-λ_max failure to be *hard*: greedy on λ_max carries a data-dependent near-optimality certificate. A hand-built failure will likely have to live in the regime where their certificate degrades, and the paper's own bound is the map to that regime. Related, same group: "Approximately Supermodular Scheduling Subject to Matroid Constraints," arXiv:2003.08841 **[U]**.

---

## 2. Verified hardness and greedy-failure results

### 2.1 Ye, Roy & Sundaram — no constant-factor approximation, and greedy arbitrarily poor **[V-full]**

Lintao Ye, Sandip Roy, Shreyas Sundaram, "On the Complexity and Approximability of Optimal Sensor Selection for Kalman Filtering," arXiv:1711.01920v2 [math.OC], 28 Mar 2018 (ACC 2018 **[U]**). Read from the extracted text:

- **Theorem 1:** "The KFSS problem is NP-hard when the system dynamics matrix A is stable and each sensor i ∈ Q has identical cost." (Reduction from Exact Cover by 3-Sets.)
- **Theorem 2:** "If P ≠ NP, then there is no polynomial-time constant-factor approximation algorithm for the KFSS problem."
- **Example 1 + Theorem 3 — the greedy counterexample, verbatim data:** W = I₃, V = 0₃ₓ₃, A = diag-like [[λ₁,0,0],[0,0,0],[0,0,0]], C = [[1,h,h],[1,0,h],[0,1,1]], with 0 < |λ₁| < 1 and h > 0; Q = {1,2,3}, budget B = 2, cost vector b = [1 1 1]ᵀ. **Theorem 3:** for this instance the greedy-to-optimal trace ratio satisfies

  lim_{h→∞} r_gre(Σ) = 2/3 + 1/(3(1 − λ₁²)).

  Since λ₁ → 1 makes this diverge, "r_gre(Σ) can be made arbitrarily large."

**Bears on the question:** this is a *published, checkable, three-state* instance where greedy-on-trace is unboundedly worse than optimal, and the blow-up parameter is exactly *degree of stability* (λ₁ → 1) — i.e. the near-critical/drifting regime the paper's survival setting lives in. **Caveat, and it matters: this is design-time selection (one fixed subset held forever), not per-step scheduling, and the metric is trace, not λ_max.** See §7.

Companion/extended version: "On the Complexity and Approximability of Optimal Sensor Selection and Attack for Kalman Filtering," arXiv:2003.11951 **[U]** (adds the adversarial-attack variant; likely IEEE TAC).

### 2.2 The frequently-quoted "myopic is highly suboptimal" line **[V-abs, but it is an assertion, not a theorem]**

The sentence that recurs across this literature — "a greedy policy that schedules the sensor which minimizes the error at each time step would be expected to be close to optimal; however such a greedy policy is highly suboptimal due to its myopic nature" — I traced to **arXiv:2312.16813, "Monitoring Correlated Sources: AoI-based Scheduling is Nearly Optimal"** (authors **[U]**). It is offered there as motivation, **not** proved, and the setting is correlated-source/AoI monitoring. **Do not cite it as a theorem.** Flagging it because it is the kind of line that gets cited as if it were one.

---

## 3. The stability / survival-condition line — closer to the actual question than the optimality line

This is the sub-neighborhood I would push hardest on, because it is about *feasibility* (bounded covariance) rather than *optimality* (minimal cost), which is what "survival" is.

### 3.1 Rohr, Marelli & Fu — necessary and sufficient, with a gap **[V-abs]**

Eduardo R. Rohr, Damián Marelli, Minyue Fu, "Kalman Filtering With Intermittent Observations: On the Boundedness of the Expected Error Covariance," IEEE Transactions on Automatic Control, vol. 59, no. 10, Oct 2014 (pages **[U]**). Author-hosted PDF exists at <https://www.eng.newcastle.edu.au/~mf140/home/Papers/TAC2014_2.pdf> (I did not extract it — worth 10 minutes if this becomes load-bearing).

They give **a necessary condition and a sufficient condition, with a "trivial gap" between them**, for boundedness of E[error covariance], requiring only that A be diagonalizable and the loss process be a stationary finite-order Markov process (generalizing beyond i.i.d. / Gilbert-Elliott, and covering degenerate systems).

**Bears on the question — this is the most important epistemic caution in the sweep.** In the *strictly easier* setting (single sensor, random dropouts, no action-dependent R_o), the field has **not** closed the gap between necessary and sufficient conditions for bounded expected covariance. That is direct evidence that proving the policy-averaged PSD condition E_{a~π}[I_o(a)] ⪰ I_min *necessary* is likely to be hard-to-impossible in general, and that the honest paper-level claim is sufficiency plus a characterized gap. It also means "is the matrix condition genuinely necessary" is not a gap in the author's work — it is a gap in the field.

### 3.2 Marelli, Sui, Rohr & Fu — random measurement *equation*, which is the E_π setting **[V-abs]**

Damián Marelli, Tianju Sui, Eduardo Rohr, Minyue Fu, "Stability of Kalman Filtering with a Random Measurement Equation: Application to Sensor Scheduling with Intermittent Observations," arXiv:1806.08098; *Automatica* (2019, vol./pages **[U]**).

Generalizes §3.1 to the case where **the measurement matrix and the measurement error covariance are both random** — i.e. exactly H(a), R_o(a) drawn from a policy — and states "a necessary and a sufficient condition for stability," plus numerical computation of them. The stated application is multi-sensor scheduling over a lossy network.

**Bears on the question:** this is the closest published match to the paper's own object of study. If any single item in this sweep deserves a full read tonight, I would nominate this one: it may already contain, in different notation, the necessary-direction analysis being attempted — and the abstract's phrasing ("*a* necessary and *a* sufficient condition") suggests it too stops short of an iff. The abstract does not mention PSD-order or expected-information-matrix conditions; whether their conditions reduce to something like E_π[I_o] ⪰ I_min is exactly what reading the text would settle. **I did not verify this; it is the biggest open item I am handing back.**

### 3.3 Gupta, Chung, Hassibi & Murray — stochastic (policy-averaged) sensor selection **[V-2nd for bibliography, U for content]**

V. Gupta, T. H. Chung, B. Hassibi, R. M. Murray, "On a stochastic sensor selection algorithm with applications in sensor scheduling and sensor coverage," *Automatica*, vol. 42, no. 2, pp. 251–260, 2006. (Bibliographic details **[V-2nd]** from Zhang et al.'s reference list [2].)

Content **[U]**, from search snippets only: they activate one sensor per step according to a *prescribed probability distribution*, derive the optimal distribution, and analyze the expected error covariance via the Riccati recursion, obtaining **upper and lower bounds** (not an exact characterization).

**Bears on the question:** this is the canonical "randomized policy, analyze E[Σ]" paper — i.e. the policy-averaging move — and the fact that it lands on bounds rather than an exact condition is another data point for §3.1's caution. It is also the natural citation for *why* one averages over π at all.

---

## 4. The one that is actually about scalar-index-vs-matrix — and calls it open

**Christopher Dance, Tomi Silander, "When are Kalman-Filter Restless Bandits Indexable?", Advances in Neural Information Processing Systems 28 (NeurIPS/NIPS 2015).** arXiv:1509.04541. **[V-full]** — read from the NeurIPS proceedings PDF.

Verbatim from the abstract: "We study the restless bandit associated with an extremely simple **scalar** Kalman filter model in discrete time. Under certain assumptions, we prove that the problem is indexable in the sense that the Whittle index is a non-decreasing function of the relevant belief state. In spite of the long history of this problem, **this appears to be the first such proof.**"

Read from the body:

- **Theorem 1:** "Suppose a threshold policy (A1) is optimal for the single-arm problem (2). Then Problem KF1 is indexable." (A supplementary Theorem 1 restates: "The index λ_W(x) of (6) is continuous and non-decreasing for x ∈ ℝ₊.")
- §5 Further Work, verbatim: "One might attempt to prove that assumption A1 holds using general results about monotone optimal policies for two-action MDPs based on submodularity [2] or multimodularity [1]. However, **we find counter-examples to the required submodularity condition.** … Finally, the question of the **indexability of the discrete-time Kalman filter in multiple dimensions remains open.**"

**Why this is the highest-value item in the sweep.** Indexability *is* the scalar-vs-matrix question in its cleanest published form: a Whittle index is precisely a scalar functional of the (matrix) belief state whose greedy argmax is asymptotically optimal. So the literature's verdict, as of this paper, is:

1. For a **1-D** Kalman filter, a scalar index provably works — **conditional** on an assumption (A1) they could not prove, and for which the obvious submodularity route has **counterexamples**.
2. For **multidimensional** Kalman filters — the paper's setting — **it is open.**

That means: (a) the live question is genuinely open in the nearest literature, which is good for novelty and bad for "cite instead of prove"; (b) there is a published *scalar-index* candidate (the Whittle index) that is neither of the four myopic scalars being tested numerically, and it is state-dependent-and-non-myopic by construction — which is exactly the "myopic vs non-myopic is the real distinction" position, arrived at independently by a different community; (c) the counterexamples-to-submodularity remark is a lead worth chasing for a hand-built myopic failure, since a broken monotone-policy structure is where greedy-index reasoning fails.

BibTeX-ready: `dance-silander-2015-kalman-restless-bandits-indexable`, NeurIPS 2015, arXiv:1509.04541.

Adjacent, unverified **[U]**: José Niño-Mora and co-authors on "multitarget tracking via restless bandit marginal productivity indices and Kalman filter in discrete time" (IEEE conference, ~2009) and "Sensor Scheduling for Hunting Elusive Hiding Targets via Whittle's Restless Bandit Index Policy." Also Whittle (1988) for the index itself. The restless-bandit framing is off the author's guess-list entirely and I think it is the most productive thing on this page.

---

## 5. Periodicity — the result that may bear on the state-independent-scalar proof

Three independent items, all pointing the same way:

- **Y. Mo, E. Garone, B. Sinopoli, "On infinite-horizon sensor scheduling," *Systems & Control Letters*, vol. 67, pp. 65–70, 2014. [V-abs]** — "any infinite-horizon (non-periodic) sensor plan [can] be approximated arbitrarily well by a periodic sensor plan"; they give a lower bound on optimal cost that quantifies the gap of any suboptimal schedule. Author page: <https://yilinmo.github.io/papers/scl-14-optschedule.html>.
- **L. Zhao, W. Zhang, J. Hu, A. Abate, C. J. Tomlin, "On the Optimal Solutions of the Infinite-Horizon Linear Sensor Scheduling Problem," IEEE TAC, 2014; arXiv:1312.0157. [V-abs]** — the optimal infinite-horizon average-per-stage cost and the optimal schedules are **independent of the initial-state covariance**; the optimal cost "can be approximated arbitrarily closely by a periodic schedule with a finite period."
- **L. Orihuela, A. Barreiro, F. Gómez-Estern, F. R. Rubio, "Periodicity of Kalman-based scheduled filters," *Automatica*, vol. 50, pp. 2672–2676, 2014. [U — search snippets only]** — under mild conditions (A nonsingular, bounded trajectory, no limit points on the switching boundary), a **Kalman-based scheduled filter (i.e. the greedy/scheduled scheme itself) produces a periodic selection of sensors**; the covariance trajectory converges to a unique limit cycle.

**Bears on the question, possibly critically.** The existing internal result is (as relayed) that *state-independent* scalars collapse to **constant-action** policies. These three results say the relevant optimal/attained behavior in this problem class is **periodic with a limit cycle**, and Zhao et al. add that it is independent of P₀. Two readings, and they have different consequences:

- If the internal proof's "constant-action" conclusion is about *open-loop constant*, then the periodicity literature says the comparison class was too small, and the honest statement is "collapse to *periodic* (equivalently, finitely-parameterized open-loop) policies" — which is a *weaker* collapse and a *harder* thing to defeat, because a periodic open-loop schedule can do things a constant one cannot (e.g. alternate to control two eigendirections in turn — precisely the mechanism a λ_max survival constraint would exercise).
- If the proof already means "constant" in a sense that subsumes periodicity (e.g. constant *distribution* π, sampled i.i.d.), then the periodicity results are a *strengthening* opportunity rather than a problem — and worth citing as independent confirmation that the reduced class is rich enough.

Either way I think this is worth 20 minutes against the actual proof before tonight's numerics are interpreted, because it changes what a "defeating configuration" has to defeat. I am **not** asserting the internal proof is wrong — I have not read it. I am saying the literature's comparison class is periodic, not constant, and the difference is load-bearing for a λ_max-style constraint.

---

## 6. Explicit negative results — things I looked for and did not find

Written down deliberately rather than omitted.

1. **A published counterexample showing greedy/myopic scheduling on λ_max(P⁺) of the Kalman covariance is not optimal — in the *per-step scheduling* (not design-time selection) setting.** I did not find one. What exists is: non-submodularity of λ_max (§1.1, §1.4 — which is *not* the same as suboptimality of greedy), *approximate* supermodularity with near-optimality certificates for λ_max (§1.4 — which points the other way), and an unbounded-ratio greedy counterexample for **trace** in the **design-time selection** problem (§2.1). **The specific artifact hoped for does not appear to exist in this literature.** Tonight's numerics are therefore not redundant — but see §7 for what I think they should be aimed at.

2. **A published counterexample for greedy on log-det in the scheduling setting.** Not found. The literature's stance on log-det is the opposite — it is the functional that *does* behave (single-step submodularity, Jawaid & Smith via §1.1; supermodularity in the placement formulation, §1.3). If the numerics defeat myopic log-det, that would be a genuinely novel data point and should be checked hard against §1.1's formulation caveat (which formulation? single-step, finite-horizon, or steady-state DARE?) before being claimed.

3. **Any result stating that no scalar functional of (P_t, I_o(a)) can maintain a covariance/survival constraint whenever it is maintainable** — i.e. the negative direction of the paper's actual question. Not found. The nearest thing is §4's "remains open," which is the same question in bandit clothing and is *not* answered.

4. **Anyone treating "survival" / λ_max(Σ) < R² as a *constraint* rather than an objective in the sensor-scheduling literature.** I found essentially nothing. The whole field minimizes a cost (trace, log-det, worst-case error) subject to *resource* constraints (budget, number of sensors, matroid, channel), not subject to a *covariance* constraint. The constraint-satisfaction / feasibility framing appears to be genuinely under-occupied here — which is a novelty argument for the paper, and also why §3 (stability/boundedness) is a better-matched sub-literature than §1–§2 (optimality).

5. **λ_max-specific submodularity conditions stated as an iff.** Not found — every statement I verified is of the form "not submodular in general" plus a counterexample, or "approximately supermodular with a certificate." No one appears to have characterized the exact boundary. If the paper needs that boundary, it is unclaimed territory.

6. **Jawaid & Smith's own theorem numbers.** Not obtained (paywalled, no arXiv version found). Flagged in §1.2 as a concrete remaining verification task.

---

## 7. Feedback on the brief, the framing, and whether this is the right neighborhood

Offered because it was invited, and because two of these change what I would do tonight.

**(a) The optimality/feasibility mismatch is the main thing I would want the author to see.** The requested artifact — "greedy on λ_max or log-det is not *optimal*" — would, if found, **not** settle the stated question. The stated question is whether greedy-on-a-scalar **maintains survival whenever survival is achievable**. A policy can be badly suboptimal in cost and still keep λ_max(Σ) below a threshold; conversely a cost-optimal policy carries no survival guarantee. So "greedy is suboptimal" is *strictly weaker* than what is needed, and importing such a citation would be a subtle overclaim. What the question actually needs is a **feasibility separation**: an instance where survival is achievable by *some* policy and the greedy-scalar policy fails it. Ye et al.'s Theorem 3 (§2.1) is the closest published thing precisely because an *unbounded* ratio, with the blow-up driven by λ₁ → 1, comes near to a feasibility separation — but it is design-time selection and trace. **My suggestion: aim the numerics at a feasibility separation directly (search over instances for "∃π surviving ∧ greedy-scalar dies"), not at a cost-ratio.** That is both the honest target and, I suspect, an easier search, because you get to choose R² adversarially after seeing the two trajectories — a large cost gap is not needed, only a gap that straddles the threshold.

**(b) The framing itself looks sound to me, with one wording caution.** "Whether a scalar functional of I_o(a) — possibly also depending on P_t — could substitute" is well-posed *once the quantifier over policies is fixed*, and the myopic/non-myopic split the author already identified is, I think, the correct axis; §4 is independent evidence from the bandit community that this is where the difficulty actually lives (their Whittle index is exactly a state-dependent non-myopic scalar, and its existence in >1 dimension is open). The caution is on **"necessary."** Per §3.1, the field does not have iff conditions for bounded expected covariance even in the much simpler intermittent-observation setting — necessary and sufficient conditions there are separated by an acknowledged gap. Claiming the matrix condition is *necessary* would be putting weight on something the adjacent literature has not been able to carry. I would expect the defensible claim to be sufficiency + a characterized gap + the §4 open-problem citation for why the scalar-substitution question is not merely unproven but recognized-open. **That is a stronger paper-level position than a necessity claim, not a weaker one** — "this reduces to a recognized open problem in restless-bandit indexability" is a citable, checkable statement, and it locates the paper's contribution honestly.

**(c) On the neighborhood.** Sensor scheduling is the right neighborhood for *hardness and submodularity*, but I think it is the **second**-best neighborhood for the actual question. The best-matched sub-literature is the **Kalman-stability-under-random-measurement-equation** line (§3.1–§3.3), because it studies boundedness (feasibility) under a *distribution over measurement models* — structurally the same object as E_{a~π}[I_o(a)]. Second-best-matched, and entirely absent from the guess-list, is **restless bandits / Whittle indexability** (§4). I would spend the next hour on Marelli et al. (arXiv:1806.08098, full text) and Dance & Silander's supplementary material, not on more of §1–§2.

**(d) On the guess-list.** It held up better than "guesses" implies: Sundaram appears (as Zhang/Ayoub/Sundaram *and* Ye/Roy/Sundaram — the latter carries the harder result), Jawaid & Smith is the real origin of the log-det/λ_max split, Tzoumas and Chamon/Ribeiro are both live and verified, Gupta is the right citation for policy-averaging, Vitus/Tomlin is real (Vitus, Zhang, Abate, Hu, Tomlin, *Automatica* 48(10):2482–2493, 2012, tree-pruning for exact finite-horizon schedules — **[U]** for content, and note Zhao/Zhang/Hu/Abate/Tomlin 2014 is the infinite-horizon companion and the more relevant one). Summers/Lygeros and Krause/Guestrin appear only as placement-literature background here (§1.1 refs [5], [6]) and I would not chase them for this question. Off-list and more interesting, as predicted: **Dance & Silander**, **Mo/Garone/Sinopoli**, **Orihuela et al.**, **Rohr/Marelli/Fu**, **Marelli/Sui/Rohr/Fu**.

**(e) On the brief.** It worked well for me — the "don't confirm what he already has, and if it's wrong that's more valuable" instruction is what made §5 (the periodicity/constant-action tension) something I chased rather than skipped, and the explicit "anything off the list is more interesting" is what got me to the restless-bandit literature, which no keyword on the list would have reached. One thing I would have wanted in the brief and had to infer: **whether "survival" is a hard constraint or a soft objective in the paper's actual formulation.** I assumed hard constraint (λ_max(Σ) < R² as feasibility), and §7(a) — the most consequential thing on this page — depends entirely on that reading being right. If it is actually a cost/penalty formulation, §7(a) weakens substantially and the optimality literature becomes directly relevant after all.

---

## 8. BibTeX-ready summary table

| Key | Cite | Rung | One-line relevance |
|---|---|---|---|
| `dance-silander-2015-kalman-restless-bandits-indexable` | Dance & Silander, NeurIPS 2015, arXiv:1509.04541 | **[V-full]** | Scalar-index-substitutes-for-matrix is proven only in 1-D, conditionally; multidimensional **open**. |
| `ye-roy-sundaram-2018-complexity-approximability-kfss` | Ye, Roy, Sundaram, arXiv:1711.01920 | **[V-full]** | Thm 1 NP-hard (stable A, equal costs); Thm 2 no constant-factor approx; Thm 3 greedy-on-trace ratio unbounded as λ₁→1. |
| `zhang-ayoub-sundaram-2015-sensor-selection-complexity` | Zhang, Ayoub, Sundaram, CDC 2015 (Automatica 78:202–210, 2017) | **[V-full]** | Example 1: explicit 2-state instance breaking sub- *and* super-modularity of trace, log-det, **and λ_max** simultaneously. |
| `chamon-pappas-ribeiro-approx-supermodularity-kalman` | Chamon, Pappas, Ribeiro, arXiv:1912.03799, IEEE TAC | **[V-abs]** | MSE and **worst-case error (λ_max)** not supermodular, but *approximately* so — greedy carries near-(1−1/e) certificates. Cuts against finding a λ_max counterexample. |
| `tzoumas-jadbabaie-pappas-2015-sensor-placement-kalman` | Tzoumas, Jadbabaie, Pappas, arXiv:1509.08146 | **[V-abs]** | log-det of covariance supermodular; MMSE not; MMSE decays only linearly in sensor count. |
| `rohr-marelli-fu-2014-boundedness-expected-covariance` | Rohr, Marelli, Fu, IEEE TAC 59(10), 2014 | **[V-abs]** | Necessary and sufficient conditions for bounded E[Σ] **with an acknowledged gap** — cautions against a necessity claim. |
| `marelli-sui-rohr-fu-random-measurement-equation` | Marelli, Sui, Rohr, Fu, arXiv:1806.08098, Automatica | **[V-abs]** | Stability under **random H and R** = the E_π setting; closest published match. **Full read outstanding.** |
| `mo-garone-sinopoli-2014-infinite-horizon-sensor-scheduling` | Mo, Garone, Sinopoli, SCL 67:65–70, 2014 | **[V-abs]** | Any finite-cost infinite-horizon schedule approximable arbitrarily well by a **periodic** one; lower bound quantifies any schedule's gap. |
| `zhao-zhang-hu-abate-tomlin-2014-infinite-horizon-scheduling` | Zhao, Zhang, Hu, Abate, Tomlin, IEEE TAC 2014, arXiv:1312.0157 | **[V-abs]** | Optimal cost/schedules independent of P₀; periodic approximation arbitrarily close. |
| `orihuela-barreiro-gomezestern-rubio-2014-periodicity` | Orihuela et al., Automatica 50:2672–2676, 2014 | **[U]** | The **greedy Kalman-based scheduler itself** converges to a periodic selection / limit cycle. |
| `gupta-chung-hassibi-murray-2006-stochastic-sensor-selection` | Gupta, Chung, Hassibi, Murray, Automatica 42(2):251–260, 2006 | **[V-2nd]** | Canonical randomized (policy-averaged) selection; **bounds** on E[Σ], not an exact condition. |
| `jawaid-smith-2015-submodularity-sensor-scheduling` | Jawaid & Smith, ACC 2014 pp. 4139–4144; Automatica 61:282–288, 2015 | **[V-2nd]** | Origin of "log-det-of-information submodular (single-step); trace and λ_max neither." **Text unread — no theorem numbers.** |
| `vitus-zhang-abate-hu-tomlin-2012-efficient-sensor-scheduling` | Vitus, Zhang, Abate, Hu, Tomlin, Automatica 48(10):2482–2493, 2012 | **[U]** | Tree-pruning for *exact* finite-horizon optimal schedules — implies greedy≠optimal operationally. |
| `dutta-wilde-smith-2023-unified-sensor-scheduling` | Dutta, Wilde, Smith, arXiv:2304.02692 | **[V-abs]** | MIQP exact solutions for trace-minimizing scheduling/selection; useful as a *numerical oracle* for optimal schedules in the numerics. |

**Note for whoever does the numerics:** `dutta-wilde-smith-2023` (MIQP, "optimal solutions for systems with 30–50 states in seconds") is worth knowing about as an **exact-optimum oracle** to compare greedy against, rather than hand-rolling a DP. That may be the most immediately practical item on this page.

---

## 9. Local resources checked

- `/Users/josephwecker-v2/src/arch/asf/ref/INDEX.md` — grepped for sensor / schedul* / submodular / kalman / greedy. **One hit only** (`levine-2018-rl-control-as-inference`, mentioning Kalman duality in passing — irrelevant here). **The ASF reference index has no sensor-scheduling material.** This neighborhood is virgin territory locally as well as in the paper's bib.
- Paper bib not re-checked (coordinator verified: no sensor-scheduling entries). Duplicate risk confirmed low for every key above.

---

# Appendix A — Follow-up pass (2026-07-29, same session)

*Added after cross-validation with the viability/index-side sweep. Three items: two corrections to §4 that came from the other sweep, then the full read of Marelli et al. that §3.2 flagged as the biggest outstanding item.*

## A.1 Corrections to §4 (Dance & Silander) — from the parallel sweep, **[U] to me, I did not verify these two myself**

The other neighborhood's sweep independently converged on Dance & Silander, which raises confidence that it is the real center of gravity rather than a search-path artifact. Two amendments it supplied, both of which I am recording at **[U]** because I have not fetched either source:

1. **The JMLR journal version discharges assumption A1.** Dance & Silander, "Optimal Policies for Observing Time Series and Related Restless Bandit Problems," *JMLR* 20, art. 35, 2019. Reportedly proves threshold optimality outright, so **scalar indexability is unconditional there**, not conditional as in the NeurIPS 2015 version I read. **My §4 read was of the conditional version — treat §4's "conditional on (A1)" as superseded for the 1-D case.** The counterexamples-to-submodularity remark in the NeurIPS §5 presumably still stands as a statement about *that proof route*, not about the conclusion.
2. **The multidimensional open status is restated much more recently, with Niño-Mora as coauthor.** Hao, Wang, Niño-Mora, Fu, Yang & Pan, arXiv:2312.07858, *Sensors* 24(23):7755. Quoted to me as: "In the more practically relevant case of multi-target tracking RMABP models with multi-dimensional state Kalman filter dynamics, indexability is currently an open problem," and "at present it is unknown whether restless projects with multi-dimensional Kalman filter dynamics such as those above are indexable, even for a single dynamics model."

**Net effect on §4's conclusion: it gets stronger, not weaker.** The 1-D case is *settled affirmatively and unconditionally* (2019), and the multidimensional case is *explicitly declared open as of Dec 2023*. That is a cleaner citable pair than what I had: scalar-index-suffices is a theorem in one dimension and an acknowledged open problem in the dimension the paper needs. Anyone folding this in should fetch both to promote them off **[U]** — the 2312.07858 quote in particular is the kind of load-bearing verbatim that should not travel at second hand.

## A.2 Marelli, Sui, Rohr & Fu (arXiv:1806.08098) — full read **[V-full]**

Fetched the PDF, extracted to text, read the setup, main theorem, remarks, and the assumption-interpretation section. **This paper matters more than anything else in the original sweep, and it does not say what I guessed it would say.**

### A.2.1 The setup is, structurally, exactly the E_π setting

Verbatim from §3: the system is x_{t+1} = A x_t + w_t, y_t = C_t x_t + v_t with v_t ∼ CN(0, R_t), and — the key sentence — "At time t, the pair γ_t = (C_t, R_t) is randomly drawn from the finite set A = C × R, where C = {C^(1), …, C^(D)} and R = {R^(1), …, R^(E)}."

**That is action-conditional observation geometry and action-conditional observation noise, drawn from a policy over a finite action set.** (C_t, R_t) ↔ (H(a), R_o(a)). A is assumed WLOG in Jordan normal form. The draw process γ_t is generated by a hidden Markov model (Eqs. 6–7), and Remark 2 argues this is WLOG for *any* specification of P(γ_t | γ_s, s<t). Assumption 12 requires γ_t **cyclostationary with period τ**, with stationary as the τ=1 special case.

So the covered policy class is: **exogenous, possibly history-dependent, possibly periodic randomized schedules — i.e. precisely the state-independent class.** It does *not* cover closed-loop state-feedback (greedy-on-P_t) policies, because γ_t is generated independently of the filter state. **That boundary is exactly the dividing line the paper cares about**, which makes this the right paper and also bounds what it can be used for.

Incidental but useful: **Assumption 12 has periodicity built into it natively** (cyclostationary with period τ, and the theorem takes max over 0 ≤ t < τ). Independent structural support for §5's flag — this literature's authors built their assumption set around periodic schedules, not constant ones, because periodic is the natural class.

### A.2.2 The stability metric is boundedness of the expected covariance, not a threshold

**Definition 3:** the ANEEC (asymptotic norm of the expected error covariance) is

  G = sup_{P_t ≥ 0} limsup_{t∈Z, T→∞} ‖ E( Ψ(P_t, Γ_{t,T}) ) ‖

where Ψ(P_t, Γ_{t,T}) = ψ_{γ_{t+T−1}} ∘ ⋯ ∘ ψ_{γ_t}(P_t) composes the Riccati maps along the random schedule. Stability = G < ∞.

**This is finiteness, not a threshold.** It is a supremum over initial P_t and a norm of an *expectation*. The paper's survival condition λ_max(Σ) < R² for a *specific finite* R² is strictly stronger and quantitatively different. **So Theorem 14 does not hand over the survival condition.** What it hands over is the sharp characterization of the *feasibility boundary* for the weaker property.

### A.2.3 Theorem 14 — and the reason this changes the framing

**Definition 10:** N_k^{t,T} ≜ {Γ_{t,T} : O_k(Γ_{t,T}) does not have FCR} — the set of length-T action sequences along which the k-th block's observability matrix **fails to have full column rank**.

The system is partitioned (Definitions 5–8) into **finite multiplicative order (FMO) blocks** (A_k, C_k), where by Remark 9 each A_k = α_k Ã_k with Ã_k having unit-modulus diagonal and strictly-upper-triangular remainder — so α_k is the common modulus of that block's eigenvalues, and distinct blocks have |α_k/α_l| not a root of unity.

**Theorem 14 (verbatim structure).** Under Assumptions 12 and 13, with

  Φ_k = max_{0 ≤ t < τ} limsup_{T→∞} P(N_k^{t,T})^{1/T},

- if **|α_k|² Φ_k < 1 for all k ∈ {1,…,K}** then G < ∞;
- if **|α_k|² Φ_k > 1 for some k** then G = ∞.

**Remark 15:** "Notice that Theorem 14 is inconclusive in the case when |α_k|² Φ_k = 1. Trivial gaps of this kind are common in the literature [1,6]." — So the "trivial gap" of §3.1/§3.2 is *only the knife-edge equality*. **This is effectively a necessary-and-sufficient condition**, sharp except on a measure-zero boundary. That is much stronger than the "necessary and *a* sufficient condition" phrasing of the abstract led me to expect in §3.2, and I was wrong to guess it stopped short of an iff.

### A.2.4 What this does to the scalar-vs-matrix question — the substantive finding

**The sharp condition is not a PSD condition on the policy-averaged information matrix. E_π[I_o] does not appear in it at all.**

The condition is **K scalar inequalities, one per spectral (FMO) block**: |α_k|² Φ_k < 1. Each compares (i) the squared modulus of that block's eigenvalues — how fast that eigendirection-cluster diverges — against (ii) Φ_k, the **exponential decay rate of the probability that the schedule leaves that block unobservable over a long window**. It is a large-deviations / rank-event quantity. Three consequences, and they are load-bearing:

1. **The magnitudes of R_o(a) are almost irrelevant to the sharp condition.** Only *which* (C, R) pairs produce full-column-rank observability of each block, and *how often* the schedule avoids them, enters. Since R_t ≥ 0 is finite-valued on a finite set, only rank enters, not conditioning. **So the matrix condition E_π[I_o(a)] ⪰ I_min is sufficient-but-very-far-from-necessary**, and now in a *characterized* way rather than a vague one: it constrains averaged information magnitude where the sharp condition constrains rank-deficiency-event rates against eigenvalue moduli. A schedule can satisfy Theorem 14 with policy-averaged information that is arbitrarily small in PSD order (long unobservable stretches, so long as their probability decays fast enough relative to |α_k|²), and it can fail Theorem 14 while carrying large averaged information (if the information is always in the wrong block).
2. **This is itself a "scalars substitute for the matrix" result — but K scalars indexed by spectral blocks, not one.** The natural reduction of the matrix condition in this problem class is not to a single functional; it is to one scalar per eigendirection-cluster. **That is independent structural corroboration of §5's periodic-not-constant flag from a completely different direction**: the reason periodic schedules matter is that different blocks can be served in turn, and the sharp condition is *per-block*, so a schedule's survival is decided blockwise. A single scalar functional of I_o(a) is aggregating across exactly the axis along which the sharp condition refuses to aggregate. **If I had to name the mechanism a myopic-scalar counterexample should exploit, it is this one:** two spectral blocks with different |α_k|, a scalar objective that aggregates over both, and a threshold that only one blockwise-aware schedule can hold.
3. **For the state-independent policy class, the survival-feasibility question is essentially closed by this paper** (modulo boundedness-vs-threshold, §A.2.2). That is a genuine "the literature already has it" answer for one half of the author's question — and it does *not* have the shape the internal argument assumes.

### A.2.5 What it does **not** do — the honest negatives

- **Does not give a threshold condition.** No route from Theorem 14 to λ_max(Σ) < R² for finite R². The gap between "bounded" and "bounded by R²" is entirely unaddressed, and for a *survival* claim that gap is the whole content. This is the single most important limitation.
- **Does not cover closed-loop policies.** γ_t is exogenous by construction. Nothing here bears on greedy-on-P_t, myopic scalars, or the myopic-vs-non-myopic distinction. **So this paper cannot substitute for tonight's numerics** — it constrains only the state-independent half.
- **Does not establish necessity of any matrix/PSD condition** — it establishes that the sharp condition has a different form entirely, which is stronger and more useful than either "necessary" or "not necessary."
- **Assumptions 12–13 are technical and non-trivial to discharge.** Proposition 18 gives the practical sufficient route (cyclostationary + Gaussian hidden Markov ⇒ both hold), via Lemmas 19–22. Anything citing Theorem 14 should say which route discharges the assumptions for its setting.
- Φ_k is defined as a limsup of a T-th root of a probability — **computable in principle** (they "address its numerical computation," §6–§7 with a worked non-diagonalizable, non-finite-order-Markov example, and Corollary 26 gives a closed product form under a special structure), but it is not a closed-form functional of the C^(d), R^(e).

### A.2.6 Bibliography and lineage **[V-full]** — all read from this paper's own reference list

- `marelli-sui-rohr-fu-2018-random-measurement-equation` — Damián Marelli, Tianju Sui, Eduardo Rohr, Minyue Fu, "Stability of Kalman Filtering with a Random Measurement Equation: Application to Sensor Scheduling with Intermittent Observations," arXiv:1806.08098v2 [cs.SY], 18 Oct 2018. Preprint submitted to *Automatica*. Affiliations: Guangdong Univ. of Technology / CIFASIS-CONICET / Dalian Univ. of Technology / ABB Corporate Research / Univ. of Newcastle.
- Lineage of necessary-and-sufficient results, read from their §1 survey (all **[V-full]** as bibliographic data, **[U]** as to precise theorem content):
  - **[1] Sinopoli, Schenato, Franceschetti, Poolla, Jordan, Sastry**, IEEE TAC 49(9):1453–1464, Sep 2004 — the critical-value result; bounds tight (hence iff) only when C is invertible. **The paper already cites this** (`sinopoli-2004-intermittent-kalman`), which makes the whole §3 line a natural extension of an existing citation rather than a new neighborhood.
  - **[7] Plarre & Bullo** — relaxes invertibility to the observable subspace.
  - **[8] Mo & Sinopoli**, "A characterization of the critical value…" — case where unstable eigenvalues of A have *different magnitudes*. (Note: distinct-moduli is exactly the FMO-block structure that Theorem 14 generalizes — and exactly the structure my §A.2.4 point 2 suggests a counterexample should exploit.)
  - **[6] Mo & Sinopoli**, "Kalman filtering with intermittent observations: Tail distribution and critical value," IEEE TAC 57(3):677–689, Mar 2012 — necessary and sufficient for "non-degenerate" systems; generalizes most Gilbert-Elliott-model iff conditions.
  - **[4] You, Fu & Xie**, "Mean square stability for Kalman filtering with Markovian packet losses," *Automatica* 47(12):2647–2657, 2011 — iff for second-order systems.
  - **[3] Huang & Dey**, *Automatica* 43(4):598–607, 2007 — peak-covariance criterion, sufficient; also necessary for scalar systems.
  - **[5] L. Xie**, IEEE TAC 53(7):1759–1764, 2008 — peak covariance; sufficient, also necessary when C has full column rank.
  - **[2] L. Xie**, SIAM J. Control Optim. 50(1):532–558, 2012 — stochastic comparison / weak convergence / ergodicity for the random Riccati equation with Markovian binary switching.
  - **[23]** (their direct predecessor, the FSMC-model result they generalize) = Rohr, Marelli & Fu 2014, my §3.1.
  - **[25] Gupta et al. 2006** — cited by them exactly as I characterized it in §3.3 ("derived the optimal probability distribution for selecting sensors at each sample time"). **[V-full]** confirmation of §3.3's content characterization, which had been **[U]**.
  - Also named in their §1: **[26] Shi, Cheng & Chen**, "Sensor data scheduling…" — including, verbatim from their summary, a scheme for the limited-computation case that "guarantees that the MSE remains within certain prescribed level," and **[27] Shi, Cheng & Chen**, "Optimal periodic sensor scheduling…". **The [26] item is the only thing I have encountered in this entire sweep that is framed as maintaining a covariance metric below a prescribed threshold — i.e. the constraint/survival framing that §6.4 recorded as absent. It is a lead worth 20 minutes and it partially retracts §6.4.** I have not read it; **[U]** as to content.

## A.3 Answers to the two smaller questions

**(a) Pang & Shan 2019** (IEEE Sensors J. 19(18):8224–8232), cited for "in general, myopic scheduling policies exhibit inevitable performance degradation in the long run." **I did not fetch it — [U].** But I'd offer a prior, from the shape of the sweep: I expect that to be a motivational remark rather than a theorem, for the same reason as §2.2. Across everything I verified, *every* rigorous negative statement about greedy in this literature is either (i) a non-submodularity counterexample (which is not a suboptimality result), (ii) a suboptimality-*ratio* result in the design-time selection problem (Ye et al. Thm 3), or (iii) an approximate-supermodularity certificate pointing the *other* way. Nobody has a theorem of the form "myopic scheduling degrades in the long run" — and given §1.4, I don't think one can be true in that generality. So I'd treat the Pang & Shan line as citable-as-motivation-only unless someone reads it and finds otherwise. Worth ten minutes for whoever merges, not worth displacing anything.

**(b) The hard-constraint reading.** Thank you for confirming — that was the assumption §7(a) rested on, and with survival as a viability condition rather than a penalty, **§7(a) stands as written and is if anything strengthened by §A.2**. Theorem 14 characterizes the feasibility boundary for *boundedness* under state-independent schedules, and the paper's survival condition is a *threshold* refinement of that boundary. So the natural shape of the paper's contribution becomes clearer: the field has the boundedness-feasibility boundary sharply (for exogenous schedules, blockwise, non-PSD in form) and has *nothing* on the threshold refinement or on closed-loop policies. That is a well-located contribution, and it is a better story than a necessity claim would have been.

## A.4 Revised bottom line for the merged document

1. **Scalar-index-suffices is settled in 1-D (JMLR 2019) and explicitly open in multiple dimensions as of Dec 2023** (§A.1). Cite as an open problem, do not attempt to cite it as a theorem.
2. **For state-independent/exogenous schedules, the sharp survival-feasibility condition is already published and is *not* a PSD condition on averaged information** — it is K blockwise scalar inequalities |α_k|² Φ_k < 1 comparing eigenvalue moduli against rank-deficiency-event decay rates (§A.2.4). Whatever the internal proof concludes about state-independent scalars should be checked against this, because this is a *sharp* result in that class and its form is not the assumed one.
3. **The remaining genuinely-unoccupied territory is: (i) the threshold refinement (bounded-by-R² rather than bounded), and (ii) closed-loop/myopic policies.** Tonight's numerics live entirely in (ii) and are not made redundant by anything I found.
4. **If I were designing the counterexample search now, I would use §A.2.4 point 2 as the generator:** two FMO blocks with distinct eigenvalue moduli, and a myopic scalar that aggregates across blocks (trace and log-det both do; λ_max does so only through the max, which is why λ_max may be the *hardest* of the four to defeat). Cross-check with Mo & Sinopoli [8] (distinct-magnitude unstable eigenvalues), which is where that structure is studied directly.
5. **One partial retraction:** §6.4 claimed nobody in this literature treats a covariance metric as a constraint to be maintained. Shi, Cheng & Chen (Marelli et al.'s [26]) reportedly give a scheme guaranteeing MSE "remains within certain prescribed level." Unverified, but §6.4 should be read as *nearly* absent rather than absent.
