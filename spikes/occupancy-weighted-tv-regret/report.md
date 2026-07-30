> **Provenance of this file.** The spike agent was blocked by harness policy from writing `report.md` itself (the same block hit the information-bound spike the same evening). This document is the agent's own text, returned on request and persisted verbatim by the parent — no edits to substance. The agent's inline `[first-hand]` / `[recon]` / `[unverified-by-either]` / `[composition, unverified]` markings are preserved deliberately; it asked specifically that the markings in §3c and §10 survive any future edit, because those are the two places a reader could mistake recon-provenance for first-hand. Please honor that.
>
> **Parent verification:** the parent independently verified only the App D quotation and the UCRL2/Azar attribution discussed in §6a — see `PARENT-VERIFICATION.md` in this directory, which also records a detail sharper than the report's own account. Every other first-hand claim here is the agent's read, not the parent's. §3c is verified by nobody.

---

# Occupancy-weighted TV regret for optimistic learners — does (A5)'s √L condition hold?

*Spike, 2026-07-29. Umbrella-level because the question is about optimistic tabular learners generally; the immediate consumer is `02-unified-convergence-rl` — (A5), App D, and conclusion (v).*

**Rung tags** on every statement: **[proved]** / **[verified-against-PDF]** / **[numerically tested]** / **[hypothesis]** / **[pattern]** / **[guess]**.

**Provenance tags**, kept separate from rungs because they are a different axis:
- **[first-hand]** — I opened the PDF and read the statement in this session.
- **[recon]** — a literature-reconnaissance sub-agent opened and read it; I did not. Reported with its own account of what it read verbatim vs. grepped.
- **[unverified-by-either]** — named because it matters, read by neither.
- **[composition, unverified]** — assembled from verified pieces by someone; the assembly itself has not been checked. Flagged individually.

---

## 0. Bottom line

Four findings, in increasing order of consequence.

**1. (A5)'s constant is wrong, and not repairable by a better constant.** **[proved]** No `Δ_min`-free `c` exists — for any algorithm and any candidate `c` there is an instance satisfying every hypothesis of Theorem 4.1 with `Σ E[TV̄_t] > 2c√L`. App D's "`c` of order `Õ(√(N_h SA))`" (submitted PDF p. 22) is false as stated.

**2. The intended repair works and the `1/Δ_min` is tight.** **[proved]** (A5) holds for UCBVI-CH with `c = Õ(√(N_h SA))/Δ_min`, and a matching lower bound gives `c ≳ √A/(N_h Δ_min)`. The `1/Δ_min` is the truth of the object, not a lossy-conversion artifact. The guess in `response-prep/math/K-03-A5-base-learner.md` is confirmed in full, including that the honest constant carries `1/Δ_min` and that conclusion (v) should display it.

**3. But the repaired hypothesis is still the wrong one, because the TV detour is a round trip.** **[proved]** (v) divides value regret by `Δ_min N_h` and multiplies back by `V_max N_h`. Since `V_max ≥ Δ_min` by the paper's own definitions, (v) is **strictly weaker** than the three-line direct argument (Azar's bound per restarted block + Cauchy–Schwarz across blocks), which needs no gap assumption at all.

**4. There is a strictly stronger replacement, and it is already the literature's canonical object.** **[proved]** + **[verified-against-PDF, recon]** The right coordinate is the *gap-weighted* occupancy sum, which is the Tirinzoni / Simchowitz–Jamieson exact gap-visitation decomposition. With it the composition loses both the `V_max` and the `1/Δ_min` and needs no gap hypothesis.

**And the plain statement asked for:** *the paper's headline rate needs a stated `Δ_min` (or `Γ_min`) dependence that it currently lacks.* Conclusion (v) as displayed — `2c V_max N_h √((B_T+1)T)` with a `Δ_min`-free `c` — is not a theorem about UCBVI/UCRL2. Either the rate term acquires an explicit `1/Δ_min`, or the hypothesis is replaced (§7) so that no gap dependence is needed. Those are the only two honest options; a `Δ_min`-free `c` with a gap-free-looking rate is not one of them.

Three citation/arithmetic defects surfaced on the way (§6), and one live hazard that contradicts something a rewrite would be tempted to assert (§6d).

---

## 1. What the condition reduces to (an exact identity)

Notation as in the paper: episodic MDP, horizon `N_h = H`, learner policy `Q_t`, deterministic optimum `π*_t = δ_{a*}`, `d_h^{Q_t}` the learner's occupancy at step `h`.

**[proved]** The performance-difference lemma in the paper's own Step 1 form (§A `A-proof-of-composition.md`; the identity is standard and the paper states it correctly), with `π' = π*`, `π = Q_t`:

```
V^{π*}_t(s_0) − V^{Q_t}_t(s_0)
  = Σ_{h<H} E_{s_h ~ d_h^{Q_t}} [ Σ_a Q_t(a|s_h)·( Q*_h(s_h,a*(s_h)) − Q*_h(s_h,a) ) ]
  = Σ_{h<H} E_{s_h ~ d_h^{Q_t}} [ Σ_{a≠a*} Q_t(a|s_h)·Δ_h(s_h,a) ]                    (†)
```

`Δ_h(s,a) := Q*_h(s,a*(s)) − Q*_h(s,a) ≥ 0`. This is an **equality**. Everything below is bookkeeping on (†).

Since `TV(δ_{a*}, Q_t(·|s)) = 1 − Q_t(a*|s) = Σ_{a≠a*} Q_t(a|s)`, (†) sandwiches immediately:

```
Δ_min · N_h · TV̄_t   ≤   V^{π*}_t − V^{Q_t}_t   ≤   V_max · N_h · TV̄_t              (‡)
```

`Δ_min := min_{h,s,a≠a*} Δ_h(s,a)`. The right half is the paper's Step 1, used to convert TV into value regret. **The left half is the one (A5) needs, and it is used nowhere in the proof of (v)** — it exists in the paper, as §C `sec-aux-action-gap` ("Action-gap matching lower bound"), stated per-state and never composed with the occupancy aggregation. The material for the repair is already in the manuscript.

**The identity is the field's, under a name.** **[verified-against-PDF, recon]** Tirinzoni–Pirotta–Lazaric, *A Fully Problem-Dependent Regret Lower Bound for Finite-Horizon MDPs* (arXiv 2106.13013v1), **Proposition 4** (Gap-based regret decomposition), stated for *any* learning algorithm `A` and *any* MDP `M`, no hypotheses:

```
E^A_M[Regret_K(M)] = Σ_{s∈S} Σ_{a∈A} Σ_{h∈[H]} E^A_M[N_{K,h}(s,a)] · Δ_{M,h}(s,a)
```

and Simchowitz–Jamieson (arXiv 1905.03814v2) give the per-episode occupancy form as an exact identity (§3, unnumbered display immediately before "The Clipping Trick"): `V*₀ − V^{π_k}₀ = Σ_{x,a} Σ_h ω_{k,h}(x,a)·gap_h(x,a)`, with `ω` the learner's **own** occupancy. Both read verbatim by the recon agent.

**Consequence worth carrying into the rewrite. [proved]** Our object is the *left factor* of that sum restricted to `a ≠ π*_h(s)`:

```
Σ_{t≤L} E[TV̄_t] = (1/N_h) Σ_h Σ_s Σ_{a≠π*_h(s)} E[N_{L,h}(s,a)]
```

i.e. **cumulative suboptimal-action visitation count**, normalized by `N_h`. The field's name for it is just `N_{K,h}(s,a)` on the non-`π*` action set. Stated that way it inherits the whole gap-dependent apparatus; stated as an occupancy-weighted TV it reads as distribution matching and will be misread as such.

**[proved] Upper bound.** **[verified-against-PDF, first-hand]** Azar–Osband–Munos 2017 (`arxiv.org/pdf/1703.05449v2`), **Theorem 1** (UCBVI-CH): `Regret(K) ≤ 20 H^{3/2} L √(SAK) + 250 H²S²A L²`, `L = ln(5HSAT/δ)`, with `Regret(K) = Σ_k V*_1(x_{k,1}) − V^{π_k}_1(x_{k,1})`; `Õ(H√(SAT))` for `T ≥ HS³A`, `SA ≥ H`. Dividing (‡)-left through:

```
Σ_{t≤L} E[TV̄_t]  ≤  (1/(Δ_min·H)) · Õ(H^{3/2}√(SAL))  =  Õ(√(N_h S A)) · √L / Δ_min
```

**[proved] What App D actually did.** Its constant `Õ(√(N_h SA))` is exactly `Õ(N_h^{3/2}√(SA))` divided by `N_h` — i.e. Step 1's inequality read in the **reverse** direction (`regret ≤ V_max N_h TV̄` bounds `TV̄` from *below*, not above). The exponents match to the digit under that division, which is why I take this to be the actual provenance rather than an omitted-`Δ_min` typo: the derivation performed was the invalid one, not the valid one with a factor dropped. This is the sharp form of the reviewer's objection (§8).

---

## 2. Why the repaired version still shouldn't be the hypothesis

**[proved]** Chain the repaired (A5) back through the proof of (v). Step 3 gives `Σ_t E[TV̄_t] ≤ 2c√((B_T+1)T)`; Step 1 multiplies by `V_max N_h`. With §1's `c`:

```
E[DynReg(T)]  ≤  (V_max/Δ_min) · [ base learner's blockwise-aggregated value regret ]  +  bias
```

`V_max/Δ_min ≥ 1` always (`Δ_min ≤ V_max` by the definitions in §3 Preliminaries). The direct argument — apply Azar Theorem 1 within each restarted block to `Σ_{t∈block}(V*_t − V^{Q_t}_t)` and Cauchy–Schwarz across blocks — gives

```
E[DynReg(T)]  ≤  Õ(N_h^{3/2}√(SA(B_T+1)T))  +  bias
```

with **no gap assumption and no `V_max/Δ_min` factor**. The TV route, even correctly executed, yields a strictly weaker bound than three lines that skip it. The `√((B_T+1)T)` aggregation is doing all the work, and it is Cauchy–Schwarz over the base learner's *own* guarantee — the restart-on-change construction (Jaksch et al. §7 / Cheung–Simchi-Levi–Zhu), not something the identity coordinate supplies.

This is the finding I would most want surfaced in the rewrite, because it is not a defect in a constant: it says (A5) is the wrong hypothesis for the job it was given. **The identity coordinate's genuine contributions — (i)'s two-sided per-round characterization, (iii)'s computability from `Q_t`, the exactness-vs-Pinsker/BH comparison — are all *per-round* and survive untouched.** Only the load-bearing role in the *cumulative* rate does not.

---

## 3. The no-go: no `Δ_min`-free constant exists

### 3a. Structural form (cleanest; needs no construction)

**[proved from a verified identity]** **[verified-against-PDF, recon]** Tirinzoni Proposition 4 shows value regret is **exactly blind** to the zero-gap set: pairs with `Δ_h(s,a) = 0` contribute nothing to the left-hand side while contributing fully to `TV̄`. Therefore **no value-regret bound of any kind, for any algorithm, can control `TV̄` there.** This is the cleanest statement of "no `Δ_min`-free `c`" available and it is a two-line consequence of a published identity.

Caveat the recon agent raises and I endorse: the pure-tie version (two Bellman-optimal actions, `Δ = 0`, `TV̄ = Θ(1)` at zero regret) is sharp but is a *tie-breaking artifact*, and a referee kills it by quantifying `π*` existentially (infimum over the optimal-policy set). So the tie should not be the load-bearing no-go. The construction below is the version that survives that repair, and it is the better result.

### 3b. Constructive form, positive gaps throughout

**[proved, first-hand]** Witness: `S = {s0,s1,s2}`, `A = 2` at `s0` (one action elsewhere), `H = 2`, start `s0`; action 0 → `s1` (Bernoulli mean `0.5 + Δ/2`), action 1 → `s2` (mean `0.5 − Δ/2`). Then `Q*_0(s0,0) − Q*_0(s0,1) = Δ` exactly, `π*` deterministic and unique, `Δ_min = Δ > 0`, stationary (`B_T = 0`), rewards in `[0,1]` — every hypothesis of Theorem 4.1 holds. Occupancy is a point mass at `s0` at `h = 0` and no misranking is possible at `s1,s2`, so

```
TV̄_t = (1/H)·1[ greedy_t(s0) ≠ 0 ],     Σ_{t≤L} E[TV̄_t] = (1/H)·E[N_sub(L)].
```

**[verified-against-PDF, first-hand]** Lattimore–Szepesvári, *Bandit Algorithms* (`refs/pdfs/lattimore-2020-bandit.pdf`), **Theorem 15.2** ("for any policy `π` there exists `µ ∈ [0,1]^k` with `R_n(π,ν_µ) ≥ (1/27)√((k−1)n)`") and the sharper two-point form at **Eq. (15.3)** (`inf_π sup_ν R_n ≥ (nΔ/8)·exp(−D(P_µ,P_µ'))`). Taking `Δ = L^{−1/2}` makes the KL term `O(1)`, so `sup_ν R_L = Ω(LΔ)` and `E[N_sub(L)] = R_L/Δ = Ω(L)`. Hence

```
Σ_{t≤L} E[TV̄_t] = Ω(L/H) = Ω(√L/H)·√L      →  the required c grows like √L.
```

**No `Δ_min`-free `c` exists, for any algorithm.** Run at general `Δ` the same computation gives `c ≳ √A/(H·Δ_min)`, so §1's `c = Õ(√(N_h SA))/Δ_min` is **tight in its `Δ_min` dependence**.

### 3c. MDP-native version of the same no-go — not in the literature, one line from verified pieces

**[composition, unverified-by-me]** The recon agent reports **Domingues–Ménard–Kaufmann–Valko (arXiv 2010.03531) Theorem 9** (for any algorithm there is a stage-dependent-transition MDP with `R_T ≥ √(H³SAT)/(48√6)` for `T ≥ HSA`), and that its proof contains at **Eq. (8)** an exact identity on the hard class:

```
R_T(π, M_{(h*,ℓ*,a*)}) = T(H̄ − H − d)·ε·( 1 − E[N^T_{(h*,ℓ*,a*)}]/T )
```

i.e. regret `= c·H·ε·(cumulative misranking mass at the single decision point)` — exactly our object. Substituting their own optimized `ε = (1/(2√2))√(HLA/T)(1 − 1/(HLA))` (which the agent reports verifying, "Optimizing ε and choosing H̄") gives **cumulative misranking mass `≍ T` with `O(√T)` regret and strictly positive gaps** — an MDP-native no-go, tight against Simchowitz–Jamieson Corollary 2.1, surviving the existential-`π*` repair.

**Explicit caveat, to survive into any future quotation of this file: the two ingredient statements were read by the recon agent, not by me, and the composition is the recon agent's, not mine. Neither the substitution nor Eq. (8)'s exact form has been checked by me. Do not cite this without opening 2010.03531 and re-deriving it.** As far as the recon could determine, nobody has published this composition, so if it holds it is ours to state — which is precisely why it needs first-hand verification before it appears in a paper.

### 3d. Numerics

**[numerically tested, first-hand]** `gap_scaling.py` in this directory: 24 seeds, UCBVI-CH's own `H√(2 log L/n)` bonus, on the §3b witness.

`Δ = L^{−1/2}`:

| L | Δ | Σ E[TV̄] | Σ/√L | Σ/L |
|---|---|---|---|---|
| 100 | 0.100 | 21.9 | 2.19 | 0.219 |
| 400 | 0.050 | 89.2 | 4.46 | 0.223 |
| 1 600 | 0.025 | 375.2 | 9.38 | 0.234 |
| 6 400 | 0.0125 | 1 473.0 | 18.41 | 0.230 |
| 25 600 | 0.00625 | 5 986.7 | 37.42 | 0.234 |
| 102 400 | 0.003125 | 24 319.7 | 76.00 | 0.238 |

`Σ/√L` doubles for every 4× in `L` (grows as `√L`); `Σ/L` is flat at ≈ 0.23. **The exponent is 1, not 1/2.** At fixed `Δ = 0.3`: `Σ/√L` = 1.74 → 2.50 → 2.90 → 2.70 → 1.95 → 1.33 across the same grid — rising then falling, consistent with `log L`, i.e. (A5) satisfied with room. At fixed `Δ = 0.05`: 2.4 → 21.1, still climbing; crossover at `L ≈ 1/Δ²` as expected.

**[proved + numerically tested]** So the honest shape is

```
Σ_{t≤L} E[TV̄_t] = Θ̃( min{ L , log L / Δ_min² } )   per block.
```

**`√L` is never the right exponent for this object** — it is linear below the identification threshold `1/Δ_min²` and logarithmic above it. `≤ 2c√L` is satisfiable only by hiding the entire `Δ_min` dependence in `c`, which is what happened.

**Reframing worth adopting (recon agent's phrasing, and I agree):** the honest reading of (A5) is **not a rate claim** but a *uniform envelope over the instance class `{Δ_min ≳ L^{−1/2}}`*; the `√L` exponent is a crossover artifact of where `Δ_min` is allowed to shrink with `L`. Saying that explicitly costs nothing and makes the hypothesis simultaneously weaker-looking and more clearly true.

---

## 4. The other direction: in the gap regime the condition holds in a strictly stronger form

**[verified-against-PDF, first-hand]** Jaksch–Ortner–Auer 2010 (`jmlr.org/papers/volume11/jaksch10a/jaksch10a.pdf`) **Theorem 4**: gap-dependent logarithmic regret for UCRL2, `≤ 34²D²S²A log(T/δ)/ε + εT`, tuned via the gain gap `g`. **Theorem 11** bounds `L_ε(T)`, *the number of steps taken in ε-bad episodes* — the closest thing in a primary source I opened to a direct misranking-count bound for an optimistic MDP learner, and exactly (A5)'s shape.

**[verified-against-PDF, recon]** Better, because it is the *named* algorithm: Tirinzoni et al. **Theorem 2** — for **UCBVI with Chernoff–Hoeffding bonus**, rewards in `[0,1]`, deterministic initial state,

```
E_M[Regret(K)] ≲ (4 H⁴ S A / Γ_min) · log(4 S A H K²)
```

scaling with the minimum **policy** gap `Γ_min := min_{π∉Π*}(V* − V^π)`, not the action gap. The recon agent read the proof: it runs on "the regret at each episode is either zero or at least `Γ_min`", hence `#{k : π_k suboptimal} ≤ Regret/Γ_min`. Also **Simchowitz–Jamieson Corollary 2.1** (p. 6) for **StrongEuler** — note *not* UCBVI; they say other optimistic algorithms enjoy similar bounds but analyze only StrongEuler for the sharpest `H`.

**[verified-against-PDF, recon; composition mine]** Composed with Proposition 4, either gives

```
Σ_{t≤L} E[TV̄_t] = O( poly(S,A,H) · log L / Δ_min² )   —  polylogarithmic in L.
```

So `2c√L` is implied with enormous room whenever `Δ_min` is instance-constant.

**[pattern]** This is the trade Joseph flagged: under a uniform gap one gets `log L`, not `√L`. The honest gap-regime hypothesis aggregates **additively** across blocks, not by Cauchy–Schwarz, giving `O((B_T+1)·log(T/(B_T+1))/Δ_min²)`. **That is the same form the paper already states for the bandit case** (§A Bandit-case sharpening; §D(a)), derived there from Lattimore–Szepesvári Theorem 7.1. The MDP case never received the same treatment: the `Δ_min²` correction was applied to the bandit paragraph on 2026-05-07 (LOG, Batch 4) and the adjacent MDP sentence was left alone. The asymmetry is visible in the source.

---

## 5. If (A5) is kept, the hypothesis it actually needs

**[proved]** Stated honestly:

> Let the MDP be stationary and episodic with horizon `N_h`, rewards in `[0,1]`, and suppose the **Bellman-convention** action gap is uniformly positive: `Δ_min := min_{h, s reachable, a≠a*_h(s)} ( Q*_h(s,a*_h(s)) − Q*_h(s,a) ) > 0`, `Q*` the optimal `Q`-function of the *true* MDP. Then UCBVI-CH restarted at each block boundary satisfies `Σ_{t≤L} E[TV̄_t] ≤ c√L` with `c = Õ(√(N_h S A))/Δ_min`, and no `Δ_min`-free `c` is possible.

Three things there are stronger than Theorem 4.1's current preamble, and each should be surfaced:

- **`Δ_min` is the wrong `Δ_min`. [proved]** §3 Preliminaries defines `Δ(a) := Q_O(a*) − Q_O(a)` under the **C1 one-step-improvement** convention (`π_cont = π_current`, §C `sec-aux-conventions`), i.e. gaps of `Q^{Q_t}`. (†) requires gaps of `Q^{π*} = Q*`, the **C3 / Bellman** convention. §C's monotonicity proposition says these differ. The theorem's `Δ_min > 0` as currently read does not supply what the proof needs.
- **It must hold uniformly over `(h,s)`, not per round.** "for each round `t` a deterministic optimum policy `π*_t = δ_{a*_t}` with action gap `Δ_min > 0`" must be read as uniform over the reachable set — materially stronger, since one nearly-tied state anywhere destroys it.
- **The `V_max/Δ_min` loss must be displayed in (v)**, as the bandit paragraph already displays its `Δ_min²`.

**[proved] Consequent correction to (v).** With the honest constant, `2c V_max N_h √((B_T+1)T) = Õ(V_max N_h √(N_h SA)/Δ_min)·√((B_T+1)T) = Õ(N_h^{5/2}√(SA)/Δ_min)·√((B_T+1)T)` at `V_max ≤ N_h`. The displayed `Õ(N_h²√(SA(B_T+1)T))` is neither this nor the round-trip value (§6b).

---

## 6. Citation, arithmetic, and hazard findings

### 6a. The App D rate is not UCRL2's **[verified-against-PDF, first-hand]**

App D: *"UCRL2 [auer-2010-nearoptimal] and UCBVI [azar-2017-minimax] give per-block cumulative trajectory-level regret `Õ(N_h^{3/2}√(SAL))`."* Azar **Theorem 1** gives exactly that — correct for UCBVI-CH. But Jaksch–Ortner–Auer **Theorem 2** reads `∆(M, UCRL2, s, T) ≤ 34 · D S √(A T log(T/δ))`: `S` **linear** not `√S`, prefactor the **diameter `D`** not `N_h^{3/2}`, and it is *undiscounted average-reward infinite-horizon* regret against `ρ*T` on a **communicating** MDP, not an episodic `Σ_k(V*_1 − V^{π_k}_1)`. UCRL2 has no episodic horizon `N_h`, so `TV̄_t` (defined via `d_h^{Q_t}`, `h < N_h`) is not well-typed for it without a translation the paper does not give.

Recommend: attribute the rate to UCBVI-CH alone; either drop UCRL2 from the (A5) instantiation or state the episodic-translation step. **This is the second cited-rate defect in this paper** (cf. the Mao `(SA)^{1/3}` correction, LOG 2026-05-07). Same mechanism both times: the surrounding math does not depend on the prefactor, so the error survives re-reads.

### 6b. The `N_h²` exponent is not reproducible **[proved]**

From the paper's own pieces, `2c·V_max·N_h` with `c = Õ(√(N_h SA))` gives `N_h^{3/2}√(SA)` if `V_max = O(1)` — which is just the round trip back to Azar's bound, an independent confirmation of §2's circularity — and `N_h^{5/2}√(SA)` if `V_max ≤ N_h` (the paper's own definition). Neither is `N_h²`. Whichever convention is intended, the displayed rate needs recomputing.

### 6c. (A5') inherits the same problem **[verified-against-PDF, first-hand]**

Wei–Luo 2021 (`refs/pdfs/wei-luo-2021-blackbox.pdf`) **Assumption 1** requires the base learner to output `f̃_t ∈ [0,1]` with `f̃_t ≥ min_{τ≤t} f*_τ − ∆_{[1,t]}` and `(1/t)Σ_τ(f̃_τ − R_τ) ≤ ρ(t) + ∆_{[1,t]}` — an **optimistic estimate of the optimal expected reward** plus a bound on cumulative **value** regret, with the nonstationarity measure `∆` also reward-based. There is no TV analogue of `f̃_t`: the optimal TV is identically 0 and TV is not a received reward. So (A5')'s phrasing — *"giving stationary regret `Σ_{t∈W} E[TV̄_t] ≤ 2c√|W|` within each MASTER-selected window"* — mis-states what MASTER delivers. MASTER's guarantee is on value regret within windows; the TV form again follows only via the `Δ_min` conversion.

**The BoBW remark is fine — it is fine about the wrong quantity.** Under §7's reframing the defect disappears by itself: `TV̄^Δ` *is* value regret, and `C(t) = Õ(N_h^{3/2}√(SAt))` is exactly the object Assumption 1 wants. Reframing repairs it verbatim.

### 6d. Live hazard: UCRL2/UCBVI provably do **not** converge in policy space **[verified-against-PDF, recon]**

**This is the item I would least want lost.** Dann, Lattimore & Brunskill (arXiv 1703.07710v3, *Uniform-PAC*), §3, quoted verbatim by the recon agent:

> *"Existing algorithms with uniform high-probability regret bounds such as UCRL2 or UCBVI also do not satisfy uniform-PAC bounds since they use upper confidence bounds with width √(log T / n)… The presence of log(T) causes the algorithm to try each action in each state infinitely often."*

(Their Theorem 3(a) is the positive side: a Uniform-PAC algorithm with `F = Õ(C₁/ε + C₂/ε²)` converges to optimal policies w.h.p., `P(lim Δ_k = 0) ≥ 1−δ`.)

**So for the exact algorithm class (A5) names, last-iterate policy-space convergence fails: `TV̄_t` does not go to zero.** The *summed* claim is unaffected — a sublinear sum with infinitely many nonzero terms is perfectly consistent, and the Cesàro tracking corollary is an average-value statement, so nothing currently in the paper is falsified by this. But **any sentence a rewrite is tempted to add about the identity coordinate converging, or the agent's policy converging to `π*`, for UCRL2/UCBVI is false and citably so.** The field's constructive answer to "is policy-space convergence achievable at all": yes, but by finite-LIL-bonus algorithms (UBEV) and elimination-style algorithms, not by log-`T`-bonus optimism. If the framework wants a convergence statement, the base-learner list has to change.

Independent shape-check on the constant, same neighborhood: **[verified-against-PDF, recon]** Liu, Li, Wang & Yang, *Uniform Last-Iterate Guarantee for Bandits and RL* (NeurIPS 2024), **Theorem 2.6** — any bandit algorithm achieving ULI has an instance forcing `F_ULI(δ,t) = Ω(t^{−1/2})`, and `Σ_{t≤L} t^{−1/2} = Θ(√L)`, a pleasing confirmation that `√L` is the right *shape* for a summed per-round policy-space quantity even though it is the wrong *exponent* for ours in the gap regime. Hazard to have in hand: that paper's abstract says "optimistic algorithms cannot achieve near-optimal ULI guarantee," which reads like a counterexample; its **Theorem 3.3** is far narrower — lil'UCB specifically, two-armed, deterministic rewards, gap `Δ ∈ (0,α)` — and degrades an *exponent* (`t^{−1/2}` → `t^{−1/4}`, which sums to `Θ(L^{3/4})`) rather than showing non-convergence. Not a counterexample to anything here, but the most citable-sounding sentence in the literature that resembles one.

---

## 7. Recommended replacement — the strengthening

**[proved]** Replace (A5)'s coordinate with the **gap-weighted occupancy sum**, i.e. adopt the Tirinzoni / Simchowitz–Jamieson decomposition as the framework's coordinate:

```
TV̄^Δ_t := (1/N_h) Σ_{h<N_h} E_{s_h ~ d_h^{Q_t}} [ Σ_{a≠a*_h(s_h)} Q_t(a|s_h) · Δ_h(s_h,a) ]
```

> **(A5v)** Within each restarted stationary interval of length `L`, the base learner satisfies `Σ_{t≤L} E[TV̄^Δ_t] ≤ c_V √L`.

Then, all **[proved]**:

- `N_h · TV̄^Δ_t = V^{π*}_t − V^{Q_t}_t` **exactly**, by (†). (A5v) is *literally* the base learner's stationary regret guarantee written in occupancy-weighted policy-space form. Steps 1–2 of the proof of (v) collapse into an identity; Step 3 (block Cauchy–Schwarz) and Step 4 (misidentification penalty) are untouched.
- UCBVI-CH satisfies (A5v) with `c_V = Õ(√(N_h S A))` (Azar Theorem 1 divided by `N_h`), **with no gap assumption**.
- Conclusion (v) becomes `E[DynReg(T)] ≤ Õ(N_h^{3/2}√(SA(B_T+1)T)) + V_max N_h (1−p_id) T` — no `V_max` prefactor on the rate term, no `1/Δ_min`, no gap hypothesis. Strictly stronger than the current claim on all three counts.
- **Component 2 is not demoted; it is relocated to where it is true.** The two-sided bound (i) *is* the sandwich `Δ_min·TV̄_t ≤ TV̄^Δ_t ≤ V_max·TV̄_t`. The paper's real asset is that the **unweighted** coordinate is computable from `Q_t` alone (`1 − Q_t(a*|s) = 1 − e^{−K_t(s)}`) while the gap-weighted one needs the gaps; (i) is exactly what licenses reading the computable one as a proxy for the rate-bearing one, and `Δ_min/V_max`-Lipschitz-equivalence is the honest price. That is a better story than "(A5) is the input to the rate," and it is the story the math supports.
- (A5') / MASTER then applies verbatim (§6c).

**Adopt, don't invent.** Since Proposition 4 states this decomposition for any algorithm and any MDP, (A5v) should be presented as adopting a known exact identity, not as a new coordinate. That is both more honest and rhetorically stronger.

---

## 7b. Which of the three would I build on — the opinion asked for

**Not (A5).** It is false as stated, and even repaired it produces a strictly weaker result than the argument it replaces (§2). There is no version of (A5) worth carrying.

**(A5v) is what I would build the composition result on today.** It is exact, gap-free, satisfied by the named algorithm with a verified theorem, it makes (v) strictly stronger on three counts, it repairs (A5') for free, and it preserves every genuine contribution of Component 2 by relocating the identity to the per-round diagnostic role where it is true. It is the safe, honest, better result and it is available now. If the paper must be rewritten to a deadline, this is the one.

**But the `Γ_min` policy-gap version is the more interesting paper, and I would spike it before freezing (A5v).** Tirinzoni Theorem 2's proof shape — "regret at each episode is either zero or at least `Γ_min`", hence `#{suboptimal episodes} ≤ Regret/Γ_min` — is a *policy*-level argument, and `Γ_min` is a **single scalar per instance** rather than a uniform-over-reachable-states condition. That is a materially weaker hypothesis than `Δ_min > 0` uniformly, which is the hypothesis I'd most expect a referee to attack (§5, second bullet). Whether the occupancy-weighted misranking object admits a `Γ_min` bound is, as far as the recon could determine, **open**. Two reasons it is worth an attempt rather than a mention:

1. It would be a *result* rather than an adoption — the one place in this whole area where the framework could contribute something the gap-dependent literature does not already have.
2. It interacts with the existential-`π*` repair (§3a): quantifying `TV̄_t` against the *nearest* optimal policy kills the tie counterexample and leaves an obstruction involving only strictly positive gaps. The `Γ_min` question and the existential-`π*` question are the same question from two sides.

So: **(A5v) as the load-bearing hypothesis; `Γ_min` as the spike that could replace it with something better; (A5) deleted rather than softened.**

And plainly, for the record: **the paper's headline rate needs a stated `Δ_min` (or `Γ_min`) dependence that it currently lacks.** If the rewrite keeps a TV-coordinate hypothesis, conclusion (v) must display `1/Δ_min` and Theorem 4.1's preamble must name the Bellman-convention uniform gap. If it adopts (A5v), the dependence disappears honestly rather than silently. What is not available is the current combination: a `Δ_min`-free constant `c` inside a rate that looks gap-free.

---

## 8. Answering the reviewer

**[proved]** The reviewer who could not see how App D follows was right, and for a sharper reason than a missing step: **the step as performed uses the paper's own inequality backwards** (§1). If a response is made it is short — the condition needs a uniform Bellman-convention gap, the constant carries `1/Δ_min`, the composition is then weaker than the direct argument, and so the hypothesis is being replaced rather than patched.

---

## 9. Where I want a second pair of eyes

- **[guess]** Whether `V_max` in (v) is intended as `N_h` or `O(1)`. I read `V_max(M_t) := max_a Q_O − min_a Q_O` as a *trajectory-value* range, hence `≤ N_h` under per-step rewards in `[0,1]`; the `N_h²` exponent suggests some other accounting I could not reconstruct.
- **[hypothesis]** The reachability qualifier on `Δ_min` in §5. UCBVI's bound does not care about unreachable states and `TV̄_t` occupancy-weights them to zero, but "reachable under `Q_t` for some `t`" is algorithm-dependent; I did not chase whether the clean statement is "reachable under some policy."
- **§3c needs first-hand verification before it is cited** (see the caveat there).
- Numerics are on the 3-state witness only. `ucbvi_tv.py` (full UCBVI on random multi-state MDPs) has a **buggy gap-enforcement routine** — it reported `gapmin_realized: 0.0` for target gap 0.05 — so its small-gap rows are unreliable and I used none of them. The multi-state occupancy question is **[untested]**, though §10 argues it should not matter.

---

## 10. On the framing of the question

Joseph asked whether the question was framed well. Three observations.

**The occupancy self-referentiality is not where the difficulty is, and it is worth saying why.** The performance-difference lemma is *already* occupancy-weighted by the learner's own `d_h^{Q_t}`. That is not a complication the TV coordinate introduces — it is the native form of the identity, and Simchowitz–Jamieson's version is stated with the learner's own `ω_{k,h}` for exactly that reason. So the occupancy weighting is **exactly free**: no occupancy-shift argument is needed anywhere, because `d^{Q_t}` is never compared to `d^{π*}`. (It *would* be needed for the non-restarting carryover variant the paper's own Remark flags, and for a `max`-over-states coordinate à la TRPO.) The real difficulty is the entirely separate near-tie problem, which is per-state and has nothing to do with occupancies. Of the two worries flagged in the brief, the first (`√L` vs `log L`) was the crux and understated; the second was a false lead.

**The TV dressing is costing more than it earns.** Deterministic-vs-deterministic makes TV an indicator, so the object is a *counting* object. Naming it that way connects it to Proposition 4 and the whole `N_{K,h}(s,a)` apparatus; naming it TV invites a distribution-matching reading. **[unverified-by-either — the recon agent's scout opened it, the recon agent did not]** Related referee risk: Foster, Krishnamurthy et al. (arXiv 2407.15007) Theorem 2.1 bounds `J(π*) − J(π̂) ≤ 4R·D²_H(P^{π̂},P^{π*})` and reportedly says explicitly that the result *"would be trivial if squared Hellinger were replaced by total variation"* — a Hellinger-primed referee will ask why ours is TV.

**The question asked is well-posed but subordinate.** The load-bearing question is "what is the weakest condition on a base learner from which a piecewise-stationary composition theorem follows," and asked that way the answer (§7) is immediate and better. The rewrite should state (A5v) and derive the TV forms as corollaries, rather than assume a TV form and instantiate it.

**One structural gift from the recon worth keeping.** Imitation learning runs *policy-space → value* with a **max**-gap multiplier: Ross–Gordon–Bagnell (arXiv 1011.0686v3, DAgger) **Theorem 2.2** — `E_{s∼d_π}[ℓ(s,π)] = ε` under the **learner's own** state distribution with `ℓ` the 0-1 loss, plus `Q^{π*}_{T−t+1}(s,a) − Q^{π*}_{T−t+1}(s,π*) ≤ u` on `d_π`'s support, gives `J(π) ≤ J(π*) + uTε` **[verified-against-PDF, recon, proof read]**. We run *value → policy-space* with a **min**-gap divisor. Both directions are gap-mediated, and that sandwich is the structural reason no gap-free constant exists in either direction. Nobody in IL goes our direction because there is no regret bound to start from — the expert is exogenous; and DAgger has no rate in `L` (cumulative control is `Σ_i ε_i ≤ N·ε_N + O(√N)`, `Θ(N)` unless realizable; their Theorem 3.1 is best-iterate). So (A5v) is a strictly stronger *shape* than anything IL provides, and it is stronger precisely because optimism supplies self-improvement an exogenous expert does not. That is a clean way to position the contribution.

---

## 11. What was not read

**[unverified-by-either]** Ok–Proutiere–Tranos; Jin et al.; Even-Dar–Mannor–Mansour; Kaufmann et al. reward-free; MOCA; Rajaraman et al.; AggreVaTe; Ross–Bagnell 2010; Foster et al. 2407.15007.

**Opened but grepped, not read (recon):** Xu–Ma–Du (2102.04692); Dann et al. (2107.01264) — the recon read the latter's Theorem 3.2, Definition 3.1 (return gaps), Theorems 4.2 and 4.5; both are value-gap-space and neither headlines a misranking-mass bound. The recon's own scout reports that the two Al Marjani BPI papers encode the relevant impossibility as a standing *assumption* (unique optimal policy) rather than a theorem, with the gap-oracle dependence admitted only in prose (§5.2 of 2009.13405) — read by neither the recon agent nor me.

**Next threads if this is picked up:** (1) whether the `Γ_min` version of the hypothesis holds — the highest-value open question here; (2) whether MOCA's occupancy-weighted gap term is a missing precedent; (3) first-hand verification of §3c.

---

## Files in this directory

- `gap_scaling.py` — the §3b/§3d witness-MDP numerics (reproduces the table; ~40 s, 24 seeds).
- `ucbvi_tv.py` + `numerics.json` / `numerics.err` — full-UCBVI-on-random-MDP attempt; **gap enforcement is buggy** (§9). Retained as a record of what was tried. **Do not cite its small-gap rows.**
