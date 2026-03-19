# Geometry test plan

## Goal

Verify that preprocessing outputs are mathematically correct before any formal planning run.

## Required checks

1. **I/O integrity**
   - segmentation files are readable
   - affine matrices are readable
   - label values are in `{0,1,2,3}` only

2. **Connected-component determinism**
   - same input gives same lesion count on repeated runs
   - connectivity definition is fixed and documented

3. **Diameter calculation sanity**
   - synthetic shapes pass deterministic checks
   - a small manual sample of real KiTS23 cases is visually cross-checked

4. **Volume sanity**
   - voxel counts and physical volume agree with affine-derived voxel volume
   - no negative or impossible values

5. **Audit outputs**
   - `planning_instances.csv`
   - `case_summary.csv`
   - `manifest.json`

## Stop conditions

Stop formal progression if any of the following occurs:

- lesion count changes across repeated runs without code/config changes
- d_max is clearly inconsistent with manual spot checks
- label set contains unexpected values
- segmentation affines are missing or malformed
