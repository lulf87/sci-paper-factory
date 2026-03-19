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
- status: OPEN
- impact: execution path is incomplete
- required fix:
  - add `03_simulation/`
  - add `04_analysis/`
  - freeze configs before first formal run

### B003 — cystic-interference exclusion not yet operationalized
- status: OPEN
- impact: main cohort cannot be formally frozen
- required fix:
  - define reviewer-facing audit rule
  - build exclusion log template
  - separate triage flags from exclusion decisions

### B004 — no first-pass planning instance table yet
- status: OPEN
- impact: cannot confirm available sample size under `d_max <= 4 cm`
- required fix:
  - run `build_planning_instances.py`
  - inspect lesion counts and subgroup counts
