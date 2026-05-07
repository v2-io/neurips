---
key: zhang-2022-online-rl
criterion: claim-supported
verifier: spike-causal-rl-stationarity-2026-05-07
outcome: verified
timestamp: 20260507T091238Z
---

B-CS1 §1 line 5 / §2 line 11 / §F line 9 / §C line 127 stationarity claim verified. Zhang-Bareinboim 2022 NeurIPS Section 2: fixed SCM M, cumulative regret R(T,M) = sum_t (E_M[Y|do(pi*)] - Y_t) against pi* fixed in M. Sublinear regret R(T,M)/T -> 0 (static-regret notion). No dynamic regret, variation budget, piecewise-stationary, or drift treatment. Confirms 'operates in stationary settings only' and 'closest causal-RL, stationary only' (the §F neighbor designation).
