#!/usr/bin/env python3
"""Plot a variable from an OpenModelica .mat result file to a PNG image.

Usage:
    python3 plot_result.py <result.mat> [variable] [output.png]

Example:
    python3 plot_result.py SimpleRC_res.mat Vc Vc.png
"""
import sys

import DyMat
import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt


def main():
    if len(sys.argv) < 2:
        print(__doc__)
        sys.exit(1)

    mat_path = sys.argv[1]
    variable = sys.argv[2] if len(sys.argv) > 2 else "Vc"
    out_path = sys.argv[3] if len(sys.argv) > 3 else f"{variable}.png"

    data = DyMat.DyMatFile(mat_path)
    time = data.abscissa(variable)[0]
    values = data.data(variable)

    plt.figure(figsize=(8, 5))
    plt.plot(time, values)
    plt.xlabel("time [s]")
    plt.ylabel(variable)
    plt.title(f"{variable} vs time ({mat_path})")
    plt.grid(True)
    plt.savefig(out_path, dpi=150)
    print(f"Saved plot to {out_path}")


if __name__ == "__main__":
    main()
