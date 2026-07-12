# CT-001 — Continuity Resume Verification

**Family:** CT (Continuity Tests)  
**Version:** v1.0  
**Status:** Active (NOT RUN)  
**Owner:** A-ZION Governance

## Related Assets
- START_HERE.md
- LOAD_ORDER.md
- CURRENT_STATE.md
- SYSTEM_MAP.md
- tests/README.md

## Purpose
Verify that a new working session resumes from the approved source-of-truth documents rather than relying on conversation memory.

## Preconditions
- [ ] Repository is accessible.
- [ ] Required continuity documents exist.
- [ ] Active phase allows continuity verification.

## Inputs
- START_HERE.md
- LOAD_ORDER.md
- CURRENT_STATE.md
- SYSTEM_MAP.md

## Procedure
1. Start a new session.
2. Load START_HERE.md.
3. Follow LOAD_ORDER.md.
4. Load CURRENT_STATE.md.
5. Load SYSTEM_MAP.md.
6. State current operating mode.
7. State known blockers.
8. Explicitly distinguish verified information from assumptions.

## Expected Result
- Session is reconstructed from repository assets.
- Missing information is declared as unknown.
- No hidden conversation memory is used as evidence.

## Failure Conditions
- Conversation memory treated as source-of-truth.
- Required document skipped.
- Unknowns presented as facts.

## Evidence Record
- Date:
- Repository revision:
- Reviewer:
- Notes:

## Result
**Status:** NOT RUN

## Failure Analysis
Complete only if result is FAIL or BLOCKED.

## Approval
- Reviewer:
- Date:
- Decision:
