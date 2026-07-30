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
