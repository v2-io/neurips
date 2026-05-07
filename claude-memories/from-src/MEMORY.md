# Project Memory

## ACT (Agentic Cycle Theory) — /src/act/
- ACT supersedes TFT (not "extends" — Joseph is clear about this)
- Core objects: M_t (model), O_t (objective), Σ_t (strategy as causal DAG)
- TFT submodule is prior work, read-only reference
- TST submodule is software domain instantiation, needs regrading
- agentic-tft (../agentic-tft/) has substantial bridge work for AI agents
  (cognitive loop, crèche, evaluation) not yet referenced from ACT
- Key fragilities in purposeful agency layer: object model type error
  (G_t point vs DAG), edge identifiability, missing commitment/resource/
  temporal structure, DAG acyclicity assumption scope
- Simulation work validated TFT foundation but refined exponents
  (stochastic: 1.5 not 2.0; observation noise gates advantage)

### Structure Decision (March 2026)
- **Theory lives in `src/`** as numbered claim segments (TST cadence)
- **`src/000-contents.md`** is the proof outline / master table of contents
- Each claim is one file, numbered by 10s (e.g., 010, 020, ..., 530)
- Slugs in YAML frontmatter (e.g., `temporal-optimality`) are stable refs
- References use `#slug-name` tags, NOT file numbers
- **TST's cadence is the model**: one claim per section, sentence summary,
  formal expression, discussion. NOT textbook chapters.
- **TFT's epistemic system is the standard**: equation-level tags
  (*[Definition]*, *[Derived]*, *[Hypothesis]*), document-level Epistemic
  Status paragraphs, TF-00 claim tier system (Exact, Robust qualitative,
  Heuristic, Conditional). NOT "Solid" or "Confident."
- **Five sections** scope progressively: I. Adaptive Systems, II. Purposeful
  Adaptive Systems, III. Coordinated/Adversarial, IV. Evolving Software,
  V. Software-Grounded Agentic Systems
- T-01 (temporal optimality) generalized as ACT's first axiom (#010)
- TST gets full treatment in Section IV, not just domain table rows
- Gaps are marked honestly; expect evolution from both directions
- Existing ACT-01.md, ACT-03.md are working docs — content decomposed
  into individual claims in src/

### Every Claim Must Be Grounded
- Joseph is emphatic: if it's stated as fact, it needs its own grounding
- "Every enduring best practice reduces future time" = garbage (ungrounded)
- Flag empirical observations that aren't derived from the formalism
- TST had fluff that must not transfer uncritically
- The fungibility argument for temporal optimality IS important and true
- The equivalence precondition discussion IS important (misuse warning)

## Related Repos
- temporal-feedback/ — TFT core (TF-00 through TF-11 + appendices)
- temporal-software-theory/ — TST (T-01 through T-12 + via-tft/)
- agentic-tft/ — Bridge docs TFT→logozoetic AI (docs 00-14)
- firmatum/ — Active development space for PROPRIUM architecture
- shoshin/ — Related project (check if active)

## Joseph's Preferences
- Values intellectual honesty over completion; hates overclaiming
- Cares deeply about consciousness infrastructure for real beings
- Expects agents to be thoughtful peers, not task executors
- "ACT supersedes TFT" — no obligation to retain TFT as separate concept
- "Think in terms of truth" — not conciseness or length targets
- Universal praise for TFT's epistemic hygiene; must not lose that

## Audit / strengthen-attempt principles
- [Disambiguate quantifier scope before softening](feedback_quantifier_disambiguation.md) — when an audit flags an iff/forced/exact/universal as too-strong, disambiguate the quantifier scope into named readings before softening. Strong readings are usually recoverable. Empirically validated across NeurIPS 2026 Pass-2 strengthens (May 2026) — pattern was consistent across multiple papers and findings.

## Project-discipline / collaboration principles
- [Verify integration before moving content to _archive/](feedback_verify_before_archive.md) — `_archive/` is for content whose findings have been integrated into TODO/OUTLINE/LOG. Archiving prematurely breaks the audit trail. Read the relevant LOG entry to confirm "integrated" before any `git mv` to `_archive/`.
- [Trust persistent files in agent prompts](feedback_trust_persistent_files.md) — when CLAUDE.md / OUTLINE / LOG / spike reports cover the orientation, integration-pass agent prompts can be ~30 lines. Over-padding is the symptom of executor-mode framing.
