#!/usr/bin/env python3
"""Compute superellipse arch offset values for different tooth and stroke values.

Usage: python -m compute_offsets
       python -m compute_offsets --tooth 60 80 100 120 --stroke 50 60 70 80
"""

import sys
import argparse

sys.path.insert(0, "src")
from config import FontConfig as fc
from utils.intersection import find_offset


def compute(tooth_values, stroke_values):
    width = fc.body_width + fc.h_overshoot
    hx = fc.hx
    hy = fc.hy

    # Print header
    header = f"{'':>10}" + "".join(f"  s={s:<12}" for s in stroke_values)
    print(header)
    print("-" * len(header))

    for tooth in tooth_values:
        row = f"t={tooth:<7}"
        for stroke in stroke_values:
            x1 = fc.width / 2 - width / 2 - stroke / 2
            y1 = -fc.overshoot
            x2 = fc.width / 2 + width / 2 + stroke / 2
            y2 = fc.x_height + fc.overshoot
            try:
                offset = find_offset(x1, y1, x2, y2, hx, hy, stroke, tooth)
                row += f"  {offset:>12.6f}"
            except ValueError:
                row += f"  {'N/A':>12}"
        print(row)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Compute arch offset for tooth/stroke combos")
    parser.add_argument(
        "--tooth", type=float, nargs="+",
        default=[60, 80, 100, 120, 140],
        help="Tooth values to test",
    )
    parser.add_argument(
        "--stroke", type=float, nargs="+",
        default=[50, 60, 70, 80, 90],
        help="Stroke values to test",
    )
    args = parser.parse_args()
    compute(args.tooth, args.stroke)
