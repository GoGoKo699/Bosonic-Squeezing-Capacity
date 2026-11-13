# The inherited quadrature-sign/parity qubit

[Scientific overview](README.md) · [Model](01-model.md) · [Achievability](02-achievability.md)

Fixed-axis squeezing preserves a coherent two-dimensional subsystem. This is the quadrature-sign/parity (QSP) encoding introduced by Marshall, James, Paler, and Lau, *Universal quantum computing with thermal state bosonic systems*, Physical Review A **99**, 032345 (2019), [DOI](https://doi.org/10.1103/PhysRevA.99.032345). Their Section III and Eq. (18) specify quadrature sign and oscillator parity as logical Pauli operators. This subsystem and its Pauli algebra are prior work; their appearance here is not the new capacity contribution.

The purpose of this account is to make the subsystem's exact action under the present noise, its reference-complete recovery, and a finite-energy example explicit.

## Logical observables and the factorization

Let $`\Pi=(-1)^n`$ be physical parity, so $`(\Pi\psi)(x)=\psi(-x)`$. The bounded observables

```math
A=\mathrm{sgn}(Q),\qquad \Pi=(-1)^n
```

satisfy

```math
A^2=\Pi^2=I,\qquad A\Pi=-\Pi A.
```

The point $`x=0`$ has zero spectral measure and does not affect these identities. Thus these observables generate the algebra of a qubit. Marshall et al. label quadrature sign as logical $`X`$ and parity as logical $`Z`$; choosing the sign eigenbasis instead only relabels the logical Pauli axes.

Use the unitary map

```math
(W\psi)_s(y)=e^{y/2}\psi(se^y),\qquad s\in\{+,-\}.
```

It identifies the physical mode with $`L^2(\mathbb R_y)\otimes\mathbb C^2`$. In this representation,

```math
WAW^\dagger=I\otimes Z_{\rm L},\qquad
W\Pi W^\dagger=I\otimes X_{\rm L},\qquad
WGW^\dagger=(-i\partial_y)\otimes I_{\rm L},
```

where $`G=(QP+PQ)/2`$. In particular,

```math
We^{-irG}W^\dagger=T_r\otimes I_{\rm L},\qquad
(T_rg)(y)=g(y-r).
```

Both logical observables commute with every fixed-axis squeezing unitary. The channel therefore has the exact form

```math
W\,\mathcal N_\sigma(W^\dagger(\,\cdot\,)W)\,W^\dagger
=\mathcal T_\sigma\otimes\mathrm{id}_{\rm L},\qquad
\mathcal T_\sigma(\eta)=\int p_\sigma(r)T_r\eta T_r^\dagger\,dr.
```

The factor $`\mathbb C^2`$ is not merely a classical sign flag. Parity exchanges the two signs coherently, and arbitrary relative phases between them are preserved.

## Exact recovery, including an external reference

Choose a fixed normalized gauge state $`\eta`$ on $`L^2(\mathbb R_y)`$ for which the resulting physical inputs have finite energy. Define

```math
\mathcal E_\eta(\tau)=W^\dagger(\eta\otimes\tau)W,\qquad
\mathcal D(\rho)=\mathrm{Tr}_{y}(W\rho W^\dagger).
```

These are a trace-preserving encoder and decoder. The channel changes only the gauge state:

```math
\mathcal N_\sigma(\mathcal E_\eta(\tau))
=W^\dagger(\mathcal T_\sigma(\eta)\otimes\tau)W.
```

Hence

```math
\mathcal D\circ\mathcal N_\sigma\circ\mathcal E_\eta
=\mathrm{id}_{\rm L}.
```

For every external reference $`R`$ and every joint state $`\omega_{R{\rm L}}`$,

```math
\bigl(\mathrm{id}_R\otimes
 [\mathcal D\circ\mathcal N_\sigma\circ\mathcal E_\eta]\bigr)
 (\omega_{R{\rm L}})=\omega_{R{\rm L}}.
```

Thus the statement preserves arbitrary qubit coherence and entanglement. It does not require estimating the squeezing realization, postselection, or returning the gauge to its initial physical state. Gauge disturbance is allowed by a noiseless-subsystem code.

## An exact example with one mean input photon

Define the orthonormal half-line wavefunctions

```math
\psi_+(x)=2\pi^{-1/4}\,x e^{-x^2/2}\,\mathbf 1_{\{x>0\}},\qquad
\psi_-(x)=\psi_+(-x).
```

They are mirrored restrictions of the first excited oscillator wavefunction, normalized on each half-line. They vanish at the origin. Their weak first derivatives are square integrable, so they lie in the oscillator quadratic-form domain even though the derivative need not match across the origin. Direct integration gives

```math
\langle Q^2\rangle_{\psi_\pm}=\frac32,\qquad
\langle P^2\rangle_{\psi_\pm}=\frac32,\qquad
\langle n\rangle_{\psi_\pm}=1.
```

Position and derivative supports of the two components are disjoint up to a null set. Therefore the off-diagonal energy quadratic forms vanish, and every normalized superposition $`\alpha\psi_++\beta\psi_-`$ also has mean input photon number exactly one.

The two functions have the same logarithmic-coordinate gauge profile,

```math
g_0(y)=2\pi^{-1/4}e^{3y/2}e^{-e^{2y}/2}.
```

Encoding the logical basis into $`\psi_+,\psi_-`$ is therefore precisely $`\mathcal E_{|g_0\rangle\langle g_0|}`$. The preceding decoder recovers every qubit and its reference exactly for every $`\sigma>0`$. In particular,

```math
Q_\sigma(E)\ge1,\qquad E\ge1.
```

This is an explicit finite-energy realization of the inherited subsystem, not an exact finite-energy capacity formula. No claim is made that one mean photon is the least average energy of every possible communication scheme.

The output can carry more energy than the input. For this example its mean output photon number is $`\tfrac32e^{2\sigma^2}-\tfrac12`$. Exact logical preservation does not mean that physical energy or the gauge state is unchanged.

## What the subsystem does and does not supply

The protected sign/parity factor contributes one qubit. The growing $`\log_2\ln E`$ rate instead comes from the increasing number of modes that fit into the logarithmic-coordinate interval, as proved in [the achievability account](02-achievability.md). The sign factor alone does not establish that growth or the converse.

The exact recovery above is an ideal capacity-model operation. A physical realization of the logarithmic-coordinate extraction, half-line profiles, and arbitrary logical recovery requires non-Gaussian control. This account establishes no efficient circuit, preparation time, detector resolution, or recovery-work bound. Finite-precision synthesis would need a separate quantitative error analysis.

The noise restriction is essential: every squeezing operation must use the same known axis. Generic rotations, displacements, loss, or uncertain squeezing axes need not preserve both quadrature sign and parity. Their addition is outside the exact identity established here.
