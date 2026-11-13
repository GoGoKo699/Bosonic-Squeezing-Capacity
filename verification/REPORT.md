# Scientific verification

The analytical account establishes the matching capacity law at fixed positive noise width and the Gaussian-input coherent-information bound. The following finite checks were run on November 13, 2026 with Python 3.12, NumPy 2.3.5, SciPy 1.17.0, and Matplotlib 3.10.8.

| Check | Observed result |
| --- | --- |
| Casimir identity in a 180-level Fock calculation | Interior maximum absolute residual below 4 × 10⁻¹² |
| Three finite-Fock Mehler-trace comparisons | Absolute differences below 4 × 10⁻¹⁵ |
| Heat-trace integral at three inverse temperatures | Numerical integrals lie below the analytic majorants |
| Four log-position subspaces | Gram, generator, and whole-subspace energy checks pass |
| Physical-coordinate/log-coordinate integral comparison | Normalization and quadratic forms agree |
| Protected qubit profile | Mean input photon number agrees with one |
| Normal log-radius variance at six noncentralities | Direct integrals and Poisson-mixture formulas agree within 5 × 10⁻¹⁵ |
| Finite-energy non-Gaussian witness | At sigma=1, E=10²⁰ and K=1/4, the rate lower bound exceeds 2.2420, while the Gaussian-input benchmark is below 1.5798 qubits per use |
| Source structure | Local links, math delimiters/braces, and Python compilation checked |

The exact finite outputs are stored under [results](results/). The [verification guide](README.md) gives the commands and their tested scope.

The scientific review reconstructed the all-block spectral-bin entropy argument, the Casimir form-domain bound, the complementary entropy estimate without a generator second-moment assumption, the whole-subspace energy bound, the constrained coding hypotheses, and the correlated Gaussian-input comparison. No controlling mathematical gap was found in that review. This is not independent expert certification or an exhaustive priority audit.

The computations support selected conventions and finite examples. They do not establish all-input theorems, experimental noise robustness, practical encoding cost, or exact finite-energy capacity. Final hosted mathematical and visual review follows furnishing and is not claimed by this report.
