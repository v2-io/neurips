# Parent verification log — occupancy-weighted TV regret spike

*What the parent (main-session agent) checked first-hand, 2026-07-29, as distinct from what the spike agent or its recon sub-agent read. Written because `report.md` makes strong claims about a defect in a submitted paper, and the difference between "an agent said so" and "verified" has to survive into the record.*

## Verified first-hand by the parent

**1. App D's text says what the spike says it says.** `02-unified-convergence-rl/src/re/D-algorithm.md:7`, verbatim:

> For $N_h > 1$ MDPs, UCRL2 \cite{auer-2010-nearoptimal} and UCBVI \cite{azar-2017-minimax} give per-block cumulative trajectory-level regret $\tilde O(N_h^{3/2}\sqrt{SA L})$ with $S, A$ the state/action sizes; rewriting in the occupancy-weighted coordinate satisfies (A5) with $c$ of order $\tilde O(\sqrt{N_h SA})$, lifting cleanly to the $\tilde O(N_h^2 \sqrt{SA(B_T+1)T})$ cumulative rate

Three of the report's claims are confirmed by this sentence alone: the rate is attributed jointly to UCRL2 and UCBVI (§6a); `c` is stated **`Δ_min`-free** (§1, §3); and the `N_h²` cumulative exponent is claimed (§6b).

**2. The bandit/MDP asymmetry is real and visible in the same paragraph** — and it is sharper than the report states. The bandit half explicitly concedes the looseness:

> The $V_{\max} \cdot \operatorname{TV}$ chain is structurally one factor of $\Delta_{\min}$ looser than direct gap-aware UCB analysis … this is a feature of the unification — the framework's contribution is composition + non-stationarity-handling + identity-coordinate exactness, not a sharper bandit constant.

So the paper **already knows** the `V_max·TV` chain costs a factor of `Δ_min`, states it for the bandit case, and defends it as a deliberate tradeoff — and then the immediately following MDP sentence carries a `Δ_min`-free `c`. This corroborates the report's §4 account (the `Δ_min²` correction landed on the bandit paragraph on 2026-05-07 and the adjacent MDP sentence was left alone) from the source text rather than from the LOG.

It also matters for how the finding should be characterized: this is **not** a case of the authors being unaware that the conversion costs a gap factor. It is a case of the correction being applied to one of two adjacent claims. That is a more mundane and more believable failure, and it should be described that way rather than as a conceptual error.

## NOT verified by the parent — treat as the agent's read

Everything else, including all of these load-bearing items:

- Azar–Osband–Munos Theorem 1's exact statement and constants `[spike, first-hand]`
- Jaksch–Ortner–Auer Theorem 2 / 4 / 11, including the claim that Theorem 2's rate is `34·D S √(AT log(T/δ))` in the undiscounted average-reward setting and therefore **not** the rate App D attributes to UCRL2 `[spike, first-hand]` — *this is the crux of §6a and the parent has not opened the JMLR PDF*
- Lattimore–Szepesvári Theorem 15.2 and Eq. (15.3) `[spike, first-hand]`
- Wei–Luo Assumption 1's exact form `[spike, first-hand]`
- Tirinzoni–Pirotta–Lazaric Proposition 4 and Theorem 2 `[recon sub-agent]`
- Simchowitz–Jamieson's occupancy identity and Corollary 2.1 `[recon sub-agent]`
- Dann–Lattimore–Brunskill §3's quoted passage — the "live hazard" `[recon sub-agent]`
- Liu et al. ULI Theorems 2.6 / 3.3 `[recon sub-agent]`
- Ross–Gordon–Bagnell DAgger Theorem 2.2 `[recon sub-agent]`
- Domingues et al. Theorem 9 / Eq. (8) — **§3c, verified by nobody**, composition assembled by the recon agent and explicitly disowned by the spike. Do not cite without opening arXiv:2010.03531.
- Foster/Krishnamurthy et al. 2407.15007 Theorem 2.1 and its TV remark — **opened by a scout, read by neither** `[unverified-by-either]`
- The numerics. `gap_scaling.py` reportedly reproduces the `Σ/L ≈ 0.23` table; the parent has not run it. `ucbvi_tv.py` is reported **buggy** by the spike itself (gap enforcement produced `gapmin_realized: 0.0`) and its small-gap rows must not be used.

## What this means operationally

The **defect in App D is established** to the parent's own satisfaction: the constant is stated `Δ_min`-free, and by the paper's own admission two sentences earlier the conversion costs a `Δ_min`. That much needs no external citation.

The **magnitude and sharpness** of the correction — that no `Δ_min`-free constant can exist, that the tight dependence is `1/Δ_min`, that the honest exponent is `Θ̃(min{L, log L/Δ_min²})` rather than `√L`, and that the UCRL2 attribution is to the wrong theorem — all rest on primary sources the parent has not opened. Before any of this informs a paper, a response, or a rewrite: open Jaksch Theorem 2 and Azar Theorem 1 directly. This project has already shipped one mis-stated rate taken on an agent's summary (`02-unified-convergence-rl/LOG.md`, 2026-05-07, the Mao `(SA)^{1/3}` correction), and the spike itself notes this would be the **second** cited-rate defect in the same paper, arising by the same mechanism — the surrounding math does not depend on the prefactor, so the error survives re-reads.

The irony is worth recording: a spike investigating a citation-shaped defect returned findings that are themselves citation-shaped until someone opens the PDFs.
