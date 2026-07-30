#!/usr/bin/env python3
"""EXP2 -- random search over diagonal configurations for cases where a
surviving schedule exists (established by exhaustive dedup-DFS on the exact
deterministic Riccati recursion) but greedy on a given myopic state-dependent
scalar exits.  Also records how often each scalar is the sole survivor."""
import numpy as np
from diag_survival import step, greedy, imin_diag
from diag_survival import phi_lmax_next, phi_logdet, phi_trace_next, phi_infogain

RNG = np.random.default_rng(7)
T_HORIZON = 120        # greedy test horizon
DFS_DEPTH = 60         # existence-of-schedule search depth
GRID = 60              # log-grid resolution for DFS state dedup


def viable(P0, q, V, R2, depth=DFS_DEPTH):
    """True iff some action sequence keeps max(P) < R2 for `depth` steps.
    Dedup on a log-grid of P makes this effectively a viability search: any
    revisited (rounded) state has already been expanded."""
    def key(P):
        return tuple(np.round(np.log(np.maximum(P, 1e-12)) * GRID).astype(int))
    seen = set()
    stack = [(np.array(P0, float), 0)]
    while stack:
        P, d = stack.pop()
        if d >= depth:
            return True
        k = key(P)
        if k in seen:
            return True          # cycle in the dedup grid => sustainable
        seen.add(k)
        for v in V:
            Pn = step(P, q, v)
            if Pn.max() < R2:
                stack.append((Pn, d + 1))
    return False


SCALARS = [("-lmax(P+)", phi_lmax_next), ("-logdet(P+)", phi_logdet),
           ("-Tr(P+)", phi_trace_next), ("infogain", phi_infogain)]


def random_config(n=3, k=2, nA=4):
    q = np.zeros(n)
    q[:k] = 10 ** RNG.uniform(-1.2, 0.4, size=k)
    R2 = 10 ** RNG.uniform(0.3, 1.1)
    if q.max() >= R2:
        return None
    V = [10 ** RNG.uniform(-2.2, 1.3, size=n) * (RNG.random(n) < 0.75)
         for _ in range(nA)]
    P0 = np.full(n, min(0.2 * R2, 0.5 * R2))
    return q, R2, V, P0


def main():
    fails = {name: [] for name, _ in SCALARS}
    n_viable = 0
    trials = 40000
    for _ in range(trials):
        cfg = random_config()
        if cfg is None:
            continue
        q, R2, V, P0 = cfg
        if not viable(P0, q, V, R2):
            continue
        n_viable += 1
        for name, phi in SCALARS:
            ok, chosen, hist = greedy(P0, q, V, R2, T_HORIZON, phi)
            if not ok:
                fails[name].append((q, R2, V, P0, len(hist)))
    print(f"viable configurations found: {n_viable} / {trials}")
    for name, _ in SCALARS:
        print(f"  greedy {name:12s} fails on {len(fails[name]):5d} "
              f"({100*len(fails[name])/max(n_viable,1):.2f}% of viable)")
    # smallest counterexample per scalar
    for name, _ in SCALARS:
        if not fails[name]:
            continue
        q, R2, V, P0, tdie = min(fails[name], key=lambda r: r[4])
        print(f"\n--- earliest-death counterexample for {name} (died t={tdie}) ---")
        print("q   =", np.round(q, 4), " R2 =", round(R2, 4),
              " iota_min =", np.round(imin_diag(q, R2), 4))
        for i, v in enumerate(V):
            print(f"  v[{i}] =", np.round(v, 4))
        print("P0  =", np.round(P0, 4))


if __name__ == "__main__":
    main()
