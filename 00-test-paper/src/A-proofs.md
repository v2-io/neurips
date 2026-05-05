## Proofs

> [!proof] Proof of [[#^thm-main]]
> Consider the candidate Lyapunov function
> $$
> \begin{aligned}
> V(x) &= f(x) - f(x^*) \\
>      &\geq \tfrac{\mu}{2} \|x - x^*\|^2,
> \end{aligned}
> $$
> where the lower bound uses strong convexity of $f$. Differentiating along trajectories of $\dot x = -\nabla f(x)$:
> $$
> \begin{aligned}
> \dot V &= \nabla f(x)^\top \dot x \\
>        &= -\|\nabla f(x)\|^2 \\
>        &\leq -2\mu \, V(x),
> \end{aligned}
> $$
> where the final inequality uses the Polyak–Łojasiewicz condition (a consequence of strong convexity). Grönwall's inequality yields $V(t) \leq e^{-2\mu t} V(0)$, and combining with the lower bound gives the claimed exponential convergence.

> [!proof] Proof of [[#^lem-lyapunov]]
> The estimate $\dot V \leq -2\mu V$ is the inequality used in line three of the previous proof. The Polyak–Łojasiewicz condition $\|\nabla f(x)\|^2 \geq 2\mu (f(x) - f(x^*))$ follows from strong convexity by minimizing both sides of the strong-convexity inequality $f(y) \geq f(x) + \nabla f(x)^\top (y - x) + \tfrac{\mu}{2}\|y - x\|^2$ over $y$.
