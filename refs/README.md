# refs/ — citation source-of-truth

Multi-agent-safe citation system for the NeurIPS umbrella. The CLI lives at `bin/refs`. This directory holds the data: per-entry YAML files, append-only verification events, the anonymization deny-list, and (eventually) cached PDFs.

## Layout

```
refs/
├── README.md                      this file
├── deny-list.yml                  anonymization vocabulary + DOIs that must not be cited
├── entries/<bibkey>.yml           one file per entry; filename is the canonical key
├── verifications/<bibkey>/        append-only directory of verification events
│   └── <ts>-<verifier>-<criterion>.md
├── pdfs/<bibkey>.pdf              registered full-text PDFs (gitignored)
└── _emitted/                      build-time outputs (gitignored)
```

## Why the structure looks like this

**Per-entry files, not one shared `.bib` file.** Three (or more) agents add citations independently. With one shared `refs.bib`, every concurrent edit is a potential bibtex syntax conflict; the fix is brittle and the failure mode is silent (a malformed entry compiles but mis-cites). With per-entry files, two agents adding distinct entries touch distinct files — git resolves trivially. Two agents editing the *same* entry surfaces as a clean single-file conflict. The shared `.bib` is recovered as a *generated* artifact via `bin/refs emit`.

**Append-only verification events, not mutable status fields.** Citation hallucination is a NeurIPS Code-of-Conduct concern; we need to know *who* verified *what* against *which criterion* and *when*. Mutable status fields lose that history (and lose it silently when overwritten). Append-only files preserve it. Filenames include a UTC timestamp + verifier + criterion, so two agents recording verifications for the same entry never collide.

**YAML, not TOML.** YAML is in the Ruby stdlib (no extra gems); the meta.md frontmatter is already YAML; agents already read/write the format. The structure is shallow enough that whitespace fragility isn't a real concern.

**Anonymization is first-class.** `refs/deny-list.yml` enumerates DOIs / authors / proper-nouns that must not appear in submitted papers. `bin/refs lint` runs the deny-list against every entry plus every key cited in any paper — surfaces before submission, not at PDF audit.

## Schema — `refs/entries/<bibkey>.yml`

```yaml
key: anderson-1985-bursting           # MUST match filename basename
type: article                         # @article / @book / @inproceedings / @incollection / @misc / @techreport / @phdthesis / @mastersthesis / @unpublished
title: Adaptive systems, lack of persistency of excitation, and bursting phenomena
authors:                              # list — no "and" joiners; importer / emitter handles BibTeX form
  - Anderson, Brian D. O.
year: 1985                            # 4-digit integer
journal: Automatica                   # type-dependent (journal / booktitle / publisher)
volume: '21'                          # quoted-string for safety; YAML number coercion is fine too
number: '3'
pages: 247--258                       # BibTeX en-dash form (LaTeX renders as en-dash)
doi: 10.1016/0005-1098(85)90058-5     # bare DOI, no URL prefix
url: ...                              # optional; for entries with no DOI
note: ...                             # optional; e.g., "Russian original 1969"
```

**Conventions inherited from the upstream `common/refs.bib`:**
- Bib keys: `firstauthor-year-shortword` (lowercase, hyphenated). Multi-author entries can extend (`boyd-ghaoui-feron-balakrishnan-1994-lmi`).
- Pages with en-dash via `--` (BibTeX rendering convention).
- DOIs without URL prefix.

## Verification — `refs/verifications/<bibkey>/<ts>-<verifier>-<criterion>.md`

Each verification act is one file. Frontmatter + free-form note:

```markdown
---
key: anderson-1985-bursting
criterion: bib-fields
verifier: joseph
outcome: verified
timestamp: 20260506T004858Z
---

DOI resolves to Automatica 21(3):247-258. Authors / year / venue match the bib
entry. Title verified against publisher landing page.
```

**Outcomes:** `verified` / `failed` / `uncertain` / `n/a`. The latest event per criterion wins; older events stay as the audit trail (never delete).

**Criteria** (defined in `bin/refs`):

| Criterion          | What it asserts                                                                          |
|--------------------|------------------------------------------------------------------------------------------|
| `bib-fields`       | Authors / year / title / venue match the published record.                               |
| `doi-resolves`     | DOI resolves to the cited paper (not redirected, not 404).                               |
| `claim-supported`  | The cited paper's text actually supports the claim it's used for.                        |
| `page-ref`         | Specific page / section reference is correct.                                            |
| `anonymization`    | Citing this entry does not violate anonymization (deny-list clean).                      |
| `no-self-cite`     | Entry is not a self-citation (does not appear on the self-cite deny-list).               |

**Overall verified** = `bib-fields` + `doi-resolves` + `anonymization` all latest-verified. `claim-supported` and `page-ref` are per-paper and surface separately (a single bib entry may be cited by multiple papers, each with its own claim/page context — those are recorded as additional events with notes scoping the verifier's pass).

## Workflow

### Adding an entry

```bash
# Pipe BibTeX on stdin (paste from publisher landing page, etc.)
echo '@article{stuart-2010-acta, ... }' | bin/refs add stuart-2010-acta

# Or scaffold an empty YAML and fill in interactively
bin/refs add stuart-2010-acta   # creates a stub at refs/entries/stuart-2010-acta.yml

# Bulk import from an existing .bib file
bin/refs import path/to/refs.bib
```

### Verifying

```bash
bin/refs verify stuart-2010-acta bib-fields --by joseph \
  --note "DOI 10.1017/S0962492910000061 resolves to Acta Numerica vol 19 pp 451-559; matches entry."

bin/refs verify stuart-2010-acta doi-resolves --by joseph
bin/refs verify stuart-2010-acta anonymization --by joseph

# Per-paper claim verification (two papers cite the same entry for different claims)
bin/refs verify stuart-2010-acta claim-supported --by paper-agent-bn8 \
  --note "B-N8 §3.2 cites Stuart 2010 Theorem 4.1 for posterior contraction; verified."

# Surface a problem
bin/refs unverify burda-edwards-storkey-klimov-2018-rnd bib-fields \
  --note "Year is 2019 (ICLR), not 2018; arXiv preprint is from 2018. Update entry then re-verify."
```

### Per-paper bib emission (build-pipeline integration)

`bin/build` reads `<paper-dir>/refs.bib`. `bin/refs emit` regenerates that file scoped to the keys actually cited in the paper:

```bash
bin/refs emit 01-tragedy-confident-agent
# wrote 01-tragedy-confident-agent/refs.bib  (47 entries; 0 missing)
```

Run `emit` whenever entries change (or wire it into `bin/build`'s preamble; see PIPELINE-TODO §C1).

### Linting before submission

```bash
bin/refs lint                       # all papers
bin/refs lint 03-llm-hallucinate-bound  # one paper
REFS_LINT_STRICT=1 bin/refs lint    # exit non-zero on any finding (CI / preflight)
```

Findings categorize as:
- `DENY` — entry violates anonymization deny-list
- `SCHEMA` — entry malformed
- `MISSING` — paper cites a key that has no entry
- `UNVERIFIED` — paper cites a key whose entry is not yet `overall verified`

### Concurrency

Two agents can run any combination of `add` / `verify` / `emit` / `lint` simultaneously without coordination as long as they don't both edit the *same* entry's YAML. Verification events carry timestamps and never overwrite — concurrent verifies serialize naturally.

## Migration from the legacy `common/refs.bib`

```bash
bin/refs import ~/src/neurips2026/common/refs.bib
# imported 164 entries; skipped 0 pre-existing.
```

The legacy bib's verification status (from `~/src/neurips2026/common/citation-verification-report.md`) is currently unverified in the new system — re-verification is needed against the actual published records. The deny-list catches anonymization issues that may have slipped the legacy pass.

## What is not (yet) here

- **Auto-fetch by DOI.** Phase 0 is manual — agents paste BibTeX on stdin or fill the YAML by hand. A future `bin/refs fetch <doi>` would call CrossRef.
- **Bib-style fingerprint dedup.** Two entries with different keys but the same DOI are not currently flagged. `bin/refs lint` could grow this.
- **PDF-to-text claim verification.** `bin/refs pdf <key> <path>` registers a PDF; nothing yet inspects the content. A future `bin/refs grep <key> <claim>` could anchor `claim-supported` verifications more rigorously.
- **Tooling for the page-ref criterion.** Currently a free-text note; could become a structured per-paper claim/page field.
