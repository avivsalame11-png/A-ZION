# Canon Rules Index

**Version**: 1.0  
**Phase**: BP2-02B Tier 0  
**Status**: Partial initial index of known approved canon rules  
**Last Updated**: Build Pack 2, Sprint BP2-02B  

---

## Purpose

This index documents all approved canon rules and governance principles for the A-ZION project. Canon rules are sacred constraints that apply universally and cannot be violated.

---

## Scope

This index lists known approved canon rules. Each rule is binding and must be enforced throughout the system. Canon rules establish the foundation for all other decision-making and design work.

**Important**: This is a partial initial index of known approved canon rules. Additional canon rules must be extracted from approved Live Master versions and project history. The list is not exhaustive.

---

## Known Approved Canon Rules

### 1. GOLDEN RULE
**Status**: Approved  
**Source**: A-ZION Governance (Approved across all Build Packs)  
**Text**: 
- Do not change the Core Domain
- Do not invent architecture
- Follow the latest Live Master as the source of truth
- Create only what is explicitly requested
- If something is missing, ask before creating it
- Do not write business code yet

**Enforcement**: Mandatory for all work in A-ZION

**Reference**: `docs/canon-rules/GOLDEN-RULE.md` (to be created in Tier 2)

---

### 2. Live Master is the Source of Truth
**Status**: Approved  
**Source**: A-ZION Governance  
**Text**: All decisions, standards, and specifications must be grounded in the approved Live Master. The Live Master is the single source of truth. No other source may override the Live Master without explicit Live Master update.

**Enforcement**: Mandatory - All work must reference and align with the current Live Master version

**Reference**: Current Live Master v3.7 Checkpoint in `docs/master/`

---

### 3. No Core Domain Changes Without RFC
**Status**: Approved  
**Source**: A-ZION Architecture Governance  
**Text**: Any proposed change to the Core Domain must be submitted as an RFC and approved before implementation. Core Domain components are immutable until RFC approval.

**Enforcement**: Mandatory - Core freeze applies until RFC approval obtained

**Reference**: `docs/core-freeze/` (to be created in Tier 2)

---

### 4. No Business Code Before Approved Contracts
**Status**: Approved  
**Source**: Entity Contract Standard v1.1 (Section 8, Approval Requirements)  
**Text**: No implementation code, database schema, or business logic may be created until the corresponding entity contract has passed Quality Gate and received formal approval.

**Enforcement**: Mandatory - Code work is blocked until contracts approved

**Reference**: `docs/methodology/entity-contract-standard-v1.1.md`

---

### 5. Entity Contract Standard v1.1 is Mandatory for All Entities
**Status**: Approved  
**Source**: Entity Contract Standard v1.1 (Section 8, Approval Requirements, Constraint 4)  
**Text**: Every entity in A-ZION must conform to Entity Contract Standard v1.1. All 8 sections must be completed. No exceptions. No variant standards.

**Enforcement**: Mandatory - All entities must conform

**Reference**: `docs/methodology/entity-contract-standard-v1.1.md`

---

### 6. Evidence Remains Blocked Until Source, Contributor, and Knowledge Upgraded and Audited
**Status**: Approved  
**Source**: Entity Contract Standard v1.1 (Section 8, Approval Requirements, Constraint 5)  
**Text**: Evidence entity remains blocked from contract upgrade until:
- Source entity upgraded to v1.1 and passes all tests
- Contributor entity upgraded to v1.1 and passes all tests
- Knowledge entity upgraded to v1.1 and passes all tests
- Global Entity Audit passes (validating all three upgraded entities and their interactions)

Only after all conditions met can Evidence entity work begin.

**Enforcement**: Mandatory - Evidence is explicitly blocked

**Reference**: Entity Contract Standard v1.1, Section 8.5; `docs/entity-contracts/`

---

### 7. Opportunity is NOT Asset
**Status**: Approved  
**Source**: RFC-008 and RFC-006 (Opportunity and Asset entity definitions)  
**Text**: Opportunity and Asset are distinct entities with separate responsibilities, data models, and lifecycles. They are not interchangeable. This boundary must be preserved in design, contracts, reviews, and future implementation.

**Enforcement**: Mandatory - Boundary preservation is enforced across all design phases

**Reference**: `docs/rfc/` (RFC-008 Opportunity, RFC-006 Asset)

---

### 8. Evidence is NOT Opinion
**Status**: Approved  
**Source**: RFC-004 (Evidence entity definition)  
**Text**: Evidence is factual, verifiable support for a claim. Opinion is subjective interpretation. Evidence and opinion must remain distinct in design, contracts, reviews, and future implementation. Opinion must not masquerade as Evidence.

**Enforcement**: Mandatory - This boundary must be preserved across all design phases

**Reference**: `docs/rfc/RFC-004-Evidence` (when available in docs/rfc/)

---

### 9. Contributor is NOT Source
**Status**: Approved  
**Source**: RFC-001 and RFC-002 (Contributor and Source entity definitions)  
**Text**: Contributor is the person, expert, organization, model, or process that created, supplied, or is responsible for knowledge or analysis. Source is the documented origin of information. They serve different purposes and must be tracked separately.

**Enforcement**: Mandatory - This boundary must be preserved in design, contracts, reviews, and future implementation

**Reference**: `docs/rfc/RFC-001-Contributor` and `docs/rfc/RFC-002-Source` (when available in docs/rfc/)

---

### 10. Knowledge is NOT Document
**Status**: Approved  
**Source**: RFC-003 (Knowledge entity definition)  
**Text**: Knowledge is structured, queryable information. Document is a formatted presentation. Knowledge may be stored in documents, but knowledge itself is the underlying structured information.

**Enforcement**: Mandatory - This boundary must be preserved in design, contracts, reviews, and future implementation

**Reference**: `docs/rfc/RFC-003-Knowledge` (when available in docs/rfc/)

---

### 11. Decision is NOT Outcome
**Status**: Approved  
**Source**: RFC-011 (Decision entity definition)  
**Text**: Decision is a choice made at a point in time. Outcome is the result of executing a decision. They must be tracked separately. A decision may have multiple outcomes or no outcome yet.

**Enforcement**: Mandatory - This boundary must be preserved in design, contracts, reviews, and future implementation

**Reference**: `docs/rfc/RFC-011-Decision` (when available in docs/rfc/)

---

### 12. Entity Contract is the Authoritative Design Artifact
**Status**: Approved  
**Source**: Entity Contract Standard v1.1 (Section 8, Approval Requirements, Constraint 3)  
**Text**: Entity Contract is the authoritative design artifact for all entities. Logical Domain Model, ERD, Persistence Design, API, and Code are all derived from and must conform to the approved Entity Contract. No implementation work (Logical Model, ERD, Persistence Design, database schema, API, code) may proceed until Entity Contract is approved.

**Enforcement**: Mandatory - Implementation is blocked until contract approved

**Reference**: `docs/methodology/entity-contract-standard-v1.1.md`

---

### 13. All Entities Must Share the Same Contract Maturity Level and Standard
**Status**: Approved  
**Source**: Entity Contract Standard v1.1 (Section 8, Approval Requirements, Constraint 4)  
**Text**: All entities in A-ZION must conform to the same Entity Contract Standard and must be at the same maturity level. When upgrading entities to a new standard version, the entire set must be upgraded together. No active approved entity baseline may mix contract standards. Older versions may remain archived as historical backups.

**Enforcement**: Mandatory - Cross-entity validation ensures consistency

**Reference**: `docs/methodology/entity-contract-standard-v1.1.md`

---

## Source Material Required

**User Must Provide:**
- Confirmation of all canon rules listed above
- Any additional canon rules not listed here
- Approval records for each canon rule
- References to where each rule appears in approved masters
- Enforcement procedures and governance oversight for each rule

---

## Important Notes

**What This Index Does:**
- ✅ Lists known approved canon rules
- ✅ Provides central governance reference
- ✅ Documents rule enforcement requirements
- ✅ Links to documentation and source materials

**What This Index Does NOT Do:**
- ❌ Does NOT claim the list is exhaustive
- ❌ Does NOT invent new canon rules
- ❌ Does NOT modify approved rules

---

## Blocked Work

**DO NOT:**
- ❌ Create new canon rules without explicit Live Master approval
- ❌ Violate any approved canon rule
- ❌ Modify or rename existing canon rules
- ❌ Create work that violates any canon rule

---

## Next Step

1. User reviews all canon rules listed above
2. User confirms each rule is accurate and complete
3. User provides any additional canon rules not listed
4. User provides approval records and enforcement procedures
5. In Tier 2, create individual canon rule documentation files
6. In Tier 2, create governance and enforcement procedures

---

**Status**: Partial initial index complete with 13 known approved canon rules. Awaiting user confirmation and extraction of additional canon rules from approved source materials.