#!/usr/bin/env python3
"""
Audit candidate planning instances and produce provisional cohort tables.

This version is designed for Step 3B execution with no manual CSV editing.
It adds placeholder-ready descriptors needed for later freezing of:
- cystic_interference
- multifocal independence

Important:
- This script does NOT create the final main cohort.
- It creates a reproducible provisional audit package.
"""

from __future__ import annotations

import argparse
import json
from pathlib import Path

import numpy as np
import pandas as pd


def build_outputs(planning_csv: Path, case_summary_csv: Path, outdir: Path) -> None:
    outdir.mkdir(parents=True, exist_ok=True)

    pi = pd.read_csv(planning_csv)
    cs = pd.read_csv(case_summary_csv)

    if "is_small_renal_mass" in pi.columns:
        pi["is_small_renal_mass"] = pi["is_small_renal_mass"].astype(bool)
    if "cyst_adjacent_1voxel" in pi.columns:
        pi["cyst_adjacent_1voxel"] = pi["cyst_adjacent_1voxel"].astype(bool)

    case_srm_counts = (
        pi.groupby("case_id", dropna=False)["is_small_renal_mass"]
        .sum()
        .rename("n_srm_candidates_in_case")
        .astype(int)
    )
    pi = pi.merge(case_srm_counts, on="case_id", how="left")

    pi["flag_dmax_gt_40mm"] = pi["d_max_mm"] > 40.0
    pi["flag_geometry_degenerate"] = (pi["n_tumor_voxels"] <= 1) | (pi["d_max_mm"] <= 0.0)
    pi["flag_micro_component_review"] = (pi["d_max_mm"] < 5.0) | (pi["n_tumor_voxels"] <= 5)
    pi["flag_cystic_interference_review_pending"] = pi["cyst_adjacent_1voxel"]
    pi["flag_multifocal_srm_review"] = pi["n_srm_candidates_in_case"] > 1

    pi["tumor_cyst_contact_flag"] = pi["cyst_adjacent_1voxel"].astype(bool)
    pi["tumor_cyst_min_distance_mm"] = np.where(pi["cyst_adjacent_1voxel"], 0.0, np.nan)
    pi["cyst_in_roi_flag"] = pi["cyst_adjacent_1voxel"].astype(bool)
    pi["nearest_other_srm_distance_mm"] = np.nan
    pi["roi_overlap_flag"] = np.nan

    pi["hard_exclude"] = pi["flag_dmax_gt_40mm"] | pi["flag_geometry_degenerate"]

    review_flag_cols = [
        "flag_micro_component_review",
        "flag_cystic_interference_review_pending",
        "flag_multifocal_srm_review",
    ]
    pi["review_only"] = pi[review_flag_cols].any(axis=1)

    eligible_v1 = pi[(pi["is_small_renal_mass"]) & (~pi["hard_exclude"])].copy()

    subgroup_labels = pi[[
        "case_id",
        "lesion_id",
        "subgroup",
        "is_small_renal_mass",
        "n_srm_candidates_in_case",
        "flag_multifocal_srm_review",
    ]].rename(columns={"subgroup": "prespecified_subgroup"})
    subgroup_labels.to_csv(outdir / "subgroup_labels.csv", index=False)

    roi_cols = [
        "case_id",
        "lesion_id",
        "segmentation_path",
        "n_tumor_voxels",
        "voxel_volume_mm3",
        "tumor_volume_mm3",
        "tumor_volume_ml",
        "d_max_mm",
        "subgroup",
        "is_small_renal_mass",
        "kidney_voxels",
        "kidney_volume_mm3",
        "kidney_volume_ml",
        "cyst_voxels",
        "cyst_volume_mm3",
        "cyst_volume_ml",
        "cyst_adjacent_1voxel",
        "tumor_cyst_contact_flag",
        "tumor_cyst_min_distance_mm",
        "cyst_in_roi_flag",
        "bbox_x_mm",
        "bbox_y_mm",
        "bbox_z_mm",
        "n_srm_candidates_in_case",
        "nearest_other_srm_distance_mm",
        "roi_overlap_flag",
        "flag_dmax_gt_40mm",
        "flag_geometry_degenerate",
        "flag_micro_component_review",
        "flag_cystic_interference_review_pending",
        "flag_multifocal_srm_review",
        "hard_exclude",
        "review_only",
    ]
    roi_metadata = pi[roi_cols].copy()
    roi_metadata.to_csv(outdir / "roi_metadata.csv", index=False)

    exclusion_rows = []

    def add_rows(mask, code, reason, hard_exclude, review_only, stage):
        if int(mask.sum()) == 0:
            return
        subset = pi.loc[mask, ["case_id", "lesion_id"]].copy()
        subset["exclusion_stage"] = stage
        subset["exclusion_code"] = code
        subset["exclusion_reason"] = reason
        subset["hard_exclude"] = hard_exclude
        subset["review_only"] = review_only
        exclusion_rows.append(subset)

    add_rows(pi["flag_dmax_gt_40mm"], "DMAX_GT_40MM", "d_max > 40 mm; outside the protocol-defined SRM range", True, False, "candidate_screening")
    add_rows(pi["flag_geometry_degenerate"], "GEOMETRY_DEGENERATE_SINGLE_VOXEL_OR_ZERO_DMAX", "single-voxel or zero-diameter component; not a stable target for distance/margin-based geometric planning", True, False, "candidate_screening")
    add_rows(pi["flag_micro_component_review"] & (~pi["flag_geometry_degenerate"]), "MICRO_COMPONENT_REVIEW", "very small component (d_max < 5 mm or <= 5 voxels); review before deciding whether to keep as a true independent planning target", False, True, "pre_main_cohort_review")
    add_rows(pi["flag_cystic_interference_review_pending"], "CYSTIC_INTERFERENCE_REVIEW_PENDING", "1-voxel cyst adjacency triage flag is positive; formal cystic_interference rule not frozen yet", False, True, "pre_main_cohort_review")
    add_rows(pi["flag_multifocal_srm_review"], "MULTIFOCAL_SRM_REVIEW", "case contains more than one <=4 cm candidate component; confirm independent single-applicator target definition under frozen rules", False, True, "pre_main_cohort_review")

    if exclusion_rows:
        exclusion_log = pd.concat(exclusion_rows, ignore_index=True).sort_values(["case_id", "lesion_id", "hard_exclude", "review_only", "exclusion_code"], ascending=[True, True, False, False, True])
    else:
        exclusion_log = pd.DataFrame(columns=["case_id", "lesion_id", "exclusion_stage", "exclusion_code", "exclusion_reason", "hard_exclude", "review_only"])
    exclusion_log.to_csv(outdir / "exclusion_log.csv", index=False)

    eligible_cols = [
        "case_id",
        "lesion_id",
        "subgroup",
        "is_small_renal_mass",
        "n_tumor_voxels",
        "tumor_volume_ml",
        "d_max_mm",
        "cyst_adjacent_1voxel",
        "tumor_cyst_contact_flag",
        "tumor_cyst_min_distance_mm",
        "cyst_in_roi_flag",
        "n_srm_candidates_in_case",
        "nearest_other_srm_distance_mm",
        "roi_overlap_flag",
        "flag_micro_component_review",
        "flag_cystic_interference_review_pending",
        "flag_multifocal_srm_review",
    ]
    eligible_v1[eligible_cols].to_csv(outdir / "eligible_main_cohort_v1.csv", index=False)

    summary = {
        "input_files": {
            "planning_instances_csv": str(planning_csv.resolve()),
            "case_summary_csv": str(case_summary_csv.resolve()),
        },
        "n_cases_in_case_summary": int(len(cs)),
        "n_raw_instances_total": int(len(pi)),
        "n_raw_srm_candidates": int(pi["is_small_renal_mass"].sum()),
        "n_hard_excluded_total": int(pi["hard_exclude"].sum()),
        "n_hard_excluded_srm": int((pi["hard_exclude"] & pi["is_small_renal_mass"]).sum()),
        "n_eligible_main_cohort_v1": int(len(eligible_v1)),
        "eligible_main_cohort_v1_subgroups": {str(k): int(v) for k, v in eligible_v1["subgroup"].value_counts(dropna=False).to_dict().items()},
        "review_flag_counts_within_eligible_v1": {
            "micro_component_review": int(eligible_v1["flag_micro_component_review"].sum()),
            "cystic_interference_review_pending": int(eligible_v1["flag_cystic_interference_review_pending"].sum()),
            "multifocal_srm_review": int(eligible_v1["flag_multifocal_srm_review"].sum()),
        },
        "notes": [
            "eligible_main_cohort_v1 applies only hard exclusions; it is not the final main cohort",
            "formal cystic_interference still requires a frozen operational rule",
            "multifocal independence still requires a frozen operational rule",
            "micro_component_review is intentionally not auto-excluded in this provisional audit",
        ],
    }
    (outdir / "cohort_audit_summary.json").write_text(json.dumps(summary, indent=2), encoding="utf-8")

    print(f"Wrote {outdir / 'subgroup_labels.csv'}")
    print(f"Wrote {outdir / 'roi_metadata.csv'}")
    print(f"Wrote {outdir / 'exclusion_log.csv'}")
    print(f"Wrote {outdir / 'eligible_main_cohort_v1.csv'}")
    print(f"Wrote {outdir / 'cohort_audit_summary.json'}")


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Audit candidate planning instances.")
    parser.add_argument("--planning-csv", required=True, type=Path)
    parser.add_argument("--case-summary-csv", required=True, type=Path)
    parser.add_argument("--outdir", required=True, type=Path)
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    build_outputs(args.planning_csv, args.case_summary_csv, args.outdir)


if __name__ == "__main__":
    main()
