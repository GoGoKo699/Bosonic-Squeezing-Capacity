# Energy, noise, and coding

Fixed-strength random squeezing does not impose a finite quantum-capacity ceiling. Nevertheless, the additional coherent rate obtained by increasing oscillator energy is small:

```math
Q_\sigma(E)=\log_2\!\ln E+O_\sigma(1),
\qquad \sigma>0\text{ fixed}.
```

The photon budget needed for rate $`R`$ consequently grows as $`\exp(\Theta_\sigma(2^R))`$ at large $`R`$. This is an asymptotic resource relation. The constants are not an experimental crossover prediction, and the finite-energy bounds are not an exact capacity formula.

## A scale coordinate changes the energy geometry

In ordinary position, squeezing multiplies the coordinate by a random factor. In logarithmic position it is additive translation. The coordinate reduction is inherited from earlier work; the capacity question also requires transforming the physical photon Hamiltonian.

That Hamiltonian contains the weights $`e^{2y}`$ and $`e^{-2y}`$. A log-position interval of length $`L`$ therefore costs energy exponential in $`L`$. Keeping the squeezing-generator bandwidth fixed allows a subspace of dimension proportional to $`L`$ and bounds the entropy lost to the environment. Its coherent information grows as $`\log_2L`$, which becomes $`\log_2\ln E`$.

The converse makes the same restriction independent of this construction. The environment learns the squeezing-generator value to a fixed resolution. Information placed in widely separated generator bins is also available to that environment. The receiver's entropy in excess of the bin entropy is bounded by the harmonic heat-trace mass within one bin. That mass grows only as $`\ln E`$, producing the upper double logarithm.

## An exact qubit is compatible with slow capacity growth

The sign of position and parity generate an inherited logical qubit whose operators commute with same-axis squeezing. A finite-energy instance uses one mean input photon. It remains protected at every fixed noise strength in the ideal model.

This qubit explains why strong squeezing noise need not destroy all quantum information. It does not determine how much more can be transmitted as energy increases. The capacity theorem concerns that growing rate and requires both an all-code converse and increasing-dimensional input subspaces.

## What the Gaussian-input comparison means

The [Gaussian-input result](05-gaussian-inputs.md) bounds coherent information per use uniformly in energy when the joint physical input state is Gaussian, including correlated Gaussian states across uses. The unrestricted lower construction uses non-Gaussian states and eventually exceeds this bounded benchmark.

The restriction is on physical input states used in the coherent-information optimization. It is not a statement that every apparatus built from Gaussian components, every code described using Gaussian operations, or every non-Gaussian logical input processed by such operations satisfies the same restriction. No hardware-optimality conclusion is inferred.

## Relation to other oscillator noise

Smooth number-rotation noise has a bounded unlimited-energy capacity in the ordinary phase-dephasing model. Fixed one-quadrature displacement noise retains a logarithmic dependence on the usual oscillator energy. These facts do not imply the squeezing law by a change of notation: the generator's spectral structure and its relation to the charged Hamiltonian differ. The [comparison account](06-related-work.md) gives the exact models and inherited results.

The distinction also limits transfer to real devices. The squeezing axis is fixed and known, the stochastic parameter is not observed, and each use has an independent realization. No channel output is lost. Additional noise can change the protected subsystem and the capacity. The result is a benchmark for this specified noise mechanism, rather than a general claim about noisy parametric amplifiers.

The drive's mean energy injection is linear in input energy at fixed variance. Including that injection preserves the leading asymptotic law. Preparation complexity, recovery work, propagation time, loss tolerance, and finite-block performance have not been priced by a practical implementation study.
