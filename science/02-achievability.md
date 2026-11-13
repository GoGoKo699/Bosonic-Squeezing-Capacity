# Achievability with finite input energy

[Scientific overview](README.md) · [Model](01-model.md) · [Converse](03-converse.md)

The logarithmic coordinate turns a finite physical energy budget into an interval whose length grows as the logarithm of that budget. We place an increasing number of orthogonal modes in this interval while keeping their squeezing-generator second moment bounded. The receiver retains the modes' growing entropy, whereas the environment entropy stays bounded.

Throughout, entropy is in bits, $`[Q,P]=i`$, $`n=(Q^2+P^2-1)/2`$, and

```math
G=\frac{QP+PQ}{2},\qquad
\mathcal N_\sigma(\rho)
=\int_{\mathbb R}\frac{e^{-r^2/(2\sigma^2)}}{\sqrt{2\pi\sigma^2}}
  e^{-irG}\rho e^{irG}\,dr,\qquad \sigma>0.
```

The input constraint is the ordinary mean photon number. The squeezing axis and noise law are known, the noise realization is unobserved, and different channel uses have independent realizations.

## A finite-energy lower bound

Fix a dimensionless number $`K>0`$ and define

```math
C_K=\frac{1+(K+\tfrac12)^2}{2},\qquad
L=\ln\!\left(\frac{E+\tfrac12}{C_K}\right),\qquad
d=\left\lfloor\frac{KL}{\pi}\right\rfloor.
```

Suppose $`d\ge1`$. There is a $`2d`$-dimensional input subspace on which **every** normalized state has mean photon number at most $`E`$. Its maximally mixed state, denoted $`\rho_{L,K}`$, satisfies

```math
I_{\mathrm c}(\rho_{L,K},\mathcal N_\sigma)
\ge \log_2(2d)-g_2(\sigma^2K^2),
\qquad
g_2(u)=(u+1)\log_2(u+1)-u\log_2u.
```

The continuous convention is $`g_2(0)=0`$. Consequently the unassisted energy-constrained quantum capacity obeys

```math
Q_\sigma(E)\ge
\left[\log_2\!\left(2\left\lfloor\frac{K}{\pi}
\ln\frac{E+\tfrac12}{C_K}\right\rfloor\right)
-g_2(\sigma^2K^2)\right]_+,
```

whenever the integer inside the logarithm is positive. Here $`[a]_+=\max\{a,0\}`$. This is an explicit achievable bound, not an assertion that this input optimizes the exact finite-energy capacity.

### 1. The logarithmic box and its modes

The unitary coordinate change is

```math
(W\psi)_s(y)=e^{y/2}\psi(se^y),\qquad
y\in\mathbb R,\quad s\in\{+,-\}.
```

Thus $`L^2(\mathbb R_x)\simeq L^2(\mathbb R_y)\otimes\mathbb C^2`$. The second factor records the coherent half-line label. It is the inherited quadrature-sign/parity subsystem discussed in [the protected-qubit account](04-protected-qubit.md).

On the first factor, $`WGW^\dagger=-i\partial_y`$. Set

```math
g_j(y)=\begin{cases}
\sqrt{\dfrac{2}{L}}\sin\!\left(\dfrac{j\pi(y+L/2)}{L}\right),
&-L/2<y<L/2,\\[1mm]
0,&\text{otherwise},
\end{cases}\qquad j=1,\ldots,d.
```

These are orthonormal. They are Dirichlet-Laplacian modes on a finite interval, extended by zero; they are **not** claimed to be eigenvectors of the full-line momentum $`-i\partial_y`$. Since they vanish at both endpoints, the extensions belong to $`H^1(\mathbb R)`$. For every $`g`$ in their span,

```math
\|g'\|_2^2
=\sum_{j=1}^d |c_j|^2\left(\frac{j\pi}{L}\right)^2
\le K^2\|g\|_2^2.
```

The physical code subspace is

```math
\mathcal C_{L,K}
=W^\dagger\!\left(\operatorname{span}\{g_1,\ldots,g_d\}\otimes\mathbb C^2\right).
```

In particular, its generator second moment, interpreted as a quadratic form, satisfies $`\operatorname{Tr}(\rho G^2)\le K^2`$ for every normalized state supported on $`\mathcal C_{L,K}`$.

### 2. The physical energy bound holds on the whole subspace

For a positive-half-line component, the inverse transformation is $`\psi(x)=x^{-1/2}g(\ln x)`$. Direct change of variables gives

```math
\langle Q^2\rangle_\psi
=\int e^{2y}|g(y)|^2\,dy,\qquad
\langle P^2\rangle_\psi
=\int e^{-2y}\left|g'(y)-\frac{g(y)}2\right|^2\,dy.
```

The same formulas hold on the negative half-line. All code components have support in $`[-L/2,L/2]`$ in $`y`$, so

```math
\langle Q^2\rangle_\psi\le e^L\|g\|_2^2,\qquad
\langle P^2\rangle_\psi
\le e^L\left(\|g'\|_2+\frac{\|g\|_2}{2}\right)^2
\le e^L(K+\tfrac12)^2\|g\|_2^2.
```

For a state with both half-line components, add the corresponding quadratic forms. This also covers complex superpositions and coherences between the two signs: their supports are disjoint in the physical position coordinate. Therefore

```math
\sup_{\substack{\psi\in\mathcal C_{L,K}\\\|\psi\|=1}}
\left\langle n+\frac12\right\rangle_\psi
\le C_K e^L=E+\frac12.
```

This calculation uses the oscillator's quadratic-form domain: $`\psi\in H^1(\mathbb R)`$ and $`x\psi\in L^2(\mathbb R)`$. A jump in the derivative at an interval endpoint is allowed; the wavefunction itself is continuous there because the sine modes vanish. No position eigenstate, sharp momentum eigenstate, or uncharged input-energy tail is used.

### 3. The environment entropy is bounded independently of the box length

Choose the Stinespring environment $`L^2(\mathbb R_r)`$ with initial wavefunction

```math
e_0(r)=(2\pi\sigma^2)^{-1/4}e^{-r^2/(4\sigma^2)}.
```

In the spectral representation of $`G`$, tracing out the receiver gives the ensemble

```math
\mathcal N_\sigma^{\mathrm c}(\rho)
=\int_{\mathbb R} p_\rho(k)\,|e_k\rangle\langle e_k|\,dk,\qquad
e_k(r)=e_0(r)e^{-ikr}.
```

Here $`p_\rho`$ is the spectral density of $`G`$, with the sign factor traced out. This formula is understood through the spectral theorem; the formal eigenvectors $`|k\rangle`$ are not normalized input states.

Rescale the environment's canonical coordinates by $`R'=R/(\sqrt2\sigma)`$ and $`P'=\sqrt2\sigma P_R`$. Then $`e_0`$ is the ordinary oscillator vacuum and $`e_k`$ is a coherent state with amplitude $`-i\sigma k`$. Hence its mean excitation is $`\sigma^2k^2`$, and

```math
\operatorname{Tr}\!\left[n_{\rm env}\,\mathcal N_\sigma^{\mathrm c}(\rho_{L,K})\right]
=\sigma^2\operatorname{Tr}(\rho_{L,K}G^2)\le\sigma^2K^2.
```

The thermal maximum-entropy bound therefore gives

```math
S\!\left(\mathcal N_\sigma^{\mathrm c}(\rho_{L,K})\right)
\le g_2(\sigma^2K^2).
```

This fixed rescaling only changes the representation of the complementary channel and does not change its entropy. It supplies no physical side information to the receiver.

### 4. Receiver entropy and coherent information

The maximally mixed input on $`\mathcal C_{L,K}`$ has entropy $`\log_2(2d)`$. The channel is an average of unitary conjugations. Entropy concavity, with unitary invariance, yields

```math
S(\mathcal N_\sigma(\rho_{L,K}))
\ge \int p_\sigma(r)\,S(e^{-irG}\rho_{L,K}e^{irG})\,dr
=\log_2(2d).
```

Subtracting the preceding environmental upper bound proves the stated coherent-information lower bound. All these entropies are finite. The output-energy calculation below supplies a uniform receiver bound, and the environmental calculation supplies a finite bound for this input.

This entropy argument avoids treating the channel merely as an approximate identity on a growing subspace. Such an approximation followed by a dimension-dependent continuity bound would unnecessarily weaken the leading rate.

## Why the coding theorem applies

The mean-energy-constrained coding result used here is Wilde and Qi, *Energy-constrained private and quantum capacities of quantum channels*, IEEE Transactions on Information Theory **64**, 7802–7827 (2018), [DOI](https://doi.org/10.1109/TIT.2018.2854766), [arXiv:1609.01997v2](https://arxiv.org/abs/1609.01997). Their Definition 3 requires a finite partition function at every positive inverse temperature; Condition 1 requires a uniformly finite output entropy on an input-energy ball. Theorem 2 establishes coherent-information achievability, and Theorem 1 relates the communication and entanglement-transmission tasks. Their Theorem 3 also gives the single-letter expression when degradability has been established.

Both relevant conditions hold here. First,

```math
\operatorname{Tr}e^{-\beta n}=\frac{1}{1-e^{-\beta}}<\infty,\qquad \beta>0.
```

Second, the centered Gaussian squeezing law satisfies $`\mathbb E e^{2r}=\mathbb E e^{-2r}=e^{2\sigma^2}`$. Thus for every finite-energy input,

```math
\operatorname{Tr}\!\left[\left(n+\frac12\right)\mathcal N_\sigma(\rho)\right]
=e^{2\sigma^2}\operatorname{Tr}\!\left[\left(n+\frac12\right)\rho\right].
```

This identity follows first on finite-energy cores from the quadrature transformation and then for all finite quadratic-form energy inputs. Consequently

```math
\sup_{\operatorname{Tr}(\rho n)\le E}S(\mathcal N_\sigma(\rho))
\le g_2\!\left(e^{2\sigma^2}(E+\tfrac12)-\tfrac12\right)<\infty.
```

The noise may supply oscillator energy, but it does not violate the theorem's finite-output-entropy condition. The capacity constraint concerns input photons; it does not charge the pump work that realizes the random squeezing.

Applying the constrained coding theorem, every rate strictly below the positive coherent information above is attainable with fidelity tending to one over many independent channel uses. The theorem also covers inputs that meet the energy bound with equality. Alternatively, one may introduce arbitrarily small energy slack by mixing with the vacuum and pass to the limit within the finite-input/finite-output-entropy setting. No finite-block guarantee or efficient coding circuit follows from this asymptotic theorem.

## Large-energy consequence

Keep $`K>0`$ and $`\sigma>0`$ fixed while $`E\to\infty`$. Then

```math
L=\ln E+O_K(1),\qquad
d=\frac{K}{\pi}\ln E+O_K(1),\qquad
Q_\sigma(E)\ge\log_2\ln E+O_{\sigma,K}(1).
```

Only an additive constant is lost to the environment. The matching converse is required to conclude the full capacity law.

The preparation and recovery operations are unrestricted ideal quantum operations in this capacity model. The logarithmic coordinate map and the box-mode encoding are non-Gaussian. This construction does not establish a laboratory implementation, efficient synthesis, robustness to an uncertain squeezing axis, or protection against additional loss or rotation noise.

The finite checks in [log_box.py](../verification/log_box.py) independently evaluate the physical-coordinate Jacobian, orthonormality, generator quadratic form, and energy matrices for four specified boxes. They also integrate the one-photon protected-qubit profile. These numerical checks support the displayed finite examples; the arguments above establish the all-energy bound.
