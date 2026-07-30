#!/usr/bin/env python3
"""EXP1 -- state-independent scalars collapse to a constant action, and for
k>=2 the LMI is satisfiable by a mixture with no single action feasible."""
import numpy as np
from diag_survival import *

np.set_printoptions(precision=4, suppress=True)

# n = k = 2, both axes drift.
q  = np.array([0.5, 0.5])
R2 = 4.0
V  = [np.array([1.0, 0.0]),      # a0: informs axis 0 only
      np.array([0.0, 1.0]),      # a1: informs axis 1 only
      np.array([0.02, 0.02])]    # a2: weak isotropic (decoy, below floor)
P0 = np.array([0.5, 0.5])
imin = imin_diag(q, R2)
print("iota_min per axis      :", imin)
for i, v in enumerate(V):
    print(f"  action {i}: v={v}  per-action LMI (v>=imin)? {bool(np.all(v>=imin))}")

for p in [0.5]:
    mix = p * V[0] + (1 - p) * V[1]
    print(f"mixture 50/50 of a0,a1 : {mix}   LMI satisfied? {bool(np.all(mix>=imin))}")

print("\n-- fixed schedules --")
for name, sched in [("constant a0", [0] * 200),
                    ("constant a1", [1] * 200),
                    ("constant a2", [2] * 200),
                    ("alternating a0,a1", [0, 1] * 100)]:
    ok, hist = sim(P0, q, V, sched, R2)
    print(f"{name:22s} survives={ok!s:5s}  died at t={len(hist) if not ok else '-'}"
          f"  max-eig at end={hist[-1]:.3f}")

print("\n-- greedy on state-independent scalars --")
for name, phi in [("Tr(I_o)", phi_trace),
                  ("Tr(Pi I_o Pi)", phi_trace_proj),
                  ("lambda_min(drift blk)", phi_lmin_proj),
                  ("normalised lambda_min", lambda P, q, v, R2: phi_norm_lmin(P, q, v, R2, imin))]:
    ok, chosen, hist = greedy(P0, q, V, R2, 200, phi)
    print(f"{name:24s} survives={ok!s:5s} actions used={sorted(set(chosen))}"
          f" died at t={len(hist) if not ok else '-'}")

print("\n-- greedy on state-DEPENDENT myopic scalars --")
for name, phi in [("-lambda_max(P+)", phi_lmax_next),
                  ("-log det P+", phi_logdet),
                  ("-Tr(P+)", phi_trace_next),
                  ("info gain", phi_infogain)]:
    ok, chosen, hist = greedy(P0, q, V, R2, 200, phi)
    print(f"{name:24s} survives={ok!s:5s} actions used={sorted(set(chosen))}"
          f" died at t={len(hist) if not ok else '-'}")
