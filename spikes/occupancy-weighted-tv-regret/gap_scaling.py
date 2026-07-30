#!/usr/bin/env python3
# Reason: numpy RNG only; scratch numerics.
# Clean witness MDP: S={s0,s1,s2}, A=2 at s0 (one action elsewhere), H=2, start s0.
#   a=0 -> s1 (Bernoulli reward mean 0.5+D/2 at step 1);  a=1 -> s2 (mean 0.5-D/2)
# So Q*_0(s0,0)-Q*_0(s0,1) = D exactly; pi* deterministic; Delta_min = D > 0.
# TVbar_t = (1/H)*1[greedy_t(s0) != 0]  (occupancy is a point mass; no misranking possible at s1,s2)
# UCBVI-CH on this MDP = UCB1 with H-scaled bonus. Report Sum_t TVbar_t vs L.
import numpy as np, json, sys

def run(L, D, seed, H=2, bonus_c=1.0):
    rng=np.random.default_rng(seed)
    n=np.zeros(2); s=np.zeros(2); tot=0.0
    mu=np.array([0.5+D/2, 0.5-D/2])
    Lg=np.log(max(L,2))
    for t in range(1,L+1):
        if n.min()==0: a=int(np.argmin(n))
        else:
            ucb=s/n + bonus_c*H*np.sqrt(2*Lg/n)
            a=int(np.argmax(ucb))
        tot += (1.0/H)*(a!=0)
        r=float(rng.random()<mu[a]); n[a]+=1; s[a]+=r
    return tot

out={}
Ls=[100,400,1600,6400,25600,102400]
SEEDS=24
# regime 1: Delta tied to L (Delta = L^{-1/2})
r1=[]
for L in Ls:
    D=L**-0.5
    v=np.mean([run(L,D,sd) for sd in range(SEEDS)])
    r1.append((L,D,v,v/np.sqrt(L)))
# regime 2: fixed Delta
r2={}
for D in [0.3,0.05]:
    row=[]
    for L in Ls:
        v=np.mean([run(L,D,sd) for sd in range(SEEDS)])
        row.append((L,v,v/np.sqrt(L)))
    r2[D]=row
print(json.dumps({"delta_tied_to_L (L, Delta, sumTV, sumTV/sqrtL)":r1,
                  "fixed_delta (L, sumTV, sumTV/sqrtL)":{str(k):v for k,v in r2.items()}},indent=1))
