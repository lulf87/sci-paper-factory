# 2026_demo_pilot

## Project identity
This project is frozen to:
- **Data**: KiTS23 public ground-truth segmentation
- **Population**: small renal masses, `d_max <= 4 cm`
- **Modeling**: single-applicator, generic, device-agnostic geometric thermal ablation surrogate
- **Primary question**: under complete coverage, what is the minimum non-tumor kidney tissue involvement fraction?
- **Primary risk**: overclaiming geometric proxy results as clinical or device-specific conclusions

## Current gate status
- current_stage: preprocessing closed-loop / cohort audit
- build_planning_instances: PASS
- preprocessing_closed_loop: IN PROGRESS
- formal_simulation_allowed: NO

### Current blockers
- formal `cystic_interference` 未冻结
- multifocal independence 未冻结
- `exclusion_log.csv` / `subgroup_labels.csv` / `roi_metadata.csv` 尚未作为 repo 内正式产物冻结

### Current evidence snapshot
- provenance and environment records already exist:
  - `02_public_data/provenance/kits23_provenance.md`
  - `02_public_data/provenance/environment_lock.md`
- first-pass preprocessing has already generated:
  - `03_simulation/runs/planning_instances/planning_instances.csv`
  - `03_simulation/runs/planning_instances/case_summary.csv`
  - `03_simulation/runs/planning_instances/manifest.json`
- provisional cohort audit summary:
  - `n_cases_in_case_summary = 489`
  - `n_raw_instances_total = 659`
  - `n_raw_srm_candidates = 347`
  - `n_eligible_main_cohort_v1 = 296`
  - subgroup split: `<=3cm = 207`, `3-4cm = 89`
- important limitation:
  - `eligible_main_cohort_v1` is **not** the final main cohort
  - formal `cystic_interference` rule still needs to be frozen

## Current execution order
1. `00_scope/` is the source of truth.
2. Build `02_public_data/provenance/` from the downloaded KiTS23 dataset.
3. Run preprocessing to generate candidate planning instances.
4. Freeze surrogate parameter table and formal run config.
5. Run geometry sanity checks.
6. Only then start first formal run.

## Immediate next files to complete
- `03_simulation/src/audit_planning_candidates.py`
- `03_simulation/runs/cohort_audit/exclusion_log.csv`
- `03_simulation/runs/cohort_audit/subgroup_labels.csv`
- `03_simulation/runs/cohort_audit/roi_metadata.csv`
- `03_simulation/configs/surrogate_parameter_table.yaml`
- `03_simulation/configs/formal_run_config.yaml`
- `06_review/fatal_issues.md`

## Immediate next execution tasks
1. Promote cohort-audit outputs into a stable repo path.
2. Freeze formal `cystic_interference` logic.
3. Freeze multifocal independence logic.
4. Recompute the final eligible main cohort after the above rules are frozen.
5. Only then decide whether preprocessing can be marked CLOSED.
6. Do not start formal simulation or manuscript expansion before these gates are closed.
