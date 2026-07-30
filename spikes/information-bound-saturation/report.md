# Spike: information-bound saturation — can a `√I`-shaped bound on a bounded metric stay informative at high information?

*Run 2026-07-29 evening. Opus spike agent + a literature sub-agent working independently. Question posed independently of any paper's rebuttal needs.*

> **Provenance note.** The spike agent was blocked by harness policy from writing this file itself and returned the derivation half as text; this report was persisted by the parent from that return, verbatim in substance. `lit-prior-art.md` and the numerics (`num.py`, `num2.py`, `num2a.py`, `num3.py`) in this directory **were** written by the agent directly. The one load-bearing claim below — that the paper's own appendix already contains the conjectured fix — was **re-verified first-hand by the parent** against `03-llm-hallucinate-bound/src/re/D-track2-companions.md` lines 14, 17, 19 before this file was written.

## Headline

**The conjectured fix was already in the paper's own appendix, and the reviewer's objection is against a claim-*selection* choice rather than a mathematical gap. But the fix does not rescue informativeness at high `I`, and the abstract's claim still has to change.**

Verified in `src/re/D-track2-companions.md:14`, inside `^thm-track2-global`, verbatim:

> Tightest form: `E d_FR ≤ 2arccos(exp(−I_M/2)) ≤ min(2√I_M, π)`, by Jensen on the concave map `ψ(K) := 2arccos(exp(−K/2))`

and the proof at line 17 runs precisely the Rényi-1/2 monotonicity → `BC ≥ exp(−KL/2)` → chord-arc-identity chain, then **deliberately relaxes** it via `φ(K) ≤ 4K` to reach the quotable constant 2. [proved; independently re-derived by the spike; parent-verified against the source]

## The affinity move works but buys an asymptote, not informativeness

Replacing the threshold with the arccos form converts a hard cliff into an exponentially fast approach to the diameter:

    π − 2arccos(e^{−I/2}) = 2arcsin(e^{−I/2}) ~ 2e^{−I/2}

| `I` (nats) | bound | vs diameter `π ≈ 3.14159` |
|---|---|---|
| 2.467 | 2.550 | — |
| 5 | 2.977 | — |
| 10 | 3.128 | — |
| 20 | 3.14150 | 9e−5 short |

[proved + tabulated] So *"never formally vacuous"* is true and worth stating. *"Informative in the adversarial regime"* is not. **The spike explicitly parted company with its own literature sub-agent here**, which had concluded nothing needed softening. The parent's read: the spike is right, and this distinction is the whole substance of the finding.

## The no-go, stronger than the parent conjectured

Not "no `√I`-shaped bound works" — **no function of `I` whatsoever works.** Define `Φ(I) := sup{E_G d_FR : I(G;M|e,M⁻) = I}` over (H1) models. Then:

- `Φ(I) ≤ 2arccos(e^{−I/2})` for all `I`;
- **`Φ(log N) = 2arccos(N^{−1/2})` exactly**, for every integer `N ≥ 2`;
- hence `π − Φ(I) ≍ 2e^{−I/2}` along a grid of spacing `log(1+1/N) → 0`.

Therefore every valid bound `E d ≤ F(I)` on a diameter-`D` metric has `F ≥ Φ → D`. The vacuity is a property of the *pair* (bounded metric, unbounded information) — not of the constant, not of the coordinate, not of the proof technique. [proved; numerics agree to 9 digits for `N ≤ 1000`; off-grid `Φ ≈ 0.988–0.995·ψ` by constrained SLSQP, exact off-grid value unknown and judged not worth chasing]

**Attainment family** — found independently by both agents; the literature agent traced it to van Erven–Harremoës Thm 3's equality condition, a useful cross-check. Partition the state space; set `w_g := Q(A_g)`, `P_g := Q(·|A_g)`, `P(G=g) := w_g`. The mixture is `Q`, so this is a legitimate instance. Then `KL(P_g‖Q) = log(1/w_g)`, `ρ = √w_g`, `I = H(w)`, and

    E[−log ρ] = I/2   exactly, for every I ∈ [0,∞), with no Jensen step.

[proved; numerics to 5.6e−17 at arbitrary Dirichlet weights] Uniform `w` makes `d_FR` constant across goals, so the arc bound is **exactly attained at every `I = log N`** — i.e. in the regime under attack, on precisely the near-disjoint-support structure the paper already argues jailbreaks exploit.

## The right coordinate, and the object the high-coupling regime does admit

The right coordinate is **`D_{1/2}`**: `E_G[D_{1/2}(P_G‖Q)] ≤ I`, with equality iff `dP_g/dQ` is `Q`-a.e. constant on its support. Every other Track-2 bound (`C=2`, arccos, Hellinger) is a lossy monotone image of this one. The Hellinger companion also improves: `E Hel ≤ √(1−e^{−I/2}) < 1`, beating the current Tsybakov-based `√(I/2)` everywhere. [proved + verified on `[0,40]`]

Read as a **rate** rather than a displacement, this is what high coupling admits: the geometric-mean Bhattacharyya affinity is `≥ e^{−I/2}`, and since `ρ` is multiplicative over replicates, **transferred goal-information caps the Chernoff exponent for identifying the goal from the model state at `I/2` nats per independent observation.** No ceiling to press against; survives the `κ×𝒜` factorization unchanged; monotone in exactly what the paper cares about. [inequality proved; the Chernoff/Bayes-error reading is standard Bhattacharyya territory — **pattern, not verified against a primary source**] A tail form falls out by Markov: `P[ρ < ε] ≤ I/(2 log(1/ε))` [proved, one line] — real but weaker; a sentence, not a section.

## Closed routes — do not re-tread

- **Tightening `C`** — dead, and now *closed* rather than merely discouraged: the sup itself converges to the diameter.
- **Hunting a sharper `f`-divergence comparison than `D_{1/2} ≤ KL`** — dead, and the spike flagged this as its most useful negative *because it surprised it*. Intuition said `ρ ≥ e^{−KL/2}` must be loose, since Rényi-monotonicity equality normally forces `P=Q`. It does not: the degenerate-likelihood-ratio family gives equality at arbitrarily large divergence. The pointwise comparison is **already exactly tight**, and residual Jensen slack is exactly zero on the `log N` grid. Harremoës–Vajda joint-range work would improve things only *between* grid points — i.e. only at small `I`, i.e. only where the bound was never in trouble. (Literature agent independently confirmed via convexity of `KL = −2log(1−H²/2)` in `H²` that convexification cannot push the boundary lower.)
- **Renormalizing the metric** — §3 is normalization-invariant.
- **Track 1 (`W₂`)** — deliberately not attempted: unbounded metric, no ceiling, the question does not arise. Worth noting the asymmetry between the two tracks under this criticism is real and **favors Track 1**.
- Both routes in `A-failed-routes.md` were read first; no adjacency, no overlap.

## Novelty verdict, stated the unfavorable way

The core inequality is textbook composition. The literature agent found it printed verbatim as **Polyanskiy–Wu (7.27)**: `KL ≥ 2log(2/(2−H²))` — in a book **already in this paper's bibliography and already cited three times** — plus van Erven–Harremoës eq. (7) printing `Hel² ≤ D_{1/2} ≤ D_1 ≤ D_2 ≤ χ²` as a display. This is a real cost against the independent "composes known inequalities" criticism and **should be conceded, not dressed**.

What appears genuinely *not* off-the-shelf: the exact attainment characterization, and the sharp no-go with the `2e^{−I/2}` rate. Small, owned, present truth.

Spike's judgment, offered as judgment: the paper's novel core is the chain-rule-on-the-post-update-law identity + the `κ×𝒜` factorization + `^lem-attention-coupled`, and the Track-2 constant-chasing was never where the contribution lived.

## Four consequences for the paper

1. **`^thm-track2-global`'s sharpness claim is *understated*.** It currently says `C=2` is sharp "as `N→∞`" — a statement about `I→0`. The arccos form is *exactly attained at every `I = log N`*, i.e. in the regime under attack. Strengthen-before-soften lands here: the honest response is a **stronger theorem**, not a concession.
2. **A named no-go is available free**, sibling to the existing `^thm-no-go`. The pincer is the best narrative product of the evening: **bounded metrics saturate; unbounded chart metrics have no universal constant.** Two no-gos with a joint reading the paper currently lacks.
3. **A sentence goes false on promotion** [parent-verified at `D-track2-companions.md:19`]: it calls `d_FR ≤ 2√KL` "the cleanest possible (PI)-invariant Fisher-Rao-to-KL bound." That needs *replacing*, not supplementing. The literature agent also suspects a class defect — appendix owns the strong form, main text carries the quotable weak one — worth a sweep over the other companions [pattern, not audited].
4. **A scope fact, flagged hard *against* use as a rebuttal:** `I ≤ H(G)`, so the 2.467-nat threshold needs a goal variable carrying ≥3.56 bits (~12 equiprobable goals). The paper's own binary-goal JSD estimator has `I ≤ log 2 = 0.693`, so `2√I ≤ 1.665 < π` — vacuity is *impossible* in that protocol [proved, trivial]. True, and relevant to the estimator's scope. It is **not** an answer to the objection, since the abstract claims rich adversarial goal spaces where `H(G)` is large and the objection lands fully. The spike named deploying this as a rebuttal as exactly the evasive move the brief asked it to avoid. **Agreed — do not use it that way.**

## Citation hygiene

Do not ship `\cite[Theorem 3]{vanerven-harremoes-2014-renyi}` or `\cite[(7.27)]{polyanskiy-wu-2024-info-theory}` on either agent's reading — those are arXiv-preprint and lecture-note numbers, while the bib entries point at IEEE and Cambridge. Either pin against the published artifacts or cite numberlessly (which `D-track2-companions.md` already does, defensibly).

Two housekeeping items: `~/src/arch/asf/ref/INDEX.md` has **zero** coverage of this neighborhood; and the five PDFs pulled tonight are in a non-durable session scratchpad — they should be registered via `bin/refs` / relata if wanted.

## Feedback on the brief (spike's own, worth keeping)

The *"finding the known result is as valuable as deriving one"* framing was load-bearing for both agents — the literature agent said so unprompted, and it is why the headline came back as "your route is in your own appendix" rather than dressed as a discovery.

Two things that would have saved time, and both are instances of a standing pattern:

- The brief's reading list named `D-track2-companions.md` for "the global `C=2` statement and the `N`-point witness," which **undersold it** — that file *contains the conjectured fix, proof and all*. Finding it in the first ten minutes would have reframed the evening.
- The single most useful citation (Polyanskiy–Wu 7.27) was **off the enumerated neighborhoods** and already in the paper's own bibliography.

Standing pattern: *the paper's own appendix is a prior-art source*, and the most consequential hit arrives off the enumerated list. Parent's note to self: I enumerated search neighborhoods in that brief, which is exactly the prescription the delegation discipline warns against, and it cost real time here.
