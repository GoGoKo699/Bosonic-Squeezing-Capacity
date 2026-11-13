#!/usr/bin/env python3
"""Selected convention checks for the squeezing-generator heat trace.

Requires NumPy and SciPy. Run: python3 verification/heat_trace.py

Finite Fock checks validate the Casimir identity away from the truncation
boundary and selected values of the Mehler trace. Numerical quadrature
checks the integral majorant. These checks do not prove the capacity
theorem, operator-domain statements, or arbitrary-input bounds.
"""
from __future__ import annotations

import json
import math

import numpy as np
from scipy.integrate import quad
from scipy.linalg import expm


def exact_trace(beta: float, t: float) -> float:
    """Stable [2(cosh(beta) cosh(t)-1)]^(-1/2)."""
    t = abs(t)
    if t > 80.0:
        return math.exp(-t / 2.0) / math.sqrt(math.cosh(beta))
    return 1.0 / (
        2.0 * math.sqrt(
            math.sinh(beta / 2.0) ** 2
            + math.cosh(beta) * math.sinh(t / 2.0) ** 2
        )
    )


def matrix_checks(cutoff: int = 180) -> dict:
    a = np.diag(np.sqrt(np.arange(1, cutoff, dtype=float)), 1)
    ad = a.T
    generator = 0.5j * (ad @ ad - a @ a)
    other_generator = 0.5 * (a @ a + ad @ ad)
    h = np.arange(cutoff, dtype=float) + 0.5
    residual = (
        generator @ generator + other_generator @ other_generator
        - np.diag(h * h + 0.75)
    )
    # Quadratic generators change Fock number by two. Four removed
    # boundary rows/columns keep this diagnostic away from truncation.
    interior_error = float(np.max(np.abs(residual[:-4, :-4])))
    cases = []
    for beta, t in [(0.2, 0.3), (0.4, 1.0), (0.8, 1.5)]:
        squeeze = expm(1j * t * generator)
        observed = np.sum(np.exp(-beta * h) * np.diag(squeeze))
        expected = exact_trace(beta, t)
        error = float(abs(observed - expected))
        case = {
            "beta": beta,
            "t": t,
            "finite_fock_trace_real": float(observed.real),
            "finite_fock_trace_imag": float(observed.imag),
            "mehler_trace": expected,
            "absolute_difference": error,
        }
        cases.append(case)
        if error > 1e-9:
            raise AssertionError(f"selected Mehler trace check failed: {case}")
    if interior_error > 1e-8:
        raise AssertionError(f"Casimir interior residual too large: {interior_error}")
    return {
        "fock_cutoff": cutoff,
        "casimir_interior_max_absolute_residual": interior_error,
        "mehler_cases": cases,
    }


def integral_checks() -> list[dict]:
    cases = []
    for beta in [1e-1, 1e-3, 1e-6]:
        # Splitting at beta resolves the small-t logarithmic contribution.
        options = {"epsabs": 1e-10, "epsrel": 1e-10, "limit": 300}
        core1, error1 = quad(lambda t: exact_trace(beta, t), 0.0, beta, **options)
        core2, error2 = quad(lambda t: exact_trace(beta, t), beta, 1.0, **options)
        tail, error3 = quad(lambda t: exact_trace(beta, t), 1.0, np.inf, **options)
        density_majorant = (core1 + core2 + tail) / math.pi
        exact_integral_bound = (
            math.asinh(1.0 / beta) - math.log(math.tanh(0.25))
        ) / math.pi
        round_constant_bound = math.log(10.0 / beta) / math.pi
        quadrature_error = (error1 + error2 + error3) / math.pi
        if density_majorant > exact_integral_bound + 1e-8:
            raise AssertionError("integral majorant violated at selected beta")
        if exact_integral_bound > round_constant_bound + 1e-12:
            raise AssertionError("rounded constant bound violated")
        cases.append({
            "beta": beta,
            "integral_over_2pi": density_majorant,
            "quadrature_error_estimate": quadrature_error,
            "analytic_split_integral_bound": exact_integral_bound,
            "log_10_over_beta_bound": round_constant_bound,
        })
    return cases


def main() -> None:
    report = {
        "status": "passed",
        "scope": (
            "Selected finite Fock convention checks and numerical quadrature "
            "of the heat-trace density majorant; no capacity certification."
        ),
        "matrix_checks": matrix_checks(),
        "integral_checks": integral_checks(),
    }
    print(json.dumps(report, indent=2))


if __name__ == "__main__":
    main()

