# Outline Strategy for Overgrown Papers

This document provides a structural blueprint and strategy for condensing the project's heavily mathematical, overgrown papers (currently 2-3x the limit) into submittable 5-10 page main texts for NeurIPS/ICML. 

The strategy is modeled after canonical, math-heavy theoretical ML papers that successfully convey the "full feel" of their results and intuition without saturating the main body with dense algebra.

## Exemplar Paper: *Provably Efficient Reinforcement Learning with Linear Function Approximation* (Jin et al., 2020)

To understand this structural strategy in action, an archetype paper has been fetched for reference. It is incredibly math-heavy, yet the main text fits cleanly within the page limits, delegating nearly 30 pages of heavy algebra to the appendix.

**Local Reference Files:**
You can find the LaTeX source and final PDF for this paper in our repository:
*   **Directory:** `spikes/paper_structure/1907.05388/`
*   **Main TeX File:** `mainQlin.tex`
*   **PDF:** `1907.05388.pdf`
*   **Appendix TeX:** `proofs.tex`, `proofs_mis.tex`, `app.tex`

### Walkthrough of the Source

If you look at the `mainQlin.tex` and the supporting `.tex` files, you'll see a strict modularity:
1.  `intro.tex`, `related.tex`, `setting.tex`, `results.tex`, and `mechanism.tex` make up the entirety of the main paper body.
2.  All derivations are fully siloed into `properties.tex`, `proofs.tex`, `proofs_mis.tex`, and `app.tex`.
3.  The main text never attempts to do step-by-step algebra. Instead, the `mechanism.tex` (Proof Sketch) references the lemmas defined in the appendix and strings them together narratively.

---

## The 8-Page Blueprint

This is the recommended structural blueprint to hit the NeurIPS page limit while keeping the impact high.

### 1. Introduction (1 - 1.5 pages)
*   **The Narrative:** Start with the problem and the gap.
*   **The Informal Result:** State the main theorem informally in the introduction. Use plain English and a simplified big-$\mathcal{O}$ notation to show the outcome before the reader has to learn the notation.

### 2. Related Work (~0.5 pages)
*   Briefly categorize prior approaches to highlight why your mathematical framework was necessary to bridge the existing gap.

### 3. Preliminaries & Setting (1 - 1.5 pages)
*   **Strict Minimalism:** This is where the math begins, but *only* define the notation and assumptions strictly required to read the Main Theorem.
*   If a variable or definition is only used during the proof, it goes in the appendix.

### 4. The Algorithm & Main Results (2 pages)
*   **The Algorithm:** Pseudocode is presented early. Spend 2-3 paragraphs giving the *intuition* behind the algorithmic design before hitting the reader with the theorem.
*   **The Formal Theorem:** The core mathematical claim is stated rigorously.
*   **The "Unpacking" (Crucial):** Immediately following the dense theorem, use bulleted **Remarks**. This is how you convey the "feel" of the math. The remarks explicitly tell the reader what the math means: *"Remark 1: Our bound scales linearly with $d$, not $S$."*

### 5. Mechanism / Proof Sketch (2 - 2.5 pages)
*   *This is the secret sauce for overgrown papers.* **Do not do step-by-step algebra in the main text.**
*   Write a **narrative of the proof strategy**.
*   Surface the 1 or 2 most critical **Key Lemmas** and state them formally.
*   Write paragraphs explaining the *challenges* and how these key lemmas interact to overcome them. 
*   Explicitly defer technical derivations (e.g., *"The full proof of Lemma 2, which requires carefully constructing a covering argument over the feature space, is deferred to Appendix B."*).

### 6. Conclusion & Future Work (~0.5 pages)
*   A brief wrap-up.

### 7. References (1-2 pages)

### 8. Technical Appendix (Unlimited)
*   This is where the paper "lives" for the reviewers who want to verify the claims. It contains the formal restatements of all theorems, auxiliary lemmas, and the full mathematical machinery.

---

## Actionable Steps for the Current Papers

If your papers are currently 2-3x overgrown, the excess is likely coming from derivations and intermediate lemmas living in the main text. 

To condense them:
1.  **Audit the main text for proofs:** Move *any* proof longer than 3 lines to the appendix. Replace it in the main text with a "Proof Sketch" paragraph that describes the strategy.
2.  **Audit the Preliminaries:** Move any definition that isn't explicitly referenced in the Main Theorem statement or the Algorithm to the appendix.
3.  **Use "Remarks":** Rely heavily on Remarks right after your theorems. They bridge the gap between the dense math you've presented and the intuitive claims you want the reader to walk away with.
