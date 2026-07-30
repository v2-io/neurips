import numpy as np, math
from scipy.optimize import minimize

# 1. concavity of psi(K)=2 arccos(exp(-K/2)) and psi <= min(2 sqrt K, pi)
K=np.linspace(1e-9,60,400000)
psi=2*np.arccos(np.exp(-K/2))
print("psi<=2sqrtK everywhere:", np.all(psi<=2*np.sqrt(K)+1e-12))
print("psi<pi everywhere:", np.all(psi<math.pi))
d2=np.diff(psi,2)
print("max second difference (concave if <=0):", d2.max())
# deficit asymptotics
for I in [1,2,2.467,3,5,10,20]:
    b=2*math.acos(math.exp(-I/2)); print(f"  I={I:6.3f} psi={b:.6f} pi-psi={math.pi-b:.3e} 2exp(-I/2)={2*math.exp(-I/2):.3e} min(2sqrtI,pi)={min(2*math.sqrt(I),math.pi):.6f}")

# 2. sharpness family: partition family, Q uniform on N, P_g = Q(.|A_g), weights w
def partition_family(w):
    w=np.asarray(w,float); w=w/w.sum()
    I=-(w*np.log(w)).sum()                 # = H(w)
    rho=np.sqrt(w)                          # rho(P_g,Q)=sqrt(w_g)
    Ed=(w*2*np.arccos(rho)).sum()
    Enegloss=(w*(-np.log(rho))).sum()
    return I,Ed,Enegloss
print("\npartition family: E[-log rho] vs I/2  (should be EXACT equality for any w)")
for w in [[.5,.5],[.7,.2,.1],[.25]*4,np.random.dirichlet(np.ones(7))]:
    I,Ed,En=partition_family(w); print(f"  I={I:.6f} E[-log rho]={En:.6f} I/2={I/2:.6f} diff={En-I/2:.2e}  Ed={Ed:.6f} psi(I)={2*math.acos(math.exp(-I/2)):.6f}")

# 3. uniform partition => I=log N, check Ed == psi(I) exactly
print("\nuniform partition (I=log N): Ed vs psi(I)")
for N in [2,3,5,10,100,1000]:
    I=math.log(N); Ed=2*math.acos(1/math.sqrt(N)); print(f"  N={N:5d} I={I:.5f} Ed={Ed:.9f} psi={2*math.acos(math.exp(-I/2)):.9f} 2sqrtI={2*math.sqrt(I):.5f}")

# 4. numerically maximize E d_FR subject to I = target, over discrete models
# model: G uniform on n goals, P_g on m atoms (n x m matrix rows sum 1)
def solve(target_I,n=3,m=6,tries=40):
    best=-1
    for _ in range(tries):
        x0=np.random.randn(n*m)
        def unpack(x):
            A=np.exp(x.reshape(n,m)); return A/A.sum(1,keepdims=True)
        def obj(x):
            P=unpack(x); Q=P.mean(0)
            rho=(np.sqrt(P*Q)).sum(1)
            return -(2*np.arccos(np.clip(rho,0,1))).mean()
        def con(x):
            P=unpack(x); Q=P.mean(0)
            return (P*np.log(np.clip(P,1e-300,None)/Q)).sum(1).mean()-target_I
        r=minimize(obj,x0,constraints=[{'type':'eq','fun':con}],method='SLSQP',
                   options={'maxiter':800,'ftol':1e-12})
        if r.success and abs(con(r.x))<1e-7 and -r.fun>best: best=-r.fun
    return best
print("\nsup E d_FR at fixed I (numeric, n=3 goals, m=6 atoms) vs psi(I)")
for tI in [0.2,0.5,0.693147,1.0,1.098612]:
    b=solve(tI); print(f"  I={tI:.6f} numeric_sup={b:.6f} psi={2*math.acos(math.exp(-tI/2)):.6f} ratio={b/(2*math.acos(math.exp(-tI/2))):.5f}")
