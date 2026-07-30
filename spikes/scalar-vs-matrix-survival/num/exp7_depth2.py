#!/usr/bin/env python3
"""EXP7 -- can depth-2 worst-case-lambda_max lookahead be defeated?

exp6 found that depth 2 repaired every instance in its ensemble, including all
configurations where all four myopic (depth-1) surrogates failed.  Two probes:
 (A) a wider random ensemble (more axes, more actions, harsher parameters);
 (B) a DESIGNED family: a round-robin "commitment" structure where the fatal
     choice is only visible d+1 steps out, so depth d cannot see it.  If (B)
     works for arbitrary d, no fixed finite lookahead suffices.
"""
import itertools
import numpy as np
from diag_survival import step, sim

RNG = np.random.default_rng(4242)


def lookahead(P0, q, V, R2, T, depth):
    seqs = list(itertools.product(range(len(V)), repeat=depth))
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


def viable_cycle(P0, q, V, R2, max_period=4, horizon=4000):
    for period in range(1, max_period + 1):
        for cyc in itertools.product(range(len(V)), repeat=period):
            if sim(P0, q, V, list(cyc) * (horizon // period + 1), R2)[0]:
                return list(cyc)
    return None


print("=" * 70)
print("(A) wider random ensemble: depth-2 failures among viable configs")
print("=" * 70)
hits = []
scanned = 0
for _ in range(200000):
    n = int(RNG.integers(3, 6))
    k = int(RNG.integers(2, n))
    nA = int(RNG.integers(3, 5))
    q = np.zeros(n)
    q[:k] = 10 ** RNG.uniform(-1.5, 0.6, size=k)
    R2 = 10 ** RNG.uniform(0.1, 1.0)
    if q.max() >= R2:
        continue
    V = [10 ** RNG.uniform(-2.5, 1.5, size=n) * (RNG.random(n) < 0.6)
         for _ in range(nA)]
    P0 = np.full(n, 0.1 * R2)
    scanned += 1
    ok2, t2 = lookahead(P0, q, V, R2, 150, 2)
    if ok2:
        continue
    cyc = viable_cycle(P0, q, V, R2, max_period=3, horizon=1500)
    if cyc is None:
        continue
    hits.append((q, R2, V, P0, t2, cyc))
    if len(hits) >= 3:
        break
print(f"scanned {scanned}; depth-2 failures on viable configs: {len(hits)}")
for q, R2, V, P0, t2, cyc in hits:
    print("\n  q =", np.round(q, 4), " R2 =", round(R2, 4))
    for i, v in enumerate(V):
        print(f"    v[{i}] =", np.round(v, 4))
    print("  P0 =", np.round(P0, 4), " witness cycle", cyc)
    for d in [1, 2, 3, 4]:
        ok, td = lookahead(P0, q, V, R2, 300, d)
        print(f"    depth {d}: survives={ok!s:5s} died_t={td if td else '-'}")

print()
print("=" * 70)
print("(B) designed round-robin commitment family, m drifting axes")
print("=" * 70)
for m in [2, 3, 4, 5]:
    q = np.full(m, 0.5)
    R2 = 4.0
    V = [np.eye(m)[i] * 8.0 for i in range(m)]
    eps = 0.9 * (q[0] / (R2 * (R2 + q[0])))     # just below the per-axis floor
    V.append(np.full(m, eps))
    P0 = np.full(m, 0.4)
    cyc = list(range(m))
    ok_rr, _ = sim(P0, q, V, cyc * (4000 // m + 1), R2)
    row = [f"m={m}", f"roundrobin_survives={ok_rr!s:5s}"]
    for d in [1, 2, 3]:
        ok, td = lookahead(P0, q, V, R2, 200, d)
        row.append(f"d{d}:{'ok' if ok else 'DIE@' + str(td)}")
    print("  " + "  ".join(row))
