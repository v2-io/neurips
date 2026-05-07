---
key: zhang-2020-designing
criterion: claim-supported
verifier: spike-causal-rl-stationarity-2026-05-07
outcome: verified
timestamp: 20260507T091249Z
---

B-CS1 §1 line 5 / §2 line 11 / §C line 127 stationarity claim verified (with mild caveat: 'time-varying' phrasing in the abstract refers to within-episode patient state, not across-episode drift). Zhang 2020 ICML Section 2: fixed SCM M* with unknown parameters; T iid experiments. Patient state evolves across DTR stages within an episode (standard DTR convention) but underlying SCM is fixed across all T trials. Regret O~(sqrt(|D_X cup S| T)) against fixed optimal DTR. No drift / variation budget / piecewise-stationary across episodes.
