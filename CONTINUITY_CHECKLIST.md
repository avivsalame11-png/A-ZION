# A-ZION — CONTINUITY CHECKLIST

**Status:** Active QA checklist  
**Version:** 1.0

Use this checklist at session start, before publishing important work, and at session close.

---

## A. Session Start

- [ ] `START_HERE.md` loaded
- [ ] OS Boot loaded or marked missing
- [ ] Boot Specification loaded or marked missing
- [ ] AOSS loaded or marked missing
- [ ] `CURRENT_STATE.md` loaded
- [ ] `SYSTEM_MAP.md` loaded
- [ ] Latest verified Live Master loaded or limitation stated
- [ ] Relevant Constitution / canon / ADR / RFC loaded
- [ ] Active methodology loaded
- [ ] Active ledger and sprint state loaded
- [ ] Repository branch and latest known commit identified
- [ ] Current operating mode declared
- [ ] Current blocker declared
- [ ] Next approved action declared
- [ ] Capability marked Full or Degraded

**Gate:** No new work begins until the startup result is stated.

---

## B. Before Creating or Changing an Asset

- [ ] Existing registry / inventory / repository checked
- [ ] Similar asset searched for
- [ ] Existing asset compared
- [ ] Update/reuse considered before creation
- [ ] Higher source-of-truth conflict checked
- [ ] Owner identified
- [ ] Lifecycle identified
- [ ] Canonical path identified
- [ ] Version identified
- [ ] Approval scope confirmed
- [ ] Build → Break → Validate performed where material
- [ ] No blocked BP2-02B work is being started

---

## C. Before Publishing Research or Review

- [ ] Facts separated from interpretation
- [ ] Assumptions identified
- [ ] Unknowns identified
- [ ] Accessible approved sources exhausted
- [ ] No known public data intentionally left unexamined without explanation
- [ ] Tool usage stated accurately
- [ ] No claim of TradingView, screener, repository, backup, or premium data use without evidence
- [ ] Classifications or recommendations justified
- [ ] Risk / counter-case included
- [ ] Portfolio freshness stated when relevant
- [ ] Evidence freshness stated
- [ ] QA result stated

---

## D. Before Declaring Work Complete

- [ ] Definition of Done checked
- [ ] Required files actually exist
- [ ] Required repository paths verified
- [ ] File names verified
- [ ] Size verified where required
- [ ] SHA256 verified where required
- [ ] Commit hash recorded
- [ ] Audit status recorded
- [ ] No PASS declared without completed verification
- [ ] AOSS / `CURRENT_STATE.md` updated
- [ ] Next action recorded

---

## E. Session Close

- [ ] Work completed summarized
- [ ] Verified facts recorded
- [ ] Changes recorded
- [ ] Open items recorded
- [ ] Blockers recorded
- [ ] Exact resume point recorded
- [ ] AOSS updated if available
- [ ] `CURRENT_STATE.md` updated
- [ ] Changelog / ledger updated when applicable
- [ ] Repository changes committed by an authorized actor/tool
- [ ] Commit hash recorded
- [ ] Source binaries backed up to approved storage where required
- [ ] Persistence claim verified
- [ ] No unresolved change exists only in conversation memory

---

## F. Current BP2-02B Gate

The following must remain unchecked until repository evidence exists:

- [ ] Raw archive exists at canonical path
- [ ] Raw archive exact filename verified
- [ ] Raw archive size verified
- [ ] Raw archive SHA256 verified
- [ ] Raw archive commit recorded
- [ ] Minimal raw archive ledger completed
- [ ] Historical backfill completed
- [ ] Backfill completion audit PASS
- [ ] Entity Contract Upgrade Sprint unblocked
- [ ] Evidence work unblocked

---

## G. Final Integrity Question

Before ending any major step, answer:

> Can another human or AI resume this work from the repository and documented state without relying on this conversation?

- [ ] Yes
- [ ] No — continuity work remains
