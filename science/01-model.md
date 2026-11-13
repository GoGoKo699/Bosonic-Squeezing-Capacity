# Random squeezing and the photon budget

A fluctuating parametric drive can squeeze an oscillator by an unknown amount even when its squeezing axis is fixed. The resulting noise changes the scale of a wavefunction rather than translating it in phase space or rotating its phase. How much quantum information can additional oscillator energy protect against this noise?

The channel and its logarithmic-coordinate description have precedents in [noise-decoupling work](../references/README.md#sakuldee-tonekaboni). Here the task is communication through independent uses of the completed noisy channel. Encoding takes place before each use and decoding afterward; the noise interval cannot be interrupted.

## Channel and conventions

The oscillator Hilbert space is $`L^2(\mathbb R,dx)`$. The canonical observables satisfy $`[Q,P]=iI`$, and its reference energy and photon number are

```math
H=\frac{Q^2+P^2}{2}=\hat n+\frac12.
```

The squeezing generator is the self-adjoint closure of

```math
G=\frac{QP+PQ}{2}
=-i\left(x\frac{d}{dx}+\frac12\right)
```

on the Schwartz core. Its unitary group acts as

```math
(U_r\psi)(x)=e^{-r/2}\psi(e^{-r}x),
\qquad U_r=e^{-irG}.
```

For fixed $`\sigma>0`$, define the normal random-unitary channel

```math
\mathcal N_\sigma(\rho)
=\int_{\mathbb R}\frac{e^{-r^2/(2\sigma^2)}}{\sqrt{2\pi}\sigma}
U_r\rho U_r^\dagger\,dr.
```

The integral is in trace norm on trace-class inputs. The axis, variance, and law are known; the realized $`r`$ is revealed to neither party. Each use has a fresh independent draw. Deterministic squeezing can be removed by a known output unitary and is excluded from the centered convention above.

Although every $`U_r`$ is a Gaussian unitary, their mixture is generally a non-Gaussian channel. For a vacuum input,

```math
\langle Q^2\rangle_{\rm out}=\frac12e^{2\sigma^2},
\qquad
\langle Q^4\rangle_{\rm out}=\frac34e^{8\sigma^2}.
```

These moments violate the Gaussian relation $`\langle Q^4\rangle=3\langle Q^2\rangle^2`$ when $`\sigma>0`$. Canonical classifications of Gaussian channels therefore do not apply directly to this physical channel.

All quantum and discrete classical entropies use base-two logarithms. The notation $`\ln`$ denotes the natural logarithm. Write

```math
g_2(u)=(u+1)\log_2(u+1)-u\log_2u,
\qquad g_2(0)=0,
```

for the maximum entropy of an oscillator of mean photon number $`u`$.

## Operational capacity

An $`m`$-use entanglement-transmission code encodes a finite-dimensional logical system into $`m`$ input oscillators, applies $`\mathcal N_\sigma^{\otimes m}`$, and decodes jointly. Its entanglement fidelity is evaluated with an inaccessible reference. For the encoded maximally mixed logical state $`\rho_{A^m}`$, require

```math
\operatorname{Tr}\!\left[\rho_{A^m}\sum_{j=1}^m\hat n_j\right]
\le mE.
```

This is an unconditional mean budget across the complete block. It allows nonuniform energy allocation, unbounded photon-number tails, correlations between channel inputs, non-Gaussian states, and arbitrary collective decoding. It supplies no shared entanglement, quantum bypass, noise record, or intermediate control. Local ancillary systems and computation are unrestricted in the usual unassisted coding model.

The capacity $`Q_\sigma(E)`$ is the supremum of reliable asymptotic qubit rates per use. The standard energy-constrained coding theorem gives

```math
Q_\sigma(E)
=\lim_{m\to\infty}\frac1m
\sup_{\operatorname{Tr}\rho\sum_j\hat n_j\le mE}
I_{\rm c}(\rho,\mathcal N_\sigma^{\otimes m}),
```

with the equivalent supremum over blocklengths. The relevant conditions are verified in [achievability](02-achievability.md): the oscillator Hamiltonian satisfies the Gibbs condition, and the channel has an affine output-energy bound. No single-letter optimization or Gaussian optimality is needed for the main converse.

## Principal result

**Capacity law.** For every fixed $`\sigma>0`$,

```math
\boxed{\displaystyle
Q_\sigma(E)=\log_2\!\ln E+O_\sigma(1)
\qquad(E\to\infty).}
```

Equivalently, finite constants depending on $`\sigma`$ bound the difference between the capacity and $`\log_2\ln E`$ above and below for all sufficiently large $`E`$. The upper bound covers every code in the mean-budget model. The lower bound uses explicit finite-energy input subspaces and coherent-information coding.

The [achievability proof](02-achievability.md) supplies a finite-energy lower bound. The [converse](03-converse.md) supplies a finite-energy upper bound uniform in blocklength and input correlations. They establish the same leading coefficient, rather than only an upper estimate on a chosen family of encodings.

The limit keeps $`\sigma`$ fixed before increasing $`E`$. At $`\sigma=0`$ the channel is the identity and its capacity is $`g_2(E)`$. The displayed expansion is not uniform as $`\sigma\to0`$ or $`\sigma\to\infty`$.

## Logarithmic position and the environment

The unitary transformation

```math
(W\psi)_s(y)=e^{y/2}\psi(se^y),
\qquad s\in\{+1,-1\},\quad y\in\mathbb R,
```

identifies

```math
L^2(\mathbb R_x)
\simeq L^2(\mathbb R_y)\otimes\mathbb C^2,
\qquad
WGW^\dagger=P_y\otimes I_2,
\quad P_y=-i\frac{d}{dy}.
```

Squeezing translates $`y`$ and leaves the coherent sign factor unchanged. The transformed channel is Gaussian random translation on the first factor and the identity on the second. The physical energy, however, is not the usual quadratic Hamiltonian of this auxiliary coordinate:

```math
\langle H\rangle
=\frac12\sum_s\int_{\mathbb R}
\left[e^{2y}|\phi_s(y)|^2+
e^{-2y}\left|\phi_s'(y)-\frac12\phi_s(y)\right|^2\right]dy.
```

This exponentially weighted form is the source of the double logarithm. A fixed-bandwidth family occupies only $`O(\ln E)`$ orthogonal log-position modes at energy $`E`$.

A complementary channel follows from the vacuum-environment unitary

```math
V=\exp[-i\sqrt2\,\sigma\,G\otimes q_{\rm env}].
```

Conditioned on the spectral value $`g`$ of $`G`$, the environment becomes the coherent state $`|-i\sigma g\rangle`$. The complementary state depends only on the spectral probability law of $`G`$; the sign factor is not disclosed. The environment's finite resolution of $`G`$ is what prevents high-frequency encodings from evading the converse.

## Energy supplied by the fluctuating drive

Since $`U_r^\dagger Q U_r=e^rQ`$ and $`U_r^\dagger P U_r=e^{-r}P`$, centered Gaussian averaging gives

```math
\mathcal N_\sigma^\dagger(H)=e^{2\sigma^2}H.
```

For an input of mean photons $`E_{\rm in}`$,

```math
E_{\rm out}+\frac12
=e^{2\sigma^2}\left(E_{\rm in}+\frac12\right).
```

The stochastic drive supplies an average oscillator-energy increase of $`(e^{2\sigma^2}-1)(E_{\rm in}+\tfrac12)`$. At fixed noise variance this is linear in the input budget, so counting this increase together with input energy changes the high-energy capacity law only by an additive constant. It is not a complete work-cost accounting of state preparation, control, or recovery.

Photon loss, axis uncertainty, additional phase or displacement noise, efficient physical encoders, finite-block errors, and receiver work restrictions require separate models. The present result concerns the exact channel above.
