import numpy as np, math
from scipy.optimize import minimize
np.seterr(all='ignore')
# where does psi <= 2 sqrt K fail?
K=np.linspace(1e-12,60,2000000); psi=2*np.arccos(np.exp(-K/2))
bad=np.where(psi>2*np.sqrt(K)+1e-15)[0]
print("violations of psi<=2sqrtK:",len(bad), "K range:", (K[bad].min(),K[bad].max()) if len(bad) else None,
      "max excess:", (psi[bad]-2*np.sqrt(K[bad])).max() if len(bad) else 0)
# exact check with mpmath at a few small K
from mpmath import mp, mpf, acos, exp, sqrt
mp.dps=40
for k in ['1e-8','1e-4','0.01','0.1','1','2']:
    k=mpf(k); print(f"  K={k}: psi={2*acos(exp(-k/2))} 2sqrtK={2*sqrt(k)} psi-2sqrtK={2*acos(exp(-k/2))-2*sqrt(k)}")

# Hellinger analogue: Hel = sqrt(1-rho) (statistician's, in [0,1]); bound Hel<=sqrt(1-exp(-K/2))
h=lambda K: np.sqrt(1-np.exp(-K/2))
Kk=np.linspace(1e-9,40,200000); hh=h(Kk)
print("\nHel bound sqrt(1-exp(-K/2)) concave?", np.diff(hh,2).max()<=1e-12, " <1 always?", np.all(hh<1),
      " <= sqrt(K/2) (Tsybakov 2Hel^2<=KL)?", np.all(hh<=np.sqrt(Kk/2)+1e-12))
for I in [1,2,4,10]: print(f"  I={I}: Hel bound={h(np.array([I]))[0]:.6f}  Tsybakov sqrt(I/2)={math.sqrt(I/2):.6f}  ceiling=1")

# off-grid sup: unconstrained n,m search
def sup(target_I,n,m,tries=60):
    best=-1
    for _ in range(tries):
        x0=np.random.randn(n*m)*2
        U=lambda x:(lambda A:A/A.sum(1,keepdims=True))(np.exp(np.clip(x.reshape(n,m),-40,40)))
        obj=lambda x:-(2*np.arccos(np.clip((np.sqrt(U(x)*U(x).mean(0))).sum(1),0,1))).mean()
        con=lambda x:( (lambda P,Q: (P*np.log(np.clip(P,1e-300,None)/np.clip(Q,1e-300,None))).sum(1).mean())(U(x),U(x).mean(0)) )-target_I
        r=minimize(obj,x0,constraints=[{'type':'eq','fun':con}],method='SLSQP',options={'maxiter':2000,'ftol':1e-14})
        if r.success and abs(con(r.x))<1e-8: best=max(best,-r.fun)
    return best
print("\nsup E d_FR at fixed I, best over (n,m) grids, vs psi(I):")
for tI in [0.693147,0.9,1.098612,1.3,1.60944,2.0]:
    b=max(sup(tI,n,m) for n,m in [(2,4),(3,6),(4,8),(5,10)])
    p=2*math.acos(math.exp(-tI/2)); print(f"  I={tI:.6f} sup~={b:.6f} psi={p:.6f} ratio={b/p:.5f}  ongrid={'yes' if abs(tI-math.log(round(math.exp(tI))))<1e-5 else 'no'}")
