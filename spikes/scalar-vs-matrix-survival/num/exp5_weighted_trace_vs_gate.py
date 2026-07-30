#!/usr/bin/env python3
"""EXP5 -- the paper's own matrix bonus is a LINEAR SCALAR functional, and the
right member of its class is a min-type gate, not a weighted trace.

The paper's action rule is argmax_a [ Q_O(a) + Tr(Lambda I_o(a)) ] with
Lambda proportional to I_min (or I_min^p).  For a FIXED Lambda,
  phi_Lambda(X) := Tr(Lambda X)
is a linear scalar functional of I_o(a) alone -- state-independent.  Two
consequences tested here:

(A) In the survival-dominated regime (Q_O negligible), the whole
    Lambda-family induces a constant action, so it lies in the weakest class
    and is killed by the same k>=2 mixture configuration that kills Tr(I_o).

(B) Among state-independent scalars the class-optimal one is the normalised
    minimum eigenvalue  g(X) = lambda_min(I_min^{-1/2} X I_min^{-1/2}), whose
    superlevel set {g >= 1} is EXACTLY {X >= I_min}.  We check that the
    weighted-trace family needs a diverging exponent p to imitate g, and that
    g itself has no isotropic breakdown -- i.e. that p_crit -> infinity as the
    drift becomes isotropic is an artefact of using a LINEAR functional to
    emulate a MIN, not a fact about survival.
"""
import numpy as np
from diag_survival import step, sim, greedy, phi_trace

np.set_printoptions(precision=4, suppress=True)


def floor_filtered(q, R2):
    return np.where(q > 0, q / (R2 * (R2 + q)), 0.0)


def weighted_trace(imin, p):
    w = np.where(imin > 0, imin, 0.0) ** p
    return lambda P, q, v, R2: float(w @ v)


def norm_lmin_gate(imin):
    m = imin > 0
    return lambda P, q, v, R2: float((v[m] / imin[m]).min()) if m.any() else 0.0


print("=" * 72)
print("(A) the Lambda-family collapses on the k=2 mixture-only configuration")
print("=" * 72)
q, R2 = np.array([0.5, 0.5]), 4.0
V = [np.array([1.0, 0.0]), np.array([0.0, 1.0]), np.array([0.02, 0.02])]
P0 = np.array([0.5, 0.5])
imin = floor_filtered(q, R2)
print("imin =", imin, "  no single action satisfies v >= imin:",
      [bool(np.all(v >= imin)) for v in V])
for p in [1, 2, 4, 8]:
    ok, chosen, hist = greedy(P0, q, V, R2, 500, weighted_trace(imin, p))
    print(f"  greedy Tr(I_min^{p} I_o)  survives={ok!s:5s} "
          f"actions={sorted(set(chosen))} died_t={len(hist) if not ok else '-'}")
ok, chosen, hist = greedy(P0, q, V, R2, 500, norm_lmin_gate(imin))
print(f"  greedy normalised-lambda_min survives={ok!s:5s} "
      f"actions={sorted(set(chosen))} died_t={len(hist) if not ok else '-'}")
print("  reference: alternating [0,1] survives:",
      sim(P0, q, V, [0, 1] * 5000, R2)[0])

print()
print("=" * 72)
print("(B) anisotropy: weighted trace needs p -> inf; the gate does not")
print("=" * 72)
# n = 2, BOTH axes drift (k = 2); a drift-probe covering both axes adequately
# versus a high-magnitude action concentrated on the weaker-drift axis.
print(f"{'sigx/sigy':>10} {'imin ratio':>11} {'p_crit(trace)':>14} "
      f"{'gate picks probe':>17}")
for ratio in [8.0, 4.0, 2.0, 1.5, 1.2, 1.05, 1.0]:
    q = np.array([1.0, 1.0 / ratio ** 2])
    R2 = 6.0
    imin = floor_filtered(q, R2)
    # probe: exactly meets the floor on both axes with margin 3
    probe = 3.0 * imin
    # "near-wall": 40x the floor on the cheap axis, 0.2x on the expensive axis
    wall = np.array([0.2 * imin[0], 40.0 * imin[1]])
    # smallest integer p at which the weighted trace prefers probe over wall
    p_crit = None
    for p in range(1, 400):
        w = imin ** p
        if w @ probe > w @ wall:
            p_crit = p
            break
    g = norm_lmin_gate(imin)
    picks = "probe" if g(None, q, probe, R2) > g(None, q, wall, R2) else "WALL"
    print(f"{ratio:10.2f} {imin[0]/imin[1]:11.3f} "
          f"{str(p_crit) if p_crit else '>=400':>14} {picks:>17}")

print("""
Reading: the gate compares each action to the floor DIRECTION BY DIRECTION and
so is unaffected by how anisotropic the drift is.  The weighted trace has to
manufacture direction-sensitivity out of the anisotropy of I_min itself, which
is why its critical exponent blows up as the drift becomes isotropic.""")
