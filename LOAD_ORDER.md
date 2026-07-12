# A-ZION — LOAD ORDER

**Status:** Mandatory continuity protocol  
**Version:** 1.0  
**Applies to:** Humans, AI systems, Copilot, agents, and future contributors

---

## 1. Purpose

This document defines the mandatory order for loading A-ZION project context.

Do not begin reasoning, architecture, implementation, research, entity work, or trading-desk work before completing the applicable sequence.

---

## 2. Standard Load Order

### 1. Entry Point

Load:

`START_HERE.md`

Confirm:

- current phase;
- active blockers;
- required operating mode;
- prohibited work.

### 2. OS Boot

Load:

`docs/operations/continuity/A-ZION_OS_BOOT_v1.0.md`

Then load:

`docs/operations/continuity/A-ZION_OS_BOOT_Specification_v1.0.md`

If missing, mark continuity capability as degraded.

### 3. Operational State

Load:

`docs/operations/continuity/A-ZION_AOSS_v1.0_Current_State.md`

Then load:

`CURRENT_STATE.md`

Use the newest verified state. If the two conflict, stop and resolve the conflict before work.

### 4. System Map

Load:

`SYSTEM_MAP.md`

Confirm:

- asset relationships;
- source-of-truth hierarchy;
- active dependency path;
- blocked layers.

### 5. Latest Verified Live Master

Load the latest verified Live Master referenced by AOSS / `CURRENT_STATE.md`.

Current verified checkpoint:

`A-ZION_Live_Master_v3.7_Checkpoint.docx`

If the document content cannot be read, use only verified summaries and clearly state the limitation.

### 6. Governance

Load as relevant:

- Constitution / certified locked assets
- `docs/canon-rules/README-canon-index.md`
- `docs/adr/README-ad-index.md`
- `docs/rfc/README-rfc-index.md`

### 7. Active Methodology

Load:

- `docs/methodology/entity-contract-standard-v1.1.md`
- any additional approved methodology required for the active task

### 8. Active Ledger and Sprint State

Load:

- `docs/ledger/BP2-02B-documentation-backfill-inventory.md`
- current sprint plan
- current audit / ledger assets
- latest verified commit information

### 9. Task-Specific Assets

Only now load:

- research assets;
- portfolio / watchlist snapshots;
- entity contracts;
- implementation specs;
- or other task-specific material.

### 10. Startup Report

Before beginning work, report:

```text
START_HERE: Loaded / Missing
BOOT: Loaded / Missing
AOSS: Loaded / Missing
CURRENT_STATE: Loaded / Missing
SYSTEM_MAP: Loaded / Missing
Live Master: Loaded / Referenced only / Missing
Governance: Loaded / Partial
Methodology: Loaded / Partial
Ledger: Loaded / Partial
Operating mode: ...
Capability: Full / Degraded
Next approved action: ...
```

---

## 3. Current Required Mode

For the current verified state:

`Archive and documentation backfill`

No implementation, entity upgrade, or Evidence work is permitted.

---

## 4. Conflict Rule

If two sources disagree:

1. stop;
2. identify the conflicting fields;
3. apply the source-of-truth hierarchy;
4. document the resolution;
5. update the lower source through an approved change.

Do not silently choose one.

---

## 5. Degraded Mode Rules

### Repository inaccessible

Use verified uploaded files or direct raw links. Do not claim repository state was checked.

### Boot or AOSS missing

Use `START_HERE.md` and `CURRENT_STATE.md`; state degraded continuity.

### Live Master unreadable

Do not invent missing details. Use verified checkpoint summary only.

### Portfolio or watchlist stale

General research may continue. Portfolio-specific execution recommendations are blocked or explicitly qualified.

---

## 6. Session Close Order

1. Record verified work completed.
2. Record changes.
3. Record unresolved items.
4. Record exact next action.
5. Update AOSS / `CURRENT_STATE.md`.
6. Commit actual repository changes.
7. Record commit hash.
8. Verify backup or archive action before claiming persistence.
