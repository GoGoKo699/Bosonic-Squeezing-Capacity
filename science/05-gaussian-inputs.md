# Gaussian inputs and the unbounded rate

[Scientific overview](README.md) · [Related work](06-related-work.md)

The double-logarithmic rate requires physical input states beyond the Gaussian family. This statement concerns the optimization of **coherent information over Gaussian channel-input states**, including correlated multimode Gaussian states. It imposes no restriction on the receiver. It does not assert an impossibility theorem for every circuit containing Gaussian operations: such a circuit can act on non-Gaussian logical data, and a classical mixture of Gaussian states can itself be non-Gaussian.

## A bound independent of input energy

For every fixed noise width $`\sigma>0`$, define

```math
B_\sigma
=1+\frac12\log_2\!\left(1+\frac{\pi^2}{8\sigma^2}\right).
```

Every finite-energy one-mode physical Gaussian state $`\rho_G`$, with arbitrary displacement and covariance, obeys

```math
I_c(\rho_G,\mathcal N_\sigma)\le B_\sigma.
```

More generally, every finite-energy $`n`$-mode Gaussian state, with arbitrary correlations and entanglement between modes, obeys

```math
I_c\!\left(\rho_G^{(n)},\mathcal N_\sigma^{\otimes n}\right)
\le n B_\sigma.
```

The bound is uniform in the photon budget. In contrast, the non-Gaussian finite log-position subspaces used in the lower construction have coherent information $`\log_2\ln E-O_\sigma(1)`$. Thus their advantage over the entire correlated-Gaussian-input coherent-information optimization grows without bound as $`E\to\infty`$. This comparison is a statement about communication rates, rather than preparation time, decoder complexity or finite-energy crossover performance.

## The log-radius variance of a normal variable

The classical estimate behind the result is sharp:

```math
X\sim\mathcal N(m,v),\quad v>0
\quad\Longrightarrow\quad
\operatorname{Var}(\ln|X|)\le\frac{\pi^2}{8}.
```

Equality holds when $`m=0`$. Rescaling $`X`$ adds a constant to $`\ln|X|`$, so its variance depends only on $`m^2/v`$.

To prove the bound, put $`\theta=m^2/(2v)`$ and let $`K`$ have the Poisson distribution of mean $`\theta`$. The standard noncentral-chi-square mixture represents $`X^2/v`$, conditionally on $`K=k`$, as a central chi-square variable with $`1+2k`$ degrees of freedom. A central chi-square variable $`Z`$ with $`\nu`$ degrees of freedom satisfies

```math
\mathbb E\ln Z=\ln2+\psi(\nu/2),
\qquad
\operatorname{Var}(\ln Z)=\psi_1(\nu/2),
```

where $`\psi`$ and $`\psi_1`$ are the digamma and trigamma functions. These log moments and the Poisson-mixture representation are established distribution identities; see [Pav, equations (1), (4) and (6)](https://arxiv.org/html/1503.06266v1). The law of total variance gives

```math
4\operatorname{Var}(\ln|X|)
=F(\theta)
:=\mathbb E_\theta\psi_1(K+\tfrac12)
  +\operatorname{Var}_\theta\psi(K+\tfrac12).
```

Let $`f(k)=\psi(k+\tfrac12)`$ and $`g(k)=(k+\tfrac12)^{-1}`$. Their recurrences give

```math
f(k+1)-f(k)=g(k),
\qquad
\psi_1(k+\tfrac32)-\psi_1(k+\tfrac12)=-g(k)^2.
```

For a Poisson expectation, differentiation with respect to its mean replaces a function by its forward difference. Applying this identity to the two terms in $`F`$ yields

```math
\begin{aligned}
\frac{d}{d\theta}\mathbb E_\theta\psi_1(K+\tfrac12)
  &=-\mathbb E_\theta g(K)^2,\\
\frac{d}{d\theta}\operatorname{Var}_\theta f(K)
  &=\mathbb E_\theta g(K)^2
    +2\operatorname{Cov}_\theta(f(K),g(K)).
\end{aligned}
```

Termwise differentiation is justified locally uniformly in $`\theta`$: $`f`$ grows only logarithmically, and $`g`$ and $`\psi_1(k+\tfrac12)`$ are bounded. The squared-increment terms cancel, leaving

```math
F'(\theta)=2\operatorname{Cov}_\theta(f(K),g(K))\le0.
```

Indeed, $`f`$ increases and $`g`$ decreases. For independent $`K,K'`$ the covariance has twice its value equal to

```math
\mathbb E\!\left[(f(K)-f(K'))(g(K)-g(K'))\right]\le0.
```

At $`\theta=0`$, $`K=0`$ deterministically and $`F(0)=\psi_1(\tfrac12)=\pi^2/2`$. This proves the variance bound, and the covariance is strictly negative for $`\theta>0`$. The trigamma value and recurrences are recorded in [DLMF §5.15](https://dlmf.nist.gov/5.15), particularly equations 5.15.3 and 5.15.5. No priority claim for this classical monotonicity consequence is needed here.

## A finite-covariance translation-channel bound

Write $`s=\sigma^2`$. For the radial translation channel $`\mathcal T_\sigma`$, every state $`\tau`$ with finite covariance satisfies

```math
I_c(\tau,\mathcal T_\sigma)
\le\frac12\log_2\!\left(1+\frac{\operatorname{Var}_\tau(Y)}{s}\right).
```

This auxiliary bound is used only at finite covariance below. It does not require a coding theorem for a degenerate cost observable or an assumption that physical harmonic energy bounds $`P_y^2`$ for arbitrary states.

An explicit pure Gaussian environment has variances $`\operatorname{Var}(q)=s`$ and $`\operatorname{Var}(p)=1/(4s)`$. Coupling by $`\exp(-iP_yq)`$ gives

```math
Y_B=Y+q,\quad P_{y,B}=P_y,
\qquad q_E=q,\quad p_E=p-P_y.
```

The complement is a measure-and-prepare channel depending only on the input distribution of $`P_y`$. That distribution is preserved by the main channel, establishing degradability. This is the established one-quadrature Gaussian channel of canonical class $`B_1`$; see [Holevo, Section 2](https://arxiv.org/html/quant-ph/0607051v2).

At fixed finite covariance, a Gaussian state maximizes coherent information. A direct proof uses relative-entropy data processing under the degrading map. If $`\tau_G`$ has the same first and second moments as $`\tau`$, the logarithms of the matching Gaussian output states are quadratic, so

```math
\begin{aligned}
D(\mathcal T_\sigma\tau\Vert\mathcal T_\sigma\tau_G)
 &=S(\mathcal T_\sigma\tau_G)-S(\mathcal T_\sigma\tau),\\
D(\mathcal T_\sigma^c\tau\Vert\mathcal T_\sigma^c\tau_G)
 &=S(\mathcal T_\sigma^c\tau_G)-S(\mathcal T_\sigma^c\tau).
\end{aligned}
```

The first relative entropy is at least the second, proving the assertion. This Gaussian-channel argument is an inherited tool, consistent with [Wolf, Pérez-García and Giedke](https://arxiv.org/html/quant-ph/0606132v1). It is applied to the radial channel, rather than to the non-Gaussian physical squeeze channel.

For centered input covariance $`\left(\begin{smallmatrix}v&c\\c&w\end{smallmatrix}\right)`$, the output and environment symplectic eigenvalues are

```math
a=\sqrt{(v+s)w-c^2},
\qquad b=\sqrt{sw+\tfrac14}.
```

Setting $`c=0`$ increases the output entropy and leaves the environmental entropy unchanged. With $`G(z)=(z+\tfrac12)\ln(z+\tfrac12)-(z-\tfrac12)\ln(z-\tfrac12)`$, the remaining coherent information in nats is

```math
f_v(w)=G\!\left(\sqrt{(v+s)w}\right)
       -G\!\left(\sqrt{sw+\tfrac14}\right),
\qquad w\ge\frac{1}{4v}.
```

This function increases to $`\tfrac12\ln(1+v/s)`$. For a short verification, let $`h(z)=\ln[(z+\tfrac12)/(z-\tfrac12)]`$. At $`c=0`$,

```math
2w f_v'(w)=a h(a)-\left(b-\frac{1}{4b}\right)h(b)\ge0.
```

The first term is at least one. With $`t=1/(2b)`$, the second is $`(1-t^2)\operatorname{atanh}(t)/t\le1`$. Endpoints follow by continuity. The limit follows from $`G(z)=\ln(ez)+o(1)`$. Displacements preserve coherent information, so $`v`$ is the centered variance, not the uncentered second moment. Dividing by $`\ln2`$ proves the auxiliary bound.

## Applying the bound to physical Gaussian states

Under the logarithmic unitary, write the input as $`\omega_{ZA}`$, with a two-dimensional sign register $`Z`$ and radial factor $`A`$. Let $`\tau_A=\operatorname{Tr}_Z\omega_{ZA}`$. The complement ignores $`Z`$, and therefore

```math
\begin{aligned}
I_c(\omega_{ZA},\operatorname{id}_Z\otimes\mathcal T_\sigma)
 &=S(ZB)-S(E)\\
 &\le1+S(B)-S(E)\\
 &=1+I_c(\tau_A,\mathcal T_\sigma).
\end{aligned}
```

The distribution of $`Y`$ on $`\tau_A`$ is exactly that of $`\ln|Q|`$ on the physical input. A physical Gaussian state's $`Q`$ marginal is normal, so its variance is at most $`\pi^2/8`$ by the preceding lemma. This proves the one-mode bound.

The moment and entropy domains are controlled here. Every finite-covariance Gaussian state has finite fourth-order physical quadrature moments. The radial momentum is the physical dilation generator $`P_y=(QP+PQ)/2`$, so its second moment is finite for these inputs. The normal log-radius distribution has a finite second moment as well. Thus the radial finite-covariance argument applies. Finite harmonic input energy also gives finite input entropy; the centered Gaussian squeeze mixture multiplies mean harmonic energy by the finite factor $`e^{2\sigma^2}`$, giving finite output entropy. Purification and subadditivity then bound the complementary entropy. None of the displayed entropy differences is an undefined infinity-minus-infinity expression.

Finally, degradability makes coherent information subadditive over channel uses. To see this directly, the difference between the sum of marginal coherent informations and the joint coherent information is the output total correlation minus the environmental total correlation. The latter cannot exceed the former under the tensor product of degrading maps. Hence

```math
I_c\!\left(\rho^{(n)},\mathcal N_\sigma^{\otimes n}\right)
\le\sum_{j=1}^n I_c(\rho_j,\mathcal N_\sigma).
```

Every marginal of a multimode Gaussian state is Gaussian. Applying the one-mode bound to each marginal proves the stated result for arbitrary correlated Gaussian block inputs.

The constant $`B_\sigma`$ is not optimized and diverges as $`\sigma\to0`$, consistently with the identity-channel limit. The conclusion is the fixed-positive-noise separation between bounded Gaussian-input coherent information and the unbounded rate obtained from explicitly non-Gaussian inputs.
