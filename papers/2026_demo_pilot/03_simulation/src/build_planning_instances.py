#!/usr/bin/env python3
"""
Build candidate KiTS23 planning instances from segmentation labels only.

Assumptions:
- dataset_root contains directories like `case_00000/`
- each case directory contains `segmentation.nii.gz`
- label encoding follows KiTS23 convention:
    0 background
    1 kidney
    2 tumor
    3 cyst

Outputs:
- planning_instances.csv
- case_summary.csv
- manifest.json

This script does NOT:
- decide cystic interference for the main cohort
- run any ablation planning
- compute clinical endpoints

It only builds a deterministic pre-audit table for protocol-frozen screening.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import math
from dataclasses import dataclass, asdict
from pathlib import Path
from typing import Iterable, List, Tuple

import nibabel as nib
import numpy as np
import pandas as pd
from scipy import ndimage
from scipy.spatial import ConvexHull, distance


LABEL_BACKGROUND = 0
LABEL_KIDNEY = 1
LABEL_TUMOR = 2
LABEL_CYST = 3


@dataclass
class PlanningInstance:
    case_id: str
    lesion_id: str
    segmentation_path: str
    n_tumor_voxels: int
    voxel_volume_mm3: float
    tumor_volume_mm3: float
    tumor_volume_ml: float
    d_max_mm: float
    subgroup: str
    is_small_renal_mass: bool
    kidney_voxels: int
    kidney_volume_mm3: float
    kidney_volume_ml: float
    cyst_voxels: int
    cyst_volume_mm3: float
    cyst_volume_ml: float
    cyst_adjacent_1voxel: bool
    bbox_x_mm: float
    bbox_y_mm: float
    bbox_z_mm: float


def sha256_of_file(path: Path, chunk_size: int = 1024 * 1024) -> str:
    h = hashlib.sha256()
    with path.open("rb") as f:
        while True:
            block = f.read(chunk_size)
            if not block:
                break
            h.update(block)
    return h.hexdigest()


def discover_cases(dataset_root: Path) -> List[Path]:
    return sorted([p for p in dataset_root.glob("case_*") if p.is_dir()])


def get_segmentation_path(case_dir: Path) -> Path:
    return case_dir / "segmentation.nii.gz"


def voxel_volume_mm3(affine: np.ndarray) -> float:
    return float(abs(np.linalg.det(affine[:3, :3])))


def voxel_centers_world(mask: np.ndarray, affine: np.ndarray) -> np.ndarray:
    ijk = np.argwhere(mask)
    if ijk.size == 0:
        return np.empty((0, 3), dtype=np.float64)
    homog = np.c_[ijk, np.ones(len(ijk))]
    xyz = homog @ affine.T
    return xyz[:, :3]


def max_pairwise_distance_mm(points_xyz: np.ndarray) -> float:
    n = len(points_xyz)
    if n == 0:
        return 0.0
    if n == 1:
        return 0.0
    if n == 2:
        return float(np.linalg.norm(points_xyz[0] - points_xyz[1]))
    try:
        hull = ConvexHull(points_xyz)
        hull_points = points_xyz[hull.vertices]
    except Exception:
        hull_points = points_xyz
    if len(hull_points) > 5000:
        # fallback: boundary subsampling by farthest-point style deterministic stride
        step = max(1, len(hull_points) // 5000)
        hull_points = hull_points[::step]
    d = distance.pdist(hull_points, metric="euclidean")
    return float(d.max()) if len(d) else 0.0


def physical_bbox_extents_mm(points_xyz: np.ndarray) -> Tuple[float, float, float]:
    if len(points_xyz) == 0:
        return 0.0, 0.0, 0.0
    mins = points_xyz.min(axis=0)
    maxs = points_xyz.max(axis=0)
    ext = maxs - mins
    return float(ext[0]), float(ext[1]), float(ext[2])


def connected_components_3d(binary_mask: np.ndarray) -> Tuple[np.ndarray, int]:
    structure = ndimage.generate_binary_structure(rank=3, connectivity=3)  # 26-connectivity
    labeled, n = ndimage.label(binary_mask.astype(np.uint8), structure=structure)
    return labeled, int(n)


def one_voxel_adjacency(component_mask: np.ndarray, other_mask: np.ndarray) -> bool:
    structure = ndimage.generate_binary_structure(rank=3, connectivity=3)
    dilated = ndimage.binary_dilation(component_mask, structure=structure, iterations=1)
    return bool(np.any(dilated & other_mask))


def subgroup_from_dmax_mm(d_max_mm: float) -> str:
    if d_max_mm <= 30.0:
        return "<=3cm"
    if d_max_mm <= 40.0:
        return "3-4cm"
    return ">4cm"


def build_case_instances(case_dir: Path) -> List[PlanningInstance]:
    seg_path = get_segmentation_path(case_dir)
    img = nib.load(str(seg_path))
    seg = np.asanyarray(img.dataobj)
    affine = img.affine
    vv = voxel_volume_mm3(affine)

    tumor_mask = seg == LABEL_TUMOR
    kidney_mask = seg == LABEL_KIDNEY
    cyst_mask = seg == LABEL_CYST

    labeled, n_components = connected_components_3d(tumor_mask)

    instances: List[PlanningInstance] = []
    kidney_voxels = int(kidney_mask.sum())
    kidney_volume_mm3 = kidney_voxels * vv
    cyst_voxels = int(cyst_mask.sum())
    cyst_volume_mm3 = cyst_voxels * vv

    for idx in range(1, n_components + 1):
        comp = labeled == idx
        n_vox = int(comp.sum())
        pts = voxel_centers_world(comp, affine)
        d_max_mm = max_pairwise_distance_mm(pts)
        bx, by, bz = physical_bbox_extents_mm(pts)
        subgroup = subgroup_from_dmax_mm(d_max_mm)
        instances.append(
            PlanningInstance(
                case_id=case_dir.name,
                lesion_id=f"{case_dir.name}_lesion_{idx:03d}",
                segmentation_path=str(seg_path),
                n_tumor_voxels=n_vox,
                voxel_volume_mm3=vv,
                tumor_volume_mm3=n_vox * vv,
                tumor_volume_ml=(n_vox * vv) / 1000.0,
                d_max_mm=d_max_mm,
                subgroup=subgroup,
                is_small_renal_mass=(d_max_mm <= 40.0),
                kidney_voxels=kidney_voxels,
                kidney_volume_mm3=kidney_volume_mm3,
                kidney_volume_ml=kidney_volume_mm3 / 1000.0,
                cyst_voxels=cyst_voxels,
                cyst_volume_mm3=cyst_volume_mm3,
                cyst_volume_ml=cyst_volume_mm3 / 1000.0,
                cyst_adjacent_1voxel=one_voxel_adjacency(comp, cyst_mask),
                bbox_x_mm=bx,
                bbox_y_mm=by,
                bbox_z_mm=bz,
            )
        )
    return instances


def ensure_parent(path: Path) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--dataset-root", type=Path, required=True, help="Path containing case_* directories.")
    parser.add_argument("--output-dir", type=Path, required=True, help="Directory for CSV/JSON outputs.")
    parser.add_argument("--hash-files", action="store_true", help="Compute SHA256 for each segmentation file.")
    args = parser.parse_args()

    dataset_root = args.dataset_root.resolve()
    output_dir = args.output_dir.resolve()
    output_dir.mkdir(parents=True, exist_ok=True)

    cases = discover_cases(dataset_root)
    if not cases:
        raise SystemExit(f"No case_* directories found under {dataset_root}")

    all_instances: List[PlanningInstance] = []
    case_rows = []

    for case_dir in cases:
        seg_path = get_segmentation_path(case_dir)
        if not seg_path.exists():
            case_rows.append(
                {
                    "case_id": case_dir.name,
                    "segmentation_path": str(seg_path),
                    "segmentation_exists": False,
                    "segmentation_sha256": None,
                    "n_lesions": 0,
                    "n_srm_lesions": 0,
                    "status": "missing_segmentation",
                }
            )
            continue

        instances = build_case_instances(case_dir)
        all_instances.extend(instances)
        case_rows.append(
            {
                "case_id": case_dir.name,
                "segmentation_path": str(seg_path),
                "segmentation_exists": True,
                "segmentation_sha256": sha256_of_file(seg_path) if args.hash_files else None,
                "n_lesions": len(instances),
                "n_srm_lesions": int(sum(x.is_small_renal_mass for x in instances)),
                "status": "ok",
            }
        )

    planning_instances_csv = output_dir / "planning_instances.csv"
    case_summary_csv = output_dir / "case_summary.csv"
    manifest_json = output_dir / "manifest.json"

    planning_df = pd.DataFrame([asdict(x) for x in all_instances]).sort_values(
        ["case_id", "lesion_id"]
    )
    case_df = pd.DataFrame(case_rows).sort_values(["case_id"])

    planning_df.to_csv(planning_instances_csv, index=False)
    case_df.to_csv(case_summary_csv, index=False)

    manifest = {
        "script": "build_planning_instances.py",
        "dataset_root": str(dataset_root),
        "output_dir": str(output_dir),
        "n_cases_discovered": len(cases),
        "n_instances_total": int(len(planning_df)),
        "n_srm_instances": int(planning_df["is_small_renal_mass"].sum()) if len(planning_df) else 0,
        "files": {
            "planning_instances_csv": str(planning_instances_csv),
            "case_summary_csv": str(case_summary_csv),
        },
        "notes": [
            "cyst_adjacent_1voxel is a triage flag only, not the formal cystic-interference exclusion rule",
            "d_max_mm is computed from maximum pairwise distance among convex-hull-reduced voxel centers in world coordinates",
            "formal eligibility still requires the protocol-frozen exclusion audit",
        ],
    }
    manifest_json.write_text(json.dumps(manifest, indent=2), encoding="utf-8")

    print(f"Wrote {planning_instances_csv}")
    print(f"Wrote {case_summary_csv}")
    print(f"Wrote {manifest_json}")


if __name__ == "__main__":
    main()
