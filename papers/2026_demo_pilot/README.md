# 2026_demo_pilot

## Project identity

This project is frozen to:

- **Data**: KiTS23 public ground-truth segmentation
- **Population**: small renal masses, `d_max <= 4 cm`
- **Modeling**: single-applicator, generic, device-agnostic geometric thermal ablation surrogate
- **Primary question**: under complete coverage, what is the minimum non-tumor kidney tissue involvement fraction?
- **Primary risk**: overclaiming geometric proxy results as clinical or device-specific conclusions

## Current execution order

1. `00_scope/` is the source of truth.
2. Build `02_public_data/provenance/` from the downloaded KiTS23 dataset.
3. Run preprocessing to generate candidate planning instances.
4. Freeze surrogate parameter table and formal run config.
5. Run geometry sanity checks.
6. Only then start first formal run.

## Immediate next files to complete

- `02_public_data/provenance/kits23_provenance.md`
- `02_public_data/provenance/environment_lock.md`
- `03_simulation/configs/surrogate_parameter_table.yaml`
- `03_simulation/configs/formal_run_config.yaml`
- `03_simulation/src/build_planning_instances.py`
- `03_simulation/verification/geometry_test_plan.md`
- `05_manuscript/claim_map.md`
- `06_review/fatal_issues.md`
