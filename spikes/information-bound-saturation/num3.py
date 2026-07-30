import numpy as np, math
from scipy.optimize import minimize
np.seterr(all='ignore')
def sup(tI,n,m,tries=25):
    best=-1
    U=lambda x:(lambda A:A/A.sum(1,keepdims=True))(np.exp(np.clip(x.reshape(n,m),-40,40)))
    obj=lambda x:-(2*np.arccos(np.clip((np.sqrt(U(x)*U(x).mean(0))).sum(1),0,1))).mean()
    def con(x):
        P=U(x);Q=P.mean(0);return (P*np.log(np.clip(P,1e-300,None)/np.clip(Q,1e-300,None))).sum(1).mean()-tI
    for _ in range(tries):
        r=minimize(obj,np.random.randn(n*m)*2,constraints=[{'type':'eq','fun':con}],method='SLSQP',options={'maxiter':400,'ftol':1e-12})
        if r.success and abs(con(r.x))<1e-7: best=max(best,-r.fun)
    return best
print("I        sup~      psi       ratio   on-grid")
for tI in [0.693147,0.9,1.098612,1.3,1.60944]:
    b=max(sup(tI,n,m) for n,m in [(2,4),(3,6),(4,8)])
    p=2*math.acos(math.exp(-tI/2))
    og='yes' if min(abs(tI-math.log(N)) for N in (2,3,4,5,6))<1e-4 else 'no'
    print(f"{tI:.6f} {b:.6f} {p:.6f} {b/p:.5f}  {og}")
