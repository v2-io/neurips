# Outline Strategy for Overgrown Papers

This document provides a structural blueprint and strategy for condensing the project's heavily mathematical, overgrown papers (currently 2-3x the limit) into submittable 5-10 page main texts for NeurIPS/ICML. 

The strategy is modeled after canonical, math-heavy theoretical ML papers that successfully convey the "full feel" of their results and intuition without saturating the main body with dense algebra.

## The Exemplar Papers

To understand this structural strategy in action, two archetype papers have been fetched for reference. They are incredibly math-heavy, yet their main texts fit cleanly within the page limits, delegating dozens of pages of heavy algebra to the appendix.

**Local Reference Files:**
You can find the source/PDFs for these papers in our repository:
1.  **Paper 1: *Provably Efficient Reinforcement Learning with Linear Function Approximation* (Jin et al., 2020)**
    *   Directory: `spikes/paper_structure/1907.05388/`
2.  **Paper 2: *Is Q-learning Provably Efficient?* (Jin et al., 2018)**
    *   Directory: `spikes/paper_structure/1807.03765/`

### Walkthrough of the Source Modularity

Both papers share a strict modularity:
1.  The main text never attempts to do step-by-step algebra. 
2.  The "Mechanism" or "Analysis" sections (Proof Sketches) reference lemmas defined in the appendix and string them together narratively.
3.  All heavy derivations are fully siloed into appendices.

---

## The 8-Page Blueprint

This is the recommended structural blueprint to hit the NeurIPS page limit while keeping the impact high.

### 1. Introduction (1 - 1.5 pages)
*   **The Narrative:** Start with the problem and the gap.
*   **The Informal Result:** State the main theorem informally in the introduction. Use plain English and a simplified big-$\mathcal{O}$ notation to show the outcome before the reader has to learn the notation.

**Example 1: Setting up the Narrative Gap (From *Provably Efficient RL*)**
```latex
Despite the empirical successes of function approximation in RL, most existing theoretical guarantees apply only to tabular RL [citations], in which the states and actions are discrete, and the value function is represented by a table. Due to the curse of dimensionality, only relatively small problems can be tackled by tabular RL... Thus the following fundamental question remains open: Is it possible to design provably efficient RL algorithms in the function approximation setting?
```

**Example 2: Setting up the Narrative Gap (From *Is Q-learning Provably Efficient?*)**
```latex
On the other hand it is believed that model-free algorithms suffer from a higher sample complexity compared to model-based approaches. This has been evidenced empirically in [7, 22], and recent work has tried to improve the sample efficiency... There is, however, little theory to support such blending, which requires a more quantitative understanding of relative sample complexities. Indeed, the following basic theoretical questions remain open: Can we design model-free algorithms that are sample efficient? In particular, is Q-learning provably efficient?
```

**Example 3: Informally Stating the Main Result (From *Provably Efficient RL*)**
```latex
Focusing on a linear setting in which the transition dynamics and reward function are assumed to be linear, we present the first algorithm that is provably efficient in both runtime and sample complexity... Concretely, we prove that an optimistic version of Least-Squares Value Iteration (LSVI) achieves \tilde{\mathcal{O}}(\sqrt{d^3H^3T}) regret, where d is the ambient dimension of feature space, H is the length of each episode, T is the total number of steps.
```

**Example 4: Informally Stating the Main Result (From *Is Q-learning Provably Efficient?*)**
```latex
In this paper, we answer the two aforementioned questions affirmatively. We show that Q-learning, when equipped with a UCB exploration policy that incorporates estimates of the confidence of Q values and assign exploration bonuses, achieves total regret \tilde{\mathcal{O}}(\sqrt{H^3 SAT})... Up to a \sqrt{H} factor, our regret matches the information-theoretic optimum.
```

### 2. Related Work (~0.5 pages)
*   Briefly categorize prior approaches to highlight why your mathematical framework was necessary to bridge the existing gap. Keep it conceptual; avoid defining excessive notation here.

**Example 5: Grouping Prior Work Conceptually (From *Provably Efficient RL*)**
```latex
\paragraph{Tabular RL:} Tabular RL is well studied in both model-based [citations] and model-free settings [citations]... Although these algorithms are (nearly) minimax-optimal, they can not cope with large state spaces, as their regret scales linearly in \sqrt{S}, where S is often exponentially large in practice.
```

**Example 6: Grouping Prior Work Conceptually (From *Is Q-learning Provably Efficient?*)**
```latex
With simulator. Some results assume access to a simulator [15]... When a simulator is available, model-free algorithms [2] are known to be almost as sample efficient as the best model-based algorithms.
Without simulator. Reinforcement learning becomes much more challenging without the presence of a simulator, and the choice of exploration policy can now determine the behavior of the learning algorithm...
```

### 3. Preliminaries & Setting (1 - 1.5 pages)
*   **Strict Minimalism:** This is where the math begins, but *only* define the notation and assumptions strictly required to read the Main Theorem.
*   If a variable or definition is only used during the proof, it goes in the appendix.

**Example 7: Defining the Core Setup (From *Provably Efficient RL*)**
```latex
We consider the setting of an episodic Markov decision process, denoted by \text{MDP}(\mathcal{S}, \mathcal{A}, H, \mathbb{P}, r), where \mathcal{S} and \mathcal{A} are the sets of possible states and actions, respectively, H is the length of each episode, \mathbb{P} = \{\mathbb{P}_h\}_{h=1}^H and r = \{r_h\}_{h=1}^H are the state transition probability measures and the reward functions.
```

**Example 8: Defining the Core Setup (From *Is Q-learning Provably Efficient?*)**
```latex
We consider the setting of a tabular episodic Markov decision process, MDP(\mathcal{S}, \mathcal{A}, H, \mathbb{P}, r), where \mathcal{S} is the set of states with |\mathcal{S}| = S, \mathcal{A} is the set of actions with |\mathcal{A}| = A, H is the number of steps in each episode, \mathbb{P} is the transition matrix so that \mathbb{P}_h(\cdot|x, a) gives the distribution over states...
```

**Example 9: A Rigorous, yet Understandable Assumption (From *Provably Efficient RL*)**
```latex
\begin{assumption}[Linear MDP]
\text{MDP}(\mathcal{S}, \mathcal{A}, H, \mathbb{P}, r) is a linear MDP with a feature map \phi: \mathcal{S} \times \mathcal{A} \rightarrow \mathbb{R}^d, if for any h \in [H], there exist d unknown measures \mu_h over \mathcal{S} and an unknown vector \theta_h \in \mathbb{R}^d, such that:
\mathbb{P}_h(\cdot \mid x, a) = \langle \phi(x, a), \mu_h(\cdot) \rangle, \quad r_h(x, a) = \langle \phi(x, a), \theta_h \rangle.
\end{assumption}

% Unpacking the Assumption in Plain English:
By definition, in a linear MDP, both the Markov transition model and the reward functions are linear in a feature mapping \phi. We remark that despite being linear, the Markov transition model \mathbb{P}_h(\cdot \mid x, a) can still have infinite degrees of freedom as the measure \mu_h is unknown. This is a key difference from [prior work]...
```

### 4. The Algorithm & Main Results (2 pages)
*   **The Algorithm:** Pseudocode is presented early. Spend 2-3 paragraphs giving the *intuition* behind the algorithmic design before hitting the reader with the theorem.
*   **The Formal Theorem:** The core mathematical claim is stated rigorously.
*   **The "Unpacking" (Crucial):** Immediately following the dense theorem, use bulleted **Remarks** or narrative paragraphs. This is how you convey the "feel" of the math.

**Example 10: Algorithm Intuition Before the Code (From *Is Q-learning Provably Efficient?*)**
```latex
As seen in the bandit setting, the choice of exploration policy plays an essential role in the efficiency of a learning algorithm. In episodic MDP, Q-learning with the commonly used \epsilon-greedy exploration strategy can be very inefficient... In contrast, our algorithm (Algorithm 1), which is Q-learning with an upper-confidence bound (UCB) exploration strategy, will be seen to be efficient. This algorithm maintains Q values...
```

**Example 11: Stating the Main Theorem (From *Provably Efficient RL*)**
```latex
\begin{theorem} \label{thm:main}
Under Assumption A, there exists an absolute constant c > 0 such that, for any fixed p \in (0, 1), if we set \lambda = 1 and \beta = c \cdot d H \sqrt{\iota} in Algorithm 1, then with probability 1-p, the total regret of LSVI-UCB is at most \mathcal{O}(\sqrt{d^3 H^3 T \iota^2}).
\end{theorem}
```

**Example 12: Unpacking the Theorem (From *Provably Efficient RL*)**
```latex
Theorem \ref{thm:main} asserts that when \lambda and \beta are set properly, LSVI-UCB will suffer total regret at most \tilde{\mathcal{O}}(\sqrt{d^3 H^3 T}). We emphasize that while a naive adaptation of existing linear bandit algorithms... yields a regret exponential in H, our regret is only polynomial in H. Avoiding this exponential dependency... is a key step.
```

**Example 13: Unpacking the Theorem (From *Is Q-learning Provably Efficient?*)**
```latex
Theorem 1 shows, under a rather simple choice of exploration bonus, Q-learning can be made very efficient, enjoying a \tilde{\mathcal{O}}(\sqrt{T}) regret which is optimal in terms of dependence on T. To the best of our knowledge, this is the first analysis of a model-free procedure that features a \sqrt{T} regret without requiring access to a "simulator." Compared to the previous model-based results, Theorem 1 shows that the regret... is as good as the best model-based one.
```

### 5. Mechanism / Proof Sketch (2 - 2.5 pages)
*   *This is the secret sauce for overgrown papers.* **Do not do step-by-step algebra in the main text.**
*   Write a **narrative of the proof strategy**.
*   Surface the 1 or 2 most critical **Key Lemmas** and state them formally.
*   Write paragraphs explaining the *challenges* and how these key lemmas interact to overcome them. 
*   Explicitly defer technical derivations.

**Example 14: Explicitly Deferring the Proofs at the Start (From *Is Q-learning Provably Efficient?*)**
```latex
\section{Proof for Q-learning with UCB-Hoeffding}
In this section, we provide the full proof of Theorem 1. Intuitively, the episodic MDP with H steps per episode can be viewed as a contextual bandit of H "layers." The key challenge here is to control the way error and confidence propagate through different "layers" in an online fashion... We first present an auxiliary lemma... The proof is based on simple manipulations on the definition of \alpha_t, and is provided in Appendix B.
```

**Example 15: Narratively Explaining an Algebraic Step (From *Is Q-learning Provably Efficient?*)**
```latex
\paragraph{Favoring Later Updates.} At any (x, a, h, k)... let t = N_h^k(x, a). According to (4.3), the Q value at episode k equals a weighted average of the V values of the "next states" with weights \alpha_t^1, ..., \alpha_t^t. As one can see from Figure 1, our choice of the learning rate ensures that, approximately speaking, the last 1/H fraction of the indices i is given non-negligible weights, whereas the first 1-1/H fraction is forgotten. This ensures that the information accumulates smoothly across the H layers of the MDP.
```

**Example 16: Step 1 of the Proof Sketch (Focusing on the "Why") (From *Provably Efficient RL*)**
```latex
\paragraph{Step 1: Prove \hat{\mathbb{P}}_h V_{h+1}(x, a) \approx \bar{\mathbb{P}}_h V_{h+1}(x, a) via Value-Aware Uniform Concentration.}
Computing the difference, we have... Since x^\tau_{h+1} is a sample from the distribution... we would expect this term to be small due to concentration... However, the function V_{h+1}... inevitably depends on the choices of actions... Therefore, the concentration of self-normalized process does not apply directly. To resolve this issue, we establish...
```

**Example 17: Surfacing a Key Lemma without the Proof (From *Is Q-learning Provably Efficient?*)**
```latex
We now proceed to the formal proof. We start with a lemma that gives a recursive formula for Q - Q^*, as a weighted average of previous updates.
\begin{lemma}[recursion on Q]
For any (x, a, h) \in \mathcal{S} \times \mathcal{A} \times [H] and episode k \in [K]...
\end{lemma}
Next, using Lemma 4.2 and the Azuma-Hoeffding concentration bound, our next lemma shows that Q^k is always an upper bound on Q^* at any episode k...
```

### 6. Conclusion & Future Work (~0.5 pages)
*   A brief wrap-up. Connect back to the opening narrative gap.
*   Discuss takeaways and limitations openly.

**Example 18: The Wrap-up & Practitioner Takeaways (From *Is Q-learning Provably Efficient?*)**
```latex
For practitioners, there are two key takeaways from our theoretical analysis:
1. The use of UCB exploration instead of \epsilon-greedy exploration in the model-free setting allows for better treatment of uncertainties for different states and actions.
2. It is essential to use a learning rate which is \alpha_t = O(H/t), instead of 1/t, when a state-action pair is being updated for the t-th time... This delicate choice of reweighting leads to the crucial difference between our sample-efficient guarantee versus earlier highly inefficient results.
```

**Example 19: Discussing Limitations/Future Work (From *Provably Efficient RL*)**
```latex
\paragraph{On the optimal dependencies on d and H.} Theorem 3.1 claims the total regret to be upper bounded by \tilde{\mathcal{O}}(\sqrt{d^3H^3T}). One immediate question is what the optimal dependencies on d and H are... We believe the \sqrt{H} difference between this lower bound and our upper bound is expected because the exploration bonus used in this paper is intrinsically "Hoeffding-type."
```

### 7. References (1-2 pages)
*   Standard bibliography. Ensure citation styling complies with the conference (e.g., NeurIPS numeric style).

### 8. Technical Appendix (Unlimited)
*   This is where the paper "lives" for the reviewers who want to verify the claims. 
*   It contains the formal restatements of all theorems, auxiliary lemmas, and the full mathematical machinery.

**Example 20: Structuring the Appendix Entry Point (From *Provably Efficient RL*)**
```latex
\section{Proof of Theorem 3.1} \label{app:proof_main}
In this section, we prove Theorem 3.1. We first introduce the notation that is used throughout this section. Then, we present lemmas and their proofs. Finally, we combine the lemmas to prove Theorem 3.1.
```

**Example 21: Introducing Proof Mechanisms in Appendix (From *Is Q-learning Provably Efficient?*)**
```latex
\section{Appendix B. Proof of Lemma 4.1}
In this section, we derive three important properties implied by our choice of the learning rate.
Recall the notation from (3.1) and (4.2)...
```

**Example 22: Stating Heavy Auxiliary Lemmas in the Appendix (From *Provably Efficient RL*)**
```latex
\begin{lemma}[Bound on Weights in Algorithm]\label{lem:wn_estimate}
For any (k, h) \in [K] \times [H], the weight w^k_h in Algorithm 1 satisfies:
\norm{w^k_h} \le 2H \sqrt{dk/\lambda}.
\end{lemma}
```

**Example 23: The Pure Algebra (Safely Hidden from Main Text) (From *Is Q-learning Provably Efficient?*)**
```latex
\begin{proof}
(a) The proof is by induction on t. For the base case t = 1 we have \frac{\alpha_1^1}{\sqrt{1}} = \alpha_1 = 1 so the statement holds. For t \ge 2, by the relationship \alpha_t^i = (1 - \alpha_t)\alpha_{t-1}^i for i = 1, 2, ..., t - 1 we have:
\sum_{i=1}^t \frac{\alpha_t^i}{\sqrt{i}} = \frac{\alpha_t^t}{\sqrt{t}} + (1 - \alpha_t) \sum_{i=1}^{t-1} \frac{\alpha_{t-1}^i}{\sqrt{i}}
...
\end{proof}
```

**Example 24: Detailed Pure Algebra (Safely Hidden) (From *Provably Efficient RL*)**
```latex
\begin{proof}
For any vector v \in \mathbb{R}^d, we have
|v^\top w^k_h| = |v^\top (\Lambda^k_h)^{-1} \sum_{\tau=1}^{k-1} \phi^\tau_h [r(x^{\tau}_h, a^{\tau}_h) + \max_a Q_{h+1}(x^{\tau}_{h+1}, a)]|
\le \sum_{\tau = 1}^{k-1} |v^\top (\Lambda^k_h)^{-1} \phi^\tau_h| \cdot 2H 
\le \sqrt{ \left[ \sum_{\tau = 1}^{k-1} v^\top (\Lambda^k_h)^{-1}v\right] \cdot \left [ \sum_{\tau = 1}^{k-1} (\phi^\tau_h)^\top (\Lambda^k_h)^{-1}\phi^\tau_h\right] } \cdot 2H
\le 2H \norm{v}\sqrt{dk/\lambda},
where the last step is due to Lemma 11.
\end{proof}
```

---

## Actionable Steps for the Current Papers

If your papers are currently 2-3x overgrown, the excess is likely coming from derivations and intermediate lemmas living in the main text. 

To condense them:
1.  **Audit the main text for proofs:** Move *any* proof longer than 3 lines to the appendix (as seen in Examples 23 and 24). Replace it in the main text with a "Proof Sketch" paragraph that describes the strategy (as seen in Examples 15 and 16).
2.  **Audit the Preliminaries:** Move any definition that isn't explicitly referenced in the Main Theorem statement or the Algorithm to the appendix.
3.  **Use "Remarks":** Rely heavily on Remarks right after your theorems. They bridge the gap between the dense math you've presented and the intuitive claims you want the reader to walk away with (as seen in Examples 12 and 13).