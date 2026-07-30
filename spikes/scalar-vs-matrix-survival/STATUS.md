# STATUS — synthesis landed

**2026-07-29, resolved.** `report.md` is present. The spike agent was killed by a server-side API error at the moment it began writing it; it was resumed, asked to synthesize from surviving artifacts **without re-running anything**, and returned the document as text, which the parent persisted verbatim.

So: the numerics and prior art were produced before the interruption; the synthesis was written after it, from those artifacts. Nothing was re-run for the write-up. `report.md`'s own header states this, and §10 is marked *unfinished at interruption* rather than resolved.

## Verification state — read before quoting

The parent has verified **nothing** in `report.md` first-hand beyond the existence of the files it cites. Two layers of second-hand sit inside it:

- Prior-art marks (`[VERIFIED — full text]`, `[VERIFIED-abstract]`, `[lead]`, `[RECALLED, UNVERIFIED]`) are a **recon sub-agent's**, preserved verbatim because the spike declined to translate marks it could not audit.
- The Marelli / Theorem 14 material in §10 is second-hand *to the spike as well* — it arrived after the spike's last read of `prior-art.md`, so the spike states plainly it "cannot vouch for it at any rung." The parent has not opened arXiv:1806.08098 either. §10 is conditional throughout.

The `[PROVED]` propositions in §3 and §4 are elementary and self-contained; those are checkable by reading. The `[TESTED]` results depend on `num/`, and §5.3's percentages carry a stated soundness caveat (the viability filter admits false positives, so denominators are approximate; the negative direction is sound).
