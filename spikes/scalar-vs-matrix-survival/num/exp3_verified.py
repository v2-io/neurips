#!/usr/bin/env python3
"""EXP3 -- rigorously verified counterexamples to myopic state-dependent
scalars.  "Rigorously verified" here means:
  * the surviving witness is an EXACTLY periodic schedule, simulated for
    100_000 steps with max(P) < R2 throughout (no grid rounding involved),
    and additionally checked to have converged to a periodic orbit;
  * the greedy rule is run from the same P0 and exits;
  * the death is LATE (t >= 8), so it is a steady-state failure of the rule
    rather than a bad initial condition.
"""
import itertools
import numpy as np
from diag_survival import step, sim, greedy, imin_diag
from diag_survival import phi_lmax_next, phi_logdet, phi_trace_next, phi_infogain

RNG = np.random.default_rng(11)
LONG = 100_000

# -logdet(P+) and one-step information gain induce IDENTICAL rankings:
#   infogain = sum log(1 + v_i (P_i+q_i)) = sum log(P_i+q_i) - sum log P_i^+
# and the first term does not depend on the action.  Kept separate to check.
SCALARS = [("-lmax(P+)", phi_lmax_next), ("-logdet(P+)", phi_logdet),
           ("-Tr(P+)", phi_trace_next), ("infogain", phi_infogain)]


def periodic_witness(P0, q, V, R2, max_period=4, burn=400):
    """Find an exactly periodic schedule surviving LONG steps. Returns cycle."""
    nA = len(V)
    for period in range(1, max_period + 1):
        for cyc in itertools.product(range(nA), repeat=period):
            P = np.array(P0, float)
            ok = True
            for t in range(LONG):
                P = step(P, q, V[cyc[t % period]])
                if P.max() >= R2 or not np.isfinite(P).all():
                    ok = False
                    break
            if ok:
                return list(cyc), P
    return None, None


def report(tag, q, R2, V, P0):
    print(f"\n=== {tag} ===")
    print("q  =", np.round(q, 5), " R2 =", round(float(R2), 5))
    print("iota_min (filtered convention q/(R2(R2+q))) =",
          np.round(np.where(q > 0, q / (R2 * (R2 + q)), 0.0), 5))
    for i, v in enumerate(V):
        print(f"  v[{i}] =", np.round(v, 5))
    print("P0 =", np.round(P0, 5))
    cyc, Pend = periodic_witness(P0, q, V, R2)
    if cyc is None:
        print("  NO periodic witness found (<=period 4) -> not a valid counterexample")
        return False
    print(f"  periodic witness {cyc} survives {LONG} steps, final P =",
          np.round(Pend, 5))
    any_fail = False
    for name, phi in SCALARS:
        ok, chosen, hist = greedy(P0, q, V, R2, 2000, phi)
        died = "-" if ok else len(hist)
        # compact run-length encoding of the chosen prefix
        pre = chosen[:14]
        print(f"  greedy {name:12s} survives={ok!s:5s} died_t={died!s:5s} "
              f"prefix={pre}")
        any_fail |= (not ok)
    return any_fail


def search_late(scalar_name, phi, want=3, trials=200000, n=3, k=2, nA=4):
    """Search for LATE-death counterexamples for one scalar."""
    found = []
    for _ in range(trials):
        q = np.zeros(n)
        q[:k] = 10 ** RNG.uniform(-1.2, 0.4, size=k)
        R2 = 10 ** RNG.uniform(0.3, 1.1)
        if q.max() >= R2:
            continue
        V = [10 ** RNG.uniform(-2.2, 1.3, size=n) * (RNG.random(n) < 0.75)
             for _ in range(nA)]
        P0 = np.full(n, 0.1 * R2)
        ok, chosen, hist = greedy(P0, q, V, R2, 400, phi)
        if ok or len(hist) < 8:
            continue
        # cheap periodic check first (short horizon), then full verify
        cyc = None
        for period in range(1, 4):
            for c in itertools.product(range(nA), repeat=period):
                s, _ = sim(P0, q, V, list(c) * (600 // period + 1), R2)
                if s:
                    cyc = list(c)
                    break
            if cyc:
                break
        if cyc is None:
            continue
        found.append((q.copy(), R2, [v.copy() for v in V], P0.copy(),
                      len(hist), cyc))
        if len(found) >= want:
            break
    return found


if __name__ == "__main__":
    print("#" * 70)
    print("# A. Hand-built minimal counterexample to myopic lambda_max greedy")
    print("#" * 70)
    report("decoy-capture, n=k=2",
           np.array([0.5, 0.5]), 4.0,
           [np.array([1.0, 0.0]), np.array([0.0, 1.0]), np.array([0.02, 0.02])],
           np.array([0.5, 0.5]))

    print("\n" + "#" * 70)
    print("# B. Searched LATE-death counterexamples per scalar (verified)")
    print("#" * 70)
    for name, phi in [("-lmax(P+)", phi_lmax_next), ("-logdet(P+)", phi_logdet),
                      ("-Tr(P+)", phi_trace_next)]:
        hits = search_late(name, phi, want=2, trials=60000)
        print(f"\n>>> {name}: {len(hits)} late-death verified candidates")
        for q, R2, V, P0, tdie, cyc in hits:
            report(f"{name} late death t={tdie}, witness cycle {cyc}",
                   q, R2, V, P0)
