ce## Supplementary

### Discrete-time analog ^supp-discrete

The continuous-time argument of Appendix A has a discrete-time analog. For gradient descent $x_{k+1} = x_k - \eta \nabla f(x_k)$ with step size $\eta \in (0, 2/L]$ where $L$ is the smoothness constant, the iterate satisfies $V(x_{k+1}) \leq (1 - 2\mu\eta)^k V(x_0)$.

> [!proposition] Discrete convergence ^prop-discrete
> Under the hypotheses of [[#^thm-main]] plus $L$-smoothness, gradient descent with $\eta = 1/L$ satisfies $V(x_k) \leq (1 - \mu/L)^k V(x_0)$.

Proof omitted; the argument parallels [[#^thm-main]] with summation replacing integration.

### Typography stress

Bold across letter-adjacent math: **Theorem $\Theta$ verifies** renders cleanly. Bold across digit-adjacent math via padding: **2 $\times$ 2** matrices and **3 $\times$ 3** blocks appear repeatedly. (The unpadded form `**2$\times$2**` would break pandoc—our converter handles both.)

The "smart" quotes here should render as curly: "she said" not the literal straight form. Single 'quotes' likewise. URLs render: see <https://en.wikipedia.org/wiki/Lyapunov_function> for background.

The 1985–2005 period—often called the "adaptive control renaissance"—saw the development of LMI-based design tools. Hyphens like "Lyapunov-stable" should not be promoted to en-dashes.

### Cross-reference stress

We've now referenced [[#^thm-main]], [[#^lem-lyapunov]], [[#^cor-rate]], [[#^def-smooth]], [[#^prop-discrete]], and [[#^tab-rates]]. The converter routes each to `\Cref{...}`; cleveref auto-types the noun ("Theorem", "Lemma", etc.) so the author doesn't have to remember.

### Raw-TeX escape hatch

For the rare case where kramdown's parser doesn't have a markup-shaped equivalent, the `nomarkdown` block lets us drop into raw LaTeX:

{::nomarkdown}
\begin{center}
  \fbox{Raw TeX block: \(e^{i\pi} + 1 = 0\)}
\end{center}
{:/nomarkdown}

Lint flags `nomarkdown` blocks as a soft warning—"are you sure?"—since the goal is to keep authors in markdown-shaped territory. Used sparingly, it's the last-resort hatch.
