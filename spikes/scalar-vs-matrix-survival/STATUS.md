# STATUS — synthesis report outstanding

**2026-07-29 23:20.** The spike agent was killed by a server-side API error at the moment it began writing `report.md`, so **no synthesis exists yet** for this directory. Everything else survived and is committed:

- `prior-art.md` + four neighborhood files (design/excitation, index policies, sensor scheduling, viability reduction) — ~144KB. `prior-art-sensor-scheduling.md` carries an **Appendix A** appended by a recon sub-agent with a full-text read of Marelli, Sui, Rohr & Fu (arXiv:1806.08098, *Automatica* 2019).
- `num/exp1`–`exp7` with saved output for exp6 (lookahead) and exp7 (depth-2). The scripts run; their conclusions are **not yet synthesized or reviewed by the parent**.

The agent has been resumed and asked to write the synthesis from the surviving artifacts without re-running anything. If it does not return, the prior-art files and numerics stand on their own and a future reader should treat any conclusion as **unsynthesized raw material**, not a finding.

## Do not quote these yet

Nothing in this directory has been parent-verified except the existence of the files. In particular the headline candidate from Appendix A — that the sharp boundedness condition for exogenous schedules is `K` blockwise scalar inequalities in which `E_π[I_o]` does not appear, making the paper's LMI sufficient but far from necessary — rests on a **sub-agent's** read of Marelli Theorem 14 and is marked `[V-full]` by that sub-agent, not by the parent. Verify against the PDF before it informs any claim. This project has already shipped one mis-stated rate taken on trust (see `02-unified-convergence-rl/LOG.md`, 2026-05-07).
