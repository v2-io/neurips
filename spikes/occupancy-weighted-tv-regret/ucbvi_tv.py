#!/usr/bin/env python3
# Reason: numpy for tabular value iteration / occupancy propagation; no Ruby equivalent needed for scratch numerics.
# Measures Sum_t E[TVbar_t] for UCBVI-CH on a small tabular episodic MDP, as a function of
# episode count L and of the action gap Delta. TVbar_t = (1/H) sum_h E_{s_h ~ d_h^{pi_t}}[TV(pi*,pi_t)].
# With deterministic pi_t (argmax of optimistic Q) and deterministic pi*, TV in {0,1}, so
# TVbar_t = (1/H) sum_h P_{pi_t}(pi_t(s_h) != pi*(s_h))  -- occupancy-weighted misranking mass.
import numpy as np, sys, json

def make_mdp(S,A,H,gap,rng):
    # random transitions; rewards constructed so the Q*-action-gap is >= gap at every (h,s)
    P = rng.dirichlet(np.ones(S)*1.0, size=(S,A))
    R = rng.uniform(0,1,size=(S,A))
    return P,R

def value_iter(P,R,H):
    S,A = R.shape
    Q = np.zeros((H,S,A)); V = np.zeros((H+1,S))
    for h in range(H-1,-1,-1):
        Q[h] = R + P@V[h+1]
        V[h] = Q[h].max(1)
    return Q,V

def enforce_gap(P,R,H,gap):
    # iteratively depress non-argmax actions so min gap >= gap at all (h,s)
    for _ in range(200):
        Q,V = value_iter(P,R,H)
        worst = np.inf; changed=False
        for h in range(H):
            for s in range(P.shape[0]):
                a=Q[h,s].argmax(); d=Q[h,s,a]-np.delete(Q[h,s],a)
                worst=min(worst,d.min())
                if d.min()<gap:
                    for b in range(P.shape[1]):
                        if b!=a and Q[h,s,b]>Q[h,s,a]-gap: R[s,b]-= (gap-(Q[h,s,a]-Q[h,s,b]))+1e-9; changed=True
        if not changed: break
    R = np.clip(R,0,1)
    return R

def run(S,A,H,gap,L,seed):
    rng=np.random.default_rng(seed)
    P,R=make_mdp(S,A,H,gap,rng)
    R=enforce_gap(P,R,H,gap)
    Qs,Vs=value_iter(P,R,H)
    pistar=Qs.argmax(2)                       # (H,S)
    gapmin=min((Qs[h,s].max()-np.delete(Qs[h,s],Qs[h,s].argmax()).max()) for h in range(H) for s in range(S))
    Nsa=np.zeros((S,A)); Nsas=np.zeros((S,A,S)); Rsum=np.zeros((S,A))
    tot=0.0; curve=[]
    Lg=np.log(5*H*S*A*L*10)
    for k in range(1,L+1):
        Nc=np.maximum(Nsa,1)
        Rhat=Rsum/Nc; Phat=Nsas/Nc[:,:,None]
        Phat[Nsa==0]=1.0/S
        b=H*np.sqrt(2*Lg/Nc)                  # Chernoff-Hoeffding style bonus (UCBVI-CH)
        Vk=np.zeros((H+1,S)); pol=np.zeros((H,S),dtype=int)
        for h in range(H-1,-1,-1):
            Qk=np.minimum(H,Rhat+Phat@Vk[h+1]+b)
            pol[h]=Qk.argmax(1); Vk[h]=Qk.max(1)
        # exact occupancy of learner's policy under TRUE P
        d=np.zeros(S); d[0]=1.0
        tv=0.0
        for h in range(H):
            tv += d@(pol[h]!=pistar[h]).astype(float)
            d = d@P[np.arange(S),pol[h]]
        tot += tv/H
        # sample one episode to update counts
        s=0
        for h in range(H):
            a=pol[h,s]; r=rng.random()<R[s,a]; s2=rng.choice(S,p=P[s,a])
            Nsa[s,a]+=1; Nsas[s,a,s2]+=1; Rsum[s,a]+=r; s=s2
        if k in CHECK: curve.append((k,tot))
    return gapmin,tot,curve

CHECK=set()
if __name__=="__main__":
    S,A,H=5,3,3
    Ls=[250,1000,4000,16000,64000]
    CHECK=set(Ls)
    out={}
    for gap in [0.3,0.05,0.01,0.002]:
        agg=None
        for seed in range(4):
            g,tot,curve=run(S,A,H,gap,max(Ls),seed)
            arr=np.array([c[1] for c in curve])
            agg=arr if agg is None else agg+arr
        agg/=4
        out[gap]={"gapmin_realized":float(g),"L":Ls,"sumTV":[float(x) for x in agg],
                  "sumTV_over_sqrtL":[float(x/np.sqrt(l)) for x,l in zip(agg,Ls)],
                  "sumTV_over_L":[float(x/l) for x,l in zip(agg,Ls)]}
    print(json.dumps(out,indent=1))
