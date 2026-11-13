#!/usr/bin/env python3
"""Cross-check the normal log-radius lemma by two distinct representations.

The proof is analytical. These bounded numerical checks compare direct
integration of a folded-normal density against its Poisson/chi-square mixture.
They do not certify a bound over an untested continuum.
"""

import json
import math

import numpy as np
from scipy.integrate import quad
from scipy.special import digamma, gammaln, polygamma


def direct_variance(theta):
    a = math.sqrt(2 * theta)

    def density(x):
        return (
            math.exp(-0.5 * (x - a) ** 2)
            + math.exp(-0.5 * (x + a) ** 2)
        ) / math.sqrt(2 * math.pi)

    cuts = sorted(set([0.0, 1.0, max(1.0, a - 7), a + 7])) + [math.inf]

    def moment(order):
        return sum(
            quad(
                lambda x: math.log(x) ** order * density(x),
                left,
                right,
                epsabs=2e-10,
                epsrel=2e-10,
                limit=300,
            )[0]
            for left, right in zip(cuts[:-1], cuts[1:])
        )

    mean = moment(1)
    return moment(2) - mean * mean


def poisson_variance(theta):
    if theta == 0:
        return math.pi**2 / 8, 0.0
    upper = int(math.ceil(theta + 15 * math.sqrt(theta + 1) + 100))
    k = np.arange(upper + 1, dtype=float)
    weights = np.exp(-theta + k * math.log(theta) - gammaln(k + 1))
    assert abs(weights.sum() - 1) < 2e-12
    f = digamma(k + 0.5)
    g = 1 / (k + 0.5)
    mean_f = np.dot(weights, f)
    variance = 0.25 * (
        np.dot(weights, polygamma(1, k + 0.5))
        + np.dot(weights, (f - mean_f) ** 2)
    )
    derivative = 0.5 * (
        np.dot(weights, f * g) - mean_f * np.dot(weights, g)
    )
    return float(variance), float(derivative)


def main():
    rows = []
    previous = math.inf
    for theta in [0, 0.01, 0.1, 1, 10, 100]:
        direct = direct_variance(theta)
        mixture, derivative = poisson_variance(theta)
        assert abs(direct - mixture) < 2e-8
        assert mixture <= math.pi**2 / 8 + 2e-12
        assert mixture <= previous + 2e-12
        assert derivative <= 2e-12
        previous = mixture
        rows.append(
            {
                "theta": theta,
                "direct_variance": direct,
                "poisson_variance": mixture,
                "variance_derivative": derivative,
                "absolute_difference": abs(direct - mixture),
            }
        )
    print(
        json.dumps(
            {
                "status": "passed",
                "scope": "Six finite theta values; direct integral versus mixture",
                "sharp_upper_bound": math.pi**2 / 8,
                "rows": rows,
            },
            indent=2,
        )
    )


if __name__ == "__main__":
    main()
