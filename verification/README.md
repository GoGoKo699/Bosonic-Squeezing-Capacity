# Reproduce the finite checks

From the repository root, install the numerical dependencies in [requirements.txt](requirements.txt), then run:

```bash
python3 verification/heat_trace.py
python3 verification/log_box.py
python3 verification/gaussian_log_variance.py
python3 verification/capacity_bounds.py
python3 verification/check_sources.py
```

| Program | Independent quantities compared | What a pass establishes |
| --- | --- | --- |
| `heat_trace.py` | Finite Fock matrices versus the Casimir identity and analytic Mehler trace; numerical integration versus the heat-trace majorant | Selected normalization, algebra, and majorant checks |
| `log_box.py` | Whole-subspace Gram, generator, and energy forms; physical-coordinate and log-coordinate quadrature; protected-qubit integrals | Selected finite constructions obey the stated forms and bounds |
| `gaussian_log_variance.py` | Direct folded-normal logarithmic integrals versus noncentral-chi-square Poisson-mixture formulas | Agreement at six declared noncentralities and the corresponding derivative signs |
| `capacity_bounds.py` | Established finite-energy formulas, their ordering, and a conservative non-Gaussian rate witness | A reproducible plot of bounds and the stated example |
| `check_sources.py` | Local links, explicit anchors, protected mathematics, and Python compilation | Source consistency and navigation |

The analytical proofs establish the capacity law and the Gaussian-input bound. Finite Fock truncations, quadrature checks, and structural checks do not prove a general capacity theorem or certify experimental performance.

The plotted lower curve is a maximum over a fixed sampled list of valid bandwidth choices, together with the inherited one-qubit floor at `E≥1`. It need not optimize the lower bound. The gray curve is an all-code upper bound. The Gaussian-input line bounds coherent information for Gaussian physical input states; it is not the capacity of a separately specified Gaussian-hardware coding model.

The figure uses the exact fixed-axis, lossless channel at `sigma=1` and mean input energy. No numerical result here establishes loss tolerance, an efficient encoder, or a practical energy crossover.

The [recorded report](REPORT.md) states the checks actually run on the integrated source. Hosted mathematical and visual review belongs to the final furnished revision and is separate from these local checks.
