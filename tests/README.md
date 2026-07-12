A-ZION — TESTS FRAMEWORK
Path: tests/README.md
Status: Active
Version: 1.0
Applies to: All formal A-ZION verification tests
Current phase: BP2-02B — Project Backfill & Full Documentation Backup
1. Purpose
The tests/ directory contains formal verification assets for A-ZION.
Its purpose is to prove that the system, its governance, continuity, architecture, entities, and research workflows behave according to approved rules.
Tests do not replace START_HERE.md, LOAD_ORDER.md, CURRENT_STATE.md, SYSTEM_MAP.md, the OS Boot, AOSS, the latest verified Live Master, canon rules, ADRs, RFCs, methodology, audits, or ledgers. Tests verify compliance with those assets.
2. Core Rule
A-ZION tests verify system behavior and compliance. They must not silently create, modify, migrate, or approve project state.
A test may produce a result, evidence, findings, failure notes, and a recommended recovery action.
A test must not alter the Core Domain, invent architecture, bypass approval gates, modify canonical state without explicit approval, or declare PASS without evidence.
3. Test Families
Prefix
Family
Purpose
CT
Continuity Tests
Verify cold start, session resume, load order, recovery, and continuity behavior
GT
Governance Tests
Verify canon, authority, source-of-truth hierarchy, approval, and policy enforcement
AT
Architecture Tests
Verify Core Domain freeze, layer boundaries, dependencies, and approved architecture constraints
ET
Entity Tests
Verify entity identity, isolation, responsibility, cross-entity behavior, misuse resistance, and approval gates
RT
Research Tests
Verify evidence quality, source validation, freshness, traceability, confidence, and research QA
Additional families require explicit approval before use.
4. Directory Structure
tests/
├── README.md
├── continuity/
├── governance/
├── architecture/
├── entity/
└── research/
Only create a new test file after:
checking whether an equivalent test already exists;
confirming the correct family;
confirming the test has a unique identifier;
confirming the test is required by an approved task or gap.
5. Test Naming Standard
Use:
<PREFIX>-<NNN>-<descriptive-name>.md
Examples:
CT-001-continuity-resume.md
GT-001-canon-enforcement.md
AT-001-core-domain-freeze.md
ET-001-source-identity.md
RT-001-evidence-freshness.md
Rules:
IDs are immutable after publication.
Do not reuse retired IDs.
Names must describe the tested behavior.
Avoid duplicate or overlapping tests.
Superseded tests remain traceable through version history or archive records.
6. Required Test Contract
Every formal test must contain:
6.1 Identity
Test ID
Test Name
Test Family
Version
Status
Owner
Related assets
Related requirement, canon rule, ADR, RFC, or methodology
6.2 Purpose
What behavior or rule is being verified, and why it matters.
6.3 Preconditions
What must exist or be loaded before execution.
6.4 Inputs
The exact files, repository paths, prompts, snapshots, or evidence used.
6.5 Procedure
Numbered execution steps.
6.6 Expected Result
Observable conditions required for success.
6.7 Failure Conditions
Explicit conditions that produce FAIL.
6.8 Evidence Record
What proof must be captured, such as direct links, commit hashes, SHA256 values, startup reports, repository paths, or audit notes.
6.9 Result
Only one result may be recorded:
PASS
FAIL
BLOCKED
NOT RUN
6.10 Failure Analysis
Required for FAIL or BLOCKED:
failed step;
observed behavior;
expected behavior;
root cause if known;
unknowns;
impact;
recovery action;
retest requirement.
6.11 Approval
Who reviewed the result, when, and under what authority.
7. Standard Test Template
# <TEST-ID> — <TEST NAME>

**Family:** <CT / GT / AT / ET / RT>  
**Version:** <vX.Y>  
**Status:** Draft / Active / Superseded / Archived  
**Owner:** <role or department>

## Related Assets
- ...

## Purpose
...

## Preconditions
- [ ] ...

## Inputs
- ...

## Procedure
1. ...

## Expected Result
- ...

## Failure Conditions
- ...

## Evidence Record
- ...

## Result
**Status:** NOT RUN

## Failure Analysis
Not applicable until FAIL or BLOCKED.

## Approval
- Reviewer:
- Date:
- Decision:
8. Execution Rules
Before any test:
Load START_HERE.md.
Follow LOAD_ORDER.md.
Load CURRENT_STATE.md.
Load SYSTEM_MAP.md.
Identify the latest verified Live Master or clearly state that it is only referenced.
Identify the active operating mode.
Identify current blockers.
Verify that running the test is allowed in the current phase.
Declare capability as Full or Degraded.
No test may silently rely on conversation memory.
9. State Mutation Rules
Default rule:
Tests are read-only.
A test must not move files, rename files, delete files, change canonical documents, commit repository changes, alter entity status, unblock work, or grant approval.
If a future test requires controlled mutation, it must be explicitly classified, define rollback, use an isolated environment, receive explicit approval, and never run against canonical production assets by default.
10. PASS Standard
A test may receive PASS only when:
all preconditions were satisfied;
all required steps were executed;
expected results were observed;
required evidence was captured;
no unsupported assumptions were used;
no canon rule was violated;
no blocked work was performed;
the result is reproducible;
and the reviewer has authority to approve it.
Partial success is not PASS.
11. FAIL Standard
A test must receive FAIL when:
an expected result is not met;
the AI invents or assumes project state;
required assets are skipped;
blockers are ignored;
source-of-truth hierarchy is violated;
evidence is missing;
the test changes state without approval;
or the process cannot be reproduced.
Every FAIL must create a failure analysis and a retest requirement.
12. BLOCKED Standard
Use BLOCKED when the test cannot be completed because a required dependency is unavailable.
Examples:
repository inaccessible;
required file missing;
checksum unavailable;
authority missing;
source-of-truth conflict unresolved.
BLOCKED is not FAIL and not PASS.
13. Relationship to Checklists and Audits
Checklists
Checklists define what must be checked during work.
Tests
Tests execute controlled verification of a defined behavior.
Audits
Audits review broader compliance, completeness, and accumulated evidence.
The three layers complement each other and must not be treated as interchangeable.
14. Current BP2-02B Restrictions
During BP2-02B, tests may verify:
repository presence;
continuity loading;
raw archive integrity;
documentation completeness;
source-of-truth behavior;
blocker enforcement;
and backfill readiness.
Tests must not start Source v1.1, Contributor v1.1, Knowledge v1.1, or Evidence; inspect implementation archives; extract the raw historical ZIP; write business code; or declare the backfill complete without audit evidence.
15. Current First Test
The first approved test is:
tests/continuity/CT-001-continuity-resume.md
Its creation and execution are separate steps.
This README defines the framework only. It does not declare CT-001 created, executed, or passed.
16. Definition of Done
This framework is complete when:
purpose is defined;
families are defined;
naming is defined;
test contract is defined;
execution rules are defined;
state mutation rules are defined;
PASS / FAIL / BLOCKED standards are defined;
relationship to checklists and audits is clear;
BP2-02B restrictions are preserved;
and the framework is stored at tests/README.md with a focused commit.
17. Recommended Commit
docs(tests): add A-ZION test framework v1.0

docs(tests): add A-ZION test framework v1.0
