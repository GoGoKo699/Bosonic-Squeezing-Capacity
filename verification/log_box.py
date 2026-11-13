#!/usr/bin/env python3
"""Finite checks of the log-box energy forms and E=1 QSP profile.

These quadrature checks support only the listed finite parameters.
The capacity and all-energy claims are proved in science/02-achievability.md.
"""
import json
import math

import numpy as np
from numpy.polynomial.legendre import leggauss
from scipy.integrate import quad


def check_box(length, bandwidth):
    dimension = math.floor(bandwidth * length / math.pi)
    z, weights = leggauss(800)
    y = z * length / 2
    weights = weights * length / 2
    j = np.arange(1, dimension + 1)[:, None]
    phase = j * math.pi * (y[None, :] + length / 2) / length
    basis = math.sqrt(2 / length) * np.sin(phase)
    derivative = math.sqrt(2 / length) * j * math.pi / length * np.cos(phase)
    gram = (basis * weights) @ basis.T
    derivative_gram = (derivative * weights) @ derivative.T
    expected_derivative = np.diag((np.arange(1, dimension + 1) * math.pi / length) ** 2)
    gram_error = float(np.max(np.abs(gram - np.eye(dimension))))
    derivative_error = float(np.max(np.abs(derivative_gram - expected_derivative)))
    form_derivative = derivative - basis / 2
    q_form = (basis * (weights * np.exp(2 * y))) @ basis.T
    p_form = (form_derivative * (weights * np.exp(-2 * y))) @ form_derivative.T
    energy_form = (q_form + p_form) / 2
    maximum_h = float(np.linalg.eigvalsh(energy_form)[-1])
    safe_h = math.exp(length) * (1 + (bandwidth + 0.5) ** 2) / 2
    assert gram_error < 2e-11
    assert derivative_error < 2e-10
    assert maximum_h <= safe_h * (1 + 2e-12)
    assert float(np.linalg.eigvalsh(energy_form)[0]) >= 0.5 - 1e-10
    return {
        "L": length,
        "K": bandwidth,
        "dimension_per_sign": dimension,
        "gram_error": gram_error,
        "generator_form_error": derivative_error,
        "maximum_H_on_half_line_subspace": maximum_h,
        "safe_H_bound": safe_h,
    }


def check_physical_jacobian():
    length = 4.0
    left, right = math.exp(-length / 2), math.exp(length / 2)

    def g(y):
        return math.sqrt(2 / length) * math.sin(math.pi * (y + length / 2) / length)

    def gp(y):
        return math.sqrt(2 / length) * math.pi / length * math.cos(
            math.pi * (y + length / 2) / length
        )

    physical_norm = quad(lambda x: g(math.log(x)) ** 2 / x, left, right, epsabs=1e-12)[0]
    physical_q = quad(lambda x: x * g(math.log(x)) ** 2, left, right, epsabs=1e-12)[0]
    physical_p = quad(
        lambda x: (gp(math.log(x)) - g(math.log(x)) / 2) ** 2 / x ** 3,
        left, right, epsabs=1e-12
    )[0]
    log_q = quad(lambda y: math.exp(2 * y) * g(y) ** 2, -length / 2, length / 2)[0]
    log_p = quad(
        lambda y: math.exp(-2 * y) * (gp(y) - g(y) / 2) ** 2,
        -length / 2, length / 2
    )[0]
    assert abs(physical_norm - 1) < 1e-11
    assert abs(physical_q - log_q) < 1e-10
    assert abs(physical_p - log_p) < 1e-10
    return {"normalization": physical_norm, "Q2": physical_q, "P2": physical_p}


def check_protected_profile():
    scale = 2 * math.pi ** (-0.25)
    norm = quad(lambda x: scale ** 2 * x ** 2 * math.exp(-x ** 2), 0, np.inf)[0]
    q2 = quad(lambda x: scale ** 2 * x ** 4 * math.exp(-x ** 2), 0, np.inf)[0]
    p2 = quad(
        lambda x: scale ** 2 * (1 - x ** 2) ** 2 * math.exp(-x ** 2), 0, np.inf
    )[0]
    assert abs(norm - 1) < 1e-11
    assert abs(q2 - 1.5) < 1e-11
    assert abs(p2 - 1.5) < 1e-11
    return {"normalization": norm, "Q2": q2, "P2": p2, "mean_photons": (q2 + p2 - 1) / 2}


if __name__ == "__main__":
    report = {
        "status": "passed",
        "scope": "finite numerical quadrature checks, not a capacity proof",
        "boxes": [check_box(L, K) for L, K in [(4.0, 1.0), (8.0, 1.5), (12.0, 2.0), (18.0, 1.0)]],
        "physical_coordinate_cross_check": check_physical_jacobian(),
        "protected_qubit_profile": check_protected_profile(),
    }
    print(json.dumps(report, indent=2))
