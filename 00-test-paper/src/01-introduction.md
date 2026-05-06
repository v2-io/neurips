## Introduction

This is a test paper—its job is to exercise the pipeline, not to make a substantive claim. The Lyapunov-LMI framework[^lmi] established by \citet{boyd-1994-lmi} anchors much of the formal-methods community; \citet{anderson-1985-bursting} gave the canonical statement of bursting (i.e., transient instability under reduced persistent excitation). The latter is invoked widely as a foundational result in adaptive control textbooks \cite{anderson-1985-bursting}, alongside cellular-neuroscience work \cite{hasselmo-1995-dynamics}. Multi-cite renders compactly via natbib's `sort&compress`: \cite{anderson-1985-bursting,boyd-1994-lmi,hasselmo-1995-dynamics}.

[^lmi]: LMI = Linear Matrix Inequality. Footnote rendered via raw TeX `\footnote{}` is also fine; this is the markdown form.

The em-dash above—and this one—tests the no-spaces convention. The hyphen in "Lyapunov-LMI" tests compound-word handling. The en-dash in pages 247–258 tests numerical-range convention; the combination "the 1985–2005 cycle" exercises year ranges. Inline math: $\mu > 0$, $\nabla^2 f \succeq 0$. Special characters: Łojasiewicz, Bretagnolle–Huber, Čencov, Grönwall, Otto–Villani.

> [!todo] Authoring note
> This callout is a working note. The build pipeline strips `[!todo]` / `[!note]` / `[!info]` / `[!warning]` / `[!tip]` blocks before LaTeX generation, so they don't appear in the rendered PDF. Useful for in-source TODOs, agent notes, drafting reminders. They're entirely free.

The headline contributions are:

1. **Convergence rate.** We give an explicit Lyapunov certificate yielding exponential convergence of gradient flow under strong convexity; see [[#^thm-main]].
2. **Empirical validation.** Three first-order methods are compared in [[#^tab-rates]], confirming the rate ordering predicted by theory.
3. **Methods generalize.** The argument extends to discrete time and accelerated methods, sketched in Appendix A and Appendix B.
