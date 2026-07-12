# A-ZION — SYSTEM MAP

**Status:** Active  
**Version:** 1.0  
**Repository:** `avivsalame11-png/A-ZION`  
**Current phase:** BP2-02B — Project Backfill & Full Documentation Backup  
**Last reviewed:** 2026-07-12

---

## 1. Purpose

This document maps the major A-ZION system assets, their roles, ownership, source-of-truth status, lifecycle, and dependencies.

It is a navigation and relationship map. It does not replace the Constitution, Live Master, AOSS, methodology, ledger, or archive.

---

## 2. System Layers

| Layer | Purpose | Canonical Assets | Owner |
|---|---|---|---|
| Entry | Universal entry point for humans and AI | `START_HERE.md` | Operations |
| Boot | Defines startup rules and loading behavior | `A-ZION_OS_BOOT_v1.0.md`, Boot Specification | Architecture |
| Operational State | Current working state and exact resume point | `A-ZION_AOSS_v1.0_Current_State.md`, `CURRENT_STATE.md` | Operations |
| Strategic State | Approved strategic project state | Latest verified Live Master | Governance |
| Governance | Constitution, canon, approvals, immutable constraints | Constitution, Canon Rules, ADR, RFC | Governance |
| Methodology | Standards, templates, quality gates | Entity Contract Standard v1.1 | Methodology |
| Ledger | Audit trail, inventory, decisions, changes, backfill | BP2-02B inventory and ledgers | Governance |
| Knowledge | Approved research, intelligence, books, expert assets | Vault and research assets | Research |
| Runtime | Execution engines and implementation packages | Runtime assets and code | Engineering |
| Archive | Raw historical originals and immutable snapshots | Raw intake ZIP, historical masters | Archive |

---

## 3. Critical Asset Map

| Asset | Purpose | Source of Truth | Lifecycle | Status | Depends On |
|---|---|---|---|---|---|
| `START_HERE.md` | Universal entry point | GitHub | Living | Active | None |
| `A-ZION_OS_BOOT_v1.0.md` | Boot rules and startup control | GitHub | Versioned | Pending repository placement verification | Constitution / Live Master references |
| `A-ZION_OS_BOOT_Specification_v1.0.md` | Boot architecture and constraints | GitHub | Versioned | Pending repository placement verification | Governance |
| `A-ZION_AOSS_v1.0_Current_State.md` | Current operational session state | GitHub | Living | Pending repository placement verification | Boot + Live Master |
| `CURRENT_STATE.md` | Minimal current-state snapshot | GitHub | Living | Active after repository upload | AOSS + latest verified commit |
| `LOAD_ORDER.md` | Mandatory loading sequence | GitHub | Versioned | Active after repository upload | START_HERE |
| `CONTINUITY_CHECKLIST.md` | Startup and close QA | GitHub | Living | Active after repository upload | LOAD_ORDER |
| Latest Live Master | Strategic project checkpoint | Repository / approved archive | Versioned | v3.7 verified as current checkpoint | Constitution |
| Entity Contract Standard v1.1 | Entity design standard | GitHub | Versioned | Audited PASS | Live Master |
| ADR Index | Architecture decision navigation | GitHub | Living index | Audited PASS | Approved source materials |
| RFC Index | RFC navigation | GitHub | Living index | Audited PASS | Approved source materials |
| Canon Rules Index | Governance rule navigation | GitHub | Living index | Audited PASS | Constitution / approved standards |
| BP2-02B Backfill Inventory | Historical backup plan and scope | GitHub | Versioned | Audited PASS | Uploaded inventory |
| Raw Intake Archive | Preserved 143 historical originals | GitHub archive path | Immutable | Repository integrity verification pending | None |

---

## 4. Dependency Flow

```text
START_HERE
    ↓
OS BOOT
    ↓
AOSS / CURRENT_STATE
    ↓
LATEST VERIFIED LIVE MASTER
    ↓
GOVERNANCE + CANON + ADR + RFC
    ↓
ACTIVE METHODOLOGY + LEDGER
    ↓
CURRENT APPROVED TASK
```

If a critical dependency is missing, continue only in the applicable degraded mode and state the limitation.

---

## 5. Authority Rules

1. Conversation memory is not authoritative.
2. Certified and locked constitutional assets override lower-level documents.
3. The latest verified Live Master is the strategic source of truth.
4. AOSS and `CURRENT_STATE.md` govern current operational state.
5. ADRs and canon rules govern approved architecture and constraints.
6. The archive preserves history but does not automatically define the current state.
7. No new asset may override a higher-level asset without explicit approval and versioning.

---

## 6. Current Active Path

```text
BP2-02B
    ↓
Preserve raw originals
    ↓
Verify repository path, size, checksum, commit
    ↓
Complete minimal raw archive ledger
    ↓
Complete historical documentation backfill
    ↓
Run backfill completion audit
    ↓
Audit PASS
    ↓
Resume Entity Contract Upgrade Sprint
```

---

## 7. Explicitly Blocked

Until BP2-02B audit PASS:

- Source v1.1 upgrade
- Contributor v1.1 upgrade
- Knowledge v1.1 upgrade
- Evidence work
- Business implementation code
- Database schema design
- Framework selection
- Implementation archive inspection
- Raw archive extraction or transformation

---

## 8. Maintenance Rule

Update this map only when:

- a canonical asset is added, removed, superseded, or relocated;
- the source-of-truth hierarchy changes;
- the active phase changes;
- or an approved architecture decision changes system relationships.

Every update requires a focused commit and a change-log entry.
