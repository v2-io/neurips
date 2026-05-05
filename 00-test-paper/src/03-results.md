## Results ^results

We validate [[#^thm-main]] numerically across three first-order methods. [[#^tab-rates]] reports empirical convergence rates.

> [!table] Empirical convergence rates (averaged over 100 trials, $\mu = 1$, $f(x) = \tfrac{1}{2}\|x\|^2 + \tfrac{1}{4}\|x\|^4$). ^tab-rates
>
> | Method           |   Rate   | Iterations to $10^{-6}$ |
> |:-----------------|:--------:|:-----------------------:|
> | Gradient descent | $0.85^t$ |       $\approx 120$     |
> | Heavy ball       | $0.62^t$ |       $\approx 45$      |
> | Nesterov         | $0.38^t$ |       $\approx 22$      |

The headline observations are:

1. **Speedup is monotone.** Each method strictly outperforms the previous on the convergence-rate axis.
2. **Iteration count tracks rate.** No method exhibits anomalous early-iteration behavior.
3. **Trends are robust.** Repeating with different random seeds reproduces the ranking.

> [!note] Implementation note
> All three methods were tuned to the optimal step size for this $\mu$; see Appendix B for sensitivity to mistuning. (This `[!note]` callout is stripped at build—use for authoring sidebars.)

These observations confirm [[#^thm-main]]'s prediction that convergence rate is set by $\mu$ alone, with method-specific accelerations layering on top. Full numerical detail is in Appendix B.
