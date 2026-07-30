#!/usr/bin/env python3
"""EXP4 -- is "the LMI is satisfiable" the right hypothesis?

In the diagonal setting the averaged-DARE floor is exact per axis:
fixed point of P = 1/(1/(P+q) + s) at P = R2 gives s_min = q/(R2 (R2+q))
(filtered-covariance convention, matching the recursion used throughout).
So "E_pi[I_o] >= I_min is satisfiable" is the LP feasibility question
   exists pi >= 0, sum pi = 1, sum_a pi_a v_{a,i} >= s_min,i for drifting i.
We ask how often that LP is feasible while NO schedule survives at all --
i.e. whether LMI-satisfiability can hold in configurations where neither a
scalar nor a matrix controller could possibly survive pathwise.
"""
import itertools
import numpy as np
from scipy.optimize import linprog
from diag_survival import step

RNG = np.random.default_rng(23)


def floor_filtered(q, R2):
    return np.where(q > 0, q / (R2 * (R2 + q)), 0.0)


def lmi_feasible(q, R2, V):
    s = floor_filtered(q, R2)
    drift = q > 0
    if not drift.any():
        return True, None
    Amat = -np.array([[v[i] for v in V] for i in np.where(drift)[0]])
    b = -s[drift]
    res = linprog(c=np.zeros(len(V)), A_ub=Amat, b_ub=b,
                  A_eq=np.ones((1, len(V))), b_eq=[1.0],
                  bounds=[(0, 1)] * len(V), method="highs")
    return bool(res.success), (res.x if res.success else None)


def viable_exact(P0, q, V, R2, depth=300, grid=200):
    """DFS with log-grid dedup; a revisit means an (approximately) sustainable
    cycle.  Returns (viable_flag, witness_cycle_or_None).  We then re-verify
    any claimed survival with an exact periodic simulation where possible."""
    def key(P):
        return tuple(np.round(np.log(np.maximum(P, 1e-14)) * grid).astype(int))
    seen = {}
    stack = [(np.array(P0, float), [])]
    while stack:
        P, path = stack.pop()
        if len(path) >= depth:
            return True, path[:12]
        k = key(P)
        if k in seen:
            return True, path[:12]
        seen[k] = True
        for a, v in enumerate(V):
            Pn = step(P, q, v)
            if Pn.max() < R2:
                stack.append((Pn, path + [a]))
    return False, None


def exact_periodic_survives(P0, q, V, R2, max_period=5, horizon=200_000):
    for period in range(1, max_period + 1):
        for cyc in itertools.product(range(len(V)), repeat=period):
            P = np.array(P0, float)
            ok = True
            for t in range(horizon):
                P = step(P, q, V[cyc[t % period]])
                if P.max() >= R2:
                    ok = False
                    break
            if ok:
                return list(cyc)
    return None


def main():
    n, k, nA = 3, 2, 4
    n_lmi, n_gap, examples = 0, 0, []
    for _ in range(30000):
        q = np.zeros(n)
        q[:k] = 10 ** RNG.uniform(-1.0, 0.5, size=k)
        R2 = 10 ** RNG.uniform(0.2, 1.0)
        if q.max() >= R2:
            continue
        V = [10 ** RNG.uniform(-2.5, 0.6, size=n) * (RNG.random(n) < 0.7)
             for _ in range(nA)]
        P0 = np.full(n, 0.05 * R2)
        feas, pi = lmi_feasible(q, R2, V)
        if not feas:
            continue
        n_lmi += 1
        vflag, _ = viable_exact(P0, q, V, R2)
        if not vflag:
            n_gap += 1
            if len(examples) < 4:
                examples.append((q.copy(), R2, [v.copy() for v in V],
                                 P0.copy(), pi.copy()))
    print(f"LMI-satisfiable configurations : {n_lmi}")
    print(f"  of which NO schedule survives: {n_gap} "
          f"({100*n_gap/max(n_lmi,1):.2f}%)")
    for q, R2, V, P0, pi in examples:
        print("\n--- LMI-satisfiable but non-viable ---")
        print("q =", np.round(q, 5), " R2 =", round(R2, 5),
              " floor =", np.round(floor_filtered(q, R2), 5))
        for i, v in enumerate(V):
            print(f"  v[{i}] =", np.round(v, 5))
        print("witness mixture pi =", np.round(pi, 4),
              " averaged info =", np.round(sum(p * v for p, v in zip(pi, V)), 5))
        print("P0 =", np.round(P0, 5),
              " exact periodic survivor (<=5):",
              exact_periodic_survives(P0, q, V, R2, max_period=3, horizon=5000))


if __name__ == "__main__":
    main()
