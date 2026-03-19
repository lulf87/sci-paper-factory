#!/usr/bin/env python3
"""
Deterministic sanity checks for geometric preprocessing helpers.
Run before first formal planning run.
"""

from __future__ import annotations

import math
import numpy as np

from build_planning_instances import (
    max_pairwise_distance_mm,
    physical_bbox_extents_mm,
)


def assert_close(a: float, b: float, tol: float = 1e-6) -> None:
    if abs(a - b) > tol:
        raise AssertionError(f"{a} != {b} within tol={tol}")


def test_line_segment() -> None:
    pts = np.array([[0.0, 0.0, 0.0], [3.0, 4.0, 0.0]])
    d = max_pairwise_distance_mm(pts)
    assert_close(d, 5.0)


def test_bbox() -> None:
    pts = np.array([
        [0.0, 0.0, 0.0],
        [10.0, 2.0, 1.0],
        [4.0, 8.0, 7.0],
    ])
    bx, by, bz = physical_bbox_extents_mm(pts)
    assert_close(bx, 10.0)
    assert_close(by, 8.0)
    assert_close(bz, 7.0)


def test_tetrahedron() -> None:
    pts = np.array([
        [0.0, 0.0, 0.0],
        [1.0, 0.0, 0.0],
        [0.0, 2.0, 0.0],
        [0.0, 0.0, 2.0],
    ])
    d = max_pairwise_distance_mm(pts)
    expected = math.sqrt(8.0)
    assert_close(d, expected)


def main() -> None:
    test_line_segment()
    test_bbox()
    test_tetrahedron()
    print("All geometry sanity checks passed.")


if __name__ == "__main__":
    main()
