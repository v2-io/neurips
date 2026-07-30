# Prior-art picture: KL/mutual-information → Bhattacharyya → Fisher-Rao spherical arc

*Literature half of the information-bound-saturation spike. Written 2026-07-29 by a research sub-agent, in parallel with `report.md` (derivation half). Audience: Joseph, deciding what changes about the paper's stated claims; and future agents who would otherwise redo this search.*

**Epistemic rungs used below:** `[VERIFIED-PRIMARY]` = I downloaded the source, extracted text, and read the statement being cited. `[SECONDHAND]` = read in a source that quotes/attributes it, but not in the original. `[PATTERN]` = structural analogy I'm confident about but did not verify in a source. `[GUESS]` = flagged speculation. `[DRY WELL]` = looked, didn't find, here's where I looked.

---

## 0. Headline — read this first, it changes the spike

**The derivation you're pursuing is already written down in the paper, in the theorem statement of Appendix D, including the concavity argument.** `[VERIFIED-PRIMARY — read the file]`

`03-llm-hallucinate-bound/src/re/D-track2-companions.md`, `^thm-track2-global` ("Track 2 global Fisher-Rao spherical-arc backstop"), contains verbatim:

> Tightest form: $\mathbb{E}\,d_{FR} \le 2\arccos\bigl(\exp(-I_M/2)\bigr) \le \min\bigl(2\sqrt{I_M},\,\pi\bigr)$, by Jensen on the concave map $\psi(K) := 2\arccos(\exp(-K/2))$ — $\psi$ is concave on $[0,\infty)$ (verifiable by $\psi'(K) = \exp(-K/2)/\sqrt{1-\exp(-K)}$ decreasing).

and its proof block already runs exactly your route: Rényi monotonicity → $\mathrm{BC} \ge e^{-\mathrm{KL}/2}$ → chord-arc identity $d_{FR} = 2\arccos \mathrm{BC}$, and then *deliberately relaxes it* via $\phi(K) := 4\arccos^2(e^{-K/2}) \le 4K$ to land on the headline constant 2.

So the honest framing of the whole spike is not "derive a new bound." It is: **the paper already owns the non-vacuous form and chose to present the relaxed one as headline.** The reviewer's saturation objection is an objection to a presentation choice, not to the theory. What changes is which inequality is promoted into the abstract, §4 main results, and the theorem headline — and whether the $\min(\cdot,\pi)$ / saturation property is stated as a feature.

I'd treat this as the load-bearing finding, above any citation question. It also means the spike should probably not be framed to Joseph or to a reviewer as a strengthening — it's a promotion of an existing appendix line.

I confirmed the numerics `[VERIFIED-PRIMARY — my own computation]`: $\psi$ is concave on $(0,20]$ (no positive second difference over 2·10⁵ grid points), $\psi(I) < \pi$ strictly for all finite $I$, $\psi(I)/2\sqrt{I} \to 1$ as $I\to0$ (0.9992 at $I=0.01$), and at the old vacuity threshold $I = (\pi/2)^2$: $\psi = 2.550$ vs $2\sqrt I = 3.1413 \approx \pi$.

---

## 1. Where D_α monotonicity in α / D_{1/2} ≤ D_1 = KL is canonically stated

`[VERIFIED-PRIMARY]` — I downloaded arXiv:1206.2459 (van Erven & Harremoës, published as IEEE Trans. IT **60**(7):3797–3820, 2014), extracted text, and read the statements.

Citable pieces, in order of usefulness to you:

1. **Theorem 3 (Increasing in the Order)**, verbatim: *"For α ∈ [0,∞] the Rényi divergence D_α(P‖Q) is nondecreasing in α. On A = {α ∈ [0,∞] | 0 ≤ α ≤ 1 or D_α(P‖Q) < ∞} it is constant if and only if P is the conditional distribution Q(· | A) for some event A ∈ F."*
   The **equality condition is the load-bearing half for you** — see §2 below. Proof is one line of Jensen on $x \mapsto x^{(\alpha-1)/(\beta-1)}$.

2. **Equation (5)**: $D_{1/2}(P\|Q) = -2\ln\bigl(1 - \tfrac{1}{2}\mathrm{Hel}^2(P,Q)\bigr)$. Since $\mathrm{BC} = 1 - \mathrm{Hel}^2/2$, this *is* $D_{1/2} = -2\ln\mathrm{BC}$ in print.

3. **Equation (7)**, the chain you actually want, printed as a display:
   $$\mathrm{Hel}^2(P,Q) \le D_{1/2}(P\|Q) \le D_1(P\|Q) \le D_2(P\|Q) \le \chi^2(P,Q).$$
   Introduced with *"It will be shown that Rényi divergence is nondecreasing in its order. Therefore, by ln t ≤ t−1, (5) and (6) imply that…"*

4. **Remark 1** confirms (5) holds on general measurable spaces, not just finite alphabets (via the Hellinger integral being an f-divergence). Worth citing if a reviewer presses on the abstract-spaces setting, which (H1) is already carrying.

**Numbering caveat, flagged explicitly** `[VERIFIED-PRIMARY that these are the arXiv numbers; NOT verified for IEEE]`: the PDF I read is the arXiv preprint (LaTeX-class header, not IEEE-typeset). Theorem 3 / eqs. (5) and (7) are the *preprint* numbers. The paper currently cites `vanerven-harremoes-2014-renyi` with IEEE volume/pages, so a `\cite[Theorem 3]{}` would be asserting IEEE numbering I have not seen. Given the project's generative-citation history, either (a) get the IEEE PDF and confirm, or (b) cite without a number ("by Rényi-divergence monotonicity in the order"), which is what `D-track2-companions.md` already does and is defensible as-is. My recommendation is (a) if it's cheap, (b) otherwise — do not let a plausible-looking "Theorem 3" into the IEEE-cited form on my word.

**Attribution note** `[SECONDHAND — read in Sason & Verdú]`: Sason–Verdú's Theorem 9 attributes the $\alpha = 1/2$ case of the KL-vs-Hellinger *ratio* bound to Birgé & Massart (7.6), with the general $\alpha \in (0,1)$ case to Haussler & Opper Lemma 4 and (6). So the statistics literature had the $\alpha=1/2$ comparison independently, earlier. If you want a non-information-theory-flavored citation for a statistics audience, that's the thread.

---

## 2. Is the sharp KL ↔ Bhattacharyya/Hellinger relation known? — Yes, and ρ ≥ e^{−KL/2} is *not* loose. It's exactly sharp.

This is the second finding I'd put weight on, and it runs the other way from your brief's framing ("presumably-loose corollary").

### 2a. The inequality is in print, in a book the paper already cites

`[VERIFIED-PRIMARY]` — Polyanskiy & Wu, *Information Theory: From Coding to Learning*, f-divergence chapter (I read the LN_fdiv.pdf lecture-note version of Ch. 7 from Polyanskiy's site). In the "collection of useful inequalities" section, under **"KL vs Hellinger", eq. (7.27)**:
$$D(P\|Q) \ge 2\log\frac{2}{2 - H^2(P,Q)}$$
which is exactly $\mathrm{KL} \ge -2\log\mathrm{BC}$, i.e. $\mathrm{BC} \ge e^{-\mathrm{KL}/2}$. The section preface says: *"Most of these inequalities are joint ranges, which means they are tight."*

`polyanskiy-wu-2024-info-theory` **is already in `llm-hallucinate-neurips-2026.extracted.bib`** and already cited in `03-setup.md`, `05-mechanism.md`, `E-proofs.md` (for the Theorem 3.4 chain rule). So this is inside the paper's own bibliography — precisely the "don't discover our own bibliography" case your brief warned about. Numbering caveat again: (7.27) is from the *lecture-note* PDF; the Cambridge book's numbering may differ `[not verified]`.

Same section also gives, as a curiosity adjacent to your composition: **(7.29)**, attributed to `[Gil10]` (Gilardoni), $\mathrm{TV} \le \sqrt{-2\ln(1 - H^2/2)} = \sqrt{D_{1/2}}$ — the same "compose through the affinity rather than through KL" move, for TV instead of the FR arc. Evidence that this composition style is standard practice rather than novel.

### 2b. Sharpness — verified, and it strengthens the paper

`[VERIFIED-PRIMARY — my own derivation + numerics; the equality condition is van Erven–Harremoës Theorem 3]`

Take any $A$ with $Q(A) = e^{-I}$ and set $P = Q(\cdot\,|\,A)$. Then
- $\mathrm{KL}(P\|Q) = \log\frac{1}{Q(A)} = I$,
- $\mathrm{BC}(P,Q) = \int_A \frac{q}{\sqrt{Q(A)}}\,d\mu = \sqrt{Q(A)} = e^{-I/2}$ — **equality**, and
- consequently $d_{FR} = 2\arccos(e^{-I/2})$ — **equality in the composed bound**, for every $I \in (0,\infty)$.

This is exactly the family van Erven–Harremoës Theorem 3 names as the equality case of $\alpha$-monotonicity ($P = Q(\cdot\,|\,A)$), which is a nice consistency check that I read the theorem right.

Two consequences worth landing in the paper:

1. **The slice-wise bound $d_{FR} \le 2\arccos(e^{-\mathrm{KL}/2})$ is pointwise exactly sharp at every value of KL** — there is no room to improve it without additional structure. That is a stronger sharpness claim than the paper currently makes.
2. **The expectation form is exactly attained too, at $I = \log N$ for every integer $N \ge 2$** `[VERIFIED-PRIMARY — my own numerics, machine-exact agreement]`. Construction: $G$ uniform on $N$ goals; partition the model alphabet into $N$ blocks; $P_{M|G=g} = Q(\cdot\,|\,\text{block }g)$ with $Q$ uniform. Then $I = \log N$, $\mathrm{BC} = N^{-1/2}$, $d_{FR} = 2\arccos(N^{-1/2})$ constant in $g$ so Jensen is tight, and $2\arccos(N^{-1/2}) = 2\arccos(e^{-I/2})$ identically (checked $N = 2,3,10,100,1000$).

   Note how this compares to the paper's existing sharpness witness in `^sec-track2-global-sharpness`, which is a *symmetric near-complement* family attaining the constant 2 only asymptotically as $N\to\infty$ (99.92% at $N=100$). The disjoint-block family above attains the *arccos form* **exactly**, at finitely many $I$ values, and it is the same "near-disjoint goal-conditional supports on a large vocabulary" structure the paper already argues jailbreaks exploit — and it saturates toward $\pi$ as $N$ grows. If the arccos form is promoted to headline, this is the witness that goes with it, and it is a cleaner story than the current one.

### 2c. The full joint range {(KL, H²)} — known machinery, no closed form found, but the direction you need is settled

`[VERIFIED-PRIMARY]` Harremoës & Vajda, "Joint Range of f-divergences" (arXiv:1001.4432; IEEE Trans. IT, July 2011). **Theorem 6** is the reduction result — I read it in the preprint: the set of $(f,g)$-divergence pairs for general distributions is determined by the two-element-set case; **Theorem 8** states any $(f,g)$-divergence pair is a convex combination of two pairs achievable on a two-element set. (The often-quoted phrasing "the joint range equals the convex hull of the binary joint range" is the standard restatement `[SECONDHAND]` — Polyanskiy–Wu state it as their **Theorem 7.8**, attributed `[HV11]`, which I did read.) A companion paper, "On Pairs of f-divergences and their Joint Range" (arXiv:1007.0097), exists in the same neighborhood `[not read]`.

`[VERIFIED-PRIMARY]` Polyanskiy–Wu work the KL-vs-TV and $H^2$-vs-TV joint ranges explicitly (their (7.18), Fig. 7.1/7.2) but for **KL vs Hellinger they give only (7.27) plus a partial converse** (a log-Sobolev/Bonami-Beckner bound requiring $Q_{\min} = \min_x Q(x)$, hence alphabet-dependent and useless for you). They also remark that for KL vs TV *"there is no known"* closed-form full-range expression. So: **I did not find a published closed form for the exact {(KL, H²)} region, and I did not find a 2-point-attainment theorem stated specifically for this pair.** `[DRY WELL — searched: Harremoës–Vajda both papers, Sason–Verdú 2016 in full text, Polyanskiy–Wu Ch. 7 in full text, plus web searches on "sharp lower bound relative entropy squared Hellinger joint range"]`

But you don't need the region. `[VERIFIED-PRIMARY — my own argument]` The direction the paper uses is *upper-bound $H^2$ (equivalently lower-bound BC) given KL*, i.e. the lower boundary of KL as a function of $H^2$. That boundary is $\mathrm{KL} = -2\log(1 - H^2/2)$: it is **attained** on 2-point-supported pairs (§2b), and it is **convex in $H^2$**, so Harremoës–Vajda convexification cannot push the full-range boundary below it. Hence (7.27) is the exact boundary in the direction that matters, and no joint-range refinement can improve the paper's bound. That is a clean "the composition is already optimal" statement, and it's the strongest thing I can hand you.

The adjacent literature on *sharp* KL/Hellinger bounds that I found is all **with side constraints** — Nishiyama, "A Tight Lower Bound for the Hellinger Distance with Given Means and Variances" (arXiv:2010.13548) and arXiv:1907.00288 on KL lower bounds given mean/variance `[SECONDHAND — read search-result abstracts only]`. Not applicable: your setting has no moment constraints.

`[SECONDHAND]` Gilardoni, "On Pinsker's and Vajda's type inequalities for Csiszár's f-divergences," IEEE Trans. IT **56**(11):5377–5386, 2010, solves the best-lower-bound-on-an-f-divergence-given-TV problem. That is the **TV**-anchored sharp theory, not the Hellinger-anchored one. It is the right citation if you ever want "sharp f-divergence-vs-TV" but it does not bear on your composition. I did not read the original.

`[VERIFIED-PRIMARY]` Sason & Verdú, "f-Divergence Inequalities" (arXiv:1508.00335; IEEE Trans. IT 2016), **Theorem 9**, bounds the *ratio* $D(P\|Q)/H_\alpha(P\|Q)$ between two continuous functions $\kappa_\alpha(\beta_2) \le D/H_\alpha \le \kappa_\alpha(\beta_1^{-1})$, where the $\beta_i$ constrain the likelihood-ratio range. Alphabet-free but **requires bounded likelihood ratio**, which your Coupled-class setting cannot assume. So: relevant neighborhood, not a usable sharpening. Worth one sentence in related work if you want to show you surveyed the sharp-f-divergence-inequality literature and explain why the ratio form doesn't apply.

---

## 3. Is the *composed* statement a named result anywhere? — No. `[DRY WELL]`

I looked for: a KL/mutual-information upper bound on a bounded metric that saturates at the diameter rather than crossing it; specifically the $2\arccos(e^{-\cdot/2})$ form; specifically a Fisher-Rao-arc-vs-mutual-information bound.

Where I looked: web searches combining `"Fisher-Rao"` / `arccos` / `Bhattacharyya affinity` / `mutual information` / `relative entropy` / `spherical`; Nielsen, "Approximation and bounding techniques for the Fisher–Rao distances" (arXiv:2403.10089) — read in extracted text; Miyamoto et al., "On Closed-Form Expressions for the Fisher–Rao Distance" (arXiv:2304.14885) `[title/abstract only]`; Polyanskiy–Wu Ch. 7 inequality catalogue in full; Sason–Verdú in full text; Harremoës–Vajda.

What I did find:

- `[VERIFIED-PRIMARY]` Nielsen 2403.10089 **eq. (4)** states the categorical Fisher–Rao distance as $\rho(p,q) = 2\arccos\sum_i\sqrt{p_iq_i}$, and **Property 1** states Fisher–Rao distances are monotone (data-processing) under stochastic kernels. That is a good, recent, clean citation for both the convention *and* the (PI)-invariance the paper leans on — currently that convention is credited to Amari–Nagaoka, which is fine, but Nielsen states it in the exact form the paper uses and adds the monotonicity property explicitly. Its own bounding sections are about *geodesic* Fisher–Rao on parametric families (Fisher–Manhattan upper bounds, isometric-embedding lower bounds) and contain nothing KL/mutual-information-flavored — no overlap with your composition.
- Nothing resembling a named "saturating information–distance inequality." My honest verdict matches your instinct: **this is a textbook composition** — one line from van Erven–Harremoës (or, equivalently, one line quoted straight from Polyanskiy–Wu (7.27)) plus the chord-arc identity plus Jensen on a concave map. It is not novel and I would state that plainly. What is *slightly* less standard, and defensible as a small contribution, is (i) the observation that the composition is exactly boundary-sharp in the needed direction (§2b/2c) and (ii) the exact-attainment witness at $I = \log N$. Those are sharpness statements, not new inequalities.

`[PATTERN — not verified in a source]` Quantum-information adjacency, in case a reviewer raises it: the same composition is folklore there, as quantum relative entropy $\ge -2\log F(\rho,\sigma)$ (sandwiched/Petz Rényi-$1/2$ $\le$ relative entropy), with the Bures angle $\arccos\sqrt F$ playing the $d_{FR}$ role and the same diameter-saturation behavior. I did not chase this to a citable theorem and do not recommend citing it — the classical statement is strictly cleaner and the paper is classical. Mentioning it only so a future agent doesn't mistake it for unexplored ground.

---

## 4. Adjacent things I tripped over that may be more load-bearing than what was asked

1. **The presentational fix may be bigger than the arccos form.** The paper's Appendix D already has the tight statement; §4/abstract carry $2\sqrt{I}$. The reviewer read the abstract. That suggests a class of defect — appendix-owns-the-strong-form, main-text-carries-the-quotable-weak-form — which is worth a sweep over the other Track 2 companions (`^thm-hellinger`, the Euclidean translations) rather than a one-line fix. I only read `D-track2-companions.md`, so this is `[PATTERN]`, not audited.

2. **The paper's own framing of "the cleanest possible (PI)-invariant bound"** in `D-track2-companions.md` says *"the bound $d_{FR} \le 2\sqrt{\mathrm{KL}}$ is the cleanest possible (PI)-invariant Fisher-Rao-to-KL bound."* Post-§2c, that sentence is now false in a specific way: $2\arccos(e^{-\mathrm{KL}/2})$ is (PI)-invariant, strictly tighter everywhere, and *boundary-optimal*. If the arccos form is promoted, that sentence needs replacing, not just supplementing — flagging it because it's exactly the kind of superseded claim that survives a promotion edit `[VERIFIED-PRIMARY — read the sentence]`.

3. **A cheap independent route to the same place, if you want a second citation:** van Erven–Harremoës (7) also gives $\mathrm{Hel}^2 \le D_{1/2} \le \mathrm{KL}$ directly, so $H^2 \le \mathrm{KL}$ without going through the log at all — weaker than $H^2 \le 2(1-e^{-\mathrm{KL}/2})$, but it's a one-symbol chain from a printed display, and it's the natural companion for the Hellinger backstop theorem `[VERIFIED-PRIMARY]`.

4. **`~/src/arch/asf/ref/INDEX.md` has none of this.** I grepped for van Erven / Harremoës / Sason / Verdú / Gilardoni / Polyanskiy / Nielsen / Amari–Nagaoka — the index is causal-inference and active-inference material; zero hits in the divergence-inequality neighborhood. `[VERIFIED-PRIMARY — grepped]` If the four PDFs I pulled are worth keeping, they're not there yet. I left them only in a session scratchpad (`/private/tmp/claude-505/…/scratchpad/`: `vE-H.pdf`, `1001.4432.pdf`, `1508.00335.pdf`, `nielsen.pdf`, `pw_fdiv.pdf`) — **not durable**; someone should re-download into `ref/` if wanted. I deliberately did not write into `ref/` since that's shared canon and not mine to edit unasked.

---

## 5. Bottom line for the claims decision

- The KL → Bhattacharyya step: **known, textbook, printed in two sources the paper already cites.** Say so plainly. `[VERIFIED-PRIMARY]`
- The composed arccos form: **not found as a named result anywhere**, and it is a two-line composition, so I would not claim novelty for the inequality. `[DRY WELL + judgment]`
- The composition **is boundary-sharp** in the direction used, with exact attainment at every $I$ slice-wise and at $I = \log N$ in expectation. This is a real, checkable, *strengthening* statement and the most citable-as-ours thing here. `[VERIFIED-PRIMARY]`
- The saturation objection is answered by promoting Appendix D's own tightest form. **Nothing needs to be softened.** `[VERIFIED-PRIMARY]`
- Numbering discipline: don't ship `\cite[Theorem 3]{vanerven-harremoes-2014-renyi}` or `\cite[(7.27)]{polyanskiy-wu-2024-info-theory}` on my reading alone — mine are preprint / lecture-note numbers, and the bib entries point at IEEE and Cambridge. Verify against those two specific published artifacts or cite numberlessly.

---

## 6. Feedback on the brief (invited)

Useful: the honest statement that a known result is as valuable as a derived one, up front, changed how I reported §2 — I'd otherwise have been tempted to present the sharpness finding as the headline rather than "your route is in your own appendix."

Two things that would have saved me time. First, the brief described the route as one *to pursue*; the route is already in `D-track2-companions.md`'s theorem statement, concavity argument included. Pointing me at `F-related-work-extended.md` and `prior-art/` (which I read) but not at `D-track2-companions.md` meant I found the decisive fact by grepping the bib for `vanerven`, incidentally, after most of the literature work was done. The general form of this, worth keeping: *the spike's own paper is a prior-art source, and the appendix that proves the theorem is a better pointer than the related-work section.*

Second, the enumeration of neighborhoods (van Erven–Harremoës, Harremoës–Vajda, Sason–Verdú, Gilardoni, Reiss/Kraft) was accurate and well-aimed — but the single most useful citation, Polyanskiy–Wu (7.27), was not on the list and is already in the paper's bibliography. Consistent with the standing note that the most consequential hit tends to arrive from off the enumerated list. Your explicit "this is my guess at neighborhoods, not a work order" is what made it comfortable to go read a lecture-note PDF that wasn't named. I did not pursue Reiss / Kraft-type bounds at all — judged them subsumed once (7.27)-plus-attainment settled the direction. That's a deliberate gap, not an oversight; if you want them covered, say so.

I'm staying on the line for follow-ups once your numerics land — in particular, if you want the IEEE / Cambridge numbering pinned down, or the $I = \log N$ witness written up in the paper's notation.
