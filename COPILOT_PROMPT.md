# A-ZION Copilot BP2-02B Backfill Master Prompt v1.0

## Use Case

This file is a **single copy/paste prompt** for GitHub Copilot after ChatGPT completed a full upload intake review.

It lets Copilot continue BP2-02B without requiring the user to manually explain the whole project again.

## Critical Limitation

Copilot cannot access files uploaded to ChatGPT unless the user places either:

1. The raw archive ZIP created by ChatGPT, or
2. The original files,

inside the GitHub repository.

Recommended shortcut:

```text
archive/raw-intake/bp2-02b-full-upload/A-ZION_BP2-02B_FULL_RAW_INTAKE_2026-07-08.zip
```

This preserves all originals in one move. Do not extract it yet unless explicitly approved.

---

# COPY FROM HERE INTO COPILOT

GOLDEN RULE:
Do not change the Core Domain.
Do not invent architecture.
Follow the latest Live Master as the source of truth.
Create only what is explicitly requested.
If something is missing, ask before creating it.
Do not write business code yet.

Current project:
A-ZION

Repository:
avivsalame11-png/A-ZION

Current phase:
BP2-02B Project Backfill & Full Documentation Backup

Current mode:
Archive and documentation backfill only.
No implementation.
No entity upgrade.
No Evidence work.

Already completed and audited PASS:
1. docs/methodology/entity-contract-standard-v1.1.md
   Commit: 84c49b8e4c88cb1041b9d60a0af5bc1ce8165457

2. docs/ledger/BP2-02B-documentation-backfill-inventory.md
   Commit: 37ef0ccb9272b8340dd41622510c5a7e0cdc4b1a

3. Tier 0 Indexes:
   - docs/rfc/README-rfc-index.md
   - docs/adr/README-ad-index.md
   - docs/canon-rules/README-canon-index.md
   Commit: b63c41bcccf57b036124e8b46dbab8e16caf4727

Current canonical source-of-truth state:
- Latest Live Master: A-ZION_Live_Master_v3.7_Checkpoint.docx
- Core Freeze v1.0 locked
- Build Pack 1 completed
- Build Pack 2 active
- Sprint BP2-01 completed
- Sprint BP2-02 in progress
- Source: Approved
- Contributor: Approved
- Knowledge: Approved
- Evidence: Not started
- Decision taken: upgrade all existing entity contracts to Entity Contract Standard v1.1 before continuing to Evidence

Current blocker:
Do not resume Entity Contract Upgrade Sprint until BP2-02B historical archive backfill is complete and audited PASS.

Backfill principle:
Preserve raw originals first.
Create summaries and extracted Markdown only after raw files are safely archived and the user approves the file strategy.

Uploaded artifact inventory from ChatGPT intake:
- Total A-ZION artifacts detected: 143
- .docx: 81
- .xlsx: 37
- .zip: 22
- .md: 2
- .pptx: 1

Provisional categories:
- Backfill Checkpoints: 2
- Certified Foundation Assets: 11
- Engines / Databases / Runtime Workbooks: 10
- Experts / Principles / Dossiers: 12
- Foundation Book / Foundation Reference: 10
- Frozen Stages: 3
- Gold Master / Gold Validation: 5
- Investment Research / Data Governance: 14
- Knowledge / Evidence / Assertions: 17
- Live Masters / BP2 Master: 18
- Masters / Backups / Updates: 6
- Other / Review Needed: 8
- Presentations: 1
- Sprint Workbooks / Core Builds: 11
- ZIP Packages / Implementation Archives: 15

Important known version chains:
1. Live Master chain:
   - A-ZION_Live_Master_v2_1.docx
   - A-ZION_Live_Master_v2_2.docx
   - A-ZION_Live_Master_v2_3.docx
   - A-ZION_Live_Master_v2.4_SYNC.docx
   - A-ZION_Live_Master_v2.5_Daily_Operations_Protocol.docx
   - A-ZION_Live_Master_v2.6_Opportunity_Refactor.docx
   - A-ZION_Live_Master_v2.7_Opportunity_Registry.docx
   - A-ZION_Live_Master_v2.8_Orchestrator_v1.0.docx
   - A-ZION_Live_Master_v2.9_Constitution_Operating_Principles.docx
   - A-ZION_Live_Master_v3.0_MVP_and_Build_Readiness.docx
   - A-ZION_Live_Master_v3.1_Expert_Intelligence_Network.docx
   - A-ZION_Live_Master_v3.2_Living_Intelligence_Engine.docx
   - A-ZION_Live_Master_v3.3_Learning_and_Meta_Intelligence.docx
   - A-ZION_Live_Master_v3.4_Core_Freeze_and_BP2.docx
   - A-ZION_Live_Master_v3.5_BP2-02.docx
   - A-ZION_Live_Master_v3.6_BP2-02_Entity_Contracts.docx
   - A-ZION_Live_Master_v3.7_Checkpoint.docx

2. Frozen stage baselines:
   - A-ZION_Stage_1_Language_Standards_v1.0_FROZEN.docx
   - A-ZION_Stage_2_Intelligence_Library_v1.0_FROZEN.docx
   - A-ZION_Stage_3_Decision_Framework_v1.0_FROZEN.docx

3. Foundation Book release chain:
   - BUILD 7
   - BUILD 8
   - Production Draft
   - Editorial Pass
   - QA Pass
   - RC1
   - FINAL RELEASE

4. Gold Master Index chain:
   - A-ZION_Gold_Master_Index_v1.0.docx
   - A-ZION_Gold_Master_Index_v1_1.docx
   - A-ZION_Gold_Master_Index_v1_2.docx

5. Knowledge Database chain:
   - A-ZION_Knowledge_Database_v1.docx
   - A-ZION_Knowledge_Database_v1_Registry.xlsx
   - A-ZION_Knowledge_Database_v1_1_Ontology_Registry.xlsx
   - A-ZION_Knowledge_Database_v1_2_Evidence_Sprint001.xlsx
   - A-ZION_Knowledge_Database_v1_3_Assertion_Sprint002.xlsx
   - A-ZION_Knowledge_Database_v1_4_Direct_Source_Sprint003.xlsx

6. Core build and implementation archive chain:
   - A-ZION_Core_v0.1_Sprint009.zip
   - A-ZION_Core_v0.2_Sprint010.zip
   - A-ZION_Core_v0.3_Sprint011.zip
   - A-ZION_Core_v0.4_Sprint012_Offline_Test_Harness.zip
   - A-ZION_Core_v0.5_Sprint013_Engines.zip
   - platform / IE / P01 / P02 / technical debt ZIP packages

Task:
Create a preview only for a minimal BP2-02B raw archive checkpoint.

Do not create files yet.
Do not modify files yet.
Do not move files.
Do not extract ZIP files.
Do not inspect implementation code.
Do not convert DOCX, XLSX, PPTX, ZIP, or MD files.
Do not create summaries from source documents.
Do not create or modify README unless explicitly approved.
Do not start Source v1.1.
Do not start Contributor v1.1.
Do not start Knowledge v1.1.
Do not start Evidence.
Do not write code.
Do not change Core Domain.
Do not invent architecture.

Expected raw archive location:
archive/raw-intake/bp2-02b-full-upload/

Expected preferred artifact:
archive/raw-intake/bp2-02b-full-upload/A-ZION_BP2-02B_FULL_RAW_INTAKE_2026-07-08.zip

If the ZIP is present:
- Confirm it exists.
- Report size.
- Do not extract.
- Treat it as raw historical archive package.

If the ZIP is not present:
- Report that raw files are not yet present.
- Do not create fake manifest.
- Ask user to place the ZIP or original files in the expected folder.

Prepare preview only for these files:
1. docs/ledger/BP2-02B-final-upload-inventory-v0.2.md
2. docs/ledger/BP2-02B-raw-archive-manifest-v0.1.md
3. docs/ledger/BP2-02B-repository-placement-plan-v0.1.md

Rules for preview:
- Use only the inventory and status provided in this prompt.
- Clearly mark ChatGPT-side inventory as "pending repository raw archive confirmation".
- Do not claim files are backed up in GitHub unless the raw archive ZIP or originals are actually present in the repository.
- Do not claim audit PASS until repository state is verified.
- Placement plan should be proposed, not executed.
- Keep raw archive as the first priority.

Return:
PREVIEW ONLY.
Do not create files until user approves.

# END COPY
