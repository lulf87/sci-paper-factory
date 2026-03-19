# fatal_issues.md

## Current blockers

### B001 — dataset provenance not yet fully logged
- status: OPEN
- impact: cannot claim full reproducibility
- required fix:
  - complete `02_public_data/provenance/kits23_provenance.md`
  - generate local inventory CSV
  - record dataset version and license from official source

### B002 — simulation and analysis directories missing from active repo
- status: CLOSED
- closing evidence:
  - `03_simulation/` and `04_analysis/` are present in active repo

### B003 — cystic-interference exclusion not yet operationalized
- status: OPEN
- impact: main cohort cannot be formally frozen
- current evidence:
  - provisional cohort audit exists, but `eligible_main_cohort_v1` is not the final main cohort
  - `cyst_adjacent_1voxel` remains a triage flag rather than a final exclusion rule
- required fix:
  - keep triage flags separate from final exclusion decisions
  - review audit descriptors and freeze formal exclusion logic

### B004 — no first-pass planning instance table yet
- status: CLOSED
- closing evidence:
  - first-pass planning instance table generated
  - cohort audit summary available

### B005 — multifocal independence rule not yet operationalized
- status: OPEN
- impact: main cohort may still contain unresolved non-independent targets
- required fix:
  - define lesion independence rule at connected-component level
  - apply rule script-wise and log decisions

### B006 — exclusion log not yet promoted to final frozen cohort artifact
- status: OPEN
- impact: preprocessing closed-loop is not yet frozen
- current evidence:
  - provisional audit artifacts can be committed now
  - final cohort artifact still requires rule freeze and rerun
- required fix:
  - commit `exclusion_log.csv`
  - commit `subgroup_labels.csv`
  - commit `roi_metadata.csv`
  - after rule freeze, regenerate and commit final cohort outputs
