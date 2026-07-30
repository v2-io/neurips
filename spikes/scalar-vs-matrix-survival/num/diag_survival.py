#!/usr/bin/env python3
"""Diagonal (simultaneously-diagonalizable) survival dynamics for the
scalar-vs-matrix spike.  A=I, Q=diag(q), actions have diagonal FIM v_a.

Riccati (information form, per axis, deterministic -- independent of data):
    P_i  <- 1 / ( 1/(P_i + q_i) + v_{a,i} )
Survival: max_i P_i < R2 for all t.

Everything here is exact arithmetic on the deterministic covariance
recursion; no Monte Carlo is involved (the Riccati recursion does not
depend on realized observations).
"""
import itertools
import numpy as np


def step(P, q, v):
    return 1.0 / (1.0 / (P + q) + v)


def sim(P0, q, V, sched, R2):
    """Run a fixed action schedule (list of action indices, cycled). Returns
    (survived, trajectory of max eigenvalue)."""
    P = np.array(P0, float)
    hist = []
    for t in range(len(sched)):
        P = step(P, q, V[sched[t]])
        hist.append(P.max())
        if P.max() >= R2:
            return False, hist
    return True, hist


def greedy(P0, q, V, R2, T, phi):
    """Greedy feedback: at each step pick argmax_a phi(P, v_a). Returns
    (survived, chosen action sequence, max-eig history)."""
    P = np.array(P0, float)
    chosen, hist = [], []
    for t in range(T):
        scores = [phi(P, q, V[a], R2) for a in range(len(V))]
        a = int(np.argmax(scores))
        P = step(P, q, V[a])
        chosen.append(a)
        hist.append(P.max())
        if P.max() >= R2:
            return False, chosen, hist
    return True, chosen, hist


# ---- candidate scalar functionals -------------------------------------------
# state-independent ones ignore P entirely.
def phi_trace(P, q, v, R2):            return v.sum()
def phi_trace_proj(P, q, v, R2):       return (v * (q > 0)).sum()
def phi_lmin_proj(P, q, v, R2):
    m = q > 0
    return v[m].min() if m.any() else 0.0
def phi_norm_lmin(P, q, v, R2, imin=None):
    """lambda_min(Imin^-1/2 I_o Imin^-1/2) on the drift block: the scalar that
    exactly encodes the per-action LMI test I_o >= Imin."""
    m = q > 0
    return (v[m] / imin[m]).min() if m.any() else 0.0
# state-dependent, myopic
def phi_lmax_next(P, q, v, R2):        return -step(P, q, v).max()
def phi_logdet(P, q, v, R2):           return -np.log(step(P, q, v)).sum()
def phi_trace_next(P, q, v, R2):       return -step(P, q, v).sum()
def phi_infogain(P, q, v, R2):
    Pp = P + q
    return np.log1p(v * Pp).sum()      # 0.5 log det(I + v (P+q)) up to factor


def imin_diag(q, R2):
    """Per-axis scalar Fisher floor from the 1-D DARE at boundary P=R2:
    iota_min_i = q_i / (R2 (R2 - q_i)) for drifting axes (A=1)."""
    out = np.zeros_like(np.asarray(q, float))
    for i, qi in enumerate(np.asarray(q, float)):
        out[i] = qi / (R2 * (R2 - qi)) if qi > 0 and qi < R2 else 0.0
    return out


def exists_surviving_schedule(P0, q, V, R2, T=40, period=None):
    """Exhaustive search for a surviving schedule. If period is given, search
    periodic schedules of that period (cycled to horizon T); else DFS with
    memo-free pruning over all sequences up to depth T (small |V| only)."""
    nA = len(V)
    if period is not None:
        for cyc in itertools.product(range(nA), repeat=period):
            sched = list(cyc) * (T // period + 1)
            ok, _ = sim(P0, q, V, sched[:T], R2)
            if ok:
                return True, list(cyc)
        return False, None
    stack = [(np.array(P0, float), [])]
    while stack:
        P, path = stack.pop()
        if len(path) == T:
            return True, path
        for a in range(nA):
            Pn = step(P, q, V[a])
            if Pn.max() < R2:
                stack.append((Pn, path + [a]))
    return False, None
