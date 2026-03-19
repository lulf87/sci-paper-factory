# Repo delta for `lulf87/sci-paper-factory`

This bootstrap pack is aligned to:

- `papers/2026_demo_pilot/00_scope/*`
- `papers/2026_demo_pilot/AGENTS.md`
- the current narrow route: KiTS23 small renal masses + single-applicator generic geometric surrogate + coverage–non-tumor kidney tissue trade-off

## What this pack adds

- `03_simulation/` skeleton
- `04_analysis/` skeleton
- provenance templates under `02_public_data/provenance/`
- one preprocessing script to build candidate planning instances from `segmentation.nii.gz`
- one geometry sanity-check script
- manuscript claim ledger template
- review blocker template

## What this pack intentionally does NOT do

- no device-specific parameterization
- no multi-applicator planning
- no clinical conclusion drafting
- no final manuscript wording
- no automated cyst-exclusion rule beyond triage flags
