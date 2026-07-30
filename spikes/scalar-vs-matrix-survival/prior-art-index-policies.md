# Prior art — index policies / restless bandits: the literature's own answer to "can a state-dependent scalar suffice?"

*This neighborhood was not on the brief's list. It turned out to be the closest match to the actual question, because the Whittle index **is** precisely "a state-dependent scalar functional whose greedy argmax is the policy" — which is the object the brief asks whether one can construct. So the restless-bandit literature has been asking the author's question, in his exact form, since 1988.*

**Epistemic marking:** **[VERIFIED]** = I fetched the PDF/publisher page and read the relevant text; quotes are verbatim from the source. **[RECALLED, UNVERIFIED]** = not checked.

---

## THE HEADLINE — the multidimensional case is an explicitly-stated open problem, verbatim, as recently as Dec 2023, with Niño-Mora as coauthor

**Hao, Y., Wang, Z., Niño-Mora, J., Fu, J., Yang, M., & Pan, Q. (2023/2024). "Non-myopic Beam Scheduling for Multiple Smart Target Tracking in Phased Array Radar Networks."** arXiv:2312.07858 (13 Dec 2023); published as *Sensors* 24(23):7755, DOI 10.3390/s24237755. **[VERIFIED — full PDF downloaded and read; all quotes below are verbatim]**

Three independent verbatim statements of the open problem:

> *"In the more practically relevant case of multi-target tracking RMABP models with multi-dimensional state Kalman filter dynamics, indexability is currently an open problem."*

> *"In models with multi-dimensional tracking error covariance (TEC) state, the application of the Whittle index policy is at present elusive."*

> *"Yet, at present it is unknown whether restless projects with multi-dimensional Kalman filter dynamics such as those above are indexable, even for a single dynamics model (M = 1). Indexability has only been established (in [49]) for the special case of target tracking with scalar Kalman filter dynamics and a single dynamics model, by applying the PCL-indexability approach for real-state projects in [43]."*

(Their `[49]` = Dance & Silander JMLR 2019; their `[43]` = Niño-Mora, *Math. of OR* 45(2):465–496, 2020 — both resolved from their reference list, **[VERIFIED]**.)

And, directly supporting the author's counterexample hunt, also verbatim:

> *"However, in general, myopic scheduling policies exhibit inevitable performance degradation in the long run [19]."*

> *"index policy outperforms greedy policies."*

Their `[19]` for the myopic-degradation claim is **Pang, C. & Shan, G. (2019), "Sensor scheduling based on risk for target tracking," *IEEE Sensors Journal* 19(18), 8224–8232** **[VERIFIED as the reference they cite; I did NOT read Pang & Shan, so whether it contains a clean counterexample vs. an empirical observation is unchecked — this is the single most promising lead I did not follow]**.

**Why this is the headline.** The author asked to be told if the whole question is answered somewhere. The honest answer is the opposite and better: *the closest well-posed version of his question is an acknowledged open problem in the operations-research literature, stated as such by the person who built the main tool for attacking it.* That means (a) he is not reinventing anything, and (b) he has a citable justification for offering a sufficient matrix certificate instead of a scalar index. It also means a counterexample defeating the natural myopic scalars in the *matrix* case would be a contribution to a named open problem, not just a lemma for his paper.

---

## Supporting: the verification-theorem machinery

- **Niño-Mora, J. (2020). "A verification theorem for threshold-indexability of real-state discounted restless bandits." *Mathematics of Operations Research* 45(2), 465–496. DOI 10.1287/moor.2019.0998.** **[VERIFIED — bibliographic data via publisher listing and two independent citing reference lists; body not read]**
  The PCL-based (partial conservation laws) verification theorem that made the scalar Kalman result reachable. Per Niño-Mora's own 2026 review **[VERIFIED, verbatim from arXiv:2601.13045]**: the PCL approach *"allowed to overcome the long-standing problem of establishing the optimality of threshold policies and proving indexability for the scalar Kalman filter restless bandit model, as demonstrated in the groundbreaking work of Dance and Silander."*
  **Why it bears:** this is the tool one would have to extend to attack the matrix case. If the author wants to say "the natural route to a scalar index requires a threshold-structure verification theorem that does not exist in the multivariate setting," this is the citation for the route.

- **Niño-Mora, J. (2026). "Markovian restless bandits and index policies: A review." arXiv:2601.13045, 19 Jan 2026.** **[VERIFIED — abstract and the relevant §body passages read from the downloaded PDF]**
  Current survey. Useful negative datum: I grepped its full text and it does **not** contain a "multidimensional Kalman remains open" sentence — its Kalman coverage (La Scala & Moran; Le Ny et al.; Dance & Silander) is all scalar-state, and it notes Le Ny et al.'s closed-form index holds *"in the scalar case with identical sensors."* So the 2023 radar paper above remains the best explicit citation for the open status; the 2026 review corroborates by omission rather than by statement.

---

## The scalar case: cite the JMLR version, not the NIPS one

**Dance, C. R., & Silander, T. (2019). "Optimal Policies for Observing Time Series and Related Restless Bandit Problems." *Journal of Machine Learning Research* 20, article 35, pp. 1–93.** **[VERIFIED — JMLR landing page, verbatim abstract]**

Verbatim abstract highlights: *"We present the first proof that a simple policy, which observes when the posterior variance exceeds a threshold, is optimal for this problem. The proof generalises to a wide range of cost functions other than the posterior variance. It is based on a new verification theorem by Nino-Mora ... and on the relation between binary sequences known as Christoffel words and the dynamics of discontinuous nonlinear maps ... This result implies that optimal policies for linear-quadratic-Gaussian control with costly observations have a threshold structure. It also implies that the restless bandit problem of observing multiple such time series, has a well-defined Whittle index policy. We discuss computation of that index, give closed-form formulae for it, and compare the performance of the associated index policy with heuristic policies."*

**Why this supersedes the NIPS 2015 paper for citation purposes:** the 2015 result was *conditional* on an unproved assumption (A1, threshold-policy optimality). The JMLR version **proves** threshold optimality, so indexability in the scalar case is unconditional there. Citing the 2015 conditional theorem when the 2019 unconditional one exists would be a (minor but real) miscitation.

Also note: it establishes that **LQG control with costly observations has threshold-structured optimal policies** — i.e. in the *scalar* case the optimal rule genuinely *is* a state-dependent scalar threshold. That is the closest thing in the literature to a positive answer to the author's step-2 intuition, and it holds only in dimension one.

**Bibliographic caution:** JMLR's own landing page gives *volume 20, article 35, pp. 1–93*; the radar paper's reference list gives *vol. 20, no. 1, pp. 1218–1310* (aggregated volume pagination). Both refer to the same paper. Pick one convention deliberately.

---

## The NIPS 2015 predecessor (still worth citing for the negative content)

**Dance, C. R., & Silander, T. (2015). "When are Kalman-Filter Restless Bandits Indexable?" *Advances in Neural Information Processing Systems 28 (NIPS 2015).*** **[VERIFIED — full PDF read; quotes verbatim]**

Abstract, verbatim: *"We study the restless bandit associated with an extremely simple scalar Kalman filter model in discrete time. Under certain assumptions, we prove that the problem is indexable in the sense that the Whittle index is a non-decreasing function of the relevant belief state. In spite of the long history of this problem, this appears to be the first such proof. We use results about Schur-convexity and mechanical words, which are particular binary strings intimately related to palindromes."*

Four separately load-bearing facts, each verbatim-verified from the body:

1. **The multivariate case is explicitly an open problem.** Final sentence of §5 (Further Work), verbatim: *"Finally, the question of the indexability of the discrete-time Kalman filter in multiple dimensions remains open."*
   **Why this matters most:** the author is asking whether a state-dependent scalar can characterize survival in the *matrix* case. The literature's closest analogue of that question — does a scalar index even exist for the multidimensional discrete-time Kalman filter — is stated as **open** as of NIPS 2015. This is strong evidence the author is not reinventing a known result, and it is exactly the kind of citable "this is open" anchor that justifies the paper's matrix condition rather than apologizing for it.

2. **Even the scalar case was open until 2015, and hard.** §1, verbatim: *"that attention has produced no satisfactory proof of indexability – even for scalar time-series and even if we assume that there is a monotone optimal policy for the single-arm problem, which is a policy that plays the arm if and only if the relevant belief-state exceeds some threshold (here the relevant belief-state is a posterior variance)."* The eventual proof needed Schur convexity and combinatorics on words (mechanical words, palindromes).
   **Why it bears:** calibrates expectations. If a scalar index for the *one-dimensional* variance recursion needed palindrome combinatorics, then "some scalar functional of `I_o(a)` and `P_t` should work" is a much heavier lift than it looks, and the author's instinct to hunt counterexamples numerically is well-founded.

3. **They found counterexamples to submodularity in this exact setting.** §5, verbatim: *"One might attempt to prove that assumption A1 holds using general results about monotone optimal policies for two-action MDPs based on submodularity [2] or multimodularity [1]. However, we find counter-examples to the required submodularity condition."*
   **Why it bears:** the brief hypothesised known non-submodularity for some covariance-derived objectives. Here is a verified instance of non-submodularity inside a Kalman-scheduling problem — though note carefully that the counterexamples are to the submodularity condition needed for *monotone optimal policies in the single-arm MDP*, **not** to submodularity of a set-function coverage objective. Those are different submodularities and conflating them would be an error. (The sensor-selection set-function submodularity literature is covered in the sibling `prior-art-sensor-scheduling.md`.)

4. **Theorem 1 is conditional, and the condition is unproven.** Verbatim: *"Theorem 1. Suppose a threshold policy (A1) is optimal for the single-arm problem (2). Then Problem KF1 is indexable."* A second numbering of the same result appears in §4 as *"Theorem 1. The index λ^W(x) of (6) is continuous and non-decreasing for x ∈ R₊."* Assumption A1 is *assumed*, not proved (§5 is about attempts to prove it).
   **Why it bears:** if cited, cite it as *conditional* indexability. Stating "indexability of the scalar Kalman bandit was proved in 2015" without the A1 hypothesis would be an overclaim a reviewer in this area would catch.

BibTeX-ready: Christopher R. Dance and Tomi Silander, NIPS 2015, paper id 5922; PDF at `https://proceedings.neurips.cc/paper_files/paper/2015/file/6d70cb65d15211726dcce4c0e971e21c-Paper.pdf`.

---

## Supporting: hardness, and the general limits of index policies

- **Papadimitriou, C. H., & Tsitsiklis, J. N. (1999). "The complexity of optimal queueing network control." *Mathematics of Operations Research* 24(2), 293–305. DOI 10.1287/moor.24.2.293.** **[VERIFIED — publisher abstract]**
  Shows the restless bandit problem (the generalization of the multi-armed bandit where unselected processes are not quiescent) is **complete for PSPACE**.
  **Why it bears:** the general hardness anchor. Survival-under-scheduling being computationally hard in general is a principled reason a *sufficient LMI condition* is the right thing for a paper to offer — no scalar greedy rule could be expected to be exactly optimal for a PSPACE-complete family. This reframes the paper's matrix condition as a tractable sufficient certificate rather than a concession.

- **Guha, S., Munagala, K., & Shi, P. (2010). "Approximation algorithms for restless bandit problems." *Journal of the ACM* 58(1), art. 3.** **[VERIFIED — bibliographic data; body not read]**
  This is the reference Dance & Silander attribute for *"such problems are in general PSPACE-hard even to approximate to any non-trivial factor."* **[the attributed claim is VERIFIED as being what Dance & Silander wrote; I did not verify it against Guha et al.'s own text]**

- **Dance & Silander's claim that index policies can be strictly suboptimal.** §1, verbatim: *"while bandits always have an optimal index policy (select the arm with the largest index), it is known that no index policy can be optimal for some discrete-state restless bandits [17]."*
  **Flag, offered as a caution rather than a finding:** their `[17]` is **Ortner, R., Ryabko, D., Auer, P., & Munos, R. (2012), "Regret bounds for restless Markov bandits," ALT 2012** — which is a regret-bounds paper, and on its face an odd source for a "no index policy is optimal" impossibility claim. I have **not** verified that Ortner et al. contain such a result, and I suspect the attribution may be loose. **Do not propagate this citation without checking it.** If the underlying fact is real it would be quite valuable to the author (an impossibility result for scalar index policies), so it is worth ten minutes — but as it stands it is **[RECALLED/ATTRIBUTED, UNVERIFIED]** and citing it on my word would be exactly the failure mode the brief warned about.

- **Le Ny, J., Feron, E., & Dahleh, M. (2011). "Scheduling continuous-time Kalman filters." *IEEE Trans. Automatic Control* 56(6), 1381–1394.** **[VERIFIED — bibliographic data via Dance & Silander's reference list and search; body not read]**
  The continuous-time scalar Kalman-Bucy restless bandit shown indexable; the result Dance & Silander position their discrete-time work against.

- **Niño-Mora, J., & Villar, S. (2009). "Multitarget tracking via restless bandit marginal productivity indices and Kalman filter in discrete time." *Proc. 48th IEEE CDC*, 2905–2910.** **[VERIFIED — bibliographic data; body not read]** And **Villar, S. (2012), PhD thesis, "Restless bandit index policies for dynamic sensor scheduling optimization," Universidad Carlos III de Madrid** **[VERIFIED — bibliographic data]**. The thesis is the most likely single place to find worked numerical counterexamples to myopic scheduling, if any exist in this literature.

- **Whittle, P. (1988). "Restless bandits: activity allocation in a changing world." *J. Applied Probability* 25A, 287–298** and **Weber, R. R., & Weiss, G. (1990). "On an index policy for restless bandits." *J. Applied Probability*, 637–648.** **[RECALLED, page ranges from Dance & Silander's reference list — VERIFIED as appearing there]** The origin of indexability and the asymptotic-optimality-of-Whittle's-policy result respectively.

---

## Negative results from this thread

- **I did not find any published counterexample to greedy/myopic λ_max or log-det Kalman scheduling in this literature.** The restless-bandit thread attacks the problem from the index-existence side rather than by exhibiting myopic failures, so it does *not* substitute for the numerics the author is running tonight. (Sibling file may have better luck from the sensor-selection side.)
- **No multivariate/matrix indexability result found at all** — and the 2015 explicit open-problem statement suggests that is because there isn't one, at least as of then. **Caveat:** I did not do a forward-citation sweep of Dance & Silander to check whether 2016–2026 work has since closed the multidimensional case. That is the single highest-value remaining check in this neighborhood and I'd flag it as unfinished.
- **Nothing in the paper's existing bib overlaps this neighborhood.** Checked `confident-agent-neurips-2026.extracted.bib`: it has nonstationary-bandit entries (`min-russo-2023-nonstat-bandit`, `russac-2019-weighted`, `garivier-2008-upperconfidence`, `slivkins-2008-adapting`, `auer-cesa-bianchi-fischer-2002-ucb`) but **no restless-bandit or index-policy entries**, and `meier-peschon-dressler-1967` is absent despite being cited by Dance & Silander as foundational.

---

## What this changes about the framing

The restless-bandit framing suggests the author's dichotomy has a third, better-posed axis. "Scalar vs matrix" and "myopic vs non-myopic" are both really asking: **does this problem admit an index?** — where an index is a state-dependent scalar whose greedy argmax is optimal. That question has (a) a precise standard name, (b) a known-hard answer in general (PSPACE-complete), (c) a hard-won conditional yes in the scalar Kalman case, and (d) an explicitly open status in the multidimensional Kalman case.

If the author adopts that vocabulary, his contribution reads as: *the multidimensional survival problem is not known to be indexable, so we give a tractable sufficient matrix certificate instead* — which is a stronger and much more defensible position than *we could not find a scalar that works*. It also means his state-independent-scalar collapse proof is best described as ruling out **static** (non-index) scalar rules, a sharper claim than "scalars fail."
