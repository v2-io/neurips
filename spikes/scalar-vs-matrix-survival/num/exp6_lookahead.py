#!/usr/bin/env python3
"""EXP6 -- is the real axis myopia rather than scalar-vs-matrix?

Two questions:
 (i)  Are there viable configurations where ALL four natural myopic scalars
      die?  (If yes, no natural member of the myopic class suffices.)
 (ii) Does receding-horizon lookahead on the SAME scalar (lambda_max) fix
      them, and how fast does the failure rate fall with horizon d?
      A depth-d rule is still "a scalar functional" in the trivial sense --
      it scores each action by a real number -- so if failure rate -> 0 with
      d, the operative variable is lookahead depth, not scalarity.
"""
import itertools
import numpy as np
from diag_survival import step, sim, greedy
from diag_survival import phi_lmax_next, phi_logdet, phi_trace_next, phi_infogain

RNG = np.random.default_rng(101)
SCALARS = [("lmax", phi_lmax_next), ("logdet", phi_logdet),
           ("trace", phi_trace_next), ("infogain", phi_infogain)]


def lookahead_greedy(P0, q, V, R2, T, depth):
    """At each step pick the action beginning the depth-d sequence that
    minimises the worst max-eigenvalue encountered over the next d steps
    (infinite penalty for exiting)."""
    nA = len(V)
    seqs = list(itertools.product(range(nA), repeat=depth))
    P = np.array(P0, float)
    for t in range(T):
        best, best_a = np.inf, 0
        for s in seqs:
            Pw, worst = P.copy(), 0.0
            for a in s:
                Pw = step(Pw, q, V[a])
                worst = max(worst, Pw.max())
                if worst >= R2:
                    break
            if worst < best:
                best, best_a = worst, s[0]
        P = step(P, q, V[best_a])
        if P.max() >= R2:
            return False, t + 1
    return True, None


def viable_cycle(P0, q, V, R2, max_period=3, horizon=3000):
    for period in range(1, max_period + 1):
        for cyc in itertools.product(range(len(V)), repeat=period):
            if sim(P0, q, V, list(cyc) * (horizon // period + 1), R2)[0]:
                return list(cyc)
    return None


def main():
    n, k, nA = 3, 2, 3
    all_fail, checked = [], 0
    for _ in range(120000):
        q = np.zeros(n)
        q[:k] = 10 ** RNG.uniform(-1.2, 0.4, size=k)
        R2 = 10 ** RNG.uniform(0.3, 1.1)
        if q.max() >= R2:
            continue
        V = [10 ** RNG.uniform(-2.2, 1.3, size=n) * (RNG.random(n) < 0.75)
             for _ in range(nA)]
        P0 = np.full(n, 0.1 * R2)
        res = [greedy(P0, q, V, R2, 300, phi)[0] for _, phi in SCALARS]
        if any(res):
            continue
        cyc = viable_cycle(P0, q, V, R2)
        if cyc is None:
            continue
        checked += 1
        all_fail.append((q.copy(), R2, [v.copy() for v in V], P0.copy(), cyc))
        if len(all_fail) >= 6:
            break
    print(f"(i) viable configs where ALL FOUR myopic scalars die: "
          f"{len(all_fail)} found")
    for q, R2, V, P0, cyc in all_fail[:3]:
        print("\n  --- all-myopic-fail instance ---")
        print("  q =", np.round(q, 5), " R2 =", round(R2, 5))
        for i, v in enumerate(V):
            print(f"    v[{i}] =", np.round(v, 5))
        print("  P0 =", np.round(P0, 5), " surviving cycle:", cyc,
              " (verified 3000 steps)")
        for d in [1, 2, 3, 4, 6]:
            ok, tdie = lookahead_greedy(P0, q, V, R2, 400, d)
            print(f"    lookahead depth {d}: survives={ok!s:5s} "
                  f"died_t={tdie if tdie else '-'}")

    print("\n(ii) failure rate of depth-d worst-case-lambda_max lookahead "
          "over viable configs")
    stats = {d: [0, 0] for d in [1, 2, 3, 4]}
    trials = 0
    for _ in range(30000):
        q = np.zeros(n)
        q[:k] = 10 ** RNG.uniform(-1.2, 0.4, size=k)
        R2 = 10 ** RNG.uniform(0.3, 1.1)
        if q.max() >= R2:
            continue
        V = [10 ** RNG.uniform(-2.2, 1.3, size=n) * (RNG.random(n) < 0.75)
             for _ in range(nA)]
        P0 = np.full(n, 0.1 * R2)
        if viable_cycle(P0, q, V, R2, max_period=3, horizon=600) is None:
            continue
        trials += 1
        if trials > 1200:
            break
        for d in stats:
            ok, _ = lookahead_greedy(P0, q, V, R2, 200, d)
            stats[d][0] += 1
            stats[d][1] += (0 if ok else 1)
    for d in sorted(stats):
        tot, bad = stats[d]
        print(f"   depth {d}: {bad}/{tot} fail ({100*bad/max(tot,1):.2f}%)")


if __name__ == "__main__":
    main()
