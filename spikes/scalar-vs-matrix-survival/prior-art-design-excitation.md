# Prior art — optimal experiment design / information-matrix scalarization, and adaptive-control persistent excitation

*Neighborhood assignment: OED scalarization theory (A/D/E, Kiefer Φ_p, Loewner order, admissibility, mixtures) + adaptive-control persistent excitation. Kalman sensor scheduling and viability theory deliberately out of scope (covered elsewhere).*

*Written 2026-07-29. Epistemic rungs are marked per item:*

- **[VERIFIED-TEXT]** — I fetched and read the actual text (PDF extracted to plain text); quoted statements are transcribed from it (OCR artifacts noted where present).
- **[VERIFIED-ABSTRACT]** — I read the publisher abstract or arXiv abstract page only; the body was not read.
- **[SECONDARY]** — the statement is verified only as *a claim made by another paper I did read*, citing a source I did not open.
- **[RECALLED-UNVERIFIED]** — my own recollection, no text fetched. Do not cite a theorem number from these.

---

## 0. Headline: the framing needs one correction before the citation hunt matters

**The literature answers the "single most valuable specific thing" — but in the direction opposite to the one hoped for.** There is a published, verified one-to-one correspondence which *constructs* a legitimate scalar criterion that exactly characterizes a Loewner-feasibility condition, including for mixtures. So a theorem of the form *"no scalar function of the information matrix can characterize Loewner-order feasibility of a mixture"* cannot exist as stated — it is false, and Pukelsheim's own machinery is the counterexample generator. Details in §1.3.

Concretely, the condition of interest is feasibility against a **fixed floor**:

$$\bar I(\pi) \;=\; \mathbb{E}_{a\sim\pi}\big[I_o(a)\big] \;\succeq\; I_{\min}.$$

Define $\varphi_{I_{\min}}(M) = \sup\{\delta > 0 : M \succeq \delta I_{\min}\} = \lambda_{\min}\!\big(I_{\min}^{-1/2} M I_{\min}^{-1/2}\big)$ (for $I_{\min}\succ0$). Then:

- $\bar I(\pi) \succeq I_{\min} \iff \varphi_{I_{\min}}(\bar I(\pi)) \ge 1$ — an exact scalar characterization;
- $\varphi_{I_{\min}}$ is **not an ad-hoc gadget**: it is a bona fide *information function* in Pukelsheim's sense (isotonic w.r.t. Loewner, concave, positively homogeneous, upper semicontinuous), because $\{M \succeq I_{\min}\}$ is a closed convex subset of NND not containing $0$ and receding in all NND directions — precisely the hypothesis of the correspondence quoted in §1.3;
- when $I_{\min} = c\,I$ (isotropic floor), $\varphi_{I_{\min}}(M) = \lambda_{\min}(M)/c$, i.e. **the condition is exactly E-optimality's criterion** and a scalar is fully sufficient.

**So the honest sharp claim is a restricted-class claim, and the restriction is where the paper's real content lives.** Candidate honest forms, in increasing strength:

1. *No **per-action separable** scalarization works.* A constraint of the form $\mathbb{E}_{a\sim\pi}[f(I_o(a))] \ge c$ cannot characterize $\bar I(\pi)\succeq I_{\min}$. For concave isotonic $f$, Jensen gives $\mathbb{E}[f(I_o(a))] \le f(\bar I(\pi))$ — so a per-action budget is *sufficient-but-not-necessary*, never equivalent; and the gap is exactly the directional-mixing effect the paper is about (two actions each individually infeasible can mix to a feasible average, precisely because feasibility is a convex-set membership and not an expectation of a scalar). This is the claim I would bet the author's own argument actually establishes.
2. *No member of the **classical A/D/E/Φ_p family** works.* $\Phi_p$ for $p\ne\infty$ are strictly Loewner-isotonic but not order-*reflecting*: $\Phi_p(M)\ge\Phi_p(I_{\min})$ is necessary, never sufficient, and $\Phi_\infty$-ish $\lambda_{\min}$ works only for isotropic $I_{\min}$ (see §1.4). This is provable in three lines and is the cleanest true statement in the neighborhood.
3. *No **fixed, floor-independent** scalar works.* Any exact scalar characterization must depend on $I_{\min}$ (the gauge above is built *from* $I_{\min}$). This is the version I'd expect to be most useful rhetorically: the matrix condition is not replaceable by a *criterion chosen in advance of the survival floor*.

**Recommendation:** cite the design literature for (a) the partial-order structure and the fact that Loewner-optimal objects mostly don't exist, (b) the matrix condition = *whole family* of scalar conditions equivalence (§1.1, this is the strongest directly-quotable matrix-vs-scalar theorem in the field), and (c) the information-function/convex-set correspondence — and then state the paper's own restricted-class no-go, which is genuinely not in this literature. **Negative result reported explicitly: no published theorem says "no scalar functional characterizes Loewner-feasibility of a mixture," and there cannot be one.**

---

## 1. Core design-theory items

### 1.1 Pukelsheim's equivalence theorem: Loewner optimality = simultaneous scalar optimality in *every* direction — **[VERIFIED-TEXT]**

**Source read:** F. Pukelsheim, *Optimality Criteria for Experimental Designs*, Biometrics Unit technical report **BU-943-M**, Cornell University, 14 October 1987. Open access: <https://ecommons.cornell.edu/bitstream/handle/1813/33058/BU-943-M.pdf>. (This report is the pre-book synopsis of what became Chapters 4–5 and 10 of the 1993 book; I read the report's full text, not the book.)

Verbatim (transcribed; OCR renders `⪰` as `~` / `≥` and `ξ` as `e`):

> **5 THEOREM.** Let $\mathcal M$ be a convex set of competing moment matrices. Then for every moment matrix $M\in\mathcal M$ the following statements are equivalent:
> a (Information optimality) $M$ is Loewner optimal for $K'\theta$ in $\mathcal M$.
> b (Dispersion optimality) $M\in A(K)$, and $K'M^-K \le K'A^-K$ for all $A\in\mathcal M\cap A(K)$.
> c (Uniform optimality) $M$ is optimal for $c'\theta$ in $\mathcal M$ **for all vectors $c\ne0$ in the range of $K$**.

**Why it bears on the question.** This is the field's canonical statement that the matrix condition is *exactly* the conjunction of a continuum of scalar (c-optimality) conditions, one per direction — and no finite or single one of them. It is the citable form of "directional, not magnitude." It also tells you the right rhetorical move: the survival condition $\bar I(\pi)\succeq I_{\min}$ is $c^\top\bar I(\pi)c \ge c^\top I_{\min}c\ \forall c$, i.e. a *family* of scalar budget conditions indexed by direction, and any single scalar summary is a projection of that family.

**BibTeX-ready:** `@techreport{pukelsheim-1987-optimality-criteria, author={Pukelsheim, Friedrich}, title={Optimality Criteria for Experimental Designs}, institution={Cornell University, Biometrics Unit}, number={BU-943-M}, year={1987}}` — no DOI; stable Cornell eCommons handle `1813/33058`.

### 1.2 Nonexistence of Loewner-optimal designs (the partial order has no maximum) — **[VERIFIED-TEXT]**

Same report, immediately after Theorem 6 (the equivalence theorem for Loewner optimality):

> **7 COROLLARY.** No moment matrix in $M(\Xi)$ is Loewner optimal for $K'\theta$ in $M(\Xi)$, except when the coefficient matrix $K$ has rank one.

And from the report's abstract: *"An equivalence theorem is presented, but Loewner optimal designs mostly fail to exist. Information functions are introduced as weaker criteria that are isotonic relative to the Loewner ordering, concave, and positively homogeneous."*

**Why it bears.** This is the sharpest published statement of *why* the field scalarizes at all: for rank > 1 the Loewner order on the achievable set has no maximum, so total-order criteria are a necessity, not a convenience. Useful in the paper as the reason a reader's instinct ("just optimize the matrix") is not available in the design literature either — and as a contrast: the paper's condition is **feasibility against a floor**, not *optimality*, and feasibility sets are exactly where the Loewner order behaves well. That distinction (optimality vs feasibility) is, I think, the crispest thing to say to a reviewer who reaches for A/D/E-optimality.

### 1.3 The information-function ↔ convex-set correspondence — the item that changes the plan — **[VERIFIED-TEXT]**

Same report, Sections D9–D13. Transcribed:

> **10** ... it is indispensable that a reasonable criterion is isotonic relative to the Loewner ordering, $C \ge D \Rightarrow \phi(C)\ge\phi(D)$ for all $C,D\ge0$. A second property, similarly obliging, is concavity ... *For otherwise the situation $\phi(\alpha C+(1-\alpha)D) < \alpha\phi(C)+(1-\alpha)\phi(D)$ will occur: Rather than carrying out the experiment belonging to $\alpha C+(1-\alpha)D$ itself, one can achieve greater information through interpolation from two other experiments. This is absurd, information cannot be increased by interpolation.* A third property is positive homogeneity ...

> **12** ... Criteria that enjoy all the properties discussed so far are called information functions. • An information function on NND(s) is a criterion $\phi:\mathrm{NND}(s)\mapsto\mathbb R$ that is isotonic, concave, positively homogeneous, nonconstant, and upper semicontinuous.

> **[Section D13]** ... the unit level set $\mathcal C=\{C\ge0:\phi(C)\ge1\}$. This is a closed convex subset of the cone NND(s) which does not contain zero and recedes in all directions of NND(s) ... Conversely, every closed convex subset $\mathcal C$ of NND(s) that does not contain zero and recedes in all directions of NND(s) determines an information function, namely $\phi(C)=\sup\{\delta>0 : C\in\delta\mathcal C\}\cup\{0\}$ ... **In other words, there is a one-to-one correspondence between information functions $\phi$ on NND(s) and closed convex subsets $\mathcal C$ of NND(s) that do not contain zero and recede in all directions of NND(s).**

**Why it bears — read this one carefully.** Two consequences, both load-bearing:

1. **It refutes the hoped-for no-go.** $\{M : M\succeq I_{\min}\}$ satisfies the correspondence's hypotheses exactly, so there *exists* an information function whose unit level set is the survival-feasible set; it is $\varphi_{I_{\min}}$ from §0. Feasibility of the *mixture* is then the single scalar test $\varphi_{I_{\min}}(\mathbb E_\pi[I_o(a)])\ge1$. If the author's own argument concludes "no scalar can do this," the argument has an implicit restriction (almost certainly: the scalar must be applied per-action and averaged, or must be chosen independently of $I_{\min}$) and that restriction should be stated as a hypothesis rather than left implicit — a reviewer from the design community will construct $\varphi_{I_{\min}}$ in about ten seconds.
2. **The concavity paragraph is quotable gold for the paper's actual point.** "Information cannot be increased by interpolation" is Pukelsheim's own justification for concavity — i.e. the design literature has *already* reasoned about mixtures of designs and concluded that any legitimate criterion must be superadditive/concave over mixtures. That is the exact structural fact that makes per-action scalar budgets fail to be necessary: mixing can only help, so a budget that every action must individually satisfy is strictly conservative.

Also verified in the same section: given positive homogeneity, **concavity is equivalent to superadditivity** $\phi(C+D)\ge\phi(C)+\phi(D)$. That is a directly citable inequality for the paper's averaging step.

### 1.4 Kiefer's $\Phi_p$ family: isotonic and concave, hence necessary-only — **[VERIFIED-ABSTRACT]** (properties) / **[VERIFIED-TEXT]** (isotonicity+concavity as class properties, §1.3)

$\Phi_p^+(M) = \big[\tfrac1m \operatorname{tr}(M^{-p})\big]^{-1/p}$; $p=1$ → A-optimality, $p\to0$ → D-optimality, $p\to\infty$ → E-optimality. For $p\in[0,\infty)$, $\Phi_p$ is positively homogeneous, continuous, concave on NND, strictly positive on nonsingular matrices, vanishing on singular ones; there is always a $\Phi_p$-optimal design with nonsingular information matrix and (by strict log-concavity) the optimal information matrix is unique.

**Verified how:** these properties as stated above come from the abstract/intro of Harman & Rosa / Pázman-school work surfaced in search, plus the arXiv paper below; I did *not* open Kiefer (1974) itself. Treat "Kiefer 1974" as **[RECALLED-UNVERIFIED]** for any specific theorem number.

- L. Pronzato, *A delimitation of the support of optimal designs for Kiefer's $\phi_p$-class of criteria*, arXiv:1303.5046 / HAL hal-00802972 — **[VERIFIED-ABSTRACT]**. Useful only as a modern citable statement of the $\Phi_p$ class's analytic properties.
- Original: J. Kiefer, *General equivalence theory for optimum designs (approximate theory)*, Annals of Statistics 2(5):849–879, 1974 — **[RECALLED-UNVERIFIED]** (volume/pages from memory; verify before citing).

**Why it bears.** Each $\Phi_p$ is Loewner-isotonic but not order-reflecting, so $\Phi_p(\bar I)\ge\Phi_p(I_{\min})$ is a *necessary* condition for survival and never sufficient (for $s\ge2$ and any $p<\infty$: take $\bar I$ with the same $\Phi_p$ value as $I_{\min}$ but eigen-rotated so it is Loewner-incomparable). The single exception is the $\lambda_{\min}$ end of the family *and only under an isotropic floor*. This is the honest, three-line version of "A/D-optimality cannot see the survival condition, E-optimality can only see it if the floor is a sphere."

### 1.5 Admissibility (Loewner-nondominated designs) — the "complete class" language — **[VERIFIED-TEXT]** for the framing, **[SECONDARY]** for the Pukelsheim pointer

**Source read:** H. Dette, X. Liu, R.-X. Yue, *Design admissibility and de la Garza phenomenon in multi-factor experiments*, arXiv:2003.09493 (20 March 2020). Verbatim:

> A prominent example of such a class is the class of admissible designs consisting of the designs with an information matrix, that cannot be improved by an information matrix of another design with respect to the Loewner ordering. In decision theoretic terms the set of admissible designs therefore forms a complete class, in the sense that the information matrix of any inadmissible design may be improved by the information matrix of an admissible design. **It is well known that optimal designs with respect to the most of the commonly used optimality criteria must be admissible (see Pukelsheim, 2006, Chapter 10.10)** and consequently in these cases the determination of optimal designs can be restricted to the class of admissible designs.

**Why it bears.** The implication runs **scalar-optimal ⟹ admissible**, one direction only. The converse — *every* admissible (Loewner-maximal) information matrix is optimal for *some* scalar criterion — is what would have been a clean citation for the bridge argument in the brief. I did **not** find it asserted in the design literature. What I did find is the general vector-optimization result it corresponds to (§1.6), which carries a real caveat: only *properly* efficient points are supported by linear functionals, and those are merely *dense* in the efficient set. So the bridge intuition in the brief is **essentially right in mechanism but not exactly right as stated**: the correct statement is about *proper* efficiency / density, not about every Loewner-maximal point being reachable by a linear criterion. (Note also that the correspondence in §1.3 shows *nonlinear* concave criteria reach much more than linear ones do — so restricting attention to "linear or concave functional ⟹ only certain boundary points" understates what concave criteria can reach. Concave gauges reach *any* closed convex recession-stable level set, which is why the no-go fails.)

Pukelsheim's Chapter 10 is titled *Admissibility of Moment and Information Matrices* — **[VERIFIED-ABSTRACT]** via the SIAM Classics-in-Applied-Mathematics chapter listing and the report's own section headings. I could not open the book (SIAM epubs returns 403; the Internet Archive copy is lending-only), so **no theorem number from the book appears anywhere in this report by design**. If a book-precise citation is wanted, chapter-level citation (`Pukelsheim 2006, Ch. 4` for Loewner optimality, `Ch. 5` for real criteria/information functions, `Ch. 10` for admissibility) is defensible from what I verified; a numbered theorem is not.

**BibTeX-ready:**
- `@book{pukelsheim-2006-optimal-design, author={Pukelsheim, Friedrich}, title={Optimal Design of Experiments}, series={Classics in Applied Mathematics}, volume={50}, publisher={SIAM}, address={Philadelphia}, year={2006}, note={Unabridged republication of the 1993 Wiley edition}, doi={10.1137/1.9780898719109}}` — DOI **[VERIFIED-ABSTRACT]** (it is the SIAM landing-page DOI I hit, which returned 403 on the PDF but is the correct identifier); series volume number 50 is **[RECALLED-UNVERIFIED]**, check before use.
- `@article{dette-liu-yue-2020-admissibility, author={Dette, Holger and Liu, Xin and Yue, Rong-Xian}, title={Design admissibility and de la Garza phenomenon in multi-factor experiments}, journal={arXiv preprint}, eprint={2003.09493}, year={2020}}` — journal version not verified.

### 1.6 The vector-optimization result the bridge argument actually wants: Arrow–Barankin–Blackwell — **[VERIFIED-ABSTRACT]**

**Statement (as consistently reported across the sources surfaced, not read in the original):** in $\mathbb R^n$ with the natural (cone) ordering, for every compact convex set $S$, the set of *properly* minimal (efficient) elements of $S$ is **dense** in the set of minimal elements. Generalizations exist to normed spaces ordered by Bishop–Phelps cones and to topological vector spaces with weakly closed cones admitting strictly positive continuous linear functionals.

- Original: K. J. Arrow, E. W. Barankin, D. Blackwell, *Admissible points of convex sets*, in *Contributions to the Theory of Games II* (Kuhn & Tucker eds.), Annals of Mathematics Studies 28, Princeton UP, 1953, pp. 87–91 — **[RECALLED-UNVERIFIED]** (page numbers from memory; verify).
- Survey: Jahn, *Arrow–Barankin–Blackwell theorems and related results in cone duality: a survey*, in Lecture Notes in Economics and Mathematical Systems, Springer, 1997/2000, doi:10.1007/978-3-642-57014-8_9 — **[VERIFIED-ABSTRACT]**.
- Limitations in infinite dimensions: arXiv:2407.10509, *ABB theorems: Results and limitations in infinite dimensions* — **[VERIFIED-ABSTRACT]**.
- Generalization to nonconvex sets: SIAM J. Control Optim. papers at doi:10.1137/0326055 and doi:10.1137/0328021 — **[VERIFIED-ABSTRACT]** (titles/DOIs seen, bodies not read).

**Why it bears.** This is the named, citable home of the brief's "supporting hyperplanes vs the PSD cone" intuition, *and* it supplies the honest caveat: linear scalarization reaches the properly-efficient points, which are dense but not necessarily all of the Loewner-maximal frontier. The set of achievable mixture information matrices $\{\mathbb E_\pi[I_o(a)] : \pi\}$ is the convex hull of $\{I_o(a)\}$ — compact convex if the action set is compact — so ABB applies directly to it. **The cone here is the PSD cone, which is not polyhedral**, and that is precisely the setting where efficient-but-not-properly-efficient points are the interesting pathology. If the author wants a *structural* obstruction result, this is the neighborhood where it lives, not in design theory.

### 1.7 Universal optimality: the closest published thing to "one scalar cannot do it" — **[VERIFIED-TEXT]**

**Source read in full:** P. Druilhet, *Conditions for optimality in experimental designs*, CREST-ENSAI (PDF at <https://lmbp.uca.fr/~druilhet/criteria.pdf>; published as *Linear Algebra and its Applications* / journal version not confirmed — cite the PDF or verify the venue). Transcribed:

> **Definition 26 (Kiefer)** A design $d^*$ is universally optimal among a class $\mathcal D$ of designs if $d^*$ is $\Phi$-optimal for all the criteria $\Phi(C)$ from $\mathcal C$ to $]-\infty,+\infty]$ satisfying: (a) $\Phi$ is invariant under each permutation of rows and (the same on) columns, (b) $\Phi(\alpha C)$ is non-increasing in the scalar $\alpha>0$, (c) $\Phi$ is convex.

> **Proposition 28 (Yeh)** A design $d^*$ is universally optimal among a class $\mathcal D$ of designs if it satisfies: (i) $\operatorname{tr} C_{d^*} = \max_{d\in\mathcal D}\operatorname{tr} C_d$, (ii) $\forall d\in\mathcal D$, there exist scalars $a_{d\sigma}\ge0$ satisfying $C_{d^*} = \sum_{\sigma\in S_t} a_{d\sigma} P_\sigma C_d P_\sigma'$.

> **Proposition 29 (Yeh's conjecture)** The sufficient condition in Proposition 28 is also a necessary condition.

The **proof technique of Proposition 29 is the directly relevant part**, and it is the same construction as §1.3 in disguise: given a design $d_1$ violating condition (ii), let $\mathcal A$ be the convex cone generated by $\{P_\sigma C_{d_1}P_\sigma'\}$; then $\Phi(C)=0$ if $C\in\mathcal A$, $+\infty$ otherwise satisfies (a)–(c) and separates — and the paper's own remark upgrades this to the continuous, homogeneous $\Phi_1(C)=\inf_{C'\in\mathcal A}\|C-C'\|$, i.e. **distance to a convex cone is a legitimate Kiefer criterion**.

Also verified in the same paper, **Proposition 30**: with the eigenvalue-invariance version of (a), $d^*$ is universally optimal iff (i) $\operatorname{tr} C_{d^*}=\max_d \operatorname{tr} C_d$ and (ii) $\lambda(C_{d^*}/\operatorname{tr} C_{d^*}) \prec \lambda(C_d/\operatorname{tr} C_d)$ (majorization).

**Why it bears.** Three things. (i) It is the published precedent that *optimality for the entire family of scalar criteria* is equivalent to an explicit **mixture** condition (Yeh's (ii) is literally a nonnegative combination of permuted information matrices) — the closest published statement to "the scalar family collectively equals a matrix-mixture condition, and no single member does." (ii) Its separating-criterion construction is the citable technique for the author's own no-go if he restricts the criterion class — build the criterion, show the class is too rich, or show his restricted class is too poor. (iii) It is **the second independent confirmation that distance-to-a-convex-set is an admissible scalar criterion**, which is exactly why an unrestricted no-go is unavailable.

**BibTeX-ready:** `@article{druilhet-criteria, author={Druilhet, Pierre}, title={Conditions for optimality in experimental designs}, note={CREST-ENSAI preprint}, url={https://lmbp.uca.fr/~druilhet/criteria.pdf}}` — **year and venue unverified**; the paper cites Yeh (ref [19]) and Kiefer (ref [11]).

### 1.8 False friend, flagged so nobody chases it — **[VERIFIED-ABSTRACT]**

S. Gutmair, *Polars and subgradients of mixtures of information functions*, Journal of Statistical Planning and Inference, April 1993, pp. 93–112 (ScienceDirect PII 037837589390070M). Despite the title, "mixtures" here means **mixtures of criteria** (e.g. a compound of the D- and A-criteria), not mixtures of designs. Contains an equivalence theorem for optimal moment matrices w.r.t. such mixtures. Relevant only if the paper ends up combining criteria; **not** relevant to mixture-feasibility. Volume number not verified.

Similarly adjacent-but-not-it: Pukelsheim, *On linear regression designs which maximize information*, J. Statist. Plann. Inference 4(4):339–364, 1980 (PII 0378375880900208) — **[VERIFIED-ABSTRACT]**, page range **[RECALLED-UNVERIFIED]**. Per its abstract: necessary and sufficient conditions for a continuous design to contain maximal information for a prescribed $s$-dimensional parameter, via a dual problem, covering c-, D-, A-, L-optimality and giving a complete account of the non-differentiable E-optimality criterion. The **E-optimality duality** is the piece worth a real read if the paper leans on $\lambda_{\min}$: E-optimality's non-differentiability is exactly the eigenvalue-crossing phenomenon that makes a scalar $\lambda_{\min}$ budget behave badly under mixing, and the dual there is a mixture over the eigenspace of the minimal eigenvalue. I did not read the body; this is the single highest-value unread item on the design side.

### 1.9 Also surfaced, lower value — **[VERIFIED-ABSTRACT]**

- *A stochastic characterization of Loewner optimality design criterion in linear models*, Metrika, doi:10.1007/s001840000106 — characterizes Loewner optimality via a generalization of a corollary of Anderson's theorem (concentration on symmetric convex sets). Potentially a nice alternative gloss: the matrix condition = a probability-concentration statement holding for *all* symmetric convex sets, again a family-not-a-scalar shape. Author/year not verified.
- Yang & Stufken (2009, 2012), Yang (2010), Dette & Melas (2011), Dette & Schorning (2013), Hu et al. (2015) — the "complete class w.r.t. Loewner ordering" series, cited **[SECONDARY]** via Dette–Liu–Yue. Machinery for reducing design search to admissible classes; not about scalarization adequacy. Only worth citing if the paper needs the admissibility-as-complete-class framing.

---

## 2. Adaptive control / persistent excitation

### 2.1 PE is *definitionally* a matrix (Loewner) condition, and the sharp characterization is directional — **[VERIFIED-TEXT]**

**Source read in full:** N. Shimkin and A. Feuer, *Persistency of excitation in continuous-time systems*, **Systems & Control Letters 9 (1987) 225–233**, North-Holland (Dept. of EE, Technion). Received 12 Jan 1987, revised 12 May 1987. Transcribed:

> **Definition 1.** The function $x\in L_{1e}(\mathbb C^n)$ is said to be persistently exciting (PE) iff there exist positive constants $\epsilon_1, T$ such that for all $\tau\ge0$, $\int_\tau^{\tau+T} x(t)x(t)^* dt > \epsilon_1 I$.

> **Theorem 1.** An input $u\in L_{1e}(\mathbb C)$ is persistently exciting for the class $SC_n$ ($PESC_n$) iff it is rich of order $n$.

where "rich of order $n$" (**Definition 3**) is itself a matrix lower bound $J_\tau(M_\tau,T)\succ\epsilon_2 I$ on a *projected* signal Gramian, with the paper's own gloss:

> **Remark 2.** ... Definition 3 is roughly equivalent to requiring that the projections of the functions $I^i u_\tau$ onto $S^\perp$, the orthogonal complement of $S$, are (uniformly) linearly independent.

The paper's stated contribution is that its conditions are **both necessary and sufficient** with no boundedness/continuity/stationarity assumptions on the input, closing the gap to the discrete-time results; it explicitly notes of a predecessor (Mareels) that *"the conditions given there for the continuous case, though necessary, are not sufficient unless complemented by other assumptions."*

**Why it bears.** (a) It is a clean, verified, citable instance of the paper's thesis in the control literature: the excitation requirement is stated as a Loewner lower bound on an averaged information-like matrix, and the necessary-and-sufficient characterization is a *uniform linear independence / projection* (directional) condition — not a magnitude/energy condition. (b) **Important caveat for the author's framing:** the floor in Definition 1 is $\epsilon_1 I$, i.e. **isotropic**, and for an isotropic floor $\lambda_{\min}$ *is* an exact scalar characterization. The control literature therefore does **not** furnish the anisotropic-floor case the paper needs; it is a supporting analogy, not a substitute theorem. If the paper's $I_{\min}$ is anisotropic (which is where all its novelty lives), that anisotropy is a genuine departure from the PE literature and should be sold as such.

**BibTeX-ready:** `@article{shimkin-feuer-1987-persistency, author={Shimkin, Nahum and Feuer, Arie}, title={Persistency of excitation in continuous-time systems}, journal={Systems \& Control Letters}, volume={9}, number={3}, pages={225--233}, year={1987}}` — issue number **[RECALLED-UNVERIFIED]**; volume/pages/year **[VERIFIED-TEXT]** from the article header. Likely DOI `10.1016/0167-6911(87)90045-3` — **[RECALLED-UNVERIFIED]**, verify.

Companion, same era, discrete time: I. Mareels and M. Gevers, *Persistency of excitation criteria for linear, multivariable, time-varying systems* / and *Persistency of excitation, sufficient richness and parameter convergence in discrete time adaptive control*, Systems & Control Letters 2 (1985) — **[VERIFIED-ABSTRACT]** (title of the second seen via ScienceDirect PII 0167691185900350; volume/pages unverified). Shimkin–Feuer's citation of Mareels as *necessary-but-not-sufficient* is the verified part and is itself a usable "a weaker condition does not suffice" data point.

### 2.2 Deficient / partial excitation: convergence happens only in the excited subspace — **[VERIFIED-ABSTRACT]**

- G. Cao, S. Wang, M. Guay, J. Wang, Z. Duan, M. M. Polycarpou, *Deficient Excitation in Parameter Learning*, arXiv:2503.02235, 2025. Introduces a **deficient excitation (DE)** condition generalizing PE; the learning error **within the identifiable subspace** converges exponentially even without PE; the algorithm explicitly computes identifiable and non-identifiable subspaces and returns a least-squares-optimal estimate on the identifiable part; distributed version uses **complementary DE conditions** across estimators, each acting in its own identifiable subspace.

**Why it bears.** This is the modern, sharp, and directly citable statement that excitation is a *subspace* object: what you learn is exactly what you excited, direction by direction. The "complementary DE conditions across multiple estimators" idea is a structural cousin of the paper's mixture: individually deficient excitations combining to cover the space. If the paper wants a recent citation for "directional, not scalar," this is the strongest one I found, and it is 2025 so it also signals the question is live. **Abstract-level only — I did not read the theorems; do not cite a numbered result from it without opening it.**

- *Composite Learning Adaptive Control under Non-Persistent Partial Excitation*, arXiv:2408.01731, 2024 — **[VERIFIED-ABSTRACT]** (title only, from search listing). Same cluster; may contain the sharper decomposition.
- *Sufficient Conditions for Persistency of Excitation with Step and ReLU Activation Functions*, arXiv:2209.06286 — **[VERIFIED-ABSTRACT]** (title only). Peripheral.

### 2.3 Performance limitation under insufficient excitation (a necessity-flavored result) — **[VERIFIED-ABSTRACT]**, metadata incomplete

*Performance limitations of adaptive parameter estimation and system identification algorithms in the absence of excitation*, **Automatica**, 1996 (ScienceDirect PII 0005109895001638; received 1995). Per the abstract as reported: constructs a **bursting scenario** to derive an **analytical lower bound on the worst-case peak steady-state error** for a wide class of parameter estimation and identification algorithms, showing that with no input constraints, arbitrarily small perturbations impose a serious performance limitation, with worst-case performance deteriorating proportionally to the size of the parametric uncertainty set.

**Why it bears.** This is the closest thing I found to a **necessity/impossibility** theorem on the control side: absent adequate excitation, *no algorithm in a broad class* avoids a quantified error floor. If the paper's survival claim has a converse ("without the matrix condition, failure"), this is the analogue to cite and to distinguish from. **ScienceDirect returned 403 for both the abstract page and PDF, so I could not confirm authors, volume, or pages** — this is a *lead*, not yet a citation. My recollection says the authors are in the Anderson/Kosut/Poolla neighborhood, but I will not guess; someone with library access should resolve it in two minutes.

### 2.4 Already in the bib — assessment

`anderson-1985-bursting`, `narendra-1987-persistent`, `bittanti-2000-persistence`, `kreisselmeier-1986-slowly-tv`, `solo-1996-deterministic`, `goel-2020-recursive`, `lee-2019-concurrent` cover the bursting phenomenon and the directional-forgetting response well. What is missing and worth adding, in priority order: **Shimkin–Feuer 1987** (§2.1 — the necessary-and-sufficient directional characterization, verified, and the one that most directly says "matrix not scalar"), then **Cao et al. 2025** (§2.2 — the subspace framing, modern), then the Automatica performance-limitation paper (§2.3) once its metadata is resolved. On the design side, **nothing in the bib overlaps**, so §1.1/§1.2/§1.3 (all one source, Pukelsheim's BU-943-M, plus the book at chapter granularity) are pure additions with zero duplicate risk.

---

## 3. Explicit negatives (reported, not omitted)

1. **No theorem of the form "no scalar function of the information matrix can characterize the Loewner-order feasibility of a mixture" exists in this literature — and cannot.** Refuted constructively by Pukelsheim's information-function ↔ convex-set correspondence (§1.3) and independently by Druilhet's distance-to-cone criterion (§1.7). Any no-go must restrict the class of admissible scalarizations, and the restriction must be stated as a hypothesis.
2. **No theorem "every admissible (Loewner-maximal) design is optimal for some scalar criterion" found in the design literature.** The verified implication runs the other way (§1.5). The general-position substitute is ABB (§1.6), which gives *density of properly efficient points*, not surjectivity onto the efficient frontier.
3. **The design literature's "mixture" vocabulary does not mean what the paper means by it** (§1.8) — mixtures of *criteria*, not of designs. Do not cite Gutmair 1993 as mixture-of-designs prior art.
4. **No anisotropic-floor persistent-excitation result found.** Every PE condition I verified uses an isotropic $\epsilon I$ floor, where $\lambda_{\min}$ is an exact scalar characterization. The anisotropic case appears to be open in that literature, which is good news for the paper's novelty and bad news for finding a citation to lean on.
5. **No book theorem numbers appear in this report.** SIAM epubs 403s; Internet Archive is lending-only. Chapter-level citation of Pukelsheim (2006) — Ch. 4 Loewner Optimality, Ch. 5 Real Optimality Criteria, Ch. 10 Admissibility of Moment and Information Matrices — is what I can defend, and BU-943-M (1987, open access, same author) carries the same content with statements I actually read.

---

## 4. Feedback on the brief and the framing

- **The brief was well-calibrated** — the "I may be wrong about the whole shape of it" and "regard anything off my suggestions as more interesting" framing is exactly what let me report §0 rather than assembling a bibliography around a premise. Pukelsheim was indeed the right guess, and the Loewner material is indeed there; the surprise is what it says.
- **The mathematical framing has one genuine confusion worth naming plainly:** *optimality* vs *feasibility*. Nearly all of the design literature's pessimism about the Loewner order ("partial order," "optimal designs mostly fail to exist," "scalarization is a necessity") is about **maximizing** over a set with no maximum. The paper's condition is **membership in a shifted PSD cone** — a convex feasibility question, where the Loewner order is perfectly well behaved and admits an exact concave scalar gauge. Importing the design literature's pessimism wholesale would be a category error, and a design-theory reviewer would catch it. The *right* import is §1.1 (matrix = family of directional scalars) and the concavity-under-mixture reasoning in §1.3.
- **My guess at what the author's own argument really proves** (and what I would sell): not "no scalar," but *"no per-action scalar budget, and no criterion chosen independently of $I_{\min}$."* Both are true, both are sharp, and the second is the interesting one — it says the survival floor's **anisotropy** is irreducible information that no off-the-shelf design criterion carries. That claim is stronger rhetorically than a false universal, and it is defended by literature rather than against it.
- **Highest-value unread item:** Pukelsheim 1980 on E-optimality duality (§1.8). If the paper's condition is a $\lambda_{\min}$-type gauge, the non-differentiability structure and the eigenspace-mixture dual are likely to be directly reusable, possibly as the strengthening route rather than as prior art. **→ Followed up; see §5, which supersedes this line.**
- **On neighborhoods:** these were the right two, but I'd add a third for whoever has capacity — **vector optimization / multi-objective scalarization theory** (the ABB cluster, §1.6). It, not design theory, is where impossibility-of-scalarization results actually live, and it is where a *correctly-hypothesized* no-go would find its citation.

---

# §5. Follow-up (appended same session): the E-optimality route is live machinery, not prior art

*Requested follow-up on the §1.8 flag. Short version: the survival-feasibility question **is** an E-optimal design problem, exactly and not by analogy; the E-optimality literature supplies (a) a dual infeasibility certificate, (b) a published theorem giving the precise dividing line between "a scalar suffices" and "no scalar suffices," (c) a published counterexample where the matrix-optimal design is optimal for **no** scalar criterion, and (d) a verified strict duality gap showing the natural scalar surrogate is one-sided. It also forces a **correction** to one of my own §2.1 claims and to the "three literatures stop at the same boundary" novelty argument. Rungs as before.*

## 5.0 Correction first: whitening dissolves the anisotropy, so the novelty is not anisotropy

I flagged in §2.1 (and the merged doc has amplified) that every literature stops where the floor becomes anisotropic. **That framing is wrong when $I_{\min}\succ0$ and is known in advance.** The congruence $M \mapsto \tilde M = I_{\min}^{-1/2} M I_{\min}^{-1/2}$ is linear and invertible, maps NND onto NND, preserves the Loewner order in both directions, and commutes with mixtures:

$$\widetilde{\mathbb E_\pi[I_o(a)]} = \mathbb E_\pi\big[\tilde I_o(a)\big], \qquad \bar I(\pi)\succeq I_{\min} \iff \mathbb E_\pi[\tilde I_o(a)] \succeq I.$$

So the anisotropic-floor problem *is* the isotropic-floor problem in whitened coordinates. Anisotropy per se is not the hard part and is not the novelty; claiming three literatures "go silent" on it would be an overclaim a reviewer can dismiss in one line. **Where the reduction genuinely fails, and where the novelty therefore has to live:**

1. **$I_{\min}$ singular / rank-deficient** — only some directions need protecting. No inverse square root; see §5.4, which is exactly Pukelsheim's parameter-subsystem theory.
2. **$I_{\min}$ not known in advance / drift-dependent** — the gauge is built *from* the floor, so a floor that moves with the environment means the criterion moves too.
3. **The genuinely hard part, which survives whitening intact:** whether the *max-min value* is $\ge1$, and whether a scalar criterion can certify it. That is the E-optimality problem, and it is hard for reasons that have nothing to do with anisotropy — eigenvalue multiplicity and non-differentiability. That is where §5.2–5.3 land, and it is a much better novelty story because it is a *structural* obstruction rather than a gap in coverage.

## 5.1 The exact correspondence, and the dual infeasibility certificate

Dictionary (mine, elementary, but the whole point): design point $x$ ↔ action $a$; design/measure $\xi$ ↔ policy $\pi$; $H(x)=f(x)f(x)^\top$ ↔ $\tilde I_o(a) = I_{\min}^{-1/2}H^\top R_o(a)^{-1}H I_{\min}^{-1/2}$; moment matrix $M(\xi)=\int H\,d\xi$ ↔ $\mathbb E_\pi[\tilde I_o(a)]$; E-optimality ↔ maximizing the survival margin. Hence

$$\text{survival feasible} \iff \max_\pi \lambda_{\min}\big(\mathbb E_\pi[\tilde I_o(a)]\big) \;\ge\; 1,$$

and the left side is *literally the E-optimal value* of a design problem whose design space is the action space. The paper's condition is therefore not merely analogous to E-optimality — it is E-optimality with a threshold.

**Dual certificate — [VERIFIED-TEXT]** (R. Harman, *Removal of the points that do not support an E-optimal experimental design*, arXiv:1808.00731, extracted and read):

> **Lemma 1.** Let $\xi\in\Xi$, such that $M(\xi)\in\mathcal M$ is nonsingular. Then $M(\xi)$ is E-optimal in $\mathcal M$ if and only if there exists a nonnegative definite $m\times m$ matrix $E$ with $\operatorname{tr}(E)=1$ such that $\operatorname{tr}(AE)\le\lambda_1(M(\xi))$ for all $A\in\mathcal M$. In the case of optimality, $\operatorname{tr}(AE)=\lambda_1(M(\xi))$ for any $A\in\mathcal M$ that is E-optimal.
>
> In fact, the matrix $E$ is given by $\sum_{i=1}^k \alpha_i u_iu_i^\top$ for some weights $\alpha_i$ and eigenvectors $u_i$ [orthonormal eigenvectors corresponding to $\lambda_1(M)$, $\alpha_i\ge0$, $\sum\alpha_i=1$].

Harman attributes this to **Pukelsheim (1993), Theorem 7.21** and Chapter 7 — **[SECONDARY]**: I verified that Harman states and uses it with that number, not the book itself. (Same for **Theorem 8.5** = the Elfving-set result, cited by Harman.)

**Immediate consequence for the paper (mine, from the verified lemma).** Minimax/LP-duality form:

$$\max_\pi \lambda_{\min}\big(\mathbb E_\pi[\tilde I_o(a)]\big) \;=\; \min_{E\succeq0,\ \operatorname{tr}E=1}\ \max_{a\in\mathcal A}\ \operatorname{tr}\big(\tilde I_o(a)\,E\big).$$

So: **survival is infeasible if and only if there exists a single PSD matrix $E$ with $\operatorname{tr}E=1$ such that $\operatorname{tr}(\tilde I_o(a)E) < 1$ for every action $a$.** That $E$ is a *mixture over directions* ($\sum\alpha_i u_iu_i^\top$) — a one-matrix, checkable certificate of doom, and the natural formal object behind "the agent cannot survive because there is a direction-mixture no action informs." This is a strengthening of what the brief described (a hand-built no-go) into a necessary-and-sufficient characterization with a published home, and it is the single most reusable thing in this appendix.

## 5.2 The dividing line: multiplicity of $\lambda_{\min}$ — **[VERIFIED-TEXT]**

**Source read in full:** F. Pukelsheim and W. J. Studden, *E-Optimal Designs for Polynomial Regression*, **The Annals of Statistics 21(1) (March 1993), 402–415**, JSTOR stable URL <http://www.jstor.org/stable/3035598>; open-access author copy at <https://www.math.uni-augsburg.de/htdocs/emeriti/pukelsheim/1993b.pdf>. Transcribed (OCR: `θ`→`6`/`O`, `ξ`→`f`/`e`, `λ`→`A`):

> **THEOREM 2.1.** Let $\xi$ be a design that has a positive definite information matrix $C$ for $K'\theta$, and let $\pm z\in\mathbb R^s$ be an eigenvector corresponding to the smallest eigenvalue of $C$. **If the smallest eigenvalue of $C$ has multiplicity one, then $\xi$ is E-optimal for $K'\theta$ if and only if $\xi$ is optimal for $z'K'\theta$.**

> PROOF. **By Theorem 8 of Pukelsheim (1980)**, if the smallest eigenvalue of $C$ is simple, then $\xi$ is E-optimal for $K'\theta$ if and only if there exists a generalized inverse $G$ of $M(\xi)$ such that $(z'K'Gf(x))^2 \le \lambda_{\min}(C)$ for all $x\in\mathcal X$. By the same theorem, the condition is necessary and sufficient for optimality for $z'K'\theta$.

**This answers the "which theorem in Pukelsheim 1980" question at rung [SECONDARY]: it is Theorem 8**, and its content is the generalized-inverse characterization quoted above. I still have not opened Pukelsheim (1980) — ScienceDirect 403s — but the number and the substance are now attested by Pukelsheim's own later paper, which is a much better footing than my earlier recollection.

**Why this is the result the author was hunting, in its only true form.** It is an exact dichotomy on the multiplicity of the minimal eigenvalue at the candidate optimum:

- **multiplicity one ⟹ the matrix criterion collapses to a single scalar criterion.** E-optimality $\equiv$ c-optimality in the one direction $z$. A scalar *does* suffice, and it is the eigendirection of the binding constraint.
- **multiplicity $\ge2$ ⟹ no such collapse, and it can fail completely** (§5.3).

For the paper this is a gift, because the multiplicity has a direct operational reading: **the multiplicity of $\lambda_{\min}$ at the optimal policy is the number of directions that must be excited simultaneously**, and it is exactly the number of terms in the certificate $E=\sum_i\alpha_iu_iu_i^\top$. "Forced exploration must be directional and must be a *mixture*" is precisely the statement that the multiplicity exceeds one. That converts the paper's qualitative thesis into a spectral quantity with a published theorem behind it.

## 5.3 The published counterexample: matrix-optimal, optimal for **no** scalar criterion — **[VERIFIED-TEXT]**

Same paper, immediately following Theorem 2.1, verbatim:

> In general, E-optimality may obtain without any scalar optimality property. For $K=I_k$ and $f(x)=(\sin x,\cos x)'$, with $x\in(0,2\pi]$, the only E-optimal design for $\theta$ has moment matrix $I_2/2$. But for every vector $0\ne c\in\mathbb R^k$ the unique optimal design for $c'\theta$ has moment matrix $cc'/\|c\|^2$. See Example 5 of Pukelsheim (1981).

**This is as close as the literature gets to the theorem the brief asked for, and it is the honest version of it.** In dimension 2, actions on the circle, rank-one information per action: the unique matrix-optimal object is a genuine **mixture** ($I_2/2$), while *every* scalar-direction criterion is uniquely optimized by a **degenerate rank-one** design. So the mixture that meets the matrix condition is reachable by no scalar-direction criterion whatsoever — and the failure is not a technicality, it is the generic situation once $\lambda_{\min}$ is degenerate.

Note how closely the witness matches the paper's own setting: action-indexed rank-one observation information $f(a)f(a)^\top$ on a circle of directions, no single action informative in all directions, uniform mixing required. If the author wants a worked example, **this one is published, minimal, in the right dimension, and already in the right vocabulary** — and citing it is strictly better than inventing a fresh witness. Follow-on pointer: **Example 5 of Pukelsheim (1981)** — **[SECONDARY]**, cited by Pukelsheim & Studden; the 1981 paper is presumably *On c- and E-optimal design of experiments* (Statistics/Ser. Statistics) — **title [RECALLED-UNVERIFIED], do not cite without checking.**

Caveat to state honestly if this is used: the example shows the matrix-optimal design is not *optimal for* any scalar criterion of c-type. It does **not** contradict §0 — the gauge $\varphi_{I_{\min}}$ still *characterizes feasibility* exactly. The two coexist because "characterizing the feasible set" and "being the argmax of a directional criterion" are different asks. Keeping that distinction visible is what will make the paper's claim survive review.

## 5.4 The singular-floor case is Pukelsheim's parameter-subsystem theory — **[VERIFIED-TEXT]**

From the same paper's setup:

> Let the parameter system of interest be $K'\theta$ where the $k\times s$ matrix $K$ has full column rank $s$. With a design $\xi$ we associate the information matrix $C_K(M(\xi))$ for $K'\theta$, given by $C_K(M(\xi)) = \min_{L\in\mathbb R^{s\times k}:\,LK=I} L\,M(\xi)\,L'$ — see Gaffke (1987). A design is called E-optimal for $K'\theta$ when it maximizes the smallest eigenvalue of the information matrix [among competing designs].

This is the machinery for case (1) of §5.0. A rank-deficient floor $I_{\min}=KK^\top$ ("protect only the directions in range $K$") is not a whitening problem; it is a **design-for-a-subsystem** problem, and $C_K(\cdot)$ — the Schur-complement-style minimum above — is the object that replaces $\tilde M$. Everything in §5.1–5.3 is stated by Pukelsheim & Studden *for $K'\theta$ already*, so the whole apparatus (dual certificate, multiplicity dichotomy, counterexample) transfers to the rank-deficient floor without modification. Likewise Pukelsheim's Theorem 5 in §1.1 was stated for $K'\theta$ with possibly rank-deficient $K$. **If the paper's floor is or could be singular, this is the route, and it is fully covered by existing theory** — which is a citation win and a de-risking of the singular case, at the cost of that case not being novel either.

## 5.5 The natural scalar surrogate is one-sided, with a verified strict gap — **[VERIFIED-TEXT]**

Same paper:

> **THEOREM 2.2.** Every design $\xi$ with information matrix $C$ for $K'\theta$ and every vector $0\ne z\in\mathbb R^s$ fulfill (1) $\lambda_{\min}(C) \le \big(\|z\|/p(Kz)\big)^2$. If a design $\xi$ and a vector $z\ne0$ satisfy (1) with equality, then [$\xi$ is E-optimal] for $K'\theta$ and every E-optimal design $\xi$ for $K'\theta$ is also optimal for $z'K'\theta$.

with $p$ the Elfving-set gauge ($p(c)=\inf\{\mu\ge0 : c\in\mu\mathcal E\}$, $\mathcal E=\operatorname{conv}\{\pm f(x)\}$) and $r$ the **in-ball radius** of the Elfving set. The paper's own framing of the gap, verbatim:

> There is a certain duality, but the kernel which relates the two problems to each other is convex in both variables. **Hence duality gaps cannot be ruled out.** Theorem 2.2 essentially states that duality holds true provided there exists a saddle-point.

> In Example 5 of Pukelsheim (1981) the E-optimal value for $\theta$, $v=1/2$, is **strictly smaller** than the squared in-ball radius, $r^2=1$. In other instances, the two are equal. The following theorem implies the general inequality $v\le r^2$.

Also verified: **Corollary 2.3** — if the E-optimal design's $\lambda_{\min}$ has multiplicity one, then (1) holds with equality (no gap). And the saddle-point remark: equality means $(z/\|z\|, M(\xi))$ is a saddle point of $(d,M)\mapsto d'K'M^{-1}Kd$, a kernel that is *convex in both variables* (Marshall & Olkin 1979, 16.E.7.f) — which is why the saddle point can fail to exist.

**Why this matters more than it looks.** The in-ball radius $r^2$ of the Elfving set is *the* natural scalar surrogate for the matrix condition — a single geometric number summarizing "how much information is available in the worst direction." Theorem 2.2 says it is always an **upper** bound on the achievable margin, i.e. an *optimistic* surrogate, and Example 5 gives a **verified factor-of-two strict gap** ($v=1/2$ vs $r^2=1$). Operationally: a scalar surrogate of this kind can **soundly certify infeasibility** ($r^2<1\Rightarrow$ doomed) but can **falsely certify feasibility** ($r^2\ge1$ with $v<1$). That one-sidedness, with a published witness of strictness and a published sufficient condition for tightness (multiplicity one, Cor. 2.3), is a far more defensible and more interesting claim than "no scalar works."

**BibTeX-ready:**
- `@article{pukelsheim-studden-1993-e-optimal, author={Pukelsheim, Friedrich and Studden, William J.}, title={E-Optimal Designs for Polynomial Regression}, journal={The Annals of Statistics}, volume={21}, number={1}, pages={402--415}, year={1993}, publisher={Institute of Mathematical Statistics}, jstor={3035598}}` — all fields **[VERIFIED-TEXT]** from the article's own header. Likely `doi={10.1214/aos/1176349033}` (matches the projecteuclid `euclid.aos/1176349033` identifier seen in search) — **[VERIFIED-ABSTRACT]**, worth one check.
- `@article{harman-2018-removal, author={Harman, Radoslav}, title={Removal of the points that do not support an E-optimal experimental design}, journal={arXiv preprint}, eprint={1808.00731}, year={2018}}` — journal version not verified; author name **[VERIFIED-TEXT]** from the PDF byline.
- `@article{pukelsheim-1980-maximize-information, author={Pukelsheim, Friedrich}, title={On linear regression designs which maximize information}, journal={Journal of Statistical Planning and Inference}, volume={4}, number={4}, pages={339--364}, year={1980}}` — **still not opened.** Page range remains **[RECALLED-UNVERIFIED]**. What *is* now attested **[SECONDARY]** is that its **Theorem 8** is the E-optimality characterization used above, and that it contains an **Example 6.2.2** (degree-2 polynomial regression, cited by Pukelsheim & Studden alongside Kiefer 1974 p. 868).
- `@article{gaffke-1987, author={Gaffke, Norbert}, year={1987}}` — cited by Pukelsheim & Studden for the $C_K(M)=\min_{LK=I}LML'$ formula; full details **not verified**.

## 5.6 Verdict on the strengthening question, and the residual negative

**Not a dead end — the strongest strengthening route found tonight.** Concretely available to the author, all with published homes:

1. Recast survival feasibility as an E-optimal design problem on whitened action information (§5.1). Exact, not analogical.
2. State the necessary-and-sufficient infeasibility certificate $\exists E\succeq0,\operatorname{tr}E=1,\ \max_a\operatorname{tr}(\tilde I_o(a)E)<1$ (§5.1). This is the theorem-shaped object his hand-built no-go was reaching for, and it is *stronger* (iff, with a constructive witness).
3. Cite Pukelsheim & Studden **Theorem 2.1** for the exact dividing line (multiplicity one ⟹ a scalar suffices) and the **$(\sin x,\cos x)$ example** for matrix-optimal-but-no-scalar-optimality (§5.2–5.3). The restricted claim is true, published, and sharper than the universal one.
4. Cite **Theorem 2.2** + **Corollary 2.3** for the one-sidedness of the in-ball scalar surrogate, with the verified strict gap $v=1/2<r^2=1$ (§5.5).
5. If the floor may be singular, use $C_K(\cdot)$ and inherit all of the above verbatim (§5.4).

**The residual negative, stated because it is real: the eigenvalue-crossing obstruction is genuine, not an artifact of the problem setup.** Non-differentiability of $\lambda_{\min}$ at multiplicity $\ge2$ is intrinsic — it is why E-optimality is the awkward member of the $\Phi_p$ family (Harman: *"the lack of differentiability and strict concavity also means that the deletion method for E-optimality requires special attention... a slightly more complicated and less powerful deletion method compared to those for other $\Phi_p$-criteria"* — **[VERIFIED-TEXT]**), why duality gaps cannot be ruled out (§5.5), and why the subgradient is a *set* of direction-mixtures rather than a gradient. The author should expect no clean first-order characterization at the interesting optima, and should treat the multiplicity as the object of study rather than an obstacle to smooth away. That is also the honest reason his instinct ("a scalar cannot do this") was pointing at something true: at multiplicity $\ge2$ there is no single direction, and the certificate is irreducibly a mixture.

## 5.7 The two lower-priority items

- **(a) Automatica 1996 excitation performance-limitation paper — still unresolved, deliberately not guessed.** Tried: direct ScienceDirect abstract page and PDF (403 both), and two targeted metadata searches including author-name probes. Search results repeat the abstract content but never surface authors, volume, or pages; one listing places related work by "Anderson, Ydstie, Kosut, and Rohrs" *in its reference list*, which is exactly the kind of adjacency that invites a wrong attribution — so I am naming no authors. Status: **PII 0005109895001638, Automatica, received 1995 / published 1996, authors unknown to me.** Two minutes of library access closes it; it should not be cited until then.
- **(b) ABB / vector-optimization cluster — my judgment is: do not spend more on it tonight.** Having now seen §5.2–5.3, the design literature turns out to hold the *sharper* instrument: a dichotomy theorem plus a minimal published counterexample, both in the exact vocabulary of information matrices. ABB remains the right home for the general mechanism and the right caveat (density of properly-efficient points), but it is a framework, not an impossibility theorem, and anything it would give is weaker and more abstract than Pukelsheim & Studden Theorem 2.1 + the circle example. The merged doc's current treatment of it is accurate; leave it there.
