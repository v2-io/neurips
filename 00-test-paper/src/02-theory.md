## Theory

Let $f: \mathbb{R}^n \to \mathbb{R}$ be a smooth function. We adopt the following definition.

> [!definition] $\mathcal{C}^k$-smoothness ^def-smooth
> A function $f$ is *$\mathcal{C}^k$-smooth* if all partial derivatives up to order $k$ exist and are continuous on the relevant domain.

The principal claim is the following.

> [!theorem] Main convergence result ^thm-main
> For any $\mathcal{C}^2$-smooth $f$ with $\nabla^2 f \succeq \mu I$ and $\mu > 0$, the gradient flow $\dot{x} = -\nabla f(x)$ converges to the unique minimizer at exponential rate determined by $\mu$.

The proof relies on a Lyapunov estimate.

> [!lemma] Lyapunov estimate ^lem-lyapunov
> Under the hypotheses of [[#^thm-main]], $V(x) = f(x) - f(x^*)$ satisfies $\dot V \leq -2\mu V$ along trajectories.

The convergence rate then follows immediately.

> [!corollary] Exponential rate ^cor-rate
> $\|x(t) - x^*\| \leq e^{-\mu t} \|x(0) - x^*\|$ for all $t \geq 0$.

The full argument appears in Appendix A; numerical validation appears in [[#^results]].

> [!remark] Sharpness
> The rate $\mu$ is tight in the worst case—a quadratic $f(x) = \tfrac{\mu}{2}\|x\|^2$ achieves equality in [[#^cor-rate]] when initialized away from the origin. Faster rates require structural assumptions beyond strong convexity (e.g., relative smoothness, restricted strong convexity).
