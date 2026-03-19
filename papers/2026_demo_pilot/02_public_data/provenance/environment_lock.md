# Environment lock

## Host

- machine: MacBook Pro, 16 GB RAM
- os: macOS 26.1 (arm64)
- python: 3.12.12
- shell: /bin/zsh
- timezone: /Asia/Shanghai

## Core packages

- numpy: 2.4.3
- scipy: 1.16.3
- pandas: 2.3.3
- nibabel: 5.4.2
- matplotlib: 3.10.7

## Reproducibility hooks

- repo_commit_hash: 395958f1f748f42946f155e8b7f896f8481b19e8
- preprocessing_script_version: pending_first_preprocessing_run
- config_snapshot_dir: papers/2026_demo_pilot/03_simulation/configs/
- random_seed_policy: deterministic where applicable; default_seed=20260317

## Notes

- Missing KiTS23 imaging files were recovered before preprocessing by a local bash script with resume, retry, and gzip integrity checks.
- The corresponding missing-case list is:
  `papers/2026_demo_pilot/02_public_data/provenance/KiTS23_missing_imaging_cases.txt`
