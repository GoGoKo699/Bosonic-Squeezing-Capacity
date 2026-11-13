#!/usr/bin/env python3
"""Plot proven bounds, not an exact finite-energy capacity computation."""
from pathlib import Path
import csv
import json
import math

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np

ROOT = Path(__file__).resolve().parents[1]
LN2 = math.log(2.0)


def g2(u):
    if u <= 0:
        return 0.0
    return (math.log1p(u) + u * math.log1p(1.0 / u)) / LN2


def lower_bound(energy, sigma, bandwidths):
    best = 1.0 if energy >= 1.0 else 0.0
    selected = None
    for k in bandwidths:
        c = (1.0 + (k + 0.5) ** 2) / 2.0
        length = math.log((energy + 0.5) / c)
        dim = math.floor(k * length / math.pi - 1e-12)
        if dim < 1:
            continue
        value = math.log2(2 * dim) - g2(sigma * sigma * k * k)
        if value > best:
            best = value
            selected = {"K": float(k), "L": length, "dimension": 2 * dim}
    return best, selected


def upper_bound(energy, sigma):
    a = max(1.0, math.exp(2.0 * sigma * sigma) * (energy + 0.5))
    c = 0.5 * math.log2(2.0 * math.pi * math.e *
                        (25.0 / 12.0 + 1.0 / (2.0 * sigma * sigma)))
    return min(g2(energy), c + math.log2(
        math.e / math.pi * math.log(10.0 * a)))


def main():
    sigma = 1.0
    gaussian = 1.0 + 0.5 * math.log2(1.0 + math.pi ** 2 /
                                   (8.0 * sigma * sigma))
    bandwidths = np.geomspace(0.015, 4.0, 320)
    x = np.linspace(0.0, 40.0, 401)
    rows = []
    for exponent in x:
        energy = 10.0 ** exponent
        low, code = lower_bound(energy, sigma, bandwidths)
        high = upper_bound(energy, sigma)
        if low > high + 1e-10:
            raise ValueError("Numerical bound ordering failed")
        rows.append((float(exponent), energy, low, high, gaussian, code))

    out = ROOT / "figures"
    out.mkdir(exist_ok=True)
    with (out / "capacity_bounds.csv").open("w", newline="") as stream:
        writer = csv.writer(stream)
        writer.writerow(["log10_mean_input_photons", "mean_input_photons",
                         "achievable_rate_lower_bound",
                         "unrestricted_capacity_upper_bound",
                         "gaussian_input_CI_upper_bound"])
        writer.writerows(row[:5] for row in rows)

    low = np.array([row[2] for row in rows])
    high = np.array([row[3] for row in rows])
    plt.rcParams.update({"font.family": "DejaVu Sans", "font.size": 11,
                         "svg.fonttype": "none"})
    fig, ax = plt.subplots(figsize=(9.5, 5.1), layout="constrained")
    ax.fill_between(x, low, high, color="#e5f1ef", zorder=0)
    ax.plot(x, high, color="#45535b", lw=2, ls="--",
            label="Upper bound for every quantum code")
    ax.plot(x, low, color="#006b65", lw=2.6,
            label="Achievable non-Gaussian rate bound")
    ax.axhline(gaussian, color="#ad6b2c", lw=2, ls=":",
               label="Upper bound for Gaussian-input coherent information")
    ax.set(xlabel=r"Mean input photon budget, $\log_{10} E$",
           ylabel="Qubits per use", xlim=(0, 40), ylim=(0, 11.2))
    ax.set_title(r"Fixed-axis squeezing noise: $\sigma=1$",
                 loc="left", fontsize=15, fontweight="bold", pad=13)
    ax.grid(axis="y", color="#d7dfdf", lw=0.6)
    ax.spines[["top", "right"]].set_visible(False)
    ax.legend(loc="upper left", frameon=False, fontsize=9.5)
    ax.text(39.5, 0.25, "Analytical bounds; constants are not optimized",
            ha="right", color="#58686d", fontsize=9)
    fig.savefig(out / "capacity_bounds.svg")
    fig.savefig(out / "capacity_bounds.png", dpi=150)
    plt.close(fig)

    energy = 1e20
    k = 0.25
    c = (1 + (k + 0.5) ** 2) / 2
    length = math.log((energy + 0.5) / c)
    d = math.floor(k * length / math.pi)
    witness = math.log2(2 * d) - g2(sigma ** 2 * k ** 2)
    if witness <= gaussian:
        raise ValueError("Finite analytical witness did not exceed benchmark")
    print(json.dumps({
        "status": "passed",
        "scope": "Evaluation of established bounds and one conservative finite-energy witness; not an optimized capacity calculation.",
        "sigma": sigma,
        "example": {"E": energy, "K": k, "L": length,
                    "dimension": 2 * d,
                    "achievable_rate_lower_bound": witness,
                    "gaussian_input_CI_upper_bound": gaussian},
        "figure_points": len(rows)
    }, indent=2))


if __name__ == "__main__":
    main()
