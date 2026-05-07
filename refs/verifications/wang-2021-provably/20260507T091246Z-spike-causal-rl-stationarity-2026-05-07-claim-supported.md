---
key: wang-2021-provably
criterion: claim-supported
verifier: spike-causal-rl-stationarity-2026-05-07
outcome: verified
timestamp: 20260507T091246Z
---

B-CS1 §1 line 5 / §2 line 11 / §C line 127 / §D line 11 stationarity claim verified (with mild caveat: 'stationarity' here means 'stationary across episodes'). Wang-Yang-Wang 2021 NeurIPS DOVI Section 2: confounded MDP tuple (S, A, W, H, P, r) with H-step episodic horizon; transition kernels P_h and reward r_h time-indexed within episode but fixed across all K episodes (standard finite-horizon convention; not the 'non-stationary RL' sense). Regret against globally optimal fixed pi*. The online-vs-offline split is interventional-vs-observational data on the SAME SCM, not drift across rounds. No variation budget / piecewise-stationary / dynamic regret.
